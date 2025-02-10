import pygame


class QuestionPopup:
    def __init__(self, screen):
        self.screen = screen
        self.width, self.height = 400, 350
        self.rect = pygame.Rect((screen.get_width() - self.width) // 2, (screen.get_height() - self.height) // 2,
                                self.width, self.height)
        self.font = pygame.font.Font(None, 30)
        self.active = False

        # Form Alanları
        self.question_text = ""
        self.choices = []
        self.correct_answer = 0
        self.choice_count = 2  # Başlangıçta 2 seçenek olacak

        self.input_active = [False] * (self.choice_count + 1)  # Soru ve seçenekler için

        # Butonlar
        self.save_button = pygame.Rect(self.rect.x + 50, self.rect.y + 300, 100, 40)
        self.cancel_button = pygame.Rect(self.rect.x + 250, self.rect.y + 300, 100, 40)
        self.up_button = pygame.Rect(self.rect.x + 320, self.rect.y + 50, 30, 30)
        self.down_button = pygame.Rect(self.rect.x + 320, self.rect.y + 90, 30, 30)

    def open(self):
        self.active = True
        self.choices = ["" for _ in range(self.choice_count)]
        self.input_active = [False] * (self.choice_count + 1)

    def close(self):
        self.active = False

    def handle_events(self, event):
        if not self.active:
            return

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.cancel_button.collidepoint(event.pos):
                self.close()
            elif self.save_button.collidepoint(event.pos):
                print("Soru Kaydedildi:", self.question_text, self.choices, self.correct_answer)
                self.close()
            elif self.up_button.collidepoint(event.pos):
                if self.choice_count < 6:
                    self.choice_count += 1
                    self.choices.append("")
            elif self.down_button.collidepoint(event.pos):
                if self.choice_count > 2:
                    self.choice_count -= 1
                    self.choices.pop()

            for i in range(self.choice_count + 1):
                input_rect = pygame.Rect(self.rect.x + 20, self.rect.y + 50 + i * 40, 280, 30)
                if input_rect.collidepoint(event.pos):
                    self.input_active = [False] * (self.choice_count + 1)
                    self.input_active[i] = True

        if event.type == pygame.KEYDOWN:
            for i in range(self.choice_count + 1):
                if self.input_active[i]:
                    if event.key == pygame.K_BACKSPACE:
                        if i == 0:
                            self.question_text = self.question_text[:-1]
                        else:
                            self.choices[i - 1] = self.choices[i - 1][:-1]
                    else:
                        if i == 0:
                            self.question_text += event.unicode
                        else:
                            self.choices[i - 1] += event.unicode

    def draw(self):
        if not self.active:
            return

        pygame.draw.rect(self.screen, (200, 200, 200), self.rect, border_radius=10)
        title = self.font.render("Soru Ekle", True, (0, 0, 0))
        self.screen.blit(title, (self.rect.x + 140, self.rect.y + 10))

        # Input Alanları
        labels = ["Soru:"] + [f"Seçenek {i + 1}:" for i in range(self.choice_count)]
        for i in range(self.choice_count + 1):
            input_rect = pygame.Rect(self.rect.x + 20, self.rect.y + 50 + i * 40, 280, 30)
            pygame.draw.rect(self.screen, (255, 255, 255), input_rect, border_radius=5)
            text_surface = self.font.render((self.question_text if i == 0 else self.choices[i - 1]), True, (0, 0, 0))
            self.screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 5))
            label_surface = self.font.render(labels[i], True, (0, 0, 0))
            self.screen.blit(label_surface, (self.rect.x + 20, self.rect.y + 30 + i * 40))

        pygame.draw.rect(self.screen, (100, 255, 100), self.save_button)
        pygame.draw.rect(self.screen, (255, 100, 100), self.cancel_button)
        pygame.draw.rect(self.screen, (180, 180, 180), self.up_button)
        pygame.draw.rect(self.screen, (180, 180, 180), self.down_button)

        up_text = self.font.render("▲", True, (0, 0, 0))
        down_text = self.font.render("▼", True, (0, 0, 0))

        self.screen.blit(up_text, (self.up_button.x + 7, self.up_button.y + 5))
        self.screen.blit(down_text, (self.down_button.x + 7, self.down_button.y + 5))

        save_text = self.font.render("Kaydet", True, (0, 0, 0))
        cancel_text = self.font.render("İptal", True, (0, 0, 0))

        self.screen.blit(save_text, (self.save_button.x + 25, self.save_button.y + 10))
        self.screen.blit(cancel_text, (self.cancel_button.x + 25, self.cancel_button.y + 10))