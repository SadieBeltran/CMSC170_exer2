def findZero(content):
    # returns the index of zero
    for i in range(0,9):
        if int(content[i]) == 0:
            return i

def getDistance(content):
    h = 0
    currRow = contentRow = 0
    #get row by int(i/3)
    #get col by i-(int(i/3)*3)
    for i in range(0,9):
        if int(content[i]) != 0:
            #abs(x1-x2 + y1-y2)
            #where x1 and y1 are the current coordinates
            #and x2 and y2 are the supposed coordinates which we can get by substituting i for (content[i]-1)
            currRow = int(i/3)
            contentRow = int((int(content[i])-1)/3)
            h = h + abs((currRow-contentRow)) + abs(((i-(currRow*3))-((int(content[i])-1)-(contentRow*3))))
            # print("i: "+content[i]+" h: "+ str(h) + " distancex: " + str(abs((currRow-contentRow))) + " distancey: "+str(abs(((i-(currRow*3))-((int(content[i])-1)-(contentRow*3))))))
        # h += indexHeuristic
    return h
        
def availPaths(zero):
    validPaths = ''
    if zero-3 >= 0:
        validPaths = validPaths + 'U'
    if int((zero+1)/3) == int(zero/3):
        validPaths = validPaths + 'R'
    if zero+3 <= 8:
        validPaths = validPaths + 'D'
    if int((zero-1)/3) == int(zero/3):
        validPaths = validPaths + 'L'
    # print(validPaths)
    return reversed(validPaths)

def ifsolved(state):
    for i in range(0,7):
        if int(state[i]) != i+1: return False
    if int(state[8]) != 0: return False
    return True

def swap(state, factor, zero):
    # print("state: "+state+" factor: "+ str(factor)+" zero: "+str(zero))
    swapped = list(state)
    swapped[zero] = swapped[zero+factor]
    swapped[zero+factor] = '0'
    return str("".join(swapped))

def searchEncountered(currSet, encountered):
    # print("\ncurrstate: "+ currSet + " encountered: "+str(encountered))
    for element in encountered:
        # print(element)
        i = 0
        for i in range(0,9):
            if int(currSet[i]) != int(element[i]):
                # print(str(i) + "<= i "+ currSet[i] +" <= currSet | element =>" + element[i])
                #if the set isn't exactly the same, break and move to the next element
                break
            #however if it completes without breaking, that means that the currentSet exists in encountere
        # print(str(i))
        if i == 8:
            return True
    # print("not encountered")
    return False

def takeH(elem):
    #used to help with sorting really
    return elem[3]

def aSearch(content):
    #first in first out
    zero = findZero(content)
    #tuple contains (state string, the solution string, the number of steps taken, and heuristic which is the sum of steps taken and the distance)
    #i think number of steps taken is just len(solString)-1
    frontier = [(content, str(zero), 0, 0)] #initial state
    encountered = set()
    i = 0
    while len(frontier) != 0:
        #find the state with the minimum heuristic (frontier[3]) and pop it
        #how to find it?
        frontier.sort(key=takeH)
        # print(str(frontier) + "\n")
        currStatetuple = frontier.pop(0)
        if ifsolved(currStatetuple[0]):
            return (currStatetuple[1], len(encountered))
        else: 
            solution = currStatetuple[1]
            currState = currStatetuple[0]
            stepsTaken = len(solution)-1
            zero = findZero(currState)
            encountered.update((currState, ))
            for action in availPaths(zero):
                match action:
                    case "U":
                        solution = solution + "U"
                        nextState = swap(currState, -3, zero)
                    case "D":
                        solution = solution + "D"
                        nextState = swap(currState, 3, zero)
                    case "L":
                        solution = solution + "L"
                        nextState = swap(currState, -1, zero)
                    case "R":
                        solution = solution + "R"
                        nextState = swap(currState, 1, zero)
                # print("state: " + nextState + " distance: "+str(getDistance(nextState)))
                if not searchEncountered(nextState, encountered):
                    frontier.append((nextState, solution, stepsTaken+1, stepsTaken+1+getDistance(nextState)))
                solution = currStatetuple[1]
        # i += 1
        # if i == 10: break
    return "no solution found"
        
# content = '123480765'
# print(aSearch(content))

#find a way to get solution to show the right thing
#fine a way to properly store the contents of encountered