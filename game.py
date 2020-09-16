import pygame
import sys




def main():
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    clock = pygame.time.Clock()

    # Game variables
    frame_rate = 90
    speed = 2
    player_pos_x = 97
    player_pos_y = 97

    background_surface = pygame.image.load('assets/Background_1280_720.png').convert()

    walls_surface = pygame.image.load('assets/Walls_1280_720.png').convert()

    player_green_screen = pygame.image.load('assets/player_green.png')
    player_green_screen = pygame.transform.scale(player_green_screen, (60, 65))
    player_rect = player_green_screen.get_rect(center=(player_pos_x, player_pos_y))

    key_s_up = True
    key_w_up = True
    key_d_up = True
    key_a_up = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    key_s_up = False
                if event.key == pygame.K_w:
                    key_w_up = False
                if event.key == pygame.K_d:
                    key_d_up = False
                if event.key == pygame.K_a:
                    key_a_up = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_s:
                    key_s_up = True
                if event.key == pygame.K_w:
                    key_w_up = True
                if event.key == pygame.K_d:
                    key_d_up = True
                if event.key == pygame.K_a:
                    key_a_up = True

        if not key_s_up:
            player_rect.centery += speed

        if not key_w_up:
            player_rect.centery -= speed

        if not key_a_up:
            player_rect.centerx -= speed

        if not key_d_up:
            player_rect.centerx += speed

        # player_rect.centery = player_pos_y

        screen.blit(background_surface, (0, 0))
        screen.blit(walls_surface, (0, 0))
        screen.blit(player_green_screen, player_rect)

        pygame.display.update()
        clock.tick(frame_rate)


if __name__ == '__main__':
    main()
