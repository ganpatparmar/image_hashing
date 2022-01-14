import glob
from PIL import Image, ImageOps
import imagehash
import itertools


boys = glob.glob('C:/Users/dell/Desktop/boys/*.jfif')
girls = glob.glob('C:/Users/dell/Desktop/girls/*.jfif')

girls_hash = []
boys_hash = []
diff_hash = []

def image_to_hash(list):
    empty_list = []
    for i in list:
        hash1 = imagehash.average_hash(Image.open(i))
        empty_list.append(hash1)
    return empty_list


girls_hash = image_to_hash(girls)
boys_hash = image_to_hash(boys)

def min_hash(boys_hash,girls_hash):
    for girl in girls_hash:
        for boy in boys_hash:
            diff = boy-girl
            diff_hash.append(diff)
            if diff == min(diff_hash):
                min_hash_boy = boy
                min_hash_girl = girl
    return min_hash_boy, min_hash_girl

mhb, mhg = min_hash(boys_hash, girls_hash)


def hash_image(hash_list):
    for neutral in hash_list:
        hash1 = imagehash.average_hash(Image.open(neutral))
        if hash1 == mhb:
            return neutral
        elif hash1 == mhg:
            return neutral
        
boy = hash_image(boys)
girl = hash_image(girls)

img1 = Image.open(boy)
img2 = Image.open(girl)

def paste_image(img1,img2):
    new_image = Image.new('RGB', (img1.width + img2.width, img2.height))
    new_image.paste(img1,(0,0))
    new_image.paste(img2,(img1.width,0))
    return new_image

def border(img):
    img_with_border = ImageOps.expand(img,border = 10, fill = 'pink')
    return img_with_border

resultent_image = border(paste_image(img1, img2))
resultent_image.show()
resultent_image.save('couple1.jpg')









        
    
        








