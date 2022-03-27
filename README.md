# futureX

A nasty hack package that allows to deploy [python-future](https://github.com/PythonCharmers/python-future) as a single dependency and work on both python 2 and python 3

In more detail, since the original python-future package contains multiple modules that are installed or not by setup.py depending on which version of Python runs the setup and that [symlinks don't actually work cross platform](https://stackoverflow.com/questions/5917249/git-symlinks-in-windows), this                 package allows to have python-future as a packaged dependency that can work out of the box in both Python versions

## Python-Future used Version

At the moment, the source version matches with [v0.18.2](https://github.com/PythonCharmers/python-future/releases/tag/v0.18.2)


## Usage

Make sure that the package is available on the `PYTHONPATH`, either by outside Python if from within a running process

```python
import sys
sys.path.append('path/to/futureX')
```

Then just import futureX first so it builds the paths for the current process, and your are ready to use future and its other modules

```python

import futureX

import future
import past
...

```

You can also alternativelly just get the proper path for current version and do whatever you need to with it

```python
import futureX
future_path = futureX.get_path()
```