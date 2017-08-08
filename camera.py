import threading
import binascii
from time import sleep
from utils import base64_to_pil_image, pil_image_to_base64


class Camera(object):
    def __init__(self, makeup_artist):
        self.to_process = []
        self.to_output = []
        self.makeup_artist = makeup_artist

        thread = threading.Thread(target=self.keep_processing, args=())
        thread.daemon = True
        thread.start()

    def process_one(self):
        if not self.to_process:
            return

        # input is an ascii string. 
        input_str = self.to_process.pop(0)

        # convert it to a pil image
        input_img = base64_to_pil_image(input_str)

        ################## where the hard work is done ############
        # output_img is an PIL image
        output_img = self.makeup_artist.apply_makeup(input_img)

        # output_str is a base64 string in ascii
        output_str = pil_image_to_base64(output_img)

        # convert eh base64 string in ascii to base64 string in _bytes_
        self.to_output.append(binascii.a2b_base64(output_str))

    def keep_processing(self):
        while True:
            self.process_one()
            sleep(0.01)

    def enqueue_input(self, input):
        self.to_process.append(input)

    def get_frame(self):
        while not self.to_output:
            sleep(0.05)
        return self.to_output.pop(0)
