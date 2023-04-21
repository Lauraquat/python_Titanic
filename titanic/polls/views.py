from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from django import forms
import requests

class ContactForm(forms.Form):
    age = forms.CharField(label='Age *', max_length=100, required = True)
    GENDER_CHOICES = [(0, 'Homme'), (1, 'Femme')]
    sexe = forms.CharField(label='Sexe *',  max_length=100, widget=forms.Select(choices= GENDER_CHOICES), required = True)
    EMBARQUEMENT_CHOICES = [('0', 'Southampton'), ('1', 'Cherbourg'), ('2', 'Queenstown')]
    embarquement = forms.CharField(label='Lieu d\'embarquement *', widget=forms.Select(choices=EMBARQUEMENT_CHOICES), max_length=100, required = True)
    CLASSE_CHOICES = [(1, 'Première classe'), (2, 'Deuxième classe'), (3, 'Troisième classe')]
    classe = forms.CharField(label='Classe * ', max_length=100,widget=forms.Select(choices=CLASSE_CHOICES), required = True)
    # widget=forms.Textarea)

def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            age = form.cleaned_data['age']
            embarquement = form.cleaned_data['embarquement']
            sexe = form.cleaned_data['sexe']
            classe = form.cleaned_data['classe']
            tarif = 0
            # On définit un tarif moyen pour chaque classe
            if( classe == '1'):
                tarif = 84.15
            elif( classe == '2'):
                tarif = 20.66
            elif( classe == '3'):
                tarif = 13.67

            # Envoyer les données à l'API FastAPI
            data = {'age': age, 'embarquement': embarquement, 'sexe': sexe, 'classe': classe, 'tarif': tarif }
            response = requests.post('http://127.0.0.1:8001/predict?age='+age+'&embarquement='+embarquement+'&sexe='+sexe+'&classe='+classe+'&tarif='+str(tarif), json=data)
            print(response.json())
            
            prediction = response.json()
            # Vérifier la réponse de l'API

    return render(request, 'index.html', {'form': form, 'prediction': prediction})

        



