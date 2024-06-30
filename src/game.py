import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pong")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Game objects
class Ball:
    def __init__(self):
        self.x = 400
        self.y = 300
        self.radius = 10
        self.speed_x = 5
        self.speed_y = 5

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y
        # Bounce off walls
        if self.x + self.radius > 800 or self.x - self.radius < 0:
            self.speed_x *= -1
        if self.y + self.radius > 600 or self.y - self.radius < 0:
            self.speed_y *= -1

class Paddle:
    def __init__(self, x, y):
        self.width = 10
        self.height = 100
        self.speed = 5
        self.x = x
        self.y = y

    def move(self, up=True):
        if up:
            self.y -= self.speed
        else:
            self.y += self.speed
        # Keep paddle within bounds
        self.y = max(0, min(600 - self.height, self.y))

# Game loop
def main():
    clock = pygame.time.Clock()
    ball = Ball()
    paddle_a = Paddle(0, 300)
    paddle_b = Paddle(790, 300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddle_a.move(up=True)
        if keys[pygame.K_s]:
            paddle_a.move(up=False)
        if keys[pygame.K_UP]:
            paddle_b.move(up=True)
        if keys[pygame.K_DOWN]:
            paddle_b.move(up=False)

        ball.move()

        # Check collision with paddles
        if ball.x - ball.radius <= paddle_a.x + paddle_a.width and \
           paddle_a.y <= ball.y <= paddle_a.y + paddle_a.height:
            ball.speed_x *= -1
        elif ball.x + ball.radius >= paddle_b.x and \
             paddle_b.y <= ball.y <= paddle_b.y + paddle_b.height:
            ball.speed_x *= -1

        # Draw everything
        screen.fill(BLACK)
        pygame.draw.circle(screen, WHITE, (ball.x, ball.y), ball.radius)
        pygame.draw.rect(screen, WHITE, pygame.Rect(paddle_a.x, paddle_a.y, paddle_a.width, paddle_a.height))
        pygame.draw.rect(screen, WHITE, pygame.Rect(paddle_b.x, paddle_b.y, paddle_b.width, paddle_b.height))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
