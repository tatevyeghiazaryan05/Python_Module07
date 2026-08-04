from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex1.creature import HealCapability, TransformCapability

if __name__ == "__main__":
    healing_factory = HealingCreatureFactory()
    healing_base = healing_factory.create_base()
    healing_evolved = healing_factory.create_evolved()
    print("Testing Creature with healing capability")
    print("base:", healing_base.describe())
    print(healing_base.attack())
    if isinstance(healing_base, HealCapability):
        print(healing_base.heal())
    print("evolved:", healing_evolved.describe())
    print(healing_evolved.attack())
    if isinstance(healing_evolved, HealCapability):
        print(healing_evolved.heal())

    print("\nTesting Creature with transform capability")
    transform_factory = TransformCreatureFactory()
    transform_base = transform_factory.create_base()
    transform_evolved = transform_factory.create_evolved()
    print("base:", transform_base.describe())
    print(transform_base.attack())
    if isinstance(transform_base, TransformCapability):
        print(transform_base.transform())
        print(transform_base.attack())
        print(transform_base.revert())
    print("evolved:", transform_evolved.describe())
    print(transform_evolved.attack())
    if isinstance(transform_evolved, TransformCapability):
        print(transform_evolved.transform())
        print(transform_evolved.attack())
        print(transform_evolved.revert())
