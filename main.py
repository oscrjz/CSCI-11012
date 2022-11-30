import pygame

pygame.init()

#Game settings. 
monitor_display = (800, 600)

game_display = pygame.display.set_mode(monitor_display)

pygame.display.set_caption("Tank Domination")

system_clock = pygame.time.Clock()

game_characteristics = {
    "sky":{
        "color": (135, 206, 235)
    }, 
    "grass":{
        "color": (0,255,0),
        "position": {
            "y": 0.8 * monitor_display[1]
        }
    }
}

game_running_flag = True 

while game_running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            game_running_flag = False

    if not game_running_flag: 
        pygame.quit()

        break 

    # Running the game. 
    game_display.fill(game_characteristics["sky"]["color"])

    # Create grass.
    pygame.draw.rect(game_display, game_characteristics["grass"]["color"], pygame.Rect(0, game_characteristics["grass"]["position"]["y"], monitor_display[0], monitor_display[1] - game_characteristics["grass"]["position"]["y"]))

    pygame.display.update()

    system_clock.tick(30)