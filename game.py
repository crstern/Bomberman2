import pygame
import sys
from collisions import *

def create_wall(i, j):
    new_wall = wall_surface.get_rect(topleft=(i, j))
    return new_wall

def create_long_border(i, j):
    new_border = long_border_surface.get_rect(topleft=(i, j))
    return new_border

def create_short_border(i, j):
    new_border = short_border_surface.get_rect(topleft=(i, j))
    return new_border

def create_bomb(i, j):
    new_bomb = bomb_surface.get_rect(center=(i, j))
    return new_bomb

def create_map(wall_map):
    for i in range(len(wall_map)):
        for j in range(len(wall_map[i])):
            if wall_map[i][j] == 1:
                wall_list.append(create_wall(j * 60, i * 65))
            elif wall_map[i][j] == 2:
                wall_list.append(create_long_border(j * 60, i * 65))
            elif wall_map[i][j] == 3:
                wall_list.append(create_short_border(j * 60, i * 65))

def draw_map(screen, wall_list, bomb_list):
    screen.blit(background_surface, (0, 0))
    for wall in wall_list:
        if wall.height == 585:
            screen.blit(short_border_surface, wall)
        elif wall.width == 60:
            screen.blit(wall_surface, wall)
        elif wall.width == 1260:
            screen.blit(long_border_surface, wall)

    for bomb in bomb_list:
        screen.blit(bomb_surface, bomb)



wall_list = []
bomb_list = []

wall_map = [
        [2],
        [3, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [2]
    ]



pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

# Game variables
frame_rate = 90
speed_top = speed_bottom = speed_left = speed_right = speed = 2
player_green_pos_x = 97
player_green_pos_y = 97

player_red_pos_x = 1100
player_red_pos_y = 500

wall_surface = pygame.image.load('assets/wall.png').convert()
wall_surface = pygame.transform.scale(wall_surface, (60, 65))

long_border_surface = pygame.image.load('assets/long_border.png').convert()
long_border_surface = pygame.transform.scale(long_border_surface, (1260, 65))

short_border_surface = pygame.image.load('assets/short_border.png').convert()

player_green_screen = pygame.image.load('assets/player_green.png')
player_green_screen = pygame.transform.scale(player_green_screen, (50, 55))

player_red_screen = pygame.image.load('assets/player_red.png')
player_red_screen = pygame.transform.scale(player_red_screen, (50, 55))

bomb_surface = pygame.image.load('assets/bomb.png')
bomb_surface = pygame.transform.scale(bomb_surface, (50, 55))

background_surface = pygame.image.load('assets/Background_1280_720.png').convert()

player_green_rect = player_green_screen.get_rect(center=(player_green_pos_x, player_green_pos_y))
player_red_rect = player_red_screen.get_rect(center=(player_red_pos_x, player_red_pos_y))

create_map(wall_map)

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
            if event.key == pygame.K_b:
                pos_x = player_green_rect.centerx
                pos_y = player_green_rect.centery
                bomb_list.append(create_bomb(pos_x, pos_y))


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

    draw_map(screen, wall_list, bomb_list)

    screen.blit(player_green_screen, player_green_rect)
    screen.blit(player_red_screen, player_red_rect)

    pygame.display.update()
    clock.tick(frame_rate)


