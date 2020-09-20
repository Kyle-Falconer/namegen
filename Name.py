from __future__ import annotations

from enum import Enum


class Gender(Enum):
    unisex = 0
    boy = 1
    girl = 2

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


class Region(Enum):
    Afghanistan = 1
    Albania = 2
    Algeria = 3
    Andorra = 4
    Angola = 5
    Antigua_And_Barbuda = 6
    Argentina = 7
    Armenia = 8
    Aruba = 9
    Australia = 10
    Austria = 11
    Azerbaijan = 12
    Bahrain = 13
    Bangladesh = 14
    Barbados = 15
    Belarus = 16
    Belgium = 17
    Bengali = 18
    Benin = 19
    Bermuda = 20
    Bhutan = 21
    Bolivia = 22
    Bosnia_And_Herzegovina = 23
    Botswana = 24
    Brazil = 25
    Brunei_Darussalam = 26
    Bulgaria = 27
    Burkina_Faso = 28
    Burundi = 29
    Cambodia = 30
    Cameroon = 31
    Canada = 32
    Cape_Verde = 33
    Central_African_Republic = 34
    Chad = 35
    Chile = 36
    China = 37
    Colombia = 38
    Congo = 39
    Costa_Rica = 40
    Croatia = 41
    Cuba = 42
    Cyprus = 43
    Czech_Republic = 44
    Democratic_Republic_Of_Congo = 45
    Denmark = 46
    Djibouti = 47
    Dominican_Republic = 48
    Ecuador = 49
    Egypt = 50
    El_Salvador = 51
    Equatorial_Guinea = 52
    Eritrea = 53
    Estonia = 54
    Ethiopia = 55
    Finland = 56
    France = 57
    Gambia = 58
    Georgia = 59
    Germany = 60
    Ghana = 61
    Gibraltar = 62
    Greece = 63
    Greenland = 64
    Guatemala = 65
    Guinea = 66
    Guinea_Bissau = 67
    Guyana = 68
    Haiti = 69
    Honduras = 70
    Hong_Kong = 71
    Hungary = 72
    Iceland = 73
    India = 74
    Indonesia = 75
    Iran = 76
    Iraq = 77
    Ireland = 78
    Isle_Of_Man = 79
    Israel = 80
    Italy = 81
    Ivory_Coast = 82
    Jamaica = 83
    Japan = 84
    Jersey = 85
    Jordan = 86
    Kazakhstan = 87
    Kenya = 88
    Kiribati = 89
    Kosovo = 90
    Kuwait = 91
    Kyrgyzstan = 92
    Laos = 93
    Latvia = 94
    Lebanon = 95
    Lesotho = 96
    Liberia = 97
    Libya = 98
    Libyan_Arab_Jamahiriya = 99
    Liechtenstein = 100
    Lithuania = 101
    Luxembourg = 102
    Madagascar = 103
    Malawi = 104
    Malayalam = 105
    Malaysia = 106
    Maldives = 107
    Mali = 108
    Malta = 109
    Marathi = 110
    Mauritania = 111
    Mauritius = 112
    Mexico = 113
    Micronesia = 114
    Moldova = 115
    Monaco = 116
    Mongolia = 117
    Montenegro = 118
    Morocco = 119
    Mozambique = 120
    Muslim = 121
    Myanmar = 122
    Namibia = 123
    Nauru = 124
    Nepal = 125
    Netherlands = 126
    New_Caledonia = 127
    New_Zealand = 128
    Nicaragua = 129
    Nigeria = 130
    North_Korea = 131
    Norway = 132
    Oman = 133
    Pakistan = 134
    Palestine = 135
    Panama = 136
    Paraguay = 137
    Peru = 138
    Philippines = 139
    Poland = 140
    Portugal = 141
    Puerto_Rico = 142
    Punjabi = 143
    Qatar = 144
    Republic_Of_Macedonia = 145
    Romania = 146
    Russia = 147
    Rwanda = 148
    Saint_Kitts_And_Nevis = 149
    Saint_Lucia = 150
    Samoa = 151
    Sanskrit = 152
    Sao_Tome_And_Principe = 153
    Saudi_Arabia = 154
    Senegal = 155
    Serbia = 156
    Seychelles = 157
    Sierra_Leone = 158
    Singapore = 159
    Slovakia = 160
    Slovenia = 161
    Somalia = 162
    South_Africa = 163
    South_Korea = 164
    South_Sudan = 165
    Spain = 166
    Sri_Lanka = 167
    Sudan = 168
    Suriname = 169
    Swaziland = 170
    Sweden = 171
    Switzerland = 172
    Syria = 173
    Taiwan = 174
    Tajikistan = 175
    Tamil = 176
    Tanzania = 177
    Telugu = 178
    Thailand = 179
    The_Netherlands = 180
    Timor_Leste = 181
    Togo = 182
    Tonga = 183
    Trinidad_And_Tobago = 184
    Tunisia = 185
    Turkey = 186
    Turkmenistan = 187
    Uganda = 188
    Ukraine = 189
    United_Arab_Emirates = 190
    United_Kingdom = 191
    United_States = 192
    Unknown = 193
    Uruguay = 194
    US_Virgin_Islands = 195
    Uzbekistan = 196
    Vanuatu = 197
    Venezuela = 198
    Vietnam = 199
    Yemen = 200
    Zambia = 201
    Zimbabwe = 202
    English = 203

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(label: str):
        label = label.lower()
        if label == 'english':
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
        if label == 'honduras':
            return Region.Honduras
        if label == 'hong kong':
            return Region.Hong_Kong
        if label == 'hungary':
            return Region.Hungary
        if label == 'iceland':
            return Region.Iceland
        if label == 'india':
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
        if label == 'sao tome and principe' or 'são tomé and príncipe':
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
            return Region.United_States


class NameDefinition(object):
    def __init__(self, name: str, gender: Gender = None, meaning: str = None, origin: Region or str= None, known_persons: str = None):
        self.name = name
        self.gender = gender
        self.meaning = []
        self.origin = []
        self.known_persons = []
        if meaning is not None:
            self.meaning.append(meaning.lower().strip())
        if origin is not None:
            if type(origin) is str:
                self.add_origins(origin)
            else:
                self.origin.append(origin)
        if known_persons is not None:
            self.known_persons.append(known_persons)

    def merge_name(self, other_name: NameDefinition):
        if self.gender is None:
            self.gender = other_name.gender
        elif other_name.gender is not None and other_name.gender != self.gender:
            self.gender = Gender.unisex
        self.meaning = self.meaning + other_name.meaning
        self.origin = self.origin + other_name.origin
        self.known_persons = self.known_persons + other_name.known_persons

    def add_origins(self, origins:str):
        if ',' in origins:
            for origin_str in origins.split(','):
                self.origin.append(Region.from_str(origin_str))
        else:
            self.origin.append(Region.from_str(origins))

    def append_attrs(self, gender: Gender = None, meaning: str = None, origin: Region = None, known_persons: str = None):
        if gender is not None and gender != self.gender:
            self.gender = Gender.unisex
        if meaning is not None:
            meaning = meaning.lower().strip()
            if meaning not in self.meaning:
                self.meaning.append(meaning)
        if origin is not None and origin not in self.origin:
            self.origin.append(origin)
        if known_persons is not None and known_persons not in self.known_persons:
            self.known_persons.append(known_persons)

    def get_meaning(self):
        return str(', '.join(self.meaning)).strip()

    #     def __iter__(self):
    #         yield self.name
    #         yield str(','.join(self.gender))
    #         yield str(','.join(self.language))
    #         yield str(','.join(self.meaning))

    def to_dict(self):
        meaning_str = ''
        if self.meaning is not None:
            meaning_str = str(','.join(self.meaning))
        return {
            "name": self.name,
            "gender": str(self.gender),
            "origin":  str(','.join([str(lang) for lang in self.origin])),
            "meaning": meaning_str,
            "known_persons": str(','.join(self.known_persons)),
        }

    @classmethod
    def columns(cls):
        return ['Name', 'Gender', 'Language', 'Meaning']


if __name__ == "__main__":
    test_name1 = NameDefinition("Sue", Gender.girl, "Graceful lily", Region.English)
    print(f"{test_name1.to_dict()}")

    print(f"{','.join(['a', 'b'])}")
    test_name1.append_attrs(gender=Gender.boy)
    print(f"{test_name1.to_dict()}")
