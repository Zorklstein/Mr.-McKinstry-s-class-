'''ezekiel mesman mod 1 lab'''

characterName = "Spider-Man"
characterAge = 14
heroStatus = True

print(f"It is {heroStatus} that {characterName} is a {characterAge} year old hero.")

if heroStatus == True:
    print(f"{characterName} is a {characterAge} year old hero.")

if heroStatus == False:
    print(f"{characterName} is a {characterAge} year old villan.")

characterAge = characterAge + 5
heroStatus = False

print(f"It is {heroStatus} that {characterName} is a {characterAge} year old hero.")

if heroStatus == True:
    print(f"{characterName} is a {characterAge} year old hero.")

if heroStatus == False:
    print(f"{characterName} is a {characterAge} year old villan.")
