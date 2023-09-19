def findZero(content):
    # returns the index of zero
    for i in range(0,9):
        if int(content[i]) == 0:
            return i
def availPaths(zero):
    validPaths = ''
    if zero-3 >= 0:
        validPaths = validPaths + 'U'
    if zero+3 <= 8:
        validPaths = validPaths + 'D'
    if int((zero-1)/3) == int(zero/3):
        validPaths = validPaths + 'L'
    if int((zero+1)/3) == int(zero/3):
        validPaths = validPaths + 'R'
    print(validPaths)
    return validPaths

def ifsolved(state):
    for i in range(0,7):
        if int(state[i]) != i+1: return False
    if int(state[i]) != 0: return False
    return True

def swap(state, factor, zero):
    swapped = list(state)
    swapped[zero] = swapped[zero+factor]
    swapped[zero+factor] = '0'
    return str("".join(swapped))

def search(content):
    frontier = {content}
    solution = ''
    # frontier.add()
    while len(frontier) != 0:
        print("frontier: " + str(frontier))
        currentState = frontier.pop()
        zero = findZero(currentState)
        print("current state: " + currentState + " zero: " + str(zero))
        if ifsolved(currentState):
            return solution
        else:
            for action in availPaths(zero):
                match action:
                    case "U":
                        solution = solution + 'U'
                        frontier.add(swap(currentState, 3, zero))
                    case "D":
                        solution = solution + 'D'
                        frontier.add(
                        swap(currentState, -3, zero))
                    case "L":
                        solution = solution + 'L'
                        frontier.add(swap(currentState, -1, zero))
                    case "R":
                        solution = solution + 'R'
                        frontier.add(swap(currentState, 1, zero))
    print(solution)
    return solution
content = '132056478'
zero = findZero(content)
# print(swap(content, -3, zero))
search(content)