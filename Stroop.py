import pygame
import sys


from Settings import settings
import Fuctions as fuc


def run_exper():
    pygame.init()
    ai_settings = settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Stroop Test")

    running = False
    begin = False

    screen.fill((255, 255, 255))
    text_caption = "STROOP TEST"
    fuc.textshow(96, text_caption, ai_settings.screen_width / 2, (ai_settings.screen_height / 2 - 260), screen)

    text_begin = "*按任意键开始*  "
    fuc.textshow(56, text_begin, ai_settings.screen_width / 2, (ai_settings.screen_height / 2 + 260), screen)

    text_fun1 = "以文字背景颜色为准"
    fuc.textshow(56, text_fun1, ai_settings.screen_width / 2, (ai_settings.screen_height / 2 + 200), screen)

    pygame.display.flip()

    while not begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                running = True
                begin = True
                lasttime = pygame.time.get_ticks()
                inittime = pygame.time.get_ticks()

                fuc.run1(running, screen, lasttime, inittime)







run_exper()





