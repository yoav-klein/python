
# Entry Points
---

Entry points in setuptools are used for 2 main purposes:
1. Provide a convenient command-line interface for the package
2. Provide an interface for plugins

We'll demonstrate the use of the first use-case.

So we have a package named `calculator`, which the user can import in his Python code as such:
```
>>> from calculator import calculator
>>> calculator.add(2, 5)
>>> calculator.mult(5, 7)
...
```

But we want to enable the user to run quick addition operations from the command-line, as such:
```
$ add 5 6
11
```

This is why we use entrypoints.

We have our `calculator` module which holds the actual calculator functions.
Now what we do is add another module named `console.py` (we don't have to do it this way, but it is organized well), 
in which we define a function `main` which reads the input from the console, and sends it to the `calculator.add` function.

Now the important part: we define in our `setup.py`:

```
...
entry_points={
        'console_scripts': [
            'add = calculator.console:main',
        ]
    }
...
```

The syntax for entrypoints is as such:
```
<name> = <package_or_module>[:<object>[.<attr>[.<nested-attr>]*]]
```

Package or module in our case is the module `calculator.console`
Object in our case is the function `main`