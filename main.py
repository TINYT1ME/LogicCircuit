import pygame
from classes import (
    NotGate,
    Options,
    Button,
    Wire,
    Switch
)

# colors
BG_COLOR = (113, 137, 179)
OPTIONS_COLOR = (179, 155, 113)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Logic Gates and what not")
OPTIONS = Options(WIDTH, int(HEIGHT * 0.1), 0, HEIGHT - int(HEIGHT * 0.1), OPTIONS_COLOR)

FPS = 60
pygame.font.init()
fps_font = pygame.font.SysFont('Arial', 15)
font = pygame.font.SysFont('adobegothicstdkalin', 20)

selected = None
first_gate = None

circle = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(circle, (123, 123, 123, 255), (10, 10), 10)

BUTTON_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))

NOT_GATE_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))
NOT_GATE_BUTTON = Button((int(WIDTH * 0.0277), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
                         BUTTON_SIZE,
                         1,
                         OPTIONS,
                         font,
                         "Not",
                         (25, 200, 255))

SWITCH_BUTTON_RADIUS = (int((HEIGHT * 0.1) / 3))
SWITCH_BUTTON = Button((int(WIDTH * 0.1108), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
                       BUTTON_SIZE,
                       2,
                       OPTIONS,
                       font,
                       "Switch",
                       (255, 255, 255))
not_gates = []
wires = []
switches = []
buttons = [NOT_GATE_BUTTON, SWITCH_BUTTON]
object_list = {
    1: [NotGate, not_gates, NOT_GATE_SIZE],
    2: [Switch, switches, SWITCH_BUTTON_RADIUS]
}


def draw_window(fps: int):
    x, y = pygame.mouse.get_pos()

    # draw bg and options
    WIN.fill(BG_COLOR)
    OPTIONS.draw(WIN)

    # draw not gates
    for gate in not_gates:
        gate.draw(WIN)

    for wire in wires:
        wire.draw(WIN)

    for switch in switches:
        switch.draw(WIN)

    # draw option buttons
    NOT_GATE_BUTTON.draw(WIN)
    SWITCH_BUTTON.draw(WIN)

    # fps counter
    fps_counter = fps_font.render(str(fps), False, (0, 204, 34))
    WIN.blit(fps_counter, (9, 9))

    # draw circle when an item is selected
    if selected is not None or first_gate is not None:
        WIN.blit(circle, (x - 10, y - 10))

    # update screen
    pygame.display.update()


def click(pos):
    global selected
    global first_gate
    x, y = pygame.mouse.get_pos()

    if selected is None:
        for gate in not_gates:
            if gate.click((x, y)):
                if first_gate:
                    wire = Wire((first_gate.pos[0] + first_gate.size[0], first_gate.pos[1]), gate.pos,
                                first_gate.transform())
                    wires.append(wire)
                    gate.switch(first_gate.transform())
                    first_gate = None
                else:
                    first_gate = gate

    if selected and OPTIONS.not_collided((x, y)):
        temp = object_list[selected][0]((x - 15, y - 15), object_list[selected][2], True, font)
        object_list[selected][1].append(temp)
        selected = None

    for button in buttons:
        if button.click(pos):
            selected = buttons.index(button) + 1
            break


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click(pygame.mouse.get_pos())

        draw_window(int(clock.get_fps()))

    pygame.quit()


if __name__ == '__main__':
    main()
