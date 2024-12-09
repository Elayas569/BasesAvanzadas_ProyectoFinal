from pymongo import MongoClient

def connect_mongo():
    try:
        client = MongoClient("mongodb+srv://Elayas:Mayab2017@cluster0.2aceg.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
        db = client["Ordinario"]  # Asegúrate de que "tu_db" sea el nombre correcto de tu base de datos
        return db
    except Exception as e:
        print(f"Error al conectar a MongoDB: {e}")