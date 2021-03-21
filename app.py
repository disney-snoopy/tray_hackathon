import streamlit as st
from tray_hackathon.predict import predict

# setting wide screen
st.set_page_config(
    page_title="Tray Clustering API",
    page_icon="🦄",
    layout="wide")

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
a2.header('**Tray API Clustering Service**')
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
        if cluster == 8:
            st.success('API integration recommended for future expansion')
        if cluster == 0 or cluster == 1 or cluster == 6 or cluster == 4:
            st.info('API integration recommended following current product protocol') 
        if cluster == 2 or cluster == 3 or cluster == 5 or cluster == 7 or cluster == 9:
            st.error('API integration NOT recommended')

if __name__ == "__main__":
    main()

"""
#
# 
"""
# Methodology
a1, a2, a3, a4 = st.beta_columns((1,1,1,1))
a2.header('Methodology')
a1, a2, a3 = st.beta_columns((1,2,1))
a2.write('''
6 main **SaaS performance indicators** were provided by Tray.io to be analyzed:
> - Analyst Value (0 - 5)
- Partner Value (0 - 5)
- Persona Value (0 - 5)
- Growing market
- Organic Search Volume
- SEO Value (0 - 3)

The objective was to identify which of these features mattered most for determining **SaaS "Unicorn" 🦄 API's** that they would want to integrate into their business package.

We wanted to create a model that *predicts* and potentially *improves* the decision making process. 
To do so we extracted the list of already served API's and combined this with the existing data (resulting in 34 matches) to identify patterns/trends in their API choices.
Below you will find the comparison between the API's in the dataset that are currently being served by Tray against those that are not. 

''')
a2.write('''
### 
''')
a2.image('imgs/serving1.png', use_column_width = True)
a2.image('imgs/serving2.png', use_column_width = True)
a2.write('''
#
We used a **K-mean clusterig model** in order to identify different groups of APIs. 
As seen in the figure directly below, 4 out of 10 clusters have the probability of being already served by Tray above average. Below that image is a breakdown of what features those clusters, and therefore Tray, are targetting.
''')
a2.image('imgs/clustering-probability.png', use_column_width = True)
a2.image('imgs/cluster-breakdown.png', use_column_width = True)

a2.write('''
#
We believe that Tray is missing out on key market potential. We think they can include more products that are well perceived by the market, even if they are not utilised by Tray’s key persona.
A **potential expansion currently not targeted by Tray** would be to introduce SaaS companies into their package that have:
- High analyst value 
- High partner value
- Low persona value
- (Potential High SEO value; not required)
#
This results in a **new product workflow**:
''')
a2.image('imgs/new-product-workflow.png', use_column_width = True)

a1, a2, a3, a4 = st.beta_columns((1,1,1,1))
a2.header('Next Steps')
a1, a2, a3 = st.beta_columns((1,2,1))
a2.write('''
Moving forward Tray could repeat this same procedure with larger SaaS datasets and input new serviced companies as those change over time.
This would allow Tray to have a **dynamic model** that stays updated with new companies.

To improve the model it would be advisable to try and get more information on SaaS companies such as:
- Non-Organic Search Volume
- Non-Organic SEO Value
- Global new user aquisition/singups for SaaS company
- Actual Tray user onboarding for offered services

All this would help create a model that continuously **identifies gaps in the actual market** beyond what Tray is targetting.
''')