#!/usr/bin/env python
"""
$Id: dice.py,v 1.2 2005/10/26 06:14:38 rwh Exp $
Support funtions for dice-rolling, non engine-specific.

The Pythonic Mud
Copyright (C) 2005 by Rohan Harris

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from random import Random

rnd = Random()


def d6(dice = 1):
	return rnd.randint(dice, dice * 6)

def d10(dice = 1):
	return rnd.randint(dice, dice * 10)

def d100(dice = 1):
	return rnd.randint(dice, dice * 100)
