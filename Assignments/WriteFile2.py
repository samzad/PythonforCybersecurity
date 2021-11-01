question1 = input("What is your name? ")
question2 = input("What is your favorite color? ")
question3 = input("What is your first pet's name? ")
question4 = input("What is your mother's maiden name? ")
question5 = input("What elementary school did you attend? ")

import os

script_path = os.path.realpath(__file__)
script_folder = os.path.split(script_path)

hack_me = open(script_folder[0] + "/hackme.txt", "w")

hack_me.write(question1 + "\n")
hack_me.write(question2 + "\n")
hack_me.write(question3 + "\n")
hack_me.write(question4 + "\n")
hack_me.write(question5 + "\n")

hack_me.close()