# coding=utf-8
from ladybug_geometry.geometry3d.pointvector import Point3D, Vector3D
from ladybug_geometry.geometry3d.cylinder import Cylinder
from ladybug.color import Color
from ladybug_display.geometry3d.cylinder import DisplayCylinder


def test_cylinder_init():
    """Test the initialization of Cylinder objects and basic properties."""
    grey = Color(100, 100, 100)
    center = Point3D(2, 0, 2)
    axis = Vector3D(0, 2, 2)
    radius = 0.7
    c = DisplayCylinder(Cylinder(center, axis, radius), grey)
    str(c)  # test the string representation of the cylinder

    assert c.color == grey
    assert c.display_mode == 'Surface'
    assert c.center == Point3D(2, 0, 2)
    assert c.axis == Vector3D(0, 2, 2)
    assert c.radius == 0.7
    assert c.height == c.axis.magnitude
    assert isinstance(c.area, float)
    assert isinstance(c.volume, float)

    blue = Color(0, 0, 100)
    c.color = blue
    c.display_mode = 'Wireframe'
    assert c.color == blue
    assert c.display_mode == 'Wireframe'


def test_cylinder_to_from_dict():
    """Test the Cone to_dict and from_dict methods."""
    grey = Color(100, 100, 100)
    center = Point3D(2, 0, 2)
    axis = Vector3D(0, 2, 2)
    radius = 0.7
    c = DisplayCylinder(Cylinder(center, axis, radius), grey)
    con_d = c.to_dict()
    new_c = DisplayCylinder.from_dict(con_d)
    assert isinstance(new_c, DisplayCylinder)
    assert new_c.to_dict() == con_d


def test_display_cylinder_to_svg():
    """Test the translation of Cylinder objects to SVG."""
    pt1 = Point3D(200, -400)
    axis = Vector3D(200, 200, 200)
    cylinder = Cylinder(pt1, axis, 30)
    svg_data = DisplayCylinder.cylinder_to_svg(cylinder)
    assert len(str(svg_data)) > 30

    import ladybug_display.svg as svg
    canvas = svg.SVG(width=800, height=600)
    canvas.elements = [svg_data]
    print(canvas)

    red = Color(255, 0, 0, 125)
    cylinder = DisplayCylinder(cylinder, red, 'SurfaceWithEdges')
    svg_data = cylinder.to_svg()
    assert len(str(svg_data)) > 30
