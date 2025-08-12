import streamlit as st
import orfishTab1
import orfishTab2

# Title of the app
st.title('OR Fishing Calculator')
st.write("OR-Finishes Web Application")
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
    st.button(st.session_state.buttonText, on_click=set_active_tab)
with col2:
    if st.button("How to Use"):
        showFishDialog()  # Call the dialog function

# Display content based on the active tab
if st.session_state.calc:
    orfishTab1.formUI()
else:
    if 'minBiomesFound' not in st.session_state:
        st.warning("Please select at least one fish.")
    elif "bestBiomeMapping" not in st.session_state:
        st.warning("No valid combination found.")
    elif "inputs" not in st.session_state:
        st.warning("Must contain at least one valid input.")
    else:
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
        st.write("Built by McSwagical (contact if issues occur.)")
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
                    border-radius: 5px;
                    font-size: 16px;
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
