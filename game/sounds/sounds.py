import pygame

pygame.mixer.init()

engine_sound = pygame.mixer.Sound("./../sound_effects/f1_car.mp3")
engine_sound.set_volume(0.1)

starting_sound = pygame.mixer.Sound("./../sound_effects/car_starting.wav")
starting_sound.set_volume(0.1)

countdown_sound = pygame.mixer.Sound("./../sound_effects/countdown_sound.wav")
countdown_sound.set_volume(0.1)

crash_sound = pygame.mixer.Sound("./../sound_effects/crash_sound.wav")
crash_sound.set_volume(0.1)

out_off_the_track_sound = pygame.mixer.Sound("./../sound_effects/off_track_sound.wav")
out_off_the_track_sound.set_volume(0.1)
