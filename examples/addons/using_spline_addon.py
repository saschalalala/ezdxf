# Purpose: examples for using Spline() add-on
# Created: 09.02.2010, 2018 adapted for ezdxf
# Copyright (c) 2010-2018, Manfred Moitzi
# License: MIT License
from __future__ import unicode_literals
import ezdxf
from ezdxf.addons import Spline

NAME = 'spline.dxf'
dwg = ezdxf.new('R12')
msp = dwg.modelspace()

spline_points = [(0.0, 0.0), (2., 2.), (3., 2.), (5., 0.)]
Spline(spline_points, color=7).render_fit_points(msp)  # curve with definition points as fit points, but just 2d support
Spline(spline_points, color=6).render_bspline(msp)  # 3d support, but not as fit points
Spline(spline_points, color=5).render_rbspline(msp, weights=[1, 500, 500, 1])  # 3d support, but not as fit points

for point in spline_points:
    msp.add_circle(radius=0.1, center=point, dxfattribs={'color': 1})

dwg.saveas(NAME)
print("drawing '%s' created.\n" % NAME)
