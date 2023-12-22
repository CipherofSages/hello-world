import socket
import re
import requests

# IRC server and channel details
server = '4.206.117.194'
port = 6667
channel = '#developer'
botnick = 'bugzyX0F'

# Bible API details
API_KEY = 'fb9fc51ba765bc00a31b2daaf929dc1e'

def send_irc_message(message):
    ircsock.send(bytes(f"PRIVMSG {channel} :{message}\n", "UTF-8"))

def get_bible_verse(reference):
    url = f'https://api.biblia.com/v1/bible/content/ASV.txt?passage={reference}&key={API_KEY}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    return "Failed to fetch Bible verse."

def join_channel(developer):
    ircsock.send(bytes(f"JOIN {developer}\n", "UTF-8"))

def connect_to_irc(server_address, server_port, bot_name):
    ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ircsock.connect((server_address, server_port))
    ircsock.send(bytes(f"USER {bot_name} {bot_name} {bot_name} :{bot_name}\n", "UTF-8"))
    ircsock.send(bytes(f"NICK {bot_name}\n", "UTF-8"))
    return ircsock

# Establish IRC connection
ircsock = connect_to_irc(server, port, botnick)
join_channel(channel)
try:
    ircsock = connect_to_irc(server, port, botnick)
    join_channel(channel)
except Exception as e:
    print(f"Failed to connect: {e}")
    # Add any specific error handling or debugging information here


while True:
    ircmsg = ircsock.recv(2048).decode('UTF-8')
    ircmsg = ircmsg.strip('\n\r')

    if ircmsg.find(' PRIVMSG ') != -1:
        username = ircmsg.split('!', 1)[0][1:]
        message = ircmsg.split(' PRIVMSG ', 1)[1].split(':', 1)[1]

        if re.search(r'!verse (.+)', message):
            verse_match = re.search(r'!verse (.+)', message)
            verse_ref = verse_match.group(1)
            verse = get_bible_verse(verse_ref)
            send_irc_message(f"@{username}, {verse}")

    if ircmsg.find('PING :') != -1:
        ping_msg = ircmsg.split(':', 1)[1]
        ircsock.send(bytes(f"PONG :{ping_msg}\n", "UTF-8"))

