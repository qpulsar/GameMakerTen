import pygame
from config.settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from core.screen_manager import ScreenManager
from screens.splash_screen import SplashScreen


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Maker")
    clock = pygame.time.Clock()

    # Ekran yöneticisini oluştur ve açılış ekranını başlat
    screen_manager = ScreenManager()
    screen_manager.set_screen(SplashScreen(screen_manager))

    running = True
    while running:
        screen.fill((0, 0, 0))  # Arka plan rengini siyah yap

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Şu anki ekrana olayları ilet
            screen_manager.handle_events(event)

        # Ekranı güncelle
        screen_manager.update()
        screen_manager.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()