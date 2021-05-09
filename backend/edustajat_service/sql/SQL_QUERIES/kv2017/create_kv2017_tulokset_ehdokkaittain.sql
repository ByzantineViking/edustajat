CREATE TABLE IF NOT EXISTS kv2017_tulokset_ehdokkaittain (
    vaalilaji VARCHAR(1),
    kuntanumero INT,
    äänestysalue_lyhenne_suomi VARCHAR(3),
    äänestysalue_suomi TEXT,
    tietuetyyppi VARCHAR(1),
    ennakkoäänet INT,
    vaalipäivän_äänet INT,
    äänet_yhteensä INT,
    osuus_ennakkoäänistä INT,
    osuus_vaalipäivän_äänistä INT,
    osuus_äänistä_yhteensä INT,
    valintatieto TEXT,
    vertausluku INT,
    sija_vertausluku INT,
    sija_lopullinen INT,
    vaali_nimilyhenne_1_vertailuvaali TEXT,
    ääniä_1_vertailuvaali INT,
    etunimi TEXT,
    sukunimi TEXT,
    sukupuoli INT,
    ikä INT,
    ammatti TEXT,
    kotikunta_koodi TEXT,
    kotikunta_nimi_suomi TEXT,
    äidinkieli VARCHAR(2),
    europarlamentaarikko BOOLEAN,
    kansanedustaja BOOLEAN,
    kunnanvaltuutettu BOOLEAN
);