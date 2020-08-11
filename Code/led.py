import json
import zipfile
from ledMatrix import Animation

matrixWith = 39
matrixHeight = 15


def askQuestion():
    global matrixWith, matrixHeight
    while True:
        col = int(input("Column [0-" + str(matrixWith) + "]: "))
        if matrixWith >= col >= 0:
            break
        else:
            print("Column Number Must be Between 0 and " + str(matrixWith))

    while True:
        row = int(input("Row [0-" + str(matrixHeight) + "]: "))
        if matrixHeight >= row >= 0:
            break
        else:
            print("Row Number Must be Between 0 and " + str(matrixHeight))

    print("LED Number: " + str(getLedNumber(col, row)))


def getLedNumber(column, row):
    global matrixWith, matrixHeight
    pcbNum = int(column / 2)
    colNum = column % 2
    if colNum == 0:
        return (matrixHeight - row) + (pcbNum * ((matrixHeight + 1) * 2))
    else:
        return ((matrixHeight + 1) + row) + (pcbNum * ((matrixHeight + 1) * 2))


def compressFileToString(inputFile):
    """
    read the given open file, compress the data and return it as string.
    """
    stream = StringIO()
    compressor = gzip.GzipFile(fileobj=stream, mode='w')
    while True:  # until EOF
        chunk = inputFile.read(8192)
        if not chunk:  # EOF?
            compressor.close()
            return stream.getvalue()
        compressor.write(chunk)


def saveAnimationData(animation, fileName):
    datFile = open(fileName, 'wb')
    for l in range(0, len(animation.matrices)):  # Write whole animation
        for i in range(0, len(animation.matrices[0].panels)):  # Write frame of animation
            for j in range(0, len(animation.matrices[0].panels[0].leds)):  # Write data for individual panel
                datFile.write(
                    animation.matrices[l].panels[i].leds[j].r.to_bytes(1, byteorder='big'))  # Write red value for led
                datFile.write(
                    animation.matrices[l].panels[i].leds[j].g.to_bytes(1, byteorder='big'))  # Write green value for led
                datFile.write(
                    animation.matrices[l].panels[i].leds[j].b.to_bytes(1, byteorder='big'))  # Write blue value for led
    datFile.close()


def loadAnimationData(fileName):
    datFile = open(fileName, 'rb')
    retAnimation = Animation()
    for i in range(0, len(retAnimation.matrices)):  # Read whole animation
        for j in range(0, len(retAnimation.matrices[0].panels)):  # Read frame of animation
            for k in range(0, len(retAnimation.matrices[0].panels[0].leds)):  # Read data for individual panel
                retAnimation.matrices[i].panels[j].leds[k].r = datFile.read(1)  # Read red
                retAnimation.matrices[i].panels[j].leds[k].g = datFile.read(1)  # Read green
                retAnimation.matrices[i].panels[j].leds[k].b = datFile.read(1)  # Read blue
    return retAnimation


if __name__ == "__main__":
    # askQuestion()
    # mainMatrix = Matrix()
    mainAnimation = Animation()

    saveAnimationData(mainAnimation, 'testAnimation.dat')
    with zipfile.ZipFile('testAnimation.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
        myzip.write('testAnimation.dat')

    # arr = bytearray(mainAnimation)
    # print(arr)
    # file.write(arr)
