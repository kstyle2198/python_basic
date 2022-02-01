
import time
import keyboard

i = 1
while True:
    if keyboard.is_pressed('q'):
        print("quit")
        break

    print(f"hello{i}")
    i += 1
    if i == 10000:
        quit()
