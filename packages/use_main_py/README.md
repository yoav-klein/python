# Use __main__.py
---

The `__main__.py` file allows you to provide a command-line interface for your package.

Consinder we have a `calculator` package, which one can import and use as such:
```
import calculator

calculator.add(1, 3)
calculator.mult(3, 6)

...
```

Now let's say I want to enable the user do quick add operations from the command-line:
```
$ python3 -m calculator 1 4
5
```

Try it, run the above command exactly as its written from the current directory.

