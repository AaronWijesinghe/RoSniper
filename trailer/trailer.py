# Code for RoSniper's revamped trailer
# Tested on RoSniper v1.6.0 (no modifications made)

import os
import time
import psutil
import pyautogui

gold = "\033[0;33m"
bold = "\033[1m"
end = "\033[0m"
rsexec = ".venv/bin/python3 rosniper.py"

def type_and_enter(word, secs=0):
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    time.sleep(secs)

def clear():
    print("\033[2J\033[3J\033[H", end='')

def print_wait(msg, secs=0):
    for char in msg:
        print(char, end="", flush=True)
        time.sleep(0.015)
    print()
    time.sleep(secs)

def open_tab():
    pyautogui.keyDown("command")
    time.sleep(0.2)
    pyautogui.press("t")
    pyautogui.keyUp("command")

def close_tab():
    pyautogui.keyDown("command")
    time.sleep(0.2)
    pyautogui.press("w")
    pyautogui.keyUp("command")
    pyautogui.press("enter")

def intro():
    clear()
    print_wait(f"{gold}{bold}Welcome to RoSniper! Here's some of the features it offers.{end}", 1.5)
    print_wait(f"First, let's snipe a player. How about my dearest friend?", 1)
    open_tab()
    type_and_enter(rsexec, 1)
    type_and_enter("awij128", 6)
    for proc in psutil.process_iter():
        if proc.name() == "RobloxPlayer":
            psutil.Process(proc.pid).kill()
    time.sleep(2)
    close_tab()

def monitoring():
    clear()
    time.sleep(0.3)
    print_wait(f"You can {bold}monitor a user's status{end} instead of join-sniping them.", 1)
    print_wait(f"Just type {bold}/m{end} in RoSniper!", 2)
    open_tab()
    type_and_enter(rsexec, 1)
    type_and_enter("/m", 1)
    type_and_enter("awij128", 3)
    close_tab()

def decline_first_server():
    clear()
    time.sleep(0.3)
    print_wait(f"You can also {bold}decline the first server{end} that is found.", 1)
    print_wait("This can be useful when joining a streamer in an already full server.", 1)
    print_wait(f"Just type {bold}/df{end} in RoSniper!", 2)
    open_tab()
    type_and_enter(rsexec, 1)
    type_and_enter("/df", 1)
    type_and_enter("awij128", 3)
    close_tab()

def settings():
    clear()
    time.sleep(0.3)
    print_wait(f"RoSniper offers {bold}a quick and easy way{end} to change settings.", 1)
    print_wait(f"{bold}Type /settings{end} in RoSniper and {bold}type a number{end} to change a setting!", 2)
    open_tab()
    type_and_enter(rsexec, 1)
    type_and_enter("/settings", 1)
    type_and_enter("4", 0.5)
    type_and_enter("5", 0.5)
    close_tab()

NIM_EXAMPLES = [
    "    - Enter a username/Recent User ID to join-snipe that user",
    "    - Use -a[ID] to authenticate with that specific cookie",
    "    - Use -d or -m to enable Decline First Server/Monitoring-Only Mode respectively"
]
def non_interactive_mode():
    clear()
    time.sleep(0.3)
    print_wait(f"We also offer {bold}a non-interactive mode!{end}", 2)
    print_wait(f"You can add command-line arguments to speedily access RoSniper.", 2)
    print_wait("\nFor example, you can:", 1)
    for item in NIM_EXAMPLES:
        print_wait(item, 0.5)
    time.sleep(2)
    print_wait("\nBy the way, arguments can be stacked.", 5)

def changelog_and_cmds():
    clear()
    time.sleep(0.3)
    print_wait(f"To see what's changed after an update, {bold}type /changelog{end} in RoSniper.", 2)
    open_tab()
    type_and_enter(rsexec, 1)
    type_and_enter("/changelog", 1)
    close_tab()
    print_wait(f"Also, you can {bold}type /help{end} to see the command documentation.", 2)
    open_tab()
    type_and_enter(rsexec, 1)
    type_and_enter("/help", 1)
    close_tab()

TECHNICAL_STUFF = [
    "Build of RoSniper displayed: v3.1.0",
    "Shot on macOS 27 Golden Gate (DB4) with no modifications made to RoSniper.py",
    "This trailer was made through 143 lines of Python",
    "    - (I kind of suck at video editing)"
]
def outro():
    clear()
    print(f"{gold}{bold}And that's the end of the trailer!{end}")
    time.sleep(2)
    print_wait("RoSniper has evolved over the past two years, and I wanted to capture all the progress in a short trailer :D", 2)
    print_wait(f"\n{bold}Now, here's some cool technical stuff about this:{end}", 1)
    for item in TECHNICAL_STUFF:
        print_wait(item, 0.5)
    time.sleep(1.5)
    print_wait("\nBuilt by Aaron with lots of love <3", 1)

intro()
monitoring()
decline_first_server()
non_interactive_mode()
settings()
changelog_and_cmds()
outro()