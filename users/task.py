from datetime import datetime

class Task:
    def __init__(self, id_assigment, id_vehicle, id_operator, date_created, state="active", date_returned = None):
        self.id_assigment = id_assigment
        self.id_vehicle = id_vehicle
        self.id_operator = id_operator
        self.date_created = date_created
        self.state = state
        self.date_return = date_returned

    def return_vehicle(self):
        if self.state == "active":
            self.state = "finished"
            self.date_return = datetime.now().strftime("%m%d%Y")
            return True, "The assigment was completed sucessfully"
        return False, "The assigment is already finished"
    def __str__(self):
        return(
            f"id_assigment:{self.id_assigment}\n"
            f"id_vehicle:{self.id_vehicle}\n"
            f"id_operator:{self.id_operator}\n"
            f"date created:{self.date_created}\n"
            f"state:{self.state}\n"
            f"date return:{self.date_return}\n"
        )