
with open('characters.txt', 'r', encoding='utf-8') as file:
    characters = [line.strip() for line in file if line.strip()]

print(characters)


import random


with open('characters.txt', 'r', encoding='utf-8') as file:
    characters = [line.strip() for line in file if line.strip()]

with open('output.txt', 'w', encoding='utf-8') as out_file:
    for character in characters:
        status = random.choice(['alive', 'dead'])
        out_file.write(f"{character} – {status}\n")
