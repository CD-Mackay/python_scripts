user_input = input("Input your text: ")
print("You have written: ", user_input)

updated = user_input.split(' ')

for word in updated:
  if len(word) >=3:
    word = word + "%say" % (word[0])
    word = word[1:]
    print(word)
  else:
    print(word)
