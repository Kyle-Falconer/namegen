from __future__ import annotations
from enum import Enum
from typing import List, Dict


class Gender(str, Enum):
    unisex = "unisex"
    boy = "boy"
    girl = "girl"

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(label: str):
        label = label.lower()
        if label in ('boy', 'male', 'm', 'b'):
            return Gender.boy
        elif label in ('girl', 'female', 'f', 'g'):
            return Gender.girl
        elif label in ('either', 'unisex', 'm or f', 'other'):
            return Gender.unisex
        else:
            print(f"cannot parse gender from {label}")
            raise NotImplementedError


class Region(str, Enum):
    Afghanistan = 'Afghanistan'
    Africa = 'Africa'
    Albania = 'Albania'
    Algeria = 'Algeria'
    Andorra = 'Andorra'
    Angola = 'Angola'
    Antigua_And_Barbuda = 'Antigua and Barbuda'
    Argentina = 'Argentina'
    Armenia = 'Armenia'
    Aruba = 'Aruba'
    Australia = 'Australia'
    Austria = 'Austria'
    Azerbaijan = 'Azerbaijan'
    Bahrain = 'Bahrain'
    Bangladesh = 'Bangladesh'
    Barbados = 'Barbados'
    Belarus = 'Belarus'
    Belgium = 'Belgium'
    Bengali = 'Bengali'
    Benin = 'Benin'
    Bermuda = 'Bermuda'
    Bhutan = 'Bhutan'
    Bolivia = 'Bolivia'
    Bosnia_And_Herzegovina = 'Bosnia And Herzegovina'
    Botswana = 'Botswana'
    Brazil = 'Brazil'
    Brunei_Darussalam = 'Brunei Darussalam'
    Bulgaria = 'Bulgaria'
    Burkina_Faso = 'Burkina Faso'
    Burundi = 'Burundi'
    Cambodia = 'Cambodia'
    Cameroon = 'Cameroon'
    Canada = 'Canada'
    Cape_Verde = 'Cape_Verde'
    Central_African_Republic = 'Central African Republic'
    Chad = 'Chad'
    Chile = 'Chile'
    China = 'China'
    Colombia = 'Colombia'
    Congo = 'Congo'
    Costa_Rica = 'Costa_Rica'
    Croatia = 'Croatia'
    Cuba = 'Cuba'
    Cyprus = 'Cyprus'
    Czech_Republic = 'Czech_Republic'
    Democratic_Republic_Of_Congo = 'Democratic Republic Of Congo'
    Denmark = 'Denmark'
    Djibouti = 'Djibouti'
    Dominican_Republic = 'Dominican Republic'
    Ecuador = 'Ecuador'
    Egypt = 'Egypt'
    El_Salvador = 'El Salvador'
    Equatorial_Guinea = 'Equatorial Guinea'
    Eritrea = 'Eritrea'
    Estonia = 'Estonia'
    Ethiopia = 'Ethiopia'
    Finland = 'Finland'
    France = 'France'
    Gambia = 'Gambia'
    Georgia = 'Georgia'
    Germany = 'Germany'
    Ghana = 'Ghana'
    Gibraltar = 'Gibraltar'
    Greece = 'Greece'
    Greenland = 'Greenland'
    Guatemala = 'Guatemala'
    Guinea = 'Guinea'
    Guinea_Bissau = 'Guinea Bissau'
    Guyana = 'Guyana'
    Haiti = 'Haiti'
    Hebrew = 'Hebrew'
    Honduras = 'Honduras'
    Hong_Kong = 'Hong Kong'
    Hungary = 'Hungary'
    Iceland = 'Iceland'
    India = 'India'
    Indonesia = 'Indonesia'
    Iran = 'Iran'
    Iraq = 'Iraq'
    Ireland = 'Ireland'
    Isle_Of_Man = 'Isle of Man'
    Israel = 'Israel'
    Italy = 'Italy'
    Ivory_Coast = 'Ivory Coast'
    Jamaica = 'Jamaica'
    Japan = 'Japan'
    Jersey = 'Jersey'
    Jordan = 'Jordan'
    Kazakhstan = 'Kazakhstan'
    Kenya = 'Kenya'
    Kiribati = 'Kiribati'
    Kosovo = 'Kosovo'
    Kuwait = 'Kuwait'
    Kyrgyzstan = 'Kyrgyzstan'
    Laos = 'Laos'
    Latvia = 'Latvia'
    Lebanon = 'Lebanon'
    Lesotho = 'Lesotho'
    Liberia = 'Liberia'
    Libya = 'Libya'
    Libyan_Arab_Jamahiriya = 'Libyan Arab Jamahiriya'
    Liechtenstein = 'Liechtenstein'
    Lithuania = 'Lithuania'
    Luxembourg = 'Luxembourg'
    Madagascar = 'Madagascar'
    Malawi = 'Malawi'
    Malayalam = 'Malayalam'
    Malaysia = 'Malaysia'
    Maldives = 'Maldives'
    Mali = 'Mali'
    Malta = 'Malta'
    Marathi = 'Marathi'
    Mauritania = 'Mauritania'
    Mauritius = 'Mauritius'
    Mexico = 'Mexico'
    Micronesia = 'Micronesia'
    Moldova = 'Moldova'
    Monaco = 'Monaco'
    Mongolia = 'Mongolia'
    Montenegro = 'Montenegro'
    Morocco = 'Morocco'
    Mozambique = 'Mozambique'
    Muslim = 'Muslim'
    Myanmar = 'Myanmar'
    Namibia = 'Namibia'
    Nauru = 'Nauru'
    Nepal = 'Nepal'
    Netherlands = 'Netherlands'
    New_Caledonia = 'New Caledonia'
    New_Zealand = 'New Zealand'
    Nicaragua = 'Nicaragua'
    Nigeria = 'Nigeria'
    North_Korea = 'North Korea'
    Norway = 'Norway'
    Oman = 'Oman'
    Pakistan = 'Pakistan'
    Palestine = 'Palestine'
    Panama = 'Panama'
    Paraguay = 'Paraguay'
    Peru = 'Peru'
    Philippines = 'Philippines'
    Poland = 'Poland'
    Portugal = 'Portugal'
    Puerto_Rico = 'Puerto_Rico'
    Punjabi = 'Punjabi'
    Qatar = 'Qatar'
    Republic_Of_Macedonia = 'Republic Of Macedonia'
    Romania = 'Romania'
    Russia = 'Russia'
    Rwanda = 'Rwanda'
    Saint_Kitts_And_Nevis = 'Saint Kitts and Nevis'
    Saint_Lucia = 'Saint_Lucia'
    Samoa = 'Samoa'
    Sanskrit = 'Sanskrit'
    Sao_Tome_And_Principe = 'São Tomé and Principe'
    Saudi_Arabia = 'Saudi Arabia'
    Senegal = 'Senegal'
    Serbia = 'Serbia'
    Seychelles = 'Seychelles'
    Sierra_Leone = 'Sierra Leone'
    Singapore = 'Singapore'
    Slovakia = 'Slovakia'
    Slovenia = 'Slovenia'
    Somalia = 'Somalia'
    South_Africa = 'South Africa'
    South_Korea = 'South Korea'
    South_Sudan = 'South Sudan'
    Spain = 'Spain'
    Sri_Lanka = 'Sri Lanka'
    Sudan = 'Sudan'
    Suriname = 'Suriname'
    Swaziland = 'Swaziland'
    Sweden = 'Sweden'
    Switzerland = 'Switzerland'
    Syria = 'Syria'
    Taiwan = 'Taiwan'
    Tajikistan = 'Tajikistan'
    Tamil = 'Tamil'
    Tanzania = 'Tanzania'
    Telugu = 'Telugu'
    Thailand = 'Thailand'
    The_Netherlands = 'The Netherlands'
    Timor_Leste = 'Timor Leste'
    Togo = 'Togo'
    Tonga = 'Tonga'
    Trinidad_And_Tobago = 'Trinidad And Tobago'
    Tunisia = 'Tunisia'
    Turkey = 'Turkey'
    Turkmenistan = 'Turkmenistan'
    Uganda = 'Uganda'
    Ukraine = 'Ukraine'
    United_Arab_Emirates = 'United Arab Emirates'
    United_Kingdom = 'United Kingdom'
    United_States = 'United States'
    Unknown = 'Unknown'
    Uruguay = 'Uruguay'
    US_Virgin_Islands = 'US Virgin Islands'
    Uzbekistan = 'Uzbekistan'
    Vanuatu = 'Vanuatu'
    Venezuela = 'Venezuela'
    Vietnam = 'Vietnam'
    Yemen = 'Yemen'
    Zambia = 'Zambia'
    Zimbabwe = 'Zimbabwe'
    English = 'English'

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(label: str):
        label = label.lower()
        if label == 'english' or label == 'england':
            return Region.English
        if label == 'tamil':
            return Region.Tamil
        if label == 'malayalam':
            return Region.Malayalam
        if label == 'sanskrit':
            return Region.Sanskrit
        if label == 'telugu':
            return Region.Telugu
        if label == 'muslim':
            return Region.Muslim
        if label == 'bengali':
            return Region.Bengali
        if label == 'marathi':
            return Region.Marathi
        if label == 'punjabi':
            return Region.Punjabi
        if label == 'afghanistan':
            return Region.Afghanistan
        if label == 'africa':
            return Region.Africa
        if label == 'albania':
            return Region.Albania
        if label == 'algeria':
            return Region.Algeria
        if label == 'andorra':
            return Region.Andorra
        if label == 'angola':
            return Region.Angola
        if label == 'antigua and barbuda':
            return Region.Antigua_And_Barbuda
        if label == 'argentina':
            return Region.Argentina
        if label == 'armenia':
            return Region.Armenia
        if label == 'aruba':
            return Region.Aruba
        if label == 'australia':
            return Region.Australia
        if label == 'austria':
            return Region.Austria
        if label == 'azerbaijan':
            return Region.Azerbaijan
        if label == 'bahrain':
            return Region.Bahrain
        if label == 'bangladesh':
            return Region.Bangladesh
        if label == 'barbados':
            return Region.Barbados
        if label == 'belarus':
            return Region.Belarus
        if label == 'belgium':
            return Region.Belgium
        if label == 'bengali':
            return Region.Bengali
        if label == 'benin':
            return Region.Benin
        if label == 'bermuda':
            return Region.Bermuda
        if label == 'bhutan':
            return Region.Bhutan
        if label == 'bolivia':
            return Region.Bolivia
        if label == 'bosnia and herzegovina':
            return Region.Bosnia_And_Herzegovina
        if label == 'botswana':
            return Region.Botswana
        if label == 'brazil':
            return Region.Brazil
        if label == 'brunei darussalam':
            return Region.Brunei_Darussalam
        if label == 'bulgaria':
            return Region.Bulgaria
        if label == 'burkina faso':
            return Region.Burkina_Faso
        if label == 'burundi':
            return Region.Burundi
        if label == 'cambodia':
            return Region.Cambodia
        if label == 'cameroon':
            return Region.Cameroon
        if label == 'canada':
            return Region.Canada
        if label == 'cape verde':
            return Region.Cape_Verde
        if label == 'central african republic':
            return Region.Central_African_Republic
        if label == 'chad':
            return Region.Chad
        if label == 'chile':
            return Region.Chile
        if label == 'china':
            return Region.China
        if label == 'colombia':
            return Region.Colombia
        if label == 'congo':
            return Region.Congo
        if label == 'costa rica':
            return Region.Costa_Rica
        if label == 'croatia':
            return Region.Croatia
        if label == 'cuba':
            return Region.Cuba
        if label == 'cyprus':
            return Region.Cyprus
        if label == 'czech republic':
            return Region.Czech_Republic
        if label == 'democratic republic of congo':
            return Region.Democratic_Republic_Of_Congo
        if label == 'denmark':
            return Region.Denmark
        if label == 'djibouti':
            return Region.Djibouti
        if label == 'dominican republic':
            return Region.Dominican_Republic
        if label == 'ecuador':
            return Region.Ecuador
        if label == 'egypt':
            return Region.Egypt
        if label == 'el salvador':
            return Region.El_Salvador
        if label == 'equatorial guinea':
            return Region.Equatorial_Guinea
        if label == 'eritrea':
            return Region.Eritrea
        if label == 'estonia':
            return Region.Estonia
        if label == 'ethiopia':
            return Region.Ethiopia
        if label == 'finland':
            return Region.Finland
        if label == 'france':
            return Region.France
        if label == 'gambia':
            return Region.Gambia
        if label == 'georgia':
            return Region.Georgia
        if label == 'germany':
            return Region.Germany
        if label == 'ghana':
            return Region.Ghana
        if label == 'gibraltar':
            return Region.Gibraltar
        if label == 'greece':
            return Region.Greece
        if label == 'greenland':
            return Region.Greenland
        if label == 'guatemala':
            return Region.Guatemala
        if label == 'guinea':
            return Region.Guinea
        if label == 'guinea-bissau':
            return Region.Guinea_Bissau
        if label == 'guyana':
            return Region.Guyana
        if label == 'haiti':
            return Region.Haiti
        if label == 'hebrew':
            return Region.Hebrew
        if label == 'honduras':
            return Region.Honduras
        if label == 'hong kong':
            return Region.Hong_Kong
        if label == 'hungary':
            return Region.Hungary
        if label == 'iceland':
            return Region.Iceland
        if label == 'india' or label == 'indian':
            return Region.India
        if label == 'indonesia':
            return Region.Indonesia
        if label == 'iran':
            return Region.Iran
        if label == 'iraq':
            return Region.Iraq
        if label == 'ireland':
            return Region.Ireland
        if label == 'isle of man':
            return Region.Isle_Of_Man
        if label == 'israel':
            return Region.Israel
        if label == 'italy':
            return Region.Italy
        if label == 'ivory coast':
            return Region.Ivory_Coast
        if label == 'jamaica':
            return Region.Jamaica
        if label == 'japan':
            return Region.Japan
        if label == 'jersey':
            return Region.Jersey
        if label == 'jordan':
            return Region.Jordan
        if label == 'kazakhstan':
            return Region.Kazakhstan
        if label == 'kenya':
            return Region.Kenya
        if label == 'kiribati':
            return Region.Kiribati
        if label == 'kosovo':
            return Region.Kosovo
        if label == 'kuwait':
            return Region.Kuwait
        if label == 'kyrgyzstan':
            return Region.Kyrgyzstan
        if label == 'laos':
            return Region.Laos
        if label == 'latvia':
            return Region.Latvia
        if label == 'lebanon':
            return Region.Lebanon
        if label == 'lesotho':
            return Region.Lesotho
        if label == 'liberia':
            return Region.Liberia
        if label == 'libya':
            return Region.Libya
        if label == 'libyan arab jamahiriya':
            return Region.Libyan_Arab_Jamahiriya
        if label == 'liechtenstein':
            return Region.Liechtenstein
        if label == 'lithuania':
            return Region.Lithuania
        if label == 'luxembourg':
            return Region.Luxembourg
        if label == 'madagascar':
            return Region.Madagascar
        if label == 'malawi':
            return Region.Malawi
        if label == 'malayalam':
            return Region.Malayalam
        if label == 'malaysia':
            return Region.Malaysia
        if label == 'maldives':
            return Region.Maldives
        if label == 'mali':
            return Region.Mali
        if label == 'malta':
            return Region.Malta
        if label == 'marathi':
            return Region.Marathi
        if label == 'mauritania':
            return Region.Mauritania
        if label == 'mauritius':
            return Region.Mauritius
        if label == 'mexico':
            return Region.Mexico
        if label == 'micronesia':
            return Region.Micronesia
        if label == 'moldova':
            return Region.Moldova
        if label == 'monaco':
            return Region.Monaco
        if label == 'mongolia':
            return Region.Mongolia
        if label == 'montenegro':
            return Region.Montenegro
        if label == 'morocco':
            return Region.Morocco
        if label == 'mozambique':
            return Region.Mozambique
        if label == 'muslim':
            return Region.Muslim
        if label == 'myanmar [burma]':
            return Region.Myanmar
        if label == 'namibia':
            return Region.Namibia
        if label == 'nauru':
            return Region.Nauru
        if label == 'nepal':
            return Region.Nepal
        if label == 'netherlands':
            return Region.Netherlands
        if label == 'new caledonia':
            return Region.New_Caledonia
        if label == 'new zealand':
            return Region.New_Zealand
        if label == 'nicaragua':
            return Region.Nicaragua
        if label == 'nigeria':
            return Region.Nigeria
        if label == 'north korea':
            return Region.North_Korea
        if label == 'norway':
            return Region.Norway
        if label == 'oman':
            return Region.Oman
        if label == 'pakistan':
            return Region.Pakistan
        if label == 'palestine':
            return Region.Palestine
        if label == 'panama':
            return Region.Panama
        if label == 'paraguay':
            return Region.Paraguay
        if label == 'peru':
            return Region.Peru
        if label == 'philippines':
            return Region.Philippines
        if label == 'poland':
            return Region.Poland
        if label == 'portugal':
            return Region.Portugal
        if label == 'puerto rico':
            return Region.Puerto_Rico
        if label == 'punjabi':
            return Region.Punjabi
        if label == 'qatar':
            return Region.Qatar
        if label == 'republic of macedonia':
            return Region.Republic_Of_Macedonia
        if label == 'romania':
            return Region.Romania
        if label == 'russia':
            return Region.Russia
        if label == 'rwanda':
            return Region.Rwanda
        if label == 'saint kitts and nevis':
            return Region.Saint_Kitts_And_Nevis
        if label == 'saint lucia':
            return Region.Saint_Lucia
        if label == 'samoa':
            return Region.Samoa
        if label == 'sanskrit':
            return Region.Sanskrit
        if label == 'sao tome and principe' or label == 'são tomé and príncipe':
            return Region.Sao_Tome_And_Principe
        if label == 'saudi arabia':
            return Region.Saudi_Arabia
        if label == 'senegal':
            return Region.Senegal
        if label == 'serbia':
            return Region.Serbia
        if label == 'seychelles':
            return Region.Seychelles
        if label == 'sierra leone':
            return Region.Sierra_Leone
        if label == 'singapore':
            return Region.Singapore
        if label == 'slovakia':
            return Region.Slovakia
        if label == 'slovenia':
            return Region.Slovenia
        if label == 'somalia':
            return Region.Somalia
        if label == 'south africa':
            return Region.South_Africa
        if label == 'south korea':
            return Region.South_Korea
        if label == 'south sudan':
            return Region.South_Sudan
        if label == 'spain':
            return Region.Spain
        if label == 'sri lanka':
            return Region.Sri_Lanka
        if label == 'sudan':
            return Region.Sudan
        if label == 'suriname':
            return Region.Suriname
        if label == 'swaziland':
            return Region.Swaziland
        if label == 'sweden':
            return Region.Sweden
        if label == 'switzerland':
            return Region.Switzerland
        if label == 'syria':
            return Region.Syria
        if label == 'taiwan':
            return Region.Taiwan
        if label == 'tajikistan':
            return Region.Tajikistan
        if label == 'tamil':
            return Region.Tamil
        if label == 'tanzania':
            return Region.Tanzania
        if label == 'telugu':
            return Region.Telugu
        if label == 'thailand':
            return Region.Thailand
        if label == 'the netherlands':
            return Region.The_Netherlands
        if label == 'timor-leste':
            return Region.Timor_Leste
        if label == 'togo':
            return Region.Togo
        if label == 'tonga':
            return Region.Tonga
        if label == 'trinidad and tobago':
            return Region.Trinidad_And_Tobago
        if label == 'tunisia':
            return Region.Tunisia
        if label == 'turkey':
            return Region.Turkey
        if label == 'turkmenistan':
            return Region.Turkmenistan
        if label == 'uganda':
            return Region.Uganda
        if label == 'ukraine':
            return Region.Ukraine
        if label == 'united arab emirates':
            return Region.United_Arab_Emirates
        if label == 'united kingdom':
            return Region.United_Kingdom
        if label == 'united states':
            return Region.United_States
        if label == 'unknown':
            return Region.Unknown
        if label == 'uruguay':
            return Region.Uruguay
        if label == 'us virgin islands':
            return Region.US_Virgin_Islands
        if label == 'uzbekistan':
            return Region.Uzbekistan
        if label == 'vanuatu':
            return Region.Vanuatu
        if label == 'venezuela':
            return Region.Venezuela
        if label == 'vietnam':
            return Region.Vietnam
        if label == 'yemen':
            return Region.Yemen
        if label == 'zambia':
            return Region.Zambia
        if label == 'zimbabwe':
            return Region.Zimbabwe
        else:
            print(f"cannot parse language or region from \"{label}\"")
            return Region.Unknown


class NameMeaning(object):
    def __init__(self, meaning: str, origins: List[Region]):
        self.meaning = meaning
        self.origins = origins


class NameDefinition(object):
    def __init__(self, name: str, gender: Gender = None, meanings: List[NameMeaning] = None, meaning: str = None,
                 origin: Region or str = None,
                 known_persons: str = None):
        self.name = name
        self.gender = gender
        self.meanings: List[NameMeaning] = []
        self.known_persons = []
        if known_persons is not None:
            self.known_persons.append(known_persons)
        self.add_meaning(meaning, origin)
        self.add_meanings(meanings)

    def add_meaning(self, meaning: str, origin: Region or str = None):
        if meaning is None:
            return
        if type(meaning) is str and meaning is not None:
            meaning = meaning.lower().strip()

        # we already know about this meaning, so just add the new origin
        for idx, cur_meaning in enumerate(self.meanings):
            if cur_meaning.meaning == meaning:
                if origin not in cur_meaning.origins:
                    cur_meaning.origins.append(origin)
                    self.meanings[idx] = cur_meaning
                return

        # new meaning, so let's save it
        clean_region: Region = Region.Unknown
        if type(origin) is str:
            clean_region = Region.from_str(origin)
        else:
            clean_region = origin
        self.meanings.append(NameMeaning(meaning=meaning, origins=[clean_region]))

    def add_meanings(self, meanings: List[NameMeaning]):
        if meanings is not None:
            for m in meanings:
                for o in m.origins:
                    self.add_meaning(m.meaning, o)

    def merge_name(self, other_name: NameDefinition):
        if self.gender is None:
            self.gender = other_name.gender
        elif other_name.gender is not None and other_name.gender != self.gender:
            self.gender = Gender.unisex

        self.known_persons = self.known_persons + other_name.known_persons

    def append_attrs(self, gender: Gender = None, meanings: List[NameMeaning] = None, meaning: str = None, origin: Region = None,
                     known_persons: str = None):
        self.add_meaning(meaning, origin)
        self.add_meanings(meanings)
        if gender is not None and gender != self.gender:
            self.gender = Gender.unisex
        if known_persons is not None and known_persons not in self.known_persons:
            self.known_persons.append(known_persons)

    def get_all_origins(self) -> List[Region]:
        res = set()
        for m in self.meanings:
            res.update(set(m.origins))
        list_result = list(res)
        list_result.sort()
        if list_result is None:
            return []
        return list_result

    def get_all_meanings(self) -> List[str]:
        res = []
        for m in self.meanings:
            res.append(m.meaning)
        return res

    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "meanings": [m.__dict__ for m in self.meanings],
            "known_persons": str(','.join(self.known_persons))
        }

    @classmethod
    def columns(cls):
        return ['Name', 'Gender', 'Language', 'Meaning']
