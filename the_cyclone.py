# Write code below 💖
height = int(input("height ?"))
credits = int(input("credits ?"))
# the height requirement is 137 cm and the cost is 10 credits
if height >= 137 and credits >= 10 :
  print("Enjoy the ride!")
elif credits >= 10 and height <= 137 :
  print("You are not tall enough to ride.")
elif height >= 137 and credits <= 10 :
  print("You don't have enough credits.")
else :
  print("You have not met either requirement.")

