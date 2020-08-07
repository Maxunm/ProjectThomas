import json
import random

class Animation:
    def __init__(self):
        self.matrices = []
        for x in range(0, 50):
            self.matrices.append(Matrix())

    # def __str__(self):
    #     returnArray = []
    #     for x in range(len(self.panels)):
    #         returnArray.append(str(self.panels[x]))
    #     return str(returnArray)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

class Matrix:
    def __init__(self):
        self.panels = []
        for x in range(0, 20):
            self.panels.append(Panel())

    # def __str__(self):
    #     returnArray = []
    #     for x in range(len(self.panels)):
    #         returnArray.append(str(self.panels[x]))
    #     return str(returnArray)


class Panel:
    def __init__(self):
        self.leds = []
        for x in range(0, 16):
            self.leds.append(LED())

    # def __str__(self):
    #     returnArray = []
    #     for x in range(len(self.leds)):
    #         returnArray.append(str(self.leds[x]))
    #     return str(returnArray)


class LED:
    def __init__(self):
        self.r = random.randrange(0, 255)
        self.g = random.randrange(0, 255)
        self.b = random.randrange(0, 255)

    # def value(self):
    #     return self.r, self, g, self.b

    # def __str__(self):
    #     return "r:" + str(self.r) + " g:" + str(self.g) + " b:" + str(self.b)


# class MatrixEncoder(JSONEncoder):
#     def default(self, o):
#         return o.__dict__
