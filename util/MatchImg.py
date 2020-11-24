import aircv as ac

def matchImg(imgsrc, imgobj, confidence=None):  # imgsrc=原始图像，imgobj=待查找的图片
    """

    :rtype: object
    """
    imsrc = ac.imread(imgsrc)
    imobj = ac.imread(imgobj)
    if confidence:
        match_result = ac.find_template(imsrc, imobj, confidence)
    else:
        match_result = ac.find_template(imsrc, imobj)
    # print(imgobj, match_result)
    # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
    if match_result is not None:
        # print(match_result)
        match_result['shape'] = (imsrc.shape[1], imsrc.shape[0])  # 0为高，1为宽

        # print(imobj, match_result)
    return match_result