

import pickle 
f = open("ab.dat", "wb")
d = { "name" : 'Arun', "roll no." : 1, "marks": 95}
pickle.dump(d,f)
f.close()
f1 =open("ab.dat","rb")
lines = pickle.load(f1)


    
  
    
