
from registry import registry

class AbstractAnimal:
    def __init_subclass__(cls):
        super().__init_subclass__()
        registry.append(cls)
