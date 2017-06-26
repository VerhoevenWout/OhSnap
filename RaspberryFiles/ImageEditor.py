from PIL import ImageFile, Image, ImageFilter
ImageFile.LOAD_TRUNCATED_IMAGES = True


def editImage():
	im = Image.open( 'capt0000.jpg' )
	overlay = Image.open('filter.jpg')

	grayscale = im.convert('L') # convert image to black and white
	grayscale.save('grayscale.jpg')

	correct_overlay = overlay.convert('L')
	correct_overlay.save('overlay.jpg')

	retroImage = Image.blend(grayscale, correct_overlay, 0.4)

	retroImage.save('retro.jpg')

editImage()
