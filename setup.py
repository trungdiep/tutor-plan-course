import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.rst"), "rt", encoding="utf8") as f:
        return f.read()


def load_about():
    about = {}
    with io.open(
        os.path.join(HERE, "tutorplan_course", "__about__.py"),
        "rt",
        encoding="utf-8",
    ) as f:
        exec(f.read(), about)  # pylint: disable=exec-used
    return about


ABOUT = load_about()


setup(
    name="tutor-plan-course",
    version=ABOUT["__version__"],
    url="https://github.com/trungdiep/tutor-plan-course.git",
    project_urls={
        "Code": "https://github.com/trungdiep/tutor-plan-course.git",
        "Issue tracker": "https://github.com/trungdiep/tutor-plan-course.git/issues",
    },
    license="AGPLv3",
    author="Diep Van Trung",
    description="plan-course plugin for Tutor",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=["tutor-openedx"],
    # entry_points={
    #     "tutor.plugin.v0": [
    #         "plan-course = tutorplan_course.plugin"
    #     ]
    # },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    entry_points={
        'lms.djangoapp': [
            "edx_when = edx_when.apps:EdxWhenConfig",
        ],
        'cms.djangoapp': [
            "edx_when = edx_when.apps:EdxWhenConfig",
        ],
        'openedx.block_structure_transformer': [
            'load_date_data = edx_when.field_data:DateOverrideTransformer'
        ],

    },
)
