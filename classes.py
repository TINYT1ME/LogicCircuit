import pygame
from colors import *


class Basic:
    def __init__(
        self,
        pos: tuple,
        size: tuple,
        color: tuple,
        text: str,
        font: pygame.font.SysFont,
        *args
    ):
        self.pos = pos
        self.size = size
        self.color = color
        self.font = font
        self.surf = pygame.Surface(self.size)
        self.text = text
        self.textsurf = font.render(self.text, False, (0, 0, 0))
        self.surf.fill(color)

    def draw(self, window):
        window.blit(self.surf, self.pos)
        window.blit(self.textsurf, self.pos)

    def click(self, mouse_pos):
        return (
            self.pos[0] < mouse_pos[0] < self.pos[0] + self.size[0]
            and self.pos[1] < mouse_pos[1] < self.pos[1] + self.size[1]
        )


# Class for logic gates
class BasicGate(Basic):
    def __init__(self, *args, logic, total_inp):
        super(BasicGate, self).__init__(*args)
        self.logic = logic
        self.out = None
        self.value = False
        self.inp = []
        for i in range(total_inp):
            self.inp.append([""])

    def update(self):
        try:
            self.value = self.logic(self.inp)
        except AttributeError:
            self.value = False


# Class for buttons
class Button(Basic):
    def __init__(self, *args, panel, gate_list=None, total_inp=None, logic=None):
        super(Button, self).__init__(*args)
        self.gate_list = gate_list
        self.total_inp = total_inp
        self.logic = logic
        self.pos = (panel.pos[0] + int(self.pos[0]), int(panel.pos[1] + self.pos[1]))


# Class for switches
class Switch:
    def __init__(self, pos: tuple, size: tuple, panel):
        self.panel = panel
        self.pos = (panel.pos[0] + int(pos[0]), int(panel.pos[1] + pos[1]))
        self.size = size
        self.surf = pygame.Surface(self.size)
        self.text = pygame.font.SysFont("adobegothicstdkalin", 20).render(
            "Switch", False, (0, 0, 0)
        )
        self.value = False
        self.out = None

    def draw(self, window):
        if self.value:
            self.surf.fill(YELLOW)
        else:
            self.surf.fill(WHITE)
        window.blit(self.surf, self.pos)
        window.blit(self.text, self.pos)

    def click(self, mouse_pos):
        return (
            self.pos[0] < mouse_pos[0] < self.pos[0] + self.size[0]
            and self.pos[1] < mouse_pos[1] < self.pos[1] + self.size[1]
        )

    def update(self):
        pass


# Class for buttons
class Led:
    def __init__(self, pos: tuple, size: tuple, panel):
        self.panel = panel
        self.pos = (panel.pos[0] + int(pos[0]), int(panel.pos[1] + pos[1]))
        self.size = size
        self.surf = pygame.Surface(self.size)
        self.text = pygame.font.SysFont("adobegothicstdkalin", 20).render(
            "LED", False, (0, 0, 0)
        )
        self.value = False
        self.inp = [[""]]

    def draw(self, window):
        if self.value:
            self.surf.fill(RED)
        else:
            self.surf.fill(WHITE)
        window.blit(self.surf, self.pos)
        window.blit(self.text, self.pos)

    def click(self, mouse_pos):
        return (
            self.pos[0] < mouse_pos[0] < self.pos[0] + self.size[0]
            and self.pos[1] < mouse_pos[1] < self.pos[1] + self.size[1]
        )

    def update(self):
        self.value = self.inp[0][0].value


# Class for wires
class Wire:
    def __init__(self, start: tuple, end: tuple, inp, out):
        self.start = start
        self.end = end
        self.inp = inp
        self.out = out
        self.value = inp.value

    def draw(self, window):
        if self.value:
            pygame.draw.line(window, (255, 255, 0), self.start, self.end, 5)
        else:
            pygame.draw.line(window, (255, 255, 255), self.start, self.end, 5)

    def update(self):
        self.inp.update()
        self.value = self.inp.value
        self.out.update()
