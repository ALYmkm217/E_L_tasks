#!/usr/bin/python3

import time
import pyautogui

# Open Visual Studio Code
pyautogui.hotkey("win", "s")  # Opens the Windows search bar
time.sleep(1)
pyautogui.write("Vs")
pyautogui.press("enter")
time.sleep(2)  # Wait for VSCode to open

# Open Extensions Marketplace
pyautogui.hotkey("ctrl", "shift", "x")

extensions = [
    "clangd",
    "C/C++ TestMate",
    "C/C++ Helper",
    "CMake",
    "CMake Tools"
]

for extension in extensions:
    pyautogui.tripleClick(247,158)
    time.sleep(0.2)
    pyautogui.write(f" {extension}")
    pyautogui.click(387,249)
    time.sleep(3)  # Wait for installation to complete

print("Extensions installed successfully.")
