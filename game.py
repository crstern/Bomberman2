import sys
from collisions import *
from helper import *
from variables import *


create_map(wall_map, wall_list, wall_surface, long_border_surface, short_border_surface)

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
                # go down
                key_s_up = False
            if event.key == pygame.K_w:
                # go up
                key_w_up = False
            if event.key == pygame.K_d:
                # go right
                key_d_up = False
            if event.key == pygame.K_a:
                # go left
                key_a_up = False
            if event.key == pygame.K_b:
                # drop a bomb
                pos_x = player_green_rect.centerx
                pos_y = player_green_rect.centery
                bomb_list.append(create_bomb(bomb_surface, pos_x, pos_y))


            if event.key == pygame.K_n:
                # fire that shit
                bomb_list.remove_all()


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                key_s_up = True
            if event.key == pygame.K_w:
                key_w_up = True
            if event.key == pygame.K_d:
                key_d_up = True
            if event.key == pygame.K_a:
                key_a_up = True

    collision = check_collisions(wall_list, player_green_rect)
    if collision:
        if collision_top(collision, player_green_rect):
            # print("up")
            speed_top = 0
        if collision_left(collision, player_green_rect):
            # print("left")
            speed_left = 0

        if collision_right(collision, player_green_rect):
            speed_right = 0
            # print("right")
        if collision_bottom(collision, player_green_rect):
            # print("down")
            speed_bottom = 0



    if not key_s_up:
        player_green_rect.centery += speed_bottom

    if not key_w_up:
        player_green_rect.centery -= speed_top

    if not key_a_up:
        player_green_rect.centerx -= speed_left

    if not key_d_up:
        player_green_rect.centerx += speed_right

    speed_top = speed_bottom = speed_left = speed_right = speed

    draw_map(screen, wall_list, bomb_list, wall_surface, long_border_surface, short_border_surface, bomb_surface, background_surface)

    screen.blit(player_green_screen, player_green_rect)
    screen.blit(player_red_screen, player_red_rect)

    pygame.display.update()
    clock.tick(frame_rate)