class FizzBuzzer:

    @staticmethod
    def run_for(number):
        if not isinstance(number, int):
            raise Exception("not a number")
        number = int(number)
        if number % 15 == 0:
            return 'fizzbuzz'
        elif number % 3 == 0:
            return 'fizz'
        elif number % 5 == 0:
            return 'buzz'
        else:
            return number
