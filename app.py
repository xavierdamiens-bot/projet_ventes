import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')
figure2 = px.pie(données, values='qte', names='produit', title='quantité vendue par produit')
figure3 = px.pie(données, values='prix', names='produit', title='chiffre d\'affaires par produit')

figure.write_html('ventes-par-region.html')
print('ventes-par-région.html généré avec succès !')

figure2.write_html('ventes-par-produit.html')
print('ventes-par-produit.html généré avec succès !')

figure3.write_html('chiffre-d-affaires-par-produit.html')
print('chiffre-d-affaires-par-produit.html généré avec succès !')
