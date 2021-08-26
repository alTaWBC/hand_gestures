import mouse

print(mouse.get_position())

mouse.click('left')
mouse.click('right')
mouse.drag(0, 0, 100, 100, absolute=False, duration=0.1)
events = mouse.record()
mouse.play(events[:-1])