import re
import datetime
from django.utils.html import strip_tags
import math


def WordCount(html_string):
    word_string = strip_tags(html_string)
    count = len(re.findall(r'\w+', word_string))
    return count


def readTime(html_string):
    count = WordCount(html_string)
    read_min = math.ceil(count / 200)
    # read_sec = read_min * 60
    # read_time = str(datetime.timedelta(minutes=read_min))
    return str(read_min)
