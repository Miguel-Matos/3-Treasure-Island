print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

direction = input("Do you want to go left or right?\n").lower()

if direction == "left":
    choice = input("Well my dude there is a lake blocking your way. Do you swim or wait?\n").lower()
    if choice == "wait":
        print('''
         ______
     ,-' ;  ! `-.
      / :  !  :  . \\
    |_ ;   __:  ;  |
    )| .  :)(.  !  |
     |"    (##)  _  |
    |  :  ;`'  (_) (
    |  :  :  .     |
    )_ !  ,  ;  ;  |
    || .  .  :  :  |
     |" .  |  :  .  |
    |mt-2_;----.___|
    ''')
        door = input("Well damn global warming did it's magic and dried up the lake! You walk across and see a red door, green door, and a blue door. Which color door do you choose?\n").lower()
        if door == "green" or door == "the green door" or door == "green door":
            print("You go in the room and find the treasure. You use it to pay off your student loans and use the rest to by a soda or something. \n Good job!")
        else:
            print('The room is filled with monitors displaying the Netflix "Are you still there?" screen. \n You know the one where you can see yourself in the reflection and contemplate your life choices. That one. \n Anyways you walk out and go home not realizing you totally could have checked out what was behind the other doors. \n Game over ')
    else:
        print("Well it turns out that by swimming you ended up ruining your phone and for some reason your credit score. You decide to take your soggy existence home.\n Game Over")

else:
    print("I don't know why, but it is game over. Go left next time.")



