#bash
!git clone https://github.com/GReX-Telescope/GReX-T3.git
%cd GReX-T3/grex_t3/

# Code for generating offline waterfall plot for GReX candidate for any terminal.

import sys
import os
from cand_plotter import gen_cand
from cand_plotter import get_cand
from cand_plotter import plot_grex
sys.path.append('/home/user/priya/GReX-T3/grex_t3')

os.listdir('/hdd/data/voltages/')

dir_mon = "/hdd/data/voltages/"
dir_plot = "/hdd/data/candidates/T3/candplots/"
dir_fil = "/hdd/data/candidates/T3/candfils/"
cluster_output = "/hdd/data/candidates/T2/cluster_output.csv"

fn_vol = "/hdd/data/voltages/grex_dump-241002aaae.nc"  
fn_tempfil = "/hdd/data/temp.fil"  
fn_filout = "/hdd/data/output.fil" 
JSON = "241002aaae.json"  
cand, tab = gen_cand(fn_vol, fn_tempfil, fn_filout, JSON, v=True)
get_cand(JSON)
plot_grex(cand, tab, JSON, v=False)



