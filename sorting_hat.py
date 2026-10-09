Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

# Question 1
a = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\n"))
if a == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif a == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input.")

# Question 2
b = int(input("\nQ2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\n"))
if b == 1:
    Hufflepuff += 2
elif b == 2:
    Slytherin += 2
elif b == 3:
    Ravenclaw += 2
elif b == 4:
    Gryffindor += 2
else:
    print("Wrong input.")

# Question 3
c = int(input("\nQ3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\n"))
if c == 1:
    Slytherin += 4
elif c == 2:
    Hufflepuff += 4
elif c == 3:
    Ravenclaw += 4
elif c == 4:
    Gryffindor += 4
else:
    print("Wrong input.")

# Determine the house with the most points
max_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

if max_points == Gryffindor:
    house = "Gryffindor 🦁"
elif max_points == Ravenclaw:
    house = "Ravenclaw 🦅"
elif max_points == Hufflepuff:
    house = "Hufflepuff 🦡"
else:
    house = "Slytherin 🐍"

print("\nThe Sorting Hat has spoken! You belong in:", house)
