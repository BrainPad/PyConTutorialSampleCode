from setuptools import setup

package = 'samplebot'
version = '0.1'

setup(
    name=package,
    version=version,
    description="Slack smaplebot",
    packages=['samplebot'],
    test_suite='test',
)
