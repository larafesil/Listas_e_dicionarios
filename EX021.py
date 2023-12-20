import pygame
pygame.init()
pygame.mixer_music.load('ex21.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()