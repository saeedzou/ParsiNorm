import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='parsinorm',  
     version='0.0.2',
     packages=['parsinorm'] ,
     author="HaraAi",
     author_email="info@hara.ai",
     description="Persain Text Pre-Proceesing Tool",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/haraai/ParsiNorm",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     install_requires=['num2fawords', 'persian-tools', 'urlextract'],
 )
