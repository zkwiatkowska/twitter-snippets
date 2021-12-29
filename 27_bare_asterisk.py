def dummy_func(a, *, b):
    print(a, b)


dummy_func(a="a", b="b")  # correct call, prints "a b"
dummy_func("a", b="b")    # correct call, prints "a b"
dummy_func("a", "b")      # TypeError: dummy_func() takes 1 positional argument but 2 were given
dummy_func("a")           # TypeError: dummy_func() missing 1 required keyword-only argument: 'b'
