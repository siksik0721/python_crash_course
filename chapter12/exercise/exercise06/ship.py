import pygame


class Ship:
    """우주선을 관리하는 클래스"""

    def __init__(self, ai_game):
        """우주선을 초기화하고 시작 위치를 설정합니다"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # 우주선 이미지를 불러오고 사각형을 가져옵니다
        self.image = pygame.transform.rotate(
            pygame.image.load("chapter12/images/ship.bmp"), 270
        )
        self.rect = self.image.get_rect()

        # 우주선의 초기 위치는 화면 하단 중앙입니다
        self.rect.midleft = self.screen_rect.midleft

        # 우주선의 정확한 세로 위치 설정을 위해 부동 소수점 숫자를 저장합니다
        self.y = float(self.rect.y)

        # 움직임 플래그는 정지 상태로 시작합니다
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """움직임 플래그를 바탕으로 우주선 위치를 업데이트합니다"""
        # rect가 아니라 우주선의 y 값을 업데이트합니다
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # self.y를 통해 rect 객체를 업데이트합니다
        self.rect.y = self.y

    def blitme(self):
        """우주선을 현재 위치에 그립니다"""
        self.screen.blit(self.image, self.rect)
