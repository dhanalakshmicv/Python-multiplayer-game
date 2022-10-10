#*******************************************************************************

# Midterm Project - ANA1001
# Dhanalakshmi C V
# A00252813
#********************************************************************************
import random
import time
from os import system, name

    
   
def intro():         #intro to the game and initial 3 rooms
    clear()
    time.sleep(2)    # suspends execution of the current thread for a given seconds
    health = 100
    bag.append('water')    #appending water to the bag
    print(" you decide to go for a treasure hunt with a magical wand presented by a witch in a mountain,")
    print ("after a long walk through the mountains, the sun is about to fade")
    print("the ground is cold, damp, and covered in thick vines")
    print("since this is winter cold breeze has begun ")
    print("there are only 3 choices on this night ")
    print()
    print("1.Go back home")
    print("2.Enter the cave")
    print("3.Stay outside the cave")
    
    choice1 =input("Which choice you choose??(1/2/3) :\n")
    if choice1 == '1':
     print("oops .... bad choice as winter is soo strong you couldn't survive this night walking back to home and you die ")
    
    elif choice1 == '2':
     cave()
    elif choice1 == '3':
     forest()
    else:
     print("Invalid choice, try again....")
     intro()


def cave():     # defining the function cave 
    global health
    clear()
    health = 80
    time.sleep(2)
    print(" A dark and dreary place where the only sound that can be heard is the drip, drip, drip of water from the stalactites.")
    print ("As you take a long walk you noted you are in a hallway.......There are few paths in different directions .you got confused")
    
    print("from distance, each path ends up in different colors :red, green light, and blue which path u choose to move ahead?")
    time.sleep(2)

    print("red","blue", "green")

       
    choice2 = input("which path u choose??\n")    #user input
    
    if choice2 == "red":
      red()
    elif choice2 == "blue":
     blue()
    elif choice2 == "green":
      green()
    else:
     print ("Invalid choice")
     cave ()
     

def red():    # defing the red path room
  time.sleep(2)
  clear()
  health = 70
  print (f"Your health is  {health} % ")
  print (f"You have {bag} items in the bag ")
  print (f"Your wallet has {wallet} ")
  time.sleep(2)
  print ("you have chosen the red light when u approach the red light you could find it blinking")
  print("And it's a wolf waiting for you. To continue your hunt you want to fight with wolf and win")
  player_points,wolf_points = 0,0 
  while True:
   print(f"\n My_score: {player_points}\twolf_score: {wolf_points}\n")
   wolf =random.randint(1,4) 
   print("fighting tips s.superpunch,b.beat,p.push,k.kick")
   player =  input(f"To fight choose s/b/p/k \n\n") #giving the coose option to player
   if player == "p":  # converting choice to numbers
    player= 2
   elif player == "b":
    player= 1
   elif player == "s":
    player= 4
   elif player == "k":
    player= 3
   else:
    print()
    
    print(f"Your fight points {player} and the wolf fight points {wolf}\n") # displaying the result

       #compare the numbers and print if it's a win, loss, or tie. 
   print("begin your fight to defeat the wolf and survive")
    
   if player > wolf:
       print("player wins!")
       player_points+=1
   elif player < wolf:
       print("wolf wins!")
       wolf_points+=1
   else:
       print ("something got wrong .. try again!")
   if wolf_points ==3 or player_points == 3: # setting the limit of points as 3 to win the game
    break

  print("fighting........".center(60,"="))
  print(f"""
     
    wolf\t {wolf_points}
    player\t {player_points}
     
    """) 
      #printing the final scores
  if wolf_points < player_points:
    print(" yaaay......you killed the wolf. Collect the gold key and the code saved by the wolf")  # giving an overview of who won the game
    wallet.append('gold_key_1111') #appending key to the wallet
    health += 20
    time.sleep(5)
    last_door()      #navigating the last door of treasure
  else:
    print("wolf wins! and you died")

 
def blue():    #defining blue room
  clear()     #  clearing the screen
  time.sleep(1)
  health =70
  print (f"Your health is  {health} % ")
  print (f"You have {bag} items in the bag ")
  print (f"Your wallet has {wallet} ")

  time.sleep(2)
  print ("So you have chosen the path showing blue light.")
  print("as you walk into the blue-colored path u  noticed that is a small water body which has a blue key and the code at the center of it . What will you do to get those diamonds? ")
  print("1. Swim and get the code and key")
  print("2.Sit and think if there is a way to get it")
  print("3.Use magic stick to get the key")
  
  choice5 =input("Which choice you choose??(1/2/3) :")
  if choice5 == '1':
    print("sorry... There are deadly snakes in the waterbody and they have eaten you and you lose")
    
  elif choice5 == '2':
    print("Sorry...  you don't have enough time to sit and think. The poisonous snakes attacked and you die ")  
  elif choice5 == '3':
    print("you got the key and the code with the help of a magic wand and managed to escape from the deadly snakes")
    wallet.append('blue_key0000')    #appending key to the wallet
    health += 20
    time.sleep(5)
    last_door()
  else:
     print("Invalid choice, try again....")
     blue()

def green():
  clear()
  time.sleep(1)
  health = 70
  print (f"Your health is  {health} % ")
  print (f"You have {bag} items in the bag ")
  print (f"Your wallet has {wallet} ")
  time.sleep(2)
  print ("you are in green light path")
  print("as you walk inside you noticed a monk and it looks strange... you approched him and knew that he has a question if you answered correctly he will give you a green key and code the key for the final treasure room ")
  print("1.Try to attack him")
  print("2.Ask the question")
 
  
  time.sleep(1)
  choice6 =input("Which choice you choose??(1/2 :")
  if choice6 == '1':  #implementing the if elif conditions
   print(" Sorry... wrong decision!!!  he is soo powerful than you and killed you")
  
  elif choice6 == '2':
   time.sleep(1)
   print("Here is your question, answer wisely!!! ")
   time.sleep(1)
   choice7=input("Which is faster light or brain?")  
   if choice7 == "light":
     print("wow.. you got the right answer and got the green key with code ")
     print("you got the real treasure room key")
     wallet.append('green_key1010')   #appending key to the wallet
     health += 20              #power up  from winning the game
     time.sleep(5)
     last_door()
     
   elif choice7 == "brain":
    print("you lose...light is faster than brain. better luck next time!!")
    print("you attacked him for the key with your wand .he is more powerful and you die ")
   else :
      print("invalid")
      green()

def last_door():
  clear()
  print ("Now you are in final room door")
  time.sleep(3)
  print (f"you are in {health}% health and have {wallet} keys in the wallet")
  time.sleep(3)    
  code = input("Please enter your key code?")
  if code == '0000':
    print("you are awesome!!! Successfully completed the task and got access to the last treasure room ")
  elif code == '1111':
    print("you are awesome!!! Successfully completed the task and got access to the last treasure room ")
  elif code == '1010':
        print("you are awesome!!! Successfully completed the task and got access to the last treasure room ")
  else:
    print ("Try again")
    last_door()

########################################

def forest():
    time.sleep(1)
    clear()
    health = 50   
    print ("you decided to stay out of the cave and sit in the nearby rock")
    print (f"Your health is  {health} % ")
    print (f"You have {bag} items in the bag ")
    print (f"Your wallet pocess {wallet} ")
  
    print ("After some time, you hear crawling noises and something moved in the dark it was a trespasser(magician). will you talk to him yes/no??")
    choice4 = input("(Y/N): ")
    if choice4 == 'y' or choice4 == 'Y':
     print("you explained to him about the treasure hunt and he got impressed and gave you a magical sword for your adventure ")
     bag.append('sword')
      
     print ("now you got a magical stick for your adventure t a courage to enter the cave and decided to enter the cave")
     time.sleep(2)
     cave()
    
    elif choice4 == 'n' or choice4 == 'N':
     print ("You were hesitant, and missed to talk with a magician")
     health -= 50
     print (f"it was freezing cold and your health went down {health}% and you died")   # printing the health bag and wallet indicators
    
    else:
     print ("something got wrong .. action required")
     forest()
  
    choice4 = input("Would you enter the cave? (Y/N): ")
    if choice4 == 'n' or choice4 == 'N':
     print("oops!!! you are eaten by flesh-eating monsters")
    elif choice4 == 'y' or choice4 == 'Y':
     cave()
    else:
     print ("something got wrong .. action required")
     forest()

###############################################################################


print(f"**************************** Welcome to the adventure game!!!***********\n")

print("**************************************************************************")

print(".............................Secret keys.................................")

print("**************************************************************************")


time.sleep(3)

name = input ("what is your name?\n")

time.sleep(1)
# define our clear function
def clear():
    if name == 'nt':    # for windows
        _ = system('cls')
    else:
        _ = system('clear')     # for mac and linux(here, os.name is 'posix')


while True:      # starting the game with the while loop
  global health, bag, wallet
  bag = []
  wallet =[]   #assigning the empty lists to wallet and bag
  health = 100  # health indicator
  time.sleep(3)
  startgame = input("Would you like to start your game? (Y/N): ")
  if startgame == 'n' or startgame == 'N':
   print("May b next time!!")
   break
  elif startgame == 'y' or startgame == 'Y':
   intro()     
  else:
   break
  






   




 
