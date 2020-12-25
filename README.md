Collision Detection in Games

This project has been designed to explain how the concept of Calculus can be applied in game design, specifically collision of objects. And also how you can use the concept to dexign a simple game using pygame.

 

Technology (Code)

As a proof of concept, I have decided to design a pygame based version of the classical Snake game. The reason why I chose Snake game is because it’s fairly easy to implement(there is not that much logic to code) and that it can be implemented using simple geometric figures like square and circle. Which saves us less worries when using pygame modules and python to design the game. 

The gameplay is very simple as well.
 And ofcourse to capture the hit testing. Now this game uses; 
import pygame
import sys
import random
Pygame, one of the python  modules, helps with building the game i.e that graphical aspects, and it’s also compatible with python. 
Also we also use ‘random’ for the math aspect of our game and ‘sys’ which is also useful for our game. 

The codes in details...

class Snake():
    def __init__(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.color = (17, 24, 47)




Collision detection in our game 
I could take all day long to explain bits and bits of our code, but because our focus is on collision detection, I am going to explain how we design our snake game to detect an object and trigger an action.
Now this first method really ties into getting the exact game space for the object(snake) to move(direction), add a new tail(list), define screen to move around a prompt to reset when the snake hits the end of our defined screen. 


    def move(self):
        cur = self.get_head_position()
        x,y = self.direction
        new = (((cur[0]+(x*gridsize))%screen_width), (cur[1]+(y*gridsize))%screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0,new)
            if len(self.positions) > self.length:
                self.positions.pop()


Hitting was really hard to figure out especially when the snake hit the end of the screen, but after extensive research, I was able to fix the problem. First I check if the current position of the snake reaches the end of the screen, then I call reset(). Else I check if the current position of the snake’s head matches the position of the current object(piece of food). If it does, I then add or replicate it size(using the initial formulae for forming the snake size)

    def reset(self):
        self.length = 1
        self.positions = [((screen_width/2), (screen_height/2))]
        self.direction = random.choice([up, down, left, right])
        self.score = 0

I also use this ‘def draw ‘ for the surface of the window. And create two repeatable colors in a set rectangle, And I accomplish this by adding ‘pygame.Rect’ which is sought of a list and holds every surface created.

    def draw(self,surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (gridsize,gridsize))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

Here is very simple to understand.

    def handle_keys(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(up)
                elif event.key == pygame.K_DOWN:
                    self.turn(down)
                elif event.key == pygame.K_LEFT:
                    self.turn(left)
                elif event.key == pygame.K_RIGHT:
                    self.turn(right)





The class food() is responsible for doing specific tasks like adding a piece of food in a random location as soon as the snake eats the current piece of food. As well as adjust the length of the snake as explained earlier. And the current game speed. 

class Food():
    def __init__(self):
        self.position = (0,0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, grid_width-1)*gridsize, random.randint(0, grid_height-1)*gridsize)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (gridsize, gridsize))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

def drawGrid(surface):
    for y in range(0, int(grid_height)):
        for x in range(0, int(grid_width)):
            if (x+y)%2 == 0:
                r = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface,(93,216,228), r)
            else:
                rr = pygame.Rect((x*gridsize, y*gridsize), (gridsize,gridsize))
                pygame.draw.rect(surface, (84,194,205), rr)

screen_width = 480
screen_height = 480

gridsize = 20
grid_width = screen_width/gridsize
grid_height = screen_height/gridsize

up = (0,-1)
down = (0,1)
left = (-1,0)
right = (1,0)

def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    drawGrid(surface)

    snake = Snake()
    food = Food()

    myfont = pygame.font.SysFont("monospace",16)

This ‘while loop’ handles the process of looping every time the snake eats the current food or other actions as explained previously. I also need to make mention of the time scores which are rendered whenever snakes eat the current food. 

    while (True):
        clock.tick(10)
        snake.handle_keys()
        drawGrid(surface)
        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            snake.score += 1
            food.randomize_position()
        snake.draw(surface)
        food.draw(surface)

Finally, I call the display.update() function. 
        screen.blit(surface, (0,0))
        text = myfont.render("Score {0}".format(snake.score), 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

main()
