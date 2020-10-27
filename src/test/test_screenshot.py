# -*- coding: utf-8 -*-

import os
import sys
import time
from PIL import ImageGrab, Image
from collections import Counter
# from pymouse import PyMouse

folderpath = "./screen/"
# left, bottom = 974, 505
# width, height = 660, 140

left, bottom = 700, 1255

width, height = 660, 140

bbox = (left, bottom, left + width, bottom + height)

def pointColor(x, y):
    return ImageGrab.grab().load()[x, y]

def screenRegionImg():
    return ImageGrab.grab(bbox)

def screenRegion():
    try:
        img = ImageGrab.grab(bbox)
        newfilename = "{}{}.png".format(folderpath, int(time.time() * 1000))
        img.save(newfilename)
        print("screen saved! " + newfilename)
        return newfilename
    except Exception as e:
        print("error:",e)

def readImage(filename):
    image = Image.open(filename)
    return image.getcolors()

if __name__ == '__main__':
    # 每1s截图一次,截图15分钟
    count = 0
    screenRegion()
    # max_count = 15 * 60
    #
    # while count < max_count:
    #     screenRegion()
    #     count += 1
    #     time.sleep(1)

    # bbox = (left, bottom + 50, left + width - 22, bottom + 51)
    # screen_start_time = time.time() * 1000
    # # screenRegionImg()
    # pointColor(left, bottom)
    # screen_end_time = time.time() * 1000
    # print(screen_end_time - screen_start_time)

    # while count < 240:
    #     colors = []
    #     image = screenRegionImg()
    #
    #     img_array = image.load()
    #
    #     if color_num != 9:
    #         y = 50
    #         color = img_array[1, y]
    #         color_num = 0
    #         last_color = color
    #         for x in range(9, width - 22 - 9):
    #             color_x_y = img_array[x, y]
    #             if color_x_y != last_color and color_x_y != color:
    #                 color_num += 1
    #             last_color = color_x_y
    #     if color_num == 0:
    #         break
    #
    #     num = color_num * color_num
    #     per_x = width / color_num
    #     per_y = height / color_num
    #     start_x = per_x / 2
    #     start_y = per_y / 2
    #
    #     for j in range(0, num):
    #         x = start_x + (j % color_num) * per_x
    #         y = start_y + (j / color_num) * per_y
    #         this_color = img_array[x, y]
    #         colors.append(this_color)
    #
    #     dict_different_color = Counter(colors)
    #     # print(dict_different_color)
    #     index = 0
    #     for key in dict_different_color.keys():
    #         if dict_different_color[key] == 1:
    #             index = colors.index(key)
    #     click_x = left + start_x + (index % color_num) * per_x
    #     click_y = bottom + start_y + (index / color_num) * per_y
    #
    #     command = 'click -x ' + str(click_x / 2) + ' -y ' + str(click_y / 2)
    #     os.system(command)
    #     count += 1
    # print(count)