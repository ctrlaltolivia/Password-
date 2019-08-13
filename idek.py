#Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
Dict = open("dictionary.txt","r")


print("Can your password survive a dictionary attack?")

#Take input from the keyboard, storing in the variable test_password
#NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords
test_password = input("Type in a trial password: ")
user_input = input
Dictionary = []
Dictionary2 = []

for x in Dict:
    Dictionary.append(x)

for y in Dictionary:
    w = y.strip("\n")
    Dictionary2.append(w)

if test_password in Dictionary2:
    print("You've been hacked!")
elif test_password not in Dictionary2:
    print("Congrats you've survived the Dictionary Attack!")
