import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

engine_sound = pygame.mixer.Sound("./../sound_effects/f1_car.mp3")
engine_sound.set_volume(0.02)

starting_sound = pygame.mixer.Sound("./../sound_effects/car_starting.wav")
starting_sound.set_volume(0.02)

countdown_sound = pygame.mixer.Sound("./../sound_effects/countdown_sound.wav")
countdown_sound.set_volume(0.02)

crash_sound = pygame.mixer.Sound("./../sound_effects/crash_sound.wav")
crash_sound.set_volume(0.02)

out_off_the_track_sound = pygame.mixer.Sound("./../sound_effects/off_track_sound.wav")
out_off_the_track_sound.set_volume(0.02)

car_engine_sound = pygame.mixer.Sound("./../sound_effects/car_engine.wav")
car_engine_sound.set_volume(0.02)

car_engine_sound2 = pygame.mixer.Sound("./../sound_effects/sound.mp3")
car_engine_sound2.set_volume(0.02)
