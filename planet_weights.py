# Write code below 💖

earth_weight = float(input("Enter you Earth weight : "))

planet_nb = int(input("Enter a planet number : "))

# destination_weight = earth_weight * relative_gravity
if planet_nb == 1:
  destination_weight = earth_weight * 0.38
  print("Your weight on Mercury would be : ")
  print(destination_weight)
elif planet_nb == 2:
  destination_weight = earth_weight * 0.91
  print("Your weight on Venus would be : ")
  print(destination_weight)
elif planet_nb == 3:
  destination_weight = earth_weight * 0.38
  print("Your weight on Mars would be : ")
  print(destination_weight)
elif planet_nb == 4:
  destination_weight = earth_weight * 2.53
  print("Your weight on Jupiter would be : ")
  print(destination_weight)
elif planet_nb == 5:
  destination_weight = earth_weight * 1.07
  print("Your weight on Saturn would be : ")
  print(destination_weight)
elif planet_nb == 6:
  destination_weight = earth_weight * 0.89
  print("Your weight on Uranus would be : ")
  print(destination_weight)
elif planet_nb == 7:
  destination_weight = earth_weight * 	1.14
  print("Your weight on Neptune would be : ")
  print(destination_weight)
else:
  print('Invalid number')
