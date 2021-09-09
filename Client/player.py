import pygame


class Player:
    def __init__(self, display, x, y, width, height, moveSpeed, jumpSpeed):
        self.display = display
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.moveSpeed = moveSpeed
        self.jumpspeed = jumpSpeed

    def draw(self):
        pygame.draw.rect(self.display, (255, 140, 0), (self.x, self.y, self.width, self.height))
    def groundCheck(self):
        if self.display.get_height() - self.height == round(self.y):
            return True
        else:
            return False
