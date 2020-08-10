import json
import random


class Animation:
    def __init__(self):
        self.matrices = []
        for x in range(0, 50):
            self.matrices.append(Matrix())


class Matrix:
    def __init__(self):
        self.panels = []
        for x in range(0, 20):
            self.panels.append(Panel())


class Panel:
    def __init__(self):
        self.leds = []
        for x in range(0, 16):
            self.leds.append(LED())


class LED:
    def __init__(self):
        self.r = random.randrange(0, 255)
        self.g = random.randrange(0, 255)
        self.b = random.randrange(0, 255)
