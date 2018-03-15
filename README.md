## Pandas Redshift

Connect to Redshift and S3 in one step.

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

## Example
```python
from pandas_redshift import connect

redshift, s3 = connect()

# List all S3 buckets
s3.buckets
['kade-test-bucket', 'kktestbucketz', 'kktestbucketz-out']

# Query Redshift and return Pandas dataframe
redshift.to_pandas('SELECT ftp.conversion_type FROM ftp LIMIT 3')

							   conversion_type
0  Consumer Credit,SEG 0,CRV 0 (Offline) (873)
1  Consumer Credit,SEG 0,CRV 0 (Offline) (873)
2  Consumer Credit,SEG 0,CRV 0 (Offline) (873)
```
