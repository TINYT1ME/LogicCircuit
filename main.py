import pygame
from colors import *
from logic import *
from classes import (
    Basic,
    Button,
    Switch,
    Wire,
    Led,
    BasicGate,
)

# Setting name, fps, and font
pygame.display.set_caption("Logic Gates and what not")
FPS = 60
pygame.font.init()
fps_font = pygame.font.SysFont("Arial", 15)
font = pygame.font.SysFont("adobegothicstdkalin", 20)

# Defining constant variables
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
BASIC_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))
SWITCH_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))
LED_SIZE = (int(WIDTH * 0.0277 * 2), int(WIDTH * 0.0277))

# Creating circle for when object is pressed
circle = pygame.Surface((20, 20), pygame.SRCALPHA)
pygame.draw.circle(circle, (123, 123, 123, 255), (10, 10), 10)

# Defining temporary variables
selected = None
first_gate = None

# Defining gates
gates = []
leds = []
wires = []
switches = []

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

# Switch add/remove buttons
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

# Led add/remove buttons
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

# Logic gate buttons
NOT_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    BLUE,
    "Not",
    font,
    panel=BUTTON_PANEL,
    gate_list=gates,
    total_inp=1,
    logic=not_gate_logic,
)
AND_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108 * 2), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    LIGHT_GREEN,
    "And",
    font,
    panel=BUTTON_PANEL,
    gate_list=gates,
    total_inp=2,
    logic=and_gate_logic,
)
OR_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108 * 3), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    LIGHT_YELLOW,
    "Or",
    font,
    panel=BUTTON_PANEL,
    gate_list=gates,
    total_inp=2,
    logic=or_gate_logic,
)
NOR_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108 * 4), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    LIGHT_ORANGE,
    "Nor",
    font,
    panel=BUTTON_PANEL,
    gate_list=gates,
    total_inp=2,
    logic=nor_gate_logic,
)
XOR_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108 * 5), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    LIGHT_PURPLE,
    "Xor",
    font,
    panel=BUTTON_PANEL,
    gate_list=gates,
    total_inp=2,
    logic=xor_gate_logic,
)
NAND_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108 * 6), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    LIGHT_PINK,
    "Nand",
    font,
    panel=BUTTON_PANEL,
    gate_list=gates,
    total_inp=2,
    logic=nand_gate_logic,
)
XNOR_GATE_BUTTON = Button(
    (int(WIDTH * 0.1108 * 7), int((HEIGHT * 0.1) / 2) - int(WIDTH * 0.01385)),
    BASIC_SIZE,
    TEA_GREEN,
    "Xnor",
    font,
    panel=BUTTON_PANEL,
    gate_list=gates,
    total_inp=2,
    logic=xnor_gate_logic,
)


buttons = [
    NOT_GATE_BUTTON,
    AND_GATE_BUTTON,
    OR_GATE_BUTTON,
    NOR_GATE_BUTTON,
    XOR_GATE_BUTTON,
    NAND_GATE_BUTTON,
    XNOR_GATE_BUTTON,
]


# Updates logic
def update():
    for wire in wires:
        wire.update()

def wire_remove(wire):
    pass

# Handling led creation/deletion
def led_handler(pos, event):
    # LEFT CLICK
    if event.button == 1:
        if LED_ADD_BUTTON.click(pos) and len(leds) < 12:
            leds.append(Led((0, int(HEIGHT * 0.06) * len(leds)), LED_SIZE, LED_PANEL))
        elif LED_REMOVE_BUTTON.click(pos):
            # Delete connected wires
            temp_wires = []
            for wire in wires:
                if leds and wire.out is leds[len(leds) - 1]:
                    temp_wires.append(wire) 
            for wire in temp_wires:
                wires.remove(wire)
                wire.disconnect()

            # Remove led
            if leds:
                leds.pop()

# Handling switch creation/deletion
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
            # Delete connected wires
            temp_wires = []
            for wire in wires:
                if switches and wire.inp is switches[len(switches) - 1]:
                    temp_wires.append(wire)
            for wire in temp_wires:
                wires.remove(wire)
                wire.disconnect()

            # Remove switch
            if switches:
                switches.pop()
    # MIDDLE CLICK
    elif event.button == 2:
        # Flipping switch value
        for switch in switches:
            if switch.click(pos):
                switch.value = not switch.value


# Handing gate creation/deletion
def gates_handler(pos, event):
    global selected

    # LEFT CLICK
    if event.button == 1:
        # Creating gates
        if selected and not BUTTON_PANEL.click(pos):
            temp = BasicGate(
                (pos[0] - 15, pos[1] - 15),
                BASIC_SIZE,
                selected.color,
                selected.text,
                font,
                logic=selected.logic,
                total_inp=selected.total_inp,
            )
            gates.append(temp)
            selected = None
        for button in buttons:
            if button.click(pos):
                selected = button
                break
    # RIGHT CLICK
    elif event.button == 3:
        for gate in gates:
            if gate.click(pos):    
                # Delete connected wires
                temp_wires = []
                for inputs in gate.inp:
                    if inputs[0]:
                        temp_wires.append(inputs[0]) 
                for wire in wires:
                    if wire.inp is gate:
                        temp_wires.append(wire)
                for wire in temp_wires:
                    wires.remove(wire)
                    wire.disconnect()

                # remove gate
                gates.remove(gate)

# Handing wire creation and attachment to other objects
def wire_handler(pos, event):
    global selected
    global first_gate

    # LEFT CLICK
    if event.button == 1 and selected is None:

        # Gates
        for gate in gates:
            if gate.click(pos):
                if first_gate:
                    for inputs in gate.inp:
                        if inputs[0] == "":
                            # Creating wire
                            wire = Wire(
                                (
                                    first_gate.pos[0] + first_gate.size[0],
                                    first_gate.pos[1],
                                ),
                                gate.pos,
                                first_gate,
                                gate,
                            )

                            # Adding wire to wires array
                            wires.append(wire)
                            wire.inp.out = wire

                            # Setting led input to wire
                            inputs[0] = wire
                            first_gate = None
                            break
                else:
                    # Assigning first_gate to currently clicked gate
                    first_gate = gate

        # Switches
        if first_gate is None:
            for switch in switches:
                if switch.click(pos):
                    first_gate = switch
                    break

        # Leds
        if first_gate:
            for led in leds:
                if led.click(pos):
                    # Creating wire
                    wire = Wire(
                        (
                            first_gate.pos[0] + first_gate.size[0],
                            first_gate.pos[1],
                        ),
                        led.pos,
                        first_gate,
                        led,
                    )

                    # Adding wire to wires array
                    wires.append(wire)
                    wire.inp.out = wire

                    # Setting led input to wire
                    led.inp[0][0] = wire
                    first_gate = None
                    break


# Handling window drawing
def draw_window(fps: int):
    x, y = pygame.mouse.get_pos()

    # draw bg and panels
    WIN.fill(BG_COLOR)
    BUTTON_PANEL.draw(WIN)
    SWITCH_PANEL.draw(WIN)
    LED_PANEL.draw(WIN)

    # draw objects
    for gate in gates:
        gate.draw(WIN)

    for wire in wires:
        wire.draw(WIN)

    for switch in switches:
        switch.draw(WIN)

    for led in leds:
        led.draw(WIN)

    # draw logic gate buttons
    for button in buttons:
        button.draw(WIN)

    # draw switch & led buttons
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


# Handling clicks
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
