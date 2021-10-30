import pygame


class NotGate:
    def __init__(self, pos: tuple, size: tuple, inp: bool, font):
        super(NotGate, self).__init__()
        self.pos = pos
        self.inp = inp
        self.size = size
        self.surf = pygame.Surface(self.size)
        self.text = font.render("Not", False, (0, 0, 0))
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()

    def transform(self):
        return not self.inp

    def switch(self, inp):
        self.inp = inp

    def draw(self, window):
        window.blit(self.surf, self.pos)
        window.blit(self.text, self.pos)

    def click(self, mpos):
        if (
                self.pos[0] < mpos[0] < self.pos[0] + self.size[0]
                and self.pos[1] < mpos[1] < self.pos[1] + self.size[1]
        ):
            return True
        return None


class Switch:
    def __init__(self, pos: tuple, radius: int, of: bool, font):
        self.pos = pos
        self.radius = radius
        self.text = font.render("Switch", False, (0, 0, 0))
        self.of = of

    def draw(self, window):
        if self.of:
            pygame.draw.circle(window, (255, 255, 0), self.pos, self.radius)
        else:
            pygame.draw.circle(window, (255, 255, 255), self.pos, self.radius)


class Wire:
    def __init__(self, start: tuple, end: tuple, of: bool):
        self.start = start
        self.end = end
        self.of = of

    def draw(self, window):
        if self.of:
            pygame.draw.line(window, (255, 255, 0), self.start, self.end, 5)
        else:
            pygame.draw.line(window, (255, 255, 255), self.start, self.end, 5)


class Button:
    def __init__(self, pos: tuple, size: tuple, assigned: int, cls, font, text: str, color: tuple):
        self.x, self.y = cls.rect.topleft
        self.pos = (self.x + int(pos[0]), int(self.y + pos[1]))
        self.cls = cls
        self.assigned = assigned
        self.size = size
        self.surf = pygame.Surface(size)
        self.text = font.render(text, False, (0, 0, 0))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()

    def draw(self, window):
        window.blit(self.surf, self.pos)
        window.blit(self.text, self.pos)

    def click(self, mpos):
        if (
                self.pos[0] < mpos[0] < self.pos[0] + self.size[0]
                and self.pos[1] < mpos[1] < self.pos[1] + self.size[1]
        ):
            return self.assigned


class Options:
    def __init__(self, width: int, height: int, x: int, y: int, color: tuple):
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.rect.topleft = (x, y)

    def draw(self, window):
        window.blit(self.surf, self.rect)

    def not_collided(self, mpos):
        return (
                not self.x < mpos[0] < self.x + self.width
                or not self.y < mpos[1] < self.y + self.height
        )
