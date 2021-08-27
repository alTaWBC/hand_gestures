import pandas as pd
from pynput import keyboard, mouse


def mouse_click(x, y, button, pressed):
    print(x, y, button, pressed)


def mouse_move(x, y):
    print(x, y)


def mouse_scroll(x, y, dx, dy):
    print(x, y, dx, dy)


mouse_listener = mouse.Listener(
    on_click=mouse_click,
    on_move=mouse_move,
    on_scroll=mouse_scroll
)


def keyboard_press(key):
    try:
        key = key.char
    except:
        print('Cannot convert to char')
    print('pressed', key)


def keyboard_release(key):
    try:
        key = key.char
    except:
        print('Cannot convert to char')
    print('released', key)


keyboard_listener = keyboard.Listener(
    on_press=keyboard_press,
    on_release=keyboard_release
)
