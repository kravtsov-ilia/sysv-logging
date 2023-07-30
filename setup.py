import setuptools


setuptools.setup(
    name='sysv_logging',
    packages=['sysv_logging'],
    version='0.1.0',
    license='MIT',
    description='Shared memory logging. Logger uses system V message queues',
    long_description='Shared memory logging. Logger uses system V message queues',
    long_description_content_type="text/plain",
    author='Ilia Kravtsov',
    author_email='kravcov2512@gmail.com',
    url='https://github.com/kravtsov-ilia/sysv-logging.git',
    project_urls={
        "Bug Tracker": "https://github.com/kravtsov-ilia/sysv-logging/issues"
    },
    install_requires=['sysv_ipc==1.1.0'],
    keywords=["pypi", "mikes_toolbox", "tutorial"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: System :: Logging',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    download_url="https://github.com/kravtsov-ilia/sysv-logging/archive/refs/heads/main.zip",
)