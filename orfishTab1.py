from fishingData import *
import streamlit as st

def modalContent():
    st.markdown(modaltext)

def formUI():
    st.header("Select Fish:")
    
    if 'tab_count' not in st.session_state:
        st.session_state.tab_count = 1
        st.session_state.inputs = {
            f'Fish {i + 1}': {
                'Fish': list(fishTypes.keys())[0].capitalize(),
                'Size': list(sizeOdds.keys())[0].capitalize(),
                'Amount': 1  # Default amount
            } for i in range(st.session_state.tab_count)
        }

    def add_tab():
        new_tab_name = f'Fish {st.session_state.tab_count + 1}'
        st.session_state.tab_count += 1
        st.session_state.inputs[new_tab_name] = {
            'Fish': list(fishTypes.keys())[0].capitalize(),
            'Size': list(sizeOdds.keys())[0].capitalize(),
            'Amount': 1  # Default amount
        }

    if st.button('Add a Fish'):
        add_tab()

    tabs = list(st.session_state.inputs.keys())
    selected_tab = st.tabs(tabs)

    for i, tab in enumerate(tabs):
        with selected_tab[i]:
            current_fish = st.session_state.inputs[tab]['Fish']
            fish_list = [' '.join(word.capitalize() for word in fish.replace('_', ' ').split()) for fish in fishTypes.keys()]

            col1, col2, col3 = st.columns(3)
            with col1:
                if current_fish not in fish_list:
                    current_fish = fish_list[0]
                
                selected_fish = st.selectbox(
                    f'Fish Type for Fish {i + 1}',
                    fish_list,
                    index=fish_list.index(current_fish),
                    key=f'fish_{tab}{i}'
                )
                st.session_state.inputs[tab]['Fish'] = selected_fish
            
            with col2:
                current_size = st.session_state.inputs[tab]['Size']
                size_list = [size.capitalize() for size in sizeOdds.keys()]

                if current_size not in size_list:
                    current_size = size_list[0]

                selected_size = st.selectbox(
                    f'Size for Fish {i + 1}',
                    size_list,
                    index=size_list.index(current_size),
                    key=f'size_{tab}{i}'  
                )
                st.session_state.inputs[tab]['Size'] = selected_size
            
            with col3:
                # Initialize the amount from session state
                current_amount = st.session_state.inputs[tab].get('Amount', 1)
                amount = st.number_input('Enter Amount:', min_value=1, value=current_amount, key=f'amount_{tab}{i}')
                st.session_state.inputs[tab]['Amount'] = amount

    # Optionally, add a submit button to handle the input data
    if st.button('Submit (Double Click)'):
        # Process the input data here
        calc()

def calc():
    # Initialize global variables to track the minimum biomes found
    minBiomesFound = float('inf')
    bestBiomeMapping = None

    # Extract fish from session state inputs
    fishList = list({item["Fish"] for item in st.session_state.inputs.values() if "Fish" in item})
    # Find the best combination of biomes
    minBiomesFound, bestBiomeMapping = findBestCombination(fishList, 0, {}, set(), minBiomesFound, bestBiomeMapping)

    # Update session state based on results
    if bestBiomeMapping:
        st.session_state.minBiomesFound = minBiomesFound
        st.session_state.bestBiomeMapping = bestBiomeMapping
        st.session_state.calc = False
    else:
        st.alert("No valid combination found.")

def findBestCombination(fishList, index, biomeMap, addedFish, minBiomesFound, bestBiomeMapping):
    # Base case: if index exceeds fishList length, check biomes count
    if index == len(fishList):
        if len(biomeMap) < minBiomesFound:
            return len(biomeMap), biomeMap.copy()  # Return a copy to avoid mutation
        return minBiomesFound, bestBiomeMapping  # Ensure to return the current best mapping

    # Get the current fish type
    currentFish = fishList[index]
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