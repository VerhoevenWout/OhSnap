from twython import TwythonStreamer
import os
import TweetSender
import ImageEditor

# Search terms
TERMS = '#ohSnap'

# GPIO pin number of LED
LED = 22

# Twitter application authentication
APP_KEY = '8eQHQmlaghvu2BNRoluxBdhfU'
APP_SECRET = 'FVjg36wCy4GyNApd7AB60fU7hRGmKWYn0QGH78ylAjBiLc4BmZ'
OAUTH_TOKEN = '806098070240972800-VLTN8qYA4UqfNcZEoLu6nsnpGfaFaLl'
OAUTH_TOKEN_SECRET = 'zSAuW9HgUd8x3oDIh2t9w4DRHPrZq7HHdMJIoMZFXGpM3'

# Setup callbacks from Twython Streamer
class MyStreamer(TwythonStreamer):
	def on_success(self, data):
                if 'text' in data:
                        print data['text'].encode('utf-8')		
		if 'user' in data:	
			os.system("gphoto2 --capture-image-and-download --force-overwrite")
			arrayText = data['text'].split("#")
			newText = ""
			for item in arrayText:
				newText+=item
			print("send tweet " + data["text"].encode("utf-8"))
			ImageEditor.editImage()
			TweetSender.send(data['user']['screen_name'],newText)
			print('username: ' + data['user']['screen_name'])
	def on_error(self, status_code, data):
		print status_code, data
# Create streamer
stream = MyStreamer(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
stream.statuses.filter(track=TERMS)
