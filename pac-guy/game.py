# Margaret Laflam (ewg2bd), Jamie Tran (pby5br)

# DESCRIPTION OF GAME
# NEW FEATURES/GAME CONCEPT - all features are new as first idea was rejected
# This game is an imitation of the popular arcade game Pac-Man
# Three Basic Features:
# User input - user moves pac man around the map
# Game over - after dying/running into to the enemies three times the player loses the game and a game over screen is displayed
# Graphics/Images - Images are used to display player lives
# Four Additional Features:
# Restart from game over - if player dies three times or wins by collecting all coins they will have the option to restart the game
# Sprite Animation - player (Pac-man) animated based on movement
# Enemies - four enemies (ink, blink, pink, clyde) will wander around the map to hinder bit collection
# Collectables - bits/coins are displayed throughout the map. If the player collects all the coins they win the game
# Health bar - the player has 3 lives and when all three are used the game will end


import uvage
import random

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


def setup():
    '''
    set up for the game including camera, basic booleans for controls and counters, character creation and game building
    '''
    global camera, player, walls, game_on, game_over, game_win, game_ends, count, score_display, score, bits, walls, ink, pink, blink, title
    global up_movement, down_movement, left_movement, right_movement, enemies, gate, lives, lives_display, choice, randx, randy, clyde

    camera = uvage.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

    # start controls & counters
    game_on = False
    game_over = False
    game_win = False
    game_ends = False
    count = 0
    score = 0
    lives = 3
    choice = False
    left_movement = False
    right_movement = False
    down_movement = False
    up_movement = False
    randx = random.randint(1, 2)
    randy = random.randint(1, 2)

    # title
    title = uvage.from_image(400, 40, "logo.png")

    # player
    player = uvage.from_image(10, 100, "pacman1.png") # pac-guy the main character

    # enemies
    ink = uvage.from_image(440, 350, "inklr.png")
    blink = uvage.from_image(400, 350, "blinklr.png")
    pink = uvage.from_image(360, 350, "pinklr.png")
    clyde = uvage.from_image(50, 570, "clyde.png")
    enemies = [ink, blink, pink, clyde]

    # images of lives
    lives_display = [

        uvage.from_image(680, 33, "life.png"),
        uvage.from_image(720, 33, "life.png"),
        uvage.from_image(760, 33, "life.png")
    ]


    # bits - collectible items that pac-guy eats
    bits = [
        # coins top max score == 11000
        uvage.from_image(120, 100, "bit.png"),
        uvage.from_image(170, 100, "bit.png"),
        uvage.from_image(220, 100, "bit.png"),
        uvage.from_image(270, 100, "bit.png"),
        uvage.from_image(320, 100, "bit.png"),
        uvage.from_image(370, 100, "bit.png"),
        uvage.from_image(420, 100, "bit.png"),
        uvage.from_image(470, 100, "bit.png"),
        uvage.from_image(530, 100, "bit.png"),  # off
        uvage.from_image(570, 100, "bit.png"),
        uvage.from_image(620, 100, "bit.png"),
        uvage.from_image(670, 100, "bit.png"),
        uvage.from_image(720, 100, "bit.png"),
        uvage.from_image(760, 100, "bit.png"),

        uvage.from_image(70, 575, "bit.png"),  # coins bottom
        uvage.from_image(120, 575, "bit.png"),
        uvage.from_image(170, 575, "bit.png"),
        uvage.from_image(220, 575, "bit.png"),
        uvage.from_image(270, 575, "bit.png"),
        uvage.from_image(320, 575, "bit.png"),
        uvage.from_image(370, 575, "bit.png"),
        uvage.from_image(420, 575, "bit.png"),
        uvage.from_image(470, 575, "bit.png"),
        uvage.from_image(530, 575, "bit.png"),  # off
        uvage.from_image(570, 575, "bit.png"),
        uvage.from_image(620, 575, "bit.png"),
        uvage.from_image(670, 575, "bit.png"),
        uvage.from_image(720, 575, "bit.png"),
        uvage.from_image(760, 575, "bit.png"),

        uvage.from_image(35, 125, "bit.png"),  # coins right below top
        uvage.from_image(760, 125, "bit.png"),
        uvage.from_image(70, 150, "bit.png"),  # coins second top
        uvage.from_image(120, 150, "bit.png"),
        uvage.from_image(170, 150, "bit.png"),
        uvage.from_image(220, 150, "bit.png"),
        uvage.from_image(270, 150, "bit.png"),

        uvage.from_image(530, 150, "bit.png"),  # coins second top
        uvage.from_image(580, 150, "bit.png"),
        uvage.from_image(630, 150, "bit.png"),
        uvage.from_image(680, 150, "bit.png"),
        uvage.from_image(730, 150, "bit.png"),
        uvage.from_image(760, 150, "bit.png"),

        # coins column left, rows columns right
        uvage.from_image(155, 190, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 190, "bit.png"),
        uvage.from_image(155, 240, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 240, "bit.png"),
        uvage.from_image(155, 290, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 290, "bit.png"),
        uvage.from_image(155, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 340, "bit.png"),
        uvage.from_image(155, 390, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 390, "bit.png"),
        uvage.from_image(155, 440, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 440, "bit.png"),
        uvage.from_image(155, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 480, "bit.png"),
        uvage.from_image(270, 190, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 190, "bit.png"),
        uvage.from_image(270, 290, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 290, "bit.png"),
        uvage.from_image(270, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 340, "bit.png"),
        uvage.from_image(270, 390, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 390, "bit.png"),
        uvage.from_image(270, 440, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 440, "bit.png"),
        uvage.from_image(270, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 480, "bit.png"),
        uvage.from_image(37, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 37, 480, "bit.png"),

        # bottom vert
        uvage.from_image(37, 530, "bit.png"), uvage.from_image(SCREEN_WIDTH - 37, 530, "bit.png"),
        uvage.from_image(37, 575, "bit.png"),
        uvage.from_image(82, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 82, 480, "bit.png"),

        # second to bottom row horiz
        uvage.from_image(115, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 115, 480, "bit.png"),
        uvage.from_image(195, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 195, 480, "bit.png"),
        uvage.from_image(235, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 235, 480, "bit.png"),
        uvage.from_image(315, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 315, 480, "bit.png"),
        uvage.from_image(345, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 480, "bit.png"),
        uvage.from_image(350, 510, "bit.png"), uvage.from_image(SCREEN_WIDTH - 350, 510, "bit.png"),
        uvage.from_image(350, 540, "bit.png"), uvage.from_image(SCREEN_WIDTH - 350, 540, "bit.png"),
        uvage.from_image(345, 200, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 200, "bit.png"),

        # middle top vert
        uvage.from_image(345, 240, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 240, "bit.png"),
        uvage.from_image(345, 280, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 280, "bit.png"),
        uvage.from_image(305, 280, "bit.png"), uvage.from_image(SCREEN_WIDTH - 305, 280, "bit.png"),

        # middle mid high horiz
        uvage.from_image(380, 280, "bit.png"), uvage.from_image(SCREEN_WIDTH - 380, 280, "bit.png"),
        uvage.from_image(195, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 195, 340, "bit.png"),

        # middle horiz
        uvage.from_image(230, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 230, 340, "bit.png"),
        uvage.from_image(305, 400, "bit.png"), uvage.from_image(SCREEN_WIDTH - 305, 400, "bit.png"),

        # middle mid lower horiz
        uvage.from_image(340, 400, "bit.png"), uvage.from_image(SCREEN_WIDTH - 340, 400, "bit.png"),
        uvage.from_image(380, 400, "bit.png"), uvage.from_image(SCREEN_WIDTH - 380, 400, "bit.png"),
        uvage.from_image(305, 200, "bit.png"), uvage.from_image(SCREEN_WIDTH - 305, 200, "bit.png")]

    # walls
    walls = [
        uvage.from_color(400, 75, "dark blue", 800, 15),  # top ceiling
        uvage.from_color(800, SCREEN_HEIGHT - 5, "dark blue", 2000, 10),  # bottom floor

        uvage.from_color(0, 30, "dark blue", 30, 300),  # top and bottom side walls
        uvage.from_color(0, 600, "dark blue", 30, 300),
        uvage.from_color(SCREEN_WIDTH, 30, "dark blue", 30, 300),
        uvage.from_color(SCREEN_WIDTH, 600, "dark blue", 30, 300),

        uvage.from_color(0, 175, "dark blue", 250, 15),  # walls coming out of top and bottom
        uvage.from_color(SCREEN_WIDTH, 175, "dark blue", 250, 15),
        uvage.from_color(0, 450, "dark blue", 250, 15),
        uvage.from_color(SCREEN_WIDTH, 450, "dark blue", 250, 15),

        uvage.from_color(120, 217, "dark blue", 15, 100),  # walls going down
        uvage.from_color(120, 406, "dark blue", 15, 100),
        uvage.from_color(675, 217, "dark blue", 15, 100),
        uvage.from_color(675, 406, "dark blue", 15, 100),

        uvage.from_color(2, 275, "dark blue", 250, 15),  # walls coming out of middle
        uvage.from_color(SCREEN_WIDTH - 8, 275, "dark blue", 250, 15),
        uvage.from_color(2, 350, "dark blue", 250, 15),
        uvage.from_color(SCREEN_WIDTH - 8, 350, "dark blue", 250, 15),

        uvage.from_color(150, 125, "dark blue", 185, 15),  # top skinny lil bois
        uvage.from_color(SCREEN_WIDTH - 150, 125, "dark blue", 185, 15),

        uvage.from_color(400, 125, "dark blue", 200, 15),  # top middle horiz
        uvage.from_color(400, 175, "dark blue", 200, 15),
        uvage.from_color(300, 150, "dark blue", 15, 65),  # top middle vert
        uvage.from_color(500, 150, "dark blue", 15, 65),

        uvage.from_color(375, 215, "dark blue", 15, 85),  # top middle vert lower
        uvage.from_color(425, 215, "dark blue", 15, 85),
        uvage.from_color(400, 250, "dark blue", 65, 15),

        uvage.from_color(330, 310, "dark blue", 75, 15),  # cage horiz
        uvage.from_color(470, 310, "dark blue", 75, 15),
        uvage.from_color(400, 375, "dark blue", 200, 15),
        uvage.from_color(300, 347, "dark blue", 15, 70),  # cage vert
        uvage.from_color(500, 347, "dark blue", 15, 70),

        uvage.from_color(215, 175, "dark blue", 45, 15),  # left side box higher horiz
        uvage.from_color(215, 310, "dark blue", 45, 15),
        uvage.from_color(190, 242, "dark blue", 15, 150),  # left side box higher vert
        uvage.from_color(235, 242, "dark blue", 15, 150),

        uvage.from_color(320, 240, "dark blue", 15, 35),  # left side tiny box vert
        uvage.from_color(280, 230, "dark blue", 80, 15),
        uvage.from_color(280, 250, "dark blue", 80, 15),

        uvage.from_color(SCREEN_WIDTH - 215, 175, "dark blue", 45, 15),  # right side box horiz
        uvage.from_color(SCREEN_WIDTH - 215, 310, "dark blue", 45, 15),
        uvage.from_color(SCREEN_WIDTH - 190, 242, "dark blue", 15, 150),  # right side box vert
        uvage.from_color(SCREEN_WIDTH - 235, 242, "dark blue", 15, 150),

        uvage.from_color(SCREEN_WIDTH - 320, 240, "dark blue", 15, 35),  # left side tiny box vert
        uvage.from_color(SCREEN_WIDTH - 280, 230, "dark blue", 80, 15),
        uvage.from_color(SCREEN_WIDTH - 280, 250, "dark blue", 80, 15),

        uvage.from_color(215, 375, "dark blue", 45, 15),  # left side box lower horiz
        uvage.from_color(215, 460, "dark blue", 45, 15),
        uvage.from_color(190, 417, "dark blue", 15, 100),  # left side box lower vert
        uvage.from_color(235, 417, "dark blue", 15, 100),

        uvage.from_color(SCREEN_WIDTH - 215, 375, "dark blue", 45, 15),  # left side box lower horiz
        uvage.from_color(SCREEN_WIDTH - 215, 460, "dark blue", 45, 15),
        uvage.from_color(SCREEN_WIDTH - 190, 417, "dark blue", 15, 100),  # left side box lower vert
        uvage.from_color(SCREEN_WIDTH - 235, 417, "dark blue", 15, 100),

        uvage.from_color(190, 515, "dark blue", 255, 15),  # bottom box left horiz
        uvage.from_color(190, 545, "dark blue", 255, 15),
        uvage.from_color(65, 530, "dark blue", 15, 45),  # bottom box left vert
        uvage.from_color(320, 530, "dark blue", 15, 45),

        uvage.from_color(SCREEN_WIDTH - 190, 515, "dark blue", 255, 15),  # bottom box right horiz
        uvage.from_color(SCREEN_WIDTH - 190, 545, "dark blue", 255, 15),
        uvage.from_color(SCREEN_WIDTH - 65, 530, "dark blue", 15, 45),  # bottom box right vert
        uvage.from_color(SCREEN_WIDTH - 320, 530, "dark blue", 15, 45),

        uvage.from_color(400, 430, "dark blue", 200, 15),  # middle box horiz
        uvage.from_color(400, 460, "dark blue", 200, 15),
        uvage.from_color(300, 445, "dark blue", 15, 45),  # middle box vert
        uvage.from_color(500, 445, "dark blue", 15, 45),

        uvage.from_color(380, 505, "dark blue", 15, 95),  # bottom middle vert
        uvage.from_color(420, 505, "dark blue", 15, 95),
        uvage.from_color(400, 545, "dark blue", 55, 15),
    ]
    gate = uvage.from_color(400, 310, "yellow", 75, 15)  # door for ghosts


def tick():
    '''
    function which calls other functions multiple times a second to produce movement and images
    '''
    global count, game_on, game_win, game_over, game_ends, ink, blink, clyde, pink
    count += 1

    if uvage.is_pressing("space"):
        game_on = True

    if game_on == True:
        camera.clear("black")
        environment()
        player_movement()
        enemy_movement()
        scoring()
        appearance()
        game_end()
        camera.display()

    if game_on == False:
        camera.draw(uvage.from_text(400, 250, "Press Space Bar", 70, "dark blue"))
        camera.draw(uvage.from_text(398, 252, "Press Space Bar", 70, "white"))
        camera.draw(uvage.from_text(400, 350, "To Start Game", 70, "dark blue"))
        camera.draw(uvage.from_text(398, 352, "To Start Game", 70, "white"))
        camera.display()


def scoring():
    '''
    accounts for the score from collecting bits as well as how many lives are left for the play through
    '''
    global count, score, camera, score_display, bits, game_win, game_ends, game_over, ink, blink, pink, lives, lives_display, clyde
    for bit in bits:
        if player.touches(bit):
            score += 100
            bits.remove(bit)
        if score == 11000:
            game_win = True
            game_ends = True
            game_over = False
        camera.draw(bit)

    if player.touches(ink):
        game_ends = True
        lives -= 1
        del lives_display[0]
    if player.touches(blink):
        game_ends = True
        lives -= 1
        del lives_display[0]
    if player.touches(pink):  # collisions - losing lives
        game_ends = True
        lives -= 1
        del lives_display[0]
    if player.touches(clyde):  # collisions - losing lives
        game_ends = True
        lives -= 1
        del lives_display[0]

    if lives == 0:
        game_over = True

    for life in lives_display:
        camera.draw(life)

    score_display = uvage.from_text(62, 35, str(score), 50, "white")
    camera.draw(score_display)


def environment():
    '''
    draws the surrounding area of the for visual effect
    '''
    global walls, player, enemies, gate, blink, ink, pink, lives_display, lives, title

    for wall in walls:
        camera.draw(wall)
        if player.touches(wall):
            player.move_to_stop_overlapping(wall)  # drawing walls
        for enemy in enemies:
            if enemy.touches(wall):
                enemy.move_to_stop_overlapping(wall)

    camera.draw(gate)
    if player.touches(gate):  # general gate details
        player.move_to_stop_overlapping(gate)

    camera.draw(title)

    if count == 62:
        walls.insert(0, gate)

    for life in lives_display:  # drawing the lives
        camera.draw(life)


def player_movement():
    '''
    controls how the player moves
    '''
    global player, game_on, right_movement, left_movement, up_movement, down_movement, game_over, camera

    # player movement
    if uvage.is_pressing("right arrow"):
        game_on = True
        right_movement = True
        left_movement = False  # continuous right movement
        down_movement = False
        up_movement = False
    if right_movement == True:
        player.x += 5

    if uvage.is_pressing("left arrow"):
        game_on = True
        left_movement = True
        right_movement = False  # continuous left movement
        down_movement = False
        up_movement = False
    if left_movement == True:
        player.x -= 5

    if uvage.is_pressing("down arrow"):
        game_on = True
        down_movement = True
        left_movement = False  # continuous downward movement
        right_movement = False
        up_movement = False
    if down_movement == True:
        player.y += 5

    if uvage.is_pressing("up arrow"):
        game_on = True
        up_movement = True
        left_movement = False  # continuous upward movement
        right_movement = False
        down_movement = False
    if up_movement == True:
        player.y -= 5

    if player.x < 0:
        player.x = 790
    if player.x > 800:  # teleportation
        player.x = 10
    camera.draw(player)


def enemy_movement():
    '''
    controls how enemies move
    '''
    global blink, pink, ink, randy, randx, rightme, downme, leftme, upme, count, bits, game_on, choice, lives, enemies, walls, clyde
    if count < 60:
        if pink.x < 400:
            pink.x += 3
        pink.y -= 3
        if ink.x > 400:  # moves the ghosts out of the gate
            ink.x -= 3
        ink.y -= 3
        blink.y -= 3

    elif count % 30 == 0:
        choice = True  # random movement generator
        randx = random.randint(1, 2)
        randy = random.randint(1, 2)
    else:
        choice = False

    if count > 60:
        if randx == 1:
            ink.x -= 3
        elif randx == 2:
            ink.x += 3  # basic movement ink
        if randy == 1:
            ink.y += 3
        elif randy == 2:
            ink.y -= 3

        if randx == 1:
            pink.y += 3
        elif randx == 2:
            pink.y -= 3  # basic movement pink
        if randy == 1:
            pink.x -= 3
        elif randy == 2:
            pink.x += 3

        if randx == 1:
            blink.x += 3
        elif randx == 2:
            blink.x -= 3  # basic movement blink
        if randy == 1:
            blink.y -= 3
        elif randy == 2:
            blink.y += 3

    if randx == 1:
        clyde.x += 7
    elif randx == 2:
        clyde.x -= 5  # clyde's questionable movement
    if randy == 1:
        clyde.x -= 4
    elif randy == 2:
        clyde.x += 3

    for enemy in enemies:
        if enemy.x < 0:
            enemy.x = 790 # teleportation through the middle
        if enemy.x > 800:
            enemy.x = 10

    camera.draw(ink)
    camera.draw(pink)
    camera.draw(blink)
    camera.draw(clyde)


def appearance():
    '''
    animates pac-guy so it looks like he is opening and closing his mouth while moving
    '''
    global right_movement, left_movement, down_movement, up_movement, count, player
    if count % 5 == 0 and right_movement == True:
        player.image = "pacman2.png"
    elif count % 5 == 0 and left_movement == True:
        player.image = "pacman25.png"
    elif count % 5 == 0 and down_movement == True:
        player.image = "pacman3.png"
    elif count % 5 == 0 and up_movement == True:
        player.image = "pacman4.png"
    if count % 8 == 0:
        player.image = "pacman1.png"
    camera.draw(player)


def game_end():
    '''
    resets the game if lives are lost, or the game is lost or won
    '''
    global player, enemies, game_on, game_over, game_win, game_end, score, bits, game_ends
    global left_movement, right_movement, down_movement, up_movement, lives, lives_display, count, gate

    if game_ends == True:
        camera.draw(uvage.from_text(400, 250, "Press Space Bar", 70, "crimson", bold=False))
        camera.draw(uvage.from_text(398, 252, "Press Space Bar", 70, "white", bold=False))
        player.x = 10
        player.y = 100
        count = 1
        left_movement = False
        right_movement = False
        down_movement = False
        up_movement = False
        # print(len(walls))
        if len(walls) > 69:
            del walls[0]
        gate = uvage.from_color(400, 310, "yellow", 75, 15)

        for enemy in enemies:
            enemy.x = 400
            enemy.y = 350
            if enemy == clyde:
                enemy.x = 50
                enemy.y = 570

        if uvage.is_pressing("space"):
            player.x = 10
            player.y = 100
            # score = 0
            game_over = False
            game_on = False
            game_win = False
            game_ends = False

        if game_over == True or game_win == True:
            bits = [
                # coins top max score == 11000
                uvage.from_image(120, 100, "bit.png"),
                uvage.from_image(170, 100, "bit.png"),
                uvage.from_image(220, 100, "bit.png"),
                uvage.from_image(270, 100, "bit.png"),
                uvage.from_image(320, 100, "bit.png"),
                uvage.from_image(370, 100, "bit.png"),
                uvage.from_image(420, 100, "bit.png"),
                uvage.from_image(470, 100, "bit.png"),
                uvage.from_image(530, 100, "bit.png"),  # off
                uvage.from_image(570, 100, "bit.png"),
                uvage.from_image(620, 100, "bit.png"),
                uvage.from_image(670, 100, "bit.png"),
                uvage.from_image(720, 100, "bit.png"),
                uvage.from_image(760, 100, "bit.png"),

                uvage.from_image(70, 575, "bit.png"),  # coins bottom
                uvage.from_image(120, 575, "bit.png"),
                uvage.from_image(170, 575, "bit.png"),
                uvage.from_image(220, 575, "bit.png"),
                uvage.from_image(270, 575, "bit.png"),
                uvage.from_image(320, 575, "bit.png"),
                uvage.from_image(370, 575, "bit.png"),
                uvage.from_image(420, 575, "bit.png"),
                uvage.from_image(470, 575, "bit.png"),
                uvage.from_image(530, 575, "bit.png"),  # off
                uvage.from_image(570, 575, "bit.png"),
                uvage.from_image(620, 575, "bit.png"),
                uvage.from_image(670, 575, "bit.png"),
                uvage.from_image(720, 575, "bit.png"),
                uvage.from_image(760, 575, "bit.png"),

                uvage.from_image(35, 125, "bit.png"),  # coins right below top
                uvage.from_image(760, 125, "bit.png"),
                uvage.from_image(70, 150, "bit.png"),  # coins second top
                uvage.from_image(120, 150, "bit.png"),
                uvage.from_image(170, 150, "bit.png"),
                uvage.from_image(220, 150, "bit.png"),
                uvage.from_image(270, 150, "bit.png"),

                uvage.from_image(530, 150, "bit.png"),  # coins second top
                uvage.from_image(580, 150, "bit.png"),
                uvage.from_image(630, 150, "bit.png"),
                uvage.from_image(680, 150, "bit.png"),
                uvage.from_image(730, 150, "bit.png"),
                uvage.from_image(760, 150, "bit.png"),

                # coins column left, rows columns right
                uvage.from_image(155, 190, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 190, "bit.png"),
                uvage.from_image(155, 240, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 240, "bit.png"),
                uvage.from_image(155, 290, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 290, "bit.png"),
                uvage.from_image(155, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 340, "bit.png"),
                uvage.from_image(155, 390, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 390, "bit.png"),
                uvage.from_image(155, 440, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 440, "bit.png"),
                uvage.from_image(155, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 155, 480, "bit.png"),
                uvage.from_image(270, 190, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 190, "bit.png"),
                uvage.from_image(270, 290, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 290, "bit.png"),
                uvage.from_image(270, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 340, "bit.png"),
                uvage.from_image(270, 390, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 390, "bit.png"),
                uvage.from_image(270, 440, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 440, "bit.png"),
                uvage.from_image(270, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 270, 480, "bit.png"),
                uvage.from_image(37, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 37, 480, "bit.png"),

                # bottom vert
                uvage.from_image(37, 530, "bit.png"), uvage.from_image(SCREEN_WIDTH - 37, 530, "bit.png"),
                uvage.from_image(37, 575, "bit.png"),
                uvage.from_image(82, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 82, 480, "bit.png"),

                # second to bottom row horiz
                uvage.from_image(115, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 115, 480, "bit.png"),
                uvage.from_image(195, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 195, 480, "bit.png"),
                uvage.from_image(235, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 235, 480, "bit.png"),
                uvage.from_image(315, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 315, 480, "bit.png"),
                uvage.from_image(345, 480, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 480, "bit.png"),
                uvage.from_image(350, 510, "bit.png"), uvage.from_image(SCREEN_WIDTH - 350, 510, "bit.png"),
                uvage.from_image(350, 540, "bit.png"), uvage.from_image(SCREEN_WIDTH - 350, 540, "bit.png"),
                uvage.from_image(345, 200, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 200, "bit.png"),

                # middle top vert
                uvage.from_image(345, 240, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 240, "bit.png"),
                uvage.from_image(345, 280, "bit.png"), uvage.from_image(SCREEN_WIDTH - 345, 280, "bit.png"),
                uvage.from_image(305, 280, "bit.png"), uvage.from_image(SCREEN_WIDTH - 305, 280, "bit.png"),

                # middle mid high horiz
                uvage.from_image(380, 280, "bit.png"), uvage.from_image(SCREEN_WIDTH - 380, 280, "bit.png"),
                uvage.from_image(195, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 195, 340, "bit.png"),

                # middle horiz
                uvage.from_image(230, 340, "bit.png"), uvage.from_image(SCREEN_WIDTH - 230, 340, "bit.png"),
                uvage.from_image(305, 400, "bit.png"), uvage.from_image(SCREEN_WIDTH - 305, 400, "bit.png"),

                # middle mid lower horiz
                uvage.from_image(340, 400, "bit.png"), uvage.from_image(SCREEN_WIDTH - 340, 400, "bit.png"),
                uvage.from_image(380, 400, "bit.png"), uvage.from_image(SCREEN_WIDTH - 380, 400, "bit.png"),
                uvage.from_image(305, 200, "bit.png"), uvage.from_image(SCREEN_WIDTH - 305, 200, "bit.png")]


            lives_display = [

                uvage.from_image(680, 33, "life.png"),
                uvage.from_image(720, 33, "life.png"),
                uvage.from_image(760, 33, "life.png")
            ]

            for life in lives_display:
                camera.draw(life)

            for bit in bits:
                camera.draw(bit)
                camera.display()

        if game_win == True:
            game_on = False
            game_ends = False
            game_win = False
            score = 0
            lives = 3
            count = 1
            camera.clear("black")
            camera.draw(uvage.from_text(400, 150, "You Won!!", 70, "green", bold=False))
            camera.draw(uvage.from_text(398, 152, "You Won!!", 70, "white", bold=False))

        if game_over == True:
            game_on = False
            game_ends = False
            score = 0
            lives = 3
            count = 1
            camera.clear("black")
            camera.draw(uvage.from_text(400, 150, "Game Over", 70, "red", bold=False))
            camera.draw(uvage.from_text(398, 152, "Game Over", 70, "white", bold=False))
    camera.display()


setup()
ticks_per_second = 30
uvage.timer_loop(ticks_per_second, tick)