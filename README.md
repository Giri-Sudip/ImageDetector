###ImageDetector
####This project is made to recognized face on uploading photos. This project is made with following:-
-Reactjs for FrontEnd
-Python FastApi for image api.
-OpenCV for face detection
In this project from frontend on clicking upload button, this image is take by api made with FastApi and is send to OpenCV. OpenCV operates to the image and display in the new python window.

Codes for different part of this project
####FrontEnd(Reactjs)
```npm start```

####Imageapi
It uses uvicorn server and needs to be run in virtual environment.
```
uvicorn <api_file_name>:app --reload
```
####Facedetection
I have used python3 so code to run file is:-
```
python3 <python_file_name> (ex. python3 face_detector.py)
