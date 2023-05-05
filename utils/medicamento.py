from typing import List
from core.entidades import Medicamento
from utils.random import random


names_medicamento = [
    "ZIAGEN",
    "TYMLOS",
    "ORENCIA",
    "REOPRO",
    "CALQUENCE",
    "PRECOSE",
    "SECTRAL",
    "DIAMOX",
    "ACETADOTE",
    "SORIATANE",
    "TUDORZA PRESSAIR",
    "ZOVIRAX",
    "HUMIRA",
    "DIFFERIN",
    "HEPSERA",
    "ADENOCARD",
    "ADUHELM",
    "GILOTRIF",
    "EYLEA",
    "FABRAZYME",
    "ALBENZA",
    "TANZEUM",
    "PROVENTIL-HFA, VENTOLIN-HFA",
    "LASTACAFT",
    "PROLEUKIN",
    "ALECENSA",
    "CAMPATH",
    "FOSAMAX",
    "UROXATRAL",
    "PRALUENT",
    "TEKTURNA",
    "ZYLOPRIM",
    "AXERT",
    "NESINA",
    "LOTRONEX",
    "XANAX",
    "CAVERJECT, EDEX, MUSE",
    "ACTIVASE",
    "ENTEREG",
    "LETAIRIS",
    "ETHYOL",
    "MIDAMOR",
    "NEXTERONE",
    "NORVASC",
    "RYBREVANT",
    "AMOXIL",
    "AUGMENTIN",
    "ADDERALL XR 10",
    "ABELCET, AMBISOME",
    "UNASYN",
    "AGRYLIN",
    "KINERET",
    "ARIMIDEX",
    "Andexxa",
    "ERAXIS",
    "EBANGA",
    "ERLEADA",
    "ELIQUIS",
    "APOKYN",
    "IOPIDINE",
    "OTEZLA",
    "EMEND",
    "BROVANA",
    "R-GENE 10",
    "ABILIFY",
    "NUVIGIL",
    "COARTEM",
    "ELSPAR",
    "DURLAZA",
    "Translarna",
    "REYATAZ",
    "TENORMIN",
    "TECENTRIQ",
    "STRATTERA",
    "LIPITOR",
    "MEPRON",
    "MALARONE",
    "ATROPEN",
    "RIDAURA",
    "STENDRA",
    "AYVAKIT",
    "DOPTELET",
    "BAVENCIO",
    "YESCARTA",
    "VIDAZA",
    "IMURAN",
    "ASTELIN, OPTIVAR",
    "EDARBI",
    "ZITHROMAX",
    "AZACTAM",
    "PHOSLYRA",
    "ARANESP",
    "PULMOZYME",
    "EPOGEN/PROCRIT",
    "COPAXONE",
    "INTRON A",
    "ALFERON",
    "PROVAYBLUE",
    "PALFORZIA",
    "PEGASYS",
    "PEGINTRON",
    "CUROSURF"
]


def get_medicamento():
    return random(array=names_medicamento)


def get_fabricante():
    return random(array=names_medicamento)


def get_medicamentos() -> List[Medicamento]:
    medicamentos = []

    for _ in range(0, 10):
        medicamentos.append(Medicamento(nome=get_medicamento(
        ), fabricante=get_fabricante(), quantidade=10, validade='01/10/2024', valor=50.0))

    return medicamentos
