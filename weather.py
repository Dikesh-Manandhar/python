import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response=requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=7cc1a37af84b2a4e2826608242160abc")
        except:
            print("Error in fetching data")
            exit(1)

        self.response_json=response.json()
        self.temp=self.response_json["main"]["temp"]
        self.temp_min=self.response_json["main"]["temp_min"]
        self.temp_max=self.response_json["main"]["temp_max"]
        self.feels_like=self.response_json["main"]["feels_like"]

    def temperature(self):
        
        print("Temperature in",self.name, ":", self.temp)
        print("Minimum Temperature:", self.temp_min)
        print("Maximum Temperature:", self.temp_max)
        print("Feels Like: ", self.feels_like)

my_city = City("Kathmandu", 27.7103, -85.3222)
my_city.temperature()

vacation_city = City("Paris", 48.8566, -2.3522)
vacation_city.temperature()
