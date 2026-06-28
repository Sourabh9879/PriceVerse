import streamlit as st
from extractor import extract_page_text
from gem_extractor import extract_product_name
from search_api import search_product

st.set_page_config(
    page_title="PriceVerse",
    layout="wide"
)

st.title("PriceVerse")

st.write("Find the cheapest price across different stores.")

url = st.text_input(
    "Enter Product URL",
    placeholder="https://www.amazon.in/..."
)

if st.button("Search"):

    if url == "":

        st.warning("Please enter a product URL.")

    else:

        with st.spinner("Extracting Product..."):

            page_text = extract_page_text(url)

            product_name = extract_product_name(page_text)

        st.success("Product identified successfully!")

        st.subheader("Product Name")

        st.write(product_name)

        with st.spinner("Searching prices..."):

            products = search_product(product_name)

        st.subheader("Top 5 Lowest Prices")

        if len(products) == 0:

            st.error("No products found.")

        else:

            for i, product in enumerate(products, start=1):

                col1, col2 = st.columns([1, 4])

                with col1:

                    if product["thumbnail"]:

                        st.image(product["thumbnail"], width=120)

                with col2:

                    st.markdown(f"### {i}. {product['store']}")

                    st.write(product["title"])

                    st.success(product["price"])

                    if product["link"]:

                        st.link_button(
                            "Open Product",
                            product["link"]
                        )

                st.divider()