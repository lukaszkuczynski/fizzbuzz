from unittest import TestCase, main
from fizzbuzzer import FizzBuzzer

class FizzBuzzTest(TestCase):

    def setUp(self):
        self.sut = FizzBuzzer()


    def test_for_3_returns_fizz(self):
        actual = self.sut.run_for(3)
        self.assertEquals(actual, 'fizz')

if __name__ == '__main__':
    main()