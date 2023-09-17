import dearpygui.dearpygui as dpg
# from dearpygui import core, simple


# from dearpygui.demo import show_demo
# show_demo()

vp = dpg.create_viewport(title="DearPyGUI_1", width=600, height=600)
dpg.setup_dearpygui(viewport=vp)
dpg.show_viewport(viewport=vp)

with dpg.window(id="Example Window", label="Example Window"):
    t = dpg.add_text("Hello, world")
    b = dpg.add_button(label="save")
    i = dpg.add_input_text(label="string", default_value="Quick Brown Fox")
    s = dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

with dpg.window(id="Primary Window", label="Primary Window"):
    dpg.add_text("Checking Primary Window...")
    dpg.add_button(label="Click Me !!!")
    ## the following captures the compiler generated IDs of the items of the other window
    dpg.add_input_text(default_value=t)
    dpg.add_input_text(default_value=b)
    dpg.add_input_text(default_value=i)
    dpg.add_input_text(default_value=s)
    
with dpg.window(id="Exp1", label="Exp1"):
    dpg.add_button(label="")

# with simple.window("Example"):
#     core.add_button("Click Click ..")
#     core.set_main_window_size(500,300)

# core.start_dearpygui()



# dpg.start_dearpygui()
while dpg.is_dearpygui_running():
    dpg.render_dearpygui_frame()

## The following line will decide which window will be the floating ones ..
## All non-primary windows are floating windows
# dpg.set_primary_window("Primary Window", True)
dpg.set_primary_window("Example Window", True)
dpg.cleanup_dearpygui()
