#example1

one = 1
two = 2
three = one / two
print(three)

#example2
hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)

#example3
a, b = 3, 4
print(a,b)

#example4 (KM TO MILES)
kmh = int(input("Enter km/h "))
mph = 0.6214 * kmh
print("Speed",kmh,"KM/H =",mph,"MPH")

#example5 (Celsius to Farenheit)
Celsius = int(input("Enter a temperature in Celsius "))
Farenheit = 9.0/5.0 * Celsius + 32
print("Temperature",Celsius,"Celsius = ", Farenheit, "F")

#example6 (Average Score)
round1 = int(input("Enter score for round 1: "))
round2 = int(input("Enter score for round 2: "))
round3 = int(input("Enter score for round 3: "))
average = (round1 + round2 + round3) / 3
print("The final average score is: ", average)

#example7 (exercise)
numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

numbers.append(1)
numbers.append(2)
numbers.append(3)

strings.append("hello")
strings.append("world")

second_name = names[1]

print(numbers)
print(strings)
print("The second name on the name list is %s" %second_name)

#example8
astring = "Hello world!"
print(astring.index("wo"))

astring = "Hello world!"
print(astring.count("l"))

astring = "Hello world!"
print(astring[3:7])

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

#example9
x = 2
print(x == 2) # prints out True
print(x == 3) # prints out False
print(x < 3) # prints out True

#example10
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
    
#example11
x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

#example12
x = [1,2,3]
y = [1,2,3]
print(x == y) # Prints out True
print(x is y) # Prints out False

#example13
phonebook = {}
phonebook["John"] = 938477566
phonebook["Jack"] = 938377264
phonebook["Jill"] = 947662781
print(phonebook)

phonebook = {
    "John" : 938477566,
    "Jack" : 938377264,
    "Jill" : 947662781
}
print(phonebook)

#example14
phonebook = {
   "John" : 938477566,
   "Jack" : 938377264,
   "Jill" : 947662781
}
del phonebook["John"]
print(phonebook)

#example15
import random

def lottery():
    # returns 6 numbers between 1 and 40
    for i in range(6):
        yield random.randint(1, 40)

    # returns a 7th number between 1 and 15
    yield random.randint(1,15)

for random_number in lottery():
       print("And the next number is... %d!" %(random_number))

#example16
sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
word_lengths = []
for word in words:
      if word != "the":
          word_lengths.append(len(word))
print(words)
print(word_lengths)

#example17 (grades)

grade_a = int(input("Insert Grade A: "))
grade_b = int(input("Insert Grade B: "))
  
average = (grade_a + grade_b)/2
   
if average >= 6:
    print('Approved')
else:
    print('Not Approved')
 
#example18 (IF)
if True:
  print("True Condition")
  print("We are inside the IF")
  
#example19 (IF, ELIF and ELSE)
number = int(input("Insert a number: "))

if number > 5:
  print("Bigger than 5")
elif number == 5:
  print("Equal to 5")
else:
  print("Less than 5");
  
#example20 (grades)

grade_1 = int(input("Insert First Grade: "))
grade_2 = int(input("Insert Second Grade: "))

sum = grade_1 + grade_2

if sum > 80:
  print("Congratz! Your Score is Fantastic!")
elif sum > 60:  
  print("You passed")

  elif sum == 60:
  print("You passed with average score")

else:
  print("You didn't pass. Try again")
  
#example21 (while)

while True:
  word = input("Type a word")
  print(word)
  
#example22 (password)

default_password = "Bruno"

password = input("Please, insert your password: ")

while password != default_password:
    password = input("Please, insert your password: ")
    if not password:
        continue
    elif password != default_password:
        print("Wrong Password")

# After this Password Checker, you can paste your code down here:

print("Welcome")
print("Initializing")

#example23 (lottery - lucky_number)

from random import randrange

lucky_number = randrange(10)

while True:
    number = int(input("Try it, insert a number: "))

    if not number:
        continue
    elif number == lucky_number:
        break
    elif number < lucky_number:
        print("More")
    else:
        print("Less")

print("Congratz! You are right!")

#example24 (