from menu.menu import Menu
from data.sql_postgres import DbFleetManagement

def main():
    DbFleetManagement.create_table()
    Menu.menu()

if __name__ == "__main__":
    main()