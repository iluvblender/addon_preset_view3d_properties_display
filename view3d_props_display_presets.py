import bpy

from bl_operators import presets


bl_info = {
    "name": "3D View Display Presets",
    "author": "Satish Goda (satishgoda@live.com)",
    "version": (0, 1),
    "blender": (2, 7, 9),
    "location": "3d View : Properties : Display Panel",
    "description": "Save all the settings under the 3D View Display Properties Panel",
    "category": "3D View"
}



class VIEW3D_MT_Preset(bpy.types.Menu):
    bl_label = "Presets"
    preset_operator = "script.execute_preset"
    preset_subdir = "view3d/display"
    draw = bpy.types.Menu.draw_preset


class VIEW3D_Display_Preset_Add(presets.AddPresetBase, bpy.types.Operator):
    bl_idname = "view3d.display_preset_add"
    bl_label = "Add 3D View Display Preset"
    preset_menu = "VIEW3D_MT_Preset"
    
    preset_subdir = "view3d/display"
    
    preset_values = [
        "bpy.context.space_data.show_only_render",
        "bpy.context.space_data.show_world",
        "bpy.context.space_data.show_outline_selected",
        "bpy.context.space_data.show_all_objects_origin",
        "bpy.context.space_data.show_relationship_lines",
        "bpy.context.space_data.show_floor",
        "bpy.context.space_data.show_axis_x",
        "bpy.context.space_data.show_axis_y",
        "bpy.context.space_data.show_axis_z",
    ]


def VIEW3D_PT_display_presets(self, context):
    layout = self.layout
    row = layout.row(align=True)
    row.menu("VIEW3D_MT_Preset", text=VIEW3D_MT_Preset.bl_label)
    row.operator("view3d.display_preset_add", text="", icon="ZOOMIN")
    op_props = row.operator("view3d.display_preset_add", text="", icon="ZOOMOUT")
    op_props.remove_active = True


def register():
    bpy.utils.register_class(VIEW3D_MT_Preset)
    bpy.utils.register_class(VIEW3D_Display_Preset_Add)
    bpy.types.VIEW3D_PT_view3d_display.prepend(VIEW3D_PT_display_presets)
    

def unregister():
    bpy.types.VIEW3D_PT_view3d_display.remove(VIEW3D_PT_display_presets)
    bpy.utils.unregister_class(VIEW3D_Display_Preset_Add)
    bpy.utils.unregister_class(VIEW3D_MT_Preset)


if __name__ == '__main__':
    register()
