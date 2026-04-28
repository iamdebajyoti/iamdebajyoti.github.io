from taipy import Gui

print("checking")
page = """
# Getting started with *Taipy*
"""
"""
import taipy.gui.builder as tgb
tgb.input("{value}")

print({value})
"""

Gui(page=page).run(debug=True, port=5008)
