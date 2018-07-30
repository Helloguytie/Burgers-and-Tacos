def space():
    i = 0
    while i < 2:
        print()
        i += 1

def naive():
    print("This is a test; you're naive")
def aware():
    print("This is a test; you're aware")
def woke():
    print("This is a test; you're woke")

college = input("What college do you want to attend?")
print ("You are a 20 year old female that is currently attending "+college+".")
print("You live in a dorm with your friends and experience various challeneges everyday, but today is different...")
space()
print ("You get to decide your fate! Choose wisely.")
print ("You are in your dorm room. You went to a concert, and you remember that a person bumped into you after the concert. Your wallet is missing.")

naive_count = 0
aware_count = 0
woke_count = 0

def personality():
    global woke_count, aware_count, naive_count
    if naive_count > aware_count:
        naive()
    elif naive_count > woke_count:
        naive()
    elif aware_count > naive_count:
        aware()
    elif aware_count > woke_count:
        aware()
    elif woke_count > naive_count:
        woke()
    elif woke_count > aware_count:
        woke()

def window_code ():
    global naive_count
    global woke_count
    global aware_count
    condition2 = True
    while condition2:
        window = input("Do you want to d) leave it open, e) close it, or f) lock your window?")
        if window == "d":
            condition2 = False
            naive_count += 1
            print ("*breathes in* 'It's a nice day out', you say.")
            door_code()
        elif window == "e":
            condition2 = False
            aware_count += 1
            print ("'There's a lot of people out there', you say as you close the window.")
            door_code()
        elif window == "f":
            condition2 = False
            woke_count += 1
            print ("'There are too many people out there', you say as you lock the window.")
            door_code()
        else:
            print("You did not put in a valid option.")

def door_code():
    global naive_count
    global woke_count
    global aware_count
    condition3 = True
    while condition3:
        door = input("Your door is unlocked. Do you want to g) leave it unlocked h) close it, or i) lock it?")
        if door == "g":
            condition3 = False
            naive_count += 1
            print ("'My roommate probably forgot', you say and walk back to your bed.")
            space()
            print ("You check your phone and see that your family has left you texts and voicemails.")
            print ("They tell you to check your Instagram.")
            photo_code()
        elif door == "h":
            condition3 = False
            aware_count += 1
            print ("'I should close it' you say as walk over to the door and walk back over to your bed.")
            space()
            print ("You check your phone and see that your family has left you texts and voicemails.")
            print ("They tell you to check your Instagram.")
            photo_code()
        elif door == "i":
            condition3 = False
            woke_count += 1
            print ("'I defintely closed this before I slept', you say as you lock the door and walk back over to your bed.")
            space()
            print ("You check your phone and see that your family has left you texts and voicemails.")
            print ("They tell you to check your Instagram.")
            photo_code()
        else:
            print("You did not put in a valid option.")
def photo_code():
    global naive_count
    global woke_count
    global aware_count
    condition4 = True
    while condition4:
        photo = input("A picture from the concert last night shows a stranger with his arm around you, and you look confused and tired. Do you want to j) keep the photo public k) make the photo private or l) delete the picture and save it to your phone?")
        if photo == "j":
            condition4 = False
            naive_count += 1
            personality()
        elif photo == "k":
            condition4 = False
            aware_count += 1
            personality()
        elif photo == "l":
            condition4 = False
            woke_count += 1
            personality()
        else:
            print("You did not put in a valid option.")



def wallet_code ():
    global naive_count
    global woke_count
    global aware_count

    condition1 = True
    while condition1:
        wallet = input("What do you think you did with your wallet?"
        " a) you misplaced it b) your friend took it c) the person took it" " Choose one of the following.")

        if wallet == "a":
            condition1 = False
            naive_count += 1
            print ("You notice that your window is open.")
            window_code()
        elif wallet == "b":
            condition1 = False
            aware_count += 1
            print ("You notice that your window is open.")
            window_code()
        elif wallet == "c":
            condition1 = False
            woke_count += 1
            print ("You notice that your window is open.")
            window_code()
        else:
            print("You did not put in a valid option.")

wallet_code()
