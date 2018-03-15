from io import StringIO
import boto3
import os


class S3:

    global s3, s3_resource
    s3 = boto3.client('s3')
    s3_resource = boto3.resource('s3')

    def __init__(self, aws_access_key_id, aws_secret_access_key, region):
        self.access_key_id = aws_access_key_id
        self.secret_access_key = aws_secret_access_key
        self.region = region
        self.__login = _login(self.access_key_id, self.secret_access_key,
                            self.region)

        self._buckets = s3.list_buckets()
        self.buckets = [bucket['Name'] for bucket in self._buckets['Buckets']]

    @staticmethod
    def bucket_files(bucket):
        content = s3.list_objects(Bucket=bucket)['Contents']
        return [key['Key'] for key in content]

    @staticmethod
    def download(bucket: str, file: str, folder: str = None):
        try:
            s3.download_file(bucket, key, folder)
        except Exception as e:
            print(e)
            print(f"Error downloading {file} from {bucket}")
            raise e

    @staticmethod
    def upload(file: str, bucket: str, folder: str = None):
        if folder is None:
            try:
                s3.upload_file(file, bucket, file)
            except Exception as e:
                print(e)
                print(f"Error uploading {file} to {bucket}")
                raise e
        else:
            try:
                s3.upload_file(file, bucket, folder)
            except Exception as e:
                print(e)
                print(f"Error uploading {file} to {bucket}")
                raise e

    @staticmethod
    def to_s3(bucket: str, dataframe: object, filename: str):
        csv_buffer = StringIO()
        dataframe.to_csv(csv_buffer)
        name_of_file = filename
        s3_resource.Object(bucket, name_of_file).put(Body=csv_buffer.getvalue())


def _login(key_id, secret_key, region):
    os.environ['AWS_ACCESS_KEY_ID'] = key_id
    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_key
    os.environ['REGION'] = region
