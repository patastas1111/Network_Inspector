"""
Network Inspector
by patastas1111

"""

import os

class icmp():
  def __init__(self, pingcheck):
    self.pingcheck = pingcheck

  def icmpcheck(self):
    hostname = self.pingcheck  # example
    response = os.system("ping -c 3 " + hostname + '> icmp.txt')

    if response == 0:
      return True
    else:
      return False


  if __name__ == '__main__':
      icmpcheck()
