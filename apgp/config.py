import os
import yaml


def _read_config() -> str:

    current_dir = os.path.abspath(os.curdir)
    file_path = os.path.join(current_dir, 'config.yaml')

    try:
        with open(file_path, mode='r', encoding='UTF-8') as file:
            config = yaml.load(file)
            dsn = f'postgresql://{config["user"]}:{config["password"]}@{config["host"]}:{config["port"]}/{config["database"]}'
            return dsn
    except IOError as e:
        print("""
        Error: could not find configuration file `config.yaml` in current directory.

        Default format is:
        ==================

        database: '<datbase name>'
        host: '<host address>'
        port: '<database port>'
        user: '<username>'
        password: '<database password>'
        """)
        raise
