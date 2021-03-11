import pygame


pygame.init()
font = pygame.font.Font('freesansbold.ttf', 15)
screen = pygame.display.set_mode((440, 440), pygame.NOFRAME)
x = 250
y = 250
r = 5
run = True
pygame.event.set_grab(True)

while run:
    pygame.display.set_caption("ReadPos") #Navn på vindue
    mousex, mousey = pygame.mouse.get_pos()
    pygame.time.delay(10) # 10 ticks pause
    pygame.mouse.set_visible(False) #Kan se mus i pygame window
    screen.fill((0, 0, 0)) #Gør skærm sort
    pygame.draw.line(screen, (0, 255, 0), (mousex, 0), (mousex, 500), 1) #tegner grøn linje
    pygame.draw.line(screen, (0, 0, 255), (0, mousey), (700, mousey), 1) #tegner blå linje 
    pygame.draw.circle(screen, (255, 0 ,0), (mousex, mousey), r) #Tegner Cirkel ved mus
    text = font.render("x= " + str(mousex) + " y= " + str(mousey), True, (255, 255, 255), (0, 0, 0)) #Tekst med kordinator
    textRect = text.get_rect() 
    textRect.center = (50, 10) #midten af tekst
    screen.blit(text, textRect) #viser skærm
    pygame.display.update() #Opdaterer skærm
    print("x= " + str(mousex), "y= " + str(mousey)) #sender kordinator



    for event in pygame.event.get(): #Finder ud af hvad der sker med pygame window
        if event.type == pygame.QUIT: #Hvis det røde kryds trykkes lukkes programmet
            run = False #Gør run False/Falsk
            print("The program was closed...")
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                print("ESC was pressed. quitting...")
                run = False



quit()