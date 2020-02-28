#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='rpihat',
      version='1.0.0',
      description='Raspberry Pi HAT',
      author='Li Bai',
      author_email='lbai@temple.edu',
      license='MIT',
      url='https://cflwww.eng.temple.edu',
      packages=find_packages(),
      install_requires=['smbus', 'adafruit-pca9685', 'wiringpi'],
      entry_points={
       'console_scripts':[
          'imu=testimu:callimu'
       ]
     } 
)
