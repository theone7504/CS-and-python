import random


def main():
    level = get_level()

    score = simgame(level)

    print("Score: ", score)



def get_level():
    while True :
        try:
            level = int(input("Level: "))
            if level in [1,2,3] :
                return level
        except :
            pass




def generate_integer(level):
    if level == 1 :
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2 :
        x= random.randint(10,99)
        y = random.randint(10,99)
    elif level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y
def simround(x,y) :
    i = 1
    while i <= 3 :
        try:
            ans = int(input(f"{x} + {y} ="))
            if ans == (x+y):
                return True
            else :
                i += 1
                print("EEE")
        except :
            i += 1
            print("EEE")
    print(f"{x} +{y} = {x+y}")
    return False

def simgame(level):
    j = 1
    score = 0
    while j <= 10 :
        x,y = generate_integer(level)
        result = simround(x,y)
        if result == True:
            score += 1
        j += 1

    return score





if __name__ == "__main__":
    main()