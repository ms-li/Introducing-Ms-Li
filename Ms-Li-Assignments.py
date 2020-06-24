#vytvorit zoznam

known_users = ["Gabo", "Michael", "Franto", "Jan", "Blazej", "Jaro", "Rado", "Matej"]

#definuj dvojity enter

def dvojenter():
    print( '\n')
    print( '\n')

while True:
    print ("Hi, I am your English trainer, Ms.Li.")
    name = input ("What is your name?: ").strip().capitalize()
    print( '\n')
    if name in known_users:
        print ("Hello {}".format (name),"Nice meeting you here.")
        break
    else:
        print ("Hmmm, I don't think I have met you yet {}".format(name))
        add_me = input ("Whould you like to be added to my list of excelling trainees y/n?: ").strip().lower()


      
# metoda append prida zadane meno do zoznamu - zapis: variable.append(what)

        if add_me == "y":
            known_users.append(name)
            print( '\n')
            print ("Congratulations {}.".format (name),"Now you can proceed to the important stuff.")
            dvojenter()
            break
        elif add_me == "n":
            dvojenter()
            print ("No hard feelings, bro. But start over please and be nice this time.")
            print( '\n')


# while loop so 4 ulohami, po ktoromkolvek "y" alebo po 4.ulohe sa loop skonci

while True:
    print ("Now, {}".format (name),"This is your first assignemnt: ")
    print( '\n')
    print ("1. Build a mind map with all known vocabulary around the topic Exotic Holidays.")
    first_hw = input ("Do you like this assignment? y/n: ").strip().lower()

    if first_hw == "y":
        print( '\n')
        print ("Best answer ever! Please finish it for your next English class.")
        break
    elif first_hw == "n":
        print( '\n')
        print ("I was expecting this. Here is another assignemnt then: ")
        print( '\n')
        print ("2. Build a mind map with all known vocabulary around the topic Work out.")
        second_hw = input ("Do you like this assignment? y/n: ").strip().lower()

    if second_hw == "y":
        print( '\n')
        print ("Best decision ever! Please finish it for your next English class.")
        break
    elif second_hw == "n":
        print( '\n')
        print ("You seem to be a bit picky, but I can give you another chance: ")
        print( '\n')
        print ("3. Study all your vocabulary that I have ever given to you.")
        third_hw = input ("Do you like this assignment? y/n: ").strip().lower()

    if third_hw == "y":
        print( '\n')
        print ("I am so proud of you. Please finish it for your next English class.")
        break
    elif third_hw == "n":
        print( '\n')
        print ("Oh, man. I don't envy you the last task, but here it is: ")
        print( '\n')
        print ("Now you are supposed to finish all three tasks and bring them to your next class.")
        break
dvojenter()

#tips na tvorbu mind map a coundown 3 sec, aby sa vsetko nevysypalo naraz


def countdown_short(t):
    import time
    print('Wait for it...')
    while t >= 0:
        time.sleep(1)
        t -= 1
t=3

def countdown_long(t):
    import time
    print('...')
    while t >= 0:
        time.sleep(1)
        t -= 1
t=6


print ("Don't go just yet.")
tips = input ("Would you like some tips for your assignement? y/n: ").strip().lower()
if tips == "y":
    print( '\n')
    print ("Now, how do you prepare a mind map, you ask? Here are 2 suggestions for you: ")

    countdown_short(t)
    print( '\n')   
    print ("1. You can do it right here on your computer, {},".format (name), "here is a nice app called 'AirMore Mind': https://bit.ly/2YsFI7S")
    print( '\n')
    countdown_long(t)
    print("2. Or you can do it in style. Be classy, {},".format (name)," use an original notebook :D https://remini.sk/")
    
elif tips == "n":
    print( '\n')
    print ("Never mind then.")
    

dvojenter()
countdown_long(t)
print ("Did you enjoy your 'new style' of getting homework? You can leave a feedback for Ms.Li on her e-mail or here: https://www.facebook.com/anglickyefektivne/" )
dvojenter()
print ("GOOD LUCK, {}".format (name))
dvojenter()




        
