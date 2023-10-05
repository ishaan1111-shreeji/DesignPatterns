from abc import ABC, abstractmethod
import platform


class Accessory(ABC):
    @abstractmethod
    def render(self):
        pass


class BlueLightSaber(Accessory):
    def render(self) -> str:
        return "render Blue Saber"


class RedLightSaber(Accessory):
    def render(self) -> str:
        return "render Red Saber"


class BlueEyes(Accessory):
    def render(self) -> str:
        return "render Blue Eyes"


class RedEyes(Accessory):
    def render(self) -> str:
        return "render Red Eyes"


class BlackRobe(Accessory):
    def render(self) -> str:
        return "render Black Robe"


class WhiteRobe(Accessory):
    def render(self) -> str:
        return "render white Robe"


# client can only see this,(abstract class)
class AbstractAccessoryFactory(ABC):
    @abstractmethod
    def create_light_saber(self) -> Accessory:
        pass

    @abstractmethod
    def create_eyes(self) -> Accessory:
        pass

    @abstractmethod
    def create_robe(self) -> Accessory:
        pass


# generate concrete class
class SithAccessoryFactory(AbstractAccessoryFactory):
    def create_light_saber(self) -> Accessory:
        return RedLightSaber()

    def create_eyes(self) -> Accessory:
        return RedEyes()

    def create_robe(self) -> Accessory:
        return BlackRobe()

# concrete class
class JediAccessoryFactory(AbstractAccessoryFactory):
    def create_light_saber(self) -> Accessory:
        return BlueLightSaber()

    def create_eyes(self) -> Accessory:
        return BlueEyes()

    def create_robe(self) -> Accessory:
        return WhiteRobe()

# client code for getting objects of abstract class
def client(accessory_factory: AbstractAccessoryFactory) -> None:
    lightsaber = accessory_factory.create_light_saber()
    eyes = accessory_factory.create_eyes()
    robe = accessory_factory.create_robe()
    print(eyes.render())
    print(lightsaber.render())
    print(robe.render())


if __name__ == "__main__":
    current_os = platform.system()
    if current_os == "Darwin":
        client(JediAccessoryFactory())
    elif current_os == "Windows":
        client(SithAccessoryFactory())
    else:
        print("os not supported")
