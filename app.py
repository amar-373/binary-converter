import streamlit as st

st.set_page_config(page_title="Number System Converter", page_icon="🔢", layout="centered")

st.title("Number System Converter")
st.caption("Digital Electronics Experiential Learning Task (ECE)")
st.divider()

# Input box
num_input = st.text_input("Enter Value:", placeholder="e.g. 1010, 50, A, or 12")

# Dropdown to select base
base_type = st.selectbox(
    "Select Input Base:",
    ["Binary (Base 2)", "Decimal (Base 10)", "Hexadecimal (Base 16)", "Octal (Base 8)"]
)

if st.button("Convert", type="primary"):
    val = num_input.strip()
    if not val:
        st.warning("Please enter a value to convert.")
    else:
        try:
            if "Binary" in base_type:
                dec = int(val, 2)
            elif "Decimal" in base_type:
                dec = int(val, 10)
            elif "Hexadecimal" in base_type:
                dec = int(val, 16)
            elif "Octal" in base_type:
                dec = int(val, 8)

            st.success("Conversion Successful!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Binary (Base 2)", bin(dec)[2:])
                st.metric("Hexadecimal (Base 16)", hex(dec)[2:].upper())
            with col2:
                st.metric("Decimal (Base 10)", str(dec))
                st.metric("Octal (Base 8)", oct(dec)[2:])

        except ValueError:
            st.error(f"Invalid input '{val}' for {base_type}!")

st.divider()

with st.expander("📊 View Reference Conversion Table (0 - 15)"):
    ref_data = {
        "Decimal": [str(i) for i in range(16)],
        "Binary": [bin(i)[2:].zfill(4) for i in range(16)],
        "Hexadecimal": [hex(i)[2:].upper() for i in range(16)],
        "Octal": [oct(i)[2:] for i in range(16)]
    }
    st.table(ref_data)
