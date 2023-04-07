from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.shortcuts import render
from django import forms
import requests

class ContactForm(forms.Form):
    age = forms.CharField(label='Age', max_length=100, required = True)
    EMBARQUEMENT_CHOICES = [('C', 'Cherbourg'), ('Q', 'Queenstown'), ('S', 'Southampton')]
    embarquement = forms.CharField(label='Lieu d\'embarquement', widget=forms.Select(choices=EMBARQUEMENT_CHOICES), max_length=100, required = True)
    GENDER_CHOICES = [(0, 'Homme'), (1, 'Femme')]
    sex = forms.CharField(label='Sex',  max_length=100, widget=forms.Select(choices= GENDER_CHOICES), required = True)
    CLASSE_CHOICES = [(0, 'Première classe'), (1, 'Second class'), (2, 'Troisieme classe')]
    classe = forms.CharField(label='Classe', max_length=100,widget=forms.Select(choices=CLASSE_CHOICES), required = True)
    # widget=forms.Textarea)

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Récupérer les données du formulaire
            age = form.cleaned_data['age']
            embarquement = form.cleaned_data['embarquement']
            sex = form.cleaned_data['sex']
            classe = form.cleaned_data['class']

            # Envoyer les données à l'API FastAPI
            data = {'age': age, 'embarquement': embarquement, 'sex': sex, 'classe': classe  }
            response = requests.post('http://localhost:8000/predict', json=data)

            # Vérifier la réponse de l'API
    else:
        form = ContactForm()

    return render(request, 'index.html', {'form': form})
