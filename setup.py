import cx_Freeze
import sys
import matplotlib

base = None

if sys.platform == 'win32':
    base="Win32GUI"

executables = [cx_Freeze.Executable("PROJET_INFO_CHIMIMAXX.py", base=base, icon='logo.ico')]

cx_Freeze.setup(
    name = "ProgrammeInfo_SPECTRES_IR",
    options = {"build_exe":{"packages":["tkinter","matplotlib","webbrowser","numpy"],"include_files":["Chimie.gif","logo.ico","Chimie2.gif","Chimie3.gif","obs1_2.gif","IRbandpo.gif","rubon427.gif","1.gif","2.gif","3.gif","4.gif","5.gif","6.gif","7.gif","8.gif","9.gif","10.gif","11.gif","12.gif","13.gif","14.gif","15.gif","fondecprinc2.gif","fondecfct3.gif","tableau_fct.gif","RMN.gif","tablper1.gif","tablper2.gif","tablpergrd1.gif","tablpergrd2.gif","tableau_fct_grd.gif","RMN_grd.gif"	]}},
    version = "3.2.0",
    description = "Programme de Jerome et Clémence CHAPTAL 2016",
    executables = executables
    )
