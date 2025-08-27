from fishingData import *
import streamlit as st
from os import path

def modalContent():
    st.link_button("See ORFinishes Fish List Here", 
               "https://docs.google.com/spreadsheets/d/1ckMvE1eoS5tl_gy2Jk7AZ94J-pN-3OCmvMz9DwqlSro/edit?gid=1659613960#gid=1659613960", 
               icon="🐟")
    st.markdown(modaltext)

def formUI():
    
    st.header("Select Fish:")
    st.markdown("---")
    # Initialize session state for tab count and inputs
    if 'tab_count' not in st.session_state:
        st.session_state.tab_count = 1
        st.session_state.inputs = {
            f'Fish {i + 1}': {
                'Fish': "Select a Fish",  # Default to "Select a Fish"
                'Size': ["Select a Size"],
                'Amount': [1],
                'InputGroup': 1 
            } for i in range(st.session_state.tab_count)
        }

    def add_tab():
        new_tab_name = f'Fish {st.session_state.tab_count + 1}'
        st.session_state.tab_count += 1
        st.session_state.inputs[new_tab_name] = {
            'Fish': "Select a Fish",
            'Size': ["Select a Size"],
            'Amount': [1],
            'InputGroup': 1 
        }
    def delete_tab(tab):
        del st.session_state.inputs[tab]
        st.rerun()
    def add_All():
        st.session_state.inputs={}
        st.session_state.tab_count=0
        for i in list(fishTypes.keys()):
            st.session_state.tab_count += 1
            new_tab_name = f'Fish {st.session_state.tab_count }'
            st.session_state.inputs[new_tab_name] = {
                'Fish': i,
                'Size': ["Giant"],
                'Amount': [1],
                'InputGroup': 1 
        }
    def fishPNG(selected_fish):
        if selected_fish == "Select a Fish":
            return
        image_path = f"fish_renders/{selected_fish.replace(' ', '_').lower()}.png"
        if path.isfile(image_path):
            st.image(image_path, caption=selected_fish, width=200)
            if current_fish != selected_fish:
                st.rerun()
        else:
            st.error(f"Image for {selected_fish} not found.")
    col1,col2=st.columns([3,1])
    with col1:
        if st.button("Add a Fish"):
            add_tab()
    with col2:
        if st.button("Add all Giant Fish Types"):
            add_All()
    if st.session_state.inputs!={}:
        fishTabs = [f"{key}: {value['Fish']}" if value["Fish"] != "Select a Fish" else key for key, value in st.session_state.inputs.items()]
        selected_tab = st.tabs(fishTabs)
        for i, tab in enumerate(fishTabs):
            with selected_tab[i]:
                tab=tab.split(":")[0]
                current_fish = st.session_state.inputs[tab]['Fish']
                
                # Gather all selected fish from previous tabs
                selected_fish_set = {st.session_state.inputs[t.split(":")[0]]['Fish'] for t in fishTabs if t.split(":")[0] != tab}
                fish_list = [' '.join(word.capitalize() for word in fish.replace('_', ' ').split()) for fish in fishTypes.keys()]
                filtered_fish_list = ["Select a Fish"] + sorted([fish for fish in fish_list if fish not in selected_fish_set])

                col1, col2 = st.columns([2, 1])

                with col1:
                    # Ensure the current fish is valid
                    if current_fish not in filtered_fish_list:
                        current_fish = filtered_fish_list[0]

                    # Select box for choosing fish type
                    selected_fish = st.selectbox(
                        f'Fish Type for Fish {i + 1}',
                        filtered_fish_list,
                        index=filtered_fish_list.index(current_fish),
                        key=f'fish_{tab}_{i}'
                    )

                    # Update session state with selected fish
                    if selected_fish != "Select a Fish":
                        st.session_state.inputs[tab]['Fish'] = selected_fish
                        if st.button("Add New Size", key=f'add_size_{tab}_{i}'):
                            st.session_state.inputs[tab]['InputGroup'] += 1
                            st.session_state.inputs[tab]['Size'].append("Select a Size")
                            st.session_state.inputs[tab]['Amount'].append(1)
                            st.rerun()

                        selectFishDetails(tab,i)
                with col2:
                    fishPNG(selected_fish)
                    if st.button("🗑️ Delete", key=f"delete_{tab}"):
                        delete_tab(tab)
        st.button('Submit', on_click=calc)
        st.markdown("---")
        if st.session_state.get("selected_biome"):
            del st.session_state['selected_biome']
        biome_options = ["Select a Biome"]+[' '.join(word.capitalize() for word in item.split("_")) for item in spawn_group_fish.keys()]
        selected_biome = st.selectbox("View Fish found in Biome:", biome_options)
        if selected_biome and selected_biome!="Select a Biome":
            st.session_state.selected_biome = selected_biome
            st.session_state.calc = False
            st.rerun()
    else:
        st.warning("Please select at least one fish.")
        st.session_state.tab_count=0
        st.session_state.inputs={}

def selectFishDetails(tab,i):
    for j in range(st.session_state.inputs[tab]['InputGroup']):
        with st.container(border=True):
            current_size = st.session_state.inputs[tab]['Size'][j]
            selected_size_set = {st.session_state.inputs[tab]['Size'][x] for x in range(len(st.session_state.inputs[tab]['Size'])) if x != j}
            size_list = [size.capitalize() for size in sizeOdds.keys()]
            filtered_size_list = ["Select a Size"] + [
                f"{size} ({sizeList[fishTypes[st.session_state.inputs[tab]['Fish']]['model']][size.lower()]} cm)"
                for size in size_list if size not in selected_size_set
            ]
            if current_size not in filtered_size_list:  
                current_size = filtered_size_list[0]
            selected_size = st.selectbox(
                f"Size for {st.session_state.inputs[tab]['Fish']} {j + 1}:",
                filtered_size_list,
                index=filtered_size_list.index(current_size), 
                key=f'size_{tab}_{j}_{i}'  
            )

            st.session_state.inputs[tab]['Size'][j] = selected_size

            current_amount = st.session_state.inputs[tab]["Amount"][j]
            amount = st.number_input(
                f'Amount for {st.session_state.inputs[tab]["Fish"]} {j+1}:',
                min_value=1,
                value=current_amount,
                key=f'amount_{tab}_{j}_{i}'
            )
            st.session_state.inputs[tab]['Amount'][j]=amount
def calc():
    keys_to_remove = []
    for key, value in st.session_state.inputs.items():
        if value["Fish"] == "Select a Fish" or set(value["Size"])=={"Select a Size"}:
            keys_to_remove.append(key)
        else:
            for i in range(len(value["Size"])):
                if value["Size"][i] == "Select a Size":
                    value["Size"].pop(i)
                    value["Amount"].pop(i)
            value["InputGroup"]=len(value["Size"])
    for key in keys_to_remove:
        del st.session_state.inputs[key]
    st.session_state.tab_count=len(st.session_state.inputs)
    if st.session_state.inputs:
        minBiomesFound = float('inf')
        bestBiomeMapping = None
        
        fishList = list({item["Fish"] for item in st.session_state.inputs.values() if "Fish" in item})
        minBiomesFound, bestBiomeMapping = findBestCombination(fishList, 0, {}, set(), minBiomesFound, bestBiomeMapping)
        if bestBiomeMapping:
            st.session_state.minBiomesFound = minBiomesFound
            st.session_state.bestBiomeMapping = bestBiomeMapping
            st.session_state.calc = False

def findBestCombination(fishList, index, biomeMap, addedFish, minBiomesFound, bestBiomeMapping):
    # Base case: if index exceeds fishList length, check biomes count
    if index == len(fishList):
        if len(biomeMap) < minBiomesFound:
            return len(biomeMap), biomeMap.copy()  # Return a copy to avoid mutation
        return minBiomesFound, bestBiomeMapping  # Ensure to return the current best mapping

    # Get the current fish type
    currentFish = fishList[index]
    if currentFish!=None:
        biomesToConsider = biomesToConsiderFormat(fishTypes[currentFish]["biomes"], biomeMap)

        for biome in biomesToConsider:
            tempBiomeMap = updateBiomeMap(biome, biomeMap)
            if currentFish not in addedFish:
                if biome not in tempBiomeMap:
                    tempBiomeMap[biome] = [currentFish]
                elif currentFish not in tempBiomeMap[biome]:
                    tempBiomeMap[biome].append(currentFish)

                addedFish.add(currentFish)  # Mark this fish as added
                # Recursive call to explore the next fish
                minBiomesFound, bestBiomeMapping = findBestCombination(
                    fishList, index + 1, tempBiomeMap, addedFish, minBiomesFound, bestBiomeMapping
                )
                addedFish.remove(currentFish)  # Backtrack: remove the fish after the recursion

    return minBiomesFound, bestBiomeMapping  # Ensure to return the best found mapping


def biomesToConsiderFormat(biomesToConsider, biomeMap):
    if "blighted_badlands" in biomeMap and "arid" in biomesToConsider:
        return [b for b in biomesToConsider if b != "arid"] + ["blighted_badlands"]
    elif "caves" in biomesToConsider:
        if "ice_caves" in biomeMap:
            return [b for b in biomesToConsider if b != "caves"] + ["ice_caves"]
        if "dripstone_caves" in biomeMap:
            return [b for b in biomesToConsider if b != "caves"] + ["dripstone_caves"]
        if "depths" in biomeMap:
            return [b for b in biomesToConsider if b != "caves"] + ["depths"]

    return biomesToConsider

def updateBiomeMap(biome, biomeMap):
    tempBiomeMap = biomeMap.copy() 
    
    if biome in ["ice_caves", "dripstone_caves", "depths"] and "caves" in biomeMap:
        tempBiomeMap[biome] = biomeMap["caves"]
        del tempBiomeMap["caves"]
        
    elif biome == "blighted_badlands" and "arid" in biomeMap:
        tempBiomeMap[biome] = biomeMap["arid"]
        del tempBiomeMap["arid"]
    
    return tempBiomeMap