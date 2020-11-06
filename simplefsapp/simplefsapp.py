#                                                            _
# Simple chris fs app demo
#
# (c) 2016 Fetal-Neonatal Neuroimaging & Developmental Science Center
#                   Boston Children's Hospital
#
#              http://childrenshospital.org/FNNDSC/
#                        dev@babyMRI.org
#

import os
import time

# import the Chris app superclass
from chrisapp.base import ChrisApp


def touch(path):
    with open(path, 'a'):
        os.utime(path, None)


class SimpleFSApp(ChrisApp):
    """
    Create file out.txt with the directory listing of the directory
    given by the --dir argument.
    """
    AUTHORS         = 'FNNDSC (dev@babyMRI.org)'
    SELFPATH        = os.path.dirname(os.path.abspath(__file__))
    SELFEXEC        = os.path.basename(__file__)
    EXECSHELL       = 'python3'
    TITLE           = 'Simple chris fs app'
    CATEGORY        = 'copy'
    TYPE            = 'fs'
    DESCRIPTION     = 'A simple chris fs app demo'
    DOCUMENTATION   = 'http://wiki'
    LICENSE         = 'Opensource (MIT)'
    VERSION         = '0.21'
    MAX_NUMBER_OF_WORKERS = 1  # Override with integer value
    MIN_NUMBER_OF_WORKERS = 1  # Override with integer value
    MAX_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MIN_CPU_LIMIT = ''  # Override with millicore value as string, e.g. '2000m'
    MAX_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_MEMORY_LIMIT = ''  # Override with string, e.g. '1Gi', '2000Mi'
    MIN_GPU_LIMIT = 0  # Override with the minimum number of GPUs, as an integer, for your plugin
    MAX_GPU_LIMIT = 0  # Override with the maximum number of GPUs, as an integer, for your plugin

    # Fill out this with key-value output descriptive info (such as an output file path
    # relative to the output dir) that you want to save to the output meta file when
    # called with the --saveoutputmeta flag
    OUTPUT_META_DICT = {'out': './out.txt'}

    def define_parameters(self):
        """
        Define the CLI arguments accepted by this plugin app.
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
        print('Sleeping for %s seconds' % options.sleepLength)
        time.sleep(options.sleepLength)
        
        str_outFile = os.path.join(options.outputdir, 'out.txt')
        print(os.system('ls ' + options.dir + '>' + str_outFile))

        # Create a 'dummy' listing of empty files mirroring the target dir listing
        with open(str_outFile) as f:
            l_ls    = f.readlines()
        print(l_ls)
        l_ls = map(str.strip, l_ls)
        for str_file in l_ls:
            str_fullPath    = os.path.join(options.outputdir, str_file)
            print('touching file... %s' % str_fullPath)
            touch(str_fullPath)


# ENTRYPOINT
if __name__ == "__main__":
    app = SimpleFSApp()
    app.launch()
