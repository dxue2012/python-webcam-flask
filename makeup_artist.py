from PIL import Image


class Makeup_artist(object):
    def __init__(self):
        pass

    def apply_makeup(self, img):
        return img.transpose(Image.FLIP_LEFT_RIGHT)
