```python
import requests
from database_management import DatabaseConnection

class TravelArrangement:
    def __init__(self, user_id):
        self.user_id = user_id
        self.db = DatabaseConnection()

    def book_flight(self, flight_details):
        # Integrate with travel booking platform API to book flight
        response = requests.post('https://travelbookingapi.com/book_flight', data=flight_details)
        if response.status_code == 200:
            self.db.store_travel_details(self.user_id, 'flight', flight_details)
            return "Flight booked successfully"
        else:
            return "Flight booking failed"

    def book_hotel(self, hotel_details):
        # Integrate with travel booking platform API to book hotel
        response = requests.post('https://travelbookingapi.com/book_hotel', data=hotel_details)
        if response.status_code == 200:
            self.db.store_travel_details(self.user_id, 'hotel', hotel_details)
            return "Hotel booked successfully"
        else:
            return "Hotel booking failed"

    def book_transportation(self, transportation_details):
        # Integrate with travel booking platform API to book transportation
        response = requests.post('https://travelbookingapi.com/book_transportation', data=transportation_details)
        if response.status_code == 200:
            self.db.store_travel_details(self.user_id, 'transportation', transportation_details)
            return "Transportation booked successfully"
        else:
            return "Transportation booking failed"
```