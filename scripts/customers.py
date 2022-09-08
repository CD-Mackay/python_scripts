customers = {'06753':'Mehzabin Afroze','02457':'Md. Ali',
'02834':'Mosarof Ahmed','05623':'Mila Hasan', '07895':'Yaqub Ali'}

customers['12345'] = 'Charlie Kelly'

print('The Customer names are:')

for e in customers:
  print(customers[e])


name = input('Enter Customer Id')

for customer in customers:
  if customer == name:
    print(customers[customer])
    break
