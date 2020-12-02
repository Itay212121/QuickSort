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

    a = f["value"]
    b = m["value"]
    c = l["value"]

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


def IssmallerThanThePivot(list, pivot, currentIndex):


    if   list[currentIndex] < pivot["value"]:
        return True

    return False

def swap(border, pointer, list):

    outputList = list
    tempParam = border
    border2 = pointer
    pointer2 = tempParam

    if pointer2["value"] != border2["value"]:
        outputList[pointer2["index"]] = border2["value"]
        outputList[border2["index"]] = pointer2["value"]
    return outputList

