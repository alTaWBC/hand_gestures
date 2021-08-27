import mouse
import time

events = []


def start(events=events):
    mouse.hook(events.append)


def stop(events=events):
    mouse.unhook(events.append)
    
def play(events=events):
    mouse.play(events)

def click(key):
    assert key in ['left', 'right', 'middle']
    mouse.click(key)


def move(right, down, duration=0.1, absolute=False):
    mouse.move(right, down, absolute=absolute, duration=duration)


def scroll(direction, amount):
    assert direction in ['up', 'down']
    scroll = [1, -1][['up', 'down'].index(direction)] * amount
    mouse.wheel(scroll)


def postion():
    return mouse.get_position()


def pressed(key):
    assert key in ['left', 'right', 'middle']
    return mouse.is_pressed(key)

