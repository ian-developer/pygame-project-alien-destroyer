
class GameStats():
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_settings):
        """Initialize statistics"""
        self.ai_settings = ai_settings
        self.reset_stats()
        #Start Alien Destroyer in an active state.
        #self.game_active = True

        #Start a game in an inactive state.
        self.game_active = False
    
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 999
