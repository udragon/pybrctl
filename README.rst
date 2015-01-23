Pybrctl
=======

Pybrctl is a pure Python library for managing bridges. It is a lightwight wrapper for the linux brctl command, included in the bridge-utils package.
It requires Python, Linux, and the bridge-utils package.

It was written by Ido Nahshon at Jan 2015, and it was released under the GPL license.

Example Usage
=============
This example shows how to set up a new bridge and remove it::

  from pybrctl import BridgeController

  brctl = BridgeController()

  b = brctl.addbr("br0")
  b.addif("eth0")
  b.addif("eth1")
  b.setmaxageing(0)
    
  brctl.delbr("br0")

Source
======

Latest version on github: https://github.com/udragon/pybrctl
Feel free to contribute. ;)

