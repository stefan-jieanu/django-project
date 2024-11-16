from django.shortcuts import render

from .models import Publicatie, Revista

# Create your views here.
def list_reviste(request):
    publicatii = Publicatie.objects.all()
    reviste = Revista.objects.all()

    return render(
        request, template_name='lista_reviste.html',
        context={'publicatii': publicatii, 'reviste': reviste})

def list_reviste_pub(request, pub_name):
    publicatii = Publicatie.objects.all()

    publicatie = Publicatie.objects.get(name=pub_name)
    reviste = Revista.objects.filter(publicatie=publicatie)

    return render(
        request, template_name='lista_reviste.html',
        context={'publicatii': publicatii, 'reviste': reviste})

def revista_detail(request, slug):
    revista = Revista.objects.get(slug=slug)

    return render(
        request, template_name='revista_detalii.html',
        context={'revista': revista}
    )