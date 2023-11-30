 
libBDDlab.print_dd.argtypes = POINTER(DdManager), POINTER(DdNode), ctypes.c_int, ctypes.c_int

libBDDlab.write_dd.argtypes = POINTER(DdManager), POINTER(DdNode), ctypes.c_char_p

libBDDlab.My_Cudd_Not.argtypes = POINTER(DdNode),
libBDDlab.My_Cudd_Not.restype = POINTER(DdNode)
libBDDlab.indiceVar.argtypes = POINTER(DdNode),
libBDDlab.indiceVar.restype = ctypes.c_int

libBDDlab.My_IsComplemented.argtypes = POINTER(DdNode),
libBDDlab.My_IsComplemented.restype = ctypes.c_int
libBDDlab.My_IsConstant.argtypes = POINTER(DdNode),
libBDDlab.My_IsConstant.restype = ctypes.c_int
libBDDlab.My_Regular.argtypes = POINTER(DdNode),
libBDDlab.My_Regular.restype = POINTER(DdNode)



#libBDDlab.MyCudd_PrioritySelect.argtypes =  POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(DdNode), ctypes.c_int , #aqui iría un puntero a función que no se poner en ctypes
#libBDDlab.MyCudd_PrioritySelect.restype =  POINTER(DdNode)

from IPython.display import Image, display
