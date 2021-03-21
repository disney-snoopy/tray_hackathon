import streamlit as st
from tray_hackathon.predict import predict

# setting wide screen
st.set_page_config(layout="wide")

expander_creators = st.beta_expander("👨‍🦰👨‍🦱Creators of Tray Clustering API👩‍🦱👱‍♂️", expanded=False)
with expander_creators:
    a1, a2, a3, a4, a5 = st.beta_columns((2,1,1,1,2))
    a2.image('https://res.cloudinary.com/dbxctsqiw/image/upload/v1616289193/tray_hackathon/sofia_a0vsic.jpg', use_column_width = True)
    a2.write('Sofia Martins')
    a3.image('https://res.cloudinary.com/dbxctsqiw/image/upload/v1616289193/tray_hackathon/diego_rh4dd4.jpg', use_column_width = True)
    a3.write('Diego Munoz')
    a4.image('https://res.cloudinary.com/dbxctsqiw/image/upload/v1616289193/tray_hackathon/jae_qh0akq.jpg', use_column_width = True)
    a4.write('Jae Kim')

a1, a2, a3, a4 = st.beta_columns((1,1,1,1))
a2.header('Tray API Clustering Service')
a1, a2, a3 = st.beta_columns((1,2,1))
a2.image('imgs/title_img.png', use_column_width = True)

m1, c1, c2, c3, c4, c5, m2 = st.beta_columns((2,1,1,1,1,1,2))

analyst_v = c1.slider('Analyst Value', 0, 5, 1)
partner_v = c2.slider('Partner Value', 0, 5, 1)
persona_v = c3.slider('Persona Value', 0, 5, 1)
seo_v = c4.slider('SEO Value', 0, 3, 1)
organic = c5.slider('Organic Search Volume', 0, 2000, 50)

def main():
    button = c3.button('Run clustering!')
    if button:
        cluster = predict(analyst_v, partner_v, persona_v, organic, seo_v)
        a1, a2, a3, a4, a5, a6, a7 = st.beta_columns((1,1,1,1,1,1,1))
        a4.write(f'This API belongs to cluster **{cluster}**.')

if __name__ == "__main__":
    main()