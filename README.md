# Face Recognition sytem using openCV
Python implementation of LBPH algorithm, for face recognition of a user from database.
Face detection using Haar feature-based cascade classifier for frontal face.

## Requirements
- python 3.5.2
- OpenCV
- OpenCV-contrib
- SQLite
- numpy
- pillow

To install these requirements run the following command

``` pip install -r requirements.txt ```

Run the files in the following order
 1. create_db.py (Creates a sqlite database to store the names)
 2. register_face.py (create a dataset of 20 images)
 3. train_model.py (trains the LBPH algorithm on dataset)
 4. f_recognize.py (to detect and recognize faces)
