import pygame

pygame.mixer.init()

engine_sound = pygame.mixer.Sound("f1_car.mp3")
engine_sound.set_volume(0.1)

starting_sound = pygame.mixer.Sound("car_starting.wav")
starting_sound.set_volume(0.05)

