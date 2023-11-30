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
