from pywinauto import Application
import time
import random

app = Application().connect(title="Battlefield™ V")
window = app.window(title="Battlefield™ V")

while True:
    
    window.click(coords=(200, 200))
    interval = random.uniform(10, 30)
    print(f"The next click will take place after {interval:.2f} seconds")
    time.sleep(interval)