import unittest


def simulate(program, tape, head):
    # program is a list of state tuples, (state, input, output, direction, new state)
    tape, state = list(tape), 0
    rules = {r[:2]: r[2:] for r in program}
    while state >= 0:
        output, direction, state = rules[(state, tape[head])]
        tape[head] = output
        if direction == "L":
            if head == 0:
                tape.insert(0, "_")
            head -= 1
        elif direction == "R":
            if head == len(tape) - 1:
                tape.append("_")
            head += 1
    # normalize tape and adjust head position
    tape_length = len(tape)
    tape = "".join(tape).lstrip("_")
    head = head - (tape_length - len(tape)) + 3
    tape = tape.rstrip("_")
    return "___" + tape + "___", head


class TuringMachineTest(unittest.TestCase):
    def test_simulator(self):
        program = [(0, "1", "1", "R", 0),
                   (0, "+", "1", "R", 1),
                   (1, "1", "1", "R", 1),
                   (1, "_", "_", "L", 2),
                   (2, "1", "_", "L", -1)]
        tape, head = "___111+11111___", 3
        self.assertEquals(simulate(program, tape, head), ("___11111111___", 10))


if __name__ == "__main__":
    unittest.main()
