# Set status

## config.json format:

```json
{
	"user_info": {
		"token": "..."
	},

	"stream_info": {
		"name": "...",
		"details": "...",
		"state": "...",

		"application_id": 1234567890,
		"assets": {
			"large_image": "1234567890",
			"large_text": "...",
			"small_image": "1234567890",
			"small_text": "..."
		},

		"url": "..."
	}
}
```

## What means what?

* **token** - your token for [https://discord.com/](https://discord.com/). I recommend you to search in google, how to get it.
* **name** - the name of the activity. I don't know why, but this is mandatory parameter
* **details** - the title of the activity
* **state** - the game of the activity
* **application_id** - id of the application, where discord will search images for the activity icons
* **large_image**, **small_image** - ids of the images
(see `Rich Presence/Art Assets` in discord developers portal or in the url `https://discord.com/developers/applications/<application_id>/rich-presence/assets`)
* **large_text**, **small_text** - Text, that will be shown when you hover activity images
* **url** - "url of the stream", but you can put every url you want, the button under the activity will redirect you to this url