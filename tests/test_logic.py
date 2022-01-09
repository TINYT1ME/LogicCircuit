from logiccircuit.logic import *

class Value:
    def __init__(self, value):
        self.value = value

true_obj = Value(True)
false_obj = Value(False)

both_false = [false_obj, false_obj]
first_true = [true_obj, false_obj]
second_true = [false_obj, true_obj]
both_true = [true_obj, true_obj]

def test_not():
    assert not_gate_logic(both_false) is True
    assert not_gate_logic(first_true) is False
    assert not_gate_logic(second_true) is True
    assert not_gate_logic(both_true) is False

def test_and():
    assert and_gate_logic(both_false) is False
    assert and_gate_logic(first_true) is False
    assert and_gate_logic(second_true) is False
    assert and_gate_logic(both_true) is True

def test_nand():
    assert nand_gate_logic(both_false) is True
    assert nand_gate_logic(first_true) is True
    assert nand_gate_logic(second_true) is True
    assert nand_gate_logic(both_true) is False

def test_or():
    assert or_gate_logic(both_false) is False
    assert or_gate_logic(first_true) is True
    assert or_gate_logic(second_true) is True
    assert or_gate_logic(both_true) is True

def test_nor():
    assert nor_gate_logic(both_false) is True
    assert nor_gate_logic(first_true) is False
    assert nor_gate_logic(second_true) is False
    assert nor_gate_logic(both_true) is False

def test_xnor():
    assert xnor_gate_logic(both_false) is True
    assert xnor_gate_logic(first_true) is False
    assert xnor_gate_logic(second_true) is False
    assert xnor_gate_logic(both_true) is True

def test_xor():
    assert xor_gate_logic(both_false) is False
    assert xor_gate_logic(first_true) is True
    assert xor_gate_logic(second_true) is True
    assert xor_gate_logic(both_true) is False
