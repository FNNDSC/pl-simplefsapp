#!/usr/bin/env python                                            
#
# simplefsapp fs ChRIS plugin app
#
# (c) 2021 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#


import os
import time

from chrisapp.base import ChrisApp


Gstr_title = """
     _                 _       __                       
    (_)               | |     / _|                      
 ___ _ _ __ ___  _ __ | | ___| |_ ___  __ _ _ __  _ __  
/ __| | '_ ` _ \| '_ \| |/ _ \  _/ __|/ _` | '_ \| '_ \ 
\__ \ | | | | | | |_) | |  __/ | \__ \ (_| | |_) | |_) |
|___/_|_| |_| |_| .__/|_|\___|_| |___/\__,_| .__/| .__/ 
                | |                        | |   | |    
                |_|                        |_|   |_|    
"""

Gstr_synopsis = """

    NAME

       simplefsapp.py 

    SYNOPSIS

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

    BRIEF EXAMPLE

        * Bare bones execution

            docker run --rm -u $(id -u) -v $(pwd)/out:/outgoing     \
                fnndsc/pl-simplefsapp simplefsapp /outgoing

    DESCRIPTION

        `simplefsapp.py` is a simple ChRIS fs app demo that to copies one or more 
        directories

    ARGS

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
        
        <outputDir> 
        Output directory.
        
        --dir <DIR> 
        Required, it's a string representing a comma-separated list of one or more 
        directories.
        
        [--sleepLength SECONDS]
        If specified, the plugin sleeps before performing any action.
"""


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


class SimpleFSApp(ChrisApp):
    """
    A simple ChRIS fs app demo.
    """
    PACKAGE                 = __package__
    TITLE                   = 'Simple ChRIS fs app'
    CATEGORY                = 'copy'
    TYPE                    = 'fs'
    ICON                    = '' # url of an icon image
    MAX_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS   = 1  # Override with integer value
    MAX_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT           = '' # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT        = '' # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT           = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT           = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Use this dictionary structure to provide key-value output descriptive information
    # that may be useful for the next downstream plugin. For example:
    #
    # {
    #   "finalOutputFile":  "final/file.out",
    #   "viewer":           "genericTextViewer",
    # }
    #
    # The above dictionary is saved when plugin is called with a ``--saveoutputmeta``
    # flag. Note also that all file paths are relative to the system specified
    # output directory.
    OUTPUT_META_DICT = {'out': './out.txt'}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
        Use self.add_argument to specify a new app argument.
        """
        self.add_argument('--dir', dest='dir', type=ChrisApp.path,
                          optional=False, help='look up directory')
        self.add_argument('--sleepLength', dest='sleepLength', type=int,
                          optional=True, default=0,
                          help='time to sleep before performing plugin action')

    def run(self, options):
        """
        Define the code to be run by this plugin app.
        """
        print(Gstr_title)
        print('Version: %s' % self.get_version())
        print('Dir: %s' % options.dir)

        print('Sleeping for %s seconds' % options.sleepLength)
        time.sleep(options.sleepLength)

        str_outFile = os.path.join(options.outputdir, 'out.txt')
        print(os.system('ls ' + options.dir + '>' + str_outFile))

        # Create a 'dummy' listing of empty files mirroring the target dir listing
        with open(str_outFile) as f:
            l_ls = f.readlines()
        print(l_ls)
        l_ls = map(str.strip, l_ls)
        for str_file in l_ls:
            str_fullPath = os.path.join(options.outputdir, str_file)
            print('touching file... %s' % str_fullPath)
            touch(str_fullPath)

    def show_man_page(self):
        """
        Print the app's man page.
        """
        print(Gstr_synopsis)
