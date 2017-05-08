##############
pl-simplefsapp
##############

# Abstract

This simple plugin demonstrates how to run the "File System" class of plugin in ChRIS. This type, FS, is used to create new top-level data trees that constitute the root node in a ChRIS Feed.

# Run

## Using <tt>docker run</tt>

Assign an "input" directory to <tt>/incoming</tt> and an output directory to <tt>/outgoing</tt>

```bash
docker run -v /home:/incoming -v $(pwd)/out:/outgoing  fnndsc/pl-simplefsapp simplefsapp.py --dir /incoming /outgoing
```
   
