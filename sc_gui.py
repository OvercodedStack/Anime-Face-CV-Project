import dearpygui.dearpygui as dpg
from dearpygui.dearpygui import *

import dearpygui.demo as demo
import sc_utilities
import sc_database
import sc_learning


#############################################################################
# This file is used to show a GUI to the user and can be used to interact with the program.
# Ideally this program should act similar to 

class GUI_Main:
    def __init__(self):
        self.sc_util_main = sc_utilities.Utilities()
        self.database_main = sc_database.Database()
        self.leaning_main = sc_learning.Learning()
    

    def show_main_gui(self):
         # Create the main window
        dpg.create_context()


        # Define a callback function for the button
        def button_callback():
            dpg.set_value("text_display", "Attempting to load images!")

            # Load the files by directory. 
            p = dpg.get_value("file_location_value")
            print(p)
            self.sc_util_main.get_all_files(p) #Single call puts the list in the utility file. 


            #Tell the user by message. 
            if (self.sc_util_main.dataLocations[0] == "Working"):
                dpg.set_value("text_display", "Files found and locations stored.")
            else:
                dpg.set_value("text_display", self.sc_util_main.dataLocations[0])

            self.sc_util_main.print_locations(self.sc_util_main.dataLocations[1])



            # with dpg.texture_registry(show=True):
            #     for path in res[1]:
            #         width, height, channels, data = dpg.load_image(path)
            #         dpg.add_static_texture(width=width, height=height, default_value=data, tag=path)

        def button_test_cv_output():
            first_image =self.sc_util_main.dataLocations[1][1]
            # self.leaning_main.cvcore.detectEyes(first_image)
            # self.leaning_main.cvcore.call_yolov5_model(first_image)
            self.leaning_main.cvcore.detect_edges_of_anime_body(first_image)
            ...

        def button_load_files_onto_directory():

            ...

        def button_():

            ...

        # Create a window
        with dpg.window(label="Main window", width=800, height=800):
            dpg.add_text("Please enter the file location you wish to load images from. Otherwise using the default location.", tag="text_display")
            dpg.add_input_text(tag="file_location_value",label="File Location", source="location",default_value=r"C:\Users\inuic\OneDrive\Documents\Anime\Latest Anime")
            dpg.add_button(label="Load images from location.", callback=button_callback)
            dpg.add_button(label="Test image extraction.", callback=button_test_cv_output)
            # dpg.add_button(label=".", callback=button_test_cv_output)

        # Setup and start the Dear PyGui context
        dpg.create_viewport(title="AIris", width=800, height=800)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()



    def show_images_gui(self):
        dpg.create_context()
        width, height, channels, data = dpg.load_image(r"C:\Users\inuic\OneDrive\Documents\Anime\Latest Anime\Miyabi kimono.png")

        with dpg.texture_registry(show=True):
            dpg.add_static_texture(width=width, height=height, default_value=data, tag="texture_tag")

        with dpg.window(label="Tutorial"):
            dpg.add_image("texture_tag")


        dpg.create_viewport(title='Custom Title', width=800, height=600)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()



    def show_test_gui(self):

        # dpg.create_context()
        # dpg.create_viewport(title='Custom Title', width=600, height=600)

        # demo.show_demo()

        # dpg.setup_dearpygui()
        # dpg.show_viewport()
        # dpg.start_dearpygui()
        # dpg.destroy_context()


        # dpg.create_context()
        # dpg.create_viewport(title='Custom Title', width=600, height=300)
        # dpg  set_style_frame_padding(4.00, 0.00)

        # with dpg.window(label="Example Window"):
        #     dpg.add_text("Hello, world")
        #     dpg.add_button(label="Save")
        #     dpg.add_input_text(label="string", default_value="Quick brown fox")
        #     dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

        # dpg.setup_dearpygui()
        # dpg.show_viewport()
        # dpg.start_dearpygui()
        # dpg.destroy_context()


        # Create the main window
        dpg.create_context()

        # Define a callback function for the button
        def button_callback():
            dpg.set_value("text_display", "Button Clicked!")
            p = dpg.get_value("potato")
            print(p)

        # Create a window
        with dpg.window(label="Simple GUI", width=500, height=400):
            dpg.add_text("Hello, Dear PyGui!", tag="text_display")
            dpg.add_button(label="Click Me", callback=button_callback)
            dpg.add_input_text(tag="potato",label="Text Input 1", source="rat",default_value=r"C:\Users\inuic\OneDrive\Documents\Anime\Latest Anime")

        # Setup and start the Dear PyGui context
        dpg.create_viewport(title="My First GUI", width=500, height=400)
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()

        
        # dpg.create_context()

        # with dpg.value_registry():
        #     dpg.add_bool_value(default_value=True, tag="bool_value")
        #     dpg.add_string_value(default_value="Default string", tag="string_value")

        # with dpg.window(label="Tutorial"):
        #     dpg.add_checkbox(label="Radio Button1", source="bool_value")
        #     dpg.add_checkbox(label="Radio Button2", source="bool_value")

        #     dpg.add_input_text(label="Text Input 1", source="string_value")
        #     dpg.add_input_text(label="Text Input 2", source="string_value", password=True)

        # dpg.create_viewport(title='Custom Title', width=800, height=600)
        # dpg.setup_dearpygui()
        # dpg.show_viewport()
        # dpg.start_dearpygui()
        # dpg.destroy_context()