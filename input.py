import re
string = input("enter a string value: ")

pattern = '^[A-Z]'

found = re.match(pattern, string)

if found:
  print("Started with capital")
else:
  print("It should start with a capita")
