"""Introducing lists

   Roberto Polli - rpolli@babel.it
"""
# before starting this lesson
#  import the python3 print capabilities
#  using the following statement
#  NB since now you *must* always use
#     parenthesis with print!
from __future__ import print_function

# executing Linux bash commands in python shell:
>>> result_ls="ls -lah"
>>> import subprocess
>>> out=subprocess.check_output(result_ls, shell=True)
>>> print(out)
total 56K
drwx------. 20 ip14aai ip14aai 4.0K Feb 15 17:18 .
drwxr-xr-x.  3 root    root      21 Feb  7 14:32 ..
-rw-------.  1 ip14aai ip14aai  12K Feb  9 16:48 .bash_history
-rw-r--r--.  1 ip14aai ip14aai   18 Aug  2  2016 .bash_logout
-rw-r--r--.  1 ip14aai ip14aai  193 Aug  2  2016 .bash_profile
-rw-r--r--.  1 ip14aai ip14aai  231 Aug  2  2016 .bashrc
...
# another example: assuming import subprocess was already done before
>>> out2=subprocess.check_output("hostnamectl", shell=True)
>>> print(out2)
   Static hostname: 02DI20161235444
         Icon name: computer-vm
           Chassis: vm
        Machine ID: 4c44df81a46e4d3ba86019ae9771ff71
           Boot ID: fd87cc19ae1140cba64fd503e4467311
    Virtualization: kvm
  Operating System: CentOS Linux 7 (Core)
       CPE OS Name: cpe:/o:centos:centos:7
            Kernel: Linux 3.10.0-514.el7.x86_64
      Architecture: x86-64

# working with values (info/source: https://pyformat.info
# old style:
>>> print('this is a %s , yes a five, and next is %s' % (5, 6))
this is a 5 , yes a five, and next is 6
# new style:
>>> print('Value 1 is {} and value 2 is {}'.format('one','two'))
Value 1 is one and value 2 is two

# user input / prompt -p:
var1=input('please enter a value: ')

# opening Linux files:
thisFile = open("/proc/diskstats")
print(*thisFile[:], sep "\n")

def introducing_lists():
    # it's easy to create a list
    list_a = ['this', 'is', 'a', 'list']
    # you can append items to a list
    # with the append method
    list_a.append("mutable")

    # check its content with print
    print(list_a)
    # see its length
    len(list_a)

    a = 11
    #range in python 2 returns a list
    # of consecutive ints
    from_0_to_10 = range(a)
    len(from_0_to_10) == a
    # in python 3 things are slightly different
    # so the above code won't work and should
    # should be replaced with the following
    from_0_to_10 = list(range(a))

    # you can get list items by index
    from_0_to_10[0]
    from_0_to_10[11]
    # python lists are doubly linked ;)
    from_0_to_10[-1]
    # please check the manual!
    #help(list)


def slicing():
    # I can slice a list with ":"
    straight = [1, 2, 3, 'star']
    straight[1:3]  # take the middle of the list...
    k = 2  # ... or using a separator
    straight[0:k], straight[k:4]

    straight[:k]         # I can omit the first...
    straight[k:]         # ...and last index


def str_and_list():
    # Strings behaves like lists
    s_a = "Counting: 123"
    # Have length..
    l_a = len(s_a)
    # ..indexes
    print(s_a[0], " ", s_a[-1])
    # and a last element
    s_a[l_a]

    # ...we can even slice them
    f = "prova.txt"
    f[:-4], f[-4], f[-3:]

# working with lambda in lists: functions map or filter:
list1=[4,7,2,9,5,8,7,0,8,7,9]
>>> print(list(filter(lambda x: x%2 == 0, list1)))
[4, 2, 8, 0, 8]

>>> print(list(map(lambda x: x*2, list1)))
[8, 14, 4, 18, 10, 16, 14, 0, 16, 14, 18]


def iterating_with_for():
    a_list = ['is', 'iterable', 'with']
    for x in a_list:
        print(x)
    for x in a_list:
        # python2 does not support the `end` argument
        print((x), end=' ')
        y = x + str(2)
        break       # stop now
    # what's the expected output of the
    # following instruction?
    print(("x,y: ", (x, y)))
    # Differently from C, `for` does not create
    #  a scope


def iterate_with_while():
    a_list = ['is', 'iterable', 'with']
    while a_list:
        # pop() modifies a list removing
        #  and returning its last element
        x = a_list.pop()
        print(("pop out %s" % x))
        break  # what happens if I remove this break?
    print(a_list)
    # What's the expected behavior of the
    #  following instructions?
    for x in a_list:
        print((x + a_list.pop()))
    # for + pop() is not always a good idea ;)
