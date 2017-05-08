##############
pl-simplefsapp
##############


Abstract
********

This simple plugin demonstrates how to run the "File System" class of plugin in ChRIS. This type, FS, is used to create new top-level data trees that constitute the root node in a ChRIS Feed.

Run
***

Using ``docker run``
====================

Assign an "input" directory to ``/incoming`` and an output directory to ``/outgoing``

.. code-block:: bash

    docker run -v /home:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-simplefsapp simplefsapp.py            \
            --dir /incoming /outgoing

The above will print the contents of the host ``/home`` dir to the file ``out.txt``. This file will be saved to the container's ``/outgoing`` which in turn has been volume mapped to the host ``$(pwd)/out`` directory. In addition, the ``/outgoing`` diretory will contain a zero-length file with name corresponding to each file in the ``/incoming`` dir.

Make sure that the host ``$(pwd)/out`` directory is world writable!

Example
=======

.. code-block:: bash

    docker run -v /usr/sbin:/incoming -v $(pwd)/out:/outgoing   \
            fnndsc/pl-simplefsapp simplefsapp.py            \
            --dir /incoming /outgoing

will save to the container's ``/outgoing`` (i.e. the host's ``$(pwd)/out``):

.. code-block:: bash

  ls -la out/
  total 20K
  drwxrwxrwx 2 rudolph fnndsc   12K May  8 16:18 ./
  drwxrwxr-x 3 rudolph fnndsc  4.0K May  8 15:45 ../
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 aa-remove-unknown
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 aa-status
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 accept
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 accessdb
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 acpid
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 addgnupghome
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 addgroup
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 add-shell
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 adduser
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 alsabat-test
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 alsactl
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 alsa-info
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 anacron
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 apparmor_status
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 applygnupgdefaults
  -rw-r--r-- 1 nobody  nogroup    0 May  8 16:18 aptd
  ...






