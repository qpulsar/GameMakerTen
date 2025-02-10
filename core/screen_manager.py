class ScreenManager:
    def __init__(self):
        self.current_screen = None

    def set_screen(self, screen):
        """Yeni bir ekran ayarla"""
        self.current_screen = screen

    def handle_events(self, event):
        """Mevcut ekrana olayları ilet"""
        if self.current_screen:
            self.current_screen.handle_events(event)

    def update(self):
        """Mevcut ekranı güncelle"""
        if self.current_screen:
            self.current_screen.update()

    def draw(self, screen):
        """Mevcut ekranı çiz"""
        if self.current_screen:
            self.current_screen.draw(screen)
