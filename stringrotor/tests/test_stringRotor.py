from unittest import TestCase
from stringrotor import StringRotor, RotorWheel


class TestStringRotor(TestCase):
    def test_integration_clock(self):
        testobj = StringRotor()
        testobj.add_wheel(RotorWheel([str(x) for x in range(0, 9)]))  # minute 1
        testobj.add_wheel(RotorWheel([str(x) for x in range(0, 5)]))  # minute 10
        testobj.add_wheel(RotorWheel([str(x) + ':' for x in range(0, 23)]))  # hour

        self.assertEqual('0:00', str(testobj))  # should start here.

        testobj.tick()
        self.assertEqual('0:01', str(testobj))

        # for i in range(1,40):
        #     testobj.tick()
        #     print('{:2d}: {}'.format(i, str(testobj)))

        testobj.tick(40)
        self.assertEqual('0:41', str(testobj))

        testobj.tick(120)
        self.assertEqual('2:41', str(testobj))

        testobj.tick(23 * 60)
        self.assertEqual('1:41', str(testobj))

    # def test_add_wheel(self):
    #     self.fail()
    #
    # def test_tick(self):
    #     self.fail()
    #
    # def test_as_str(self):
    #     self.fail()
