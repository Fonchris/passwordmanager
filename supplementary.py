import random
letters=['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i' ,'J','j',
          'K','k','L','l','M','m','N','n','O','o','P','p','Q','q','R','r','S','s','T','t','U','u','V',
          'v','W','w','X','x','Y','y','Z','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=[';',':','/','>','<','?','#','@','!','"','.','+','_','-','(',')','*','&','^','%','$',']']
password_list = []
print("welcome to the python password generator")
letter_no = int(input("how many letters should your password have ?"))
number_no = int(input("how many numbers should your password have ?"))
symbol_num = int(input("how many symbols should your password have ?"))
for let in range(letter_no+1):
    password_list.append(random.choice(letters))
for num in range(number_no + 1):
    password_list.append(random.choice(numbers))
for sym in range(symbol_num + 1):
    password_list.append(random.choice(symbols))
random.shuffle(password_list)
password= ""
for char in password_list:
    password+=char
print(f"your password is {password}")
