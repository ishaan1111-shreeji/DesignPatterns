# strategy design pattern:
# context primary class is used as a reference to strategy and add other funcnalities like set,execute
# strategy interface(abstract method) is contact with the concreteStrategies(algo) to be implemented
# CONCRETE STRATEGIES overrides execute method of stratgies.
# users  select the strategy they want at the runtime.
#  Create an object of context and pass a concrete strategy.
from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self) -> str:
        pass


## Concrete strategies overrides ABS strategy
class ConcreteStrategyA(Strategy):
    def execute(self) -> str:
        return "ConcreteStrategy A"


class ConcreteStrategyB(Strategy):
    def execute(self) -> str:
        return "ConcreteStrategy B"


class Default(Strategy):
    def execute(self) -> str:
        return "Default"


class Context:
    strategy = Strategy  ## the strategy interface

    def setStrategy(self, strategy: Strategy = None) -> None:
        if strategy is not None:
            self.strategy = strategy
        else:
            self.strategy = Default()

    def executeStrategy(self):
        print(self.strategy.execute())
        return str


## Strategy interface


if __name__ == "__main__":
    appA = Context()
    appB = Context()
    appC = Context()

## selecting strategies
appC.setStrategy()  ## sets to default strategy
appA.setStrategy(ConcreteStrategyA())
appB.setStrategy(ConcreteStrategyB())


## each object below execute different strategy with same method
appC.executeStrategy()
appA.executeStrategy()
appB.executeStrategy()

