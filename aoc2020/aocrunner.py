class InfiniteLoopException(Exception):
    def __init__(self, index: int):
        self.message = f"infinite loop detected at instruction {index}"
        super().__init__(self.message)

class AOCRunner(object):
    """
    class to read a set of instructions and execute them, started at day 8
    of adventofcode/2020
    """

    """ code related properties """
    _program = None         # text blob containing instructions (one per line)
    _instructions = []      # array containing instructions
    _executed = set()       # already exceute

    """ registers and pointers """
    _ip = 0         # instruction pointer
    _acc = 0        # acc register

    """ helpers """
    _jump = 1       # amount to increase _ip with after current instructions
    _func = ""      # current function
    _params = []    # current parameters

    def __init__(self):
        self._ip = 0
        self._acc = 0
        self._program = ""
        self._instructions = []

    def load_program(self, blob: str):
        self._program = blob
        self.reset()

    def reset(self):
        self._ip = 0
        self._instructions = [line.rstrip() for line in self._program.splitlines()]
        self._acc = 0
        self._executed = set()

    def do_nop(self):
        self._jump = 1

    def do_acc(self):
        self._jump = 1
        self._acc += int(self._params[0])

    def do_jmp(self):
        self._jump = int(self._params[0])

    def execute(self):
        def not_impl():
            raise Exception(f"'{self._func}' not implemented!")
        self._executed.add(self._ip)     
        return getattr(self, f"do_{self._func}", not_impl)()

    def run(self):
        while self._ip < len(self._instructions):       
            # execute instruction
            parts = self._instructions[self._ip].split(" ", 1)
            self._func = parts[0]
            self._params = parts[1:]
            self.execute()

            # jump to next instruction 
            next_ip = self._ip + self._jump
            if next_ip in self._executed:
                raise InfiniteLoopException(self._ip)
            self._ip = next_ip

    def dump(self):
        print("=" * 76)
        print(" internals:")
        print(f" {'ip:':<8} {self._ip:<10} {'#lines:':<8} {len(self._instructions):<8}")
        print(f" {'func:':<8} {self._func:<10} {'params:':<8} {self._params}")
        print("","-" * 74)
        print(" registers:")
        print(f" {'acc:':<8} {self._acc}")
        print("=" * 76)