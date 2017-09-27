from PIL import Image
img = Image.open(r'c:\Users\eshiyho\Documents\Untitleddafei.png')
img.size
img2 = img.crop((0,0,144,200))
img3 = img2.resize((358,441), Image.ANTIALIAS)
img3.save(r'c:\Users\eshiyho\Documents\dafei.jpg')
img3 = img2.resize((358, int(358 * 200 /144)), Image.ANTIALIAS)
img4 = img3.crop((0,36,358,477))
img4.save(r'c:\Users\eshiyho\Documents\dafei.jpg')
