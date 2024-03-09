import random
# List of all lowercase letters
letters = [chr(i) for i in range(ord('a'), ord('z')+1)]

# List of numbers from 0 to 9
numbers = [str(i) for i in range(10)]

# List of common symbols
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', '}', '[', ']', '|', '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']

q = int(input("how many Letters do you want "))
n = int(input("how many numbers do you want "))
s = int(input("how many symbols do you want "))

# for _ in range(q):
#     newguy0 = random.choice(letters)
#     print(newguy0, end="")
    
# for _ in range(n):
#     newguy1 = random.choice(numbers)
#     print(newguy1, end="")

# for _ in range(s):
#     newguy2 = random.choice(symbols)
#     print(newguy2, end="")

password = ""
for _ in range(1, q +1):
    password += random.choice(letters)
    
for _ in range(1, n +1):
    password += random.choice(numbers)

for _ in range(1, s +1):
    password += random.choice(symbols)

print(password)
