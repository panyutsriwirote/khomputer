TH2NUM = str.maketrans("๐๑๒๓๔๕๖๗๘๙", "0123456789")
NUM2KH = str.maketrans("0123456789", "០១២៣៤៥៦៧៨៩")

def thai2num(th_num: str):
    if '.' in th_num:
        cls = float
    else:
        cls = int
    return cls(th_num.translate(TH2NUM))

def num2khom(i: int | float):
    return str(i).translate(NUM2KH)
