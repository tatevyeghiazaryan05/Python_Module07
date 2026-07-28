from ex0 import FlameFactory, AquaFactory, CreatureFactory


def test_factory(factory: CreatureFactory) -> None:
    print("Testing factory")
    base = factory.create_base()
    print(base.describe())
    print(base.attack())
    evolved = factory.create_evolved()
    print(evolved.describe())
    print(evolved.attack())


def battle(factory1: CreatureFactory, factory2: CreatureFactory) -> None:
    print("\nTesting battle")
    c1 = factory1.create_base()
    c2 = factory2.create_base()
    print(f"{c1.describe()} vs. {c2.describe()}")
    print("fight!")
    print(c1.attack())
    print(c2.attack())


if __name__ == "__main__":
    flame_factory = FlameFactory()
    aqua_factory = AquaFactory()

    test_factory(flame_factory)
    test_factory(aqua_factory)
    battle(flame_factory, aqua_factory)
