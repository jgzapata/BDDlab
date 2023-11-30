libcudd.Cudd_Init.restype = POINTER(DdManager)
libcudd.Cudd_ReadOne.argtypes = POINTER(DdManager),
libcudd.Cudd_ReadOne.restype = POINTER(DdNode)
libcudd.Cudd_ReadZero.argtypes = POINTER(DdManager),
libcudd.Cudd_ReadZero.restype = POINTER(DdNode)
libcudd.Cudd_ReadLogicZero.argtypes = POINTER(DdManager),
libcudd.Cudd_ReadLogicZero.restype = POINTER(DdNode)
libcudd.Cudd_Ref.argtypes = POINTER(DdNode),
libcudd.Cudd_Ref.restype = None
libcudd.Cudd_bddIthVar.argtypes = POINTER(DdManager), ctypes.c_int
libcudd.Cudd_bddIthVar.restype = POINTER(DdNode)
libcudd.Cudd_ReadVars.argtypes = POINTER(DdManager), ctypes.c_int
libcudd.Cudd_ReadVars.restype = POINTER(DdNode)
# resulta que sí es una macro, y a veces da problemas, porejemplo si el bdd es parte de una estructura
libcudd.Cudd_IsConstant.argtypes = POINTER(DdNode),
libcudd.Cudd_IsConstant.restype = ctypes.c_int
libcudd.Cudd_ReadPerm.argtypes = POINTER(DdManager), ctypes.c_int
libcudd.Cudd_ReadPerm.restype = ctypes.c_int



libcudd.Cudd_RecursiveDeref.argtypes = POINTER(DdManager), POINTER(DdNode)
libcudd.Cudd_RecursiveDeref.restype = None
libcudd.Cudd_BddToAdd.restype = POINTER(DdNode)
#libcudd.Cudd_PrintDebug.restype
#libcudd.Cudd_DumpDot.restype = 
libcudd.Cudd_bddOr.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddOr.restype = POINTER(DdNode)
libcudd.Cudd_bddAnd.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddAnd.restype = POINTER(DdNode)
libcudd.Cudd_bddXor.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddXor.restype = POINTER(DdNode)
libcudd.Cudd_bddXnor.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddXnor.restype = POINTER(DdNode)
libcudd.Cudd_bddIte.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddIte.restype = POINTER(DdNode)
libcudd.Cudd_Eval.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(ctypes.c_int)
libcudd.Cudd_Eval.restype = POINTER(DdNode)
#libcudd.Cudd_Eval.restype = ctypes.c_int

#CUDD_VALUE_TYPE # double, exported by cudd.py

libcudd.Cudd_bddExistAbstract.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddExistAbstract.restype = POINTER(DdNode)
libcudd.Cudd_bddUnivAbstract.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddUnivAbstract.restype = POINTER(DdNode)

libcudd.Cudd_bddCompose.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode), ctypes.c_int
libcudd.Cudd_bddCompose.restype = POINTER(DdNode) 
libcudd.Cudd_bddLeq.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddLeq.restype = ctypes.c_int 
libcudd.Cudd_Xeqy.argtypes = POINTER(DdManager), ctypes.c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode))
libcudd.Cudd_Xeqy.restype = POINTER(DdNode) 



libcudd.Cudd_IndicesToCube.argtypes = POINTER(DdManager), POINTER(ctypes.c_int), ctypes.c_int
libcudd.Cudd_IndicesToCube.restype = POINTER(DdNode) 
#libcudd.Cudd_CubeArrayToBdd.argtypes = POINTER(DdManager), POINTER(ctypes.c_int)  <-- no funciona, por alguna razón
libcudd.Cudd_CubeArrayToBdd.restype = POINTER(DdNode)
libcudd.Cudd_bddExistAbstract.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_bddExistAbstract.restype = POINTER(DdNode)
libcudd.Cudd_Cofactor.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(DdNode)
libcudd.Cudd_Cofactor.restype = POINTER(DdNode)
libcudd.Cudd_bddSwapVariables.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), ctypes.c_int 
libcudd.Cudd_bddSwapVariables.restype = POINTER(DdNode)
libcudd.Cudd_bddVectorCompose.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)) 
libcudd.Cudd_bddVectorCompose.restype = POINTER(DdNode)
#libcudd.Cudd_BddToCubeArray.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(ctypes.c_int)  <-- no funciona, por alguna razón relacinada con lo antior
libcudd.Cudd_BddToCubeArray.restype = ctypes.c_int
libcudd.Cudd_Support.argtypes = POINTER(DdManager), POINTER(DdNode),
libcudd.Cudd_Support.restype = POINTER(DdNode)
libcudd.Cudd_NodeReadIndex.argtypes = POINTER(DdNode),
libcudd.Cudd_NodeReadIndex.restype = ctypes.c_uint
libcudd.Cudd_ReadSize.argtypes = POINTER(DdManager),
libcudd.Cudd_ReadSize.restype = ctypes.c_int


libcudd.Cudd_FirstNode.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)) 
libcudd.Cudd_FirstNode.restype = POINTER(DdGen)
libcudd.Cudd_IsGenEmpty.argtypes = POINTER(DdGen), 
libcudd.Cudd_IsGenEmpty.restype =  ctypes.c_int
libcudd.Cudd_GenFree.argtypes = POINTER(DdGen), 
libcudd.Cudd_GenFree.restype =  ctypes.c_int
libcudd.Cudd_NextNode.argtypes = POINTER(DdGen),  POINTER(POINTER(DdNode))
libcudd.Cudd_NextNode.restype =  ctypes.c_int

libcudd.Cudd_CProjection.argtypes =  POINTER(DdManager), POINTER(DdNode), POINTER(DdNode),
libcudd.Cudd_CProjection.restype =  POINTER(DdNode)
libcudd.Cudd_PrioritySelect.argtypes =  POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(DdNode), ctypes.c_int , #aqui iría un puntero a función que no se poner en ctypes
libcudd.Cudd_PrioritySelect.restype =  POINTER(DdNode)
libcudd.Cudd_Xgty.argtypes =  POINTER(DdManager), ctypes.c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), 
libcudd.Cudd_Xgty.restype =  POINTER(DdNode)
libcudd.Cudd_Dxygtdxz.argtypes =  POINTER(DdManager), ctypes.c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), 
libcudd.Cudd_Dxygtdxz.restype =  POINTER(DdNode)
libcudd.Cudd_Dxygtdyz.argtypes =  POINTER(DdManager), ctypes.c_int, POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), POINTER(POINTER(DdNode)), 
libcudd.Cudd_Dxygtdyz.restype =  POINTER(DdNode)


# Cudd_Not es una macro   c_double
#libcudd.Cudd_Not.argtypes = POINTER(DdNode)
#libcudd.Cudd_Not.restype = POINTER(DdNode)
# Cudd_V no es una macro

libcudd.Cudd_T.argtypes = POINTER(DdNode),  
libcudd.Cudd_T.restype = POINTER(DdNode)
libcudd.Cudd_E.argtypes = POINTER(DdNode),  
libcudd.Cudd_E.restype = POINTER(DdNode)
libcudd.Cudd_V.argtypes = POINTER(DdNode),  
libcudd.Cudd_V.restype = ctypes.c_double


libcudd.Cudd_bddPickOneMinterm.argtypes = POINTER(DdManager), POINTER(DdNode), POINTER(POINTER(DdNode)), ctypes.c_int, 
libcudd.Cudd_bddPickOneMinterm.restype = POINTER(DdNode)


libcudd.Cudd_ReduceHeap.argtypes = POINTER(DdManager), Cudd_ReorderingType , ctypes.c_int 
libcudd.Cudd_ReduceHeap.restype = ctypes.c_int 
libcudd.Cudd_CheckZeroRef.argtypes = POINTER(DdManager),
libcudd.Cudd_addBddPattern.argtypes = POINTER(DdManager), POINTER(DdNode)
libcudd.Cudd_addBddPattern.restype = POINTER(DdNode)

libcudd.Cudd_DagSize.argtypes = POINTER(DdNode),
libcudd.Cudd_DagSize.restype = ctypes.c_int 
libcudd.Cudd_CountLeaves.argtypes = POINTER(DdNode),
libcudd.Cudd_CountLeaves.restype = ctypes.c_int 
libcudd.Cudd_CountMinterm.argtypes = POINTER(DdManager), POINTER(DdNode), ctypes.c_int 
libcudd.Cudd_CountMinterm.restype = ctypes.c_double
libcudd.Cudd_CountPath.argtypes = POINTER(DdNode), 
libcudd.Cudd_CountPath.restype = ctypes.c_double
libcudd.Cudd_CountPathsToNonZero.argtypes = POINTER(DdNode), 
libcudd.Cudd_CountPathsToNonZero.restype = ctypes.c_double
libcudd.Cudd_CountLeaves.argtypes = POINTER(DdNode), 
libcudd.Cudd_CountLeaves.restype = ctypes.c_int
libcudd.Cudd_PrintMinterm.argtypes = POINTER(DdManager), POINTER(DdNode), 
libcudd.Cudd_PrintMinterm.restype = ctypes.c_int

libcudd.Cudd_AutodynDisable.argtypes = POINTER(DdManager), 
libcudd.Cudd_AutodynDisable.restype = None

libcudd.Cudd_ShuffleHeap.argtypes = POINTER(DdManager), POINTER(ctypes.c_int)
libcudd.Cudd_ShuffleHeap.restype = ctypes.c_int
 
