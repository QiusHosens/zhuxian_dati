# -*- coding: utf-8 -*-

import os
import pyperclip

input_pos_start = [200, 1255]
input_paste_end = [200, 705]
input_send = [700, 1255]
command = 'click -x ' + str(input_pos_start[0] / 2) + ' -y ' + str(input_pos_start[1] / 2)
pyperclip.copy("hello world")
pyperclip.paste()
os.system(command)
