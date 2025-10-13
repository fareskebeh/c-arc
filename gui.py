import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Clang Editor', width=600, height=300)

with dpg.window(label="Clang Editor"):
    dpg.add_input_text(label="string", default_value="Enter code here")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()