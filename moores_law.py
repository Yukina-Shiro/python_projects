# Write code below 💖

transistors = 25000000000

years = 10


def nb_transistors(transistors, years):
    transistors = transistors * (2**(years/2))
    print(transistors)

nb_transistors(transistors, years)