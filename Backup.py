def woke_intro():
    print('''You leave your bedroom and run into your roommate in the living room. She is your party friend of the group. She’s known for being mildly irresponsible and is VERY go-with-the-flow. She wants you to go out to a new bar with her. She says you could meet guys there, and it sounds like a nice break from school. You agree to go to the bar later, but right now you’re already late for work. You finish getting ready and head out the door. You arrive at the news station twenty minutes after you were expected to. As an intern, you were supposed to have the day’s reports ready and on their desks. As you’re laying them out, your colleague, Jeff, approaches you. You’ve only known him for a month or so. You’ve caught him staring at you from his desk before, and the other interns have warned you to stay away from him. He suddenly hugs you as he says, “Good morning!”''')

new2_dict = []

def hug2_code():
    condition_a = True
    while condition_a:
        hug2 = input("Do you push him off? yes/no")
        if hug2 == "yes":
            condition_a = False
            print('''You immediately push Jeff away from you. He’s visibly angry, but his anger quickly turns to smugness. “Mr. Parker’s waiting for you in his office,” he says. As you walk towards your supervisor’s office, Jeff grabs your wrist. “Wait a minute,” he says. You pull your hand away as Jeff says, “good luck”. You walk to your supervisor’s office.''')
        elif hug2 == "no":
            condition_a = False
            print('''Jeff holds you for a few uncomfortable seconds, and you realize that you should have probably listened to those interns. He lets you go and says, “Mr. Parker’s waiting for you in his office. I wouldn’t keep him waiting.” He leans in a little closer and says, “By the way...that dress was made for you.” He straightens as a co-worker passes by and says, “Well, good luck.” You quickly walk to your supervisor’s office.''')
        else:
            print("You did not put in a valid option.")

def tell2_code():
    condition_b = True
    while condition_b:
        tell2 = input("Should you tell him? yes/no")
        if tell2 == "yes":
            condition_b = False
            print('''“I...I can explain the other incidents, Mr. Parker, but I don’t know what happened this morning,” you admit. “You don’t know what happened?” he asks. “No. I went to a concert last night, I was dancing with my friends, and then there’s a whole part of the night that’s missing. I didn’t even have a drink,” you say.''')
        elif tell2 == "no":
            condition_b = False
            print('''”I...I don’t know what happened today, Mr. Parker. But I promise, it won’t happen again,” you say.''')
        else:
            print("You did not put a valid option.")

def boss2_code():
    condition_c = True
    while condition_c:
        boss2 = input("Should you try to reason with Mr. Parker or quit? reason/quit")
        if boss2 == "reason":
            condition_c = False
            print('''You remove Mr. Parker’s hand and take a few steps towards the door.
            “Mr. Parker, I really want to stay at this station, but I just can’t do that,” you say.
            “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself? I could make or break your career,” he says.
            You rush out the door, and Mr. Parker yells after you, “Don’t come back!”''')
        elif boss2 == "quit":
            condition_c = False
            print('''You quickly remove Mr. Parker’s hand and take a few steps towards the door.
            “I can’t do that, Mr. Parker,” you say.
            “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself?” he says.
            “I don’t know,” you say, “but I can’t stay at this station, either.”
            You rush out the door, and Mr. Parker yells after you, “You’re finished!”''')
        else:
            print("You did not put a valid option.")

def complaint2_code():
    condition_d = True
    while condition_d:
        complaint2 = input("Do you file a complaint before you leave? yes/no")
        if complaint2 == "yes":
            condition_d = False
            print('''You take Emma’s advice and file a complaint with Human Resources. You ask if anyone else has filed a complaint against Mr. Parker, but they tell you that information is private. They do tell you that they’ll be in contact. You meet Emma near the entrance, and she has brought two other interns with her. You all exchange contact information and plan for a future meeting. You leave the news station.''')
        elif complaint2 == "no":
            condition_d = False
            print('''You can’t seem to understand what good it would do to file a complaint, so you decide not to. Just imagine the damage that Mr. Parker could do to your career. Who would listen to you anyway? You think about the former interns...one of them must have filed a complaint, right? You walk past Emma as you leave the news station.''')
        else:
            print("You did not put a valid option.")

def eavesdrop2_continued_code():
    condition_e = True
    while condition_e:
        eavesdrop2_continued = input("'Wasn’t it great?'' one of your classmates asks. yes/no")
        if eavesdrop2_continued == "yes":
            condition_e = False
            print('''You talk about the great time you had, and the other classmate adds, “From your posts, it sure looked like you had a good time.”
            You thought there was only one picture...what else did you post?
            You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
            You look around and notice that other students are glancing at you. What happened last night?
            There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
        elif eavesdrop2_continued == "no":
            condition_e = False
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

def eavesdrop2_code():
    condition_f = True
    while condition_f:
        eavesdrop2 = input("Do you continue walking or wait where you are? continue/wait")
        if eavesdrop2 == "continue":
            condition_f = False
            print('''You continue walking and run into your two classmates.
            “Hey, you. We were just talking about the concert last night."''')
            eavesdrop2_continued_code()
        elif eavesdrop2 == "wait":
            condition_f = False
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
def take_it_code():
    condition_g = True
    while condition_g:
        take = input("Do you want to take your drink to the dance floor? yes/no")
        if take == "yes":
            condition_g = False
            new2_dict.append("took")
            print('''You take your drink to the dance floor with your friend. You might have to stay a little closer to the edge of the crowd to avoid being bumped, but you know it’s the safest option.''')
        elif take == "no":
            condition_g = False
            new2_dict.append("didn't take")
            print("Even though it’s the safest option, you don’t want to dance with your drink all night. You probably know some of these guys from college. What’s the worst that could happen? You leave your drink at the bar and go to the dance floor.")
        else:
            print("You did not put a valid option.")
def drink2_code():
    condition_h = True
    while condition_h:
        drink2 = input("Do you accept his drink? yes/no")
        if drink2 == "yes":
            condition_h = False
            new2_dict.append("accepted")
            print("You accept the drink, and the man cuts you off as you begin to order. Once he finishes ordering, you tell the bartender what you’d prefer instead.")
            print()
            print('''“I think that guy was a little strange,” your friend says. She invites you to join her on the dance floor. You consider taking your drink to the dance floor. You’ve heard of some people getting into serious trouble, and you don’t want to risk it.''')
            take_it_code()
        elif drink2 == "no":
            condition_h = False
            new2_dict.append("unaccepted")
            print('''You decline the drink, and the man slurs, “But I bought it already. You don’t know...what’s good for you…” You move further away, and you buy yourself a drink.''')
            print()
            print('''“I think we should stay away from that guy,” your friend warns you. She invites you to join her on the dance floor. You consider taking your drink to the dance floor. You’ve heard of some people getting into serious trouble, and you don’t want to risk it.''')
            take_it_code()
        else:
            print("You did not put a valid option.")
def dance2_code():
    condition_i = True
    while condition_i:
        dance2 = input("Do you dance with him? yes/no")
        if dance2 == "yes":
            condition_i = False
            print('''You feel sorry for him and accept his invitation to dance. He reaches for your arm and misses, knocking a glass over. He waves you away before walking to the other end of the bar, and you return to your friend.''')
        elif dance2 == "no":
            condition_i = False
            print("You decline his offer. He reaches for your arm and misses, knocking a glass over.")
            if "accepted" in new2_dict:
                print('''“I paid for one drink already...waste of my money. You girls think you can get anything for free.” He stumbles towards the end of the bar and sits down. You return to your friend.''')
            elif "unaccepted" in new2_dict:
                print('''"If you didn’t want me to pay for it before,” he says, “I won’t pay for it now”. He stumbles towards the end of the bar and sits down. You return to your friend.''')
        else:
            print("You did not put a valid option.")

def spiked2_code():
    condition_j = True
    while condition_j:
        spiked2 = input("Do you still want to drink it? yes/no")
        if spiked2 == "yes":
            condition_j = False
            print("You drink the remainder of your drink over a conversation with your friend.")
            print()
            print('''While your friend is gone, another man asks if you need a ride home.
            Your vision is only getting blurrier, and your friend hasn’t returned yet. You can’t seem to form any words.
            Without waiting for a response, he supports your weight as you lean against him, and he leads you out of the bar.
            This man has led you halfway down the street before your friend and a police officer come running after you.
            He suddenly drops you and runs away. Your friend cradles your head in her lap while an ambulance is called.
            Your friend apologizes profusely for the day you’ve been through. Your head is swimming, but you think about the things you could have done differently.
            You realize you might not have had a lot of decisions to make. Some things seem to be just out of your control, but there were some things you could have done differently.''')
        elif spiked2 == "no":
            condition_j = False
            print("You decide not to take any chances, and you ask the bartender for a new drink.")
            print('''You and your friend leave the bar and return to your dorm. She apologizes for the day you’ve been through, but she knows you’ll get through it.
            As you lay in bed, you reflect on your day. You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
            Some things seem to be just out of your control, but you were able to do something about it.''')
        else:
            print("You did not put a valid option.")
def woke():
    woke_intro()
    hug2_code()
    print('''You knock on the door, and Mr. Parker calls you in. He’s a well-respected man, and he has helped a lot of interns reach their ultimate goal of becoming full-time reporters or news anchors. You take a seat across from him, and he begins to speak. “You know, it takes everyone doing their work to keep this place afloat. And you’ve been late at least four times this month. Do you have a reason?” he asks. You try to remember the previous night, but there’s a section of the night that just seems to be missing. You don’t want your boss to think you’re irresponsible.''')
    tell2_code()
    print('''
    “I’m a gracious man, but I can’t allow so many mistakes from one member of this team,” he admits.
    Mr. Parker sits on his desk in front of you and continues: “I could ignore your late arrivals, but you need to make up your missing time.”
    You tell Mr. Parker that your work can’t cut into anymore of your classes.
    “That won’t be an issue. We can arrange something...you can make up the time you missed another way,” he says, putting a hand on your knee.
    Your body freezes, and you can’t believe what you’re hearing.''')
    boss2_code()
    print('''As you’re walking back to your desk, you’re still a little shocked that this is happening. First it was Jeff, and now Mr. Parker? You always knew things like this happened, and you should have known it could happen to you, too. Mr. Parker does carry a lot of influence in the news business, but you will not let him do this to anyone else. Even though you weren’t being paid a lot, you still need the money. Your scholarship doesn’t cover everything…''')
    print()
    print('''While you pack the belongings on your desk, another intern shows up. She gives you a weak smile and asks if you would like help with packing. You accept.
    “My name is Emma. I’m also an intern,” she says. You introduce yourself to Emma.
    “Did Mr. Parker make you an offer?” she asks. You look up suddenly, and she looks away.
    “I think you did the right thing...saying no. Mr. Parker thinks he owns us, but he doesn’t. We can’t be afraid of him,” she says.''')
    print()
    print('''“I won’t let him do this to anyone else,” you say. Emma smiles hopefully. “Human Resources could help you if you filed a complaint, and we could even talk to former interns about their experiences.”''')
    complaint2_code()
    print('''You arrive at your college just in time for your first class. As you’re nearing the corner of a hallway, you hear two of your classmates talking. One of your classmates mentions your name, and you stop walking before you round the corner.''')
    eavesdrop2_code()
    print('''You return to your dorm and tell your roommate about your day. How could it have gone so wrong? Last night must be the cause of your problems.
    You ask your friend what happened, but she doesn’t have any new information. She manages to convince you to go to the bar with her later that night.
    Maybe it will take your mind off of the recent chain of events. You arrive and take a seat at the bar with your friend. Several minutes pass before you are offered a drink from a nicely-dressed, good-looking man. He’s obviously intoxicated.''')
    drink2_code()
    print('''You return to the bar after a few songs have played. The guy from earlier approaches you and your friend at the bar and asks you to dance.
    He’s had a few more drinks since the last time you talked to him, and he’s slurring his words.''')
    dance2_code()
    if "took" in new2_dict:
        print("You sit back down at the bar and finish your drink over a conversation with your friend.")
        print('''You and your friend leave the bar and return to your dorm. She apologizes for the day you’ve been through, but she knows you’ll get through it.
        As you lay in bed, you reflect on your day. You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
        Some things seem to be just out of your control, but you were able to do something about it.''')
    elif "didn't take" in new2_dict:
        print("You sit back down at the bar and reach for your drink. It doesn’t look like there is anything wrong with it, but it does have a strange smell.")
        spiked2_code()
woke()
