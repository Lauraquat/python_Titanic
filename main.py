from typing import Union
from fastapi import FastAPI
import pandas as pd
import xgboost as xgb

# On charge le modèle
model2 = xgb.XGBClassifier()
model2.load_model("modelTitanic.json")

# On créé l'application FastAPI
app = FastAPI()

# On créé une route pour faire des prédictions
@app.post("/predict")
def predict(age, embarquement, sexe, classe, tarif):

    # On met les données dans un tableau NumPy
    data = pd.DataFrame([[int(age), int(embarquement), int(sexe), int(classe), float(tarif)]], columns = ["Age", "Embarked", "Sex", "Pclass", "Fare"])
   
    # On génère la prédiction
    prediction = model2.predict_proba(data)
    
    # On retourne la prédiction
    return str(prediction[0][1]*100)[0:4]+ " %"