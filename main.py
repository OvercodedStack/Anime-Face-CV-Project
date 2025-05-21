

# Own functions
import sc_database
import sc_gui
import sc_learning
#    ===== Required operations from the tool =====
# 
# o Select the data from a folder
# o Select images that will be used for training
# o Set the name of images unfamiliar with the internal model
# o Determine the images that are unfamilar with the internal model
# o Train internal ML model to recognize new images and label them correctly




# Requirements: 
#  GUI
#  Pytorch or Tensorflow
#  A permanent dataset for SQL images locally
#  Future: pull from the internet the required images. 


class MainProgram:
    def __init__(self):
        self.GUI_main = sc_gui.GUI_Main()
        

        self.call_GUI()

    def call_GUI(self):
        # self.GUI_main.show_test_gui()
        self.GUI_main.show_main_gui()
        # self.GUI_main.show_images_gui()

    def call_learning(self):
        ... 

m = MainProgram() 

