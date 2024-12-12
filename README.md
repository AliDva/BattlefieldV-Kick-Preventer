# Battlefield-Kick-Preventer

This toolkit prevents idle kicks in Battlefield V.

## Requirements 

Python: 3.x (The test passed in 3.10) 

`pywinauto` library

To install `pywinauto`, use the following command:

```
pip install pywinauto
```

## How to Run
**Make sure the autoclick.bat and the autoclick.py are in the same path**

Click on [autoclick.bat](https://github.com/SY-Ch/Battlefield-Kick-Preventer/blob/main/autoclick.bat) to start the program.

If you're using Anaconda, make sure to activate the virtual environment in the batch file.

UPdate 2024-12-12
Now BFV will no longer pop up to the foreground, you need to run BFV in window mode to use this script properly. to update
现在bfv将不再弹出到前台，你需要以窗口模式运行bfv才能正常使用此脚本。

Known issue: Although the BFV window no longer pops up, it will be placed in the foreground. This does not affect your ability to play other games, but it will disconnect your mouse and keyboard from the game you are currently playing. You need to click again or Tab+Alt to switch to the game you are currently playing.
已知的问题：虽然bfv窗口不再弹出但是会将bfv窗口放置到前台。这不影响你游玩其他游戏，但是会将你的鼠标和键盘与你正在玩的游戏断开链接。你需要重新点击或Tab+Alt切换到你正在玩的游戏才行。
