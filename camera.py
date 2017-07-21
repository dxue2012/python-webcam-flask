from time import sleep


class Camera(object):
    def __init__(self):
        # input queue
        self.to_process = []

        # output queue
        self.to_output = []

    def enqueueInput(self, input):
        self.to_process.append(input)

    def applyMakeup(self, img):
        # TODO: actually do stuff here
        return img

    def processOne(self):
        if not self.to_process:
            return
        input = self.to_process.pop(0)
        output = self.applyMakeup(input)
        self.to_output.append(output)

    def get_frame(self):
        while not self.to_output:
            sleep(1)

        return self.to_output.pop(0)
