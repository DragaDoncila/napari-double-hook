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
5. Repeat for writer hooks
6. Attempt multiple `provide_function` implementations and compare behaviour to returning a list of functions
7. Repeat for `add_dock_widget`

## napari_get_reader & napari_get_writer
- All implementations are discovered and shown under the plugin name as defined in setup.py
- The implementations are sorted in reverse alphabetical order of function name (in terms of call order)
- Plugin sorter allows you to pick which implementation you are using, though they are indistinguishable in name - **suggest** saving plugin name + function as the implementation name, and/or allowing dev to pass argument to decorator for what name they'd like to use

## dock_widget and provide_function
- User can return a list of functions and/or dock widgets, both of which are handled appropriately in the GUI
- User CAN declare multiple hook implementations and in such a case, the name of the **returned** function is provided as the GUI title
- Reader and writer should behave similarly, but return the name of the implementation function?


## Notes
This is a set of associated notes regarding plugin development, the cookiecutter template and other potentially relevant but unstructured details discovered throughout the investigation.

1. Writer plugin does not actually have an example.
2. Functional hooks and dock widgets all appear in dock widget? Can be confusing as a dock widget could appear before any layers, but calling a function without layers causes an error.
3. Plugin errors are unreadable in both light and dark theme
4. Exposed entry points appear in the installer even if they don't have any hook implementations
5. Installer shows multiple copies of a plugin, and each entry point is shown as a separate package
6. Uninstalling using the installer doesn't remove the plugin (any of the copies) from the installer, or the hooks from the sorter. Clicking Remove again shows "nothing to uninstall" in status **is this just for editable packages??** 

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
