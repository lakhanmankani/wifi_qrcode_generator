import setuptools

LONG_DESCRIPTION = r'''
wifi_qrcode_generator
=====================

Generate a qr code for your wifi network to let others quickly connect your wifi without having the need to tell them your long and complicated password.

Dependencies:

* Pillow
* qrcode

Usage:

.. code-block:: bash

    $ wifi-qrcode-generator

Or as a Python API

.. code-block:: python

    #!/usr/bin/env python3
    import wifi_qrcode_generator

    wifi_qrcode_generator.wifi_qrcode(
      'Home wifi', False, 'WPA', 'very complicated password'
    )

'''.lstrip('\n')

setuptools.setup(
    name='wifi_qrcode_generator',

    version='0.1',

    description='Generate a qr code for your wifi to let others quickly connect your wifi.',
    long_description=LONG_DESCRIPTION,

    url='https://github.com/lakhanmankani/wifi_qrcode_generator',

    author='Lakhan Mankani',
    author_email='lakhan.mankani@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Environment :: Console',

        'Intended Audience :: End Users/Desktop',

        'License :: OSI Approved :: MIT License',

        'Operating System :: OS Independent',

        'Topic :: Communications',
        
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],

    keywords=['WiFi', 'qrcode'],

    py_modules=['wifi_qrcode_generator'],

    install_requires=['Pillow', 'qrcode'],

    entry_points={
        'console_scripts': [
            'wifi-qrcode-generator=wifi_qrcode_generator:main',
        ]
    },

    test_suite='setup.test_suite'
)
