##############
pl-simplefsapp
##############

Abstract
========

This simple plugin demonstrates how to run the "File System" class of plugin in ChRIS. This type, FS, is used to create new top-level data trees that constitute the root node in a ChRIS Feed.

***
Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v /home:/incoming -v $(pwd)/out:/outgoing  fnndsc/pl-simplefsapp simplefsapp.py --dir /incoming /outgoing

The above will print the contents of the host ``/home`` dir to the file ``out.txt`` and store in the container's ``/outgoing`` which has been volume mapped to the host ``$(pwd)/out`` directory.

Make sure that the host ``$(pwd)/out`` directory is world writable!


