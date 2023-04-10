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

    # On définit un tarif moyen pour chaque classe
    if( classe == 1):
        tarif == 84.15
    elif( classe == 2):
        tarif == 20.66
    elif( classe == 3):
        tarif == 13.67

    # On met les données dans un tableau NumPy
    data = pd.DataFrame([[int(age), int(embarquement), int(sexe), int(classe), int(tarif)]], columns = ["Age", "Embarked", "Sex", "Pclass", "Fare"])
   
    # On génère la prédiction
    prediction = model2.predict_proba(data)
    print(prediction) 
    
    # On retourne la prédiction sous forme de dictionnaire
    return {"prediction": str(prediction[0])}