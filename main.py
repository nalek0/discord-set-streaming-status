import datetime
import json

import discord

config = {}
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

		# Setting streaming status:
		activity = discord.Activity(
			name=config['stream_info']['name'],
			type=discord.ActivityType.streaming,
			state=config['stream_info']['state'],
			details=config['stream_info']['details'],
			start=datetime.datetime.now(),
			application_id=config['stream_info']['application_id'],
			assets=config['stream_info']['assets'],
			url=config['stream_info']['url'])

		await self.change_presence(
			status=discord.Status.idle,
			activity=activity)
		print("Status changed!")


if __name__ == "__main__":
	client = MyClient()
	client.run(config['user_info']['token'], bot=False)
