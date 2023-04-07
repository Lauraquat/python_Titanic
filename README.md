# python_Titanic

- Lancer le site :  `python ./*nomfichier.py*`


# Jupyter notebook

- Dans le projet, dans le terminal, lancer la commande `jupyter notebook`
- Dans Jupyter, cliquer sur « nouveau » puis sur « Python » pour ouvrir jupyter en édition
- Exécuter CSV : `pd.read_csv('titanic.csv')`




# IA dans jupyter notebook

* colab .research.google.com
* Séparer colonnes verticalement (X => toutes et Y => survie)

## sklearn
* Séparer lignes horizontalement (train et test) (80% train et 20% test) (X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2,)

## XGBoost
* `pip install xgboost`
* `import xgboost as xgb`
* exemple avec ".fit" + model.predict

model = xgbosst()
model.fit(X_train, Y_train)
model.predict(X_test)

export en csv + réimport dans backend pour test un cas précis

datascience how to create classification model using xgboost
