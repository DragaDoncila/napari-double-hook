"""
This module is an example of a barebones writer plugin for napari

It implements the ``napari_get_writer`` and ``napari_write_image`` hook specifications.
see: https://napari.org/docs/dev/plugins/hook_specifications.html

Replace code below according to your needs
"""

from napari_plugin_engine import napari_hook_implementation
from skimage.io import imsave

@napari_hook_implementation(specname="napari_get_writer")
def napari_writer_one(path):
    print("Getting writer 1...")
    return napari_write_images

@napari_hook_implementation(specname="napari_get_writer")
def napari_writer_two(path):
    print("Getting writer 2...")
    return napari_write_images    

def napari_write_images(path, layers):
    print("Writing layers...")
    return [path]

@napari_hook_implementation
def napari_write_image(path, data, meta):
    print("Writing single layer...")
    return path
