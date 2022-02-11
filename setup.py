"""Setup for RequestCertXBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='request_cert-xblock',
    version='0.1',
    description='Custom HTML XBlock',
    packages=[
        'request_cert',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'request_cert = request_cert:RequestCertXBlock',
        ]
    },
    package_data=package_data("request_cert", "static"),
)
