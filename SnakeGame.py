# from user304_rsf8mD0BOQ_1 import Vector
from vector import Vector
import random,math

try:
    import simplegui
except ImportError:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui

CANVAS_HEIGHT = 800
CANVAS_WIDTH = 800

CELL_NUM = 20
CELL_SIZE = CANVAS_HEIGHT/CELL_NUM
CELL_CENTRE = (CELL_SIZE/2,CELL_SIZE/2)
count = 0
#Class Border:


#Class Food:
class Food:
    def __init__(self, url):
        self.food_img = simplegui.load_image(url)
        self.food_dims = (self.food_img.get_width(), self.food_img.get_height())
        self.food_img_centre = (self.food_dims[0]/2, self.food_dims[1]/2)
        self.x = 0
        self.y = 0
        
        

    def draw_apple(self,canvas):
        global count
        if count % 120 == 0 :
            self.x = random.randint(0,CELL_NUM-1)
            self.y = random.randint(0,CELL_NUM-1)
        apple_dims  = (self.food_dims[0]/5, self.food_dims[1]/6)
        apple_centre = (apple_dims[0]/2, apple_dims[1]/2)
        canvas.draw_image(self.food_img, apple_centre, apple_dims, (CELL_CENTRE[0] + self.x*CELL_SIZE,CELL_CENTRE[1] + self.y*CELL_SIZE),(CELL_SIZE,CELL_SIZE))
        count += 1

    def draw_carrot(self,canvas):
        apple_dims  = (self.food_dims[0]/5, self.food_dims[1]/6)
        apple_centre = ((apple_dims[0]/2)+apple_dims[0], (apple_dims[1]/2) + apple_dims[1])
        
        canvas.draw_image(self.food_img, apple_centre, apple_dims, (CANVAS_WIDTH/3,CANVAS_HEIGHT/3),(CELL_SIZE,CELL_SIZE))

#Class Obstacle
class Obstacle:
    def __init__(self, url,column):
        self.x = random.randint(0,CELL_NUM-1)
        self.y = random.randint(0,CELL_NUM-1)
        self.row = 1
        self.column = column
        self.obs_img = simplegui.load_image(url)
        self.width = self.obs_img.get_width()
        self.height = self.obs_img.get_height()
        self.dims_of_frame = (self.width/self.column, self.height/self.row)
        self.centre = (self.dims_of_frame[0]/2, self.dims_of_frame[1]/2)

    def draw(self, canvas):
        canvas.draw_circle((CELL_CENTRE[0] + self.x*CELL_SIZE,CELL_CENTRE[1] + self.y*CELL_SIZE), CELL_SIZE + CELL_SIZE/2, 1, 'red')
        canvas.draw_image(self.obs_img,self.centre, self.dims_of_frame,(CELL_CENTRE[0] + self.x*CELL_SIZE,CELL_CENTRE[1] + self.y*CELL_SIZE), (CELL_SIZE,CELL_SIZE))


    def next_frame(self):
        if (self.centre[0] + self.dims_of_frame[0] < self.width):
            self.centre = (self.centre[0]+self.dims_of_frame[0], self.centre[1])
        else:
            if (self.centre[1] + self.dims_of_frame[1] > self.height):
                self.centre = (self.dims_of_frame[0]/2, self.dims_of_frame[1]/2)
            else:
                self.centre = (self.dims_of_frame[0]/2,self.centre[1]+self.dims_of_frame[1])

#Grid Map
class Map:
    def __init__(self):
        self.x = 0

    def draw(self,canvas):
        i = 0
        while(i <= CELL_NUM):
            canvas.draw_line((i*CELL_SIZE, 0), (i*CELL_SIZE, CANVAS_HEIGHT), 1, 'white')
            canvas.draw_line((0,i*CELL_SIZE), (CANVAS_WIDTH,i*CELL_SIZE), 1, 'white')
            i += 1
            

# class Clock to test sprite sheet
class Clock:
    def __init__(self, spritesheet):
        self.time = 0
        self.spritesheet = spritesheet

    def tick(self, canvas):
        self.time += 1
        if self.transition(self.time):
            self.spritesheet.next_frame()
            self.spritesheet.draw(canvas)
        else:
            self.spritesheet.draw(canvas)    


    def transition(self, frame_duration):
        if frame_duration % 2:
            return True
        return False

     
#class Snake:
    
class Keyboard:
    def __init__(self):
        self.arrow_right = False
        self.arrow_left = False
        self.arrow_up = False
        self.arrow_down = False
        
    def KeyDown(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.arrow_right = True
        if key == simplegui.KEY_MAP['left']:
            self.arrow_left = True
        if key == simplegui.KEY_MAP['up']:
            self.arrow_up == True
        if key == simplegui.KEY_MAP['down']:
            self.arrow_down == True
            
    def KeyUp(self, key):
        if key == simplegui.KEY_MAP['right']:
            self.arrow_right = False
        if key == simplegui.KEY_MAP['left']:
            self.arrow_left = False
        if key == simplegui.KEY_MAP['up']:
            self.arrow_up = False
        if key == simplegui.KEY_MAP['down']:
            self.arrow_down = False
                        

#class Interaction:
        
# creat clock and spritesheet
obs_url = 'https://www.cs.rhul.ac.uk/home/wkis088/NewCampFire.png'
obs = Obstacle(obs_url,5)
clock = Clock(obs)

# create a food obj
food_url = 'https://www.cs.rhul.ac.uk/home/wkis088/food-thekingphoenix.png'
food = Food(food_url)

# load the background
background = simplegui.load_image('https://www.cs.rhul.ac.uk/home/wkis088/grass.png')
background_dims = (background.get_width(), background.get_height())
print(background_dims)
background_centre = (background_dims[0]/2, background_dims[1]/2)

m = Map()

# draw handler
def draw_handler(canvas):
    # canvas.draw_image(background, background_centre, background_dims, (CANVAS_WIDTH/2,CANVAS_HEIGHT/2),(CANVAS_WIDTH,CANVAS_HEIGHT))
    m.draw(canvas)
    food.draw_apple(canvas)
    clock.tick(canvas)
    










frame = simplegui.create_frame("SnAkE",CANVAS_WIDTH,CANVAS_HEIGHT )
frame.set_draw_handler(draw_handler)
frame.start()