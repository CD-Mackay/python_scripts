import pickle

dataObject = []

for num in range(10,15):
  dataObject.append(num)

file_handler = open('languages', 'wb')

pickle.dump(dataObject, file_handler)

file_handler.close()

file_handler = open('languages', 'rb')

data_Object = pickle.load(file_handler)

for val in data_Object:
  print("cool:", val)

file_handler.close()  