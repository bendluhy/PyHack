import pygame
from enum import Enum
import sys
from color import color
from termcolor import colored
from connect import NewServer
import player
import socket
port = None
username = "Benji"
server = input("Server Ip (type \"dev\") to use development server>")
if server != "dev":
    port = input("port>")
    try:
        port = int(port)
    except ValueError:
        print("Error in program port must be a whole number")
        sys.exit()
else:
    server = "127.0.0.1"
    port = 55255
GameServer = NewServer(server, port, username)


pygame.init()
display = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption('Hgame')
clock = pygame.time.Clock()
backGroundColor=pygame.Color("LIGHTBLUE")
gravityEnabled = True
#x = pygame.draw.rect(display, (255, 255, 255), pygame.Rect(40, 30, 60, 60))
user = player.Player(display, 300, 300, 50, 50, 0.2, 100)
gravity = 0.05
jumpPower = 0
doubleJumpReady = False
canJump = user.groundCheck()
# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GameServer.disconnect()
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if user.groundCheck():
                    user.y -= user.jumpspeed
                elif doubleJumpReady:
                    print("Double Jump Activated")
                    user.y -= user.jumpspeed
                    doubleJumpReady = False
            if event.key == pygame.K_q:
                GameServer.disconnect()
                pygame.quit()
                sys.exit()
    if user.groundCheck():
        doubleJumpReady = True
    keys = pygame.key.get_pressed()

    if keys[pygame.K_s] and user.y < 550:
        user.y += user.moveSpeed
    if keys[pygame.K_d] and user.x < 850:
        user.x += user.moveSpeed
    if keys[pygame.K_a] and user.x > 0:
        user.x -= user.moveSpeed


    #Main Game
    #Gravity
    canJump = user.groundCheck()
    if user.y < 550 and gravityEnabled:
        user.y += gravity
    display.fill(backGroundColor)
    user.draw()
    pygame.display.update()
