import cv2
import urllib.request
import numpy as np




url = [
    "http://127.0.0.1:8000/images/"
]


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    #return the image
    return image


for url in url:
    trained_face_data = cv2.CascadeClassifier(
        'haarcascade_frontalface_default.xml')
    x = y = w = h = int
    image = url_to_image(url)
    face_coordinates = trained_face_data.detectMultiScale(image,
                                                          scaleFactor=1.1,
                                                          minNeighbors=5,
                                                          minSize=(30, 30),
                                                          flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in face_coordinates:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imshow("Image", image)
cv2.waitKey(0)






# from tkinter import image_names
# import cv2
# import urllib.request
# import numpy as np

# # load some pre-trained data on face frontals from opencv using algorithm
# trained_face_data = cv2.CascadeClassifier(
#     'haarcascade_frontalface_default.xml')


# url='http://127.0.0.1:8000/images/'
# url_response = urllib.request.urlopen(url)
# # # bytes_data = uploaded_file.getvalue()


# #  choosing image to detect face
# img = cv2.imread(url_response)


# # # converting color to gray scale.
# grayscaled_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# facecascade = cv2.CascadeClassifier('http://127.0.0.1:8000/images/')


# # # Detect faces
# face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)

# # # Draw rectangles
# # # cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 2)
# cv2.rectangle(img, (315, 431), (315+1286, 431+1286), (0, 255, 0), 2)

# img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
# img = cv2.imdecode(img_array, -1)

# # # Display Grey Image
# cv2.imshow('Face Detection', img)


# print(face_coordinates)


# # # wait for execution
# cv2.waitKey()

# print("successfully done")


# import numpy as np

# import io
# import json
# import cv2
# import os              #const.py


# def detect_face(binaryimg):
#     data = {"success": False}
#     if binaryimg is None:
#         return data

#     # convert the binary image to image
#     image = read_cv2_image(binaryimg)

#     # convert the image to grayscale
#     imagegray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # load the face cascade detector,
#     facecascade = cv2.CascadeClassifier('http://127.0.0.1:8000/images/')

#     # detect faces in the image
#     facedetects = facecascade.detectMultiScale(imagegray, scaleFactor=1.1, minNeighbors=5,
#         minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

#     # construct a list of bounding boxes from the detection
#     facerect = [(int(fx), int(fy), int(fx + fw), int(fy + fh)) for (fx, fy, fw, fh) in facedetects]

#     # update the data dictionary with the faces detected
#     data.update({"num_faces": len(facerect), "faces": facerect, "success": True})
#     print(json.dumps(data))

#     # return the data dictionary as a JSON response
#     return data


# def read_cv2_image(binaryimg):

#     stream = io.BytesIO(binaryimg)

#     image = np.asarray(bytearray(stream.read()), dtype="uint8")
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)

#     return image
