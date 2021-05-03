from edustajat_service.helpers.print import bcolors, section_print
from edustajat_service.db.connect import connect
from pathlib import Path
import pandas as pd
from edustajat_service.sql.create_table import create_table_if_not_exists


def run(conn):
    data_folder = Path("edustajat_service/manual_data/kuntavaalit2017/master")
    ehdokkaat = data_folder / "ehd_maa.csv"
    header_file = data_folder / "Ehdokkaat_otsikkorivit_FI.xlsx"
    data = pd.read_csv(ehdokkaat, sep=";", header=None, encoding='ISO-8859-1')
    headers = pd.ExcelFile(header_file)
    #df1 = pd.read_excel(xls, 'FI ehdokasasettajatiedosto')
    header_ehdokkaat = pd.read_excel(headers, 'FI ehdokastiedosto')

    # drop last (empty) column
    # data = data.iloc[:, :-1]
    def sanitize(col):
        return col.replace("/", " tai").replace("-", "")

    columns = [sanitize(col) for col in header_ehdokkaat.columns[:33]]

    data.columns = columns




    create_table_if_not_exists(conn, data, "ehdokkaat")
