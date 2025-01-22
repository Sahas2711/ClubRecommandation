import pandas as pd
import streamlit as st

st.set_page_config(page_title="Club Recommendation System", layout="wide")

# Header Section
st.markdown("<h1 style='text-align: center;'>Club Recommendation System</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>Discover the best clubs tailored to your skills and interests.</p>",
    unsafe_allow_html=True)

# Load Datasets
club_skills_df = pd.read_excel('Dataset/Club_Skills_Dataset_Extended.xlsx')
ratings_df = pd.read_excel('Dataset/Ratings_dataset.xlsx')

# Preprocess Data
club_skills_df.columns = club_skills_df.columns.str.strip()
ratings_df.columns = ratings_df.columns.str.strip()
club_skills_df.rename(columns={'Club': 'Club Name'}, inplace=True)
ratings_df.rename(columns={'Club Name': 'Club Name'}, inplace=True)

# Merge Datasets
merged_df = pd.merge(club_skills_df, ratings_df, on='Club Name', how='inner')


def recommend_clubs(skill, top_n=5):
    """
    Recommend top clubs based on a specific skill, sorted by their rating.
    """
    clubs_with_skill = merged_df[merged_df['Skill'] == skill]

    if clubs_with_skill.empty:
        return pd.DataFrame()

    top_clubs = clubs_with_skill[['Club Name', 'image_url', 'Rating']].drop_duplicates().sort_values(
        by='Rating', ascending=False
    ).head(top_n)

    return top_clubs


# Skill Selection and Button
skills = merged_df['Skill'].unique().tolist()

st.write("")  # Adds spacing
col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    skill = st.selectbox("Select a skill:", skills, help="Choose a skill to get club recommendations.")
    st.markdown("<br>", unsafe_allow_html=True)  # Adds space below input box

    # Updated button style with proper padding and font size
    button_style = """
        <style>
            div.stButton > button {
                width: 200px;
                height: 40px;
                font-size: 14px;
                font-weight: bold;
                padding: 5px;
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                text-align: center;
                cursor: pointer;
            }
            div.stButton > button:hover {
                background-color: #45a049;
            }
        </style>
    """
    st.markdown(button_style, unsafe_allow_html=True)

    # Button aligned below input
    if st.button("Get Recommendations"):
        recommended_clubs_info = recommend_clubs(skill)

        if recommended_clubs_info.empty:
            st.warning(f"No clubs found with the skill '{skill}'.")
        else:
            st.subheader(f"Top Clubs for the skill '{skill}':")

            # Display recommendations in a dynamic grid
            num_clubs = len(recommended_clubs_info)
            cols = st.columns(num_clubs)  # Adjusts the number of columns dynamically

            for i, (_, row) in enumerate(recommended_clubs_info.iterrows()):
                with cols[i]:
                    st.markdown(
                        f"""
                        <div style="
                            text-align: center;
                            padding: 10px; 
                            border: 1px solid #444;
                            border-radius: 10px;
                            background-color: #000;
                            color: #fff;">
                            <h4 style="color: #00e6e6; margin-bottom: 10px;">{row['Club Name']}</h4>
                            <img src="{row['image_url']}" 
                                 style="width:150px; height:150px; object-fit:cover; border-radius:10px;" 
                                 alt="Club Image">
                            <p style="font-size: 14px; margin-top: 10px;"> Rating: {row['Rating']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

# Footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>© 2024 Club Elite</p>", unsafe_allow_html=True)
