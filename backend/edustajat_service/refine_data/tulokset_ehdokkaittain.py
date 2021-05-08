from pathlib import Path
import pandas as pd

from edustajat_service.helpers.print import bcolors, section_print
from edustajat_service.sql.SQL_QUERIES.kv2017.pandas_columns_kv2017_tulokset_ehdokkaittain import columns, selected_columns
from pandasgui import show
from edustajat_service.sql.SQL_QUERIES.kv2017.pandas_columns_kv2017_tulokset_ehdokkaittain import selected_columns
from edustajat_service.sql.helpers.execute_sql_file import execute_sql_file
from edustajat_service.sql.table_operations import bulk_insert_stringio


def run(conn):

    # Load data
    data_folder = Path("edustajat_service/manual_data/kuntavaalit2017/master")
    ehdokkaittain = data_folder / "kv-2017_teat_maa.csv"
    data = pd.read_csv(ehdokkaittain, sep=";",
                       header=None, encoding='ISO-8859-1')
    section_print(bcolors.OKCYAN, 'Loaded data', ehdokkaittain)

    # drop last (empty) column
    data = data.iloc[:, :-1]

    # contains no duplicates
    # data.drop_duplicates().shape
    #

    data.columns = columns
    # show(data)
    # Convert data to categorical

    data['valintatieto'] = data['valintatieto'].astype('category').cat.rename_categories({
        0: 'puuttuu',
        1: 'valittu',
        2: 'varalla',
        3: 'ei_valittu'
    })

    valitut_raw = data.loc[data.valintatieto == 'valittu']

    valitut = valitut_raw[selected_columns]
    # Change indicator variables to booleans
    indicator_columns = [
        'europarlamentaarikko',
        'kansanedustaja',
        'kunnanvaltuutettu'
    ]
    di = {
        "1": True
    }

    valitut[indicator_columns] = valitut[indicator_columns].apply(
        lambda col: col.map(di).fillna(value=False))

    # show(valitut)

    print("Creating table kv2017_tulokset_ehdokkaittain")
    execute_sql_file(
        "edustajat_service/sql/SQL_QUERIES/kv2017/create_kv2017_tulokset_ehdokkaittain.sql")

    bulk_insert_stringio(conn, valitut, "kv2017_tulokset_ehdokkaittain")
