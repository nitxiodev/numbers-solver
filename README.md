# numbers-solver
Solver of the numbers part of the mythical French TV game 'Des chiffres et des lettres'.

# Rules of game
- Target number **must** be in the range of 100 to 999, both includes.
- Choices **must** be an array with **6** of these numbers (repeated numbers are allowed): 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 25, 50, 75 or 100.

The script **doesn't** check those restrictions.

# How it works?
This solver implements a backtracking approach with several branch and prune optimizations:
- Numbers in increasing order.
- Partial results less than 0 or floats are discarded.
- If performing an operation give us the same result than a or b, we discard that operation.
- We only explore solutions that improve the previous solution (i.e. less number of operations).
- If it is impossible to reach the target, we keep the solution that minimizes the distance to that target.

# Use
Go to the example.py file, and choose the target number and the list of choices. After that, run it!

# Examples
| Numbers  | Target | Solution | time(s) | #Recursions |
| ------------- | ------------- | ------------- | ------------- |  ------------- |
| 25, 75, 100, 50, 8, 1  | 944  | 8+1=9, 75+50=125, 125/25=5, 100+5=105, 105x9=945 | 0.31s | 18680 |
| 4, 10, 25, 6, 7, 7  | 378  | 10x7=70, 70-7=63, 63x6=378 | 0.15s | 5158 |
| 75, 25, 50, 100, 8, 2  | 431  | 100+2=102, 75x50=3750, 3750-102=3648, 3648/8=456, 456-25=431 | 0.44s | 25126 |
| 25, 100, 75, 50, 6, 4  | 821  | 75+4=79, 100+50=150, 150x6=900, 900-79=821 | 0.33s | 14329 |
| 25, 50, 75, 100, 3, 6  | 952  | 75x3=225, 100+6=106, 225x106=23850, 23850-50=23800, 23800/25=952 | 0.43s | 25381 |
| 6, 5, 4, 3, 2, 2  | 952  | 3x2=6, 6+2=8, 5x4=20, 8x6=48, 48x20=960 | 0.08s | 2758 |
