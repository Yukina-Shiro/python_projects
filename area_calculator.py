print("===============")
print("Area Calculator")
print("===============")

print("")
print("1) Triangle")
print("2) Rectangle")
print("3) Square")
print("4) Circle")
print("5) Quit")


selection = int(input("Which shape: "))

# Triangle
if selection == 1:
    tri_base = int(input("Base: "))
    tri_height = int(input("Height: "))
    
    tri_result = (tri_height * tri_base) / 2
    print(f"The area is: {tri_result}")

#Rectangle
elif selection == 2:
    rec_lenght = int(input("Lenght: "))
    rec_widht = int(input("Width: "))

    rec_result = rec_lenght * rec_widht
    print(f"The area is: {rec_result}")

# Square
elif selection == 3:
    sqr_side = int(input("Side: "))

    sqr_result = sqr_side ** 2
    print(f"The area is: {sqr_result}")

# Circle
elif selection == 4:
    crl_radius = int(input("Radius: "))
    crl_pie = 3.14

    crl_result = crl_pie * (crl_radius ** 2)
    print(f"The area is: {crl_result}")

# Quit
else:
    print("Quiting...")