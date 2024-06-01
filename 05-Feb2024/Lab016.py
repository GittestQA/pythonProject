name="batman"
name2='batman'

print(len(name)) # len starts from 1
print(name[0]) # index starts from 0
#print(name[6]) # indexerror: string index out of range

print(len(name)-1)
print(name[len(name)-1])

#Strings - Immutabile meaning they can't be changed or modified

string = "Hello"
#string[0] = "P" #TypeError: 'str' object does not support item assignment (you cannot change the value)
print(string)

string= "pramod" # you can replace the value
print(string)