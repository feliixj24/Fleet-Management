from coordinator.fleet_coordinator import FleetManagenment


class Menu:

    def menu():
        fleet = FleetManagenment()

        while True:
            print("==========================")
            print("======FLEET MANAGER======")
            print("==========================")
            print("1 - Register")
            print("2 - Search")
            print("3 - Show information")
            print("4 - Delete")
            print("5 - Return vehicle")
            print("6 - Exit")

            try:
                option = int(input("Select an option: "))
            except ValueError:
                print("The information submitted is invalid, try again")
                continue

            if option == 1:
                Menu.menu_register(fleet)
            elif option == 2:
                Menu.menu_search(fleet)
            elif option == 3:
                Menu.menu_list(fleet)
            elif option == 4:
                Menu.menu_detele(fleet)
            elif option == 5:
                fleet.return_vehicle()
            elif option == 6:
                break
            else:
                print("This option is not in this menu, try again")
                continue

    def menu_validation():
        while True:
            print("Are you sure you want to continue?")
            print("1 - Yes")
            print("2 - No")

            try:
                option_validation = int(input("Select option: "))
            except ValueError:
                print("The information submitted is invalid")
                continue

            if option_validation == 1:
                return 1
            elif option_validation == 2:
                return 2
            else:
                print("This option is not in this menu, try again")

    def menu_register(fleet):
        while True:
            print("====REGISTER FLEET MANAGER====")
            print("1 - Register Vehicle")
            print("2 - Register Operator")
            print("3 - Register Assignment")
            print("4 - Back to main menu")

            try:
                opcion_register = int(input("Select the option: "))
            except ValueError:
                print("This menu only accepts numbers, not letters")
                continue

            if opcion_register == 1:
                fleet.register_vehicle()
            elif opcion_register == 2:
                fleet.register_operator()
            elif opcion_register == 3:
                fleet.register_task()
            elif opcion_register == 4:
                break
            else:
                print("This option is not in the menu")

    def menu_search(fleet):
        while True:
            print("====SEARCH FLEET MANAGER====")
            print("1 - Search vehicle")
            print("2 - Search operator")
            print("3 - Back to main menu")

            try:
                opcion_search = int(input("Select the option: "))
            except ValueError:
                print("This menu only accepts numbers, not letters")
                continue

            if opcion_search == 1:
                fleet.search_vehicle()
            elif opcion_search == 2:
                fleet.search_operator()
            elif opcion_search == 3:
                break
            else:
                print("This option is not in the menu")

    def menu_detele(fleet):
        while True:
            print("====DELETE FLEET MANAGEMENT====")
            print("1 - Delete vehicle")
            print("2 - Delete operator")
            print("3 - Back to main menu")

            try:
                opcion_delete = int(input("Select the option: "))
            except ValueError:
                print("This menu only accepts numbers, not letters")
                continue

            if opcion_delete == 1:
                fleet.delete_vehicle(Menu.menu_validation)
            elif opcion_delete == 2:
                fleet.delete_operator(Menu.menu_validation)
            elif opcion_delete == 3:
                break
            else:
                print("This option is not in the menu")

    def menu_list(fleet):
        while True:
            print("====SHOW FLEET MANAGEMENT====")
            print("1 - Show vehicles")
            print("2 - Show operators")
            print("3 - Show tasks")
            print("4 - Vehicle assignment history")
            print("5 - Operator assignment history")
            print("6 - Back to main menu")

            try:
                opcion_list = int(input("Select an option: "))
            except ValueError:
                print("This menu only accepts numbers, not letters")
                continue

            if opcion_list == 1:
                fleet.list_vehicles()
            elif opcion_list == 2:
                fleet.list_operator()
            elif opcion_list == 3:
                fleet.assigment_histoy()
            elif opcion_list == 4:
                fleet.assigment_history_vehicle()
            elif opcion_list == 5:
                fleet.assigment_history_operator()
            elif opcion_list == 6:
                break
            else:
                print("This option is not in the menu")