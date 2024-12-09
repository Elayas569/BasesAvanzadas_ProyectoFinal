import psycopg2
import urllib.parse

connectionString = "postgresql://SQLOrdinario_owner:7FgoRNxOfMm1@ep-weathered-field-a5ks8222.us-east-2.aws.neon.tech/SQLOrdinario?sslmode=require"

result = urllib.parse.urlparse(connectionString)

# Extraer los componentes
user = result.username
password = result.password
host = result.hostname
dbname = result.path[1:]  # Eliminar la barra inicial
port = result.port if result.port else 5432

def connect_postgres():
    try:
        connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
        return connection
    except Exception as e:
        print(f"Error al conectar a PostgreSQL: {e}")

        