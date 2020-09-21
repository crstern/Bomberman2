
def create_object(object_surface, i, j):
    new_object = object_surface.get_rect(topleft=(i, j))
    return new_object

def create_bomb(object_surface, i, j):
    new_object = object_surface.get_rect(center=(i, j))
    return new_object


def create_map(wall_map, wall_list, wall_surface, long_border_surface, short_border_surface):
    for i in range(len(wall_map)):
        for j in range(len(wall_map[i])):
            if wall_map[i][j] == 1:
                wall_list.append(create_object(wall_surface, j * 60, i * 65))
            elif wall_map[i][j] == 2:
                wall_list.append(create_object(long_border_surface, j * 60, i * 65))
            elif wall_map[i][j] == 3:
                wall_list.append(create_object(short_border_surface, j * 60, i * 65))

def draw_map(screen, wall_list, bomb_list, wall_surface, long_border_surface, short_border_surface, bomb_surface, background_surface):
    screen.blit(background_surface, (0, 0))
    for wall in wall_list:
        if wall.height == 585:
            screen.blit(short_border_surface, wall)
        elif wall.width == 60:
            screen.blit(wall_surface, wall)
        elif wall.width == 1260:
            screen.blit(long_border_surface, wall)

    for bomb in bomb_list.iterate():
        if bomb.val:
            screen.blit(bomb_surface, bomb.val)

