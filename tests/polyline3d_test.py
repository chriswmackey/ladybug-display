# coding=utf-8
from ladybug_geometry.geometry3d.pointvector import Point3D
from ladybug_geometry.geometry3d.line import LineSegment3D
from ladybug_geometry.geometry3d.polyline import Polyline3D
from ladybug.color import Color
from ladybug_display.geometry3d.polyline import DisplayPolyline3D
from ladybug_display.altnumber import default


def test_display_polyline3d_init():
    """Test the initialization of DisplayPolyline3D objects and basic properties."""
    grey = Color(100, 100, 100)
    pts = (Point3D(0, 0), Point3D(2, 0), Point3D(2, 2), Point3D(0, 2))
    pline = DisplayPolyline3D(Polyline3D(pts), grey)
    str(pline)  # test the string representation of the polyline

    assert pline.color == grey
    assert pline.line_width == default
    assert pline.line_type == 'Continuous'

    assert isinstance(pline.vertices, tuple)
    assert len(pline.vertices) == 4
    for point in pline.vertices:
        assert isinstance(point, Point3D)

    assert isinstance(pline.segments, tuple)
    assert len(pline.segments) == 3
    for seg in pline.segments:
        assert isinstance(seg, LineSegment3D)
        assert seg.length == 2

    assert pline.p1 == pts[0]
    assert pline.p2 == pts[-1]
    assert pline.length == 6

    blue = Color(0, 0, 100)
    pline.color = blue
    pline.line_width = 2
    pline.line_type = 'Dashed'
    assert pline.color == blue
    assert pline.line_width == 2
    assert pline.line_type == 'Dashed'


def test_polyline3d_to_from_dict():
    """Test the to/from dict of DisplayPolyline3D objects."""
    grey = Color(100, 100, 100)
    pts = (Point3D(0, 0), Point3D(2, 0), Point3D(2, 2), Point3D(0, 2))
    pline = DisplayPolyline3D(Polyline3D(pts), grey)
    pline.line_width = 2
    pline.line_type = 'Dashed'
    pline_dict = pline.to_dict()
    new_pline = DisplayPolyline3D.from_dict(pline_dict)
    assert isinstance(new_pline, DisplayPolyline3D)
    assert new_pline.to_dict() == pline_dict


def test_polyline3d_to_svg():
    """Test the translation of Polyline3D objects to SVG."""
    pts = (Point3D(200, -100), Point3D(200, -50), Point3D(100, -50), Point3D(100, -100))
    p_line = Polyline3D(pts)
    svg_data = DisplayPolyline3D.polyline3d_to_svg(p_line)
    assert len(str(svg_data)) > 30

    red = Color(255, 0, 0, 125)
    p_line = DisplayPolyline3D(p_line, red, line_width=2, line_type='Dashed')
    svg_data = p_line.to_svg()
    assert len(str(svg_data)) > 30

    p_line = Polyline3D(pts, interpolated=True)
    p_line = DisplayPolyline3D(p_line, red, line_width=2, line_type='Dashed')
    svg_data = p_line.to_svg()
    assert len(str(svg_data)) > 30
