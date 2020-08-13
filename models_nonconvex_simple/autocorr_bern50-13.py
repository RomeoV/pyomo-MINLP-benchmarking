#  MINLP written by GAMS Convert at 08/13/20 17:37:51
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         51        1       50        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         51        1       50        0


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x51, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*
                       m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*
                       m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b4*m.b5*
                       m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*
                       m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*
                       m.b1*m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*
                       m.b13 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*m.b2*
                       m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 128*m.b2*m.b3*m.b10*m.b11
                        + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*m.b12*m.b13 + 64*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*
                       m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 
                       128*m.b2*m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 64*m.b2*m.b4*
                       m.b12*m.b14 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10 + 128*m.b2*m.b5*m.b8*m.b11 + 128
                       *m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 64*m.b2*m.b5*m.b11*m.b14 + 128*m.b2*m.b6*m.b7
                       *m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 64*m.b2*m.b6*m.b10*m.b14 + 128*
                       m.b2*m.b7*m.b8*m.b13 + 64*m.b2*m.b7*m.b9*m.b14 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*
                       m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*
                       m.b4*m.b10*m.b11 + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 128*m.b3*m.b4*m.b13*
                       m.b14 + 64*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*
                       m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*m.b5*m.b10*m.b12 + 192*m.b3*m.b5*m.b11*
                       m.b13 + 128*m.b3*m.b5*m.b12*m.b14 + 64*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b6*m.b7*m.b10 + 192*
                       m.b3*m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13 + 128*m.b3*m.b6*m.b11
                       *m.b14 + 64*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*m.b13 + 128*
                       m.b3*m.b7*m.b10*m.b14 + 64*m.b3*m.b7*m.b11*m.b15 + 128*m.b3*m.b8*m.b9*m.b14 + 64*m.b3*m.b8*m.b10*
                       m.b15 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4*m.b5*m.b8*m.b9 + 256*m.b4*
                       m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*m.b12 + 256*m.b4*m.b5*m.b12*
                       m.b13 + 192*m.b4*m.b5*m.b13*m.b14 + 128*m.b4*m.b5*m.b14*m.b15 + 64*m.b4*m.b5*m.b15*m.b16 + 256*
                       m.b4*m.b6*m.b7*m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 256*m.b4*m.b6*m.b10*
                       m.b12 + 256*m.b4*m.b6*m.b11*m.b13 + 192*m.b4*m.b6*m.b12*m.b14 + 128*m.b4*m.b6*m.b13*m.b15 + 64*
                       m.b4*m.b6*m.b14*m.b16 + 256*m.b4*m.b7*m.b8*m.b11 + 256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7*m.b10
                       *m.b13 + 192*m.b4*m.b7*m.b11*m.b14 + 128*m.b4*m.b7*m.b12*m.b15 + 64*m.b4*m.b7*m.b13*m.b16 + 256*
                       m.b4*m.b8*m.b9*m.b13 + 192*m.b4*m.b8*m.b10*m.b14 + 128*m.b4*m.b8*m.b11*m.b15 + 64*m.b4*m.b8*m.b12
                       *m.b16 + 128*m.b4*m.b9*m.b10*m.b15 + 64*m.b4*m.b9*m.b11*m.b16 + 320*m.b5*m.b6*m.b7*m.b8 + 320*
                       m.b5*m.b6*m.b8*m.b9 + 320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*m.b11 + 320*m.b5*m.b6*m.b11*
                       m.b12 + 320*m.b5*m.b6*m.b12*m.b13 + 256*m.b5*m.b6*m.b13*m.b14 + 192*m.b5*m.b6*m.b14*m.b15 + 128*
                       m.b5*m.b6*m.b15*m.b16 + 64*m.b5*m.b6*m.b16*m.b17 + 320*m.b5*m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*
                       m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*m.b13 + 256*m.b5*m.b7*m.b12*m.b14 + 192*
                       m.b5*m.b7*m.b13*m.b15 + 128*m.b5*m.b7*m.b14*m.b16 + 64*m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b8*m.b9
                       *m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 256*m.b5*m.b8*m.b11*m.b14 + 192*m.b5*m.b8*m.b12*m.b15 + 128*
                       m.b5*m.b8*m.b13*m.b16 + 64*m.b5*m.b8*m.b14*m.b17 + 256*m.b5*m.b9*m.b10*m.b14 + 192*m.b5*m.b9*
                       m.b11*m.b15 + 128*m.b5*m.b9*m.b12*m.b16 + 64*m.b5*m.b9*m.b13*m.b17 + 128*m.b5*m.b10*m.b11*m.b16
                        + 64*m.b5*m.b10*m.b12*m.b17 + 384*m.b6*m.b7*m.b8*m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7
                       *m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 384*m.b6*m.b7*m.b12*m.b13 + 320*m.b6*m.b7*m.b13*m.b14
                        + 256*m.b6*m.b7*m.b14*m.b15 + 192*m.b6*m.b7*m.b15*m.b16 + 128*m.b6*m.b7*m.b16*m.b17 + 64*m.b6*
                       m.b7*m.b17*m.b18 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*
                       m.b13 + 320*m.b6*m.b8*m.b12*m.b14 + 256*m.b6*m.b8*m.b13*m.b15 + 192*m.b6*m.b8*m.b14*m.b16 + 128*
                       m.b6*m.b8*m.b15*m.b17 + 64*m.b6*m.b8*m.b16*m.b18 + 384*m.b6*m.b9*m.b10*m.b13 + 320*m.b6*m.b9*
                       m.b11*m.b14 + 256*m.b6*m.b9*m.b12*m.b15 + 192*m.b6*m.b9*m.b13*m.b16 + 128*m.b6*m.b9*m.b14*m.b17
                        + 64*m.b6*m.b9*m.b15*m.b18 + 256*m.b6*m.b10*m.b11*m.b15 + 192*m.b6*m.b10*m.b12*m.b16 + 128*m.b6*
                       m.b10*m.b13*m.b17 + 64*m.b6*m.b10*m.b14*m.b18 + 128*m.b6*m.b11*m.b12*m.b17 + 64*m.b6*m.b11*m.b13*
                       m.b18 + 448*m.b7*m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*
                       m.b7*m.b8*m.b12*m.b13 + 384*m.b7*m.b8*m.b13*m.b14 + 320*m.b7*m.b8*m.b14*m.b15 + 256*m.b7*m.b8*
                       m.b15*m.b16 + 192*m.b7*m.b8*m.b16*m.b17 + 128*m.b7*m.b8*m.b17*m.b18 + 64*m.b7*m.b8*m.b18*m.b19 + 
                       448*m.b7*m.b9*m.b10*m.b12 + 448*m.b7*m.b9*m.b11*m.b13 + 384*m.b7*m.b9*m.b12*m.b14 + 320*m.b7*m.b9
                       *m.b13*m.b15 + 256*m.b7*m.b9*m.b14*m.b16 + 192*m.b7*m.b9*m.b15*m.b17 + 128*m.b7*m.b9*m.b16*m.b18
                        + 64*m.b7*m.b9*m.b17*m.b19 + 384*m.b7*m.b10*m.b11*m.b14 + 320*m.b7*m.b10*m.b12*m.b15 + 256*m.b7*
                       m.b10*m.b13*m.b16 + 192*m.b7*m.b10*m.b14*m.b17 + 128*m.b7*m.b10*m.b15*m.b18 + 64*m.b7*m.b10*m.b16
                       *m.b19 + 256*m.b7*m.b11*m.b12*m.b16 + 192*m.b7*m.b11*m.b13*m.b17 + 128*m.b7*m.b11*m.b14*m.b18 + 
                       64*m.b7*m.b11*m.b15*m.b19 + 128*m.b7*m.b12*m.b13*m.b18 + 64*m.b7*m.b12*m.b14*m.b19 + 512*m.b8*
                       m.b9*m.b10*m.b11 + 512*m.b8*m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*m.b13 + 448*m.b8*m.b9*m.b13*
                       m.b14 + 384*m.b8*m.b9*m.b14*m.b15 + 320*m.b8*m.b9*m.b15*m.b16 + 256*m.b8*m.b9*m.b16*m.b17 + 192*
                       m.b8*m.b9*m.b17*m.b18 + 128*m.b8*m.b9*m.b18*m.b19 + 64*m.b8*m.b9*m.b19*m.b20 + 512*m.b8*m.b10*
                       m.b11*m.b13 + 448*m.b8*m.b10*m.b12*m.b14 + 384*m.b8*m.b10*m.b13*m.b15 + 320*m.b8*m.b10*m.b14*
                       m.b16 + 256*m.b8*m.b10*m.b15*m.b17 + 192*m.b8*m.b10*m.b16*m.b18 + 128*m.b8*m.b10*m.b17*m.b19 + 64
                       *m.b8*m.b10*m.b18*m.b20 + 384*m.b8*m.b11*m.b12*m.b15 + 320*m.b8*m.b11*m.b13*m.b16 + 256*m.b8*
                       m.b11*m.b14*m.b17 + 192*m.b8*m.b11*m.b15*m.b18 + 128*m.b8*m.b11*m.b16*m.b19 + 64*m.b8*m.b11*m.b17
                       *m.b20 + 256*m.b8*m.b12*m.b13*m.b17 + 192*m.b8*m.b12*m.b14*m.b18 + 128*m.b8*m.b12*m.b15*m.b19 + 
                       64*m.b8*m.b12*m.b16*m.b20 + 128*m.b8*m.b13*m.b14*m.b19 + 64*m.b8*m.b13*m.b15*m.b20 + 576*m.b9*
                       m.b10*m.b11*m.b12 + 576*m.b9*m.b10*m.b12*m.b13 + 512*m.b9*m.b10*m.b13*m.b14 + 448*m.b9*m.b10*
                       m.b14*m.b15 + 384*m.b9*m.b10*m.b15*m.b16 + 320*m.b9*m.b10*m.b16*m.b17 + 256*m.b9*m.b10*m.b17*
                       m.b18 + 192*m.b9*m.b10*m.b18*m.b19 + 128*m.b9*m.b10*m.b19*m.b20 + 64*m.b9*m.b10*m.b20*m.b21 + 512
                       *m.b9*m.b11*m.b12*m.b14 + 448*m.b9*m.b11*m.b13*m.b15 + 384*m.b9*m.b11*m.b14*m.b16 + 320*m.b9*
                       m.b11*m.b15*m.b17 + 256*m.b9*m.b11*m.b16*m.b18 + 192*m.b9*m.b11*m.b17*m.b19 + 128*m.b9*m.b11*
                       m.b18*m.b20 + 64*m.b9*m.b11*m.b19*m.b21 + 384*m.b9*m.b12*m.b13*m.b16 + 320*m.b9*m.b12*m.b14*m.b17
                        + 256*m.b9*m.b12*m.b15*m.b18 + 192*m.b9*m.b12*m.b16*m.b19 + 128*m.b9*m.b12*m.b17*m.b20 + 64*m.b9
                       *m.b12*m.b18*m.b21 + 256*m.b9*m.b13*m.b14*m.b18 + 192*m.b9*m.b13*m.b15*m.b19 + 128*m.b9*m.b13*
                       m.b16*m.b20 + 64*m.b9*m.b13*m.b17*m.b21 + 128*m.b9*m.b14*m.b15*m.b20 + 64*m.b9*m.b14*m.b16*m.b21
                        + 640*m.b10*m.b11*m.b12*m.b13 + 576*m.b10*m.b11*m.b13*m.b14 + 512*m.b10*m.b11*m.b14*m.b15 + 448*
                       m.b10*m.b11*m.b15*m.b16 + 384*m.b10*m.b11*m.b16*m.b17 + 320*m.b10*m.b11*m.b17*m.b18 + 256*m.b10*
                       m.b11*m.b18*m.b19 + 192*m.b10*m.b11*m.b19*m.b20 + 128*m.b10*m.b11*m.b20*m.b21 + 64*m.b10*m.b11*
                       m.b21*m.b22 + 512*m.b10*m.b12*m.b13*m.b15 + 448*m.b10*m.b12*m.b14*m.b16 + 384*m.b10*m.b12*m.b15*
                       m.b17 + 320*m.b10*m.b12*m.b16*m.b18 + 256*m.b10*m.b12*m.b17*m.b19 + 192*m.b10*m.b12*m.b18*m.b20
                        + 128*m.b10*m.b12*m.b19*m.b21 + 64*m.b10*m.b12*m.b20*m.b22 + 384*m.b10*m.b13*m.b14*m.b17 + 320*
                       m.b10*m.b13*m.b15*m.b18 + 256*m.b10*m.b13*m.b16*m.b19 + 192*m.b10*m.b13*m.b17*m.b20 + 128*m.b10*
                       m.b13*m.b18*m.b21 + 64*m.b10*m.b13*m.b19*m.b22 + 256*m.b10*m.b14*m.b15*m.b19 + 192*m.b10*m.b14*
                       m.b16*m.b20 + 128*m.b10*m.b14*m.b17*m.b21 + 64*m.b10*m.b14*m.b18*m.b22 + 128*m.b10*m.b15*m.b16*
                       m.b21 + 64*m.b10*m.b15*m.b17*m.b22 + 640*m.b11*m.b12*m.b13*m.b14 + 576*m.b11*m.b12*m.b14*m.b15 + 
                       512*m.b11*m.b12*m.b15*m.b16 + 448*m.b11*m.b12*m.b16*m.b17 + 384*m.b11*m.b12*m.b17*m.b18 + 320*
                       m.b11*m.b12*m.b18*m.b19 + 256*m.b11*m.b12*m.b19*m.b20 + 192*m.b11*m.b12*m.b20*m.b21 + 128*m.b11*
                       m.b12*m.b21*m.b22 + 64*m.b11*m.b12*m.b22*m.b23 + 512*m.b11*m.b13*m.b14*m.b16 + 448*m.b11*m.b13*
                       m.b15*m.b17 + 384*m.b11*m.b13*m.b16*m.b18 + 320*m.b11*m.b13*m.b17*m.b19 + 256*m.b11*m.b13*m.b18*
                       m.b20 + 192*m.b11*m.b13*m.b19*m.b21 + 128*m.b11*m.b13*m.b20*m.b22 + 64*m.b11*m.b13*m.b21*m.b23 + 
                       384*m.b11*m.b14*m.b15*m.b18 + 320*m.b11*m.b14*m.b16*m.b19 + 256*m.b11*m.b14*m.b17*m.b20 + 192*
                       m.b11*m.b14*m.b18*m.b21 + 128*m.b11*m.b14*m.b19*m.b22 + 64*m.b11*m.b14*m.b20*m.b23 + 256*m.b11*
                       m.b15*m.b16*m.b20 + 192*m.b11*m.b15*m.b17*m.b21 + 128*m.b11*m.b15*m.b18*m.b22 + 64*m.b11*m.b15*
                       m.b19*m.b23 + 128*m.b11*m.b16*m.b17*m.b22 + 64*m.b11*m.b16*m.b18*m.b23 + 640*m.b12*m.b13*m.b14*
                       m.b15 + 576*m.b12*m.b13*m.b15*m.b16 + 512*m.b12*m.b13*m.b16*m.b17 + 448*m.b12*m.b13*m.b17*m.b18
                        + 384*m.b12*m.b13*m.b18*m.b19 + 320*m.b12*m.b13*m.b19*m.b20 + 256*m.b12*m.b13*m.b20*m.b21 + 192*
                       m.b12*m.b13*m.b21*m.b22 + 128*m.b12*m.b13*m.b22*m.b23 + 64*m.b12*m.b13*m.b23*m.b24 + 512*m.b12*
                       m.b14*m.b15*m.b17 + 448*m.b12*m.b14*m.b16*m.b18 + 384*m.b12*m.b14*m.b17*m.b19 + 320*m.b12*m.b14*
                       m.b18*m.b20 + 256*m.b12*m.b14*m.b19*m.b21 + 192*m.b12*m.b14*m.b20*m.b22 + 128*m.b12*m.b14*m.b21*
                       m.b23 + 64*m.b12*m.b14*m.b22*m.b24 + 384*m.b12*m.b15*m.b16*m.b19 + 320*m.b12*m.b15*m.b17*m.b20 + 
                       256*m.b12*m.b15*m.b18*m.b21 + 192*m.b12*m.b15*m.b19*m.b22 + 128*m.b12*m.b15*m.b20*m.b23 + 64*
                       m.b12*m.b15*m.b21*m.b24 + 256*m.b12*m.b16*m.b17*m.b21 + 192*m.b12*m.b16*m.b18*m.b22 + 128*m.b12*
                       m.b16*m.b19*m.b23 + 64*m.b12*m.b16*m.b20*m.b24 + 128*m.b12*m.b17*m.b18*m.b23 + 64*m.b12*m.b17*
                       m.b19*m.b24 + 640*m.b13*m.b14*m.b15*m.b16 + 576*m.b13*m.b14*m.b16*m.b17 + 512*m.b13*m.b14*m.b17*
                       m.b18 + 448*m.b13*m.b14*m.b18*m.b19 + 384*m.b13*m.b14*m.b19*m.b20 + 320*m.b13*m.b14*m.b20*m.b21
                        + 256*m.b13*m.b14*m.b21*m.b22 + 192*m.b13*m.b14*m.b22*m.b23 + 128*m.b13*m.b14*m.b23*m.b24 + 64*
                       m.b13*m.b14*m.b24*m.b25 + 512*m.b13*m.b15*m.b16*m.b18 + 448*m.b13*m.b15*m.b17*m.b19 + 384*m.b13*
                       m.b15*m.b18*m.b20 + 320*m.b13*m.b15*m.b19*m.b21 + 256*m.b13*m.b15*m.b20*m.b22 + 192*m.b13*m.b15*
                       m.b21*m.b23 + 128*m.b13*m.b15*m.b22*m.b24 + 64*m.b13*m.b15*m.b23*m.b25 + 384*m.b13*m.b16*m.b17*
                       m.b20 + 320*m.b13*m.b16*m.b18*m.b21 + 256*m.b13*m.b16*m.b19*m.b22 + 192*m.b13*m.b16*m.b20*m.b23
                        + 128*m.b13*m.b16*m.b21*m.b24 + 64*m.b13*m.b16*m.b22*m.b25 + 256*m.b13*m.b17*m.b18*m.b22 + 192*
                       m.b13*m.b17*m.b19*m.b23 + 128*m.b13*m.b17*m.b20*m.b24 + 64*m.b13*m.b17*m.b21*m.b25 + 128*m.b13*
                       m.b18*m.b19*m.b24 + 64*m.b13*m.b18*m.b20*m.b25 + 640*m.b14*m.b15*m.b16*m.b17 + 576*m.b14*m.b15*
                       m.b17*m.b18 + 512*m.b14*m.b15*m.b18*m.b19 + 448*m.b14*m.b15*m.b19*m.b20 + 384*m.b14*m.b15*m.b20*
                       m.b21 + 320*m.b14*m.b15*m.b21*m.b22 + 256*m.b14*m.b15*m.b22*m.b23 + 192*m.b14*m.b15*m.b23*m.b24
                        + 128*m.b14*m.b15*m.b24*m.b25 + 64*m.b14*m.b15*m.b25*m.b26 + 512*m.b14*m.b16*m.b17*m.b19 + 448*
                       m.b14*m.b16*m.b18*m.b20 + 384*m.b14*m.b16*m.b19*m.b21 + 320*m.b14*m.b16*m.b20*m.b22 + 256*m.b14*
                       m.b16*m.b21*m.b23 + 192*m.b14*m.b16*m.b22*m.b24 + 128*m.b14*m.b16*m.b23*m.b25 + 64*m.b14*m.b16*
                       m.b24*m.b26 + 384*m.b14*m.b17*m.b18*m.b21 + 320*m.b14*m.b17*m.b19*m.b22 + 256*m.b14*m.b17*m.b20*
                       m.b23 + 192*m.b14*m.b17*m.b21*m.b24 + 128*m.b14*m.b17*m.b22*m.b25 + 64*m.b14*m.b17*m.b23*m.b26 + 
                       256*m.b14*m.b18*m.b19*m.b23 + 192*m.b14*m.b18*m.b20*m.b24 + 128*m.b14*m.b18*m.b21*m.b25 + 64*
                       m.b14*m.b18*m.b22*m.b26 + 128*m.b14*m.b19*m.b20*m.b25 + 64*m.b14*m.b19*m.b21*m.b26 + 640*m.b15*
                       m.b16*m.b17*m.b18 + 576*m.b15*m.b16*m.b18*m.b19 + 512*m.b15*m.b16*m.b19*m.b20 + 448*m.b15*m.b16*
                       m.b20*m.b21 + 384*m.b15*m.b16*m.b21*m.b22 + 320*m.b15*m.b16*m.b22*m.b23 + 256*m.b15*m.b16*m.b23*
                       m.b24 + 192*m.b15*m.b16*m.b24*m.b25 + 128*m.b15*m.b16*m.b25*m.b26 + 64*m.b15*m.b16*m.b26*m.b27 + 
                       512*m.b15*m.b17*m.b18*m.b20 + 448*m.b15*m.b17*m.b19*m.b21 + 384*m.b15*m.b17*m.b20*m.b22 + 320*
                       m.b15*m.b17*m.b21*m.b23 + 256*m.b15*m.b17*m.b22*m.b24 + 192*m.b15*m.b17*m.b23*m.b25 + 128*m.b15*
                       m.b17*m.b24*m.b26 + 64*m.b15*m.b17*m.b25*m.b27 + 384*m.b15*m.b18*m.b19*m.b22 + 320*m.b15*m.b18*
                       m.b20*m.b23 + 256*m.b15*m.b18*m.b21*m.b24 + 192*m.b15*m.b18*m.b22*m.b25 + 128*m.b15*m.b18*m.b23*
                       m.b26 + 64*m.b15*m.b18*m.b24*m.b27 + 256*m.b15*m.b19*m.b20*m.b24 + 192*m.b15*m.b19*m.b21*m.b25 + 
                       128*m.b15*m.b19*m.b22*m.b26 + 64*m.b15*m.b19*m.b23*m.b27 + 128*m.b15*m.b20*m.b21*m.b26 + 64*m.b15
                       *m.b20*m.b22*m.b27 + 640*m.b16*m.b17*m.b18*m.b19 + 576*m.b16*m.b17*m.b19*m.b20 + 512*m.b16*m.b17*
                       m.b20*m.b21 + 448*m.b16*m.b17*m.b21*m.b22 + 384*m.b16*m.b17*m.b22*m.b23 + 320*m.b16*m.b17*m.b23*
                       m.b24 + 256*m.b16*m.b17*m.b24*m.b25 + 192*m.b16*m.b17*m.b25*m.b26 + 128*m.b16*m.b17*m.b26*m.b27
                        + 64*m.b16*m.b17*m.b27*m.b28 + 512*m.b16*m.b18*m.b19*m.b21 + 448*m.b16*m.b18*m.b20*m.b22 + 384*
                       m.b16*m.b18*m.b21*m.b23 + 320*m.b16*m.b18*m.b22*m.b24 + 256*m.b16*m.b18*m.b23*m.b25 + 192*m.b16*
                       m.b18*m.b24*m.b26 + 128*m.b16*m.b18*m.b25*m.b27 + 64*m.b16*m.b18*m.b26*m.b28 + 384*m.b16*m.b19*
                       m.b20*m.b23 + 320*m.b16*m.b19*m.b21*m.b24 + 256*m.b16*m.b19*m.b22*m.b25 + 192*m.b16*m.b19*m.b23*
                       m.b26 + 128*m.b16*m.b19*m.b24*m.b27 + 64*m.b16*m.b19*m.b25*m.b28 + 256*m.b16*m.b20*m.b21*m.b25 + 
                       192*m.b16*m.b20*m.b22*m.b26 + 128*m.b16*m.b20*m.b23*m.b27 + 64*m.b16*m.b20*m.b24*m.b28 + 128*
                       m.b16*m.b21*m.b22*m.b27 + 64*m.b16*m.b21*m.b23*m.b28 + 640*m.b17*m.b18*m.b19*m.b20 + 576*m.b17*
                       m.b18*m.b20*m.b21 + 512*m.b17*m.b18*m.b21*m.b22 + 448*m.b17*m.b18*m.b22*m.b23 + 384*m.b17*m.b18*
                       m.b23*m.b24 + 320*m.b17*m.b18*m.b24*m.b25 + 256*m.b17*m.b18*m.b25*m.b26 + 192*m.b17*m.b18*m.b26*
                       m.b27 + 128*m.b17*m.b18*m.b27*m.b28 + 64*m.b17*m.b18*m.b28*m.b29 + 512*m.b17*m.b19*m.b20*m.b22 + 
                       448*m.b17*m.b19*m.b21*m.b23 + 384*m.b17*m.b19*m.b22*m.b24 + 320*m.b17*m.b19*m.b23*m.b25 + 256*
                       m.b17*m.b19*m.b24*m.b26 + 192*m.b17*m.b19*m.b25*m.b27 + 128*m.b17*m.b19*m.b26*m.b28 + 64*m.b17*
                       m.b19*m.b27*m.b29 + 384*m.b17*m.b20*m.b21*m.b24 + 320*m.b17*m.b20*m.b22*m.b25 + 256*m.b17*m.b20*
                       m.b23*m.b26 + 192*m.b17*m.b20*m.b24*m.b27 + 128*m.b17*m.b20*m.b25*m.b28 + 64*m.b17*m.b20*m.b26*
                       m.b29 + 256*m.b17*m.b21*m.b22*m.b26 + 192*m.b17*m.b21*m.b23*m.b27 + 128*m.b17*m.b21*m.b24*m.b28
                        + 64*m.b17*m.b21*m.b25*m.b29 + 128*m.b17*m.b22*m.b23*m.b28 + 64*m.b17*m.b22*m.b24*m.b29 + 640*
                       m.b18*m.b19*m.b20*m.b21 + 576*m.b18*m.b19*m.b21*m.b22 + 512*m.b18*m.b19*m.b22*m.b23 + 448*m.b18*
                       m.b19*m.b23*m.b24 + 384*m.b18*m.b19*m.b24*m.b25 + 320*m.b18*m.b19*m.b25*m.b26 + 256*m.b18*m.b19*
                       m.b26*m.b27 + 192*m.b18*m.b19*m.b27*m.b28 + 128*m.b18*m.b19*m.b28*m.b29 + 64*m.b18*m.b19*m.b29*
                       m.b30 + 512*m.b18*m.b20*m.b21*m.b23 + 448*m.b18*m.b20*m.b22*m.b24 + 384*m.b18*m.b20*m.b23*m.b25
                        + 320*m.b18*m.b20*m.b24*m.b26 + 256*m.b18*m.b20*m.b25*m.b27 + 192*m.b18*m.b20*m.b26*m.b28 + 128*
                       m.b18*m.b20*m.b27*m.b29 + 64*m.b18*m.b20*m.b28*m.b30 + 384*m.b18*m.b21*m.b22*m.b25 + 320*m.b18*
                       m.b21*m.b23*m.b26 + 256*m.b18*m.b21*m.b24*m.b27 + 192*m.b18*m.b21*m.b25*m.b28 + 128*m.b18*m.b21*
                       m.b26*m.b29 + 64*m.b18*m.b21*m.b27*m.b30 + 256*m.b18*m.b22*m.b23*m.b27 + 192*m.b18*m.b22*m.b24*
                       m.b28 + 128*m.b18*m.b22*m.b25*m.b29 + 64*m.b18*m.b22*m.b26*m.b30 + 128*m.b18*m.b23*m.b24*m.b29 + 
                       64*m.b18*m.b23*m.b25*m.b30 + 640*m.b19*m.b20*m.b21*m.b22 + 576*m.b19*m.b20*m.b22*m.b23 + 512*
                       m.b19*m.b20*m.b23*m.b24 + 448*m.b19*m.b20*m.b24*m.b25 + 384*m.b19*m.b20*m.b25*m.b26 + 320*m.b19*
                       m.b20*m.b26*m.b27 + 256*m.b19*m.b20*m.b27*m.b28 + 192*m.b19*m.b20*m.b28*m.b29 + 128*m.b19*m.b20*
                       m.b29*m.b30 + 64*m.b19*m.b20*m.b30*m.b31 + 512*m.b19*m.b21*m.b22*m.b24 + 448*m.b19*m.b21*m.b23*
                       m.b25 + 384*m.b19*m.b21*m.b24*m.b26 + 320*m.b19*m.b21*m.b25*m.b27 + 256*m.b19*m.b21*m.b26*m.b28
                        + 192*m.b19*m.b21*m.b27*m.b29 + 128*m.b19*m.b21*m.b28*m.b30 + 64*m.b19*m.b21*m.b29*m.b31 + 384*
                       m.b19*m.b22*m.b23*m.b26 + 320*m.b19*m.b22*m.b24*m.b27 + 256*m.b19*m.b22*m.b25*m.b28 + 192*m.b19*
                       m.b22*m.b26*m.b29 + 128*m.b19*m.b22*m.b27*m.b30 + 64*m.b19*m.b22*m.b28*m.b31 + 256*m.b19*m.b23*
                       m.b24*m.b28 + 192*m.b19*m.b23*m.b25*m.b29 + 128*m.b19*m.b23*m.b26*m.b30 + 64*m.b19*m.b23*m.b27*
                       m.b31 + 128*m.b19*m.b24*m.b25*m.b30 + 64*m.b19*m.b24*m.b26*m.b31 + 640*m.b20*m.b21*m.b22*m.b23 + 
                       576*m.b20*m.b21*m.b23*m.b24 + 512*m.b20*m.b21*m.b24*m.b25 + 448*m.b20*m.b21*m.b25*m.b26 + 384*
                       m.b20*m.b21*m.b26*m.b27 + 320*m.b20*m.b21*m.b27*m.b28 + 256*m.b20*m.b21*m.b28*m.b29 + 192*m.b20*
                       m.b21*m.b29*m.b30 + 128*m.b20*m.b21*m.b30*m.b31 + 64*m.b20*m.b21*m.b31*m.b32 + 512*m.b20*m.b22*
                       m.b23*m.b25 + 448*m.b20*m.b22*m.b24*m.b26 + 384*m.b20*m.b22*m.b25*m.b27 + 320*m.b20*m.b22*m.b26*
                       m.b28 + 256*m.b20*m.b22*m.b27*m.b29 + 192*m.b20*m.b22*m.b28*m.b30 + 128*m.b20*m.b22*m.b29*m.b31
                        + 64*m.b20*m.b22*m.b30*m.b32 + 384*m.b20*m.b23*m.b24*m.b27 + 320*m.b20*m.b23*m.b25*m.b28 + 256*
                       m.b20*m.b23*m.b26*m.b29 + 192*m.b20*m.b23*m.b27*m.b30 + 128*m.b20*m.b23*m.b28*m.b31 + 64*m.b20*
                       m.b23*m.b29*m.b32 + 256*m.b20*m.b24*m.b25*m.b29 + 192*m.b20*m.b24*m.b26*m.b30 + 128*m.b20*m.b24*
                       m.b27*m.b31 + 64*m.b20*m.b24*m.b28*m.b32 + 128*m.b20*m.b25*m.b26*m.b31 + 64*m.b20*m.b25*m.b27*
                       m.b32 + 640*m.b21*m.b22*m.b23*m.b24 + 576*m.b21*m.b22*m.b24*m.b25 + 512*m.b21*m.b22*m.b25*m.b26
                        + 448*m.b21*m.b22*m.b26*m.b27 + 384*m.b21*m.b22*m.b27*m.b28 + 320*m.b21*m.b22*m.b28*m.b29 + 256*
                       m.b21*m.b22*m.b29*m.b30 + 192*m.b21*m.b22*m.b30*m.b31 + 128*m.b21*m.b22*m.b31*m.b32 + 64*m.b21*
                       m.b22*m.b32*m.b33 + 512*m.b21*m.b23*m.b24*m.b26 + 448*m.b21*m.b23*m.b25*m.b27 + 384*m.b21*m.b23*
                       m.b26*m.b28 + 320*m.b21*m.b23*m.b27*m.b29 + 256*m.b21*m.b23*m.b28*m.b30 + 192*m.b21*m.b23*m.b29*
                       m.b31 + 128*m.b21*m.b23*m.b30*m.b32 + 64*m.b21*m.b23*m.b31*m.b33 + 384*m.b21*m.b24*m.b25*m.b28 + 
                       320*m.b21*m.b24*m.b26*m.b29 + 256*m.b21*m.b24*m.b27*m.b30 + 192*m.b21*m.b24*m.b28*m.b31 + 128*
                       m.b21*m.b24*m.b29*m.b32 + 64*m.b21*m.b24*m.b30*m.b33 + 256*m.b21*m.b25*m.b26*m.b30 + 192*m.b21*
                       m.b25*m.b27*m.b31 + 128*m.b21*m.b25*m.b28*m.b32 + 64*m.b21*m.b25*m.b29*m.b33 + 128*m.b21*m.b26*
                       m.b27*m.b32 + 64*m.b21*m.b26*m.b28*m.b33 + 640*m.b22*m.b23*m.b24*m.b25 + 576*m.b22*m.b23*m.b25*
                       m.b26 + 512*m.b22*m.b23*m.b26*m.b27 + 448*m.b22*m.b23*m.b27*m.b28 + 384*m.b22*m.b23*m.b28*m.b29
                        + 320*m.b22*m.b23*m.b29*m.b30 + 256*m.b22*m.b23*m.b30*m.b31 + 192*m.b22*m.b23*m.b31*m.b32 + 128*
                       m.b22*m.b23*m.b32*m.b33 + 64*m.b22*m.b23*m.b33*m.b34 + 512*m.b22*m.b24*m.b25*m.b27 + 448*m.b22*
                       m.b24*m.b26*m.b28 + 384*m.b22*m.b24*m.b27*m.b29 + 320*m.b22*m.b24*m.b28*m.b30 + 256*m.b22*m.b24*
                       m.b29*m.b31 + 192*m.b22*m.b24*m.b30*m.b32 + 128*m.b22*m.b24*m.b31*m.b33 + 64*m.b22*m.b24*m.b32*
                       m.b34 + 384*m.b22*m.b25*m.b26*m.b29 + 320*m.b22*m.b25*m.b27*m.b30 + 256*m.b22*m.b25*m.b28*m.b31
                        + 192*m.b22*m.b25*m.b29*m.b32 + 128*m.b22*m.b25*m.b30*m.b33 + 64*m.b22*m.b25*m.b31*m.b34 + 256*
                       m.b22*m.b26*m.b27*m.b31 + 192*m.b22*m.b26*m.b28*m.b32 + 128*m.b22*m.b26*m.b29*m.b33 + 64*m.b22*
                       m.b26*m.b30*m.b34 + 128*m.b22*m.b27*m.b28*m.b33 + 64*m.b22*m.b27*m.b29*m.b34 + 640*m.b23*m.b24*
                       m.b25*m.b26 + 576*m.b23*m.b24*m.b26*m.b27 + 512*m.b23*m.b24*m.b27*m.b28 + 448*m.b23*m.b24*m.b28*
                       m.b29 + 384*m.b23*m.b24*m.b29*m.b30 + 320*m.b23*m.b24*m.b30*m.b31 + 256*m.b23*m.b24*m.b31*m.b32
                        + 192*m.b23*m.b24*m.b32*m.b33 + 128*m.b23*m.b24*m.b33*m.b34 + 64*m.b23*m.b24*m.b34*m.b35 + 512*
                       m.b23*m.b25*m.b26*m.b28 + 448*m.b23*m.b25*m.b27*m.b29 + 384*m.b23*m.b25*m.b28*m.b30 + 320*m.b23*
                       m.b25*m.b29*m.b31 + 256*m.b23*m.b25*m.b30*m.b32 + 192*m.b23*m.b25*m.b31*m.b33 + 128*m.b23*m.b25*
                       m.b32*m.b34 + 64*m.b23*m.b25*m.b33*m.b35 + 384*m.b23*m.b26*m.b27*m.b30 + 320*m.b23*m.b26*m.b28*
                       m.b31 + 256*m.b23*m.b26*m.b29*m.b32 + 192*m.b23*m.b26*m.b30*m.b33 + 128*m.b23*m.b26*m.b31*m.b34
                        + 64*m.b23*m.b26*m.b32*m.b35 + 256*m.b23*m.b27*m.b28*m.b32 + 192*m.b23*m.b27*m.b29*m.b33 + 128*
                       m.b23*m.b27*m.b30*m.b34 + 64*m.b23*m.b27*m.b31*m.b35 + 128*m.b23*m.b28*m.b29*m.b34 + 64*m.b23*
                       m.b28*m.b30*m.b35 + 640*m.b24*m.b25*m.b26*m.b27 + 576*m.b24*m.b25*m.b27*m.b28 + 512*m.b24*m.b25*
                       m.b28*m.b29 + 448*m.b24*m.b25*m.b29*m.b30 + 384*m.b24*m.b25*m.b30*m.b31 + 320*m.b24*m.b25*m.b31*
                       m.b32 + 256*m.b24*m.b25*m.b32*m.b33 + 192*m.b24*m.b25*m.b33*m.b34 + 128*m.b24*m.b25*m.b34*m.b35
                        + 64*m.b24*m.b25*m.b35*m.b36 + 512*m.b24*m.b26*m.b27*m.b29 + 448*m.b24*m.b26*m.b28*m.b30 + 384*
                       m.b24*m.b26*m.b29*m.b31 + 320*m.b24*m.b26*m.b30*m.b32 + 256*m.b24*m.b26*m.b31*m.b33 + 192*m.b24*
                       m.b26*m.b32*m.b34 + 128*m.b24*m.b26*m.b33*m.b35 + 64*m.b24*m.b26*m.b34*m.b36 + 384*m.b24*m.b27*
                       m.b28*m.b31 + 320*m.b24*m.b27*m.b29*m.b32 + 256*m.b24*m.b27*m.b30*m.b33 + 192*m.b24*m.b27*m.b31*
                       m.b34 + 128*m.b24*m.b27*m.b32*m.b35 + 64*m.b24*m.b27*m.b33*m.b36 + 256*m.b24*m.b28*m.b29*m.b33 + 
                       192*m.b24*m.b28*m.b30*m.b34 + 128*m.b24*m.b28*m.b31*m.b35 + 64*m.b24*m.b28*m.b32*m.b36 + 128*
                       m.b24*m.b29*m.b30*m.b35 + 64*m.b24*m.b29*m.b31*m.b36 + 640*m.b25*m.b26*m.b27*m.b28 + 576*m.b25*
                       m.b26*m.b28*m.b29 + 512*m.b25*m.b26*m.b29*m.b30 + 448*m.b25*m.b26*m.b30*m.b31 + 384*m.b25*m.b26*
                       m.b31*m.b32 + 320*m.b25*m.b26*m.b32*m.b33 + 256*m.b25*m.b26*m.b33*m.b34 + 192*m.b25*m.b26*m.b34*
                       m.b35 + 128*m.b25*m.b26*m.b35*m.b36 + 64*m.b25*m.b26*m.b36*m.b37 + 512*m.b25*m.b27*m.b28*m.b30 + 
                       448*m.b25*m.b27*m.b29*m.b31 + 384*m.b25*m.b27*m.b30*m.b32 + 320*m.b25*m.b27*m.b31*m.b33 + 256*
                       m.b25*m.b27*m.b32*m.b34 + 192*m.b25*m.b27*m.b33*m.b35 + 128*m.b25*m.b27*m.b34*m.b36 + 64*m.b25*
                       m.b27*m.b35*m.b37 + 384*m.b25*m.b28*m.b29*m.b32 + 320*m.b25*m.b28*m.b30*m.b33 + 256*m.b25*m.b28*
                       m.b31*m.b34 + 192*m.b25*m.b28*m.b32*m.b35 + 128*m.b25*m.b28*m.b33*m.b36 + 64*m.b25*m.b28*m.b34*
                       m.b37 + 256*m.b25*m.b29*m.b30*m.b34 + 192*m.b25*m.b29*m.b31*m.b35 + 128*m.b25*m.b29*m.b32*m.b36
                        + 64*m.b25*m.b29*m.b33*m.b37 + 128*m.b25*m.b30*m.b31*m.b36 + 64*m.b25*m.b30*m.b32*m.b37 + 640*
                       m.b26*m.b27*m.b28*m.b29 + 576*m.b26*m.b27*m.b29*m.b30 + 512*m.b26*m.b27*m.b30*m.b31 + 448*m.b26*
                       m.b27*m.b31*m.b32 + 384*m.b26*m.b27*m.b32*m.b33 + 320*m.b26*m.b27*m.b33*m.b34 + 256*m.b26*m.b27*
                       m.b34*m.b35 + 192*m.b26*m.b27*m.b35*m.b36 + 128*m.b26*m.b27*m.b36*m.b37 + 64*m.b26*m.b27*m.b37*
                       m.b38 + 512*m.b26*m.b28*m.b29*m.b31 + 448*m.b26*m.b28*m.b30*m.b32 + 384*m.b26*m.b28*m.b31*m.b33
                        + 320*m.b26*m.b28*m.b32*m.b34 + 256*m.b26*m.b28*m.b33*m.b35 + 192*m.b26*m.b28*m.b34*m.b36 + 128*
                       m.b26*m.b28*m.b35*m.b37 + 64*m.b26*m.b28*m.b36*m.b38 + 384*m.b26*m.b29*m.b30*m.b33 + 320*m.b26*
                       m.b29*m.b31*m.b34 + 256*m.b26*m.b29*m.b32*m.b35 + 192*m.b26*m.b29*m.b33*m.b36 + 128*m.b26*m.b29*
                       m.b34*m.b37 + 64*m.b26*m.b29*m.b35*m.b38 + 256*m.b26*m.b30*m.b31*m.b35 + 192*m.b26*m.b30*m.b32*
                       m.b36 + 128*m.b26*m.b30*m.b33*m.b37 + 64*m.b26*m.b30*m.b34*m.b38 + 128*m.b26*m.b31*m.b32*m.b37 + 
                       64*m.b26*m.b31*m.b33*m.b38 + 640*m.b27*m.b28*m.b29*m.b30 + 576*m.b27*m.b28*m.b30*m.b31 + 512*
                       m.b27*m.b28*m.b31*m.b32 + 448*m.b27*m.b28*m.b32*m.b33 + 384*m.b27*m.b28*m.b33*m.b34 + 320*m.b27*
                       m.b28*m.b34*m.b35 + 256*m.b27*m.b28*m.b35*m.b36 + 192*m.b27*m.b28*m.b36*m.b37 + 128*m.b27*m.b28*
                       m.b37*m.b38 + 64*m.b27*m.b28*m.b38*m.b39 + 512*m.b27*m.b29*m.b30*m.b32 + 448*m.b27*m.b29*m.b31*
                       m.b33 + 384*m.b27*m.b29*m.b32*m.b34 + 320*m.b27*m.b29*m.b33*m.b35 + 256*m.b27*m.b29*m.b34*m.b36
                        + 192*m.b27*m.b29*m.b35*m.b37 + 128*m.b27*m.b29*m.b36*m.b38 + 64*m.b27*m.b29*m.b37*m.b39 + 384*
                       m.b27*m.b30*m.b31*m.b34 + 320*m.b27*m.b30*m.b32*m.b35 + 256*m.b27*m.b30*m.b33*m.b36 + 192*m.b27*
                       m.b30*m.b34*m.b37 + 128*m.b27*m.b30*m.b35*m.b38 + 64*m.b27*m.b30*m.b36*m.b39 + 256*m.b27*m.b31*
                       m.b32*m.b36 + 192*m.b27*m.b31*m.b33*m.b37 + 128*m.b27*m.b31*m.b34*m.b38 + 64*m.b27*m.b31*m.b35*
                       m.b39 + 128*m.b27*m.b32*m.b33*m.b38 + 64*m.b27*m.b32*m.b34*m.b39 + 640*m.b28*m.b29*m.b30*m.b31 + 
                       576*m.b28*m.b29*m.b31*m.b32 + 512*m.b28*m.b29*m.b32*m.b33 + 448*m.b28*m.b29*m.b33*m.b34 + 384*
                       m.b28*m.b29*m.b34*m.b35 + 320*m.b28*m.b29*m.b35*m.b36 + 256*m.b28*m.b29*m.b36*m.b37 + 192*m.b28*
                       m.b29*m.b37*m.b38 + 128*m.b28*m.b29*m.b38*m.b39 + 64*m.b28*m.b29*m.b39*m.b40 + 512*m.b28*m.b30*
                       m.b31*m.b33 + 448*m.b28*m.b30*m.b32*m.b34 + 384*m.b28*m.b30*m.b33*m.b35 + 320*m.b28*m.b30*m.b34*
                       m.b36 + 256*m.b28*m.b30*m.b35*m.b37 + 192*m.b28*m.b30*m.b36*m.b38 + 128*m.b28*m.b30*m.b37*m.b39
                        + 64*m.b28*m.b30*m.b38*m.b40 + 384*m.b28*m.b31*m.b32*m.b35 + 320*m.b28*m.b31*m.b33*m.b36 + 256*
                       m.b28*m.b31*m.b34*m.b37 + 192*m.b28*m.b31*m.b35*m.b38 + 128*m.b28*m.b31*m.b36*m.b39 + 64*m.b28*
                       m.b31*m.b37*m.b40 + 256*m.b28*m.b32*m.b33*m.b37 + 192*m.b28*m.b32*m.b34*m.b38 + 128*m.b28*m.b32*
                       m.b35*m.b39 + 64*m.b28*m.b32*m.b36*m.b40 + 128*m.b28*m.b33*m.b34*m.b39 + 64*m.b28*m.b33*m.b35*
                       m.b40 + 640*m.b29*m.b30*m.b31*m.b32 + 576*m.b29*m.b30*m.b32*m.b33 + 512*m.b29*m.b30*m.b33*m.b34
                        + 448*m.b29*m.b30*m.b34*m.b35 + 384*m.b29*m.b30*m.b35*m.b36 + 320*m.b29*m.b30*m.b36*m.b37 + 256*
                       m.b29*m.b30*m.b37*m.b38 + 192*m.b29*m.b30*m.b38*m.b39 + 128*m.b29*m.b30*m.b39*m.b40 + 64*m.b29*
                       m.b30*m.b40*m.b41 + 512*m.b29*m.b31*m.b32*m.b34 + 448*m.b29*m.b31*m.b33*m.b35 + 384*m.b29*m.b31*
                       m.b34*m.b36 + 320*m.b29*m.b31*m.b35*m.b37 + 256*m.b29*m.b31*m.b36*m.b38 + 192*m.b29*m.b31*m.b37*
                       m.b39 + 128*m.b29*m.b31*m.b38*m.b40 + 64*m.b29*m.b31*m.b39*m.b41 + 384*m.b29*m.b32*m.b33*m.b36 + 
                       320*m.b29*m.b32*m.b34*m.b37 + 256*m.b29*m.b32*m.b35*m.b38 + 192*m.b29*m.b32*m.b36*m.b39 + 128*
                       m.b29*m.b32*m.b37*m.b40 + 64*m.b29*m.b32*m.b38*m.b41 + 256*m.b29*m.b33*m.b34*m.b38 + 192*m.b29*
                       m.b33*m.b35*m.b39 + 128*m.b29*m.b33*m.b36*m.b40 + 64*m.b29*m.b33*m.b37*m.b41 + 128*m.b29*m.b34*
                       m.b35*m.b40 + 64*m.b29*m.b34*m.b36*m.b41 + 640*m.b30*m.b31*m.b32*m.b33 + 576*m.b30*m.b31*m.b33*
                       m.b34 + 512*m.b30*m.b31*m.b34*m.b35 + 448*m.b30*m.b31*m.b35*m.b36 + 384*m.b30*m.b31*m.b36*m.b37
                        + 320*m.b30*m.b31*m.b37*m.b38 + 256*m.b30*m.b31*m.b38*m.b39 + 192*m.b30*m.b31*m.b39*m.b40 + 128*
                       m.b30*m.b31*m.b40*m.b41 + 64*m.b30*m.b31*m.b41*m.b42 + 512*m.b30*m.b32*m.b33*m.b35 + 448*m.b30*
                       m.b32*m.b34*m.b36 + 384*m.b30*m.b32*m.b35*m.b37 + 320*m.b30*m.b32*m.b36*m.b38 + 256*m.b30*m.b32*
                       m.b37*m.b39 + 192*m.b30*m.b32*m.b38*m.b40 + 128*m.b30*m.b32*m.b39*m.b41 + 64*m.b30*m.b32*m.b40*
                       m.b42 + 384*m.b30*m.b33*m.b34*m.b37 + 320*m.b30*m.b33*m.b35*m.b38 + 256*m.b30*m.b33*m.b36*m.b39
                        + 192*m.b30*m.b33*m.b37*m.b40 + 128*m.b30*m.b33*m.b38*m.b41 + 64*m.b30*m.b33*m.b39*m.b42 + 256*
                       m.b30*m.b34*m.b35*m.b39 + 192*m.b30*m.b34*m.b36*m.b40 + 128*m.b30*m.b34*m.b37*m.b41 + 64*m.b30*
                       m.b34*m.b38*m.b42 + 128*m.b30*m.b35*m.b36*m.b41 + 64*m.b30*m.b35*m.b37*m.b42 + 640*m.b31*m.b32*
                       m.b33*m.b34 + 576*m.b31*m.b32*m.b34*m.b35 + 512*m.b31*m.b32*m.b35*m.b36 + 448*m.b31*m.b32*m.b36*
                       m.b37 + 384*m.b31*m.b32*m.b37*m.b38 + 320*m.b31*m.b32*m.b38*m.b39 + 256*m.b31*m.b32*m.b39*m.b40
                        + 192*m.b31*m.b32*m.b40*m.b41 + 128*m.b31*m.b32*m.b41*m.b42 + 64*m.b31*m.b32*m.b42*m.b43 + 512*
                       m.b31*m.b33*m.b34*m.b36 + 448*m.b31*m.b33*m.b35*m.b37 + 384*m.b31*m.b33*m.b36*m.b38 + 320*m.b31*
                       m.b33*m.b37*m.b39 + 256*m.b31*m.b33*m.b38*m.b40 + 192*m.b31*m.b33*m.b39*m.b41 + 128*m.b31*m.b33*
                       m.b40*m.b42 + 64*m.b31*m.b33*m.b41*m.b43 + 384*m.b31*m.b34*m.b35*m.b38 + 320*m.b31*m.b34*m.b36*
                       m.b39 + 256*m.b31*m.b34*m.b37*m.b40 + 192*m.b31*m.b34*m.b38*m.b41 + 128*m.b31*m.b34*m.b39*m.b42
                        + 64*m.b31*m.b34*m.b40*m.b43 + 256*m.b31*m.b35*m.b36*m.b40 + 192*m.b31*m.b35*m.b37*m.b41 + 128*
                       m.b31*m.b35*m.b38*m.b42 + 64*m.b31*m.b35*m.b39*m.b43 + 128*m.b31*m.b36*m.b37*m.b42 + 64*m.b31*
                       m.b36*m.b38*m.b43 + 640*m.b32*m.b33*m.b34*m.b35 + 576*m.b32*m.b33*m.b35*m.b36 + 512*m.b32*m.b33*
                       m.b36*m.b37 + 448*m.b32*m.b33*m.b37*m.b38 + 384*m.b32*m.b33*m.b38*m.b39 + 320*m.b32*m.b33*m.b39*
                       m.b40 + 256*m.b32*m.b33*m.b40*m.b41 + 192*m.b32*m.b33*m.b41*m.b42 + 128*m.b32*m.b33*m.b42*m.b43
                        + 64*m.b32*m.b33*m.b43*m.b44 + 512*m.b32*m.b34*m.b35*m.b37 + 448*m.b32*m.b34*m.b36*m.b38 + 384*
                       m.b32*m.b34*m.b37*m.b39 + 320*m.b32*m.b34*m.b38*m.b40 + 256*m.b32*m.b34*m.b39*m.b41 + 192*m.b32*
                       m.b34*m.b40*m.b42 + 128*m.b32*m.b34*m.b41*m.b43 + 64*m.b32*m.b34*m.b42*m.b44 + 384*m.b32*m.b35*
                       m.b36*m.b39 + 320*m.b32*m.b35*m.b37*m.b40 + 256*m.b32*m.b35*m.b38*m.b41 + 192*m.b32*m.b35*m.b39*
                       m.b42 + 128*m.b32*m.b35*m.b40*m.b43 + 64*m.b32*m.b35*m.b41*m.b44 + 256*m.b32*m.b36*m.b37*m.b41 + 
                       192*m.b32*m.b36*m.b38*m.b42 + 128*m.b32*m.b36*m.b39*m.b43 + 64*m.b32*m.b36*m.b40*m.b44 + 128*
                       m.b32*m.b37*m.b38*m.b43 + 64*m.b32*m.b37*m.b39*m.b44 + 640*m.b33*m.b34*m.b35*m.b36 + 576*m.b33*
                       m.b34*m.b36*m.b37 + 512*m.b33*m.b34*m.b37*m.b38 + 448*m.b33*m.b34*m.b38*m.b39 + 384*m.b33*m.b34*
                       m.b39*m.b40 + 320*m.b33*m.b34*m.b40*m.b41 + 256*m.b33*m.b34*m.b41*m.b42 + 192*m.b33*m.b34*m.b42*
                       m.b43 + 128*m.b33*m.b34*m.b43*m.b44 + 64*m.b33*m.b34*m.b44*m.b45 + 512*m.b33*m.b35*m.b36*m.b38 + 
                       448*m.b33*m.b35*m.b37*m.b39 + 384*m.b33*m.b35*m.b38*m.b40 + 320*m.b33*m.b35*m.b39*m.b41 + 256*
                       m.b33*m.b35*m.b40*m.b42 + 192*m.b33*m.b35*m.b41*m.b43 + 128*m.b33*m.b35*m.b42*m.b44 + 64*m.b33*
                       m.b35*m.b43*m.b45 + 384*m.b33*m.b36*m.b37*m.b40 + 320*m.b33*m.b36*m.b38*m.b41 + 256*m.b33*m.b36*
                       m.b39*m.b42 + 192*m.b33*m.b36*m.b40*m.b43 + 128*m.b33*m.b36*m.b41*m.b44 + 64*m.b33*m.b36*m.b42*
                       m.b45 + 256*m.b33*m.b37*m.b38*m.b42 + 192*m.b33*m.b37*m.b39*m.b43 + 128*m.b33*m.b37*m.b40*m.b44
                        + 64*m.b33*m.b37*m.b41*m.b45 + 128*m.b33*m.b38*m.b39*m.b44 + 64*m.b33*m.b38*m.b40*m.b45 + 640*
                       m.b34*m.b35*m.b36*m.b37 + 576*m.b34*m.b35*m.b37*m.b38 + 512*m.b34*m.b35*m.b38*m.b39 + 448*m.b34*
                       m.b35*m.b39*m.b40 + 384*m.b34*m.b35*m.b40*m.b41 + 320*m.b34*m.b35*m.b41*m.b42 + 256*m.b34*m.b35*
                       m.b42*m.b43 + 192*m.b34*m.b35*m.b43*m.b44 + 128*m.b34*m.b35*m.b44*m.b45 + 64*m.b34*m.b35*m.b45*
                       m.b46 + 512*m.b34*m.b36*m.b37*m.b39 + 448*m.b34*m.b36*m.b38*m.b40 + 384*m.b34*m.b36*m.b39*m.b41
                        + 320*m.b34*m.b36*m.b40*m.b42 + 256*m.b34*m.b36*m.b41*m.b43 + 192*m.b34*m.b36*m.b42*m.b44 + 128*
                       m.b34*m.b36*m.b43*m.b45 + 64*m.b34*m.b36*m.b44*m.b46 + 384*m.b34*m.b37*m.b38*m.b41 + 320*m.b34*
                       m.b37*m.b39*m.b42 + 256*m.b34*m.b37*m.b40*m.b43 + 192*m.b34*m.b37*m.b41*m.b44 + 128*m.b34*m.b37*
                       m.b42*m.b45 + 64*m.b34*m.b37*m.b43*m.b46 + 256*m.b34*m.b38*m.b39*m.b43 + 192*m.b34*m.b38*m.b40*
                       m.b44 + 128*m.b34*m.b38*m.b41*m.b45 + 64*m.b34*m.b38*m.b42*m.b46 + 128*m.b34*m.b39*m.b40*m.b45 + 
                       64*m.b34*m.b39*m.b41*m.b46 + 640*m.b35*m.b36*m.b37*m.b38 + 576*m.b35*m.b36*m.b38*m.b39 + 512*
                       m.b35*m.b36*m.b39*m.b40 + 448*m.b35*m.b36*m.b40*m.b41 + 384*m.b35*m.b36*m.b41*m.b42 + 320*m.b35*
                       m.b36*m.b42*m.b43 + 256*m.b35*m.b36*m.b43*m.b44 + 192*m.b35*m.b36*m.b44*m.b45 + 128*m.b35*m.b36*
                       m.b45*m.b46 + 64*m.b35*m.b36*m.b46*m.b47 + 512*m.b35*m.b37*m.b38*m.b40 + 448*m.b35*m.b37*m.b39*
                       m.b41 + 384*m.b35*m.b37*m.b40*m.b42 + 320*m.b35*m.b37*m.b41*m.b43 + 256*m.b35*m.b37*m.b42*m.b44
                        + 192*m.b35*m.b37*m.b43*m.b45 + 128*m.b35*m.b37*m.b44*m.b46 + 64*m.b35*m.b37*m.b45*m.b47 + 384*
                       m.b35*m.b38*m.b39*m.b42 + 320*m.b35*m.b38*m.b40*m.b43 + 256*m.b35*m.b38*m.b41*m.b44 + 192*m.b35*
                       m.b38*m.b42*m.b45 + 128*m.b35*m.b38*m.b43*m.b46 + 64*m.b35*m.b38*m.b44*m.b47 + 256*m.b35*m.b39*
                       m.b40*m.b44 + 192*m.b35*m.b39*m.b41*m.b45 + 128*m.b35*m.b39*m.b42*m.b46 + 64*m.b35*m.b39*m.b43*
                       m.b47 + 128*m.b35*m.b40*m.b41*m.b46 + 64*m.b35*m.b40*m.b42*m.b47 + 640*m.b36*m.b37*m.b38*m.b39 + 
                       576*m.b36*m.b37*m.b39*m.b40 + 512*m.b36*m.b37*m.b40*m.b41 + 448*m.b36*m.b37*m.b41*m.b42 + 384*
                       m.b36*m.b37*m.b42*m.b43 + 320*m.b36*m.b37*m.b43*m.b44 + 256*m.b36*m.b37*m.b44*m.b45 + 192*m.b36*
                       m.b37*m.b45*m.b46 + 128*m.b36*m.b37*m.b46*m.b47 + 64*m.b36*m.b37*m.b47*m.b48 + 512*m.b36*m.b38*
                       m.b39*m.b41 + 448*m.b36*m.b38*m.b40*m.b42 + 384*m.b36*m.b38*m.b41*m.b43 + 320*m.b36*m.b38*m.b42*
                       m.b44 + 256*m.b36*m.b38*m.b43*m.b45 + 192*m.b36*m.b38*m.b44*m.b46 + 128*m.b36*m.b38*m.b45*m.b47
                        + 64*m.b36*m.b38*m.b46*m.b48 + 384*m.b36*m.b39*m.b40*m.b43 + 320*m.b36*m.b39*m.b41*m.b44 + 256*
                       m.b36*m.b39*m.b42*m.b45 + 192*m.b36*m.b39*m.b43*m.b46 + 128*m.b36*m.b39*m.b44*m.b47 + 64*m.b36*
                       m.b39*m.b45*m.b48 + 256*m.b36*m.b40*m.b41*m.b45 + 192*m.b36*m.b40*m.b42*m.b46 + 128*m.b36*m.b40*
                       m.b43*m.b47 + 64*m.b36*m.b40*m.b44*m.b48 + 128*m.b36*m.b41*m.b42*m.b47 + 64*m.b36*m.b41*m.b43*
                       m.b48 + 640*m.b37*m.b38*m.b39*m.b40 + 576*m.b37*m.b38*m.b40*m.b41 + 512*m.b37*m.b38*m.b41*m.b42
                        + 448*m.b37*m.b38*m.b42*m.b43 + 384*m.b37*m.b38*m.b43*m.b44 + 320*m.b37*m.b38*m.b44*m.b45 + 256*
                       m.b37*m.b38*m.b45*m.b46 + 192*m.b37*m.b38*m.b46*m.b47 + 128*m.b37*m.b38*m.b47*m.b48 + 64*m.b37*
                       m.b38*m.b48*m.b49 + 512*m.b37*m.b39*m.b40*m.b42 + 448*m.b37*m.b39*m.b41*m.b43 + 384*m.b37*m.b39*
                       m.b42*m.b44 + 320*m.b37*m.b39*m.b43*m.b45 + 256*m.b37*m.b39*m.b44*m.b46 + 192*m.b37*m.b39*m.b45*
                       m.b47 + 128*m.b37*m.b39*m.b46*m.b48 + 64*m.b37*m.b39*m.b47*m.b49 + 384*m.b37*m.b40*m.b41*m.b44 + 
                       320*m.b37*m.b40*m.b42*m.b45 + 256*m.b37*m.b40*m.b43*m.b46 + 192*m.b37*m.b40*m.b44*m.b47 + 128*
                       m.b37*m.b40*m.b45*m.b48 + 64*m.b37*m.b40*m.b46*m.b49 + 256*m.b37*m.b41*m.b42*m.b46 + 192*m.b37*
                       m.b41*m.b43*m.b47 + 128*m.b37*m.b41*m.b44*m.b48 + 64*m.b37*m.b41*m.b45*m.b49 + 128*m.b37*m.b42*
                       m.b43*m.b48 + 64*m.b37*m.b42*m.b44*m.b49 + 640*m.b38*m.b39*m.b40*m.b41 + 576*m.b38*m.b39*m.b41*
                       m.b42 + 512*m.b38*m.b39*m.b42*m.b43 + 448*m.b38*m.b39*m.b43*m.b44 + 384*m.b38*m.b39*m.b44*m.b45
                        + 320*m.b38*m.b39*m.b45*m.b46 + 256*m.b38*m.b39*m.b46*m.b47 + 192*m.b38*m.b39*m.b47*m.b48 + 128*
                       m.b38*m.b39*m.b48*m.b49 + 64*m.b38*m.b39*m.b49*m.b50 + 512*m.b38*m.b40*m.b41*m.b43 + 448*m.b38*
                       m.b40*m.b42*m.b44 + 384*m.b38*m.b40*m.b43*m.b45 + 320*m.b38*m.b40*m.b44*m.b46 + 256*m.b38*m.b40*
                       m.b45*m.b47 + 192*m.b38*m.b40*m.b46*m.b48 + 128*m.b38*m.b40*m.b47*m.b49 + 64*m.b38*m.b40*m.b48*
                       m.b50 + 384*m.b38*m.b41*m.b42*m.b45 + 320*m.b38*m.b41*m.b43*m.b46 + 256*m.b38*m.b41*m.b44*m.b47
                        + 192*m.b38*m.b41*m.b45*m.b48 + 128*m.b38*m.b41*m.b46*m.b49 + 64*m.b38*m.b41*m.b47*m.b50 + 256*
                       m.b38*m.b42*m.b43*m.b47 + 192*m.b38*m.b42*m.b44*m.b48 + 128*m.b38*m.b42*m.b45*m.b49 + 64*m.b38*
                       m.b42*m.b46*m.b50 + 128*m.b38*m.b43*m.b44*m.b49 + 64*m.b38*m.b43*m.b45*m.b50 + 576*m.b39*m.b40*
                       m.b41*m.b42 + 512*m.b39*m.b40*m.b42*m.b43 + 448*m.b39*m.b40*m.b43*m.b44 + 384*m.b39*m.b40*m.b44*
                       m.b45 + 320*m.b39*m.b40*m.b45*m.b46 + 256*m.b39*m.b40*m.b46*m.b47 + 192*m.b39*m.b40*m.b47*m.b48
                        + 128*m.b39*m.b40*m.b48*m.b49 + 64*m.b39*m.b40*m.b49*m.b50 + 448*m.b39*m.b41*m.b42*m.b44 + 384*
                       m.b39*m.b41*m.b43*m.b45 + 320*m.b39*m.b41*m.b44*m.b46 + 256*m.b39*m.b41*m.b45*m.b47 + 192*m.b39*
                       m.b41*m.b46*m.b48 + 128*m.b39*m.b41*m.b47*m.b49 + 64*m.b39*m.b41*m.b48*m.b50 + 320*m.b39*m.b42*
                       m.b43*m.b46 + 256*m.b39*m.b42*m.b44*m.b47 + 192*m.b39*m.b42*m.b45*m.b48 + 128*m.b39*m.b42*m.b46*
                       m.b49 + 64*m.b39*m.b42*m.b47*m.b50 + 192*m.b39*m.b43*m.b44*m.b48 + 128*m.b39*m.b43*m.b45*m.b49 + 
                       64*m.b39*m.b43*m.b46*m.b50 + 64*m.b39*m.b44*m.b45*m.b50 + 512*m.b40*m.b41*m.b42*m.b43 + 448*m.b40
                       *m.b41*m.b43*m.b44 + 384*m.b40*m.b41*m.b44*m.b45 + 320*m.b40*m.b41*m.b45*m.b46 + 256*m.b40*m.b41*
                       m.b46*m.b47 + 192*m.b40*m.b41*m.b47*m.b48 + 128*m.b40*m.b41*m.b48*m.b49 + 64*m.b40*m.b41*m.b49*
                       m.b50 + 384*m.b40*m.b42*m.b43*m.b45 + 320*m.b40*m.b42*m.b44*m.b46 + 256*m.b40*m.b42*m.b45*m.b47
                        + 192*m.b40*m.b42*m.b46*m.b48 + 128*m.b40*m.b42*m.b47*m.b49 + 64*m.b40*m.b42*m.b48*m.b50 + 256*
                       m.b40*m.b43*m.b44*m.b47 + 192*m.b40*m.b43*m.b45*m.b48 + 128*m.b40*m.b43*m.b46*m.b49 + 64*m.b40*
                       m.b43*m.b47*m.b50 + 128*m.b40*m.b44*m.b45*m.b49 + 64*m.b40*m.b44*m.b46*m.b50 + 448*m.b41*m.b42*
                       m.b43*m.b44 + 384*m.b41*m.b42*m.b44*m.b45 + 320*m.b41*m.b42*m.b45*m.b46 + 256*m.b41*m.b42*m.b46*
                       m.b47 + 192*m.b41*m.b42*m.b47*m.b48 + 128*m.b41*m.b42*m.b48*m.b49 + 64*m.b41*m.b42*m.b49*m.b50 + 
                       320*m.b41*m.b43*m.b44*m.b46 + 256*m.b41*m.b43*m.b45*m.b47 + 192*m.b41*m.b43*m.b46*m.b48 + 128*
                       m.b41*m.b43*m.b47*m.b49 + 64*m.b41*m.b43*m.b48*m.b50 + 192*m.b41*m.b44*m.b45*m.b48 + 128*m.b41*
                       m.b44*m.b46*m.b49 + 64*m.b41*m.b44*m.b47*m.b50 + 64*m.b41*m.b45*m.b46*m.b50 + 384*m.b42*m.b43*
                       m.b44*m.b45 + 320*m.b42*m.b43*m.b45*m.b46 + 256*m.b42*m.b43*m.b46*m.b47 + 192*m.b42*m.b43*m.b47*
                       m.b48 + 128*m.b42*m.b43*m.b48*m.b49 + 64*m.b42*m.b43*m.b49*m.b50 + 256*m.b42*m.b44*m.b45*m.b47 + 
                       192*m.b42*m.b44*m.b46*m.b48 + 128*m.b42*m.b44*m.b47*m.b49 + 64*m.b42*m.b44*m.b48*m.b50 + 128*
                       m.b42*m.b45*m.b46*m.b49 + 64*m.b42*m.b45*m.b47*m.b50 + 320*m.b43*m.b44*m.b45*m.b46 + 256*m.b43*
                       m.b44*m.b46*m.b47 + 192*m.b43*m.b44*m.b47*m.b48 + 128*m.b43*m.b44*m.b48*m.b49 + 64*m.b43*m.b44*
                       m.b49*m.b50 + 192*m.b43*m.b45*m.b46*m.b48 + 128*m.b43*m.b45*m.b47*m.b49 + 64*m.b43*m.b45*m.b48*
                       m.b50 + 64*m.b43*m.b46*m.b47*m.b50 + 256*m.b44*m.b45*m.b46*m.b47 + 192*m.b44*m.b45*m.b47*m.b48 + 
                       128*m.b44*m.b45*m.b48*m.b49 + 64*m.b44*m.b45*m.b49*m.b50 + 128*m.b44*m.b46*m.b47*m.b49 + 64*m.b44
                       *m.b46*m.b48*m.b50 + 192*m.b45*m.b46*m.b47*m.b48 + 128*m.b45*m.b46*m.b48*m.b49 + 64*m.b45*m.b46*
                       m.b49*m.b50 + 64*m.b45*m.b47*m.b48*m.b50 + 128*m.b46*m.b47*m.b48*m.b49 + 64*m.b46*m.b47*m.b49*
                       m.b50 + 64*m.b47*m.b48*m.b49*m.b50 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 
                       64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*
                       m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 32*m.b1*m.b2*m.b13 - 64*m.b1*m.b3*m.b4 - 32*
                       m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 
                       64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*m.b11 - 32*m.b1*m.b3*m.b12 - 32*m.b1*m.b3*m.b13 - 64*m.b1*m.b4*
                       m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*
                       m.b4*m.b10 - 32*m.b1*m.b4*m.b11 - 32*m.b1*m.b4*m.b12 - 32*m.b1*m.b4*m.b13 - 64*m.b1*m.b5*m.b6 - 
                       64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 32*m.b1*m.b5*m.b10 - 32*m.b1*m.b5*
                       m.b11 - 32*m.b1*m.b5*m.b12 - 32*m.b1*m.b5*m.b13 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 32*m.b1
                       *m.b6*m.b9 - 32*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*m.b12 - 32*m.b1*m.b6*m.b13 - 32*m.b1*m.b7*m.b8 - 
                       32*m.b1*m.b7*m.b9 - 32*m.b1*m.b7*m.b10 - 32*m.b1*m.b7*m.b11 - 32*m.b1*m.b7*m.b12 - 32*m.b1*m.b8*
                       m.b9 - 32*m.b1*m.b8*m.b10 - 32*m.b1*m.b8*m.b11 - 32*m.b1*m.b8*m.b12 - 32*m.b1*m.b8*m.b13 - 32*
                       m.b1*m.b9*m.b10 - 32*m.b1*m.b9*m.b11 - 32*m.b1*m.b9*m.b12 - 32*m.b1*m.b9*m.b13 - 32*m.b1*m.b10*
                       m.b11 - 32*m.b1*m.b10*m.b12 - 32*m.b1*m.b10*m.b13 - 32*m.b1*m.b11*m.b12 - 32*m.b1*m.b11*m.b13 - 
                       32*m.b1*m.b12*m.b13 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3
                       *m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*m.b11 - 128
                       *m.b2*m.b3*m.b12 - 96*m.b2*m.b3*m.b13 - 32*m.b2*m.b3*m.b14 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*
                       m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*
                       m.b2*m.b4*m.b11 - 96*m.b2*m.b4*m.b12 - 64*m.b2*m.b4*m.b13 - 32*m.b2*m.b4*m.b14 - 160*m.b2*m.b5*
                       m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 96*
                       m.b2*m.b5*m.b11 - 64*m.b2*m.b5*m.b12 - 64*m.b2*m.b5*m.b13 - 32*m.b2*m.b5*m.b14 - 160*m.b2*m.b6*
                       m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*m.b6*m.b9 - 32*m.b2*m.b6*m.b10 - 64*m.b2*m.b6*m.b11 - 64*
                       m.b2*m.b6*m.b12 - 64*m.b2*m.b6*m.b13 - 32*m.b2*m.b6*m.b14 - 160*m.b2*m.b7*m.b8 - 96*m.b2*m.b7*
                       m.b9 - 64*m.b2*m.b7*m.b10 - 64*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b13 - 32*m.b2*m.b7*m.b14 - 96*
                       m.b2*m.b8*m.b9 - 64*m.b2*m.b8*m.b10 - 64*m.b2*m.b8*m.b11 - 64*m.b2*m.b8*m.b12 - 64*m.b2*m.b8*
                       m.b13 - 96*m.b2*m.b9*m.b10 - 64*m.b2*m.b9*m.b11 - 64*m.b2*m.b9*m.b12 - 64*m.b2*m.b9*m.b13 - 32*
                       m.b2*m.b9*m.b14 - 96*m.b2*m.b10*m.b11 - 64*m.b2*m.b10*m.b12 - 64*m.b2*m.b10*m.b13 - 32*m.b2*m.b10
                       *m.b14 - 96*m.b2*m.b11*m.b12 - 64*m.b2*m.b11*m.b13 - 32*m.b2*m.b11*m.b14 - 96*m.b2*m.b12*m.b13 - 
                       32*m.b2*m.b12*m.b14 - 32*m.b2*m.b13*m.b14 - 160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*
                       m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4*m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11
                        - 192*m.b3*m.b4*m.b12 - 160*m.b3*m.b4*m.b13 - 96*m.b3*m.b4*m.b14 - 32*m.b3*m.b4*m.b15 - 256*m.b3
                       *m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10
                        - 192*m.b3*m.b5*m.b11 - 160*m.b3*m.b5*m.b12 - 128*m.b3*m.b5*m.b13 - 64*m.b3*m.b5*m.b14 - 32*m.b3
                       *m.b5*m.b15 - 256*m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10
                        - 160*m.b3*m.b6*m.b11 - 128*m.b3*m.b6*m.b12 - 96*m.b3*m.b6*m.b13 - 64*m.b3*m.b6*m.b14 - 32*m.b3*
                       m.b6*m.b15 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 160*m.b3*m.b7*m.b10 - 32*m.b3*m.b7*m.b11
                        - 96*m.b3*m.b7*m.b12 - 96*m.b3*m.b7*m.b13 - 64*m.b3*m.b7*m.b14 - 32*m.b3*m.b7*m.b15 - 224*m.b3*
                       m.b8*m.b9 - 160*m.b3*m.b8*m.b10 - 96*m.b3*m.b8*m.b11 - 96*m.b3*m.b8*m.b12 - 64*m.b3*m.b8*m.b14 - 
                       32*m.b3*m.b8*m.b15 - 160*m.b3*m.b9*m.b10 - 128*m.b3*m.b9*m.b11 - 96*m.b3*m.b9*m.b12 - 96*m.b3*
                       m.b9*m.b13 - 64*m.b3*m.b9*m.b14 - 160*m.b3*m.b10*m.b11 - 128*m.b3*m.b10*m.b12 - 96*m.b3*m.b10*
                       m.b13 - 64*m.b3*m.b10*m.b14 - 32*m.b3*m.b10*m.b15 - 160*m.b3*m.b11*m.b12 - 128*m.b3*m.b11*m.b13
                        - 64*m.b3*m.b11*m.b14 - 32*m.b3*m.b11*m.b15 - 160*m.b3*m.b12*m.b13 - 64*m.b3*m.b12*m.b14 - 32*
                       m.b3*m.b12*m.b15 - 96*m.b3*m.b13*m.b14 - 32*m.b3*m.b13*m.b15 - 32*m.b3*m.b14*m.b15 - 224*m.b4*
                       m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 
                       256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 224*m.b4*m.b5*m.b13 - 160*m.b4*m.b5*m.b14 - 96*m.b4*
                       m.b5*m.b15 - 32*m.b4*m.b5*m.b16 - 352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 
                       256*m.b4*m.b6*m.b10 - 256*m.b4*m.b6*m.b11 - 224*m.b4*m.b6*m.b12 - 192*m.b4*m.b6*m.b13 - 128*m.b4*
                       m.b6*m.b14 - 64*m.b4*m.b6*m.b15 - 32*m.b4*m.b6*m.b16 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 
                       160*m.b4*m.b7*m.b10 - 224*m.b4*m.b7*m.b11 - 192*m.b4*m.b7*m.b12 - 160*m.b4*m.b7*m.b13 - 96*m.b4*
                       m.b7*m.b14 - 64*m.b4*m.b7*m.b15 - 32*m.b4*m.b7*m.b16 - 352*m.b4*m.b8*m.b9 - 288*m.b4*m.b8*m.b10
                        - 224*m.b4*m.b8*m.b11 - 32*m.b4*m.b8*m.b12 - 128*m.b4*m.b8*m.b13 - 96*m.b4*m.b8*m.b14 - 64*m.b4*
                       m.b8*m.b15 - 32*m.b4*m.b8*m.b16 - 288*m.b4*m.b9*m.b10 - 224*m.b4*m.b9*m.b11 - 160*m.b4*m.b9*m.b12
                        - 128*m.b4*m.b9*m.b13 - 64*m.b4*m.b9*m.b15 - 32*m.b4*m.b9*m.b16 - 224*m.b4*m.b10*m.b11 - 192*
                       m.b4*m.b10*m.b12 - 160*m.b4*m.b10*m.b13 - 96*m.b4*m.b10*m.b14 - 64*m.b4*m.b10*m.b15 - 224*m.b4*
                       m.b11*m.b12 - 192*m.b4*m.b11*m.b13 - 96*m.b4*m.b11*m.b14 - 64*m.b4*m.b11*m.b15 - 32*m.b4*m.b11*
                       m.b16 - 224*m.b4*m.b12*m.b13 - 128*m.b4*m.b12*m.b14 - 64*m.b4*m.b12*m.b15 - 32*m.b4*m.b12*m.b16
                        - 160*m.b4*m.b13*m.b14 - 64*m.b4*m.b13*m.b15 - 32*m.b4*m.b13*m.b16 - 96*m.b4*m.b14*m.b15 - 32*
                       m.b4*m.b14*m.b16 - 32*m.b4*m.b15*m.b16 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*
                       m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*m.b6*m.b11 - 320*m.b5*m.b6*m.b12 - 288*m.b5*m.b6*m.b13 - 
                       224*m.b5*m.b6*m.b14 - 160*m.b5*m.b6*m.b15 - 96*m.b5*m.b6*m.b16 - 32*m.b5*m.b6*m.b17 - 448*m.b5*
                       m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11 - 288*m.b5*m.b7*m.b12
                        - 256*m.b5*m.b7*m.b13 - 192*m.b5*m.b7*m.b14 - 128*m.b5*m.b7*m.b15 - 64*m.b5*m.b7*m.b16 - 32*m.b5
                       *m.b7*m.b17 - 448*m.b5*m.b8*m.b9 - 416*m.b5*m.b8*m.b10 - 192*m.b5*m.b8*m.b11 - 288*m.b5*m.b8*
                       m.b12 - 224*m.b5*m.b8*m.b13 - 160*m.b5*m.b8*m.b14 - 96*m.b5*m.b8*m.b15 - 64*m.b5*m.b8*m.b16 - 32*
                       m.b5*m.b8*m.b17 - 416*m.b5*m.b9*m.b10 - 352*m.b5*m.b9*m.b11 - 288*m.b5*m.b9*m.b12 - 64*m.b5*m.b9*
                       m.b13 - 128*m.b5*m.b9*m.b14 - 96*m.b5*m.b9*m.b15 - 64*m.b5*m.b9*m.b16 - 32*m.b5*m.b9*m.b17 - 352*
                       m.b5*m.b10*m.b11 - 288*m.b5*m.b10*m.b12 - 224*m.b5*m.b10*m.b13 - 128*m.b5*m.b10*m.b14 - 64*m.b5*
                       m.b10*m.b16 - 32*m.b5*m.b10*m.b17 - 288*m.b5*m.b11*m.b12 - 256*m.b5*m.b11*m.b13 - 160*m.b5*m.b11*
                       m.b14 - 96*m.b5*m.b11*m.b15 - 64*m.b5*m.b11*m.b16 - 288*m.b5*m.b12*m.b13 - 192*m.b5*m.b12*m.b14
                        - 96*m.b5*m.b12*m.b15 - 64*m.b5*m.b12*m.b16 - 32*m.b5*m.b12*m.b17 - 224*m.b5*m.b13*m.b14 - 128*
                       m.b5*m.b13*m.b15 - 64*m.b5*m.b13*m.b16 - 32*m.b5*m.b13*m.b17 - 160*m.b5*m.b14*m.b15 - 64*m.b5*
                       m.b14*m.b16 - 32*m.b5*m.b14*m.b17 - 96*m.b5*m.b15*m.b16 - 32*m.b5*m.b15*m.b17 - 32*m.b5*m.b16*
                       m.b17 - 352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416
                       *m.b6*m.b7*m.b12 - 352*m.b6*m.b7*m.b13 - 288*m.b6*m.b7*m.b14 - 224*m.b6*m.b7*m.b15 - 160*m.b6*
                       m.b7*m.b16 - 96*m.b6*m.b7*m.b17 - 32*m.b6*m.b7*m.b18 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10
                        - 480*m.b6*m.b8*m.b11 - 416*m.b6*m.b8*m.b12 - 352*m.b6*m.b8*m.b13 - 256*m.b6*m.b8*m.b14 - 192*
                       m.b6*m.b8*m.b15 - 128*m.b6*m.b8*m.b16 - 64*m.b6*m.b8*m.b17 - 32*m.b6*m.b8*m.b18 - 544*m.b6*m.b9*
                       m.b10 - 480*m.b6*m.b9*m.b11 - 224*m.b6*m.b9*m.b12 - 352*m.b6*m.b9*m.b13 - 224*m.b6*m.b9*m.b14 - 
                       160*m.b6*m.b9*m.b15 - 96*m.b6*m.b9*m.b16 - 64*m.b6*m.b9*m.b17 - 32*m.b6*m.b9*m.b18 - 480*m.b6*
                       m.b10*m.b11 - 416*m.b6*m.b10*m.b12 - 352*m.b6*m.b10*m.b13 - 64*m.b6*m.b10*m.b14 - 128*m.b6*m.b10*
                       m.b15 - 96*m.b6*m.b10*m.b16 - 64*m.b6*m.b10*m.b17 - 32*m.b6*m.b10*m.b18 - 416*m.b6*m.b11*m.b12 - 
                       352*m.b6*m.b11*m.b13 - 224*m.b6*m.b11*m.b14 - 128*m.b6*m.b11*m.b15 - 64*m.b6*m.b11*m.b17 - 32*
                       m.b6*m.b11*m.b18 - 352*m.b6*m.b12*m.b13 - 256*m.b6*m.b12*m.b14 - 160*m.b6*m.b12*m.b15 - 96*m.b6*
                       m.b12*m.b16 - 64*m.b6*m.b12*m.b17 - 288*m.b6*m.b13*m.b14 - 192*m.b6*m.b13*m.b15 - 96*m.b6*m.b13*
                       m.b16 - 64*m.b6*m.b13*m.b17 - 32*m.b6*m.b13*m.b18 - 224*m.b6*m.b14*m.b15 - 128*m.b6*m.b14*m.b16
                        - 64*m.b6*m.b14*m.b17 - 32*m.b6*m.b14*m.b18 - 160*m.b6*m.b15*m.b16 - 64*m.b6*m.b15*m.b17 - 32*
                       m.b6*m.b15*m.b18 - 96*m.b6*m.b16*m.b17 - 32*m.b6*m.b16*m.b18 - 32*m.b6*m.b17*m.b18 - 416*m.b7*
                       m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 480*m.b7*m.b8*m.b13
                        - 352*m.b7*m.b8*m.b14 - 288*m.b7*m.b8*m.b15 - 224*m.b7*m.b8*m.b16 - 160*m.b7*m.b8*m.b17 - 96*
                       m.b7*m.b8*m.b18 - 32*m.b7*m.b8*m.b19 - 640*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 544*m.b7*m.b9*
                       m.b12 - 480*m.b7*m.b9*m.b13 - 352*m.b7*m.b9*m.b14 - 256*m.b7*m.b9*m.b15 - 192*m.b7*m.b9*m.b16 - 
                       128*m.b7*m.b9*m.b17 - 64*m.b7*m.b9*m.b18 - 32*m.b7*m.b9*m.b19 - 608*m.b7*m.b10*m.b11 - 544*m.b7*
                       m.b10*m.b12 - 256*m.b7*m.b10*m.b13 - 352*m.b7*m.b10*m.b14 - 224*m.b7*m.b10*m.b15 - 160*m.b7*m.b10
                       *m.b16 - 96*m.b7*m.b10*m.b17 - 64*m.b7*m.b10*m.b18 - 32*m.b7*m.b10*m.b19 - 544*m.b7*m.b11*m.b12
                        - 480*m.b7*m.b11*m.b13 - 352*m.b7*m.b11*m.b14 - 64*m.b7*m.b11*m.b15 - 128*m.b7*m.b11*m.b16 - 96*
                       m.b7*m.b11*m.b17 - 64*m.b7*m.b11*m.b18 - 32*m.b7*m.b11*m.b19 - 480*m.b7*m.b12*m.b13 - 352*m.b7*
                       m.b12*m.b14 - 224*m.b7*m.b12*m.b15 - 128*m.b7*m.b12*m.b16 - 64*m.b7*m.b12*m.b18 - 32*m.b7*m.b12*
                       m.b19 - 352*m.b7*m.b13*m.b14 - 256*m.b7*m.b13*m.b15 - 160*m.b7*m.b13*m.b16 - 96*m.b7*m.b13*m.b17
                        - 64*m.b7*m.b13*m.b18 - 288*m.b7*m.b14*m.b15 - 192*m.b7*m.b14*m.b16 - 96*m.b7*m.b14*m.b17 - 64*
                       m.b7*m.b14*m.b18 - 32*m.b7*m.b14*m.b19 - 224*m.b7*m.b15*m.b16 - 128*m.b7*m.b15*m.b17 - 64*m.b7*
                       m.b15*m.b18 - 32*m.b7*m.b15*m.b19 - 160*m.b7*m.b16*m.b17 - 64*m.b7*m.b16*m.b18 - 32*m.b7*m.b16*
                       m.b19 - 96*m.b7*m.b17*m.b18 - 32*m.b7*m.b17*m.b19 - 32*m.b7*m.b18*m.b19 - 480*m.b8*m.b9*m.b10 - 
                       704*m.b8*m.b9*m.b11 - 672*m.b8*m.b9*m.b12 - 608*m.b8*m.b9*m.b13 - 480*m.b8*m.b9*m.b14 - 352*m.b8*
                       m.b9*m.b15 - 288*m.b8*m.b9*m.b16 - 224*m.b8*m.b9*m.b17 - 160*m.b8*m.b9*m.b18 - 96*m.b8*m.b9*m.b19
                        - 32*m.b8*m.b9*m.b20 - 736*m.b8*m.b10*m.b11 - 416*m.b8*m.b10*m.b12 - 608*m.b8*m.b10*m.b13 - 480*
                       m.b8*m.b10*m.b14 - 352*m.b8*m.b10*m.b15 - 256*m.b8*m.b10*m.b16 - 192*m.b8*m.b10*m.b17 - 128*m.b8*
                       m.b10*m.b18 - 64*m.b8*m.b10*m.b19 - 32*m.b8*m.b10*m.b20 - 672*m.b8*m.b11*m.b12 - 608*m.b8*m.b11*
                       m.b13 - 256*m.b8*m.b11*m.b14 - 352*m.b8*m.b11*m.b15 - 224*m.b8*m.b11*m.b16 - 160*m.b8*m.b11*m.b17
                        - 96*m.b8*m.b11*m.b18 - 64*m.b8*m.b11*m.b19 - 32*m.b8*m.b11*m.b20 - 608*m.b8*m.b12*m.b13 - 480*
                       m.b8*m.b12*m.b14 - 352*m.b8*m.b12*m.b15 - 64*m.b8*m.b12*m.b16 - 128*m.b8*m.b12*m.b17 - 96*m.b8*
                       m.b12*m.b18 - 64*m.b8*m.b12*m.b19 - 32*m.b8*m.b12*m.b20 - 480*m.b8*m.b13*m.b14 - 352*m.b8*m.b13*
                       m.b15 - 224*m.b8*m.b13*m.b16 - 128*m.b8*m.b13*m.b17 - 64*m.b8*m.b13*m.b19 - 32*m.b8*m.b13*m.b20
                        - 352*m.b8*m.b14*m.b15 - 256*m.b8*m.b14*m.b16 - 160*m.b8*m.b14*m.b17 - 96*m.b8*m.b14*m.b18 - 64*
                       m.b8*m.b14*m.b19 - 288*m.b8*m.b15*m.b16 - 192*m.b8*m.b15*m.b17 - 96*m.b8*m.b15*m.b18 - 64*m.b8*
                       m.b15*m.b19 - 32*m.b8*m.b15*m.b20 - 224*m.b8*m.b16*m.b17 - 128*m.b8*m.b16*m.b18 - 64*m.b8*m.b16*
                       m.b19 - 32*m.b8*m.b16*m.b20 - 160*m.b8*m.b17*m.b18 - 64*m.b8*m.b17*m.b19 - 32*m.b8*m.b17*m.b20 - 
                       96*m.b8*m.b18*m.b19 - 32*m.b8*m.b18*m.b20 - 32*m.b8*m.b19*m.b20 - 544*m.b9*m.b10*m.b11 - 800*m.b9
                       *m.b10*m.b12 - 736*m.b9*m.b10*m.b13 - 608*m.b9*m.b10*m.b14 - 480*m.b9*m.b10*m.b15 - 352*m.b9*
                       m.b10*m.b16 - 288*m.b9*m.b10*m.b17 - 224*m.b9*m.b10*m.b18 - 160*m.b9*m.b10*m.b19 - 96*m.b9*m.b10*
                       m.b20 - 32*m.b9*m.b10*m.b21 - 800*m.b9*m.b11*m.b12 - 448*m.b9*m.b11*m.b13 - 608*m.b9*m.b11*m.b14
                        - 480*m.b9*m.b11*m.b15 - 352*m.b9*m.b11*m.b16 - 256*m.b9*m.b11*m.b17 - 192*m.b9*m.b11*m.b18 - 
                       128*m.b9*m.b11*m.b19 - 64*m.b9*m.b11*m.b20 - 32*m.b9*m.b11*m.b21 - 736*m.b9*m.b12*m.b13 - 608*
                       m.b9*m.b12*m.b14 - 256*m.b9*m.b12*m.b15 - 352*m.b9*m.b12*m.b16 - 224*m.b9*m.b12*m.b17 - 160*m.b9*
                       m.b12*m.b18 - 96*m.b9*m.b12*m.b19 - 64*m.b9*m.b12*m.b20 - 32*m.b9*m.b12*m.b21 - 608*m.b9*m.b13*
                       m.b14 - 480*m.b9*m.b13*m.b15 - 352*m.b9*m.b13*m.b16 - 64*m.b9*m.b13*m.b17 - 128*m.b9*m.b13*m.b18
                        - 96*m.b9*m.b13*m.b19 - 64*m.b9*m.b13*m.b20 - 32*m.b9*m.b13*m.b21 - 480*m.b9*m.b14*m.b15 - 352*
                       m.b9*m.b14*m.b16 - 224*m.b9*m.b14*m.b17 - 128*m.b9*m.b14*m.b18 - 64*m.b9*m.b14*m.b20 - 32*m.b9*
                       m.b14*m.b21 - 352*m.b9*m.b15*m.b16 - 256*m.b9*m.b15*m.b17 - 160*m.b9*m.b15*m.b18 - 96*m.b9*m.b15*
                       m.b19 - 64*m.b9*m.b15*m.b20 - 288*m.b9*m.b16*m.b17 - 192*m.b9*m.b16*m.b18 - 96*m.b9*m.b16*m.b19
                        - 64*m.b9*m.b16*m.b20 - 32*m.b9*m.b16*m.b21 - 224*m.b9*m.b17*m.b18 - 128*m.b9*m.b17*m.b19 - 64*
                       m.b9*m.b17*m.b20 - 32*m.b9*m.b17*m.b21 - 160*m.b9*m.b18*m.b19 - 64*m.b9*m.b18*m.b20 - 32*m.b9*
                       m.b18*m.b21 - 96*m.b9*m.b19*m.b20 - 32*m.b9*m.b19*m.b21 - 32*m.b9*m.b20*m.b21 - 608*m.b10*m.b11*
                       m.b12 - 864*m.b10*m.b11*m.b13 - 736*m.b10*m.b11*m.b14 - 608*m.b10*m.b11*m.b15 - 480*m.b10*m.b11*
                       m.b16 - 352*m.b10*m.b11*m.b17 - 288*m.b10*m.b11*m.b18 - 224*m.b10*m.b11*m.b19 - 160*m.b10*m.b11*
                       m.b20 - 96*m.b10*m.b11*m.b21 - 32*m.b10*m.b11*m.b22 - 864*m.b10*m.b12*m.b13 - 448*m.b10*m.b12*
                       m.b14 - 608*m.b10*m.b12*m.b15 - 480*m.b10*m.b12*m.b16 - 352*m.b10*m.b12*m.b17 - 256*m.b10*m.b12*
                       m.b18 - 192*m.b10*m.b12*m.b19 - 128*m.b10*m.b12*m.b20 - 64*m.b10*m.b12*m.b21 - 32*m.b10*m.b12*
                       m.b22 - 736*m.b10*m.b13*m.b14 - 608*m.b10*m.b13*m.b15 - 256*m.b10*m.b13*m.b16 - 352*m.b10*m.b13*
                       m.b17 - 224*m.b10*m.b13*m.b18 - 160*m.b10*m.b13*m.b19 - 96*m.b10*m.b13*m.b20 - 64*m.b10*m.b13*
                       m.b21 - 32*m.b10*m.b13*m.b22 - 608*m.b10*m.b14*m.b15 - 480*m.b10*m.b14*m.b16 - 352*m.b10*m.b14*
                       m.b17 - 64*m.b10*m.b14*m.b18 - 128*m.b10*m.b14*m.b19 - 96*m.b10*m.b14*m.b20 - 64*m.b10*m.b14*
                       m.b21 - 32*m.b10*m.b14*m.b22 - 480*m.b10*m.b15*m.b16 - 352*m.b10*m.b15*m.b17 - 224*m.b10*m.b15*
                       m.b18 - 128*m.b10*m.b15*m.b19 - 64*m.b10*m.b15*m.b21 - 32*m.b10*m.b15*m.b22 - 352*m.b10*m.b16*
                       m.b17 - 256*m.b10*m.b16*m.b18 - 160*m.b10*m.b16*m.b19 - 96*m.b10*m.b16*m.b20 - 64*m.b10*m.b16*
                       m.b21 - 288*m.b10*m.b17*m.b18 - 192*m.b10*m.b17*m.b19 - 96*m.b10*m.b17*m.b20 - 64*m.b10*m.b17*
                       m.b21 - 32*m.b10*m.b17*m.b22 - 224*m.b10*m.b18*m.b19 - 128*m.b10*m.b18*m.b20 - 64*m.b10*m.b18*
                       m.b21 - 32*m.b10*m.b18*m.b22 - 160*m.b10*m.b19*m.b20 - 64*m.b10*m.b19*m.b21 - 32*m.b10*m.b19*
                       m.b22 - 96*m.b10*m.b20*m.b21 - 32*m.b10*m.b20*m.b22 - 32*m.b10*m.b21*m.b22 - 640*m.b11*m.b12*
                       m.b13 - 864*m.b11*m.b12*m.b14 - 736*m.b11*m.b12*m.b15 - 608*m.b11*m.b12*m.b16 - 480*m.b11*m.b12*
                       m.b17 - 352*m.b11*m.b12*m.b18 - 288*m.b11*m.b12*m.b19 - 224*m.b11*m.b12*m.b20 - 160*m.b11*m.b12*
                       m.b21 - 96*m.b11*m.b12*m.b22 - 32*m.b11*m.b12*m.b23 - 864*m.b11*m.b13*m.b14 - 448*m.b11*m.b13*
                       m.b15 - 608*m.b11*m.b13*m.b16 - 480*m.b11*m.b13*m.b17 - 352*m.b11*m.b13*m.b18 - 256*m.b11*m.b13*
                       m.b19 - 192*m.b11*m.b13*m.b20 - 128*m.b11*m.b13*m.b21 - 64*m.b11*m.b13*m.b22 - 32*m.b11*m.b13*
                       m.b23 - 736*m.b11*m.b14*m.b15 - 608*m.b11*m.b14*m.b16 - 256*m.b11*m.b14*m.b17 - 352*m.b11*m.b14*
                       m.b18 - 224*m.b11*m.b14*m.b19 - 160*m.b11*m.b14*m.b20 - 96*m.b11*m.b14*m.b21 - 64*m.b11*m.b14*
                       m.b22 - 32*m.b11*m.b14*m.b23 - 608*m.b11*m.b15*m.b16 - 480*m.b11*m.b15*m.b17 - 352*m.b11*m.b15*
                       m.b18 - 64*m.b11*m.b15*m.b19 - 128*m.b11*m.b15*m.b20 - 96*m.b11*m.b15*m.b21 - 64*m.b11*m.b15*
                       m.b22 - 32*m.b11*m.b15*m.b23 - 480*m.b11*m.b16*m.b17 - 352*m.b11*m.b16*m.b18 - 224*m.b11*m.b16*
                       m.b19 - 128*m.b11*m.b16*m.b20 - 64*m.b11*m.b16*m.b22 - 32*m.b11*m.b16*m.b23 - 352*m.b11*m.b17*
                       m.b18 - 256*m.b11*m.b17*m.b19 - 160*m.b11*m.b17*m.b20 - 96*m.b11*m.b17*m.b21 - 64*m.b11*m.b17*
                       m.b22 - 288*m.b11*m.b18*m.b19 - 192*m.b11*m.b18*m.b20 - 96*m.b11*m.b18*m.b21 - 64*m.b11*m.b18*
                       m.b22 - 32*m.b11*m.b18*m.b23 - 224*m.b11*m.b19*m.b20 - 128*m.b11*m.b19*m.b21 - 64*m.b11*m.b19*
                       m.b22 - 32*m.b11*m.b19*m.b23 - 160*m.b11*m.b20*m.b21 - 64*m.b11*m.b20*m.b22 - 32*m.b11*m.b20*
                       m.b23 - 96*m.b11*m.b21*m.b22 - 32*m.b11*m.b21*m.b23 - 32*m.b11*m.b22*m.b23 - 640*m.b12*m.b13*
                       m.b14 - 864*m.b12*m.b13*m.b15 - 736*m.b12*m.b13*m.b16 - 608*m.b12*m.b13*m.b17 - 480*m.b12*m.b13*
                       m.b18 - 352*m.b12*m.b13*m.b19 - 288*m.b12*m.b13*m.b20 - 224*m.b12*m.b13*m.b21 - 160*m.b12*m.b13*
                       m.b22 - 96*m.b12*m.b13*m.b23 - 32*m.b12*m.b13*m.b24 - 864*m.b12*m.b14*m.b15 - 448*m.b12*m.b14*
                       m.b16 - 608*m.b12*m.b14*m.b17 - 480*m.b12*m.b14*m.b18 - 352*m.b12*m.b14*m.b19 - 256*m.b12*m.b14*
                       m.b20 - 192*m.b12*m.b14*m.b21 - 128*m.b12*m.b14*m.b22 - 64*m.b12*m.b14*m.b23 - 32*m.b12*m.b14*
                       m.b24 - 736*m.b12*m.b15*m.b16 - 608*m.b12*m.b15*m.b17 - 256*m.b12*m.b15*m.b18 - 352*m.b12*m.b15*
                       m.b19 - 224*m.b12*m.b15*m.b20 - 160*m.b12*m.b15*m.b21 - 96*m.b12*m.b15*m.b22 - 64*m.b12*m.b15*
                       m.b23 - 32*m.b12*m.b15*m.b24 - 608*m.b12*m.b16*m.b17 - 480*m.b12*m.b16*m.b18 - 352*m.b12*m.b16*
                       m.b19 - 64*m.b12*m.b16*m.b20 - 128*m.b12*m.b16*m.b21 - 96*m.b12*m.b16*m.b22 - 64*m.b12*m.b16*
                       m.b23 - 32*m.b12*m.b16*m.b24 - 480*m.b12*m.b17*m.b18 - 352*m.b12*m.b17*m.b19 - 224*m.b12*m.b17*
                       m.b20 - 128*m.b12*m.b17*m.b21 - 64*m.b12*m.b17*m.b23 - 32*m.b12*m.b17*m.b24 - 352*m.b12*m.b18*
                       m.b19 - 256*m.b12*m.b18*m.b20 - 160*m.b12*m.b18*m.b21 - 96*m.b12*m.b18*m.b22 - 64*m.b12*m.b18*
                       m.b23 - 288*m.b12*m.b19*m.b20 - 192*m.b12*m.b19*m.b21 - 96*m.b12*m.b19*m.b22 - 64*m.b12*m.b19*
                       m.b23 - 32*m.b12*m.b19*m.b24 - 224*m.b12*m.b20*m.b21 - 128*m.b12*m.b20*m.b22 - 64*m.b12*m.b20*
                       m.b23 - 32*m.b12*m.b20*m.b24 - 160*m.b12*m.b21*m.b22 - 64*m.b12*m.b21*m.b23 - 32*m.b12*m.b21*
                       m.b24 - 96*m.b12*m.b22*m.b23 - 32*m.b12*m.b22*m.b24 - 32*m.b12*m.b23*m.b24 - 640*m.b13*m.b14*
                       m.b15 - 864*m.b13*m.b14*m.b16 - 736*m.b13*m.b14*m.b17 - 608*m.b13*m.b14*m.b18 - 480*m.b13*m.b14*
                       m.b19 - 352*m.b13*m.b14*m.b20 - 288*m.b13*m.b14*m.b21 - 224*m.b13*m.b14*m.b22 - 160*m.b13*m.b14*
                       m.b23 - 96*m.b13*m.b14*m.b24 - 32*m.b13*m.b14*m.b25 - 864*m.b13*m.b15*m.b16 - 448*m.b13*m.b15*
                       m.b17 - 608*m.b13*m.b15*m.b18 - 480*m.b13*m.b15*m.b19 - 352*m.b13*m.b15*m.b20 - 256*m.b13*m.b15*
                       m.b21 - 192*m.b13*m.b15*m.b22 - 128*m.b13*m.b15*m.b23 - 64*m.b13*m.b15*m.b24 - 32*m.b13*m.b15*
                       m.b25 - 736*m.b13*m.b16*m.b17 - 608*m.b13*m.b16*m.b18 - 256*m.b13*m.b16*m.b19 - 352*m.b13*m.b16*
                       m.b20 - 224*m.b13*m.b16*m.b21 - 160*m.b13*m.b16*m.b22 - 96*m.b13*m.b16*m.b23 - 64*m.b13*m.b16*
                       m.b24 - 32*m.b13*m.b16*m.b25 - 608*m.b13*m.b17*m.b18 - 480*m.b13*m.b17*m.b19 - 352*m.b13*m.b17*
                       m.b20 - 64*m.b13*m.b17*m.b21 - 128*m.b13*m.b17*m.b22 - 96*m.b13*m.b17*m.b23 - 64*m.b13*m.b17*
                       m.b24 - 32*m.b13*m.b17*m.b25 - 480*m.b13*m.b18*m.b19 - 352*m.b13*m.b18*m.b20 - 224*m.b13*m.b18*
                       m.b21 - 128*m.b13*m.b18*m.b22 - 64*m.b13*m.b18*m.b24 - 32*m.b13*m.b18*m.b25 - 352*m.b13*m.b19*
                       m.b20 - 256*m.b13*m.b19*m.b21 - 160*m.b13*m.b19*m.b22 - 96*m.b13*m.b19*m.b23 - 64*m.b13*m.b19*
                       m.b24 - 288*m.b13*m.b20*m.b21 - 192*m.b13*m.b20*m.b22 - 96*m.b13*m.b20*m.b23 - 64*m.b13*m.b20*
                       m.b24 - 32*m.b13*m.b20*m.b25 - 224*m.b13*m.b21*m.b22 - 128*m.b13*m.b21*m.b23 - 64*m.b13*m.b21*
                       m.b24 - 32*m.b13*m.b21*m.b25 - 160*m.b13*m.b22*m.b23 - 64*m.b13*m.b22*m.b24 - 32*m.b13*m.b22*
                       m.b25 - 96*m.b13*m.b23*m.b24 - 32*m.b13*m.b23*m.b25 - 32*m.b13*m.b24*m.b25 - 640*m.b14*m.b15*
                       m.b16 - 864*m.b14*m.b15*m.b17 - 736*m.b14*m.b15*m.b18 - 608*m.b14*m.b15*m.b19 - 480*m.b14*m.b15*
                       m.b20 - 352*m.b14*m.b15*m.b21 - 288*m.b14*m.b15*m.b22 - 224*m.b14*m.b15*m.b23 - 160*m.b14*m.b15*
                       m.b24 - 96*m.b14*m.b15*m.b25 - 32*m.b14*m.b15*m.b26 - 864*m.b14*m.b16*m.b17 - 448*m.b14*m.b16*
                       m.b18 - 608*m.b14*m.b16*m.b19 - 480*m.b14*m.b16*m.b20 - 352*m.b14*m.b16*m.b21 - 256*m.b14*m.b16*
                       m.b22 - 192*m.b14*m.b16*m.b23 - 128*m.b14*m.b16*m.b24 - 64*m.b14*m.b16*m.b25 - 32*m.b14*m.b16*
                       m.b26 - 736*m.b14*m.b17*m.b18 - 608*m.b14*m.b17*m.b19 - 256*m.b14*m.b17*m.b20 - 352*m.b14*m.b17*
                       m.b21 - 224*m.b14*m.b17*m.b22 - 160*m.b14*m.b17*m.b23 - 96*m.b14*m.b17*m.b24 - 64*m.b14*m.b17*
                       m.b25 - 32*m.b14*m.b17*m.b26 - 608*m.b14*m.b18*m.b19 - 480*m.b14*m.b18*m.b20 - 352*m.b14*m.b18*
                       m.b21 - 64*m.b14*m.b18*m.b22 - 128*m.b14*m.b18*m.b23 - 96*m.b14*m.b18*m.b24 - 64*m.b14*m.b18*
                       m.b25 - 32*m.b14*m.b18*m.b26 - 480*m.b14*m.b19*m.b20 - 352*m.b14*m.b19*m.b21 - 224*m.b14*m.b19*
                       m.b22 - 128*m.b14*m.b19*m.b23 - 64*m.b14*m.b19*m.b25 - 32*m.b14*m.b19*m.b26 - 352*m.b14*m.b20*
                       m.b21 - 256*m.b14*m.b20*m.b22 - 160*m.b14*m.b20*m.b23 - 96*m.b14*m.b20*m.b24 - 64*m.b14*m.b20*
                       m.b25 - 288*m.b14*m.b21*m.b22 - 192*m.b14*m.b21*m.b23 - 96*m.b14*m.b21*m.b24 - 64*m.b14*m.b21*
                       m.b25 - 32*m.b14*m.b21*m.b26 - 224*m.b14*m.b22*m.b23 - 128*m.b14*m.b22*m.b24 - 64*m.b14*m.b22*
                       m.b25 - 32*m.b14*m.b22*m.b26 - 160*m.b14*m.b23*m.b24 - 64*m.b14*m.b23*m.b25 - 32*m.b14*m.b23*
                       m.b26 - 96*m.b14*m.b24*m.b25 - 32*m.b14*m.b24*m.b26 - 32*m.b14*m.b25*m.b26 - 640*m.b15*m.b16*
                       m.b17 - 864*m.b15*m.b16*m.b18 - 736*m.b15*m.b16*m.b19 - 608*m.b15*m.b16*m.b20 - 480*m.b15*m.b16*
                       m.b21 - 352*m.b15*m.b16*m.b22 - 288*m.b15*m.b16*m.b23 - 224*m.b15*m.b16*m.b24 - 160*m.b15*m.b16*
                       m.b25 - 96*m.b15*m.b16*m.b26 - 32*m.b15*m.b16*m.b27 - 864*m.b15*m.b17*m.b18 - 448*m.b15*m.b17*
                       m.b19 - 608*m.b15*m.b17*m.b20 - 480*m.b15*m.b17*m.b21 - 352*m.b15*m.b17*m.b22 - 256*m.b15*m.b17*
                       m.b23 - 192*m.b15*m.b17*m.b24 - 128*m.b15*m.b17*m.b25 - 64*m.b15*m.b17*m.b26 - 32*m.b15*m.b17*
                       m.b27 - 736*m.b15*m.b18*m.b19 - 608*m.b15*m.b18*m.b20 - 256*m.b15*m.b18*m.b21 - 352*m.b15*m.b18*
                       m.b22 - 224*m.b15*m.b18*m.b23 - 160*m.b15*m.b18*m.b24 - 96*m.b15*m.b18*m.b25 - 64*m.b15*m.b18*
                       m.b26 - 32*m.b15*m.b18*m.b27 - 608*m.b15*m.b19*m.b20 - 480*m.b15*m.b19*m.b21 - 352*m.b15*m.b19*
                       m.b22 - 64*m.b15*m.b19*m.b23 - 128*m.b15*m.b19*m.b24 - 96*m.b15*m.b19*m.b25 - 64*m.b15*m.b19*
                       m.b26 - 32*m.b15*m.b19*m.b27 - 480*m.b15*m.b20*m.b21 - 352*m.b15*m.b20*m.b22 - 224*m.b15*m.b20*
                       m.b23 - 128*m.b15*m.b20*m.b24 - 64*m.b15*m.b20*m.b26 - 32*m.b15*m.b20*m.b27 - 352*m.b15*m.b21*
                       m.b22 - 256*m.b15*m.b21*m.b23 - 160*m.b15*m.b21*m.b24 - 96*m.b15*m.b21*m.b25 - 64*m.b15*m.b21*
                       m.b26 - 288*m.b15*m.b22*m.b23 - 192*m.b15*m.b22*m.b24 - 96*m.b15*m.b22*m.b25 - 64*m.b15*m.b22*
                       m.b26 - 32*m.b15*m.b22*m.b27 - 224*m.b15*m.b23*m.b24 - 128*m.b15*m.b23*m.b25 - 64*m.b15*m.b23*
                       m.b26 - 32*m.b15*m.b23*m.b27 - 160*m.b15*m.b24*m.b25 - 64*m.b15*m.b24*m.b26 - 32*m.b15*m.b24*
                       m.b27 - 96*m.b15*m.b25*m.b26 - 32*m.b15*m.b25*m.b27 - 32*m.b15*m.b26*m.b27 - 640*m.b16*m.b17*
                       m.b18 - 864*m.b16*m.b17*m.b19 - 736*m.b16*m.b17*m.b20 - 608*m.b16*m.b17*m.b21 - 480*m.b16*m.b17*
                       m.b22 - 352*m.b16*m.b17*m.b23 - 288*m.b16*m.b17*m.b24 - 224*m.b16*m.b17*m.b25 - 160*m.b16*m.b17*
                       m.b26 - 96*m.b16*m.b17*m.b27 - 32*m.b16*m.b17*m.b28 - 864*m.b16*m.b18*m.b19 - 448*m.b16*m.b18*
                       m.b20 - 608*m.b16*m.b18*m.b21 - 480*m.b16*m.b18*m.b22 - 352*m.b16*m.b18*m.b23 - 256*m.b16*m.b18*
                       m.b24 - 192*m.b16*m.b18*m.b25 - 128*m.b16*m.b18*m.b26 - 64*m.b16*m.b18*m.b27 - 32*m.b16*m.b18*
                       m.b28 - 736*m.b16*m.b19*m.b20 - 608*m.b16*m.b19*m.b21 - 256*m.b16*m.b19*m.b22 - 352*m.b16*m.b19*
                       m.b23 - 224*m.b16*m.b19*m.b24 - 160*m.b16*m.b19*m.b25 - 96*m.b16*m.b19*m.b26 - 64*m.b16*m.b19*
                       m.b27 - 32*m.b16*m.b19*m.b28 - 608*m.b16*m.b20*m.b21 - 480*m.b16*m.b20*m.b22 - 352*m.b16*m.b20*
                       m.b23 - 64*m.b16*m.b20*m.b24 - 128*m.b16*m.b20*m.b25 - 96*m.b16*m.b20*m.b26 - 64*m.b16*m.b20*
                       m.b27 - 32*m.b16*m.b20*m.b28 - 480*m.b16*m.b21*m.b22 - 352*m.b16*m.b21*m.b23 - 224*m.b16*m.b21*
                       m.b24 - 128*m.b16*m.b21*m.b25 - 64*m.b16*m.b21*m.b27 - 32*m.b16*m.b21*m.b28 - 352*m.b16*m.b22*
                       m.b23 - 256*m.b16*m.b22*m.b24 - 160*m.b16*m.b22*m.b25 - 96*m.b16*m.b22*m.b26 - 64*m.b16*m.b22*
                       m.b27 - 288*m.b16*m.b23*m.b24 - 192*m.b16*m.b23*m.b25 - 96*m.b16*m.b23*m.b26 - 64*m.b16*m.b23*
                       m.b27 - 32*m.b16*m.b23*m.b28 - 224*m.b16*m.b24*m.b25 - 128*m.b16*m.b24*m.b26 - 64*m.b16*m.b24*
                       m.b27 - 32*m.b16*m.b24*m.b28 - 160*m.b16*m.b25*m.b26 - 64*m.b16*m.b25*m.b27 - 32*m.b16*m.b25*
                       m.b28 - 96*m.b16*m.b26*m.b27 - 32*m.b16*m.b26*m.b28 - 32*m.b16*m.b27*m.b28 - 640*m.b17*m.b18*
                       m.b19 - 864*m.b17*m.b18*m.b20 - 736*m.b17*m.b18*m.b21 - 608*m.b17*m.b18*m.b22 - 480*m.b17*m.b18*
                       m.b23 - 352*m.b17*m.b18*m.b24 - 288*m.b17*m.b18*m.b25 - 224*m.b17*m.b18*m.b26 - 160*m.b17*m.b18*
                       m.b27 - 96*m.b17*m.b18*m.b28 - 32*m.b17*m.b18*m.b29 - 864*m.b17*m.b19*m.b20 - 448*m.b17*m.b19*
                       m.b21 - 608*m.b17*m.b19*m.b22 - 480*m.b17*m.b19*m.b23 - 352*m.b17*m.b19*m.b24 - 256*m.b17*m.b19*
                       m.b25 - 192*m.b17*m.b19*m.b26 - 128*m.b17*m.b19*m.b27 - 64*m.b17*m.b19*m.b28 - 32*m.b17*m.b19*
                       m.b29 - 736*m.b17*m.b20*m.b21 - 608*m.b17*m.b20*m.b22 - 256*m.b17*m.b20*m.b23 - 352*m.b17*m.b20*
                       m.b24 - 224*m.b17*m.b20*m.b25 - 160*m.b17*m.b20*m.b26 - 96*m.b17*m.b20*m.b27 - 64*m.b17*m.b20*
                       m.b28 - 32*m.b17*m.b20*m.b29 - 608*m.b17*m.b21*m.b22 - 480*m.b17*m.b21*m.b23 - 352*m.b17*m.b21*
                       m.b24 - 64*m.b17*m.b21*m.b25 - 128*m.b17*m.b21*m.b26 - 96*m.b17*m.b21*m.b27 - 64*m.b17*m.b21*
                       m.b28 - 32*m.b17*m.b21*m.b29 - 480*m.b17*m.b22*m.b23 - 352*m.b17*m.b22*m.b24 - 224*m.b17*m.b22*
                       m.b25 - 128*m.b17*m.b22*m.b26 - 64*m.b17*m.b22*m.b28 - 32*m.b17*m.b22*m.b29 - 352*m.b17*m.b23*
                       m.b24 - 256*m.b17*m.b23*m.b25 - 160*m.b17*m.b23*m.b26 - 96*m.b17*m.b23*m.b27 - 64*m.b17*m.b23*
                       m.b28 - 288*m.b17*m.b24*m.b25 - 192*m.b17*m.b24*m.b26 - 96*m.b17*m.b24*m.b27 - 64*m.b17*m.b24*
                       m.b28 - 32*m.b17*m.b24*m.b29 - 224*m.b17*m.b25*m.b26 - 128*m.b17*m.b25*m.b27 - 64*m.b17*m.b25*
                       m.b28 - 32*m.b17*m.b25*m.b29 - 160*m.b17*m.b26*m.b27 - 64*m.b17*m.b26*m.b28 - 32*m.b17*m.b26*
                       m.b29 - 96*m.b17*m.b27*m.b28 - 32*m.b17*m.b27*m.b29 - 32*m.b17*m.b28*m.b29 - 640*m.b18*m.b19*
                       m.b20 - 864*m.b18*m.b19*m.b21 - 736*m.b18*m.b19*m.b22 - 608*m.b18*m.b19*m.b23 - 480*m.b18*m.b19*
                       m.b24 - 352*m.b18*m.b19*m.b25 - 288*m.b18*m.b19*m.b26 - 224*m.b18*m.b19*m.b27 - 160*m.b18*m.b19*
                       m.b28 - 96*m.b18*m.b19*m.b29 - 32*m.b18*m.b19*m.b30 - 864*m.b18*m.b20*m.b21 - 448*m.b18*m.b20*
                       m.b22 - 608*m.b18*m.b20*m.b23 - 480*m.b18*m.b20*m.b24 - 352*m.b18*m.b20*m.b25 - 256*m.b18*m.b20*
                       m.b26 - 192*m.b18*m.b20*m.b27 - 128*m.b18*m.b20*m.b28 - 64*m.b18*m.b20*m.b29 - 32*m.b18*m.b20*
                       m.b30 - 736*m.b18*m.b21*m.b22 - 608*m.b18*m.b21*m.b23 - 256*m.b18*m.b21*m.b24 - 352*m.b18*m.b21*
                       m.b25 - 224*m.b18*m.b21*m.b26 - 160*m.b18*m.b21*m.b27 - 96*m.b18*m.b21*m.b28 - 64*m.b18*m.b21*
                       m.b29 - 32*m.b18*m.b21*m.b30 - 608*m.b18*m.b22*m.b23 - 480*m.b18*m.b22*m.b24 - 352*m.b18*m.b22*
                       m.b25 - 64*m.b18*m.b22*m.b26 - 128*m.b18*m.b22*m.b27 - 96*m.b18*m.b22*m.b28 - 64*m.b18*m.b22*
                       m.b29 - 32*m.b18*m.b22*m.b30 - 480*m.b18*m.b23*m.b24 - 352*m.b18*m.b23*m.b25 - 224*m.b18*m.b23*
                       m.b26 - 128*m.b18*m.b23*m.b27 - 64*m.b18*m.b23*m.b29 - 32*m.b18*m.b23*m.b30 - 352*m.b18*m.b24*
                       m.b25 - 256*m.b18*m.b24*m.b26 - 160*m.b18*m.b24*m.b27 - 96*m.b18*m.b24*m.b28 - 64*m.b18*m.b24*
                       m.b29 - 288*m.b18*m.b25*m.b26 - 192*m.b18*m.b25*m.b27 - 96*m.b18*m.b25*m.b28 - 64*m.b18*m.b25*
                       m.b29 - 32*m.b18*m.b25*m.b30 - 224*m.b18*m.b26*m.b27 - 128*m.b18*m.b26*m.b28 - 64*m.b18*m.b26*
                       m.b29 - 32*m.b18*m.b26*m.b30 - 160*m.b18*m.b27*m.b28 - 64*m.b18*m.b27*m.b29 - 32*m.b18*m.b27*
                       m.b30 - 96*m.b18*m.b28*m.b29 - 32*m.b18*m.b28*m.b30 - 32*m.b18*m.b29*m.b30 - 640*m.b19*m.b20*
                       m.b21 - 864*m.b19*m.b20*m.b22 - 736*m.b19*m.b20*m.b23 - 608*m.b19*m.b20*m.b24 - 480*m.b19*m.b20*
                       m.b25 - 352*m.b19*m.b20*m.b26 - 288*m.b19*m.b20*m.b27 - 224*m.b19*m.b20*m.b28 - 160*m.b19*m.b20*
                       m.b29 - 96*m.b19*m.b20*m.b30 - 32*m.b19*m.b20*m.b31 - 864*m.b19*m.b21*m.b22 - 448*m.b19*m.b21*
                       m.b23 - 608*m.b19*m.b21*m.b24 - 480*m.b19*m.b21*m.b25 - 352*m.b19*m.b21*m.b26 - 256*m.b19*m.b21*
                       m.b27 - 192*m.b19*m.b21*m.b28 - 128*m.b19*m.b21*m.b29 - 64*m.b19*m.b21*m.b30 - 32*m.b19*m.b21*
                       m.b31 - 736*m.b19*m.b22*m.b23 - 608*m.b19*m.b22*m.b24 - 256*m.b19*m.b22*m.b25 - 352*m.b19*m.b22*
                       m.b26 - 224*m.b19*m.b22*m.b27 - 160*m.b19*m.b22*m.b28 - 96*m.b19*m.b22*m.b29 - 64*m.b19*m.b22*
                       m.b30 - 32*m.b19*m.b22*m.b31 - 608*m.b19*m.b23*m.b24 - 480*m.b19*m.b23*m.b25 - 352*m.b19*m.b23*
                       m.b26 - 64*m.b19*m.b23*m.b27 - 128*m.b19*m.b23*m.b28 - 96*m.b19*m.b23*m.b29 - 64*m.b19*m.b23*
                       m.b30 - 32*m.b19*m.b23*m.b31 - 480*m.b19*m.b24*m.b25 - 352*m.b19*m.b24*m.b26 - 224*m.b19*m.b24*
                       m.b27 - 128*m.b19*m.b24*m.b28 - 64*m.b19*m.b24*m.b30 - 32*m.b19*m.b24*m.b31 - 352*m.b19*m.b25*
                       m.b26 - 256*m.b19*m.b25*m.b27 - 160*m.b19*m.b25*m.b28 - 96*m.b19*m.b25*m.b29 - 64*m.b19*m.b25*
                       m.b30 - 288*m.b19*m.b26*m.b27 - 192*m.b19*m.b26*m.b28 - 96*m.b19*m.b26*m.b29 - 64*m.b19*m.b26*
                       m.b30 - 32*m.b19*m.b26*m.b31 - 224*m.b19*m.b27*m.b28 - 128*m.b19*m.b27*m.b29 - 64*m.b19*m.b27*
                       m.b30 - 32*m.b19*m.b27*m.b31 - 160*m.b19*m.b28*m.b29 - 64*m.b19*m.b28*m.b30 - 32*m.b19*m.b28*
                       m.b31 - 96*m.b19*m.b29*m.b30 - 32*m.b19*m.b29*m.b31 - 32*m.b19*m.b30*m.b31 - 640*m.b20*m.b21*
                       m.b22 - 864*m.b20*m.b21*m.b23 - 736*m.b20*m.b21*m.b24 - 608*m.b20*m.b21*m.b25 - 480*m.b20*m.b21*
                       m.b26 - 352*m.b20*m.b21*m.b27 - 288*m.b20*m.b21*m.b28 - 224*m.b20*m.b21*m.b29 - 160*m.b20*m.b21*
                       m.b30 - 96*m.b20*m.b21*m.b31 - 32*m.b20*m.b21*m.b32 - 864*m.b20*m.b22*m.b23 - 448*m.b20*m.b22*
                       m.b24 - 608*m.b20*m.b22*m.b25 - 480*m.b20*m.b22*m.b26 - 352*m.b20*m.b22*m.b27 - 256*m.b20*m.b22*
                       m.b28 - 192*m.b20*m.b22*m.b29 - 128*m.b20*m.b22*m.b30 - 64*m.b20*m.b22*m.b31 - 32*m.b20*m.b22*
                       m.b32 - 736*m.b20*m.b23*m.b24 - 608*m.b20*m.b23*m.b25 - 256*m.b20*m.b23*m.b26 - 352*m.b20*m.b23*
                       m.b27 - 224*m.b20*m.b23*m.b28 - 160*m.b20*m.b23*m.b29 - 96*m.b20*m.b23*m.b30 - 64*m.b20*m.b23*
                       m.b31 - 32*m.b20*m.b23*m.b32 - 608*m.b20*m.b24*m.b25 - 480*m.b20*m.b24*m.b26 - 352*m.b20*m.b24*
                       m.b27 - 64*m.b20*m.b24*m.b28 - 128*m.b20*m.b24*m.b29 - 96*m.b20*m.b24*m.b30 - 64*m.b20*m.b24*
                       m.b31 - 32*m.b20*m.b24*m.b32 - 480*m.b20*m.b25*m.b26 - 352*m.b20*m.b25*m.b27 - 224*m.b20*m.b25*
                       m.b28 - 128*m.b20*m.b25*m.b29 - 64*m.b20*m.b25*m.b31 - 32*m.b20*m.b25*m.b32 - 352*m.b20*m.b26*
                       m.b27 - 256*m.b20*m.b26*m.b28 - 160*m.b20*m.b26*m.b29 - 96*m.b20*m.b26*m.b30 - 64*m.b20*m.b26*
                       m.b31 - 288*m.b20*m.b27*m.b28 - 192*m.b20*m.b27*m.b29 - 96*m.b20*m.b27*m.b30 - 64*m.b20*m.b27*
                       m.b31 - 32*m.b20*m.b27*m.b32 - 224*m.b20*m.b28*m.b29 - 128*m.b20*m.b28*m.b30 - 64*m.b20*m.b28*
                       m.b31 - 32*m.b20*m.b28*m.b32 - 160*m.b20*m.b29*m.b30 - 64*m.b20*m.b29*m.b31 - 32*m.b20*m.b29*
                       m.b32 - 96*m.b20*m.b30*m.b31 - 32*m.b20*m.b30*m.b32 - 32*m.b20*m.b31*m.b32 - 640*m.b21*m.b22*
                       m.b23 - 864*m.b21*m.b22*m.b24 - 736*m.b21*m.b22*m.b25 - 608*m.b21*m.b22*m.b26 - 480*m.b21*m.b22*
                       m.b27 - 352*m.b21*m.b22*m.b28 - 288*m.b21*m.b22*m.b29 - 224*m.b21*m.b22*m.b30 - 160*m.b21*m.b22*
                       m.b31 - 96*m.b21*m.b22*m.b32 - 32*m.b21*m.b22*m.b33 - 864*m.b21*m.b23*m.b24 - 448*m.b21*m.b23*
                       m.b25 - 608*m.b21*m.b23*m.b26 - 480*m.b21*m.b23*m.b27 - 352*m.b21*m.b23*m.b28 - 256*m.b21*m.b23*
                       m.b29 - 192*m.b21*m.b23*m.b30 - 128*m.b21*m.b23*m.b31 - 64*m.b21*m.b23*m.b32 - 32*m.b21*m.b23*
                       m.b33 - 736*m.b21*m.b24*m.b25 - 608*m.b21*m.b24*m.b26 - 256*m.b21*m.b24*m.b27 - 352*m.b21*m.b24*
                       m.b28 - 224*m.b21*m.b24*m.b29 - 160*m.b21*m.b24*m.b30 - 96*m.b21*m.b24*m.b31 - 64*m.b21*m.b24*
                       m.b32 - 32*m.b21*m.b24*m.b33 - 608*m.b21*m.b25*m.b26 - 480*m.b21*m.b25*m.b27 - 352*m.b21*m.b25*
                       m.b28 - 64*m.b21*m.b25*m.b29 - 128*m.b21*m.b25*m.b30 - 96*m.b21*m.b25*m.b31 - 64*m.b21*m.b25*
                       m.b32 - 32*m.b21*m.b25*m.b33 - 480*m.b21*m.b26*m.b27 - 352*m.b21*m.b26*m.b28 - 224*m.b21*m.b26*
                       m.b29 - 128*m.b21*m.b26*m.b30 - 64*m.b21*m.b26*m.b32 - 32*m.b21*m.b26*m.b33 - 352*m.b21*m.b27*
                       m.b28 - 256*m.b21*m.b27*m.b29 - 160*m.b21*m.b27*m.b30 - 96*m.b21*m.b27*m.b31 - 64*m.b21*m.b27*
                       m.b32 - 288*m.b21*m.b28*m.b29 - 192*m.b21*m.b28*m.b30 - 96*m.b21*m.b28*m.b31 - 64*m.b21*m.b28*
                       m.b32 - 32*m.b21*m.b28*m.b33 - 224*m.b21*m.b29*m.b30 - 128*m.b21*m.b29*m.b31 - 64*m.b21*m.b29*
                       m.b32 - 32*m.b21*m.b29*m.b33 - 160*m.b21*m.b30*m.b31 - 64*m.b21*m.b30*m.b32 - 32*m.b21*m.b30*
                       m.b33 - 96*m.b21*m.b31*m.b32 - 32*m.b21*m.b31*m.b33 - 32*m.b21*m.b32*m.b33 - 640*m.b22*m.b23*
                       m.b24 - 864*m.b22*m.b23*m.b25 - 736*m.b22*m.b23*m.b26 - 608*m.b22*m.b23*m.b27 - 480*m.b22*m.b23*
                       m.b28 - 352*m.b22*m.b23*m.b29 - 288*m.b22*m.b23*m.b30 - 224*m.b22*m.b23*m.b31 - 160*m.b22*m.b23*
                       m.b32 - 96*m.b22*m.b23*m.b33 - 32*m.b22*m.b23*m.b34 - 864*m.b22*m.b24*m.b25 - 448*m.b22*m.b24*
                       m.b26 - 608*m.b22*m.b24*m.b27 - 480*m.b22*m.b24*m.b28 - 352*m.b22*m.b24*m.b29 - 256*m.b22*m.b24*
                       m.b30 - 192*m.b22*m.b24*m.b31 - 128*m.b22*m.b24*m.b32 - 64*m.b22*m.b24*m.b33 - 32*m.b22*m.b24*
                       m.b34 - 736*m.b22*m.b25*m.b26 - 608*m.b22*m.b25*m.b27 - 256*m.b22*m.b25*m.b28 - 352*m.b22*m.b25*
                       m.b29 - 224*m.b22*m.b25*m.b30 - 160*m.b22*m.b25*m.b31 - 96*m.b22*m.b25*m.b32 - 64*m.b22*m.b25*
                       m.b33 - 32*m.b22*m.b25*m.b34 - 608*m.b22*m.b26*m.b27 - 480*m.b22*m.b26*m.b28 - 352*m.b22*m.b26*
                       m.b29 - 64*m.b22*m.b26*m.b30 - 128*m.b22*m.b26*m.b31 - 96*m.b22*m.b26*m.b32 - 64*m.b22*m.b26*
                       m.b33 - 32*m.b22*m.b26*m.b34 - 480*m.b22*m.b27*m.b28 - 352*m.b22*m.b27*m.b29 - 224*m.b22*m.b27*
                       m.b30 - 128*m.b22*m.b27*m.b31 - 64*m.b22*m.b27*m.b33 - 32*m.b22*m.b27*m.b34 - 352*m.b22*m.b28*
                       m.b29 - 256*m.b22*m.b28*m.b30 - 160*m.b22*m.b28*m.b31 - 96*m.b22*m.b28*m.b32 - 64*m.b22*m.b28*
                       m.b33 - 288*m.b22*m.b29*m.b30 - 192*m.b22*m.b29*m.b31 - 96*m.b22*m.b29*m.b32 - 64*m.b22*m.b29*
                       m.b33 - 32*m.b22*m.b29*m.b34 - 224*m.b22*m.b30*m.b31 - 128*m.b22*m.b30*m.b32 - 64*m.b22*m.b30*
                       m.b33 - 32*m.b22*m.b30*m.b34 - 160*m.b22*m.b31*m.b32 - 64*m.b22*m.b31*m.b33 - 32*m.b22*m.b31*
                       m.b34 - 96*m.b22*m.b32*m.b33 - 32*m.b22*m.b32*m.b34 - 32*m.b22*m.b33*m.b34 - 640*m.b23*m.b24*
                       m.b25 - 864*m.b23*m.b24*m.b26 - 736*m.b23*m.b24*m.b27 - 608*m.b23*m.b24*m.b28 - 480*m.b23*m.b24*
                       m.b29 - 352*m.b23*m.b24*m.b30 - 288*m.b23*m.b24*m.b31 - 224*m.b23*m.b24*m.b32 - 160*m.b23*m.b24*
                       m.b33 - 96*m.b23*m.b24*m.b34 - 32*m.b23*m.b24*m.b35 - 864*m.b23*m.b25*m.b26 - 448*m.b23*m.b25*
                       m.b27 - 608*m.b23*m.b25*m.b28 - 480*m.b23*m.b25*m.b29 - 352*m.b23*m.b25*m.b30 - 256*m.b23*m.b25*
                       m.b31 - 192*m.b23*m.b25*m.b32 - 128*m.b23*m.b25*m.b33 - 64*m.b23*m.b25*m.b34 - 32*m.b23*m.b25*
                       m.b35 - 736*m.b23*m.b26*m.b27 - 608*m.b23*m.b26*m.b28 - 256*m.b23*m.b26*m.b29 - 352*m.b23*m.b26*
                       m.b30 - 224*m.b23*m.b26*m.b31 - 160*m.b23*m.b26*m.b32 - 96*m.b23*m.b26*m.b33 - 64*m.b23*m.b26*
                       m.b34 - 32*m.b23*m.b26*m.b35 - 608*m.b23*m.b27*m.b28 - 480*m.b23*m.b27*m.b29 - 352*m.b23*m.b27*
                       m.b30 - 64*m.b23*m.b27*m.b31 - 128*m.b23*m.b27*m.b32 - 96*m.b23*m.b27*m.b33 - 64*m.b23*m.b27*
                       m.b34 - 32*m.b23*m.b27*m.b35 - 480*m.b23*m.b28*m.b29 - 352*m.b23*m.b28*m.b30 - 224*m.b23*m.b28*
                       m.b31 - 128*m.b23*m.b28*m.b32 - 64*m.b23*m.b28*m.b34 - 32*m.b23*m.b28*m.b35 - 352*m.b23*m.b29*
                       m.b30 - 256*m.b23*m.b29*m.b31 - 160*m.b23*m.b29*m.b32 - 96*m.b23*m.b29*m.b33 - 64*m.b23*m.b29*
                       m.b34 - 288*m.b23*m.b30*m.b31 - 192*m.b23*m.b30*m.b32 - 96*m.b23*m.b30*m.b33 - 64*m.b23*m.b30*
                       m.b34 - 32*m.b23*m.b30*m.b35 - 224*m.b23*m.b31*m.b32 - 128*m.b23*m.b31*m.b33 - 64*m.b23*m.b31*
                       m.b34 - 32*m.b23*m.b31*m.b35 - 160*m.b23*m.b32*m.b33 - 64*m.b23*m.b32*m.b34 - 32*m.b23*m.b32*
                       m.b35 - 96*m.b23*m.b33*m.b34 - 32*m.b23*m.b33*m.b35 - 32*m.b23*m.b34*m.b35 - 640*m.b24*m.b25*
                       m.b26 - 864*m.b24*m.b25*m.b27 - 736*m.b24*m.b25*m.b28 - 608*m.b24*m.b25*m.b29 - 480*m.b24*m.b25*
                       m.b30 - 352*m.b24*m.b25*m.b31 - 288*m.b24*m.b25*m.b32 - 224*m.b24*m.b25*m.b33 - 160*m.b24*m.b25*
                       m.b34 - 96*m.b24*m.b25*m.b35 - 32*m.b24*m.b25*m.b36 - 864*m.b24*m.b26*m.b27 - 448*m.b24*m.b26*
                       m.b28 - 608*m.b24*m.b26*m.b29 - 480*m.b24*m.b26*m.b30 - 352*m.b24*m.b26*m.b31 - 256*m.b24*m.b26*
                       m.b32 - 192*m.b24*m.b26*m.b33 - 128*m.b24*m.b26*m.b34 - 64*m.b24*m.b26*m.b35 - 32*m.b24*m.b26*
                       m.b36 - 736*m.b24*m.b27*m.b28 - 608*m.b24*m.b27*m.b29 - 256*m.b24*m.b27*m.b30 - 352*m.b24*m.b27*
                       m.b31 - 224*m.b24*m.b27*m.b32 - 160*m.b24*m.b27*m.b33 - 96*m.b24*m.b27*m.b34 - 64*m.b24*m.b27*
                       m.b35 - 32*m.b24*m.b27*m.b36 - 608*m.b24*m.b28*m.b29 - 480*m.b24*m.b28*m.b30 - 352*m.b24*m.b28*
                       m.b31 - 64*m.b24*m.b28*m.b32 - 128*m.b24*m.b28*m.b33 - 96*m.b24*m.b28*m.b34 - 64*m.b24*m.b28*
                       m.b35 - 32*m.b24*m.b28*m.b36 - 480*m.b24*m.b29*m.b30 - 352*m.b24*m.b29*m.b31 - 224*m.b24*m.b29*
                       m.b32 - 128*m.b24*m.b29*m.b33 - 64*m.b24*m.b29*m.b35 - 32*m.b24*m.b29*m.b36 - 352*m.b24*m.b30*
                       m.b31 - 256*m.b24*m.b30*m.b32 - 160*m.b24*m.b30*m.b33 - 96*m.b24*m.b30*m.b34 - 64*m.b24*m.b30*
                       m.b35 - 288*m.b24*m.b31*m.b32 - 192*m.b24*m.b31*m.b33 - 96*m.b24*m.b31*m.b34 - 64*m.b24*m.b31*
                       m.b35 - 32*m.b24*m.b31*m.b36 - 224*m.b24*m.b32*m.b33 - 128*m.b24*m.b32*m.b34 - 64*m.b24*m.b32*
                       m.b35 - 32*m.b24*m.b32*m.b36 - 160*m.b24*m.b33*m.b34 - 64*m.b24*m.b33*m.b35 - 32*m.b24*m.b33*
                       m.b36 - 96*m.b24*m.b34*m.b35 - 32*m.b24*m.b34*m.b36 - 32*m.b24*m.b35*m.b36 - 640*m.b25*m.b26*
                       m.b27 - 864*m.b25*m.b26*m.b28 - 736*m.b25*m.b26*m.b29 - 608*m.b25*m.b26*m.b30 - 480*m.b25*m.b26*
                       m.b31 - 352*m.b25*m.b26*m.b32 - 288*m.b25*m.b26*m.b33 - 224*m.b25*m.b26*m.b34 - 160*m.b25*m.b26*
                       m.b35 - 96*m.b25*m.b26*m.b36 - 32*m.b25*m.b26*m.b37 - 864*m.b25*m.b27*m.b28 - 448*m.b25*m.b27*
                       m.b29 - 608*m.b25*m.b27*m.b30 - 480*m.b25*m.b27*m.b31 - 352*m.b25*m.b27*m.b32 - 256*m.b25*m.b27*
                       m.b33 - 192*m.b25*m.b27*m.b34 - 128*m.b25*m.b27*m.b35 - 64*m.b25*m.b27*m.b36 - 32*m.b25*m.b27*
                       m.b37 - 736*m.b25*m.b28*m.b29 - 608*m.b25*m.b28*m.b30 - 256*m.b25*m.b28*m.b31 - 352*m.b25*m.b28*
                       m.b32 - 224*m.b25*m.b28*m.b33 - 160*m.b25*m.b28*m.b34 - 96*m.b25*m.b28*m.b35 - 64*m.b25*m.b28*
                       m.b36 - 32*m.b25*m.b28*m.b37 - 608*m.b25*m.b29*m.b30 - 480*m.b25*m.b29*m.b31 - 352*m.b25*m.b29*
                       m.b32 - 64*m.b25*m.b29*m.b33 - 128*m.b25*m.b29*m.b34 - 96*m.b25*m.b29*m.b35 - 64*m.b25*m.b29*
                       m.b36 - 32*m.b25*m.b29*m.b37 - 480*m.b25*m.b30*m.b31 - 352*m.b25*m.b30*m.b32 - 224*m.b25*m.b30*
                       m.b33 - 128*m.b25*m.b30*m.b34 - 64*m.b25*m.b30*m.b36 - 32*m.b25*m.b30*m.b37 - 352*m.b25*m.b31*
                       m.b32 - 256*m.b25*m.b31*m.b33 - 160*m.b25*m.b31*m.b34 - 96*m.b25*m.b31*m.b35 - 64*m.b25*m.b31*
                       m.b36 - 288*m.b25*m.b32*m.b33 - 192*m.b25*m.b32*m.b34 - 96*m.b25*m.b32*m.b35 - 64*m.b25*m.b32*
                       m.b36 - 32*m.b25*m.b32*m.b37 - 224*m.b25*m.b33*m.b34 - 128*m.b25*m.b33*m.b35 - 64*m.b25*m.b33*
                       m.b36 - 32*m.b25*m.b33*m.b37 - 160*m.b25*m.b34*m.b35 - 64*m.b25*m.b34*m.b36 - 32*m.b25*m.b34*
                       m.b37 - 96*m.b25*m.b35*m.b36 - 32*m.b25*m.b35*m.b37 - 32*m.b25*m.b36*m.b37 - 640*m.b26*m.b27*
                       m.b28 - 864*m.b26*m.b27*m.b29 - 736*m.b26*m.b27*m.b30 - 608*m.b26*m.b27*m.b31 - 480*m.b26*m.b27*
                       m.b32 - 352*m.b26*m.b27*m.b33 - 288*m.b26*m.b27*m.b34 - 224*m.b26*m.b27*m.b35 - 160*m.b26*m.b27*
                       m.b36 - 96*m.b26*m.b27*m.b37 - 32*m.b26*m.b27*m.b38 - 864*m.b26*m.b28*m.b29 - 448*m.b26*m.b28*
                       m.b30 - 608*m.b26*m.b28*m.b31 - 480*m.b26*m.b28*m.b32 - 352*m.b26*m.b28*m.b33 - 256*m.b26*m.b28*
                       m.b34 - 192*m.b26*m.b28*m.b35 - 128*m.b26*m.b28*m.b36 - 64*m.b26*m.b28*m.b37 - 32*m.b26*m.b28*
                       m.b38 - 736*m.b26*m.b29*m.b30 - 608*m.b26*m.b29*m.b31 - 256*m.b26*m.b29*m.b32 - 352*m.b26*m.b29*
                       m.b33 - 224*m.b26*m.b29*m.b34 - 160*m.b26*m.b29*m.b35 - 96*m.b26*m.b29*m.b36 - 64*m.b26*m.b29*
                       m.b37 - 32*m.b26*m.b29*m.b38 - 608*m.b26*m.b30*m.b31 - 480*m.b26*m.b30*m.b32 - 352*m.b26*m.b30*
                       m.b33 - 64*m.b26*m.b30*m.b34 - 128*m.b26*m.b30*m.b35 - 96*m.b26*m.b30*m.b36 - 64*m.b26*m.b30*
                       m.b37 - 32*m.b26*m.b30*m.b38 - 480*m.b26*m.b31*m.b32 - 352*m.b26*m.b31*m.b33 - 224*m.b26*m.b31*
                       m.b34 - 128*m.b26*m.b31*m.b35 - 64*m.b26*m.b31*m.b37 - 32*m.b26*m.b31*m.b38 - 352*m.b26*m.b32*
                       m.b33 - 256*m.b26*m.b32*m.b34 - 160*m.b26*m.b32*m.b35 - 96*m.b26*m.b32*m.b36 - 64*m.b26*m.b32*
                       m.b37 - 288*m.b26*m.b33*m.b34 - 192*m.b26*m.b33*m.b35 - 96*m.b26*m.b33*m.b36 - 64*m.b26*m.b33*
                       m.b37 - 32*m.b26*m.b33*m.b38 - 224*m.b26*m.b34*m.b35 - 128*m.b26*m.b34*m.b36 - 64*m.b26*m.b34*
                       m.b37 - 32*m.b26*m.b34*m.b38 - 160*m.b26*m.b35*m.b36 - 64*m.b26*m.b35*m.b37 - 32*m.b26*m.b35*
                       m.b38 - 96*m.b26*m.b36*m.b37 - 32*m.b26*m.b36*m.b38 - 32*m.b26*m.b37*m.b38 - 640*m.b27*m.b28*
                       m.b29 - 864*m.b27*m.b28*m.b30 - 736*m.b27*m.b28*m.b31 - 608*m.b27*m.b28*m.b32 - 480*m.b27*m.b28*
                       m.b33 - 352*m.b27*m.b28*m.b34 - 288*m.b27*m.b28*m.b35 - 224*m.b27*m.b28*m.b36 - 160*m.b27*m.b28*
                       m.b37 - 96*m.b27*m.b28*m.b38 - 32*m.b27*m.b28*m.b39 - 864*m.b27*m.b29*m.b30 - 448*m.b27*m.b29*
                       m.b31 - 608*m.b27*m.b29*m.b32 - 480*m.b27*m.b29*m.b33 - 352*m.b27*m.b29*m.b34 - 256*m.b27*m.b29*
                       m.b35 - 192*m.b27*m.b29*m.b36 - 128*m.b27*m.b29*m.b37 - 64*m.b27*m.b29*m.b38 - 32*m.b27*m.b29*
                       m.b39 - 736*m.b27*m.b30*m.b31 - 608*m.b27*m.b30*m.b32 - 256*m.b27*m.b30*m.b33 - 352*m.b27*m.b30*
                       m.b34 - 224*m.b27*m.b30*m.b35 - 160*m.b27*m.b30*m.b36 - 96*m.b27*m.b30*m.b37 - 64*m.b27*m.b30*
                       m.b38 - 32*m.b27*m.b30*m.b39 - 608*m.b27*m.b31*m.b32 - 480*m.b27*m.b31*m.b33 - 352*m.b27*m.b31*
                       m.b34 - 64*m.b27*m.b31*m.b35 - 128*m.b27*m.b31*m.b36 - 96*m.b27*m.b31*m.b37 - 64*m.b27*m.b31*
                       m.b38 - 32*m.b27*m.b31*m.b39 - 480*m.b27*m.b32*m.b33 - 352*m.b27*m.b32*m.b34 - 224*m.b27*m.b32*
                       m.b35 - 128*m.b27*m.b32*m.b36 - 64*m.b27*m.b32*m.b38 - 32*m.b27*m.b32*m.b39 - 352*m.b27*m.b33*
                       m.b34 - 256*m.b27*m.b33*m.b35 - 160*m.b27*m.b33*m.b36 - 96*m.b27*m.b33*m.b37 - 64*m.b27*m.b33*
                       m.b38 - 288*m.b27*m.b34*m.b35 - 192*m.b27*m.b34*m.b36 - 96*m.b27*m.b34*m.b37 - 64*m.b27*m.b34*
                       m.b38 - 32*m.b27*m.b34*m.b39 - 224*m.b27*m.b35*m.b36 - 128*m.b27*m.b35*m.b37 - 64*m.b27*m.b35*
                       m.b38 - 32*m.b27*m.b35*m.b39 - 160*m.b27*m.b36*m.b37 - 64*m.b27*m.b36*m.b38 - 32*m.b27*m.b36*
                       m.b39 - 96*m.b27*m.b37*m.b38 - 32*m.b27*m.b37*m.b39 - 32*m.b27*m.b38*m.b39 - 640*m.b28*m.b29*
                       m.b30 - 864*m.b28*m.b29*m.b31 - 736*m.b28*m.b29*m.b32 - 608*m.b28*m.b29*m.b33 - 480*m.b28*m.b29*
                       m.b34 - 352*m.b28*m.b29*m.b35 - 288*m.b28*m.b29*m.b36 - 224*m.b28*m.b29*m.b37 - 160*m.b28*m.b29*
                       m.b38 - 96*m.b28*m.b29*m.b39 - 32*m.b28*m.b29*m.b40 - 864*m.b28*m.b30*m.b31 - 448*m.b28*m.b30*
                       m.b32 - 608*m.b28*m.b30*m.b33 - 480*m.b28*m.b30*m.b34 - 352*m.b28*m.b30*m.b35 - 256*m.b28*m.b30*
                       m.b36 - 192*m.b28*m.b30*m.b37 - 128*m.b28*m.b30*m.b38 - 64*m.b28*m.b30*m.b39 - 32*m.b28*m.b30*
                       m.b40 - 736*m.b28*m.b31*m.b32 - 608*m.b28*m.b31*m.b33 - 256*m.b28*m.b31*m.b34 - 352*m.b28*m.b31*
                       m.b35 - 224*m.b28*m.b31*m.b36 - 160*m.b28*m.b31*m.b37 - 96*m.b28*m.b31*m.b38 - 64*m.b28*m.b31*
                       m.b39 - 32*m.b28*m.b31*m.b40 - 608*m.b28*m.b32*m.b33 - 480*m.b28*m.b32*m.b34 - 352*m.b28*m.b32*
                       m.b35 - 64*m.b28*m.b32*m.b36 - 128*m.b28*m.b32*m.b37 - 96*m.b28*m.b32*m.b38 - 64*m.b28*m.b32*
                       m.b39 - 32*m.b28*m.b32*m.b40 - 480*m.b28*m.b33*m.b34 - 352*m.b28*m.b33*m.b35 - 224*m.b28*m.b33*
                       m.b36 - 128*m.b28*m.b33*m.b37 - 64*m.b28*m.b33*m.b39 - 32*m.b28*m.b33*m.b40 - 352*m.b28*m.b34*
                       m.b35 - 256*m.b28*m.b34*m.b36 - 160*m.b28*m.b34*m.b37 - 96*m.b28*m.b34*m.b38 - 64*m.b28*m.b34*
                       m.b39 - 288*m.b28*m.b35*m.b36 - 192*m.b28*m.b35*m.b37 - 96*m.b28*m.b35*m.b38 - 64*m.b28*m.b35*
                       m.b39 - 32*m.b28*m.b35*m.b40 - 224*m.b28*m.b36*m.b37 - 128*m.b28*m.b36*m.b38 - 64*m.b28*m.b36*
                       m.b39 - 32*m.b28*m.b36*m.b40 - 160*m.b28*m.b37*m.b38 - 64*m.b28*m.b37*m.b39 - 32*m.b28*m.b37*
                       m.b40 - 96*m.b28*m.b38*m.b39 - 32*m.b28*m.b38*m.b40 - 32*m.b28*m.b39*m.b40 - 640*m.b29*m.b30*
                       m.b31 - 864*m.b29*m.b30*m.b32 - 736*m.b29*m.b30*m.b33 - 608*m.b29*m.b30*m.b34 - 480*m.b29*m.b30*
                       m.b35 - 352*m.b29*m.b30*m.b36 - 288*m.b29*m.b30*m.b37 - 224*m.b29*m.b30*m.b38 - 160*m.b29*m.b30*
                       m.b39 - 96*m.b29*m.b30*m.b40 - 32*m.b29*m.b30*m.b41 - 864*m.b29*m.b31*m.b32 - 448*m.b29*m.b31*
                       m.b33 - 608*m.b29*m.b31*m.b34 - 480*m.b29*m.b31*m.b35 - 352*m.b29*m.b31*m.b36 - 256*m.b29*m.b31*
                       m.b37 - 192*m.b29*m.b31*m.b38 - 128*m.b29*m.b31*m.b39 - 64*m.b29*m.b31*m.b40 - 32*m.b29*m.b31*
                       m.b41 - 736*m.b29*m.b32*m.b33 - 608*m.b29*m.b32*m.b34 - 256*m.b29*m.b32*m.b35 - 352*m.b29*m.b32*
                       m.b36 - 224*m.b29*m.b32*m.b37 - 160*m.b29*m.b32*m.b38 - 96*m.b29*m.b32*m.b39 - 64*m.b29*m.b32*
                       m.b40 - 32*m.b29*m.b32*m.b41 - 608*m.b29*m.b33*m.b34 - 480*m.b29*m.b33*m.b35 - 352*m.b29*m.b33*
                       m.b36 - 64*m.b29*m.b33*m.b37 - 128*m.b29*m.b33*m.b38 - 96*m.b29*m.b33*m.b39 - 64*m.b29*m.b33*
                       m.b40 - 32*m.b29*m.b33*m.b41 - 480*m.b29*m.b34*m.b35 - 352*m.b29*m.b34*m.b36 - 224*m.b29*m.b34*
                       m.b37 - 128*m.b29*m.b34*m.b38 - 64*m.b29*m.b34*m.b40 - 32*m.b29*m.b34*m.b41 - 352*m.b29*m.b35*
                       m.b36 - 256*m.b29*m.b35*m.b37 - 160*m.b29*m.b35*m.b38 - 96*m.b29*m.b35*m.b39 - 64*m.b29*m.b35*
                       m.b40 - 288*m.b29*m.b36*m.b37 - 192*m.b29*m.b36*m.b38 - 96*m.b29*m.b36*m.b39 - 64*m.b29*m.b36*
                       m.b40 - 32*m.b29*m.b36*m.b41 - 224*m.b29*m.b37*m.b38 - 128*m.b29*m.b37*m.b39 - 64*m.b29*m.b37*
                       m.b40 - 32*m.b29*m.b37*m.b41 - 160*m.b29*m.b38*m.b39 - 64*m.b29*m.b38*m.b40 - 32*m.b29*m.b38*
                       m.b41 - 96*m.b29*m.b39*m.b40 - 32*m.b29*m.b39*m.b41 - 32*m.b29*m.b40*m.b41 - 640*m.b30*m.b31*
                       m.b32 - 864*m.b30*m.b31*m.b33 - 736*m.b30*m.b31*m.b34 - 608*m.b30*m.b31*m.b35 - 480*m.b30*m.b31*
                       m.b36 - 352*m.b30*m.b31*m.b37 - 288*m.b30*m.b31*m.b38 - 224*m.b30*m.b31*m.b39 - 160*m.b30*m.b31*
                       m.b40 - 96*m.b30*m.b31*m.b41 - 32*m.b30*m.b31*m.b42 - 864*m.b30*m.b32*m.b33 - 448*m.b30*m.b32*
                       m.b34 - 608*m.b30*m.b32*m.b35 - 480*m.b30*m.b32*m.b36 - 352*m.b30*m.b32*m.b37 - 256*m.b30*m.b32*
                       m.b38 - 192*m.b30*m.b32*m.b39 - 128*m.b30*m.b32*m.b40 - 64*m.b30*m.b32*m.b41 - 32*m.b30*m.b32*
                       m.b42 - 736*m.b30*m.b33*m.b34 - 608*m.b30*m.b33*m.b35 - 256*m.b30*m.b33*m.b36 - 352*m.b30*m.b33*
                       m.b37 - 224*m.b30*m.b33*m.b38 - 160*m.b30*m.b33*m.b39 - 96*m.b30*m.b33*m.b40 - 64*m.b30*m.b33*
                       m.b41 - 32*m.b30*m.b33*m.b42 - 608*m.b30*m.b34*m.b35 - 480*m.b30*m.b34*m.b36 - 352*m.b30*m.b34*
                       m.b37 - 64*m.b30*m.b34*m.b38 - 128*m.b30*m.b34*m.b39 - 96*m.b30*m.b34*m.b40 - 64*m.b30*m.b34*
                       m.b41 - 32*m.b30*m.b34*m.b42 - 480*m.b30*m.b35*m.b36 - 352*m.b30*m.b35*m.b37 - 224*m.b30*m.b35*
                       m.b38 - 128*m.b30*m.b35*m.b39 - 64*m.b30*m.b35*m.b41 - 32*m.b30*m.b35*m.b42 - 352*m.b30*m.b36*
                       m.b37 - 256*m.b30*m.b36*m.b38 - 160*m.b30*m.b36*m.b39 - 96*m.b30*m.b36*m.b40 - 64*m.b30*m.b36*
                       m.b41 - 288*m.b30*m.b37*m.b38 - 192*m.b30*m.b37*m.b39 - 96*m.b30*m.b37*m.b40 - 64*m.b30*m.b37*
                       m.b41 - 32*m.b30*m.b37*m.b42 - 224*m.b30*m.b38*m.b39 - 128*m.b30*m.b38*m.b40 - 64*m.b30*m.b38*
                       m.b41 - 32*m.b30*m.b38*m.b42 - 160*m.b30*m.b39*m.b40 - 64*m.b30*m.b39*m.b41 - 32*m.b30*m.b39*
                       m.b42 - 96*m.b30*m.b40*m.b41 - 32*m.b30*m.b40*m.b42 - 32*m.b30*m.b41*m.b42 - 640*m.b31*m.b32*
                       m.b33 - 864*m.b31*m.b32*m.b34 - 736*m.b31*m.b32*m.b35 - 608*m.b31*m.b32*m.b36 - 480*m.b31*m.b32*
                       m.b37 - 352*m.b31*m.b32*m.b38 - 288*m.b31*m.b32*m.b39 - 224*m.b31*m.b32*m.b40 - 160*m.b31*m.b32*
                       m.b41 - 96*m.b31*m.b32*m.b42 - 32*m.b31*m.b32*m.b43 - 864*m.b31*m.b33*m.b34 - 448*m.b31*m.b33*
                       m.b35 - 608*m.b31*m.b33*m.b36 - 480*m.b31*m.b33*m.b37 - 352*m.b31*m.b33*m.b38 - 256*m.b31*m.b33*
                       m.b39 - 192*m.b31*m.b33*m.b40 - 128*m.b31*m.b33*m.b41 - 64*m.b31*m.b33*m.b42 - 32*m.b31*m.b33*
                       m.b43 - 736*m.b31*m.b34*m.b35 - 608*m.b31*m.b34*m.b36 - 256*m.b31*m.b34*m.b37 - 352*m.b31*m.b34*
                       m.b38 - 224*m.b31*m.b34*m.b39 - 160*m.b31*m.b34*m.b40 - 96*m.b31*m.b34*m.b41 - 64*m.b31*m.b34*
                       m.b42 - 32*m.b31*m.b34*m.b43 - 608*m.b31*m.b35*m.b36 - 480*m.b31*m.b35*m.b37 - 352*m.b31*m.b35*
                       m.b38 - 64*m.b31*m.b35*m.b39 - 128*m.b31*m.b35*m.b40 - 96*m.b31*m.b35*m.b41 - 64*m.b31*m.b35*
                       m.b42 - 32*m.b31*m.b35*m.b43 - 480*m.b31*m.b36*m.b37 - 352*m.b31*m.b36*m.b38 - 224*m.b31*m.b36*
                       m.b39 - 128*m.b31*m.b36*m.b40 - 64*m.b31*m.b36*m.b42 - 32*m.b31*m.b36*m.b43 - 352*m.b31*m.b37*
                       m.b38 - 256*m.b31*m.b37*m.b39 - 160*m.b31*m.b37*m.b40 - 96*m.b31*m.b37*m.b41 - 64*m.b31*m.b37*
                       m.b42 - 288*m.b31*m.b38*m.b39 - 192*m.b31*m.b38*m.b40 - 96*m.b31*m.b38*m.b41 - 64*m.b31*m.b38*
                       m.b42 - 32*m.b31*m.b38*m.b43 - 224*m.b31*m.b39*m.b40 - 128*m.b31*m.b39*m.b41 - 64*m.b31*m.b39*
                       m.b42 - 32*m.b31*m.b39*m.b43 - 160*m.b31*m.b40*m.b41 - 64*m.b31*m.b40*m.b42 - 32*m.b31*m.b40*
                       m.b43 - 96*m.b31*m.b41*m.b42 - 32*m.b31*m.b41*m.b43 - 32*m.b31*m.b42*m.b43 - 640*m.b32*m.b33*
                       m.b34 - 864*m.b32*m.b33*m.b35 - 736*m.b32*m.b33*m.b36 - 608*m.b32*m.b33*m.b37 - 480*m.b32*m.b33*
                       m.b38 - 352*m.b32*m.b33*m.b39 - 288*m.b32*m.b33*m.b40 - 224*m.b32*m.b33*m.b41 - 160*m.b32*m.b33*
                       m.b42 - 96*m.b32*m.b33*m.b43 - 32*m.b32*m.b33*m.b44 - 864*m.b32*m.b34*m.b35 - 448*m.b32*m.b34*
                       m.b36 - 608*m.b32*m.b34*m.b37 - 480*m.b32*m.b34*m.b38 - 352*m.b32*m.b34*m.b39 - 256*m.b32*m.b34*
                       m.b40 - 192*m.b32*m.b34*m.b41 - 128*m.b32*m.b34*m.b42 - 64*m.b32*m.b34*m.b43 - 32*m.b32*m.b34*
                       m.b44 - 736*m.b32*m.b35*m.b36 - 608*m.b32*m.b35*m.b37 - 256*m.b32*m.b35*m.b38 - 352*m.b32*m.b35*
                       m.b39 - 224*m.b32*m.b35*m.b40 - 160*m.b32*m.b35*m.b41 - 96*m.b32*m.b35*m.b42 - 64*m.b32*m.b35*
                       m.b43 - 32*m.b32*m.b35*m.b44 - 608*m.b32*m.b36*m.b37 - 480*m.b32*m.b36*m.b38 - 352*m.b32*m.b36*
                       m.b39 - 64*m.b32*m.b36*m.b40 - 128*m.b32*m.b36*m.b41 - 96*m.b32*m.b36*m.b42 - 64*m.b32*m.b36*
                       m.b43 - 32*m.b32*m.b36*m.b44 - 480*m.b32*m.b37*m.b38 - 352*m.b32*m.b37*m.b39 - 224*m.b32*m.b37*
                       m.b40 - 128*m.b32*m.b37*m.b41 - 64*m.b32*m.b37*m.b43 - 32*m.b32*m.b37*m.b44 - 352*m.b32*m.b38*
                       m.b39 - 256*m.b32*m.b38*m.b40 - 160*m.b32*m.b38*m.b41 - 96*m.b32*m.b38*m.b42 - 64*m.b32*m.b38*
                       m.b43 - 288*m.b32*m.b39*m.b40 - 192*m.b32*m.b39*m.b41 - 96*m.b32*m.b39*m.b42 - 64*m.b32*m.b39*
                       m.b43 - 32*m.b32*m.b39*m.b44 - 224*m.b32*m.b40*m.b41 - 128*m.b32*m.b40*m.b42 - 64*m.b32*m.b40*
                       m.b43 - 32*m.b32*m.b40*m.b44 - 160*m.b32*m.b41*m.b42 - 64*m.b32*m.b41*m.b43 - 32*m.b32*m.b41*
                       m.b44 - 96*m.b32*m.b42*m.b43 - 32*m.b32*m.b42*m.b44 - 32*m.b32*m.b43*m.b44 - 640*m.b33*m.b34*
                       m.b35 - 864*m.b33*m.b34*m.b36 - 736*m.b33*m.b34*m.b37 - 608*m.b33*m.b34*m.b38 - 480*m.b33*m.b34*
                       m.b39 - 352*m.b33*m.b34*m.b40 - 288*m.b33*m.b34*m.b41 - 224*m.b33*m.b34*m.b42 - 160*m.b33*m.b34*
                       m.b43 - 96*m.b33*m.b34*m.b44 - 32*m.b33*m.b34*m.b45 - 864*m.b33*m.b35*m.b36 - 448*m.b33*m.b35*
                       m.b37 - 608*m.b33*m.b35*m.b38 - 480*m.b33*m.b35*m.b39 - 352*m.b33*m.b35*m.b40 - 256*m.b33*m.b35*
                       m.b41 - 192*m.b33*m.b35*m.b42 - 128*m.b33*m.b35*m.b43 - 64*m.b33*m.b35*m.b44 - 32*m.b33*m.b35*
                       m.b45 - 736*m.b33*m.b36*m.b37 - 608*m.b33*m.b36*m.b38 - 256*m.b33*m.b36*m.b39 - 352*m.b33*m.b36*
                       m.b40 - 224*m.b33*m.b36*m.b41 - 160*m.b33*m.b36*m.b42 - 96*m.b33*m.b36*m.b43 - 64*m.b33*m.b36*
                       m.b44 - 32*m.b33*m.b36*m.b45 - 608*m.b33*m.b37*m.b38 - 480*m.b33*m.b37*m.b39 - 352*m.b33*m.b37*
                       m.b40 - 64*m.b33*m.b37*m.b41 - 128*m.b33*m.b37*m.b42 - 96*m.b33*m.b37*m.b43 - 64*m.b33*m.b37*
                       m.b44 - 32*m.b33*m.b37*m.b45 - 480*m.b33*m.b38*m.b39 - 352*m.b33*m.b38*m.b40 - 224*m.b33*m.b38*
                       m.b41 - 128*m.b33*m.b38*m.b42 - 64*m.b33*m.b38*m.b44 - 32*m.b33*m.b38*m.b45 - 352*m.b33*m.b39*
                       m.b40 - 256*m.b33*m.b39*m.b41 - 160*m.b33*m.b39*m.b42 - 96*m.b33*m.b39*m.b43 - 64*m.b33*m.b39*
                       m.b44 - 288*m.b33*m.b40*m.b41 - 192*m.b33*m.b40*m.b42 - 96*m.b33*m.b40*m.b43 - 64*m.b33*m.b40*
                       m.b44 - 32*m.b33*m.b40*m.b45 - 224*m.b33*m.b41*m.b42 - 128*m.b33*m.b41*m.b43 - 64*m.b33*m.b41*
                       m.b44 - 32*m.b33*m.b41*m.b45 - 160*m.b33*m.b42*m.b43 - 64*m.b33*m.b42*m.b44 - 32*m.b33*m.b42*
                       m.b45 - 96*m.b33*m.b43*m.b44 - 32*m.b33*m.b43*m.b45 - 32*m.b33*m.b44*m.b45 - 640*m.b34*m.b35*
                       m.b36 - 864*m.b34*m.b35*m.b37 - 736*m.b34*m.b35*m.b38 - 608*m.b34*m.b35*m.b39 - 480*m.b34*m.b35*
                       m.b40 - 352*m.b34*m.b35*m.b41 - 288*m.b34*m.b35*m.b42 - 224*m.b34*m.b35*m.b43 - 160*m.b34*m.b35*
                       m.b44 - 96*m.b34*m.b35*m.b45 - 32*m.b34*m.b35*m.b46 - 864*m.b34*m.b36*m.b37 - 448*m.b34*m.b36*
                       m.b38 - 608*m.b34*m.b36*m.b39 - 480*m.b34*m.b36*m.b40 - 352*m.b34*m.b36*m.b41 - 256*m.b34*m.b36*
                       m.b42 - 192*m.b34*m.b36*m.b43 - 128*m.b34*m.b36*m.b44 - 64*m.b34*m.b36*m.b45 - 32*m.b34*m.b36*
                       m.b46 - 736*m.b34*m.b37*m.b38 - 608*m.b34*m.b37*m.b39 - 256*m.b34*m.b37*m.b40 - 352*m.b34*m.b37*
                       m.b41 - 224*m.b34*m.b37*m.b42 - 160*m.b34*m.b37*m.b43 - 96*m.b34*m.b37*m.b44 - 64*m.b34*m.b37*
                       m.b45 - 32*m.b34*m.b37*m.b46 - 608*m.b34*m.b38*m.b39 - 480*m.b34*m.b38*m.b40 - 352*m.b34*m.b38*
                       m.b41 - 64*m.b34*m.b38*m.b42 - 128*m.b34*m.b38*m.b43 - 96*m.b34*m.b38*m.b44 - 64*m.b34*m.b38*
                       m.b45 - 32*m.b34*m.b38*m.b46 - 480*m.b34*m.b39*m.b40 - 352*m.b34*m.b39*m.b41 - 224*m.b34*m.b39*
                       m.b42 - 128*m.b34*m.b39*m.b43 - 64*m.b34*m.b39*m.b45 - 32*m.b34*m.b39*m.b46 - 352*m.b34*m.b40*
                       m.b41 - 256*m.b34*m.b40*m.b42 - 160*m.b34*m.b40*m.b43 - 96*m.b34*m.b40*m.b44 - 64*m.b34*m.b40*
                       m.b45 - 288*m.b34*m.b41*m.b42 - 192*m.b34*m.b41*m.b43 - 96*m.b34*m.b41*m.b44 - 64*m.b34*m.b41*
                       m.b45 - 32*m.b34*m.b41*m.b46 - 224*m.b34*m.b42*m.b43 - 128*m.b34*m.b42*m.b44 - 64*m.b34*m.b42*
                       m.b45 - 32*m.b34*m.b42*m.b46 - 160*m.b34*m.b43*m.b44 - 64*m.b34*m.b43*m.b45 - 32*m.b34*m.b43*
                       m.b46 - 96*m.b34*m.b44*m.b45 - 32*m.b34*m.b44*m.b46 - 32*m.b34*m.b45*m.b46 - 640*m.b35*m.b36*
                       m.b37 - 864*m.b35*m.b36*m.b38 - 736*m.b35*m.b36*m.b39 - 608*m.b35*m.b36*m.b40 - 480*m.b35*m.b36*
                       m.b41 - 352*m.b35*m.b36*m.b42 - 288*m.b35*m.b36*m.b43 - 224*m.b35*m.b36*m.b44 - 160*m.b35*m.b36*
                       m.b45 - 96*m.b35*m.b36*m.b46 - 32*m.b35*m.b36*m.b47 - 864*m.b35*m.b37*m.b38 - 448*m.b35*m.b37*
                       m.b39 - 608*m.b35*m.b37*m.b40 - 480*m.b35*m.b37*m.b41 - 352*m.b35*m.b37*m.b42 - 256*m.b35*m.b37*
                       m.b43 - 192*m.b35*m.b37*m.b44 - 128*m.b35*m.b37*m.b45 - 64*m.b35*m.b37*m.b46 - 32*m.b35*m.b37*
                       m.b47 - 736*m.b35*m.b38*m.b39 - 608*m.b35*m.b38*m.b40 - 256*m.b35*m.b38*m.b41 - 352*m.b35*m.b38*
                       m.b42 - 224*m.b35*m.b38*m.b43 - 160*m.b35*m.b38*m.b44 - 96*m.b35*m.b38*m.b45 - 64*m.b35*m.b38*
                       m.b46 - 32*m.b35*m.b38*m.b47 - 608*m.b35*m.b39*m.b40 - 480*m.b35*m.b39*m.b41 - 352*m.b35*m.b39*
                       m.b42 - 64*m.b35*m.b39*m.b43 - 128*m.b35*m.b39*m.b44 - 96*m.b35*m.b39*m.b45 - 64*m.b35*m.b39*
                       m.b46 - 32*m.b35*m.b39*m.b47 - 480*m.b35*m.b40*m.b41 - 352*m.b35*m.b40*m.b42 - 224*m.b35*m.b40*
                       m.b43 - 128*m.b35*m.b40*m.b44 - 64*m.b35*m.b40*m.b46 - 32*m.b35*m.b40*m.b47 - 352*m.b35*m.b41*
                       m.b42 - 256*m.b35*m.b41*m.b43 - 160*m.b35*m.b41*m.b44 - 96*m.b35*m.b41*m.b45 - 64*m.b35*m.b41*
                       m.b46 - 288*m.b35*m.b42*m.b43 - 192*m.b35*m.b42*m.b44 - 96*m.b35*m.b42*m.b45 - 64*m.b35*m.b42*
                       m.b46 - 32*m.b35*m.b42*m.b47 - 224*m.b35*m.b43*m.b44 - 128*m.b35*m.b43*m.b45 - 64*m.b35*m.b43*
                       m.b46 - 32*m.b35*m.b43*m.b47 - 160*m.b35*m.b44*m.b45 - 64*m.b35*m.b44*m.b46 - 32*m.b35*m.b44*
                       m.b47 - 96*m.b35*m.b45*m.b46 - 32*m.b35*m.b45*m.b47 - 32*m.b35*m.b46*m.b47 - 640*m.b36*m.b37*
                       m.b38 - 864*m.b36*m.b37*m.b39 - 736*m.b36*m.b37*m.b40 - 608*m.b36*m.b37*m.b41 - 480*m.b36*m.b37*
                       m.b42 - 352*m.b36*m.b37*m.b43 - 288*m.b36*m.b37*m.b44 - 224*m.b36*m.b37*m.b45 - 160*m.b36*m.b37*
                       m.b46 - 96*m.b36*m.b37*m.b47 - 32*m.b36*m.b37*m.b48 - 864*m.b36*m.b38*m.b39 - 448*m.b36*m.b38*
                       m.b40 - 608*m.b36*m.b38*m.b41 - 480*m.b36*m.b38*m.b42 - 352*m.b36*m.b38*m.b43 - 256*m.b36*m.b38*
                       m.b44 - 192*m.b36*m.b38*m.b45 - 128*m.b36*m.b38*m.b46 - 64*m.b36*m.b38*m.b47 - 32*m.b36*m.b38*
                       m.b48 - 736*m.b36*m.b39*m.b40 - 608*m.b36*m.b39*m.b41 - 256*m.b36*m.b39*m.b42 - 352*m.b36*m.b39*
                       m.b43 - 224*m.b36*m.b39*m.b44 - 160*m.b36*m.b39*m.b45 - 96*m.b36*m.b39*m.b46 - 64*m.b36*m.b39*
                       m.b47 - 32*m.b36*m.b39*m.b48 - 608*m.b36*m.b40*m.b41 - 480*m.b36*m.b40*m.b42 - 352*m.b36*m.b40*
                       m.b43 - 64*m.b36*m.b40*m.b44 - 128*m.b36*m.b40*m.b45 - 96*m.b36*m.b40*m.b46 - 64*m.b36*m.b40*
                       m.b47 - 32*m.b36*m.b40*m.b48 - 480*m.b36*m.b41*m.b42 - 352*m.b36*m.b41*m.b43 - 224*m.b36*m.b41*
                       m.b44 - 128*m.b36*m.b41*m.b45 - 64*m.b36*m.b41*m.b47 - 32*m.b36*m.b41*m.b48 - 352*m.b36*m.b42*
                       m.b43 - 256*m.b36*m.b42*m.b44 - 160*m.b36*m.b42*m.b45 - 96*m.b36*m.b42*m.b46 - 64*m.b36*m.b42*
                       m.b47 - 288*m.b36*m.b43*m.b44 - 192*m.b36*m.b43*m.b45 - 96*m.b36*m.b43*m.b46 - 64*m.b36*m.b43*
                       m.b47 - 32*m.b36*m.b43*m.b48 - 224*m.b36*m.b44*m.b45 - 128*m.b36*m.b44*m.b46 - 64*m.b36*m.b44*
                       m.b47 - 32*m.b36*m.b44*m.b48 - 160*m.b36*m.b45*m.b46 - 64*m.b36*m.b45*m.b47 - 32*m.b36*m.b45*
                       m.b48 - 96*m.b36*m.b46*m.b47 - 32*m.b36*m.b46*m.b48 - 32*m.b36*m.b47*m.b48 - 640*m.b37*m.b38*
                       m.b39 - 864*m.b37*m.b38*m.b40 - 736*m.b37*m.b38*m.b41 - 608*m.b37*m.b38*m.b42 - 480*m.b37*m.b38*
                       m.b43 - 352*m.b37*m.b38*m.b44 - 288*m.b37*m.b38*m.b45 - 224*m.b37*m.b38*m.b46 - 160*m.b37*m.b38*
                       m.b47 - 96*m.b37*m.b38*m.b48 - 32*m.b37*m.b38*m.b49 - 864*m.b37*m.b39*m.b40 - 448*m.b37*m.b39*
                       m.b41 - 608*m.b37*m.b39*m.b42 - 480*m.b37*m.b39*m.b43 - 352*m.b37*m.b39*m.b44 - 256*m.b37*m.b39*
                       m.b45 - 192*m.b37*m.b39*m.b46 - 128*m.b37*m.b39*m.b47 - 64*m.b37*m.b39*m.b48 - 32*m.b37*m.b39*
                       m.b49 - 736*m.b37*m.b40*m.b41 - 608*m.b37*m.b40*m.b42 - 256*m.b37*m.b40*m.b43 - 352*m.b37*m.b40*
                       m.b44 - 224*m.b37*m.b40*m.b45 - 160*m.b37*m.b40*m.b46 - 96*m.b37*m.b40*m.b47 - 64*m.b37*m.b40*
                       m.b48 - 32*m.b37*m.b40*m.b49 - 608*m.b37*m.b41*m.b42 - 480*m.b37*m.b41*m.b43 - 352*m.b37*m.b41*
                       m.b44 - 64*m.b37*m.b41*m.b45 - 128*m.b37*m.b41*m.b46 - 96*m.b37*m.b41*m.b47 - 64*m.b37*m.b41*
                       m.b48 - 32*m.b37*m.b41*m.b49 - 480*m.b37*m.b42*m.b43 - 352*m.b37*m.b42*m.b44 - 224*m.b37*m.b42*
                       m.b45 - 128*m.b37*m.b42*m.b46 - 64*m.b37*m.b42*m.b48 - 32*m.b37*m.b42*m.b49 - 352*m.b37*m.b43*
                       m.b44 - 256*m.b37*m.b43*m.b45 - 160*m.b37*m.b43*m.b46 - 96*m.b37*m.b43*m.b47 - 64*m.b37*m.b43*
                       m.b48 - 288*m.b37*m.b44*m.b45 - 192*m.b37*m.b44*m.b46 - 96*m.b37*m.b44*m.b47 - 64*m.b37*m.b44*
                       m.b48 - 32*m.b37*m.b44*m.b49 - 224*m.b37*m.b45*m.b46 - 128*m.b37*m.b45*m.b47 - 64*m.b37*m.b45*
                       m.b48 - 32*m.b37*m.b45*m.b49 - 160*m.b37*m.b46*m.b47 - 64*m.b37*m.b46*m.b48 - 32*m.b37*m.b46*
                       m.b49 - 96*m.b37*m.b47*m.b48 - 32*m.b37*m.b47*m.b49 - 32*m.b37*m.b48*m.b49 - 640*m.b38*m.b39*
                       m.b40 - 864*m.b38*m.b39*m.b41 - 736*m.b38*m.b39*m.b42 - 608*m.b38*m.b39*m.b43 - 480*m.b38*m.b39*
                       m.b44 - 352*m.b38*m.b39*m.b45 - 288*m.b38*m.b39*m.b46 - 224*m.b38*m.b39*m.b47 - 160*m.b38*m.b39*
                       m.b48 - 96*m.b38*m.b39*m.b49 - 32*m.b38*m.b39*m.b50 - 864*m.b38*m.b40*m.b41 - 448*m.b38*m.b40*
                       m.b42 - 608*m.b38*m.b40*m.b43 - 480*m.b38*m.b40*m.b44 - 352*m.b38*m.b40*m.b45 - 256*m.b38*m.b40*
                       m.b46 - 192*m.b38*m.b40*m.b47 - 128*m.b38*m.b40*m.b48 - 64*m.b38*m.b40*m.b49 - 32*m.b38*m.b40*
                       m.b50 - 736*m.b38*m.b41*m.b42 - 608*m.b38*m.b41*m.b43 - 256*m.b38*m.b41*m.b44 - 352*m.b38*m.b41*
                       m.b45 - 224*m.b38*m.b41*m.b46 - 160*m.b38*m.b41*m.b47 - 96*m.b38*m.b41*m.b48 - 64*m.b38*m.b41*
                       m.b49 - 32*m.b38*m.b41*m.b50 - 608*m.b38*m.b42*m.b43 - 480*m.b38*m.b42*m.b44 - 352*m.b38*m.b42*
                       m.b45 - 64*m.b38*m.b42*m.b46 - 128*m.b38*m.b42*m.b47 - 96*m.b38*m.b42*m.b48 - 64*m.b38*m.b42*
                       m.b49 - 32*m.b38*m.b42*m.b50 - 480*m.b38*m.b43*m.b44 - 352*m.b38*m.b43*m.b45 - 224*m.b38*m.b43*
                       m.b46 - 128*m.b38*m.b43*m.b47 - 64*m.b38*m.b43*m.b49 - 32*m.b38*m.b43*m.b50 - 352*m.b38*m.b44*
                       m.b45 - 256*m.b38*m.b44*m.b46 - 160*m.b38*m.b44*m.b47 - 96*m.b38*m.b44*m.b48 - 64*m.b38*m.b44*
                       m.b49 - 288*m.b38*m.b45*m.b46 - 192*m.b38*m.b45*m.b47 - 96*m.b38*m.b45*m.b48 - 64*m.b38*m.b45*
                       m.b49 - 32*m.b38*m.b45*m.b50 - 224*m.b38*m.b46*m.b47 - 128*m.b38*m.b46*m.b48 - 64*m.b38*m.b46*
                       m.b49 - 32*m.b38*m.b46*m.b50 - 160*m.b38*m.b47*m.b48 - 64*m.b38*m.b47*m.b49 - 32*m.b38*m.b47*
                       m.b50 - 96*m.b38*m.b48*m.b49 - 32*m.b38*m.b48*m.b50 - 32*m.b38*m.b49*m.b50 - 608*m.b39*m.b40*
                       m.b41 - 800*m.b39*m.b40*m.b42 - 672*m.b39*m.b40*m.b43 - 544*m.b39*m.b40*m.b44 - 416*m.b39*m.b40*
                       m.b45 - 288*m.b39*m.b40*m.b46 - 224*m.b39*m.b40*m.b47 - 160*m.b39*m.b40*m.b48 - 96*m.b39*m.b40*
                       m.b49 - 32*m.b39*m.b40*m.b50 - 800*m.b39*m.b41*m.b42 - 416*m.b39*m.b41*m.b43 - 544*m.b39*m.b41*
                       m.b44 - 416*m.b39*m.b41*m.b45 - 288*m.b39*m.b41*m.b46 - 192*m.b39*m.b41*m.b47 - 128*m.b39*m.b41*
                       m.b48 - 64*m.b39*m.b41*m.b49 - 32*m.b39*m.b41*m.b50 - 672*m.b39*m.b42*m.b43 - 544*m.b39*m.b42*
                       m.b44 - 224*m.b39*m.b42*m.b45 - 288*m.b39*m.b42*m.b46 - 160*m.b39*m.b42*m.b47 - 96*m.b39*m.b42*
                       m.b48 - 64*m.b39*m.b42*m.b49 - 32*m.b39*m.b42*m.b50 - 544*m.b39*m.b43*m.b44 - 416*m.b39*m.b43*
                       m.b45 - 288*m.b39*m.b43*m.b46 - 32*m.b39*m.b43*m.b47 - 96*m.b39*m.b43*m.b48 - 64*m.b39*m.b43*
                       m.b49 - 32*m.b39*m.b43*m.b50 - 416*m.b39*m.b44*m.b45 - 288*m.b39*m.b44*m.b46 - 192*m.b39*m.b44*
                       m.b47 - 96*m.b39*m.b44*m.b48 - 32*m.b39*m.b44*m.b50 - 320*m.b39*m.b45*m.b46 - 224*m.b39*m.b45*
                       m.b47 - 128*m.b39*m.b45*m.b48 - 64*m.b39*m.b45*m.b49 - 32*m.b39*m.b45*m.b50 - 256*m.b39*m.b46*
                       m.b47 - 160*m.b39*m.b46*m.b48 - 64*m.b39*m.b46*m.b49 - 32*m.b39*m.b46*m.b50 - 192*m.b39*m.b47*
                       m.b48 - 96*m.b39*m.b47*m.b49 - 32*m.b39*m.b47*m.b50 - 128*m.b39*m.b48*m.b49 - 32*m.b39*m.b48*
                       m.b50 - 64*m.b39*m.b49*m.b50 - 544*m.b40*m.b41*m.b42 - 736*m.b40*m.b41*m.b43 - 608*m.b40*m.b41*
                       m.b44 - 480*m.b40*m.b41*m.b45 - 352*m.b40*m.b41*m.b46 - 224*m.b40*m.b41*m.b47 - 160*m.b40*m.b41*
                       m.b48 - 96*m.b40*m.b41*m.b49 - 32*m.b40*m.b41*m.b50 - 704*m.b40*m.b42*m.b43 - 384*m.b40*m.b42*
                       m.b44 - 480*m.b40*m.b42*m.b45 - 352*m.b40*m.b42*m.b46 - 224*m.b40*m.b42*m.b47 - 128*m.b40*m.b42*
                       m.b48 - 64*m.b40*m.b42*m.b49 - 32*m.b40*m.b42*m.b50 - 576*m.b40*m.b43*m.b44 - 480*m.b40*m.b43*
                       m.b45 - 192*m.b40*m.b43*m.b46 - 224*m.b40*m.b43*m.b47 - 96*m.b40*m.b43*m.b48 - 64*m.b40*m.b43*
                       m.b49 - 32*m.b40*m.b43*m.b50 - 448*m.b40*m.b44*m.b45 - 352*m.b40*m.b44*m.b46 - 224*m.b40*m.b44*
                       m.b47 - 32*m.b40*m.b44*m.b48 - 64*m.b40*m.b44*m.b49 - 32*m.b40*m.b44*m.b50 - 320*m.b40*m.b45*
                       m.b46 - 256*m.b40*m.b45*m.b47 - 160*m.b40*m.b45*m.b48 - 64*m.b40*m.b45*m.b49 - 256*m.b40*m.b46*
                       m.b47 - 192*m.b40*m.b46*m.b48 - 96*m.b40*m.b46*m.b49 - 32*m.b40*m.b46*m.b50 - 192*m.b40*m.b47*
                       m.b48 - 128*m.b40*m.b47*m.b49 - 32*m.b40*m.b47*m.b50 - 128*m.b40*m.b48*m.b49 - 64*m.b40*m.b48*
                       m.b50 - 64*m.b40*m.b49*m.b50 - 480*m.b41*m.b42*m.b43 - 640*m.b41*m.b42*m.b44 - 544*m.b41*m.b42*
                       m.b45 - 416*m.b41*m.b42*m.b46 - 288*m.b41*m.b42*m.b47 - 160*m.b41*m.b42*m.b48 - 96*m.b41*m.b42*
                       m.b49 - 32*m.b41*m.b42*m.b50 - 608*m.b41*m.b43*m.b44 - 320*m.b41*m.b43*m.b45 - 416*m.b41*m.b43*
                       m.b46 - 288*m.b41*m.b43*m.b47 - 160*m.b41*m.b43*m.b48 - 64*m.b41*m.b43*m.b49 - 32*m.b41*m.b43*
                       m.b50 - 480*m.b41*m.b44*m.b45 - 384*m.b41*m.b44*m.b46 - 160*m.b41*m.b44*m.b47 - 160*m.b41*m.b44*
                       m.b48 - 64*m.b41*m.b44*m.b49 - 32*m.b41*m.b44*m.b50 - 352*m.b41*m.b45*m.b46 - 256*m.b41*m.b45*
                       m.b47 - 192*m.b41*m.b45*m.b48 - 32*m.b41*m.b45*m.b49 - 32*m.b41*m.b45*m.b50 - 256*m.b41*m.b46*
                       m.b47 - 192*m.b41*m.b46*m.b48 - 128*m.b41*m.b46*m.b49 - 32*m.b41*m.b46*m.b50 - 192*m.b41*m.b47*
                       m.b48 - 128*m.b41*m.b47*m.b49 - 64*m.b41*m.b47*m.b50 - 128*m.b41*m.b48*m.b49 - 64*m.b41*m.b48*
                       m.b50 - 64*m.b41*m.b49*m.b50 - 416*m.b42*m.b43*m.b44 - 544*m.b42*m.b43*m.b45 - 448*m.b42*m.b43*
                       m.b46 - 352*m.b42*m.b43*m.b47 - 224*m.b42*m.b43*m.b48 - 96*m.b42*m.b43*m.b49 - 32*m.b42*m.b43*
                       m.b50 - 512*m.b42*m.b44*m.b45 - 256*m.b42*m.b44*m.b46 - 320*m.b42*m.b44*m.b47 - 224*m.b42*m.b44*
                       m.b48 - 96*m.b42*m.b44*m.b49 - 32*m.b42*m.b44*m.b50 - 384*m.b42*m.b45*m.b46 - 288*m.b42*m.b45*
                       m.b47 - 96*m.b42*m.b45*m.b48 - 128*m.b42*m.b45*m.b49 - 32*m.b42*m.b45*m.b50 - 256*m.b42*m.b46*
                       m.b47 - 192*m.b42*m.b46*m.b48 - 128*m.b42*m.b46*m.b49 - 32*m.b42*m.b46*m.b50 - 192*m.b42*m.b47*
                       m.b48 - 128*m.b42*m.b47*m.b49 - 64*m.b42*m.b47*m.b50 - 128*m.b42*m.b48*m.b49 - 64*m.b42*m.b48*
                       m.b50 - 64*m.b42*m.b49*m.b50 - 352*m.b43*m.b44*m.b45 - 448*m.b43*m.b44*m.b46 - 352*m.b43*m.b44*
                       m.b47 - 256*m.b43*m.b44*m.b48 - 160*m.b43*m.b44*m.b49 - 32*m.b43*m.b44*m.b50 - 416*m.b43*m.b45*
                       m.b46 - 192*m.b43*m.b45*m.b47 - 224*m.b43*m.b45*m.b48 - 128*m.b43*m.b45*m.b49 - 64*m.b43*m.b45*
                       m.b50 - 288*m.b43*m.b46*m.b47 - 192*m.b43*m.b46*m.b48 - 64*m.b43*m.b46*m.b49 - 64*m.b43*m.b46*
                       m.b50 - 192*m.b43*m.b47*m.b48 - 128*m.b43*m.b47*m.b49 - 64*m.b43*m.b47*m.b50 - 128*m.b43*m.b48*
                       m.b49 - 64*m.b43*m.b48*m.b50 - 64*m.b43*m.b49*m.b50 - 288*m.b44*m.b45*m.b46 - 352*m.b44*m.b45*
                       m.b47 - 256*m.b44*m.b45*m.b48 - 160*m.b44*m.b45*m.b49 - 64*m.b44*m.b45*m.b50 - 320*m.b44*m.b46*
                       m.b47 - 128*m.b44*m.b46*m.b48 - 128*m.b44*m.b46*m.b49 - 64*m.b44*m.b46*m.b50 - 192*m.b44*m.b47*
                       m.b48 - 128*m.b44*m.b47*m.b49 - 32*m.b44*m.b47*m.b50 - 128*m.b44*m.b48*m.b49 - 64*m.b44*m.b48*
                       m.b50 - 64*m.b44*m.b49*m.b50 - 224*m.b45*m.b46*m.b47 - 256*m.b45*m.b46*m.b48 - 160*m.b45*m.b46*
                       m.b49 - 64*m.b45*m.b46*m.b50 - 224*m.b45*m.b47*m.b48 - 64*m.b45*m.b47*m.b49 - 64*m.b45*m.b47*
                       m.b50 - 128*m.b45*m.b48*m.b49 - 64*m.b45*m.b48*m.b50 - 64*m.b45*m.b49*m.b50 - 160*m.b46*m.b47*
                       m.b48 - 160*m.b46*m.b47*m.b49 - 64*m.b46*m.b47*m.b50 - 128*m.b46*m.b48*m.b49 - 32*m.b46*m.b48*
                       m.b50 - 64*m.b46*m.b49*m.b50 - 96*m.b47*m.b48*m.b49 - 64*m.b47*m.b48*m.b50 - 64*m.b47*m.b49*m.b50
                        - 32*m.b48*m.b49*m.b50 + 160*m.b1*m.b2 + 152*m.b1*m.b3 + 144*m.b1*m.b4 + 136*m.b1*m.b5 + 128*
                       m.b1*m.b6 + 120*m.b1*m.b7 + 128*m.b1*m.b8 + 120*m.b1*m.b9 + 112*m.b1*m.b10 + 104*m.b1*m.b11 + 96*
                       m.b1*m.b12 + 88*m.b1*m.b13 + 320*m.b2*m.b3 + 320*m.b2*m.b4 + 304*m.b2*m.b5 + 288*m.b2*m.b6 + 272*
                       m.b2*m.b7 + 272*m.b2*m.b8 + 272*m.b2*m.b9 + 256*m.b2*m.b10 + 240*m.b2*m.b11 + 224*m.b2*m.b12 + 
                       192*m.b2*m.b13 + 88*m.b2*m.b14 + 496*m.b3*m.b4 + 488*m.b3*m.b5 + 480*m.b3*m.b6 + 456*m.b3*m.b7 + 
                       432*m.b3*m.b8 + 440*m.b3*m.b9 + 432*m.b3*m.b10 + 408*m.b3*m.b11 + 368*m.b3*m.b12 + 328*m.b3*m.b13
                        + 192*m.b3*m.b14 + 88*m.b3*m.b15 + 688*m.b4*m.b5 + 672*m.b4*m.b6 + 656*m.b4*m.b7 + 640*m.b4*m.b8
                        + 624*m.b4*m.b9 + 624*m.b4*m.b10 + 592*m.b4*m.b11 + 544*m.b4*m.b12 + 480*m.b4*m.b13 + 328*m.b4*
                       m.b14 + 192*m.b4*m.b15 + 88*m.b4*m.b16 + 896*m.b5*m.b6 + 872*m.b5*m.b7 + 848*m.b5*m.b8 + 824*m.b5
                       *m.b9 + 816*m.b5*m.b10 + 792*m.b5*m.b11 + 736*m.b5*m.b12 + 664*m.b5*m.b13 + 480*m.b5*m.b14 + 328*
                       m.b5*m.b15 + 192*m.b5*m.b16 + 88*m.b5*m.b17 + 1120*m.b6*m.b7 + 1088*m.b6*m.b8 + 1040*m.b6*m.b9 + 
                       1008*m.b6*m.b10 + 976*m.b6*m.b11 + 944*m.b6*m.b12 + 864*m.b6*m.b13 + 664*m.b6*m.b14 + 480*m.b6*
                       m.b15 + 328*m.b6*m.b16 + 192*m.b6*m.b17 + 88*m.b6*m.b18 + 1344*m.b7*m.b8 + 1288*m.b7*m.b9 + 1216*
                       m.b7*m.b10 + 1176*m.b7*m.b11 + 1120*m.b7*m.b12 + 1064*m.b7*m.b13 + 864*m.b7*m.b14 + 664*m.b7*
                       m.b15 + 480*m.b7*m.b16 + 328*m.b7*m.b17 + 192*m.b7*m.b18 + 88*m.b7*m.b19 + 1552*m.b8*m.b9 + 1472*
                       m.b8*m.b10 + 1392*m.b8*m.b11 + 1328*m.b8*m.b12 + 1248*m.b8*m.b13 + 1064*m.b8*m.b14 + 864*m.b8*
                       m.b15 + 664*m.b8*m.b16 + 480*m.b8*m.b17 + 328*m.b8*m.b18 + 192*m.b8*m.b19 + 88*m.b8*m.b20 + 1744*
                       m.b9*m.b10 + 1640*m.b9*m.b11 + 1552*m.b9*m.b12 + 1464*m.b9*m.b13 + 1248*m.b9*m.b14 + 1064*m.b9*
                       m.b15 + 864*m.b9*m.b16 + 664*m.b9*m.b17 + 480*m.b9*m.b18 + 328*m.b9*m.b19 + 192*m.b9*m.b20 + 88*
                       m.b9*m.b21 + 1920*m.b10*m.b11 + 1808*m.b10*m.b12 + 1696*m.b10*m.b13 + 1464*m.b10*m.b14 + 1248*
                       m.b10*m.b15 + 1064*m.b10*m.b16 + 864*m.b10*m.b17 + 664*m.b10*m.b18 + 480*m.b10*m.b19 + 328*m.b10*
                       m.b20 + 192*m.b10*m.b21 + 88*m.b10*m.b22 + 2080*m.b11*m.b12 + 1960*m.b11*m.b13 + 1696*m.b11*m.b14
                        + 1464*m.b11*m.b15 + 1248*m.b11*m.b16 + 1064*m.b11*m.b17 + 864*m.b11*m.b18 + 664*m.b11*m.b19 + 
                       480*m.b11*m.b20 + 328*m.b11*m.b21 + 192*m.b11*m.b22 + 88*m.b11*m.b23 + 2240*m.b12*m.b13 + 1960*
                       m.b12*m.b14 + 1696*m.b12*m.b15 + 1464*m.b12*m.b16 + 1248*m.b12*m.b17 + 1064*m.b12*m.b18 + 864*
                       m.b12*m.b19 + 664*m.b12*m.b20 + 480*m.b12*m.b21 + 328*m.b12*m.b22 + 192*m.b12*m.b23 + 88*m.b12*
                       m.b24 + 2240*m.b13*m.b14 + 1960*m.b13*m.b15 + 1696*m.b13*m.b16 + 1464*m.b13*m.b17 + 1248*m.b13*
                       m.b18 + 1064*m.b13*m.b19 + 864*m.b13*m.b20 + 664*m.b13*m.b21 + 480*m.b13*m.b22 + 328*m.b13*m.b23
                        + 192*m.b13*m.b24 + 88*m.b13*m.b25 + 2240*m.b14*m.b15 + 1960*m.b14*m.b16 + 1696*m.b14*m.b17 + 
                       1464*m.b14*m.b18 + 1248*m.b14*m.b19 + 1064*m.b14*m.b20 + 864*m.b14*m.b21 + 664*m.b14*m.b22 + 480*
                       m.b14*m.b23 + 328*m.b14*m.b24 + 192*m.b14*m.b25 + 88*m.b14*m.b26 + 2240*m.b15*m.b16 + 1960*m.b15*
                       m.b17 + 1696*m.b15*m.b18 + 1464*m.b15*m.b19 + 1248*m.b15*m.b20 + 1064*m.b15*m.b21 + 864*m.b15*
                       m.b22 + 664*m.b15*m.b23 + 480*m.b15*m.b24 + 328*m.b15*m.b25 + 192*m.b15*m.b26 + 88*m.b15*m.b27 + 
                       2240*m.b16*m.b17 + 1960*m.b16*m.b18 + 1696*m.b16*m.b19 + 1464*m.b16*m.b20 + 1248*m.b16*m.b21 + 
                       1064*m.b16*m.b22 + 864*m.b16*m.b23 + 664*m.b16*m.b24 + 480*m.b16*m.b25 + 328*m.b16*m.b26 + 192*
                       m.b16*m.b27 + 88*m.b16*m.b28 + 2240*m.b17*m.b18 + 1960*m.b17*m.b19 + 1696*m.b17*m.b20 + 1464*
                       m.b17*m.b21 + 1248*m.b17*m.b22 + 1064*m.b17*m.b23 + 864*m.b17*m.b24 + 664*m.b17*m.b25 + 480*m.b17
                       *m.b26 + 328*m.b17*m.b27 + 192*m.b17*m.b28 + 88*m.b17*m.b29 + 2240*m.b18*m.b19 + 1960*m.b18*m.b20
                        + 1696*m.b18*m.b21 + 1464*m.b18*m.b22 + 1248*m.b18*m.b23 + 1064*m.b18*m.b24 + 864*m.b18*m.b25 + 
                       664*m.b18*m.b26 + 480*m.b18*m.b27 + 328*m.b18*m.b28 + 192*m.b18*m.b29 + 88*m.b18*m.b30 + 2240*
                       m.b19*m.b20 + 1960*m.b19*m.b21 + 1696*m.b19*m.b22 + 1464*m.b19*m.b23 + 1248*m.b19*m.b24 + 1064*
                       m.b19*m.b25 + 864*m.b19*m.b26 + 664*m.b19*m.b27 + 480*m.b19*m.b28 + 328*m.b19*m.b29 + 192*m.b19*
                       m.b30 + 88*m.b19*m.b31 + 2240*m.b20*m.b21 + 1960*m.b20*m.b22 + 1696*m.b20*m.b23 + 1464*m.b20*
                       m.b24 + 1248*m.b20*m.b25 + 1064*m.b20*m.b26 + 864*m.b20*m.b27 + 664*m.b20*m.b28 + 480*m.b20*m.b29
                        + 328*m.b20*m.b30 + 192*m.b20*m.b31 + 88*m.b20*m.b32 + 2240*m.b21*m.b22 + 1960*m.b21*m.b23 + 
                       1696*m.b21*m.b24 + 1464*m.b21*m.b25 + 1248*m.b21*m.b26 + 1064*m.b21*m.b27 + 864*m.b21*m.b28 + 664
                       *m.b21*m.b29 + 480*m.b21*m.b30 + 328*m.b21*m.b31 + 192*m.b21*m.b32 + 88*m.b21*m.b33 + 2240*m.b22*
                       m.b23 + 1960*m.b22*m.b24 + 1696*m.b22*m.b25 + 1464*m.b22*m.b26 + 1248*m.b22*m.b27 + 1064*m.b22*
                       m.b28 + 864*m.b22*m.b29 + 664*m.b22*m.b30 + 480*m.b22*m.b31 + 328*m.b22*m.b32 + 192*m.b22*m.b33
                        + 88*m.b22*m.b34 + 2240*m.b23*m.b24 + 1960*m.b23*m.b25 + 1696*m.b23*m.b26 + 1464*m.b23*m.b27 + 
                       1248*m.b23*m.b28 + 1064*m.b23*m.b29 + 864*m.b23*m.b30 + 664*m.b23*m.b31 + 480*m.b23*m.b32 + 328*
                       m.b23*m.b33 + 192*m.b23*m.b34 + 88*m.b23*m.b35 + 2240*m.b24*m.b25 + 1960*m.b24*m.b26 + 1696*m.b24
                       *m.b27 + 1464*m.b24*m.b28 + 1248*m.b24*m.b29 + 1064*m.b24*m.b30 + 864*m.b24*m.b31 + 664*m.b24*
                       m.b32 + 480*m.b24*m.b33 + 328*m.b24*m.b34 + 192*m.b24*m.b35 + 88*m.b24*m.b36 + 2240*m.b25*m.b26
                        + 1960*m.b25*m.b27 + 1696*m.b25*m.b28 + 1464*m.b25*m.b29 + 1248*m.b25*m.b30 + 1064*m.b25*m.b31
                        + 864*m.b25*m.b32 + 664*m.b25*m.b33 + 480*m.b25*m.b34 + 328*m.b25*m.b35 + 192*m.b25*m.b36 + 88*
                       m.b25*m.b37 + 2240*m.b26*m.b27 + 1960*m.b26*m.b28 + 1696*m.b26*m.b29 + 1464*m.b26*m.b30 + 1248*
                       m.b26*m.b31 + 1064*m.b26*m.b32 + 864*m.b26*m.b33 + 664*m.b26*m.b34 + 480*m.b26*m.b35 + 328*m.b26*
                       m.b36 + 192*m.b26*m.b37 + 88*m.b26*m.b38 + 2240*m.b27*m.b28 + 1960*m.b27*m.b29 + 1696*m.b27*m.b30
                        + 1464*m.b27*m.b31 + 1248*m.b27*m.b32 + 1064*m.b27*m.b33 + 864*m.b27*m.b34 + 664*m.b27*m.b35 + 
                       480*m.b27*m.b36 + 328*m.b27*m.b37 + 192*m.b27*m.b38 + 88*m.b27*m.b39 + 2240*m.b28*m.b29 + 1960*
                       m.b28*m.b30 + 1696*m.b28*m.b31 + 1464*m.b28*m.b32 + 1248*m.b28*m.b33 + 1064*m.b28*m.b34 + 864*
                       m.b28*m.b35 + 664*m.b28*m.b36 + 480*m.b28*m.b37 + 328*m.b28*m.b38 + 192*m.b28*m.b39 + 88*m.b28*
                       m.b40 + 2240*m.b29*m.b30 + 1960*m.b29*m.b31 + 1696*m.b29*m.b32 + 1464*m.b29*m.b33 + 1248*m.b29*
                       m.b34 + 1064*m.b29*m.b35 + 864*m.b29*m.b36 + 664*m.b29*m.b37 + 480*m.b29*m.b38 + 328*m.b29*m.b39
                        + 192*m.b29*m.b40 + 88*m.b29*m.b41 + 2240*m.b30*m.b31 + 1960*m.b30*m.b32 + 1696*m.b30*m.b33 + 
                       1464*m.b30*m.b34 + 1248*m.b30*m.b35 + 1064*m.b30*m.b36 + 864*m.b30*m.b37 + 664*m.b30*m.b38 + 480*
                       m.b30*m.b39 + 328*m.b30*m.b40 + 192*m.b30*m.b41 + 88*m.b30*m.b42 + 2240*m.b31*m.b32 + 1960*m.b31*
                       m.b33 + 1696*m.b31*m.b34 + 1464*m.b31*m.b35 + 1248*m.b31*m.b36 + 1064*m.b31*m.b37 + 864*m.b31*
                       m.b38 + 664*m.b31*m.b39 + 480*m.b31*m.b40 + 328*m.b31*m.b41 + 192*m.b31*m.b42 + 88*m.b31*m.b43 + 
                       2240*m.b32*m.b33 + 1960*m.b32*m.b34 + 1696*m.b32*m.b35 + 1464*m.b32*m.b36 + 1248*m.b32*m.b37 + 
                       1064*m.b32*m.b38 + 864*m.b32*m.b39 + 664*m.b32*m.b40 + 480*m.b32*m.b41 + 328*m.b32*m.b42 + 192*
                       m.b32*m.b43 + 88*m.b32*m.b44 + 2240*m.b33*m.b34 + 1960*m.b33*m.b35 + 1696*m.b33*m.b36 + 1464*
                       m.b33*m.b37 + 1248*m.b33*m.b38 + 1064*m.b33*m.b39 + 864*m.b33*m.b40 + 664*m.b33*m.b41 + 480*m.b33
                       *m.b42 + 328*m.b33*m.b43 + 192*m.b33*m.b44 + 88*m.b33*m.b45 + 2240*m.b34*m.b35 + 1960*m.b34*m.b36
                        + 1696*m.b34*m.b37 + 1464*m.b34*m.b38 + 1248*m.b34*m.b39 + 1064*m.b34*m.b40 + 864*m.b34*m.b41 + 
                       664*m.b34*m.b42 + 480*m.b34*m.b43 + 328*m.b34*m.b44 + 192*m.b34*m.b45 + 88*m.b34*m.b46 + 2240*
                       m.b35*m.b36 + 1960*m.b35*m.b37 + 1696*m.b35*m.b38 + 1464*m.b35*m.b39 + 1248*m.b35*m.b40 + 1064*
                       m.b35*m.b41 + 864*m.b35*m.b42 + 664*m.b35*m.b43 + 480*m.b35*m.b44 + 328*m.b35*m.b45 + 192*m.b35*
                       m.b46 + 88*m.b35*m.b47 + 2240*m.b36*m.b37 + 1960*m.b36*m.b38 + 1696*m.b36*m.b39 + 1464*m.b36*
                       m.b40 + 1248*m.b36*m.b41 + 1064*m.b36*m.b42 + 864*m.b36*m.b43 + 664*m.b36*m.b44 + 480*m.b36*m.b45
                        + 328*m.b36*m.b46 + 192*m.b36*m.b47 + 88*m.b36*m.b48 + 2240*m.b37*m.b38 + 1960*m.b37*m.b39 + 
                       1696*m.b37*m.b40 + 1464*m.b37*m.b41 + 1248*m.b37*m.b42 + 1064*m.b37*m.b43 + 864*m.b37*m.b44 + 664
                       *m.b37*m.b45 + 480*m.b37*m.b46 + 328*m.b37*m.b47 + 192*m.b37*m.b48 + 88*m.b37*m.b49 + 2240*m.b38*
                       m.b39 + 1960*m.b38*m.b40 + 1696*m.b38*m.b41 + 1464*m.b38*m.b42 + 1248*m.b38*m.b43 + 1064*m.b38*
                       m.b44 + 864*m.b38*m.b45 + 664*m.b38*m.b46 + 480*m.b38*m.b47 + 328*m.b38*m.b48 + 192*m.b38*m.b49
                        + 88*m.b38*m.b50 + 2080*m.b39*m.b40 + 1808*m.b39*m.b41 + 1552*m.b39*m.b42 + 1328*m.b39*m.b43 + 
                       1120*m.b39*m.b44 + 944*m.b39*m.b45 + 736*m.b39*m.b46 + 544*m.b39*m.b47 + 368*m.b39*m.b48 + 224*
                       m.b39*m.b49 + 96*m.b39*m.b50 + 1920*m.b40*m.b41 + 1640*m.b40*m.b42 + 1392*m.b40*m.b43 + 1176*
                       m.b40*m.b44 + 976*m.b40*m.b45 + 792*m.b40*m.b46 + 592*m.b40*m.b47 + 408*m.b40*m.b48 + 240*m.b40*
                       m.b49 + 104*m.b40*m.b50 + 1744*m.b41*m.b42 + 1472*m.b41*m.b43 + 1216*m.b41*m.b44 + 1008*m.b41*
                       m.b45 + 816*m.b41*m.b46 + 624*m.b41*m.b47 + 432*m.b41*m.b48 + 256*m.b41*m.b49 + 112*m.b41*m.b50
                        + 1552*m.b42*m.b43 + 1288*m.b42*m.b44 + 1040*m.b42*m.b45 + 824*m.b42*m.b46 + 624*m.b42*m.b47 + 
                       440*m.b42*m.b48 + 272*m.b42*m.b49 + 120*m.b42*m.b50 + 1344*m.b43*m.b44 + 1088*m.b43*m.b45 + 848*
                       m.b43*m.b46 + 640*m.b43*m.b47 + 432*m.b43*m.b48 + 272*m.b43*m.b49 + 128*m.b43*m.b50 + 1120*m.b44*
                       m.b45 + 872*m.b44*m.b46 + 656*m.b44*m.b47 + 456*m.b44*m.b48 + 272*m.b44*m.b49 + 120*m.b44*m.b50
                        + 896*m.b45*m.b46 + 672*m.b45*m.b47 + 480*m.b45*m.b48 + 288*m.b45*m.b49 + 128*m.b45*m.b50 + 688*
                       m.b46*m.b47 + 488*m.b46*m.b48 + 304*m.b46*m.b49 + 136*m.b46*m.b50 + 496*m.b47*m.b48 + 320*m.b47*
                       m.b49 + 144*m.b47*m.b50 + 320*m.b48*m.b49 + 152*m.b48*m.b50 + 160*m.b49*m.b50 - 264*m.b1 - 564*
                       m.b2 - 892*m.b3 - 1240*m.b4 - 1600*m.b5 - 1964*m.b6 - 2324*m.b7 - 2688*m.b8 - 3048*m.b9 - 3396*
                       m.b10 - 3724*m.b11 - 4024*m.b12 - 4288*m.b13 - 4288*m.b14 - 4288*m.b15 - 4288*m.b16 - 4288*m.b17
                        - 4288*m.b18 - 4288*m.b19 - 4288*m.b20 - 4288*m.b21 - 4288*m.b22 - 4288*m.b23 - 4288*m.b24 - 
                       4288*m.b25 - 4288*m.b26 - 4288*m.b27 - 4288*m.b28 - 4288*m.b29 - 4288*m.b30 - 4288*m.b31 - 4288*
                       m.b32 - 4288*m.b33 - 4288*m.b34 - 4288*m.b35 - 4288*m.b36 - 4288*m.b37 - 4288*m.b38 - 4024*m.b39
                        - 3724*m.b40 - 3396*m.b41 - 3048*m.b42 - 2688*m.b43 - 2324*m.b44 - 1964*m.b45 - 1600*m.b46 - 
                       1240*m.b47 - 892*m.b48 - 564*m.b49 - 264*m.b50 - m.x51 <= 0)
