# Write code below 💖
import random

Question = input("Question:")

random_number = random.randint(1, 9)

if random_number == 1:
    response = "Yes - definitely."
elif random_number == 2:
    response = "It is decidedly so."
elif random_number == 3:
    response = "Without a doubt."
elif random_number == 4:
    response = "Reply hazy, try again."
elif random_number == 5:
    response = "Ask again later."
elif random_number == 6:
    response = "Better not tell you now."
elif random_number == 7:
    response = "My sources say no."
elif random_number == 8:
    response = "Outlook not so good."
else:
    response = "Very doubtful."
print("Magic 8 Ball:", response)