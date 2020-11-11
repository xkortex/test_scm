# setuptools_scm issue

#### Works from $REPO/:
 - python setup.py --version
 - pip install .
 - python setup.py install
 - python setup.py sdist bdist_wheel
 - python sub2/setup.py --version
 - pip install -e ./sub/
 - pip install -e ./sub2/

#### Works from $REPO/sub:
 - python setup.py --version

#### Fails from $REPO: 
 - pip install $PWD/sub
 - pip install $PWD/sub2
 - pip install $PWD/sub3 # this is expected due to lack of setup.py
 

#### Succeeds but does not insert version (generates UNKNOWN-0.0.0):
- pip install $PWD/sub3