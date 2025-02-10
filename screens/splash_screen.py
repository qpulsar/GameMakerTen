import pygame
import random
import time


class SplashScreen:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.start_time = time.time()
        self.font = pygame.font.Font(None, 80)
        self.width, self.height = pygame.display.get_surface().get_size()
        self.title_text = self.font.render("Game Maker", True, (255, 255, 255))
        self.text_x = (self.width - self.title_text.get_width()) // 2
        self.text_y = self.height // 3
        self.particles = []

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN or time.time() - self.start_time > 3:
            from screens.main_menu import MainMenu
            self.screen_manager.set_screen(MainMenu(self.screen_manager))

    def update(self):
        self.particles.append([
            random.randint(0, self.width), self.height, random.choice([(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        ])
        for p in self.particles:
            p[1] -= random.randint(2, 5)
        self.particles = [p for p in self.particles if p[1] > 0]

    def draw(self, screen):
        screen.fill((30, 30, 30))
        screen.blit(self.title_text, (self.text_x, self.text_y))

        for p in self.particles:
            pygame.draw.circle(screen, p[2], (p[0], p[1]), 5)