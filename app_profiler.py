import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Human Language Technologist Profile Page")

# Collect basic information
name = "Remo Motsuenyane"
field = "Human Language Technology"
institution = "North-West University"

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

st.image(
    "https://i.pinimg.com/736x/c9/a5/df/c9a5dfe5dca850387fb97c83e3f2c22c.jpg",
    caption="Polygot (Pinterest)"
)

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add STEM Data Section
st.header("Explore South African Language Data")

# Generate dummy data = zulu, tswana, venda
zulu_data = pd.read_csv("zulu_data.csv", encoding="utf-8", nrows=20, usecols=["text","lemma", "pos", "upos"])
tswana_data = pd.read_csv("tswana_data.csv", encoding="utf-8", nrows=20, usecols=["text","lemma", "pos", "upos"])
venda_data = pd.read_csv("venda_data.csv", encoding="utf-8", nrows=20, usecols=["text","lemma", "pos", "upos"])

# Tabbed view for language data
st.subheader("SA Language Data Viewer")
data_option = st.selectbox(
    "Choose a dataset to explore", 
    ["isiZulu Data", "Setswana Data", "Tshivenda Data"]
)

if data_option == "isiZulu Data":
    st.write("### isiZulu Linguistic Data")
    st.dataframe(zulu_data)
    # Add widget to filter by UPOS columns
    upos_list = zulu_data["upos"].unique().tolist()
    selected_upos = st.multiselect(
        "Select UPOS Tags to view:", 
        options=upos_list, 
        default=upos_list
    )
    filtered_df = zulu_data[zulu_data["upos"].isin(selected_upos)]
    st.write(f"Displaying {len(filtered_df)} tokens matching selected tags.")
    st.dataframe(filtered_df)
    
elif data_option == "Setswana Data":
    st.write("### Setswana Linguistic Data")
    st.dataframe(tswana_data)
    # Add widget to filter by UPOS columns
    upos_list = tswana_data["upos"].unique().tolist()
    selected_upos = st.multiselect(
        "Select UPOS Tags to view:", 
        options=upos_list, 
        default=upos_list
    )
    filtered_df = tswana_data[tswana_data["upos"].isin(selected_upos)]
    st.write(f"Displaying {len(filtered_df)} tokens matching selected tags.")
    st.dataframe(filtered_df)

elif data_option == "Tshivenda Data":
    st.write("### Tshivenda Linguistic Data")
    st.dataframe(venda_data)
    # Add widget to filter by UPOS columns
    upos_list = venda_data["upos"].unique().tolist()
    selected_upos = st.multiselect(
        "Select UPOS Tags to view:", 
        options=upos_list, 
        default=upos_list
    )
    filtered_df = venda_data[venda_data["upos"].isin(selected_upos)]
    st.write(f"Displaying {len(filtered_df)} tokens matching selected tags.")
    st.dataframe(filtered_df)

# Add a contact section
st.header("Contact Information")
email = "rkmotsuenyane@gmail.com"
st.write(f"You can reach {name} at {email}.")