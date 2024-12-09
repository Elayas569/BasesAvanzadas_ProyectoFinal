from postgres_db import connect_postgres
from mongo_db import connect_mongo
from utils import get_players, update_player, get_matches, update_match, get_goals, get_cards, add_goal
from pprint import pprint

def main():
    postgres_conn = connect_postgres()
    mongo_db = connect_mongo()

    while True:
        print("1. Consultar jugadores (PostgreSQL)")
        print("2. Actualizar jugador (PostgreSQL)")
        print("3. Consultar partidos (MongoDB)")
        print("4. Actualizar partido (MongoDB)")
        print("5. Consultar goles (MongoDB)")
        print("6. Consultar tarjetas (MongoDB)")
        print("7. Salir")

        choice = input("Selecciona una opción: ")

        if choice == '1':
            players = get_players(postgres_conn)
            for player in players:
                print(player)

        elif choice == '2':
            player_id = input("Ingresa el ID del jugador a actualizar: ")
            new_name = input("Ingresa el nuevo nombre: ")
            update_player(postgres_conn, player_id, new_name)
            print("Jugador actualizado.")

        elif choice == '3':
            matches = get_matches(mongo_db)
            if matches:
                for match in matches:
                    pprint(match)  # Imprime el documento completo de manera legible
            else:
                print("No se encontraron partidos.")

        elif choice == '4':
            match_id = input("Ingresa el ID del partido a actualizar (ej. M001): ")
            new_data = {}

            # Modificar nombres de los equipos
            new_team1 = input("Ingresa el nuevo nombre del equipo 1: ")
            new_team2 = input("Ingresa el nuevo nombre del equipo 2: ")
            new_data["equipo_1"] = new_team1  # Asegúrate de usar "equipo_1"
            new_data["equipo_2"] = new_team2  # Asegúrate de usar "equipo_2"

            update_match(mongo_db, match_id, new_data)
            print("Nombres de los equipos actualizados.")

        elif choice == '5':
            goals = get_goals(mongo_db)
            if goals:
                for goal in goals:
                    pprint(goal)  # Imprime el documento completo de manera legible
            else:
                print("No se encontraron goles.")

        elif choice == '6':
            cards = get_cards(mongo_db)
            if cards:
                for card in cards:
                    pprint(card)  # Imprime el documento completo de manera legible
            else:
                print("No se encontraron tarjetas.")

        elif choice == '7':
            break

        else:
            print("Opción no válida.")

    postgres_conn.close()

if __name__ == "__main__":
    main()