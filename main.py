import pygame
from colors import *
from classes import Basic, Button, NotGate, Switch, Wire, Led

pygame.display.set_caption("Logic Gates and what not")
FPS = 60
pygame.font.init()
fps_font = pygame.font.SysFont("Arial", 15)
font = pygame.font.SysFont("adobegothicstdkalin", 20)

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BASIC_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))
SWITCH_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))
LED_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))

# Defining panels
BUTTON_PANEL = Basic(
    (0, HEIGHT - int(HEIGHT * 0.1)), (WIDTH, int(HEIGHT * 0.1)), PANEL_COLOR, "", font
)
SWITCH_PANEL = Basic(
    (0, HEIGHT / 6),
    (int(WIDTH * 0.0277 * 2), int(HEIGHT * 0.06) * 12),
    PANEL_COLOR,
    "",
    font,
)

LED_PANEL = Basic(
    (WIDTH - int(WIDTH * 0.0277 * 2), HEIGHT / 6),
    (int(WIDTH * 0.0277 * 2), int(HEIGHT * 0.06) * 12),
    PANEL_COLOR,
    "",
    font,
)

selected = None
first_gate = None

circle = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(circle, (123, 123, 123, 255), (10, 10), 10)

SWITCH_ADD_BUTTON = Button(
    (0, -(int((HEIGHT * 0.15) / 2) - int(WIDTH * 0.01385) + BASIC_SIZE[1] + 2)),
    BASIC_SIZE,
    GREEN,
    "+Switch",
    font,
    panel=SWITCH_PANEL,
)

SWITCH_REMOVE_BUTTON = Button(
    (0, -(int((HEIGHT * 0.15) / 2) - int(WIDTH * 0.01385))),
    BASIC_SIZE,
    RED,
    "-Switch",
    font,
    panel=SWITCH_PANEL,
)

LED_ADD_BUTTON = Button(
    (0, -(int((HEIGHT * 0.15) / 2) - int(WIDTH * 0.01385) + BASIC_SIZE[1] + 2)),
    BASIC_SIZE,
    GREEN,
    "+LED",
    font,
    panel=LED_PANEL,
)

LED_REMOVE_BUTTON = Button(
    (0, -(int((HEIGHT * 0.15) / 2) - int(WIDTH * 0.01385))),
    BASIC_SIZE,
    RED,
    "-LED",
    font,
    panel=LED_PANEL,
)

NOT_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    BLUE,
    "Not",
    font,
    panel=BUTTON_PANEL,
)

not_gates = []
leds = []
wires = []
switches = []
buttons = [NOT_GATE_BUTTON]

object_list = {
    1: [NotGate, not_gates, BASIC_SIZE, "Not", BLUE],
    2: [Switch, switches, SWITCH_SIZE, "Switch", None],
    3: [Led, leds, LED_SIZE, "LED", None],
}


# Updates logic
def update():
    for wire in wires:
        wire.update()


def led_handler(pos, event):
    # LEFT CLICK
    if event.button == 1:
        if LED_ADD_BUTTON.click(pos) and len(leds) < 12:
            leds.append(Led((0, int(HEIGHT * 0.06) * len(leds)), LED_SIZE, LED_PANEL))
        elif LED_REMOVE_BUTTON.click(pos):
            # Removes wire connected to led
            try:
                wires.remove(leds[len(leds) - 1].inp1)
            except (ValueError, IndexError):
                pass

            # Remove led
            try:
                leds.pop()
            except IndexError:
                pass


def switch_handler(pos, event):
    # LEFT CLICK
    if event.button == 1:
        # Creating/removing switches
        if SWITCH_ADD_BUTTON.click(pos) and len(switches) < 12:
            switches.append(
                Switch(
                    (0, int(HEIGHT * 0.06) * len(switches)), SWITCH_SIZE, SWITCH_PANEL
                )
            )
        elif SWITCH_REMOVE_BUTTON.click(pos):
            # Removes wire connected to switch
            try:
                wires.remove(switches[len(switches) - 1].out)
            except (ValueError, IndexError):
                pass

            # Remove switch
            try:
                switches.pop()
            except IndexError:
                pass
    # MIDDLE CLICK
    elif event.button == 2:
        # Flipping switch value
        for switch in switches:
            if switch.click(pos):
                switch.value = not switch.value


def wire_handler(pos, event):
    global selected
    global first_gate

    # LEFT CLICK
    if event.button == 1 and selected is None:
        for obj in object_list:
            for out in object_list[obj][1]:
                if out.click(pos):
                    if first_gate:
                        if out.inp1 is None:
                            wire = Wire(
                                (
                                    first_gate.pos[0] + first_gate.size[0],
                                    first_gate.pos[1],
                                ),
                                out.pos,
                                first_gate,
                                out,
                            )
                            wires.append(wire)
                            wire.inp.out = wire
                            wire.out.inp1 = wire
                            first_gate = None
                    else:
                        first_gate = out


def gates_handler(pos, event):
    global selected

    # LEFT CLICK
    if event.button == 1:
        # Creating gates
        if selected and not BUTTON_PANEL.click(pos):
            temp = object_list[selected][0](
                (pos[0] - 15, pos[1] - 15),
                object_list[selected][2],
                object_list[selected][4],
                object_list[selected][3],
                font,
            )
            object_list[selected][1].append(temp)
            selected = None
        for button in buttons:
            if button.click(pos):
                selected = buttons.index(button) + 1
                break


def draw_window(fps: int):
    x, y = pygame.mouse.get_pos()

    # draw bg and panels
    WIN.fill(BG_COLOR)
    BUTTON_PANEL.draw(WIN)
    SWITCH_PANEL.draw(WIN)
    LED_PANEL.draw(WIN)

    # draw not gates
    for gate in not_gates:
        gate.draw(WIN)

    for wire in wires:
        wire.draw(WIN)

    for switch in switches:
        switch.draw(WIN)

    for led in leds:
        led.draw(WIN)

    # draw option buttons
    NOT_GATE_BUTTON.draw(WIN)
    SWITCH_ADD_BUTTON.draw(WIN)
    SWITCH_REMOVE_BUTTON.draw(WIN)
    LED_ADD_BUTTON.draw(WIN)
    LED_REMOVE_BUTTON.draw(WIN)

    # fps counter
    fps_counter = fps_font.render(str(fps), False, (0, 204, 34))
    WIN.blit(fps_counter, (9, 9))

    # draw circle when an item is selected
    if selected is not None or first_gate is not None:
        WIN.blit(circle, (x - 10, y - 10))

    # update screen
    pygame.display.update()


def click(pos, event):
    led_handler(pos, event)
    switch_handler(pos, event)
    wire_handler(pos, event)
    gates_handler(pos, event)


def main():
    global selected
    global first_gate
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                click(pygame.mouse.get_pos(), event)

            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                selected = None
                first_gate = None

        draw_window(int(clock.get_fps()))

    pygame.quit()


if __name__ == "__main__":
    main()
