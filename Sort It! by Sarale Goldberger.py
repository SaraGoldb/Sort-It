# Sort It! By Sarale Goldberger

#"I hereby certify that this program is solely the result of my own work and is 
# in compliance with the Academic Integrity policy of the course syllabus and 
# the academic integrity policy of the CS department.”

import Draw
import random

# Custom Colors for my balls
RED = Draw.color(247, 74, 87)
ORANGE = Draw.color(255, 181, 28)
GREEN = Draw.color(37, 230, 186)
BLUE = Draw.color(78, 170, 237)
VIOLET = Draw.color(150, 37, 230)
PINK = Draw.color(230, 37, 202)

# Other custom colors
TEAL = Draw.color(183, 251, 249)
LIGHTTEAL = Draw.color(235, 255, 252)
LILAC = Draw.color(191, 3, 214)
PALEPINK = Draw.color(255, 250, 253)
MINT = Draw.color(228, 255, 255)
LIGHTMINT = Draw.color(245, 255, 255)
DEEPBLUE = Draw.color(21, 131, 232)
BUTTER = Draw.color(255, 248, 150)

# Dictionary of my custom ball colors with corresponding letter keys
COLORS = {'R': RED, 'O': ORANGE, 'G': GREEN, 'B': BLUE, 'V': VIOLET, 'P': PINK}

# Basic dimensions accessed throughout my program, authorized globals
CANVASW = 1000
CANVASH = 500
BALL_SIZE = 60
BALL_SPACING = 10  # the space between the ball and the wall of the tube
TUBE_SPACING = 20  # the space between each tube
TUBE_WIDTH = BALL_SIZE + BALL_SPACING*2
TUBE_BLOCKING = TUBE_WIDTH + TUBE_SPACING 
REDOX = 22
REDOY = CANVASH - 89
REDOSIZE = 40

# Initial mixed puzzles
puzzle1 = [['G', 'R', 'B', 'R'],
           ['G', 'B', 'R', 'G'],
           ['B', 'R', 'G', 'B'],
           []
           ]
puzzle2 = [['O', 'B', 'O', 'R'],
           ['R', 'O', 'R', 'B'],
           ['B', 'R', 'B', 'O'],
           []
           ]
puzzle3 = [['R', 'G', 'B', 'R'],
           ['G', 'B', 'O', 'B'],
           ['R', 'O', 'B', 'O'],
           ['O', 'G', 'R', 'G'],
           []
           ]
puzzle4 = [['B', 'V', 'O', 'B'],
           ['G', 'O', 'V', 'G'],
           ['V', 'B', 'O', 'B'],
           ['G', 'O', 'G', 'V'],
           [],
           ]
puzzle5 = [['O', 'P', 'O', 'G'],
           ['B', 'R', 'P', 'R'],
           ['G', 'R', 'G', 'O'],
           ['P', 'G', 'P', 'B'],           
           ['B', 'O', 'B', 'R'],
           [],
           ]
puzzle6 = [['B', 'G', 'P', 'R'],
           ['P', 'G', 'O', 'P'],
           ['O', 'R', 'G', 'O'],
           ['B', 'P', 'R', 'B'],
           ['R', 'O', 'B', 'G'],
           [],
           ]
puzzle7 = [['P', 'V', 'B', 'B'],
           ['V', 'O', 'V', 'R'],
           ['O', 'G', 'R', 'P'],
           ['V', 'O', 'G', 'B'],
           ['G', 'P', 'B', 'G'],
           ['R', 'O', 'P', 'R'],           
           [],
           [],
           ]
puzzle8 = [['V', 'R', 'B', 'P'],
           ['O', 'G', 'O', 'O'],
           ['R', 'V', 'B', 'V'],
           ['B', 'R', 'B', 'V'],
           ['P', 'G', 'O', 'P'],
           ['G', 'R', 'G', 'P'],
           [],
           [],
           ]
puzzle9 = [['R', 'O', 'V', 'V'],
           ['B', 'O', 'V', 'O'],
           ['R', 'P', 'P', 'G'],
           ['V', 'O', 'P', 'G'],
           ['B', 'R', 'B', 'G'],
           ['B', 'R', 'G', 'P'],
           [],
           [],
           ]
puzzle10 = [['G', 'P', 'O', 'V'],
           ['B', 'O', 'R', 'P'],
           ['B', 'O', 'V', 'G'],
           ['P', 'R', 'P', 'B'],
           ['V', 'G', 'O', 'R'],
           ['B', 'G', 'V', 'R'],
           [],
           [],
           ]
puzzle11 = [['P', 'V', 'B', 'B'],
           ['O', 'O', 'V', 'R'],
           ['R', 'G', 'R', 'P'],
           ['V', 'O', 'G', 'B'],
           ['G', 'P', 'B', 'G'],
           ['O', 'V', 'P', 'R'],
           [],
           [],
           ]
puzzle12 = [['G', 'O', 'P', 'R', 'P'],
           ['O', 'P', 'P', 'B', 'G'],
           ['G', 'R', 'R', 'R', 'O'],
           ['O', 'G', 'R', 'B', 'B'],
           ['B', 'G', 'O', 'B', 'P'],
           [],
           [],
           ]
puzzle13 = [['B', 'G', 'B', 'B', 'R'],
           ['B', 'P', 'P', 'G', 'G'],
           ['O', 'P', 'P', 'R', 'G'],
           ['R', 'O', 'O', 'O', 'P'],
           ['G', 'R', 'B', 'R', 'O'],
           [],
           [],
           ]
puzzle14 = [['B', 'O', 'G', 'V', 'O'],
           ['V', 'B', 'V', 'G', 'P'],
           ['R', 'P', 'R', 'V', 'G'],
           ['P', 'B', 'G', 'R', 'R'],
           ['B', 'R', 'P', 'O', 'G'],
           ['P', 'O', 'B', 'V', 'O'],
           [],
           [],
           ]
puzzle15 = [['P', 'V', 'B', 'R', 'G', 'R'],
           ['R', 'P', 'V', 'P', 'B', 'O'],
           ['O', 'V', 'B', 'G', 'V', 'B'],
           ['G', 'P', 'O', 'P', 'R', 'P'],
           ['O', 'G', 'V', 'G', 'O', 'B'],
           ['V', 'O', 'G', 'R', 'B', 'R'],
           [],
           [],
           ]
puzzle16 = [['O', 'V', 'B', 'O', 'G', 'V'],
           ['R', 'P', 'P', 'V', 'B', 'P'],
           ['P', 'B', 'G', 'O', 'R', 'P'],
           ['B', 'G', 'R', 'R', 'G', 'V'],
           ['G', 'B', 'R', 'O', 'P', 'O'],
           ['V', 'O', 'G', 'R', 'B', 'V'],
           [],
           [],
           ]

# 3D list of all my puzzles
PUZZLES = [puzzle1, puzzle2, puzzle3, puzzle4, puzzle5, puzzle6, puzzle7, \
           puzzle8, puzzle9, puzzle10, puzzle11, puzzle12, puzzle13, puzzle14,\
           puzzle15, puzzle16]


# draw a BSD (beis samach daled i.e. bisyata dishmaya) in the upper right corner
def BSD():
    Draw.setFontSize(12)
    Draw.setColor(BLUE)
    Draw.setFontFamily('Lucida Sans Unicode')
    Draw.string('B"SD', CANVASW-45, 5)

# Home page display of the game
def homePage():
    Draw.setBackground(TEAL) 
    
    # draw a row of balls along the top and bottom of the canvas
    ballColors = [RED, ORANGE, GREEN, BLUE, VIOLET, PINK]
    x = -20
    for row in range(15):
	    Draw.setColor(ballColors[row%6])
	    Draw.filledOval(x, 10, BALL_SIZE, BALL_SIZE)
	    Draw.setColor(ballColors[-(row%6 +1)])
	    Draw.filledOval(x, CANVASH-70, BALL_SIZE, BALL_SIZE)
	    x += 70
    
    # draw a row of balls along the sides of the canvas, not intersecting the
    # top and bottom row of balls drawn before
    y = 80
    for row in range(5):
	    Draw.setColor(ballColors[-(row%6 +1)])
	    Draw.filledOval(-20, y, BALL_SIZE, BALL_SIZE)
	    Draw.filledOval(960, y, BALL_SIZE, BALL_SIZE)
	    y += 70
    
    Draw.setColor(LIGHTTEAL)    
    Draw.filledRect(CANVASW/4.65, CANVASH/5, 560, 220)
    
    Draw.setColor(LILAC)
    Draw.setFontSize(70)
    Draw.setFontFamily('Ravie')
    Draw.string('Sort It!', CANVASW/4, CANVASH/4.54)

    Draw.setColor(PINK)    
    Draw.setFontSize(22)
    Draw.setFontFamily('Lucida Sans Typewriter')
    Draw.string('By: Sarale Goldberger', CANVASW/3.125, CANVASH/4.54 +135)
    
    Draw.setColor(DEEPBLUE)    
    Draw.setFontSize(20)
    Draw.setFontFamily('System')
    Draw.string('( Click anywhere to start )', CANVASW/3, CANVASH/1.38) 
    
    BSD()    


# create a copy of the puzzle called so the original list is not mutated, and
# can be replayed
def puzzleCopy(puzzle):
    return [[puzzle[row][col] for col in range(len(puzzle[row]))] \
                   for row in range(len(puzzle))]
    

# Loop through the rows of the puzzle.
# If every row is either empty or contains the max amount of the same color key
# of that puzzle, the puzzle is solved, and return False (the level is over).
# Otherwise, return True (the level is not over)
def GameOver(puzzle, max_balls):    
    for row in range(len(puzzle)):
	    same_color = True
	    for col in range(len(puzzle[row])-1):
		    if puzzle[row][col] != puzzle[row][col+1]:
		        same_color = False
	    if (len(puzzle[row]) != 0 and len(puzzle[row]) != max_balls) or \
	       (len(puzzle[row]) == max_balls and same_color == False):
			    return False
	    
    return True

    
# if the x,y coord of the player's click is within the space a tube occupies on
# the canvas, return which tube number it is. Otherwise, return None i.e. no 
# tube was clicked.
def getTubeNum(x, y, puzzle, tube_height, tubeLeftX, tubesY, tubesBottomY):    
    # The tube number is the difference of the x coord of the click and the x 
    # coord of the first tube (i.e. the shift) plus tube blocking (so the first
    # tube is included), all int-divided by tube blocking (the spacing of tubes)
    tubeNum = (x - tubeLeftX + TUBE_BLOCKING) // TUBE_BLOCKING
    
    # Calculate the x coord of the last tube in the puzzle:
    # The sum of the x coord of the first tube and tube blocking of every tube,
    # minus a tube spacing (fencepost problem, to remove the extra spacing).
    tube_bottomX = tubeLeftX + ((len(puzzle))*TUBE_BLOCKING) - TUBE_SPACING
    
    # Calculate the x coord of the current tube of the puzzle: The sum of the x 
    # coord of the first tube and the product of the tube blocking and the 
    # amount of tubes to its left.
    tube_currentX = tubeLeftX + ((tubeNum - 1) * TUBE_BLOCKING)
    
    # if the y coord of the click is above the y coord of the first tube, or 
    # below the y of the bottom of the first tube, or to the left of the x of
    # the first tube, or to the right of the x of the bottom of the last tube,
    # and x is not within the space of the current tube, the tube num is 
    # invalid, return None
    if y < tubesY or y > tubesBottomY or x < tubeLeftX or x > tube_bottomX or \
       not(x >= tube_currentX and x <= tube_currentX + TUBE_WIDTH): 
	    tubeNum = None

    # otherwise the tube num is valid
    return tubeNum


# if the tube sending a ball is empty or the tube receiving the ball is full,
# it is not a valid click. If the tube getting the ball is empty or the ball
# being sent is the same color as the last ball in the tube receiving, the click
# is valid. Otherwise, the click is not valid.
# Note: tube num counts from 1, indexing from 0. Subtract 1 to allign.
def validClicks(puzzle, clicks, max_balls):
    send = clicks[0] - 1
    get = clicks[1] - 1
    if len(puzzle[send]) == 0 or len(puzzle[get]) == max_balls: return False
    if len(puzzle[get]) == 0 or puzzle[get][-1] == puzzle[send][-1]: return True
    return False

    
# Remove the last 'ball' (element) from the first tube clicked and append it to
# the end of the second tube clicked.
def transferBall(puzzle, clicks):
    p = puzzle[clicks[0]-1].pop()
    puzzle[clicks[1]-1].append(p)    
 
 
# if the player clicks within the space the redo button takes up on the canvas,
# return True. Otherwise return False.   
def redoLevel(x, y):
    if x >= REDOX and x <= REDOX + REDOSIZE and y >= REDOY and \
       y <= REDOY + REDOSIZE: return True
    return False
    
    
# draw the puzzle according to the updated list
def DrawBoard(puzzle, clicks, level, randomColor, max_balls, tube_height, \
              tubeLeftX, tubesY, tubesBottomY):
    Draw.clear()
    Draw.setBackground(MINT) 
    
    BSD()
    
    Draw.setFontSize(20)   
    Draw.setFontFamily('System')
    Draw.setColor(randomColor)
    Draw.string('Level %d' % (level), 5, 5) 

    Draw.setColor(ORANGE)
    Draw.string('redo', REDOX - 8, REDOY + 42)
    Draw.picture('restart.gif', REDOX, REDOY) 
    
    # loop through each position of the tubes
    for row in range(len(puzzle)):
	
	    # Calculate the x,y coordinate of the tube:
	    # Each tube x is equal to the sum of the first tube x and the width 
	    # and spacing of the tubes to its left.
	    tubeX = tubeLeftX + (row * TUBE_BLOCKING)
	
	    # Draw a tube at x,y: Draw a black rectangle with a slightly smaller
	    # light mint rectangle on top to create a thick black outline.
	    Draw.setColor(Draw.BLACK)
	    Draw.filledRect(tubeX, tubesY, TUBE_WIDTH, tube_height)
	    Draw.setColor(LIGHTMINT)
	    Draw.filledRect(tubeX+2, tubesY, TUBE_WIDTH-4, tube_height-2)	    
	    
	    # for each ball (col) in the tube (row) calculate its x,y coord
	    # draw a filled circle at that coord, set to the color which 
	    # corresponds to the color key at that col of the puzzle
	    for col in range(len(puzzle[row])):
		    # the x coord of the ball is equal to the sum of the
		    # x coord of the current tube and the ball spacing 
		    ballX = tubeX + BALL_SPACING
		    
		    # the y coord of the ball is equal to the difference of the 
		    # last y coord of the tube and the sum of balls and spaces
		    # below it
		    ballY = tubesBottomY - ((col+1)*(BALL_SIZE + BALL_SPACING))
	    
		    # Draw a ball at x,y in the color that the key from the 
		    # color dictionary corresponds to
		    Draw.setColor(COLORS[str(puzzle[row][col])])	    
		    Draw.filledOval(ballX, ballY, BALL_SIZE, BALL_SIZE)
	    
		    # Outline in yellow the top ball of the send tube using the
		    # same outlining method as with the tubes
		    if len(clicks) > 0 and row == clicks[0]-1 and col == \
		       len(puzzle[row])-1:
			    Draw.setColor(Draw.YELLOW)
			    Draw.filledOval(ballX-3, ballY-3, \
			                    BALL_SIZE+6, BALL_SIZE+6)
			    Draw.setColor(COLORS[puzzle[row][col]])
			    Draw.filledOval(ballX+1, ballY+1, \
			                    BALL_SIZE-2, BALL_SIZE-2)

    Draw.show()
	

def playGame(puzzleCalled, level):
    # make a copy of the puzzle so that the original puzzle list is not changed
    puzzle = puzzleCopy(puzzleCalled)
    
    clicks = []
    max_balls = len(puzzle[0])
    
    # Calculate the tube height:
    # The tube height is equal to the sum of the ball spacing and the ball size
    # multiplied by the max balls per tube of the puzzle, plus an extra ball
    # spacing (there is a space on the bottom and top, meaning 1 extra spacing).    
    tube_height = (BALL_SPACING + BALL_SIZE)*(max_balls) + BALL_SPACING 
    
    # Calculate the first tube x coord: The difference of half the canvas width
    # and half the width that all the tubes takes up
    tubeLeftX = CANVASW//2 - ((len(puzzle)) * TUBE_BLOCKING - TUBE_SPACING)//2
    
    # Calculate the tubes' y coord: The difference of half the canvas height
    # and half the tube height
    tubesY = CANVASH//2 - tube_height//2
    
    # Calculate the tubes' bottom y coord: The sum of half the canvas height 
    # and half the tube height    
    tubesBottomY = CANVASH//2 + tube_height//2 
        
    # initialize a random color for the color of the 'Level' string
    randomColor = random.choice([RED, GREEN, BLUE, VIOLET, PINK])    
    
    # if the puzzle has not yet been solved, continue playing i.e. modifying
    while not GameOver(puzzle, max_balls):
	    if Draw.mousePressed():
		    x = Draw.mouseX()
		    y = Draw.mouseY()
		    
		    # if the redo function returns True i.e. if the redo button
		    # was clicked, reset puzzle to the original unmodified 
		    # puzzle passed through playGame, and reset the clicks list
		    if redoLevel(x, y) == True:
			    clicks = []
			    puzzle = puzzleCopy(puzzleCalled)
			    
		    # Find the tube number, check if it is valid, if so append
		    # it to clicks. Once clicks has two tube numbers check if
		    # the ball can be transferred, if so transfer it. Reset 
		    # clicks.
		    tubeNum = getTubeNum(x, y, puzzle, tube_height, tubeLeftX,\
		                         tubesY, tubesBottomY)
		    if tubeNum != None and tubeNum not in clicks:
			    clicks.append(tubeNum)
		    if len(clicks) == 2:
			    if validClicks(puzzle, clicks, max_balls) == True:
				    transferBall(puzzle, clicks)
			    clicks = []
	    # after modifying the list, redraw the board with the shuffled balls
	    DrawBoard(puzzle, clicks, level, randomColor, max_balls, \
	              tube_height, tubeLeftX, tubesY, tubesBottomY)
    

# When the current puzzle is solved, before playing the next puzzle display the 
# words 'Next level!' in flashing colors
def nextLevelDisplay():
    # Draw a box under the 'Next level!' display
    Draw.setColor(PALEPINK)    
    Draw.filledRect(CANVASW//2 - 225, CANVASH//2 - 70, 450, 140)
    
    # A 2D list of pairs of colors
    colorsList = [[Draw.BLUE, Draw.ORANGE],
                 [Draw.RED, Draw.GREEN],
                 [Draw.YELLOW, VIOLET],
                 [Draw.RED, Draw.BLUE],
                 [Draw.GREEN, Draw.PINK],
                 [Draw.ORANGE, VIOLET]]
    
    # Before the loop, choose a list of two different colors to 'flash'
    colorsChosen = random.choice(colorsList)
    
    # Make the string reappear rapidly and randomly change the color to create
    # a flash effect
    for i in range(200):
	    Draw.setFontSize(90)
	    Draw.setFontFamily('System')	    
	    colorFlash = colorsChosen[i%2]
	    Draw.setColor(colorFlash)
	    Draw.string('Next level!', CANVASW//2 - 210, CANVASH//2 - 65)  
	    Draw.show()    


# use on confetti page so that the confetti page does not count mouse clicks
def flushClicks():
    while Draw.mousePressed():
	    Draw.mouseX()
	    Draw.mouseY()


# initialize conffetti with random x coords that span the canvas width and 
# random y coords from tripple -CANVASH to 0 so a long stream of confetti falls
def initializeConfetti():
    confettiColors = [Draw.RED, ORANGE, VIOLET, Draw.MAGENTA, Draw.CYAN, GREEN]
    confettiXY = [[random.randint(-30,CANVASW+30), random.randint(-CANVASH*3,0)\
                   , random.choice(confettiColors)] for i in range(900)]
    return confettiXY


# content of the winner page, accessed on the confetti page and winner page
def winnerContent(): 
    Draw.setFontSize(100)   
    Draw.setFontFamily('Magneto')
    Draw.setColor(GREEN)
    Draw.string('Winner!', 205, 90)
    Draw.setColor(BLUE)  
    Draw.string('Winner!', 210, 95)
    Draw.setColor(VIOLET)
    Draw.string('Winner!', 215, 100)
    Draw.setColor(Draw.PINK)
    Draw.string('Winner!', 220, 105) 
    
    Draw.setFontSize(20)   
    Draw.setFontFamily('Fixedsys')
    Draw.setColor(PINK)
    Draw.string('Congratulations, you have completed all levels!', 120, 282)

    
    # List of border square colors
    borderList = [RED, ORANGE, VIOLET, PINK, BLUE, GREEN]  
    
    # initial x and y coord of border square
    borderX = 20
    borderY = 20
    borderY2 = 460
    
    # Redraw the border squares across the entire top and bottom of the 
    # canvas, in different colors and at three different heights
    for i in range(23):
	    Draw.setColor(borderList[i%6])
	    Draw.filledRect(borderX + i * 50 - 15, borderY, 8, 20)
	    Draw.setColor(borderList[i%6 - 2])        
	    Draw.filledRect(borderX + i * 50, borderY + 5, 8, 20)    
	    Draw.setColor(borderList[i%6 - 3])        
	    Draw.filledRect(borderX + i * 50 + 15, borderY, 8, 20)
	    
	    Draw.setColor(borderList[i%6])
	    Draw.filledRect(borderX + i * 50 - 15, borderY2, 8, 20)
	    Draw.setColor(borderList[i%6 - 1])        
	    Draw.filledRect(borderX + i * 50, borderY2 + 5, 8, 20)    
	    Draw.setColor(borderList[i%6 - 2])        
	    Draw.filledRect(borderX + i * 50 + 15, borderY2, 8, 20)    
	

# draw many confetti rectangles falling from above the canvas to below on top
# of the winner page
def confettiPage():
    Draw.setBackground(BUTTER)
    y = 0
    y2 = 0
    confettiXY = initializeConfetti()
    
    while y < CANVASH*5:
        flushClicks()
        Draw.clear() 
        BSD()
        winnerContent()
	
	# increment the value being added to the y coord of each confetti to
        # make them move towards the bottom of the canvas	
	# Note: for some reason the 'Magneto' font of the string Winner makes
	# the confetti fall slower
        y += 50    
        y2 += 45
	
        # For each piece  of confetti, increment its y coord, then draw it
        # Draw the confetti stream twice, one slower than the other for effect
        for i in range(900): 
            Draw.setColor(confettiXY[i][2])
            Draw.filledRect(confettiXY[i][0], confettiXY[i][1]+y, 8, 20) 
            Draw.filledRect(confettiXY[i][0]+10, confettiXY[i][1]+y2, 8, 20)
        
        Draw.show()


# When all the levels have been played, clear the canvas and display a winner 
# page. Allow the user to click anywhere on the page to return to the homepage
# and play the game all over again.
def winnerPage():
    
    while True:
	    Draw.clear()
	    Draw.setBackground(BUTTER) 
	    
	    BSD()
	    
	    winnerContent()
		 
	    Draw.setFontSize(20)
	    Draw.setFontFamily('System')
	    Draw.setColor(GREEN)
	    Draw.string('( Click anywhere to return to home page )', 240, 360)  
	    
	    Draw.show()
	    
	    # if the winner page is clicked, restart the game i.e. restart main
	    if Draw.mousePressed():
		    Draw.clear()
		    main()  


def main():
    # Display home page
    # if the homepage is clicked, for each of the puzzles, play the puzzle
    # display a next level string in between each level, except the last
    # when all puzzles have been played, display the confetti and winner page
    homePage()
    while True:
	    if Draw.mousePressed():
		    for i in range(len(PUZZLES)):
			    playGame(PUZZLES[i], i+1)
			    # display next level unless it is the last game
			    if i != len(PUZZLES)-1: nextLevelDisplay()
		    confettiPage() 
		    winnerPage()
    
    
# Create Canvas. Must be initialized outside of main because I reinvoke main in
# winnerPage so that the game can be played through forever, and I only want
# to draw the canvas once.
Draw.setCanvasSize(CANVASW, CANVASH)  
    
main()