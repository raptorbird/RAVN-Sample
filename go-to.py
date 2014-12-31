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

from ravn import Drone
from time import sleep #important to import

myDrone = Drone(async=True)
myDrone.takeoff()
sleep(10) #delay accounts for async
myDrone.goto(insert your latitude, insert your longitude, 2) #insert the parameters with 4 digits of precision. such as ##.####
sleep(30) #delay accounts for async
myDrone.land()
myDrone.close()
