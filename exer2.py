import tkinter as tk

#check if the input in puzzle.in is solvable or not
def solvable(content):
    # taken from https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    lessthan = 0
    for i in range(0, 9):
        for sub in range(i+1, 9):
            if int(content[i]) != 0 and int(content[sub]) != 0 and int(content[i]) > int(content[sub]): lessthan += 1
    return lessthan%2

#this function checks if the buttons in the buttons list are in order or not
#must accept a string so i'll have to change my implementation 
def goalTest(buttons):
    global w
    for i in range(0,7):
        if buttons[i]['text'] != i+1: return False
    if buttons[8]['text'] != 0: return False
    disableAllButtons()
    tk.messagebox.showinfo("", "you win!")
    return True

def disableAllButtons():
    for i in range(0,9):
        buttons[i].config(state="disabled")
    return

def swap(zero, direction):
    zero['text'] = direction['text']
    direction['text'] = 0
    return

#this function checks if the button being clicked is adjacent (VALID) to the empty tile and swaps it
def ifValid(row, column):
    #if clicked, check if adjacent to 0
    to_check = [-1, 1]
    if buttons[row*3+column]['text'] == 0:
        return
    #check horizontally
    for y_test in to_check:
        #row*3+(column+y_test) << 0
        if  0 <= column+y_test <= 2:
            if buttons[row*3+(column+y_test)]['text'] == 0:
                swap(buttons[row*3+(column+y_test)], buttons[row*3+column])
                goalTest(buttons)
                return
    #check vertically
    for y_test in to_check:
        #(row+y_test)*3+column << 0
        if  0 <= row+y_test <= 2:
            if buttons[(row+y_test)*3+column]['text'] == 0:
                swap(buttons[(row+y_test)*3+column], buttons[row*3+column])
                goalTest(buttons)
                return

    #find a way to get the row and column of button clicked
    print('not adjacent')
    return 0

def availPaths(zero):
    #zero is the index of zero
    validPaths = ''
    if zero-3 >= 0:
        validPaths = validPaths + 'U'
    if zero+3 <= 8:
        validPaths = validPaths + 'D'
    if int((zero-1)/3) == int(zero/3):
        validPaths = validPaths + 'L'
    if int((zero+1)/3) == int(zero/3):
        validPaths = validPaths + 'R'

    return validPaths

def recordStates():
    state = ''
    for i in range(0,9):
        state = state + buttons[i]['text']
    return state

def disableAllButtons():
    for i in range(0,9):
        buttons[i].config(state="disabled")
    return

def BFSearch(content, zero):
    print(zero)
    initialState = content #content is string
    frontier = {} #list of strings containing the states
    # currentState = frontier.pop()
    for action in availPaths(zero):
        match action:
            case "U":
                print('up')
            case "D":
                print('down')
            case "L":
                print('left')
            case "R":
                print('right')
    print("")
    return

#--------- main function -------
with open("puzzle.in", "r") as file:
    content = file.read()

#content is a string so we need to remove the spaces
content = content.replace(" ","")
content = content.replace("\n","")

if not solvable(content):
    w = tk.Tk()
    w.title("Beltran - 8 game")
    buttons = []
    
    for row in range(0,3):
        for column in range(0,3):
            buttons.append(tk.Button(w, text=int(content[row*3+column]),padx=30, pady=30, command=lambda i=row, j=column: ifValid(i,j)))
            buttons[row*3+column].grid(row=row, column=column)
            if int(content[row*3+column]) == 0:
                zero = row*3+column

    solved = goalTest(buttons)
    print(solved)
    while not solved:
        tk.Button(w, text='search', command= BFSearch(content, zero)).grid(row=3,column=0)
        w.mainloop()
        solved = True
        #uhh the string is an array now i think so we can use that to display it in a GUI
    print("solved!")
else:
    print("unsolvable!")