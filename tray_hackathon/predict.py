import pandas as pd
import joblib

model_path = 'model/tray_minmax_kmeans_pipeline.joblib'

def predict(analyst_v, partner_v, persona_v, organic_search, seo):
    df = pd.DataFrame({1:[analyst_v],
                       2:[partner_v],
                       3:[persona_v],
                       4:[organic_search],
                       5:[seo]
                       })
    model = joblib.load(model_path)
    cluster = model.predict(df)
    return cluster[0]
