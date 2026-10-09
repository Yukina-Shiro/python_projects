# Write code below 💖

def pet_age():
    pet_type = input("Is your pet a cat or a dog ?")

    if pet_type == "cat":
        pet_age = int(input("Enter your cat's age:"))
        human_age = 6*pet_age
        print(human_age)
    elif pet_type == "dog":
        pet_age = int(input("Enter your dog's age:"))
        human_age = 7*pet_age
        print(human_age)
    else:
        print("Not a pet")


pet_age()