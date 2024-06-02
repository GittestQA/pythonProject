# Strings

dir = 'C:/nomedir/some.txt'
print(dir)
dir = "C:/nomedir/some.txt"
print(dir)

dir = "C:\nomedir\some.txt"
print(dir)

dir = "C:\aomedir\some.txt"
print(dir)

# \n, \a - are special character in order to use them as is use r - which will keep it as raw value
# eg, (dir = r'C:\nomedir\some.txt') - raw string concept - This will be used in dir paths

dir = r'C:\nomedir\some.txt'
print(dir)

dir = r"C:\aomedir\some.txt"
print(dir)

# Format String

first_name = "Dhaval"
last_name = 'Lalan'
roll_number = 27
isMarried = False
print(f"Your name is {first_name} {last_name} \n and Roll number is {roll_number}")
print("Your name is {first_name} {last_name}")
print(f"Your name is {first_name} {last_name} , Roll number is {roll_number}")
print(f'Your name is {first_name} {last_name}, your roll number is {roll_number} and you are Married: {isMarried}')

first_name = input("enter your name")
print(f'Your name is {first_name}')