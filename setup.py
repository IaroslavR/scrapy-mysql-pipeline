import setuptools
import os

import pypandoc

with open('README.rst', 'w') as f:
    f.write(pypandoc.convert('README.md', 'rst'))

os.environ.update(
    SKIP_GENERATE_AUTHORS='1',
    # SKIP_WRITE_GIT_CHANGELOG='1'
)
setuptools.setup(
    setup_requires=['pbr', ],
    pbr=True
)
