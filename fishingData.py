fishingBiomes = {
    "lush":
     ["minecraft:birch_forest",
     "minecraft:dark_forest",
     "minecraft:flower_forest",
     "minecraft:forest",
     "minecraft:plains",
     "minecraft:swamp",
     "originrealms:maple_forest",
     "originrealms:autumn_forest"],
  "boreal":
     ["minecraft:meadow",
          "minecraft:old_growth_spruce_taiga",
          "minecraft:taiga",
          "minecraft:windswept_hills",
          "originrealms:cold_maple_forest",
          "originrealms:foothills",
          "originrealms:mountain_valley",
          "originrealms:cold_birch_forest"],
  "tropical": ["minecraft:bamboo_jungle",
          "minecraft:cherry_grove",
          "minecraft:jungle",
          "minecraft:sparse_jungle",
          "originrealms:jungle_oasis",
          "originrealms:oasis",
          "originrealms:mangrove_swamp"],
  "arid":
     ["minecraft:badlands",
          "minecraft:desert",
          "minecraft:savanna",
          "minecraft:wooded_badlands",
          "originrealms:badlands_oasis",
          "originrealms:blighted_badlands"],
  "arctic":
     ["minecraft:snowy_plains",
          "minecraft:snowy_slopes",
          "minecraft:snowy_taiga",
          "minecraft:ice_spikes"],
  "shoreline":
     ["minecraft:beach",
          "minecraft:snowy_beach"],
  "ocean":
     ["minecraft:frozen_ocean",
          "minecraft:ocean",
          "minecraft:cold_ocean",
          "minecraft:lukewarm_ocean",
          "minecraft:warm_ocean",
          "minecraft:deep_frozen_ocean",
          "minecraft:deep_cold_ocean",
          "minecraft:deep_ocean",
          "minecraft:deep_lukewarm_ocean"],
  "caves":
     ["originrealms:underground",
          "originrealms:ice_caves", 
          "minecraft:lush_caves",
          "minecraft:dripstone_caves",
          "originrealms:depths",
          "minecraft:deep_dark",
          "minecraft:deep_lush_caves",
          "minecraft:deep_dripstone_caves"],
  "ice_caves":
     ["originrealms:ice_caves"],
  "dripstone_caves":
     ["minecraft:dripstone_caves"],
  "depths":
     ["originrealms:depths",
          "minecraft:deep_dark",
          "minecraft:deep_lush_caves",
          "minecraft:deep_dripstone_caves"],
  "blighted_badlands":
     ["originrealms:blighted_badlands"]
}

sizeList= {
   "small": {
      "tiny": 20,
      "small": 40,
      "medium": 60,
      "large": 80,
      "huge": 100,
      "giant": 200
   },
   "medium": {
      "tiny": 60,
      "small": 80,
      "medium": 100,
      "large": 200,
      "huge": 300,
      "giant": 400
   },
   "large": {
      "tiny": 100,
      "small": 200,
      "medium": 300,
      "large": 400,
      "huge": 500,
      "giant": 600
   }
}

priceList={20:0,40:4,60:13,80:25,100:45,200:85,300:170,400:300,500:470,600:600}
rarityList={"common":9,"uncommon":50,"rare":170,"epic":425}
sizeOdds={"tiny":14,"small":22,"medium":24,"large":14,"huge":14,"giant":8}
rarityOdds={"common":57,"uncommon":30,"rare":10,"epic":3}
fishTypes={'Cod': {'biomes': ['lush', 'boreal', 'arid', 'arctic', 'tropical'], 'model': 'small', 'rarity': 'common'}, 'Bass': {'biomes': ['lush', 'boreal', 'arid', 'arctic', 'tropical'], 'model': 'medium', 'rarity': 'common'}, 'Salmon': {'biomes': ['lush', 'boreal', 'arctic'], 'model': 'medium', 'rarity': 'uncommon'}, 'Catfish': {'biomes': ['lush'], 'model': 'large', 'rarity': 'rare'}, 'Bluegill': {'biomes': ['lush'], 'model': 'small', 'rarity': 'common'}, 'Yellow Perch': {'biomes': ['lush'], 'model': 'small', 'rarity': 'uncommon'}, 'Goby': {'biomes': ['lush', 'boreal', 'tropical', 'caves'], 'model': 'small', 'rarity': 'common'}, 'Gar': {'biomes': ['lush', 'arid', 'tropical'], 'model': 'large', 'rarity': 'rare'}, 'Rainbow Trout': {'biomes': ['boreal'], 'model': 'medium', 'rarity': 'common'}, 'Sturgeon': {'biomes': ['boreal'], 'model': 'large', 'rarity': 'epic'}, 'Golden Trout': {'biomes': ['boreal'], 'model': 'medium', 'rarity': 'uncommon'}, 'Bitterling': {'biomes': ['boreal', 'arctic'], 'model': 'medium', 'rarity': 'uncommon'}, 'Grayling': {'biomes': ['boreal', 'arctic'], 'model': 'large', 'rarity': 'epic'}, 'Arowana': {'biomes': ['arid'], 'model': 'large', 'rarity': 'epic'}, 'Bonytail Chub': {'biomes': ['arid'], 'model': 'medium', 'rarity': 'common'}, 'Loach': {'biomes': ['arid', 'tropical'], 'model': 'medium', 'rarity': 'common'}, 'Banded Barb': {'biomes': ['arid'], 'model': 'small', 'rarity': 'uncommon'}, 'Goldfish': {'biomes': ['arid', 'tropical'], 'model': 'small', 'rarity': 'uncommon'}, 'Neon Tetra': {'biomes': ['arctic'], 'model': 'small', 'rarity': 'common'}, 'Char': {'biomes': ['arctic'], 'model': 'medium', 'rarity': 'common'}, 'Pike': {'biomes': ['arctic'], 'model': 'large', 'rarity': 'rare'}, 'Betta': {'biomes': ['arctic'], 'model': 'small', 'rarity': 'rare'}, 'Damselfish': {'biomes': ['tropical', 'shoreline'], 'model': 'small', 'rarity': 'common'}, 'Angelfish': {'biomes': ['tropical'], 'model': 'small', 'rarity': 'common'}, 'Piranha': {'biomes': ['tropical'], 'model': 'small', 'rarity': 'uncommon'}, 'Rainbowfish': {'biomes': ['tropical'], 'model': 'small', 'rarity': 'rare'}, 'Mahi Mahi': {'biomes': ['tropical'], 'model': 'large', 'rarity': 'epic'}, 'Clownfish': {'biomes': ['tropical', 'shoreline', 'ocean'], 'model': 'small', 'rarity': 'common'}, 'Seatrout': {'biomes': ['shoreline'], 'model': 'medium', 'rarity': 'common'}, 'Anchovy': {'biomes': ['shoreline'], 'model': 'small', 'rarity': 'common'}, 'Coelacanth': {'biomes': ['shoreline', 'caves'], 'model': 'large', 'rarity': 'epic'}, 'Blue Marlin': {'biomes': ['shoreline'], 'model': 'large', 'rarity': 'rare'}, 'Pufferfish': {'biomes': ['shoreline', 'ocean'], 'model': 'small', 'rarity': 'uncommon'}, 'Tuna': {'biomes': ['shoreline', 'ocean'], 'model': 'medium', 'rarity': 'uncommon'}, 'Butterflyfish': {'biomes': ['shoreline', 'ocean'], 'model': 'small', 'rarity': 'common'}, 'Red Snapper': {'biomes': ['shoreline', 'ocean'], 'model': 'medium', 'rarity': 'uncommon'}, 'Turkeyfish': {'biomes': ['ocean'], 'model': 'small', 'rarity': 'rare'}, 'Surgeonfish': {'biomes': ['ocean'], 'model': 'small', 'rarity': 'uncommon'}, 'Oarfish': {'biomes': ['ocean'], 'model': 'large', 'rarity': 'epic'}, 'Napoleonfish': {'biomes': ['ocean'], 'model': 'large', 'rarity': 'rare'}, 'Ocean Sunfish': {'biomes': ['ocean'], 'model': 'large', 'rarity': 'epic'}, 'Anglerfish': {'biomes': ['ocean', 'caves'], 'model': 'medium', 'rarity': 'rare'}, 'Blobfish': {'biomes': ['ocean', 'caves'], 'model': 'medium', 'rarity': 'rare'}, 'Moss Feeder': {'biomes': ['caves'], 'model': 'small', 'rarity': 'common'}, 'Lanternfish': {'biomes': ['caves'], 'model': 'small', 'rarity': 'common'}, 'Barreleye': {'biomes': ['caves'], 'model': 'medium', 'rarity': 'rare'}, 'Blindcat': {'biomes': ['caves'], 'model': 'medium', 'rarity': 'uncommon'}, 'Glintail': {'biomes': ['ice_caves'], 'model': 'large', 'rarity': 'epic'}, 'Boneshark': {'biomes': ['dripstone_caves'], 'model': 'large', 'rarity': 'epic'}, 'Echoliath': {'biomes': ['depths'], 'model': 'large', 'rarity': 'epic'}, 'Besmirch': {'biomes': ['blighted_badlands'], 'model': 'large', 'rarity': 'epic'}}
modaltext="hi"