import pygame
import pygame as pg

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
    step = 1
    choise = None

def start():
    px.step = px.step + 1

def VariantA():
        px.choise = 0
        px.step = px.step + 1
def VariantB():
        px.choise = 1
        px.step = px.step + 1
def VariantC():
        px.choise = 2
        px.step = px.step + 1

def render(screen, text, position, font_size):
    font = pygame.font.SysFont("Sans", font_size)
    text_render = font.render(text, 1, (255, 255, 255))
    x, y = position
    return screen.blit(text_render, (x, y))


def main():
    def button(screen, position, text, font_size, isel = True):
        font = pygame.font.SysFont("Sans", font_size)
        text_render = font.render(text, 1, (32, 32, 32))
        x, y, w , h = text_render.get_rect()
        if isel:
        	x, y = position
        else:
        	x = infoObject.current_w / 2 - w / 2
        	y = position[1]
        pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
        pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        pygame.draw.rect(screen, (190, 190, 200), (x, y, w , h))
        return screen.blit(text_render, (x, y))
    infoObject = pygame.display.Info()
    screen = pygame.display.set_mode((infoObject.current_w, infoObject.current_h)) 
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(infoObject.current_w - 890, 175, infoObject.current_w - 200, 38)
    color_inactive = pygame.Color(48, 200, 120)
    color_active = pygame.Color(45, 242, 13)
    color = color_inactive
    active = False
    text = ''
    done = False
    font = pygame.font.SysFont('Arial', 24)
    
    
    while not done:
        if px.step == 1:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_ESCAPE:
                                done = True
                        img1 = font.render('Расчёт данных', True, (255, 255, 255))
                        txt_surface = font.render(text, True, color)
                        screen.fill((50, 105, 0))  
                        screen.blit(img1, (infoObject.current_w - 870, 10))
                        b = button(screen, (infoObject.current_w - 870, 300), " Start ", 70)
                        bexit = button (screen, (infoObject.current_w - 60, 10), " X ", 50)
                        if event.type == pg.MOUSEBUTTONDOWN:
                            if bexit.collidepoint(event.pos):
                                done = True
                            if b.collidepoint(event.pos):
                                start()
                pygame.display.flip()


        elif px.step == 2:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        done = True
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
                                    px.px3 = text
                                    print(px.px3)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 4:
                                    px.px4 = text
                                    print(px.px4)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 5:
                                    px.px5 = text
                                    print(px.px5)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 6:
                                    px.px6 = text
                                    print(px.px6)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 7:
                                    px.px7 = text
                                    print(px.px7)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 8:
                                    px.px8 = text
                                    print(px.px8)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 9:
                                    px.px9 = text
                                    print(px.px9)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 10:
                                    px.px10 = text
                                    print(px.px10)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 11:
                                    px.px11 = text
                                    print(px.px11)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 12:
                                    px.px12 = text
                                    print(px.px12)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 13:
                                    px.px13 = text
                                    print(px.px13)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 14:
                                    px.px14 = text
                                    print(px.px14)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 15:
                                    px.px15 = text
                                    print(px.px15)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 16:
                                    px.px16 = text
                                    print(px.px16)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 17:
                                    px.px17 = text
                                    print(px.px17)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 18:
                                    px.px18 = text
                                    print(px.px18)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 19:
                                    px.px19 = text
                                    print(px.px19)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 20:
                                    px.px20 = text
                                    print(px.px20)
                                    text = ''
                                    px.loop = px.loop + 1
                            elif px.loop == 21:
                                    px.px21 = text
                                    print(px.px21)
                                    text = ''
                                    px.loop = px.loop + 1
                            else:
                                print("Error")
                        
                        elif event.key == pg.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode
                screen.fill((50, 105, 0))  
                txt_surface = font.render(text, True, color)
                width = max(200, txt_surface.get_width()+10)
                input_box.w = width
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                pg.draw.rect(screen, color, input_box, 2)
                if px.loop < 22:
                        img = font.render('Введите значение PX' + str(px.loop), True, (255, 255, 255))
                        screen.blit(img, (infoObject.current_w - 890, 100))
                        if px.loop == 1:
                            render(screen, "Физико-химические и механические свойства изоляции", (100,300), 40)
                        elif px.loop == 2:
                            render(screen, "Электрические параметры изоляции", (100,300), 40)
                        elif px.loop == 3:
                            render(screen, "Электрические параметры радиоэлектронных и микропроцессорных устройств", (100,300), 40)
                        elif px.loop == 4:
                            render(screen, "Физико-химические свойства полимерной изоляции оболочки кабелей и проводов", (100,300), 40)
                        elif px.loop == 5:
                            render(screen, "Электрические параметры кабелей и проводов", (100,300), 40)
                        elif px.loop == 6:
                            render(screen, "Состояние обмоток электрических машин и трансформаторов", (100,300), 40)
                        elif px.loop == 7:
                            render(screen, "Показатели качества трансформаторного масла", (100,300), 40)
                        elif px.loop == 8:
                            render(screen, "Толщина стенки бака маслянного трансформатора", (100,300), 40)
                        elif px.loop == 9:
                            render(screen, "Количество циклов включения-выключения аппарата вторичных цепей", (100,300), 40)
                        elif px.loop == 10:
                            render(screen, "Сопротивление контактных соединений аппаратуры управления", (100,300), 40)
                        elif px.loop == 11:
                            render(screen, "Рабочие характеристики и долговечность стационарных свиницово-кислотных аккумуляторных батарей", (100,300), 40)
                        elif px.loop == 12:
                            render(screen, "Состав электролита аккумуляторных батарей", (100,300), 40)
                        elif px.loop == 13:
                            render(screen, "Воздушные зазоры между статером и ротером электрических машин", (100,300), 40)
                        elif px.loop == 14:
                            render(screen, "Зазоры и величина вибрации в подшипниках скольжения электродвигателя", (100,300), 40)
                        elif px.loop == 15:
                            render(screen, "Прочность и вибростойкость оборудования", (100,300), 40)
                        elif px.loop == 16:
                            render(screen, "Время и разновременность замыкания и размыкания главных контактов выключателей", (100,300), 40)
                        elif px.loop == 17:
                            render(screen, "Сопротивление постоянному току трубчатых электронагревателей", (100,300), 40)
                        elif px.loop == 18:
                            render(screen, "Срок службы", (100,300), 40)
                        elif px.loop == 19:
                            render(screen, "Наработка", (100,300), 40)
                        elif px.loop == 20:
                            render(screen, "Характеристики чехла привода СУЗ - ШЭМ", (100,300), 40)
                        elif px.loop == 21:
                            render(screen, "Электрические характеристики датчиков положения привода СУЗ - ШЭМ", (100,300), 40)
                        else:
                            print("Error")
                elif px.loop == 22:
                        screen.fill((50, 105, 0))
                        img = font.render('Выберите вариант расчётов', True, (255, 255, 255))
                        screen.blit(img, (infoObject.current_w - 900, 10))
                        px.step = px.step + 1
                else:
                        print("Error")
                bexit = button (screen, (infoObject.current_w - 60, 10), " X ", 50)
                if event.type == pg.MOUSEBUTTONDOWN:
                        if bexit.collidepoint(event.pos):
                                done = True

        
        elif px.step == 3:
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                done = True
                        b1 = button(screen, (infoObject.current_w - 870, 100), "Вариант А", 50, False)
                        b2 = button(screen, (infoObject.current_w - 870, 200), "Вариант Б", 50, False)
                        b3 = button(screen, (infoObject.current_w - 870, 300), "Вариант В", 50, False)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                                if b1.collidepoint(event.pos):
                                                VariantA()
                                elif b2.collidepoint(event.pos):
                                                VariantB()
                                elif b3.collidepoint(event.pos):
                                                VariantC()
                                else:
                                        print("Error")
                        bexit = button (screen, (infoObject.current_w - 60, 10), " X ", 50)
                        if event.type == pg.MOUSEBUTTONDOWN:
                                if bexit.collidepoint(event.pos):
                                        done = True
                pygame.display.flip()
        
        
        elif px.step == 4:
                done = True



        else:
            print("Error")

        pg.display.update()
        clock.tick(30)


if __name__ == '__main__':
    pygame.init()
    main()
    pygame.quit()
subprocess.call(str(path.join(path.dirname(__file__), filename)))
