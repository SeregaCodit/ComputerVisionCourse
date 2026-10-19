from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class ROI:
    x: int
    y: int
    w: int
    h: int