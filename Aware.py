def aware_intro():
    print('''You leave your bedroom and run into your roommate in the living room. She is your party friend of the group. She’s known for being mildly irresponsible and is VERY go-with-the-flow. She wants you to go out to a new bar with her. She says you could meet guys there, and it sounds like a nice break from school. You agree to go to the bar later, but right now you’re already late for work. You finish getting ready and head out the door. You arrive at the news station twenty minutes after you were expected to. As an intern, you were supposed to have the day’s reports ready and on their desks. As you’re laying them out, your colleague, Jeff, approaches you. You’ve only known him for a month or so. You sometimes catch him staring at you from his desk, but your colleagues only have good things to say about him. He suddenly hugs you as he says, “Good morning!”''')

new_dict = []

def hug_code():
    condition5 = True
    while condition5:
        hug = input("Do you push him off? yes/no")
        if hug == "yes":
            condition5 = False
            print('''You quickly push Jeff away from you. He’s visibly angry, but his expression clears. He says, “Mr. Parker’s waiting for you in his office.” As you walk towards your supervisor’s office, Jeff grabs your wrist. “Wait a minute,” he says. You ask what he wants, and he whispers, “good luck” before you pull away and walk to your supervisor’s office.''')
        elif hug == "no":
            condition5 = False
            print('''Jeff holds you for a few uncomfortable seconds before letting go. He looks a little concerned while he says, “Mr. Parker’s waiting for you in his office.” As you’re walking towards your supervisor’s office, Jeff calls out “good luck!” You turn back to him as you reach the office, and Jeff is still watching you.''')
        else:
            print("You did not put in a valid option.")

def tell_code():
    condition6 = True
    while condition6:
        tell = input("Should you tell him? yes/no")
        if tell == "yes":
            condition6 = False
            print('''“I...I can explain the other incidents, Mr. Parker, but I don’t know what happened this morning,” you admit. “You don’t know what happened?” he asks. “No. I went to a concert last night, I was dancing with my friends, and then there’s a whole part of the night that’s missing. I didn’t even have a drink,” you say.''')
        elif tell == "no":
            condition6 = False
            print('''”I...I don’t know what happened today, Mr. Parker. But I promise, it won’t happen again,” you say.''')
        else:
            print("You did not put a valid option.")

def boss_code():
    condition7 = True
    while condition7:
        boss = input("Should you try to reason with Mr. Parker or quit? reason/quit")
        if boss == "reason":
            condition7 = False
            print('''You remove Mr. Parker’s hand and take a few steps towards the door.
            “Mr. Parker, I really want to stay at this station, but I just can’t do that,” you say.
            “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself? I could make or break your career,” he says.
            You rush out the door, and Mr. Parker yells after you, “Don’t come back!”''')
        elif boss == "quit":
            condition7 = False
            print('''You quickly remove Mr. Parker’s hand and take a few steps towards the door.
            “I can’t do that, Mr. Parker,” you say.
            “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself?” he says.
            “I don’t know,” you say, “but I can’t stay at this station, either.”
            You rush out the door, and Mr. Parker yells after you, “You’re finished!”''')
        else:
            print("You did not put a valid option.")

def complaint_code():
    condition8 = True
    while condition8:
        complaint = input("Do you file a complaint before you leave? yes/no")
        if complaint == "yes":
            condition8 = False
            print('''You take Emma’s advice and file a complaint with Human Resources.
            You ask if anyone else has filed a complaint against Mr. Parker, but they tell you that they’re not at liberty to give out that information.
            They do tell you that they’ll be in contact. Emma gives you her contact information, and you leave the news station.''')
        elif complaint == "no":
            condition8 = False
            print('''You can’t seem to understand what good it would do to file a complaint, so you decide not to.
            Just imagine the damage that Mr. Parker could do to your career.
            You think about the former interns...one of them must have filed a complaint, right?
            You walk past Emma as you leave the news station.''')
        else:
            print("You did not put a valid option.")

def eavesdrop_continued_code():
    condition10 = True
    while condition10:
        eavesdrop_continued = input("'Wasn’t it great?'' one of your classmates asks. yes/no")
        if eavesdrop_continued == "yes":
            condition10 = False
            print('''You talk about the great time you had, and the other classmate adds, “From your posts, it sure looked like you had a good time.”
            You thought there was only one picture...what else did you post?
            You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
            You look around and notice that other students are glancing at you. What happened last night?
            There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
        elif eavesdrop_continued == "no":
            condition10 = False
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

def eavesdrop_code():
    condition9 = True
    while condition9:
        eavesdrop = input("Do you continue walking or wait where you are? continue/wait")
        if eavesdrop == "continue":
            condition9 = False
            print('''You continue walking and run into your two classmates.
            “Hey, you. We were just talking about the concert last night."''')
            eavesdrop_continued_code()
        elif eavesdrop == "wait":
            condition9 = False
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
def watch_it_code():
    condition12 = True
    while condition12:
        watch = input("Do you want to dance and watch your drink? yes/no")
        if watch == "yes":
            condition12 = False
            new_dict.append("watched")
            print('''You leave your drink and go to the dance floor with your friend, but you make sure to stay close to the edge of the crowd.
            You’re able to see the bar and your drink while you’re dancing, but your friend feels like you’re distracted.''')
        elif watch == "no":
            condition12 = False
            new_dict.append("didn't watch")
            print("You drink the rest of your drink before joining your friend on the dance floor.")
        else:
            print("You did not put a valid option.")
def drink_code():
    condition11 = True
    while condition11:
        drink = input("Do you accept his drink? yes/no")
        if drink == "yes":
            condition11 = False
            new_dict.append("accepted")
            print("You accept the drink, and the man cuts you off as you begin to order. You think to yourself, 'What a jerk.'")
            print()
            print('''"Man, that guy was a jerk,” your friend says with a laugh. She invites you to join her on the dance floor.
            You think about leaving your drink and watching it from the dance floor.
            You won’t be that far from it, and nobody would try anything when you’re so close to the bar.''')
            watch_it_code()
        elif drink == "no":
            condition11 = False
            new_dict.append("unaccepted")
            print("You decline the drink, and the man mutters, 'Are you sure? I already bought it.' You decline again, and he says, 'If that’s what you want...fine. By the way you’re dressed, I thought you came for free drinks.' He leaves the bar, and you buy yourself a drink.")
            print('''“That guy was terrible. Try to forget about him,” your friend advises.
            She invites you to join her on the dance floor. You think about leaving your drink and watching it from the dance floor.
            You won’t be that far from it, and nobody would try anything when you’re so close to the bar.''')
            watch_it_code()
        else:
            print("You did not put a valid option.")
def dance_code():
    condition12 = True
    while condition12:
        dance = input("Do you dance with him? yes/no")
        if dance == "yes":
            condition12 = False
            print('''He tightly grasps your arm as he leads you to the dance floor. He continues to hold onto as you two start to dance.
            You push him off and hurry back to your friend.''')
        elif dance == "no":
            condition12 = False
            print("You decline his offer. He glares at you for a few seconds, but his expression softens.")
            if "accepted" in new_dict:
                print('''He puts his hand on your shoulder and says, "You’ll accept a drink but you won’t dance with me? Talk about getting a guy’s hopes up.
                Some people would say you owe me." You jerk your shoulder back and turn to your friend.''')
            elif "unaccepted" in new_dict:
                print("He puts his hand on your shoulder and says, 'If you didn’t come to drink and you didn’t come to dance, what are you here for? You shouldn’t get a guy’s hopes up.' You jerk your shoulder back and turn to your friend.")
        else:
            print("You did not put a valid option.")

def spiked_code():
    condition13 = True
    while condition13:
        spiked = input("Do you still want to drink it? yes/no")
        if spiked == "yes":
            condition13 = False
            print("You drink the remainder of your drink over a conversation with your friend.")
            print()
            print('''While your friend is gone, another man asks if you need a ride home.
            Your vision is only getting blurrier, and your friend hasn’t returned yet. You can’t seem to form any words.
            Without waiting for a response, he supports your weight as you lean against him, and he leads you out of the bar.
            This man has led you halfway down the street before your friend and a police officer come running after you.
            He suddenly drops you and runs away. Your friend cradles your head in her lap while an ambulance is called.
            Your friend apologizes profusely for the day you’ve been through. Your head is swimming, but you think about the things you could have done differently.
            You realize you might not have had a lot of decisions to make. Some things seem to be just out of your control, but there were some things you could have done differently.''')
        elif spiked == "no":
            condition13 = False
            print("You decide not to take any chances, and you ask the bartender for a new drink.")
            print('''You and your friend leave the bar and return to your dorm. She apologizes for the day you’ve been through, but she knows you’ll get through it.
            As you lay in bed, you reflect on your day. You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
            Some things seem to be just out of your control, but you were able to do something about it.''')
        else:
            print("You did not put a valid option.")
def aware():
    aware_intro()
    hug_code()
    print('''You knock on the door, and Mr. Parker calls you in. He’s a well-respected man, and he has helped a lot of interns reach their ultimate goal of becoming full-time reporters or news anchors. You take a seat across from him, and he begins to speak. “You know, it takes everyone doing their work to keep this place afloat. And you’ve been late at least four times this month. Do you have a reason?” he asks. You try to remember the previous night, but there’s a section of the night that just seems to be missing. You don’t want your boss to think you’re irresponsible.''')
    tell_code()
    print('''
    “I’m a gracious man, but I can’t allow so many mistakes from one member of this team,” he admits.
    Mr. Parker sits on his desk in front of you and continues: “I could ignore your late arrivals, but you need to make up your missing time.”
    You tell Mr. Parker that your work can’t cut into anymore of your classes.
    “That won’t be an issue. We can arrange something...you can make up the time you missed another way,” he says, putting a hand on your knee.
    Your body freezes, and you can’t believe what you’re hearing.''')
    boss_code()
    print('''As you’re walking back to your desk, you’re still a little shocked that this is happening.
    First it was Jeff, and now Mr. Parker? You should have known something like this could happen, but you never thought about it before.
    Mr. Parker does carry a lot of influence in the news business, but maybe you could do something to stop him.
    What do you do know? Of course you weren’t being paid a lot, but you need the money. Your scholarship doesn’t cover everything…''')
    print()
    print('''While you pack the belongings on your desk, another intern shows up. She gives you a weak smile and asks if you would like help with packing. You accept.
    “My name is Emma. I’m also an intern,” she says. You introduce yourself to Emma.
    “Did Mr. Parker make you an offer?” she asks. You look up suddenly, and she looks away.
    “I think you did the right thing...saying no. Mr. Parker thinks he owns us, but he doesn’t. We can’t be afraid of him,” she says.''')
    print()
    print('''“I don’t want anyone else to go through this, but I don’t know what to do,” you admit.
    Emma lets out a sigh. “Human Resources might be able to help if you filed a complaint. Maybe former interns would come forward as well.”''')
    complaint_code()
    print('''You arrive at your college just in time for your first class. As you’re nearing the corner of a hallway, you hear two of your classmates talking. One of your classmates mentions your name, and you stop walking before you round the corner.''')
    eavesdrop_code()
    print('''You return to your dorm and tell your roommate about your day. How could it have gone so wrong? Last night must be the cause of your problems.
    You ask your friend what happened, but she doesn’t have any new information. She manages to convince you to go to the bar with her later that night.
    Maybe it will take your mind off of the recent chain of events. You arrive and take a seat at the bar with your friend. Several minutes pass before you are offered a drink from a nicely-dressed, good-looking man. He seems a little out of it.''')
    drink_code()
    print('''You return to the bar after a few songs have played. The guy from earlier approaches you and your friend at the bar and asks you to dance.
    He’s been very rude, and he seems to be worse off than he was before.''')
    dance_code()
    if "watched" in new_dict:
        print("You sit back down at the bar and reach for your drink. It doesn’t look like there is anything wrong with it, and you were able to watch it from the dance floor.")
        spiked_code()
    elif "didn't watch" in new_dict:
        print("You sit back down at the bar and have a conversation with your friend. Your friend tells you to wait for her while she uses the restroom.")
        print()
        print('''You and your friend leave the bar and return to your dorm.
        She apologizes for the day you’ve been through, but she knows you’ll get through it. As you lay in bed, you reflect on your day.
        You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
        Some things seem to be just out of your control, but you were able to do something about it.''')
aware()
