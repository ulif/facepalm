facepalm
========

A tool to blur or pixelize faces in photographs.


Installation
------------

To run `facpalm` script, a suitable environment is required, especially the needed
Python packages and the libs they depend on need to be in place. You can create
a working runtime environment by following the steps described below.

Create a Python virtual environment::

    $ virtualenv -p /usr/bin/python3.6 py36

Activate it::

    $ source ./py36/bin/activate

Install `face_recognition`_::

    (py36) $ pip install face_recognition

Install OpenCV_ Python bindings::

    (py36) $ pip install opencv-python

Now you should be able to import the `face_recognition` and `cv2` packages in
Python scripts. You can check like this::

    (py36) $ python
    >>> import face_recognition
    >>> import cv2

You can leave the interpreter pressing ``CTRL-D``. The above imports should not
raise any exception.

