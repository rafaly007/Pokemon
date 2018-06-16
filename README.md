# Project Name:
Devoir Pokemon;
C'est de développer une API REST FULL CRUD avec tous les pokemons
Contient les fichiers:
	- README.md
	- init.py
	- api.py
	- .gitignore

# Installation:

# Usage:
Le fichier init.py est utilisé pour recuperer une liste des Pokemon et les insère dans la table pokemon de la base de donné pokemon_db dans mysql.

Le fichier api.py sert à:
Pour consulter et afficher un Pokemon par son id:
Par exemple ici l'id est 1, et on utilise un navigateur ou Postman (en mode GET) pour le faire avec:
http://localhost:8000/allPokemon?id=1

Pour supprimer un pokemon par son idPar exemple id=1; dans postman (en mode DELETE):
http://localhost:8000/delPokemon?id=1

Pour ajouter un nouveau Pokemon avec Postman (en mode POST), par exemple:
http://localhost:8000/Pokemon?ident=001&nom=toto&types=fire&total=200&hp=20&attack=8&defense=9&sp_atk=9&sp_def=9&speed=2

Pour modifier un Pokemon avec Postman (en mode PUT):
http://localhost:8000/updPokemon?id=1&ident=001&nom=toto&types=fire&total=200&hp=20&attack=8&defense=9&sp_atk=9&sp_def=9&speed=2
