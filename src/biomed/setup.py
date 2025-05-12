import os
from glob import glob
from setuptools import setup

package_name = 'biomed'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    package_data={
        package_name: [
            'resource/biomed/*',
            'urdf/*',
        ],
    },
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/biomed_launch.py']),
        # ↓↓↓ urdf klasöründeki tüm dosyaları listele
        ('share/' + package_name + '/urdf', glob('urdf/*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='yavuzhan',
    maintainer_email='yavuzhan@todo.todo',
    description='Biomed robot el simülasyonu',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'mainCode = biomed.publisher:main',
        ],
    },
)
