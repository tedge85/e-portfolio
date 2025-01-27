class Cars:

    def __init__(self):
        
        self.car_range = {
            "car1" : {
                "make": "Skoda",
                "sold": True
            },
            "car2" : {
                "make": "Ford",
                "sold": False
            },
            "car3" : {
                "make": "Nissan",
                "sold": False
            },
            "car4" : {
                "make": "Fiat",
                "sold": True
            },
            "car5" : {
                "make": "Subaru",
                "sold": False
            },
            "car6" : {
                "make": "Honda",
                "sold": True
            },
        }


    def show_all_car_ref_nums(self):
        """Print all car reference numbers, sold and unsold."""
            
        cars_nums_str = ""

        car_keys = self.car_range.keys()

        for cars in car_keys:
            cars_nums_str += cars + " "

        print(f"Full car range (ref numbers): {cars_nums_str}")


    def show_car_info(self):
        """Print all car info."""

        for cars in self.car_range.items():
            print(cars)

    
    def show_available_cars(self):
        """Print all unsold car models."""

        car_make_str = ""

        for details in self.car_range.values():
            if details["sold"] == False:
                car_make_str += details["make"] + " "
                        
        print(f"Available car models: {car_make_str}")


# Instantiate the Cars class.
cars = Cars()


# Call methods
cars.show_all_car_ref_nums()

cars.show_car_info()

cars.show_available_cars()