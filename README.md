# PG Pandas - WIP
![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?style=flat-square)

Easily transfer data from Postgres (using asyncpg) to Pandas with additional support for Redshfit.

![logo](https://i.imgur.com/PeL46uS.png)

## TODO

- [ ] Replace psycopg2 with [asyncpg](https://github.com/MagicStack/asyncpg)
- [ ] Separate out S3 methods
- [ ] Finish type annotations
- [ ] Additional convenience methods for S3
- [ ] Take out AWS Creds, instead set with aws-cli
- [x] Add proper column names from PG

## Features

- Query Postgres and receive response as pd.DataFrame()
- Write data to S3, locally, or back to Postgres/Redshift
- Upload and download files from S3

## Setup

In order to connect in one step you will need a `config.yaml` file in your project root. The format mirror the following:

```yaml
dbname: 'dbname'
host: 'host'
port: 5439
user: 'username'
password: 'password'
```
