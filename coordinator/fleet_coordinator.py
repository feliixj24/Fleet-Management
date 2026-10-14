import psycopg
from register.create_vehicle import CreateVehicle
from register.create_operator import CreateOperator
from register.create_task import CreateTask
from data.sql_postgres import DbFleetManagement
from users.vehicle import Vehicle
from users.operator import Operator
from users.task import Task


class FleetManagenment:

    def register_vehicle(self):
        vehicle = CreateVehicle.create_vehicle()
        try:
            DbFleetManagement.save_vehicle_information(vehicle)
        except psycopg.Error as error:
            print("The register fail to be save in PostgresSQL")
            print(f"Tecnic Detail{error}")
            return
        print("Information saved sucessfully")
    def register_operator(self):
        operator = CreateOperator.create_operator()
        
        try:
            DbFleetManagement.save_operator_information(operator)
        except psycopg.Error as error:
            print("The register fail to be save in PostgresSQL")
            print(f"Tecnic Detail{error}")
            return
        print("Information saved sucessfully")
    def register_task(self):
        task = CreateTask.create_task()
        if task is None:
            print("Vehicle or operator not found")
            return
        result_vehicle = DbFleetManagement.search_vehicle_information(
            task.id_vehicle
        )
        result_operator = DbFleetManagement.search_operator_information(
            task.id_operator
        )
        
        vehicle = Vehicle(*result_vehicle)
        operator = Operator(*result_operator)

        if vehicle.state != "active" or operator.state != "active":
            print("Vehicle or operator is inactive")
            return
        if vehicle.status != "available":
            print("The vehicle is not available")
            return
        assigments = DbFleetManagement.get_history_operator(
            task.id_operator
        )
        for assigment in assigments:
                    if assigment[4] == "active":
                        print("The operator already has an active assigment")
                        return
        try:
            DbFleetManagement.save_task_information(task)
        except psycopg.Error as error:
            print("The creation fail to be save in postgresSQL")
            print(f"Tecnic Detail{error}")
            return
        print("Vehicle assigned to operator sucessfully")

    def delete_operator(self, confirm):
        print("Type the operator ID: ")
        result = input("")
        result = result.strip().upper()
        operator_data = DbFleetManagement.search_operator_information(result)

        if operator_data is None:
            print("Operator not found")
            return
        assigments = DbFleetManagement.get_history_operator(result)
        for assigment in assigments:
            if assigment[4] == "active":
                print("The operator has an active assigment")
                return
        validation = confirm()
        if validation == 1:
            DbFleetManagement.delete_operator_information(result)            
            print("The operator has been desactivated sucessfully")
        else:
            print("The operation was cancel.")
    def delete_vehicle(self, confirm):
        print("Type the vehicle ID: ")
        result = input("")
        result = result.strip().upper()
        vehicle_data = DbFleetManagement.search_vehicle_information(result)

        if vehicle_data is None:
            print("Vehicle not found")
            return
        assigments = DbFleetManagement.get_history_vehicle(result)
        for assigment in assigments:
            if assigment[4] == "active":
                print("The vehicle is assigned")
                return
        validation = confirm()
        if validation == 1:
            DbFleetManagement.delete_vehicle_information(result)
            print("The vehicle has been desactivated sucessfully")
        else:
            print("The operation was cancel.")
    def return_vehicle(self):
        id_task = input("Type in task ID: ")
        id_task = id_task.strip().upper()

        result = DbFleetManagement.search_task_information(id_task)
        if not result:
            print("The assigment doesn't exist")
            return

        task = Task(*result)
        if task.state !="active":
            print("The assigment is already finished")
            return
        task.return_vehicle()

        try:
            DbFleetManagement.save_vehicle_return(task)
        except psycopg.Error as error:
            print("The vehicle return could not be saved")
            print(f"Technical detail: {error}")
            return

        print("Vehicle returned successfully")


    def search_vehicle(self):
        option_id = input("Type in the ID for the vehicle to search: ")
        option_id = option_id.strip().upper()

        result = DbFleetManagement.search_vehicle_information(option_id)
        if result is None:
            print("The vehicle doesn't exist")
            return
        else:
            vehicle = Vehicle(*result)
            print(vehicle)
    def search_operator(self):
        option_id = input("Type in the ID for the operator to search: ")
        option_id = option_id.strip().upper()
        result = DbFleetManagement.search_operator_information(option_id)

        if result is None:
            print("The operator doesn't exist")
            return
        else:
            operator = Operator(*result)
            print(operator)
    def list_vehicles(self):
        result = DbFleetManagement.get_vehicles()
        if not result:
            print("There is not vehicle registered")
            return
        for data in result:
            vehicle = Vehicle(*data)
            print(vehicle)
            print("-" * 30)
    def list_operator(self):
        result = DbFleetManagement.get_operator()
        if not result:
            print("There is not operator registered")
            return
        for data in result:
            operator = Operator(*data)
            print(operator)
            print("-" * 30)
    def assigment_histoy(self):
        result = DbFleetManagement.get_task()

        if not result:
            print("There is not task registered")
            return
        for task in result:
            print(task)
            print("-" * 30)
    def assigment_history_vehicle(self):
        print("Type in the ID to show the history for the vehicle: ")
        history_id = input("")
        history_id = history_id.strip().upper()
        result = DbFleetManagement.get_history_vehicle(history_id)
        if not result:
            print("This ID doesn't have any history")
            return
        for vehicle in result:
            print(vehicle)
            print("-" * 30)
    def assigment_history_operator(self):
        print("Type in the ID to show the history for the operator: ")
        history_id = input("")
        history_id = history_id.strip().upper()
        result = DbFleetManagement.get_history_operator(history_id)
        if not result:
            print("This ID doesn't have any history")
            return
        for operator in result:
            print(operator)
            print("-" * 30)