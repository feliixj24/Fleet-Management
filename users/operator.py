class Operator:

    def __init__(self, id_operator, name, last_name, cel_phone, license, date_created, state="active" ):

        self.id_operator = id_operator
        self.name = name
        self.last_name = last_name
        self.cel_phone = cel_phone
        self.license = license
        self.state = state
        self.date = date_created

    def __str__(self):
        return(
            f"id_operator:{self.id_operator}\n"
            f"name:{self.name}\n"
            f"last_name:{self.last_name}\n"
            f"cell_phone:{self.cel_phone}\n"
            f"license:{self.license}\n"
            f"state:{self.state}\n"
            f"date:{self.date}\n"
        )
