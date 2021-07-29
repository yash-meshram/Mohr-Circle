This App is an app to visualise Mohr Circle in 3-D
Made by - Rwik Rana, Yash Meshram

# HOW TO USE via EXE #
To run the executable form of the app, 
1. Go to build
2. GO to exe.win-amd64-3.8
3. Double-Click on Mohr_game.executable

The app would start!!

# HOW TO USE via Python #
Python Dependencies required:
1. Python 3.4 + 
2. Matplotlib
3. Scipy
4. Numpy
5. Pygame
------------------------------------------------------------------
The entire project has a category of files.
1. Backend Code
2. Front End Code

Backend Code has 2 files:
1. MohrCircle_stress.py
2. MohrCircle_strain.py

View the above files to know how to run the code. Currently, 
the execution of these files on their own have been commented
for app purpose, one can uncomment to use these files independently.

To run the files type in the command prompt/bash

python MohrCircle_stress.py 
OR
python MohrCircle_strain.py 
--------------------------------------------------------------

These two files are very similar and have similar working.
These files are the backbone to all calculations in the app.
These files can be used separately to get the graphs.

The Frontend Code is made on Pygame.
There are many types of files in the Frontend.
1. Window files (Manages the windows)
2. Utility files (Manages utilities like buttons, boxes)
3. Main files (main execution)

To run the app via python, use the following line in the cmd:

python mohr_game.py
