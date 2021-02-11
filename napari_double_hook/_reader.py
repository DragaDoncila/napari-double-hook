"""
This module is an example of a barebones numpy reader plugin for napari.

It implements the ``napari_get_reader`` hook specification, (to create
a reader plugin) but your plugin may choose to implement any of the hook
specifications offered by napari.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below accordingly.  For complete documentation see:
https://napari.org/docs/dev/plugins/for_plugin_developers.html
"""
import numpy as np
from napari_plugin_engine import napari_hook_implementation
from skimage.io import imread

@napari_hook_implementation(specname="napari_get_reader")
def load_delayed(path: str):
    print("Loading delayed...")
    return reader_function

@napari_hook_implementation(specname="napari_get_reader")
def load_immediate(path:str):
    print("Loading immediate...")
    return reader_function

@napari_hook_implementation(specname="napari_get_reader")
def load_partial(path:str):
    print("Loading partial...")
    return reader_function

def reader_function(path):
    print("Reading image...")
    data = imread(path)
    add_kwargs = {}
    layer_type = "image"
    return [(data, add_kwargs, layer_type)]


# @napari_hook_implementation
# def napari_get_reader(path:str):
#     print("Using hook...")
#     return reader_function