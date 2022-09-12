import os 
import pickle
def search(r):
    f = open ('flights2.dat', 'rb')
    flag = False 
    
    rec = pickle.load(f)
    if rec['flight no.'] == r:
         print(23)
         flag = True 
        
    
     
    if flag == False:
        print(20)
    f.close()
search(1)