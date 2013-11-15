# Production_Folder.py (c) 2012 SSG Software Solutions (P) Ltd., (SSG)
#
# ***** BEGIN GPL LICENSE BLOCK *****
#
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.	See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ***** END GPL LICENCE BLOCK *****

"""
bl_info = {
    "name": "Production Folder",
    "author": "SSG Software Solutions (P) Ltd., (SSG)",
    "version": (0,1),
    "blender": (2, 6, 5),
    "location": "Info -> File Menu -> Create Production",
    "description": "Create Production folder",
    "warning": "",
    "category": "System"}

"Purpose:-
	"This addon is only for Linux based systems to create "Production" folder and its sub folders in 	     
	"user specified path
"How to install this addon:-
	"Open Blender and Goto File menu -> User Preferences 
	"Click addons tab	
	"Choose Install from file... (see bottom of the User preferences window)
	"Select the addon folder and Click the addon file.
	"It will install and checkbox will not be checked.
"How to run this addon:-
	"Just mark(enable/make checked) the checkbox
	"Close the User Preferences window and Goto file menu
	"From file menu click the ""
	"Now, folders will be created in the user specified path
"How to enable/disable the addon:-
	"Mark the checkbox of this addon to make enable
	"Unmark the checkbox of this addon to make disable
"How to uninstall this addon:-
	"Open Blender and Goto File menu -> User Preferences 
	"Click addons tab	
	"Choose this addon and click the expander(arrow symbol)
	"Click remove button
	"It will uninstall this addon.
"""

import bpy
import os
from bpy_extras.io_utils import ExportHelper
from platform import system as currentOS
pfopath=""
# ------ operator 0 ------

class Set_Production_Folder(bpy.types.Operator, ExportHelper):
    '''Save selected objects to a chosen format'''
    bl_idname = "production_scene.selected"
    bl_label = "Set Production"
    bl_options = {'REGISTER', 'UNDO'}
    
    filename_ext = bpy.props.StringProperty(
        default="",
        options={'HIDDEN'},
        )

    def invoke(self, context, event):
        self.filename_ext = ".blend" 
        self.filepath = pfopath + "/prod/scenes/untitled"
        return ExportHelper.invoke(self, context, event)
    
    def execute(self, context):        
        bpy.ops.wm.save_mainfile(
            filepath=self.filepath,
        )
        return {'FINISHED'}

class Production_Folder(bpy.types.Operator, ExportHelper):
    """Open the Production Folder in a file Browser"""
    bl_idname = "productionfolder_scene.selected"
    bl_label = "Create Production"
    bl_options = {'REGISTER', 'UNDO'}

    filename_ext = bpy.props.StringProperty(  #--- If we hides this, both 2menu works but 2nd shows only run time error after creating folder.
        default="",
        options={'HIDDEN'},
        )
    
    filter_glob = bpy.props.StringProperty(
        default="",
        options={'HIDDEN'},
        )

    def invoke(self, context, event):
        self.filepath = "Production Folder"
        return ExportHelper.invoke(self, context, event)

    def execute(self, context):
        try : 
            global pfopath
            pfopath = self.filepath
            folder_path = self.filepath + '/'
            path = folder_path + 'preprod'
            if not os.path.exists(path): os.makedirs(path)
            path = folder_path + 'prod'
            if not os.path.exists(path): os.makedirs(path)
            path = folder_path + 'ref'
            if not os.path.exists(path): os.makedirs(path)
            path = folder_path + 'resources'
            if not os.path.exists(path): os.makedirs(path)
            path = folder_path + 'wip'
            if not os.path.exists(path): os.makedirs(path)
            path1 = folder_path + 'prod/scenes'
            if not os.path.exists(path1): os.makedirs(path1)
            path1 = folder_path + 'prod/sets'
            if not os.path.exists(path1): os.makedirs(path1)
            path1 = folder_path + 'prod/props/textures'
            if not os.path.exists(path1): os.makedirs(path1)
            path1 = folder_path + 'prod/chars/textures'
            if not os.path.exists(path1): os.makedirs(path1)
            path1 = folder_path + 'prod/envs/textures'
            if not os.path.exists(path1): os.makedirs(path1)
            path1 = folder_path + 'prod/mattes/textures'
            if not os.path.exists(path1): os.makedirs(path1)
            self.report({'INFO'}, "Production folder created.")
        except ValueError:
            self.report({'INFO'}, "No Production folder created yet")
            return {'FINISHED'}
        return {'FINISHED'}

class Show_Production_Folder(bpy.types.Operator):
    bl_idname = "file.production_folder"
    bl_label = "Show Project"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        try :
            bpy.ops.wm.path_open(filepath=pfopath) 
        except ValueError:
            self.report({'INFO'}, "No project folder yet")
            return {'FINISHED'}       
        return {'FINISHED'}

# Registration

def menu_func(self, context):
    self.layout.operator(
        Production_Folder.bl_idname,
        text="Create Production", 
        icon="FILESEL")
    if pfopath != "":
        self.layout.operator(
            Show_Production_Folder.bl_idname,
            text="Show Production", 
            icon="FILE_FOLDER")
        self.layout.operator(
            Set_Production_Folder.bl_idname,
            text="Set Production", 
            icon="FILE_TICK")

def register():
    bpy.utils.register_class(Set_Production_Folder)
    bpy.utils.register_class(Show_Production_Folder)
    bpy.utils.register_class(Production_Folder)
    bpy.types.INFO_MT_file.prepend(menu_func)

def unregister():
    bpy.types.INFO_MT_file.remove(menu_func)
    bpy.utils.unregister_class(Production_Folder)
    bpy.utils.unregister_class(Show_Production_Folder)
    bpy.utils.unregister_class(Set_Production_Folder)
   

if __name__ == "__main__":
    register()
