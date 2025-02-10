import pygame


class Button:
    def __init__(self, x, y, width, height, text, font_size=40, base_color=(100, 100, 255),
                 hover_color=(255, 100, 100)):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, font_size)
        self.base_color = base_color
        self.hover_color = hover_color
        self.current_color = self.base_color
        self.is_hovering = False
        self.animation_step = 0

    def is_hovered(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        return self.rect.collidepoint(mouse_x, mouse_y)

    def update(self):
        if self.is_hovered():
            self.animation_step = min(self.animation_step + 1, 10)
        else:
            self.animation_step = max(self.animation_step - 1, 0)

        self.current_color = (
            self.base_color[0] + (self.hover_color[0] - self.base_color[0]) * self.animation_step // 10,
            self.base_color[1] + (self.hover_color[1] - self.base_color[1]) * self.animation_step // 10,
            self.base_color[2] + (self.hover_color[2] - self.base_color[2]) * self.animation_step // 10,
        )

    def draw(self, screen):
        pygame.draw.rect(screen, self.current_color, self.rect, border_radius=10)
        text_surface = self.font.render(self.text, True, (255, 255, 255))
        text_x = self.rect.x + (self.rect.width - text_surface.get_width()) // 2
        text_y = self.rect.y + (self.rect.height - text_surface.get_height()) // 2
        screen.blit(text_surface, (text_x, text_y))
