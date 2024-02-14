/*
* FILENAME: BDDlab.c
* Overview: utilidades para BDD
* AUTHOR:  jgzapata, a partir de un tutorial de David Kebo Houngninou
*/

#include <sys/types.h>
#include <sys/time.h>
#include <stdio.h>
#include <string.h>
#include <time.h>
#include <math.h>
#include <stdlib.h>
#include "cudd.h"
#include "cuddInt.h"
#include "util.h"




/***
 ***
 * 
 * 
 * Funciones de acceso a implementación CUDD
 * 
 ***
 ***/

DdNode * My_Cudd_Not(DdNode * node) {
  DdNode * NoNode;
  NoNode = Cudd_Not(node);
  return NoNode;
//   DdNode TheNode = *node;
//   TheNode = &Cudd_Not(node);
//   return TheNode;
}

//  requiere cuddInt.h, que define DdNode
// tiene que ser un puntero regular (con libBDDlab.My_Regular vale)
int indiceVar(DdNode * node){
   return (int) node->index;
}

int My_IsComplemented(DdNode * node) {
   
   return Cudd_IsComplement(node);
}

DdNode *  My_Regular(DdNode * node) {
   
   return Cudd_Regular(node);
}


int My_IsConstant(DdNode * node) {
   
   return Cudd_IsConstant(node);
}

DdNode * My_Cudd_NotCond(DdNode * node, int c) {
   
   return Cudd_NotCond(node,c);
}





/***
 *** 
 * 
 * 
 * Funciones de consulta
 * 
 * 
 ***
 ***/

/**
 * Print a dd summmary
 * pr = 0 : prints nothing
 * pr = 1 : prints counts of nodes and minterms
 * pr = 2 : prints counts + disjoint sum of product
 * pr = 3 : prints counts + list of nodes
 * pr > 3 : prints counts + disjoint sum of product + list of nodes
 * @param the dd node
 */
void print_dd (DdManager *gbm, DdNode	*dd, int n, int pr )
{
    printf("DdManager nodes: %ld | ", Cudd_ReadNodeCount(gbm)); /*Reports the number of live nodes in BDDs and ADDs*/
    printf("DdManager vars: %d | ", Cudd_ReadSize(gbm) ); /*Returns the number of BDD variables in existance*/
    printf("DdManager reorderings: %d | ", Cudd_ReadReorderings(gbm) ); /*Returns the number of times reordering has occurred*/
    printf("DdManager memory: %ld \n", Cudd_ReadMemoryInUse(gbm) ); /*Returns the memory in use by the manager measured in bytes*/
    Cudd_PrintDebug(gbm, dd, n, pr);	// Prints to the standard output a DD and its statistics: number of nodes, number of leaves, number of minterms.
}


/**
 * Writes a dot file representing the argument DDs
 * @param the node object
 */
void write_dd (DdManager *gbm, DdNode	*dd, char* filename)
{
    FILE *outfile; // output file pointer for .dot file
    outfile = fopen(filename,"w");
    DdNode **ddnodearray = (DdNode**)malloc(sizeof(DdNode*)); // initialize the function array
    ddnodearray[0] = dd;
    Cudd_DumpDot(gbm, 1, ddnodearray, NULL, NULL, outfile);	// dump the function to .dot file
    free(ddnodearray);
    fclose (outfile); // close the file */
}

/**
 * 
 * Ajusta la salida a un fichero
 * 
 * 
 */
void setOutput(DdManager *gbm, char* filename)
{
    FILE *archivo = fopen(filename, "w");
    if (archivo == NULL) {
        printf("Error al abrir el archivo\n");
        return;
    }
    gbm->out = archivo;    
}

void closeOutput(DdManager *gbm) {
   fclose(gbm->out);
}

void My_Cudd_PrintInfo(DdManager *gbm) {
  setOutput(gbm,"tempo.txt");
  Cudd_PrintInfo(gbm,gbm->out);
  closeOutput(gbm);
}


/**
 * 
 * interfaz a Cudd_BddToCubeArray, a ver si así puedo
 * 
 *
int MyBddToCubeArray (DdManager *gbm, DdNode	*dd, int * vars, int n)
{
   Cudd_BddToCubeArray(

*/





/***
 ***
 *
 * Funciones replicadas para trastear
 * 
 ***
 ***/



/**
  @brief Selects pairs from R using a priority function.

  @details Selects pairs from a relation R(x,y) (given as a %BDD)
  in such a way that a given x appears in one pair only. Uses a
  priority function to determine which y should be paired to a given x.
  Three of the arguments--x, y, and z--are vectors of %BDD variables.
  The first two are the variables on which R depends. The third vector
  is a vector of auxiliary variables, used during the computation. This
  vector is optional. If a NULL value is passed instead,
  Cudd_PrioritySelect will create the working variables on the fly.
  The sizes of x and y (and z if it is not NULL) should equal n.
  The priority function Pi can be passed as a %BDD, or can be built by
  Cudd_PrioritySelect. If NULL is passed instead of a DdNode *,
  parameter Pifunc is used by Cudd_PrioritySelect to build a %BDD for the
  priority function. (Pifunc is a pointer to a C function.) If Pi is not
  NULL, then Pifunc is ignored. Pifunc should have the same interface as
  the standard priority functions (e.g., Cudd_Dxygtdxz).
  Cudd_PrioritySelect and Cudd_CProjection can sometimes be used
  interchangeably. Specifically, calling Cudd_PrioritySelect with
  Cudd_Xgty as Pifunc produces the same result as calling
  Cudd_CProjection with the all-zero minterm as reference minterm.
  However, depending on the application, one or the other may be
  preferable:
  <ul>
  <li> When extracting representatives from an equivalence relation,
  Cudd_CProjection has the advantage of nor requiring the auxiliary
  variables.
  <li> When computing matchings in general bipartite graphs,
  Cudd_PrioritySelect normally obtains better results because it can use
  more powerful matching schemes (e.g., Cudd_Dxygtdxz).
  </ul>

  @return a pointer to the selected function if successful; NULL
  otherwise.

  @sideeffect If called with z == NULL, will create new variables in
  the manager.

  @see Cudd_Dxygtdxz Cudd_Dxygtdyz Cudd_Xgty
  Cudd_bddAdjPermuteX Cudd_CProjection

*/
DdNode *
MyCudd_PrioritySelect(
  DdManager * dd /**< manager */,
  DdNode * R /**< %BDD of the relation */,
  DdNode ** x /**< array of x variables */,
  DdNode ** y /**< array of y variables */,
  DdNode ** z /**< array of z variables (optional: may be NULL) */,
  DdNode * Pi /**< %BDD of the priority function (optional: may be NULL) */,
  int  n /**< size of x, y, and z */,
  DD_PRFP Pifunc /**< function used to build Pi if it is NULL */)
{
    DdNode *res = NULL;
    DdNode *zcube = NULL;
    DdNode *Rxz, *Q;
    int createdZ = 0;
    int createdPi = 0;
    int i;

    /* Create z variables if needed. */
    if (z == NULL) {
       printf("---> z es null\n");
	if (Pi != NULL) {printf("---> Pi no es null\n");return(NULL);}
	z = ALLOC(DdNode *,n);
	if (z == NULL) {
	    dd->errorCode = CUDD_MEMORY_OUT;
	    return(NULL);
	}
	createdZ = 1;
	for (i = 0; i < n; i++) {
	    if (dd->size >= (int) CUDD_MAXINDEX - 1) goto endgame;
	    z[i] = cuddUniqueInter(dd,dd->size,dd->one,Cudd_Not(dd->one));
	    if (z[i] == NULL) goto endgame;
	}
    }

    /* Create priority function BDD if needed. */
    if (Pi == NULL) {
	Pi = Pifunc(dd,n,x,y,z);
	if (Pi == NULL) goto endgame;
	createdPi = 1;
	cuddRef(Pi);
    }

    /* Initialize abstraction cube. */
    zcube = DD_ONE(dd);
    cuddRef(zcube);
    for (i = n - 1; i >= 0; i--) {
	DdNode *tmpp;
	tmpp = Cudd_bddAnd(dd,z[i],zcube);
	if (tmpp == NULL) goto endgame;
	cuddRef(tmpp);
	Cudd_RecursiveDeref(dd,zcube);
	zcube = tmpp;
    }
    
    /* Compute subset of (x,y) pairs. */
    Rxz = Cudd_bddSwapVariables(dd,R,y,z,n);

    if (Rxz == NULL) goto endgame;
    cuddRef(Rxz);

    Q = Cudd_bddAndAbstract(dd,Rxz,Pi,zcube);

    if (Q == NULL) {
	Cudd_RecursiveDeref(dd,Rxz);
	goto endgame;
    }

    cuddRef(Q);
    Cudd_RecursiveDeref(dd,Rxz);
    res = Cudd_bddAnd(dd,R,Cudd_Not(Q));
    if (res == NULL) {
	Cudd_RecursiveDeref(dd,Q);
	goto endgame;
    }

    cuddRef(res);
    Cudd_RecursiveDeref(dd,Q);

    
endgame:
    if (zcube != NULL) Cudd_RecursiveDeref(dd,zcube);
    if (createdZ) {
	FREE(z);
    }
    if (createdPi) {
	Cudd_RecursiveDeref(dd,Pi);
    }
    if (res != NULL) cuddDeref(res);
    return(res);

} /* Cudd_PrioritySelect */


// int main (int argc, char *argv[])
// {
//     char filename[30];
//     DdManager *gbm;	/* Global BDD manager. */
//     gbm = Cudd_Init(0,0,CUDD_UNIQUE_SLOTS,CUDD_CACHE_SLOTS,0); /* Initialize a new BDD manager. */
//     DdNode *bdd, *var, *tmp_neg, *tmp;
//     int i, j, miarr[8] = {1,0,1,1,1,0,1,1};
//     srand(semilla);
//   
//     bdd = Cudd_ReadOne(gbm); /*Returns the logic one constant of the manager*/
//     Cudd_Ref(bdd); /*Increases the reference count of a node*/
// 
//     for (i = 8; i >= 0; i--) {
//         var = Cudd_bddIthVar(gbm,i); /*Create a new BDD variable*/
//         tmp_neg = Cudd_Not(var); /*Perform NOT boolean operation*/
//         if (i%2 == 0)
//            tmp = Cudd_bddAnd(gbm, tmp_neg, bdd); /*Perform AND boolean operation*/
//         else
//            tmp = Cudd_bddOr(gbm, tmp_neg, bdd); /*Perform or boolean operation*/
//         Cudd_Ref(tmp);
//         Cudd_RecursiveDeref(gbm,bdd);
//         bdd = tmp;
//     }
//     
//     
//     for (i = 8; i >= 0; i--) {
//       var = Cudd_bddIthVar(gbm,i); /*Create a new BDD variable*/
//     }
//   
//         /* un minterm al azar */
//       for (i = 0; i < 8; i++) {
//         miarr[i] = rand() % 2;
//       }
//       tmp = Cudd_CubeArrayToBdd(gbm, miarr);
//       Cudd_Ref(tmp);
//       
//       Cudd_RecursiveDeref(gbm,bdd);
//       bdd = tmp;
//     
//     int numMinterm = 128;
//     for (j = 0; j < numMinterm -1; j++) {
//       /* otro minterm al azar */
//       for (i = 0; i < 8; i++) {
//         miarr[i] = rand() % 2;
//       }
//       tmp = Cudd_CubeArrayToBdd(gbm, miarr);
//       Cudd_Ref(tmp);
//       
//       Cudd_RecursiveDeref(gbm,bdd);
//       bdd = Cudd_bddOr(gbm, tmp, bdd);
// 
//     }
//     
//        
//     /* añadir el mintern de miarr */
//     tmp = Cudd_CubeArrayToBdd(gbm, miarr);
//     Cudd_Ref(tmp);
//     Cudd_RecursiveDeref(gbm,bdd);
//     bdd = tmp;
// 
//     bdd = Cudd_BddToAdd(gbm, bdd); /*Convert BDD to ADD for display purpose*/
//     print_dd (gbm, bdd, 2,4);	/*Print the dd to standard output*/
//     sprintf(filename, "./bdd/graph.dot"); /*Write .dot filename to a string*/
//     write_dd(gbm, bdd, filename);  /*Write the resulting cascade dd to a file*/
//     Cudd_Quit(gbm);
//     return 0;
// }
