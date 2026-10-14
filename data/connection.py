import psycopg

def open_connection():
    connection = psycopg.connect(
        dbname = "fleet_management",
        user = "postgres",
        password = "Soyprogramador15_",
        host = "localhost",
        port = 5432
    )
    return connection