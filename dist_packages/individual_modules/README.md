# Modules Package example
---

This demonstrate a package that contains individual modules.

In order to include individual modules in your package, you need to specify in the `py_modules`
field what modules you want to include.
In this exmaple, we include `kuku` and `bar`

```
 package_dir={"": "src"},
 py_modules = ["kuku", "bar"],
```

So after running
```
$ py -m pip install .
```
You can see that you can

```
$ py -m kuku
$ py -m bar
```

But you can't
```
$ py -m foo
```