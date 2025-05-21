from setuptools import find_packages, setup

package_name = 'new_pkg'

setup(
    name=package_name,
    version='1.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='muntaham',
    maintainer_email='muntahammahmud@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'puber = new_pkg.pub1:main',
            'puber2 = new_pkg.pub2:main',
            'puber3 = new_pkg.mode_runner:main',

        ],
    },
)
