# import modules
import string
import random
 
 
# store all characters in lists 
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)
 
 
# Length of password
user_input = input("How many characters do you want in your password? ")
 
 
# check if password is more than 8 characters
while True:
 
    try:
 
        characters_number = int(user_input)
 
        if characters_number < 8:
 
            print("The Password should be more than 8 Characters")
 
            user_input = input("Please, Enter your number again: ")
 
        else:
 
            break
 
    except:
 
        print("Please, Enter numbers only.")
 
        user_input = input("How many characters do you want in your password? ")
 
 
# shuffle lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)
 
 
# calculate 30% & 20% of number of characters
part1 = round(characters_number * (30/100))
part2 = round(characters_number * (20/100))
 
 
# generation of the password (60% letters and 40% digits & punctuations)
result = []
 
for x in range(part1):
 
    result.append(s1[x])
    result.append(s2[x])
 
for x in range(part2):
 
    result.append(s3[x])
    result.append(s4[x])
 
 
# shuffle result
random.shuffle(result)
 
 
# join result
password = "".join(result)
print("Strong Password: ", password)
