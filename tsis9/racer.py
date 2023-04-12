import random

import pygame

pygame.init()
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 40
WHITE = (255, 255, 255)
SCORE = 0
clock = pygame.time.Clock()
background = pygame.image.load('AnimatedStreet.png')
score_font = pygame.font.SysFont("Verdana", 30)
#

class Coin(pygame.sprite.Sprite): #coin class. it works and I am scared to touch it
    def __init__(self):
        super().__init__()
        self.x = random.randint(20, WIDTH-20)
        self.image = pygame.Rect(self.x , HEIGHT - 50, 1, 1)
        self.rect = self.image
        self.rect.center = (self.x, HEIGHT - 50)
    def draw(self):
        pygame.draw.circle(SCREEN, 'yellow', center=(self.x, HEIGHT-50), radius=15)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.image = pygame.image.load('Enemy.png')
        self.rect = self.image.get_rect()
        self.rect.center = (
            random.randint(self.rect.width, WIDTH - self.rect.width),
            0,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.y > HEIGHT:
            SCORE += 1
            self.speed += 1
            self.rect.center = (
                random.randint(self.rect.width, WIDTH - self.rect.width),
                0,
            )


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 5
        self.image = pygame.image.load('Player.png')
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - self.rect.height // 2 - 20)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def update(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LEFT] and self.rect.x - self.speed >= 0:
            self.rect.move_ip(-self.speed, 0)
        elif pressed[pygame.K_RIGHT] and self.rect.x + self.speed + self.rect.width <= WIDTH:
            self.rect.move_ip(self.speed, 0)


def main():
    running = True
    player = Player()
    enemy = Enemy()
    enemies = pygame.sprite.Group()
    enemies.add(enemy)
    coin = Coin()#coins
    coins = pygame.sprite.Group()
    coins.add(coin)
    cnt = 0

    while running:
        # SCREEN.fill(WHITE)
        SCREEN.blit(background, (0, 0))
        score = score_font.render(f" Your score: {SCORE}", True, (0, 0, 0))
        SCREEN.blit(score, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        player.update()
        enemy.update()
        coin.draw()
        player.draw(SCREEN)
        enemy.draw(SCREEN)

        if pygame.sprite.spritecollideany(player, enemies):
            running = False
        if pygame.sprite.spritecollideany(player, coins):
            num = random.randint(1,3) #random weight of a coin for count (?)
            cnt += num # i decided not to write it on screen, because there is already a score
            coins.remove(coin)
            coin = Coin()
            coins.add(coin)
            coin.draw()
            enemy.speed += 1 #increasing speed each time coin got pick up
        pygame.display.flip()
        clock.tick(60)

    print("coins collected", cnt)
if __name__ == '__main__':
    main()