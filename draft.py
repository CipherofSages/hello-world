#!/usr/bin/env python
# librarybot.py - A simple Python IRC bot
# Author : struggling student
# License:
# Revision : see git rev.

# Suggestions
#
# 1. Limit lines to 70 characters (code or commands)
# 2. Indent using 4 spaces as opposed to tabs
# 3. Use some inline comments
# 4. Start to handle error cases
# 5. Change hard-coded constrants to program parameters

#
# Overview
# 1. Original code has been tested and works in pure Python.
# The code is compatible with Python 2 but hasnt been tested with Py3.
#


# Import Modules

#

# Some constants

zero = 0            # Zero

one = 1             # One

false = 0           # Boolean False

true = 1            # Boolean True


#
# Program parameters


# botnick   = Default nick
# bufsize   = Input buffer size
# channel   = Default IRC Channel
# port      = Default IRC port
# server    = Default IRC server
# developer = Operator of the Bot
# uname     = Bot username (NOT NICK!)
# realname  = Bots real name

botnick = ""
bufsize = 2048
channel = ""
port = 7000  
server = ""
oper = ""
uname = ""
realname ""

# Setup a dictionary of brief replies/responses


# This is used to implement brief replies to brief commans or remarks
#

Replies = dict()
['master'       ] = master + "Jesus is my Lord"
Replies[''] = " " 
Replies[''] = " "
# Etc Etc

# Subroutine


# Name:
# Arguments: None
# Purpose: Responds to server Pings

def ping():
    global ircsock
    ircsock.send ("PONG :ping\n")

