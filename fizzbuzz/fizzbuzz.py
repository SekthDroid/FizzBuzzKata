__author__ = 'SekthDroid'


class FizzBuzz(object):
    def execute(self, param):
        result = ""
        if param % 3 is 0:
            result += "fizz"

        if param % 5 is 0:
            result += "buzz"

        if param % 7 is 0:
            result += "pop"

        return result if len(result) > 0 else param