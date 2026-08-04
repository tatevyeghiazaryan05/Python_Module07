from abc import ABC, abstractmethod
from ex0.creature import Creature


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str = "") -> str:
        ...


class TransformCapability(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        ...

    @abstractmethod
    def revert(self) -> str:
        ...


class Sproutling(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Sproutling", "Grass")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str = "") -> str:
        return "Sproutling heals itself for a small amount"


class Bloomelle(Creature, HealCapability):
    def __init__(self) -> None:
        super().__init__("Bloomelle", "Grass/Fairy")
        HealCapability.__init__(self)

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str = "") -> str:
        return "Bloomelle heals itself and others for a large amount"


class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return "Shiftling shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Shiftling returns to normal."

    def attack(self) -> str:
        if self.is_transformed:
            return "Shiftling performs a boosted strike!"
        return "Shiftling attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        super().__init__("Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return "Morphagon morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return "Morphagon stabilizes its form."

    def attack(self) -> str:
        if self.is_transformed:
            return "Morphagon unleashes a devastating morph strike!"
        return "Morphagon attacks normally."
