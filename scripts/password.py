import getpass

password = getpass.getpass('Password:')

if password == 'Plorky':
  print("You are authenticated")
else:
  print("DENIEEEED")