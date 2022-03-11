from collections import namedtuple


def create_named_tuple(name, *values):
  return namedtuple(name, values)(*values)
