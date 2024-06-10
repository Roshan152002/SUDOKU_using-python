# import pygame library
import pygame
import random
# initialise the pygame font
pygame.font.init()
pygame.display.set_caption("SUDOKU")

# Total window
screen = pygame.display.set_mode((500, 650))
x = 0
y = 0
dif = 500 / 9
val = 0

grid=[
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


sgrid1=[
        [7, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [8, 5, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 9, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7] 
   ]
# Load test fonts for use
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 15)

def get_cord(pos):
       global x
       x = pos[0]//dif
       global y
       y = pos[1]//dif
       global R

# Function to draw required lines for making Sudoku grid 
def draw ():	
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0:
				pygame.draw.rect (screen,  (51,79,255),  (j* dif, i * dif, dif + 1, dif + 1))
				text_1 = font1.render(str(grid[i][j]), 1,  (0, 0, 0))
				screen.blit (text_1,  (j * dif + 15 , i * dif ))
	for i in range (10):
		if i % 3 == 0 :
                         thick = 4
		else:
	                thick = 1
		pygame.draw.line (screen,  (0, 0, 0),  (0, i * dif),  (550, i * dif), thick)
		pygame.draw.line (screen,  (0, 0, 0),  (i * dif, 0),  (i * dif, 500), thick)
 
 # Highlight the cell selected
def draw_box():
       for i in range(2):
                pygame.draw.line(screen, (0, 0, 0), (x * dif-3, (y + i)*dif), (x * dif + dif + 3, (y + i)*dif), 7)
                pygame.draw.line(screen, (0, 0, 0), ( (x + i)* dif, y * dif ), ((x + i) * dif, y * dif + dif), 7)

# Fill value entered in cell
def draw_val(val,sgrid1):
         text1 = font1.render(str(val), 1, (0, 0, 0))
         screen.blit(text1, (x * dif + 15, y * dif ))
# Raise error when wrong value entered
def raise_error1():
        text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))
        
def raise_error2():
        text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
        screen.blit(text1, (20, 570))

# Check if the value entered in board is valid
def valid(s ,m , i, j, val):
       for it in range(9):
                 if m[i][it]== val:
                            return False
                 if m[it][j]== val:
                            return False
                            
       it = i//3
       jt = j//3
       for i in range(it * 3, it * 3 + 3):
                for j in range (jt * 3, jt * 3 + 3):
                         if m[i][j]== val:
                                   return False
       return True

# Solves the sudoku board using the Backtracking Algorithm
def solve(grid, i, j):

    while grid[i][j]!= 0:
          if i<8:
               i+= 1
          elif i == 8 and j<8:
               i = 0
               j+= 1
          elif i == 8 and j == 8:
               return True
    pygame.event.pump()
    
    for it in range(1, 10):
          if valid(sgrid1,grid, i, j, it)== True:
                   grid[i][j]= it
                   global x, y
                   y = i
                   x = j
                   # white color background
                   screen.fill((255, 255, 255))
                   draw()
                   draw_box()
                   pygame.display.update()
                   pygame.time.delay(20)
                   if solve(grid, i, j)== 1:
                              return True
                   else:
                              grid[i][j]= 0
                   # white color background\
                   screen.fill((255, 255, 255))
                   draw()
                   draw_box()
                   pygame.display.update()
                   pygame.time.delay(50)
    return False

# Display instruction for the game
def instruction():
        text1 = font2.render("press D for default grid and R for blank grid", 1, (0, 0, 0))
        text2 = font2.render("press Enter for solution of sudoku", 1, (0, 0, 0))
        text3 = font2.render("press N for New Game!!", 1, (0, 0, 0))
        screen.blit(text1, (20, 520))
        screen.blit(text2, (20, 540))
        screen.blit(text3, (20, 560))

# Display options when solved
def result():
      text1 = font1.render("GAME FINISHED!!", 1, (0, 0, 0))
      screen.blit(text1, (10, 570))
run = True
flag1 = 0
flag2 = 0
rs = 0
error = 0

# The loop thats keep the window running
while run:
      # White color background
        screen.fill((255, 255, 255))
      # Loop through the events stored in event.get()
        for event in pygame.event.get():
            # Quit the game window
             if event.type == pygame.QUIT:
                  run = False
           # Get the mouse position to insert number
             if event.type == pygame.MOUSEBUTTONDOWN:
                 flag1 = 1
                 pos = pygame.mouse.get_pos()
                 get_cord(pos)
                 
           # Get the number to be inserted if key pressed
             if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                             x-= 1
                             flag1 = 1
                     if event.key == pygame.K_RIGHT:
                             x+= 1
                             flag1 = 1
                     if event.key == pygame.K_UP:
                             y-= 1
                             flag1 = 1
                     if event.key == pygame.K_DOWN:
                             y+= 1
                             flag1 = 1
                     if event.key == pygame.K_1:
                            val = 1
                     if event.key == pygame.K_2:
                             val = 2
                     if event.key == pygame.K_3:
                             val = 3
                     if event.key == pygame.K_4:
                             val = 4
                     if event.key == pygame.K_5:
                             val = 5
                     if event.key == pygame.K_6:
                             val = 6
                     if event.key == pygame.K_7:
                             val = 7
                     if event.key == pygame.K_8:
                             val = 8
                     if event.key == pygame.K_9:
                             val = 9
                     if event.key == pygame.K_RETURN:
                             flag2 = 1
                    # If R pressed clear the sudoku board
                     if event.key == pygame.K_r:
                             rs = 0
                             error = 0
                             flag2 = 0
                             grid =[
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0],
                            [0, 0, 0, 0, 0, 0, 0, 0, 0]
                            ]
                   # If D is pressed reset the board to default
                     if event.key == pygame.K_d:
                            rs = 0
                            error = 0
                            flag2 = 0
                            grid =[
                            [7, 8, 0, 4, 0, 0, 1, 2, 0],
                            [6, 0, 0, 0, 7, 5, 0, 0, 9],
                            [0, 0, 0, 6, 0, 1, 0, 7, 8],
                            [0, 0, 7, 0, 4, 0, 2, 6, 0],
                            [0, 0, 1, 0, 5, 0, 9, 3, 0],
                            [9, 0, 4, 0, 6, 0, 0, 0, 5],
                            [0, 7, 0, 3, 0, 0, 0, 1, 2],
                            [1, 2, 0, 0, 0, 7, 4, 0, 0],
                            [0, 4, 9, 2, 0, 6, 0, 0, 7]
                            ]
                     if event.key == pygame.K_n:
                        rs = 0
                        error = 0 
                        flag2 = 0 
                        # grid = random.choice(grids)
             if flag2 == 1:
                  if solve(grid, 0, 0)== False:
                           error = 1
                  else:
                           rs = 1
                           flag2 = 0
             if val != 0: 
                   draw_val(val,sgrid1)
                   if valid(sgrid1,grid, int(y), int(x), val)== True:
                        if val == sgrid1[int(y)][int(x)] :
                           grid[int(y)][int(x)] = val 
                           flag1 = 0
                   else:
                           grid[int(y)][int(x)]= 0
                           raise_error2()
             val = 0
             if error == 1:
                    raise_error1()
             if rs == 1:
                    result()
             draw()
             if flag1 == 1:
                    draw_box()
             instruction()
            # Update window
             pygame.display.update()
# Quit pygame window
pygame.quit()