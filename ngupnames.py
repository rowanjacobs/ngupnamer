import random
from dataclasses import dataclass
from typing import List

@dataclass
class Lang:
    months: List[str]
    numbers: List[str]
    bynames: List[str]
    given_names: List[str]

def init_langs():
    ndxiixun = Lang(
            [
                'Kwą¹rá²se²', 'Chi²¹xí²', 'Za²ñą¹³',
                'Ñą¹³mba³', 'Ru²¹qua²', 'Ti¹rú³',
                'Wá²ko¹xe²', 'Ñį²nda¹³', 'Ku¹su³hi¹',
                'Lli¹³ya³mba¹te¹xe²', 'Mbi²ché³la¹', 'Sa³¹ka¹',
                'Ŋų¹nį²́'
            ],
            [
                'Mbi³', 'Rra³', 'Li³', 'Hé³xi²', 'Ha³',
                'Nį́³', 'Nde¹rra³', 'Nde¹li³', 'Ŋgo³kú³', 'Zį²ʼą¹zą²'
            ],
            [
                'Se²'
                ],
            []
            )

    for number in ndxiixun.numbers[:-1]:
        ndxiixun.numbers.append('Zį²ʼą¹zą² ' + number)
        ndxiixun.numbers.append('Rra³ Zį²ʼą¹zą² ' + number)

    mañi = Lang(
             [
                'Hàkmąŗał', 'Chiixichko', 'Zñąą̀', 'Ñąą̀nma',
                'Řuukwa', 'Tirùkkoxał', 'Waxkoxko', 'Ñįnnaàko',
                'Kułùhiko', 'Liìyàmatexe', 'Michèʼŗļani', 'Łàakani',
                'Ŋųnįŋ'
                ],
             [
                'Mwì', 'Rà', 'Ļì', 'Hèx', 'Hà', 'Ŋų̀nįm',
                'Ŋų̀nerà', 'Ŋų̀neļì', 'Ŋòkunm', 'Zįʼązą'
                ],
             [
                 'Řù',
                 'Xą',
                 'Zą̀ą',
                 'Zįųñ',
                 'Mįŋąmb',
                 'Hàpin',
                 'Hàtambum',
                 'Chałŋo',
                 'Ąndupokuŋo', # beautiful
                 'Ąndułįŋ', # bright/light
                 'Ąnduwiiwii', # whisperer
                 'Ąnduʼliʼli', # kind
                 'Nąnduŋawkaŋawka', # I hear they're a liar
                 'Nąndòinchiʼdaʼ', # I hear they stole something
                 'Nąnduapaà', # rumored to be dangerous
                 'Nąndotumąyek', # accused murderer
                 'Nąñą Kachaą̀ni' # scarred
                 ],
             [
                 'Ząmřani', 'ʼAchùlani', 'Chułiko', 'Ŋàaze', 'Yawuu',
                 'Iʼichułko', 'Emiknoʼoł', 'Ateche',
                 'Mirèñą Zamřani', 'Į̀ŋuʼa ʼAchùlani', 'Rùchani Chułiko',
                 'Mirèʼaa Iʼichułko', 'Chuunchoochhą Ateche',
                 'Ŋòruyàļàaex', 'Ñi Kayà', 'Ŋųhŋąą', 'Hàłahu'
                 ]
             )

    for number in mañi.numbers[:-1]:
        mañi.numbers.append('Zįʼązą ' + number)
        mañi.numbers.append('Rà Zįʼązą ' + number)

    hlung = Lang(
             [
                'Jakwarał', 'Xiixixok', 'Sñaa', 'Ñạạnạ',
                'Luukwa', 'Tirukkoxał', 'Waxkoxok', 'Ñịlạạkọ',
                'Kułujiko', 'Liyihi', 'Michehelani', 'Łaakani',
                'Ŋụlịị'
                ],
             [
                'Muwi', 'Ra', 'Li', 'Jex', 'Ja', 'Ŋụlịw',
                'Ŋụlẹrạ','Ŋụlẹlị','Ŋokun','Sịyịhạạsạ'
                ],
             [
                 'Tọnụldạh',
                 'Ŋoruyalayex'
                 ],
             [
                 'Sạmlạnị'
                 ]
             )

    for number in hlung.numbers[:-1]:
        hlung.numbers.append('Sịyịhạạsạ ' + number)
        hlung.numbers.append('Ra Sịyịhạạsạ ' + number)

    nichoh = Lang(
             [
                'Jàcuą́uhtlà', 'Chístzi', 'Zñą̂', 'Ñą̂u',
                'Ácuú', 'Tírùj', 'Guascsó', 'Ñįndâ',
                'Cúsùjí', 'Llîmbátzé', 'Mbitzèꞌrguá', 'Tlǎcá',
                'Ŋų́nįuh'
                ],
             [
                'Mbguì', 'Rà', 'Guì', 'Jsè', 'Jà',
                'Nį̀u', 'Ndérà', 'Ndéguì', 'Ŋcòcùu', 'Zįꞌzą́'
                ],
             [],
             []
             )

    for number in nichoh.numbers[:-1]:
        nichoh.numbers.append('Zįꞌzą́ ' + number)
        nichoh.numbers.append('Rà Zįꞌzą́ ' + number)

    awatese = Lang(
            [
                'Karał', 'Tixin', 'Zahang', 'Nayąnmanga',
                'Řuką', 'Tukoxąru', 'Wąxku', 'Ningną',
                'Kułi', 'Liyąmąte', 'Miteřą', 'Łak',
                'Nguning'
                ],
            [
                'Mwi', 'Řą', 'Łi', 'Exe', 'Ahą',
                'Ngunim', 'Ngunrą', 'Ngunłi', 'Ngukunum',
                'Ziya'
                ],
            [],
            []
            )

    for number in awatese.numbers[:-1]:
        awatese.numbers.append('Ziya ' + number)
        awatese.numbers.append('Řąziya ' + number)

    return [ndxiixun, hlung, mañi, nichoh, awatese]


def datename(lang):
    month = random.choice(lang.months)
    number = random.choice(lang.numbers)
    return number + ' ' + month


def byname(lang):
    if random.randint(1,3) > 1:
        return ''
    if len(lang.bynames) == 0:
        return ''
    return random.choice(lang.bynames)


def given_name(lang):
    if random.randint(1,6) > 1:
        return ''
    if len(lang.given_names) == 0:
        return ''
    return random.choice(lang.given_names)


def ngupname(langs):
    lang = random.choice(langs)
    name = datename(lang)
    this_byname = byname(lang)
    this_given_name = given_name(lang)
    if this_given_name != '':
        name = this_given_name + ' ' + name
    if this_byname != '':
        name = name + ' ' + this_byname
    return name

