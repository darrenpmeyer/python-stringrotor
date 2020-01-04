import stringrotor.rotorwheel as rotorwheel


class StringRotor(object):
    def __init__(self, rotors=[], *args, **kwargs):
        assert isinstance(rotors, list)
        self.rotors = []
        for rotor in rotors:
            self.add_wheel(rotor)

    def add_wheel(self, wheel):
        assert isinstance(wheel, rotorwheel.RotorWheel)
        self.rotors.insert(0, wheel)

        # make this the nextwheel of the previous rotor, unless it's the first rotor
        if len(self.rotors) > 1:
            self.rotors[1].nextwheel = self.rotors[0]

        return self

    def tick(self, steps=1):
        self.rotors[-1].increment(steps)
        return self

    def as_str(self, sep=''):
        outstr = sep.join([str(x) for x in self.rotors])
        return outstr

    def __str__(self):
        return self.as_str()
