from dataclasses import dataclass

@dataclass
class Instruction:
    """Промежуточное представление команды УВМ."""
    opcode: int
    fields: dict[str, int]
