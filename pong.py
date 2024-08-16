import pygame,sys,random,time
pygame.init()

class settings():
    def __init__(self):
        self.background = pygame.display.set_mode((750,550))

        pygame.display.set_caption("pong")
        
        #imgaes
        self.Menu = pygame.image.load("Main_menu.png")
        self.Menu = pygame.transform.smoothscale(self.Menu,(750,550))
        
        self.game_mode_img = pygame.image.load("Game_mode.png")
        self.game_mode_img = pygame.transform.smoothscale(self.game_mode_img,(200,100))
        
        self.select_button = pygame.image.load("select_button.png")
        self.select_button_rect = self.select_button.get_rect()
        self.select_button_rect.center = [230,400]
        
        self.start_button = pygame.image.load("start_button.jpg")
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.center = [375,435]
        
        self.exit_button = pygame.image.load("exit.png")
        self.exit_button_rect = self.exit_button.get_rect()
        self.exit_button_rect.center = [475,375]
        
        self.replay_button = pygame.image.load("replay.png")
        self.replay_button_rect = self.replay_button.get_rect()
        self.replay_button_rect.center = [275,375]
        
        
        #settings
        self.font = pygame.font.SysFont(None,30)
        self.start = False
        self.clock = pygame.time.Clock()
        self.singleplayer_mode = False
        self.multiplayer_mode = False
        self.begin_game = False
        self.display_score = False
        self.player_1_goalCount = 0
        self.player_2_goalCount = 0
        self.player_1_goalText = self.font.render(f"goal : {self.player_1_goalCount}",1,"white")
        self.player_2_goalText = self.font.render(f"goal : {self.player_2_goalCount}",1,"white")
        



            
    def draw_screen(self):
                pygame.display.update()
                self.clock.tick(60)
                self.background.fill("grey12")
                pygame.draw.aaline(self.background,"grey12",(375,0),(375,550))
                player_1.draw()
                player_2.draw()    
                if game_window.player_1_goalCount != 3 and game_window.player_2_goalCount != 3:
                       pygame.draw.aaline(self.background,"white",(375,0),(375,550))
                pygame.draw.ellipse(self.background,"white",ball.body)
                self.background.blit(game_window.player_1_goalText,(150,80))
                self.background.blit(game_window.player_2_goalText,(520,80))
                if not self.begin_game and self.player_2_goalCount < 3 and self.player_1_goalCount < 3:
                    self.background.blit(self.start_button,(self.start_button_rect.topleft))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if self.start_button_rect.collidepoint(mouse_pos):
                            self.begin_game = True
                            game_loop()
    
    def gameover_and_reset(self,player):
        font = pygame.font.SysFont("Cambria",55)
        ball.x_velocity = 0
        ball.y_velocity = 0
        game_window.begin_game = False
        text = font.render(f"Winner : Player {player}",1,"white")
        self.background.blit(text,(175,200))
        self.background.blit(self.replay_button,(self.replay_button_rect.topleft))
        self.background.blit(self.exit_button,(self.exit_button_rect.topleft))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.exit_button_rect.collidepoint(mouse_pos):
                    sys.exit()
                elif self.replay_button_rect.collidepoint(mouse_pos):
                    self.player_1_goalCount = 0
                    self.player_2_goalCount = 0
                    self.player_1_goalText = self.font.render(f"goal : {self.player_1_goalCount}",1,"white")
                    self.player_2_goalText = self.font.render(f"goal : {self.player_2_goalCount}",1,"white")
                    self.begin_game = False
                    self.draw_screen()
        
        
            
    

                
game_window = settings()

class player():
    def __init__(self,x,y,id):
        self.body = pygame.Rect(x,y,10,150)
        self.goals = 0
        self.x_velocity = 7
        self.y_velocity = 7
        self.id = id
    
    def draw(self):
        pygame.draw.rect(game_window.background,"white",self.body)
    
    def first_controller(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.body.top >= 0 and game_window.begin_game:
            self.body.y -= 7
        elif keys[pygame.K_DOWN] and self.body.bottom <= 550 and game_window.begin_game:
            self.body.y += 7
            
    def second_controller(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.body.top >= 0 and game_window.begin_game:
            self.body.y -= 7
        elif keys[pygame.K_s] and self.body.bottom <= 550 and game_window.begin_game:
            self.body.y += 7
        
player_1 = player(0,200,"human".upper())
if game_window.singleplayer_mode:
    player_2 = player(740,200,"human".upper())
else:
    player_2 = player(740,200,"ai".upper())
        
      
      
      
      
      
      
        
class circle():
    def __init__(self):

        self.body = pygame.Rect(365,265,20,20)
        self.x_velocity = random.choice([7,-7,])
        self.y_velocity = random.choice([7,-7,5,-5])
        self.player_1_goals = 0
        self.player_2_goals = 0
        self.font = pygame.font.SysFont("default",30)
        

        
    
    
    def update(self):
        if game_window.begin_game:
            self.body.x += self.x_velocity
            self.body.y += self.y_velocity
        
        if self.body.top <= 0 or self.body.bottom >= 550:
                self.y_velocity *= -1

             
        if self.body.left <= 0 and game_window.player_2_goalCount <3 :
                game_window.player_2_goalCount += 1
                game_window.player_2_goalText = self.font.render(f"goal : {game_window.player_2_goalCount}",1,"white")   
                game_window.begin_game = False
                if game_window.player_2_goalCount < 3:
                    self.x_velocity = random.choice([7,-7,6,5,-5])
                    self.y_velocity = random.choice([7,-7,6,-6,5,-5])
                    self.body.center = [375,265]
        
             
             
        if self.body.right >= 750 and game_window.player_1_goalCount <3:
                game_window.player_1_goalCount += 1
                game_window.player_1_goalText = self.font.render(f"goal : {game_window.player_1_goalCount}",1,"white")
                game_window.begin_game = False
                if game_window.player_1_goalCount < 3:
                    self.x_velocity = random.choice([7,-7,6,-6,5,-5])
                    self.y_velocity = random.choice([7,-7,6,-6,5,-5,4,-4])
                    self.body.center = [375,265]
            

        if self.body.colliderect(player_1.body) or self.body.colliderect(player_2.body):
                self.x_velocity *= -1
        
    



            
            
            

            

ball = circle()









def main_menu():

    while True:
        
        pygame.display.update()
        game_window.background.blit(game_window.Menu,(0,0))
        game_window.background.blit(game_window.game_mode_img,(250,375))
        game_window.background.blit(game_window.select_button,(game_window.select_button_rect.topleft))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                sys.exit()
            if events.type == pygame.KEYDOWN:
                if events.key == pygame.K_RETURN:
                    game_loop()
                elif events.key == pygame.K_UP or events.key == pygame.K_DOWN:
                    if game_window.select_button_rect.y >= 400:
                        game_window.select_button_rect.y -= 50
                        game_window.single_player_mode = True
                        game_window.multiplayer_mode = False
                    else:
                        game_window.select_button_rect.y += 50
                        game_window.multiplayer_mode = True
                        game_window.single_player_mode = False

def start_game():
    while True:
        game_window.draw_screen()
    
    
def game_loop():
    while True:
        
        
        pygame.display.update()
        game_window.clock.tick(60)
        game_window.background.fill("grey12")
        pygame.draw.aaline(game_window.background,"grey12",(375,0),(375,550))
        player_1.draw()
        player_2.draw()    
        if game_window.player_1_goalCount != 3 and game_window.player_2_goalCount != 3:
            pygame.draw.aaline(game_window.background,"white",(375,0),(375,550))
        pygame.draw.ellipse(game_window.background,"white",ball.body)
        game_window.background.blit(game_window.player_1_goalText,(150,80))
        game_window.background.blit(game_window.player_2_goalText,(520,80))
        if not game_window.begin_game and game_window.player_2_goalCount < 3 and game_window.player_1_goalCount < 3:
            game_window.background.blit(game_window.start_button,(game_window.start_button_rect.topleft))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if game_window.start_button_rect.collidepoint(mouse_pos):
                    game_window.begin_game = True
        

        ball.update()
        player_1.first_controller()
        player_2.second_controller()
        if game_window.player_1_goalCount == 3 :
            game_window.gameover_and_reset(1)
        if game_window.player_2_goalCount == 3 :
            game_window.gameover_and_reset(2)
            
main_menu()