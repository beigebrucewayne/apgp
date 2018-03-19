# Asychronous Postgres to Pandas (APGP) - WIP
Asynchronously read data from Postgres, returned as a Pandas dataframe.

![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg?style=flat-square)

![logo](https://i.imgur.com/JTKlXCC.png)

As of right now, the library is ludicrously small, but works as inteded (with support for Redshift as well). As I research more into writing async libraries further additions will be made. However, this library can be used to *in theory* read data 3x times faster than [psycopg2](http://initd.org/psycopg/docs/index.html). Obviously, this lib is meant for Data nerds, so if you do need to write back one option is to use Pandas [to_sql()](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql) method. 

## Example

```python
from apgp import Query

q = Query("""SELECT * FROM github.repository""")

q.execute()

#         id        name                        full_name description   fork  \
#  122866357  test_repo2  secretagentjamesbond/test_repo2        None  False
#  122866319   test_repo   secretagentjamesbond/test_repo        None  False

# homepage language default_branch          created_at  owner_id  private 
#     None     None         master 2018-02-25 19:02:37  36823666    False
#     None     None         master 2018-02-25 19:02:15  36823666    False

q.close()
```

## Performance
Graphic pulled from [Asyncpg](https://github.com/MagicStack/asyncpg) github page.

![performance](https://github.com/MagicStack/asyncpg/raw/master/performance.png)

## Install

Not worth sending to PyPi as of yet, but you can pip install directly from github. Make sure that you have a `config.yaml`, as shown below.

```bash
pip install git+https://github.com/beigebrucewayne/apgp.git
```

## Setup

In order to bypass manually connecting you will need a `config.yaml` in your project root.
You can see an an example in the `config.yaml.example` file.

```yaml
database: 'dbname'
host: 'host'
port: 5439
user: 'username'
password: 'password'
```
