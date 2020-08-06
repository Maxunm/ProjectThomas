def askQuestion():
    while True:
        col = int(input("Column [0-31]: "))
        if col <= 31 and col >= 0:
            break
        else:
            print("Column Number Must be Between 0 and 31")

    while True:
        row = int(input("Row [0-7]: "))
        if row <= 7 and row >= 0:
            break
        else:
            print("Row Number Must be Between 0 and 7")
    
    print("LED Number: " + str(getLedNumber(col, row)))


def getLedNumber(column, row):
    pcbNum = int(column / 2)
    colNum = column % 2
    if colNum == 0:
        return ((7-row) + (pcbNum * 16))
    else:
        return ((8 + row) + (pcbNum * 16))


if __name__ == "__main__":
    askQuestion()