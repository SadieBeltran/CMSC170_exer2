# Repo for CMSC 170 U - exer 2: BFS/DFS algo for 8 puzzle game

https://classroom.google.com/c/NjE5NzU3NDU5Njkz/a/NjIzMjU1NDc3NDc3/details

## BFS (FIFO) and DFS (FILO)
- Way to check available moves
- Keep track of the parent state and the path cost
- Queue the possible states (imagine a tree)
- note that one of the possible children states can be a duplicate, we can avoid it.
- Create a set of explored frontiers.
    - so a way to check if the resulting state exists in the explored set

## TODO:
- reimplement the game so that GoalTest() accepts a string
- implement changes from beltranesb_ui_review.py
- **FIGURE OUT HOW BFS AND DFS WORKS**