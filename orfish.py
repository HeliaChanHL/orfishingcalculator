import streamlit as st
import orfishTab1
import orfishTab2

# Title of the app
st.title('OR Fishing Calculator')
st.write("OR-Finishes Web Application")
st.write("Ever need to find the least amouont of biomes to visit to get all the fish you need? What about income from fishing? Here's the tool for you!")
custom_css = """
<style>
.st-emotion-cache-zh2fnc { /* stElementContainer */
  width: 100%;
  max-width: 100%;  
}
</style>
"""
st.markdown('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">', unsafe_allow_html=True)
st.markdown(custom_css, unsafe_allow_html=True)

if 'calc' not in st.session_state:
    st.session_state.calc = True
if 'buttonText' not in st.session_state:
    st.session_state.buttonText = "Fishing Calculator"
    st.session_state.buttonDis = True
# Function to set the active tab
def set_active_tab():
    st.session_state.calc = not st.session_state.calc
    if st.session_state.calc==True:
        st.session_state.buttonText="Results"
    else:
        st.session_state.buttonText = "Fishing Calculator"

# Function to show the dialog with crop information
@st.dialog("How to Use the OR Fishing Calculator")
def showFishDialog():
    orfishTab1.modalContent() 

# Create columns for buttons
col1, col2 = st.columns(2)

with col1:
    st.button(st.session_state.buttonText, on_click=set_active_tab,disabled=st.session_state.buttonDis)
with col2:
    if st.button("How to Use"):
        showFishDialog()  # Call the dialog function

# Display content based on the active tab
if st.session_state.calc:
    orfishTab1.formUI()
else:
    if 'selected_biome' not in st.session_state:
        if 'minBiomesFound' not in st.session_state:
            st.session_state.buttonDis=True
        elif "inputs" not in st.session_state:
            st.session_state.buttonDis=True
        elif "bestBiomeMapping" not in st.session_state:
            st.warning("No valid combination found.")
            st.session_state.buttonDis=True
        else:
            if st.session_state.buttonDis:
                st.session_state.buttonDis=False
                st.rerun()
            orfishTab2.display()
    else:
        if st.session_state.buttonDis:
            st.session_state.buttonDis=False
            st.rerun()
        orfishTab2.display()

st.write("")
st.write("")
st.write("")
st.markdown("""
---
""")
footer_container = st.container()
with footer_container:
    col1, col2, col3 = st.columns((3, 2, 1))
    
    with col1:
        with col1:
         st.markdown("""
            <style>
                .kofi-button {
                    display: inline-block;
                    background-color: #FFDBBB;
                    color: #e55300;
                    width: 100%;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    border: 2px solid #e55300;
                    border-radius: 5px;
                    font-size: 16px;
                    font-family: Arial, sans-serif;
                    transition: background-color 0.3s, color 0.3s;
                }

                .kofi-button:hover {
                    background-color: #FF5C00;
                    color: white;
                    border: 2px solid #FFDBBB;
                }
            </style>
            <a href="https://ko-fi.com/mcswagical">
                <button target="_blank" class="kofi-button">
                    <i class="fa fa-coffee"></i> Built by McSwagical (ko-fi) <i class="fa fa-coffee"></i>
                </button>
            </a>
                    
        """, unsafe_allow_html=True)
    
        st.write("Fish Assets by itsMarkiS")
    
    with col2:
        st.write("Copyright © Amelia Freeman")
    
    with col3:
        st.markdown("""
            <style>
                .discord-button {
                    display: inline-block;
                    background-color: #5865F2;
                    color: white;
                    padding: 10px 20px;
                    text-align: center;
                    text-decoration: none;
                    border: 2px solid #111978;
                    border-radius: 5px;
                    font-size: 14px;
                    font-family: Arial, sans-serif;
                    transition: background-color 0.3s;
                }
                .discord-button:hover {
                    background-color: #3E20C4;  /* Change this to your desired hover color */
                }
            </style>
            <a href="https://discord.gg/or-finishes">
                <button target="_blank" class="discord-button">
                    <i class='fa-brands fa-discord'></i> <b>ORF</b>
                </button>
            </a>
                    

        """, unsafe_allow_html=True)
