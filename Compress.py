# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Compress.py
#
# Description:  This script looks for an SDE admin account sde file and
# compresses the enterprise FGDB that the sde file points to.
#
# The 'pudConnectionFile' variable will need to be changed to match the SDE admin
# account on whatever computer the script is ran from.
# ---------------------------------------------------------------------------

# Import arcpy module
import arcpy

# Local variables:
pudConnectionFile = "Database Connections\\zAtlas-editdev.sde (SDE ADMIN).sde"

# Process: Compress
arcpy.Compress_management(pudConnectionFile)

