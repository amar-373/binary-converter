import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Number System Converter",
    page_icon="🔢",
    layout="centered"
)

# Custom CSS for Modern UI Styling
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
    }
    .stApp {
        background-color: #0f172a;
    }
    h1 {
        color: #38bdf8 !important;
        text-align: center;
        font-weight: 700;
    }
    .sub-title {
        text-align: center;
        color: #94a3b8;
        font-size: 1.1rem;
        margin-bottom: 25px;
    }
    .stButton>button {
        width: 100%;
        background-color: #ef4444;
        color: white;
        font-weight: bold;
        border: none;
        padding: 0.6rem;
        border-radius: 6px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #dc2626;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Header Section
st.title("Number System Converter")
st.markdown("<p class='sub-title'>Digital Electronics Experiential Learning Task (ECE)</p>", unsafe_allow_html=True)
st.divider()

# Session State Initialization for inputs
if "binary" not in st.session_state:
    st.session_state.binary = ""
if "decimal" not in st.session_state:
    st.session_state.decimal = ""
if "hex" not in st.session_state:
    st.session_state.hex = ""
if "octal" not in st.session_state:
    st.session_state.octal = ""

# Callback Functions for Real-Time Conversions
def clear_all():
    st.session_state.binary = ""
    st.session_state.decimal = ""
    st.session_state.hex = ""
    st.session_state.octal = ""

def on_binary_change():
    val = st.session_state.binary_input.strip()
    if not val:
        clear_all()
        return
    try:
        dec = int(val, 2)
        st.session_state.binary = val
        st.session_state.decimal = str(dec)
        st.session_state.hex = hex(dec)[2:].upper()
        st.session_state.octal = oct(dec)[2:]
    except ValueError:
        st.error("Invalid Binary Input! Only digits 0 and 1 are allowed.")

def on_decimal_change():
    val = st.session_state.decimal_input.strip()
    if not val:
        clear_all()
        return
    try:
        dec = int(val, 10)
        if dec < 0:
            st.error("Please enter a positive decimal integer.")
            return
        st.session_state.binary = bin(dec)[2:]
        st.session_state.decimal = val
        st.session_state.hex = hex(dec)[2:].upper()
        st.session_state.octal = oct(dec)[2:]
    except ValueError:
        st.error("Invalid Decimal Input! Only digits 0-9 are allowed.")

def on_hex_change():
    val = st.session_state.hex_input.strip()
    if not val:
        clear_all()
        return
    try:
        dec = int(val, 16)
        st.session_state.binary = bin(dec)[2:]
        st.session_state.decimal = str(dec)
        st.session_state.hex = val.upper()
        st.session_state.octal = oct(dec)[2:]
    except ValueError:
        st.error("Invalid Hexadecimal Input! Allowed: 0-9 and A-F.")

def on_octal_change():
    val = st.session_state.octal_input.strip()
    if not val:
        clear_all()
        return
    try:
        dec = int(val, 8)
        st.session_state.binary = bin(dec)[2:]
        st.session_state.decimal = str(dec)
        st.session_state.hex = hex(dec)[2:].upper()
        st.session_state.octal = val
    except ValueError:
        st.error("Invalid Octal Input! Only digits 0-7 are allowed.")

# Input UI Fields
st.subheader("Interactive Base Conversion")

st.text_input(
    "Binary (Base 2)",
    value=st.session_state.binary,
    key="binary_input",
    on_change=on_binary_change,
    placeholder="e.g., 1010"
)

st.text_input(
    "Decimal (Base 10)",
    value=st.session_state.decimal,
    key="decimal_input",
    on_change=on_decimal_change,
    placeholder="e.g., 10"
)

st.text_input(
    "Hexadecimal (Base 16)",
    value=st.session_state.hex,
    key="hex_input",
    on_change=on_hex_change,
    placeholder="e.g., A"
)

st.text_input(
    "Octal (Base 8)",
    value=st.session_state.octal,
    key="octal_input",
    on_change=on_octal_change,
    placeholder="e.g., 12"
)

st.button("Reset All Fields", on_click=clear_all)

st.divider()

# Reference Table Section
with st.expander("📊 View Reference Conversion Table (0 - 15)"):
    ref_data = {
        "Decimal (Base 10)": [str(i) for i in range(16)],
        "Binary (Base 2)": [bin(i)[2:].zfill(4) for i in range(16)],
        "Hexadecimal (Base 16)": [hex(i)[2:].upper() for i in range(16)],
        "Octal (Base 8)": [oct(i)[2:] for i in range(16)]
    }
    st.table(ref_data)
