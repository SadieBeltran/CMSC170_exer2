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
def ifSolved():    
    global w
    for i in range(0,7):
        if buttons[i]['text'] != i+1: return False
    if buttons[8]['text'] != 0: return False
    w.quit()
    return True

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
                buttons[row*3+(column+y_test)]['text'] = buttons[row*3+column]['text'] # zero to number to swap
                buttons[row*3+column]['text'] = 0 #number to zero
                ifSolved()
                return
    #check vertically
    for y_test in to_check:
        #(row+y_test)*3+column << 0
        if  0 <= row+y_test <= 2:
            if buttons[(row+y_test)*3+column]['text'] == 0:
                buttons[(row+y_test)*3+column]['text'] = buttons[row*3+column]['text'] # zero to number to swap
                buttons[row*3+column]['text'] = 0 #number to zero
                ifSolved()
                return

    #find a way to get the row and column of button clicked
    print('not adjacent')
    return 0

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

    solved = ifSolved()
    print(solved)
    while not solved:
        w.mainloop()
        solved = True
        #uhh the string is an array now i think so we can use that to display it in a GUI
    print("solved!")
else:
    print("unsolvable!")