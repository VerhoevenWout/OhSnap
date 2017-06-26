from twython import Twython
import os

# Twitter application authentication
APP_KEY = '8eQHQmlaghvu2BNRoluxBdhfU'
APP_SECRET = 'FVjg36wCy4GyNApd7AB60fU7hRGmKWYn0QGH78ylAjBiLc4BmZ'
OAUTH_TOKEN = '806098070240972800-VLTN8qYA4UqfNcZEoLu6nsnpGfaFaLl'
OAUTH_TOKEN_SECRET = 'zSAuW9HgUd8x3oDIh2t9w4DRHPrZq7HHdMJIoMZFXGpM3'

def send(name,text):
	app = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
	image = open('retro.jpg', 'rb')
	response = app.upload_media(media=image)
	app.update_status(status="@"+name+" "+text, media_ids=[response['media_id']])
	#app.update_status(status="@"+name)
	print('picture is send')
