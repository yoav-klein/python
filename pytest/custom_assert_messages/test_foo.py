from foo import Foo

def test_foo():
    foo1 = Foo(1)
    foo2 = Foo(2)

    assert foo1 == foo2