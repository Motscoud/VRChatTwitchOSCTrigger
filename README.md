# VRChatTwitchOSCTrigger
Python project that uses PythonOSC + WebSockets to connect to Twitch.tv's IRC, to push parameters to VRChat avatars

#Dependencies
Requires PythonOSC

#Usage
Change Channel @#Edit the JOIN here to connect to your Twitch
twitchchat.send(f"JOIN #patchesdoggo\n".encode('utf-8'))
under the JOIN # to your channel ID to connect to your channel
