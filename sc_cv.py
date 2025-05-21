import argparse
import os
import platform
import shutil
import time
from pathlib import Path
import sqlite3


import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

import sys
import yolo_5_anime.yolov5_anime


from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import (
    check_img_size, non_max_suppression, apply_classifier, scale_coords, xyxy2xywh, plot_one_box, strip_optimizer)
from utils.torch_utils import select_device, load_classifier, time_synchronized


from third_party import PhaseCongruencyKovesi


class Packaged_Features_and_Names:
    def __init__(self):
        self.name = ""
        self.original_image_location = ""
        self.original_file_name = ""
        self.changed_name = ""
        self.changed_file_name = ""
        self.features = []

    

class ComputerVision:

    def __init__(self):
        ...


    #This can be used to load a single image or multiple images
    def call_yolov5_model(self,image_location):        
        #Need to set some default variables since these were required. 
        imgsz = 640
        source = image_location
        weights = r"C:\Users\inuic\OneDrive\Documents\GitHub\Image-Labeling-Project\src\weights\yolov5x_anime.pt"
        out = "Testing/Images"
        device_main = ""
        augment = True
        update = True
        conf_thres_down = 0.4
        iou_thres_down = 0.5
        classes = 0
        agnostic_nms = True
        save_txt = True
        view_img = True

        # Initialize
        device = select_device(device_main)
        if os.path.exists(out):
            shutil.rmtree(out)  # delete output folder
        os.makedirs(out)  # make new output folder
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(weights, map_location=device)  # load FP32 model
        imgsz = check_img_size(imgsz, s=model.stride.max())  # check img_size
        if half:
            model.half()  # to FP16

        # Set Dataloader
        dataset = LoadImages(source, img_size=imgsz)

        # Get names and colors
        names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in range(len(names))]

        # Run inference
        t0 = time.time()
        img = torch.zeros((1, 3, imgsz, imgsz), device=device)  # init img
        _ = model(img.half() if half else img) if device.type != 'cpu' else None  # run once

        #Dictionary for creating a bind between different images and their respective features. 
        dict_features = {}
              
        for path, img, im0s, vid_cap in dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            # Inference
            t1 = time_synchronized()
            pred = model(img, augment=augment)[0]

            # Apply NMS
            pred = non_max_suppression(pred, conf_thres_down, iou_thres_down, classes=classes, agnostic=agnostic_nms)
            t2 = time_synchronized()

            # # Apply Classifier
            # if classify:
            #     pred = apply_classifier(pred, modelc, img, im0s)

            # Process detections
            for i, det in enumerate(pred):  # detections per image
                # if webcam:  # batch_size >= 1
                #     p, s, im0 = path[i], '%g: ' % i, im0s[i].copy()
                # else:
                p, s, im0 = path, '', im0s

                save_path = str(Path(out) / Path(p).name)
                txt_path = str(Path(out) / Path(p).stem) + ('_%g' % dataset.frame if dataset.mode == 'video' else '')
                s += '%gx%g ' % img.shape[2:]  # print string
                gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                if det is not None and len(det):
                    # Rescale boxes from img_size to im0 size
                    det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                    # Print results
                    for c in det[:, -1].unique():
                        n = (det[:, -1] == c).sum()  # detections per class
                        s += '%g %ss, ' % (n, names[int(c)])  # add to string

                    # Write results
                    for *xyxy, conf, cls in det:
                        if save_txt:  # Write to file
                            xywh = (xyxy2xywh(torch.tensor(xyxy).view(1, 4)) / gn).view(-1).tolist()  # normalized xywh
                            with open(txt_path + '.txt', 'a') as f:
                                f.write(('%g ' * 5 + '\n') % (cls, *xywh))  # label format

                        dat = None
                        # if save_img or view_img:  # Add bbox to image
                        if view_img:  # Add bbox to image
                            label = '%s %.2f' % (names[int(cls)], conf)
                            print(xyxy)
                            print(int(xyxy[0]))
                            print(int(xyxy[1]))
                            print(int(xyxy[2]))
                            print(int(xyxy[3]))
                            # plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=3)
                            dat = im0[ int(xyxy[1]):int(xyxy[3]),int(xyxy[0]):int(xyxy[2])]


                        package = Packaged_Features_and_Names()
                        package.original_file_name = path
                        package.features.append([int(xyxy[1]),int(xyxy[3]),int(xyxy[0]),int(xyxy[2])])

                        # print(dat)
                        # cv2.imshow('Eyes Detection',dat)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                # Print time (inference + NMS)
                print('%sDone. (%.3fs)' % (s, t2 - t1))
            print('Done. (%.3fs)' % (time.time() - t0))

    def detect_edges_of_anime_body(self,image):
        # img = cv2.imread(image)
        
        # Use these constants to tune your results:
        # SMOOTHING_KERNEL = (11, 11)  # Must be odd numbers.
        # NUM_CONTOURS = 8
        # ALPHA = 0.6  

        # # Load the moon image:
        IMG_GRAY = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
        edged = cv2.Canny(IMG_GRAY, 15, 150) 
        contours, hierarchy = cv2.findContours(edged,  
            cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

        # # Smooth the image using Gaussian blur:
        # smoothed_img = cv2.GaussianBlur(IMG_GRAY, 
        #                             SMOOTHING_KERNEL, 
        #                             sigmaX=0)

        # contours, hierarchy = cv2.findContours(smoothed_img,  
        #     cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 

        cv2.drawContours(IMG_GRAY, contours, -1, (0, 255, 0), 3) 

        cv2.imshow('Eyes Detection',IMG_GRAY)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def detectEyes(self,image_location):
        # read input image

        print(image_location)
        img = cv2.imread(image_location)

        # convert to grayscale of each frames
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # read the haarcascade to detect the faces in an image
        face_cascade = cv2.CascadeClassifier(r"C:\Users\inuic\OneDrive\Documents\GitHub\Image-Labeling-Project\util_files\lbpcascade_animeface.xml") #'..\\util_files\\haarcascade_frontalface_default.xml')

        # read the haarcascade to detect the eyes in an image
        eye_cascade = cv2.CascadeClassifier(r"C:\Users\inuic\OneDrive\Documents\GitHub\Image-Labeling-Project\util_files\haar3cascade_eye.xml")

        # detects faces in the input image
        faces = face_cascade.detectMultiScale(gray, 1.3, 4)
        # print('Number of detected faces:', len(faces))

        # while True:
        #converting the image to grayscale for easier processing.
        # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # for (x, y, w, h) in faces:
        #     cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        #     roi_gray = gray[y:y+h, x:x+w]
        #     roi_color = img[y:y+h, x:x+w]
        #     eyes = eye_cascade.detectMultiScale(roi_gray)
        #     for (ex, ey, ew, eh) in eyes:
        #         cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
        
        # # Press 'ESC' to release the camera.        
        # cv2.imshow('img', img)
        #     # k = cv2.waitKey(30) & 0xff
        #     # if k == 27:
            #     break

        # loop over the detected faces
        for (x,y,w,h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]
            
            # detects eyes of within the detected face area (roi)
            eyes = eye_cascade.detectMultiScale(roi_gray)
            
            # draw a rectangle around eyes
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,255),2)

        # display the image with detected eyes
        cv2.imshow('Eyes Detection',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()