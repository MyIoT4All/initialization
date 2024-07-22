from setuptools import setup

setup(
   name='MyIoT4All',
   version='1.0',
   description='Remote Telemetry Tools ofr MyIoT4All.com',
   author='MyIoT4All.com',
   author_email='welcome@myiot4all.com',
   packages=['MyIoT4All'],  #same as name
   install_requires=['RPi.version'], #external packages as dependencies
)
