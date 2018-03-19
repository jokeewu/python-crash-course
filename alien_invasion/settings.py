class Settings():
    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (222, 222, 222)
        self.ship_speed_factor = 10

        # 子弹设置
        self.bullet_speed_factor = 10
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 100

        # 外星人
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # 1表示右移, -1表示左移
        self.fleet_direction = 1