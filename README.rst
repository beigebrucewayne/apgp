.. code:: text

                      ___.-~"~-._   __....__
                    .'    `    \ ~"~        ``-.
                   /` _      )  `\              `\                          ------------
                  /`  a)    /     |               `\
                 :`        /      |                 \       ---------
            <`-._|`  .-.  (      /   .            `;\\
             `-. `--'_.'-.;\___/'   .      .       | \\           ---
          _     /:--`     |        /     /        .'  \\
         ("\   /`/        |       '     '         /    :`;
         `\'\_/`/         .\     /`~`=-.:        /     ``             ------------
           `._.'          /`\    |      `\      /(
                         /  /\   |        `Y   /  \     -----------
                        J  /  Y  |         |  /`\  \                                ------
                       /  |   |  |         |  |  |  |
                      "---"  /___|        /___|  /__|                     
                             '"""         '"""  '"""

Asynchronous Postgres to Pandas (APGP)
======================================

Asynchronously read data from Postgres, returned as a Pandas dataframe.

.. figure:: https://img.shields.io/packagist/l/doctrine/orm.svg?style=flat-square
   :alt: Packagist

   Packagist

Features
--------

-  Read data from Postgres (Redshift) into a Pandas DataFrame

Usage
-----

.. code:: python

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

Performance
-----------

Graphic pulled from `Asyncpg <https://github.com/MagicStack/asyncpg>`__
github page.

.. figure:: https://github.com/MagicStack/asyncpg/raw/master/performance.png
   :alt: performance

   performance

Setup
-----

In order to bypass manually connecting you will need a ``config.yaml``
in your project root. You can see an an example in the
``config.yaml.example`` file.

.. code:: yaml

    database: 'dbname'
    host: 'host'
    port: 5439
    user: 'username'
    password: 'password'

Installation
------------

.. code:: bash

    $ pip install apgp
