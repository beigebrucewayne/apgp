from collections import namedtuple
import yaml
import os


# Easily store credentials after reading in
# from `config.yaml`
Creds = namedtuple('Creds', [
    'dbname',
    'host',
    'port',
    'user',
    'password',
    'aws_access_key_id',
    'aws_secret_access_key',
    'aws_region'
])


def read_config():
    # Find `config.yaml` in project root
    # Parse the yaml into the `config` variable
    # Pass config details into namedtuple
    current_dir = os.path.abspath(os.curdir)
    file_path = os.path.join(current_dir, 'config.yaml')

    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            config = yaml.load(file)
            return Creds(**config)
    except IOError:
        print("""
        Unable to find `config.yaml` in current directory.

        Default format is:
        dbname: 'dbname'
        host: 'host'
        port: 5439
        user: 'user'
        password: 'password'
        """)
        raise
