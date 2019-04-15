from setuptools import setup, find_packages
setup(name='time_matters',
      version='1.1',
      description='module that discover the relevant dates from a text',
      author='Jorge Alexandre Rocha Mendes',
      author_email='mendesjorge49@gmail.com',
      url='https://github.com/JMendes1995/Time_Matters.git',
      packages=find_packages(include=['time_matters']),
      install_requires=["numpy", "nltk", "pandas", "regex", "langdetect"],
      dependency_links=["git+http://github.com/LIAAD/yake"],
      py_modules=['time_matters'],

)



