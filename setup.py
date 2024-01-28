from setuptools import find_packages, setup


PACKAGE_NAME = "cv_generator_dsl"
VERSION = "0.1.0"
AUTHOR = "Vuk Vukovic"
AUTHOR_EMAIL = "vuk.vukovic.2000@gmail.com"
DESCRIPTION = "A domain-specific language for generating CVs"
KEYWORDS = "textX dsl python CV generator"
LICENSE = "MIT"
URL = "https://github.com/VukV/cv-generator-dsl"


setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords=KEYWORDS,
    license=LICENSE,
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    include_package_data=True,
    package_data={
        "": ["src/dsl/*.tx", "src/transform/templates/*.j2"]
    },
    install_requires=["textx", "Jinja2", "weasyprint"],
    entry_points={
        'textx_languages': [
            'cv_lang = parser.config:cv_parser',
        ],
        'textx_generators': [
            'cv_gen = transform.generator:cv_generator',
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research"
        "Topic :: Software Development :: Code Generators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
