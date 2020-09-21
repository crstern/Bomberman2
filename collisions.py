collision_tollerance = 10

def check_collisions(walls, player):
    collisions = []
    for wall in walls:
        if wall.colliderect(player):
            collisions.append(wall)
    return collisions

def collision_top(collisions, player):
    for wall in collisions:
        if abs(wall.bottom - player.top) < collision_tollerance + 10:
            # print("top")
            return True
    return False

def collision_left(collisions, player):
    for wall in collisions:
        if abs(wall.right - player.left) < collision_tollerance:
            # print("left")
            return True
    return False

def collision_right(collisions, player):
    for wall in collisions:
        if abs(wall.left - player.right) < collision_tollerance:
            # print("right")
            return True
    return False

def collision_bottom(collisions, player):
    for wall in collisions:
        if abs(wall.top - player.bottom) < collision_tollerance + 10:
            # print("bottom")
            return True
    return False