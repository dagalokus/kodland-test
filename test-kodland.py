import pygame, sys, random, math, textwrap
pygame.init()

SKY = (135,206,235)
WHITE = (255,255,255)
GRAY = (128, 143, 135)
RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (0,0,255)

holes_list=[]

            
def main():
    size = (800,500)
    screen = pygame.display.set_mode(size)

    while True:
        

        screen.fill(BLUE)
        font = pygame.font.SysFont('MS Gothic', 24)
        button_surface = pygame.Surface((150, 50))
        text = font.render("PLAY", True, BLACK)
        text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
        button_rect = pygame.Rect(125, 125, 150, 50)

        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        button_surface.blit(text, text_rect)

        screen.blit(button_surface, (button_rect.x, button_rect.y))

    
        button_surface_2 = pygame.Surface((150, 50))
        text_2 = font.render("HOW TO PLAY", True, BLACK)
        text_rect_2 = text_2.get_rect(center=(button_surface_2.get_width()/2, button_surface_2.get_height()/2))
        button_rect_2 = pygame.Rect(125, 220, 150, 50)

        if button_rect_2.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface_2, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface_2, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface_2, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_2, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface_2, (0, 100, 0), (1, 48, 148, 10), 2)

        button_surface_2.blit(text_2, text_rect_2)

        screen.blit(button_surface_2, (button_rect_2.x, button_rect_2.y))

        button_surface_3 = pygame.Surface((350, 350))
        text_3 = font.render("THE LITTLE CAR GAME", True, BLACK)
        text_rect_3 = text_3.get_rect(center=(button_surface_3.get_width()/2, button_surface_3.get_height()/2))
        button_rect_3 = pygame.Rect(350, 80, 150, 50)
        pygame.draw.rect(button_surface_3, (127, 255, 212), (1, 1, 349, 349))
        button_surface_3.blit(text_3, text_rect_3)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Call the on_mouse_button_down() function
                if button_rect.collidepoint(event.pos):
                    game()
                elif button_rect_2.collidepoint(event.pos):
                    inst()

        screen.blit(button_surface_3, (button_rect_3.x, button_rect_3.y))

        pygame.display.flip()


def inst():
    size = (800,500)
    screen = pygame.display.set_mode(size)
    while True:
        
        

        screen.fill(WHITE)

        right_click = 'To move up, use the left click on your mouse'
        pygame.display.set_caption('Instructions')
        font = pygame.font.SysFont('MS Gothic', 24)
        text = font.render(right_click,False, BLACK) 
        textRect = text.get_rect()
        textRect.center = (400, 175)
        screen.blit(text, textRect)

        left_click = 'To move down, use the right click on your mouse'
        pygame.display.set_caption('Instructions')
        font = pygame.font.SysFont('MS Gothic', 24)
        text = font.render(left_click,False, BLACK) 
        textRect = text.get_rect()
        textRect.center = (400, 275)
        screen.blit(text, textRect)
        
        button_surface = pygame.Surface((150, 50))
        text = font.render("BACK", True, BLACK)
        text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
        button_rect = pygame.Rect(0, 0, 150, 50)

        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        button_surface.blit(text, text_rect)

        screen.blit(button_surface, (button_rect.x, button_rect.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Call the on_mouse_button_down() function
                    if button_rect.collidepoint(event.pos):
                        main()
        pygame.display.flip()

def lost():
    size = (800,500)
    screen = pygame.display.set_mode(size)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(RED)

        pygame.display.set_caption('You Lost')
        font = pygame.font.SysFont('MS Gothic', 75)
        text = font.render('YOU LOST',False, WHITE) 
        textRect = text.get_rect()
        textRect.center = (400, 250)
        screen.blit(text, textRect)
        
        pygame.display.flip()

def game():
    size = (800,500)
    
    SKY = (135,206,235)
    WHITE = (255,255,255)
    GRAY = (128, 143, 135)
    HOUSES = {
        0:(187,163,138),
        1:(125,130,184),
        2:(97, 63, 117),
        3:(194, 249, 112),
        4:(214, 40, 57),
        5:(41, 231, 205),
        6:(114, 14, 7),
        7:(194, 232, 18),
    }
    screen = pygame.display.set_mode(size)
    clock = pygame.time.Clock()


    coor_y = 250

    coor_list =[]
    
    for i in range(8):
        coor_i = 105 * i
        coor_list.append(coor_i)
    speed_x = -3
    car_position = [275,300,280]
    while True:
            
        screen.fill(SKY)

        pygame.draw.rect(screen, GRAY, (0, 200, 800, 200))
        
        if random.random() < 0.012 and len(holes_list) < 10:
            holes()

        for i in range(8):
            if coor_list[i] < -30:
                coor_list[i] = 800
            else:
                coor_list[i] += speed_x
            pygame.draw.rect(screen, WHITE, (coor_list[i], 250, 30, 10))
            pygame.draw.rect(screen, WHITE, (coor_list[i], 325, 30, 10))
           
            car = ch(screen, car_position)

        font = pygame.font.SysFont('MS Gothic', 24)
        button_surface = pygame.Surface((150, 50))
        text = font.render("BACK", True, BLACK)
        text_rect = text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
        button_rect = pygame.Rect(0, 0, 150, 50)

        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)

        button_surface.blit(text, text_rect)

        screen.blit(button_surface, (button_rect.x, button_rect.y))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    # Call the on_mouse_button_down() function
                    if button_rect.collidepoint(event.pos):
                        main()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if car_position[0] > 275:
                        car_position = [275, 300, 280]
                    elif car_position[0] > 205:
                        car_position = [205,230,210]
                if event.button == 3:
                    if car_position[0] <= 205:
                        car_position = [275, 300, 280]
                    elif car_position[0] <= 275:
                        car_position = [345,370,350]
        

        print(holes_list)
        move_holes(speed_x, screen)
        loose(car_position)
        pygame.display.flip()
        clock.tick(30)  

def ch(screen, car_position):
    pygame.draw.ellipse(screen, BLACK, (100, car_position[0], 20, 10))
    pygame.draw.ellipse(screen, BLACK, (100, car_position[1], 20, 10))
    pygame.draw.ellipse(screen, BLACK, (130, car_position[0], 20, 10))
    pygame.draw.ellipse(screen, BLACK, (130, car_position[1], 20, 10))
    pygame.draw.rect(screen, RED, (100, car_position[2], 50, 25))
    return car_position
    
def holes():
    line = random.random()
    if line < 0.33:
        holes_list.append([800, 200])
    elif line < .66:
        holes_list.append([800, 280])
    else:
        holes_list.append([800, 350])
    
def move_holes(speed_x, screen):
    for idx, hole in enumerate(holes_list):
        if hole[0] < 0:
            holes_list.remove(hole)
        else:
            holes_list[idx] = (hole[0]+speed_x, hole[1])
            pygame.draw.ellipse(screen, BLACK, (hole[0], hole[1], 30, 50))

def loose(car_position):
    for hole in holes_list:
        dist = math.hypot(hole[0]-152, hole[1]-car_position[2])
        if dist < 5:
            lost()

    

main()
