from collections import OrderedDict

__author__ = 'SekthDroid'


class FizzBuzz(object):
    variations = OrderedDict()
    variations["fizz"] = 3
    variations["buzz"] = 5
    variations["pop"] = 7

    def execute(self, param, variations=None):
        result = ""
        variations = variations if variations else self.variations
        for key, value in variations.items():
            result += key if param % value is 0 else ""

        return result if len(result) > 0 else param