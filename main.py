# https://stackoverflow.com/questions/2685435/cooler-ascii-spinners
# https://raw.githubusercontent.com/sindresorhus/cli-spinners/master/spinners.json
from time import sleep
import json

def load_spinners():
    with open('spinners.json', 'r', encoding='utf-8') as f:
        spinners = json.load(f)

    return spinners

def animate_spinner(spinner_name = 'arc'):
    spinner = load_spinners()[spinner_name]
    frames = spinner['frames']
    interval = int(spinner['interval']) / 1000
    for frame in frames:
        print(frame, end = '\r')
        sleep(interval)

animate_spinner(spinner_name='material')
