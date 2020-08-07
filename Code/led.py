import json
import zipfile
from ledMatrix import Animation

matrixWith = 39
matrixHeight = 15


def askQuestion():
    global matrixWith, matrixHeight
    while True:
        col = int(input("Column [0-" + str(matrixWith) + "]: "))
        if col <= matrixWith and col >= 0:
            break
        else:
            print("Column Number Must be Between 0 and " + str(matrixWith))

    while True:
        row = int(input("Row [0-" + str(matrixHeight) + "]: "))
        if row <= matrixHeight and row >= 0:
            break
        else:
            print("Row Number Must be Between 0 and " + str(matrixHeight))

    print("LED Number: " + str(getLedNumber(col, row)))


def getLedNumber(column, row):
    global matrixWith, matrixHeight
    pcbNum = int(column / 2)
    colNum = column % 2
    if colNum == 0:
        return ((matrixHeight-row) + (pcbNum * ((matrixHeight+1)*2)))
    else:
        return (((matrixHeight+1) + row) + (pcbNum * ((matrixHeight+1)*2)))


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


if __name__ == "__main__":
    askQuestion()
    # mainMatrix = Matrix()
    mainAnimation = Animation()
    file = open('matrix.json', 'w')

    matrixJSONData = mainAnimation.toJSON()
    file.write(matrixJSONData)
    file.close()
    with zipfile.ZipFile('matrix.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
        myzip.write('matrix.json')


    # arr = bytearray(mainAnimation)
    # print(arr)
    # file.write(arr)

