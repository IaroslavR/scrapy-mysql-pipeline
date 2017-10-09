import setuptools
import os

if "PY_DEV" in os.environ:
    import pypandoc
    with open('README.rst', 'w') as f:
        f.write(pypandoc.convert('README.md', 'rst'))
else:
    os.environ.update(SKIP_WRITE_GIT_CHANGELOG='1')
os.environ.update(SKIP_GENERATE_AUTHORS='1')
setuptools.setup(
    setup_requires=['pbr', ],
    pbr=True
)
