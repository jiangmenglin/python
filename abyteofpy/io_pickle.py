import pickle

#The name of the file where we will store the object
shoplistfile = 'shoplist.data'
#The list of things to buy
shoplist = ['apple', 'mango', 'carrot']

#write to the file
f = open(shoplistfile, 'wb')
#Dump the object to a file
pickle.dump(shoplist, f)
f.close()

#Destory the shoplist variable
del shoplist

#Read back the object from the storage
f = open(shoplistfile, 'rb')
#Load the object from the file
storedlist = pickle.load(f)
print(storedlist)
