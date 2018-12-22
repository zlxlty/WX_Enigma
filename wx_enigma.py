from wxpy import *
import os

bot = Bot()

text = "NULL"

name = input("Enter a friend you want to chat with: ")

my_friend = bot.friends().search(name)[0]

@bot.register(my_friend)
def receive_msg(msg):
    print(msg)
    text = msg.text
    with open("text.txt", "w") as f:
        f.write(text+'\n')
        f.write('-')
    decrypts = os.popen("./Enigma -df <text.txt").readlines()
    print(decrypts[0])

def sent_msg():
    plaintxt = input("Enter the plaintxt: ")
    with open("text.txt", "w") as f:
        f.write(plaintxt+'\n')
        f.write('-')
    cipher = os.popen("./Enigma -df <text.txt").readlines()
    my_friend.send(cipher[0])

embed()
