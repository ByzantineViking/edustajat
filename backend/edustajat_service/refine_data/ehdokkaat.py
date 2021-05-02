from pathlib import Path
import pandas as pd
from edustajat_service.helpers.print import bcolors, section_print

def run():
    data_folder = Path("edustajat_service/manual_data/kuntavaalit2017/master")
    ehdokkaat = data_folder / "ehd_maa.csv"
    header_file = data_folder / "Ehdokkaat_otsikkorivit_FI.xlsx"
    data = pd.read_csv(ehdokkaat, sep=";", header=None, encoding='ISO-8859-1')
    headers = pd.ExcelFile(header_file)
    #df1 = pd.read_excel(xls, 'FI ehdokasasettajatiedosto')
    header_ehdokkaat = pd.read_excel(headers, 'FI ehdokastiedosto')

    # drop last (empty) column
    # data = data.iloc[:, :-1]
    data.columns = header_ehdokkaat.iloc[:, 32]


    # restructed_folder = Path("manual_data/kuntavaalit2017/restructured")
    # ehdokkaat_path = restructed_folder / "ehdokkaat.csv"
    # ehdokkaat.to_csv(ehdokkaat_path)
    # section_print(bcolors.OKCYAN, 'Saved data to', ehdokkaat_path)


run()
