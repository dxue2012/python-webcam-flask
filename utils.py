from PIL import Image
from io import BytesIO
import base64


def pil_image_to_base64(pil_image):
    buf = BytesIO()
    pil_image.save(buf, format="JPEG")
    return base64.b64encode(buf.getvalue())


def base64_to_pil_image(base64_img):
    image = Image.open(BytesIO(base64.b64decode(base64_img)))
    round_tripped = pil_image_to_base64(image)
    try:
        assert(base64_img == round_tripped)
    except:
        print('input: {}, output: {}'.format(base64_img, round_tripped))
        assert False
    return image
