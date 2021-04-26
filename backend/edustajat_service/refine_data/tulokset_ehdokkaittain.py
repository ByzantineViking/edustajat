from pathlib import Path
import pandas as pd

from helpers.print import bcolors, section_print

data_folder = Path("manual_data/kuntavaalit2017/master")
ehdokkaittain = data_folder / "ehdokkaittain.csv"


data = pd.read_csv(ehdokkaittain, sep=";", header=None, encoding='ISO-8859-1')
section_print(bcolors.OKCYAN, 'Loaded data', ehdokkaittain)

# drop last (empty) column
data = data.iloc[:, :-1]

# contains no duplicates
# data.drop_duplicates().shape
#


columns = [
    # tunnistetiedot
    'vaalilaji',
    'vaalipiirinumero',
    'kuntanumero',
    'tietuetyyppi',
    'äänestysalue_tunnus',
    'äänestysalue_lyhenne_suomi',
    'äänestysalue_lyhenne_ruotsi',
    'puoluetunniste',
    'vakiopuoluenumero',
    'listajärjestysnumero',
    'vaalilittonumero',
    'puoluelyhenne_suomi',
    'puoluelyhenne_ruotsi',
    'puoluelyhenne_englanti',
    'ehdokasnumero',
    # taustatiedot
    'äänestysalue_suomi',
    'äänestysalue_ruotsi',
    'etunimi',
    'sukunimi',
    'sukupuoli',
    'ikä',
    'ammatti',
    'kotikunta_koodi',
    'kotikunta_nimi_suomi',
    'kotikunta_nimi_ruotsi',
    'äidinkieli',
    'europarlamentaarikko',
    'kansanedustaja',
    'kunnanvaltuutettu',
    'ei_käytössä_maakuntavaltuutettu',
    # vertailutiedot
    'vaali_nimilyhenne_1_vertailuvaali',
    'ääniä_1_vertailuvaali',
    # laskentatulokset
    'ennakkoäänet',
    'vaalipäivän_äänet',
    'äänet_yhteensä',
    'osuus_ennakkoäänistä',
    'osuus_vaalipäivän_äänistä',
    'osuus_äänistä_yhteensä',
    'valintatieto',
    'vertausluku',
    'sija_vertausluku',
    'sija_lopullinen',
    'laskennan_tila',
    'laskentavaihe',
    'viimeisin_päivitys'
]


data.columns = columns


# Convert data to categorical

data['valintatieto'] = data['valintatieto'].astype('category').cat.rename_categories({
    0: 'puuttuu',
    1: 'valittu',
    2: 'varalla',
    3: 'ei_valittu'
})


valitut_raw = data.loc[data.valintatieto == 'valittu']


valitut = valitut_raw[[
    'vaalilaji',

    'kuntanumero',
    'äänestysalue_lyhenne_suomi',
    'äänestysalue_suomi',

    'tietuetyyppi',

    'ennakkoäänet',
    'vaalipäivän_äänet',
    'äänet_yhteensä',
    'osuus_ennakkoäänistä',
    'osuus_vaalipäivän_äänistä',
    'osuus_äänistä_yhteensä',
    'valintatieto',
    'vertausluku',
    'sija_vertausluku',
    'sija_lopullinen',

    'vaali_nimilyhenne_1_vertailuvaali',
    'ääniä_1_vertailuvaali',

    'etunimi',
    'sukunimi',

    'sukupuoli',
    'ikä',
    'ammatti',
    'kotikunta_koodi',
    'kotikunta_nimi_suomi',
    'äidinkieli',
    'europarlamentaarikko',
    'kansanedustaja',
    'kunnanvaltuutettu',

]]


restructed_folder = Path("manual_data/kuntavaalit2017/restructured")
valitut_path = restructed_folder / "valitut.csv"

valitut.to_csv(valitut_path)
section_print(bcolors.OKCYAN, 'Saved data to', valitut_path)
