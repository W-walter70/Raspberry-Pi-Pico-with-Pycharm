# WTimer class is written by Ing. Walter Porcellini , Milan (Italy)

class WTon:
    PT = 0
    Counter = 0
    Out = False

    def __init__(self, preset):
        self.PT = preset
        self.Counter = 0
        self.Out = False

    def run(self, delta_time, IN):
        if IN and self.Counter < self.PT:
            self.Counter += delta_time

        if not IN:
            self.Counter = 0

        self.Out = IN and (self.Counter >= self.PT)

    def getOutput(self):
        return self.Out


class WTof:
    PT = 0
    Counter = 0
    Out = False
    Memory = False

    def __init__(self, preset):
        self.PT = preset
        self.Counter = 0
        self.Out = False
        self.Memory = False

    def run(self, delta_time, IN):
        if IN:
            self.Memory = True

        if not IN and self.Memory and self.Counter < self.PT:
            self.Counter += delta_time

        if self.Counter >= self.PT:
            self.Memory = False
            self.Counter = 0

        self.Out = IN or (self.Counter < self.PT and self.Memory == True)

    def getOutput(self):
        return self.Out





