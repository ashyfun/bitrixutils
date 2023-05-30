from datetime import date, timedelta
from base64 import b64encode


class Define:
    _salt = 'DO_NOT_STEAL_OUR_BUS'
    _template = 'ET73IS41X6IR0T2I5B'
    _how_many_days = 30

    def __init__(self, how_many_days=30):
        if how_many_days > 30:
            self._how_many_days = how_many_days

    def encode(self):
        filled = self._fill_template()
        hash = ''; k = 0; last_index = len(self._salt) - 1
        for i, val in enumerate(filled):
            hash += chr(ord(val) ^ ord(self._salt[k]))
            k += (-k) if k == last_index else 1

        return b64encode(hash.encode('utf8'))

    def _fill_template(self):
        litra = date.today() + timedelta(days=self._how_many_days)
        template = self._template
        for i, val in enumerate(litra.strftime('%Y%m%d')):
            for k, v in enumerate(template):
                unicode = ord(v)
                if unicode > 47 and unicode < 56 and int(v) == i:
                    template = template[:k] + val + template[k + 1:]
                    break

        return template


class AdminPasswordh(Define):
    _salt = 'thRH4u67fhw87V7Hyr12Hwy0rFr'
    _template = 'a6B5Ra42Ka0d3A7Bra1'
