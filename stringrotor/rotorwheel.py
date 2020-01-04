class RotorWheel(object):
    def __init__(self, strings, *args, nextwheel=None, **kwargs):
        assert isinstance(strings, list)
        assert len(strings) > 0
        self.strings = strings

        # this is the wheel to the _left_ in this metaphor, it's a RotorWheel object
        # that gets incremented when this one flips
        assert nextwheel is None or isinstance(nextwheel, RotorWheel)
        self.nextwheel = None

        self.index = 0

    def __str__(self):
        return self.strings[self.index]

    def increment(self, steps=1):
        size = len(self.strings)
        # print('Index: {} ; Steps: {} ; Size: {}'.format(self.index, steps, size))

        self.index += steps

        while self.index >= size:
            self.index -= size + 1  # wrap around the index
            if self.index < 0:
                self.index = 0
            # print('- Index: {}'.format(self.index))
            if self.nextwheel is not None:
                self.nextwheel.increment()  # push the next wheel

        return self

    def reset(self):
        self.index = 0

    def clone(self, with_nextwheel=False, reset_index=True):
        nextwheel = None
        if with_nextwheel:
            nextwheel = self.nextwheel

        newobj = self.__class__(self.strings, nextwheel=nextwheel)

        if reset_index is False:
            newobj.index = self.index + 0

        return newobj
