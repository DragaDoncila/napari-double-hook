# napari-double-hook

[![License](https://img.shields.io/pypi/l/napari-double-hook.svg?color=green)](https://github.com/DragaDoncila/napari-double-hook/raw/master/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-double-hook.svg?color=green)](https://pypi.org/project/napari-double-hook)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-double-hook.svg?color=green)](https://python.org)
[![tests](https://github.com/DragaDoncila/napari-double-hook/workflows/tests/badge.svg)](https://github.com/DragaDoncila/napari-double-hook/actions)
[![codecov](https://codecov.io/gh/DragaDoncila/napari-double-hook/branch/master/graph/badge.svg)](https://codecov.io/gh/DragaDoncila/napari-double-hook)

Testing behaviour of plugins with multiple implementations of the same hook

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using with [@napari]'s [cookiecutter-napari-plugin] template.

## Testing Plan
1. Add implementation for two reader hooks which open the same image (using two different I/O functions e.g. tifffile and skimage imread). Add console messages
to distinguish between the two implementations
2. Install plugin and identify which (if any) of the implementations is being used, whether this can be changed (and how), any error messages arising
3. Check the appearance of both hooks (if they appear) in the GUI plugin installer
4. Attempt returning list of implementations similar to the current `provide_function` solution
5. Repeat for writer hooks
6. Attempt multiple `provide_function` implementations and compare behaviour to returning a list of functions
7. Repeat for `add_dock_widget`

## Installation

You can install `napari-double-hook` via [pip]:

    pip install napari-double-hook

## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [MIT] license,
"napari-double-hook" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin
[file an issue]: https://github.com/DragaDoncila/napari-double-hook/issues
[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
