from typing import ClassVar


class WritingInstrument:
    pass


class Pen:
    pass


class Writer:
    def __init__(self, writing_instrument: ClassVar[WritingInstrument]):
        self.writing_instrument = writing_instrument


if __name__ == "__main__":
    writer = Writer(writing_instrument=Pen())
