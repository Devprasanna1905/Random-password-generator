import random
import os
length=int(input("Enter the password length:"))
upper="ABCDEFGHIJKLLMOPQRSTUVWXYZ"
lower="abcdefghijklmnopqrstuvwxyz"
special="!@#$%^&*1234567890"
pas=upper+lower+special
print("".join(random.sample(pas,length)))
