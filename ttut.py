r"""MIT License

Copyright (c) 2019 Wiktor Zając

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""

import os
import time

colors = {
    "reset": "\u001b[0m",
    "black": "\u001b[30m",
    "red": "\u001b[31m",
    "green": "\u001b[32m",
    "yellow": "\u001b[33m",
    "blue": "\u001b[34m",
    "magenta": "\u001b[35m",
    "cyan": "\u001b[36m",
    "white": "\u001b[37m",
    "b_black": "\u001b[30;1m",
    "b_red": "\u001b[31;1m",
    "b_green": "\u001b[32;1m",
    "b_yellow": "\u001b[33;1m",
    "b_blue": "\u001b[34;1m",
    "b_magenta": "\u001b[35;1m",
    "b_cyan": "\u001b[36;1m",
    "b_white": "\u001b[37;1m",
    "bg_black": "\u001b[40m",
    "bg_red": "\u001b[41m",
    "bg_green": "\u001b[42m",
    "bg_yellow": "\u001b[43m",
    "bg_blue": "\u001b[44m",
    "bg_magenta": "\u001b[45m",
    "bg_cyan": "\u001b[46m",
    "bg_white": "\u001b[47m",
    "bg_b_black": "\u001b[40;1m",
    "bg_b_red": "\u001b[42;1m",
    "bg_b_yellow": "\u001b[43;1m",
    "bg_b_blue": "\u001b[44;1m",
    "bg_b_magenta": "\u001b[45;1m",
    "bg_b_cyan": "\u001b[46;1m",
    "bg_b_white": "\u001b[47;1m",
    "bold": "\u001b[1m",
    "underline": "\u001b[4m",
    "reversed": "\u001b[7m",
    "default": "\u001b[0m"
}

allowed_list = (str, int, float)
ERROR = "ERROR"
WARN = "WARN"
INFO = "INFO"
log_file = "log.log"


def log(text, log_type="INFO"):
    try:
        if type(text) in allowed_list:
            pass
        else:
            raise AttributeError()
    except AttributeError:
        raise AttributeError()
    try:
        f = open(log_file, "a")
    except PermissionError:
        raise PermissionError(f"Can't get access to '{log_file}' file")
    f.write(f"[{log_type}] [{time.ctime(time.time())}] {text}\n")
    if log_type == "INFO":
        print(formatText(f"[bold][b_white]INFO[reset] {text}"))
    elif log_type == "WARN":
        print(formatText(f"[bold][bg_b_yellow]WARN[reset] {text}"))
    elif log_type == "ERROR":
        print(formatText(f"[bold][bg_red]ERROR[reset] {text}"))


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def formatText(text):
    os.system("")
    text = text + "[reset][default]"
    for color in colors:
        text = text.replace("[" + color + "]", colors[color])
    return text
