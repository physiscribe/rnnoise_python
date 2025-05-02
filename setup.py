from setuptools import setup

setup(
    name="rnnoise_python",
    version="0.1",
    author="Shb742",
    description="Python wrapper for RNNoise",
    py_modules=["rnnoise"],  # If the main file is rnnoise.py
    install_requires=["numpy", "soundfile"],  # Add dependencies here
)