class Foo:
    def __init__(self):
        self.val = 0


def func1(foo, bar):
    print(foo.val)
    foo.val = 5  # change also affects caller
    print(foo.val)
    bar[2] = 4 # change also affects caller


def main():
    foo = Foo()
    bar = [1, 2, 3]
    func1(foo, bar)
    print(bar)
    print(foo.val)
    print(bar)


if __name__ == '__main__':
    main()
