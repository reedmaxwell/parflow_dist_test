set tcl_precision 17

set runname LW_surface_press

#
# Import the ParFlow TCL package
#
lappend auto_path $env(PARFLOW_DIR)/bin
package require parflow
namespace import Parflow::*


file copy -force orig_files/lw.1km.slope_x.10x.pfb lw.1km.slope_x.10x.tcl.pfb 
file copy -force orig_files/lw.1km.slope_y.10x.pfb lw.1km.slope_y.10x.tcl.pfb

pfset FileVersion 4

pfset Process.Topology.P       1 
pfset Process.Topology.Q       1
pfset Process.Topology.R       1

pfset ComputationalGrid.NX                45
pfset ComputationalGrid.NY                32
pfset ComputationalGrid.NZ               1

# Slope files 1D files so distribute with -nz 1
pfdist -nz 1 lw.1km.slope_x.10x.tcl.pfb
pfdist -nz 1 lw.1km.slope_y.10x.tcl.pfb

