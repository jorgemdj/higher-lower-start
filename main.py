from game_data import data
import random
from art import logo, vs
import os

def profile_info(dataset):
  list = []
  list.append(dataset["name"])
  list.append(dataset["follower_count"])
  list.append(dataset["description"])
  list.append(dataset["country"])
  return list


print(logo)
id = random.randint(0,len(data)-1)
A = data.pop(id)
game = True
cont = 0

while game == True:
  id = random.randint(0,len(data)-1)
  B = data.pop(id)
  print(f"Compare A: {profile_info(A)[0]}, a {profile_info(A)[2]}, from {profile_info(A)[3]}")
  
  print(vs)
  
  print(f"Compare B: {profile_info(B)[0]}, a {profile_info(B)[2]}, from {profile_info(B)[3]}")

  ans = input("Who has more followers? Type 'A' or 'B: ").lower()
  
  if (ans == "a" and profile_info(A)[1] > profile_info(B)[1]):
    cont += 1
    os.system('cls')
    print(logo)
    print(f"You're right! Current score: {cont}")
    
  elif (ans == "b" and profile_info(B)[1] > profile_info(A)[1]):
    cont += 1
    os.system('cls')
    print(logo)
    print(f"You're right! Current score: {cont}")
    A = B   
    
  else:
      game = False
