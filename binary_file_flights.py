import os
import pickle
f = open('flights.dat', 'rb')
flight1 = {{ 'flight no.':1, 'airline name':'indigo','Departure':'India','destination':'dubai'},
{'flight no.':2, 'airline name':'jet airways','Departure':'USA','destination':'dubai'},
 {'flight no.':3, 'airline name':'indigo','Departure':'India','destination':'USA'},
{'flight no.':4, 'airline name':'indigo','Departure':'India','destination':'Spain'}}
pickle.dump(flight1,f)
pickle.dump(flight2,f)
pickle.dump(flight3,f)
pickle.dump(flight4,f)
if flight1["destination"] = 