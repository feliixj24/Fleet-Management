from validation.validation import Validation
from users.operator import Operator
from data.sql_postgres import DbFleetManagement
from datetime import datetime

class CreateOperator:

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
    def create_operator():
        name = CreateOperator.request_information_str(
            "Please type in the name of the operator: ",
            Validation.validate_name
        )
        last_name = CreateOperator.request_information_str(
            "Please type in the last name of the operator: ",
            Validation.validate_last_name
        )
        cellphone = CreateOperator.request_information_num(
            "Please type in the cell phone of the operator: ",
            Validation.validate_cel_phone
        )
        license = CreateOperator.request_information_num(
            "Please enter de license of the operator: ",
            Validation.validate_license
        )
        date = datetime.now().strftime("%m%d%Y")
        new_id = CreateOperator.create_id_operator()
        operator = Operator(new_id, name, last_name, cellphone, license, date)
        return operator

    @staticmethod
    def create_id_operator():
        return DbFleetManagement.generator_id_operator()