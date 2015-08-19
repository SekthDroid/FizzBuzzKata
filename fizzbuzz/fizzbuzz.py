__author__ = 'SekthDroid'


class FizzBuzz(object):
    def execute(self, param, variations=None):
        result = ""
        if variations is not None:
            for key, value in variations.items():
                if param % value is 0:
                    result += key
        else:
            if param % 3 is 0:
                result += "fizz"

            if param % 5 is 0:
                result += "buzz"

            if param % 7 is 0:
                result += "pop"

        return result if len(result) > 0 else param