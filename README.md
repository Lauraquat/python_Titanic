# python_Titanic

- Lancer le site :  cd titanic
                    python3.9 manage.py runserver
                    url site : http://127.0.0.1:8000/

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

####################################################################################################################
# Auriez vous survécu au naufrage du Titanic? Les secrets du projet...

Nous avons téléchargé les données concernant les passagers du Titanic, leur âge, leur classe, la localisation de leur cabine, etc.

Grâce à Jupyter notebook, nous avons pu réaliser des statistiques et conserver les données qui nous semblaient cohérentes pour analyser les chances de survie des passagers.

Après avoir effectué des tests et un apprentissage, nous avons généré un modèle de données qui nous a permis de calculer les chances de survie d’un passager en fonction des informations que nous transmettons.

Ainsi, avec l’API fastApi, dans le fichier main.py, nous avons généré la prédiction via pandas.
Nous la retournons ensuite vers le front (Django) en la formatant au préalable.

Django nécessite une arborescence spécifique :

- Le premier répertoire /titanic est le contenant du projet

Dans ce répertoire nous avons créé le fichier [manage.py](http://manage.py) qui permet d’interagir avec Django.

- Un sous répertoire /titanic à été créé dans lequel se trouvent tous les paquets Python .
- Le sous répertoire /polls contient tous les éléments pour l’affichage et la récupération des données.

Nous y trouvons entre autre le style qui se trouve dans le dossier /static.

De plus à la racine de /polls nous avons le fichier [views.py](http://views.py) dans lequel nous effectuons l’envoi et la récupération de données vers fastApi.

- Dans le dossier /templates se trouvent notre page index.html qui contient notre vue principale ainsi que notre formulaire de requête à l’api.

####################################################################################################################