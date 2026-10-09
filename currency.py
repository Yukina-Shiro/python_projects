# Write code below 💖
p = float(input("What do you have left in pesos? "))
s = float(input("What do you have left in soles? "))
r = float(input("What do you have left in reais? "))

# Convert the amounts to USD
u = (p * 0.00031) + (s * 0.29) + (r * 0.20)

# Print the total amount in USD
print(f"{u:.2f}")
