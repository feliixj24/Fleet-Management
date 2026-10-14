import psycopg

def open_connection():
    connection = psycopg.connect(
        dbname = "",
        user = "",
        password = "",
        host = "",
        port = ""
    )
    return connection
