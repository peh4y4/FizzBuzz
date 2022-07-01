from itertools import count

def FizzBuzz(startNumber,countNumber,endNumber):

    while countNumber == startNumber or countNumber <= endNumber:
        countNumber += 1
        if countNumber % 3 == 0 and countNumber % 5 == 0:
            print(str(countNumber) + " FizzBuzz")
            continue
        elif countNumber % 5 == 0:
            print(str(countNumber) + " Buzz")
            continue
        elif countNumber % 3 == 0:
            print(str(countNumber) + " Fizz")
        else:
            print(str(countNumber))

def main():
    startNumber = 0
    countNumber = 0
    endNumber = 100
    FizzBuzz(startNumber,countNumber,endNumber)

main()