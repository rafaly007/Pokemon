# filename: api.py
"""A basic (single function) API written using hug"""
import hug
import mysql.connector
import json

# Pour tester hug
# @hug.get('/happy')
# def happy_birthday(name, age:hug.types.number=1):
#     """Says happy birthday to a user"""
#     return "Happy {age} Birthday {name}!".format(**locals())

# Afficher par son id
@hug.get('/allPokemon')
def allPokemon(id):
    conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="pokemon_db")
    cursor = conn.cursor()
    cursor.execute(
        """ select ident, nom, types, total, hp, attack, defense, sp_atk, sp_def, speed from pokemon WHERE id = %s""",
        [id])
    rows = cursor.fetchall()
    # print(rows)
    for row in rows:
        result = '{0} | {1} | {2} | {3} | {4} | {5} | {6} | {7} | {8} | {9}'.format(row[0], row[1], row[2], row[3],
                                                                                    row[4], row[5], row[6], row[7],
                                                                                    row[8], row[9])
    conn.close()
    return json.dumps(result)


# Pour supprimer par son id
@hug.delete('/delPokemon')
def delPokemon(id:int):
    conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="pokemon_db")
    cursor = conn.cursor()
    cursor.execute(""" delete from pokemon WHERE id = %s""", [id])
    print("supprimé")
    conn.commit()
    conn.close()
    return json.dumps("delete")


#Pour insérer un Pokemon
@hug.post('/Pokemon')
def addPokemon(ident, nom, types, total, hp, attack, defense, sp_atk, sp_def, speed):
    conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="pokemon_db")
    cursor = conn.cursor()
    tt = [ident, nom, types, total, hp, attack, defense, sp_atk, sp_def, speed]
    cursor.execute(""" INSERT INTO pokemon(ident, nom, types, total, hp, attack, defense, sp_atk, sp_def, speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", tt)
    conn.commit()
    conn.close()
    return json.dumps(tt)


# Pour faire Mise à jour par son id
@hug.put('/updPokemon')
def updPokemon(id,ident, nom, types, total, hp, attack, defense, sp_atk, sp_def, speed):
    conn = mysql.connector.connect(host="localhost", user="root", password="admin", database="pokemon_db")
    cursor = conn.cursor()
    tt = [id, ident, nom, types, total, hp, attack, defense, sp_atk, sp_def, speed]
    cursor.execute("""
       UPDATE pokemon
       SET ident=%s, nom=%s, types=%s, total=%s, hp=%s, attack=%s, defense=%s, sp_atk=%s, sp_def=%s, speed=%s
       WHERE id=%s
    """, tt)
    conn.commit()
    conn.close()
    return json.dumps(tt)
