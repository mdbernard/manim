# Manim - Mathematical Animation Engine
[![Documentation Status](https://readthedocs.org/projects/manim/badge/?version=latest)](https://manim.readthedocs.io/en/latest/?badge=latest)
[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](http://choosealicense.com/licenses/mit/)

Manim is an animation engine for explanatory math videos. It's used to create precise animations programmatically.

## Installation
Manim runs on python 3.7. You can install the python requirements with
`python3 -m pip install -r requirements.txt`. System requirements are
[cairo](https://www.cairographics.org), [latex](https://www.latex-project.org),
[ffmpeg](https://www.ffmpeg.org), and [sox](http://sox.sourceforge.net).

### Directly
```sh
git clone https://github.com/mdbernard/manim.git
cd manim
python3 setup.py install
python3 -m manim example_scenes.py SquareToCircle -pl
```

## Using manim
Try running the following:
```sh
python3 -m manim example_scenes.py SquareToCircle -pl
```
The -p is for previewing, meaning the the video file will automatically open when it is done rendering.
Use -l for a faster rendering at a lower quality.
Use -s to skip to the end and just show the final frame.
Use -n (number) to skip ahead to the n'th animation of a scene.
Use -f to show the file in finder (for osx)

Set MEDIA_DIR environment variable to determine where image and animation files will be written.

Look through the old_projects folder to see the code for previous 3b1b videos.  Note, however, that developments are often made to the library without considering backwards compatibility on those old_projects.  To run them with a guarantee that they will work, you will have to go back to the commit which complete that project.

While developing a scene, the `-sp` flags are helpful to just see what things look like at the end without having to generate the full animation.  It can also be helpful to use the `-n` flag to skip over some number of animations.

### Documentation
Documentation is in progress at [manim.readthedocs.io](https://manim.readthedocs.io).


### Walkthrough
Todd Zimmerman put together a [tutorial](https://talkingphysics.wordpress.com/2019/01/08/getting-started-animating-with-manim-and-python-3-7/) on getting started with manim, which has been updated to run on python 3.7.


## Contributing
Is always welcome. In particular, there is a dire need for tests and documentation.


## License
All files in the directories active_projects and old_projects, which by and large generate the visuals for 3b1b videos, are copyright 3Blue1Brown.

The general purpose animation code found in the remainder of the repository, on the other hand, is under the MIT license.

Note: all 3Blue1Brown copyrighted content removed from this repository (I think).
