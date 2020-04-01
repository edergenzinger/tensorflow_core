import setuptools

setuptools.setup(name='tensorflow_core',
    version='0.1',
    description='Bugfix to create a tensorflow_core alias for tensorflow',
    #url
    author='Ergenzinger',
    author_email='eergenzinger@outlook.com',
    keywords=['alias','bugfix','tensorflow'],
    license='MIT',
    #packages=[''],
    install_requires=['tensorflow'],
    zip_safe=True,
    classifiers=[
    'Development Status :: 4 - Beta',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 2', #to be checked
    ],
  )