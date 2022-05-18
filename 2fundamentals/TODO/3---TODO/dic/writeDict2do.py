import pickle

d={'20223142':'Enrique Iglesias', '24356722':'Roberto Martinez', '2016780':'Matty Healey'}

with open('dic.bin','wb') as fh:
        pickle.dump(d,fh)

print('done...')

