#!/usr/bin/env python

from setuptools import setup, Extension

ext = Extension('myext._myfunc',
                 sources  =['src/myfunc.i', 'src/myfunc.c']
                 )

setup (name = 'myext',
       version = '1.0.0',
       description = """test python extension""",
       author      = "Xiaoqiang Wang",
       author_email= "xiaoqiangwang@gmail.com",
       ext_modules = [ext],
       packages    = ["myext"],
       package_dir={"myext": "src"},
       license     = "BSD",
    )


