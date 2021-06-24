from setuptools import setup

setup(
    name='cronhost',
    version='0.1',
    description='Cron Host',
    url='https://github.com/thinknum/cronhost',
    download_url='https://github.com/thinknum/cronhost/archive/0.1.tar.gz',    
    packages=['cronhost'],
    package_dir={
        'cronhost': 'src/cronhost',
    },
    install_requires=[
        'contextdecorator==0.10.0',
    ],
    license='BSD',
)
