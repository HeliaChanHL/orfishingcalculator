import streamlit as st
import pandas as pd
from fishingData import *

def fishperBiome(fishTypes):
    biome_counts = {}
    for attr in fishTypes.values():
        for biome in attr["biomes"]:
            if biome not in biome_counts:
                biome_counts[biome] = 0
            biome_counts[biome] += 1
    return biome_counts

# Calculate biome counts
biome_counts = fishperBiome(fishTypes)

def calcOdds(fish,j):
	fishbiome=0
	rarity = fishTypes[fish["Fish"]]["rarity"]
		
	for biome in st.session_state.bestBiomeMapping.keys():
		if fish["Fish"] in st.session_state.bestBiomeMapping[biome]:
			fishbiome=biome
			break
	return (sizeOdds[fish["Size"][j].lower()] / 100) * rarityOdds[rarity] * (1 /biome_counts[fishbiome])

def calcPrices(fish,j):
    model = fishTypes[fish["Fish"]]["model"]
    size = sizeList[model][fish["Size"][j].lower()]
    return priceList[size]+rarityList[fishTypes[fish["Fish"]]["rarity"]]

def display():
    st.header("Results:")
    st.write(f"Best combination with {st.session_state.minBiomesFound} unique biomes:")

    df_biome_fish = pd.DataFrame(
        st.session_state.bestBiomeMapping.items(),
        columns=["Biome", "Fish"]
    )
    st.dataframe(df_biome_fish)
    with st.expander("Raw Inputs:", expanded=False):
        st.write(st.session_state.inputs)
    st.write("Fish Price List:")

    data = [
        (
            item["Fish"],
            item["Size"][j],
            item["Amount"][j],
            calcPrices(item, j),
            item["Amount"][j] * calcPrices(item, j)
        )
        for item in st.session_state.inputs.values()
        for j in range(len(item["Size"]))
    ]

    df_inputs = pd.DataFrame(data, columns=["Fish", "Size", "Amount", "Price", "Total Price"])
    st.dataframe(df_inputs)
    total_income = df_inputs["Total Price"].sum()
    st.success(f"Total Income from Selling Fish: {total_income} rubies")

    st.write("Fish List:")

    data = [
        (
            item["Fish"],
            fishTypes[item["Fish"]]["biomes"],
            item["Size"][j],
            calcOdds(item,j),
        )
        for item in st.session_state.inputs.values()
        for j in range(len(item["Size"]))
    ]

    df_inputs = pd.DataFrame(data, columns=["Fish", "Biomes", "Size", "Catch Odds % per Fish"])
    st.dataframe(df_inputs)

