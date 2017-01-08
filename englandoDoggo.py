# EnglandoDoggo 0.1
# Turns English into doggo-speak
# Written by Evan Bruns
# "Protected" by WTFPL

import random

DOG_TRANS = ["doggo", "doge", "pupper", "shoober", "smol pupper", "big ol doggo", "shooblet", "long doggo",
             "lengthy doggo"]
CAT_TRANS = ["catto", "catter", "meow monster", "fur devil", "kitteh", "l0lcat", "meower"]
SNOUT_TRANS = ["snoot", "booper", "sniffer", "bork beak", "muzzle", "pup probiscus", "nose nozzle", "snoot spout"]


def look_at(name_list):
    index = random.randint(0, len(name_list)-1)
    return name_list[index]


def doggo_filter(word):
    if word.lower() == "dog":
        return look_at(DOG_TRANS)
    if word.lower() == "cat":
        return look_at(CAT_TRANS)
    if word.lower() in ["nose", "snout"]:
        return look_at(SNOUT_TRANS)
    return word


def main():
    englando = input("Please enter the string you'd like converted to doggo speak: \n")
    doggo = [""]
    englist = englando.split(" ")
    for word in englist:
        doggo.append(doggo_filter(word))
    print(" ".join(doggo))

main()
