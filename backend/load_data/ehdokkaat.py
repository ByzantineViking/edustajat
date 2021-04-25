from pathlib import Path
import pandas as pd
from helpers.print import bcolors, section_print

data_folder = Path("../manual_data/kuntavaalit2017/master")
ehdokkaat = data_folder / "ehd_maa.csv"


data = pd.read_csv(ehdokkaat, sep=";", header=None, encoding='ISO-8859-1')
section_print(bcolors.OKCYAN, 'Loaded data', ehdokkaat)

# drop last (empty) column
# data = data.iloc[:, :-1]



# restructed_folder = Path("manual_data/kuntavaalit2017/restructured")
# ehdokkaat_path = restructed_folder / "ehdokkaat.csv"
# ehdokkaat.to_csv(ehdokkaat_path)
# section_print(bcolors.OKCYAN, 'Saved data to', ehdokkaat_path)


