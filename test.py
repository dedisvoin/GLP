from src.app import *
from src.functs import *
from src.shapes import *
from src.mouse import *
from src.events import *

a = App(_size = [1000, 600], _flags = WindowFlags.RESIZE)
events = EventLoop()
events.add(Event(Event.Types.MOUSE_CLICK, 'id_1').btn(Mouse.Button.BTN_LEFT))
events.add(Event(Event.Types.MOUSE_CLICK, 'id_2').btn(Mouse.Button.BTN_RIGHT))

@AppProcess(a, True)
def render(delta):
    a.title = f'fps {a.fps} delta {delta}'

    events.update()
    print(events.get('id_1'), events.get('id_2'))

a.run()