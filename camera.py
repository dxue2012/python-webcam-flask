import threading
import binascii
from time import sleep


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
        input_uri = self.to_process.pop(0)
        base64_str = input_uri.split(",")[1]
        bin_img = binascii.a2b_base64(base64_str)
        output = self.makeup_artist.apply_makeup(bin_img)
        self.to_output.append(output)

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
