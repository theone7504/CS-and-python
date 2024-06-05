from random import *
from sys import *
import os



def main():
    global domain
    global password
def main():
    global domain
    global password
    try:
        if (argv[1].strip == "") or (argv[1].lower().strip()) == "generate":
            length = input("How long? ")
            keyword = input("Any keywords? ")
            domain = input("For what domain? ").strip.lower.replace(" ", "")
            password = genpass(length, keyword)
            save(password, domain)
            print(f"here is your {domain} password: {password}\n")
            t = input()
    except IndexError:
        length = input("How long? ")
        keyword = input("Any keywords? ")
        domain = input("For what domain? ")
        password = genpass(length, keyword)
        save(password, domain)
        print(f"here is your {domain} password: {password}")
        asss = input()
    else:
        domain = input("what was the domani? ")
        get(domain)
        youuuu = input("anytime:)")

def genpass(l, k):
    try:
        if not l:
            exit("Please specify the length at least")

        if not k:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            password = ""
            keyword = k
            while len(password) < int(l):
                password += choice(chars)
        else:
            chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
            password = ""
            keyword = k
            while len(password) < int(l):
                password += choice(chars)
                password += choice(keyword.replace(" ", ""))

        return password
    except ValueError:
        exit("length must be an integer")


def save(password, domain):
    try:
        passwords = open("passwords.txt", "x")
        with open("passwords.txt", "a") as passwords:
            passwords.write(f"the password of {domain} is {password}\n")

    except FileExistsError:
        with open("passwords.txt", "r") as f2:
            ls2 = f2.readlines()
        with open("passwords.txt", "r") as f:
            ls = f.readlines()
            for l in ls:
                if l.find(domain) != -1:
                    ans = input(
                        f"there is an already existant password for {domain}\ndo you want to change it (yes or no) "
                    )
                    if ans.strip().lower() == "no":
                        get(domain)
                        exit()
                    elif ans.strip().lower() == "yes":
                        change_line(ls.index(l), ls)
                    else:
                        exit("Why bro!")

            if ls == ls2:
                with open("passwords.txt", "a") as f3:
                    f3.write(f"the password of {domain} is {password}\n")


def get(domain):
    with open("passwords.txt", "r") as getters:
        lines = getters.readlines()
        for line in lines:
            if line.find(domain) != -1:
                print(lines[lines.index(line)].replace("\n", ""))


def change_line(i, contents):
    with open("passwords.txt", "w") as gees:
        contents[i] = f"the password of {domain} is {password}\n"
        for j in range(len(contents)):
            gees.write(contents[j])


if __name__ == "__main__":
    main()
