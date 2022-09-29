#---------------------------------------------------------
#  This runs a Little Washita test problem with variable dz
#  and adjusts surface pressures
#---------------------------------------------------------

from parflow import Run
from parflow.tools.fs import cp, mkdir, chdir, get_absolute_path

cp('orig_files/lw.1km.slope_x.10x.pfb','lw.1km.slope_x.10x.py.pfb')
cp('orig_files/lw.1km.slope_y.10x.pfb','lw.1km.slope_y.10x.py.pfb')

LW_surface_press = Run("LW_surface_press", __file__)

LW_surface_press.FileVersion = 4

LW_surface_press.Process.Topology.P = 1
LW_surface_press.Process.Topology.Q = 1
LW_surface_press.Process.Topology.R = 1

LW_surface_press.ComputationalGrid.NX = 45
LW_surface_press.ComputationalGrid.NY = 32
LW_surface_press.ComputationalGrid.NZ = 6
#LW_surface_press.ComputationalGrid.NZ = 1


#---------------------------------------------------------
#  Distribute slopes
#---------------------------------------------------------

LW_surface_press.dist('lw.1km.slope_x.10x.py.pfb')
LW_surface_press.dist('lw.1km.slope_y.10x.py.pfb')
