import sys
import pygame


SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class Block:
    def __init__(self, pos, mass, speed, color):
        self.pos = list(pos)
        self.mass = mass
        self.speed = speed
        self.color = tuple(color)

    def move(self):
        self.pos[0] += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.pos)


class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("PI calculator")
        self.font = pygame.font.SysFont("Arial", 24)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.collisions = 0
        self.sb = Block((SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT - 100, 100, 100), 1, 0, (0, 255, 155))
        self.bb = Block((SCREEN_WIDTH - 200, SCREEN_HEIGHT - 200, 200, 200), 100**1, -1, (0, 155, 255))
        self.main()

    def main(self):
        while True:
            self.handle_events()
            self.move()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)

    def move(self):
        self.sb.move()
        self.bb.move()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.sb.draw(self.screen)
        self.bb.draw(self.screen)
        text = self.font.render(f"Collisions: {self.collisions}", True, (0, 255, 255))
        self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, 0))
        pygame.display.flip()


if __name__ == "__main__":
    Main()
