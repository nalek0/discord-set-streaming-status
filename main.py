import datetime
import requests
import discord
import base64
import json

try:
	f = open("config.json", 'r')
	config = json.load(f)
except IOError:
	print("You must have config.json file!")
	exit(0)
else:
	f.close()


class MyClient(discord.Client):
	async def on_ready(self):
		print(self.user, "is ready!")

		# Seting streaming status:
		activity = discord.Activity(
			application_id 	= config['stream_info']['assets']['application_id'],
			assets 			= { 
				"large_image": config['stream_info']['assets']['large_image'], 
				"large_text": config['stream_info']['assets']['large_text'] 
			},
			
			details			= config['stream_info']['details'],
			name			= "Stream",
			
			start 			= datetime.datetime.now(),
			type 			= discord.ActivityType.streaming,
			url				= config['stream_info']['url'])


		await self.change_presence(
			status 		= discord.Status.idle,
			activity	= activity)

		print("Status changed!")

client = MyClient()
client.run(config['user_info']['token'], bot = False)