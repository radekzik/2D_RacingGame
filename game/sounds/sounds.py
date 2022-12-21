import pygame

pygame.mixer.init()

engine_sound = pygame.mixer.Sound("./../sound_effects/f1_car.mp3")
engine_sound.set_volume(0.1)

starting_sound = pygame.mixer.Sound("./../sound_effects/car_starting.wav")
starting_sound.set_volume(0.05)