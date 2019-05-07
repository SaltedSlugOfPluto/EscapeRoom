import time
import winsound
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
init(strip=not sys.stdout.isatty())  # strip colors if stdout is redirected

playersName = input("What is you name? ")
time.sleep(3)
print("Hello " + playersName + " Welcome to ")
time.sleep(4)
print("")
cprint(figlet_format('Trigometric Terror', font='slant'),
       'yellow', 'on_grey', attrs=['bold'])


# Skip story
boolSkipStory = False


# Answers for question 1
AnswerOne_Hyp = "20"
boolAnswerOne_Hyp = False

AnswerOne_Sin = "20"
boolAnswerOne_Sin = False

AnswerOne_CoSin = "20"
boolAnswerOne_CoSin = False

AnswerOne_Tan = "12"
boolAnswerOne_Tan = False

AnswerOne_CoSec = "16"
boolAnswerOne_CoSec = False

AnswerOne_Sec = "12"
boolAnswerOne_Sec = False

AnswerOne_CoTan = "16"
boolAnswerOne_CoTan = False


# Answers for question 2
AnswerTwo_Hyp = "30"
boolAnswerTwo_Hyp = False

AnswerTwo_Sin = "18"
boolAnswerTwo_Sin = False

AnswerTwo_CoSin = "24"
boolAnswerTwo_CoSin = False

AnswerTwo_Tan = "18"
boolAnswerTwo_Tan = False

AnswerTwo_CoSec = "30"
boolAnswerTwo_CoSec = False

AnswerTwo_Sec = "30"
boolAnswerTwo_Sec = False

AnswerTwo_CoTan = "24"
boolAnswerTwo_CoTan = False


# Answer for question 3
AnswerThree = "53"
boolAnswerThree = False
# Answer for question 4
AnswerFour = "35"
boolAnswerFour = False
# Answer for question 5
AnswerFive = "33"
boolAnswerFive = False
# Answer for question 6
AnswerSix = "41"
boolAnswerSix = False
# Answer for question 7
AnswerSeven = "12"
boolAnswerSeven = False
# Answer for question 8
AnswerEight = "30"
boolAnswerEight = False
# Answer for question 9
AnswerNine = "102"
boolAnswerNine = False
# Answer for question 10
AnswerTen = "23"
boolAnswerTen = False


input("Press enter to begin")
print("")
userSkip = input(
    "would you like to skip the story to go to the next question? type 'yes' or 'no'")
if userSkip == "no":
    boolSkipStory = False
elif userSkip == "yes":
    boolSkipStory = True
else:
    input("please type 'yes' or 'no'")

if boolSkipStory == False:
    for i in range(2):
        print("You wake up to find yourself in a dark room, unsure how you got there.")
        print("")
        time.sleep(3)
        print("you crawl around the room franticaly to find a way out.")
        print("")
        time.sleep(5)
        print("as you were crawling around the room, you hit your head on a wall and got knocked out.")
        print("")
        time.sleep(4)
        print("")
        print("")

    print("You wake up to find yourself in a dark room, with a pounding headache, unsure how you got there.")
    print("")
    time.sleep(3)
    print("you crawl around the room frantically for a way out, suddenly you hear a stern voice comsume the room. the voice says..")
    print("")
    time.sleep(5)
    print("  'STOP....'  ")
    print("")
    time.sleep(4)
    print(" you feel your heart pounding as you fear for your life, you stay still waiting for the voice to speak agian... You feel as if this voice could be your only glimmer of hope.")
    print("")
    time.sleep(6)
    print("")
    print("")
    print("The voice speaks and says")
    print("")
    time.sleep(2)
    print(" 'WELCOME... YOU MAY BE CONFUSED AT THE MOMENT, BUT PLEASE, YOU HAVE NOTHING TO WORRY ABOUT... YET' ")
    print("")
    time.sleep(6)
    print("The lights turn on. A small room with some furniture and a keypad is revealed.")
    print("")
    time.sleep(3)
    print("I WANT TO SEE SOME MATH...   says the voice")
    time.sleep(4)
    print("")
    print("you get off the ground and walk around the room. you try processing what the stranger just said")
    print("")
    time.sleep(3)
    print(" you think 'What do you mean math?'")
    print("")
    print("GOOD LUCK")
    time.sleep(3)
    print("")
    print("the room begins to make strange mechanical noises")
    time.sleep(3)
    print("")
    print("suddenly")
    time.sleep(2)
    print("")
    print("")
    print("A small part of the room opens up to reveal a hidden box")
    time.sleep(3)
    print("")
    print("You open up the box and find a notepad, pencil, and caculator.")
    time.sleep(3)
    print("")
    print("you think 'what kind of sick joke is this' ")
    time.sleep(3)
    print("")
    print("as you get all the items from the box and put them in your pocket you look over and remember the keypad")
    time.sleep(3)
    print("")
    print("you walk over to the keypad and become very confused")
    time.sleep(3)
    print("")
    print("the keypad dosent have numbers 0 to 9 like normal kepayds but has numbers 10 to 30 on each button, giving it 20 diffrent buttons")
    time.sleep(3)
    print("")
    print("you inspect the door and see an odd shape")
    time.sleep(3)
    print("")
    print("its a triangle!")
    time.sleep(2)
    print("")
    print("")
    print("")

print("                    /|   ")
print("                   / |   ")
print("                  /  |   ")
print("                 /   |   ")
print("                /    |   ")
print("               /     |   ")
print("              /      |   ")
print("             /       |   ")
print("           c/        |16 ")
print("           /         |   ")
print("          /          |   ")
print("         /           |   ")
print("        /            |   ")
print("       /             |   ")
print("      /              |   ")
print("     /_______________|   ")
print("             12          ")
print("")
print("")
print("find c")
print("a= 12    b= 16    c= ?    ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")

while boolAnswerOne_Hyp == False:
    inputAnswerOne_Hyp = input("c=")
    if inputAnswerOne_Hyp == AnswerOne_Hyp:
        boolAnswerOne_Hyp = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerOne_Hyp = False
        print("Incorrect, try agian")
        time.sleep(1)


print("You now have the complete triangle and read a long text bellow it")
print("")
time.sleep(3)
print("Sin is First, CoSine is Fourth, Tan is Sixth, CoSec is Second, Sec is Third, CoTan is Fifth ")
print("(write this down you will need it soon)")
print("")
time.sleep(10)
input("Press enter to continue")
print("")
print("with the completed triangle you try to solve for the answers in the riddle")
time.sleep(3)
print("")
print("")


print("                    /|   ")
print("                   / |   ")
print("                  /  |   ")
print("                 /   |   ")
print("                /    |   ")
print("               /     |   ")
print("              /      |   ")
print("             /       |   ")
print("          20/        |16 ")
print("           /         |   ")
print("          /          |   ")
print("         /           |   ")
print("        /            |   ")
print("       /             |   ")
print("      /              |   ")
print("     /x______________|   ")
print("             12          ")
print("")
print("")
print("Sin(x) = 16/? ")
print("a= 12    b= 16    c= 20    ")
print("")


while boolAnswerOne_Sin == False:
    inputAnswerOne_Sin = input("?=")
    if inputAnswerOne_Sin == AnswerOne_Sin:
        boolAnswerOne_Sin = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerOne_Sin = False
        print("Incorrect, try agian")
        time.sleep(2)


print("                    /|   ")
print("                   / |   ")
print("                  /  |   ")
print("                 /   |   ")
print("                /    |   ")
print("               /     |   ")
print("              /      |   ")
print("             /       |   ")
print("          20/        |16 ")
print("           /         |   ")
print("          /          |   ")
print("         /           |   ")
print("        /            |   ")
print("       /             |   ")
print("      /              |   ")
print("     /x______________|   ")
print("             12          ")
print("")
print("")
print("CoSin(x) = 12/? ")
print("a= 12    ,b= 16    ,c= 20    ")
print("")


while boolAnswerOne_CoSin == False:
    inputAnswerOne_CoSin = input("?=")
    if inputAnswerOne_CoSin == AnswerOne_CoSin:
        boolAnswerOne_CoSin = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerOne_CoSin = False
        print("Incorrect, try agian")
        time.sleep(1)

print("                    /|   ")
print("                   / |   ")
print("                  /  |   ")
print("                 /   |   ")
print("                /    |   ")
print("               /     |   ")
print("              /      |   ")
print("             /       |   ")
print("          20/        |16 ")
print("           /         |   ")
print("          /          |   ")
print("         /           |   ")
print("        /            |   ")
print("       /             |   ")
print("      /              |   ")
print("     /x______________|   ")
print("             12          ")
print("")
print("")
print("Tan(x) = 16/? ")
print("a= 12    ,b= 16    ,c= 20    ")
print("")


while boolAnswerOne_Tan == False:
    inputAnswerOne_Tan = input("?=")
    if inputAnswerOne_Tan == AnswerOne_Tan:
        boolAnswerOne_Tan = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerOne_Tan = False
        print("Incorrect, try agian")
        time.sleep(1)


print("                    /|   ")
print("                   / |   ")
print("                  /  |   ")
print("                 /   |   ")
print("                /    |   ")
print("               /     |   ")
print("              /      |   ")
print("             /       |   ")
print("          20/        |16 ")
print("           /         |   ")
print("          /          |   ")
print("         /           |   ")
print("        /            |   ")
print("       /             |   ")
print("      /              |   ")
print("     /x______________|   ")
print("             12          ")
print("")
print("")
print("CoSec(x) = 12/? ")
print("a= 12    ,b= 16    ,c= 20    ")
print("")


while boolAnswerOne_CoSec == False:
    inputAnswerOne_CoSec = input("?=")
    if inputAnswerOne_CoSec == AnswerOne_CoSec:
        boolAnswerOne_CoSec = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerOne_CoSec = False
        print("Incorrect, try agian")
        time.sleep(2)


print("                    /|   ")
print("                   / |   ")
print("                  /  |   ")
print("                 /   |   ")
print("                /    |   ")
print("               /     |   ")
print("              /      |   ")
print("             /       |   ")
print("          20/        |16 ")
print("           /         |   ")
print("          /          |   ")
print("         /           |   ")
print("        /            |   ")
print("       /             |   ")
print("      /              |   ")
print("     /x______________|   ")
print("             12          ")
print("")
print("")
print("Sec(x) = 20/? ")
print("a= 12    ,b= 16    ,c= 20    ")
print("")


while boolAnswerOne_Sec == False:
    inputAnswerOne_Sec = input("?=")
    if inputAnswerOne_Sec == AnswerOne_Sec:
        boolAnswerOne_Sec = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerOne_Sec = False
        print("Incorrect, try agian")
        time.sleep(1)


print("                    /|   ")
print("                   / |   ")
print("                  /  |   ")
print("                 /   |   ")
print("                /    |   ")
print("               /     |   ")
print("              /      |   ")
print("             /       |   ")
print("          20/        |16 ")
print("           /         |   ")
print("          /          |   ")
print("         /           |   ")
print("        /            |   ")
print("       /             |   ")
print("      /              |   ")
print("     /x______________|   ")
print("             12          ")
print("")
print("")
print("CoTan(x) = 12/? ")
print("a= 12    ,b= 16    ,c= 20    ")
print("")


while boolAnswerOne_CoTan == False:
    inputAnswerOne_CoTan = input("?=")
    if inputAnswerOne_CoTan == AnswerOne_CoTan:
        boolAnswerOne_CoTan = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerOne_CoTan = False
        print("Incorrect, try agian")
        time.sleep(1)

print("")
userSkip = input(
    "would you like to skip the story to go to the next question? type 'yes' or 'no'")
if userSkip == "no":
    boolSkipStory = False
elif userSkip == "yes":
    boolSkipStory = True
else:
    input("please type 'yes' or 'no'")

if boolSkipStory == False:
    print("you now have all of the numbers you need for the keypad")
    print("")
    print("your numbers.")
    print("Sin = 20   Cos = 20   Tan = 12    CoSec = 16   Sec = 12    CoTan = 16   ")
    print("you go to the keypad and type")

    boolDoneKeyOne = False
    boolDoneKeyTwo = False
    boolDoneKeyThree = False
    boolDoneKeyFour = False
    boolDoneKeyFive = False
    boolDoneKeySix = False





    while boolDoneKeyOne == False:
        userKeyPadOne = input("FirstButton: ")
        if userKeyPadOne == "20":
            boolDoneKeyOne = True
        else:
            boolKeyDoneOne = False
            print("you put in the key but it was incorrect, try agian")
            print("")

    while boolDoneKeyTwo == False:
        userKeyPadTwo = input("SecondButton: ")
        if userKeyPadTwo == "16":
            boolDoneKeyTwo = True
        else:
            boolKeyDoneTwo = False
            print("you put in the key but it was incorrect, try agian")
            print("")

    while boolDoneKeyThree == False:
        userKeyPadThree = input("ThirdButton: ")
        if userKeyPadThree == "12":
            boolDoneKeyThree = True
        else:
            boolKeyDoneThree = False
            print("you put in the key but it was incorrect, try agian")
            print("")

    while boolDoneKeyFour == False:
        userKeyPadFour = input("FourthButton: ")
        if userKeyPadFour == "20":
            boolDoneKeyFour = True
        else:
            boolKeyDoneFour = False
            print("you put in the key but it was incorrect, try agian")
            print("")

    while boolDoneKeyFive == False:
        userKeyPadFive = input("FifthButton: ")
        if userKeyPadFive == "16":
            boolDoneKeyFive = True
        else:
            boolKeyDoneFive = False
            print("you put in the key but it was incorrect, try agian")
            print("")

    while boolDoneKeySix == False:
        userKeyPadSix = input("SixthButton: ")
        if userKeyPadSix == "12":
            print("boop")
            boolDoneKeySix = True
            time.sleep(3)
    else:
            boolKeyDoneSix = False
            print("you put in the key but it was incorrect, try agian")
            print("")
    print("")
    print("beep..beep.beep...beepbeep....beep")
    time.sleep(4)
    print("")
    print("After putting in the password correctly the wall in front of you shoots into the ground revealing a long hallway.")
    print("")
    time.sleep(2)
    print("Oh no....")
    time.sleep(3)
    print("as you walk down the hallway, painted on the walls, you see.")
    time.sleep(3)
    print("")
    print("triangles and more triangles")
    time.sleep(3)
    print("")
    print("you know that there is only one thing you can do.")
    time.sleep(3)
    print("you start on the triangle labeled 'triangle one' ")
    time.sleep(3)
    print("")
    print("")







# ALL QUESTIONS BELLOW HERE IN ORDER

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("          b /        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A = 37    B= 90   C= ?      a=      b=      c=    ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerThree == False:
    inputAnswerThree = input("?=")
    if inputAnswerThree == AnswerThree:
        boolAnswerThree = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerThree = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("           b/        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A = ?     B= 90     C=     a= 8     b= 14     c=     ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerFour == False:
    inputAnswerFour = input("?=")
    if inputAnswerFour == AnswerFour:
        boolAnswerFour = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerFour = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("           b/        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A = ?    ,B= 90   ,C=    ,a=    ,b= 13   ,c= 7    ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerFive == False:
    inputAnswerFive = input("?=")
    if inputAnswerFive == AnswerFive:
        boolAnswerFive = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerFive = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("           b/        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A = ?    ,B= 90   ,C=    ,a= 14    ,b=    ,c= 16    ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerSix == False:
    inputAnswerSix = input("?=")
    if inputAnswerSix == AnswerSix:
        boolAnswerSix = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerSix = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("           b/        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A = 23   ,B= 82   ,C= 75   ,a= 5    ,b=    ,c= ?   ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerSeven == False:
    inputAnswerSeven = input("?=")
    if inputAnswerSeven == AnswerSeven:
        boolAnswerSeven = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerSven = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("           b/        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A = 54    ,B=    ,C= ?   ,a= 36    ,b=    ,c= 22   ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerEight == False:
    inputAnswerEight = input("?=")
    if inputAnswerEight == AnswerEight:
        boolAnswerEight = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerEight = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("           b/        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A = ?   ,B=    ,C=    ,a= 21   ,b= 15   ,c= 12    ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerNine == False:
    inputAnswerNine = input("?=")
    if inputAnswerNine == AnswerNine:
        boolAnswerNine = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerNine = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("                    /|  ")
print("                   /C|  ")
print("                  /  |  ")
print("                 /   |  ")
print("                /    |  ")
print("               /     |  ")
print("              /      |  ")
print("             /       |  ")
print("           b/        |a ")
print("           /         |  ")
print("          /          |  ")
print("         /           |  ")
print("        /            |  ")
print("       /             |  ")
print("      /              |  ")
print("     /A_____________B|  ")
print("             c          ")
print("")
print("")
print("A =    ,B=    ,C= 42   ,a= 33   ,b= 18    ,c= ?    ")
print("")
print("Round to the closest WHOLE NUMBER")
print("")


while boolAnswerTen == False:
    inputAnswerTen = input("?=")
    if inputAnswerTen == AnswerTen:
        boolAnswerTen = True
        print("Correct!")
        print("")
        print("")
    else:
        boolAnswerTeen = False
        print("Incorrect, try agian")
        time.sleep(1)
print("")
print("")

print("")
print("with the final answer done you hear static coming from the walls.")
time.sleep(3)
print(" 'GOOD JOB' ")
time.sleep(3)
print("the walls of the building fall down and reveal a desert.")
time.sleep(3)
print("you see a sign with an arrow saying ' town 5 miles away '  ")
time.sleep(3)
time.sleep(3)
print("")
print("")



# TEST SHAPES OR CODE
cprint(figlet_format('Trigometric Terror', font='slant'),
       'yellow', 'on_grey', attrs=['bold'])
print("")
print("")
cprint(figlet_format('Created by: Payton Domville', font='starwars'),
       'yellow', 'on_grey', attrs=['bold'])

input("press enter to leave game")
