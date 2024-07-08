from pythaidate import CsDate
from datetime import timedelta
from .number import num2khom

LUNAR_DAY = "᧡᧢᧣᧤᧥᧦᧧᧨᧩᧪᧫᧬᧭᧮᧯᧱᧲᧳᧴᧵᧶᧷᧸᧹᧺᧻᧼᧽᧾᧿"
NAKSATR = ("ជ្វត", "ឆ្លូ", "ខា្ល", "ថោះ", "មរោ្ង", "មសេ្ង", "មមើ្យ", "មមេ", "វ្អក", "រកា", "ច្អ", "កុន")

class KhomDate(CsDate):

    def __str__(self):
        weekday = self.csweekday()
        if weekday == 0:
            weekday = 7
        weekday = num2khom(weekday)
        day = LUNAR_DAY[self.day - 1]
        month = self.month
        if self.leap_month:
            if month == 8:
                month = '᧠'
            elif month == 88:
                month = '᧰'
            else:
                month = num2khom(month)
        else:
            month = num2khom(month)
        year = self.year
        idx = (year + 11) % 12
        if idx == 0:
            idx = 12
        naksatr = NAKSATR[idx - 1]
        year = num2khom(year)
        return f"{weekday}{day}{month} បី{naksatr} ចុលសករាជ {year}"

    def __add__(self, other):
        if isinstance(other, timedelta):
            return KhomDate.fromjulianday(self.julianday + other.days)
        return NotImplemented
