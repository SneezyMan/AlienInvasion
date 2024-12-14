import sys
import pygame

class AlienInvasion:
    """Overall class to manage the game assets and behaviour."""

    def __init__(self):
        """Initialize the game, and crate game resources."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Start the main loop and mouse events."""
        while True:
            # Watch for keyboard and mouse events.
            for even in pygame.event.get():
                if even.type == pygame.QUIT:
                    sys.exit()

            # Make the most recently drawn screen visible.
            pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
        