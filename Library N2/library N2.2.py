from colorama import Fore, Back, Style, init
import emoji


init()

print("happy - 1")
print("sad - 2")
print("scared - 3")
print("shocked - 4")
print("tired - 5")


mood = input(Fore.CYAN + 'Choose what is your mood today? ' + emoji.emojize(":pile_of_poo:", language="alias"))

if mood == "1":
    print(Back.YELLOW + 'I am happy for you! ' + emoji.emojize(":zany_face:", language="alias"))
elif mood == "2":
    print(Back.BLUE + 'i feel sorry for you ' + emoji.emojize(":cry:", language="alias"))
elif mood == "3":
    print(Back.GREEN + 'Don’t be scared everything is okay ' + emoji.emojize(":fearful:", language="alias"))
elif mood == "4":
    print(Back.WHITE + 'Wow shocked? ' + emoji.emojize(":astonished:", language="alias"))
elif mood == "5":
    print(Back.MAGENTA + 'take a rest ' + emoji.emojize(":sleeping_face:", language="alias"))
else:
    print(Fore.RED + 'Please enter 1-5 ' + emoji.emojize(":enraged_face:", language="alias"))
