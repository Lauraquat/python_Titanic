from typing import Union
from fastapi import FastAPI
import pandas as pd
import xgboost as xgb
import numpy as np

# On charge le modèle
model2 = xgb.XGBClassifier()
model2.load_model("modelTitanic.json")

# On créé l'application FastAPI
app = FastAPI()

# On créé une route pour faire des prédictions
@app.get("/predict")
def predict():
    # On met les données dans un tableau NumPy
    data = pd.DataFrame([[36, 2, 1, 2, 17]], columns = ["Age", "Embarked", "Sex", "Pclass", "Fare"])
    # On créé un DMatrix à partir de vos données 
    dmatrix = xgb.DMatrix(data)
    # On utilise le DMatrix pour faire la prédiction
    prediction = model2.predict_proba(data)
    print(prediction) 
    
    # On retourne la prédiction sous forme de dictionnaire
    return {"prediction": str(prediction[0])}