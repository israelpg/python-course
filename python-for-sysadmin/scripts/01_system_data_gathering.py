""" Python for System Administrators

    Gathering System Data with multiplatform
     and platform-dependent tools like command
     line output and files.

"""
#
# Our code is p3-ready
#
from __future__ import print_function


# execute Linux command using a def:
def bashCommand(cmd):
        import subprocess
        output = subprocess.check_output(cmd, shell = True)
        print(output)
# ... in execution:
>>> bashCommand("pwd ; touch aaa1.txt ; ls -lah")
/home/ip14aai
total 56K
drwx------. 20 ip14aai ip14aai 4.0K Feb 16 16:17 .
drwxr-xr-x.  3 root    root      21 Feb  7 14:32 ..
-rw-rw-r--.  1 ip14aai ip14aai    0 Feb 16 16:17 aaa1.txt
-rw-------.  1 ip14aai ip14aai  12K Feb  9 16:48 .bash_history
-rw-r--r--.  1 ip14aai ip14aai   18 Aug  2  2016 .bash_logout
...

# although sometimes is better to pass command bash arguments in a list:
# and use Popen for dealing with PIPE:
cmd = ["ls", "-la"]
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
for line in proc.stdout.readlines():
    print line

# open file works like this:

>>> x=open("/proc/diskstats")
>>> type(x)
<type 'file'>
>>> print(x)
<open file '/proc/diskstats', mode 'r' at 0x13d30c0>
>>> for i in x:
	print(i)

	
   8       0 sda 20604 39 1792286 54075 49982 9471 918230 74705 0 41844 128612

   8       1 sda1 1965 0 55152 888 29 0 4289 106 0 425 994

   8       2 sda2 18514 39 1735198 53049 42056 9471 913941 71125 0 39259 124005

  11       0 sr0 21 0 132 8 0 0 0 0 0 8 8

 253       0 dm-0 18381 0 1732278 55318 52002 0 913941 205451 0 41690 260771

 253       1 dm-1 128 0 2136 159 0 0 0 0 0 156 159


# function grep with two args, one is the grep itself-->needle (string) and fpath
# a for loop is used to iterate in conjunction with open function
# the function is called like this: disk_l = grep("sda", "/proc/diskstats")
def grep(needle, fpath):
    """A simple grep implementation

       goal: open() is iterable and don't
             needs splitlines()
       goal: comprehension can filter lists
    """
    # for x in open.. "iterates to fetch lines content of opened file", checking grep for x, return if exists:
    resultGrep = return [x for x in open(fpath) if needle in x]
    print(*resultGrep[:], sep="\n")

    #-------------------
    # for instance in python shell:
    >>> resultGrep1=grepFunction('sda','/proc/diskstats')
    >>> type(resultGrep1)
    <type 'list'>
    >>> print(resultGrep1)
    ['   8       0 sda 20604 39 1792286 54075 50072 9482 919249 74794 0 41927 128701\n', '   8       1 sda1 1965 0 55152 888 29 0 4289 106 0 425 994\n', '   8       2 sda2 18514 39 1735198 53049 42127 9482 914960 71206 0 39336 124086\n']
    # better with a nice \n format:
    print(*resultGrep1[:], sep="\n") # \t for tab
           8       0 sda 20604 39 1792286 54075 50072 9482 919249 74794 0 41927 128701

           8       1 sda1 1965 0 55152 888 29 0 4289 106 0 425 994

           8       2 sda2 18514 39 1735198 53049 42127 9482 914960 71206 0 39336 124086
    #--------------------

def linux_threads(pid):
    """"Glob emulates shell expansion of * and ?

         goal: use globbing and format
         goal: linux proc structure
         goal: startswith accepts tuple arguments
    """
    import glob
    path = "/proc/{}/task/*/status".format(pid) # need format to enter arg in string, cannot call var
    t_info = ('Pid', 'Tgid', 'voluntary')  # this is a tuple!
    for t in glob.glob(path): # glob.glob() --> selects a folder in Linux file hierarchy, fetch file by file
        t_info = [x for x in open(t) if x.startswith(t_info)] # and checks in that file if name startswith..
        print(*t_info[:], sep="\n")


def multiplatform_stats(count):
    """Multiplatform stats with numpy.array"""
    raise NotImplementedError


def sh(cmd, shell=False, timeout=0):
    """"Execute a command returning a line-splitted list

       @param cmd - a command string
       @param shell - run command in a shell
       @param timeout - (for python 3.3+) in seconds

       goal: use sys to check python features
       goal: use subprocess.check_output
    """
    from sys import version_info as python_version
    from subprocess import check_output
    if python_version < (3, 3):
        if timeout:
            raise ValueError("Timeout not supported until Python 3.3")
        output = check_output(cmd.split(), shell=shell)
    else:
        output = check_output(cmd.split(), shell=shell, timeout=timeout)
    return output.splitlines()


def system_info_from_command_output():
    """Exercise: write a multiplatform
        pgrep-like function

       Solution is at the EOF
    """
    def pgrep(expr):
        raise NotImplementedError


def zip_iterables():
    """The zip method joins list elements pairwise
        like a zip fastener
    """
    from sys import version_info as python_version
    a_list = [0, 1, 2, 3]
    b_list = ["a", "b", "c", "d"]
    zipper = zip(a_list, b_list)
    if python_version >= (3,):
        zipper = list(zipper)
    assert zipper == [(0, "a"), (1, "b"), (2, "c"), (3, "d")]

# calling this function, eg: linux_diskstats(sda)
def linux_diskstats(disk):
    """Get I/O information from /proc/diskstats

       @param disk def sda
       goal: usage of time.sleep
       goal: usage of zip
       goal: use string concatenation to increase readability
       goal: use *magic with print+sep, splitting and slicing
    """
    from time import sleep
    info = ('reads reads_merged reads_sectors reads_ms'
            ' writes writes_merged writes_sectors writes_ms'
            ' io_in_progress io_ms_weight').split()
    print(*info[:8], sep="\t")
    old = [0] * 11

    while True:
        disk_l = grep(disk, "/proc/diskstats")
        if len(disk_l) > 1:
            raise ValueError("More than one partition matches!")

        info = disk_l[0].split()
        # the first 3 fields are disk informations
        cur = map(int, info[3:])
        delta = [x - y for (x, y) in zip(cur, old)]
        print(*delta[:8], sep="\t")
        old = cur
        sleep(1)

#
# A more complex exercise using a lot of stuff
#

