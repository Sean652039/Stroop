import sys
import pygame

from Settings import settings

def run1(running, screen, lasttime, inittime):
    ai_settings = settings()
    words1 = ["红色", "粉色", "黑色", "蓝色", "绿色", "褐色", "黄色", "紫色", "橙色", "灰色"]
    word_font = pygame.font.Font('/System/Library/Fonts/Supplemental/Songti.ttc', 288)

    times = {}
    times1 = {}

    # inittime = pygame.time.get_ticks()
    # lasttime = pygame.time.get_ticks()
    newtime = pygame.time.get_ticks()
    avetime = 0

    colors = []
    red =  (255, 0, 0)
    colors.append(red)
    pink = (255, 193, 193)
    colors.append(pink)
    black = (0, 0, 0)
    colors.append(black)
    blue = (0, 191, 255)
    colors.append(blue)
    green = (0, 128, 0)
    colors.append(green)
    brown = (139, 69, 19)
    colors.append(brown)
    yellow = (255, 255, 0)
    colors.append(yellow)
    purple = (128, 0, 128)
    colors.append(purple)
    orange = (255, 165, 0)
    colors.append(orange)
    gray = (128, 128, 128)
    colors.append(gray)

    num = 0
    num1 = 0
    running1 = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if(num <= 9):
                    if(event.key == pygame.K_SPACE):
                        newtime = pygame.time.get_ticks()
                        differtime = newtime - lasttime
                        times[words1[num]] = differtime
                        num += 1
        screen.fill((255, 255, 255))
        lasttime = newtime
        if num <= 9:
            word_text = word_font.render(str(words1[num]), True, colors[num-1])
            wordrect = word_text.get_rect()
            wordrect.center = (ai_settings.screen_width/2, ai_settings.screen_height/2)
            screen.blit(word_text, wordrect)
        elif num == 10:
            temptext = ""
            with open(r"Stroop\record.txt", 'w') as f:
                # for i in words1:
                #     temptext = (i + ":" + str(times[i]) + "毫秒 " + '\n')
                #     f.write(temptext)
                avetime = (newtime - inittime) / 9
                temptext = ("以背景为准的平均用时" + str(avetime) + "毫秒" + '\n')
                f.write(temptext)
                f.close()
                textshow(54, temptext, ai_settings.screen_width / 2, ai_settings.screen_height / 2, screen)
                text_again = "*按任意键继续*"
                textshow(56, text_again, ai_settings.screen_width / 2, (ai_settings.screen_height / 2 + 260), screen)
                text_fun2 = "以文字意义为准"
                textshow(56, text_fun2, ai_settings.screen_width / 2, (ai_settings.screen_height / 2 + 200), screen)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if (event.key == pygame.K_SPACE):
                            running1 = True
                            lasttime = pygame.time.get_ticks()
                            inittime = pygame.time.get_ticks()

        pygame.display.flip()



        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    lasttime = pygame.time.get_ticks()
                    if (num1 <= 9):
                        if (event.key == pygame.K_SPACE):
                            newtime = pygame.time.get_ticks()
                            differtime = newtime - lasttime
                            times1[words1[num1-3]] = differtime
                            num1 += 1
            screen.fill((255, 255, 255))
            lasttime = newtime
            if num1 <= 9:
                word_text = word_font.render(str(words1[num1-3]), True, colors[num1])
                wordrect = word_text.get_rect()
                wordrect.center = (ai_settings.screen_width / 2, ai_settings.screen_height / 2)
                screen.blit(word_text, wordrect)
            elif num1 == 10:
                temptext = ""
                with open(r"Stroop\record.txt", 'a') as f:
                    # for i in words1:
                    #     temptext = (i + ":" + str(times1[i]) + "毫秒 " + '\n')
                    #     f.write(temptext)
                    avetime = (newtime - inittime) / 9
                    temptext = ("以文字为准的的平均用时" + str(avetime) + "毫秒")
                    f.write(temptext)
                    f.close()
                    textshow(54, temptext, ai_settings.screen_width / 2, ai_settings.screen_height / 2, screen)
                    running = False
                    running1 = False
            pygame.display.flip()





def textshow(size, text, position_x, position_y, screen):
    result_font = pygame.font.Font('/System/Library/Fonts/Supplemental/Songti.ttc', size)
    result_text = result_font.render(text, True, (0, 0, 0))
    resultrect = result_text.get_rect()
    resultrect.center = (position_x, position_y)
    screen.blit(result_text, resultrect)








