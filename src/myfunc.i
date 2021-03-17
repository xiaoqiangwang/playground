%module myfunc

%{
#define SWIG_FILE_WITH_INIT
#include "myfunc.h"
%}

int add_two(int a);
