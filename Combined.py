def space_line():
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

def intro_code():
    space_line()
    print('''You leave your bedroom and run into your roommate in the living room. She is your party friend of the group. She’s known for being mildly irresponsible and is VERY go-with-the-flow. She wants you to go out to a new bar with her. She says you could meet guys there, and it sounds like a nice break from school. You agree to go to the bar later, but right now you’re already late for work. You finish getting ready and head out the door. You arrive at the news station twenty minutes after you were expected to. As an intern, you were supposed to have the day’s reports ready and on their desks. As you’re laying them out, your colleague, Jeff, approaches you. You’ve only known him for a month or so. You sometimes catch him staring at you from his desk, but your colleagues only have good things to say about him. He suddenly hugs you as he says, “Good morning!”''')

def end_code():
    space_line()
    print('''Thank you for playing. "How Would You React?” is the final project from the 2018 Girls Who Code Summer Immersion Program at AT&T: Los Angeles. It was created by five students: Aliyah McDaniel, Jessica Moreno, Shawahnah Haraway, Sophie Gutierrez, and Zari Williams. Aliyah will be a junior at Mira Costa High School. Jessica is a rising junior at Animo Pat Brown Charter High School. Shawahnah is homeschooled and is going to become a junior this year. Sophie is a rising junior at Da Vinci Science High School. She enjoys playing choose-your-own adventure games, and one of her favorite games is Telltale Games’ The Walking Dead. Zari will be a senior attending Alexander Hamilton Senior High School. Her favorite part of coding is being able to control what she wants to happen and being behind the scenes. The website for “How Would You React?” was coded using HTML, CSS, and JavaScript. “How Would You React?” was coded using Python. If you or someone you know has been a victim of sexual assault, resources include  800.656.HOPE (4673), rainn.org, projectcallisto.org, and (202) 467-8700 (National Center for Victims of Crime). If you or someone you know has been a victim of sexual harassment or discrimination in the workplace, a resource includes 1-800-522-0925 (9 to 5: National Association of Working Women). For immediate help, contact the National Sexual Assault Hotline at 1-800-656-4673.''')

def naive():
    space_line()
    intro_code()
    new1_dict = []

    def hug1_code():
        first_condition = True
        while first_condition:
            hug1 = input("Do you push him off? a) yes or b) no")
            if hug1 == "a":
                first_condition = False
                print('''You push Jeff away and take a step back. He has an injured look on his face, but it is quickly replaced by concern. He says, “Mr. Parker’s waiting for you in his office.” You thank him and quickly walk towards your supervisor’s office.''')
            elif hug1 == "b":
                first_condition = False
                print('''Jeff holds you for one more uncomfortable second before letting go. He looks a little concerned while he says, “Mr. Parker’s waiting for you in his office.” You thank him and quickly walk towards your supervisor’s office.''')
            else:
                print("You did not put in a valid option.")

    def tell1_code():
        second_condition = True
        while second_condition:
            tell1 = input("Should you tell him? a) yes or b) no")
            if tell1 == "a":
                second_condition = False
                space_line()
                print('''“I...I can explain the other incidents, Mr. Parker, but I don’t know what happened this morning,” you admit. “You don’t know what happened?” he asks. “No. I went to a concert last night, I was dancing with my friends, and then there’s a whole part of the night that’s missing. I didn’t even have a drink,” you say.''')
            elif tell1 == "b":
                second_condition = False
                space_line()
                print('''”I...I don’t know what happened today, Mr. Parker. But I promise, it won’t happen again,” you say.''')
            else:
                print("You did not put a valid option.")

    def boss1_code():
        third_condition = True
        while third_condition:
            boss1 = input("Should you try to reason with Mr. Parker or quit? a) reason or b) quit")
            if boss1 == "a":
                third_condition = False
                space_line()
                print('''You remove Mr. Parker’s hand and take a few steps towards the door.
                “Mr. Parker, I really want to stay at this station, but I just can’t do that,” you say.
                “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself? I could make or break your career,” he says.
                You rush out the door, and Mr. Parker yells after you, “Don’t come back!”''')
            elif boss1 == "b":
                third_condition = False
                space_line()
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
            complaint1 = input("Do you file a complaint before you leave? a) yes or b) no")
            if complaint1 == "a":
                fourth_condition = False
                space_line()
                print('''You take Emma’s advice and file a complaint with Human Resources. They tell you that they’ll be in contact, and you leave the news station.''')
            elif complaint1 == "b":
                fourth_condition = False
                space_line()
                print('''You can’t seem to understand what good it would do to file a complaint, so you decide not to. You leave the news station.''')
            else:
                print("You did not put a valid option.")

    def eavesdrop1_continued_code():
        fifth_condition = True
        while fifth_condition:
            eavesdrop1_continued = input("'Wasn’t it great?'' one of your classmates asks. a) yes or b) no")
            if eavesdrop1_continued == "a":
                fifth_condition = False
                space_line()
                print('''You talk about the great time you had, and the other classmate adds, “From your posts, it sure looked like you had a good time.”
                You thought there was only one picture...what else did you post?
                You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
                You look around and notice that other students are glancing at you. What happened last night?
                There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
            elif eavesdrop1_continued == "b":
                fifth_condition = False
                space_line()
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
            eavesdrop1 = input("Do you continue walking or wait where you are? a) continue or b) wait")
            if eavesdrop1 == "a":
                sixth_condition = False
                space_line()
                print('''You continue walking and run into your two classmates.
                “Hey, you. We were just talking about the concert last night."''')
                eavesdrop1_continued_code()
            elif eavesdrop1 == "b":
                sixth_condition = False
                space_line()
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
    def leave_it_code():
        seventh_condition = True
        while seventh_condition:
            leave = input("Do you want to leave your drink? a) yes or b) no")
            if leave == "a":
                seventh_condition = False
                new1_dict.append("left")
                space_line()
                print('''You leave your drink and go to the dance floor with your friend. You and your friend move further into the crowd. You can no longer see the bar or your drink, but your friend is really excited.''')
            elif leave == "b":
                seventh_condition = False
                new1_dict.append("didn't leave")
                space_line()
                print("You drink the rest of your drink before joining your friend on the dance floor.")
            else:
                print("You did not put a valid option.")
    def drink1_code():
        eighth_condition = True
        while eighth_condition:
            drink1 = input("Do you accept his drink? a) yes or b) no")
            if drink1 == "a":
                eighth_condition = False
                space_line()
                print("You accept the drink, and the man cuts you off as you begin to order. You think to yourself, 'If he’s buying, he’s ordering, right?'")
                print()
                print('''“That wasn’t so bad, huh?” your friend asks. She invites you to join her on the dance floor. You think about leaving the drink at the bar in order to dance. You’re sure it’ll be safe, and you’ll only be gone for a little while.''')
                leave_it_code()
            elif drink1 == "b":
                eighth_condition = False
                space_line()
                print('''You decline the drink, and the man yells, “But I already bought it!” You decline again, and he says, “It could be the only offer you get tonight, sweetheart, but fine.” You buy yourself a drink instead.''')
                print(''' “That guy was rude, but don’t let it spoil your night,” your friend says. She invites you to join her on the dance floor. You think about leaving the drink at the bar in order to dance. You’re sure it’ll be safe, and you’ll only be gone for a little while.''')
                leave_it_code()
            else:
                print("You did not put a valid option.")
    def dance1_code():
        ninth_condition = True
        while ninth_condition:
            dance1 = input("Do you dance with him? a) yes or b) no")
            if dance1 == "a":
                ninth_condition = False
                space_line()
                print('''You agree to dance with him. He grabs your wrist a little too tightly and leads you to the dance floor. He probably just doesn’t want to lose you in the crowd. You make it back to your friend after dancing with him for a while.''')
            elif dance1 == "b":
                ninth_condition = False
                space_line()
                print("You decline his offer. He glares at you for a few seconds, but his expression softens. He puts his hand on your shoulder and says, “I’m never this forward, but you look great, and I just had to ask.” You thank him, move closer to your friend, and the man walks away.")
            else:
                print("You did not put a valid option.")

    def spiked1_code():
        tenth_condition = True
        while tenth_condition:
            spiked1 = input("Do you still want to drink it? a) yes or b) no")
            if spiked1 == "a":
                tenth_condition = False
                print("You drink the remainder of your drink over a conversation with your friend. You feel a little dizzy, and the lights in the bar seem to be fading into each other. Your friend tells you to wait for her while she uses the restroom. You lay your head on the bar to stop your head from spinning.")
                print()
                print('''While your friend is gone, another man asks if you need a ride home. Your vision is only getting blurrier, and your friend hasn’t returned yet. You can’t seem to form any words. Without waiting for a response, he supports your weight as you lean against him, and he leads you out of the bar. This man has led you halfway down the street before your friend and a police officer come running after you. He suddenly drops you and runs away. Your friend cradles your head in her lap while an ambulance is called. Your friend apologizes profusely for the day you’ve been through. Your head is swimming, but you think about the things you could have done differently. You realize you might not have had a lot of decisions to make. Some things seem to be just out of your control, but there were some things you could have done differently.''')
            elif spiked1 == "b":
                tenth_condition = False
                print("You decide not to take any chances, and you ask the bartender for a new drink.")
                print('''You and your friend leave the bar and return to your dorm. She apologizes for the day you’ve been through, but she knows you’ll get through it.
                As you lay in bed, you reflect on your day. You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
                Some things seem to be just out of your control, but you were able to do something about it.''')
            else:
                print("You did not put a valid option.")

    hug1_code()
    space_line()
    print('''You knock on the door, and Mr. Parker calls you in. He’s a well-respected man, and he has helped a lot of interns reach their ultimate goal of becoming full-time reporters or news anchors. You take a seat across from him, and he begins to speak. “You know, it takes everyone doing their work to keep this place afloat. And you’ve been late at least four times this month. Do you have a reason?” he asks. You try to remember the previous night, but there’s a section of the night that just seems to be missing. You don’t want your boss to think you’re irresponsible.''')
    tell1_code()
    space_line()
    print('''
    “I’m a gracious man, but I can’t allow so many mistakes from one member of this team,” he admits.
    Mr. Parker sits on his desk in front of you and continues: “I could ignore your late arrivals, but you need to make up your missing time.”
    You tell Mr. Parker that your work can’t cut into anymore of your classes.
    “That won’t be an issue. We can arrange something...you can make up the time you missed another way,” he says, putting a hand on your knee.
    Your body freezes, and you can’t believe what you’re hearing.''')
    boss1_code()
    space_line()
    print('''As you’re walking back to your desk, you’re still shocked that this is happening. First it was Jeff, and now Mr. Parker? You never thought something like this could happen to you. What do you do now? You weren’t being paid a lot, but you need the money. Your scholarship doesn’t cover everything…''')
    print('''While you pack the belongings on your desk, another intern shows up. She gives you a weak smile and asks if you would like help with packing. You accept.
    “My name is Emma. I’m also an intern,” she says. You introduce yourself to Emma.
    “Did Mr. Parker make you an offer?” she asks. You look up suddenly, and she looks away.
    “I think you did the right thing...saying no. Mr. Parker thinks he owns us, but he doesn’t. We can’t be afraid of him,” she says.''')
    space_line()
    print('''“I don’t know what to do,” you say. Emma lets out a sigh, and her shoulders sag a little. “Maybe you could file a complaint before you leave? Human Resources could help you.”''')
    complaint1_code()
    space_line()
    print("You arrive at "+college+" just in time for your first class. As you’re nearing the corner of a hallway, you hear two of your classmates talking. One of your classmates mentions your name, and you stop walking before you round the corner.")
    eavesdrop1_code()
    space_line()
    print('''You return to your dorm and tell your roommate about your day. How could it have gone so wrong? Last night must be the cause of your problems.
    You ask your friend what happened, but she doesn’t have any new information. She manages to convince you to go to the bar with her later that night.
    Maybe it will take your mind off of the recent chain of events. You arrive and take a seat at the bar with your friend. Several minutes pass before you are offered a drink from a nicely-dressed, good-looking man. He seems trustworthy.''')
    drink1_code()
    space_line()
    print('''You return to the bar after a few songs have played. The guy from earlier approaches you and asks you to dance. He hasn’t been a perfect gentleman, but you could give him a second chance.''')
    dance1_code()
    if "left" in new1_dict:
        space_line()
        print("You sit back down at the bar and reach for your drink. It doesn’t look like there is anything wrong with it, and you were able to watch it from the dance floor.")
        spiked1_code()
    elif "didn't leave" in new1_dict:
        space_line()
        print("You sit back down at the bar and have a conversation with your friend. Your friend tells you to wait for her while she uses the restroom.")
        space_line()
        print('''You and your friend leave the bar and return to your dorm.
        She apologizes for the day you’ve been through, but she knows you’ll get through it. As you lay in bed, you reflect on your day.
        You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
        Some things seem to be just out of your control, but you were able to do something about it.''')
        space_line()
    end_code()
def aware():
    space_line()
    intro_code()
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
                space_line()
                print('''“I...I can explain the other incidents, Mr. Parker, but I don’t know what happened this morning,” you admit. “You don’t know what happened?” he asks. “No. I went to a concert last night, I was dancing with my friends, and then there’s a whole part of the night that’s missing. I didn’t even have a drink,” you say.''')
            elif tell == "no":
                condition6 = False
                space_line()
                print('''”I...I don’t know what happened today, Mr. Parker. But I promise, it won’t happen again,” you say.''')
            else:
                print("You did not put a valid option.")

    def boss_code():
        condition7 = True
        while condition7:
            boss = input("Should you try to reason with Mr. Parker or quit? reason/quit")
            if boss == "reason":
                condition7 = False
                space_line()
                print('''You remove Mr. Parker’s hand and take a few steps towards the door.
                “Mr. Parker, I really want to stay at this station, but I just can’t do that,” you say.
                “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself? I could make or break your career,” he says.
                You rush out the door, and Mr. Parker yells after you, “Don’t come back!”''')
            elif boss == "quit":
                condition7 = False
                space_line()
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
                space_line()
                print('''You take Emma’s advice and file a complaint with Human Resources.
                You ask if anyone else has filed a complaint against Mr. Parker, but they tell you that they’re not at liberty to give out that information.
                They do tell you that they’ll be in contact. Emma gives you her contact information, and you leave the news station.''')
            elif complaint == "no":
                condition8 = False
                space_line()
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
                space_line()
                print('''You talk about the great time you had, and the other classmate adds, “From your posts, it sure looked like you had a good time.”
                You thought there was only one picture...what else did you post?
                You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
                You look around and notice that other students are glancing at you. What happened last night?
                There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
            elif eavesdrop_continued == "no":
                condition10 = False
                space_line()
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
                space_line()
                print('''You continue walking and run into your two classmates.
                “Hey, you. We were just talking about the concert last night."''')
                eavesdrop_continued_code()
            elif eavesdrop == "wait":
                condition9 = False
                space_line()
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
                space_line()
                print('''You leave your drink and go to the dance floor with your friend, but you make sure to stay close to the edge of the crowd.
                You’re able to see the bar and your drink while you’re dancing, but your friend feels like you’re distracted.''')
            elif watch == "no":
                condition12 = False
                new_dict.append("didn't watch")
                space_line()
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
                space_line()
                print("You accept the drink, and the man cuts you off as you begin to order. You think to yourself, 'What a jerk.'")
                print()
                print('''"Man, that guy was a jerk,” your friend says with a laugh. She invites you to join her on the dance floor.
                You think about leaving your drink and watching it from the dance floor.
                You won’t be that far from it, and nobody would try anything when you’re so close to the bar.''')
                watch_it_code()
            elif drink == "no":
                condition11 = False
                new_dict.append("unaccepted")
                space_line()
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
                space_line()
                print('''He tightly grasps your arm as he leads you to the dance floor. He continues to hold onto as you two start to dance.
                You push him off and hurry back to your friend.''')
            elif dance == "no":
                condition12 = False
                space_line()
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
    hug_code()
    space_line()
    print('''You knock on the door, and Mr. Parker calls you in. He’s a well-respected man, and he has helped a lot of interns reach their ultimate goal of becoming full-time reporters or news anchors. You take a seat across from him, and he begins to speak. “You know, it takes everyone doing their work to keep this place afloat. And you’ve been late at least four times this month. Do you have a reason?” he asks. You try to remember the previous night, but there’s a section of the night that just seems to be missing. You don’t want your boss to think you’re irresponsible.''')
    tell_code()
    space_line()
    print('''
    “I’m a gracious man, but I can’t allow so many mistakes from one member of this team,” he admits.
    Mr. Parker sits on his desk in front of you and continues: “I could ignore your late arrivals, but you need to make up your missing time.”
    You tell Mr. Parker that your work can’t cut into anymore of your classes.
    “That won’t be an issue. We can arrange something...you can make up the time you missed another way,” he says, putting a hand on your knee.
    Your body freezes, and you can’t believe what you’re hearing.''')
    boss_code()
    space_line()
    print('''As you’re walking back to your desk, you’re still a little shocked that this is happening.
    First it was Jeff, and now Mr. Parker? You should have known something like this could happen, but you never thought about it before.
    Mr. Parker does carry a lot of influence in the news business, but maybe you could do something to stop him.
    What do you do know? Of course you weren’t being paid a lot, but you need the money. Your scholarship doesn’t cover everything…''')
    print()
    print('''While you pack the belongings on your desk, another intern shows up. She gives you a weak smile and asks if you would like help with packing. You accept.
    “My name is Emma. I’m also an intern,” she says. You introduce yourself to Emma.
    “Did Mr. Parker make you an offer?” she asks. You look up suddenly, and she looks away.
    “I think you did the right thing...saying no. Mr. Parker thinks he owns us, but he doesn’t. We can’t be afraid of him,” she says.''')
    space_line()
    print('''“I don’t want anyone else to go through this, but I don’t know what to do,” you admit.
    Emma lets out a sigh. “Human Resources might be able to help if you filed a complaint. Maybe former interns would come forward as well.”''')
    complaint_code()
    space_line()
    print("You arrive at "+college+" just in time for your first class. As you’re nearing the corner of a hallway, you hear two of your classmates talking. One of your classmates mentions your name, and you stop walking before you round the corner.")
    eavesdrop_code()
    space_line()
    print('''You return to your dorm and tell your roommate about your day. How could it have gone so wrong? Last night must be the cause of your problems.
    You ask your friend what happened, but she doesn’t have any new information. She manages to convince you to go to the bar with her later that night.
    Maybe it will take your mind off of the recent chain of events. You arrive and take a seat at the bar with your friend. Several minutes pass before you are offered a drink from a nicely-dressed, good-looking man. He seems a little out of it.''')
    drink_code()
    space_line()
    print('''You return to the bar after a few songs have played. The guy from earlier approaches you and your friend at the bar and asks you to dance.
    He’s been very rude, and he seems to be worse off than he was before.''')
    dance_code()
    if "watched" in new_dict:
        space_line()
        print("You sit back down at the bar and reach for your drink. It doesn’t look like there is anything wrong with it, and you were able to watch it from the dance floor.")
        spiked_code()
    elif "didn't watch" in new_dict:
        print("You sit back down at the bar and have a conversation with your friend. Your friend tells you to wait for her while she uses the restroom.")
        space_line()
        print('''You and your friend leave the bar and return to your dorm.
        She apologizes for the day you’ve been through, but she knows you’ll get through it. As you lay in bed, you reflect on your day.
        You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
        Some things seem to be just out of your control, but you were able to do something about it.''')
        space_line()
    end_code()
def woke():
    space_line()
    intro_code()
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
                space_line()
                print('''“I...I can explain the other incidents, Mr. Parker, but I don’t know what happened this morning,” you admit. “You don’t know what happened?” he asks. “No. I went to a concert last night, I was dancing with my friends, and then there’s a whole part of the night that’s missing. I didn’t even have a drink,” you say.''')
            elif tell2 == "no":
                condition_b = False
                space_line()
                print('''”I...I don’t know what happened today, Mr. Parker. But I promise, it won’t happen again,” you say.''')
            else:
                print("You did not put a valid option.")

    def boss2_code():
        condition_c = True
        while condition_c:
            boss2 = input("Should you try to reason with Mr. Parker or quit? reason/quit")
            if boss2 == "reason":
                condition_c = False
                space_line()
                print('''You remove Mr. Parker’s hand and take a few steps towards the door.
                “Mr. Parker, I really want to stay at this station, but I just can’t do that,” you say.
                “What do you want to be, huh? Journalist? News anchor? You really think you can do that all by yourself? I could make or break your career,” he says.
                You rush out the door, and Mr. Parker yells after you, “Don’t come back!”''')
            elif boss2 == "quit":
                condition_c = False
                space_line()
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
                space_line()
                print('''You take Emma’s advice and file a complaint with Human Resources. You ask if anyone else has filed a complaint against Mr. Parker, but they tell you that information is private. They do tell you that they’ll be in contact. You meet Emma near the entrance, and she has brought two other interns with her. You all exchange contact information and plan for a future meeting. You leave the news station.''')
            elif complaint2 == "no":
                condition_d = False
                space_line()
                print('''You can’t seem to understand what good it would do to file a complaint, so you decide not to. Just imagine the damage that Mr. Parker could do to your career. Who would listen to you anyway? You think about the former interns...one of them must have filed a complaint, right? You walk past Emma as you leave the news station.''')
            else:
                print("You did not put a valid option.")

    def eavesdrop2_continued_code():
        condition_e = True
        while condition_e:
            eavesdrop2_continued = input("'Wasn’t it great?'' one of your classmates asks. yes/no")
            if eavesdrop2_continued == "yes":
                condition_e = False
                space_line()
                print('''You talk about the great time you had, and the other classmate adds, “From your posts, it sure looked like you had a good time.”
                You thought there was only one picture...what else did you post?
                You enter the lecture hall and take a seat, and it doesn’t take long before the whispering starts.
                You look around and notice that other students are glancing at you. What happened last night?
                There’s a few whistles, but the professor quiets the room and no one will meet your eye. You decide to leave class early.''')
            elif eavesdrop2_continued == "no":
                condition_e = False
                space_line()
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
                space_line()
                print('''You continue walking and run into your two classmates.
                “Hey, you. We were just talking about the concert last night."''')
                eavesdrop2_continued_code()
            elif eavesdrop2 == "wait":
                condition_f = False
                space_line()
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
                space_line()
                print('''You take your drink to the dance floor with your friend. You might have to stay a little closer to the edge of the crowd to avoid being bumped, but you know it’s the safest option.''')
            elif take == "no":
                condition_g = False
                new2_dict.append("didn't take")
                space_line()
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
                space_line()
                print("You accept the drink, and the man cuts you off as you begin to order. Once he finishes ordering, you tell the bartender what you’d prefer instead.")
                print()
                print('''“I think that guy was a little strange,” your friend says. She invites you to join her on the dance floor. You consider taking your drink to the dance floor. You’ve heard of some people getting into serious trouble, and you don’t want to risk it.''')
                take_it_code()
            elif drink2 == "no":
                condition_h = False
                new2_dict.append("unaccepted")
                space_line()
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
                space_line()
                print('''You feel sorry for him and accept his invitation to dance. He reaches for your arm and misses, knocking a glass over. He waves you away before walking to the other end of the bar, and you return to your friend.''')
            elif dance2 == "no":
                condition_i = False
                space_line()
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
    hug2_code()
    space_line()
    print('''You knock on the door, and Mr. Parker calls you in. He’s a well-respected man, and he has helped a lot of interns reach their ultimate goal of becoming full-time reporters or news anchors. You take a seat across from him, and he begins to speak. “You know, it takes everyone doing their work to keep this place afloat. And you’ve been late at least four times this month. Do you have a reason?” he asks. You try to remember the previous night, but there’s a section of the night that just seems to be missing. You don’t want your boss to think you’re irresponsible.''')
    tell2_code()
    space_line()
    print('''
    “I’m a gracious man, but I can’t allow so many mistakes from one member of this team,” he admits.
    Mr. Parker sits on his desk in front of you and continues: “I could ignore your late arrivals, but you need to make up your missing time.”
    You tell Mr. Parker that your work can’t cut into anymore of your classes.
    “That won’t be an issue. We can arrange something...you can make up the time you missed another way,” he says, putting a hand on your knee.
    Your body freezes, and you can’t believe what you’re hearing.''')
    boss2_code()
    space_line()
    print('''As you’re walking back to your desk, you’re still a little shocked that this is happening. First it was Jeff, and now Mr. Parker? You always knew things like this happened, and you should have known it could happen to you, too. Mr. Parker does carry a lot of influence in the news business, but you will not let him do this to anyone else. Even though you weren’t being paid a lot, you still need the money. Your scholarship doesn’t cover everything…''')
    print()
    print('''While you pack the belongings on your desk, another intern shows up. She gives you a weak smile and asks if you would like help with packing. You accept.
    “My name is Emma. I’m also an intern,” she says. You introduce yourself to Emma.
    “Did Mr. Parker make you an offer?” she asks. You look up suddenly, and she looks away.
    “I think you did the right thing...saying no. Mr. Parker thinks he owns us, but he doesn’t. We can’t be afraid of him,” she says.''')
    space_line()
    print('''“I won’t let him do this to anyone else,” you say. Emma smiles hopefully. “Human Resources could help you if you filed a complaint, and we could even talk to former interns about their experiences.”''')
    complaint2_code()
    space_line()
    print("You arrive at "+college+" just in time for your first class. As you’re nearing the corner of a hallway, you hear two of your classmates talking. One of your classmates mentions your name, and you stop walking before you round the corner.")
    eavesdrop2_code()
    space_line()
    print('''You return to your dorm and tell your roommate about your day. How could it have gone so wrong? Last night must be the cause of your problems.
    You ask your friend what happened, but she doesn’t have any new information. She manages to convince you to go to the bar with her later that night.
    Maybe it will take your mind off of the recent chain of events. You arrive and take a seat at the bar with your friend. Several minutes pass before you are offered a drink from a nicely-dressed, good-looking man. He’s obviously intoxicated.''')
    drink2_code()
    space_line()
    print('''You return to the bar after a few songs have played. The guy from earlier approaches you and your friend at the bar and asks you to dance.
    He’s had a few more drinks since the last time you talked to him, and he’s slurring his words.''')
    dance2_code()
    space_line()
    if "took" in new2_dict:
        space_line()
        print("You sit back down at the bar and finish your drink over a conversation with your friend.")
        print('''You and your friend leave the bar and return to your dorm. She apologizes for the day you’ve been through, but she knows you’ll get through it.
        As you lay in bed, you reflect on your day. You think about the things you could have done differently, and you realize that you didn’t have a lot of decisions to make.
        Some things seem to be just out of your control, but you were able to do something about it.''')
    elif "didn't take" in new2_dict:
        space_line()
        print("You sit back down at the bar and reach for your drink. It doesn’t look like there is anything wrong with it, but it does have a strange smell.")
        spiked2_code()
        space_line()
        end_code()

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
            space_line()
            door_code()
        elif window == "e":
            condition2 = False
            aware_count += 1
            print ("'There's a lot of people out there', you say as you close the window.")
            space_line()
            door_code()
        elif window == "f":
            condition2 = False
            woke_count += 1
            print ("'There are too many people out there', you say as you lock the window.")
            space_line()
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
            space_line()
            print ("You check your phone and see that your family has left you texts and voicemails.")
            print ("They tell you to check your Instagram.")
            photo_code()
        elif door == "h":
            condition3 = False
            aware_count += 1
            print ("'I should close it' you say as walk over to the door and walk back over to your bed.")
            space_line()
            print ("You check your phone and see that your family has left you texts and voicemails.")
            print ("They tell you to check your Instagram.")
            photo_code()
        elif door == "i":
            condition3 = False
            woke_count += 1
            print ("'I defintely closed this before I slept', you say as you lock the door and walk back over to your bed.")
            space_line()
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
            space_line()
            print ("You notice that your window is open.")
            window_code()
        elif wallet == "b":
            condition1 = False
            aware_count += 1
            space_line()
            print ("You notice that your window is open.")
            window_code()
        elif wallet == "c":
            condition1 = False
            woke_count += 1
            space_line()
            print ("You notice that your window is open.")
            window_code()
        else:
            print("You did not put in a valid option.")
def main():
    college = input("What college do you want to attend?")
    print ("You are a 20 year old female that is currently attending "+college+".")
    print("You live in a dorm with your friends and experience various challenges everyday, but today is different...")
    print ("You get to decide your fate! Choose wisely.")
    space_line()
    print ("You are in your dorm room. You went to a concert, and you remember that a person bumped into you after the concert. Your wallet is missing.")
    wallet_code()


main()
