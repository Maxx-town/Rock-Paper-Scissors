random_letters=[]
  exact=0 
  for letter in letters:
    if exact!=nr_letters:
      random_letters.extend(letters[random.randint(0,len(letters)-1)])
      exact=exact+1
  
  exact=0
  random_symbols=[]
  for symbol in symbols:
    if  exact!=nr_symbols:
      random_symbols.extend(symbols[random.randint(0,len(symbols)-1)])
      exact=exact+1
  
  exact=0
  random_numbers=[]
  for number in numbers:
    if exact!=nr_numbers:
      random_numbers.extend(numbers[random.randint(0,len(numbers)-1)])
      exact=exact+1
  password=random_letters+random_numbers+random_symbols
  x=0
  password1=0
  for x in range(0,len(password)-1):
    password1=password1+password[x]
