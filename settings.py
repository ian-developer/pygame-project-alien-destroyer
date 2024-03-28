class Settings():
    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_speed_factor = 0.5

        # Bullet settings
        self.bullet_speed_factor = 0.4
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3