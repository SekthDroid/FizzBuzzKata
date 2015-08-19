__author__ = 'SekthDroid'


class FizzBuzz(object):
    def execute(self, param):
        if param % 3 is 0:
            return "fizz"

        if param % 5 is 0:
            return "buzz"

        return param