class Vehicle:

    def __init__(self, id_vehicle, brand, model, year, dish, date_created, status="available",state="active", ):
        self.id_vehicle = id_vehicle
        self.brand = brand
        self.model = model
        self.year = year
        self.dish = dish
        self.status = status
        self.state = state
        self.date = date_created
        
    def __str__(self):
        return(
            f"id_vehicle:{self.id_vehicle}\n"
            f"brand:{self.brand}\n"
            f"model:{self.model}\n"
            f"year:{self.year}\n"
            f"dish:{self.dish}\n"
            f"status:{self.status}\n"
            f"state:{self.state}\n"
            f"date:{self.date}\n"
        )
            
    
   