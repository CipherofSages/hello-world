# Modules to import
from irc_class import *
import os
import random


# IRC Config
server = "4.206.117.194" # Provide a valid server IP/Hostname
port = 6668
channel = "#codebooth"
botnick = "ThePreacher"
verbose = True
debug = False
botnickpass = "guido"
botpass = "<%= @guido_password %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)
 
    if "PRIVMSG" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")
