#/usr/bin/python
import sys,os
pkg_name = sys.argv[1]
a = os.system(f"pacman -Ss {pkg_name}")
if a != 256:
    c = os.system(f"sudo pacman -S {pkg_name} ")
