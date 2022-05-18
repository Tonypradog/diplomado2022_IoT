import pickle

with open('tuple.bin','rb') as fh:
        atuple = pickle.load(fh) 

print(type(atuple))

print(atuple)