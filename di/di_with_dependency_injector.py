from typing import ClassVar
from dependency_injector import containers, providers


class WritingInstrument:
    def __init__(self, size: str):
        self.size = size


class Pen:
    pass


class Writer:
    def __init__(self, writing_instrument: ClassVar[WritingInstrument]):
        self.writing_instrument = writing_instrument


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    pen = providers.Singleton(
        Pen,
        size=config.writing_instruments.size,
    )
    writer = providers.Factory(
        Writer,
        writing_instrument=pen,
    )


if __name__ == "__main__":
    container = Container()
    container.config.writing_instruments.size.from_value('big')
    writer = container.writer
