
import re

def kwik(pattern,text,size = 10):
    matches = re.finditer(pattern,text)
    for m in matches:
        span = m.span()
        context = text[span[0]-size : span[1]+size]
        print(re.sub(pattern,'\033[31m\g<0>\033[0m',context))
