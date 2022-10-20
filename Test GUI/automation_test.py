from pywinauto import Application
import pywinauto
import os


app = Application().start(cmd_line="Notepad.exe")

# will open file explorer
app.UntitiledNotepad.menu_item(u'&File->&Open... Ctrl+O').click()


# debug = app.top_window_().print_control_identifiers()

# fileBox = app.top_window_().child_window(title="File name:", auto_id="1148",
#                                          control_type="Edit").wrapper_object()
# fileBox.type_keys("this is a test.txt")

# doc = app.top_window_().ToolBarAddressDocuments.print_control_identifiers()
# app.top_window().get_toolar().click()
# match = pywinauto.findwindows.find_element(class_name_re="path")
# print(debug)


app.top_window().type_keys("C:\\Users\\Chowt\\Documents\\test.txt")
app.top_window_().OpenButton.click()

# app2 = Application().start(cmd_line="matlab.exe")
os.system("matlab.exe")
