# Face_comparison
**🧠 Face Recognition using Python and OpenCV**

This project demonstrates face recognition using the face_recognition library along with OpenCV. It compares two images of a person and determines whether they belong to the same individual or not.

**📸 Overview**

The code performs the following steps:
Loads two images (a reference and a test image).
Detects the face in both images.
Encodes facial features into numerical arrays.
Compares the encodings to find a match.
Displays both images with bounding boxes and matching results.

**🧩 Features
**
Face detection and encoding using the face_recognition library.
Face comparison using Euclidean distance.
Displays real-time match result and confidence value.
Simple and easy to extend for multiple faces or datasets.

**🛠️ Requirements**

Install the following Python libraries before running the code:

pip install face_recognition
pip install opencv-python
pip install numpy


Note: face_recognition requires dlib.
On Windows, you may need to install CMake and Visual Studio Build Tools before installing it.
**
📂 Project Structure**
face_recognition_project/
│
├── musk1.jpg               # Reference image
├── musk2.jpg               # Test image
├── face_recognition_demo.py  # Main Python script
└── README.md               # Project documentation

**▶️ How to Run**

Clone the repository:
git clone https://github.com/<your-username>/face-recognition-project.git
Navigate to the project folder:
cd face-recognition-project

Run the script:
python face_recognition_demo.py
Two windows will appear showing:
The reference image with a bounding box.
The test image with the match result and face distance.

**🧮 Output Example**

Example console output:
[True] [0.48]

The window will display text like:
True 0.48

True → The faces match.

0.48 → Lower distance means higher similarity.

**📘 Future Improvements**

Extend to recognize multiple people from a dataset.
Integrate webcam-based real-time face recognition.
Add attendance marking using recognized faces.
