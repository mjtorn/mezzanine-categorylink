
# vim: tabstop=4 expandtab autoindent shiftwidth=4 fileencoding=utf-8

from setuptools import setup, find_packages

NAME = 'mezzanine-categorylink'
VERSION = '0.0.1'

DESCR = """\
Mezzanine Link objects work with direct slugs or remote http locations.
This allows you to create a link to a blog category by selecting from a dropdown
"""

AUTHOR = u'Markus Törnqvist'
AUTHOR_EMAIL = 'mjt@fadconsulting.com'

URL = 'https://github.com/mjtorn/mezzanine-categorylink'

setup(
    name=NAME,
    version=VERSION,
    description=DESCR,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
    requires=['mezzanine']
)

# EOF

