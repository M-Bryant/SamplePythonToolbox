# -*- coding: utf-8 -*-

from typing import List

import arcpy


class PythonToolBase(object):
    """Base class for defining Python tools"""

    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool"
        self.description = ""
        self.canRunInBackground = True

    def getParameterInfo(self):
        """Define parameter definitions"""
        params = None
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        standard = arcpy.CheckProduct("ArcEditor") in ("Available", "AlreadyInitialized")
        advanced = arcpy.CheckProduct("ArcInfo") in ("Available", "AlreadyInitialized")
        ddd = arcpy.CheckExtension("3D") == "Available"
        spatial = arcpy.CheckExtension("Spatial") == "Available"
        return standard or advanced

    def updateParameters(self, parameters: List[arcpy.Parameter]):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters: List[arcpy.Parameter]):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters: List[arcpy.Parameter], messages):
        """The source code of the tool."""
        return
