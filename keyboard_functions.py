# https://www.thepythoncode.com/article/control-keyboard-python
import keyboard
import time

events = []


def pressed(key):
    return keyboard.is_pressed(key)


def press(key):
    keyboard.send(key)


def combination(keys):
    keyboard.send('+'.join(keys))


def hold(key):
    keyboard.press(key)


def release(key):
    keyboard.release(key)


def write(text, delay=0.1):
    keyboard.write(text, delay=delay)


def start(events=events):
    keyboard.hook(events.append)


def stop(events=events):
    keyboard.unhook(events.append)


def play(events=events):
    keyboard.play(events)
