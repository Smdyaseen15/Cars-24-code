class CarInfo:
    def __init__(self, car_id, car_name, car_type, city):
        self.__car_id = car_id
        self.__car_name = car_name
        self.__car_type = car_type
        self.__city = city

    # Getters and setters
    def get_car_id(self):
        return self.__car_id

    def get_car_name(self):
        return self.__car_name

    def get_car_type(self):
        return self.__car_type

    def get_city(self):
        return self.__city

    def check_availability(self):
        car_data = {
            "Nissan": {
                "Sedan": ("Kicks", 8400.0),
                "SUV": ("Magnite", 10800.0),
                "MUV": ("Terrano", 14400.0),
            },
            "Ford": {
                "Sedan": ("Figo", 4802.0),
                "SUV": ("Eco Sport", 9605.0),
                "MUV": ("Endeavour", 21600.0),
            },
        }

        valid_cities = ["New York", "Denver", "Los Angeles"]

        if self.__car_name not in car_data:
            return "Not Available"
        if self.__car_type not in car_data[self.__car_name]:
            return "Not Available"
        if self.__city not in valid_cities:
            return "Not Available"

        available_car, price = car_data[self.__car_name][self.__car_type]
        return f"Available car and price is: {available_car} and ${price}"

class UserInterface:
    @staticmethod
    def extract_details(car_details):
        try:
            car_id, car_name, car_type, city = car_details.split(":")
            return CarInfo(car_id, car_name, car_type, city)
        except ValueError:
            print("Invalid Details")
            return None

# Example Usage
def main():
    car_details = input("Enter the Car Details: ")
    car_info = UserInterface.extract_details(car_details)

    if car_info:
        print(f"Car Id: {car_info.get_car_id()}")
        print(f"Car Name: {car_info.get_car_name()}")
        print(f"Car Type: {car_info.get_car_type()}")
        print(f"City: {car_info.get_city()}")
        print(car_info.check_availability())

if __name__ == "__main__":
    main()