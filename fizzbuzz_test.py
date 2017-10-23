from unittest import TestCase, main
from fizzbuzzer import FizzBuzzer


class FizzBuzzTest(TestCase):

    def setUp(self):
        self.sut = FizzBuzzer()

    def test_for_3_returns_fizz(self):
        actual = self.sut.run_for(3)
        self.assertEquals(actual, 'fizz')

    def test_for_5_returns_buzz(self):
        actual = self.sut.run_for(5)
        self.assertEquals(actual, 'buzz')

    def test_for_15_returns_fizzbuzz(self):
        actual = self.sut.run_for(15)
        self.assertEquals(actual, 'fizzbuzz')

    def test_for_other_return_this_number(self):
        actual = self.sut.run_for(4)
        self.assertEquals(actual, 4)

    def test_for_other_input_raise_exception(self):
        try:
            self.sut.run_for("zzz")
            self.fail("should throw an exception")
        except Exception as e:
            print(e)
            pass


if __name__ == '__main__':
    main()