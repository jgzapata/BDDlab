# Project: BDDlab
# Makefile created a mano


all: BDDlab.o libBDDlab.so

BDDlab.o: BDDlab.c
	gcc *.c -c -fPIC

libBDDlab.so: BDDlab.o
	gcc *.o -shared -o libBDDlab.so -L. -lcudd
















#### viejo de ejemplo:

# CC   = gcc
# 
# RES  = 
# OBJ  = BDDlab.o $(RES)
# LINKOBJ  = gb2dot.o ../../SGB/sgb/gb_basic.o ../../SGB/sgb/gb_graph.o ../../SGB/sgb/gb_save.o ../../SGB/sgb/gb_io.o $(RES)
# LIBS =  -L"lib" -L"C:/Dev-Cpp/lib"  
# INCS =  -I"C:/Dev-Cpp/include" 
# CXXINCS =  -I"lib/gcc/mingw32/3.4.2/include"  -I"include/c++/3.4.2/backward"  -I"include/c++/3.4.2/mingw32"  -I"include/c++/3.4.2"  -I"include" 
# BIN  = gb2dot
# CXXFLAGS = $(CXXINCS)   -Wall -w
# CFLAGS = $(INCS) -I../../SGB/sgb -Wall   -Wall -w
# RM = rm -f
# 
# .PHONY: all all-before all-after clean clean-custom
# 
# all: all-before gb2dot all-after
# 
# 
# clean: clean-custom
# 	${RM} $(OBJ) $(BIN)
# 
# $(BIN): $(OBJ)
# 	$(CC) $(LINKOBJ) -o "gb2dot" $(LIBS)
# 
# gb2dot.o: gb2dot.c
# 	$(CC) -c gb2dot.c -o gb2dot.o $(CFLAGS)
# 
# ../../sgb/gb_basic.o: ../../sgb/gb_basic.c
# 	$(CC) -c ../../sgb/gb_basic.c -o ../../sgb/gb_basic.o $(CFLAGS)
# 
# ../../sgb/gb_graph.o: ../../sgb/gb_graph.c
# 	$(CC) -c ../../sgb/gb_graph.c -o ../../sgb/gb_graph.o $(CFLAGS)
# 
# ../../sgb/gb_save.o: ../../sgb/gb_save.c
# 	$(CC) -c ../../sgb/gb_save.c -o ../../sgb/gb_save.o $(CFLAGS)
# 
# ../../sgb/gb_io.o: ../../sgb/gb_io.c
# 	$(CC) -c ../../sgb/gb_io.c -o ../../sgb/gb_io.o $(CFLAGS)
