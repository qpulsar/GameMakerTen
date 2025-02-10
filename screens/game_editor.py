import pygame
from core.ui_elements import Button
from core.question_popup import QuestionPopup

from core.ui_elements import Button

class GameEditor:
    def __init__(self, screen_manager):
        self.screen_manager = screen_manager
        self.width, self.height = pygame.display.get_surface().get_size()

        # Başlık Fontu
        self.font = pygame.font.Font(None, 50)
        self.title_text = self.font.render("Oyun Tasarım Editörü", True, (255, 255, 255))
        self.text_x = (self.width - self.title_text.get_width()) // 2
        self.text_y = 20

        # Araç Kutusu (Sol Panel)
        self.toolbox_width = 200
        self.toolbox_buttons = [
            Button(20, 100, 160, 40, "Soru Ekle"),
            Button(20, 160, 160, 40, "Şık Ekle"),
            Button(20, 220, 160, 40, "Doğru Cevap"),
            Button(20, 280, 160, 40, "Zorluk Seç"),
            Button(20, 340, 160, 40, "Kaydet")
        ]

        # Çalışma Alanı (Sağ Panel)
        self.workspace_rect = pygame.Rect(self.toolbox_width + 20, 80, self.width - self.toolbox_width - 40,
                                          self.height - 100)

        # Soru Ekleme Popup
        self.question_popup = QuestionPopup(pygame.display.get_surface())

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.toolbox_buttons:
                if button.is_hovered():
                    if button.text == "Soru Ekle":
                        self.question_popup.open()
                    else:
                        print(f"{button.text} butonuna tıklandı")

        # Popup içindeki olayları yakala
        self.question_popup.handle_events(event)

    def update(self):
        for button in self.toolbox_buttons:
            button.update()

    def draw(self, screen):
        screen.fill((40, 40, 40))
        screen.blit(self.title_text, (self.text_x, self.text_y))

        # Araç Kutusu
        pygame.draw.rect(screen, (60, 60, 60), (0, 80, self.toolbox_width, self.height - 80))
        for button in self.toolbox_buttons:
            button.draw(screen)

        # Çalışma Alanı
        pygame.draw.rect(screen, (30, 30, 30), self.workspace_rect, border_radius=10)

        # Soru Ekleme Popup'ı Çiz
        self.question_popup.draw()
