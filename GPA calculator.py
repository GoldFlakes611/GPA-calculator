def add_list(list = []):
    tmpstorage = 0
    total = 0
    for l in list:
        total = total+l
    return total



GPA = 0
gradelist = []
gradepoints = {
    "A+": 4.3,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0
}
while True:
    classes = input("How many classes do you take?")
    if classes.isnumeric() == True:
        break
    elif classes.isnumeric() == False:
        if classes == "exit":
            exit()
        else:
            print("Please enter a valid response")

classes = int(classes)
userinput = ""


while True:
    roundnumber = False
    roundornot = input("Do you want to round your GPA? (yes/no)")
    roundornot = roundornot.lower()
    if roundornot == 'yes':
        roundnumber = True
        break
    elif roundornot == "no":
        roundnumber = False
        break
    elif roundornot == "exit":
        exit()
    else:
        print("please enter a valid response")


for i in range(classes):

    while True:
        userinput = input("Enter grades for each of your classes")
        userinput = userinput.upper()
        if userinput == "A+" or "A" or "A-" or "B+" or "B" or "B-" or "C+" or "C" or "C-" or "D+" or "D" or "D-" or "F":
            print()
            break
        else:
            print("please enter a valid response")

    if userinput == exit:
        exit()
    else:
        gradelist.append(gradepoints.get(userinput))


total_points = add_list(gradelist)



GPA = total_points/classes
if roundnumber == True:
    GPA = round(GPA,1)
elif roundnumber == False:
    GPA = GPA
print(f"Your GPA is {GPA}")

rawinput = input('return to exit')
if rawinput == "":
    exit()





