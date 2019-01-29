import requests
import io
from PIL import Image
'''
# **pyaxiscam**

pyaxiscam is a Python library used to control Axis Communications IP cameras.  You can access information about the
camera as well as grab images (and video stream in the future).



## **Getting Started**

Your Axis camera must first be set up using its web interface.
It is recommended to do this with Internet Explorer on a Windows PC for the best compatibility.
Once set up, you now have a host name (or IP address), username ('root' by default), and the password.
Initialize an AxisCam object using the following line:

    cam = AxisCam('host', 'username', 'password')

A live image can be retrieved by using the following command:

    image = cam.get_live_image()

This image can then be processed using OpenCV for example.

A live image can be retrieved and displayed by using the following command:

    image = cam.display_live_image()

The image is displayed by the default image viewer.

## **Prerequisites**
requests,
io,
PIL
'''

class AxisCam:
    '''
    MIT License

    Copyright (c) 2018 Daniel Orf

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    '''
    def __init__(self, host, username, password):
        """Initializes the AxisCam object
        :param host (str):      The camera's IP address or host name
        :param username (str):  Camera username
        :param password (str):  Camera password
        """
        self.base_url = 'http://{}:{}@{}/axis-cgi/'.format(username, password, host)

    def get_supported_VAPIX_version(self):
        """Returns the version of Axis VAPIX camera API supported by the camera"""
        r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.API.HTTP.Version')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))
        return r.status_code, r.content.decode('utf-8')

    def get_supported_resolutions(self):
        """Returns the available resolutions supported by the camera"""
        r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.Image.Resolution')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))

    def get_supported_image_formats(self):
        """Returns the image formats supported by the camera"""
        r = requests.get(self.base_url + 'param.cgi?action=list&group=Properties.Image.Format')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))

    def get_default_resolution(self):
        """Returns the camera's default image and video resolution"""
        r = requests.get(self.base_url + 'imagesize.cgi?camera=1')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))

    def get_live_image(self):
        """Gets the latest image from the camera
        :return http status code, image:
        """
        r = requests.get(self.base_url + 'jpg/image.cgi')
        print('Return status: ' + str(r.status_code))
        if r.status_code == 200:
            f = io.BytesIO(r.content)
            img = Image.open(f)
        return r.status_code, img

    def display_live_image(self):
        """Gets the latest image from the camera and displays it using PIL package
        :return http status code:
        """
        r = requests.get(self.base_url + 'jpg/image.cgi')
        print('Return status: ' + str(r.status_code))
        if r.status_code == 200:
            f = io.BytesIO(r.content)
            img = Image.open(f)
            img.show()
        return r.status_code

    def get_MJPEG_stream(self):
        # TODO: https://stackoverflow.com/questions/21702477/how-to-parse-mjpeg-http-stream-from-ip-camera
        r = requests.get(self.base_url + 'mjpg/video.cgi')
        print('Return status: ' + str(r.status_code))
        print(r.content.decode('utf-8'))

if __name__ == "__main__":
    cam = AxisCam("192.168.1.26", "root", "u1RlojQp")
    cam.get_supported_VAPIX_version()
    cam.get_supported_resolutions()
    cam.get_supported_image_formats()
    cam.get_live_image()
    cam.get_default_resolution()
    cam.display_live_image()
    cam.get_MJPEG_stream()