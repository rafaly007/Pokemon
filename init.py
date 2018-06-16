import requests
from bs4 import BeautifulSoup
import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",password="admin", database="pokemon_db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS pokemon
(
   id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
   ident VARCHAR(5),
   nom VARCHAR(50),
   types VARCHAR(50),
   total INT,
   hp INT,
   attack INT,
   defense INT,
   sp_atk INT,
   sp_def INT,
   speed INT
);
""")

url = "https://pokemondb.net/pokedex/all"
response = requests.get(url)
html = str(response.content)
soup = BeautifulSoup(html, "html.parser")
tab = soup.find(id="pokedex")
for link in tab.find_all("tr"):
    tt = []
    for l in link.find_all("td"):
        tt.append(l.text)
    # print(tt)
    if not tt:
        print("liste vide")
    else:
        cursor.execute(""" INSERT INTO pokemon(ident, nom, types, total, hp, attack, defense, sp_atk, sp_def, speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tt)


# recuperer les données dans un fichier
# fichier = open("data.html", "w")
# print(fichier.write(html))
# fichier.close()

conn.commit()
conn.close()