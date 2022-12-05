import requests
from bs4 import BeautifulSoup
from csv import DictWriter

# url de depart
category_url = input("Entrer une url:")
page = requests.get(category_url)
if page.status_code == requests.codes.ok:
    soup = BeautifulSoup(page.content, 'html.parser')
    # selectionne l'élément ul contennant les informations titre et prix
    grp_vignette = soup.find('ul', id='vignette-produits')
    prix = []
    titre = []
    for i in grp_vignette.select('li'):
        prix.append(i.get('data-price')[:6])
        # prix.append(i.find('span', attrs={'class':'product_price'}).text),
        titre.append(i.find('h2').text)
        datasuite = prix, titre
        data = {
        'prix': prix,
        'titre': titre,
    }
    # ecrit le résultat dans un fichier
    liste_resultat =[]
    file = open('fiche_prix.txt', 'w', encoding='UTF-8')
    for q, a in zip(titre, prix):
        resultat = ('Le produit {0} est vendu {1} euro.'.format(q, a)+'\n' )
        
        file.write (resultat)
    file.closed
    
   