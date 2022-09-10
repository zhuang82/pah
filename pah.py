#/usr/bin/python
import sys,os
def aur(pkg_name):
    out_aur = os.popen(f"git clone https://aur.archlinux.org/{pkg_name}.git","r").read()
    if out_aur.split(str="\n")[-1][0:7] == "warning:":
        os.system(f"pacman -S {pkg_name}")
        os.system(f"links \"https://aur.archlinux.org/packages?O=0&SeB=nd&K={pkg_name}&outdated=&SB=p&SO=d&PP=50&submit=Go\"")
    else:
        os.chroot("{pkg_name}")
        input("Please edit PKGBUILD in ~/PAH directory or press enter to continue")
        with open("PKGBUILD","r") as pkgbuild:
            for i in pkgbuild.readlines():
                if i[0:6] == "depends":
                    depends = i
        depends = depends.split("(")[1][0:-2].split(" ")
        for i in depends:
            pkg = eval(depends.strip())
            out = os.system(f"sudo pacman -S {pkg}")
            if out == 256:
                aur(i)
pkg_name = sys.argv[1]
os.system("mkdir ~/PAH")
os.chroot("~/PAH")
aur(pkg_name)
