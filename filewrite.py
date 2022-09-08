filename = "languages.txt"

fileHandler = open(filename, "w")

fileHandler.write("Python")
fileHandler.write("Irish")
fileHandler.write("AAAAAAH")

fileHandler.close()

fileHandler = open(filename, "r")
for line in fileHandler:
  print("I know")
  print(line)
  print('!\n')

fileHandler.close()

