"""
Linux brctl wrapper
Written by Ido Nahshon.
"""

import subprocess 

class BridgeException(Exception):
    pass

class Bridge(object):

    def __init__(self, name): 
        self.name = name
        p = subprocess.Popen(['/sbin/brctl', 'addbr', self.name])
        if p.wait():
            raise BridgeException("Could not create bridge %s." % self.name)
        p = subprocess.Popen(['/sbin/ip', 'link', 'set', 'dev', self.name, 'up'])
        if p.wait():
            raise BridgeException("Could not set link up for %s." % self.name)

    def __del__(self):
        p = subprocess.Popen(['/sbin/ip', 'link', 'set', 'dev', self.name, 'down'])
        if p.wait():
            raise BridgeException("Could not set link down for %s." % self.name)
        p = subprocess.Popen(['/sbin/brctl', 'delbr', self.name])
        if p.wait():
            raise BridgeException("Could not delete bridge %s." % self.name)

    def addif(self, iname):
        p = subprocess.Popen(['/sbin/brctl', 'addif', self.name, iname])
        if p.wait():
            raise BridgeException("Could not add interface %s to %s." % (iname, self.name))

    def delif(self, iname):
        p = subprocess.Popen(['/sbin/brctl', 'delif', self.name, iname])
        if p.wait():
            raise BridgeException("Could not delete interface %s from %s." % (iname, self.name))

    def hairpin(self, port, val):
        if val: state = 'on' 
        else: state = 'off'
        p = subprocess.Popen(['/sbin/brctl', 'hairpin', self.name, port, state])
        if p.wait():
            raise BridgeException("Could not set hairpin in port %s in %s." % (port, self.name))

    def stp(self, val):
        if val: state = 'on' 
        else: state = 'off'
        p = subprocess.Popen(['/sbin/brctl', 'stp', self.name, state])
        if p.wait():
            raise BridgeException("Could not set stp on %s." % self.name)


    def setageing(self, time):
        p = subprocess.Popen(['/sbin/brctl', 'setageing', self.name, str(time)])
        if p.wait():
            raise BridgeException("Could not set ageing time in %s." % self.name)

    def setbridgeprio(self, prio):
        p = subprocess.Popen(['/sbin/brctl', 'setbridgeprio', self.name, str(prio)])
        if p.wait():
            raise BridgeException("Could not set bridge priority in %s." % self.name)
    
    def setfd(self, time):
        p = subprocess.Popen(['/sbin/brctl', 'setfd', self.name, str(time)])
        if p.wait():
            raise BridgeException("Could not set forward delay in %s." % self.name)

    def sethello(self, time):
        p = subprocess.Popen(['/sbin/brctl', 'sethello', self.name, str(time)])
        if p.wait():
            raise BridgeException("Could not set hello time in %s." % self.name)
   
    def setmaxage(self, time):
        p = subprocess.Popen(['/sbin/brctl', 'setmaxage', self.name, str(time)])
        if p.wait():
            raise BridgeException("Could not set max message age in %s." % self.name)
 
    def setpathcost(self, port, cost):
        p = subprocess.Popen(['/sbin/brctl', 'setpathcost', self.name, port, str(cost)])
        if p.wait():
            raise BridgeException("Could not set path cost in port %s in %s." % (port, self.name))
 
    def setportprio(self, port, prio):
        p = subprocess.Popen(['/sbin/brctl', 'setportprio', self.name, port, str(prio)])
        if p.wait():
            raise BridgeException("Could not set priority in port %s in %s." % (port, self.name))

    def _show(self):
        p = subprocess.Popen(['/sbin/brctl', 'show', self.name], stdout=subprocess.PIPE)
        if p.wait():
            raise BridgeException("Could not show %s." % self.name)
        return p.stdout.read().split()[7:]

    def get_id(self):
        return self._show()[1]

    def get_interfaces(self):
        return self._show()[3:]

    def is_stp_enabled(self):
        return self._show()[2] == 'yes'

    def showmacs(self):
        raise NotImplementedError()

    def showstp(self):
        raise NotImplementedError()
            
