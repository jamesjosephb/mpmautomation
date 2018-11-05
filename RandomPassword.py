import random
import string


# Generates a new password
def randomPassword():
    randomCharacterList = []
    randomCharacterList.append(randomUpperCase())
    randomCharacterList.append(randomLowerCase())
    randomCharacterList.append(randomInt())
    randomCharacterList.append(randomSpecialCharacter())
    for i in range(10):
        char = random.choice([randomUpperCase(), randomLowerCase(), randomInt(), randomSpecialCharacter()])
        randomCharacterList.append(char)
    random.shuffle(randomCharacterList)
    passwordString = ''.join(randomCharacterList)
    return passwordString

def randomUpperCase():
    upperCase = random.choice(string.ascii_uppercase)
    while upperCase == 'I' or upperCase == 'O':
        upperCase = random.choice(string.ascii_uppercase)
    return upperCase

def randomLowerCase():
    lowerCase = random.choice(string.ascii_lowercase)
    while lowerCase == 'l' or lowerCase == 'o':
        lowerCase = random.choice(string.ascii_lowercase)
    return lowerCase

def randomInt():
    return str(random.randint(2, 9))

def randomSpecialCharacter():
    specialCharacter = ['$', '!', '@', '#', '%']    # should include the special characater * but
    return random.choice(specialCharacter)          # it does not get sent with the post request correctly

if __name__ == '__main__':
    print(randomPassword())