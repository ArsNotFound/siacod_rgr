import dataclasses

__all__ = ("Graph",)


@dataclasses.dataclass
class Graph:
    matrix: list[list[int]]
    header: list[str]

