import pygame

def run():

    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Color-Theories")

    #Clock Speed
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)
                print("Mouse clicked")

            elif event.type == pygame.MOUSEBUTTONUP:
                print(event.pos)
                print("Mouse UNclicked")

            elif event.type == pygame.DROPBEGIN:
                print(event)
                print("File drop begin!")
            
            elif event.type == pygame.DROPCOMPLETE:
                print(event)
                print("File drop complete!")

        #Display objects on screen
        screen.fill((0, 0, 0))
        pygame.display.update()
        clock.tick(30)