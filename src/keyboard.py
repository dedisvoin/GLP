import keyboard

class Keyboard:
    def __init__(self) -> 'Keyboard':
        ...

    def press(self, key: str) -> bool:
        return keyboard.is_pressed(key)
    
class Key:
    def __init__(self, key: str) -> None:
        self.__key = key
    
    @property
    def get(self): return self.__key



    

keyboard = Keyboard()