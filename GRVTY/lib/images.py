from PIL import Image

def crop_image(path, x=0, y=0, w=None, h=None):
    img = Image.open(path)
    if w is None and h is None:
        if img.width < img.height:
            w = img.width
            h = img.width
        else:
            w = img.height
            h = img.height
    cropped = img.crop((x, y, x+w, y+h))
    cropped.save(path)
    return path
