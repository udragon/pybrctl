#!/usr/bin/python

from pybrctl import BridgeController

def main():
    brctl = BridgeController()
    print brctl.showall()

    b = brctl.addbr("testbr")
    b.stp(False)
    b.addif("eth1")

    print b.getifs()
    print brctl.showall()

    brctl.delbr("testbr")


if __name__ == '__main__':
    main()
