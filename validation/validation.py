class Validation:

    def validate_name(name):
        name = name.strip().lower()

        if not name:
            return False, "This field is mandatory"
        if not name.isalpha():
            return False, "The information is invalid, try again"
        if len(name) < 2:
            return False, "The name is to short, try again"
        else:
            return True, ""
    def validate_last_name(last_name):
        last_name = last_name.strip().lower()

        if not last_name:
            return False, "This file is mandatory"
        if not last_name.isalpha():
            return False, "The information is invalid, try again"
        else:
            return True, ""
    def validate_cel_phone(cel_phone):
        cel_phone = cel_phone.strip()

        if not cel_phone:
            return False, "This field is mandatory", int
        if not cel_phone.isdigit():
            return False, "The information is invalid, try again", int
        if len(cel_phone) != 10:
            return False, "The celphone must have 10 digits, try again", int
        else:
            return True, "", int
    def validate_license(license):
        license = license.strip()

        if not license:
            return False, "This field is mandatory", int
        try:
            license = int(license)
        except ValueError:
            return False, "The information is invalid, try again", int
        else:
            return True, "", int
    def validate_brand(brand):
        brand = brand.strip().lower()

        if not brand:
            return False, "This field is mandatory"
        if not all(char.isalnum() or char in " -" for char in brand):
            return False, "The information is invalid, try again"
        if len(brand) < 2:
            return False, "The brand is short, try again"
        else:
            return True, ""
    def validate_model(model):
        model = model.strip().lower()

        if not model:
           return False, "This field is mandatory"
        if not all(char.isalnum() or char in " -" for char in model):
            return False, "The information is invalid, try again"
        if len(model) < 2:
            return False, "The model is short, try again"
        else:
            return True, ""
    def validate_dish(dish):
        dish = dish.strip().lower()

        if not dish:
            return False, "This field is mandatory"
        if len(dish) < 5:
            return False, "The plate is short, try again"
        else:
            return True, ""

    def validate_year(year):
        year = year.strip()

        if not year:
            return False, "This field is mandatoy", int
        try:
            year = int(year)
        except ValueError:
            return False, "The information is invalid, try again", int
        if year <= 1990:
            return False, "The year need to be greater than 1990, try again", int
        else:
            return True, "", int
        
       
        
        
            