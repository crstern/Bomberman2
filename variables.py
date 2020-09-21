from linkedList import *
import pygame

wall_list = []
bomb_list = LinkedList(Node('bomb_head'))

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