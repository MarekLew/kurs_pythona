_print = print


def print(*arg, **kwarg):
    _print(*arg, **kwarg)
    breakpoint()
