'''
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
Ammaar Siddiqui
Asteroids
Version 1
This game is Galaga played horizontally.
You have a spaceship and have to go through enemy spaceships and asteroid fields.
There are 5 stages. Each stage consists of 8 levels. 6 enemies and 2 asteroid fields.
There is also a shop where you can buy lives, bombs, speed, and multi-lasers.
It is programmed in Python's Pygame.
The aim of the game is to finish as many stages as possible with 5 deaths.
'''

# Ammaar Siddiqui
# Advanced Computer Programming
# 2/22/19

import pygame
import random
import math
import sys
import subprocess
import os




class Entity(pygame.sprite.Sprite):
    """Inherited by any object in the game."""

    def __init__(self, x, y, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # This makes a rectangle around the entity, used for anything
        # from collision to moving around.
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


class Spaceship(Entity):
    """
    Player controlled or AI controlled, main interaction with
    the game
    """

    def __init__(self, x, y, width, height):
        super(Spaceship, self).__init__(x, y, width, height)

        self.image = spaceship1Img


class Player(Spaceship):
    """The player controlled Spaceship"""

    def __init__(self, x, y, width, height):
        global speed
        super(Player, self).__init__(x, y, width, height)

        # How many pixels the Player Paddle should move on a given frame.
        self.y_change = 0
        # How many pixels the paddle should move each frame a key is pressed.
        self.y_dist = speed

    def MoveKeyDown(self, key):
        global multilasers
        global bombs
        global enemy_laser_list
        global just_shoot
        """Responds to a key-down event and moves accordingly"""
        if (key == pygame.K_UP):
            self.y_change += -self.y_dist
        elif (key == pygame.K_DOWN ):
            self.y_change += self.y_dist
        elif (key == pygame.K_SPACE):
            laser_noise.play()
            if stage==1 and just_shoot==False:
                x = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2, 44, 5)
                all_sprites_list.add(x)
                laser_list.append(x)
            elif stage==2 and just_shoot==False:
                x = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 - 5, 44, 5)
                all_sprites_list.add(x)
                laser_list.append(x)
                y = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 + 5, 44, 5)
                all_sprites_list.add(y)
                laser_list.append(y)
            elif stage==3 and just_shoot==False:
                x = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 - 7, 44, 5)
                all_sprites_list.add(x)
                laser_list.append(x)
                y = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2, 44, 5)
                all_sprites_list.add(y)
                laser_list.append(y)
                z = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 + 7, 44, 5)
                all_sprites_list.add(z)
                laser_list.append(z)
            elif stage == 4 and just_shoot==False:
                x = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 - 15, 44, 5)
                all_sprites_list.add(x)
                laser_list.append(x)
                y = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2, 44, 5)
                all_sprites_list.add(y)
                laser_list.append(y)
                z = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 + 15, 44, 5)
                all_sprites_list.add(z)
                laser_list.append(z)
            elif stage==5 and just_shoot==False:
                x = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 + 5, 44, 5)
                all_sprites_list.add(x)
                laser_list.append(x)
                y = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2, 44, 5)
                all_sprites_list.add(y)
                laser_list.append(y)
                z = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2 - 5, 44, 5)
                all_sprites_list.add(z)
                laser_list.append(z)
            elif stage==6 and just_shoot==False:
                v = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2-25, 44, 5)
                all_sprites_list.add(v)
                laser_list.append(v)
                x = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2, 44, 5)
                all_sprites_list.add(x)
                laser_list.append(x)
                y = Laser(spaceship.rect.x + 70, spaceship.rect.y + spaceship.rect.height/2+25, 44, 5)
                all_sprites_list.add(y)
                laser_list.append(y)
            just_shoot=True
        elif (key == pygame.K_z):  # Pressing Z creates a shotgun blast of lasers
            if multilasers > 0:
                w = Laser(spaceship.rect.x + 90, spaceship.rect.y + 7, 44, 5)
                all_sprites_list.add(w)
                laser_list.append(w)
                x = Laser(spaceship.rect.x + 100, spaceship.rect.y + 17, 44, 5)
                all_sprites_list.add(x)
                laser_list.append(x)
                y = Laser(spaceship.rect.x + 110, spaceship.rect.y + 27, 44, 5)
                all_sprites_list.add(y)
                laser_list.append(y)
                z = Laser(spaceship.rect.x + 100, spaceship.rect.y + 37, 44, 5)
                all_sprites_list.add(z)
                laser_list.append(z)
                v = Laser(spaceship.rect.x + 90, spaceship.rect.y + 47, 44, 5)
                all_sprites_list.add(v)
                laser_list.append(v)
                multilasers -= 1
        elif (key==pygame.K_x):
            global asteroid_list
            global enemy_laser_list
            global score
            if bombs > 0:
                explosion_noise.play()
                if asteroids==False:
                    for elaser in enemy_laser_list:
                        if isinstance(elaser, EnemyLaser):
                            elaser.remove(all_sprites_list)
                    enemy_laser_list = []
                elif asteroids:
                    score+=len(asteroid_list)*2
                    for asteroid in asteroid_list:
                        if isinstance(asteroid, Asteroid):
                            asteroid.remove(all_sprites_list)
                    asteroid_list = []
                bombs-=1

    def MoveKeyUp(self, key):
        global POINTS1
        global POINTS2
        global score_display
        """Responds to a key-up event and stops movement accordingly"""
        if (key == pygame.K_UP):
            self.y_change += self.y_dist
        elif (key == pygame.K_DOWN ):
            self.y_change += -self.y_dist

    def update(self):
        """
        Makes sure the spaceship stays in bounds
        """
        # Moves it relative to its current location.
        self.rect.move_ip(0, self.y_change)

        # If the spaceship moves off the screen, put it back on.
        if self.rect.y < 75:
            self.rect.y = 75
        elif self.rect.y > window_height - self.height - 5:
            self.rect.y = window_height - self.height - 5


class Enemy(Spaceship):
    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__(x, y, width, height)
        self.image = enemy1Img

        self.y_change = 4

    def update(self):
        global window_height
        if spaceship.rect.y + spaceship.rect.height / 2 < (self.rect.y + self.rect.height / 2)-10:
            self.rect.y -= self.y_change
        elif spaceship.rect.y + spaceship.rect.height / 2 > (self.rect.y + self.rect.height / 2)+10:
            self.rect.y += self.y_change
        if self.rect.y + self.rect.height > window_height - 5:
            self.rect.y = window_height - self.rect.height - 5
        elif self.rect.y < 35:
            self.rect.y = 35


class EnemyLaser(Entity):
    def __init__(self, x, y, width, height):
        super(EnemyLaser, self).__init__(x, y, width, height)

        self.image = enemylaserImg

    def update(self):
        self.rect.x -= 8


class Laser(Entity):
    def __init__(self, x, y, width, height):
        super(Laser, self).__init__(x, y, width, height)

        self.image = laserImg

    def update(self):
        self.rect.x += 8  # moves right at a speed of 8


class Asteroid(Entity):
    def __init__(self, x, y, width, height):
        super(Asteroid, self).__init__(x, y, width, height)

        self.image = asteroidImg

    def update(self):
        self.rect.x -= asteroid_speed  # moves left at an increasing speed


class Bonus(Entity):
    def __init__(self, x, y, width, height):
        super(Bonus, self).__init__(x, y, width, height)

        self.image = speed_upImg

    def update(self):
        self.rect.x -= asteroid_speed  # moves left at the same speed as the asteroids


def lasast_collide(asteroids, lasers):  # checks if the laser has collided with the asteroid
    global asteroid_speed
    global score
    for asteroid in asteroids:
        for laser in lasers:
            if asteroid.rect.colliderect(laser):
                asteroid.remove(all_sprites_list)
                if asteroid in asteroids:
                    asteroids.remove(asteroid)
                laser.remove(all_sprites_list)
                if laser in lasers:
                    lasers.remove(laser)
                asteroid_speed += .1
                asteroid_explosion.play()
                score += 2


def lasbonus_collide(bonuses, lasers):  # checks if the laser has collided with the bonus
    global extra_lasers
    for bonus in bonuses:
        for laser in lasers:
            if bonus.rect.colliderect(laser):
                bonus.remove(all_sprites_list)
                if bonus in bonuses:
                    bonuses.remove(bonus)
                laser.remove(all_sprites_list)
                if laser in lasers:
                    lasers.remove(laser)
                extra_lasers += 3


def astship_collide(asts):  # checks if any asteroids have hit the ship
    global lives
    for ast in asts:
        if ast.rect.colliderect(spaceship.rect):
            if ast in asts:
                asts.remove(ast)
            ast.remove(all_sprites_list)
            lives -= 1
            explosion_noise.play()


def lasship_collide(lasers):
    global lives
    for laser in lasers:
        if laser.rect.colliderect(spaceship.rect):
            if laser in lasers:
                lasers.remove(laser)
            laser.remove(all_sprites_list)
            lives -= 1
            explosion_noise.play()


def lasenemy_collide(lasers):
    global score
    global enemy_lives
    global enemy_list
    global enemy_num
    for laser in lasers:
        if laser.rect.colliderect(enemy_list[enemy_num].rect):
            score+=25
            if laser in lasers:
                lasers.remove(laser)
                laser.remove(all_sprites_list)
            enemy_lives -= 1
            explosion_noise.play()


def laslascollide(lasers, e_lasers):
    for laser in lasers:
        for elaser in e_lasers:
            if laser.rect.colliderect(elaser.rect):
                if laser in lasers:
                    lasers.remove(laser)
                    laser.remove(all_sprites_list)
                if elaser in e_lasers:
                    e_lasers.remove(elaser)
                    elaser.remove(all_sprites_list)


def update_score():  # function changes score
    global score
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render(("POINTS:" + str(score)), True, (WHITE))
    return text


def update_lives():  # function changes lives
    global lives
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render(("LIVES:" + str(lives)), True, (WHITE))
    return text


def update_e_lives():  # function changes the amount of bonuses
    global enemy_lives
    font = pygame.font.SysFont("comicsansms", 25)
    text = font.render(("ENEMY LIVES: " + str(enemy_lives)), True, (WHITE))
    return text

def end_game_screen():
    global lives_lost
    global stage
    global current_level
    font4 = pygame.font.SysFont("arialblack", 35)
    file = open("highscores.txt", "r")
    scores = file.readlines()
    file.close()
    scores = [SCORE.replace('\n', '') for SCORE in scores]#gets scores
    scores = [SCORE.split("|") for SCORE in scores]
    if stage > int(scores[9][0]) or (stage==scores[9][0] and current_level>scores[9][1]):
        for SCORE in scores:
            if stage == int(SCORE[0]):
                if current_level>int(SCORE[1]):
                    scores.insert(scores.index(SCORE), [str(stage), str(current_level)])
                    break
            elif stage>int(SCORE[0]):
                scores.insert(scores.index(SCORE), [str(stage), str(current_level)])
                break
        del scores[-1]
    file2=open("highscores.txt", "w")
    for SCORE in scores:
        file2.write(str(SCORE[0])+"|"+str(SCORE[1])+"\n")
    file2.close()
    while True:
        screen.fill((0, 0, 0))
        game_finish2 = font4.render("Click to Restart", True, (WHITE))
        lowest_lives=font4.render("HIGHSCORES", True, (WHITE))
        score1=font4.render("1. Stage " + str(scores[0][0]) + ", Level " + str(scores[0][1]), True, (WHITE))
        score2=font4.render("2. Stage " + str(scores[1][0]) + ", Level " + str(scores[1][1]), True, (WHITE))
        score3=font4.render("3. Stage " + str(scores[2][0]) + ", Level " + str(scores[2][1]), True, (WHITE))
        score4=font4.render("4. Stage " + str(scores[3][0]) + ", Level " + str(scores[3][1]), True, (WHITE))
        score5=font4.render("5. Stage " + str(scores[4][0]) + ", Level " + str(scores[4][1]), True, (WHITE))
        score6=font4.render("6. Stage " + str(scores[5][0]) + ", Level " + str(scores[5][1]), True, (WHITE))
        score7=font4.render("7. Stage " + str(scores[6][0]) + ", Level " + str(scores[6][1]), True, (WHITE))
        score8=font4.render("8. Stage " + str(scores[7][0]) + ", Level " + str(scores[7][1]), True, (WHITE))
        score9=font4.render("9. Stage " + str(scores[8][0]) + ", Level " + str(scores[8][1]), True, (WHITE))
        score10=font4.render("10. Stage " + str(scores[9][0]) + ", Level " + str(scores[9][1]), True, (WHITE))
        score11=font4.render("Your Level Reached: ", True, (WHITE))
        score12=font4.render("Stage "+str(stage), True, (WHITE))
        score13=font4.render("Level "+str(current_level), True, (WHITE))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==pygame.MOUSEBUTTONUP:
                #pygame.quit()
                #os.execv(sys.executable, ['python'] + sys.argv)
                #os.system("Asteroid Shooter.py")
                return
        
        screen.blit(lowest_lives, (0, 0))
        screen.blit(score1, (0, 50))
        screen.blit(score2, (0, 100))
        screen.blit(score3, (0, 150))
        screen.blit(score4, (0, 200))
        screen.blit(score5, (0, 250))
        screen.blit(score6, (0, 300))
        screen.blit(score7, (0, 350))
        screen.blit(score8, (0, 400))
        screen.blit(score9, (0, 450))
        screen.blit(score10, (0, 500))
        screen.blit(score11, (500, 100))
        screen.blit(score12, (500, 140))
        screen.blit(score13, (500, 180))
        screen.blit(game_finish2, (0, 550))
        pygame.display.flip()






def start_game():
    global total_lives
    global spaceship
    global spaceship_list
    global spaceship_num
    global spaceshipImg_num
    global spaceshipImg_list
    global stage
    global background
    global lives
    global score
    global asteroid_limit
    global laser_list
    global enemy_laser_list
    global asteroid_list
    global bonus_list
    global asteroid_speed
    global extra_lasers
    global score_display
    global laser_count
    global entity_color
    global WHITE
    global POINTS1
    global POINTS2
    global window_width
    global window_height
    global bonus_count
    global wall_count
    global screen
    global clock
    global shop_screen
    global level_screen
    global start_screen
    global speed
    global enemy_lives
    global level
    global enemies
    global shoot_speed
    global enemy_num
    global enemy_list
    global enemyImg_num
    global enemyImg_list
    global bg_x
    global bg_y
    global bg_w
    global bg_h
    global bg_x1
    global bg_y1
    global enemyImgadd
    global shields
    global multilasers
    global bombs
    global asteroids
    global just_asteroid
    global allow_shoot
    global just_shoot
    global lives_lost
    global current_level
    ##-------------------------------------------------------------------------##
    ##-------------------------------------------------------------------------##
    ##WHILE TRUE LOOOOOOP
    ##-------------------------------------------------------------------------##
    ##-------------------------------------------------------------------------##

    while True:
        allow_shoot+=1
        if allow_shoot%15==0:
            just_shoot=False
        lasast_collide(asteroid_list, laser_list)
        astship_collide(asteroid_list)
        lasbonus_collide(bonus_list, laser_list)
        lasship_collide(enemy_laser_list)
        if asteroids==False:
            lasenemy_collide(laser_list)
        laslascollide(laser_list, enemy_laser_list)

        if asteroids:
            wall_count+=1

        if wall_count==50 and asteroids:#adds a wall every 40 asteroids
            asteroid_limit=35
            wall_count=-30

        if len(asteroid_list)>30 and asteroids:#resets the asteroid limit if there are too many astroids on screen
            asteroid_limit=5

        if len(asteroid_list) < asteroid_limit and asteroids:#adds an asteroid if they have less then a certain number of asteroids on the screen
            x = Asteroid(random.randint(window_width, window_width+1000), random.randint(75, 500), 87, 85)
            asteroid_list.append(x)
            all_sprites_list.add(x)

        laser_count += 1

        if laser_count % shoot_speed == 0 and asteroids==False:
            if enemy_num == 0:
                y = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2), 44, 5)
                all_sprites_list.add(y)
                enemy_laser_list.append(y)
                enemy_laser_noise.play()
            elif enemy_num == 1:
                y = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 5), 44, 5)
                all_sprites_list.add(y)
                enemy_laser_list.append(y)
                enemy_laser_noise.play()
            elif enemy_num == 2:
                x = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 10), 44, 5)
                all_sprites_list.add(x)
                enemy_laser_list.append(x)
                y = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 5), 44, 5)
                all_sprites_list.add(y)
                enemy_laser_list.append(y)
                z = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2), 44, 5)
                all_sprites_list.add(z)
                enemy_laser_list.append(z)
                enemy_laser_noise.play()
            elif enemy_num == 3:
                w = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 15), 44, 5)
                all_sprites_list.add(w)
                enemy_laser_list.append(w)
                x = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 10), 44, 5)
                all_sprites_list.add(x)
                enemy_laser_list.append(x)
                y = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 10), 44, 5)
                all_sprites_list.add(y)
                enemy_laser_list.append(y)
                z = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 15), 44, 5)
                all_sprites_list.add(z)
                enemy_laser_list.append(z)
                enemy_laser_noise.play()
            elif enemy_num == 4:
                t = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 30), 44, 5)
                all_sprites_list.add(t)
                enemy_laser_list.append(t)
                u = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 25), 44, 5)
                all_sprites_list.add(u)
                enemy_laser_list.append(u)
                v = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 5), 44, 5)
                all_sprites_list.add(v)
                enemy_laser_list.append(v)
                w = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2), 44, 5)
                all_sprites_list.add(w)
                enemy_laser_list.append(w)
                x = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 5), 44, 5)
                all_sprites_list.add(x)
                enemy_laser_list.append(x)
                y = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 25), 44, 5)
                all_sprites_list.add(y)
                enemy_laser_list.append(y)
                z = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 30), 44, 5)
                all_sprites_list.add(z)
                enemy_laser_list.append(z)
                enemy_laser_noise.play()
            elif enemy_num == 5:
                t = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 60), 44, 5)
                all_sprites_list.add(t)
                enemy_laser_list.append(t)
                u = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 55), 44, 5)
                all_sprites_list.add(u)
                enemy_laser_list.append(u)
                v = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 - 5), 44, 5)
                all_sprites_list.add(v)
                enemy_laser_list.append(v)
                w = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2), 44, 5)
                all_sprites_list.add(w)
                enemy_laser_list.append(w)
                x = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 5), 44, 5)
                all_sprites_list.add(x)
                enemy_laser_list.append(x)
                y = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 55), 44, 5)
                all_sprites_list.add(y)
                enemy_laser_list.append(y)
                z = EnemyLaser(enemy_list[enemy_num].rect.x + 20,
                               (enemy_list[enemy_num].rect.y + enemy_list[enemy_num].height / 2 + 60), 44, 5)
                all_sprites_list.add(z)
                enemy_laser_list.append(z)
                enemy_laser_noise.play()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                spaceship.MoveKeyDown(event.key)
            elif event.type == pygame.KEYUP:
                spaceship.MoveKeyUp(event.key)

        for ent in all_sprites_list:
            ent.update()

        for laser in laser_list:  # checks if lasers have left the screen
            if laser.rect.x > 900:
                laser.remove(all_sprites_list)
                laser_list.remove(laser)

        for asteroid in asteroid_list:#checks if asteroids have left the screen
            if asteroid.rect.x<=0:
                asteroid.remove(all_sprites_list)
                asteroid_list.remove(asteroid)

        if enemy_lives == 1 and enemyImgadd:
            if enemyImg_num!=11:
                enemyImg_num += 1
                enemy_list[enemy_num].image = enemyImg_list[enemyImg_num]
                enemyImgadd = False
            else:
                enemyImg_num=2
        if enemy_lives <= 0:
            enemies -=1
        if lives <= 0 or enemies == 0:# if they die it displays highscores from a text file and waits for a click to restart
            if enemies==0 or (lives<=0 and asteroids==True):
                current_level+=1
            if current_level==9:
                current_level=1
            if lives<=0 and asteroids==False:
                total_lives-=1
            if total_lives<=0:
                end_game_screen()
                return
            if enemies==0:
                enemy_list[enemy_num].remove(all_sprites_list)
                big_explosion.play()
            if lives<=0:
                lives_lost+=1
                lose_noise.play()
            stage_added=False
            end_screen = True
            next_screen = False
            mouseClicked = False
            while (end_screen):
                for laser in laser_list:
                    if isinstance(laser, Laser):
                        laser.remove(all_sprites_list)
                laser_list=[]
                for elaser in enemy_laser_list:
                    if isinstance(elaser, EnemyLaser):
                        elaser.remove(all_sprites_list)
                enemy_laser_list=[]
                screen.fill((0, 0, 0))
                screen.blit(bgImg, (bg_x, bg_y))
                screen.blit(bgImg, (bg_x1 - 5, bg_y1 - 5))
                font4 = pygame.font.SysFont("arialblack", 28)
                font5 = pygame.font.SysFont("arialblack", 28)
                speed_upgrade = font4.render("Upgrade Speed:2000 POINTS", True, (WHITE))
                current_speed = font4.render(("Current Speed: "+str(speed)), True, (WHITE))
                buy_shields = font4.render("Buy Lives:1500 POINTS", True, (WHITE))
                current_shields = font4.render(("Current Lives: "+str(shields)), True, (WHITE))
                buy_bombs = font4.render("Buy Bombs:300 POINTS", True, (WHITE))
                current_bombs = font4.render(("Current Bombs: "+str(bombs)), True, (WHITE))
                bomb_instruction = font4.render("Press X to use", True, (WHITE))
                buy_multi_lasers = font4.render("Buy Multi-Lasers:300 POINTS", True, (WHITE))
                current_multi_lasers = font4.render(("Current Multi-Lasers: "+str(multilasers)), True, (WHITE))
                multi_laser_instruction = font4.render("Press Z to use", True, (WHITE))
                current_points = font5.render("POINTS: "+str(score), True, (WHITE))
                deaths = font5.render("DEATHS LEFT: "+str(total_lives), True, (WHITE))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:  # checks if mouse is released
                        mousex, mousey = event.pos
                        mouseClicked = True

                screen.blit(speed_upgrade, (0, 0))
                screen.blit(speed_symbol, (450, 10))
                screen.blit(current_speed, (0, 35))
                screen.blit(buy_shields, (0, 125))
                screen.blit(shield_symbol, (450, 155))
                screen.blit(current_shields, (0, 160))
                screen.blit(buy_bombs, (0, 310))
                screen.blit(bomb_symbol, (450, 340))
                screen.blit(current_bombs, (0, 345))
                screen.blit(bomb_instruction, (0, 380))
                screen.blit(buy_multi_lasers, (0, 495))
                screen.blit(speed_up, (450, 525))
                screen.blit(current_multi_lasers, (0, 530))
                screen.blit(multi_laser_instruction, (0, 565))
                screen.blit(current_points, (600, 10))
                screen.blit(deaths, (600, 40))
                screen.blit(next_button, (750, 500))
                if mouseClicked:
                    if mousex>450 and mousex<522 and mousey>10 and mousey<82:
                        if score>=2000:
                            spaceship.y_dist=speed+1
                            speed+=1
                            score-=2000
                        mouseClicked=False
                    elif mousex>450 and mousex<537 and mousey>155 and mousey<242:
                        if score>=1500:
                            shields+=1
                            score-=1500
                        mouseClicked=False
                    elif mousex>450 and mousex<540 and mousey>340 and mousey<430:
                        if score>=300:
                            bombs+=1
                            score-=300
                        mouseClicked=False
                    elif mousex>450 and mousex<531 and mousey>525 and mousey<573:
                        if score>=300:
                            multilasers+=1
                            score-=300
                        mouseClicked=False
                    if (math.sqrt((mousex-795)**2+(mousey-545)**2))<45:
                        just_asteroid=False
                        if enemies == 0:
                            if enemy_num==1 or enemy_num==3:
                                asteroids=True
                            if asteroids==False:
                                enemyImg_num += 1
                                if enemyImg_num%2==1:
                                    enemyImg_num+=1
                                if enemyImg_num == 12:
                                    if shoot_speed>=10:
                                        shoot_speed -= 5
                                    enemy_list[enemy_num].y_change+=1
                                    enemyImg_num = 0
                                enemy_num += 1
                                if enemy_num == 6:
                                    enemy_num = 0
                                all_sprites_list.add(enemy_list[enemy_num])
                                enemy_list[enemy_num].image = enemyImg_list[enemyImg_num]
                        elif lives <= 0:
                            if asteroids:
                                asteroids=False
                                just_asteroid=True
                                for asteroid in asteroid_list:
                                    if isinstance(asteroid, Asteroid):
                                        asteroid.remove(all_sprites_list)
                                asteroid_list=[]
                                enemyImg_num += 1
                                if enemyImg_num == 12:
                                    if shoot_speed>=10:
                                        shoot_speed -= 5
                                    enemyImg_num = 0
                                enemy_num += 1
                                if enemy_num == 6:
                                    enemy_num = 0
                                all_sprites_list.add(enemy_list[enemy_num])
                                enemy_list[enemy_num].image = enemyImg_list[enemyImg_num]
                            if enemyImg_num%2 == 1:
                                enemyImg_num -= 1
                                enemy_list[enemy_num].image = enemyImg_list[enemyImg_num]
                        end_screen=False
                        next_screen=True
                pygame.display.flip()
            while(next_screen):
                screen.fill((0, 0, 0))
                screen.blit(bgImg, (bg_x, bg_y))
                screen.blit(bgImg, (bg_x1 - 5, bg_y1 - 5))
                font4 = pygame.font.SysFont("arialblack", 35)
                game_finish=font4.render("You Finished The Game!!", True, (WHITE))
                game_finish2=font4.render("Click To Restart", True, (WHITE))
                click_continue=font4.render("Click to Continue", True, (WHITE))
                if stage!=6:
                    next_stage1=font4.render("Congrats on finishing the stage!", True, (WHITE))
                    next_stage2=font4.render("The next stage will have the same", True, (WHITE))
                    next_stage4 = font4.render("enemies but they shoot and move faster", True, (WHITE))
                    next_stage3=font4.render("You also get a new ship", True, (WHITE))
                if enemies==0 or just_asteroid:
                    pass_fail = font4.render("You finished the level!", True, (WHITE))
                    if asteroids:
                        level_descrip = font4.render("The next level is an asteroid field.", True, (WHITE))
                        level_descrip2 = font4.render("Shoot asteroids to get as many points", True, (WHITE))
                        level_descrip3 = font4.render("as possible until you die", True, (WHITE))
                    else:
                        level_descrip = font4.render("The next level is a harder enemy.", True, (WHITE))
                elif lives <=0:
                    pass_fail = font4.render("You failed the level!", True, (WHITE))
                    level_descrip = font4.render("Try Again", True, (WHITE))
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONUP:# checks if mouse is released
                        if stage!=7:
                            asteroid_speed=stage+4
                            spaceship.rect.y = window_height / 2
                            if asteroids==False:
                                enemy_list[enemy_num].rect.y = window_height / 2
                            spaceship.y_change = 0
                            lives = shields
                            enemies = 1
                            enemy_lives=stage+4
                            enemyImgadd = True
                            start_game()
                        else:
                            pygame.quit()
                            sys.exit()
                if enemy_num==0 and enemies==0 and stage!=6:
                    if stage_added==False:
                        stage+=1
                        stage_added=True
                        all_sprites_list.remove(spaceship)
                        spaceship_num+=1
                        spaceshipImg_num+=1
                        spaceship=spaceship_list[spaceship_num]
                        spaceship.image=spaceshipImg_list[spaceshipImg_num]
                        all_sprites_list.add(spaceship)
                        next_level=font4.render("Next Level: Stage "+str(stage)+", Level "+str(current_level), True, (WHITE))
                    screen.blit(next_stage1, (0,0))
                    screen.blit(next_stage2, (0,100))
                    screen.blit(next_stage4, (0,140))
                    screen.blit(next_stage3, (0,200))
                    screen.blit(next_level, (0, 300))
                    screen.blit(click_continue, (0, 400))
                elif enemy_num==0 and enemies==0 and stage==6:
                    end_game_screen()
                    return
                else:
                    next_level=font4.render("Next Level: Stage "+str(stage)+", Level "+str(current_level), True, (WHITE))
                    screen.blit(pass_fail, (0, 0))
                    screen.blit(level_descrip, (0, 100))
                    if asteroids:
                        screen.blit(level_descrip2, (0, 150))
                        screen.blit(level_descrip3, (0, 190))
                    screen.blit(next_level, (0, 300))
                    screen.blit(click_continue, (0, 400))
                pygame.display.flip()

        screen.fill((0, 0, 0))
        bg_x1 -= 5
        bg_x -= 5
        screen.blit(bgImg, (bg_x, bg_y))
        screen.blit(bgImg, (bg_x1 - 5, bg_y1 - 5))
        if bg_x <= -bg_w:
            bg_x = bg_w
        if bg_x1 <= -bg_w:
            bg_x1 = bg_w

        text1 = update_score()
        screen.blit(text1, (600, 25))

        text2 = update_lives()
        screen.blit(text2, (400, 25))

        text3 = update_e_lives()
        screen.blit(text3, (100, 25))

        all_sprites_list.draw(screen)

        pygame.display.flip()

        clock.tick(60)

def init_game():
    pygame.init()

    global total_lives
    total_lives=1

    global current_level
    current_level=1

    global lives_lost
    lives_lost=0

    global just_shoot
    just_shoot=False

    global allow_shoot
    allow_shoot=0

    global just_asteroid
    just_asteroid=False

    global stage_added
    stage_added=False

    global background
    background = (0, 0, 0)

    global lives
    lives = 3

    global score
    score = 0

    global asteroid_limit
    asteroid_limit = 5

    global laser_list
    laser_list = []  # list for all flying objects

    global enemy_laser_list
    enemy_laser_list = []

    global asteroid_list
    asteroid_list = []

    global bonus_list
    bonus_list = []

    global asteroid_speed
    asteroid_speed = 5

    global extra_lasers
    extra_lasers = 0

    global score_display
    score_display = False

    global laser_count
    laser_count = 0

    global entity_color
    entity_color = (255, 255, 255)
    global WHITE
    WHITE = (255, 255, 255)

    global POINTS1
    POINTS1 = 0
    global POINTS2
    POINTS2 = 0

    global window_width
    window_width = 900
    global window_height
    window_height = 600

    global bonus_count
    bonus_count = 0  # counts time so the bonuses and walls come at intervals
    global wall_count
    wall_count = 0

    global shop_screen
    shop_screen = False

    global start_screen
    start_screen = False

    global speed
    speed = 6

    global enemy_lives
    enemy_lives = 3

    global level
    level = 1

    global enemies
    enemies = 1

    global shoot_speed
    shoot_speed = 40

    global enemy_list
    enemy_list = []

    global enemy_num
    enemy_num = 0

    global enemyImg_num
    enemyImg_num = 0

    global bgImg
    bgImg = pygame.image.load("space_background2.jpg")  # loads all files
    global bg_size, bg_rect
    bg_size = bgImg.get_size()
    bg_rect = bgImg.get_rect()
    global bg_w
    global bg_h
    bg_w, bg_h = bg_size
    global bg_x
    bg_x = 0
    global bg_y
    bg_y = 0
    global bg_x1
    bg_x1 = -bg_w
    global bg_y1
    bg_y1 = 0
    global enemyImgadd
    enemyImgadd = True

    global shields
    shields=3

    global bombs
    bombs=0

    global multilasers
    multilasers=0

    global stage
    stage=1

    global asteroids
    asteroids=False

    shooterImg = pygame.image.load("spaceship.png")

    global enemy1Img
    global enemy2Img
    global enemy3Img
    global enemy4Img
    global enemy5Img
    global enemy6Img
    enemy1Img = pygame.image.load("Enemy 1.png")
    enemy2Img = pygame.image.load("Enemy 2.png")
    enemy3Img = pygame.image.load("Enemy 3.png")
    enemy4Img = pygame.image.load("Enemy 4.png")
    enemy5Img = pygame.image.load("Enemy 5.png")
    enemy6Img = pygame.image.load("Enemy 6.png")
    global enemydmg1Img
    global enemydmg2Img
    global enemydmg3Img
    global enemydmg4Img
    global enemydmg5Img
    global enemydmg6Img
    
    enemydmg1Img = pygame.image.load("EnemyDmg 1.png")
    enemydmg2Img = pygame.image.load("EnemyDmg 2.png")
    enemydmg3Img = pygame.image.load("EnemyDmg 3.png")
    enemydmg4Img = pygame.image.load("EnemyDmg 4.png")
    enemydmg5Img = pygame.image.load("EnemyDmg 5.png")
    enemydmg6Img = pygame.image.load("EnemyDmg 6.png")

    global spaceship1Img
    global spaceship2Img
    global spaceship3Img
    global spaceship4Img
    global spaceship5Img
    global spaceship6Img
    
    spaceship1Img=pygame.image.load("spaceship1.png")
    spaceship2Img=pygame.image.load("spaceship2.png")
    spaceship3Img=pygame.image.load("spaceship3.png")
    spaceship4Img=pygame.image.load("spaceship4.png")
    spaceship5Img=pygame.image.load("spaceship5.png")
    spaceship6Img=pygame.image.load("spaceship6.png")

    global spaceshipImg_num
    spaceshipImg_num=0

    global spaceship_num
    spaceship_num=0

    global spaceshipImg_list
    spaceshipImg_list = [spaceship1Img, spaceship2Img, spaceship3Img, spaceship4Img, spaceship5Img, spaceship6Img]

    global enemyImg_list
    enemyImg_list = [enemy1Img, enemydmg1Img, enemy2Img, enemydmg2Img, enemy3Img, enemydmg3Img, enemy4Img, enemydmg4Img,
                     enemy5Img, enemydmg5Img, enemy6Img, enemydmg6Img]


    global asteroidImg, laserImg, enemylaserImg, bomb_symbol,shield_symbol,shield_symbol,speed_up,next_button
    global enemy_laser_noise, laser_noise, explosion_noise
    asteroidImg = pygame.image.load("Asteroid.png")
    global speed_upImg
    speed_upImg = pygame.image.load("speed_up.png")

    laserImg = pygame.image.load("laser.png")
    enemylaserImg = pygame.image.load("enemylaser.gif")

    bomb_symbol = pygame.image.load("bomb_symbol2.png")
    shield_symbol = pygame.image.load("shield_symbol.png")
    shield_symbol = pygame.image.load("speed_symbol.png")
    speed_up = pygame.image.load("speed_up.png")
    next_button = pygame.image.load("next_button.png")


    pygame.mixer.music.load("DarkKnight.mp3")
    pygame.mixer.music.set_volume(0.5)#sets the background music volume
    pygame.mixer.music.play(-1, 0.0)

    global lose_noise, big_explosion, asteroid_explosion
    lose_noise=pygame.mixer.Sound("SHUTDOWN.wav")
    lose_noise.set_volume(5)
    explosion_noise = pygame.mixer.Sound("explosion.wav")
    big_explosion = pygame.mixer.Sound("big_explosion.wav")
    asteroid_explosion = pygame.mixer.Sound("export.wav")
    laser_noise = pygame.mixer.Sound("pew_pew.wav")
    enemy_laser_noise = pygame.mixer.Sound("enemy_laser_sound.wav")

    spaceship1 = Player(15, window_height/2, 106, 113)
    spaceship2 = Player(15, window_height/2, 122, 92)
    spaceship3 = Player(15, window_height/2, 99, 124)
    spaceship4 = Player(15, window_height/2, 98, 127)
    spaceship5 = Player(15, window_height/2, 111, 90)
    spaceship6 = Player(15, window_height/2, 118, 85)

    global spaceship
    spaceship=spaceship1

    spaceship_list=[spaceship1, spaceship2, spaceship3, spaceship4, spaceship5, spaceship6]
    enemy1 = Enemy(770, window_height / 2, 120, 96)
    enemy2 = Enemy(735, window_height / 2, 155, 68)
    enemy3 = Enemy(755, window_height / 2, 123, 82)
    enemy4 = Enemy(755, window_height / 2, 123, 86)
    enemy5 = Enemy(785, window_height / 2, 94, 129)
    enemy6 = Enemy(785, window_height / 2, 91, 170)

    
    enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]

    global screen
    screen = pygame.display.set_mode((window_width, window_height))

    pygame.display.set_caption("Asteroids")

    global clock
    clock = pygame.time.Clock()

    global all_sprites_list
    all_sprites_list = pygame.sprite.Group()
    all_sprites_list.add(spaceship)
    all_sprites_list.add(enemy1)

    start_screen = True

    while (start_screen):  # start screen, runs until they click, displays controls and runs pygame event loop to check for click
        screen.fill((0, 0, 0))
        screen.blit(bgImg, (0, 0))
        font1 = pygame.font.SysFont("arialblack", 75)
        title = font1.render("Space Fight", True, (WHITE))
        font2 = pygame.font.SysFont("arialblack", 27)
        objective1 = font2.render("OBJECTIVE: ", True, (WHITE))
        objective2 = font2.render("There are 5 stages", True, (WHITE))
        objective3 = font2.render("Each stage has 6 enemies and 2 asteroid fields", True, (WHITE))
        objective4 = font2.render("Get as far as you can with 5 lives", True, (WHITE))
        control1 = font2.render("INSTRUCTIONS:", True, (WHITE))
        control2 = font2.render("ARROW KEYS -- MOVE UP & DOWN", True, (WHITE))
        control3 = font2.render("SPACEBAR -- SHOOT NORMAL LASER", True, (WHITE))
        control4 = font2.render("Z -- SHOOT MULTI-LASER", True, (WHITE))
        instruction1 = font2.render("X -- USE BOMB(CLEAR SCREEN)", True, (WHITE))
        click_start = font2.render("CLICK TO START", True, (WHITE))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    start_screen = False
        screen.blit(title, (200, 25))
        screen.blit(objective1, (150, 150))
        screen.blit(objective2, (150, 195))
        screen.blit(objective3, (150, 240))
        screen.blit(objective4, (150, 285))
        screen.blit(control1, (150, 330))
        screen.blit(control2, (150, 375))
        screen.blit(control3, (150, 420))
        screen.blit(control4, (150, 465))
        screen.blit(instruction1, (150, 510))
        screen.blit(click_start, (150, 555))
        pygame.display.flip()

global screen
global clock

    
while True:
    init_game()
    start_game()
