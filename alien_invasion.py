import sys
from settings import Settings
import pygame

class AlienInvasion:
    """Overall class to manage the game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and crate game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop and mouse events."""
        while True:
            # Watch for keyboard and mouse events.
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit()

            # Redraw the screen during each pass through the loop.
            self.screen.fill(self.settings.bg_color)

            # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
        