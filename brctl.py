"""
Linux brctl wrapper
Written by Ido Nahshon.
"""

import subprocess 

class BridgeException(Exception):
    pass

class Bridge(object):

    def __init__(self, name):
        """ Create a bridge a set the device up """
        self.name = name
        self._runshell(['/sbin/brctl', 'addbr', self.name],
            "Could not create bridge %s." % self.name)
        self._runshell(['/sbin/ip', 'link', 'set', 'dev', self.name, 'up'],
            "Could not set link up for %s." % self.name)

    def __del__(self):
        """ Set the device down and delete the bridge. """
        self._runshell(['/sbin/ip', 'link', 'set', 'dev', self.name, 'down'],
            "Could not set link down for %s." % self.name)
        self._runshell(['/sbin/brctl', 'delbr', self.name],
            "Could not delete bridge %s." % self.name)

    def _runshell(self, cmd, exception):
        """ Run a shell command. if fails, raise a proper exception. """
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if p.wait() != 0:
            raise BridgeException(exception)
        return p
 
    def addif(self, iname):
        """ Add an interface to the bridge """
        self._runshell(['/sbin/brctl', 'addif', self.name, iname],
            "Could not add interface %s to %s." % (iname, self.name))

    def delif(self, iname):
        """ Delete an interface from the bridge. """
        self._runshell(['/sbin/brctl', 'delif', self.name, iname],
            "Could not delete interface %s from %s." % (iname, self.name))

    def hairpin(self, port, val=True):
        """ Turn harpin on/off on a port. """ 
        if val: state = 'on' 
        else: state = 'off'
        self._runshell(['/sbin/brctl', 'hairpin', self.name, port, state],
            "Could not set hairpin in port %s in %s." % (port, self.name))

    def stp(self, val=True):
        """ Turn STP protocol on/off. """
        if val: state = 'on' 
        else: state = 'off'
        self._runshell(['/sbin/brctl', 'stp', self.name, state],
            "Could not set stp on %s." % self.name)

    def setageing(self, time):
        """ Set bridge ageing time. """
        self._runshell(['/sbin/brctl', 'setageing', self.name, str(time)],
            "Could not set ageing time in %s." % self.name)

    def setbridgeprio(self, prio):
        """ Set bridge priority value. """
        self._runshell(['/sbin/brctl', 'setbridgeprio', self.name, str(prio)],
            "Could not set bridge priority in %s." % self.name)
    
    def setfd(self, time):
        """ Set bridge forward delay time value. """
        self._runshell(['/sbin/brctl', 'setfd', self.name, str(time)],
            "Could not set forward delay in %s." % self.name)

    def sethello(self, time):
        """ Set bridge hello time value. """
        self._runshell(['/sbin/brctl', 'sethello', self.name, str(time)],
            "Could not set hello time in %s." % self.name)
   
    def setmaxage(self, time):
        """ Set bridge max message age time. """
        self._runshell(['/sbin/brctl', 'setmaxage', self.name, str(time)],
            "Could not set max message age in %s." % self.name)
 
    def setpathcost(self, port, cost):
        """ Set port path cost value for STP protocol. """
        self._runshell(['/sbin/brctl', 'setpathcost', self.name, port, str(cost)],
            "Could not set path cost in port %s in %s." % (port, self.name))
 
    def setportprio(self, port, prio):
        """ Set port priority value. """
        self._runshell(['/sbin/brctl', 'setportprio', self.name, port, str(prio)],
            "Could not set priority in port %s in %s." % (port, self.name))

    def _show(self):
        """ Return a list of unsorted bridge details. """ 
        p = self._runshell(['/sbin/brctl', 'show', self.name],
            "Could not show %s." % self.name)
        return p.stdout.read().split()[7:]

    def get_id(self):
        """ Return the bridge id value. """
        return self._show()[1]

    def get_interfaces(self):
        """ Return a list of bridge interfaces. """
        return self._show()[3:]

    def is_stp_enabled(self):
        """ Return if STP protocol is enabled. """
        return self._show()[2] == 'yes'

    def showmacs(self):
        """ Return a list of mac addresses. """
        raise NotImplementedError()

    def showstp(self):
        """ Return STP information. """
        raise NotImplementedError()
            
