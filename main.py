from typing import Union
from fastapi import FastAPI
import pandas as pd
import xgboost as xgb

# On charge le modèle
model2 = xgb.XGBClassifier()
model2.load_model("modelTitanic.json")

# On créé l'application FastAPI
app = FastAPI()


if( Pclass == 1):
    Fare == 84.15
elif( Pclass == 2):
    Fare == 20.66
elif( Pclass == 3):
    Fare == 13.67


# On créé une route pour faire des prédictions
@app.get("/predict")
def predict():
    # On met les données dans un tableau NumPy
    data = pd.DataFrame([[Age, Embarked, Sex, Pclass, Fare]], columns = ["Age", "Embarked", "Sex", "Pclass", "Fare"])
   
    # On utilise le DMatrix pour faire la prédiction
    prediction = model2.predict_proba(data)
    print(prediction) 
    
    # On retourne la prédiction sous forme de dictionnaire
    return {"prediction": str(prediction[0])}