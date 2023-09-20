import tkinter as tk
import tkinter.messagebox
import searchAlgos

solstep = 0
zero = 0
#check if the input in puzzle.in is solvable or not
def solvable(content):
    # taken from https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
    lessthan = 0
    for i in range(0, 9):
        for sub in range(i+1, 9):
            if int(content[i]) != 0 and int(content[sub]) != 0 and int(content[i]) > int(content[sub]): lessthan += 1
    return lessthan%2

#this function checks if the buttons in the buttons list are in order or not
def goalTest(buttons):    
    global w, solstep
    for i in range(0,7):
        if buttons[i]['text'] != i+1: return False
    if buttons[8]['text'] != 0: return False
    disableAllButtons()
    tk.messagebox.showinfo("", "you win!")
    solstep = 0
    return True

def disableAllButtons():
    for i in range(0,9):
        buttons[i].config(state="disabled", bg="light grey")
    return

def solvingMode():
    for i in range(0,9):
        if(int(buttons[i]['text']) == 0):
            buttons[i].config(bg='light grey')
        else:
            buttons[i].config(bg='#8ac2ed')
    return

def swap(zero, direction):
    zero['text'] = direction['text']
    direction['text'] = 0
    direction.config(bg="light grey")
    zero.config(bg='#8ac2ed')
    w.update()
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

def reset(content, buttons):
    for i in range(0,9):
        buttons[i]['text'] = int(content[i])
        buttons[i].config(state='normal',bg='#8ac2ed')
    buttons[searchAlgos.findZero(content)].config(bg='light grey')
    w.update()
    return

def step(direction, solutiontuple, buttons):
    global solstep, zero
    solstep = solstep + direction

    if not goalTest(buttons):
        if direction == 1:  
            match solutiontuple[0][solstep]:
                case "U":
                    swap(buttons[zero], buttons[zero-3])
                    zero = zero-3
                case "D":
                    swap(buttons[zero], buttons[zero+3])
                    zero = zero+3
                case "L":
                    swap(buttons[zero], buttons[zero-1])
                    zero = zero-1
                case "R":
                    swap(buttons[zero], buttons[zero+1])
                    zero = zero+1
        elif direction == -1:
            match solutiontuple[0][solstep+1]:
                case "U":
                    swap(buttons[zero], buttons[zero+3])
                    zero = zero+3
                case "D":
                    swap(buttons[zero], buttons[zero-3])
                    zero = zero-3
                case "L":
                    swap(buttons[zero], buttons[zero+1])
                    zero = zero+1
                case "R":
                    swap(buttons[zero], buttons[zero-1])
                    zero = zero-1
    return

def solve(content, buttons, algo):
    global solstep, zero
    solstep = 0
    reset(content, buttons)
    disableAllButtons()
    if algo == 0: #BFS
        solutiontuple = searchAlgos.bFSearch(content)
    else:
        solutiontuple = searchAlgos.dFSearch(content)
    solvingMode()

    if type(solutiontuple) != str:
        stepsFound = len(solutiontuple[0])-1
        zero = int(solutiontuple[0][0])
        tk.Label(w, text="steps found: "+str(stepsFound)+"\nstates encountered: "+str(solutiontuple[1])).grid(row=5, columnspan=2)
        # print(solutiontuple[0])

        tk.Button(w, text=">", command=lambda solutiontuple=solutiontuple, buttons=buttons: step(1,solutiontuple, buttons)).grid(row=6, column=2)
        
        tk.Button(w, text="<", command=lambda solutiontuple=solutiontuple, buttons=buttons:step(-1,solutiontuple, buttons)).grid(row=6, column=0)
        w.update()
        
    else:
        print("no sol")
        reset(content, buttons)

    return

#--------- main function -------
with open("puzzle.in", "r") as file:
    content = file.read()

#content is a string so we need to remove the spaces
content = content.replace(" ","")
content = content.replace("\n","")
w = tk.Tk()
w['padx'] = w['pady'] = 3
w.title("Beltran - 8 game")
buttons = []

for row in range(0,3):
    for column in range(0,3):
        buttons.append(tk.Button(w, text=int(content[row*3+column]),padx=30, pady=30, command=lambda i=row, j=column: ifValid(i,j), bg='#8ac2ed'))
        buttons[row*3+column].grid(row=row, column=column)

if not solvable(content):
    buttons[searchAlgos.findZero(content)].config(bg='light grey')
    solved = goalTest(buttons)
    print(solved)
    while not solved:
        tk.Button(w, text='Reset', padx=10, pady=20, command=lambda content=content, buttons=buttons: reset(content, buttons)).grid(row=4,column=0)
        bFSearch = tk.Button(w, text='BFS', padx=10, pady=20, command=lambda content=content, buttons=buttons: solve(content, buttons, 0)).grid(row=4,column=1)
        dFSearch = tk.Button(w, text='DFS', padx=10, pady=20, command=lambda content=content, buttons=buttons: solve(content, buttons, 1)).grid(row=4,column=2)
        w.mainloop()
        solved = True
        #uhh the string is an array now i think so we can use that to display it in a GUI
else:
    tk.Label(w, text="unsolvable!")
    disableAllButtons()
    tk.messagebox.showinfo("", "unsolvable!")
    w.mainloop()
    print("unsolvable!")
    