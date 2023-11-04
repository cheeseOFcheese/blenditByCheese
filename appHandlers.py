import os
import bpy
from bpy.app import handlers
from bpy.app.handlers import persistent
from bpy.types import Operator

class SavePostHandler(Operator):
    """Save Post Handler"""
    
    bl_idname = "wm.save_post_handler"
    bl_label = "Save Post Handler"
    
    def execute(self, context):
        filepath = bpy.path.abspath("//")
        filename = bpy.path.basename(bpy.data.filepath).split(".")[0]
        commands = reports.getCommands()

        # Ensure the folder for the .py file exists
        if not os.path.exists(filepath):
            os.makedirs(filepath)

        with open(os.path.join(filepath, f"{filename}.py"), "a") as file:
            for command in commands:
                file.write(f"\t{command}\n")

        reports.clearReports()
        return {'FINISHED'}

def register():
    # Register the Save Post Handler operator
    bpy.utils.register_class(SavePostHandler)

    # Add the Save Post Handler to save_post handlers
    handlers.save_post.append(SavePostHandler)

def unregister():
    # Remove the Save Post Handler from save_post handlers
    handlers.save_post.remove(SavePostHandler)

    # Unregister the Save Post Handler operator
    bpy.utils.unregister_class(SavePostHandler)
