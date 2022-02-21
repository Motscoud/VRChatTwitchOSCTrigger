#/bin/env python3
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
### Patches' Fantabulous Twitch Chat Parser
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               TODO:
#   Create External File to store API keys and definitions such as ChannelName
#   Use External File to define custom commands, starting with !
#   Create support for Stream Points. I am not affiliated, so I can't test myself.

from pythonosc import udp_client
import socket, time
#Creates a websocket that connects to Twitch IRC
twitchchat = socket.socket()
twitchchat.connect(('irc.chat.twitch.tv',6667))
twitchchat.send(f"NICK justinfan42069\n".encode('utf-8'))
#Edit the JOIN here to connect to your Twitch
twitchchat.send(f"JOIN #patchesdoggo\n".encode('utf-8'))
#Creates OSC Socket to communicate to VRChat
client_osc = udp_client.SimpleUDPClient("127.0.0.1",9000)

def readchat(resp):
    resp = resp.rstrip().split('\r\n')
    for line in resp:
        if "PRIVMSG" in line:
            user = line.split(':')[1].split('!')[0]
            msg = line.split(':', maxsplit=2)[2]
            line = user + ": " + msg
            return msg
        print(line)
        

while True:
    resp = twitchchat.recv(2048).decode('utf-8')
    if resp.startswith('PING'):
        twichchat.send("PONG\n".encode('utf-8'))
        
    if len(resp) > 0:
        message = readchat(resp)
        print(resp)
        print(message)
        #Python 3.9 lacks Switch cases, will update to 3.10 or likely rewrite in another language once PoC works
        try:
            if(message.startswith('!')):
               #This is where the fun begins.
                if(message == '!love'):
                   client_osc.send_message("/avatar/parameters/love",1)
                   #100ms delay to ensure message has been sent
                   time.sleep(0.1)
                   client_osc.send_message("/avatar/parameters/love",0)
        except Exception as e:
            print("This message lacks a command.")
