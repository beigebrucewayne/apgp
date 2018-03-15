import traceback
import sys

from red_pandas.config import read_config
from red_pandas.redshift import Redshift
from red_pandas.s3 import S3


def connect():
    # Connect to Redshift and S3 in one swoop
    # Credentials are being read in from `config.yaml`.
    config = read_config()

    redshift_connection = Redshift(config.dbname, config.host, config.port,
                                   config.user, password=config.password)

    s3_connection = S3(config.aws_access_key_id, config.aws_secret_access_key,
                       config.aws_region)

    return redshift_conn, s3_conn


# TODO: Figure out if anything was lost
# If not, delete out

#  def connect_to_s3(aws_access_key_id, aws_secret_access_key, bucket, subdirectory = None, **kwargs):
    #  global s3, s3_bucket_var, s3_subdirectory_var, aws_1, aws_2, aws_token
    #  s3 = boto3.resource('s3',
                        #  aws_access_key_id = aws_access_key_id,
                        #  aws_secret_access_key = aws_secret_access_key,
                        #  **kwargs)
    #  s3_bucket_var = bucket
    #  if subdirectory is None:
        #  s3_subdirectory_var = ''
    #  else:
        #  s3_subdirectory_var = subdirectory + '/'
    #  aws_1 = aws_access_key_id
    #  aws_2 = aws_secret_access_key
    #  if kwargs.get('aws_session_token'):
        #  aws_token = kwargs.get('aws_session_token')
    #  else:
        #  aws_token = ''



# TODO: Move this out to under `redshift` folder
def pandas_to_redshift(data_frame,
                       redshift_table_name,
                       column_data_types = None,
                       index = False,
                       save_local = False,
                       delimiter = ',',
                       quotechar = '"',
                       dateformat = 'auto',
                       timeformat = 'auto',
                       region = '',
                       append = False):

    rrwords = open(os.path.join(os.path.dirname(__file__), \
    'redshift_reserve_words.txt'), 'r').readlines()
    rrwords = [r.strip().lower() for r in rrwords]
    data_frame.columns = [x.lower() for x in data_frame.columns]
    not_valid = [r for r in data_frame.columns if r in rrwords]
    if not_valid:
        raise ValueError('DataFrame column name {0} is a reserve word in redshift'.format(not_valid[0]))
    else:
        csv_name = redshift_table_name + '.csv'
        if save_local == True:
            data_frame.to_csv(csv_name, index = index, sep = delimiter)
            print('saved file {0} in {1}'.format(csv_name, os.getcwd()))
        # SEND DATA TO S3
        csv_buffer = StringIO()
        data_frame.to_csv(csv_buffer, index = index, sep = delimiter)
        s3.Bucket(s3_bucket_var).put_object(Key= s3_subdirectory_var + csv_name, Body = csv_buffer.getvalue())
        print('saved file {0} in bucket {1}'.format(csv_name, s3_subdirectory_var + csv_name))
        # CREATE AN EMPTY TABLE IN REDSHIFT
        if index == True:
            columns = list(data_frame.columns)
            if data_frame.index.name:
                columns.insert(0, data_frame.index.name)
            else:
                columns.insert(0, "index")
        else:
            columns = list(data_frame.columns)
        if column_data_types is None:
            column_data_types = ['varchar(256)'] * len(columns)
        columns_and_data_type = ', '.join(['{0} {1}'.format(x, y) for x,y in zip(columns, column_data_types)])
        if append is False:
            create_table_query = 'create table {0} ({1})'.format(redshift_table_name, columns_and_data_type)
            print(create_table_query)
            print('CREATING A TABLE IN REDSHIFT')
            cursor.execute('drop table if exists {0}'.format(redshift_table_name))
            cursor.execute(create_table_query)
            connect.commit()
        # CREATE THE COPY STATEMENT TO SEND FROM S3 TO THE TABLE IN REDSHIFT
        bucket_name = 's3://{0}/{1}'.format(s3_bucket_var, s3_subdirectory_var + csv_name)
        s3_to_sql = """
        copy {0}
        from '{1}'
        delimiter '{2}'
        ignoreheader 1
        csv quote as '{3}'
        dateformat '{4}'
        timeformat '{5}'
        access_key_id '{6}'
        secret_access_key '{7}'
        """.format(redshift_table_name, bucket_name, delimiter, quotechar, dateformat, timeformat,
                   config.aws_access_key_id, config.aws_secret_access_key)
        if region:
            s3_to_sql = s3_to_sql +  "region '{0}'".format(config.region)
        if aws_token != '':
            s3_to_sql = s3_to_sql +  "\n\tsession_token '{0}'".format(aws_token)
        s3_to_sql = s3_to_sql + ';'
        print(s3_to_sql)
        # send the file
        print('FILLING THE TABLE IN REDSHIFT')
        try:
            cursor.execute(s3_to_sql)
            connect.commit()
        except Exception as e:
            print(e)
            traceback.print_exc(file=sys.stdout)
            connect.rollback()
            raise


# TODO: Re-write to work with all variables defined across package
# Probably just leave here
def close_up_shop():
    global connect, cursor, s3, s3_bucket_var, s3_subdirectory_var, aws_1, aws_2, aws_token
    cursor.close()
    connect.commit()
    connect.close()
    try:
        del connect, cursor
    except:
        pass
    try:
        del s3, s3_bucket_var, s3_subdirectory_var, aws_1, aws_2, aws_token
    except:
        pass

#-------------------------------------------------------------------------------
