import pygame


class Basic:
    def __init__(self, pos: tuple, size: tuple, color: tuple, text: str, font: pygame.font.SysFont, *args):
        self.pos = pos
        self.size = size
        self.color = color
        self.font = font
        self.surf = pygame.Surface(self.size)
        self.text = font.render(text, False, (0, 0, 0))
        self.surf.fill(color)

    def draw(self, window):
        window.blit(self.surf, self.pos)
        window.blit(self.text, self.pos)

    def click(self, mouse_pos):
        return (
                self.pos[0] < mouse_pos[0] < self.pos[0] + self.size[0]
                and self.pos[1] < mouse_pos[1] < self.pos[1] + self.size[1]
        )


class NotGate(Basic):
    def __init__(self, *args, value: bool):
        super(NotGate, self).__init__(*args)
        self.inp = value

    def transform(self):
        return not self.inp

    def switch(self, inp):
        self.inp = inp


class Switch(Basic):
    def __init__(self, *args, value: bool):
        super(Switch, self).__init__(*args)
        self.value = value


class Button(Basic):
    def __init__(self, *args, assigned: int, panel):
        super(Button, self).__init__(*args)
        self.assigned = assigned
        self.pos = (panel.pos[0] + int(self.pos[0]), int(panel.pos[1] + self.pos[1]))


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
