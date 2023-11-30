r"""Wrapper for cudd.h

Generated with:
/home/juanlu/anaconda3/bin/ctypesgen -llibcudd-3.0.0.so cudd.h -o cudd.py

Do not modify this file.
"""

__docformat__ = "restructuredtext"

# Begin preamble for Python v(3, 2)

import ctypes, os, sys
from ctypes import *

_int_types = (c_int16, c_int32)
if hasattr(ctypes, "c_int64"):
    # Some builds of ctypes apparently do not have c_int64
    # defined; it's a pretty good bet that these builds do not
    # have 64-bit pointers.
    _int_types += (c_int64,)
for t in _int_types:
    if sizeof(t) == sizeof(c_size_t):
        c_ptrdiff_t = t
del t
del _int_types


class UserString:
    def __init__(self, seq):
        if isinstance(seq, bytes):
            self.data = seq
        elif isinstance(seq, UserString):
            self.data = seq.data[:]
        else:
            self.data = str(seq).encode()

    def __bytes__(self):
        return self.data

    def __str__(self):
        return self.data.decode()

    def __repr__(self):
        return repr(self.data)

    def __int__(self):
        return int(self.data.decode())

    def __long__(self):
        return int(self.data.decode())

    def __float__(self):
        return float(self.data.decode())

    def __complex__(self):
        return complex(self.data.decode())

    def __hash__(self):
        return hash(self.data)

    def __cmp__(self, string):
        if isinstance(string, UserString):
            return cmp(self.data, string.data)
        else:
            return cmp(self.data, string)

    def __le__(self, string):
        if isinstance(string, UserString):
            return self.data <= string.data
        else:
            return self.data <= string

    def __lt__(self, string):
        if isinstance(string, UserString):
            return self.data < string.data
        else:
            return self.data < string

    def __ge__(self, string):
        if isinstance(string, UserString):
            return self.data >= string.data
        else:
            return self.data >= string

    def __gt__(self, string):
        if isinstance(string, UserString):
            return self.data > string.data
        else:
            return self.data > string

    def __eq__(self, string):
        if isinstance(string, UserString):
            return self.data == string.data
        else:
            return self.data == string

    def __ne__(self, string):
        if isinstance(string, UserString):
            return self.data != string.data
        else:
            return self.data != string

    def __contains__(self, char):
        return char in self.data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.__class__(self.data[index])

    def __getslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        return self.__class__(self.data[start:end])

    def __add__(self, other):
        if isinstance(other, UserString):
            return self.__class__(self.data + other.data)
        elif isinstance(other, bytes):
            return self.__class__(self.data + other)
        else:
            return self.__class__(self.data + str(other).encode())

    def __radd__(self, other):
        if isinstance(other, bytes):
            return self.__class__(other + self.data)
        else:
            return self.__class__(str(other).encode() + self.data)

    def __mul__(self, n):
        return self.__class__(self.data * n)

    __rmul__ = __mul__

    def __mod__(self, args):
        return self.__class__(self.data % args)

    # the following methods are defined in alphabetical order:
    def capitalize(self):
        return self.__class__(self.data.capitalize())

    def center(self, width, *args):
        return self.__class__(self.data.center(width, *args))

    def count(self, sub, start=0, end=sys.maxsize):
        return self.data.count(sub, start, end)

    def decode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.decode(encoding, errors))
            else:
                return self.__class__(self.data.decode(encoding))
        else:
            return self.__class__(self.data.decode())

    def encode(self, encoding=None, errors=None):  # XXX improve this?
        if encoding:
            if errors:
                return self.__class__(self.data.encode(encoding, errors))
            else:
                return self.__class__(self.data.encode(encoding))
        else:
            return self.__class__(self.data.encode())

    def endswith(self, suffix, start=0, end=sys.maxsize):
        return self.data.endswith(suffix, start, end)

    def expandtabs(self, tabsize=8):
        return self.__class__(self.data.expandtabs(tabsize))

    def find(self, sub, start=0, end=sys.maxsize):
        return self.data.find(sub, start, end)

    def index(self, sub, start=0, end=sys.maxsize):
        return self.data.index(sub, start, end)

    def isalpha(self):
        return self.data.isalpha()

    def isalnum(self):
        return self.data.isalnum()

    def isdecimal(self):
        return self.data.isdecimal()

    def isdigit(self):
        return self.data.isdigit()

    def islower(self):
        return self.data.islower()

    def isnumeric(self):
        return self.data.isnumeric()

    def isspace(self):
        return self.data.isspace()

    def istitle(self):
        return self.data.istitle()

    def isupper(self):
        return self.data.isupper()

    def join(self, seq):
        return self.data.join(seq)

    def ljust(self, width, *args):
        return self.__class__(self.data.ljust(width, *args))

    def lower(self):
        return self.__class__(self.data.lower())

    def lstrip(self, chars=None):
        return self.__class__(self.data.lstrip(chars))

    def partition(self, sep):
        return self.data.partition(sep)

    def replace(self, old, new, maxsplit=-1):
        return self.__class__(self.data.replace(old, new, maxsplit))

    def rfind(self, sub, start=0, end=sys.maxsize):
        return self.data.rfind(sub, start, end)

    def rindex(self, sub, start=0, end=sys.maxsize):
        return self.data.rindex(sub, start, end)

    def rjust(self, width, *args):
        return self.__class__(self.data.rjust(width, *args))

    def rpartition(self, sep):
        return self.data.rpartition(sep)

    def rstrip(self, chars=None):
        return self.__class__(self.data.rstrip(chars))

    def split(self, sep=None, maxsplit=-1):
        return self.data.split(sep, maxsplit)

    def rsplit(self, sep=None, maxsplit=-1):
        return self.data.rsplit(sep, maxsplit)

    def splitlines(self, keepends=0):
        return self.data.splitlines(keepends)

    def startswith(self, prefix, start=0, end=sys.maxsize):
        return self.data.startswith(prefix, start, end)

    def strip(self, chars=None):
        return self.__class__(self.data.strip(chars))

    def swapcase(self):
        return self.__class__(self.data.swapcase())

    def title(self):
        return self.__class__(self.data.title())

    def translate(self, *args):
        return self.__class__(self.data.translate(*args))

    def upper(self):
        return self.__class__(self.data.upper())

    def zfill(self, width):
        return self.__class__(self.data.zfill(width))


class MutableString(UserString):
    """mutable string objects

    Python strings are immutable objects.  This has the advantage, that
    strings may be used as dictionary keys.  If this property isn't needed
    and you insist on changing string values in place instead, you may cheat
    and use MutableString.

    But the purpose of this class is an educational one: to prevent
    people from inventing their own mutable string class derived
    from UserString and than forget thereby to remove (override) the
    __hash__ method inherited from UserString.  This would lead to
    errors that would be very hard to track down.

    A faster and better solution is to rewrite your program using lists."""

    def __init__(self, string=""):
        self.data = string

    def __hash__(self):
        raise TypeError("unhashable type (it is mutable)")

    def __setitem__(self, index, sub):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + sub + self.data[index + 1 :]

    def __delitem__(self, index):
        if index < 0:
            index += len(self.data)
        if index < 0 or index >= len(self.data):
            raise IndexError
        self.data = self.data[:index] + self.data[index + 1 :]

    def __setslice__(self, start, end, sub):
        start = max(start, 0)
        end = max(end, 0)
        if isinstance(sub, UserString):
            self.data = self.data[:start] + sub.data + self.data[end:]
        elif isinstance(sub, bytes):
            self.data = self.data[:start] + sub + self.data[end:]
        else:
            self.data = self.data[:start] + str(sub).encode() + self.data[end:]

    def __delslice__(self, start, end):
        start = max(start, 0)
        end = max(end, 0)
        self.data = self.data[:start] + self.data[end:]

    def immutable(self):
        return UserString(self.data)

    def __iadd__(self, other):
        if isinstance(other, UserString):
            self.data += other.data
        elif isinstance(other, bytes):
            self.data += other
        else:
            self.data += str(other).encode()
        return self

    def __imul__(self, n):
        self.data *= n
        return self


class String(MutableString, Union):

    _fields_ = [("raw", POINTER(c_char)), ("data", c_char_p)]

    def __init__(self, obj=""):
        if isinstance(obj, (bytes, UserString)):
            self.data = bytes(obj)
        else:
            self.raw = obj

    def __len__(self):
        return self.data and len(self.data) or 0

    def from_param(cls, obj):
        # Convert None or 0
        if obj is None or obj == 0:
            return cls(POINTER(c_char)())

        # Convert from String
        elif isinstance(obj, String):
            return obj

        # Convert from bytes
        elif isinstance(obj, bytes):
            return cls(obj)

        # Convert from str
        elif isinstance(obj, str):
            return cls(obj.encode())

        # Convert from c_char_p
        elif isinstance(obj, c_char_p):
            return obj

        # Convert from POINTER(c_char)
        elif isinstance(obj, POINTER(c_char)):
            return obj

        # Convert from raw pointer
        elif isinstance(obj, int):
            return cls(cast(obj, POINTER(c_char)))

        # Convert from c_char array
        elif isinstance(obj, c_char * len(obj)):
            return obj

        # Convert from object
        else:
            return String.from_param(obj._as_parameter_)

    from_param = classmethod(from_param)


def ReturnString(obj, func=None, arguments=None):
    return String.from_param(obj)


# As of ctypes 1.0, ctypes does not support custom error-checking
# functions on callbacks, nor does it support custom datatypes on
# callbacks, so we must ensure that all callbacks return
# primitive datatypes.
#
# Non-primitive return values wrapped with UNCHECKED won't be
# typechecked, and will be converted to c_void_p.
def UNCHECKED(type):
    if hasattr(type, "_type_") and isinstance(type._type_, str) and type._type_ != "P":
        return type
    else:
        return c_void_p


# ctypes doesn't have direct support for variadic functions, so we have to write
# our own wrapper class
class _variadic_function(object):
    def __init__(self, func, restype, argtypes, errcheck):
        self.func = func
        self.func.restype = restype
        self.argtypes = argtypes
        if errcheck:
            self.func.errcheck = errcheck

    def _as_parameter_(self):
        # So we can pass this variadic function as a function pointer
        return self.func

    def __call__(self, *args):
        fixed_args = []
        i = 0
        for argtype in self.argtypes:
            # Typecheck what we can
            fixed_args.append(argtype.from_param(args[i]))
            i += 1
        return self.func(*fixed_args + list(args[i:]))


def ord_if_char(value):
    """
    Simple helper used for casts to simple builtin types:  if the argument is a
    string type, it will be converted to it's ordinal value.

    This function will raise an exception if the argument is string with more
    than one characters.
    """
    return ord(value) if (isinstance(value, bytes) or isinstance(value, str)) else value

# End preamble

_libs = {}
_libdirs = []

# Begin loader

# ----------------------------------------------------------------------------
# Copyright (c) 2008 David James
# Copyright (c) 2006-2008 Alex Holkner
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in
#    the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of pyglet nor the names of its
#    contributors may be used to endorse or promote products
#    derived from this software without specific prior written
#    permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
# ----------------------------------------------------------------------------

import os.path, re, sys, glob
import platform
import ctypes
import ctypes.util


def _environ_path(name):
    if name in os.environ:
        return os.environ[name].split(":")
    else:
        return []


class LibraryLoader(object):
    # library names formatted specifically for platforms
    name_formats = ["%s"]

    class Lookup(object):
        mode = ctypes.DEFAULT_MODE

        def __init__(self, path):
            super(LibraryLoader.Lookup, self).__init__()
            self.access = dict(cdecl=ctypes.CDLL(path, self.mode))

        def get(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                raise LookupError(
                    "Unknown calling convention '{}' for function '{}'".format(
                        calling_convention, name
                    )
                )
            return getattr(self.access[calling_convention], name)

        def has(self, name, calling_convention="cdecl"):
            if calling_convention not in self.access:
                return False
            return hasattr(self.access[calling_convention], name)

        def __getattr__(self, name):
            return getattr(self.access["cdecl"], name)

    def __init__(self):
        self.other_dirs = []

    def __call__(self, libname):
        """Given the name of a library, load it."""
        paths = self.getpaths(libname)

        for path in paths:
            try:
                return self.Lookup(path)
            except:
                pass

        raise ImportError("Could not load %s." % libname)

    def getpaths(self, libname):
        """Return a list of paths where the library might be found."""
        if os.path.isabs(libname):
            yield libname
        else:
            # search through a prioritized series of locations for the library

            # we first search any specific directories identified by user
            for dir_i in self.other_dirs:
                for fmt in self.name_formats:
                    # dir_i should be absolute already
                    yield os.path.join(dir_i, fmt % libname)

            # then we search the directory where the generated python interface is stored
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.dirname(__file__), fmt % libname))

            # now, use the ctypes tools to try to find the library
            for fmt in self.name_formats:
                path = ctypes.util.find_library(fmt % libname)
                if path:
                    yield path

            # then we search all paths identified as platform-specific lib paths
            for path in self.getplatformpaths(libname):
                yield path

            # Finally, we'll try the users current working directory
            for fmt in self.name_formats:
                yield os.path.abspath(os.path.join(os.path.curdir, fmt % libname))

    def getplatformpaths(self, libname):
        return []


# Darwin (Mac OS X)


class DarwinLibraryLoader(LibraryLoader):
    name_formats = [
        "lib%s.dylib",
        "lib%s.so",
        "lib%s.bundle",
        "%s.dylib",
        "%s.so",
        "%s.bundle",
        "%s",
    ]

    class Lookup(LibraryLoader.Lookup):
        # Darwin requires dlopen to be called with mode RTLD_GLOBAL instead
        # of the default RTLD_LOCAL.  Without this, you end up with
        # libraries not being loadable, resulting in "Symbol not found"
        # errors
        mode = ctypes.RTLD_GLOBAL

    def getplatformpaths(self, libname):
        if os.path.pathsep in libname:
            names = [libname]
        else:
            names = [format % libname for format in self.name_formats]

        for dir in self.getdirs(libname):
            for name in names:
                yield os.path.join(dir, name)

    def getdirs(self, libname):
        """Implements the dylib search as specified in Apple documentation:

        http://developer.apple.com/documentation/DeveloperTools/Conceptual/
            DynamicLibraries/Articles/DynamicLibraryUsageGuidelines.html

        Before commencing the standard search, the method first checks
        the bundle's ``Frameworks`` directory if the application is running
        within a bundle (OS X .app).
        """

        dyld_fallback_library_path = _environ_path("DYLD_FALLBACK_LIBRARY_PATH")
        if not dyld_fallback_library_path:
            dyld_fallback_library_path = [os.path.expanduser("~/lib"), "/usr/local/lib", "/usr/lib"]

        dirs = []

        if "/" in libname:
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))
        else:
            dirs.extend(_environ_path("LD_LIBRARY_PATH"))
            dirs.extend(_environ_path("DYLD_LIBRARY_PATH"))

        if hasattr(sys, "frozen") and sys.frozen == "macosx_app":
            dirs.append(os.path.join(os.environ["RESOURCEPATH"], "..", "Frameworks"))

        dirs.extend(dyld_fallback_library_path)

        return dirs


# Posix


class PosixLibraryLoader(LibraryLoader):
    _ld_so_cache = None

    _include = re.compile(r"^\s*include\s+(?P<pattern>.*)")

    class _Directories(dict):
        def __init__(self):
            self.order = 0

        def add(self, directory):
            if len(directory) > 1:
                directory = directory.rstrip(os.path.sep)
            # only adds and updates order if exists and not already in set
            if not os.path.exists(directory):
                return
            o = self.setdefault(directory, self.order)
            if o == self.order:
                self.order += 1

        def extend(self, directories):
            for d in directories:
                self.add(d)

        def ordered(self):
            return (i[0] for i in sorted(self.items(), key=lambda D: D[1]))

    def _get_ld_so_conf_dirs(self, conf, dirs):
        """
        Recursive funtion to help parse all ld.so.conf files, including proper
        handling of the `include` directive.
        """

        try:
            with open(conf) as f:
                for D in f:
                    D = D.strip()
                    if not D:
                        continue

                    m = self._include.match(D)
                    if not m:
                        dirs.add(D)
                    else:
                        for D2 in glob.glob(m.group("pattern")):
                            self._get_ld_so_conf_dirs(D2, dirs)
        except IOError:
            pass

    def _create_ld_so_cache(self):
        # Recreate search path followed by ld.so.  This is going to be
        # slow to build, and incorrect (ld.so uses ld.so.cache, which may
        # not be up-to-date).  Used only as fallback for distros without
        # /sbin/ldconfig.
        #
        # We assume the DT_RPATH and DT_RUNPATH binary sections are omitted.

        directories = self._Directories()
        for name in (
            "LD_LIBRARY_PATH",
            "SHLIB_PATH",  # HPUX
            "LIBPATH",  # OS/2, AIX
            "LIBRARY_PATH",  # BE/OS
        ):
            if name in os.environ:
                directories.extend(os.environ[name].split(os.pathsep))

        self._get_ld_so_conf_dirs("/etc/ld.so.conf", directories)

        bitage = platform.architecture()[0]

        unix_lib_dirs_list = []
        if bitage.startswith("64"):
            # prefer 64 bit if that is our arch
            unix_lib_dirs_list += ["/lib64", "/usr/lib64"]

        # must include standard libs, since those paths are also used by 64 bit
        # installs
        unix_lib_dirs_list += ["/lib", "/usr/lib"]
        if sys.platform.startswith("linux"):
            # Try and support multiarch work in Ubuntu
            # https://wiki.ubuntu.com/MultiarchSpec
            if bitage.startswith("32"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/i386-linux-gnu", "/usr/lib/i386-linux-gnu"]
            elif bitage.startswith("64"):
                # Assume Intel/AMD x86 compat
                unix_lib_dirs_list += ["/lib/x86_64-linux-gnu", "/usr/lib/x86_64-linux-gnu"]
            else:
                # guess...
                unix_lib_dirs_list += glob.glob("/lib/*linux-gnu")
        directories.extend(unix_lib_dirs_list)

        cache = {}
        lib_re = re.compile(r"lib(.*)\.s[ol]")
        ext_re = re.compile(r"\.s[ol]$")
        for dir in directories.ordered():
            try:
                for path in glob.glob("%s/*.s[ol]*" % dir):
                    file = os.path.basename(path)

                    # Index by filename
                    cache_i = cache.setdefault(file, set())
                    cache_i.add(path)

                    # Index by library name
                    match = lib_re.match(file)
                    if match:
                        library = match.group(1)
                        cache_i = cache.setdefault(library, set())
                        cache_i.add(path)
            except OSError:
                pass

        self._ld_so_cache = cache

    def getplatformpaths(self, libname):
        if self._ld_so_cache is None:
            self._create_ld_so_cache()

        result = self._ld_so_cache.get(libname, set())
        for i in result:
            # we iterate through all found paths for library, since we may have
            # actually found multiple architectures or other library types that
            # may not load
            yield i


# Windows


class WindowsLibraryLoader(LibraryLoader):
    name_formats = ["%s.dll", "lib%s.dll", "%slib.dll", "%s"]

    class Lookup(LibraryLoader.Lookup):
        def __init__(self, path):
            super(WindowsLibraryLoader.Lookup, self).__init__(path)
            self.access["stdcall"] = ctypes.windll.LoadLibrary(path)


# Platform switching

# If your value of sys.platform does not appear in this dict, please contact
# the Ctypesgen maintainers.

loaderclass = {
    "darwin": DarwinLibraryLoader,
    "cygwin": WindowsLibraryLoader,
    "win32": WindowsLibraryLoader,
    "msys": WindowsLibraryLoader,
}

load_library = loaderclass.get(sys.platform, PosixLibraryLoader)()


def add_library_search_dirs(other_dirs):
    """
    Add libraries to search paths.
    If library paths are relative, convert them to absolute with respect to this
    file's directory
    """
    for F in other_dirs:
        if not os.path.isabs(F):
            F = os.path.abspath(F)
        load_library.other_dirs.append(F)


del loaderclass

# End loader

add_library_search_dirs([])

# Begin libraries
_libs["libcudd-3.0.0.so"] = load_library("libcudd-3.0.0.so")

# 1 libraries
# End libraries

# No modules

uintptr_t = c_ulong# /usr/include/stdint.h: 90

enum_anon_3 = c_int# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_SAME = 0# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_NONE = (CUDD_REORDER_SAME + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_RANDOM = (CUDD_REORDER_NONE + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_RANDOM_PIVOT = (CUDD_REORDER_RANDOM + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_SIFT = (CUDD_REORDER_RANDOM_PIVOT + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_SIFT_CONVERGE = (CUDD_REORDER_SIFT + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_SYMM_SIFT = (CUDD_REORDER_SIFT_CONVERGE + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_SYMM_SIFT_CONV = (CUDD_REORDER_SYMM_SIFT + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_WINDOW2 = (CUDD_REORDER_SYMM_SIFT_CONV + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_WINDOW3 = (CUDD_REORDER_WINDOW2 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_WINDOW4 = (CUDD_REORDER_WINDOW3 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_WINDOW2_CONV = (CUDD_REORDER_WINDOW4 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_WINDOW3_CONV = (CUDD_REORDER_WINDOW2_CONV + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_WINDOW4_CONV = (CUDD_REORDER_WINDOW3_CONV + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_GROUP_SIFT = (CUDD_REORDER_WINDOW4_CONV + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_GROUP_SIFT_CONV = (CUDD_REORDER_GROUP_SIFT + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_ANNEALING = (CUDD_REORDER_GROUP_SIFT_CONV + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_GENETIC = (CUDD_REORDER_ANNEALING + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_LINEAR = (CUDD_REORDER_GENETIC + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_LINEAR_CONVERGE = (CUDD_REORDER_LINEAR + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_LAZY_SIFT = (CUDD_REORDER_LINEAR_CONVERGE + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

CUDD_REORDER_EXACT = (CUDD_REORDER_LAZY_SIFT + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

Cudd_ReorderingType = enum_anon_3# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 117

enum_anon_4 = c_int# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_NO_CHECK = 0# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK = (CUDD_NO_CHECK + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK2 = (CUDD_GROUP_CHECK + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK3 = (CUDD_GROUP_CHECK2 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK4 = (CUDD_GROUP_CHECK3 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK5 = (CUDD_GROUP_CHECK4 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK6 = (CUDD_GROUP_CHECK5 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK7 = (CUDD_GROUP_CHECK6 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK8 = (CUDD_GROUP_CHECK7 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

CUDD_GROUP_CHECK9 = (CUDD_GROUP_CHECK8 + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

Cudd_AggregationType = enum_anon_4# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 134

enum_anon_5 = c_int# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 145

CUDD_PRE_GC_HOOK = 0# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 145

CUDD_POST_GC_HOOK = (CUDD_PRE_GC_HOOK + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 145

CUDD_PRE_REORDERING_HOOK = (CUDD_POST_GC_HOOK + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 145

CUDD_POST_REORDERING_HOOK = (CUDD_PRE_REORDERING_HOOK + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 145

Cudd_HookType = enum_anon_5# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 145

enum_anon_6 = c_int# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_NO_ERROR = 0# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_MEMORY_OUT = (CUDD_NO_ERROR + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_TOO_MANY_NODES = (CUDD_MEMORY_OUT + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_MAX_MEM_EXCEEDED = (CUDD_TOO_MANY_NODES + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_TIMEOUT_EXPIRED = (CUDD_MAX_MEM_EXCEEDED + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_TERMINATION = (CUDD_TIMEOUT_EXPIRED + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_INVALID_ARG = (CUDD_TERMINATION + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

CUDD_INTERNAL_ERROR = (CUDD_INVALID_ARG + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

Cudd_ErrorType = enum_anon_6# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 160

enum_anon_7 = c_int# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 171

CUDD_LAZY_NONE = 0# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 171

CUDD_LAZY_SOFT_GROUP = (CUDD_LAZY_NONE + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 171

CUDD_LAZY_HARD_GROUP = (CUDD_LAZY_SOFT_GROUP + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 171

CUDD_LAZY_UNGROUP = (CUDD_LAZY_HARD_GROUP + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 171

Cudd_LazyGroupType = enum_anon_7# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 171

enum_anon_8 = c_int# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 184

CUDD_VAR_PRIMARY_INPUT = 0# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 184

CUDD_VAR_PRESENT_STATE = (CUDD_VAR_PRIMARY_INPUT + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 184

CUDD_VAR_NEXT_STATE = (CUDD_VAR_PRESENT_STATE + 1)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 184

Cudd_VariableType = enum_anon_8# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 184

CUDD_VALUE_TYPE = c_double# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 189

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 194
class struct_DdNode(Structure):
    pass

DdNode = struct_DdNode# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 194

DdNodePtr = POINTER(DdNode)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 199

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 204
class struct_DdManager(Structure):
    pass

DdManager = struct_DdManager# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 204

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 209
class struct_DdGen(Structure):
    pass

DdGen = struct_DdGen# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 209

DdApaDigit = c_uint32# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 214

DdApaNumber = POINTER(DdApaDigit)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 219

DdConstApaNumber = POINTER(DdApaDigit)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 224

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 229
class struct_DdTlcInfo(Structure):
    pass

DdTlcInfo = struct_DdTlcInfo# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 229

DD_HFP = CFUNCTYPE(UNCHECKED(c_int), POINTER(DdManager), String, POINTER(None))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 234

DD_PRFP = CFUNCTYPE(UNCHECKED(POINTER(DdNode)), POINTER(DdManager), c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 238

DD_AOP = CFUNCTYPE(UNCHECKED(POINTER(DdNode)), POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 242

DD_MAOP = CFUNCTYPE(UNCHECKED(POINTER(DdNode)), POINTER(DdManager), POINTER(DdNode))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 246

DD_CTFP = CFUNCTYPE(UNCHECKED(POINTER(DdNode)), POINTER(DdManager), POINTER(DdNode), POINTER(DdNode))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 250

DD_CTFP1 = CFUNCTYPE(UNCHECKED(POINTER(DdNode)), POINTER(DdManager), POINTER(DdNode))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 254

DD_OOMFP = CFUNCTYPE(UNCHECKED(None), c_size_t)# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 258

DD_QSFP = CFUNCTYPE(UNCHECKED(c_int), POINTER(None), POINTER(None))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 262

DD_THFP = CFUNCTYPE(UNCHECKED(c_int), POINTER(None))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 266

DD_TOHFP = CFUNCTYPE(UNCHECKED(None), POINTER(DdManager), POINTER(None))# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 270

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 506
if _libs["libcudd-3.0.0.so"].has("Cudd_addNewVar", "cdecl"):
    Cudd_addNewVar = _libs["libcudd-3.0.0.so"].get("Cudd_addNewVar", "cdecl")
    Cudd_addNewVar.argtypes = [POINTER(DdManager)]
    Cudd_addNewVar.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 507
if _libs["libcudd-3.0.0.so"].has("Cudd_addNewVarAtLevel", "cdecl"):
    Cudd_addNewVarAtLevel = _libs["libcudd-3.0.0.so"].get("Cudd_addNewVarAtLevel", "cdecl")
    Cudd_addNewVarAtLevel.argtypes = [POINTER(DdManager), c_int]
    Cudd_addNewVarAtLevel.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 508
if _libs["libcudd-3.0.0.so"].has("Cudd_bddNewVar", "cdecl"):
    Cudd_bddNewVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddNewVar", "cdecl")
    Cudd_bddNewVar.argtypes = [POINTER(DdManager)]
    Cudd_bddNewVar.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 509
if _libs["libcudd-3.0.0.so"].has("Cudd_bddNewVarAtLevel", "cdecl"):
    Cudd_bddNewVarAtLevel = _libs["libcudd-3.0.0.so"].get("Cudd_bddNewVarAtLevel", "cdecl")
    Cudd_bddNewVarAtLevel.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddNewVarAtLevel.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 510
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsVar", "cdecl"):
    Cudd_bddIsVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsVar", "cdecl")
    Cudd_bddIsVar.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_bddIsVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 511
if _libs["libcudd-3.0.0.so"].has("Cudd_addIthVar", "cdecl"):
    Cudd_addIthVar = _libs["libcudd-3.0.0.so"].get("Cudd_addIthVar", "cdecl")
    Cudd_addIthVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_addIthVar.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 512
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIthVar", "cdecl"):
    Cudd_bddIthVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddIthVar", "cdecl")
    Cudd_bddIthVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddIthVar.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 513
if _libs["libcudd-3.0.0.so"].has("Cudd_zddIthVar", "cdecl"):
    Cudd_zddIthVar = _libs["libcudd-3.0.0.so"].get("Cudd_zddIthVar", "cdecl")
    Cudd_zddIthVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_zddIthVar.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 514
if _libs["libcudd-3.0.0.so"].has("Cudd_zddVarsFromBddVars", "cdecl"):
    Cudd_zddVarsFromBddVars = _libs["libcudd-3.0.0.so"].get("Cudd_zddVarsFromBddVars", "cdecl")
    Cudd_zddVarsFromBddVars.argtypes = [POINTER(DdManager), c_int]
    Cudd_zddVarsFromBddVars.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 515
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxIndex", "cdecl"):
    Cudd_ReadMaxIndex = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxIndex", "cdecl")
    Cudd_ReadMaxIndex.argtypes = []
    Cudd_ReadMaxIndex.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 516
if _libs["libcudd-3.0.0.so"].has("Cudd_addConst", "cdecl"):
    Cudd_addConst = _libs["libcudd-3.0.0.so"].get("Cudd_addConst", "cdecl")
    Cudd_addConst.argtypes = [POINTER(DdManager), CUDD_VALUE_TYPE]
    Cudd_addConst.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 517
if _libs["libcudd-3.0.0.so"].has("Cudd_IsConstant", "cdecl"):
    Cudd_IsConstant = _libs["libcudd-3.0.0.so"].get("Cudd_IsConstant", "cdecl")
    Cudd_IsConstant.argtypes = [POINTER(DdNode)]
    Cudd_IsConstant.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 518
if _libs["libcudd-3.0.0.so"].has("Cudd_IsNonConstant", "cdecl"):
    Cudd_IsNonConstant = _libs["libcudd-3.0.0.so"].get("Cudd_IsNonConstant", "cdecl")
    Cudd_IsNonConstant.argtypes = [POINTER(DdNode)]
    Cudd_IsNonConstant.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 519
if _libs["libcudd-3.0.0.so"].has("Cudd_T", "cdecl"):
    Cudd_T = _libs["libcudd-3.0.0.so"].get("Cudd_T", "cdecl")
    Cudd_T.argtypes = [POINTER(DdNode)]
    Cudd_T.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 520
if _libs["libcudd-3.0.0.so"].has("Cudd_E", "cdecl"):
    Cudd_E = _libs["libcudd-3.0.0.so"].get("Cudd_E", "cdecl")
    Cudd_E.argtypes = [POINTER(DdNode)]
    Cudd_E.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 521
if _libs["libcudd-3.0.0.so"].has("Cudd_V", "cdecl"):
    Cudd_V = _libs["libcudd-3.0.0.so"].get("Cudd_V", "cdecl")
    Cudd_V.argtypes = [POINTER(DdNode)]
    Cudd_V.restype = CUDD_VALUE_TYPE

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 522
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadStartTime", "cdecl"):
    Cudd_ReadStartTime = _libs["libcudd-3.0.0.so"].get("Cudd_ReadStartTime", "cdecl")
    Cudd_ReadStartTime.argtypes = [POINTER(DdManager)]
    Cudd_ReadStartTime.restype = c_ulong

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 523
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadElapsedTime", "cdecl"):
    Cudd_ReadElapsedTime = _libs["libcudd-3.0.0.so"].get("Cudd_ReadElapsedTime", "cdecl")
    Cudd_ReadElapsedTime.argtypes = [POINTER(DdManager)]
    Cudd_ReadElapsedTime.restype = c_ulong

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 524
if _libs["libcudd-3.0.0.so"].has("Cudd_SetStartTime", "cdecl"):
    Cudd_SetStartTime = _libs["libcudd-3.0.0.so"].get("Cudd_SetStartTime", "cdecl")
    Cudd_SetStartTime.argtypes = [POINTER(DdManager), c_ulong]
    Cudd_SetStartTime.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 525
if _libs["libcudd-3.0.0.so"].has("Cudd_ResetStartTime", "cdecl"):
    Cudd_ResetStartTime = _libs["libcudd-3.0.0.so"].get("Cudd_ResetStartTime", "cdecl")
    Cudd_ResetStartTime.argtypes = [POINTER(DdManager)]
    Cudd_ResetStartTime.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 526
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadTimeLimit", "cdecl"):
    Cudd_ReadTimeLimit = _libs["libcudd-3.0.0.so"].get("Cudd_ReadTimeLimit", "cdecl")
    Cudd_ReadTimeLimit.argtypes = [POINTER(DdManager)]
    Cudd_ReadTimeLimit.restype = c_ulong

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 527
if _libs["libcudd-3.0.0.so"].has("Cudd_SetTimeLimit", "cdecl"):
    Cudd_SetTimeLimit = _libs["libcudd-3.0.0.so"].get("Cudd_SetTimeLimit", "cdecl")
    Cudd_SetTimeLimit.argtypes = [POINTER(DdManager), c_ulong]
    Cudd_SetTimeLimit.restype = c_ulong

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 528
if _libs["libcudd-3.0.0.so"].has("Cudd_UpdateTimeLimit", "cdecl"):
    Cudd_UpdateTimeLimit = _libs["libcudd-3.0.0.so"].get("Cudd_UpdateTimeLimit", "cdecl")
    Cudd_UpdateTimeLimit.argtypes = [POINTER(DdManager)]
    Cudd_UpdateTimeLimit.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 529
if _libs["libcudd-3.0.0.so"].has("Cudd_IncreaseTimeLimit", "cdecl"):
    Cudd_IncreaseTimeLimit = _libs["libcudd-3.0.0.so"].get("Cudd_IncreaseTimeLimit", "cdecl")
    Cudd_IncreaseTimeLimit.argtypes = [POINTER(DdManager), c_ulong]
    Cudd_IncreaseTimeLimit.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 530
if _libs["libcudd-3.0.0.so"].has("Cudd_UnsetTimeLimit", "cdecl"):
    Cudd_UnsetTimeLimit = _libs["libcudd-3.0.0.so"].get("Cudd_UnsetTimeLimit", "cdecl")
    Cudd_UnsetTimeLimit.argtypes = [POINTER(DdManager)]
    Cudd_UnsetTimeLimit.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 531
if _libs["libcudd-3.0.0.so"].has("Cudd_TimeLimited", "cdecl"):
    Cudd_TimeLimited = _libs["libcudd-3.0.0.so"].get("Cudd_TimeLimited", "cdecl")
    Cudd_TimeLimited.argtypes = [POINTER(DdManager)]
    Cudd_TimeLimited.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 532
if _libs["libcudd-3.0.0.so"].has("Cudd_RegisterTerminationCallback", "cdecl"):
    Cudd_RegisterTerminationCallback = _libs["libcudd-3.0.0.so"].get("Cudd_RegisterTerminationCallback", "cdecl")
    Cudd_RegisterTerminationCallback.argtypes = [POINTER(DdManager), DD_THFP, POINTER(None)]
    Cudd_RegisterTerminationCallback.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 533
if _libs["libcudd-3.0.0.so"].has("Cudd_UnregisterTerminationCallback", "cdecl"):
    Cudd_UnregisterTerminationCallback = _libs["libcudd-3.0.0.so"].get("Cudd_UnregisterTerminationCallback", "cdecl")
    Cudd_UnregisterTerminationCallback.argtypes = [POINTER(DdManager)]
    Cudd_UnregisterTerminationCallback.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 534
if _libs["libcudd-3.0.0.so"].has("Cudd_RegisterOutOfMemoryCallback", "cdecl"):
    Cudd_RegisterOutOfMemoryCallback = _libs["libcudd-3.0.0.so"].get("Cudd_RegisterOutOfMemoryCallback", "cdecl")
    Cudd_RegisterOutOfMemoryCallback.argtypes = [POINTER(DdManager), DD_OOMFP]
    Cudd_RegisterOutOfMemoryCallback.restype = DD_OOMFP

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 535
if _libs["libcudd-3.0.0.so"].has("Cudd_UnregisterOutOfMemoryCallback", "cdecl"):
    Cudd_UnregisterOutOfMemoryCallback = _libs["libcudd-3.0.0.so"].get("Cudd_UnregisterOutOfMemoryCallback", "cdecl")
    Cudd_UnregisterOutOfMemoryCallback.argtypes = [POINTER(DdManager)]
    Cudd_UnregisterOutOfMemoryCallback.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 536
if _libs["libcudd-3.0.0.so"].has("Cudd_RegisterTimeoutHandler", "cdecl"):
    Cudd_RegisterTimeoutHandler = _libs["libcudd-3.0.0.so"].get("Cudd_RegisterTimeoutHandler", "cdecl")
    Cudd_RegisterTimeoutHandler.argtypes = [POINTER(DdManager), DD_TOHFP, POINTER(None)]
    Cudd_RegisterTimeoutHandler.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 537
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadTimeoutHandler", "cdecl"):
    Cudd_ReadTimeoutHandler = _libs["libcudd-3.0.0.so"].get("Cudd_ReadTimeoutHandler", "cdecl")
    Cudd_ReadTimeoutHandler.argtypes = [POINTER(DdManager), POINTER(POINTER(None))]
    Cudd_ReadTimeoutHandler.restype = DD_TOHFP

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 538
if _libs["libcudd-3.0.0.so"].has("Cudd_AutodynEnable", "cdecl"):
    Cudd_AutodynEnable = _libs["libcudd-3.0.0.so"].get("Cudd_AutodynEnable", "cdecl")
    Cudd_AutodynEnable.argtypes = [POINTER(DdManager), Cudd_ReorderingType]
    Cudd_AutodynEnable.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 539
if _libs["libcudd-3.0.0.so"].has("Cudd_AutodynDisable", "cdecl"):
    Cudd_AutodynDisable = _libs["libcudd-3.0.0.so"].get("Cudd_AutodynDisable", "cdecl")
    Cudd_AutodynDisable.argtypes = [POINTER(DdManager)]
    Cudd_AutodynDisable.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 540
if _libs["libcudd-3.0.0.so"].has("Cudd_ReorderingStatus", "cdecl"):
    Cudd_ReorderingStatus = _libs["libcudd-3.0.0.so"].get("Cudd_ReorderingStatus", "cdecl")
    Cudd_ReorderingStatus.argtypes = [POINTER(DdManager), POINTER(Cudd_ReorderingType)]
    Cudd_ReorderingStatus.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 541
if _libs["libcudd-3.0.0.so"].has("Cudd_AutodynEnableZdd", "cdecl"):
    Cudd_AutodynEnableZdd = _libs["libcudd-3.0.0.so"].get("Cudd_AutodynEnableZdd", "cdecl")
    Cudd_AutodynEnableZdd.argtypes = [POINTER(DdManager), Cudd_ReorderingType]
    Cudd_AutodynEnableZdd.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 542
if _libs["libcudd-3.0.0.so"].has("Cudd_AutodynDisableZdd", "cdecl"):
    Cudd_AutodynDisableZdd = _libs["libcudd-3.0.0.so"].get("Cudd_AutodynDisableZdd", "cdecl")
    Cudd_AutodynDisableZdd.argtypes = [POINTER(DdManager)]
    Cudd_AutodynDisableZdd.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 543
if _libs["libcudd-3.0.0.so"].has("Cudd_ReorderingStatusZdd", "cdecl"):
    Cudd_ReorderingStatusZdd = _libs["libcudd-3.0.0.so"].get("Cudd_ReorderingStatusZdd", "cdecl")
    Cudd_ReorderingStatusZdd.argtypes = [POINTER(DdManager), POINTER(Cudd_ReorderingType)]
    Cudd_ReorderingStatusZdd.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 544
if _libs["libcudd-3.0.0.so"].has("Cudd_zddRealignmentEnabled", "cdecl"):
    Cudd_zddRealignmentEnabled = _libs["libcudd-3.0.0.so"].get("Cudd_zddRealignmentEnabled", "cdecl")
    Cudd_zddRealignmentEnabled.argtypes = [POINTER(DdManager)]
    Cudd_zddRealignmentEnabled.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 545
if _libs["libcudd-3.0.0.so"].has("Cudd_zddRealignEnable", "cdecl"):
    Cudd_zddRealignEnable = _libs["libcudd-3.0.0.so"].get("Cudd_zddRealignEnable", "cdecl")
    Cudd_zddRealignEnable.argtypes = [POINTER(DdManager)]
    Cudd_zddRealignEnable.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 546
if _libs["libcudd-3.0.0.so"].has("Cudd_zddRealignDisable", "cdecl"):
    Cudd_zddRealignDisable = _libs["libcudd-3.0.0.so"].get("Cudd_zddRealignDisable", "cdecl")
    Cudd_zddRealignDisable.argtypes = [POINTER(DdManager)]
    Cudd_zddRealignDisable.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 547
if _libs["libcudd-3.0.0.so"].has("Cudd_bddRealignmentEnabled", "cdecl"):
    Cudd_bddRealignmentEnabled = _libs["libcudd-3.0.0.so"].get("Cudd_bddRealignmentEnabled", "cdecl")
    Cudd_bddRealignmentEnabled.argtypes = [POINTER(DdManager)]
    Cudd_bddRealignmentEnabled.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 548
if _libs["libcudd-3.0.0.so"].has("Cudd_bddRealignEnable", "cdecl"):
    Cudd_bddRealignEnable = _libs["libcudd-3.0.0.so"].get("Cudd_bddRealignEnable", "cdecl")
    Cudd_bddRealignEnable.argtypes = [POINTER(DdManager)]
    Cudd_bddRealignEnable.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 549
if _libs["libcudd-3.0.0.so"].has("Cudd_bddRealignDisable", "cdecl"):
    Cudd_bddRealignDisable = _libs["libcudd-3.0.0.so"].get("Cudd_bddRealignDisable", "cdecl")
    Cudd_bddRealignDisable.argtypes = [POINTER(DdManager)]
    Cudd_bddRealignDisable.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 550
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadOne", "cdecl"):
    Cudd_ReadOne = _libs["libcudd-3.0.0.so"].get("Cudd_ReadOne", "cdecl")
    Cudd_ReadOne.argtypes = [POINTER(DdManager)]
    Cudd_ReadOne.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 551
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadZddOne", "cdecl"):
    Cudd_ReadZddOne = _libs["libcudd-3.0.0.so"].get("Cudd_ReadZddOne", "cdecl")
    Cudd_ReadZddOne.argtypes = [POINTER(DdManager), c_int]
    Cudd_ReadZddOne.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 552
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadZero", "cdecl"):
    Cudd_ReadZero = _libs["libcudd-3.0.0.so"].get("Cudd_ReadZero", "cdecl")
    Cudd_ReadZero.argtypes = [POINTER(DdManager)]
    Cudd_ReadZero.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 553
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadLogicZero", "cdecl"):
    Cudd_ReadLogicZero = _libs["libcudd-3.0.0.so"].get("Cudd_ReadLogicZero", "cdecl")
    Cudd_ReadLogicZero.argtypes = [POINTER(DdManager)]
    Cudd_ReadLogicZero.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 554
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadPlusInfinity", "cdecl"):
    Cudd_ReadPlusInfinity = _libs["libcudd-3.0.0.so"].get("Cudd_ReadPlusInfinity", "cdecl")
    Cudd_ReadPlusInfinity.argtypes = [POINTER(DdManager)]
    Cudd_ReadPlusInfinity.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 555
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMinusInfinity", "cdecl"):
    Cudd_ReadMinusInfinity = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMinusInfinity", "cdecl")
    Cudd_ReadMinusInfinity.argtypes = [POINTER(DdManager)]
    Cudd_ReadMinusInfinity.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 556
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadBackground", "cdecl"):
    Cudd_ReadBackground = _libs["libcudd-3.0.0.so"].get("Cudd_ReadBackground", "cdecl")
    Cudd_ReadBackground.argtypes = [POINTER(DdManager)]
    Cudd_ReadBackground.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 557
if _libs["libcudd-3.0.0.so"].has("Cudd_SetBackground", "cdecl"):
    Cudd_SetBackground = _libs["libcudd-3.0.0.so"].get("Cudd_SetBackground", "cdecl")
    Cudd_SetBackground.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_SetBackground.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 558
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadCacheSlots", "cdecl"):
    Cudd_ReadCacheSlots = _libs["libcudd-3.0.0.so"].get("Cudd_ReadCacheSlots", "cdecl")
    Cudd_ReadCacheSlots.argtypes = [POINTER(DdManager)]
    Cudd_ReadCacheSlots.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 559
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadCacheUsedSlots", "cdecl"):
    Cudd_ReadCacheUsedSlots = _libs["libcudd-3.0.0.so"].get("Cudd_ReadCacheUsedSlots", "cdecl")
    Cudd_ReadCacheUsedSlots.argtypes = [POINTER(DdManager)]
    Cudd_ReadCacheUsedSlots.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 560
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadCacheLookUps", "cdecl"):
    Cudd_ReadCacheLookUps = _libs["libcudd-3.0.0.so"].get("Cudd_ReadCacheLookUps", "cdecl")
    Cudd_ReadCacheLookUps.argtypes = [POINTER(DdManager)]
    Cudd_ReadCacheLookUps.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 561
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadCacheHits", "cdecl"):
    Cudd_ReadCacheHits = _libs["libcudd-3.0.0.so"].get("Cudd_ReadCacheHits", "cdecl")
    Cudd_ReadCacheHits.argtypes = [POINTER(DdManager)]
    Cudd_ReadCacheHits.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 562
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadRecursiveCalls", "cdecl"):
    Cudd_ReadRecursiveCalls = _libs["libcudd-3.0.0.so"].get("Cudd_ReadRecursiveCalls", "cdecl")
    Cudd_ReadRecursiveCalls.argtypes = [POINTER(DdManager)]
    Cudd_ReadRecursiveCalls.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 563
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMinHit", "cdecl"):
    Cudd_ReadMinHit = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMinHit", "cdecl")
    Cudd_ReadMinHit.argtypes = [POINTER(DdManager)]
    Cudd_ReadMinHit.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 564
if _libs["libcudd-3.0.0.so"].has("Cudd_SetMinHit", "cdecl"):
    Cudd_SetMinHit = _libs["libcudd-3.0.0.so"].get("Cudd_SetMinHit", "cdecl")
    Cudd_SetMinHit.argtypes = [POINTER(DdManager), c_uint]
    Cudd_SetMinHit.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 565
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadLooseUpTo", "cdecl"):
    Cudd_ReadLooseUpTo = _libs["libcudd-3.0.0.so"].get("Cudd_ReadLooseUpTo", "cdecl")
    Cudd_ReadLooseUpTo.argtypes = [POINTER(DdManager)]
    Cudd_ReadLooseUpTo.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 566
if _libs["libcudd-3.0.0.so"].has("Cudd_SetLooseUpTo", "cdecl"):
    Cudd_SetLooseUpTo = _libs["libcudd-3.0.0.so"].get("Cudd_SetLooseUpTo", "cdecl")
    Cudd_SetLooseUpTo.argtypes = [POINTER(DdManager), c_uint]
    Cudd_SetLooseUpTo.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 567
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxCache", "cdecl"):
    Cudd_ReadMaxCache = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxCache", "cdecl")
    Cudd_ReadMaxCache.argtypes = [POINTER(DdManager)]
    Cudd_ReadMaxCache.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 568
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxCacheHard", "cdecl"):
    Cudd_ReadMaxCacheHard = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxCacheHard", "cdecl")
    Cudd_ReadMaxCacheHard.argtypes = [POINTER(DdManager)]
    Cudd_ReadMaxCacheHard.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 569
if _libs["libcudd-3.0.0.so"].has("Cudd_SetMaxCacheHard", "cdecl"):
    Cudd_SetMaxCacheHard = _libs["libcudd-3.0.0.so"].get("Cudd_SetMaxCacheHard", "cdecl")
    Cudd_SetMaxCacheHard.argtypes = [POINTER(DdManager), c_uint]
    Cudd_SetMaxCacheHard.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 570
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadSize", "cdecl"):
    Cudd_ReadSize = _libs["libcudd-3.0.0.so"].get("Cudd_ReadSize", "cdecl")
    Cudd_ReadSize.argtypes = [POINTER(DdManager)]
    Cudd_ReadSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 571
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadZddSize", "cdecl"):
    Cudd_ReadZddSize = _libs["libcudd-3.0.0.so"].get("Cudd_ReadZddSize", "cdecl")
    Cudd_ReadZddSize.argtypes = [POINTER(DdManager)]
    Cudd_ReadZddSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 572
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadSlots", "cdecl"):
    Cudd_ReadSlots = _libs["libcudd-3.0.0.so"].get("Cudd_ReadSlots", "cdecl")
    Cudd_ReadSlots.argtypes = [POINTER(DdManager)]
    Cudd_ReadSlots.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 573
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadUsedSlots", "cdecl"):
    Cudd_ReadUsedSlots = _libs["libcudd-3.0.0.so"].get("Cudd_ReadUsedSlots", "cdecl")
    Cudd_ReadUsedSlots.argtypes = [POINTER(DdManager)]
    Cudd_ReadUsedSlots.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 574
if _libs["libcudd-3.0.0.so"].has("Cudd_ExpectedUsedSlots", "cdecl"):
    Cudd_ExpectedUsedSlots = _libs["libcudd-3.0.0.so"].get("Cudd_ExpectedUsedSlots", "cdecl")
    Cudd_ExpectedUsedSlots.argtypes = [POINTER(DdManager)]
    Cudd_ExpectedUsedSlots.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 575
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadKeys", "cdecl"):
    Cudd_ReadKeys = _libs["libcudd-3.0.0.so"].get("Cudd_ReadKeys", "cdecl")
    Cudd_ReadKeys.argtypes = [POINTER(DdManager)]
    Cudd_ReadKeys.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 576
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadDead", "cdecl"):
    Cudd_ReadDead = _libs["libcudd-3.0.0.so"].get("Cudd_ReadDead", "cdecl")
    Cudd_ReadDead.argtypes = [POINTER(DdManager)]
    Cudd_ReadDead.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 577
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMinDead", "cdecl"):
    Cudd_ReadMinDead = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMinDead", "cdecl")
    Cudd_ReadMinDead.argtypes = [POINTER(DdManager)]
    Cudd_ReadMinDead.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 578
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadReorderings", "cdecl"):
    Cudd_ReadReorderings = _libs["libcudd-3.0.0.so"].get("Cudd_ReadReorderings", "cdecl")
    Cudd_ReadReorderings.argtypes = [POINTER(DdManager)]
    Cudd_ReadReorderings.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 579
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxReorderings", "cdecl"):
    Cudd_ReadMaxReorderings = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxReorderings", "cdecl")
    Cudd_ReadMaxReorderings.argtypes = [POINTER(DdManager)]
    Cudd_ReadMaxReorderings.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 580
if _libs["libcudd-3.0.0.so"].has("Cudd_SetMaxReorderings", "cdecl"):
    Cudd_SetMaxReorderings = _libs["libcudd-3.0.0.so"].get("Cudd_SetMaxReorderings", "cdecl")
    Cudd_SetMaxReorderings.argtypes = [POINTER(DdManager), c_uint]
    Cudd_SetMaxReorderings.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 581
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadReorderingTime", "cdecl"):
    Cudd_ReadReorderingTime = _libs["libcudd-3.0.0.so"].get("Cudd_ReadReorderingTime", "cdecl")
    Cudd_ReadReorderingTime.argtypes = [POINTER(DdManager)]
    Cudd_ReadReorderingTime.restype = c_long

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 582
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadGarbageCollections", "cdecl"):
    Cudd_ReadGarbageCollections = _libs["libcudd-3.0.0.so"].get("Cudd_ReadGarbageCollections", "cdecl")
    Cudd_ReadGarbageCollections.argtypes = [POINTER(DdManager)]
    Cudd_ReadGarbageCollections.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 583
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadGarbageCollectionTime", "cdecl"):
    Cudd_ReadGarbageCollectionTime = _libs["libcudd-3.0.0.so"].get("Cudd_ReadGarbageCollectionTime", "cdecl")
    Cudd_ReadGarbageCollectionTime.argtypes = [POINTER(DdManager)]
    Cudd_ReadGarbageCollectionTime.restype = c_long

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 584
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadNodesFreed", "cdecl"):
    Cudd_ReadNodesFreed = _libs["libcudd-3.0.0.so"].get("Cudd_ReadNodesFreed", "cdecl")
    Cudd_ReadNodesFreed.argtypes = [POINTER(DdManager)]
    Cudd_ReadNodesFreed.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 585
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadNodesDropped", "cdecl"):
    Cudd_ReadNodesDropped = _libs["libcudd-3.0.0.so"].get("Cudd_ReadNodesDropped", "cdecl")
    Cudd_ReadNodesDropped.argtypes = [POINTER(DdManager)]
    Cudd_ReadNodesDropped.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 586
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadUniqueLookUps", "cdecl"):
    Cudd_ReadUniqueLookUps = _libs["libcudd-3.0.0.so"].get("Cudd_ReadUniqueLookUps", "cdecl")
    Cudd_ReadUniqueLookUps.argtypes = [POINTER(DdManager)]
    Cudd_ReadUniqueLookUps.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 587
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadUniqueLinks", "cdecl"):
    Cudd_ReadUniqueLinks = _libs["libcudd-3.0.0.so"].get("Cudd_ReadUniqueLinks", "cdecl")
    Cudd_ReadUniqueLinks.argtypes = [POINTER(DdManager)]
    Cudd_ReadUniqueLinks.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 588
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadSiftMaxVar", "cdecl"):
    Cudd_ReadSiftMaxVar = _libs["libcudd-3.0.0.so"].get("Cudd_ReadSiftMaxVar", "cdecl")
    Cudd_ReadSiftMaxVar.argtypes = [POINTER(DdManager)]
    Cudd_ReadSiftMaxVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 589
if _libs["libcudd-3.0.0.so"].has("Cudd_SetSiftMaxVar", "cdecl"):
    Cudd_SetSiftMaxVar = _libs["libcudd-3.0.0.so"].get("Cudd_SetSiftMaxVar", "cdecl")
    Cudd_SetSiftMaxVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetSiftMaxVar.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 590
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadSiftMaxSwap", "cdecl"):
    Cudd_ReadSiftMaxSwap = _libs["libcudd-3.0.0.so"].get("Cudd_ReadSiftMaxSwap", "cdecl")
    Cudd_ReadSiftMaxSwap.argtypes = [POINTER(DdManager)]
    Cudd_ReadSiftMaxSwap.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 591
if _libs["libcudd-3.0.0.so"].has("Cudd_SetSiftMaxSwap", "cdecl"):
    Cudd_SetSiftMaxSwap = _libs["libcudd-3.0.0.so"].get("Cudd_SetSiftMaxSwap", "cdecl")
    Cudd_SetSiftMaxSwap.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetSiftMaxSwap.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 592
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxGrowth", "cdecl"):
    Cudd_ReadMaxGrowth = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxGrowth", "cdecl")
    Cudd_ReadMaxGrowth.argtypes = [POINTER(DdManager)]
    Cudd_ReadMaxGrowth.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 593
if _libs["libcudd-3.0.0.so"].has("Cudd_SetMaxGrowth", "cdecl"):
    Cudd_SetMaxGrowth = _libs["libcudd-3.0.0.so"].get("Cudd_SetMaxGrowth", "cdecl")
    Cudd_SetMaxGrowth.argtypes = [POINTER(DdManager), c_double]
    Cudd_SetMaxGrowth.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 594
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxGrowthAlternate", "cdecl"):
    Cudd_ReadMaxGrowthAlternate = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxGrowthAlternate", "cdecl")
    Cudd_ReadMaxGrowthAlternate.argtypes = [POINTER(DdManager)]
    Cudd_ReadMaxGrowthAlternate.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 595
if _libs["libcudd-3.0.0.so"].has("Cudd_SetMaxGrowthAlternate", "cdecl"):
    Cudd_SetMaxGrowthAlternate = _libs["libcudd-3.0.0.so"].get("Cudd_SetMaxGrowthAlternate", "cdecl")
    Cudd_SetMaxGrowthAlternate.argtypes = [POINTER(DdManager), c_double]
    Cudd_SetMaxGrowthAlternate.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 596
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadReorderingCycle", "cdecl"):
    Cudd_ReadReorderingCycle = _libs["libcudd-3.0.0.so"].get("Cudd_ReadReorderingCycle", "cdecl")
    Cudd_ReadReorderingCycle.argtypes = [POINTER(DdManager)]
    Cudd_ReadReorderingCycle.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 597
if _libs["libcudd-3.0.0.so"].has("Cudd_SetReorderingCycle", "cdecl"):
    Cudd_SetReorderingCycle = _libs["libcudd-3.0.0.so"].get("Cudd_SetReorderingCycle", "cdecl")
    Cudd_SetReorderingCycle.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetReorderingCycle.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 598
if _libs["libcudd-3.0.0.so"].has("Cudd_NodeReadIndex", "cdecl"):
    Cudd_NodeReadIndex = _libs["libcudd-3.0.0.so"].get("Cudd_NodeReadIndex", "cdecl")
    Cudd_NodeReadIndex.argtypes = [POINTER(DdNode)]
    Cudd_NodeReadIndex.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 599
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadPerm", "cdecl"):
    Cudd_ReadPerm = _libs["libcudd-3.0.0.so"].get("Cudd_ReadPerm", "cdecl")
    Cudd_ReadPerm.argtypes = [POINTER(DdManager), c_int]
    Cudd_ReadPerm.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 600
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadPermZdd", "cdecl"):
    Cudd_ReadPermZdd = _libs["libcudd-3.0.0.so"].get("Cudd_ReadPermZdd", "cdecl")
    Cudd_ReadPermZdd.argtypes = [POINTER(DdManager), c_int]
    Cudd_ReadPermZdd.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 601
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadInvPerm", "cdecl"):
    Cudd_ReadInvPerm = _libs["libcudd-3.0.0.so"].get("Cudd_ReadInvPerm", "cdecl")
    Cudd_ReadInvPerm.argtypes = [POINTER(DdManager), c_int]
    Cudd_ReadInvPerm.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 602
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadInvPermZdd", "cdecl"):
    Cudd_ReadInvPermZdd = _libs["libcudd-3.0.0.so"].get("Cudd_ReadInvPermZdd", "cdecl")
    Cudd_ReadInvPermZdd.argtypes = [POINTER(DdManager), c_int]
    Cudd_ReadInvPermZdd.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 603
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadVars", "cdecl"):
    Cudd_ReadVars = _libs["libcudd-3.0.0.so"].get("Cudd_ReadVars", "cdecl")
    Cudd_ReadVars.argtypes = [POINTER(DdManager), c_int]
    Cudd_ReadVars.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 604
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadEpsilon", "cdecl"):
    Cudd_ReadEpsilon = _libs["libcudd-3.0.0.so"].get("Cudd_ReadEpsilon", "cdecl")
    Cudd_ReadEpsilon.argtypes = [POINTER(DdManager)]
    Cudd_ReadEpsilon.restype = CUDD_VALUE_TYPE

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 605
if _libs["libcudd-3.0.0.so"].has("Cudd_SetEpsilon", "cdecl"):
    Cudd_SetEpsilon = _libs["libcudd-3.0.0.so"].get("Cudd_SetEpsilon", "cdecl")
    Cudd_SetEpsilon.argtypes = [POINTER(DdManager), CUDD_VALUE_TYPE]
    Cudd_SetEpsilon.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 606
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadGroupcheck", "cdecl"):
    Cudd_ReadGroupcheck = _libs["libcudd-3.0.0.so"].get("Cudd_ReadGroupcheck", "cdecl")
    Cudd_ReadGroupcheck.argtypes = [POINTER(DdManager)]
    Cudd_ReadGroupcheck.restype = Cudd_AggregationType

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 607
if _libs["libcudd-3.0.0.so"].has("Cudd_SetGroupcheck", "cdecl"):
    Cudd_SetGroupcheck = _libs["libcudd-3.0.0.so"].get("Cudd_SetGroupcheck", "cdecl")
    Cudd_SetGroupcheck.argtypes = [POINTER(DdManager), Cudd_AggregationType]
    Cudd_SetGroupcheck.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 608
if _libs["libcudd-3.0.0.so"].has("Cudd_GarbageCollectionEnabled", "cdecl"):
    Cudd_GarbageCollectionEnabled = _libs["libcudd-3.0.0.so"].get("Cudd_GarbageCollectionEnabled", "cdecl")
    Cudd_GarbageCollectionEnabled.argtypes = [POINTER(DdManager)]
    Cudd_GarbageCollectionEnabled.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 609
if _libs["libcudd-3.0.0.so"].has("Cudd_EnableGarbageCollection", "cdecl"):
    Cudd_EnableGarbageCollection = _libs["libcudd-3.0.0.so"].get("Cudd_EnableGarbageCollection", "cdecl")
    Cudd_EnableGarbageCollection.argtypes = [POINTER(DdManager)]
    Cudd_EnableGarbageCollection.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 610
if _libs["libcudd-3.0.0.so"].has("Cudd_DisableGarbageCollection", "cdecl"):
    Cudd_DisableGarbageCollection = _libs["libcudd-3.0.0.so"].get("Cudd_DisableGarbageCollection", "cdecl")
    Cudd_DisableGarbageCollection.argtypes = [POINTER(DdManager)]
    Cudd_DisableGarbageCollection.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 611
if _libs["libcudd-3.0.0.so"].has("Cudd_DeadAreCounted", "cdecl"):
    Cudd_DeadAreCounted = _libs["libcudd-3.0.0.so"].get("Cudd_DeadAreCounted", "cdecl")
    Cudd_DeadAreCounted.argtypes = [POINTER(DdManager)]
    Cudd_DeadAreCounted.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 612
if _libs["libcudd-3.0.0.so"].has("Cudd_TurnOnCountDead", "cdecl"):
    Cudd_TurnOnCountDead = _libs["libcudd-3.0.0.so"].get("Cudd_TurnOnCountDead", "cdecl")
    Cudd_TurnOnCountDead.argtypes = [POINTER(DdManager)]
    Cudd_TurnOnCountDead.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 613
if _libs["libcudd-3.0.0.so"].has("Cudd_TurnOffCountDead", "cdecl"):
    Cudd_TurnOffCountDead = _libs["libcudd-3.0.0.so"].get("Cudd_TurnOffCountDead", "cdecl")
    Cudd_TurnOffCountDead.argtypes = [POINTER(DdManager)]
    Cudd_TurnOffCountDead.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 614
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadRecomb", "cdecl"):
    Cudd_ReadRecomb = _libs["libcudd-3.0.0.so"].get("Cudd_ReadRecomb", "cdecl")
    Cudd_ReadRecomb.argtypes = [POINTER(DdManager)]
    Cudd_ReadRecomb.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 615
if _libs["libcudd-3.0.0.so"].has("Cudd_SetRecomb", "cdecl"):
    Cudd_SetRecomb = _libs["libcudd-3.0.0.so"].get("Cudd_SetRecomb", "cdecl")
    Cudd_SetRecomb.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetRecomb.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 616
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadSymmviolation", "cdecl"):
    Cudd_ReadSymmviolation = _libs["libcudd-3.0.0.so"].get("Cudd_ReadSymmviolation", "cdecl")
    Cudd_ReadSymmviolation.argtypes = [POINTER(DdManager)]
    Cudd_ReadSymmviolation.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 617
if _libs["libcudd-3.0.0.so"].has("Cudd_SetSymmviolation", "cdecl"):
    Cudd_SetSymmviolation = _libs["libcudd-3.0.0.so"].get("Cudd_SetSymmviolation", "cdecl")
    Cudd_SetSymmviolation.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetSymmviolation.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 618
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadArcviolation", "cdecl"):
    Cudd_ReadArcviolation = _libs["libcudd-3.0.0.so"].get("Cudd_ReadArcviolation", "cdecl")
    Cudd_ReadArcviolation.argtypes = [POINTER(DdManager)]
    Cudd_ReadArcviolation.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 619
if _libs["libcudd-3.0.0.so"].has("Cudd_SetArcviolation", "cdecl"):
    Cudd_SetArcviolation = _libs["libcudd-3.0.0.so"].get("Cudd_SetArcviolation", "cdecl")
    Cudd_SetArcviolation.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetArcviolation.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 620
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadPopulationSize", "cdecl"):
    Cudd_ReadPopulationSize = _libs["libcudd-3.0.0.so"].get("Cudd_ReadPopulationSize", "cdecl")
    Cudd_ReadPopulationSize.argtypes = [POINTER(DdManager)]
    Cudd_ReadPopulationSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 621
if _libs["libcudd-3.0.0.so"].has("Cudd_SetPopulationSize", "cdecl"):
    Cudd_SetPopulationSize = _libs["libcudd-3.0.0.so"].get("Cudd_SetPopulationSize", "cdecl")
    Cudd_SetPopulationSize.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetPopulationSize.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 622
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadNumberXovers", "cdecl"):
    Cudd_ReadNumberXovers = _libs["libcudd-3.0.0.so"].get("Cudd_ReadNumberXovers", "cdecl")
    Cudd_ReadNumberXovers.argtypes = [POINTER(DdManager)]
    Cudd_ReadNumberXovers.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 623
if _libs["libcudd-3.0.0.so"].has("Cudd_SetNumberXovers", "cdecl"):
    Cudd_SetNumberXovers = _libs["libcudd-3.0.0.so"].get("Cudd_SetNumberXovers", "cdecl")
    Cudd_SetNumberXovers.argtypes = [POINTER(DdManager), c_int]
    Cudd_SetNumberXovers.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 624
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadOrderRandomization", "cdecl"):
    Cudd_ReadOrderRandomization = _libs["libcudd-3.0.0.so"].get("Cudd_ReadOrderRandomization", "cdecl")
    Cudd_ReadOrderRandomization.argtypes = [POINTER(DdManager)]
    Cudd_ReadOrderRandomization.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 625
if _libs["libcudd-3.0.0.so"].has("Cudd_SetOrderRandomization", "cdecl"):
    Cudd_SetOrderRandomization = _libs["libcudd-3.0.0.so"].get("Cudd_SetOrderRandomization", "cdecl")
    Cudd_SetOrderRandomization.argtypes = [POINTER(DdManager), c_uint]
    Cudd_SetOrderRandomization.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 626
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMemoryInUse", "cdecl"):
    Cudd_ReadMemoryInUse = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMemoryInUse", "cdecl")
    Cudd_ReadMemoryInUse.argtypes = [POINTER(DdManager)]
    Cudd_ReadMemoryInUse.restype = c_size_t

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 628
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadPeakNodeCount", "cdecl"):
    Cudd_ReadPeakNodeCount = _libs["libcudd-3.0.0.so"].get("Cudd_ReadPeakNodeCount", "cdecl")
    Cudd_ReadPeakNodeCount.argtypes = [POINTER(DdManager)]
    Cudd_ReadPeakNodeCount.restype = c_long

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 629
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadPeakLiveNodeCount", "cdecl"):
    Cudd_ReadPeakLiveNodeCount = _libs["libcudd-3.0.0.so"].get("Cudd_ReadPeakLiveNodeCount", "cdecl")
    Cudd_ReadPeakLiveNodeCount.argtypes = [POINTER(DdManager)]
    Cudd_ReadPeakLiveNodeCount.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 630
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadNodeCount", "cdecl"):
    Cudd_ReadNodeCount = _libs["libcudd-3.0.0.so"].get("Cudd_ReadNodeCount", "cdecl")
    Cudd_ReadNodeCount.argtypes = [POINTER(DdManager)]
    Cudd_ReadNodeCount.restype = c_long

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 631
if _libs["libcudd-3.0.0.so"].has("Cudd_zddReadNodeCount", "cdecl"):
    Cudd_zddReadNodeCount = _libs["libcudd-3.0.0.so"].get("Cudd_zddReadNodeCount", "cdecl")
    Cudd_zddReadNodeCount.argtypes = [POINTER(DdManager)]
    Cudd_zddReadNodeCount.restype = c_long

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 632
if _libs["libcudd-3.0.0.so"].has("Cudd_AddHook", "cdecl"):
    Cudd_AddHook = _libs["libcudd-3.0.0.so"].get("Cudd_AddHook", "cdecl")
    Cudd_AddHook.argtypes = [POINTER(DdManager), DD_HFP, Cudd_HookType]
    Cudd_AddHook.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 633
if _libs["libcudd-3.0.0.so"].has("Cudd_RemoveHook", "cdecl"):
    Cudd_RemoveHook = _libs["libcudd-3.0.0.so"].get("Cudd_RemoveHook", "cdecl")
    Cudd_RemoveHook.argtypes = [POINTER(DdManager), DD_HFP, Cudd_HookType]
    Cudd_RemoveHook.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 634
if _libs["libcudd-3.0.0.so"].has("Cudd_IsInHook", "cdecl"):
    Cudd_IsInHook = _libs["libcudd-3.0.0.so"].get("Cudd_IsInHook", "cdecl")
    Cudd_IsInHook.argtypes = [POINTER(DdManager), DD_HFP, Cudd_HookType]
    Cudd_IsInHook.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 635
if _libs["libcudd-3.0.0.so"].has("Cudd_StdPreReordHook", "cdecl"):
    Cudd_StdPreReordHook = _libs["libcudd-3.0.0.so"].get("Cudd_StdPreReordHook", "cdecl")
    Cudd_StdPreReordHook.argtypes = [POINTER(DdManager), String, POINTER(None)]
    Cudd_StdPreReordHook.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 636
if _libs["libcudd-3.0.0.so"].has("Cudd_StdPostReordHook", "cdecl"):
    Cudd_StdPostReordHook = _libs["libcudd-3.0.0.so"].get("Cudd_StdPostReordHook", "cdecl")
    Cudd_StdPostReordHook.argtypes = [POINTER(DdManager), String, POINTER(None)]
    Cudd_StdPostReordHook.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 637
if _libs["libcudd-3.0.0.so"].has("Cudd_EnableReorderingReporting", "cdecl"):
    Cudd_EnableReorderingReporting = _libs["libcudd-3.0.0.so"].get("Cudd_EnableReorderingReporting", "cdecl")
    Cudd_EnableReorderingReporting.argtypes = [POINTER(DdManager)]
    Cudd_EnableReorderingReporting.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 638
if _libs["libcudd-3.0.0.so"].has("Cudd_DisableReorderingReporting", "cdecl"):
    Cudd_DisableReorderingReporting = _libs["libcudd-3.0.0.so"].get("Cudd_DisableReorderingReporting", "cdecl")
    Cudd_DisableReorderingReporting.argtypes = [POINTER(DdManager)]
    Cudd_DisableReorderingReporting.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 639
if _libs["libcudd-3.0.0.so"].has("Cudd_ReorderingReporting", "cdecl"):
    Cudd_ReorderingReporting = _libs["libcudd-3.0.0.so"].get("Cudd_ReorderingReporting", "cdecl")
    Cudd_ReorderingReporting.argtypes = [POINTER(DdManager)]
    Cudd_ReorderingReporting.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 640
if _libs["libcudd-3.0.0.so"].has("Cudd_PrintGroupedOrder", "cdecl"):
    Cudd_PrintGroupedOrder = _libs["libcudd-3.0.0.so"].get("Cudd_PrintGroupedOrder", "cdecl")
    Cudd_PrintGroupedOrder.argtypes = [POINTER(DdManager), String, POINTER(None)]
    Cudd_PrintGroupedOrder.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 641
if _libs["libcudd-3.0.0.so"].has("Cudd_EnableOrderingMonitoring", "cdecl"):
    Cudd_EnableOrderingMonitoring = _libs["libcudd-3.0.0.so"].get("Cudd_EnableOrderingMonitoring", "cdecl")
    Cudd_EnableOrderingMonitoring.argtypes = [POINTER(DdManager)]
    Cudd_EnableOrderingMonitoring.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 642
if _libs["libcudd-3.0.0.so"].has("Cudd_DisableOrderingMonitoring", "cdecl"):
    Cudd_DisableOrderingMonitoring = _libs["libcudd-3.0.0.so"].get("Cudd_DisableOrderingMonitoring", "cdecl")
    Cudd_DisableOrderingMonitoring.argtypes = [POINTER(DdManager)]
    Cudd_DisableOrderingMonitoring.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 643
if _libs["libcudd-3.0.0.so"].has("Cudd_OrderingMonitoring", "cdecl"):
    Cudd_OrderingMonitoring = _libs["libcudd-3.0.0.so"].get("Cudd_OrderingMonitoring", "cdecl")
    Cudd_OrderingMonitoring.argtypes = [POINTER(DdManager)]
    Cudd_OrderingMonitoring.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 644
if _libs["libcudd-3.0.0.so"].has("Cudd_SetApplicationHook", "cdecl"):
    Cudd_SetApplicationHook = _libs["libcudd-3.0.0.so"].get("Cudd_SetApplicationHook", "cdecl")
    Cudd_SetApplicationHook.argtypes = [POINTER(DdManager), POINTER(None)]
    Cudd_SetApplicationHook.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 645
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadApplicationHook", "cdecl"):
    Cudd_ReadApplicationHook = _libs["libcudd-3.0.0.so"].get("Cudd_ReadApplicationHook", "cdecl")
    Cudd_ReadApplicationHook.argtypes = [POINTER(DdManager)]
    Cudd_ReadApplicationHook.restype = POINTER(c_ubyte)
    Cudd_ReadApplicationHook.errcheck = lambda v,*a : cast(v, c_void_p)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 646
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadErrorCode", "cdecl"):
    Cudd_ReadErrorCode = _libs["libcudd-3.0.0.so"].get("Cudd_ReadErrorCode", "cdecl")
    Cudd_ReadErrorCode.argtypes = [POINTER(DdManager)]
    Cudd_ReadErrorCode.restype = Cudd_ErrorType

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 647
if _libs["libcudd-3.0.0.so"].has("Cudd_ClearErrorCode", "cdecl"):
    Cudd_ClearErrorCode = _libs["libcudd-3.0.0.so"].get("Cudd_ClearErrorCode", "cdecl")
    Cudd_ClearErrorCode.argtypes = [POINTER(DdManager)]
    Cudd_ClearErrorCode.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 648
if _libs["libcudd-3.0.0.so"].has("Cudd_InstallOutOfMemoryHandler", "cdecl"):
    Cudd_InstallOutOfMemoryHandler = _libs["libcudd-3.0.0.so"].get("Cudd_InstallOutOfMemoryHandler", "cdecl")
    Cudd_InstallOutOfMemoryHandler.argtypes = [DD_OOMFP]
    Cudd_InstallOutOfMemoryHandler.restype = DD_OOMFP

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 653
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadNextReordering", "cdecl"):
    Cudd_ReadNextReordering = _libs["libcudd-3.0.0.so"].get("Cudd_ReadNextReordering", "cdecl")
    Cudd_ReadNextReordering.argtypes = [POINTER(DdManager)]
    Cudd_ReadNextReordering.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 654
if _libs["libcudd-3.0.0.so"].has("Cudd_SetNextReordering", "cdecl"):
    Cudd_SetNextReordering = _libs["libcudd-3.0.0.so"].get("Cudd_SetNextReordering", "cdecl")
    Cudd_SetNextReordering.argtypes = [POINTER(DdManager), c_uint]
    Cudd_SetNextReordering.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 655
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadSwapSteps", "cdecl"):
    Cudd_ReadSwapSteps = _libs["libcudd-3.0.0.so"].get("Cudd_ReadSwapSteps", "cdecl")
    Cudd_ReadSwapSteps.argtypes = [POINTER(DdManager)]
    Cudd_ReadSwapSteps.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 656
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxLive", "cdecl"):
    Cudd_ReadMaxLive = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxLive", "cdecl")
    Cudd_ReadMaxLive.argtypes = [POINTER(DdManager)]
    Cudd_ReadMaxLive.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 657
if _libs["libcudd-3.0.0.so"].has("Cudd_SetMaxLive", "cdecl"):
    Cudd_SetMaxLive = _libs["libcudd-3.0.0.so"].get("Cudd_SetMaxLive", "cdecl")
    Cudd_SetMaxLive.argtypes = [POINTER(DdManager), c_uint]
    Cudd_SetMaxLive.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 658
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadMaxMemory", "cdecl"):
    Cudd_ReadMaxMemory = _libs["libcudd-3.0.0.so"].get("Cudd_ReadMaxMemory", "cdecl")
    Cudd_ReadMaxMemory.argtypes = [POINTER(DdManager)]
    Cudd_ReadMaxMemory.restype = c_size_t

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 659
if _libs["libcudd-3.0.0.so"].has("Cudd_SetMaxMemory", "cdecl"):
    Cudd_SetMaxMemory = _libs["libcudd-3.0.0.so"].get("Cudd_SetMaxMemory", "cdecl")
    Cudd_SetMaxMemory.argtypes = [POINTER(DdManager), c_size_t]
    Cudd_SetMaxMemory.restype = c_size_t

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 660
if _libs["libcudd-3.0.0.so"].has("Cudd_bddBindVar", "cdecl"):
    Cudd_bddBindVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddBindVar", "cdecl")
    Cudd_bddBindVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddBindVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 661
if _libs["libcudd-3.0.0.so"].has("Cudd_bddUnbindVar", "cdecl"):
    Cudd_bddUnbindVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddUnbindVar", "cdecl")
    Cudd_bddUnbindVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddUnbindVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 662
if _libs["libcudd-3.0.0.so"].has("Cudd_bddVarIsBound", "cdecl"):
    Cudd_bddVarIsBound = _libs["libcudd-3.0.0.so"].get("Cudd_bddVarIsBound", "cdecl")
    Cudd_bddVarIsBound.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddVarIsBound.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 663
if _libs["libcudd-3.0.0.so"].has("Cudd_addExistAbstract", "cdecl"):
    Cudd_addExistAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_addExistAbstract", "cdecl")
    Cudd_addExistAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addExistAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 664
if _libs["libcudd-3.0.0.so"].has("Cudd_addUnivAbstract", "cdecl"):
    Cudd_addUnivAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_addUnivAbstract", "cdecl")
    Cudd_addUnivAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addUnivAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 665
if _libs["libcudd-3.0.0.so"].has("Cudd_addOrAbstract", "cdecl"):
    Cudd_addOrAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_addOrAbstract", "cdecl")
    Cudd_addOrAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addOrAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 666
if _libs["libcudd-3.0.0.so"].has("Cudd_addApply", "cdecl"):
    Cudd_addApply = _libs["libcudd-3.0.0.so"].get("Cudd_addApply", "cdecl")
    Cudd_addApply.argtypes = [POINTER(DdManager), DD_AOP, POINTER(DdNode), POINTER(DdNode)]
    Cudd_addApply.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 667
if _libs["libcudd-3.0.0.so"].has("Cudd_addPlus", "cdecl"):
    Cudd_addPlus = _libs["libcudd-3.0.0.so"].get("Cudd_addPlus", "cdecl")
    Cudd_addPlus.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addPlus.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 668
if _libs["libcudd-3.0.0.so"].has("Cudd_addTimes", "cdecl"):
    Cudd_addTimes = _libs["libcudd-3.0.0.so"].get("Cudd_addTimes", "cdecl")
    Cudd_addTimes.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addTimes.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 669
if _libs["libcudd-3.0.0.so"].has("Cudd_addThreshold", "cdecl"):
    Cudd_addThreshold = _libs["libcudd-3.0.0.so"].get("Cudd_addThreshold", "cdecl")
    Cudd_addThreshold.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addThreshold.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 670
if _libs["libcudd-3.0.0.so"].has("Cudd_addSetNZ", "cdecl"):
    Cudd_addSetNZ = _libs["libcudd-3.0.0.so"].get("Cudd_addSetNZ", "cdecl")
    Cudd_addSetNZ.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addSetNZ.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 671
if _libs["libcudd-3.0.0.so"].has("Cudd_addDivide", "cdecl"):
    Cudd_addDivide = _libs["libcudd-3.0.0.so"].get("Cudd_addDivide", "cdecl")
    Cudd_addDivide.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addDivide.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 672
if _libs["libcudd-3.0.0.so"].has("Cudd_addMinus", "cdecl"):
    Cudd_addMinus = _libs["libcudd-3.0.0.so"].get("Cudd_addMinus", "cdecl")
    Cudd_addMinus.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addMinus.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 673
if _libs["libcudd-3.0.0.so"].has("Cudd_addMinimum", "cdecl"):
    Cudd_addMinimum = _libs["libcudd-3.0.0.so"].get("Cudd_addMinimum", "cdecl")
    Cudd_addMinimum.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addMinimum.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 674
if _libs["libcudd-3.0.0.so"].has("Cudd_addMaximum", "cdecl"):
    Cudd_addMaximum = _libs["libcudd-3.0.0.so"].get("Cudd_addMaximum", "cdecl")
    Cudd_addMaximum.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addMaximum.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 675
if _libs["libcudd-3.0.0.so"].has("Cudd_addOneZeroMaximum", "cdecl"):
    Cudd_addOneZeroMaximum = _libs["libcudd-3.0.0.so"].get("Cudd_addOneZeroMaximum", "cdecl")
    Cudd_addOneZeroMaximum.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addOneZeroMaximum.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 676
if _libs["libcudd-3.0.0.so"].has("Cudd_addDiff", "cdecl"):
    Cudd_addDiff = _libs["libcudd-3.0.0.so"].get("Cudd_addDiff", "cdecl")
    Cudd_addDiff.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addDiff.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 677
if _libs["libcudd-3.0.0.so"].has("Cudd_addAgreement", "cdecl"):
    Cudd_addAgreement = _libs["libcudd-3.0.0.so"].get("Cudd_addAgreement", "cdecl")
    Cudd_addAgreement.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addAgreement.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 678
if _libs["libcudd-3.0.0.so"].has("Cudd_addOr", "cdecl"):
    Cudd_addOr = _libs["libcudd-3.0.0.so"].get("Cudd_addOr", "cdecl")
    Cudd_addOr.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addOr.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 679
if _libs["libcudd-3.0.0.so"].has("Cudd_addNand", "cdecl"):
    Cudd_addNand = _libs["libcudd-3.0.0.so"].get("Cudd_addNand", "cdecl")
    Cudd_addNand.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addNand.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 680
if _libs["libcudd-3.0.0.so"].has("Cudd_addNor", "cdecl"):
    Cudd_addNor = _libs["libcudd-3.0.0.so"].get("Cudd_addNor", "cdecl")
    Cudd_addNor.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addNor.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 681
if _libs["libcudd-3.0.0.so"].has("Cudd_addXor", "cdecl"):
    Cudd_addXor = _libs["libcudd-3.0.0.so"].get("Cudd_addXor", "cdecl")
    Cudd_addXor.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addXor.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 682
if _libs["libcudd-3.0.0.so"].has("Cudd_addXnor", "cdecl"):
    Cudd_addXnor = _libs["libcudd-3.0.0.so"].get("Cudd_addXnor", "cdecl")
    Cudd_addXnor.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addXnor.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 683
if _libs["libcudd-3.0.0.so"].has("Cudd_addMonadicApply", "cdecl"):
    Cudd_addMonadicApply = _libs["libcudd-3.0.0.so"].get("Cudd_addMonadicApply", "cdecl")
    Cudd_addMonadicApply.argtypes = [POINTER(DdManager), DD_MAOP, POINTER(DdNode)]
    Cudd_addMonadicApply.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 684
if _libs["libcudd-3.0.0.so"].has("Cudd_addLog", "cdecl"):
    Cudd_addLog = _libs["libcudd-3.0.0.so"].get("Cudd_addLog", "cdecl")
    Cudd_addLog.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_addLog.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 685
if _libs["libcudd-3.0.0.so"].has("Cudd_addFindMax", "cdecl"):
    Cudd_addFindMax = _libs["libcudd-3.0.0.so"].get("Cudd_addFindMax", "cdecl")
    Cudd_addFindMax.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_addFindMax.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 686
if _libs["libcudd-3.0.0.so"].has("Cudd_addFindMin", "cdecl"):
    Cudd_addFindMin = _libs["libcudd-3.0.0.so"].get("Cudd_addFindMin", "cdecl")
    Cudd_addFindMin.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_addFindMin.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 687
if _libs["libcudd-3.0.0.so"].has("Cudd_addIthBit", "cdecl"):
    Cudd_addIthBit = _libs["libcudd-3.0.0.so"].get("Cudd_addIthBit", "cdecl")
    Cudd_addIthBit.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_addIthBit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 688
if _libs["libcudd-3.0.0.so"].has("Cudd_addScalarInverse", "cdecl"):
    Cudd_addScalarInverse = _libs["libcudd-3.0.0.so"].get("Cudd_addScalarInverse", "cdecl")
    Cudd_addScalarInverse.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addScalarInverse.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 689
if _libs["libcudd-3.0.0.so"].has("Cudd_addIte", "cdecl"):
    Cudd_addIte = _libs["libcudd-3.0.0.so"].get("Cudd_addIte", "cdecl")
    Cudd_addIte.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addIte.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 690
if _libs["libcudd-3.0.0.so"].has("Cudd_addIteConstant", "cdecl"):
    Cudd_addIteConstant = _libs["libcudd-3.0.0.so"].get("Cudd_addIteConstant", "cdecl")
    Cudd_addIteConstant.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addIteConstant.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 691
if _libs["libcudd-3.0.0.so"].has("Cudd_addEvalConst", "cdecl"):
    Cudd_addEvalConst = _libs["libcudd-3.0.0.so"].get("Cudd_addEvalConst", "cdecl")
    Cudd_addEvalConst.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addEvalConst.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 692
if _libs["libcudd-3.0.0.so"].has("Cudd_addLeq", "cdecl"):
    Cudd_addLeq = _libs["libcudd-3.0.0.so"].get("Cudd_addLeq", "cdecl")
    Cudd_addLeq.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addLeq.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 693
if _libs["libcudd-3.0.0.so"].has("Cudd_addCmpl", "cdecl"):
    Cudd_addCmpl = _libs["libcudd-3.0.0.so"].get("Cudd_addCmpl", "cdecl")
    Cudd_addCmpl.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_addCmpl.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 694
if _libs["libcudd-3.0.0.so"].has("Cudd_addNegate", "cdecl"):
    Cudd_addNegate = _libs["libcudd-3.0.0.so"].get("Cudd_addNegate", "cdecl")
    Cudd_addNegate.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_addNegate.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 695
if _libs["libcudd-3.0.0.so"].has("Cudd_addRoundOff", "cdecl"):
    Cudd_addRoundOff = _libs["libcudd-3.0.0.so"].get("Cudd_addRoundOff", "cdecl")
    Cudd_addRoundOff.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_addRoundOff.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 696
if _libs["libcudd-3.0.0.so"].has("Cudd_addWalsh", "cdecl"):
    Cudd_addWalsh = _libs["libcudd-3.0.0.so"].get("Cudd_addWalsh", "cdecl")
    Cudd_addWalsh.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), c_int]
    Cudd_addWalsh.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 697
if _libs["libcudd-3.0.0.so"].has("Cudd_addResidue", "cdecl"):
    Cudd_addResidue = _libs["libcudd-3.0.0.so"].get("Cudd_addResidue", "cdecl")
    Cudd_addResidue.argtypes = [POINTER(DdManager), c_int, c_int, c_int, c_int]
    Cudd_addResidue.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 698
if _libs["libcudd-3.0.0.so"].has("Cudd_bddAndAbstract", "cdecl"):
    Cudd_bddAndAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_bddAndAbstract", "cdecl")
    Cudd_bddAndAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddAndAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 699
if _libs["libcudd-3.0.0.so"].has("Cudd_bddAndAbstractLimit", "cdecl"):
    Cudd_bddAndAbstractLimit = _libs["libcudd-3.0.0.so"].get("Cudd_bddAndAbstractLimit", "cdecl")
    Cudd_bddAndAbstractLimit.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode), c_uint]
    Cudd_bddAndAbstractLimit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 700
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaNumberOfDigits", "cdecl"):
    Cudd_ApaNumberOfDigits = _libs["libcudd-3.0.0.so"].get("Cudd_ApaNumberOfDigits", "cdecl")
    Cudd_ApaNumberOfDigits.argtypes = [c_int]
    Cudd_ApaNumberOfDigits.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 701
if _libs["libcudd-3.0.0.so"].has("Cudd_NewApaNumber", "cdecl"):
    Cudd_NewApaNumber = _libs["libcudd-3.0.0.so"].get("Cudd_NewApaNumber", "cdecl")
    Cudd_NewApaNumber.argtypes = [c_int]
    Cudd_NewApaNumber.restype = DdApaNumber

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 702
if _libs["libcudd-3.0.0.so"].has("Cudd_FreeApaNumber", "cdecl"):
    Cudd_FreeApaNumber = _libs["libcudd-3.0.0.so"].get("Cudd_FreeApaNumber", "cdecl")
    Cudd_FreeApaNumber.argtypes = [DdApaNumber]
    Cudd_FreeApaNumber.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 703
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaCopy", "cdecl"):
    Cudd_ApaCopy = _libs["libcudd-3.0.0.so"].get("Cudd_ApaCopy", "cdecl")
    Cudd_ApaCopy.argtypes = [c_int, DdConstApaNumber, DdApaNumber]
    Cudd_ApaCopy.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 704
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaAdd", "cdecl"):
    Cudd_ApaAdd = _libs["libcudd-3.0.0.so"].get("Cudd_ApaAdd", "cdecl")
    Cudd_ApaAdd.argtypes = [c_int, DdConstApaNumber, DdConstApaNumber, DdApaNumber]
    Cudd_ApaAdd.restype = DdApaDigit

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 705
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaSubtract", "cdecl"):
    Cudd_ApaSubtract = _libs["libcudd-3.0.0.so"].get("Cudd_ApaSubtract", "cdecl")
    Cudd_ApaSubtract.argtypes = [c_int, DdConstApaNumber, DdConstApaNumber, DdApaNumber]
    Cudd_ApaSubtract.restype = DdApaDigit

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 706
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaShortDivision", "cdecl"):
    Cudd_ApaShortDivision = _libs["libcudd-3.0.0.so"].get("Cudd_ApaShortDivision", "cdecl")
    Cudd_ApaShortDivision.argtypes = [c_int, DdConstApaNumber, DdApaDigit, DdApaNumber]
    Cudd_ApaShortDivision.restype = DdApaDigit

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 707
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaIntDivision", "cdecl"):
    Cudd_ApaIntDivision = _libs["libcudd-3.0.0.so"].get("Cudd_ApaIntDivision", "cdecl")
    Cudd_ApaIntDivision.argtypes = [c_int, DdConstApaNumber, c_uint, DdApaNumber]
    Cudd_ApaIntDivision.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 708
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaShiftRight", "cdecl"):
    Cudd_ApaShiftRight = _libs["libcudd-3.0.0.so"].get("Cudd_ApaShiftRight", "cdecl")
    Cudd_ApaShiftRight.argtypes = [c_int, DdApaDigit, DdConstApaNumber, DdApaNumber]
    Cudd_ApaShiftRight.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 709
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaSetToLiteral", "cdecl"):
    Cudd_ApaSetToLiteral = _libs["libcudd-3.0.0.so"].get("Cudd_ApaSetToLiteral", "cdecl")
    Cudd_ApaSetToLiteral.argtypes = [c_int, DdApaNumber, DdApaDigit]
    Cudd_ApaSetToLiteral.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 710
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaPowerOfTwo", "cdecl"):
    Cudd_ApaPowerOfTwo = _libs["libcudd-3.0.0.so"].get("Cudd_ApaPowerOfTwo", "cdecl")
    Cudd_ApaPowerOfTwo.argtypes = [c_int, DdApaNumber, c_int]
    Cudd_ApaPowerOfTwo.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 711
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaCompare", "cdecl"):
    Cudd_ApaCompare = _libs["libcudd-3.0.0.so"].get("Cudd_ApaCompare", "cdecl")
    Cudd_ApaCompare.argtypes = [c_int, DdConstApaNumber, c_int, DdConstApaNumber]
    Cudd_ApaCompare.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 712
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaCompareRatios", "cdecl"):
    Cudd_ApaCompareRatios = _libs["libcudd-3.0.0.so"].get("Cudd_ApaCompareRatios", "cdecl")
    Cudd_ApaCompareRatios.argtypes = [c_int, DdConstApaNumber, c_uint, c_int, DdConstApaNumber, c_uint]
    Cudd_ApaCompareRatios.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 715
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaStringDecimal", "cdecl"):
    Cudd_ApaStringDecimal = _libs["libcudd-3.0.0.so"].get("Cudd_ApaStringDecimal", "cdecl")
    Cudd_ApaStringDecimal.argtypes = [c_int, DdConstApaNumber]
    if sizeof(c_int) == sizeof(c_void_p):
        Cudd_ApaStringDecimal.restype = ReturnString
    else:
        Cudd_ApaStringDecimal.restype = String
        Cudd_ApaStringDecimal.errcheck = ReturnString

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 717
if _libs["libcudd-3.0.0.so"].has("Cudd_ApaCountMinterm", "cdecl"):
    Cudd_ApaCountMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_ApaCountMinterm", "cdecl")
    Cudd_ApaCountMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, POINTER(c_int)]
    Cudd_ApaCountMinterm.restype = DdApaNumber

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 721
if _libs["libcudd-3.0.0.so"].has("Cudd_UnderApprox", "cdecl"):
    Cudd_UnderApprox = _libs["libcudd-3.0.0.so"].get("Cudd_UnderApprox", "cdecl")
    Cudd_UnderApprox.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int, c_int, c_double]
    Cudd_UnderApprox.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 722
if _libs["libcudd-3.0.0.so"].has("Cudd_OverApprox", "cdecl"):
    Cudd_OverApprox = _libs["libcudd-3.0.0.so"].get("Cudd_OverApprox", "cdecl")
    Cudd_OverApprox.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int, c_int, c_double]
    Cudd_OverApprox.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 723
if _libs["libcudd-3.0.0.so"].has("Cudd_RemapUnderApprox", "cdecl"):
    Cudd_RemapUnderApprox = _libs["libcudd-3.0.0.so"].get("Cudd_RemapUnderApprox", "cdecl")
    Cudd_RemapUnderApprox.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int, c_double]
    Cudd_RemapUnderApprox.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 724
if _libs["libcudd-3.0.0.so"].has("Cudd_RemapOverApprox", "cdecl"):
    Cudd_RemapOverApprox = _libs["libcudd-3.0.0.so"].get("Cudd_RemapOverApprox", "cdecl")
    Cudd_RemapOverApprox.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int, c_double]
    Cudd_RemapOverApprox.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 725
if _libs["libcudd-3.0.0.so"].has("Cudd_BiasedUnderApprox", "cdecl"):
    Cudd_BiasedUnderApprox = _libs["libcudd-3.0.0.so"].get("Cudd_BiasedUnderApprox", "cdecl")
    Cudd_BiasedUnderApprox.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_int, c_int, c_double, c_double]
    Cudd_BiasedUnderApprox.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 726
if _libs["libcudd-3.0.0.so"].has("Cudd_BiasedOverApprox", "cdecl"):
    Cudd_BiasedOverApprox = _libs["libcudd-3.0.0.so"].get("Cudd_BiasedOverApprox", "cdecl")
    Cudd_BiasedOverApprox.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_int, c_int, c_double, c_double]
    Cudd_BiasedOverApprox.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 727
if _libs["libcudd-3.0.0.so"].has("Cudd_bddExistAbstract", "cdecl"):
    Cudd_bddExistAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_bddExistAbstract", "cdecl")
    Cudd_bddExistAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddExistAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 728
if _libs["libcudd-3.0.0.so"].has("Cudd_bddExistAbstractLimit", "cdecl"):
    Cudd_bddExistAbstractLimit = _libs["libcudd-3.0.0.so"].get("Cudd_bddExistAbstractLimit", "cdecl")
    Cudd_bddExistAbstractLimit.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_uint]
    Cudd_bddExistAbstractLimit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 729
if _libs["libcudd-3.0.0.so"].has("Cudd_bddXorExistAbstract", "cdecl"):
    Cudd_bddXorExistAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_bddXorExistAbstract", "cdecl")
    Cudd_bddXorExistAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddXorExistAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 730
if _libs["libcudd-3.0.0.so"].has("Cudd_bddUnivAbstract", "cdecl"):
    Cudd_bddUnivAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_bddUnivAbstract", "cdecl")
    Cudd_bddUnivAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddUnivAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 731
if _libs["libcudd-3.0.0.so"].has("Cudd_bddBooleanDiff", "cdecl"):
    Cudd_bddBooleanDiff = _libs["libcudd-3.0.0.so"].get("Cudd_bddBooleanDiff", "cdecl")
    Cudd_bddBooleanDiff.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_bddBooleanDiff.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 732
if _libs["libcudd-3.0.0.so"].has("Cudd_bddVarIsDependent", "cdecl"):
    Cudd_bddVarIsDependent = _libs["libcudd-3.0.0.so"].get("Cudd_bddVarIsDependent", "cdecl")
    Cudd_bddVarIsDependent.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddVarIsDependent.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 733
if _libs["libcudd-3.0.0.so"].has("Cudd_bddCorrelation", "cdecl"):
    Cudd_bddCorrelation = _libs["libcudd-3.0.0.so"].get("Cudd_bddCorrelation", "cdecl")
    Cudd_bddCorrelation.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddCorrelation.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 734
if _libs["libcudd-3.0.0.so"].has("Cudd_bddCorrelationWeights", "cdecl"):
    Cudd_bddCorrelationWeights = _libs["libcudd-3.0.0.so"].get("Cudd_bddCorrelationWeights", "cdecl")
    Cudd_bddCorrelationWeights.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(c_double)]
    Cudd_bddCorrelationWeights.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 735
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIte", "cdecl"):
    Cudd_bddIte = _libs["libcudd-3.0.0.so"].get("Cudd_bddIte", "cdecl")
    Cudd_bddIte.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddIte.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 736
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIteLimit", "cdecl"):
    Cudd_bddIteLimit = _libs["libcudd-3.0.0.so"].get("Cudd_bddIteLimit", "cdecl")
    Cudd_bddIteLimit.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode), c_uint]
    Cudd_bddIteLimit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 737
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIteConstant", "cdecl"):
    Cudd_bddIteConstant = _libs["libcudd-3.0.0.so"].get("Cudd_bddIteConstant", "cdecl")
    Cudd_bddIteConstant.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddIteConstant.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 738
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIntersect", "cdecl"):
    Cudd_bddIntersect = _libs["libcudd-3.0.0.so"].get("Cudd_bddIntersect", "cdecl")
    Cudd_bddIntersect.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddIntersect.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 739
if _libs["libcudd-3.0.0.so"].has("Cudd_bddAnd", "cdecl"):
    Cudd_bddAnd = _libs["libcudd-3.0.0.so"].get("Cudd_bddAnd", "cdecl")
    Cudd_bddAnd.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddAnd.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 740
if _libs["libcudd-3.0.0.so"].has("Cudd_bddAndLimit", "cdecl"):
    Cudd_bddAndLimit = _libs["libcudd-3.0.0.so"].get("Cudd_bddAndLimit", "cdecl")
    Cudd_bddAndLimit.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_uint]
    Cudd_bddAndLimit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 741
if _libs["libcudd-3.0.0.so"].has("Cudd_bddOr", "cdecl"):
    Cudd_bddOr = _libs["libcudd-3.0.0.so"].get("Cudd_bddOr", "cdecl")
    Cudd_bddOr.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddOr.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 742
if _libs["libcudd-3.0.0.so"].has("Cudd_bddOrLimit", "cdecl"):
    Cudd_bddOrLimit = _libs["libcudd-3.0.0.so"].get("Cudd_bddOrLimit", "cdecl")
    Cudd_bddOrLimit.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_uint]
    Cudd_bddOrLimit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 743
if _libs["libcudd-3.0.0.so"].has("Cudd_bddNand", "cdecl"):
    Cudd_bddNand = _libs["libcudd-3.0.0.so"].get("Cudd_bddNand", "cdecl")
    Cudd_bddNand.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddNand.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 744
if _libs["libcudd-3.0.0.so"].has("Cudd_bddNor", "cdecl"):
    Cudd_bddNor = _libs["libcudd-3.0.0.so"].get("Cudd_bddNor", "cdecl")
    Cudd_bddNor.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddNor.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 745
if _libs["libcudd-3.0.0.so"].has("Cudd_bddXor", "cdecl"):
    Cudd_bddXor = _libs["libcudd-3.0.0.so"].get("Cudd_bddXor", "cdecl")
    Cudd_bddXor.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddXor.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 746
if _libs["libcudd-3.0.0.so"].has("Cudd_bddXnor", "cdecl"):
    Cudd_bddXnor = _libs["libcudd-3.0.0.so"].get("Cudd_bddXnor", "cdecl")
    Cudd_bddXnor.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddXnor.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 747
if _libs["libcudd-3.0.0.so"].has("Cudd_bddXnorLimit", "cdecl"):
    Cudd_bddXnorLimit = _libs["libcudd-3.0.0.so"].get("Cudd_bddXnorLimit", "cdecl")
    Cudd_bddXnorLimit.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_uint]
    Cudd_bddXnorLimit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 748
if _libs["libcudd-3.0.0.so"].has("Cudd_bddLeq", "cdecl"):
    Cudd_bddLeq = _libs["libcudd-3.0.0.so"].get("Cudd_bddLeq", "cdecl")
    Cudd_bddLeq.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddLeq.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 749
if _libs["libcudd-3.0.0.so"].has("Cudd_addBddThreshold", "cdecl"):
    Cudd_addBddThreshold = _libs["libcudd-3.0.0.so"].get("Cudd_addBddThreshold", "cdecl")
    Cudd_addBddThreshold.argtypes = [POINTER(DdManager), POINTER(DdNode), CUDD_VALUE_TYPE]
    Cudd_addBddThreshold.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 750
if _libs["libcudd-3.0.0.so"].has("Cudd_addBddStrictThreshold", "cdecl"):
    Cudd_addBddStrictThreshold = _libs["libcudd-3.0.0.so"].get("Cudd_addBddStrictThreshold", "cdecl")
    Cudd_addBddStrictThreshold.argtypes = [POINTER(DdManager), POINTER(DdNode), CUDD_VALUE_TYPE]
    Cudd_addBddStrictThreshold.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 751
if _libs["libcudd-3.0.0.so"].has("Cudd_addBddInterval", "cdecl"):
    Cudd_addBddInterval = _libs["libcudd-3.0.0.so"].get("Cudd_addBddInterval", "cdecl")
    Cudd_addBddInterval.argtypes = [POINTER(DdManager), POINTER(DdNode), CUDD_VALUE_TYPE, CUDD_VALUE_TYPE]
    Cudd_addBddInterval.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 752
if _libs["libcudd-3.0.0.so"].has("Cudd_addBddIthBit", "cdecl"):
    Cudd_addBddIthBit = _libs["libcudd-3.0.0.so"].get("Cudd_addBddIthBit", "cdecl")
    Cudd_addBddIthBit.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_addBddIthBit.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 753
if _libs["libcudd-3.0.0.so"].has("Cudd_BddToAdd", "cdecl"):
    Cudd_BddToAdd = _libs["libcudd-3.0.0.so"].get("Cudd_BddToAdd", "cdecl")
    Cudd_BddToAdd.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_BddToAdd.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 754
if _libs["libcudd-3.0.0.so"].has("Cudd_addBddPattern", "cdecl"):
    Cudd_addBddPattern = _libs["libcudd-3.0.0.so"].get("Cudd_addBddPattern", "cdecl")
    Cudd_addBddPattern.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_addBddPattern.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 755
if _libs["libcudd-3.0.0.so"].has("Cudd_bddTransfer", "cdecl"):
    Cudd_bddTransfer = _libs["libcudd-3.0.0.so"].get("Cudd_bddTransfer", "cdecl")
    Cudd_bddTransfer.argtypes = [POINTER(DdManager), POINTER(DdManager), POINTER(DdNode)]
    Cudd_bddTransfer.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 756
if _libs["libcudd-3.0.0.so"].has("Cudd_DebugCheck", "cdecl"):
    Cudd_DebugCheck = _libs["libcudd-3.0.0.so"].get("Cudd_DebugCheck", "cdecl")
    Cudd_DebugCheck.argtypes = [POINTER(DdManager)]
    Cudd_DebugCheck.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 757
if _libs["libcudd-3.0.0.so"].has("Cudd_CheckKeys", "cdecl"):
    Cudd_CheckKeys = _libs["libcudd-3.0.0.so"].get("Cudd_CheckKeys", "cdecl")
    Cudd_CheckKeys.argtypes = [POINTER(DdManager)]
    Cudd_CheckKeys.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 758
if _libs["libcudd-3.0.0.so"].has("Cudd_bddClippingAnd", "cdecl"):
    Cudd_bddClippingAnd = _libs["libcudd-3.0.0.so"].get("Cudd_bddClippingAnd", "cdecl")
    Cudd_bddClippingAnd.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_int, c_int]
    Cudd_bddClippingAnd.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 759
if _libs["libcudd-3.0.0.so"].has("Cudd_bddClippingAndAbstract", "cdecl"):
    Cudd_bddClippingAndAbstract = _libs["libcudd-3.0.0.so"].get("Cudd_bddClippingAndAbstract", "cdecl")
    Cudd_bddClippingAndAbstract.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode), c_int, c_int]
    Cudd_bddClippingAndAbstract.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 760
if _libs["libcudd-3.0.0.so"].has("Cudd_Cofactor", "cdecl"):
    Cudd_Cofactor = _libs["libcudd-3.0.0.so"].get("Cudd_Cofactor", "cdecl")
    Cudd_Cofactor.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_Cofactor.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 761
if _libs["libcudd-3.0.0.so"].has("Cudd_CheckCube", "cdecl"):
    Cudd_CheckCube = _libs["libcudd-3.0.0.so"].get("Cudd_CheckCube", "cdecl")
    Cudd_CheckCube.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_CheckCube.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 762
if _libs["libcudd-3.0.0.so"].has("Cudd_VarsAreSymmetric", "cdecl"):
    Cudd_VarsAreSymmetric = _libs["libcudd-3.0.0.so"].get("Cudd_VarsAreSymmetric", "cdecl")
    Cudd_VarsAreSymmetric.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_VarsAreSymmetric.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 763
if _libs["libcudd-3.0.0.so"].has("Cudd_bddCompose", "cdecl"):
    Cudd_bddCompose = _libs["libcudd-3.0.0.so"].get("Cudd_bddCompose", "cdecl")
    Cudd_bddCompose.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_int]
    Cudd_bddCompose.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 764
if _libs["libcudd-3.0.0.so"].has("Cudd_addCompose", "cdecl"):
    Cudd_addCompose = _libs["libcudd-3.0.0.so"].get("Cudd_addCompose", "cdecl")
    Cudd_addCompose.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), c_int]
    Cudd_addCompose.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 765
if _libs["libcudd-3.0.0.so"].has("Cudd_addPermute", "cdecl"):
    Cudd_addPermute = _libs["libcudd-3.0.0.so"].get("Cudd_addPermute", "cdecl")
    Cudd_addPermute.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int)]
    Cudd_addPermute.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 766
if _libs["libcudd-3.0.0.so"].has("Cudd_addSwapVariables", "cdecl"):
    Cudd_addSwapVariables = _libs["libcudd-3.0.0.so"].get("Cudd_addSwapVariables", "cdecl")
    Cudd_addSwapVariables.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), c_int]
    Cudd_addSwapVariables.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 767
if _libs["libcudd-3.0.0.so"].has("Cudd_bddPermute", "cdecl"):
    Cudd_bddPermute = _libs["libcudd-3.0.0.so"].get("Cudd_bddPermute", "cdecl")
    Cudd_bddPermute.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int)]
    Cudd_bddPermute.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 768
if _libs["libcudd-3.0.0.so"].has("Cudd_bddVarMap", "cdecl"):
    Cudd_bddVarMap = _libs["libcudd-3.0.0.so"].get("Cudd_bddVarMap", "cdecl")
    Cudd_bddVarMap.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_bddVarMap.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 769
if _libs["libcudd-3.0.0.so"].has("Cudd_SetVarMap", "cdecl"):
    Cudd_SetVarMap = _libs["libcudd-3.0.0.so"].get("Cudd_SetVarMap", "cdecl")
    Cudd_SetVarMap.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), c_int]
    Cudd_SetVarMap.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 770
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSwapVariables", "cdecl"):
    Cudd_bddSwapVariables = _libs["libcudd-3.0.0.so"].get("Cudd_bddSwapVariables", "cdecl")
    Cudd_bddSwapVariables.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), c_int]
    Cudd_bddSwapVariables.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 771
if _libs["libcudd-3.0.0.so"].has("Cudd_bddAdjPermuteX", "cdecl"):
    Cudd_bddAdjPermuteX = _libs["libcudd-3.0.0.so"].get("Cudd_bddAdjPermuteX", "cdecl")
    Cudd_bddAdjPermuteX.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int]
    Cudd_bddAdjPermuteX.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 772
if _libs["libcudd-3.0.0.so"].has("Cudd_addVectorCompose", "cdecl"):
    Cudd_addVectorCompose = _libs["libcudd-3.0.0.so"].get("Cudd_addVectorCompose", "cdecl")
    Cudd_addVectorCompose.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode))]
    Cudd_addVectorCompose.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 773
if _libs["libcudd-3.0.0.so"].has("Cudd_addGeneralVectorCompose", "cdecl"):
    Cudd_addGeneralVectorCompose = _libs["libcudd-3.0.0.so"].get("Cudd_addGeneralVectorCompose", "cdecl")
    Cudd_addGeneralVectorCompose.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addGeneralVectorCompose.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 774
if _libs["libcudd-3.0.0.so"].has("Cudd_addNonSimCompose", "cdecl"):
    Cudd_addNonSimCompose = _libs["libcudd-3.0.0.so"].get("Cudd_addNonSimCompose", "cdecl")
    Cudd_addNonSimCompose.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode))]
    Cudd_addNonSimCompose.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 775
if _libs["libcudd-3.0.0.so"].has("Cudd_bddVectorCompose", "cdecl"):
    Cudd_bddVectorCompose = _libs["libcudd-3.0.0.so"].get("Cudd_bddVectorCompose", "cdecl")
    Cudd_bddVectorCompose.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode))]
    Cudd_bddVectorCompose.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 776
if _libs["libcudd-3.0.0.so"].has("Cudd_bddApproxConjDecomp", "cdecl"):
    Cudd_bddApproxConjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddApproxConjDecomp", "cdecl")
    Cudd_bddApproxConjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddApproxConjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 777
if _libs["libcudd-3.0.0.so"].has("Cudd_bddApproxDisjDecomp", "cdecl"):
    Cudd_bddApproxDisjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddApproxDisjDecomp", "cdecl")
    Cudd_bddApproxDisjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddApproxDisjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 778
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIterConjDecomp", "cdecl"):
    Cudd_bddIterConjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddIterConjDecomp", "cdecl")
    Cudd_bddIterConjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddIterConjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 779
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIterDisjDecomp", "cdecl"):
    Cudd_bddIterDisjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddIterDisjDecomp", "cdecl")
    Cudd_bddIterDisjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddIterDisjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 780
if _libs["libcudd-3.0.0.so"].has("Cudd_bddGenConjDecomp", "cdecl"):
    Cudd_bddGenConjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddGenConjDecomp", "cdecl")
    Cudd_bddGenConjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddGenConjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 781
if _libs["libcudd-3.0.0.so"].has("Cudd_bddGenDisjDecomp", "cdecl"):
    Cudd_bddGenDisjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddGenDisjDecomp", "cdecl")
    Cudd_bddGenDisjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddGenDisjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 782
if _libs["libcudd-3.0.0.so"].has("Cudd_bddVarConjDecomp", "cdecl"):
    Cudd_bddVarConjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddVarConjDecomp", "cdecl")
    Cudd_bddVarConjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddVarConjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 783
if _libs["libcudd-3.0.0.so"].has("Cudd_bddVarDisjDecomp", "cdecl"):
    Cudd_bddVarDisjDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddVarDisjDecomp", "cdecl")
    Cudd_bddVarDisjDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(POINTER(DdNode)))]
    Cudd_bddVarDisjDecomp.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 784
if _libs["libcudd-3.0.0.so"].has("Cudd_FindEssential", "cdecl"):
    Cudd_FindEssential = _libs["libcudd-3.0.0.so"].get("Cudd_FindEssential", "cdecl")
    Cudd_FindEssential.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_FindEssential.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 785
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsVarEssential", "cdecl"):
    Cudd_bddIsVarEssential = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsVarEssential", "cdecl")
    Cudd_bddIsVarEssential.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_bddIsVarEssential.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 786
if _libs["libcudd-3.0.0.so"].has("Cudd_FindTwoLiteralClauses", "cdecl"):
    Cudd_FindTwoLiteralClauses = _libs["libcudd-3.0.0.so"].get("Cudd_FindTwoLiteralClauses", "cdecl")
    Cudd_FindTwoLiteralClauses.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_FindTwoLiteralClauses.restype = POINTER(DdTlcInfo)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 788
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadIthClause", "cdecl"):
    Cudd_ReadIthClause = _libs["libcudd-3.0.0.so"].get("Cudd_ReadIthClause", "cdecl")
    Cudd_ReadIthClause.argtypes = [POINTER(DdTlcInfo), c_int, POINTER(c_uint), POINTER(c_uint), POINTER(c_int), POINTER(c_int)]
    Cudd_ReadIthClause.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 789
if _libs["libcudd-3.0.0.so"].has("Cudd_tlcInfoFree", "cdecl"):
    Cudd_tlcInfoFree = _libs["libcudd-3.0.0.so"].get("Cudd_tlcInfoFree", "cdecl")
    Cudd_tlcInfoFree.argtypes = [POINTER(DdTlcInfo)]
    Cudd_tlcInfoFree.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 796
if _libs["libcudd-3.0.0.so"].has("Cudd_FactoredFormString", "cdecl"):
    Cudd_FactoredFormString = _libs["libcudd-3.0.0.so"].get("Cudd_FactoredFormString", "cdecl")
    Cudd_FactoredFormString.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(c_char))]
    if sizeof(c_int) == sizeof(c_void_p):
        Cudd_FactoredFormString.restype = ReturnString
    else:
        Cudd_FactoredFormString.restype = String
        Cudd_FactoredFormString.errcheck = ReturnString

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 797
if _libs["libcudd-3.0.0.so"].has("Cudd_bddConstrain", "cdecl"):
    Cudd_bddConstrain = _libs["libcudd-3.0.0.so"].get("Cudd_bddConstrain", "cdecl")
    Cudd_bddConstrain.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddConstrain.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 798
if _libs["libcudd-3.0.0.so"].has("Cudd_bddRestrict", "cdecl"):
    Cudd_bddRestrict = _libs["libcudd-3.0.0.so"].get("Cudd_bddRestrict", "cdecl")
    Cudd_bddRestrict.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddRestrict.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 799
if _libs["libcudd-3.0.0.so"].has("Cudd_bddNPAnd", "cdecl"):
    Cudd_bddNPAnd = _libs["libcudd-3.0.0.so"].get("Cudd_bddNPAnd", "cdecl")
    Cudd_bddNPAnd.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddNPAnd.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 800
if _libs["libcudd-3.0.0.so"].has("Cudd_addConstrain", "cdecl"):
    Cudd_addConstrain = _libs["libcudd-3.0.0.so"].get("Cudd_addConstrain", "cdecl")
    Cudd_addConstrain.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addConstrain.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 801
if _libs["libcudd-3.0.0.so"].has("Cudd_bddConstrainDecomp", "cdecl"):
    Cudd_bddConstrainDecomp = _libs["libcudd-3.0.0.so"].get("Cudd_bddConstrainDecomp", "cdecl")
    Cudd_bddConstrainDecomp.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_bddConstrainDecomp.restype = POINTER(POINTER(DdNode))

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 802
if _libs["libcudd-3.0.0.so"].has("Cudd_addRestrict", "cdecl"):
    Cudd_addRestrict = _libs["libcudd-3.0.0.so"].get("Cudd_addRestrict", "cdecl")
    Cudd_addRestrict.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addRestrict.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 803
if _libs["libcudd-3.0.0.so"].has("Cudd_bddCharToVect", "cdecl"):
    Cudd_bddCharToVect = _libs["libcudd-3.0.0.so"].get("Cudd_bddCharToVect", "cdecl")
    Cudd_bddCharToVect.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_bddCharToVect.restype = POINTER(POINTER(DdNode))

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 804
if _libs["libcudd-3.0.0.so"].has("Cudd_bddLICompaction", "cdecl"):
    Cudd_bddLICompaction = _libs["libcudd-3.0.0.so"].get("Cudd_bddLICompaction", "cdecl")
    Cudd_bddLICompaction.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddLICompaction.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 805
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSqueeze", "cdecl"):
    Cudd_bddSqueeze = _libs["libcudd-3.0.0.so"].get("Cudd_bddSqueeze", "cdecl")
    Cudd_bddSqueeze.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddSqueeze.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 806
if _libs["libcudd-3.0.0.so"].has("Cudd_bddInterpolate", "cdecl"):
    Cudd_bddInterpolate = _libs["libcudd-3.0.0.so"].get("Cudd_bddInterpolate", "cdecl")
    Cudd_bddInterpolate.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddInterpolate.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 807
if _libs["libcudd-3.0.0.so"].has("Cudd_bddMinimize", "cdecl"):
    Cudd_bddMinimize = _libs["libcudd-3.0.0.so"].get("Cudd_bddMinimize", "cdecl")
    Cudd_bddMinimize.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddMinimize.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 808
if _libs["libcudd-3.0.0.so"].has("Cudd_SubsetCompress", "cdecl"):
    Cudd_SubsetCompress = _libs["libcudd-3.0.0.so"].get("Cudd_SubsetCompress", "cdecl")
    Cudd_SubsetCompress.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_SubsetCompress.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 809
if _libs["libcudd-3.0.0.so"].has("Cudd_SupersetCompress", "cdecl"):
    Cudd_SupersetCompress = _libs["libcudd-3.0.0.so"].get("Cudd_SupersetCompress", "cdecl")
    Cudd_SupersetCompress.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_SupersetCompress.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 811
if _libs["libcudd-3.0.0.so"].has("Cudd_Init", "cdecl"):
    Cudd_Init = _libs["libcudd-3.0.0.so"].get("Cudd_Init", "cdecl")
    Cudd_Init.argtypes = [c_uint, c_uint, c_uint, c_uint, c_size_t]
    Cudd_Init.restype = POINTER(DdManager)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 812
if _libs["libcudd-3.0.0.so"].has("Cudd_Quit", "cdecl"):
    Cudd_Quit = _libs["libcudd-3.0.0.so"].get("Cudd_Quit", "cdecl")
    Cudd_Quit.argtypes = [POINTER(DdManager)]
    Cudd_Quit.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 813
if _libs["libcudd-3.0.0.so"].has("Cudd_PrintLinear", "cdecl"):
    Cudd_PrintLinear = _libs["libcudd-3.0.0.so"].get("Cudd_PrintLinear", "cdecl")
    Cudd_PrintLinear.argtypes = [POINTER(DdManager)]
    Cudd_PrintLinear.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 814
if _libs["libcudd-3.0.0.so"].has("Cudd_ReadLinear", "cdecl"):
    Cudd_ReadLinear = _libs["libcudd-3.0.0.so"].get("Cudd_ReadLinear", "cdecl")
    Cudd_ReadLinear.argtypes = [POINTER(DdManager), c_int, c_int]
    Cudd_ReadLinear.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 815
if _libs["libcudd-3.0.0.so"].has("Cudd_bddLiteralSetIntersection", "cdecl"):
    Cudd_bddLiteralSetIntersection = _libs["libcudd-3.0.0.so"].get("Cudd_bddLiteralSetIntersection", "cdecl")
    Cudd_bddLiteralSetIntersection.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddLiteralSetIntersection.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 816
if _libs["libcudd-3.0.0.so"].has("Cudd_addMatrixMultiply", "cdecl"):
    Cudd_addMatrixMultiply = _libs["libcudd-3.0.0.so"].get("Cudd_addMatrixMultiply", "cdecl")
    Cudd_addMatrixMultiply.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int]
    Cudd_addMatrixMultiply.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 817
if _libs["libcudd-3.0.0.so"].has("Cudd_addTimesPlus", "cdecl"):
    Cudd_addTimesPlus = _libs["libcudd-3.0.0.so"].get("Cudd_addTimesPlus", "cdecl")
    Cudd_addTimesPlus.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int]
    Cudd_addTimesPlus.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 818
if _libs["libcudd-3.0.0.so"].has("Cudd_addTriangle", "cdecl"):
    Cudd_addTriangle = _libs["libcudd-3.0.0.so"].get("Cudd_addTriangle", "cdecl")
    Cudd_addTriangle.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int]
    Cudd_addTriangle.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 819
if _libs["libcudd-3.0.0.so"].has("Cudd_addOuterSum", "cdecl"):
    Cudd_addOuterSum = _libs["libcudd-3.0.0.so"].get("Cudd_addOuterSum", "cdecl")
    Cudd_addOuterSum.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_addOuterSum.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 820
if _libs["libcudd-3.0.0.so"].has("Cudd_PrioritySelect", "cdecl"):
    Cudd_PrioritySelect = _libs["libcudd-3.0.0.so"].get("Cudd_PrioritySelect", "cdecl")
    Cudd_PrioritySelect.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(DdNode), c_int, DD_PRFP]
    Cudd_PrioritySelect.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 821
if _libs["libcudd-3.0.0.so"].has("Cudd_Xgty", "cdecl"):
    Cudd_Xgty = _libs["libcudd-3.0.0.so"].get("Cudd_Xgty", "cdecl")
    Cudd_Xgty.argtypes = [POINTER(DdManager), c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_Xgty.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 822
if _libs["libcudd-3.0.0.so"].has("Cudd_Xeqy", "cdecl"):
    Cudd_Xeqy = _libs["libcudd-3.0.0.so"].get("Cudd_Xeqy", "cdecl")
    Cudd_Xeqy.argtypes = [POINTER(DdManager), c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_Xeqy.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 823
if _libs["libcudd-3.0.0.so"].has("Cudd_addXeqy", "cdecl"):
    Cudd_addXeqy = _libs["libcudd-3.0.0.so"].get("Cudd_addXeqy", "cdecl")
    Cudd_addXeqy.argtypes = [POINTER(DdManager), c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_addXeqy.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 824
if _libs["libcudd-3.0.0.so"].has("Cudd_Dxygtdxz", "cdecl"):
    Cudd_Dxygtdxz = _libs["libcudd-3.0.0.so"].get("Cudd_Dxygtdxz", "cdecl")
    Cudd_Dxygtdxz.argtypes = [POINTER(DdManager), c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_Dxygtdxz.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 825
if _libs["libcudd-3.0.0.so"].has("Cudd_Dxygtdyz", "cdecl"):
    Cudd_Dxygtdyz = _libs["libcudd-3.0.0.so"].get("Cudd_Dxygtdyz", "cdecl")
    Cudd_Dxygtdyz.argtypes = [POINTER(DdManager), c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_Dxygtdyz.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 826
if _libs["libcudd-3.0.0.so"].has("Cudd_Inequality", "cdecl"):
    Cudd_Inequality = _libs["libcudd-3.0.0.so"].get("Cudd_Inequality", "cdecl")
    Cudd_Inequality.argtypes = [POINTER(DdManager), c_int, c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_Inequality.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 827
if _libs["libcudd-3.0.0.so"].has("Cudd_Disequality", "cdecl"):
    Cudd_Disequality = _libs["libcudd-3.0.0.so"].get("Cudd_Disequality", "cdecl")
    Cudd_Disequality.argtypes = [POINTER(DdManager), c_int, c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_Disequality.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 828
if _libs["libcudd-3.0.0.so"].has("Cudd_bddInterval", "cdecl"):
    Cudd_bddInterval = _libs["libcudd-3.0.0.so"].get("Cudd_bddInterval", "cdecl")
    Cudd_bddInterval.argtypes = [POINTER(DdManager), c_int, POINTER(POINTER(DdNode)), c_uint, c_uint]
    Cudd_bddInterval.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 829
if _libs["libcudd-3.0.0.so"].has("Cudd_CProjection", "cdecl"):
    Cudd_CProjection = _libs["libcudd-3.0.0.so"].get("Cudd_CProjection", "cdecl")
    Cudd_CProjection.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_CProjection.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 830
if _libs["libcudd-3.0.0.so"].has("Cudd_addHamming", "cdecl"):
    Cudd_addHamming = _libs["libcudd-3.0.0.so"].get("Cudd_addHamming", "cdecl")
    Cudd_addHamming.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), c_int]
    Cudd_addHamming.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 831
if _libs["libcudd-3.0.0.so"].has("Cudd_MinHammingDist", "cdecl"):
    Cudd_MinHammingDist = _libs["libcudd-3.0.0.so"].get("Cudd_MinHammingDist", "cdecl")
    Cudd_MinHammingDist.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int), c_int]
    Cudd_MinHammingDist.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 832
if _libs["libcudd-3.0.0.so"].has("Cudd_bddClosestCube", "cdecl"):
    Cudd_bddClosestCube = _libs["libcudd-3.0.0.so"].get("Cudd_bddClosestCube", "cdecl")
    Cudd_bddClosestCube.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(c_int)]
    Cudd_bddClosestCube.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 835
if _libs["libcudd-3.0.0.so"].has("Cudd_Ref", "cdecl"):
    Cudd_Ref = _libs["libcudd-3.0.0.so"].get("Cudd_Ref", "cdecl")
    Cudd_Ref.argtypes = [POINTER(DdNode)]
    Cudd_Ref.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 836
if _libs["libcudd-3.0.0.so"].has("Cudd_RecursiveDeref", "cdecl"):
    Cudd_RecursiveDeref = _libs["libcudd-3.0.0.so"].get("Cudd_RecursiveDeref", "cdecl")
    Cudd_RecursiveDeref.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_RecursiveDeref.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 837
if _libs["libcudd-3.0.0.so"].has("Cudd_IterDerefBdd", "cdecl"):
    Cudd_IterDerefBdd = _libs["libcudd-3.0.0.so"].get("Cudd_IterDerefBdd", "cdecl")
    Cudd_IterDerefBdd.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_IterDerefBdd.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 838
if _libs["libcudd-3.0.0.so"].has("Cudd_DelayedDerefBdd", "cdecl"):
    Cudd_DelayedDerefBdd = _libs["libcudd-3.0.0.so"].get("Cudd_DelayedDerefBdd", "cdecl")
    Cudd_DelayedDerefBdd.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_DelayedDerefBdd.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 839
if _libs["libcudd-3.0.0.so"].has("Cudd_RecursiveDerefZdd", "cdecl"):
    Cudd_RecursiveDerefZdd = _libs["libcudd-3.0.0.so"].get("Cudd_RecursiveDerefZdd", "cdecl")
    Cudd_RecursiveDerefZdd.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_RecursiveDerefZdd.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 840
if _libs["libcudd-3.0.0.so"].has("Cudd_Deref", "cdecl"):
    Cudd_Deref = _libs["libcudd-3.0.0.so"].get("Cudd_Deref", "cdecl")
    Cudd_Deref.argtypes = [POINTER(DdNode)]
    Cudd_Deref.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 841
if _libs["libcudd-3.0.0.so"].has("Cudd_CheckZeroRef", "cdecl"):
    Cudd_CheckZeroRef = _libs["libcudd-3.0.0.so"].get("Cudd_CheckZeroRef", "cdecl")
    Cudd_CheckZeroRef.argtypes = [POINTER(DdManager)]
    Cudd_CheckZeroRef.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 842
if _libs["libcudd-3.0.0.so"].has("Cudd_ReduceHeap", "cdecl"):
    Cudd_ReduceHeap = _libs["libcudd-3.0.0.so"].get("Cudd_ReduceHeap", "cdecl")
    Cudd_ReduceHeap.argtypes = [POINTER(DdManager), Cudd_ReorderingType, c_int]
    Cudd_ReduceHeap.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 843
if _libs["libcudd-3.0.0.so"].has("Cudd_ShuffleHeap", "cdecl"):
    Cudd_ShuffleHeap = _libs["libcudd-3.0.0.so"].get("Cudd_ShuffleHeap", "cdecl")
    Cudd_ShuffleHeap.argtypes = [POINTER(DdManager), POINTER(c_int)]
    Cudd_ShuffleHeap.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 844
if _libs["libcudd-3.0.0.so"].has("Cudd_Eval", "cdecl"):
    Cudd_Eval = _libs["libcudd-3.0.0.so"].get("Cudd_Eval", "cdecl")
    Cudd_Eval.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int)]
    Cudd_Eval.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 845
if _libs["libcudd-3.0.0.so"].has("Cudd_ShortestPath", "cdecl"):
    Cudd_ShortestPath = _libs["libcudd-3.0.0.so"].get("Cudd_ShortestPath", "cdecl")
    Cudd_ShortestPath.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int), POINTER(c_int), POINTER(c_int)]
    Cudd_ShortestPath.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 846
if _libs["libcudd-3.0.0.so"].has("Cudd_LargestCube", "cdecl"):
    Cudd_LargestCube = _libs["libcudd-3.0.0.so"].get("Cudd_LargestCube", "cdecl")
    Cudd_LargestCube.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int)]
    Cudd_LargestCube.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 847
if _libs["libcudd-3.0.0.so"].has("Cudd_ShortestLength", "cdecl"):
    Cudd_ShortestLength = _libs["libcudd-3.0.0.so"].get("Cudd_ShortestLength", "cdecl")
    Cudd_ShortestLength.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int)]
    Cudd_ShortestLength.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 848
if _libs["libcudd-3.0.0.so"].has("Cudd_Decreasing", "cdecl"):
    Cudd_Decreasing = _libs["libcudd-3.0.0.so"].get("Cudd_Decreasing", "cdecl")
    Cudd_Decreasing.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_Decreasing.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 849
if _libs["libcudd-3.0.0.so"].has("Cudd_Increasing", "cdecl"):
    Cudd_Increasing = _libs["libcudd-3.0.0.so"].get("Cudd_Increasing", "cdecl")
    Cudd_Increasing.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_Increasing.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 850
if _libs["libcudd-3.0.0.so"].has("Cudd_EquivDC", "cdecl"):
    Cudd_EquivDC = _libs["libcudd-3.0.0.so"].get("Cudd_EquivDC", "cdecl")
    Cudd_EquivDC.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_EquivDC.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 851
if _libs["libcudd-3.0.0.so"].has("Cudd_bddLeqUnless", "cdecl"):
    Cudd_bddLeqUnless = _libs["libcudd-3.0.0.so"].get("Cudd_bddLeqUnless", "cdecl")
    Cudd_bddLeqUnless.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddLeqUnless.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 852
if _libs["libcudd-3.0.0.so"].has("Cudd_EqualSupNorm", "cdecl"):
    Cudd_EqualSupNorm = _libs["libcudd-3.0.0.so"].get("Cudd_EqualSupNorm", "cdecl")
    Cudd_EqualSupNorm.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), CUDD_VALUE_TYPE, c_int]
    Cudd_EqualSupNorm.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 853
if _libs["libcudd-3.0.0.so"].has("Cudd_bddMakePrime", "cdecl"):
    Cudd_bddMakePrime = _libs["libcudd-3.0.0.so"].get("Cudd_bddMakePrime", "cdecl")
    Cudd_bddMakePrime.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddMakePrime.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 854
if _libs["libcudd-3.0.0.so"].has("Cudd_bddMaximallyExpand", "cdecl"):
    Cudd_bddMaximallyExpand = _libs["libcudd-3.0.0.so"].get("Cudd_bddMaximallyExpand", "cdecl")
    Cudd_bddMaximallyExpand.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddMaximallyExpand.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 855
if _libs["libcudd-3.0.0.so"].has("Cudd_bddLargestPrimeUnate", "cdecl"):
    Cudd_bddLargestPrimeUnate = _libs["libcudd-3.0.0.so"].get("Cudd_bddLargestPrimeUnate", "cdecl")
    Cudd_bddLargestPrimeUnate.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddLargestPrimeUnate.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 856
if _libs["libcudd-3.0.0.so"].has("Cudd_CofMinterm", "cdecl"):
    Cudd_CofMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_CofMinterm", "cdecl")
    Cudd_CofMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_CofMinterm.restype = POINTER(c_double)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 857
if _libs["libcudd-3.0.0.so"].has("Cudd_SolveEqn", "cdecl"):
    Cudd_SolveEqn = _libs["libcudd-3.0.0.so"].get("Cudd_SolveEqn", "cdecl")
    Cudd_SolveEqn.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(c_int)), c_int]
    Cudd_SolveEqn.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 858
if _libs["libcudd-3.0.0.so"].has("Cudd_VerifySol", "cdecl"):
    Cudd_VerifySol = _libs["libcudd-3.0.0.so"].get("Cudd_VerifySol", "cdecl")
    Cudd_VerifySol.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(c_int), c_int]
    Cudd_VerifySol.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 859
if _libs["libcudd-3.0.0.so"].has("Cudd_SplitSet", "cdecl"):
    Cudd_SplitSet = _libs["libcudd-3.0.0.so"].get("Cudd_SplitSet", "cdecl")
    Cudd_SplitSet.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int, c_double]
    Cudd_SplitSet.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 860
if _libs["libcudd-3.0.0.so"].has("Cudd_SubsetHeavyBranch", "cdecl"):
    Cudd_SubsetHeavyBranch = _libs["libcudd-3.0.0.so"].get("Cudd_SubsetHeavyBranch", "cdecl")
    Cudd_SubsetHeavyBranch.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_SubsetHeavyBranch.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 861
if _libs["libcudd-3.0.0.so"].has("Cudd_SupersetHeavyBranch", "cdecl"):
    Cudd_SupersetHeavyBranch = _libs["libcudd-3.0.0.so"].get("Cudd_SupersetHeavyBranch", "cdecl")
    Cudd_SupersetHeavyBranch.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_SupersetHeavyBranch.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 862
if _libs["libcudd-3.0.0.so"].has("Cudd_SubsetShortPaths", "cdecl"):
    Cudd_SubsetShortPaths = _libs["libcudd-3.0.0.so"].get("Cudd_SubsetShortPaths", "cdecl")
    Cudd_SubsetShortPaths.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int, c_int]
    Cudd_SubsetShortPaths.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 863
if _libs["libcudd-3.0.0.so"].has("Cudd_SupersetShortPaths", "cdecl"):
    Cudd_SupersetShortPaths = _libs["libcudd-3.0.0.so"].get("Cudd_SupersetShortPaths", "cdecl")
    Cudd_SupersetShortPaths.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int, c_int]
    Cudd_SupersetShortPaths.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 864
if _libs["libcudd-3.0.0.so"].has("Cudd_SymmProfile", "cdecl"):
    Cudd_SymmProfile = _libs["libcudd-3.0.0.so"].get("Cudd_SymmProfile", "cdecl")
    Cudd_SymmProfile.argtypes = [POINTER(DdManager), c_int, c_int]
    Cudd_SymmProfile.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 865
if _libs["libcudd-3.0.0.so"].has("Cudd_Prime", "cdecl"):
    Cudd_Prime = _libs["libcudd-3.0.0.so"].get("Cudd_Prime", "cdecl")
    Cudd_Prime.argtypes = [c_uint]
    Cudd_Prime.restype = c_uint

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 866
if _libs["libcudd-3.0.0.so"].has("Cudd_Reserve", "cdecl"):
    Cudd_Reserve = _libs["libcudd-3.0.0.so"].get("Cudd_Reserve", "cdecl")
    Cudd_Reserve.argtypes = [POINTER(DdManager), c_int]
    Cudd_Reserve.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 867
if _libs["libcudd-3.0.0.so"].has("Cudd_PrintMinterm", "cdecl"):
    Cudd_PrintMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_PrintMinterm", "cdecl")
    Cudd_PrintMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_PrintMinterm.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 868
if _libs["libcudd-3.0.0.so"].has("Cudd_bddPrintCover", "cdecl"):
    Cudd_bddPrintCover = _libs["libcudd-3.0.0.so"].get("Cudd_bddPrintCover", "cdecl")
    Cudd_bddPrintCover.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddPrintCover.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 869
if _libs["libcudd-3.0.0.so"].has("Cudd_PrintDebug", "cdecl"):
    Cudd_PrintDebug = _libs["libcudd-3.0.0.so"].get("Cudd_PrintDebug", "cdecl")
    Cudd_PrintDebug.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_PrintDebug.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 870
if _libs["libcudd-3.0.0.so"].has("Cudd_PrintSummary", "cdecl"):
    Cudd_PrintSummary = _libs["libcudd-3.0.0.so"].get("Cudd_PrintSummary", "cdecl")
    Cudd_PrintSummary.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_PrintSummary.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 871
if _libs["libcudd-3.0.0.so"].has("Cudd_DagSize", "cdecl"):
    Cudd_DagSize = _libs["libcudd-3.0.0.so"].get("Cudd_DagSize", "cdecl")
    Cudd_DagSize.argtypes = [POINTER(DdNode)]
    Cudd_DagSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 872
if _libs["libcudd-3.0.0.so"].has("Cudd_EstimateCofactor", "cdecl"):
    Cudd_EstimateCofactor = _libs["libcudd-3.0.0.so"].get("Cudd_EstimateCofactor", "cdecl")
    Cudd_EstimateCofactor.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_EstimateCofactor.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 873
if _libs["libcudd-3.0.0.so"].has("Cudd_EstimateCofactorSimple", "cdecl"):
    Cudd_EstimateCofactorSimple = _libs["libcudd-3.0.0.so"].get("Cudd_EstimateCofactorSimple", "cdecl")
    Cudd_EstimateCofactorSimple.argtypes = [POINTER(DdNode), c_int]
    Cudd_EstimateCofactorSimple.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 874
if _libs["libcudd-3.0.0.so"].has("Cudd_SharingSize", "cdecl"):
    Cudd_SharingSize = _libs["libcudd-3.0.0.so"].get("Cudd_SharingSize", "cdecl")
    Cudd_SharingSize.argtypes = [POINTER(POINTER(DdNode)), c_int]
    Cudd_SharingSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 875
if _libs["libcudd-3.0.0.so"].has("Cudd_CountMinterm", "cdecl"):
    Cudd_CountMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_CountMinterm", "cdecl")
    Cudd_CountMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_CountMinterm.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 879
if _libs["libcudd-3.0.0.so"].has("Cudd_LdblCountMinterm", "cdecl"):
    Cudd_LdblCountMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_LdblCountMinterm", "cdecl")
    Cudd_LdblCountMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_LdblCountMinterm.restype = c_longdouble

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 880
if _libs["libcudd-3.0.0.so"].has("Cudd_EpdPrintMinterm", "cdecl"):
    Cudd_EpdPrintMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_EpdPrintMinterm", "cdecl")
    Cudd_EpdPrintMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_EpdPrintMinterm.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 881
if _libs["libcudd-3.0.0.so"].has("Cudd_CountPath", "cdecl"):
    Cudd_CountPath = _libs["libcudd-3.0.0.so"].get("Cudd_CountPath", "cdecl")
    Cudd_CountPath.argtypes = [POINTER(DdNode)]
    Cudd_CountPath.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 882
if _libs["libcudd-3.0.0.so"].has("Cudd_CountPathsToNonZero", "cdecl"):
    Cudd_CountPathsToNonZero = _libs["libcudd-3.0.0.so"].get("Cudd_CountPathsToNonZero", "cdecl")
    Cudd_CountPathsToNonZero.argtypes = [POINTER(DdNode)]
    Cudd_CountPathsToNonZero.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 883
if _libs["libcudd-3.0.0.so"].has("Cudd_SupportIndices", "cdecl"):
    Cudd_SupportIndices = _libs["libcudd-3.0.0.so"].get("Cudd_SupportIndices", "cdecl")
    Cudd_SupportIndices.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(c_int))]
    Cudd_SupportIndices.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 884
if _libs["libcudd-3.0.0.so"].has("Cudd_Support", "cdecl"):
    Cudd_Support = _libs["libcudd-3.0.0.so"].get("Cudd_Support", "cdecl")
    Cudd_Support.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_Support.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 885
if _libs["libcudd-3.0.0.so"].has("Cudd_SupportIndex", "cdecl"):
    Cudd_SupportIndex = _libs["libcudd-3.0.0.so"].get("Cudd_SupportIndex", "cdecl")
    Cudd_SupportIndex.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_SupportIndex.restype = POINTER(c_int)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 886
if _libs["libcudd-3.0.0.so"].has("Cudd_SupportSize", "cdecl"):
    Cudd_SupportSize = _libs["libcudd-3.0.0.so"].get("Cudd_SupportSize", "cdecl")
    Cudd_SupportSize.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_SupportSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 887
if _libs["libcudd-3.0.0.so"].has("Cudd_VectorSupportIndices", "cdecl"):
    Cudd_VectorSupportIndices = _libs["libcudd-3.0.0.so"].get("Cudd_VectorSupportIndices", "cdecl")
    Cudd_VectorSupportIndices.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), c_int, POINTER(POINTER(c_int))]
    Cudd_VectorSupportIndices.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 888
if _libs["libcudd-3.0.0.so"].has("Cudd_VectorSupport", "cdecl"):
    Cudd_VectorSupport = _libs["libcudd-3.0.0.so"].get("Cudd_VectorSupport", "cdecl")
    Cudd_VectorSupport.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), c_int]
    Cudd_VectorSupport.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 889
if _libs["libcudd-3.0.0.so"].has("Cudd_VectorSupportIndex", "cdecl"):
    Cudd_VectorSupportIndex = _libs["libcudd-3.0.0.so"].get("Cudd_VectorSupportIndex", "cdecl")
    Cudd_VectorSupportIndex.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), c_int]
    Cudd_VectorSupportIndex.restype = POINTER(c_int)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 890
if _libs["libcudd-3.0.0.so"].has("Cudd_VectorSupportSize", "cdecl"):
    Cudd_VectorSupportSize = _libs["libcudd-3.0.0.so"].get("Cudd_VectorSupportSize", "cdecl")
    Cudd_VectorSupportSize.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), c_int]
    Cudd_VectorSupportSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 891
if _libs["libcudd-3.0.0.so"].has("Cudd_ClassifySupport", "cdecl"):
    Cudd_ClassifySupport = _libs["libcudd-3.0.0.so"].get("Cudd_ClassifySupport", "cdecl")
    Cudd_ClassifySupport.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))]
    Cudd_ClassifySupport.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 892
if _libs["libcudd-3.0.0.so"].has("Cudd_CountLeaves", "cdecl"):
    Cudd_CountLeaves = _libs["libcudd-3.0.0.so"].get("Cudd_CountLeaves", "cdecl")
    Cudd_CountLeaves.argtypes = [POINTER(DdNode)]
    Cudd_CountLeaves.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 893
if _libs["libcudd-3.0.0.so"].has("Cudd_bddPickOneCube", "cdecl"):
    Cudd_bddPickOneCube = _libs["libcudd-3.0.0.so"].get("Cudd_bddPickOneCube", "cdecl")
    Cudd_bddPickOneCube.argtypes = [POINTER(DdManager), POINTER(DdNode), String]
    Cudd_bddPickOneCube.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 894
if _libs["libcudd-3.0.0.so"].has("Cudd_bddPickOneMinterm", "cdecl"):
    Cudd_bddPickOneMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_bddPickOneMinterm", "cdecl")
    Cudd_bddPickOneMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int]
    Cudd_bddPickOneMinterm.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 895
if _libs["libcudd-3.0.0.so"].has("Cudd_bddPickArbitraryMinterms", "cdecl"):
    Cudd_bddPickArbitraryMinterms = _libs["libcudd-3.0.0.so"].get("Cudd_bddPickArbitraryMinterms", "cdecl")
    Cudd_bddPickArbitraryMinterms.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int, c_int]
    Cudd_bddPickArbitraryMinterms.restype = POINTER(POINTER(DdNode))

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 896
if _libs["libcudd-3.0.0.so"].has("Cudd_SubsetWithMaskVars", "cdecl"):
    Cudd_SubsetWithMaskVars = _libs["libcudd-3.0.0.so"].get("Cudd_SubsetWithMaskVars", "cdecl")
    Cudd_SubsetWithMaskVars.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), c_int, POINTER(POINTER(DdNode)), c_int]
    Cudd_SubsetWithMaskVars.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 897
if _libs["libcudd-3.0.0.so"].has("Cudd_FirstCube", "cdecl"):
    Cudd_FirstCube = _libs["libcudd-3.0.0.so"].get("Cudd_FirstCube", "cdecl")
    Cudd_FirstCube.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(c_int)), POINTER(CUDD_VALUE_TYPE)]
    Cudd_FirstCube.restype = POINTER(DdGen)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 898
if _libs["libcudd-3.0.0.so"].has("Cudd_NextCube", "cdecl"):
    Cudd_NextCube = _libs["libcudd-3.0.0.so"].get("Cudd_NextCube", "cdecl")
    Cudd_NextCube.argtypes = [POINTER(DdGen), POINTER(POINTER(c_int)), POINTER(CUDD_VALUE_TYPE)]
    Cudd_NextCube.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 899
if _libs["libcudd-3.0.0.so"].has("Cudd_FirstPrime", "cdecl"):
    Cudd_FirstPrime = _libs["libcudd-3.0.0.so"].get("Cudd_FirstPrime", "cdecl")
    Cudd_FirstPrime.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(POINTER(c_int))]
    Cudd_FirstPrime.restype = POINTER(DdGen)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 900
if _libs["libcudd-3.0.0.so"].has("Cudd_NextPrime", "cdecl"):
    Cudd_NextPrime = _libs["libcudd-3.0.0.so"].get("Cudd_NextPrime", "cdecl")
    Cudd_NextPrime.argtypes = [POINTER(DdGen), POINTER(POINTER(c_int))]
    Cudd_NextPrime.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 901
if _libs["libcudd-3.0.0.so"].has("Cudd_bddComputeCube", "cdecl"):
    Cudd_bddComputeCube = _libs["libcudd-3.0.0.so"].get("Cudd_bddComputeCube", "cdecl")
    Cudd_bddComputeCube.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(c_int), c_int]
    Cudd_bddComputeCube.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 902
if _libs["libcudd-3.0.0.so"].has("Cudd_addComputeCube", "cdecl"):
    Cudd_addComputeCube = _libs["libcudd-3.0.0.so"].get("Cudd_addComputeCube", "cdecl")
    Cudd_addComputeCube.argtypes = [POINTER(DdManager), POINTER(POINTER(DdNode)), POINTER(c_int), c_int]
    Cudd_addComputeCube.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 903
if _libs["libcudd-3.0.0.so"].has("Cudd_CubeArrayToBdd", "cdecl"):
    Cudd_CubeArrayToBdd = _libs["libcudd-3.0.0.so"].get("Cudd_CubeArrayToBdd", "cdecl")
    Cudd_CubeArrayToBdd.argtypes = [POINTER(DdManager), POINTER(c_int)]
    Cudd_CubeArrayToBdd.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 904
if _libs["libcudd-3.0.0.so"].has("Cudd_BddToCubeArray", "cdecl"):
    Cudd_BddToCubeArray = _libs["libcudd-3.0.0.so"].get("Cudd_BddToCubeArray", "cdecl")
    Cudd_BddToCubeArray.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(c_int)]
    Cudd_BddToCubeArray.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 905
if _libs["libcudd-3.0.0.so"].has("Cudd_FirstNode", "cdecl"):
    Cudd_FirstNode = _libs["libcudd-3.0.0.so"].get("Cudd_FirstNode", "cdecl")
    Cudd_FirstNode.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode))]
    Cudd_FirstNode.restype = POINTER(DdGen)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 906
if _libs["libcudd-3.0.0.so"].has("Cudd_NextNode", "cdecl"):
    Cudd_NextNode = _libs["libcudd-3.0.0.so"].get("Cudd_NextNode", "cdecl")
    Cudd_NextNode.argtypes = [POINTER(DdGen), POINTER(POINTER(DdNode))]
    Cudd_NextNode.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 907
if _libs["libcudd-3.0.0.so"].has("Cudd_GenFree", "cdecl"):
    Cudd_GenFree = _libs["libcudd-3.0.0.so"].get("Cudd_GenFree", "cdecl")
    Cudd_GenFree.argtypes = [POINTER(DdGen)]
    Cudd_GenFree.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 908
if _libs["libcudd-3.0.0.so"].has("Cudd_IsGenEmpty", "cdecl"):
    Cudd_IsGenEmpty = _libs["libcudd-3.0.0.so"].get("Cudd_IsGenEmpty", "cdecl")
    Cudd_IsGenEmpty.argtypes = [POINTER(DdGen)]
    Cudd_IsGenEmpty.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 909
if _libs["libcudd-3.0.0.so"].has("Cudd_IndicesToCube", "cdecl"):
    Cudd_IndicesToCube = _libs["libcudd-3.0.0.so"].get("Cudd_IndicesToCube", "cdecl")
    Cudd_IndicesToCube.argtypes = [POINTER(DdManager), POINTER(c_int), c_int]
    Cudd_IndicesToCube.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 911
if _libs["libcudd-3.0.0.so"].has("Cudd_AverageDistance", "cdecl"):
    Cudd_AverageDistance = _libs["libcudd-3.0.0.so"].get("Cudd_AverageDistance", "cdecl")
    Cudd_AverageDistance.argtypes = [POINTER(DdManager)]
    Cudd_AverageDistance.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 912
if _libs["libcudd-3.0.0.so"].has("Cudd_Random", "cdecl"):
    Cudd_Random = _libs["libcudd-3.0.0.so"].get("Cudd_Random", "cdecl")
    Cudd_Random.argtypes = [POINTER(DdManager)]
    Cudd_Random.restype = c_int32

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 913
if _libs["libcudd-3.0.0.so"].has("Cudd_Srandom", "cdecl"):
    Cudd_Srandom = _libs["libcudd-3.0.0.so"].get("Cudd_Srandom", "cdecl")
    Cudd_Srandom.argtypes = [POINTER(DdManager), c_int32]
    Cudd_Srandom.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 914
if _libs["libcudd-3.0.0.so"].has("Cudd_Density", "cdecl"):
    Cudd_Density = _libs["libcudd-3.0.0.so"].get("Cudd_Density", "cdecl")
    Cudd_Density.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_Density.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 915
if _libs["libcudd-3.0.0.so"].has("Cudd_OutOfMem", "cdecl"):
    Cudd_OutOfMem = _libs["libcudd-3.0.0.so"].get("Cudd_OutOfMem", "cdecl")
    Cudd_OutOfMem.argtypes = [c_size_t]
    Cudd_OutOfMem.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 916
if _libs["libcudd-3.0.0.so"].has("Cudd_OutOfMemSilent", "cdecl"):
    Cudd_OutOfMemSilent = _libs["libcudd-3.0.0.so"].get("Cudd_OutOfMemSilent", "cdecl")
    Cudd_OutOfMemSilent.argtypes = [c_size_t]
    Cudd_OutOfMemSilent.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 917
if _libs["libcudd-3.0.0.so"].has("Cudd_zddCount", "cdecl"):
    Cudd_zddCount = _libs["libcudd-3.0.0.so"].get("Cudd_zddCount", "cdecl")
    Cudd_zddCount.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddCount.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 918
if _libs["libcudd-3.0.0.so"].has("Cudd_zddCountDouble", "cdecl"):
    Cudd_zddCountDouble = _libs["libcudd-3.0.0.so"].get("Cudd_zddCountDouble", "cdecl")
    Cudd_zddCountDouble.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddCountDouble.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 919
if _libs["libcudd-3.0.0.so"].has("Cudd_zddProduct", "cdecl"):
    Cudd_zddProduct = _libs["libcudd-3.0.0.so"].get("Cudd_zddProduct", "cdecl")
    Cudd_zddProduct.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddProduct.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 920
if _libs["libcudd-3.0.0.so"].has("Cudd_zddUnateProduct", "cdecl"):
    Cudd_zddUnateProduct = _libs["libcudd-3.0.0.so"].get("Cudd_zddUnateProduct", "cdecl")
    Cudd_zddUnateProduct.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddUnateProduct.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 921
if _libs["libcudd-3.0.0.so"].has("Cudd_zddWeakDiv", "cdecl"):
    Cudd_zddWeakDiv = _libs["libcudd-3.0.0.so"].get("Cudd_zddWeakDiv", "cdecl")
    Cudd_zddWeakDiv.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddWeakDiv.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 922
if _libs["libcudd-3.0.0.so"].has("Cudd_zddDivide", "cdecl"):
    Cudd_zddDivide = _libs["libcudd-3.0.0.so"].get("Cudd_zddDivide", "cdecl")
    Cudd_zddDivide.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddDivide.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 923
if _libs["libcudd-3.0.0.so"].has("Cudd_zddWeakDivF", "cdecl"):
    Cudd_zddWeakDivF = _libs["libcudd-3.0.0.so"].get("Cudd_zddWeakDivF", "cdecl")
    Cudd_zddWeakDivF.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddWeakDivF.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 924
if _libs["libcudd-3.0.0.so"].has("Cudd_zddDivideF", "cdecl"):
    Cudd_zddDivideF = _libs["libcudd-3.0.0.so"].get("Cudd_zddDivideF", "cdecl")
    Cudd_zddDivideF.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddDivideF.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 925
if _libs["libcudd-3.0.0.so"].has("Cudd_zddComplement", "cdecl"):
    Cudd_zddComplement = _libs["libcudd-3.0.0.so"].get("Cudd_zddComplement", "cdecl")
    Cudd_zddComplement.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddComplement.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 926
if _libs["libcudd-3.0.0.so"].has("Cudd_zddIsop", "cdecl"):
    Cudd_zddIsop = _libs["libcudd-3.0.0.so"].get("Cudd_zddIsop", "cdecl")
    Cudd_zddIsop.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(POINTER(DdNode))]
    Cudd_zddIsop.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 927
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsop", "cdecl"):
    Cudd_bddIsop = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsop", "cdecl")
    Cudd_bddIsop.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_bddIsop.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 928
if _libs["libcudd-3.0.0.so"].has("Cudd_MakeBddFromZddCover", "cdecl"):
    Cudd_MakeBddFromZddCover = _libs["libcudd-3.0.0.so"].get("Cudd_MakeBddFromZddCover", "cdecl")
    Cudd_MakeBddFromZddCover.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_MakeBddFromZddCover.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 929
if _libs["libcudd-3.0.0.so"].has("Cudd_zddDagSize", "cdecl"):
    Cudd_zddDagSize = _libs["libcudd-3.0.0.so"].get("Cudd_zddDagSize", "cdecl")
    Cudd_zddDagSize.argtypes = [POINTER(DdNode)]
    Cudd_zddDagSize.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 930
if _libs["libcudd-3.0.0.so"].has("Cudd_zddCountMinterm", "cdecl"):
    Cudd_zddCountMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_zddCountMinterm", "cdecl")
    Cudd_zddCountMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_zddCountMinterm.restype = c_double

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 931
if _libs["libcudd-3.0.0.so"].has("Cudd_zddPrintSubtable", "cdecl"):
    Cudd_zddPrintSubtable = _libs["libcudd-3.0.0.so"].get("Cudd_zddPrintSubtable", "cdecl")
    Cudd_zddPrintSubtable.argtypes = [POINTER(DdManager)]
    Cudd_zddPrintSubtable.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 932
if _libs["libcudd-3.0.0.so"].has("Cudd_zddPortFromBdd", "cdecl"):
    Cudd_zddPortFromBdd = _libs["libcudd-3.0.0.so"].get("Cudd_zddPortFromBdd", "cdecl")
    Cudd_zddPortFromBdd.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddPortFromBdd.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 933
if _libs["libcudd-3.0.0.so"].has("Cudd_zddPortToBdd", "cdecl"):
    Cudd_zddPortToBdd = _libs["libcudd-3.0.0.so"].get("Cudd_zddPortToBdd", "cdecl")
    Cudd_zddPortToBdd.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddPortToBdd.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 934
if _libs["libcudd-3.0.0.so"].has("Cudd_zddReduceHeap", "cdecl"):
    Cudd_zddReduceHeap = _libs["libcudd-3.0.0.so"].get("Cudd_zddReduceHeap", "cdecl")
    Cudd_zddReduceHeap.argtypes = [POINTER(DdManager), Cudd_ReorderingType, c_int]
    Cudd_zddReduceHeap.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 935
if _libs["libcudd-3.0.0.so"].has("Cudd_zddShuffleHeap", "cdecl"):
    Cudd_zddShuffleHeap = _libs["libcudd-3.0.0.so"].get("Cudd_zddShuffleHeap", "cdecl")
    Cudd_zddShuffleHeap.argtypes = [POINTER(DdManager), POINTER(c_int)]
    Cudd_zddShuffleHeap.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 936
if _libs["libcudd-3.0.0.so"].has("Cudd_zddIte", "cdecl"):
    Cudd_zddIte = _libs["libcudd-3.0.0.so"].get("Cudd_zddIte", "cdecl")
    Cudd_zddIte.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddIte.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 937
if _libs["libcudd-3.0.0.so"].has("Cudd_zddUnion", "cdecl"):
    Cudd_zddUnion = _libs["libcudd-3.0.0.so"].get("Cudd_zddUnion", "cdecl")
    Cudd_zddUnion.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddUnion.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 938
if _libs["libcudd-3.0.0.so"].has("Cudd_zddIntersect", "cdecl"):
    Cudd_zddIntersect = _libs["libcudd-3.0.0.so"].get("Cudd_zddIntersect", "cdecl")
    Cudd_zddIntersect.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddIntersect.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 939
if _libs["libcudd-3.0.0.so"].has("Cudd_zddDiff", "cdecl"):
    Cudd_zddDiff = _libs["libcudd-3.0.0.so"].get("Cudd_zddDiff", "cdecl")
    Cudd_zddDiff.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddDiff.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 940
if _libs["libcudd-3.0.0.so"].has("Cudd_zddDiffConst", "cdecl"):
    Cudd_zddDiffConst = _libs["libcudd-3.0.0.so"].get("Cudd_zddDiffConst", "cdecl")
    Cudd_zddDiffConst.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)]
    Cudd_zddDiffConst.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 941
if _libs["libcudd-3.0.0.so"].has("Cudd_zddSubset1", "cdecl"):
    Cudd_zddSubset1 = _libs["libcudd-3.0.0.so"].get("Cudd_zddSubset1", "cdecl")
    Cudd_zddSubset1.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_zddSubset1.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 942
if _libs["libcudd-3.0.0.so"].has("Cudd_zddSubset0", "cdecl"):
    Cudd_zddSubset0 = _libs["libcudd-3.0.0.so"].get("Cudd_zddSubset0", "cdecl")
    Cudd_zddSubset0.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_zddSubset0.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 943
if _libs["libcudd-3.0.0.so"].has("Cudd_zddChange", "cdecl"):
    Cudd_zddChange = _libs["libcudd-3.0.0.so"].get("Cudd_zddChange", "cdecl")
    Cudd_zddChange.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int]
    Cudd_zddChange.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 944
if _libs["libcudd-3.0.0.so"].has("Cudd_zddSymmProfile", "cdecl"):
    Cudd_zddSymmProfile = _libs["libcudd-3.0.0.so"].get("Cudd_zddSymmProfile", "cdecl")
    Cudd_zddSymmProfile.argtypes = [POINTER(DdManager), c_int, c_int]
    Cudd_zddSymmProfile.restype = None

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 945
if _libs["libcudd-3.0.0.so"].has("Cudd_zddPrintMinterm", "cdecl"):
    Cudd_zddPrintMinterm = _libs["libcudd-3.0.0.so"].get("Cudd_zddPrintMinterm", "cdecl")
    Cudd_zddPrintMinterm.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddPrintMinterm.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 946
if _libs["libcudd-3.0.0.so"].has("Cudd_zddPrintCover", "cdecl"):
    Cudd_zddPrintCover = _libs["libcudd-3.0.0.so"].get("Cudd_zddPrintCover", "cdecl")
    Cudd_zddPrintCover.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddPrintCover.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 947
if _libs["libcudd-3.0.0.so"].has("Cudd_zddPrintDebug", "cdecl"):
    Cudd_zddPrintDebug = _libs["libcudd-3.0.0.so"].get("Cudd_zddPrintDebug", "cdecl")
    Cudd_zddPrintDebug.argtypes = [POINTER(DdManager), POINTER(DdNode), c_int, c_int]
    Cudd_zddPrintDebug.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 948
if _libs["libcudd-3.0.0.so"].has("Cudd_zddFirstPath", "cdecl"):
    Cudd_zddFirstPath = _libs["libcudd-3.0.0.so"].get("Cudd_zddFirstPath", "cdecl")
    Cudd_zddFirstPath.argtypes = [POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(c_int))]
    Cudd_zddFirstPath.restype = POINTER(DdGen)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 949
if _libs["libcudd-3.0.0.so"].has("Cudd_zddNextPath", "cdecl"):
    Cudd_zddNextPath = _libs["libcudd-3.0.0.so"].get("Cudd_zddNextPath", "cdecl")
    Cudd_zddNextPath.argtypes = [POINTER(DdGen), POINTER(POINTER(c_int))]
    Cudd_zddNextPath.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 950
if _libs["libcudd-3.0.0.so"].has("Cudd_zddCoverPathToString", "cdecl"):
    Cudd_zddCoverPathToString = _libs["libcudd-3.0.0.so"].get("Cudd_zddCoverPathToString", "cdecl")
    Cudd_zddCoverPathToString.argtypes = [POINTER(DdManager), POINTER(c_int), String]
    if sizeof(c_int) == sizeof(c_void_p):
        Cudd_zddCoverPathToString.restype = ReturnString
    else:
        Cudd_zddCoverPathToString.restype = String
        Cudd_zddCoverPathToString.errcheck = ReturnString

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 951
if _libs["libcudd-3.0.0.so"].has("Cudd_zddSupport", "cdecl"):
    Cudd_zddSupport = _libs["libcudd-3.0.0.so"].get("Cudd_zddSupport", "cdecl")
    Cudd_zddSupport.argtypes = [POINTER(DdManager), POINTER(DdNode)]
    Cudd_zddSupport.restype = POINTER(DdNode)

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 953
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSetPiVar", "cdecl"):
    Cudd_bddSetPiVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddSetPiVar", "cdecl")
    Cudd_bddSetPiVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddSetPiVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 954
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSetPsVar", "cdecl"):
    Cudd_bddSetPsVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddSetPsVar", "cdecl")
    Cudd_bddSetPsVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddSetPsVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 955
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSetNsVar", "cdecl"):
    Cudd_bddSetNsVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddSetNsVar", "cdecl")
    Cudd_bddSetNsVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddSetNsVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 956
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsPiVar", "cdecl"):
    Cudd_bddIsPiVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsPiVar", "cdecl")
    Cudd_bddIsPiVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddIsPiVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 957
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsPsVar", "cdecl"):
    Cudd_bddIsPsVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsPsVar", "cdecl")
    Cudd_bddIsPsVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddIsPsVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 958
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsNsVar", "cdecl"):
    Cudd_bddIsNsVar = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsNsVar", "cdecl")
    Cudd_bddIsNsVar.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddIsNsVar.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 959
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSetPairIndex", "cdecl"):
    Cudd_bddSetPairIndex = _libs["libcudd-3.0.0.so"].get("Cudd_bddSetPairIndex", "cdecl")
    Cudd_bddSetPairIndex.argtypes = [POINTER(DdManager), c_int, c_int]
    Cudd_bddSetPairIndex.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 960
if _libs["libcudd-3.0.0.so"].has("Cudd_bddReadPairIndex", "cdecl"):
    Cudd_bddReadPairIndex = _libs["libcudd-3.0.0.so"].get("Cudd_bddReadPairIndex", "cdecl")
    Cudd_bddReadPairIndex.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddReadPairIndex.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 961
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSetVarToBeGrouped", "cdecl"):
    Cudd_bddSetVarToBeGrouped = _libs["libcudd-3.0.0.so"].get("Cudd_bddSetVarToBeGrouped", "cdecl")
    Cudd_bddSetVarToBeGrouped.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddSetVarToBeGrouped.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 962
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSetVarHardGroup", "cdecl"):
    Cudd_bddSetVarHardGroup = _libs["libcudd-3.0.0.so"].get("Cudd_bddSetVarHardGroup", "cdecl")
    Cudd_bddSetVarHardGroup.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddSetVarHardGroup.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 963
if _libs["libcudd-3.0.0.so"].has("Cudd_bddResetVarToBeGrouped", "cdecl"):
    Cudd_bddResetVarToBeGrouped = _libs["libcudd-3.0.0.so"].get("Cudd_bddResetVarToBeGrouped", "cdecl")
    Cudd_bddResetVarToBeGrouped.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddResetVarToBeGrouped.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 964
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsVarToBeGrouped", "cdecl"):
    Cudd_bddIsVarToBeGrouped = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsVarToBeGrouped", "cdecl")
    Cudd_bddIsVarToBeGrouped.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddIsVarToBeGrouped.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 965
if _libs["libcudd-3.0.0.so"].has("Cudd_bddSetVarToBeUngrouped", "cdecl"):
    Cudd_bddSetVarToBeUngrouped = _libs["libcudd-3.0.0.so"].get("Cudd_bddSetVarToBeUngrouped", "cdecl")
    Cudd_bddSetVarToBeUngrouped.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddSetVarToBeUngrouped.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 966
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsVarToBeUngrouped", "cdecl"):
    Cudd_bddIsVarToBeUngrouped = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsVarToBeUngrouped", "cdecl")
    Cudd_bddIsVarToBeUngrouped.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddIsVarToBeUngrouped.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 967
if _libs["libcudd-3.0.0.so"].has("Cudd_bddIsVarHardGroup", "cdecl"):
    Cudd_bddIsVarHardGroup = _libs["libcudd-3.0.0.so"].get("Cudd_bddIsVarHardGroup", "cdecl")
    Cudd_bddIsVarHardGroup.argtypes = [POINTER(DdManager), c_int]
    Cudd_bddIsVarHardGroup.restype = c_int

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 66
try:
    CUDD_TRUE = 1
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 67
try:
    CUDD_FALSE = 0
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 72
try:
    CUDD_OUT_OF_MEM = (-1)
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 74
try:
    CUDD_UNIQUE_SLOTS = 256
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 75
try:
    CUDD_CACHE_SLOTS = 262144
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 78
try:
    CUDD_RESIDUE_DEFAULT = 0
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 79
try:
    CUDD_RESIDUE_MSB = 1
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 80
try:
    CUDD_RESIDUE_TC = 2
except:
    pass

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 293
def Cudd_Not(node):
    return cast(((uintptr_t (ord_if_char(node))).value ^ (uintptr_t (ord_if_char(1))).value), POINTER(DdNode))

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 308
def Cudd_NotCond(node, c):
    return cast(((uintptr_t (ord_if_char(node))).value ^ (uintptr_t (ord_if_char(c))).value), POINTER(DdNode))

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 321
def Cudd_Regular(node):
    return cast(((uintptr_t (ord_if_char(node))).value & (~(uintptr_t (ord_if_char(1))).value)), POINTER(DdNode))

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 334
def Cudd_Complement(node):
    return cast(((uintptr_t (ord_if_char(node))).value | (uintptr_t (ord_if_char(1))).value), POINTER(DdNode))

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 347
def Cudd_IsComplement(node):
    return (c_int (ord_if_char(((uintptr_t (ord_if_char(node))).value & (uintptr_t (ord_if_char(1))).value)))).value

# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 363
def Cudd_ReadIndex(dd, index):
    return (Cudd_ReadPerm (dd, index))

DdNode = struct_DdNode# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 194

DdManager = struct_DdManager# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 204

DdGen = struct_DdGen# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 209

DdTlcInfo = struct_DdTlcInfo# /home/juanlu/od/copi_seg/work/programacion/BDD/NativeCudd/ctypes/cudd.h: 229

# No inserted files

# No prefix-stripping

