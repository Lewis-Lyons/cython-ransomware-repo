# cython: infer_types=True
# cython: language_level=3
# cython: embedsignature=True
# cython: boundscheck=False
# coding: utf8

from libc.stdlib cimport malloc, realloc, free
from libc.stdio cimport fopen, fclose, FILE, EOF, fseek, SEEK_END, SEEK_SET
from libc.stdio cimport ftell, fgetc, fgets, getc, gets, feof, fread, getline
from libc.string cimport strlen, memcpy, strcpy, strtok, strchr, strncpy
from cython.parallel cimport prange, parallel, threadid

# - C structure that is set to readonly
cdef readonly struct FileContents:
    char *contents

cdef class CyReadFile:
    """Read in the contents of a file."""
    cdef:
        FileContents *File
        FILE *fp
        char *filename
        char *delimiter
        long file_size
        bint is_open
        bint EO_STR


    def __init__(self, char *delimiter, char *filename):
        self.File = <FileContents*>malloc(sizeof(CyReadFile))
        self.delimiter = delimiter
        self.filename = filename
        self.File.contents = NULL
        self.is_open = 0
        self.EO_STR = 0
        self.file_size = 0
        self.fp = NULL

    def open_file(self):
        """Open the file for reading."""
        self.fp = fopen(self.filename, "rb")
        if self.fp == NULL:
            raise FileNotFoundError(2, "No such file or directory: '%s'" % self.filename)
        else:
            # file is now open
            self.is_open = 1

    def read_in_file(self):
        """Read in the entire file."""
        if self.is_open == 1:
            # get the length of the file
            fseek(self.fp, 0, SEEK_END)
            self.file_size = ftell(self.fp)
            fseek(self.fp, 0, SEEK_SET)
            # allocate memory for reading in the file
            self.File.contents = <char*>malloc(self.file_size*sizeof(char))
            # read entire file into the struct
            fread(self.File.contents, 1, self.file_size, self.fp)
            # Due to Cython conventions, by asigning the variable self.File.contents to the native python variable holder,Python recieves an automaticlly compatible type from Cython.
            holder = self.File.contents
            #return holder
            # close the file once it's read into the char array
            fclose(self.fp)
            # set is_open to 0
            self.is_open = 0
            return holder

    def read_file_in_parallel(self):
        """Bypass the gil and read in the file."""
        if self.is_open == 1:
            with nogil:
                # get the length of the file
                fseek(self.fp, 0, SEEK_END)
                self.file_size = ftell(self.fp)
                fseek(self.fp, 0, SEEK_SET)
                # allocate memory for reading in the file
                self.File.contents = <char*>malloc(self.file_size*sizeof(char))
                # read entire file into the struct
                fread(self.File.contents, 1, self.file_size, self.fp)
                # close the file once it's read into the char array
                fclose(self.fp)
                # set is_open to 0
                self.is_open = 0

    def __dealloc__(self):
        """Deallocate memory"""
        free(self.File.contents)
        free(self.File)
        free(self.fp)
        free(self.filename)
        free(self.delimiter)


# - To use the cython class, we must create a python subclass that inherits from it.
# - I will set the cython variables concretely in the Python subclass

# test data
File = b"C:\\Users\\User\\Music\\file1.txt"

class PyReadFile(CyReadFile):
    """A python wrapper around a cython class."""
    def __init__(self):
        super().__init__(b',', File)


def py_read_file(filename):
    with open(filename, "r") as f:
        return f.read()
