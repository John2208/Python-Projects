import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "!@#$%^&*()_+-=[]{}|;':\"<>,./"
numbers = "0123456789"


all_char = lower + upper + symbols + numbers
length = int(input("Enter Password Length: "))

password = ''.join(random.sample(all_char,length))
print("Generated Password: ",password)