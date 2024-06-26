class Settings():
    def __init__(self):
        """Initialize the game static settings."""
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (255, 255, 255)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 30

        #How quickly the game speeds up
        self.speedup_scale = 1.1
        self.initialize_dynamic_settings()

        # How quickly the alien point value increase
        self.score_scale = 1.5

    def initialize_dynamic_settings(self):
        """Initialize setting that change throughout the game."""
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.7
        self.alien_speed_factor = 0.1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)