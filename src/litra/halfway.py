from datetime import datetime, timedelta
from base64 import b64encode, b64decode

from bitrixutils.litra.exceptions import LitraException


class Define:
    _salt = 'DO_NOT_STEAL_OUR_BUS'
    _template = 'ET73IS41X6IR0T2I5B'
    _how_many_days = 30

    def __init__(self, how_many_days=30):
        if how_many_days > 30:
            self._how_many_days = how_many_days

    def encode(self):
        template = self._fill_template()
        return b64encode(
            self._convert(template).encode('utf8')
        )

    def decode(self, encoded):
        template = self._convert(
            b64decode(encoded).decode('utf8')
        )
        return self._extract_from_template(template)

    def _convert(self, target):
        k = 0
        converted = ''
        last_index = len(self._salt) - 1
        for i, val in enumerate(target):
            converted += chr(ord(val) ^ ord(self._salt[k]))
            k += (-k) if k == last_index else 1

        return converted

    def _fill_template(self):
        litra = datetime.today() + timedelta(days=self._how_many_days)
        template = self._template
        for i, val in enumerate(litra.strftime('%Y%m%d')):
            for k, v in enumerate(template):
                unicode = ord(v)
                if 47 < unicode < 56 and int(v) == i:
                    template = template[:k] + val + template[k + 1:]
                    break

        return template

    def _extract_from_template(self, template):
        if len(template) != len(self._template):
            raise LitraException('template not compatible with hash')

        litra = [''] * 8
        for i, v in enumerate(template):
            index = ord(self._template[i])
            unicode = ord(v)
            if 47 < index < 56 and 47 < unicode < 58:
                litra[int(self._template[i])] = v

        return datetime.strptime(''.join(litra), '%Y%m%d').date()


class AdminPasswordh(Define):
    _salt = 'thRH4u67fhw87V7Hyr12Hwy0rFr'
    _template = 'a6B5Ra42Ka0d3A7Bra1'
