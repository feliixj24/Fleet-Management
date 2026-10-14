from users.task import Task
from data.sql_postgres import DbFleetManagement
from datetime import datetime

class CreateTask:


    @staticmethod
    def create_task():
        id_vehicle = input("Type in the vehicle ID to be assigned: ")
        id_vehicle = id_vehicle.strip().upper()
        result_vehicle = DbFleetManagement.search_vehicle_information(id_vehicle)
        if result_vehicle is None:
            return None           
                       
        id_operator = input("Type in the operator ID to recevied the vehicle: ")
        id_operator = id_operator.strip().upper()
        result_operator = DbFleetManagement.search_operator_information(id_operator)
        if result_operator is None:
            return None

        date_created = datetime.now().strftime("%m%d%Y")
        new_id = CreateTask.create_id_task()
        task = Task(new_id, id_vehicle, id_operator, date_created)
        return task
        


    @staticmethod
    def create_id_task():
        return DbFleetManagement.generator_id_task()