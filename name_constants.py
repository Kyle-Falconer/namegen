from Name import Region

religious_indicators = ["lord", "god", "g-d", "goddess", "jesus", "zeus", "virgin", "brahma", "vishnu", "shiva",
                        "ganapati", "lakshmi", "durga", "krishna", "hanuman", "agni", "surya", "indra", "religious",
                        "king david", "old testament", "new testament", "baptist", "saint"]
excluded_name_endings = (
    'ita', 'line', 'ina', 'loena', 'iden', 'aden', 'adun', 'idun', 'idena', 'adena', 'aduna', 'iduna')
excluded_startings = ('a', 'k', 'jy', 'eu', 'mary', 'mara', 'bah', 'baka', 'brit', 'shawn', 'hild')
excluded_contains = ('kini', 'ika', 'eswit', 'sheba', 'shit', 'sheet')
hard_to_pronounce = ('kh', 'gh', 'haa', 'ayn', 'aij')

western_origins = [
    Region.English,
    Region.France,
    Region.Germany,
    Region.Italy,
    Region.United_Kingdom,
    Region.United_States
]

indian_origins = [
    Region.Bengali,
    Region.Malayalam,
    Region.Marathi,
    Region.Muslim,
    Region.Punjabi,
    Region.Sanskrit,
    Region.Tamil,
    Region.Telugu
]

# exclude names that have a single origin in any of these countries or regions
exclude_only_origins = [
    Region.Afghanistan,
    Region.Africa,
    Region.African_American,
    Region.China,
    Region.Ireland,
    Region.Japan,
    Region.Latin_America,
    Region.Mexico,
    Region.North_Korea,
    Region.Saudi_Arabia,
    Region.Scotland,
    Region.South_Africa,
    Region.South_Korea,
    Region.Spain,
    Region.Taiwan
]
