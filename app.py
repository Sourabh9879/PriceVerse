import streamlit as st
from extractor import get_product_name

st.set_page_config(
    page_title="PriceVerse",
)

st.title("PriceVerse")

product_url = st.text_input(
    "Enter Product URL",
    placeholder="https://www.amazon.in/..."
)
if st.button("Search"):
    if product_url:
        with st.spinner("Extracting product information..."):
            try:
                product_name = get_product_name(product_url)

                st.success("Product extracted successfully!")

                st.subheader("Product Name")
                st.write(product_name)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter a product URL.")