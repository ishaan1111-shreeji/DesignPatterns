from abc import ABC, abstractmethod
import platform


class Component(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class WindowsPlaybutton(Component):
    def render(self) -> str:
        return "render Windows Play button"


class WindowsTimeline(Component):
    def render(self) -> str:
        return "render Windows timeline"


class WindowsWindow(Component):
    def render(self) -> str:
        return "render Windows window"


class MacPlaybutton(Component):
    def render(self) -> str:
        return "render Mac Play button"


class MacTimeline(Component):
    def render(self) -> str:
        return "render Mac timeline"


class MacWindow(Component):
    def render(self) -> str:
        return "render Mac window"


class AbstractPlayerComponentFactory:
    @abstractmethod
    def create_component(self, component_type: str) -> Component:
        pass


class WindowPlayerComponentFactory(AbstractPlayerComponentFactory):
    def create_component(self, component_type: str) -> Component:
        if component_type == "play_button":
            return WindowsPlaybutton()
        if component_type == "timeline":
            return WindowsTimeline()
        if component_type == "window":
            return WindowsWindow()
        return None


class MacPlayerComponentFactory(AbstractPlayerComponentFactory):
    def create_component(self, component_type: str) -> Component:
        if component_type == "play_button":
            return MacPlaybutton()
        if component_type == "timeline":
            return MacPlaybutton()
        if component_type == "window":
            return MacWindow()
        return None

#client code ,client will directly derive the object of class without knowing the implementation
#
def client(Factory: AbstractPlayerComponentFactory) -> None:
    window = Factory.create_component("window")
    timeline = Factory.create_component("timeline")
    play_button = Factory.create_component("play_button")
    print(window.render(), timeline.render(), play_button.render())


if __name__ == "__main__":
    current_os = platform.system()
    if current_os == "Windows":
        client(WindowPlayerComponentFactory())
    elif current_os == "Darwin":
        client(MacPlayerComponentFactory())
    else:
        print("os not supported")
