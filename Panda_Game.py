import pygame, random, os
pygame.init()
pygame.mixer.init()
size_of_screen = (640, 540)
# game window
window = pygame.display.set_mode((size_of_screen))
pygame.display.set_caption("Panda Game")
# Outgameloop Game variebles
font_sh = pygame.font.SysFont(None, 40, 60, 60)
font_wel = pygame.font.SysFont(None, 40, 255, 0)
font_dev = pygame.font.SysFont(None, 20, 60, 50)
font_30 = pygame.font.SysFont(None, 30, 60, 60)
font = pygame.font.SysFont(None, 40)
clock = pygame.time.Clock()

# IMAGES #

# game over image
go = pygame.image.load("gameover.png")
go = pygame.transform.scale(go, (640, 540)).convert_alpha()

# welcome screen image
wel = pygame.image.load("la.png")
wel = pygame.transform.scale(wel, (640, 540)).convert_alpha()

# background image
bgimg = pygame.image.load("bgimg.png")
bgimg = pygame.transform.scale(bgimg, (640, 540)).convert_alpha()

# functions
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    window.blit(screen_text , [x, y])

def text_screen_sh(text, color, x, y):
    screen_text = font_sh.render(text, True, color)
    window.blit(screen_text , [x, y])

def text_screen_wel(text, color, x, y):
    screen_text = font_wel.render(text, True, color)
    window.blit(screen_text , [x, y])

def text_screen_dev(text, color, x, y):
    screen_text = font_dev.render(text, True, color)
    window.blit(screen_text , [x, y])

def text_screen_30(text, color, x, y):
    screen_text = font_30.render(text, True, color)
    window.blit(screen_text , [x, y])

def welcome():
    exit_game = False
    while not exit_game:
        window.fill(pink)
        window.blit(wel, (0, 0))
        text_screen_wel("Press SPACE Button To Play", blue, 110, 10)
        text_screen_wel("Read The Instructions Before Playing!!!", blue, 12, 430)
        # text_screen("Press Space To Play", black, 180, 225)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("emty_music.wav")
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(30) 

   
# colors
yellow = (255, 255, 0)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
pink = (255, 192, 203)
blue = (65, 170, 230)
brown = (60, 15, 15)
green = (100, 185, 55)
new_color1 = (73, 237, 85)
new_color2 = (100, 237, 95)
new_color4 = (150, 237, 105)

def gameloop():
    if(not os.path.exists("hscore.txt")):
        with open("hscore.txt", "w") as h:
            h.write("0")
    with open("hscore.txt", "r") as h:
        highscore = h.read()
    # Ingameloop Game specific variebles
    insect_all_res1 = (480, 150, 300, 330, 120, 510)
    insect_all_res2 = (480, 300, 330, 120, 510, 150)
    insect_all_res3 = (480, 150, 330, 120, 510, 300)
    insect_all_res4 = (480, 150, 300, 120, 510, 330)
    insect_all_res = (480, 150, 300, 330, 510, 120)
    insect_all_res5 = (480, 510, 120, 150, 300, 330)
    insect_x = random.choice(insect_all_res)
    insect_x1 = random.choice(insect_all_res1)
    insect_x2 = random.choice(insect_all_res2)
    insect_x3 = random.choice(insect_all_res3)
    insect_x4 = random.choice(insect_all_res4)
    insect_x5 = random.choice(insect_all_res5)
    insect_y = 550
    insect_y1 = 600*2
    insect_y2 = 650*2
    insect_y3 = 700*2
    insect_y4 = 750*2
    insect_y5 = 710*2
    exit_game = False
    game_over = False
    red_panda_x = 300
    red_panda_y = 240
    panda_size = 10
    piller_1_width = 40
    piller_1_height = 480
    piller_1_x = 300
    piller_1_y = 60
    piller_2_width = 40
    piller_2_height = 480
    piller_2_x = 120
    piller_2_y = 60
    piller_3_width = 40
    piller_3_height = 480
    piller_3_x = 480
    piller_3_y = 60
    fps = 30
    velocity_x = 0
    velocity_y = 0
    margine_1_x = 0
    margine_1_y = 60
    margine_1_width = 640
    margine_1_height = 10
    margine_2_x = 0
    margine_2_y = 60
    margine_2_width = 10
    margine_2_height = 480
    margine_3_x = 630
    margine_3_y = 60
    margine_3_width = 10
    margine_3_height = 480
    margine_4_x = 0
    margine_4_y = 530
    margine_4_width = 640
    margine_4_height = 10
    score = 0
    outside_the_margine = 0
    reason_for_GM = "nothing"
    reason_for_GM1 = "nothing"
    reason_for_GM2 = "nothing"
    # main game
    while not exit_game:
        # making the game over event
        if game_over:
            with open("hscore.txt", "w") as h:
                h.write(str(highscore))
            window.fill(pink)
            window.blit(go, (0, 50))
            text_screen_sh("Press SPACE To Continue", red, 135, 50)
            text_screen_sh("--Developed By Harshit Kashyap Sarma--", red, 60, 465)
            if reason_for_GM == reason_for_GM1:
                text_screen_sh(reason_for_GM1, red, 200, 415)
            else:
                text_screen_30(reason_for_GM2, red, 13, 415)
            # text_screen("Game Over !!!, Press Enter To Continue", red, 40, 280)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.load("emty_music.wav")
                        pygame.mixer.music.play()
                        gameloop()
            pygame.display.update()                        
        else:
            # giving the panda a velocity
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        velocity_x = velocity_x + 0
                        velocity_y = velocity_y + 4
                    if event.key == pygame.K_DOWN:
                        velocity_x = velocity_x + 0
                        velocity_y = velocity_y + 4
                    if event.key == pygame.K_UP:
                        velocity_x = velocity_x + 0
                        velocity_y = velocity_y - 4
                    
                    if event.key == pygame.K_s:
                        score = score + 50
                # this 'else' statement is only for the above section not for any other section
                else: 
                    velocity_x = 0
                    velocity_y = 0 
                # handling the quit event           
                if event.type == pygame.QUIT:
                    exit_game = True
                
                # handling all the panda movements
                if red_panda_x == 510:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            red_panda_x = red_panda_x - 30               
                else:
                    if red_panda_x == 480:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_RIGHT:
                                red_panda_x = red_panda_x + 30
                            if event.key == pygame.K_LEFT:
                                red_panda_x = red_panda_x - 150
                    else:
                        if red_panda_x == 330:
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RIGHT:
                                    red_panda_x = red_panda_x + 150      
                                if event.key == pygame.K_LEFT:
                                    red_panda_x = red_panda_x - 30
                        else:
                            if red_panda_x == 300:
                                if event.type == pygame.KEYDOWN:
                                    if event.key == pygame.K_RIGHT:
                                        red_panda_x = red_panda_x + 30
                                    if event.key == pygame.K_LEFT:
                                        red_panda_x = red_panda_x - 150
                            else:
                                if red_panda_x == 150:
                                    if event.type == pygame.KEYDOWN:
                                        if event.key == pygame.K_RIGHT:
                                            red_panda_x = red_panda_x + 150
                                        if event.key == pygame.K_LEFT:
                                            red_panda_x = red_panda_x - 30
                                else:
                                    if red_panda_x == 120:
                                        if event.type == pygame.KEYDOWN:
                                            if event.key == pygame.K_RIGHT:
                                                red_panda_x = red_panda_x + 30
            # filling the screen with color
            window.fill(pink)
            # setting the backgroud image
            window.blit(bgimg, (0, 60))
            text_screen_dev("--Developed By Harshit Kashyap--", black, 400, 45)  
            red_panda_y = red_panda_y + velocity_y            
            red_panda_x = red_panda_x + velocity_x
            if score <=100:
                insect_y = insect_y - 1.50
                insect_y1 = insect_y1 - 1.50
                insect_y2 = insect_y2 - 1.50
                insect_y3 = insect_y3 - 1.50*0
                insect_y4 = insect_y4 - 1.50
                insect_y5 = insect_y5 - 1.50
            if score <=120 and score >100:
                insect_y = insect_y - 1.75
                insect_y1 = insect_y1 - 1.75
                insect_y2 = insect_y2 - 1.75
                # insect_y3 = insect_y3 - 1.5750
                insect_y4 = insect_y4 - 1.75
                insect_y5 = insect_y5 - 1.75
            if score <= 150 and score > 120:
                insect_y = insect_y - 2
                insect_y1 = insect_y1 - 2
                insect_y2 = insect_y2 - 2
                # insect_y3 = insect_y3 - 2*0
                insect_y4 = insect_y4 - 2
                insect_y5 = insect_y5 - 2
            if score <= 170 and score > 150:
                insect_y = insect_y - 2.25
                insect_y1 = insect_y1 - 2.25
                insect_y2 = insect_y2 - 2.25
                # insect_y3 = insect_y3 -.25 2*0
                insect_y4 = insect_y4 - 2.25
                insect_y5 = insect_y5 - 2.25                
            if score <= 200 and score > 170:
                insect_y = insect_y - 2.50
                insect_y1 = insect_y1 - 2.50
                insect_y2 = insect_y2 - 2.50
                # insect_y3 = insect_y3 - 2.50*0
                insect_y4 = insect_y4 - 2.50
                insect_y5 = insect_y5 - 2.50
            if score <= 230 and score > 200:
                insect_y = insect_y - 2.75
                insect_y1 = insect_y1 - 2.75
                insect_y2 = insect_y2 - 2.75
                # insect_y3 = insect_y3 - 7550*0
                insect_y4 = insect_y4 - 2.75
                insect_y5 = insect_y5 - 2.75
            if score <= 250 and score > 230 :
                red_panda_y = red_panda_y + 1.10*velocity_y          
                insect_y = insect_y - 3
                insect_y1 = insect_y1 - 3
                insect_y2 = insect_y2 - 3
                # insect_y3 = insect_y3 - 3*0
                insect_y4 = insect_y4 - 3
                insect_y5 = insect_y5 - 3
            if score <= 270 and score > 250 :
                red_panda_y = red_panda_y + 1.10*velocity_y          
                insect_y = insect_y - 3.25
                insect_y1 = insect_y1 - 3.25
                insect_y2 = insect_y2 - 3.25
                # insect_y3 = insect_y3 -.25 3*0
                insect_y4 = insect_y4 - 3.25
                insect_y5 = insect_y5 - 3.25
            if score <= 300 and score > 270 :
                red_panda_y = red_panda_y + 1.10*velocity_y            
                insect_y = insect_y - 3.5
                insect_y1 = insect_y1 - 3.5
                insect_y2 = insect_y2 - 3.5
                # insect_y3 = insect_y3 - 3.5*0
                insect_y4 = insect_y4 - 3.5
                insect_y5 = insect_y5 - 3.5
            if score > 300 :
                red_panda_y = red_panda_y + 1.10*velocity_y            
                insect_y = insect_y -3.75
                insect_y1 = insect_y1 -3.75
                insect_y2 = insect_y2 -3.75
                # insect_y3 = insect_y3 - 3.75*0
                insect_y4 = insect_y4 -3.75
                insect_y5 = insect_y5 -3.75
            # handling the insects which tries to go outside_the_margine
            if red_panda_y < 70:
                red_panda_y = 69.99
            if red_panda_y > 520:
                red_panda_y = 519.9999
            if insect_y < 70:
                insect_y = 550             
                outside_the_margine = outside_the_margine + 1
                print("Number of insects went outside : ",   outside_the_margine)
                insect_x = random.choice(insect_all_res) 
            if insect_y1 < 70:
                insect_y1 = 600              
                outside_the_margine = outside_the_margine + 1
                print("Number of insects went outside : ",   outside_the_margine)
                insect_x1 = random.choice(insect_all_res1)
            if insect_y2 < 70:
                insect_y2 = 650 
                outside_the_margine = outside_the_margine + 1
                print("Number of insects went outside : ",   outside_the_margine) 
                insect_x2 = random.choice(insect_all_res2)                 
            if insect_y3 < 70:
                insect_y3 = 70
                outside_the_margine = outside_the_margine + 1
                print("Number of insects went outside : ",   outside_the_margine)
                insect_x3 = random.choice(insect_all_res3)
            if insect_y4 < 70:
                insect_y4 = 750   
                outside_the_margine = outside_the_margine + 1
                print("Number of insects went outside : ",   outside_the_margine)
                insect_x4 = random.choice(insect_all_res4)
            if insect_y5 < 70:
                insect_y5 = 710  
                outside_the_margine = outside_the_margine + 1
                print("Number of insects went outside : ",   outside_the_margine)
                insect_x5 = random.choice(insect_all_res5)    
            # handling the cause of game over and the cause of score
            if velocity_y == 4:
                if abs(red_panda_x - insect_x)<6 and abs(red_panda_y - insect_y)<6:
                    insect_x = random.choice(insect_all_res)
                    insect_y = 550
                    score = score + 10
                    if score > int(highscore):
                        highscore = score
                    pygame.mixer.music.load("smb_fireball.wav")
                    pygame.mixer.music.play()
                if abs(red_panda_x - insect_x1)<6 and abs(red_panda_y - insect_y1)<6:
                    insect_x1 = random.choice(insect_all_res1)
                    insect_y1 = 600
                    score = score + 10
                    if score > int(highscore):
                        highscore = score
                    pygame.mixer.music.load("smb_fireball.wav")
                    pygame.mixer.music.play()
                if abs(red_panda_x - insect_x2)<6 and abs(red_panda_y - insect_y2)<6:
                    insect_x2 = random.choice(insect_all_res2)
                    insect_y2 = 650
                    score = score + 10
                    if score > int(highscore):
                        highscore = score
                    pygame.mixer.music.load("smb_fireball.wav")
                    pygame.mixer.music.play()
                if abs(red_panda_x - insect_x3)<6 and abs(red_panda_y - insect_y3)<6:
                    insect_x3 = random.choice(insect_all_res3)
                    insect_y3 = 700
                    score = score + 10
                    if score > int(highscore):
                        highscore = score
                    pygame.mixer.music.load("smb_fireball.wav")
                    pygame.mixer.music.play()
                if abs(red_panda_x - insect_x4)<6 and abs(red_panda_y - insect_y4)<6:
                    insect_x4 = random.choice(insect_all_res4)
                    insect_y4 = 750
                    score = score + 10
                    if score > int(highscore):
                        highscore = score
                    pygame.mixer.music.load("smb_fireball.wav")
                    pygame.mixer.music.play()
                if abs(red_panda_x - insect_x5)<6 and abs(red_panda_y - insect_y5)<6:
                    insect_x5 = random.choice(insect_all_res5)
                    insect_y5 = 710
                    score = score + 10
                    if score > int(highscore):
                        highscore = score
                    pygame.mixer.music.load("smb_fireball.wav")
                    pygame.mixer.music.play()
            if abs(insect_x - red_panda_x)<6 and abs(insect_y - red_panda_y)<6:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM1 = "Insects bit you!"
                reason_for_GM = reason_for_GM1
                game_over = True
            if abs(insect_x1 - red_panda_x)<6 and abs(insect_y1 - red_panda_y)<6:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM1 = "Insects bit you!"
                reason_for_GM = reason_for_GM1
                game_over = True
            if abs(insect_x2 - red_panda_x)<6 and abs(insect_y2 - red_panda_y)<6:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM1 = "Insects bit you!"
                reason_for_GM = reason_for_GM1
                game_over = True
            if abs(insect_x3 - red_panda_x)<6 and abs(insect_y3 - red_panda_y)<6:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM1 = "Insects bit you!"
                reason_for_GM = reason_for_GM1
                game_over = True
            if abs(insect_x4 - red_panda_x)<6 and abs(insect_y4 - red_panda_y)<6:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM1 = "Insects bit you!"
                reason_for_GM = reason_for_GM1
                game_over = True
            if abs(insect_x5 - red_panda_x)<6 and abs(insect_y5 - red_panda_y)<6:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM1 = "Insects bit you!"
                reason_for_GM = reason_for_GM1
                game_over = True
            if outside_the_margine == 5 and score <= 200:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM2 = "You let 5 insects go outside the margin."
                reason_for_GM = reason_for_GM2
                game_over = True
            if outside_the_margine == 10 and score > 200:
                pygame.mixer.music.load("smb_gameover.wav")
                pygame.mixer.music.play()
                reason_for_GM2 = "You let 5 insects go outside the margin."
                reason_for_GM = reason_for_GM2
                game_over = True
            if int(highscore) > 1000:
                text_screen_sh("SCORE : " + str(score) + "          HIGHSCORE : " + str(highscore), blue, 30, 5) 
            else:           
                text_screen_sh("SCORE : " + str(score) + "              HIGHSCORE : " + str(highscore), blue, 30, 5)
            pygame.draw.rect(window, yellow, [insect_x, insect_y, panda_size, panda_size])
            pygame.draw.rect(window, brown, [piller_3_x, piller_3_y, piller_3_width, piller_3_height])
            pygame.draw.rect(window, brown, [piller_1_x, piller_1_y, piller_1_width, piller_1_height])
            pygame.draw.rect(window, brown, [piller_2_x, piller_2_y, piller_2_width, piller_2_height])
            pygame.draw.rect(window, red, [red_panda_x, red_panda_y, panda_size, panda_size])
            pygame.draw.rect(window, yellow, [insect_x, insect_y, panda_size, panda_size])
            pygame.draw.rect(window, yellow, [insect_x1, insect_y1, panda_size, panda_size])
            pygame.draw.rect(window, yellow, [insect_x2, insect_y2, panda_size, panda_size])
            pygame.draw.rect(window, yellow, [insect_x3, insect_y3, panda_size, panda_size])
            pygame.draw.rect(window, yellow, [insect_x4, insect_y4, panda_size, panda_size])
            pygame.draw.rect(window, yellow, [insect_x5, insect_y5, panda_size, panda_size])
            pygame.draw.rect(window, black, [margine_1_x, margine_1_y, margine_1_width, margine_1_height])
            pygame.draw.rect(window, black, [margine_2_x, margine_2_y, margine_2_width, margine_2_height])
            pygame.draw.rect(window, black, [margine_3_x, margine_3_y, margine_3_width, margine_3_height])
            pygame.draw.rect(window, black, [margine_4_x, margine_4_y, margine_4_width, margine_4_height])
            clock.tick(fps)
            pygame.display.update()
    pygame.quit()
    quit()
welcome() 






# have to give the score in the game over manu