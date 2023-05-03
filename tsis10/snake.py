import random
import time
import pygame
import psycopg2
from config import host, user, password, db_name

pygame.init()
WIDTH, HEIGHT = 400, 400
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLOCK_SIZE = 20
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
AQUA = (0, 255, 255)
clock = pygame.time.Clock()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class TimedFood: #class for timed food
    def __init__ (self, x, y):
        self.location = Point(x,y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            AQUA,
            pygame.Rect(
            self.location.x * BLOCK_SIZE,
            self.location.y * BLOCK_SIZE,
            BLOCK_SIZE,
            BLOCK_SIZE
            )
        )

class BadFood:
    def __init__(self, x, y):
        self.location = Point(x,y)
    
    def draw(self):
        pygame.draw.rect(
            SCREEN,
            YELLOW,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE
                )
        )

class Wall: #class for walls
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            WHITE,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )  

class Snake:
    def __init__(self):
        self.body = [
            Point(
                x=WIDTH // BLOCK_SIZE // 2,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
            Point(
                x=WIDTH // BLOCK_SIZE // 2 + 1,
                y=HEIGHT // BLOCK_SIZE // 2,
            ),
        ]

    def draw(self):
        head = self.body[0]
        pygame.draw.rect(
            SCREEN,
            RED,
            pygame.Rect(
                head.x * BLOCK_SIZE,
                head.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
        for body in self.body[1:]:
            pygame.draw.rect(
                SCREEN,
                BLUE,
                pygame.Rect(
                    body.x * BLOCK_SIZE,
                    body.y * BLOCK_SIZE,
                    BLOCK_SIZE,
                    BLOCK_SIZE,
                )
            )

    def move(self, dx, dy):
        for idx in range(len(self.body) - 1, 0, -1):
            self.body[idx].x = self.body[idx - 1].x
            self.body[idx].y = self.body[idx - 1].y
        # [Point(0, 1), Point(2, 5), Point(5, 9)]
        # [Point(0, 0), Point(0, 1), Point(2, 5)]
        self.body[0].x += dx
        self.body[0].y += dy

        if self.body[0].x > WIDTH // BLOCK_SIZE:
            self.body[0].x = 0
        elif self.body[0].x < 0:
            self.body[0].x = WIDTH // BLOCK_SIZE
        elif self.body[0].y < 0:
            self.body[0].y = WIDTH // BLOCK_SIZE
        elif self.body[0].y > HEIGHT // BLOCK_SIZE:
            self.body[0].y = 0

    def check_collision(self, food):
        if food.location.x != self.body[0].x:
            return False
        if food.location.y != self.body[0].y:
            return False
        return True
    
    def check_game_over(self): #if snake eats itself
        for idx in range(1,len(self.body[1:])):
            if (self.body[0].x, self.body[0].y) == (self.body[idx].x,self.body[idx].y):
                return True
        return False

def draw_grid():
    for x in range(0, WIDTH, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(x, 0), end_pos=(x, HEIGHT), width=1)
    for y in range(0, HEIGHT, BLOCK_SIZE):
        pygame.draw.line(SCREEN, WHITE, start_pos=(0, y), end_pos=(WIDTH, y), width=1)


class Food:
    def __init__(self, x, y):
        self.location = Point(x, y)

    def draw(self):
        pygame.draw.rect(
            SCREEN,
            GREEN,
            pygame.Rect(
                self.location.x * BLOCK_SIZE,
                self.location.y * BLOCK_SIZE,
                BLOCK_SIZE,
                BLOCK_SIZE,
            )
        )
def main():
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
    )
        cursor = connection.cursor()
        connection.autocommit = True
        name = input("type your name")
        cursor.execute("SELECT username, user_score, user_level from users WHERE EXISTS (SELECT 1 FROM users WHERE username = '" + name + "')" )
        a = cursor.fetchone()
        if a is None:
            cursor.execute("INSERT INTO users(username, user_score, user_level) VALUES('" + name + "', 0 , 1)")
        else:
            cursor.execute("SELECT user_level FROM users WHERE username = '" + name + "'")
            print(cursor.fetchone())
        timed = 0
        level = 1
        score = 0
        speed = 3
        running = True
        timedfood = TimedFood(7,7)
        wall = Wall(3,4)
        snake = Snake()
        food = Food(5, 5)
        badfood = BadFood(3,3)
        dx, dy = 0, 0
        font = pygame.font.Font(None, 70)

        walls = []
        for i in range(random.randint(0,0)):
            x = random.randint(1,20)
            y = random.randint(1,20) 
            walls.append(Point(x,y))
    
        while running:
            SCREEN.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        dx, dy = 0, -1
                    elif event.key == pygame.K_DOWN:
                        dx, dy = 0, +1
                    elif event.key == pygame.K_RIGHT:
                        dx, dy = 1, 0
                    elif event.key == pygame.K_LEFT:
                        dx, dy = -1, 0
                    elif event.key == pygame.K_p:
                        filler = input("Type anything to continue")
                        cursor.execute("UPDATE users SET user_score = '" + str(score) + "' , user_level = '" + str(level) + "' WHERE username = '" + name + "'")
            snake.move(dx, dy)
            if snake.check_collision(timedfood): #eating timefood
                timed = 0
                snake.body.append(
                    Point(snake.body[-1].x , snake.body[-1].y)
                )
                timedfood.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                timedfood.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
            if timed == 15: #relocating timefood after 15 gameticks
                timedfood.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                timedfood.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                timed = 0
            timed += 1
            if snake.check_collision(food):
                pygame.mixer.music.load("android-10.mp3")
                pygame.mixer.music.play()
                num = random.randint(1,3)
                score += 1
                for idx in range(num):
                    snake.body.append(
                        Point(snake.body[-1].x, snake.body[-1].y)
                    )
                food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1)
                for idx in walls: #regenerating food if on wall
                    if food.location == idx:
                        while food.location != idx:
                            food.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                            food.location.y = random.randint(0, HEIGHT // BLOCK_SIZE - 1) 
            for i in walls: #drawing walls and checking colisions
                wall.location = i
                wall.draw()
                if snake.check_collision(wall):
                    running = False
            if snake.check_game_over():
                running = False
            timedfood.draw()
            snake.draw()
            food.draw()
            wall.draw()
            badfood.draw()
            draw_grid()
            if snake.check_collision(badfood):
                if len(snake.body) == 1:
                    SCREEN.fill((0,0,0))
                    font.render("GAME OVER. Your score : {score}", True, (255,0,0))
                    pygame.display.flip()
                    time.sleep(4)
                    pygame.quit()
                else:
                    pygame.mixer.music.load("sony-4_4.mp3")
                    pygame.mixer.music.play()    
                    snake.body.remove(snake.body[-1])
                    badfood.location.x = random.randint(0, WIDTH // BLOCK_SIZE - 1)
                    badfood.location.y = random.randint(0, HEIGHT//BLOCK_SIZE - 1)
            pygame.display.flip()
            if score == 4: #increasing speed each 4 score to max 8
                speed = 5
                level = 2
            if score == 8:
                speed = 8
                level = 3
            clock.tick(speed)
        print ("your score is", score) #displaying score at the end
    except Exception as _ex:
        print ("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print ("[INFO] PostgreSQL connection closed")
if __name__ == '__main__':
    main()