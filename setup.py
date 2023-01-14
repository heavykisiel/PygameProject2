from setuptools import setup, find_packages

setup(
    name='GamePack',
    version='1.0.1',
    url='https://github.com/heavykisiel/PygameProject2.git',
    author='LLMM',
    description='Package that need to by installed to play a game',
    entry_points={
        'console_scripts': ['start=PygameProject2:main']
    },
    packages=find_packages(include=['PygameProject']),
    install_requires=['pygame'],
)