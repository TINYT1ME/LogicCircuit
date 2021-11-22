# Logic for all gates
def not_gate_logic(inp):
    return not inp[0][0].value


def and_gate_logic(inp):
    if inp[0][0].value is True and inp[1][0].value is True:
        return True
    else:
        return False


def nand_gate_logic(inp):
    if inp[0][0].value is True and inp[1][0].value is True:
        return False
    else:
        return True


def or_gate_logic(inp):
    if inp[0][0].value is True or inp[1][0].value is True:
        return True
    else:
        return False


def nor_gate_logic(inp):
    if inp[0][0].value is False and inp[1][0].value is False:
        return True
    else:
        return False


def xnor_gate_logic(inp):
    if inp[0][0].value is inp[1][0].value:
        return True
    else:
        return False


def xor_gate_logic(inp):
    if inp[0][0].value is not inp[1][0].value:
        return True
    else:
        return False
