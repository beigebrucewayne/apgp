import os


def check_columns(dataframe):

    file_path = os.path.join(os.path.abspath(os.curdir),
                             'redshift_reserve_words.txt')
    reserved_words_file = open(file_path, 'r').readlines()
    reserved_words = [r.strip().lower() for r in reserved_words_file]

    if dataframe.columns.isin(reserved_words).any():
        raise RedshiftColumnNameError('Dataframe column name is a Redshift ',
                                      'reserved word. Pleae rename and try ',
                                      'again.')
