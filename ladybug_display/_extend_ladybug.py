# coding=utf-8
# import the core ladybug modules
from ladybug.compass import Compass
from ladybug.sunpath import Sunpath

# import the extension functions
from .extension.compass import compass_to_vis_set
from .extension.sunpath import sunpath_to_vis_set

# inject the methods onto the classes
Compass.to_vis_set = compass_to_vis_set
Sunpath.to_vis_set = sunpath_to_vis_set