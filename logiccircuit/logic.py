# Logic for all gates


def not_gate_logic(inp):
    return not inp[0].value


def and_gate_logic(inp):
    return inp[0].value and inp[1].value


def nand_gate_logic(inp):
    return not (inp[0].value and inp[1].value)


def or_gate_logic(inp):
    return inp[0].value or inp[1].value


def nor_gate_logic(inp):
    return not (inp[0].value or inp[1].value)


def xnor_gate_logic(inp):
    return inp[0].value is inp[1].value


def xor_gate_logic(inp):
    return inp[0].value is not inp[1].value
