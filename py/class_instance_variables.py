class Foo:
    class_var = 5

    def __init__(self):
        self.instance_var = 10


if __name__ == '__main__':
    assert Foo.class_var == 5  # access class variable
    try:
        print(Foo.instance_var)
    except AttributeError:
        print('Cannot access instance variable at the class level')

    foo = Foo()
    assert foo.class_var == 5  # access class variable from instance

    new_foo = Foo()
    assert new_foo.class_var == 5

    Foo.class_var = 7  # change the class variable at the class scope
    assert foo.class_var == 7
    assert new_foo.class_var == 7

    foo.class_var = 9  # re-bound the name 'class_var' within the instance's scope
    assert Foo.class_var == 7  # class variable remains unchanged
    assert foo.class_var == 9  # `class_var` is in the scope of foo, not Foo
    assert new_foo.class_var == 7
