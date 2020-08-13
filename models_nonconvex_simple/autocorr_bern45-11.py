#  MINLP written by GAMS Convert at 08/13/20 17:37:49
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         46        1       45        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         46        1       45        0


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
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x46, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*
                       m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*
                       m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b5*m.b6*m.b10 + 64
                       *m.b1*m.b5*m.b7*m.b11 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*
                       m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 128*m.b2*
                       m.b3*m.b10*m.b11 + 64*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8
                        + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*m.b4*m.b9*m.b11 + 64*m.b2*m.b4*
                       m.b10*m.b12 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10 + 128*m.b2*m.b5*m.b8*m.b11 + 64*
                       m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b6*m.b7*m.b11 + 64*m.b2*m.b6*m.b8*m.b12 + 192*m.b3*m.b4*m.b5*
                       m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*
                       m.b4*m.b9*m.b10 + 192*m.b3*m.b4*m.b10*m.b11 + 128*m.b3*m.b4*m.b11*m.b12 + 64*m.b3*m.b4*m.b12*
                       m.b13 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*m.b5*m.b8*m.b10 + 192*m.b3*
                       m.b5*m.b9*m.b11 + 128*m.b3*m.b5*m.b10*m.b12 + 64*m.b3*m.b5*m.b11*m.b13 + 192*m.b3*m.b6*m.b7*m.b10
                        + 192*m.b3*m.b6*m.b8*m.b11 + 128*m.b3*m.b6*m.b9*m.b12 + 64*m.b3*m.b6*m.b10*m.b13 + 128*m.b3*m.b7
                       *m.b8*m.b12 + 64*m.b3*m.b7*m.b9*m.b13 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*
                       m.b4*m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 192*m.b4*m.b5*m.b11*
                       m.b12 + 128*m.b4*m.b5*m.b12*m.b13 + 64*m.b4*m.b5*m.b13*m.b14 + 256*m.b4*m.b6*m.b7*m.b9 + 256*m.b4
                       *m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 192*m.b4*m.b6*m.b10*m.b12 + 128*m.b4*m.b6*m.b11*
                       m.b13 + 64*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*m.b7*m.b8*m.b11 + 192*m.b4*m.b7*m.b9*m.b12 + 128*m.b4
                       *m.b7*m.b10*m.b13 + 64*m.b4*m.b7*m.b11*m.b14 + 128*m.b4*m.b8*m.b9*m.b13 + 64*m.b4*m.b8*m.b10*
                       m.b14 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*
                       m.b6*m.b10*m.b11 + 256*m.b5*m.b6*m.b11*m.b12 + 192*m.b5*m.b6*m.b12*m.b13 + 128*m.b5*m.b6*m.b13*
                       m.b14 + 64*m.b5*m.b6*m.b14*m.b15 + 320*m.b5*m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*m.b11 + 256*m.b5
                       *m.b7*m.b10*m.b12 + 192*m.b5*m.b7*m.b11*m.b13 + 128*m.b5*m.b7*m.b12*m.b14 + 64*m.b5*m.b7*m.b13*
                       m.b15 + 256*m.b5*m.b8*m.b9*m.b12 + 192*m.b5*m.b8*m.b10*m.b13 + 128*m.b5*m.b8*m.b11*m.b14 + 64*
                       m.b5*m.b8*m.b12*m.b15 + 128*m.b5*m.b9*m.b10*m.b14 + 64*m.b5*m.b9*m.b11*m.b15 + 384*m.b6*m.b7*m.b8
                       *m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 320*m.b6*m.b7*m.b11*m.b12 + 256*
                       m.b6*m.b7*m.b12*m.b13 + 192*m.b6*m.b7*m.b13*m.b14 + 128*m.b6*m.b7*m.b14*m.b15 + 64*m.b6*m.b7*
                       m.b15*m.b16 + 384*m.b6*m.b8*m.b9*m.b11 + 320*m.b6*m.b8*m.b10*m.b12 + 256*m.b6*m.b8*m.b11*m.b13 + 
                       192*m.b6*m.b8*m.b12*m.b14 + 128*m.b6*m.b8*m.b13*m.b15 + 64*m.b6*m.b8*m.b14*m.b16 + 256*m.b6*m.b9*
                       m.b10*m.b13 + 192*m.b6*m.b9*m.b11*m.b14 + 128*m.b6*m.b9*m.b12*m.b15 + 64*m.b6*m.b9*m.b13*m.b16 + 
                       128*m.b6*m.b10*m.b11*m.b15 + 64*m.b6*m.b10*m.b12*m.b16 + 448*m.b7*m.b8*m.b9*m.b10 + 448*m.b7*m.b8
                       *m.b10*m.b11 + 384*m.b7*m.b8*m.b11*m.b12 + 320*m.b7*m.b8*m.b12*m.b13 + 256*m.b7*m.b8*m.b13*m.b14
                        + 192*m.b7*m.b8*m.b14*m.b15 + 128*m.b7*m.b8*m.b15*m.b16 + 64*m.b7*m.b8*m.b16*m.b17 + 384*m.b7*
                       m.b9*m.b10*m.b12 + 320*m.b7*m.b9*m.b11*m.b13 + 256*m.b7*m.b9*m.b12*m.b14 + 192*m.b7*m.b9*m.b13*
                       m.b15 + 128*m.b7*m.b9*m.b14*m.b16 + 64*m.b7*m.b9*m.b15*m.b17 + 256*m.b7*m.b10*m.b11*m.b14 + 192*
                       m.b7*m.b10*m.b12*m.b15 + 128*m.b7*m.b10*m.b13*m.b16 + 64*m.b7*m.b10*m.b14*m.b17 + 128*m.b7*m.b11*
                       m.b12*m.b16 + 64*m.b7*m.b11*m.b13*m.b17 + 512*m.b8*m.b9*m.b10*m.b11 + 448*m.b8*m.b9*m.b11*m.b12
                        + 384*m.b8*m.b9*m.b12*m.b13 + 320*m.b8*m.b9*m.b13*m.b14 + 256*m.b8*m.b9*m.b14*m.b15 + 192*m.b8*
                       m.b9*m.b15*m.b16 + 128*m.b8*m.b9*m.b16*m.b17 + 64*m.b8*m.b9*m.b17*m.b18 + 384*m.b8*m.b10*m.b11*
                       m.b13 + 320*m.b8*m.b10*m.b12*m.b14 + 256*m.b8*m.b10*m.b13*m.b15 + 192*m.b8*m.b10*m.b14*m.b16 + 
                       128*m.b8*m.b10*m.b15*m.b17 + 64*m.b8*m.b10*m.b16*m.b18 + 256*m.b8*m.b11*m.b12*m.b15 + 192*m.b8*
                       m.b11*m.b13*m.b16 + 128*m.b8*m.b11*m.b14*m.b17 + 64*m.b8*m.b11*m.b15*m.b18 + 128*m.b8*m.b12*m.b13
                       *m.b17 + 64*m.b8*m.b12*m.b14*m.b18 + 512*m.b9*m.b10*m.b11*m.b12 + 448*m.b9*m.b10*m.b12*m.b13 + 
                       384*m.b9*m.b10*m.b13*m.b14 + 320*m.b9*m.b10*m.b14*m.b15 + 256*m.b9*m.b10*m.b15*m.b16 + 192*m.b9*
                       m.b10*m.b16*m.b17 + 128*m.b9*m.b10*m.b17*m.b18 + 64*m.b9*m.b10*m.b18*m.b19 + 384*m.b9*m.b11*m.b12
                       *m.b14 + 320*m.b9*m.b11*m.b13*m.b15 + 256*m.b9*m.b11*m.b14*m.b16 + 192*m.b9*m.b11*m.b15*m.b17 + 
                       128*m.b9*m.b11*m.b16*m.b18 + 64*m.b9*m.b11*m.b17*m.b19 + 256*m.b9*m.b12*m.b13*m.b16 + 192*m.b9*
                       m.b12*m.b14*m.b17 + 128*m.b9*m.b12*m.b15*m.b18 + 64*m.b9*m.b12*m.b16*m.b19 + 128*m.b9*m.b13*m.b14
                       *m.b18 + 64*m.b9*m.b13*m.b15*m.b19 + 512*m.b10*m.b11*m.b12*m.b13 + 448*m.b10*m.b11*m.b13*m.b14 + 
                       384*m.b10*m.b11*m.b14*m.b15 + 320*m.b10*m.b11*m.b15*m.b16 + 256*m.b10*m.b11*m.b16*m.b17 + 192*
                       m.b10*m.b11*m.b17*m.b18 + 128*m.b10*m.b11*m.b18*m.b19 + 64*m.b10*m.b11*m.b19*m.b20 + 384*m.b10*
                       m.b12*m.b13*m.b15 + 320*m.b10*m.b12*m.b14*m.b16 + 256*m.b10*m.b12*m.b15*m.b17 + 192*m.b10*m.b12*
                       m.b16*m.b18 + 128*m.b10*m.b12*m.b17*m.b19 + 64*m.b10*m.b12*m.b18*m.b20 + 256*m.b10*m.b13*m.b14*
                       m.b17 + 192*m.b10*m.b13*m.b15*m.b18 + 128*m.b10*m.b13*m.b16*m.b19 + 64*m.b10*m.b13*m.b17*m.b20 + 
                       128*m.b10*m.b14*m.b15*m.b19 + 64*m.b10*m.b14*m.b16*m.b20 + 512*m.b11*m.b12*m.b13*m.b14 + 448*
                       m.b11*m.b12*m.b14*m.b15 + 384*m.b11*m.b12*m.b15*m.b16 + 320*m.b11*m.b12*m.b16*m.b17 + 256*m.b11*
                       m.b12*m.b17*m.b18 + 192*m.b11*m.b12*m.b18*m.b19 + 128*m.b11*m.b12*m.b19*m.b20 + 64*m.b11*m.b12*
                       m.b20*m.b21 + 384*m.b11*m.b13*m.b14*m.b16 + 320*m.b11*m.b13*m.b15*m.b17 + 256*m.b11*m.b13*m.b16*
                       m.b18 + 192*m.b11*m.b13*m.b17*m.b19 + 128*m.b11*m.b13*m.b18*m.b20 + 64*m.b11*m.b13*m.b19*m.b21 + 
                       256*m.b11*m.b14*m.b15*m.b18 + 192*m.b11*m.b14*m.b16*m.b19 + 128*m.b11*m.b14*m.b17*m.b20 + 64*
                       m.b11*m.b14*m.b18*m.b21 + 128*m.b11*m.b15*m.b16*m.b20 + 64*m.b11*m.b15*m.b17*m.b21 + 512*m.b12*
                       m.b13*m.b14*m.b15 + 448*m.b12*m.b13*m.b15*m.b16 + 384*m.b12*m.b13*m.b16*m.b17 + 320*m.b12*m.b13*
                       m.b17*m.b18 + 256*m.b12*m.b13*m.b18*m.b19 + 192*m.b12*m.b13*m.b19*m.b20 + 128*m.b12*m.b13*m.b20*
                       m.b21 + 64*m.b12*m.b13*m.b21*m.b22 + 384*m.b12*m.b14*m.b15*m.b17 + 320*m.b12*m.b14*m.b16*m.b18 + 
                       256*m.b12*m.b14*m.b17*m.b19 + 192*m.b12*m.b14*m.b18*m.b20 + 128*m.b12*m.b14*m.b19*m.b21 + 64*
                       m.b12*m.b14*m.b20*m.b22 + 256*m.b12*m.b15*m.b16*m.b19 + 192*m.b12*m.b15*m.b17*m.b20 + 128*m.b12*
                       m.b15*m.b18*m.b21 + 64*m.b12*m.b15*m.b19*m.b22 + 128*m.b12*m.b16*m.b17*m.b21 + 64*m.b12*m.b16*
                       m.b18*m.b22 + 512*m.b13*m.b14*m.b15*m.b16 + 448*m.b13*m.b14*m.b16*m.b17 + 384*m.b13*m.b14*m.b17*
                       m.b18 + 320*m.b13*m.b14*m.b18*m.b19 + 256*m.b13*m.b14*m.b19*m.b20 + 192*m.b13*m.b14*m.b20*m.b21
                        + 128*m.b13*m.b14*m.b21*m.b22 + 64*m.b13*m.b14*m.b22*m.b23 + 384*m.b13*m.b15*m.b16*m.b18 + 320*
                       m.b13*m.b15*m.b17*m.b19 + 256*m.b13*m.b15*m.b18*m.b20 + 192*m.b13*m.b15*m.b19*m.b21 + 128*m.b13*
                       m.b15*m.b20*m.b22 + 64*m.b13*m.b15*m.b21*m.b23 + 256*m.b13*m.b16*m.b17*m.b20 + 192*m.b13*m.b16*
                       m.b18*m.b21 + 128*m.b13*m.b16*m.b19*m.b22 + 64*m.b13*m.b16*m.b20*m.b23 + 128*m.b13*m.b17*m.b18*
                       m.b22 + 64*m.b13*m.b17*m.b19*m.b23 + 512*m.b14*m.b15*m.b16*m.b17 + 448*m.b14*m.b15*m.b17*m.b18 + 
                       384*m.b14*m.b15*m.b18*m.b19 + 320*m.b14*m.b15*m.b19*m.b20 + 256*m.b14*m.b15*m.b20*m.b21 + 192*
                       m.b14*m.b15*m.b21*m.b22 + 128*m.b14*m.b15*m.b22*m.b23 + 64*m.b14*m.b15*m.b23*m.b24 + 384*m.b14*
                       m.b16*m.b17*m.b19 + 320*m.b14*m.b16*m.b18*m.b20 + 256*m.b14*m.b16*m.b19*m.b21 + 192*m.b14*m.b16*
                       m.b20*m.b22 + 128*m.b14*m.b16*m.b21*m.b23 + 64*m.b14*m.b16*m.b22*m.b24 + 256*m.b14*m.b17*m.b18*
                       m.b21 + 192*m.b14*m.b17*m.b19*m.b22 + 128*m.b14*m.b17*m.b20*m.b23 + 64*m.b14*m.b17*m.b21*m.b24 + 
                       128*m.b14*m.b18*m.b19*m.b23 + 64*m.b14*m.b18*m.b20*m.b24 + 512*m.b15*m.b16*m.b17*m.b18 + 448*
                       m.b15*m.b16*m.b18*m.b19 + 384*m.b15*m.b16*m.b19*m.b20 + 320*m.b15*m.b16*m.b20*m.b21 + 256*m.b15*
                       m.b16*m.b21*m.b22 + 192*m.b15*m.b16*m.b22*m.b23 + 128*m.b15*m.b16*m.b23*m.b24 + 64*m.b15*m.b16*
                       m.b24*m.b25 + 384*m.b15*m.b17*m.b18*m.b20 + 320*m.b15*m.b17*m.b19*m.b21 + 256*m.b15*m.b17*m.b20*
                       m.b22 + 192*m.b15*m.b17*m.b21*m.b23 + 128*m.b15*m.b17*m.b22*m.b24 + 64*m.b15*m.b17*m.b23*m.b25 + 
                       256*m.b15*m.b18*m.b19*m.b22 + 192*m.b15*m.b18*m.b20*m.b23 + 128*m.b15*m.b18*m.b21*m.b24 + 64*
                       m.b15*m.b18*m.b22*m.b25 + 128*m.b15*m.b19*m.b20*m.b24 + 64*m.b15*m.b19*m.b21*m.b25 + 512*m.b16*
                       m.b17*m.b18*m.b19 + 448*m.b16*m.b17*m.b19*m.b20 + 384*m.b16*m.b17*m.b20*m.b21 + 320*m.b16*m.b17*
                       m.b21*m.b22 + 256*m.b16*m.b17*m.b22*m.b23 + 192*m.b16*m.b17*m.b23*m.b24 + 128*m.b16*m.b17*m.b24*
                       m.b25 + 64*m.b16*m.b17*m.b25*m.b26 + 384*m.b16*m.b18*m.b19*m.b21 + 320*m.b16*m.b18*m.b20*m.b22 + 
                       256*m.b16*m.b18*m.b21*m.b23 + 192*m.b16*m.b18*m.b22*m.b24 + 128*m.b16*m.b18*m.b23*m.b25 + 64*
                       m.b16*m.b18*m.b24*m.b26 + 256*m.b16*m.b19*m.b20*m.b23 + 192*m.b16*m.b19*m.b21*m.b24 + 128*m.b16*
                       m.b19*m.b22*m.b25 + 64*m.b16*m.b19*m.b23*m.b26 + 128*m.b16*m.b20*m.b21*m.b25 + 64*m.b16*m.b20*
                       m.b22*m.b26 + 512*m.b17*m.b18*m.b19*m.b20 + 448*m.b17*m.b18*m.b20*m.b21 + 384*m.b17*m.b18*m.b21*
                       m.b22 + 320*m.b17*m.b18*m.b22*m.b23 + 256*m.b17*m.b18*m.b23*m.b24 + 192*m.b17*m.b18*m.b24*m.b25
                        + 128*m.b17*m.b18*m.b25*m.b26 + 64*m.b17*m.b18*m.b26*m.b27 + 384*m.b17*m.b19*m.b20*m.b22 + 320*
                       m.b17*m.b19*m.b21*m.b23 + 256*m.b17*m.b19*m.b22*m.b24 + 192*m.b17*m.b19*m.b23*m.b25 + 128*m.b17*
                       m.b19*m.b24*m.b26 + 64*m.b17*m.b19*m.b25*m.b27 + 256*m.b17*m.b20*m.b21*m.b24 + 192*m.b17*m.b20*
                       m.b22*m.b25 + 128*m.b17*m.b20*m.b23*m.b26 + 64*m.b17*m.b20*m.b24*m.b27 + 128*m.b17*m.b21*m.b22*
                       m.b26 + 64*m.b17*m.b21*m.b23*m.b27 + 512*m.b18*m.b19*m.b20*m.b21 + 448*m.b18*m.b19*m.b21*m.b22 + 
                       384*m.b18*m.b19*m.b22*m.b23 + 320*m.b18*m.b19*m.b23*m.b24 + 256*m.b18*m.b19*m.b24*m.b25 + 192*
                       m.b18*m.b19*m.b25*m.b26 + 128*m.b18*m.b19*m.b26*m.b27 + 64*m.b18*m.b19*m.b27*m.b28 + 384*m.b18*
                       m.b20*m.b21*m.b23 + 320*m.b18*m.b20*m.b22*m.b24 + 256*m.b18*m.b20*m.b23*m.b25 + 192*m.b18*m.b20*
                       m.b24*m.b26 + 128*m.b18*m.b20*m.b25*m.b27 + 64*m.b18*m.b20*m.b26*m.b28 + 256*m.b18*m.b21*m.b22*
                       m.b25 + 192*m.b18*m.b21*m.b23*m.b26 + 128*m.b18*m.b21*m.b24*m.b27 + 64*m.b18*m.b21*m.b25*m.b28 + 
                       128*m.b18*m.b22*m.b23*m.b27 + 64*m.b18*m.b22*m.b24*m.b28 + 512*m.b19*m.b20*m.b21*m.b22 + 448*
                       m.b19*m.b20*m.b22*m.b23 + 384*m.b19*m.b20*m.b23*m.b24 + 320*m.b19*m.b20*m.b24*m.b25 + 256*m.b19*
                       m.b20*m.b25*m.b26 + 192*m.b19*m.b20*m.b26*m.b27 + 128*m.b19*m.b20*m.b27*m.b28 + 64*m.b19*m.b20*
                       m.b28*m.b29 + 384*m.b19*m.b21*m.b22*m.b24 + 320*m.b19*m.b21*m.b23*m.b25 + 256*m.b19*m.b21*m.b24*
                       m.b26 + 192*m.b19*m.b21*m.b25*m.b27 + 128*m.b19*m.b21*m.b26*m.b28 + 64*m.b19*m.b21*m.b27*m.b29 + 
                       256*m.b19*m.b22*m.b23*m.b26 + 192*m.b19*m.b22*m.b24*m.b27 + 128*m.b19*m.b22*m.b25*m.b28 + 64*
                       m.b19*m.b22*m.b26*m.b29 + 128*m.b19*m.b23*m.b24*m.b28 + 64*m.b19*m.b23*m.b25*m.b29 + 512*m.b20*
                       m.b21*m.b22*m.b23 + 448*m.b20*m.b21*m.b23*m.b24 + 384*m.b20*m.b21*m.b24*m.b25 + 320*m.b20*m.b21*
                       m.b25*m.b26 + 256*m.b20*m.b21*m.b26*m.b27 + 192*m.b20*m.b21*m.b27*m.b28 + 128*m.b20*m.b21*m.b28*
                       m.b29 + 64*m.b20*m.b21*m.b29*m.b30 + 384*m.b20*m.b22*m.b23*m.b25 + 320*m.b20*m.b22*m.b24*m.b26 + 
                       256*m.b20*m.b22*m.b25*m.b27 + 192*m.b20*m.b22*m.b26*m.b28 + 128*m.b20*m.b22*m.b27*m.b29 + 64*
                       m.b20*m.b22*m.b28*m.b30 + 256*m.b20*m.b23*m.b24*m.b27 + 192*m.b20*m.b23*m.b25*m.b28 + 128*m.b20*
                       m.b23*m.b26*m.b29 + 64*m.b20*m.b23*m.b27*m.b30 + 128*m.b20*m.b24*m.b25*m.b29 + 64*m.b20*m.b24*
                       m.b26*m.b30 + 512*m.b21*m.b22*m.b23*m.b24 + 448*m.b21*m.b22*m.b24*m.b25 + 384*m.b21*m.b22*m.b25*
                       m.b26 + 320*m.b21*m.b22*m.b26*m.b27 + 256*m.b21*m.b22*m.b27*m.b28 + 192*m.b21*m.b22*m.b28*m.b29
                        + 128*m.b21*m.b22*m.b29*m.b30 + 64*m.b21*m.b22*m.b30*m.b31 + 384*m.b21*m.b23*m.b24*m.b26 + 320*
                       m.b21*m.b23*m.b25*m.b27 + 256*m.b21*m.b23*m.b26*m.b28 + 192*m.b21*m.b23*m.b27*m.b29 + 128*m.b21*
                       m.b23*m.b28*m.b30 + 64*m.b21*m.b23*m.b29*m.b31 + 256*m.b21*m.b24*m.b25*m.b28 + 192*m.b21*m.b24*
                       m.b26*m.b29 + 128*m.b21*m.b24*m.b27*m.b30 + 64*m.b21*m.b24*m.b28*m.b31 + 128*m.b21*m.b25*m.b26*
                       m.b30 + 64*m.b21*m.b25*m.b27*m.b31 + 512*m.b22*m.b23*m.b24*m.b25 + 448*m.b22*m.b23*m.b25*m.b26 + 
                       384*m.b22*m.b23*m.b26*m.b27 + 320*m.b22*m.b23*m.b27*m.b28 + 256*m.b22*m.b23*m.b28*m.b29 + 192*
                       m.b22*m.b23*m.b29*m.b30 + 128*m.b22*m.b23*m.b30*m.b31 + 64*m.b22*m.b23*m.b31*m.b32 + 384*m.b22*
                       m.b24*m.b25*m.b27 + 320*m.b22*m.b24*m.b26*m.b28 + 256*m.b22*m.b24*m.b27*m.b29 + 192*m.b22*m.b24*
                       m.b28*m.b30 + 128*m.b22*m.b24*m.b29*m.b31 + 64*m.b22*m.b24*m.b30*m.b32 + 256*m.b22*m.b25*m.b26*
                       m.b29 + 192*m.b22*m.b25*m.b27*m.b30 + 128*m.b22*m.b25*m.b28*m.b31 + 64*m.b22*m.b25*m.b29*m.b32 + 
                       128*m.b22*m.b26*m.b27*m.b31 + 64*m.b22*m.b26*m.b28*m.b32 + 512*m.b23*m.b24*m.b25*m.b26 + 448*
                       m.b23*m.b24*m.b26*m.b27 + 384*m.b23*m.b24*m.b27*m.b28 + 320*m.b23*m.b24*m.b28*m.b29 + 256*m.b23*
                       m.b24*m.b29*m.b30 + 192*m.b23*m.b24*m.b30*m.b31 + 128*m.b23*m.b24*m.b31*m.b32 + 64*m.b23*m.b24*
                       m.b32*m.b33 + 384*m.b23*m.b25*m.b26*m.b28 + 320*m.b23*m.b25*m.b27*m.b29 + 256*m.b23*m.b25*m.b28*
                       m.b30 + 192*m.b23*m.b25*m.b29*m.b31 + 128*m.b23*m.b25*m.b30*m.b32 + 64*m.b23*m.b25*m.b31*m.b33 + 
                       256*m.b23*m.b26*m.b27*m.b30 + 192*m.b23*m.b26*m.b28*m.b31 + 128*m.b23*m.b26*m.b29*m.b32 + 64*
                       m.b23*m.b26*m.b30*m.b33 + 128*m.b23*m.b27*m.b28*m.b32 + 64*m.b23*m.b27*m.b29*m.b33 + 512*m.b24*
                       m.b25*m.b26*m.b27 + 448*m.b24*m.b25*m.b27*m.b28 + 384*m.b24*m.b25*m.b28*m.b29 + 320*m.b24*m.b25*
                       m.b29*m.b30 + 256*m.b24*m.b25*m.b30*m.b31 + 192*m.b24*m.b25*m.b31*m.b32 + 128*m.b24*m.b25*m.b32*
                       m.b33 + 64*m.b24*m.b25*m.b33*m.b34 + 384*m.b24*m.b26*m.b27*m.b29 + 320*m.b24*m.b26*m.b28*m.b30 + 
                       256*m.b24*m.b26*m.b29*m.b31 + 192*m.b24*m.b26*m.b30*m.b32 + 128*m.b24*m.b26*m.b31*m.b33 + 64*
                       m.b24*m.b26*m.b32*m.b34 + 256*m.b24*m.b27*m.b28*m.b31 + 192*m.b24*m.b27*m.b29*m.b32 + 128*m.b24*
                       m.b27*m.b30*m.b33 + 64*m.b24*m.b27*m.b31*m.b34 + 128*m.b24*m.b28*m.b29*m.b33 + 64*m.b24*m.b28*
                       m.b30*m.b34 + 512*m.b25*m.b26*m.b27*m.b28 + 448*m.b25*m.b26*m.b28*m.b29 + 384*m.b25*m.b26*m.b29*
                       m.b30 + 320*m.b25*m.b26*m.b30*m.b31 + 256*m.b25*m.b26*m.b31*m.b32 + 192*m.b25*m.b26*m.b32*m.b33
                        + 128*m.b25*m.b26*m.b33*m.b34 + 64*m.b25*m.b26*m.b34*m.b35 + 384*m.b25*m.b27*m.b28*m.b30 + 320*
                       m.b25*m.b27*m.b29*m.b31 + 256*m.b25*m.b27*m.b30*m.b32 + 192*m.b25*m.b27*m.b31*m.b33 + 128*m.b25*
                       m.b27*m.b32*m.b34 + 64*m.b25*m.b27*m.b33*m.b35 + 256*m.b25*m.b28*m.b29*m.b32 + 192*m.b25*m.b28*
                       m.b30*m.b33 + 128*m.b25*m.b28*m.b31*m.b34 + 64*m.b25*m.b28*m.b32*m.b35 + 128*m.b25*m.b29*m.b30*
                       m.b34 + 64*m.b25*m.b29*m.b31*m.b35 + 512*m.b26*m.b27*m.b28*m.b29 + 448*m.b26*m.b27*m.b29*m.b30 + 
                       384*m.b26*m.b27*m.b30*m.b31 + 320*m.b26*m.b27*m.b31*m.b32 + 256*m.b26*m.b27*m.b32*m.b33 + 192*
                       m.b26*m.b27*m.b33*m.b34 + 128*m.b26*m.b27*m.b34*m.b35 + 64*m.b26*m.b27*m.b35*m.b36 + 384*m.b26*
                       m.b28*m.b29*m.b31 + 320*m.b26*m.b28*m.b30*m.b32 + 256*m.b26*m.b28*m.b31*m.b33 + 192*m.b26*m.b28*
                       m.b32*m.b34 + 128*m.b26*m.b28*m.b33*m.b35 + 64*m.b26*m.b28*m.b34*m.b36 + 256*m.b26*m.b29*m.b30*
                       m.b33 + 192*m.b26*m.b29*m.b31*m.b34 + 128*m.b26*m.b29*m.b32*m.b35 + 64*m.b26*m.b29*m.b33*m.b36 + 
                       128*m.b26*m.b30*m.b31*m.b35 + 64*m.b26*m.b30*m.b32*m.b36 + 512*m.b27*m.b28*m.b29*m.b30 + 448*
                       m.b27*m.b28*m.b30*m.b31 + 384*m.b27*m.b28*m.b31*m.b32 + 320*m.b27*m.b28*m.b32*m.b33 + 256*m.b27*
                       m.b28*m.b33*m.b34 + 192*m.b27*m.b28*m.b34*m.b35 + 128*m.b27*m.b28*m.b35*m.b36 + 64*m.b27*m.b28*
                       m.b36*m.b37 + 384*m.b27*m.b29*m.b30*m.b32 + 320*m.b27*m.b29*m.b31*m.b33 + 256*m.b27*m.b29*m.b32*
                       m.b34 + 192*m.b27*m.b29*m.b33*m.b35 + 128*m.b27*m.b29*m.b34*m.b36 + 64*m.b27*m.b29*m.b35*m.b37 + 
                       256*m.b27*m.b30*m.b31*m.b34 + 192*m.b27*m.b30*m.b32*m.b35 + 128*m.b27*m.b30*m.b33*m.b36 + 64*
                       m.b27*m.b30*m.b34*m.b37 + 128*m.b27*m.b31*m.b32*m.b36 + 64*m.b27*m.b31*m.b33*m.b37 + 512*m.b28*
                       m.b29*m.b30*m.b31 + 448*m.b28*m.b29*m.b31*m.b32 + 384*m.b28*m.b29*m.b32*m.b33 + 320*m.b28*m.b29*
                       m.b33*m.b34 + 256*m.b28*m.b29*m.b34*m.b35 + 192*m.b28*m.b29*m.b35*m.b36 + 128*m.b28*m.b29*m.b36*
                       m.b37 + 64*m.b28*m.b29*m.b37*m.b38 + 384*m.b28*m.b30*m.b31*m.b33 + 320*m.b28*m.b30*m.b32*m.b34 + 
                       256*m.b28*m.b30*m.b33*m.b35 + 192*m.b28*m.b30*m.b34*m.b36 + 128*m.b28*m.b30*m.b35*m.b37 + 64*
                       m.b28*m.b30*m.b36*m.b38 + 256*m.b28*m.b31*m.b32*m.b35 + 192*m.b28*m.b31*m.b33*m.b36 + 128*m.b28*
                       m.b31*m.b34*m.b37 + 64*m.b28*m.b31*m.b35*m.b38 + 128*m.b28*m.b32*m.b33*m.b37 + 64*m.b28*m.b32*
                       m.b34*m.b38 + 512*m.b29*m.b30*m.b31*m.b32 + 448*m.b29*m.b30*m.b32*m.b33 + 384*m.b29*m.b30*m.b33*
                       m.b34 + 320*m.b29*m.b30*m.b34*m.b35 + 256*m.b29*m.b30*m.b35*m.b36 + 192*m.b29*m.b30*m.b36*m.b37
                        + 128*m.b29*m.b30*m.b37*m.b38 + 64*m.b29*m.b30*m.b38*m.b39 + 384*m.b29*m.b31*m.b32*m.b34 + 320*
                       m.b29*m.b31*m.b33*m.b35 + 256*m.b29*m.b31*m.b34*m.b36 + 192*m.b29*m.b31*m.b35*m.b37 + 128*m.b29*
                       m.b31*m.b36*m.b38 + 64*m.b29*m.b31*m.b37*m.b39 + 256*m.b29*m.b32*m.b33*m.b36 + 192*m.b29*m.b32*
                       m.b34*m.b37 + 128*m.b29*m.b32*m.b35*m.b38 + 64*m.b29*m.b32*m.b36*m.b39 + 128*m.b29*m.b33*m.b34*
                       m.b38 + 64*m.b29*m.b33*m.b35*m.b39 + 512*m.b30*m.b31*m.b32*m.b33 + 448*m.b30*m.b31*m.b33*m.b34 + 
                       384*m.b30*m.b31*m.b34*m.b35 + 320*m.b30*m.b31*m.b35*m.b36 + 256*m.b30*m.b31*m.b36*m.b37 + 192*
                       m.b30*m.b31*m.b37*m.b38 + 128*m.b30*m.b31*m.b38*m.b39 + 64*m.b30*m.b31*m.b39*m.b40 + 384*m.b30*
                       m.b32*m.b33*m.b35 + 320*m.b30*m.b32*m.b34*m.b36 + 256*m.b30*m.b32*m.b35*m.b37 + 192*m.b30*m.b32*
                       m.b36*m.b38 + 128*m.b30*m.b32*m.b37*m.b39 + 64*m.b30*m.b32*m.b38*m.b40 + 256*m.b30*m.b33*m.b34*
                       m.b37 + 192*m.b30*m.b33*m.b35*m.b38 + 128*m.b30*m.b33*m.b36*m.b39 + 64*m.b30*m.b33*m.b37*m.b40 + 
                       128*m.b30*m.b34*m.b35*m.b39 + 64*m.b30*m.b34*m.b36*m.b40 + 512*m.b31*m.b32*m.b33*m.b34 + 448*
                       m.b31*m.b32*m.b34*m.b35 + 384*m.b31*m.b32*m.b35*m.b36 + 320*m.b31*m.b32*m.b36*m.b37 + 256*m.b31*
                       m.b32*m.b37*m.b38 + 192*m.b31*m.b32*m.b38*m.b39 + 128*m.b31*m.b32*m.b39*m.b40 + 64*m.b31*m.b32*
                       m.b40*m.b41 + 384*m.b31*m.b33*m.b34*m.b36 + 320*m.b31*m.b33*m.b35*m.b37 + 256*m.b31*m.b33*m.b36*
                       m.b38 + 192*m.b31*m.b33*m.b37*m.b39 + 128*m.b31*m.b33*m.b38*m.b40 + 64*m.b31*m.b33*m.b39*m.b41 + 
                       256*m.b31*m.b34*m.b35*m.b38 + 192*m.b31*m.b34*m.b36*m.b39 + 128*m.b31*m.b34*m.b37*m.b40 + 64*
                       m.b31*m.b34*m.b38*m.b41 + 128*m.b31*m.b35*m.b36*m.b40 + 64*m.b31*m.b35*m.b37*m.b41 + 512*m.b32*
                       m.b33*m.b34*m.b35 + 448*m.b32*m.b33*m.b35*m.b36 + 384*m.b32*m.b33*m.b36*m.b37 + 320*m.b32*m.b33*
                       m.b37*m.b38 + 256*m.b32*m.b33*m.b38*m.b39 + 192*m.b32*m.b33*m.b39*m.b40 + 128*m.b32*m.b33*m.b40*
                       m.b41 + 64*m.b32*m.b33*m.b41*m.b42 + 384*m.b32*m.b34*m.b35*m.b37 + 320*m.b32*m.b34*m.b36*m.b38 + 
                       256*m.b32*m.b34*m.b37*m.b39 + 192*m.b32*m.b34*m.b38*m.b40 + 128*m.b32*m.b34*m.b39*m.b41 + 64*
                       m.b32*m.b34*m.b40*m.b42 + 256*m.b32*m.b35*m.b36*m.b39 + 192*m.b32*m.b35*m.b37*m.b40 + 128*m.b32*
                       m.b35*m.b38*m.b41 + 64*m.b32*m.b35*m.b39*m.b42 + 128*m.b32*m.b36*m.b37*m.b41 + 64*m.b32*m.b36*
                       m.b38*m.b42 + 512*m.b33*m.b34*m.b35*m.b36 + 448*m.b33*m.b34*m.b36*m.b37 + 384*m.b33*m.b34*m.b37*
                       m.b38 + 320*m.b33*m.b34*m.b38*m.b39 + 256*m.b33*m.b34*m.b39*m.b40 + 192*m.b33*m.b34*m.b40*m.b41
                        + 128*m.b33*m.b34*m.b41*m.b42 + 64*m.b33*m.b34*m.b42*m.b43 + 384*m.b33*m.b35*m.b36*m.b38 + 320*
                       m.b33*m.b35*m.b37*m.b39 + 256*m.b33*m.b35*m.b38*m.b40 + 192*m.b33*m.b35*m.b39*m.b41 + 128*m.b33*
                       m.b35*m.b40*m.b42 + 64*m.b33*m.b35*m.b41*m.b43 + 256*m.b33*m.b36*m.b37*m.b40 + 192*m.b33*m.b36*
                       m.b38*m.b41 + 128*m.b33*m.b36*m.b39*m.b42 + 64*m.b33*m.b36*m.b40*m.b43 + 128*m.b33*m.b37*m.b38*
                       m.b42 + 64*m.b33*m.b37*m.b39*m.b43 + 512*m.b34*m.b35*m.b36*m.b37 + 448*m.b34*m.b35*m.b37*m.b38 + 
                       384*m.b34*m.b35*m.b38*m.b39 + 320*m.b34*m.b35*m.b39*m.b40 + 256*m.b34*m.b35*m.b40*m.b41 + 192*
                       m.b34*m.b35*m.b41*m.b42 + 128*m.b34*m.b35*m.b42*m.b43 + 64*m.b34*m.b35*m.b43*m.b44 + 384*m.b34*
                       m.b36*m.b37*m.b39 + 320*m.b34*m.b36*m.b38*m.b40 + 256*m.b34*m.b36*m.b39*m.b41 + 192*m.b34*m.b36*
                       m.b40*m.b42 + 128*m.b34*m.b36*m.b41*m.b43 + 64*m.b34*m.b36*m.b42*m.b44 + 256*m.b34*m.b37*m.b38*
                       m.b41 + 192*m.b34*m.b37*m.b39*m.b42 + 128*m.b34*m.b37*m.b40*m.b43 + 64*m.b34*m.b37*m.b41*m.b44 + 
                       128*m.b34*m.b38*m.b39*m.b43 + 64*m.b34*m.b38*m.b40*m.b44 + 512*m.b35*m.b36*m.b37*m.b38 + 448*
                       m.b35*m.b36*m.b38*m.b39 + 384*m.b35*m.b36*m.b39*m.b40 + 320*m.b35*m.b36*m.b40*m.b41 + 256*m.b35*
                       m.b36*m.b41*m.b42 + 192*m.b35*m.b36*m.b42*m.b43 + 128*m.b35*m.b36*m.b43*m.b44 + 64*m.b35*m.b36*
                       m.b44*m.b45 + 384*m.b35*m.b37*m.b38*m.b40 + 320*m.b35*m.b37*m.b39*m.b41 + 256*m.b35*m.b37*m.b40*
                       m.b42 + 192*m.b35*m.b37*m.b41*m.b43 + 128*m.b35*m.b37*m.b42*m.b44 + 64*m.b35*m.b37*m.b43*m.b45 + 
                       256*m.b35*m.b38*m.b39*m.b42 + 192*m.b35*m.b38*m.b40*m.b43 + 128*m.b35*m.b38*m.b41*m.b44 + 64*
                       m.b35*m.b38*m.b42*m.b45 + 128*m.b35*m.b39*m.b40*m.b44 + 64*m.b35*m.b39*m.b41*m.b45 + 448*m.b36*
                       m.b37*m.b38*m.b39 + 384*m.b36*m.b37*m.b39*m.b40 + 320*m.b36*m.b37*m.b40*m.b41 + 256*m.b36*m.b37*
                       m.b41*m.b42 + 192*m.b36*m.b37*m.b42*m.b43 + 128*m.b36*m.b37*m.b43*m.b44 + 64*m.b36*m.b37*m.b44*
                       m.b45 + 320*m.b36*m.b38*m.b39*m.b41 + 256*m.b36*m.b38*m.b40*m.b42 + 192*m.b36*m.b38*m.b41*m.b43
                        + 128*m.b36*m.b38*m.b42*m.b44 + 64*m.b36*m.b38*m.b43*m.b45 + 192*m.b36*m.b39*m.b40*m.b43 + 128*
                       m.b36*m.b39*m.b41*m.b44 + 64*m.b36*m.b39*m.b42*m.b45 + 64*m.b36*m.b40*m.b41*m.b45 + 384*m.b37*
                       m.b38*m.b39*m.b40 + 320*m.b37*m.b38*m.b40*m.b41 + 256*m.b37*m.b38*m.b41*m.b42 + 192*m.b37*m.b38*
                       m.b42*m.b43 + 128*m.b37*m.b38*m.b43*m.b44 + 64*m.b37*m.b38*m.b44*m.b45 + 256*m.b37*m.b39*m.b40*
                       m.b42 + 192*m.b37*m.b39*m.b41*m.b43 + 128*m.b37*m.b39*m.b42*m.b44 + 64*m.b37*m.b39*m.b43*m.b45 + 
                       128*m.b37*m.b40*m.b41*m.b44 + 64*m.b37*m.b40*m.b42*m.b45 + 320*m.b38*m.b39*m.b40*m.b41 + 256*
                       m.b38*m.b39*m.b41*m.b42 + 192*m.b38*m.b39*m.b42*m.b43 + 128*m.b38*m.b39*m.b43*m.b44 + 64*m.b38*
                       m.b39*m.b44*m.b45 + 192*m.b38*m.b40*m.b41*m.b43 + 128*m.b38*m.b40*m.b42*m.b44 + 64*m.b38*m.b40*
                       m.b43*m.b45 + 64*m.b38*m.b41*m.b42*m.b45 + 256*m.b39*m.b40*m.b41*m.b42 + 192*m.b39*m.b40*m.b42*
                       m.b43 + 128*m.b39*m.b40*m.b43*m.b44 + 64*m.b39*m.b40*m.b44*m.b45 + 128*m.b39*m.b41*m.b42*m.b44 + 
                       64*m.b39*m.b41*m.b43*m.b45 + 192*m.b40*m.b41*m.b42*m.b43 + 128*m.b40*m.b41*m.b43*m.b44 + 64*m.b40
                       *m.b41*m.b44*m.b45 + 64*m.b40*m.b42*m.b43*m.b45 + 128*m.b41*m.b42*m.b43*m.b44 + 64*m.b41*m.b42*
                       m.b44*m.b45 + 64*m.b42*m.b43*m.b44*m.b45 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*
                       m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*
                       m.b2*m.b10 - 32*m.b1*m.b2*m.b11 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*
                       m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 32*m.b1*m.b3*m.b10 - 32*m.b1*m.b3*m.b11
                        - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 32*m.b1*m.b4*
                       m.b9 - 32*m.b1*m.b4*m.b10 - 32*m.b1*m.b4*m.b11 - 64*m.b1*m.b5*m.b6 - 64*m.b1*m.b5*m.b7 - 32*m.b1*
                       m.b5*m.b8 - 32*m.b1*m.b5*m.b10 - 32*m.b1*m.b5*m.b11 - 32*m.b1*m.b6*m.b7 - 32*m.b1*m.b6*m.b8 - 32*
                       m.b1*m.b6*m.b9 - 32*m.b1*m.b6*m.b10 - 32*m.b1*m.b7*m.b8 - 32*m.b1*m.b7*m.b9 - 32*m.b1*m.b7*m.b10
                        - 32*m.b1*m.b7*m.b11 - 32*m.b1*m.b8*m.b9 - 32*m.b1*m.b8*m.b10 - 32*m.b1*m.b8*m.b11 - 32*m.b1*
                       m.b9*m.b10 - 32*m.b1*m.b9*m.b11 - 32*m.b1*m.b10*m.b11 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 
                       128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3
                       *m.b10 - 96*m.b2*m.b3*m.b11 - 32*m.b2*m.b3*m.b12 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*
                       m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 128*m.b2*m.b4*m.b9 - 96*m.b2*m.b4*m.b10 - 64*m.b2*m.b4*
                       m.b11 - 32*m.b2*m.b4*m.b12 - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b8 - 96*
                       m.b2*m.b5*m.b9 - 64*m.b2*m.b5*m.b10 - 64*m.b2*m.b5*m.b11 - 32*m.b2*m.b5*m.b12 - 160*m.b2*m.b6*
                       m.b7 - 96*m.b2*m.b6*m.b8 - 64*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b11 - 32*m.b2*m.b6*m.b12 - 96*m.b2*
                       m.b7*m.b8 - 64*m.b2*m.b7*m.b9 - 64*m.b2*m.b7*m.b10 - 64*m.b2*m.b7*m.b11 - 96*m.b2*m.b8*m.b9 - 64*
                       m.b2*m.b8*m.b10 - 64*m.b2*m.b8*m.b11 - 32*m.b2*m.b8*m.b12 - 96*m.b2*m.b9*m.b10 - 64*m.b2*m.b9*
                       m.b11 - 32*m.b2*m.b9*m.b12 - 96*m.b2*m.b10*m.b11 - 32*m.b2*m.b10*m.b12 - 32*m.b2*m.b11*m.b12 - 
                       160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4
                       *m.b9 - 192*m.b3*m.b4*m.b10 - 160*m.b3*m.b4*m.b11 - 96*m.b3*m.b4*m.b12 - 32*m.b3*m.b4*m.b13 - 256
                       *m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 160*m.b3*m.b5*
                       m.b10 - 128*m.b3*m.b5*m.b11 - 64*m.b3*m.b5*m.b12 - 32*m.b3*m.b5*m.b13 - 256*m.b3*m.b6*m.b7 - 224*
                       m.b3*m.b6*m.b8 - 64*m.b3*m.b6*m.b9 - 128*m.b3*m.b6*m.b10 - 96*m.b3*m.b6*m.b11 - 64*m.b3*m.b6*
                       m.b12 - 32*m.b3*m.b6*m.b13 - 224*m.b3*m.b7*m.b8 - 160*m.b3*m.b7*m.b9 - 96*m.b3*m.b7*m.b10 - 64*
                       m.b3*m.b7*m.b12 - 32*m.b3*m.b7*m.b13 - 160*m.b3*m.b8*m.b9 - 128*m.b3*m.b8*m.b10 - 96*m.b3*m.b8*
                       m.b11 - 64*m.b3*m.b8*m.b12 - 160*m.b3*m.b9*m.b10 - 128*m.b3*m.b9*m.b11 - 64*m.b3*m.b9*m.b12 - 32*
                       m.b3*m.b9*m.b13 - 160*m.b3*m.b10*m.b11 - 64*m.b3*m.b10*m.b12 - 32*m.b3*m.b10*m.b13 - 96*m.b3*
                       m.b11*m.b12 - 32*m.b3*m.b11*m.b13 - 32*m.b3*m.b12*m.b13 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7
                        - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 224*m.b4*m.b5*m.b11 - 160*m.b4
                       *m.b5*m.b12 - 96*m.b4*m.b5*m.b13 - 32*m.b4*m.b5*m.b14 - 352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8
                        - 288*m.b4*m.b6*m.b9 - 224*m.b4*m.b6*m.b10 - 192*m.b4*m.b6*m.b11 - 128*m.b4*m.b6*m.b12 - 64*m.b4
                       *m.b6*m.b13 - 32*m.b4*m.b6*m.b14 - 352*m.b4*m.b7*m.b8 - 288*m.b4*m.b7*m.b9 - 96*m.b4*m.b7*m.b10
                        - 160*m.b4*m.b7*m.b11 - 96*m.b4*m.b7*m.b12 - 64*m.b4*m.b7*m.b13 - 32*m.b4*m.b7*m.b14 - 288*m.b4*
                       m.b8*m.b9 - 224*m.b4*m.b8*m.b10 - 160*m.b4*m.b8*m.b11 - 64*m.b4*m.b8*m.b13 - 32*m.b4*m.b8*m.b14
                        - 224*m.b4*m.b9*m.b10 - 192*m.b4*m.b9*m.b11 - 96*m.b4*m.b9*m.b12 - 64*m.b4*m.b9*m.b13 - 224*m.b4
                       *m.b10*m.b11 - 128*m.b4*m.b10*m.b12 - 64*m.b4*m.b10*m.b13 - 32*m.b4*m.b10*m.b14 - 160*m.b4*m.b11*
                       m.b12 - 64*m.b4*m.b11*m.b13 - 32*m.b4*m.b11*m.b14 - 96*m.b4*m.b12*m.b13 - 32*m.b4*m.b12*m.b14 - 
                       32*m.b4*m.b13*m.b14 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*
                       m.b6*m.b10 - 288*m.b5*m.b6*m.b11 - 224*m.b5*m.b6*m.b12 - 160*m.b5*m.b6*m.b13 - 96*m.b5*m.b6*m.b14
                        - 32*m.b5*m.b6*m.b15 - 448*m.b5*m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 352*m.b5*m.b7*m.b10 - 288*m.b5*
                       m.b7*m.b11 - 192*m.b5*m.b7*m.b12 - 128*m.b5*m.b7*m.b13 - 64*m.b5*m.b7*m.b14 - 32*m.b5*m.b7*m.b15
                        - 416*m.b5*m.b8*m.b9 - 352*m.b5*m.b8*m.b10 - 128*m.b5*m.b8*m.b11 - 160*m.b5*m.b8*m.b12 - 96*m.b5
                       *m.b8*m.b13 - 64*m.b5*m.b8*m.b14 - 32*m.b5*m.b8*m.b15 - 352*m.b5*m.b9*m.b10 - 288*m.b5*m.b9*m.b11
                        - 160*m.b5*m.b9*m.b12 - 64*m.b5*m.b9*m.b14 - 32*m.b5*m.b9*m.b15 - 288*m.b5*m.b10*m.b11 - 192*
                       m.b5*m.b10*m.b12 - 96*m.b5*m.b10*m.b13 - 64*m.b5*m.b10*m.b14 - 224*m.b5*m.b11*m.b12 - 128*m.b5*
                       m.b11*m.b13 - 64*m.b5*m.b11*m.b14 - 32*m.b5*m.b11*m.b15 - 160*m.b5*m.b12*m.b13 - 64*m.b5*m.b12*
                       m.b14 - 32*m.b5*m.b12*m.b15 - 96*m.b5*m.b13*m.b14 - 32*m.b5*m.b13*m.b15 - 32*m.b5*m.b14*m.b15 - 
                       352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 416*m.b6*m.b7*m.b11 - 288*m.b6*
                       m.b7*m.b12 - 224*m.b6*m.b7*m.b13 - 160*m.b6*m.b7*m.b14 - 96*m.b6*m.b7*m.b15 - 32*m.b6*m.b7*m.b16
                        - 544*m.b6*m.b8*m.b9 - 288*m.b6*m.b8*m.b10 - 416*m.b6*m.b8*m.b11 - 288*m.b6*m.b8*m.b12 - 192*
                       m.b6*m.b8*m.b13 - 128*m.b6*m.b8*m.b14 - 64*m.b6*m.b8*m.b15 - 32*m.b6*m.b8*m.b16 - 480*m.b6*m.b9*
                       m.b10 - 416*m.b6*m.b9*m.b11 - 128*m.b6*m.b9*m.b12 - 160*m.b6*m.b9*m.b13 - 96*m.b6*m.b9*m.b14 - 64
                       *m.b6*m.b9*m.b15 - 32*m.b6*m.b9*m.b16 - 416*m.b6*m.b10*m.b11 - 288*m.b6*m.b10*m.b12 - 160*m.b6*
                       m.b10*m.b13 - 64*m.b6*m.b10*m.b15 - 32*m.b6*m.b10*m.b16 - 288*m.b6*m.b11*m.b12 - 192*m.b6*m.b11*
                       m.b13 - 96*m.b6*m.b11*m.b14 - 64*m.b6*m.b11*m.b15 - 224*m.b6*m.b12*m.b13 - 128*m.b6*m.b12*m.b14
                        - 64*m.b6*m.b12*m.b15 - 32*m.b6*m.b12*m.b16 - 160*m.b6*m.b13*m.b14 - 64*m.b6*m.b13*m.b15 - 32*
                       m.b6*m.b13*m.b16 - 96*m.b6*m.b14*m.b15 - 32*m.b6*m.b14*m.b16 - 32*m.b6*m.b15*m.b16 - 416*m.b7*
                       m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 544*m.b7*m.b8*m.b11 - 416*m.b7*m.b8*m.b12 - 288*m.b7*m.b8*m.b13
                        - 224*m.b7*m.b8*m.b14 - 160*m.b7*m.b8*m.b15 - 96*m.b7*m.b8*m.b16 - 32*m.b7*m.b8*m.b17 - 608*m.b7
                       *m.b9*m.b10 - 320*m.b7*m.b9*m.b11 - 416*m.b7*m.b9*m.b12 - 288*m.b7*m.b9*m.b13 - 192*m.b7*m.b9*
                       m.b14 - 128*m.b7*m.b9*m.b15 - 64*m.b7*m.b9*m.b16 - 32*m.b7*m.b9*m.b17 - 544*m.b7*m.b10*m.b11 - 
                       416*m.b7*m.b10*m.b12 - 128*m.b7*m.b10*m.b13 - 160*m.b7*m.b10*m.b14 - 96*m.b7*m.b10*m.b15 - 64*
                       m.b7*m.b10*m.b16 - 32*m.b7*m.b10*m.b17 - 416*m.b7*m.b11*m.b12 - 288*m.b7*m.b11*m.b13 - 160*m.b7*
                       m.b11*m.b14 - 64*m.b7*m.b11*m.b16 - 32*m.b7*m.b11*m.b17 - 288*m.b7*m.b12*m.b13 - 192*m.b7*m.b12*
                       m.b14 - 96*m.b7*m.b12*m.b15 - 64*m.b7*m.b12*m.b16 - 224*m.b7*m.b13*m.b14 - 128*m.b7*m.b13*m.b15
                        - 64*m.b7*m.b13*m.b16 - 32*m.b7*m.b13*m.b17 - 160*m.b7*m.b14*m.b15 - 64*m.b7*m.b14*m.b16 - 32*
                       m.b7*m.b14*m.b17 - 96*m.b7*m.b15*m.b16 - 32*m.b7*m.b15*m.b17 - 32*m.b7*m.b16*m.b17 - 480*m.b8*
                       m.b9*m.b10 - 672*m.b8*m.b9*m.b11 - 544*m.b8*m.b9*m.b12 - 416*m.b8*m.b9*m.b13 - 288*m.b8*m.b9*
                       m.b14 - 224*m.b8*m.b9*m.b15 - 160*m.b8*m.b9*m.b16 - 96*m.b8*m.b9*m.b17 - 32*m.b8*m.b9*m.b18 - 672
                       *m.b8*m.b10*m.b11 - 320*m.b8*m.b10*m.b12 - 416*m.b8*m.b10*m.b13 - 288*m.b8*m.b10*m.b14 - 192*m.b8
                       *m.b10*m.b15 - 128*m.b8*m.b10*m.b16 - 64*m.b8*m.b10*m.b17 - 32*m.b8*m.b10*m.b18 - 544*m.b8*m.b11*
                       m.b12 - 416*m.b8*m.b11*m.b13 - 128*m.b8*m.b11*m.b14 - 160*m.b8*m.b11*m.b15 - 96*m.b8*m.b11*m.b16
                        - 64*m.b8*m.b11*m.b17 - 32*m.b8*m.b11*m.b18 - 416*m.b8*m.b12*m.b13 - 288*m.b8*m.b12*m.b14 - 160*
                       m.b8*m.b12*m.b15 - 64*m.b8*m.b12*m.b17 - 32*m.b8*m.b12*m.b18 - 288*m.b8*m.b13*m.b14 - 192*m.b8*
                       m.b13*m.b15 - 96*m.b8*m.b13*m.b16 - 64*m.b8*m.b13*m.b17 - 224*m.b8*m.b14*m.b15 - 128*m.b8*m.b14*
                       m.b16 - 64*m.b8*m.b14*m.b17 - 32*m.b8*m.b14*m.b18 - 160*m.b8*m.b15*m.b16 - 64*m.b8*m.b15*m.b17 - 
                       32*m.b8*m.b15*m.b18 - 96*m.b8*m.b16*m.b17 - 32*m.b8*m.b16*m.b18 - 32*m.b8*m.b17*m.b18 - 512*m.b9*
                       m.b10*m.b11 - 672*m.b9*m.b10*m.b12 - 544*m.b9*m.b10*m.b13 - 416*m.b9*m.b10*m.b14 - 288*m.b9*m.b10
                       *m.b15 - 224*m.b9*m.b10*m.b16 - 160*m.b9*m.b10*m.b17 - 96*m.b9*m.b10*m.b18 - 32*m.b9*m.b10*m.b19
                        - 672*m.b9*m.b11*m.b12 - 320*m.b9*m.b11*m.b13 - 416*m.b9*m.b11*m.b14 - 288*m.b9*m.b11*m.b15 - 
                       192*m.b9*m.b11*m.b16 - 128*m.b9*m.b11*m.b17 - 64*m.b9*m.b11*m.b18 - 32*m.b9*m.b11*m.b19 - 544*
                       m.b9*m.b12*m.b13 - 416*m.b9*m.b12*m.b14 - 128*m.b9*m.b12*m.b15 - 160*m.b9*m.b12*m.b16 - 96*m.b9*
                       m.b12*m.b17 - 64*m.b9*m.b12*m.b18 - 32*m.b9*m.b12*m.b19 - 416*m.b9*m.b13*m.b14 - 288*m.b9*m.b13*
                       m.b15 - 160*m.b9*m.b13*m.b16 - 64*m.b9*m.b13*m.b18 - 32*m.b9*m.b13*m.b19 - 288*m.b9*m.b14*m.b15
                        - 192*m.b9*m.b14*m.b16 - 96*m.b9*m.b14*m.b17 - 64*m.b9*m.b14*m.b18 - 224*m.b9*m.b15*m.b16 - 128*
                       m.b9*m.b15*m.b17 - 64*m.b9*m.b15*m.b18 - 32*m.b9*m.b15*m.b19 - 160*m.b9*m.b16*m.b17 - 64*m.b9*
                       m.b16*m.b18 - 32*m.b9*m.b16*m.b19 - 96*m.b9*m.b17*m.b18 - 32*m.b9*m.b17*m.b19 - 32*m.b9*m.b18*
                       m.b19 - 512*m.b10*m.b11*m.b12 - 672*m.b10*m.b11*m.b13 - 544*m.b10*m.b11*m.b14 - 416*m.b10*m.b11*
                       m.b15 - 288*m.b10*m.b11*m.b16 - 224*m.b10*m.b11*m.b17 - 160*m.b10*m.b11*m.b18 - 96*m.b10*m.b11*
                       m.b19 - 32*m.b10*m.b11*m.b20 - 672*m.b10*m.b12*m.b13 - 320*m.b10*m.b12*m.b14 - 416*m.b10*m.b12*
                       m.b15 - 288*m.b10*m.b12*m.b16 - 192*m.b10*m.b12*m.b17 - 128*m.b10*m.b12*m.b18 - 64*m.b10*m.b12*
                       m.b19 - 32*m.b10*m.b12*m.b20 - 544*m.b10*m.b13*m.b14 - 416*m.b10*m.b13*m.b15 - 128*m.b10*m.b13*
                       m.b16 - 160*m.b10*m.b13*m.b17 - 96*m.b10*m.b13*m.b18 - 64*m.b10*m.b13*m.b19 - 32*m.b10*m.b13*
                       m.b20 - 416*m.b10*m.b14*m.b15 - 288*m.b10*m.b14*m.b16 - 160*m.b10*m.b14*m.b17 - 64*m.b10*m.b14*
                       m.b19 - 32*m.b10*m.b14*m.b20 - 288*m.b10*m.b15*m.b16 - 192*m.b10*m.b15*m.b17 - 96*m.b10*m.b15*
                       m.b18 - 64*m.b10*m.b15*m.b19 - 224*m.b10*m.b16*m.b17 - 128*m.b10*m.b16*m.b18 - 64*m.b10*m.b16*
                       m.b19 - 32*m.b10*m.b16*m.b20 - 160*m.b10*m.b17*m.b18 - 64*m.b10*m.b17*m.b19 - 32*m.b10*m.b17*
                       m.b20 - 96*m.b10*m.b18*m.b19 - 32*m.b10*m.b18*m.b20 - 32*m.b10*m.b19*m.b20 - 512*m.b11*m.b12*
                       m.b13 - 672*m.b11*m.b12*m.b14 - 544*m.b11*m.b12*m.b15 - 416*m.b11*m.b12*m.b16 - 288*m.b11*m.b12*
                       m.b17 - 224*m.b11*m.b12*m.b18 - 160*m.b11*m.b12*m.b19 - 96*m.b11*m.b12*m.b20 - 32*m.b11*m.b12*
                       m.b21 - 672*m.b11*m.b13*m.b14 - 320*m.b11*m.b13*m.b15 - 416*m.b11*m.b13*m.b16 - 288*m.b11*m.b13*
                       m.b17 - 192*m.b11*m.b13*m.b18 - 128*m.b11*m.b13*m.b19 - 64*m.b11*m.b13*m.b20 - 32*m.b11*m.b13*
                       m.b21 - 544*m.b11*m.b14*m.b15 - 416*m.b11*m.b14*m.b16 - 128*m.b11*m.b14*m.b17 - 160*m.b11*m.b14*
                       m.b18 - 96*m.b11*m.b14*m.b19 - 64*m.b11*m.b14*m.b20 - 32*m.b11*m.b14*m.b21 - 416*m.b11*m.b15*
                       m.b16 - 288*m.b11*m.b15*m.b17 - 160*m.b11*m.b15*m.b18 - 64*m.b11*m.b15*m.b20 - 32*m.b11*m.b15*
                       m.b21 - 288*m.b11*m.b16*m.b17 - 192*m.b11*m.b16*m.b18 - 96*m.b11*m.b16*m.b19 - 64*m.b11*m.b16*
                       m.b20 - 224*m.b11*m.b17*m.b18 - 128*m.b11*m.b17*m.b19 - 64*m.b11*m.b17*m.b20 - 32*m.b11*m.b17*
                       m.b21 - 160*m.b11*m.b18*m.b19 - 64*m.b11*m.b18*m.b20 - 32*m.b11*m.b18*m.b21 - 96*m.b11*m.b19*
                       m.b20 - 32*m.b11*m.b19*m.b21 - 32*m.b11*m.b20*m.b21 - 512*m.b12*m.b13*m.b14 - 672*m.b12*m.b13*
                       m.b15 - 544*m.b12*m.b13*m.b16 - 416*m.b12*m.b13*m.b17 - 288*m.b12*m.b13*m.b18 - 224*m.b12*m.b13*
                       m.b19 - 160*m.b12*m.b13*m.b20 - 96*m.b12*m.b13*m.b21 - 32*m.b12*m.b13*m.b22 - 672*m.b12*m.b14*
                       m.b15 - 320*m.b12*m.b14*m.b16 - 416*m.b12*m.b14*m.b17 - 288*m.b12*m.b14*m.b18 - 192*m.b12*m.b14*
                       m.b19 - 128*m.b12*m.b14*m.b20 - 64*m.b12*m.b14*m.b21 - 32*m.b12*m.b14*m.b22 - 544*m.b12*m.b15*
                       m.b16 - 416*m.b12*m.b15*m.b17 - 128*m.b12*m.b15*m.b18 - 160*m.b12*m.b15*m.b19 - 96*m.b12*m.b15*
                       m.b20 - 64*m.b12*m.b15*m.b21 - 32*m.b12*m.b15*m.b22 - 416*m.b12*m.b16*m.b17 - 288*m.b12*m.b16*
                       m.b18 - 160*m.b12*m.b16*m.b19 - 64*m.b12*m.b16*m.b21 - 32*m.b12*m.b16*m.b22 - 288*m.b12*m.b17*
                       m.b18 - 192*m.b12*m.b17*m.b19 - 96*m.b12*m.b17*m.b20 - 64*m.b12*m.b17*m.b21 - 224*m.b12*m.b18*
                       m.b19 - 128*m.b12*m.b18*m.b20 - 64*m.b12*m.b18*m.b21 - 32*m.b12*m.b18*m.b22 - 160*m.b12*m.b19*
                       m.b20 - 64*m.b12*m.b19*m.b21 - 32*m.b12*m.b19*m.b22 - 96*m.b12*m.b20*m.b21 - 32*m.b12*m.b20*m.b22
                        - 32*m.b12*m.b21*m.b22 - 512*m.b13*m.b14*m.b15 - 672*m.b13*m.b14*m.b16 - 544*m.b13*m.b14*m.b17
                        - 416*m.b13*m.b14*m.b18 - 288*m.b13*m.b14*m.b19 - 224*m.b13*m.b14*m.b20 - 160*m.b13*m.b14*m.b21
                        - 96*m.b13*m.b14*m.b22 - 32*m.b13*m.b14*m.b23 - 672*m.b13*m.b15*m.b16 - 320*m.b13*m.b15*m.b17 - 
                       416*m.b13*m.b15*m.b18 - 288*m.b13*m.b15*m.b19 - 192*m.b13*m.b15*m.b20 - 128*m.b13*m.b15*m.b21 - 
                       64*m.b13*m.b15*m.b22 - 32*m.b13*m.b15*m.b23 - 544*m.b13*m.b16*m.b17 - 416*m.b13*m.b16*m.b18 - 128
                       *m.b13*m.b16*m.b19 - 160*m.b13*m.b16*m.b20 - 96*m.b13*m.b16*m.b21 - 64*m.b13*m.b16*m.b22 - 32*
                       m.b13*m.b16*m.b23 - 416*m.b13*m.b17*m.b18 - 288*m.b13*m.b17*m.b19 - 160*m.b13*m.b17*m.b20 - 64*
                       m.b13*m.b17*m.b22 - 32*m.b13*m.b17*m.b23 - 288*m.b13*m.b18*m.b19 - 192*m.b13*m.b18*m.b20 - 96*
                       m.b13*m.b18*m.b21 - 64*m.b13*m.b18*m.b22 - 224*m.b13*m.b19*m.b20 - 128*m.b13*m.b19*m.b21 - 64*
                       m.b13*m.b19*m.b22 - 32*m.b13*m.b19*m.b23 - 160*m.b13*m.b20*m.b21 - 64*m.b13*m.b20*m.b22 - 32*
                       m.b13*m.b20*m.b23 - 96*m.b13*m.b21*m.b22 - 32*m.b13*m.b21*m.b23 - 32*m.b13*m.b22*m.b23 - 512*
                       m.b14*m.b15*m.b16 - 672*m.b14*m.b15*m.b17 - 544*m.b14*m.b15*m.b18 - 416*m.b14*m.b15*m.b19 - 288*
                       m.b14*m.b15*m.b20 - 224*m.b14*m.b15*m.b21 - 160*m.b14*m.b15*m.b22 - 96*m.b14*m.b15*m.b23 - 32*
                       m.b14*m.b15*m.b24 - 672*m.b14*m.b16*m.b17 - 320*m.b14*m.b16*m.b18 - 416*m.b14*m.b16*m.b19 - 288*
                       m.b14*m.b16*m.b20 - 192*m.b14*m.b16*m.b21 - 128*m.b14*m.b16*m.b22 - 64*m.b14*m.b16*m.b23 - 32*
                       m.b14*m.b16*m.b24 - 544*m.b14*m.b17*m.b18 - 416*m.b14*m.b17*m.b19 - 128*m.b14*m.b17*m.b20 - 160*
                       m.b14*m.b17*m.b21 - 96*m.b14*m.b17*m.b22 - 64*m.b14*m.b17*m.b23 - 32*m.b14*m.b17*m.b24 - 416*
                       m.b14*m.b18*m.b19 - 288*m.b14*m.b18*m.b20 - 160*m.b14*m.b18*m.b21 - 64*m.b14*m.b18*m.b23 - 32*
                       m.b14*m.b18*m.b24 - 288*m.b14*m.b19*m.b20 - 192*m.b14*m.b19*m.b21 - 96*m.b14*m.b19*m.b22 - 64*
                       m.b14*m.b19*m.b23 - 224*m.b14*m.b20*m.b21 - 128*m.b14*m.b20*m.b22 - 64*m.b14*m.b20*m.b23 - 32*
                       m.b14*m.b20*m.b24 - 160*m.b14*m.b21*m.b22 - 64*m.b14*m.b21*m.b23 - 32*m.b14*m.b21*m.b24 - 96*
                       m.b14*m.b22*m.b23 - 32*m.b14*m.b22*m.b24 - 32*m.b14*m.b23*m.b24 - 512*m.b15*m.b16*m.b17 - 672*
                       m.b15*m.b16*m.b18 - 544*m.b15*m.b16*m.b19 - 416*m.b15*m.b16*m.b20 - 288*m.b15*m.b16*m.b21 - 224*
                       m.b15*m.b16*m.b22 - 160*m.b15*m.b16*m.b23 - 96*m.b15*m.b16*m.b24 - 32*m.b15*m.b16*m.b25 - 672*
                       m.b15*m.b17*m.b18 - 320*m.b15*m.b17*m.b19 - 416*m.b15*m.b17*m.b20 - 288*m.b15*m.b17*m.b21 - 192*
                       m.b15*m.b17*m.b22 - 128*m.b15*m.b17*m.b23 - 64*m.b15*m.b17*m.b24 - 32*m.b15*m.b17*m.b25 - 544*
                       m.b15*m.b18*m.b19 - 416*m.b15*m.b18*m.b20 - 128*m.b15*m.b18*m.b21 - 160*m.b15*m.b18*m.b22 - 96*
                       m.b15*m.b18*m.b23 - 64*m.b15*m.b18*m.b24 - 32*m.b15*m.b18*m.b25 - 416*m.b15*m.b19*m.b20 - 288*
                       m.b15*m.b19*m.b21 - 160*m.b15*m.b19*m.b22 - 64*m.b15*m.b19*m.b24 - 32*m.b15*m.b19*m.b25 - 288*
                       m.b15*m.b20*m.b21 - 192*m.b15*m.b20*m.b22 - 96*m.b15*m.b20*m.b23 - 64*m.b15*m.b20*m.b24 - 224*
                       m.b15*m.b21*m.b22 - 128*m.b15*m.b21*m.b23 - 64*m.b15*m.b21*m.b24 - 32*m.b15*m.b21*m.b25 - 160*
                       m.b15*m.b22*m.b23 - 64*m.b15*m.b22*m.b24 - 32*m.b15*m.b22*m.b25 - 96*m.b15*m.b23*m.b24 - 32*m.b15
                       *m.b23*m.b25 - 32*m.b15*m.b24*m.b25 - 512*m.b16*m.b17*m.b18 - 672*m.b16*m.b17*m.b19 - 544*m.b16*
                       m.b17*m.b20 - 416*m.b16*m.b17*m.b21 - 288*m.b16*m.b17*m.b22 - 224*m.b16*m.b17*m.b23 - 160*m.b16*
                       m.b17*m.b24 - 96*m.b16*m.b17*m.b25 - 32*m.b16*m.b17*m.b26 - 672*m.b16*m.b18*m.b19 - 320*m.b16*
                       m.b18*m.b20 - 416*m.b16*m.b18*m.b21 - 288*m.b16*m.b18*m.b22 - 192*m.b16*m.b18*m.b23 - 128*m.b16*
                       m.b18*m.b24 - 64*m.b16*m.b18*m.b25 - 32*m.b16*m.b18*m.b26 - 544*m.b16*m.b19*m.b20 - 416*m.b16*
                       m.b19*m.b21 - 128*m.b16*m.b19*m.b22 - 160*m.b16*m.b19*m.b23 - 96*m.b16*m.b19*m.b24 - 64*m.b16*
                       m.b19*m.b25 - 32*m.b16*m.b19*m.b26 - 416*m.b16*m.b20*m.b21 - 288*m.b16*m.b20*m.b22 - 160*m.b16*
                       m.b20*m.b23 - 64*m.b16*m.b20*m.b25 - 32*m.b16*m.b20*m.b26 - 288*m.b16*m.b21*m.b22 - 192*m.b16*
                       m.b21*m.b23 - 96*m.b16*m.b21*m.b24 - 64*m.b16*m.b21*m.b25 - 224*m.b16*m.b22*m.b23 - 128*m.b16*
                       m.b22*m.b24 - 64*m.b16*m.b22*m.b25 - 32*m.b16*m.b22*m.b26 - 160*m.b16*m.b23*m.b24 - 64*m.b16*
                       m.b23*m.b25 - 32*m.b16*m.b23*m.b26 - 96*m.b16*m.b24*m.b25 - 32*m.b16*m.b24*m.b26 - 32*m.b16*m.b25
                       *m.b26 - 512*m.b17*m.b18*m.b19 - 672*m.b17*m.b18*m.b20 - 544*m.b17*m.b18*m.b21 - 416*m.b17*m.b18*
                       m.b22 - 288*m.b17*m.b18*m.b23 - 224*m.b17*m.b18*m.b24 - 160*m.b17*m.b18*m.b25 - 96*m.b17*m.b18*
                       m.b26 - 32*m.b17*m.b18*m.b27 - 672*m.b17*m.b19*m.b20 - 320*m.b17*m.b19*m.b21 - 416*m.b17*m.b19*
                       m.b22 - 288*m.b17*m.b19*m.b23 - 192*m.b17*m.b19*m.b24 - 128*m.b17*m.b19*m.b25 - 64*m.b17*m.b19*
                       m.b26 - 32*m.b17*m.b19*m.b27 - 544*m.b17*m.b20*m.b21 - 416*m.b17*m.b20*m.b22 - 128*m.b17*m.b20*
                       m.b23 - 160*m.b17*m.b20*m.b24 - 96*m.b17*m.b20*m.b25 - 64*m.b17*m.b20*m.b26 - 32*m.b17*m.b20*
                       m.b27 - 416*m.b17*m.b21*m.b22 - 288*m.b17*m.b21*m.b23 - 160*m.b17*m.b21*m.b24 - 64*m.b17*m.b21*
                       m.b26 - 32*m.b17*m.b21*m.b27 - 288*m.b17*m.b22*m.b23 - 192*m.b17*m.b22*m.b24 - 96*m.b17*m.b22*
                       m.b25 - 64*m.b17*m.b22*m.b26 - 224*m.b17*m.b23*m.b24 - 128*m.b17*m.b23*m.b25 - 64*m.b17*m.b23*
                       m.b26 - 32*m.b17*m.b23*m.b27 - 160*m.b17*m.b24*m.b25 - 64*m.b17*m.b24*m.b26 - 32*m.b17*m.b24*
                       m.b27 - 96*m.b17*m.b25*m.b26 - 32*m.b17*m.b25*m.b27 - 32*m.b17*m.b26*m.b27 - 512*m.b18*m.b19*
                       m.b20 - 672*m.b18*m.b19*m.b21 - 544*m.b18*m.b19*m.b22 - 416*m.b18*m.b19*m.b23 - 288*m.b18*m.b19*
                       m.b24 - 224*m.b18*m.b19*m.b25 - 160*m.b18*m.b19*m.b26 - 96*m.b18*m.b19*m.b27 - 32*m.b18*m.b19*
                       m.b28 - 672*m.b18*m.b20*m.b21 - 320*m.b18*m.b20*m.b22 - 416*m.b18*m.b20*m.b23 - 288*m.b18*m.b20*
                       m.b24 - 192*m.b18*m.b20*m.b25 - 128*m.b18*m.b20*m.b26 - 64*m.b18*m.b20*m.b27 - 32*m.b18*m.b20*
                       m.b28 - 544*m.b18*m.b21*m.b22 - 416*m.b18*m.b21*m.b23 - 128*m.b18*m.b21*m.b24 - 160*m.b18*m.b21*
                       m.b25 - 96*m.b18*m.b21*m.b26 - 64*m.b18*m.b21*m.b27 - 32*m.b18*m.b21*m.b28 - 416*m.b18*m.b22*
                       m.b23 - 288*m.b18*m.b22*m.b24 - 160*m.b18*m.b22*m.b25 - 64*m.b18*m.b22*m.b27 - 32*m.b18*m.b22*
                       m.b28 - 288*m.b18*m.b23*m.b24 - 192*m.b18*m.b23*m.b25 - 96*m.b18*m.b23*m.b26 - 64*m.b18*m.b23*
                       m.b27 - 224*m.b18*m.b24*m.b25 - 128*m.b18*m.b24*m.b26 - 64*m.b18*m.b24*m.b27 - 32*m.b18*m.b24*
                       m.b28 - 160*m.b18*m.b25*m.b26 - 64*m.b18*m.b25*m.b27 - 32*m.b18*m.b25*m.b28 - 96*m.b18*m.b26*
                       m.b27 - 32*m.b18*m.b26*m.b28 - 32*m.b18*m.b27*m.b28 - 512*m.b19*m.b20*m.b21 - 672*m.b19*m.b20*
                       m.b22 - 544*m.b19*m.b20*m.b23 - 416*m.b19*m.b20*m.b24 - 288*m.b19*m.b20*m.b25 - 224*m.b19*m.b20*
                       m.b26 - 160*m.b19*m.b20*m.b27 - 96*m.b19*m.b20*m.b28 - 32*m.b19*m.b20*m.b29 - 672*m.b19*m.b21*
                       m.b22 - 320*m.b19*m.b21*m.b23 - 416*m.b19*m.b21*m.b24 - 288*m.b19*m.b21*m.b25 - 192*m.b19*m.b21*
                       m.b26 - 128*m.b19*m.b21*m.b27 - 64*m.b19*m.b21*m.b28 - 32*m.b19*m.b21*m.b29 - 544*m.b19*m.b22*
                       m.b23 - 416*m.b19*m.b22*m.b24 - 128*m.b19*m.b22*m.b25 - 160*m.b19*m.b22*m.b26 - 96*m.b19*m.b22*
                       m.b27 - 64*m.b19*m.b22*m.b28 - 32*m.b19*m.b22*m.b29 - 416*m.b19*m.b23*m.b24 - 288*m.b19*m.b23*
                       m.b25 - 160*m.b19*m.b23*m.b26 - 64*m.b19*m.b23*m.b28 - 32*m.b19*m.b23*m.b29 - 288*m.b19*m.b24*
                       m.b25 - 192*m.b19*m.b24*m.b26 - 96*m.b19*m.b24*m.b27 - 64*m.b19*m.b24*m.b28 - 224*m.b19*m.b25*
                       m.b26 - 128*m.b19*m.b25*m.b27 - 64*m.b19*m.b25*m.b28 - 32*m.b19*m.b25*m.b29 - 160*m.b19*m.b26*
                       m.b27 - 64*m.b19*m.b26*m.b28 - 32*m.b19*m.b26*m.b29 - 96*m.b19*m.b27*m.b28 - 32*m.b19*m.b27*m.b29
                        - 32*m.b19*m.b28*m.b29 - 512*m.b20*m.b21*m.b22 - 672*m.b20*m.b21*m.b23 - 544*m.b20*m.b21*m.b24
                        - 416*m.b20*m.b21*m.b25 - 288*m.b20*m.b21*m.b26 - 224*m.b20*m.b21*m.b27 - 160*m.b20*m.b21*m.b28
                        - 96*m.b20*m.b21*m.b29 - 32*m.b20*m.b21*m.b30 - 672*m.b20*m.b22*m.b23 - 320*m.b20*m.b22*m.b24 - 
                       416*m.b20*m.b22*m.b25 - 288*m.b20*m.b22*m.b26 - 192*m.b20*m.b22*m.b27 - 128*m.b20*m.b22*m.b28 - 
                       64*m.b20*m.b22*m.b29 - 32*m.b20*m.b22*m.b30 - 544*m.b20*m.b23*m.b24 - 416*m.b20*m.b23*m.b25 - 128
                       *m.b20*m.b23*m.b26 - 160*m.b20*m.b23*m.b27 - 96*m.b20*m.b23*m.b28 - 64*m.b20*m.b23*m.b29 - 32*
                       m.b20*m.b23*m.b30 - 416*m.b20*m.b24*m.b25 - 288*m.b20*m.b24*m.b26 - 160*m.b20*m.b24*m.b27 - 64*
                       m.b20*m.b24*m.b29 - 32*m.b20*m.b24*m.b30 - 288*m.b20*m.b25*m.b26 - 192*m.b20*m.b25*m.b27 - 96*
                       m.b20*m.b25*m.b28 - 64*m.b20*m.b25*m.b29 - 224*m.b20*m.b26*m.b27 - 128*m.b20*m.b26*m.b28 - 64*
                       m.b20*m.b26*m.b29 - 32*m.b20*m.b26*m.b30 - 160*m.b20*m.b27*m.b28 - 64*m.b20*m.b27*m.b29 - 32*
                       m.b20*m.b27*m.b30 - 96*m.b20*m.b28*m.b29 - 32*m.b20*m.b28*m.b30 - 32*m.b20*m.b29*m.b30 - 512*
                       m.b21*m.b22*m.b23 - 672*m.b21*m.b22*m.b24 - 544*m.b21*m.b22*m.b25 - 416*m.b21*m.b22*m.b26 - 288*
                       m.b21*m.b22*m.b27 - 224*m.b21*m.b22*m.b28 - 160*m.b21*m.b22*m.b29 - 96*m.b21*m.b22*m.b30 - 32*
                       m.b21*m.b22*m.b31 - 672*m.b21*m.b23*m.b24 - 320*m.b21*m.b23*m.b25 - 416*m.b21*m.b23*m.b26 - 288*
                       m.b21*m.b23*m.b27 - 192*m.b21*m.b23*m.b28 - 128*m.b21*m.b23*m.b29 - 64*m.b21*m.b23*m.b30 - 32*
                       m.b21*m.b23*m.b31 - 544*m.b21*m.b24*m.b25 - 416*m.b21*m.b24*m.b26 - 128*m.b21*m.b24*m.b27 - 160*
                       m.b21*m.b24*m.b28 - 96*m.b21*m.b24*m.b29 - 64*m.b21*m.b24*m.b30 - 32*m.b21*m.b24*m.b31 - 416*
                       m.b21*m.b25*m.b26 - 288*m.b21*m.b25*m.b27 - 160*m.b21*m.b25*m.b28 - 64*m.b21*m.b25*m.b30 - 32*
                       m.b21*m.b25*m.b31 - 288*m.b21*m.b26*m.b27 - 192*m.b21*m.b26*m.b28 - 96*m.b21*m.b26*m.b29 - 64*
                       m.b21*m.b26*m.b30 - 224*m.b21*m.b27*m.b28 - 128*m.b21*m.b27*m.b29 - 64*m.b21*m.b27*m.b30 - 32*
                       m.b21*m.b27*m.b31 - 160*m.b21*m.b28*m.b29 - 64*m.b21*m.b28*m.b30 - 32*m.b21*m.b28*m.b31 - 96*
                       m.b21*m.b29*m.b30 - 32*m.b21*m.b29*m.b31 - 32*m.b21*m.b30*m.b31 - 512*m.b22*m.b23*m.b24 - 672*
                       m.b22*m.b23*m.b25 - 544*m.b22*m.b23*m.b26 - 416*m.b22*m.b23*m.b27 - 288*m.b22*m.b23*m.b28 - 224*
                       m.b22*m.b23*m.b29 - 160*m.b22*m.b23*m.b30 - 96*m.b22*m.b23*m.b31 - 32*m.b22*m.b23*m.b32 - 672*
                       m.b22*m.b24*m.b25 - 320*m.b22*m.b24*m.b26 - 416*m.b22*m.b24*m.b27 - 288*m.b22*m.b24*m.b28 - 192*
                       m.b22*m.b24*m.b29 - 128*m.b22*m.b24*m.b30 - 64*m.b22*m.b24*m.b31 - 32*m.b22*m.b24*m.b32 - 544*
                       m.b22*m.b25*m.b26 - 416*m.b22*m.b25*m.b27 - 128*m.b22*m.b25*m.b28 - 160*m.b22*m.b25*m.b29 - 96*
                       m.b22*m.b25*m.b30 - 64*m.b22*m.b25*m.b31 - 32*m.b22*m.b25*m.b32 - 416*m.b22*m.b26*m.b27 - 288*
                       m.b22*m.b26*m.b28 - 160*m.b22*m.b26*m.b29 - 64*m.b22*m.b26*m.b31 - 32*m.b22*m.b26*m.b32 - 288*
                       m.b22*m.b27*m.b28 - 192*m.b22*m.b27*m.b29 - 96*m.b22*m.b27*m.b30 - 64*m.b22*m.b27*m.b31 - 224*
                       m.b22*m.b28*m.b29 - 128*m.b22*m.b28*m.b30 - 64*m.b22*m.b28*m.b31 - 32*m.b22*m.b28*m.b32 - 160*
                       m.b22*m.b29*m.b30 - 64*m.b22*m.b29*m.b31 - 32*m.b22*m.b29*m.b32 - 96*m.b22*m.b30*m.b31 - 32*m.b22
                       *m.b30*m.b32 - 32*m.b22*m.b31*m.b32 - 512*m.b23*m.b24*m.b25 - 672*m.b23*m.b24*m.b26 - 544*m.b23*
                       m.b24*m.b27 - 416*m.b23*m.b24*m.b28 - 288*m.b23*m.b24*m.b29 - 224*m.b23*m.b24*m.b30 - 160*m.b23*
                       m.b24*m.b31 - 96*m.b23*m.b24*m.b32 - 32*m.b23*m.b24*m.b33 - 672*m.b23*m.b25*m.b26 - 320*m.b23*
                       m.b25*m.b27 - 416*m.b23*m.b25*m.b28 - 288*m.b23*m.b25*m.b29 - 192*m.b23*m.b25*m.b30 - 128*m.b23*
                       m.b25*m.b31 - 64*m.b23*m.b25*m.b32 - 32*m.b23*m.b25*m.b33 - 544*m.b23*m.b26*m.b27 - 416*m.b23*
                       m.b26*m.b28 - 128*m.b23*m.b26*m.b29 - 160*m.b23*m.b26*m.b30 - 96*m.b23*m.b26*m.b31 - 64*m.b23*
                       m.b26*m.b32 - 32*m.b23*m.b26*m.b33 - 416*m.b23*m.b27*m.b28 - 288*m.b23*m.b27*m.b29 - 160*m.b23*
                       m.b27*m.b30 - 64*m.b23*m.b27*m.b32 - 32*m.b23*m.b27*m.b33 - 288*m.b23*m.b28*m.b29 - 192*m.b23*
                       m.b28*m.b30 - 96*m.b23*m.b28*m.b31 - 64*m.b23*m.b28*m.b32 - 224*m.b23*m.b29*m.b30 - 128*m.b23*
                       m.b29*m.b31 - 64*m.b23*m.b29*m.b32 - 32*m.b23*m.b29*m.b33 - 160*m.b23*m.b30*m.b31 - 64*m.b23*
                       m.b30*m.b32 - 32*m.b23*m.b30*m.b33 - 96*m.b23*m.b31*m.b32 - 32*m.b23*m.b31*m.b33 - 32*m.b23*m.b32
                       *m.b33 - 512*m.b24*m.b25*m.b26 - 672*m.b24*m.b25*m.b27 - 544*m.b24*m.b25*m.b28 - 416*m.b24*m.b25*
                       m.b29 - 288*m.b24*m.b25*m.b30 - 224*m.b24*m.b25*m.b31 - 160*m.b24*m.b25*m.b32 - 96*m.b24*m.b25*
                       m.b33 - 32*m.b24*m.b25*m.b34 - 672*m.b24*m.b26*m.b27 - 320*m.b24*m.b26*m.b28 - 416*m.b24*m.b26*
                       m.b29 - 288*m.b24*m.b26*m.b30 - 192*m.b24*m.b26*m.b31 - 128*m.b24*m.b26*m.b32 - 64*m.b24*m.b26*
                       m.b33 - 32*m.b24*m.b26*m.b34 - 544*m.b24*m.b27*m.b28 - 416*m.b24*m.b27*m.b29 - 128*m.b24*m.b27*
                       m.b30 - 160*m.b24*m.b27*m.b31 - 96*m.b24*m.b27*m.b32 - 64*m.b24*m.b27*m.b33 - 32*m.b24*m.b27*
                       m.b34 - 416*m.b24*m.b28*m.b29 - 288*m.b24*m.b28*m.b30 - 160*m.b24*m.b28*m.b31 - 64*m.b24*m.b28*
                       m.b33 - 32*m.b24*m.b28*m.b34 - 288*m.b24*m.b29*m.b30 - 192*m.b24*m.b29*m.b31 - 96*m.b24*m.b29*
                       m.b32 - 64*m.b24*m.b29*m.b33 - 224*m.b24*m.b30*m.b31 - 128*m.b24*m.b30*m.b32 - 64*m.b24*m.b30*
                       m.b33 - 32*m.b24*m.b30*m.b34 - 160*m.b24*m.b31*m.b32 - 64*m.b24*m.b31*m.b33 - 32*m.b24*m.b31*
                       m.b34 - 96*m.b24*m.b32*m.b33 - 32*m.b24*m.b32*m.b34 - 32*m.b24*m.b33*m.b34 - 512*m.b25*m.b26*
                       m.b27 - 672*m.b25*m.b26*m.b28 - 544*m.b25*m.b26*m.b29 - 416*m.b25*m.b26*m.b30 - 288*m.b25*m.b26*
                       m.b31 - 224*m.b25*m.b26*m.b32 - 160*m.b25*m.b26*m.b33 - 96*m.b25*m.b26*m.b34 - 32*m.b25*m.b26*
                       m.b35 - 672*m.b25*m.b27*m.b28 - 320*m.b25*m.b27*m.b29 - 416*m.b25*m.b27*m.b30 - 288*m.b25*m.b27*
                       m.b31 - 192*m.b25*m.b27*m.b32 - 128*m.b25*m.b27*m.b33 - 64*m.b25*m.b27*m.b34 - 32*m.b25*m.b27*
                       m.b35 - 544*m.b25*m.b28*m.b29 - 416*m.b25*m.b28*m.b30 - 128*m.b25*m.b28*m.b31 - 160*m.b25*m.b28*
                       m.b32 - 96*m.b25*m.b28*m.b33 - 64*m.b25*m.b28*m.b34 - 32*m.b25*m.b28*m.b35 - 416*m.b25*m.b29*
                       m.b30 - 288*m.b25*m.b29*m.b31 - 160*m.b25*m.b29*m.b32 - 64*m.b25*m.b29*m.b34 - 32*m.b25*m.b29*
                       m.b35 - 288*m.b25*m.b30*m.b31 - 192*m.b25*m.b30*m.b32 - 96*m.b25*m.b30*m.b33 - 64*m.b25*m.b30*
                       m.b34 - 224*m.b25*m.b31*m.b32 - 128*m.b25*m.b31*m.b33 - 64*m.b25*m.b31*m.b34 - 32*m.b25*m.b31*
                       m.b35 - 160*m.b25*m.b32*m.b33 - 64*m.b25*m.b32*m.b34 - 32*m.b25*m.b32*m.b35 - 96*m.b25*m.b33*
                       m.b34 - 32*m.b25*m.b33*m.b35 - 32*m.b25*m.b34*m.b35 - 512*m.b26*m.b27*m.b28 - 672*m.b26*m.b27*
                       m.b29 - 544*m.b26*m.b27*m.b30 - 416*m.b26*m.b27*m.b31 - 288*m.b26*m.b27*m.b32 - 224*m.b26*m.b27*
                       m.b33 - 160*m.b26*m.b27*m.b34 - 96*m.b26*m.b27*m.b35 - 32*m.b26*m.b27*m.b36 - 672*m.b26*m.b28*
                       m.b29 - 320*m.b26*m.b28*m.b30 - 416*m.b26*m.b28*m.b31 - 288*m.b26*m.b28*m.b32 - 192*m.b26*m.b28*
                       m.b33 - 128*m.b26*m.b28*m.b34 - 64*m.b26*m.b28*m.b35 - 32*m.b26*m.b28*m.b36 - 544*m.b26*m.b29*
                       m.b30 - 416*m.b26*m.b29*m.b31 - 128*m.b26*m.b29*m.b32 - 160*m.b26*m.b29*m.b33 - 96*m.b26*m.b29*
                       m.b34 - 64*m.b26*m.b29*m.b35 - 32*m.b26*m.b29*m.b36 - 416*m.b26*m.b30*m.b31 - 288*m.b26*m.b30*
                       m.b32 - 160*m.b26*m.b30*m.b33 - 64*m.b26*m.b30*m.b35 - 32*m.b26*m.b30*m.b36 - 288*m.b26*m.b31*
                       m.b32 - 192*m.b26*m.b31*m.b33 - 96*m.b26*m.b31*m.b34 - 64*m.b26*m.b31*m.b35 - 224*m.b26*m.b32*
                       m.b33 - 128*m.b26*m.b32*m.b34 - 64*m.b26*m.b32*m.b35 - 32*m.b26*m.b32*m.b36 - 160*m.b26*m.b33*
                       m.b34 - 64*m.b26*m.b33*m.b35 - 32*m.b26*m.b33*m.b36 - 96*m.b26*m.b34*m.b35 - 32*m.b26*m.b34*m.b36
                        - 32*m.b26*m.b35*m.b36 - 512*m.b27*m.b28*m.b29 - 672*m.b27*m.b28*m.b30 - 544*m.b27*m.b28*m.b31
                        - 416*m.b27*m.b28*m.b32 - 288*m.b27*m.b28*m.b33 - 224*m.b27*m.b28*m.b34 - 160*m.b27*m.b28*m.b35
                        - 96*m.b27*m.b28*m.b36 - 32*m.b27*m.b28*m.b37 - 672*m.b27*m.b29*m.b30 - 320*m.b27*m.b29*m.b31 - 
                       416*m.b27*m.b29*m.b32 - 288*m.b27*m.b29*m.b33 - 192*m.b27*m.b29*m.b34 - 128*m.b27*m.b29*m.b35 - 
                       64*m.b27*m.b29*m.b36 - 32*m.b27*m.b29*m.b37 - 544*m.b27*m.b30*m.b31 - 416*m.b27*m.b30*m.b32 - 128
                       *m.b27*m.b30*m.b33 - 160*m.b27*m.b30*m.b34 - 96*m.b27*m.b30*m.b35 - 64*m.b27*m.b30*m.b36 - 32*
                       m.b27*m.b30*m.b37 - 416*m.b27*m.b31*m.b32 - 288*m.b27*m.b31*m.b33 - 160*m.b27*m.b31*m.b34 - 64*
                       m.b27*m.b31*m.b36 - 32*m.b27*m.b31*m.b37 - 288*m.b27*m.b32*m.b33 - 192*m.b27*m.b32*m.b34 - 96*
                       m.b27*m.b32*m.b35 - 64*m.b27*m.b32*m.b36 - 224*m.b27*m.b33*m.b34 - 128*m.b27*m.b33*m.b35 - 64*
                       m.b27*m.b33*m.b36 - 32*m.b27*m.b33*m.b37 - 160*m.b27*m.b34*m.b35 - 64*m.b27*m.b34*m.b36 - 32*
                       m.b27*m.b34*m.b37 - 96*m.b27*m.b35*m.b36 - 32*m.b27*m.b35*m.b37 - 32*m.b27*m.b36*m.b37 - 512*
                       m.b28*m.b29*m.b30 - 672*m.b28*m.b29*m.b31 - 544*m.b28*m.b29*m.b32 - 416*m.b28*m.b29*m.b33 - 288*
                       m.b28*m.b29*m.b34 - 224*m.b28*m.b29*m.b35 - 160*m.b28*m.b29*m.b36 - 96*m.b28*m.b29*m.b37 - 32*
                       m.b28*m.b29*m.b38 - 672*m.b28*m.b30*m.b31 - 320*m.b28*m.b30*m.b32 - 416*m.b28*m.b30*m.b33 - 288*
                       m.b28*m.b30*m.b34 - 192*m.b28*m.b30*m.b35 - 128*m.b28*m.b30*m.b36 - 64*m.b28*m.b30*m.b37 - 32*
                       m.b28*m.b30*m.b38 - 544*m.b28*m.b31*m.b32 - 416*m.b28*m.b31*m.b33 - 128*m.b28*m.b31*m.b34 - 160*
                       m.b28*m.b31*m.b35 - 96*m.b28*m.b31*m.b36 - 64*m.b28*m.b31*m.b37 - 32*m.b28*m.b31*m.b38 - 416*
                       m.b28*m.b32*m.b33 - 288*m.b28*m.b32*m.b34 - 160*m.b28*m.b32*m.b35 - 64*m.b28*m.b32*m.b37 - 32*
                       m.b28*m.b32*m.b38 - 288*m.b28*m.b33*m.b34 - 192*m.b28*m.b33*m.b35 - 96*m.b28*m.b33*m.b36 - 64*
                       m.b28*m.b33*m.b37 - 224*m.b28*m.b34*m.b35 - 128*m.b28*m.b34*m.b36 - 64*m.b28*m.b34*m.b37 - 32*
                       m.b28*m.b34*m.b38 - 160*m.b28*m.b35*m.b36 - 64*m.b28*m.b35*m.b37 - 32*m.b28*m.b35*m.b38 - 96*
                       m.b28*m.b36*m.b37 - 32*m.b28*m.b36*m.b38 - 32*m.b28*m.b37*m.b38 - 512*m.b29*m.b30*m.b31 - 672*
                       m.b29*m.b30*m.b32 - 544*m.b29*m.b30*m.b33 - 416*m.b29*m.b30*m.b34 - 288*m.b29*m.b30*m.b35 - 224*
                       m.b29*m.b30*m.b36 - 160*m.b29*m.b30*m.b37 - 96*m.b29*m.b30*m.b38 - 32*m.b29*m.b30*m.b39 - 672*
                       m.b29*m.b31*m.b32 - 320*m.b29*m.b31*m.b33 - 416*m.b29*m.b31*m.b34 - 288*m.b29*m.b31*m.b35 - 192*
                       m.b29*m.b31*m.b36 - 128*m.b29*m.b31*m.b37 - 64*m.b29*m.b31*m.b38 - 32*m.b29*m.b31*m.b39 - 544*
                       m.b29*m.b32*m.b33 - 416*m.b29*m.b32*m.b34 - 128*m.b29*m.b32*m.b35 - 160*m.b29*m.b32*m.b36 - 96*
                       m.b29*m.b32*m.b37 - 64*m.b29*m.b32*m.b38 - 32*m.b29*m.b32*m.b39 - 416*m.b29*m.b33*m.b34 - 288*
                       m.b29*m.b33*m.b35 - 160*m.b29*m.b33*m.b36 - 64*m.b29*m.b33*m.b38 - 32*m.b29*m.b33*m.b39 - 288*
                       m.b29*m.b34*m.b35 - 192*m.b29*m.b34*m.b36 - 96*m.b29*m.b34*m.b37 - 64*m.b29*m.b34*m.b38 - 224*
                       m.b29*m.b35*m.b36 - 128*m.b29*m.b35*m.b37 - 64*m.b29*m.b35*m.b38 - 32*m.b29*m.b35*m.b39 - 160*
                       m.b29*m.b36*m.b37 - 64*m.b29*m.b36*m.b38 - 32*m.b29*m.b36*m.b39 - 96*m.b29*m.b37*m.b38 - 32*m.b29
                       *m.b37*m.b39 - 32*m.b29*m.b38*m.b39 - 512*m.b30*m.b31*m.b32 - 672*m.b30*m.b31*m.b33 - 544*m.b30*
                       m.b31*m.b34 - 416*m.b30*m.b31*m.b35 - 288*m.b30*m.b31*m.b36 - 224*m.b30*m.b31*m.b37 - 160*m.b30*
                       m.b31*m.b38 - 96*m.b30*m.b31*m.b39 - 32*m.b30*m.b31*m.b40 - 672*m.b30*m.b32*m.b33 - 320*m.b30*
                       m.b32*m.b34 - 416*m.b30*m.b32*m.b35 - 288*m.b30*m.b32*m.b36 - 192*m.b30*m.b32*m.b37 - 128*m.b30*
                       m.b32*m.b38 - 64*m.b30*m.b32*m.b39 - 32*m.b30*m.b32*m.b40 - 544*m.b30*m.b33*m.b34 - 416*m.b30*
                       m.b33*m.b35 - 128*m.b30*m.b33*m.b36 - 160*m.b30*m.b33*m.b37 - 96*m.b30*m.b33*m.b38 - 64*m.b30*
                       m.b33*m.b39 - 32*m.b30*m.b33*m.b40 - 416*m.b30*m.b34*m.b35 - 288*m.b30*m.b34*m.b36 - 160*m.b30*
                       m.b34*m.b37 - 64*m.b30*m.b34*m.b39 - 32*m.b30*m.b34*m.b40 - 288*m.b30*m.b35*m.b36 - 192*m.b30*
                       m.b35*m.b37 - 96*m.b30*m.b35*m.b38 - 64*m.b30*m.b35*m.b39 - 224*m.b30*m.b36*m.b37 - 128*m.b30*
                       m.b36*m.b38 - 64*m.b30*m.b36*m.b39 - 32*m.b30*m.b36*m.b40 - 160*m.b30*m.b37*m.b38 - 64*m.b30*
                       m.b37*m.b39 - 32*m.b30*m.b37*m.b40 - 96*m.b30*m.b38*m.b39 - 32*m.b30*m.b38*m.b40 - 32*m.b30*m.b39
                       *m.b40 - 512*m.b31*m.b32*m.b33 - 672*m.b31*m.b32*m.b34 - 544*m.b31*m.b32*m.b35 - 416*m.b31*m.b32*
                       m.b36 - 288*m.b31*m.b32*m.b37 - 224*m.b31*m.b32*m.b38 - 160*m.b31*m.b32*m.b39 - 96*m.b31*m.b32*
                       m.b40 - 32*m.b31*m.b32*m.b41 - 672*m.b31*m.b33*m.b34 - 320*m.b31*m.b33*m.b35 - 416*m.b31*m.b33*
                       m.b36 - 288*m.b31*m.b33*m.b37 - 192*m.b31*m.b33*m.b38 - 128*m.b31*m.b33*m.b39 - 64*m.b31*m.b33*
                       m.b40 - 32*m.b31*m.b33*m.b41 - 544*m.b31*m.b34*m.b35 - 416*m.b31*m.b34*m.b36 - 128*m.b31*m.b34*
                       m.b37 - 160*m.b31*m.b34*m.b38 - 96*m.b31*m.b34*m.b39 - 64*m.b31*m.b34*m.b40 - 32*m.b31*m.b34*
                       m.b41 - 416*m.b31*m.b35*m.b36 - 288*m.b31*m.b35*m.b37 - 160*m.b31*m.b35*m.b38 - 64*m.b31*m.b35*
                       m.b40 - 32*m.b31*m.b35*m.b41 - 288*m.b31*m.b36*m.b37 - 192*m.b31*m.b36*m.b38 - 96*m.b31*m.b36*
                       m.b39 - 64*m.b31*m.b36*m.b40 - 224*m.b31*m.b37*m.b38 - 128*m.b31*m.b37*m.b39 - 64*m.b31*m.b37*
                       m.b40 - 32*m.b31*m.b37*m.b41 - 160*m.b31*m.b38*m.b39 - 64*m.b31*m.b38*m.b40 - 32*m.b31*m.b38*
                       m.b41 - 96*m.b31*m.b39*m.b40 - 32*m.b31*m.b39*m.b41 - 32*m.b31*m.b40*m.b41 - 512*m.b32*m.b33*
                       m.b34 - 672*m.b32*m.b33*m.b35 - 544*m.b32*m.b33*m.b36 - 416*m.b32*m.b33*m.b37 - 288*m.b32*m.b33*
                       m.b38 - 224*m.b32*m.b33*m.b39 - 160*m.b32*m.b33*m.b40 - 96*m.b32*m.b33*m.b41 - 32*m.b32*m.b33*
                       m.b42 - 672*m.b32*m.b34*m.b35 - 320*m.b32*m.b34*m.b36 - 416*m.b32*m.b34*m.b37 - 288*m.b32*m.b34*
                       m.b38 - 192*m.b32*m.b34*m.b39 - 128*m.b32*m.b34*m.b40 - 64*m.b32*m.b34*m.b41 - 32*m.b32*m.b34*
                       m.b42 - 544*m.b32*m.b35*m.b36 - 416*m.b32*m.b35*m.b37 - 128*m.b32*m.b35*m.b38 - 160*m.b32*m.b35*
                       m.b39 - 96*m.b32*m.b35*m.b40 - 64*m.b32*m.b35*m.b41 - 32*m.b32*m.b35*m.b42 - 416*m.b32*m.b36*
                       m.b37 - 288*m.b32*m.b36*m.b38 - 160*m.b32*m.b36*m.b39 - 64*m.b32*m.b36*m.b41 - 32*m.b32*m.b36*
                       m.b42 - 288*m.b32*m.b37*m.b38 - 192*m.b32*m.b37*m.b39 - 96*m.b32*m.b37*m.b40 - 64*m.b32*m.b37*
                       m.b41 - 224*m.b32*m.b38*m.b39 - 128*m.b32*m.b38*m.b40 - 64*m.b32*m.b38*m.b41 - 32*m.b32*m.b38*
                       m.b42 - 160*m.b32*m.b39*m.b40 - 64*m.b32*m.b39*m.b41 - 32*m.b32*m.b39*m.b42 - 96*m.b32*m.b40*
                       m.b41 - 32*m.b32*m.b40*m.b42 - 32*m.b32*m.b41*m.b42 - 512*m.b33*m.b34*m.b35 - 672*m.b33*m.b34*
                       m.b36 - 544*m.b33*m.b34*m.b37 - 416*m.b33*m.b34*m.b38 - 288*m.b33*m.b34*m.b39 - 224*m.b33*m.b34*
                       m.b40 - 160*m.b33*m.b34*m.b41 - 96*m.b33*m.b34*m.b42 - 32*m.b33*m.b34*m.b43 - 672*m.b33*m.b35*
                       m.b36 - 320*m.b33*m.b35*m.b37 - 416*m.b33*m.b35*m.b38 - 288*m.b33*m.b35*m.b39 - 192*m.b33*m.b35*
                       m.b40 - 128*m.b33*m.b35*m.b41 - 64*m.b33*m.b35*m.b42 - 32*m.b33*m.b35*m.b43 - 544*m.b33*m.b36*
                       m.b37 - 416*m.b33*m.b36*m.b38 - 128*m.b33*m.b36*m.b39 - 160*m.b33*m.b36*m.b40 - 96*m.b33*m.b36*
                       m.b41 - 64*m.b33*m.b36*m.b42 - 32*m.b33*m.b36*m.b43 - 416*m.b33*m.b37*m.b38 - 288*m.b33*m.b37*
                       m.b39 - 160*m.b33*m.b37*m.b40 - 64*m.b33*m.b37*m.b42 - 32*m.b33*m.b37*m.b43 - 288*m.b33*m.b38*
                       m.b39 - 192*m.b33*m.b38*m.b40 - 96*m.b33*m.b38*m.b41 - 64*m.b33*m.b38*m.b42 - 224*m.b33*m.b39*
                       m.b40 - 128*m.b33*m.b39*m.b41 - 64*m.b33*m.b39*m.b42 - 32*m.b33*m.b39*m.b43 - 160*m.b33*m.b40*
                       m.b41 - 64*m.b33*m.b40*m.b42 - 32*m.b33*m.b40*m.b43 - 96*m.b33*m.b41*m.b42 - 32*m.b33*m.b41*m.b43
                        - 32*m.b33*m.b42*m.b43 - 512*m.b34*m.b35*m.b36 - 672*m.b34*m.b35*m.b37 - 544*m.b34*m.b35*m.b38
                        - 416*m.b34*m.b35*m.b39 - 288*m.b34*m.b35*m.b40 - 224*m.b34*m.b35*m.b41 - 160*m.b34*m.b35*m.b42
                        - 96*m.b34*m.b35*m.b43 - 32*m.b34*m.b35*m.b44 - 672*m.b34*m.b36*m.b37 - 320*m.b34*m.b36*m.b38 - 
                       416*m.b34*m.b36*m.b39 - 288*m.b34*m.b36*m.b40 - 192*m.b34*m.b36*m.b41 - 128*m.b34*m.b36*m.b42 - 
                       64*m.b34*m.b36*m.b43 - 32*m.b34*m.b36*m.b44 - 544*m.b34*m.b37*m.b38 - 416*m.b34*m.b37*m.b39 - 128
                       *m.b34*m.b37*m.b40 - 160*m.b34*m.b37*m.b41 - 96*m.b34*m.b37*m.b42 - 64*m.b34*m.b37*m.b43 - 32*
                       m.b34*m.b37*m.b44 - 416*m.b34*m.b38*m.b39 - 288*m.b34*m.b38*m.b40 - 160*m.b34*m.b38*m.b41 - 64*
                       m.b34*m.b38*m.b43 - 32*m.b34*m.b38*m.b44 - 288*m.b34*m.b39*m.b40 - 192*m.b34*m.b39*m.b41 - 96*
                       m.b34*m.b39*m.b42 - 64*m.b34*m.b39*m.b43 - 224*m.b34*m.b40*m.b41 - 128*m.b34*m.b40*m.b42 - 64*
                       m.b34*m.b40*m.b43 - 32*m.b34*m.b40*m.b44 - 160*m.b34*m.b41*m.b42 - 64*m.b34*m.b41*m.b43 - 32*
                       m.b34*m.b41*m.b44 - 96*m.b34*m.b42*m.b43 - 32*m.b34*m.b42*m.b44 - 32*m.b34*m.b43*m.b44 - 512*
                       m.b35*m.b36*m.b37 - 672*m.b35*m.b36*m.b38 - 544*m.b35*m.b36*m.b39 - 416*m.b35*m.b36*m.b40 - 288*
                       m.b35*m.b36*m.b41 - 224*m.b35*m.b36*m.b42 - 160*m.b35*m.b36*m.b43 - 96*m.b35*m.b36*m.b44 - 32*
                       m.b35*m.b36*m.b45 - 672*m.b35*m.b37*m.b38 - 320*m.b35*m.b37*m.b39 - 416*m.b35*m.b37*m.b40 - 288*
                       m.b35*m.b37*m.b41 - 192*m.b35*m.b37*m.b42 - 128*m.b35*m.b37*m.b43 - 64*m.b35*m.b37*m.b44 - 32*
                       m.b35*m.b37*m.b45 - 544*m.b35*m.b38*m.b39 - 416*m.b35*m.b38*m.b40 - 128*m.b35*m.b38*m.b41 - 160*
                       m.b35*m.b38*m.b42 - 96*m.b35*m.b38*m.b43 - 64*m.b35*m.b38*m.b44 - 32*m.b35*m.b38*m.b45 - 416*
                       m.b35*m.b39*m.b40 - 288*m.b35*m.b39*m.b41 - 160*m.b35*m.b39*m.b42 - 64*m.b35*m.b39*m.b44 - 32*
                       m.b35*m.b39*m.b45 - 288*m.b35*m.b40*m.b41 - 192*m.b35*m.b40*m.b42 - 96*m.b35*m.b40*m.b43 - 64*
                       m.b35*m.b40*m.b44 - 224*m.b35*m.b41*m.b42 - 128*m.b35*m.b41*m.b43 - 64*m.b35*m.b41*m.b44 - 32*
                       m.b35*m.b41*m.b45 - 160*m.b35*m.b42*m.b43 - 64*m.b35*m.b42*m.b44 - 32*m.b35*m.b42*m.b45 - 96*
                       m.b35*m.b43*m.b44 - 32*m.b35*m.b43*m.b45 - 32*m.b35*m.b44*m.b45 - 480*m.b36*m.b37*m.b38 - 608*
                       m.b36*m.b37*m.b39 - 480*m.b36*m.b37*m.b40 - 352*m.b36*m.b37*m.b41 - 224*m.b36*m.b37*m.b42 - 160*
                       m.b36*m.b37*m.b43 - 96*m.b36*m.b37*m.b44 - 32*m.b36*m.b37*m.b45 - 608*m.b36*m.b38*m.b39 - 288*
                       m.b36*m.b38*m.b40 - 352*m.b36*m.b38*m.b41 - 224*m.b36*m.b38*m.b42 - 128*m.b36*m.b38*m.b43 - 64*
                       m.b36*m.b38*m.b44 - 32*m.b36*m.b38*m.b45 - 480*m.b36*m.b39*m.b40 - 352*m.b36*m.b39*m.b41 - 96*
                       m.b36*m.b39*m.b42 - 96*m.b36*m.b39*m.b43 - 64*m.b36*m.b39*m.b44 - 32*m.b36*m.b39*m.b45 - 352*
                       m.b36*m.b40*m.b41 - 224*m.b36*m.b40*m.b42 - 128*m.b36*m.b40*m.b43 - 32*m.b36*m.b40*m.b45 - 256*
                       m.b36*m.b41*m.b42 - 160*m.b36*m.b41*m.b43 - 64*m.b36*m.b41*m.b44 - 32*m.b36*m.b41*m.b45 - 192*
                       m.b36*m.b42*m.b43 - 96*m.b36*m.b42*m.b44 - 32*m.b36*m.b42*m.b45 - 128*m.b36*m.b43*m.b44 - 32*
                       m.b36*m.b43*m.b45 - 64*m.b36*m.b44*m.b45 - 416*m.b37*m.b38*m.b39 - 544*m.b37*m.b38*m.b40 - 416*
                       m.b37*m.b38*m.b41 - 288*m.b37*m.b38*m.b42 - 160*m.b37*m.b38*m.b43 - 96*m.b37*m.b38*m.b44 - 32*
                       m.b37*m.b38*m.b45 - 512*m.b37*m.b39*m.b40 - 256*m.b37*m.b39*m.b41 - 288*m.b37*m.b39*m.b42 - 160*
                       m.b37*m.b39*m.b43 - 64*m.b37*m.b39*m.b44 - 32*m.b37*m.b39*m.b45 - 384*m.b37*m.b40*m.b41 - 288*
                       m.b37*m.b40*m.b42 - 64*m.b37*m.b40*m.b43 - 64*m.b37*m.b40*m.b44 - 32*m.b37*m.b40*m.b45 - 256*
                       m.b37*m.b41*m.b42 - 192*m.b37*m.b41*m.b43 - 96*m.b37*m.b41*m.b44 - 192*m.b37*m.b42*m.b43 - 128*
                       m.b37*m.b42*m.b44 - 32*m.b37*m.b42*m.b45 - 128*m.b37*m.b43*m.b44 - 64*m.b37*m.b43*m.b45 - 64*
                       m.b37*m.b44*m.b45 - 352*m.b38*m.b39*m.b40 - 448*m.b38*m.b39*m.b41 - 352*m.b38*m.b39*m.b42 - 224*
                       m.b38*m.b39*m.b43 - 96*m.b38*m.b39*m.b44 - 32*m.b38*m.b39*m.b45 - 416*m.b38*m.b40*m.b41 - 192*
                       m.b38*m.b40*m.b42 - 224*m.b38*m.b40*m.b43 - 96*m.b38*m.b40*m.b44 - 32*m.b38*m.b40*m.b45 - 288*
                       m.b38*m.b41*m.b42 - 192*m.b38*m.b41*m.b43 - 64*m.b38*m.b41*m.b44 - 32*m.b38*m.b41*m.b45 - 192*
                       m.b38*m.b42*m.b43 - 128*m.b38*m.b42*m.b44 - 64*m.b38*m.b42*m.b45 - 128*m.b38*m.b43*m.b44 - 64*
                       m.b38*m.b43*m.b45 - 64*m.b38*m.b44*m.b45 - 288*m.b39*m.b40*m.b41 - 352*m.b39*m.b40*m.b42 - 256*
                       m.b39*m.b40*m.b43 - 160*m.b39*m.b40*m.b44 - 32*m.b39*m.b40*m.b45 - 320*m.b39*m.b41*m.b42 - 128*
                       m.b39*m.b41*m.b43 - 128*m.b39*m.b41*m.b44 - 64*m.b39*m.b41*m.b45 - 192*m.b39*m.b42*m.b43 - 128*
                       m.b39*m.b42*m.b44 - 32*m.b39*m.b42*m.b45 - 128*m.b39*m.b43*m.b44 - 64*m.b39*m.b43*m.b45 - 64*
                       m.b39*m.b44*m.b45 - 224*m.b40*m.b41*m.b42 - 256*m.b40*m.b41*m.b43 - 160*m.b40*m.b41*m.b44 - 64*
                       m.b40*m.b41*m.b45 - 224*m.b40*m.b42*m.b43 - 64*m.b40*m.b42*m.b44 - 64*m.b40*m.b42*m.b45 - 128*
                       m.b40*m.b43*m.b44 - 64*m.b40*m.b43*m.b45 - 64*m.b40*m.b44*m.b45 - 160*m.b41*m.b42*m.b43 - 160*
                       m.b41*m.b42*m.b44 - 64*m.b41*m.b42*m.b45 - 128*m.b41*m.b43*m.b44 - 32*m.b41*m.b43*m.b45 - 64*
                       m.b41*m.b44*m.b45 - 96*m.b42*m.b43*m.b44 - 64*m.b42*m.b43*m.b45 - 64*m.b42*m.b44*m.b45 - 32*m.b43
                       *m.b44*m.b45 + 128*m.b1*m.b2 + 120*m.b1*m.b3 + 112*m.b1*m.b4 + 104*m.b1*m.b5 + 96*m.b1*m.b6 + 104
                       *m.b1*m.b7 + 96*m.b1*m.b8 + 88*m.b1*m.b9 + 80*m.b1*m.b10 + 72*m.b1*m.b11 + 256*m.b2*m.b3 + 256*
                       m.b2*m.b4 + 240*m.b2*m.b5 + 224*m.b2*m.b6 + 224*m.b2*m.b7 + 224*m.b2*m.b8 + 208*m.b2*m.b9 + 192*
                       m.b2*m.b10 + 160*m.b2*m.b11 + 72*m.b2*m.b12 + 400*m.b3*m.b4 + 392*m.b3*m.b5 + 384*m.b3*m.b6 + 360
                       *m.b3*m.b7 + 368*m.b3*m.b8 + 360*m.b3*m.b9 + 320*m.b3*m.b10 + 280*m.b3*m.b11 + 160*m.b3*m.b12 + 
                       72*m.b3*m.b13 + 560*m.b4*m.b5 + 544*m.b4*m.b6 + 528*m.b4*m.b7 + 528*m.b4*m.b8 + 512*m.b4*m.b9 + 
                       480*m.b4*m.b10 + 416*m.b4*m.b11 + 280*m.b4*m.b12 + 160*m.b4*m.b13 + 72*m.b4*m.b14 + 736*m.b5*m.b6
                        + 712*m.b5*m.b7 + 672*m.b5*m.b8 + 664*m.b5*m.b9 + 640*m.b5*m.b10 + 584*m.b5*m.b11 + 416*m.b5*
                       m.b12 + 280*m.b5*m.b13 + 160*m.b5*m.b14 + 72*m.b5*m.b15 + 912*m.b6*m.b7 + 864*m.b6*m.b8 + 816*
                       m.b6*m.b9 + 784*m.b6*m.b10 + 736*m.b6*m.b11 + 584*m.b6*m.b12 + 416*m.b6*m.b13 + 280*m.b6*m.b14 + 
                       160*m.b6*m.b15 + 72*m.b6*m.b16 + 1072*m.b7*m.b8 + 1000*m.b7*m.b9 + 944*m.b7*m.b10 + 888*m.b7*
                       m.b11 + 736*m.b7*m.b12 + 584*m.b7*m.b13 + 416*m.b7*m.b14 + 280*m.b7*m.b15 + 160*m.b7*m.b16 + 72*
                       m.b7*m.b17 + 1216*m.b8*m.b9 + 1136*m.b8*m.b10 + 1056*m.b8*m.b11 + 888*m.b8*m.b12 + 736*m.b8*m.b13
                        + 584*m.b8*m.b14 + 416*m.b8*m.b15 + 280*m.b8*m.b16 + 160*m.b8*m.b17 + 72*m.b8*m.b18 + 1344*m.b9*
                       m.b10 + 1256*m.b9*m.b11 + 1056*m.b9*m.b12 + 888*m.b9*m.b13 + 736*m.b9*m.b14 + 584*m.b9*m.b15 + 
                       416*m.b9*m.b16 + 280*m.b9*m.b17 + 160*m.b9*m.b18 + 72*m.b9*m.b19 + 1472*m.b10*m.b11 + 1256*m.b10*
                       m.b12 + 1056*m.b10*m.b13 + 888*m.b10*m.b14 + 736*m.b10*m.b15 + 584*m.b10*m.b16 + 416*m.b10*m.b17
                        + 280*m.b10*m.b18 + 160*m.b10*m.b19 + 72*m.b10*m.b20 + 1472*m.b11*m.b12 + 1256*m.b11*m.b13 + 
                       1056*m.b11*m.b14 + 888*m.b11*m.b15 + 736*m.b11*m.b16 + 584*m.b11*m.b17 + 416*m.b11*m.b18 + 280*
                       m.b11*m.b19 + 160*m.b11*m.b20 + 72*m.b11*m.b21 + 1472*m.b12*m.b13 + 1256*m.b12*m.b14 + 1056*m.b12
                       *m.b15 + 888*m.b12*m.b16 + 736*m.b12*m.b17 + 584*m.b12*m.b18 + 416*m.b12*m.b19 + 280*m.b12*m.b20
                        + 160*m.b12*m.b21 + 72*m.b12*m.b22 + 1472*m.b13*m.b14 + 1256*m.b13*m.b15 + 1056*m.b13*m.b16 + 
                       888*m.b13*m.b17 + 736*m.b13*m.b18 + 584*m.b13*m.b19 + 416*m.b13*m.b20 + 280*m.b13*m.b21 + 160*
                       m.b13*m.b22 + 72*m.b13*m.b23 + 1472*m.b14*m.b15 + 1256*m.b14*m.b16 + 1056*m.b14*m.b17 + 888*m.b14
                       *m.b18 + 736*m.b14*m.b19 + 584*m.b14*m.b20 + 416*m.b14*m.b21 + 280*m.b14*m.b22 + 160*m.b14*m.b23
                        + 72*m.b14*m.b24 + 1472*m.b15*m.b16 + 1256*m.b15*m.b17 + 1056*m.b15*m.b18 + 888*m.b15*m.b19 + 
                       736*m.b15*m.b20 + 584*m.b15*m.b21 + 416*m.b15*m.b22 + 280*m.b15*m.b23 + 160*m.b15*m.b24 + 72*
                       m.b15*m.b25 + 1472*m.b16*m.b17 + 1256*m.b16*m.b18 + 1056*m.b16*m.b19 + 888*m.b16*m.b20 + 736*
                       m.b16*m.b21 + 584*m.b16*m.b22 + 416*m.b16*m.b23 + 280*m.b16*m.b24 + 160*m.b16*m.b25 + 72*m.b16*
                       m.b26 + 1472*m.b17*m.b18 + 1256*m.b17*m.b19 + 1056*m.b17*m.b20 + 888*m.b17*m.b21 + 736*m.b17*
                       m.b22 + 584*m.b17*m.b23 + 416*m.b17*m.b24 + 280*m.b17*m.b25 + 160*m.b17*m.b26 + 72*m.b17*m.b27 + 
                       1472*m.b18*m.b19 + 1256*m.b18*m.b20 + 1056*m.b18*m.b21 + 888*m.b18*m.b22 + 736*m.b18*m.b23 + 584*
                       m.b18*m.b24 + 416*m.b18*m.b25 + 280*m.b18*m.b26 + 160*m.b18*m.b27 + 72*m.b18*m.b28 + 1472*m.b19*
                       m.b20 + 1256*m.b19*m.b21 + 1056*m.b19*m.b22 + 888*m.b19*m.b23 + 736*m.b19*m.b24 + 584*m.b19*m.b25
                        + 416*m.b19*m.b26 + 280*m.b19*m.b27 + 160*m.b19*m.b28 + 72*m.b19*m.b29 + 1472*m.b20*m.b21 + 1256
                       *m.b20*m.b22 + 1056*m.b20*m.b23 + 888*m.b20*m.b24 + 736*m.b20*m.b25 + 584*m.b20*m.b26 + 416*m.b20
                       *m.b27 + 280*m.b20*m.b28 + 160*m.b20*m.b29 + 72*m.b20*m.b30 + 1472*m.b21*m.b22 + 1256*m.b21*m.b23
                        + 1056*m.b21*m.b24 + 888*m.b21*m.b25 + 736*m.b21*m.b26 + 584*m.b21*m.b27 + 416*m.b21*m.b28 + 280
                       *m.b21*m.b29 + 160*m.b21*m.b30 + 72*m.b21*m.b31 + 1472*m.b22*m.b23 + 1256*m.b22*m.b24 + 1056*
                       m.b22*m.b25 + 888*m.b22*m.b26 + 736*m.b22*m.b27 + 584*m.b22*m.b28 + 416*m.b22*m.b29 + 280*m.b22*
                       m.b30 + 160*m.b22*m.b31 + 72*m.b22*m.b32 + 1472*m.b23*m.b24 + 1256*m.b23*m.b25 + 1056*m.b23*m.b26
                        + 888*m.b23*m.b27 + 736*m.b23*m.b28 + 584*m.b23*m.b29 + 416*m.b23*m.b30 + 280*m.b23*m.b31 + 160*
                       m.b23*m.b32 + 72*m.b23*m.b33 + 1472*m.b24*m.b25 + 1256*m.b24*m.b26 + 1056*m.b24*m.b27 + 888*m.b24
                       *m.b28 + 736*m.b24*m.b29 + 584*m.b24*m.b30 + 416*m.b24*m.b31 + 280*m.b24*m.b32 + 160*m.b24*m.b33
                        + 72*m.b24*m.b34 + 1472*m.b25*m.b26 + 1256*m.b25*m.b27 + 1056*m.b25*m.b28 + 888*m.b25*m.b29 + 
                       736*m.b25*m.b30 + 584*m.b25*m.b31 + 416*m.b25*m.b32 + 280*m.b25*m.b33 + 160*m.b25*m.b34 + 72*
                       m.b25*m.b35 + 1472*m.b26*m.b27 + 1256*m.b26*m.b28 + 1056*m.b26*m.b29 + 888*m.b26*m.b30 + 736*
                       m.b26*m.b31 + 584*m.b26*m.b32 + 416*m.b26*m.b33 + 280*m.b26*m.b34 + 160*m.b26*m.b35 + 72*m.b26*
                       m.b36 + 1472*m.b27*m.b28 + 1256*m.b27*m.b29 + 1056*m.b27*m.b30 + 888*m.b27*m.b31 + 736*m.b27*
                       m.b32 + 584*m.b27*m.b33 + 416*m.b27*m.b34 + 280*m.b27*m.b35 + 160*m.b27*m.b36 + 72*m.b27*m.b37 + 
                       1472*m.b28*m.b29 + 1256*m.b28*m.b30 + 1056*m.b28*m.b31 + 888*m.b28*m.b32 + 736*m.b28*m.b33 + 584*
                       m.b28*m.b34 + 416*m.b28*m.b35 + 280*m.b28*m.b36 + 160*m.b28*m.b37 + 72*m.b28*m.b38 + 1472*m.b29*
                       m.b30 + 1256*m.b29*m.b31 + 1056*m.b29*m.b32 + 888*m.b29*m.b33 + 736*m.b29*m.b34 + 584*m.b29*m.b35
                        + 416*m.b29*m.b36 + 280*m.b29*m.b37 + 160*m.b29*m.b38 + 72*m.b29*m.b39 + 1472*m.b30*m.b31 + 1256
                       *m.b30*m.b32 + 1056*m.b30*m.b33 + 888*m.b30*m.b34 + 736*m.b30*m.b35 + 584*m.b30*m.b36 + 416*m.b30
                       *m.b37 + 280*m.b30*m.b38 + 160*m.b30*m.b39 + 72*m.b30*m.b40 + 1472*m.b31*m.b32 + 1256*m.b31*m.b33
                        + 1056*m.b31*m.b34 + 888*m.b31*m.b35 + 736*m.b31*m.b36 + 584*m.b31*m.b37 + 416*m.b31*m.b38 + 280
                       *m.b31*m.b39 + 160*m.b31*m.b40 + 72*m.b31*m.b41 + 1472*m.b32*m.b33 + 1256*m.b32*m.b34 + 1056*
                       m.b32*m.b35 + 888*m.b32*m.b36 + 736*m.b32*m.b37 + 584*m.b32*m.b38 + 416*m.b32*m.b39 + 280*m.b32*
                       m.b40 + 160*m.b32*m.b41 + 72*m.b32*m.b42 + 1472*m.b33*m.b34 + 1256*m.b33*m.b35 + 1056*m.b33*m.b36
                        + 888*m.b33*m.b37 + 736*m.b33*m.b38 + 584*m.b33*m.b39 + 416*m.b33*m.b40 + 280*m.b33*m.b41 + 160*
                       m.b33*m.b42 + 72*m.b33*m.b43 + 1472*m.b34*m.b35 + 1256*m.b34*m.b36 + 1056*m.b34*m.b37 + 888*m.b34
                       *m.b38 + 736*m.b34*m.b39 + 584*m.b34*m.b40 + 416*m.b34*m.b41 + 280*m.b34*m.b42 + 160*m.b34*m.b43
                        + 72*m.b34*m.b44 + 1472*m.b35*m.b36 + 1256*m.b35*m.b37 + 1056*m.b35*m.b38 + 888*m.b35*m.b39 + 
                       736*m.b35*m.b40 + 584*m.b35*m.b41 + 416*m.b35*m.b42 + 280*m.b35*m.b43 + 160*m.b35*m.b44 + 72*
                       m.b35*m.b45 + 1344*m.b36*m.b37 + 1136*m.b36*m.b38 + 944*m.b36*m.b39 + 784*m.b36*m.b40 + 640*m.b36
                       *m.b41 + 480*m.b36*m.b42 + 320*m.b36*m.b43 + 192*m.b36*m.b44 + 80*m.b36*m.b45 + 1216*m.b37*m.b38
                        + 1000*m.b37*m.b39 + 816*m.b37*m.b40 + 664*m.b37*m.b41 + 512*m.b37*m.b42 + 360*m.b37*m.b43 + 208
                       *m.b37*m.b44 + 88*m.b37*m.b45 + 1072*m.b38*m.b39 + 864*m.b38*m.b40 + 672*m.b38*m.b41 + 528*m.b38*
                       m.b42 + 368*m.b38*m.b43 + 224*m.b38*m.b44 + 96*m.b38*m.b45 + 912*m.b39*m.b40 + 712*m.b39*m.b41 + 
                       528*m.b39*m.b42 + 360*m.b39*m.b43 + 224*m.b39*m.b44 + 104*m.b39*m.b45 + 736*m.b40*m.b41 + 544*
                       m.b40*m.b42 + 384*m.b40*m.b43 + 224*m.b40*m.b44 + 96*m.b40*m.b45 + 560*m.b41*m.b42 + 392*m.b41*
                       m.b43 + 240*m.b41*m.b44 + 104*m.b41*m.b45 + 400*m.b42*m.b43 + 256*m.b42*m.b44 + 112*m.b42*m.b45
                        + 256*m.b43*m.b44 + 120*m.b43*m.b45 + 128*m.b44*m.b45 - 180*m.b1 - 388*m.b2 - 616*m.b3 - 856*
                       m.b4 - 1100*m.b5 - 1340*m.b6 - 1584*m.b7 - 1824*m.b8 - 2052*m.b9 - 2260*m.b10 - 2440*m.b11 - 2440
                       *m.b12 - 2440*m.b13 - 2440*m.b14 - 2440*m.b15 - 2440*m.b16 - 2440*m.b17 - 2440*m.b18 - 2440*m.b19
                        - 2440*m.b20 - 2440*m.b21 - 2440*m.b22 - 2440*m.b23 - 2440*m.b24 - 2440*m.b25 - 2440*m.b26 - 
                       2440*m.b27 - 2440*m.b28 - 2440*m.b29 - 2440*m.b30 - 2440*m.b31 - 2440*m.b32 - 2440*m.b33 - 2440*
                       m.b34 - 2440*m.b35 - 2260*m.b36 - 2052*m.b37 - 1824*m.b38 - 1584*m.b39 - 1340*m.b40 - 1100*m.b41
                        - 856*m.b42 - 616*m.b43 - 388*m.b44 - 180*m.b45 - m.x46 <= 0)
