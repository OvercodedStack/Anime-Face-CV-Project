import glob
import cv2
import pandas
import os
from natsort import os_sorted


class Utilities:
    def __init__(self):
        ...

    #Returns the image locations. 
    filter_extensions = [".jpg", ".png"] #, ".webp"]



    
    def get_all_files(self,location):
        status = "Working"

        #Check if the file location exist. 
        if (not os.path.isdir(location)):
            self.dataLocations = ("Location does not exist",[])
            # return ("Location does not exist",[])

        images_names = sorted(glob.glob(location + "/*"))
        images_names = os_sorted(images_names)

        filtered_names = []
        for path in images_names:
            allow_path = False
            for x in self.filter_extensions:
                if x in path:
                    allow_path = True
                    break;
            if (allow_path):
                filtered_names.append(path)
        self.dataLocations = (status, filtered_names)
        # return (status, filtered_names)

    def print_locations(self, locations):
        for path in locations:
            print(path)

    def get_images(self, images):
        ...

    def rename_files(self, file_names):
        ...

