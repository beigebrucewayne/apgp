# Red Pandas

Easily transfer data from Redshift to Pandas.

![logo](https://i.imgur.com/PeL46uS.png)

## Features

- Query Redshift and receive response as pd.DataFrame()
- Save data to S3, locally, or back to Redshift
- Upload and download files from S3

## Setup

In order to connect in one step you will need a `config.yaml` file in your project root. The format mirror the following:

```yaml
dbname: 'dbname'
host: 'host'
port: 5439
user: 'username'
password: 'password'
aws_access_key_id: 'aws_access_key_id'
aws_secret_access_key: 'aws_secret_access_key'
aws_region: 'aws_region'
```

## Redshift Operations

```python
from red_pandas import connect

# Just connect to Redshift
redshift, _ = connect()

# Query Redshift and receive pd.DataFrame() as response
redshift.to_pandas('SELECT * FROM github.repository')

          id        name                        full_name description   fork  \
0  122866319   test_repo   secretagentjamesbond/test_repo        None  False
1  122866357  test_repo2  secretagentjamesbond/test_repo2        None  False

  homepage language default_branch          created_at  owner_id  private  \
0     None     None         master 2018-02-25 19:02:15  36823666    False
1     None     None         master 2018-02-25 19:02:37  36823666    False
```

## S3 Operations

```python
from red_pandas import connect

_, s3 = connect()

# List all S3 buckets
s3.buckets
['kade-test-bucket', 'kktestbucketz', 'kktestbucketz-out']

# See files in bucket
s3.bucket_files('kade-test-bucket')

# Download file
s3.download('kade-test-bucket', 'test.jpg')
```
