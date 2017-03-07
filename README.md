### Bounding box detection of drones (small scale quadcopters)

Localization of quadcopters in images with [CNTK's implemententation of Fast R-CNN](https://github.com/Microsoft/CNTK/wiki/Object-Detection-using-Fast-R-CNN). I collected a total of 500 images of the quadcopter **DJI Phantom 3** from Google's image search and dozens of screenshots from YouTube videos. After that I manually added bounding boxes to the collected images. 350 images were used for training and 150 images for testing. A mAP of about 0.42 was achieved.

![alt text](https://github.com/creiser/drone-detection/blob/master/result.png "Detection results")

### Parameters

| var                                                      | val                              | 
| -------------------------------------------------------- | -------------------------------- | 
| number of regions of interest (cntk_nrRois)              | 500                              |
| minimum region of interest relative size (roi_minDimRel) | 0.04                             |
| maximum region of interest relative size (roi_maxDimRel) | 1.0 (had to increase this value) |
| number of images used for training                       | 350                              |
| number of images used for testing                        | 150                              |
| mAP                                                      | ~0.42                            |




