import torch

import sc_cv

class Learning:

    def __init__(self):
        self.cvcore = sc_cv.ComputerVision()
        
        

    def distillate_picture(self,image_location):
        self.cvcore.detectEyes(image_location)
        
        ...

    def learn_pictures(self, input_pictures_folder):
        ...

    def recall_name_from_picture(self, image_path):
        ...

    def search_internet_for_image(self, image_name):
        ...


    def CNN_implementation(self):

        ...

