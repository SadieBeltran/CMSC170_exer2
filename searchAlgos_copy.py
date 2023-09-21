def findZero(content):
    # returns the index of zero
    for i in range(0,9):
        if int(content[i]) == 0:
            return i

def stateHeuristic(content):
    h = 0
    for i in range(0,9):
        if int(content[i]) == 0:
            indexHeuristic = abs(i - 8)
        else:
            indexHeuristic = abs(i - (int(content[i])-1))
        h += indexHeuristic
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

def bFSearch(content):
    #first in first out
    zero = findZero(content)
    frontier = [(content, str(zero), 0, -1)] #initial state
    encountered = set()

    while len(frontier) != 0:
        #while frontier is not empty
        #pop the first element of the frontier
        currStatetuple = frontier.pop(0)
        #a tuple containing the current state and the solution path
        #then we check if the current state has already been encountered or solved
        if ifsolved(currStatetuple[0]):
            #return the solution path if solved
            return (currStatetuple[1], len(encountered))
        elif not searchEncountered(currStatetuple[0], encountered): 
            #check if currstate has already been encountered. If not...
            solution = currStatetuple[1]
            currState = currStatetuple[0]
            zero = findZero(currState)
            encountered.update((currState, )) #order doesn't really matter here since it's just a set of encountered states.
            for action in availPaths(zero):
                match action:
                    case "U":
                        solution = solution + "U"
                        frontier.append((swap(currState, -3, zero), solution))
                    case "D":
                        solution = solution + "D"
                        frontier.append((    
                        swap(currState, 3, zero), solution))
                    case "L":
                        solution = solution + "L"
                        frontier.append((swap(currState, -1, zero),solution))
                    case "R":
                        solution = solution + "R"
                        frontier.append((swap(currState, 1, zero),solution))
                solution = currStatetuple[1]
    return "no solution found"

def dFSearch(content):
    #FIRST IN LAST OUT
    frontier = [(content, str(findZero(content)))]
    encountered = set()
    while len(frontier) != 0:
        currStatetuple = frontier.pop(0)
        if ifsolved(currStatetuple[0]):
            #return the solution path if solved
            return (currStatetuple[1], len(encountered))
        elif not searchEncountered(currStatetuple[0], encountered): 
            #check if currstate has already been encountered. If not...
            solution = currStatetuple[1]
            currState = currStatetuple[0]
            zero = findZero(currState)
            encountered.update((currState, )) #order doesn't really matter here since it's just a set of encountered states.
            for action in availPaths(zero):
                match action:
                    case "U":
                        solution = solution + "U"
                        frontier.insert(0, (swap(currState, -3, zero), solution))
                    case "D":
                        solution = solution + "D"
                        frontier.insert(0, (    
                        swap(currState, 3, zero), solution))
                    case "L":
                        solution = solution + "L"
                        frontier.insert(0, (swap(currState, -1, zero),solution))
                    case "R":
                        solution = solution + "R"
                        frontier.insert(0, (swap(currState, 1, zero),solution))
                solution = currStatetuple[1]
    return "no solution found"
        
content = '123405786'
# print(ifsolved(content))
# print(swap(content, -3, zero))
# print("input: "+content)
# print("dfS: " + str(dFSearch(content)))
print("bfS: " + str(bFSearch(content)))
print(stateHeuristic(content))
# print(str(('hello', 'world', 1, 0)))
#find a way to get solution to show the right thing
#fine a way to properly store the contents of encountered