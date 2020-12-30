from Name import Region

religious_indicators = ["lord", "god", "g-d", "goddess", "jesus", "zeus", "virgin", "brahma", "vishnu", "shiva",
                        "ganapati", "lakshmi", "durga", "krishna", "hanuman", "agni", "surya", "indra", "religious",
                        "king david", "old testament", "new testament"]
excluded_name_endings = (
'ita', 'line', 'ina', 'loena', 'iden', 'aden', 'adun', 'idun', 'idena', 'adena', 'aduna', 'iduna')
excluded_startings = ('a', 'k', 'jy', 'eu', 'mary', 'mara', 'bah', 'baka', 'brit', 'shawn', 'hild')
excluded_contains = ('kini', 'ika', 'eswit', 'sheba', 'shit', 'sheet')
hard_to_pronounce = ('kh', 'gh', 'haa', 'ayn', 'aij')

western_origins = [Region.United_States, Region.United_Kingdom, Region.English, Region.Germany, Region.France,
                   Region.Italy]
indian_origins = [Region.Tamil, Region.Malayalam, Region.Sanskrit, Region.Telugu, Region.Muslim, Region.Bengali,
                  Region.Marathi, Region.Punjabi]

# exclude names that have a single origin in any of these countries or regions
exclude_only_origins = [Region.Japan, Region.Saudi_Arabia, Region.South_Africa, Region.Ireland, Region.African_American,
                        Region.Africa, Region.Afghanistan, Region.China, Region.Latin_America, Region.Spain,
                        Region.Mexico, Region.Scotland, Region.South_Korea, Region.North_Korea, Region.Taiwan]
