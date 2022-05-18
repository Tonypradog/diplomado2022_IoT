import pickle
import pprint

with open('dic.bin','rb') as fh:
        adic = pickle.load(fh) 

print(type(adic))
print("Sin pprint:\n",adic)
print("Con pprint:\n")

pprint.pprint(adic)
