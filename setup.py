from setuptools import setup

setup(name="test2",
      version="0.1",
      description="LED Testing for Assignment3 in COMP30670 2017",
      url="",
      author="Wen-ting, Chang",
      author_email="wen-ting.chang@ucdconnect.ie",
      licence="GPL3",
      packages=['src'],
      entry_points={
        'console_scripts':['test2=src.main:main']
        },
      install_requires=[
          'numpy',
      ],
      )