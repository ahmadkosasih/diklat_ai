import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
	
setuptools.setup(
	name='diklat_ai_kosasih',
	version='0.3',
	author="Ahmad Kosasih",
	author_email="ahmad.kosasih@big.go.id",
	description="An Diklat AI package",
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/ahmadkosasih/diklat_ai",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		],
	install_requires=[
        'Click',
    ],
	entry_points={
        "console_scripts": ['diklat_ai_kosasih=diklat_ai_kosasih.main:welcome']
    },
 )