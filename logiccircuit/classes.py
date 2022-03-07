# Classes for Logic Circuit

import pygame
from colors import *

# parent class
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

    # draw
    def draw(self, window):
        window.blit(self.surf, self.pos)
        window.blit(self.textsurf, self.pos)

    # return positive if clicked on object
    def click(self, mouse_pos):
        return (
            self.pos[0] < mouse_pos[0] < self.pos[0] + self.size[0]
            and self.pos[1] < mouse_pos[1] < self.pos[1] + self.size[1]
        )


class Input(Basic):
    def __init__(self, *args):
        super(Input, self).__init__(*args)
        self.value = False
        self.connected_wires = []


# class for logic gates
class BasicGate(Basic):
    def __init__(self, *args, logic, total_inp):
        super(BasicGate, self).__init__(*args)
        self.logic = logic  # Assigning the gate
        self.io_rect_size = self.size[0] * 0.204  # Size of output and input squares
        self.out_rect = pygame.Rect(
            self.pos[0] + self.size[0],
            self.pos[1],
            self.io_rect_size,
            self.io_rect_size,
        )  # Drawing output square
        self.value = False  # Output value of gate
        self.inp = []
        self.total_inp = total_inp
        for i in range(total_inp):  # Creating inputs
            self.inp.append(
                Input(
                    (
                        self.pos[0] - self.io_rect_size,
                        self.pos[1] + (self.size[1] - self.io_rect_size) * i,
                    ),
                    (self.io_rect_size, self.io_rect_size),
                    WHITE,
                    "",
                    pygame.font.SysFont("adobegothicstdkalin", 20),
                )
            )

    # Draw gate, and input and output squares
    def draw(self, window):
        window.blit(self.surf, self.pos)
        window.blit(self.textsurf, self.pos)
        for inp in self.inp:
            inp.draw(window)
        pygame.draw.rect(window, WHITE, self.out_rect)

    # Update gate value
    def update(self):
        try:
            self.value = self.logic(self.inp)
        except AttributeError:
            self.value = False


# class for buttons
class Button(Basic):
    def __init__(self, *args, panel: Basic, gate_list=None, total_inp=None, logic=None):
        super(Button, self).__init__(*args)
        self.gate_list = gate_list
        self.total_inp = total_inp
        self.logic = logic
        self.pos = (panel.pos[0] + int(self.pos[0]), int(panel.pos[1] + self.pos[1]))


# class for switches
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
        self.out = []

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


# class for leds
class Led:
    def __init__(self, pos: tuple, size: tuple, panel):
        self.panel = panel
        self.pos = (panel.pos[0] + int(pos[0]), int(panel.pos[1] + pos[1]))
        self.size = size
        self.surf = pygame.Surface(self.size)
        self.text = pygame.font.SysFont("adobegothicstdkalin", 20).render(
            "LED", False, (0, 0, 0)
        )
        self.io_rect_size = 10
        self.value = False
        self.inp = Input(
            (
                self.pos[0] - self.io_rect_size,
                self.pos[1],
            ),
            (self.io_rect_size, self.io_rect_size),
            WHITE,
            "",
            pygame.font.SysFont("adobegothicstdkalin", 20),
        )

    def draw(self, window):
        if self.value:
            self.surf.fill(RED)
        else:
            self.surf.fill(WHITE)
        window.blit(self.surf, self.pos)
        window.blit(self.text, self.pos)
        self.inp.draw(window)

    def update(self):
        self.value = False
        for wire in self.inp.connected_wires:
            if wire.value:
                self.value = True
                break


# class for wires
class Wire:
    def __init__(self, inp, temp_points):
        self.inp = inp
        self.value = inp.value
        self.points = []
        self.points = temp_points
        self.radius = 5

    def draw(self, window):
        # Iterate through the points in the list and draw a line between them
        for i in range(len(self.points) - 1):
            if self.value:
                pygame.draw.line(
                    window,
                    (255, 255, 0),
                    (int(self.points[i][0]), int(self.points[i][1])),
                    (int(self.points[i + 1][0]), int(self.points[i + 1][1])),
                    self.radius,
                )
            else:
                pygame.draw.line(
                    window,
                    (255, 255, 255),
                    (int(self.points[i][0]), int(self.points[i][1])),
                    (int(self.points[i + 1][0]), int(self.points[i + 1][1])),
                    self.radius,
                )

    def update(self):
        self.inp.update()
        self.value = self.inp.value
