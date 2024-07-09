# load and dump -- file handling
# loads and dumps -- without file handling

# pickle -- also called as serialization

# picke is parsing
# used to change form obj to binary
# rb -> read binary
# wb -> write binary


## python object to Bytestream -- called as pickling
## Bytestream to python object -- called as unpickling

# without filehandling
# n_v=pickle.dumps(iterable)
# n_v=pickle.loads(v_n)

# with file handling
# with open('filename', 'mode') as file:
# n_v = pickle.dump(iterable, file)



# import pickle
# s="python"
# x=pickle.dump(s)
# print(x)
#
#
# import os
# print(os.getcwd())
#
# os.chdir(r 'PATH')
# print(os.getcwd())

import pickle
with open('lastday.pkl','wb') as file:
    data=pickele.dump(["a","b","c","d"],file)

with open("lastday.pkl","rb")as file:
    data=pickle.load(file)
    print(data)

os.popen("lastday.pkl")

