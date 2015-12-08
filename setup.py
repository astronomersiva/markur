from setuptools import setup

setup(
	name='markur',
    version='0.1',
    description='URL to Markdown converter',
    license='MIT',
    scripts=['markur'],
    install_requires=[
    	'pyperclip',
    ],
    zip_safe=False
)
