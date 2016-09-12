import os
from setuptools import setup

requirements_file = os.path.join(os.curdir, 'requirements.txt')

with open(requirements_file, 'r') as fh: 
    requirements = [line for line in fh.read().splitlines() if line]

setup(
      name='youtube_editor',
      version='0.1.1',
      install_requires=requirements,
      description='A quick and dirty package for creating YouTube edits in Jupyter notebooks.',
      url='git@github.com:dm-wyncode/pynotebook-youtube-editor.git',
      author='Don Morehouse',
      author_email='dm.wyncode@gmail.com',
      license='MIT',
      packages=['youtube_editor', ],
      zip_safe=False,
)
