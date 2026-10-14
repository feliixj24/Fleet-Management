from validation.validation import Validation
from users.vehicle import Vehicle
from data.sql_postgres import DbFleetManagement
from datetime import datetime

class CreateVehicle:

    @staticmethod
    def request_information_str(message, funtion_validation):
            while True:
                data = input(message)
                valid, message_funtion = funtion_validation(data)
        
                if valid:
                    return data
                print(message_funtion)

    @staticmethod
    def request_information_num(message, funtion_validation):
        while True:
            data = input(message)
            valid, message_funtion, type_data = funtion_validation(data)
            if valid:
                data = type_data(data)
                return data
            print(message_funtion)

    @staticmethod
    def create_vehicle():
        brand = CreateVehicle.request_information_str(
            "Please type in the brand of the vehicle: ",
            Validation.validate_brand
        )
        model = CreateVehicle.request_information_str(
             "Please type in the model of the vehicle: ",
             Validation.validate_model
        )
        year = CreateVehicle.request_information_num(
             "Please type in the year of the vehicle: ",
             Validation.validate_year
        )
        dish = CreateVehicle.request_information_str(
             "Please type in the plate of the vehicle: ",
             Validation.validate_dish
        )
        date = datetime.now().strftime("%m%d%Y")
        new_id = CreateVehicle.create_id_vehicle()
        vehicle = Vehicle(new_id, brand, model, year, dish, date)
        return vehicle

    @staticmethod
    def create_id_vehicle():
         return DbFleetManagement.generator_id_vehicle()