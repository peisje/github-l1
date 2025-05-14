from colorama import init, Fore, Back, Style
# print(Fore.CYAN + 'some cyan text')
# print(Back.MAGENTA + 'and with a magenta background')
# print(Style.DIM + 'and in dim text')
# print(Style.RESET_ALL)
# print('back to normal now')

import emoji
# print(emoji.emojize('Python is :pile_of_poo:'))
# print(emoji.emojize('Python is :orangutan:', language='alias'))
# print(emoji.demojize('Python is 😏'))
# print(emoji.emojize("Python is fun :hamburger:"))
# print(emoji.emojize("Python is fun :smirking_face:", variant="emoji_type"))
# print(emoji.is_emoji("🥞"))


init()

print("happy - 1")
print("sad - 2")
print("scared - 3")
print("schoked - 4")
mood = input(Fore.CYAN + 'choose what is your mood today? ')


if mood == 1:
    print(Back.MAGENTA + 'cool you are happy')