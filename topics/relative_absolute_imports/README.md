
# Absolute vs Relative Imports

This directory contains a *package* with subpackages in it.
This is to simulate the use of relative and absolute imports. 

We have `function1` in `subpackage1/module2`, and we will import this module from different places in the package. 

Notice that in order that the top-level package will be recognized by Python as a package, you need to be positioned outside of it, and run the scripts in the form `package.subpackage2.module4` 

For example:
```
# These demonstrarte relative imports
# py -m package.subpackage1.module1
# py -m package.subpackage2.module3
# py -m package.subpackage2.nested.module5

# This demonstrate absolute import
# py -m package.subpackage2.module4
```



