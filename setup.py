from pathlib import Path
import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

version = {}
exec((this_directory / 'wifi_qrcode_generator' / '__version__.py').read_text(), {}, version)

setuptools.setup(
    name='wifi_qrcode_generator',

    version=version['__version__'],

    description='Generate a QR code for your WiFi network to let others quickly connect.',
    long_description=long_description,
    long_description_content_type='text/markdown',

    url='https://github.com/lakhanmankani/wifi_qrcode_generator',

    author='Lakhan Mankani',
    author_email='lakhan.mankani@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Topic :: Communications',
        
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],

    keywords=['WiFi', 'qrcode'],

    install_requires=['qrcode[pil]'],

    packages=['wifi_qrcode_generator'],

    entry_points={
        'console_scripts': [
            'wifi-qrcode-generator=wifi_qrcode_generator.runner:main',
        ]
    },

    test_suite='setup.test_suite'
)
