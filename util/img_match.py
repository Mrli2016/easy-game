#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import cv2
import numpy as np


# 找图 返回最近似的点
def search_img(img, template, threshold=0.9, debug=False, gray=0):
    """
    在大图中找小图
    :param img: 大图
    :param template: 小图
    :param threshold: 相似度 1为完美 -1为最差
    :param debug: 是否显示图片匹配情况，True会框选出匹配项
    :param gray: 是否灰度匹配
    :return:
    """
    if gray == 0:
        color_mode = cv2.IMREAD_COLOR
    else:
        color_mode = cv2.COLOR_BGR2GRAY

    img = cv2.cvtColor(img, color_mode)
    template = cv2.cvtColor(template, color_mode)
    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)

    # res大于70%
    loc = np.where(result >= threshold)
    # 使用灰度图像中的坐标对原始RGB图像进行标记
    point = ()
    for pt in zip(*loc[::-1]):
        template_size = template.shape[:2]
        cv2.rectangle(img, pt, (pt[0] + template_size[1], pt[1] + + template_size[0]), (7, 249, 151), 2)
        point = pt
    if point == ():
        return None
    if debug:
        cv2.circle(img, (int(point[0]), int(point[1])), 3, (0, 0, 255), 0)
        cv2.imshow("image", img)
        cv2.waitKey(0)
    return point[0], point[1]


if __name__ == '__main__':
    scale = 1

    test_img = cv2.imread('../images/liaoyan/test.png')  # 要找的大图
    # img = cv2.resize(img, (0, 0), fx=scale, fy=scale)

    test_template = cv2.imread('../images/liaoyan/num3.png')  # 图中的小图
    # template = cv2.resize(template, (0, 0), fx=scale, fy=scale)

    point_color = (0, 0, 255)
    x, y = search_img(test_img, test_template, threshold=0.9, debug=True)
    cv2.circle(test_img, (int(x), int(y)), 3, point_color, 0)
    # cv2.imshow("image", img)
    # cv2.waitKey(0)
    if test_img is None:
        print("没找到图片")
    else:
        print("找到图片 位置:" + str(x) + " " + str(y))
