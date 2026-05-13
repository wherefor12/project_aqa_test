class Practice:
    numbers = list(range(1, 8))
    for n in numbers:
        print(n)
        if n == 5:
            break

    words = [f"str{i}" for i in range(10)]
    for word in words:
        print(word)

import random
import time

class Rostics_Load:
    def monitor_load(self):
        i = 0
        while i < 10:
            load = random.randint(0, 100)
            if load > 85:
                print("Нагрузка больше 85%")
                time.sleep(0.2)
                i = i + 1
monitor = Rostics_Load()
monitor.monitor_load()              


