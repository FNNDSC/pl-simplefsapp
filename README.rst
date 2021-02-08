pl-simplefsapp
================================

.. image:: https://img.shields.io/docker/v/fnndsc/pl-simplefsapp
    :target: https://hub.docker.com/r/fnndsc/pl-simplefsapp

.. image:: https://img.shields.io/github/license/fnndsc/pl-simplefsapp
    :target: https://github.com/FNNDSC/pl-simplefsapp/blob/master/LICENSE

.. image:: https://github.com/FNNDSC/pl-simplefsapp/workflows/ci/badge.svg
    :target: https://github.com/FNNDSC/pl-simplefsapp/actions


.. contents:: Table of Contents


Abstract
--------

A simple ChRIS fs app demo. If called directly, i.e. from the command line, the input directory
is an actual specification on an actual filesystem. If called from a client that is talking to
CUBE, this input directory is interpreted to mean a location within swift storage, and is not a
file system location.


Description
-----------

``simplefsapp`` is a simple ChRIS-based application that demonstrates how to run the "File System"
class of plugin in ChRIS. This type, FS, is used to create new top-level data trees that constitute
the root node in a ChRIS Feed.


Usage
-----

.. code::

        python simplefsapp.py
            [-h] [--help]
            [--json]
            [--man]
            [--meta]
            [--savejson <DIR>]
            [-v <level>] [--verbosity <level>]
            [--version]
            <outputDir>
            --dir <DIR>
            [--sleepLength SECONDS]


The above will print the contents of the host ``/home`` dir to the file ``out.txt``. This file will be saved to the container's ``/outgoing`` which in turn has been volume mapped to the host ``$(pwd)/out`` directory. In addition, the ``/outgoing`` diretory will contain a zero-length file with name corresponding to each file in the ``/incoming`` dir.
Arguments
~~~~~~~~~

.. code::

    [-h] [--help]
    If specified, show help message and exit.
    
    [--json]
    If specified, show json representation of app and exit.
    
    [--man]
    If specified, print (this) man page and exit.

    [--meta]
    If specified, print plugin meta data and exit.
    
    [--savejson <DIR>] 
    If specified, save json representation file to DIR and exit. 
    
    [-v <level>] [--verbosity <level>]
    Verbosity level for app. Not used currently.
    
    [--version]
    If specified, print version number and exit. 


Getting inline help is:

.. code:: bash

    docker run --rm fnndsc/pl-simplefsapp simplefsapp --man

Run
~~~

You need you need to specify input and output directories using the `-v` flag to `docker run`.


.. code:: bash

    docker run --rm -u $(id -u) -v $(pwd)/out:/outgoing      \
        fnndsc/pl-simplefsapp simplefsapp /outgoing --dir <DIR>

The above will print the contents of <DIR> to the file ``out.txt``. This file
will be saved to the container's ``/outgoing`` which in turn has been volume mapped to the host
``$(pwd)/out`` directory. In addition, the ``/outgoing`` diretory will contain zero-length files
with name corresponding to each file in <DIR>.


Development
-----------

Build the Docker container:

.. code:: bash

    docker build -t local/pl-simplefsapp .

Run unit tests:

.. code:: bash

    docker run --rm local/pl-simplefsapp nosetests

Examples
--------

.. code:: bash

    docker run --rm -v $(pwd)/out:/outgoing fnndsc/pl-simplefsapp    \
        simplefsapp /outgoing --dir '~/uploads,/tmp'


.. image:: https://raw.githubusercontent.com/FNNDSC/cookiecutter-chrisapp/master/doc/assets/badge/light.png
    :target: https://chrisstore.co
