def returnMiddleValueint(a, b, c):



    if a <= b and a >= c:
        return a

    if b <= a and b >= c:
        return b

    if c <= b and c >= a:
        return c

    if a <= c and a >= b:
        return a

    if b <= c and b >= a:
        return b

    if c <= a and c >= b:
        return c


def returnMiddleValue(f, m, l):

    a = f[0]
    b = m[0]
    c = l[0]

    if a <= b and a >= c:
        return f

    if b <= a and b >= c:
        return m

    if c <= b and c >= a:
        return l

    if a <= c and a >= b:
        return f

    if b <= c and b >= a:
        return m

    if c <= a and c >= b:
        return l


def IssmallerThanThePivot(list, pivotValue, elementToCheckValue):


    if   elementToCheckValue < pivotValue:
        return True

    return False

def swap(firstElementArray, secondElementArray, list):

    outputList = list
    tempParam = firstElementArray
    SwitchedFirstElement = secondElementArray
    SwitchedSecondElement = tempParam

    if SwitchedSecondElement[0] != SwitchedFirstElement[0]:
        outputList[SwitchedSecondElement[1]] = SwitchedFirstElement[0]
        outputList[SwitchedFirstElement[1]] = SwitchedSecondElement[0]
    return outputList

