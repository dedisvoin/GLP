import keyboard
import pygame
from src.constants import *

class WindowFlags:
    FULLSCREEN =                   pygame.FULLSCREEN
    RESIZE =                       pygame.RESIZABLE
    SCALE =                        pygame.SCALED
    NO_FRAME =                     pygame.NOFRAME

class WindowEvents:
    def __init__(self) -> 'WindowEvents':
        self.__whell = 0

    def update(self):
        self.__whell = 0
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEWHEEL:
                self.__whell = event.y
    
    @property
    def whell(self):
        return self.__whell

class Window:
    def __init__(self, 
                 _size: list[int] = STANDART_WINDOW_SIZE, 
                 _title: str = STANDART_WINDOW_TITLE, 
                 _events: WindowEvents = WindowEvents(),
                 _vsync: bool = STANDART_WINDOW_VSYNC, 
                 _flags: WindowFlags = WindowFlags.RESIZE) -> 'Window':
        self.__title = _title
        self.__flags = _flags
        self.__vsync = _vsync
        self.__events = _events
        self.__exit_key = 'esc'
        self.__opened = True
        self.__surf = pygame.display.set_mode(_size, _flags, 0, 0, _vsync)
        self.__timer = pygame.time.Clock()
        self.__fps = 60
        

        pygame.display.set_caption(_title)

    def update(self, _bg_color: tuple[int, int, int] = STANDART_WINDOW_BG_COLOR):
        self.__events.update()
        self.__timer.tick(self.__fps)
        pygame.display.flip()
        self.__surf.fill(_bg_color)
        if keyboard.is_pressed(self.__exit_key):
            self.__opened = False
            return False
        return self.__opened
    
    @property
    def surf(self):
        return self.__surf
    
    @property
    def size(self) -> list[int]:
        class ws:
            ...
        s = ws()
        s.w = self.__surf.get_width()
        s.h = self.__surf.get_height()
        return s
    
    @property
    def vsync(self) -> bool:
        return self.__vsync
    
    @property
    def fps(self) -> float:
        return int(self.__timer.get_fps())
    
    @fps.setter
    def fps(self, _fps: int):
        self.__fps = _fps
    
    @property
    def title(self) -> str:
        return self.__title
    
    @title.setter
    def title(self, _title: str):
        pygame.display.set_caption(_title)
        self.__title = _title

    @property
    def flags(self) -> WindowFlags:
        return self.__flags
    
    @property
    def whell(self):
        return self.__events.whell