import os
from setuptools import setup


NAME = "manim"
DESCRIPTION = "Manim is an animation engine for explanatory math videos. It\'s used to create precise animations programmatically."
URL = "https://github.com/mdbernard/manim"
AUTHOR = "3Blue1Brown"
REQUIRES_PYTHON = ">=3.7.0"
VERSION = "1.0.0"

REQUIRED = [
    "argparse==1.4.0",
    "colour==0.1.5",
    "numpy==1.15.0",
    "Pillow==5.2.0",
    "progressbar==2.5",
    "scipy==1.1.0",
    "tqdm==4.24.0",
    "opencv-python==3.4.2.17",
    "pycairo==1.17.1",
    "pydub==0.23.0"
]

here = os.path.abspath(os.path.dirname(__file__))

try:
    with open(os.path.join(here, "README.md"), encoding="utf-8") as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

about = {}
if not VERSION:
    project_slug = NAME.lower().replace("-", "_").replace(" ", "_")
    try:
        with open(os.path.join(here, project_slug, "__version__.py")) as f:
            exec(f.read(), about)
    except FileNotFoundError:
        about["__version__"] = VERSION
else:
    about["__version__"] = VERSION

setup(
    name=NAME,
    version=about["__version__"],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    install_requires=REQUIRED,
    include_package_data=True,
    license="MIT"
)

