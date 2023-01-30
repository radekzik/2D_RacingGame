import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


class Sounds:

    starting_sound = pygame.mixer.Sound("./../sound_effects/car_starting.wav")
    starting_sound.set_volume(0.02)

    countdown_sound = pygame.mixer.Sound("./../sound_effects/countdown_sound.wav")
    countdown_sound.set_volume(0.02)

    crash_sound = pygame.mixer.Sound("./../sound_effects/crash_sound.wav")
    crash_sound.set_volume(0.02)

    out_off_the_track_sound = pygame.mixer.Sound("./../sound_effects/off_track_sound.wav")
    out_off_the_track_sound.set_volume(0.02)

    car_engine = pygame.mixer.Sound("./../sound_effects/car-acceleration.wav")
    car_engine.set_volume(0.1)

    car_turbo = pygame.mixer.Sound("./../sound_effects/turbo_sound.wav")
    car_turbo.set_volume(0.02)

    finish = pygame.mixer.Sound("./../sound_effects/finish_sound.wav")
    finish.set_volume(0.02)

    win = pygame.mixer.Sound("./../sound_effects/win_sound.wav")
    win.set_volume(0.02)

    lose = pygame.mixer.Sound("./../sound_effects/lose_sound.wav")
    lose.set_volume(0.02)
