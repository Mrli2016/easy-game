# -*- coding: utf-8 -*-

def subtime(starttime, endtime, to_sec=False):
    """
    计算两个时间差
    参数starttime为开始时间、参数endtime为结束时间、参数to_sec为精确计算到秒数
    返回时间差的中文描述
    """
    if starttime == 0:
        return "0" + u"秒"
    time_span = endtime - starttime
    tmp = int(time_span / 86400)
    ret = ""
    if tmp != 0:
        ret = str(tmp).replace("-", "") + u"天"
        time_span -= tmp * 86400
    tmp = int(time_span / 3600)
    if tmp != 0:
        ret += str(tmp).replace("-", "") + u"时"
        time_span -= tmp * 3600
    tmp = int(int(time_span) / 60)
    # if tmp != 0:
    if not to_sec and not ret:
        ret += str(tmp).replace("-", "") + u"分钟"
    else:
        ret += str(tmp).replace("-", "") + u"分"
    if to_sec:
        ret += str(int(time_span) % 60).replace("-", "") + u"秒"
    return ret