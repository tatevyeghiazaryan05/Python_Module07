from ex0.factory import FlameFactory, AquaFactory, CreatureFactory
from ex1.factory import HealingCreatureFactory, TransformCreatureFactory
from ex2 import (
    BattleStrategy,
    NormalStrategy,
    AggressiveStrategy,
    InvalidStrategyError,
    DefensiveStrategy,
)


def battle(
    opponents: list[tuple[CreatureFactory, BattleStrategy]]
) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")
    creatur = [
                (factory.create_base(), strategy)
                for factory, strategy in opponents
              ]
    for i in range(len(creatur)):
        for j in range(i + 1, len(creatur)):
            creature1, strategy1 = creatur[i]
            creature2, strategy2 = creatur[j]
            print("\n* Battle *")
            print(f"{creature1.describe()}")
            print(" vs.")
            print(f"{creature2.describe()}")
            try:
                print(strategy1.act(creature1))
                print(strategy2.act(creature2))
            except InvalidStrategyError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame = FlameFactory()
    normal = NormalStrategy()
    healing = HealingCreatureFactory()
    defensive = DefensiveStrategy()
    aggresive = AggressiveStrategy()
    aquabub = AquaFactory()
    transform = TransformCreatureFactory()
    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame, normal), (healing, defensive)])
    print("\nTournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame, aggresive), (healing, defensive)])
    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aquabub, normal), (healing, defensive), (transform, aggresive)])
