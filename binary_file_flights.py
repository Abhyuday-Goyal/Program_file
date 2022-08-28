import os
import pickle
f = open('flights.dat', 'wb')
flight1 = [{'flight no.': 1, 'airline name': 'indigo', 'Departure': 'India', 'destination': 'dubai'},
           {'flight no.': 2, 'airline name': 'jet airways',
               'Departure': 'USA', 'destination': 'dubai'},
           {'flight no.': 3, 'airline name': 'indigo',
               'Departure': 'India', 'destination': 'USA'},
           {'flight no.': 4, 'airline name': 'indigo', 'Departure': 'India', 'destination': 'Spain'}]
pickle.dump(flight1, f)
f.close()
f1 = open('flights.dat', 'rb')
flight_list = pickle.load(f1)
print(flight_list)
flight_count = 0
for flight in flight_list:
    if flight['destination'] == 'dubai':
        flight_count += 1
print(flight_count)
