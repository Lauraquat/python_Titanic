# python_Titanic

- Lancer le site :  cd titanic
                    python3.9 manage.py runserver
                    <!-- pour léa -->
                    py manage.py runserver
        
        
- Lancer API : `uvicorn main:app --reload --port 8001`
                url: http://127.0.0.1:8001/docs#/default/predict_predict_post


# Jupyter notebook

- Dans le projet, dans le terminal, lancer la commande `jupyter notebook`
- Dans Jupyter, cliquer sur « nouveau » puis sur « Python » pour ouvrir jupyter en édition
- Exécuter CSV : `pd.read_csv('titanic.csv')`

# Install FastApi
* pip install fastapi
* pip install "uvicorn[standard]"
