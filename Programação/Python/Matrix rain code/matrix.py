from cgitb import text
from sre_parse import WHITESPACE
from time import clock_getres
import pygame
from pygame.locals import *
from sys import exit

pygame.init()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

FPS = 15

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

LETTERS = ["a",
  "b",
  "c",
  "d",
  "e",
  "f",
  "g",
  "h",
  "i",
  "j",
  "k",
  "l",
  "m",
  "n",
  "o",
  "p",
  "q",
  "r",
  "s",
  "t",
  "u",
  "v",
  "w",
  "x",
  "y",
  "z",
  "1",
  "2",
  "3",
  "4",
  "5",
  "6",
  "7",
  "8",
  "А",
  "В",
  "Г",
  "Д",
  "Є",
  "Ѕ",
  "З",
  "И",
  "Ѳ",
  "І",
  "К",
  "Л",
  "М",
  "Н",
  "Ѯ",
  "Ѻ",
  "П",
  "Ч",
  "Р",
  "С",
  "Т",
  "Ѵ",
  "Ф",
  "Х",
  "Ѱ",
  "Ѿ",
  "Ц",]
screen = pygame.display.set_mode((SCREEN_WIDTH,
SCREEN_HEIGHT))
pygame.display.set_caption('Matrix Animation')

font = pygame.font.sysFont('arial', 15 , True , True)
message = 'hello world'
text = font.render(message , True , GREEN)

clock = pygame.time.Clock()

while True:
    clock.tick(FPS)
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    screen.blit(text,(SCREEN_WIDTH/2 ,SCREEN_HEIGHT/2))
    pygame.display.update()