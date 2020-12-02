from usedFunctions import IssmallerThanThePivot, returnMiddleValue, swap, returnMiddleValueint
import time

def sort(givenList):


    if givenList == []:
        print(8)

    firstElement = {
        "index": 0,
        "value": givenList[0]
    }

    lastElement = {
        "index": len(givenList) - 1,
        "value": givenList[len(givenList) - 1]
    }

    midElement = {
        "index": len(givenList) // 2,
        "value": givenList[len(givenList) // 2]
    }



    if len(givenList) == 1:
        return givenList



    if len(givenList) == 2:
        firstNum = None
        lastNum = None

        if givenList[0] > givenList[1]:
            firstNum = givenList[1]
            lastNum = givenList[0]

        else:
            firstNum = givenList[0]
            lastNum = givenList[1]
        newArray = [firstNum, lastNum]
        return newArray



    sortedList = givenList #this was created so the list can be changed
    pivot = returnMiddleValue(firstElement, midElement, lastElement)

    if pivot["index"] != 0:
        sortedList = swap(pivot, {"value": givenList[0], "index": 0}, sortedList)

    pivot = {"value": sortedList[0], "index": 0}
    borderIndex = 1
    border = {"value": givenList[borderIndex], "index": borderIndex}
    pointerIndex = 1
    for p in range(1, len(givenList)):

        pointer = {"value": givenList[p], "index": pointerIndex}



        IsSmaller = IssmallerThanThePivot(givenList, pivot, pointer["index"])
        if IsSmaller:

            sortedList = swap(border, pointer, sortedList)
            if borderIndex + 1 != len(givenList):
                borderIndex += 1

                border = {"value": givenList[borderIndex], "index": borderIndex}

        pointerIndex += 1



    border = {"value": givenList[border["index"] - 1], "index": border["index"] - 1}
    sortedList = swap(pivot, border, sortedList)



    if border["index"] == 0:
        border["index"] = 1

    return sort(sortedList[:border["index"]]) + [border["value"]] + sort(sortedList[border["index"] + 1:])


class Sort:
    def __init__(self):
        self.quick_sort = quick_sort




class quick_sort(Sort):
    def __init__(self):
        self.swap = swap
        self.IssmallerThanThePivot = IssmallerThanThePivot
        self.sort = sort







def returnStringThatSaysHowManyNumbers(givenList):
    numbersInThisArray = []
    stringOutput = ""

    for num in range(101):
        numbersInThisArray.append(givenList.count(num))
    for num in range(101):
        stringOutput += (str(num) + ". " + str(numbersInThisArray[num]) + " times\n")
    return stringOutput

sortClass = quick_sort()


def main():

    with  open("input.txt", "r") as inputFile:

        startTimer = time.time()
        arrayOfLines = list(filter(lambda element:  element != "", inputFile.readlines()))
        arrayOfLines = list(map(lambda element: int(element.replace("\n", "")), arrayOfLines))
        sortedList = sortClass.sort(arrayOfLines)

        outputFile = open("output.txt", "w")
        outputString = ""
        for num in sortedList:
            outputString += (str(num) + "\n")

        outputFile.write(outputString)
        afterTimer = time.time()
        print("Time it took to quick sort algorithm: " + str((afterTimer - startTimer) * 1000) + "ms")
        print(returnStringThatSaysHowManyNumbers(sortedList))


if __name__ == '__main__':
    main()




