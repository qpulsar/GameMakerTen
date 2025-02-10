import pygame
from core.ui_elements import Button


class MainMenu:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.width, self.height = pygame.display.get_surface().get_size()
        self.font = pygame.font.Font(None, 60)
        self.title_text = self.font.render("Game Maker", True, (255, 255, 255))
        self.text_x = (self.width - self.title_text.get_width()) // 2
        self.text_y = self.height // 5

        # Menü Butonları
        self.create_game_button = Button(self.width // 2 - 100, self.height // 2, 200, 50, "Oyun Oluştur")
        self.quit_button = Button(self.width // 2 - 100, self.height // 2 + 70, 200, 50, "Çıkış")

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.create_game_button.is_hovered():
                from screens.game_editor import GameEditor
                self.screen_manager.set_screen(GameEditor(self.screen_manager))
            elif self.quit_button.is_hovered():
                pygame.quit()
                exit()

    def update(self):
        self.create_game_button.update()
        self.quit_button.update()

    def draw(self, screen):
        screen.fill((50, 50, 50))
        screen.blit(self.title_text, (self.text_x, self.text_y))
        self.create_game_button.draw(screen)
        self.quit_button.draw(screen)
