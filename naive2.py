print('''You leave your bedroom and run into your roommate in the living room. She is your party friend of the group. She’s known for being mildly irresponsible and is VERY go-with-the-flow. She wants you to go out to a new bar with her. She says you could meet guys there, and it sounds like a nice break from school. You agree to go to the bar later, but right now you’re already late for work. You finish getting ready and head out the door. You arrive at the news station twenty minutes after you were expected to. As an intern, you were supposed to have the day’s reports ready and on their desks. As you’re laying them out, your colleague, Jeff, approaches you. You’ve only known him for a month or so. You sometimes catch him staring at you from his desk, but your colleagues only have good things to say about him. He suddenly hugs you as he says, “Good morning!”''')

new1_dict = []

def hug1_code():
    first_condition = True
    while first_condition:
        hug1 = input("Do you push him off? a) yes or b) no")
        if hug1 == "yes":
            first_condition = False
            print('''You push Jeff away and take a step back. He has an injured look on his face, but it is quickly replaced by concern. He says, “Mr. Parker’s waiting for you in his office.” You thank him and quickly walk towards your supervisor’s office.''')
        elif hug1 == "no":
            first_condition = False
            print('''Jeff holds you for one more uncomfortable second before letting go. He looks a little concerned while he says, “Mr. Parker’s waiting for you in his office.” You thank him and quickly walk towards your supervisor’s office.''')
        else:
            print("You did not put in a valid option.")

def tell1_code():
    second_condition = True
    while second_condition:
        tell1 = input("Should you tell him? yes/no")
        if tell1 == "yes":
            second_condition = False
            print('''“I...I can explain the other incidents, Mr. Parker, but I don’t know what happened this morning,” you admit. “You don’t know what happened?” he asks. “No. I went to a concert last night, I was dancing with my friends, and then there’s a whole part of the night that’s missing. I didn’t even have a drink,” you say.''')
        elif tell1 == "no":
            second_condition = False
            print('''”I...I don’t know what happened today, Mr. Parker. But I promise, it won’t happen again,” you say.''')
        else:
            print("You did not put a valid option.")

def boss1_code():
    third_condition = True
    while third_condition:
        boss1 = input("Should you try to reason with Mr. Parker or quit? reason/quit")
        if boss1 == "reason":
            third_condition = False
            print('''You remove Mr. Parker’s hand and take a few steps towards the door.
            “Mr. Parker, I really want to stay at this station, but I just can’t do that,” you say.
            “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself? I could make or break your career,” he says.
            You rush out the door, and Mr. Parker yells after you, “Don’t come back!”''')
        elif boss1 == "quit":
            third_condition = False
            print('''You quickly remove Mr. Parker’s hand and take a few steps towards the door.
            “I can’t do that, Mr. Parker,” you say.
            “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself?” he says.
            “I don’t know,” you say, “but I can’t stay at this station, either.”
            You rush out the door, and Mr. Parker yells after you, “You’re finished!”''')
        else:
            print("You did not put a valid option.")

def complaint1_code():
    fourth_condition = True
    while fourth_condition:
        complaint1 = input("Do you file a complaint before you leave? yes/no")
        if complaint1 == "yes":
            fourth_condition = False
            print('''You take Emma’s advice and file a complaint with Human Resources. You ask if anyone else has filed a complaint against Mr. Parker, but they tell you that they’re not at liberty to give out that information. They do tell you that they’ll be in contact. Emma gives you her contact information, and you leave the news station.''')
        elif complaint1 == "no":
            fourth_condition = False
            print('''You can’t seem to understand what good it would do to file a complaint, so you decide not to. Just imagine the damage that Mr. Parker could do to your career. You think about the former interns...one of them must have filed a complaint, right? You walk past Emma as you leave the news station.''')
        else:
            print("You did not put a valid option.")

def eavesdrop1_continued_code():
    fifth_condition = True
    while fifth_condition:
        eavesdrop1_continued = input("'Wasn’t it great?'' one of your classmates asks. yes/no")
        if eavesdrop1_continued == "yes":
            fifth_condition = False
            print('''You talk about the great time you had, and the other classmate adds, “From your posts, it sure looked like you had a good time.”
            You thought there was only one picture...what else did you post?
            You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
            You look around and notice that other students are glancing at you. What happened last night?
            There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
        elif eavesdrop1_continued == "no":
            fifth_condition = False
            print('''You admit that you don’t really remember what happened at the concert.
            “Sure, sure. I never thought you’d let yourself go like that. You didn’t strike me as a party animal.
            Have you called that guy back yet?” one classmate asks.
            “What guy?” you respond.
            “Right...playing it cool. See you inside,” they say.
            You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
            You look around and notice that other students are glancing at you. What happened with that guy last night?
            There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
        else:
            print("You did not put a valid option.")

def eavesdrop1_code():
    sixth_condition = True
    while sixth_condition:
        eavesdrop1 = input("Do you continue walking or wait where you are? continue/wait")
        if eavesdrop1 == "continue":
            sixth_condition = False
            print('''You continue walking and run into your two classmates.
            “Hey, you. We were just talking about the concert last night."''')
            eavesdrop1_continued_code()
        elif eavesdrop1 == "wait":
            sixth_condition = False
            print('''"You wait in the hallway and listen to your classmates, who are unaware that you’re just around the corner.
            “That was a crazy concert. Some people really let themselves go last night,” one classmate says. They begin to talk about you.
            “Did you see the guy she was with? I don’t think he goes here, and he never let her out of his sight.”
            “Forget about the guy, did you see her? She really didn’t seem all there...I don’t think she knew him. It was really out of character.”
            “Well, was she drunk?”
            “She never drinks!”
            “What was she wearing?”
            “Are you joking? That doesn’t mean anything. You know better than that.”
            “I’m just saying...we don’t really know what happened.”
            You continue walking and run into your two classmates.
            “Hey, you. .We were just talking about...the concert.”
            “Have you called that guy back yet?”
            Quit bothering her. See you inside, alright?”
            You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
            You look around and notice that other students are glancing at you. What happened with that guy last night?
            There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
        else:
            print("You did not put a valid option.")
def watch_it1_code():
    seventh_condition = True
    while seventh_condition:
        watch1 = input("Do you want to dance and watch your drink? yes/no")
        if watch1 == "yes":
            seventh_condition = False
            new1_dict.append("watched")
            print('''You leave your drink and go to the dance floor with your friend, but you make sure to stay close to the edge of the crowd.
            You’re able to see the bar and your drink while you’re dancing, but your friend feels like you’re distracted.''')
        elif watch1 == "no":
            seventh_condition = False
            new1_dict.append("didn't watch")
            print("You drink the rest of your drink before joining your friend on the dance floor.")
        else:
            print("You did not put a valid option.")
def drink1_code():
    eighth_condition = True
    while eighth_condition:
        drink1 = input("Do you accept his drink? yes/no")
        if drink1 == "yes":
            eighth_condition = False
            new1_dict.append("accepted")
            print("You accept the drink, and the man cuts you off as you begin to order. You think to yourself, 'If he’s buying, he’s ordering, right?'")
            print()
            print('''"That wasn’t so bad, huh?” your friend asks. She invites you to join her on the dance floor. You think about leaving the drink at the bar in order to dance. You’re sure it’ll be safe, and you’ll only be gone for a little while. Do you want to leave your drink?''')
            watch_it1_code()
        elif drink1 == "no":
            eighth_condition = False
            new1_dict.append("unaccepted")
            print("You decline the drink, and the man mutters, 'Are you sure? I already bought it.' You decline again, and he says, 'If that’s what you want...fine. By the way you’re dressed, I thought you came for free drinks.' He leaves the bar, and you buy yourself a drink.")
            print('''“That guy was terrible. Try to forget about him,” your friend advises.
            She invites you to join her on the dance floor. You think about leaving your drink and watching it from the dance floor.
            You won’t be that far from it, and nobody would try anything when you’re so close to the bar.''')
            watch_it1_code()
        else:
            print("You did not put a valid option.")
def dance1_code():
    ninth_condition = True
    while ninth_condition:
        dance1 = input("Do you dance with him? yes/no")
        if dance1 == "yes":
            ninth_condition = False
            print('''He tightly grasps your arm as he leads you to the dance floor. He continues to hold onto as you two start to dance.
            You push him off and hurry back to your friend.''')
        elif dance1 == "no":
            ninth_condition = False
            print("You decline his offer. He glares at you for a few seconds, but his expression softens.")
            if "accepted" in new1_dict:
                print('''He puts his hand on your shoulder and says, "You’ll accept a drink but you won’t dance with me? Talk about getting a guy’s hopes up.
                Some people would say you owe me." You jerk your shoulder back and turn to your friend.''')
            elif "unaccepted" in new1_dict:
                print("He puts his hand on your shoulder and says, 'If you didn’t come to drink and you didn’t come to dance, what are you here for? You shouldn’t get a guy’s hopes up.' You jerk your shoulder back and turn to your friend.")
        else:
            print("You did not put a valid option.")

def spiked1_code():
    tenth_condition = True
    while tenth_condition:
        spiked1 = input("Do you still want to drink it? yes/no")
        if spiked1 == "yes":
            tenth_condition = False
            print("You drink the remainder of your drink over a conversation with your friend.")
            print()
            print('''While your friend is gone, another man asks if you need a ride home.
            Your vision is only getting blurrier, and your friend hasn’t returned yet. You can’t seem to form any words.
            Without waiting for a response, he supports your weight as you lean against him, and he leads you out of the bar.
            This man has led you halfway down the street before your friend and a police officer come running after you.
            He suddenly drops you and runs away. Your friend cradles your head in her lap while an ambulance is called.
            Your friend apologizes profusely for the day you’ve been through. Your head is swimming, but you think about the things you could have done differently.
            You realize you might not have had a lot of decisions to make. Some things seem to be just out of your control, but there were some things you could have done differently.''')
        elif spiked1 == "no":
            tenth_condition = False
            print("You decide not to take any chances, and you ask the bartender for a new drink.")
            print('''You and your friend leave the bar and return to your dorm. She apologizes for the day you’ve been through, but she knows you’ll get through it.
            As you lay in bed, you reflect on your day. You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
            Some things seem to be just out of your control, but you were able to do something about it.''')
        else:
            print("You did not put a valid option.")
def naive():
    hug1_code()
    print('''You knock on the door, and Mr. Parker calls you in. He’s a well-respected man, and he has helped a lot of interns reach their ultimate goal of becoming full-time reporters or news anchors. You take a seat across from him, and he begins to speak. “You know, it takes everyone doing their work to keep this place afloat. And you’ve been late at least four times this month. Do you have a reason?” he asks. You try to remember the previous night, but there’s a section of the night that just seems to be missing. You don’t want your boss to think you’re irresponsible.''')
    tell1_code()
    print('''
    “I’m a gracious man, but I can’t allow so many mistakes from one member of this team,” he admits.
    Mr. Parker sits on his desk in front of you and continues: “I could ignore your late arrivals, but you need to make up your missing time.”
    You tell Mr. Parker that your work can’t cut into anymore of your classes.
    “That won’t be an issue. We can arrange something...you can make up the time you missed another way,” he says, putting a hand on your knee.
    Your body freezes, and you can’t believe what you’re hearing.''')
    boss1_code()
    print('''As you’re walking back to your desk, you’re still shocked that this is happening.
    First it was Jeff, and now Mr. Parker? You never thought something like this could happen to you. What do you do now? You weren’t being paid a lot, but you need the money.
    Your scholarship doesn’t cover everything…''')
    print()
    print('''While you pack the belongings on your desk, another intern shows up. She gives you a weak smile and asks if you would like help with packing. You accept.
    “My name is Emma. I’m also an intern,” she says. You introduce yourself to Emma.
    “Did Mr. Parker make you an offer?” she asks. You look up suddenly, and she looks away.
    “I think you did the right thing...saying no. Mr. Parker thinks he owns us, but he doesn’t. We can’t be afraid of him,” she says.''')
    print()
    print('''“I don’t know what to do,” you say. Emma lets out a sigh, and her shoulders sag a little. “Maybe you could file a complaint before you leave? Human Resources could help you.”''')
    complaint1_code()
    print('''You arrive at your college just in time for your first class. As you’re nearing the corner of a hallway, you hear two of your classmates talking. One of your classmates mentions your name, and you stop walking before you round the corner.''')
    eavesdrop1_code()
    print('''You return to your dorm and tell your roommate about your day. How could it have gone so wrong? Last night must be the cause of your problems.
    You ask your friend what happened, but she doesn’t have any new information. She manages to convince you to go to the bar with her later that night.
    Maybe it will take your mind off of the recent chain of events. You arrive and take a seat at the bar with your friend. Several minutes pass before you are offered a drink from a nicely-dressed, good-looking man. He seems trustworthy.''')
    drink1_code()
    print('''You return to the bar after a few songs have played. The guy from earlier approaches you and asks you to dance. He hasn’t been a perfect gentleman, but you could give him a second chance.''')
    dance1_code()
    if "watched" in new1_dict:
        print("You sit back down at the bar and reach for your drink. It doesn’t look like there is anything wrong with it, and you were able to watch it from the dance floor.")
        spiked1_code()
    elif "didn't watch" in new1_dict:
        print("You sit back down at the bar and have a conversation with your friend. Your friend tells you to wait for her while she uses the restroom.")
        print()
        print('''You and your friend leave the bar and return to your dorm.
        She apologizes for the day you’ve been through, but she knows you’ll get through it. As you lay in bed, you reflect on your day.
        You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
        Some things seem to be just out of your control, but you were able to do something about it.''')
naive()
