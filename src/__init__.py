class Iterable:
  def __instancecheck__(self, value, instance):
    return "__next__" in dir(value) and "__iter__" in dir(value) and instance == Iterable


class Callable:
  def __instancecheck__(self, value, instance):
    return "__call__" in dir(value) and instance == Iterable


def draise(err): raise err


def final(cls): cls.__init__subclass__ = lambda:draise("cannot implement final class")


