import pandas as pd
from pynput import keyboard, mouse
import time
from keyboard import release

columns = ['Controller', 'Type', 'Button',
           'Coordinates', 'ScrollDirection', 'Time']
events = pd.DataFrame(columns=columns)

mouse_controller = mouse.Controller()
keyboard_controller = keyboard.Controller()

position = mouse_controller.position
mouse_listener = mouse.Listener(
    on_click=mouse_click,
    on_move=mouse_move,
    on_scroll=mouse_scroll
)
keyboard_listener = keyboard.Listener(
    on_press=keyboard_press,
    on_release=keyboard_release
)


def clear():
    global events, position
    position = mouse_controller.position
    events = pd.DataFrame(columns=columns).append({
        'Controller': 'Mouse',
        'Type': 'Initial',
        'Button': 'None',
        'Coordinates': position,
        'ScrollDirection': (0, 0),
        'Time': time.time()
    }, ignore_index=True)
    create_listeners()


def mouse_click(x, y, button, pressed):
    global events, position
    events = events.append({
        'Controller': 'Mouse',
        'Type': 'Press' if pressed else 'Release',
        'Button': button,
        'Coordinates': (x-position[0], y-position[1]),
        'ScrollDirection': (0, 0),
        'Time': time.time()
    }, ignore_index=True)
    position = (x, y)


def mouse_move(x, y):
    global events, position
    events = events.append({
        'Controller': 'Mouse',
        'Type': 'Move',
        'Button': 'None',
        'Coordinates': (x-position[0], y-position[1]),
        'ScrollDirection': (0, 0),
        'Time': time.time()
    }, ignore_index=True)
    position = (x, y)


def mouse_scroll(x, y, dx, dy):
    global events, position
    events = events.append({
        'Controller': 'Mouse',
        'Type': 'Scroll',
        'Button': 'None',
        'Coordinates': (x-position[0], y-position[1]),
        'ScrollDirection': (dx, dy),
        'Time': time.time()
    }, ignore_index=True)
    position = (x, y)


def keyboard_press(key):
    global events
    events = events.append({
        'Controller': 'Keyboard',
        'Type': 'Press',
        'Button': key,
        'Coordinates': (0, 0),
        'ScrollDirection': (0, 0),
        'Time': time.time()
    }, ignore_index=True)


def keyboard_release(key):
    global events
    events = events.append({
        'Controller': 'Keyboard',
        'Type': 'Release',
        'Button': key,
        'Coordinates': (0, 0),
        'ScrollDirection': (0, 0),
        'Time': time.time()
    }, ignore_index=True)


def create_listeners():
    global mouse_listener, keyboard_listener
    mouse_listener = mouse.Listener(
        on_click=mouse_click,
        on_move=mouse_move,
        on_scroll=mouse_scroll
    )
    keyboard_listener = keyboard.Listener(
        on_press=keyboard_press,
        on_release=keyboard_release
    )


def start():
    clear()
    mouse_listener.start()
    keyboard_listener.start()


def stop():
    mouse_listener.stop()
    keyboard_listener.stop()


def play():
    previous = -1
    for _, line in events.iterrows():
        waitTime = line.Time - previous if previous != -1 else 0
        previous = line.Time
        event_controller = line.Controller
        time.sleep(waitTime)
        if event_controller == 'Mouse':
            playMouse(line.Type, line.Button,
                      line.Coordinates, line.ScrollDirection)
        elif event_controller == 'Keyboard':
            playKeyboard(line.Type, line.Button)
    keyboard_controller.release(keyboard.Key.shift)
    # TODO: REMOVE WHEN USING BUTTONS


def playMouse(types, button, coordinates, scroll):
    if types == 'Initial':
        mouse_controller.move(
            coordinates[0] - mouse_controller.position[0], coordinates[1] - mouse_controller.position[1])
    else:
        mouse_controller.move(coordinates[0], coordinates[1])
        if types == 'Press':
            mouse_controller.press(button)
        elif types == 'Release':
            mouse_controller.release(button)
        elif types == 'scroll':
            mouse_controller.scroll(scroll[0], scroll[1])
        elif types == 'Move':
            pass
        else:
            print(types, 'is not supported')


def playKeyboard(types, button):
    if types == 'Press':
        keyboard_controller.press(button)
    elif types == 'Release':
        keyboard_controller.release(button)
    else:
        print(types, 'is not supported')
