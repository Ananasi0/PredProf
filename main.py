import pygame as pg
import pygame

class px():
    px1 = 0
    px2 = 0
    px3 = 0
    px4 = 0
    px5 = 0
    px6 = 0
    px7 = 0
    px8 = 0
    px9 = 0
    px10 = 0
    px11 = 0
    px12 = 0
    px13 = 0
    px14 = 0
    px15 = 0
    px15 = 0
    px16 = 0
    px17 = 0
    px18 = 0
    px19 = 0
    px20 = 0
    px21 = 0
    loop = 1
    step = 2
    
def main():
    screen = pg.display.set_mode((500, 500))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(150, 60, 150, 38)
    color_inactive = pg.Color(48, 200, 120)
    color_active = pg.Color(45, 242, 13)
    color = color_inactive
    active = False
    text = ''
    done = False
    font = pygame.font.SysFont('Arial', 24)
    
    
    while not done:
        if px.step == 2:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    # If the user clicked on the input_box rect.
                    if input_box.collidepoint(event.pos):
                        # Toggle the active variable.
                        active = not active
                    else:
                        active = False
                    # Change the current color of the input box.
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if active:
                        if event.key == pg.K_RETURN:
                            if px.loop == 1:
                                    px.px1 = text
                                    print(px.px1)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 2:
                                    px.px2 = text
                                    print(px.px2)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 3:
                                    px.px2 = text
                                    print(px.px3)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 4:
                                    px.px2 = text
                                    print(px.px4)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 5:
                                    px.px2 = text
                                    print(px.px5)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 6:
                                    px.px2 = text
                                    print(px.px6)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 7:
                                    px.px2 = text
                                    print(px.px7)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 8:
                                    px.px2 = text
                                    print(px.px8)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 9:
                                    px.px2 = text
                                    print(px.px9)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 10:
                                    px.px2 = text
                                    print(px.px10)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 11:
                                    px.px2 = text
                                    print(px.px11)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 12:
                                    px.px2 = text
                                    print(px.px12)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 13:
                                    px.px2 = text
                                    print(px.px13)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 14:
                                    px.px2 = text
                                    print(px.px14)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 15:
                                    px.px2 = text
                                    print(px.px15)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 16:
                                    px.px2 = text
                                    print(px.px16)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 17:
                                    px.px2 = text
                                    print(px.px17)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 18:
                                    px.px2 = text
                                    print(px.px18)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 19:
                                    px.px2 = text
                                    print(px.px19)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 20:
                                    px.px2 = text
                                    print(px.px20)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 21:
                                    px.px2 = text
                                    print(px.px21)
                                    text = ''
                                    px.loop = px.loop + 1
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

        
            screen.fill((3, 187, 231))  
            txt_surface = font.render(text, True, color)
            
            
            if px.loop < 22:
                img = font.render('Введите значение PX' + str(px.loop), True, (10, 100, 150))
            elif px.loop > 21:
                img = font.render('Выберите вариант расчётов', True, (10, 100, 150))
            screen.blit(img, (145, 10))
            # Resize the box if the text is too long.
            width = max(200, txt_surface.get_width()+10)
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            # Blit the input_box rect.
            pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
