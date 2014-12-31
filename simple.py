"""
RAVN Smart Drone Platform
Copyright (C) 2014 RaptorBird Robotics Inc.
<http://www.raptorbird.com/>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; Version 2

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from RAVN import Drone
from time import sleep
myDrone = Drone(async=True)
sleep(10)
print(myDrone.get_location())
myDrone.close()