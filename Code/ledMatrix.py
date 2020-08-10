import json
import random


class Animation:
    def __init__(self):
        self.matrices = []
        for x in range(0, 50):
            self.matrices.append(Matrix())

    def play(self):
        for x in range(len(self.matrices)):
            self.matrices[x].setMatrixLights()


class Matrix:
    def __init__(self):
        self.panels = []
        for x in range(0, 20):
            self.panels.append(Panel(x))

    def setMatrixLights(self):
        for x in range(len(self.panels)):
            self.panels[x].setPanelLights()


class Panel:
    def __init__(self, panelNumber):
        self.panelNumber = panelNumber
        self.leds = []
        for x in range(0, 16):
            self.leds.append(LED((16*panelNumber)+x)  # Might have to look at this math later

    def setPanelLights(self):
        for x in range(len(self.leds)):
            self.leds[x].setLedColor()


class LED:
    def __init__(self, ledNumber):
        self.ledNumber=ledNumber
        self.r=random.randrange(0, 255)
        self.g=random.randrange(0, 255)
        self.b=random.randrange(0, 255)

    def setLedColor(self):  # Implement later with actual WS2813 lib function
        # self.ledNumber.set(r,g,b)
        return
