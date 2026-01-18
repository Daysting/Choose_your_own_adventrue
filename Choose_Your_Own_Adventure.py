print(f"Hello Adventurer!  I have a tale to tell you about a young elf.  I cannot wait to share it.")
print(f"Before I can begin, I will need some information.")
print(f"After typing your answer to each question, press the enter key.")
input(f"\nPress the enter key to teleport to the new world.")
keepPlaying = "yes"
while keepPlaying.lower() == "yes":
    #first question
    gender = input(f"\nAre you a Male or Female Elf? ")
    while len(gender) == 0:
        gender - input(f"Please enter your elf's gender: ")
    #second question
    elfName = input("\nWhat is your Elf's Name? ")
    while len(elfName) == 0:
        elfName = input(f"Please enter your name: ")
    #third question
    streetName = input(f"\nWhat is the name of the street your elf lives on? ")
    while len(streetName) == 0:
        streetName = input(f"Please enter a street name: ")
    #forth question
    favoriteDrink = input(f"\nWhat do you drink to calm your nerves? ")
    while len(favoriteDrink) == 0:
        favoriteDrink - input(f"Please enter the name of your favorite drink: ")
    #fifth question
    bedTime = input("\nWhat time do you go to bed? ")
    while not bedTime.isdigit():
        bedTime = input(f"Please enter your bed time: ")
    print(f"\nWelcome to Arborlonian Traveler!")
    print(f"\nOne day, {elfName}, a {gender} elf was outside the city gates, exploreing the forest. ")
    print(f"{elfName} was having fun.  That is until they heard something coming tward them. ")
    print(f"They wished that they had a cup of {favoriteDrink}. {elfName} was completly on edge. ")
    print(f"This is because Goblins have come too close to the city's edge, and now, they are focusing on {elfName}! ")
    #decision 1
    fight = input(f"\nAs a young magic user, will you fight to protect yourself?  Type yes or no: ")
    while fight.lower() != "yes" and fight.lower() !="no":
        fight = input("Please type yes or no: ")
    if fight == "yes":
        print(f"\n{elfName} casts Fireball, throwing it at the goblins.  This causes a huge explosion! ")
        print(f"The goblins lie there, lifeless.  {elfName} catches their breath, Trying to calm themself. ")
        print(f"The explosion catches the attention of the gate guards and they run to see what has happened. ")
        print(f"One of the guards shouts, 'You! What has happened here?'  {elfName} explains what happened. ")
    else:
        print(f"\n{elfName} panics!  They start to run tward the city gates.  The goblins hot on their tail. ")
        print(f"{elfName} makes it to the gates. The guards instantly start to battle the goblins. ")
        print(f"The guards made quick work of the goblins.  One of the guards asks {elfName} where their house is. ")
        print(f"{elfName} explains that they live on {streetName}.  The guard starts to take {elfName} home. ")
        print(f"The guard asks {elfName} what happened to cause the goblins to give chase.  {elfName} tells them. ")
    #decision 2
    adventurersGuild = input(f"\nThe Adventurer's Guild will want to know what happened, does {elfName} tell them? Type yes or no: ")
    while adventurersGuild.lower() != "yes" and adventurersGuild.lower() != "no":
        adventurersGuild = input("Please type yes or no: ")
    if adventurersGuild == "yes":
        print(f"\n{elfName} Heads to the Adventurers Guild.  Once there, they tell the receptonist what happened. ")
        print(f"The receptionist states that they already know how many goblins were killed and thanks {elfName}. ")
        print(f"{elfName} went home to have a cup of {favoriteDrink} to calm their nerves. ")
    else:
        print(f"\n{elfName} went home to have a cup of {favoriteDrink}, dig into their favorite book and reflect on the day. ")
    #Alternate Endings
    if fight == "yes" and adventurersGuild == "Yes":
        print(f"\nThe receptionist then explains that the bounty for defeated goblins is 2 silver pieces! ")
        print(f"{elfName} earned 6 silver pieces as there were 3 goblins cought in the fireball's explosion. ")
    elif fight == "no" and adventurersGuild == "no":
        print(f"\n{elfName} falls asleep in their bed at {bedTime} after a long period of drinking {favoriteDrink}. ")
    else:
        print(f"{elfName} is satisfide with the results of the day. ")
        print(f"They were unaware that they could have earned a little money if they had seized every opportunity the day presented to them. ")
    keepPlaying = input(f"\nDo you want to play again? Type yes or no: ")
    while keepPlaying.lower() != "yes" and keepPlaying.lower() != "no":
        keepPlaying = input(f"please type yes or no: ")