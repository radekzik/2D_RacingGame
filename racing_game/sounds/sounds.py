import pygame

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()


class Sounds:

    # CAR SOUNDS -------------------------------------------------------------------------------------------------------

    car_starting = pygame.mixer.Sound("./sound_effects/car_starting.wav")
    car_starting.set_volume(0.02)

    car_engine = pygame.mixer.Sound("./sound_effects/car_engine.wav")
    car_engine.set_volume(0.02)

    nitro = pygame.mixer.Sound("./sound_effects/nitro.wav")
    nitro.set_volume(0.02)

    # COLLISION SOUNDS -------------------------------------------------------------------------------------------------

    crash = pygame.mixer.Sound("./sound_effects/crash.wav")
    crash.set_volume(0.02)

    out_off_track = pygame.mixer.Sound("./sound_effects/out_off_track.wav")
    out_off_track.set_volume(0.02)

    # GAME EVENT SOUNDS -----------------------------------------------------------------------------------------------

    countdown = pygame.mixer.Sound("./sound_effects/countdown.wav")
    countdown.set_volume(0.02)

    finish = pygame.mixer.Sound("./sound_effects/finish.wav")
    finish.set_volume(0.02)

    win = pygame.mixer.Sound("./sound_effects/win.wav")
    win.set_volume(0.02)

    lose = pygame.mixer.Sound("./sound_effects/lose.wav")
    lose.set_volume(0.02)
