def get_players(connection):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM players;")
            return cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener jugadores: {e}")
        return []

def update_player(connection, player_id, new_name):
    try:
        with connection.cursor() as cursor:
            cursor.execute("UPDATE players SET nombre = %s WHERE id = %s;", (new_name, player_id))
            connection.commit()
    except Exception as e:
        print(f"Error al actualizar jugador: {e}")
        connection.rollback()

def get_matches(db):
    try:
        matches = list(db.matches.find({}))
        print(f"Partidos encontrados: {len(matches)}")  # Verifica cuántos partidos se encontraron
        return matches
    except Exception as e:
        print(f"Error al obtener partidos: {e}")
        return []

def update_match(db, match_id, new_data):
    try:
        # Usar el campo "_id" para buscar el partido
        result = db.matches.update_one({"_id": match_id}, {"$set": new_data})
        if result.matched_count == 0:
            print(f"No se encontró el partido con ID: {match_id}")
        else:
            print("Partido actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar partido: {e}")

def get_goals(db):
    try:
        goals = list(db.goals.find({}))  # Asegúrate de que la colección se llame "goals"
        print(f"Goles encontrados: {len(goals)}")  # Verifica cuántos goles se encontraron
        return goals
    except Exception as e:
        print(f"Error al obtener goles: {e}")
        return []

def get_cards(db):
    try:
        cards = list(db.cards.find({}))  # Asegúrate de que la colección se llame "cards"
        print(f"Tarjetas encontradas: {len(cards)}")  # Verifica cuántas tarjetas se encontraron
        return cards
    except Exception as e:
        print(f"Error al obtener tarjetas: {e}")
        return []

def add_goal(db, goal_data):
    try:
        db.goals.insert_one(goal_data)  # Inserta el nuevo gol en la colección "goals"
        print("Gol agregado exitosamente.")
    except Exception as e:
        print(f"Error al agregar gol: {e}")