import pygame
import os
import time
import threading 
import webbrowser



from pygame.locals import *


SCREEN_HEIGHT = 250
SCREEN_WIDTH = 400

x = 880
y = 505

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Get to Work")



clock = pygame.time.Clock()
fps = 24

class Video(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 40):
            img = pygame.image.load(f"Working/{num}.png")
            img = pygame.transform.scale(img, (400, 250))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.counter = 0

    def update(self):
        explosion_speed = 1

        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.index = 0
            self.image = self.images[self.index]

Video_group = pygame.sprite.Group()
video = Video()
Video_group.add(video)

class VideoSW(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        for num in range(1, 90):
            img = pygame.image.load(f"StartWorking/{num}.png")
            img = pygame.transform.scale(img, (400, 250))
            self.images.append(img)
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.counter = 0

    def update(self):
        explosion_speed = 1

        self.counter += 1

        if self.counter >= explosion_speed and self.index < len(self.images) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]

        if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
            self.index = 0
            self.image = self.images[self.index]

VideoSW_group = pygame.sprite.Group()
VideoSW = VideoSW()
VideoSW_group.add(VideoSW)

class Button():
    def __init__(self, group, screen):
        self.group = group
        self.screen = screen
        self.mouse_pressed = False
        self.background_thread = threading.Thread(target=self.background_task)
        self.background_thread.daemon = True
        self.background_thread.start()

    def draw(self):
        pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0] == 1:
            if not self.mouse_pressed:
                self.handle_click()  
                self.mouse_pressed = True
        else:
            self.mouse_pressed = False

        self.group.draw(self.screen)
        self.group.update()

    def handle_click(self):

        if self.group == VideoSW_group:
            self.group = Video_group
            webbrowser.open_new("https://brookdalecc.instructure.com/")
        else:
            self.group = VideoSW_group

    def background_task(self):
        while True:
            if self.group == Video_group:
                os.system("taskkill /f /im Discord.exe")
                os.system("taskkill /f /im steam.exe")
                time.sleep(10)

            else:
                None


current_button = Button(VideoSW_group, screen)



run = True
while run:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
            
    current_button.draw()

    pygame.display.update()

pygame.quit()
