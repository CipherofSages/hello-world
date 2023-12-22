import socket
import time
import sys

# IRC server details
server = "4.206.117.194"
port = 6667
channel = "#codebooth"
botnick = "TheScribe"
#botnickpass = "guido"
#botpass = "<%= @guido_password %>"
verbose = True
debug = False

# Establish connection to the IRC server
ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ircsock.connect((server, port))
ircsock.send(bytes("USER " + botnick + " " + botnick + " " + botnick + " :Python IRC\n", "UTF-8"))
ircsock.send(bytes("NICK " + botnick + "\n", "UTF-8"))
ircsock.send(bytes("JOIN " + channel + "\n", "UTF-8"))


# Function to send messages to the IRC server
def send_message(message):
    ircsock.send(bytes("PRIVMSG " + channel + " :" + message + "\n", "UTF-8"))


# Function to handle incoming messages and perform actions
def handle_messages():
    while True:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')

        if ircmsg.startswith("PING :"):
            ping_value = ircmsg.split()[1]  # Extract the ping value
            ircsock.send(bytes("PONG " + ping_value + "\n", "UTF-8"))  # Respond with PONG

        if verbose:
            print("Received:", ircmsg)

        # Add your bot's logic here based on incoming messages
        # For instance, if you want to respond to a specific message:
        if ircmsg.find(":Hello " + botnick) != -1:
            send_message("Hello! What's Up?")


# Run message handling loop
handle_messages()
