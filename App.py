import string
import random

s1 = list(string.ascii_lowercase)

s2 = list(string.ascii_uppercase)

s3 = list(string.digits)

s4 = list(string.punctuation)

char_num = input("How many characters for the password ? ")

while True :
    try :
        char_num = int(char_num)
        if char_num < 6 : 
            print("You need at leaset 6 charecters !!! ")
            char_num = input("Plese enter the number again >> ")
        else :
            break 
    except :
        print("Please enter number ! ")
        char_num = input("How many characters for the password ? ")

random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

part_one = round(char_num * (30/100))
part_tow = round(char_num *(20/100))

password = []

for i in range(part_one):
    password.append(s1[i])
    password.append(s2[i])

for i in range(part_tow):
    password.append(s3[i])
    password.append(s4[i])    


password = "".join(password[0:])
print(password)

