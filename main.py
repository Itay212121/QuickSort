from usedFunctions import IssmallerThanThePivot, returnMiddleValue, swap, returnMiddleValueint
import time
import json
def sort(givenList):

    firstElementIndex = 0
    firstElement = givenList[0]


    lastElementIndex = len(givenList) - 1
    lastElement =  givenList[len(givenList) - 1]


    midElementIndex = len(givenList) // 2
    midElement = givenList[len(givenList) // 2]




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
    pivotArray = returnMiddleValue([firstElement, firstElementIndex], [midElement, midElementIndex], [lastElement, lastElementIndex])
    pivotValue = pivotArray[0]
    pivotIndex = pivotArray[1]

    if pivotIndex != 0:
        sortedList = swap(pivotArray,  [givenList[0],  0], sortedList)

    borderIndex = 1
    borderValue = givenList[borderIndex]
    for currentPointerIndex in range(1, len(givenList)):

        ThisIterPointerValue = givenList[currentPointerIndex]



        IsSmaller = IssmallerThanThePivot(givenList, pivotValue, ThisIterPointerValue)
        if IsSmaller:

            sortedList = swap([borderValue, borderIndex], [ThisIterPointerValue, currentPointerIndex], sortedList)
            if borderIndex + 1 != len(givenList):
                borderIndex += 1

                borderValue = givenList[borderIndex]

    sortedList = swap([pivotValue, pivotIndex], [borderValue, borderIndex], sortedList)

    if borderIndex == 0:
        borderIndex = 1

    return sort(sortedList[:borderIndex]) + [borderValue] + sort(sortedList[borderIndex + 1:])


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



def returnAvrageSortTime(timeItTook):
    with open("sortTime.json") as jsonFile:
        data = json.load(jsonFile)
        currentSortHistory = data["sortHistory"]
        currentSortHistory = currentSortHistory.strip('][').split(', ')
        if currentSortHistory == [""]:
            currentSortHistory = []
        if currentSortHistory == []:
            currentSortHistory = [timeItTook]
            with open("sortTime.json", "w") as jsonFile:
                jsonFormat = {'sortHistory': str(currentSortHistory) }
                json.dump(jsonFormat, jsonFile)
            return timeItTook

        currentSortHistory.append(timeItTook)
        totalTime = 0
        IndexOfTime = 0
        betterSortHistory = []
        for time in currentSortHistory:
            betterSortHistory.append(time.replace('"', "").replace("'", ""))
            totalTime += int(time.replace('"', "").replace("'", ""))
            IndexOfTime += 1
        avrageTime = totalTime / IndexOfTime
    with open("sortTime.json", "w") as jsonFile:
        jsonFormat = {'sortHistory': str(betterSortHistory)}

        json.dump(jsonFormat, jsonFile)
    return avrageTime


def main():
    IsWantToSeeList = "y" in input("Do u want to see a full list of the numbers with the numbers they show up? (y/n)")
    with  open("input.txt", "r") as inputFile:
        MainClass = Sort()
        sortClass = MainClass.quick_sort()
        startTimer = time.time()
        arrayOfLines = list(filter(lambda element:  element != "", inputFile.readlines()))
        arrayOfLines = list(map(lambda element: int(element.replace("\n", "")), arrayOfLines))
        print("Sorting a list with length of " + str(len(arrayOfLines)))

        sortedList = sortClass.sort(arrayOfLines)

        outputFile = open("output.txt", "w")
        outputString = ""
        for num in sortedList:
            outputString += (str(num) + "\n")

        outputFile.write(outputString)
        afterTimer = time.time()
        timeItTook = (afterTimer - startTimer) * 1000
        avrageTime = str(returnAvrageSortTime(str(timeItTook)[:4]))

        print("Time it took to quick sort algorithm: " + str(timeItTook)[:4] + "ms")
        print("The current avrage time it takes: " + avrageTime[:4]  + "ms")

        if IsWantToSeeList:
            print(returnStringThatSaysHowManyNumbers(sortedList))


if __name__ == '__main__':

    main()




