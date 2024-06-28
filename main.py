def createRandom(length):
    return id(length) % len(length)


uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_cases = ['@', '!', '#', '$', '%', '^', '&', '&']

uprCasesReq = int(input('What are the number of uppercase letters you need : '))
lwrCasesReq = int(input('What are the number of lowercase letters you need : '))
digitsReq = int(input('What are the number of digits you need : '))
spclCasesReq = int(input('What are the number of special case characters you need : '))

password = []

for x in range(0, int(uprCasesReq) - 1):
    password += uppercase_letters[createRandom(length=uppercase_letters)]
    uppercase_letters.remove(uppercase_letters[createRandom(length=uppercase_letters)])

for x in range(0, int(lwrCasesReq) - 1):
    password += lowercase_letters[createRandom(length=lowercase_letters)]
    lowercase_letters.remove(lowercase_letters[createRandom(length=lowercase_letters)])

for x in range(0, int(digitsReq) - 1):
    password += digits[createRandom(length=digits)]
    digits.remove(digits[createRandom(length=digits)])

for x in range(0, int(spclCasesReq) - 1):
    password += special_cases[createRandom(length=special_cases)]
    special_cases.remove(special_cases[createRandom(length=special_cases)])

final_password = ""
for x in range(0, len(password)):
    final_password += password[createRandom(password)]
    password.remove(password[createRandom(password)])
print(final_password)
