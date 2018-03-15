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

    return redshift_connection, s3_connection
