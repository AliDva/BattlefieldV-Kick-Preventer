from pywinauto import Application 
import time
import random

app = Application().connect(title="Battlefield™ V")
window = app.window(title="Battlefield™ V")


while True:
    


    
    # 最小化窗口
    window.minimize()

    # 后台点击
    window.click(button='left', pressed='', coords=(1250, 1253), double=False, absolute=False)
    window.click(button='left', pressed='', coords=(222, 1339), double=False, absolute=False)

    # 等待一段时间
    interval = random.uniform(150, 160) #随机休眠150-160秒，如果你想要更高请自行更改
    print(f"下一次点击将在 {interval:.2f} 秒后进行")
    time.sleep(interval)
