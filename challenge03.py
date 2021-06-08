#!/usr/bin/env python3

heroes=  {
"wolverine":
    {"real name": "James Howlett",
    "powers": "regeneration",
    "archenemy": "Sabertooth",},
"harry potter":
    {"real name": "Harry Potter",
    "powers": "magic",
    "archenemy": "Voldemort",},
"captain america":
    {"real name": "Steve Rogers",
    "powers": "frisbee shield",
    "archenemy": "Hydra",}
        }

while(True):
    char_name = input(" Which character do you want to know about? (Wolverine, Harry Potter, Captain America)\n>")

    #making error proof input
    char_name = char_name.lower()

    char_stats = input(" What statistic do you want to know about? (real name, powers, archenemy)\n>")

    #making error proof input
    char_stats = char_stats.lower()

    print(f"{char_name.title()}'s {char_stats} is : {heroes[char_name][char_stats]}")

    keepGoing = input("Would you like to keep going?Y/N\n>")
    if(keepGoing == "N"): break


