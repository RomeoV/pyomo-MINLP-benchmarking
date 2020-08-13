#  MINLP written by GAMS Convert at 08/13/20 17:37:53
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         56        1       55        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         56        1       55        0


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
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x56, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*
                       m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*m.b12 + 64*m.b1*m.b3*m.b11*
                       m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4
                       *m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*
                       m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*m.b1*m.b5*m.b8*
                       m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*
                       m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b7*m.b8*m.b14 + 128*m.b2*m.b3*m.b4*m.b5 + 
                       128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*
                       m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 128*m.b2*m.b3*m.b10*m.b11 + 128*m.b2*m.b3*m.b11*m.b12 + 128*
                       m.b2*m.b3*m.b12*m.b13 + 128*m.b2*m.b3*m.b13*m.b14 + 64*m.b2*m.b3*m.b14*m.b15 + 128*m.b2*m.b4*m.b5
                       *m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*
                       m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*
                       m.b14 + 64*m.b2*m.b4*m.b13*m.b15 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10 + 128*m.b2*
                       m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 128*m.b2*m.b5*m.b11*
                       m.b14 + 64*m.b2*m.b5*m.b12*m.b15 + 128*m.b2*m.b6*m.b7*m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2
                       *m.b6*m.b9*m.b13 + 128*m.b2*m.b6*m.b10*m.b14 + 64*m.b2*m.b6*m.b11*m.b15 + 128*m.b2*m.b7*m.b8*
                       m.b13 + 128*m.b2*m.b7*m.b9*m.b14 + 64*m.b2*m.b7*m.b10*m.b15 + 64*m.b2*m.b8*m.b9*m.b15 + 192*m.b3*
                       m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 
                       192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*m.b4*m.b10*m.b11 + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*
                       m.b12*m.b13 + 192*m.b3*m.b4*m.b13*m.b14 + 128*m.b3*m.b4*m.b14*m.b15 + 64*m.b3*m.b4*m.b15*m.b16 + 
                       192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9
                       *m.b11 + 192*m.b3*m.b5*m.b10*m.b12 + 192*m.b3*m.b5*m.b11*m.b13 + 192*m.b3*m.b5*m.b12*m.b14 + 128*
                       m.b3*m.b5*m.b13*m.b15 + 64*m.b3*m.b5*m.b14*m.b16 + 192*m.b3*m.b6*m.b7*m.b10 + 192*m.b3*m.b6*m.b8*
                       m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13 + 192*m.b3*m.b6*m.b11*m.b14 + 128*
                       m.b3*m.b6*m.b12*m.b15 + 64*m.b3*m.b6*m.b13*m.b16 + 192*m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*
                       m.b13 + 192*m.b3*m.b7*m.b10*m.b14 + 128*m.b3*m.b7*m.b11*m.b15 + 64*m.b3*m.b7*m.b12*m.b16 + 192*
                       m.b3*m.b8*m.b9*m.b14 + 128*m.b3*m.b8*m.b10*m.b15 + 64*m.b3*m.b8*m.b11*m.b16 + 64*m.b3*m.b9*m.b10*
                       m.b16 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4*m.b5*m.b8*m.b9 + 256*m.b4*
                       m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*m.b12 + 256*m.b4*m.b5*m.b12*
                       m.b13 + 256*m.b4*m.b5*m.b13*m.b14 + 192*m.b4*m.b5*m.b14*m.b15 + 128*m.b4*m.b5*m.b15*m.b16 + 64*
                       m.b4*m.b5*m.b16*m.b17 + 256*m.b4*m.b6*m.b7*m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*
                       m.b11 + 256*m.b4*m.b6*m.b10*m.b12 + 256*m.b4*m.b6*m.b11*m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 192*
                       m.b4*m.b6*m.b13*m.b15 + 128*m.b4*m.b6*m.b14*m.b16 + 64*m.b4*m.b6*m.b15*m.b17 + 256*m.b4*m.b7*m.b8
                       *m.b11 + 256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7*m.b10*m.b13 + 256*m.b4*m.b7*m.b11*m.b14 + 192*
                       m.b4*m.b7*m.b12*m.b15 + 128*m.b4*m.b7*m.b13*m.b16 + 64*m.b4*m.b7*m.b14*m.b17 + 256*m.b4*m.b8*m.b9
                       *m.b13 + 256*m.b4*m.b8*m.b10*m.b14 + 192*m.b4*m.b8*m.b11*m.b15 + 128*m.b4*m.b8*m.b12*m.b16 + 64*
                       m.b4*m.b8*m.b13*m.b17 + 192*m.b4*m.b9*m.b10*m.b15 + 128*m.b4*m.b9*m.b11*m.b16 + 64*m.b4*m.b9*
                       m.b12*m.b17 + 64*m.b4*m.b10*m.b11*m.b17 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 320
                       *m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*m.b5*m.b6*
                       m.b12*m.b13 + 320*m.b5*m.b6*m.b13*m.b14 + 256*m.b5*m.b6*m.b14*m.b15 + 192*m.b5*m.b6*m.b15*m.b16
                        + 128*m.b5*m.b6*m.b16*m.b17 + 64*m.b5*m.b6*m.b17*m.b18 + 320*m.b5*m.b7*m.b8*m.b10 + 320*m.b5*
                       m.b7*m.b9*m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*m.b13 + 320*m.b5*m.b7*m.b12*
                       m.b14 + 256*m.b5*m.b7*m.b13*m.b15 + 192*m.b5*m.b7*m.b14*m.b16 + 128*m.b5*m.b7*m.b15*m.b17 + 64*
                       m.b5*m.b7*m.b16*m.b18 + 320*m.b5*m.b8*m.b9*m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*m.b5*m.b8*
                       m.b11*m.b14 + 256*m.b5*m.b8*m.b12*m.b15 + 192*m.b5*m.b8*m.b13*m.b16 + 128*m.b5*m.b8*m.b14*m.b17
                        + 64*m.b5*m.b8*m.b15*m.b18 + 320*m.b5*m.b9*m.b10*m.b14 + 256*m.b5*m.b9*m.b11*m.b15 + 192*m.b5*
                       m.b9*m.b12*m.b16 + 128*m.b5*m.b9*m.b13*m.b17 + 64*m.b5*m.b9*m.b14*m.b18 + 192*m.b5*m.b10*m.b11*
                       m.b16 + 128*m.b5*m.b10*m.b12*m.b17 + 64*m.b5*m.b10*m.b13*m.b18 + 64*m.b5*m.b11*m.b12*m.b18 + 384*
                       m.b6*m.b7*m.b8*m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*
                       m.b12 + 384*m.b6*m.b7*m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 320*m.b6*m.b7*m.b14*m.b15 + 256*
                       m.b6*m.b7*m.b15*m.b16 + 192*m.b6*m.b7*m.b16*m.b17 + 128*m.b6*m.b7*m.b17*m.b18 + 64*m.b6*m.b7*
                       m.b18*m.b19 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*m.b13 + 
                       384*m.b6*m.b8*m.b12*m.b14 + 320*m.b6*m.b8*m.b13*m.b15 + 256*m.b6*m.b8*m.b14*m.b16 + 192*m.b6*m.b8
                       *m.b15*m.b17 + 128*m.b6*m.b8*m.b16*m.b18 + 64*m.b6*m.b8*m.b17*m.b19 + 384*m.b6*m.b9*m.b10*m.b13
                        + 384*m.b6*m.b9*m.b11*m.b14 + 320*m.b6*m.b9*m.b12*m.b15 + 256*m.b6*m.b9*m.b13*m.b16 + 192*m.b6*
                       m.b9*m.b14*m.b17 + 128*m.b6*m.b9*m.b15*m.b18 + 64*m.b6*m.b9*m.b16*m.b19 + 320*m.b6*m.b10*m.b11*
                       m.b15 + 256*m.b6*m.b10*m.b12*m.b16 + 192*m.b6*m.b10*m.b13*m.b17 + 128*m.b6*m.b10*m.b14*m.b18 + 64
                       *m.b6*m.b10*m.b15*m.b19 + 192*m.b6*m.b11*m.b12*m.b17 + 128*m.b6*m.b11*m.b13*m.b18 + 64*m.b6*m.b11
                       *m.b14*m.b19 + 64*m.b6*m.b12*m.b13*m.b19 + 448*m.b7*m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11
                        + 448*m.b7*m.b8*m.b11*m.b12 + 448*m.b7*m.b8*m.b12*m.b13 + 448*m.b7*m.b8*m.b13*m.b14 + 384*m.b7*
                       m.b8*m.b14*m.b15 + 320*m.b7*m.b8*m.b15*m.b16 + 256*m.b7*m.b8*m.b16*m.b17 + 192*m.b7*m.b8*m.b17*
                       m.b18 + 128*m.b7*m.b8*m.b18*m.b19 + 64*m.b7*m.b8*m.b19*m.b20 + 448*m.b7*m.b9*m.b10*m.b12 + 448*
                       m.b7*m.b9*m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 384*m.b7*m.b9*m.b13*m.b15 + 320*m.b7*m.b9*
                       m.b14*m.b16 + 256*m.b7*m.b9*m.b15*m.b17 + 192*m.b7*m.b9*m.b16*m.b18 + 128*m.b7*m.b9*m.b17*m.b19
                        + 64*m.b7*m.b9*m.b18*m.b20 + 448*m.b7*m.b10*m.b11*m.b14 + 384*m.b7*m.b10*m.b12*m.b15 + 320*m.b7*
                       m.b10*m.b13*m.b16 + 256*m.b7*m.b10*m.b14*m.b17 + 192*m.b7*m.b10*m.b15*m.b18 + 128*m.b7*m.b10*
                       m.b16*m.b19 + 64*m.b7*m.b10*m.b17*m.b20 + 320*m.b7*m.b11*m.b12*m.b16 + 256*m.b7*m.b11*m.b13*m.b17
                        + 192*m.b7*m.b11*m.b14*m.b18 + 128*m.b7*m.b11*m.b15*m.b19 + 64*m.b7*m.b11*m.b16*m.b20 + 192*m.b7
                       *m.b12*m.b13*m.b18 + 128*m.b7*m.b12*m.b14*m.b19 + 64*m.b7*m.b12*m.b15*m.b20 + 64*m.b7*m.b13*m.b14
                       *m.b20 + 512*m.b8*m.b9*m.b10*m.b11 + 512*m.b8*m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*m.b13 + 512*
                       m.b8*m.b9*m.b13*m.b14 + 448*m.b8*m.b9*m.b14*m.b15 + 384*m.b8*m.b9*m.b15*m.b16 + 320*m.b8*m.b9*
                       m.b16*m.b17 + 256*m.b8*m.b9*m.b17*m.b18 + 192*m.b8*m.b9*m.b18*m.b19 + 128*m.b8*m.b9*m.b19*m.b20
                        + 64*m.b8*m.b9*m.b20*m.b21 + 512*m.b8*m.b10*m.b11*m.b13 + 512*m.b8*m.b10*m.b12*m.b14 + 448*m.b8*
                       m.b10*m.b13*m.b15 + 384*m.b8*m.b10*m.b14*m.b16 + 320*m.b8*m.b10*m.b15*m.b17 + 256*m.b8*m.b10*
                       m.b16*m.b18 + 192*m.b8*m.b10*m.b17*m.b19 + 128*m.b8*m.b10*m.b18*m.b20 + 64*m.b8*m.b10*m.b19*m.b21
                        + 448*m.b8*m.b11*m.b12*m.b15 + 384*m.b8*m.b11*m.b13*m.b16 + 320*m.b8*m.b11*m.b14*m.b17 + 256*
                       m.b8*m.b11*m.b15*m.b18 + 192*m.b8*m.b11*m.b16*m.b19 + 128*m.b8*m.b11*m.b17*m.b20 + 64*m.b8*m.b11*
                       m.b18*m.b21 + 320*m.b8*m.b12*m.b13*m.b17 + 256*m.b8*m.b12*m.b14*m.b18 + 192*m.b8*m.b12*m.b15*
                       m.b19 + 128*m.b8*m.b12*m.b16*m.b20 + 64*m.b8*m.b12*m.b17*m.b21 + 192*m.b8*m.b13*m.b14*m.b19 + 128
                       *m.b8*m.b13*m.b15*m.b20 + 64*m.b8*m.b13*m.b16*m.b21 + 64*m.b8*m.b14*m.b15*m.b21 + 576*m.b9*m.b10*
                       m.b11*m.b12 + 576*m.b9*m.b10*m.b12*m.b13 + 576*m.b9*m.b10*m.b13*m.b14 + 512*m.b9*m.b10*m.b14*
                       m.b15 + 448*m.b9*m.b10*m.b15*m.b16 + 384*m.b9*m.b10*m.b16*m.b17 + 320*m.b9*m.b10*m.b17*m.b18 + 
                       256*m.b9*m.b10*m.b18*m.b19 + 192*m.b9*m.b10*m.b19*m.b20 + 128*m.b9*m.b10*m.b20*m.b21 + 64*m.b9*
                       m.b10*m.b21*m.b22 + 576*m.b9*m.b11*m.b12*m.b14 + 512*m.b9*m.b11*m.b13*m.b15 + 448*m.b9*m.b11*
                       m.b14*m.b16 + 384*m.b9*m.b11*m.b15*m.b17 + 320*m.b9*m.b11*m.b16*m.b18 + 256*m.b9*m.b11*m.b17*
                       m.b19 + 192*m.b9*m.b11*m.b18*m.b20 + 128*m.b9*m.b11*m.b19*m.b21 + 64*m.b9*m.b11*m.b20*m.b22 + 448
                       *m.b9*m.b12*m.b13*m.b16 + 384*m.b9*m.b12*m.b14*m.b17 + 320*m.b9*m.b12*m.b15*m.b18 + 256*m.b9*
                       m.b12*m.b16*m.b19 + 192*m.b9*m.b12*m.b17*m.b20 + 128*m.b9*m.b12*m.b18*m.b21 + 64*m.b9*m.b12*m.b19
                       *m.b22 + 320*m.b9*m.b13*m.b14*m.b18 + 256*m.b9*m.b13*m.b15*m.b19 + 192*m.b9*m.b13*m.b16*m.b20 + 
                       128*m.b9*m.b13*m.b17*m.b21 + 64*m.b9*m.b13*m.b18*m.b22 + 192*m.b9*m.b14*m.b15*m.b20 + 128*m.b9*
                       m.b14*m.b16*m.b21 + 64*m.b9*m.b14*m.b17*m.b22 + 64*m.b9*m.b15*m.b16*m.b22 + 640*m.b10*m.b11*m.b12
                       *m.b13 + 640*m.b10*m.b11*m.b13*m.b14 + 576*m.b10*m.b11*m.b14*m.b15 + 512*m.b10*m.b11*m.b15*m.b16
                        + 448*m.b10*m.b11*m.b16*m.b17 + 384*m.b10*m.b11*m.b17*m.b18 + 320*m.b10*m.b11*m.b18*m.b19 + 256*
                       m.b10*m.b11*m.b19*m.b20 + 192*m.b10*m.b11*m.b20*m.b21 + 128*m.b10*m.b11*m.b21*m.b22 + 64*m.b10*
                       m.b11*m.b22*m.b23 + 576*m.b10*m.b12*m.b13*m.b15 + 512*m.b10*m.b12*m.b14*m.b16 + 448*m.b10*m.b12*
                       m.b15*m.b17 + 384*m.b10*m.b12*m.b16*m.b18 + 320*m.b10*m.b12*m.b17*m.b19 + 256*m.b10*m.b12*m.b18*
                       m.b20 + 192*m.b10*m.b12*m.b19*m.b21 + 128*m.b10*m.b12*m.b20*m.b22 + 64*m.b10*m.b12*m.b21*m.b23 + 
                       448*m.b10*m.b13*m.b14*m.b17 + 384*m.b10*m.b13*m.b15*m.b18 + 320*m.b10*m.b13*m.b16*m.b19 + 256*
                       m.b10*m.b13*m.b17*m.b20 + 192*m.b10*m.b13*m.b18*m.b21 + 128*m.b10*m.b13*m.b19*m.b22 + 64*m.b10*
                       m.b13*m.b20*m.b23 + 320*m.b10*m.b14*m.b15*m.b19 + 256*m.b10*m.b14*m.b16*m.b20 + 192*m.b10*m.b14*
                       m.b17*m.b21 + 128*m.b10*m.b14*m.b18*m.b22 + 64*m.b10*m.b14*m.b19*m.b23 + 192*m.b10*m.b15*m.b16*
                       m.b21 + 128*m.b10*m.b15*m.b17*m.b22 + 64*m.b10*m.b15*m.b18*m.b23 + 64*m.b10*m.b16*m.b17*m.b23 + 
                       704*m.b11*m.b12*m.b13*m.b14 + 640*m.b11*m.b12*m.b14*m.b15 + 576*m.b11*m.b12*m.b15*m.b16 + 512*
                       m.b11*m.b12*m.b16*m.b17 + 448*m.b11*m.b12*m.b17*m.b18 + 384*m.b11*m.b12*m.b18*m.b19 + 320*m.b11*
                       m.b12*m.b19*m.b20 + 256*m.b11*m.b12*m.b20*m.b21 + 192*m.b11*m.b12*m.b21*m.b22 + 128*m.b11*m.b12*
                       m.b22*m.b23 + 64*m.b11*m.b12*m.b23*m.b24 + 576*m.b11*m.b13*m.b14*m.b16 + 512*m.b11*m.b13*m.b15*
                       m.b17 + 448*m.b11*m.b13*m.b16*m.b18 + 384*m.b11*m.b13*m.b17*m.b19 + 320*m.b11*m.b13*m.b18*m.b20
                        + 256*m.b11*m.b13*m.b19*m.b21 + 192*m.b11*m.b13*m.b20*m.b22 + 128*m.b11*m.b13*m.b21*m.b23 + 64*
                       m.b11*m.b13*m.b22*m.b24 + 448*m.b11*m.b14*m.b15*m.b18 + 384*m.b11*m.b14*m.b16*m.b19 + 320*m.b11*
                       m.b14*m.b17*m.b20 + 256*m.b11*m.b14*m.b18*m.b21 + 192*m.b11*m.b14*m.b19*m.b22 + 128*m.b11*m.b14*
                       m.b20*m.b23 + 64*m.b11*m.b14*m.b21*m.b24 + 320*m.b11*m.b15*m.b16*m.b20 + 256*m.b11*m.b15*m.b17*
                       m.b21 + 192*m.b11*m.b15*m.b18*m.b22 + 128*m.b11*m.b15*m.b19*m.b23 + 64*m.b11*m.b15*m.b20*m.b24 + 
                       192*m.b11*m.b16*m.b17*m.b22 + 128*m.b11*m.b16*m.b18*m.b23 + 64*m.b11*m.b16*m.b19*m.b24 + 64*m.b11
                       *m.b17*m.b18*m.b24 + 704*m.b12*m.b13*m.b14*m.b15 + 640*m.b12*m.b13*m.b15*m.b16 + 576*m.b12*m.b13*
                       m.b16*m.b17 + 512*m.b12*m.b13*m.b17*m.b18 + 448*m.b12*m.b13*m.b18*m.b19 + 384*m.b12*m.b13*m.b19*
                       m.b20 + 320*m.b12*m.b13*m.b20*m.b21 + 256*m.b12*m.b13*m.b21*m.b22 + 192*m.b12*m.b13*m.b22*m.b23
                        + 128*m.b12*m.b13*m.b23*m.b24 + 64*m.b12*m.b13*m.b24*m.b25 + 576*m.b12*m.b14*m.b15*m.b17 + 512*
                       m.b12*m.b14*m.b16*m.b18 + 448*m.b12*m.b14*m.b17*m.b19 + 384*m.b12*m.b14*m.b18*m.b20 + 320*m.b12*
                       m.b14*m.b19*m.b21 + 256*m.b12*m.b14*m.b20*m.b22 + 192*m.b12*m.b14*m.b21*m.b23 + 128*m.b12*m.b14*
                       m.b22*m.b24 + 64*m.b12*m.b14*m.b23*m.b25 + 448*m.b12*m.b15*m.b16*m.b19 + 384*m.b12*m.b15*m.b17*
                       m.b20 + 320*m.b12*m.b15*m.b18*m.b21 + 256*m.b12*m.b15*m.b19*m.b22 + 192*m.b12*m.b15*m.b20*m.b23
                        + 128*m.b12*m.b15*m.b21*m.b24 + 64*m.b12*m.b15*m.b22*m.b25 + 320*m.b12*m.b16*m.b17*m.b21 + 256*
                       m.b12*m.b16*m.b18*m.b22 + 192*m.b12*m.b16*m.b19*m.b23 + 128*m.b12*m.b16*m.b20*m.b24 + 64*m.b12*
                       m.b16*m.b21*m.b25 + 192*m.b12*m.b17*m.b18*m.b23 + 128*m.b12*m.b17*m.b19*m.b24 + 64*m.b12*m.b17*
                       m.b20*m.b25 + 64*m.b12*m.b18*m.b19*m.b25 + 704*m.b13*m.b14*m.b15*m.b16 + 640*m.b13*m.b14*m.b16*
                       m.b17 + 576*m.b13*m.b14*m.b17*m.b18 + 512*m.b13*m.b14*m.b18*m.b19 + 448*m.b13*m.b14*m.b19*m.b20
                        + 384*m.b13*m.b14*m.b20*m.b21 + 320*m.b13*m.b14*m.b21*m.b22 + 256*m.b13*m.b14*m.b22*m.b23 + 192*
                       m.b13*m.b14*m.b23*m.b24 + 128*m.b13*m.b14*m.b24*m.b25 + 64*m.b13*m.b14*m.b25*m.b26 + 576*m.b13*
                       m.b15*m.b16*m.b18 + 512*m.b13*m.b15*m.b17*m.b19 + 448*m.b13*m.b15*m.b18*m.b20 + 384*m.b13*m.b15*
                       m.b19*m.b21 + 320*m.b13*m.b15*m.b20*m.b22 + 256*m.b13*m.b15*m.b21*m.b23 + 192*m.b13*m.b15*m.b22*
                       m.b24 + 128*m.b13*m.b15*m.b23*m.b25 + 64*m.b13*m.b15*m.b24*m.b26 + 448*m.b13*m.b16*m.b17*m.b20 + 
                       384*m.b13*m.b16*m.b18*m.b21 + 320*m.b13*m.b16*m.b19*m.b22 + 256*m.b13*m.b16*m.b20*m.b23 + 192*
                       m.b13*m.b16*m.b21*m.b24 + 128*m.b13*m.b16*m.b22*m.b25 + 64*m.b13*m.b16*m.b23*m.b26 + 320*m.b13*
                       m.b17*m.b18*m.b22 + 256*m.b13*m.b17*m.b19*m.b23 + 192*m.b13*m.b17*m.b20*m.b24 + 128*m.b13*m.b17*
                       m.b21*m.b25 + 64*m.b13*m.b17*m.b22*m.b26 + 192*m.b13*m.b18*m.b19*m.b24 + 128*m.b13*m.b18*m.b20*
                       m.b25 + 64*m.b13*m.b18*m.b21*m.b26 + 64*m.b13*m.b19*m.b20*m.b26 + 704*m.b14*m.b15*m.b16*m.b17 + 
                       640*m.b14*m.b15*m.b17*m.b18 + 576*m.b14*m.b15*m.b18*m.b19 + 512*m.b14*m.b15*m.b19*m.b20 + 448*
                       m.b14*m.b15*m.b20*m.b21 + 384*m.b14*m.b15*m.b21*m.b22 + 320*m.b14*m.b15*m.b22*m.b23 + 256*m.b14*
                       m.b15*m.b23*m.b24 + 192*m.b14*m.b15*m.b24*m.b25 + 128*m.b14*m.b15*m.b25*m.b26 + 64*m.b14*m.b15*
                       m.b26*m.b27 + 576*m.b14*m.b16*m.b17*m.b19 + 512*m.b14*m.b16*m.b18*m.b20 + 448*m.b14*m.b16*m.b19*
                       m.b21 + 384*m.b14*m.b16*m.b20*m.b22 + 320*m.b14*m.b16*m.b21*m.b23 + 256*m.b14*m.b16*m.b22*m.b24
                        + 192*m.b14*m.b16*m.b23*m.b25 + 128*m.b14*m.b16*m.b24*m.b26 + 64*m.b14*m.b16*m.b25*m.b27 + 448*
                       m.b14*m.b17*m.b18*m.b21 + 384*m.b14*m.b17*m.b19*m.b22 + 320*m.b14*m.b17*m.b20*m.b23 + 256*m.b14*
                       m.b17*m.b21*m.b24 + 192*m.b14*m.b17*m.b22*m.b25 + 128*m.b14*m.b17*m.b23*m.b26 + 64*m.b14*m.b17*
                       m.b24*m.b27 + 320*m.b14*m.b18*m.b19*m.b23 + 256*m.b14*m.b18*m.b20*m.b24 + 192*m.b14*m.b18*m.b21*
                       m.b25 + 128*m.b14*m.b18*m.b22*m.b26 + 64*m.b14*m.b18*m.b23*m.b27 + 192*m.b14*m.b19*m.b20*m.b25 + 
                       128*m.b14*m.b19*m.b21*m.b26 + 64*m.b14*m.b19*m.b22*m.b27 + 64*m.b14*m.b20*m.b21*m.b27 + 704*m.b15
                       *m.b16*m.b17*m.b18 + 640*m.b15*m.b16*m.b18*m.b19 + 576*m.b15*m.b16*m.b19*m.b20 + 512*m.b15*m.b16*
                       m.b20*m.b21 + 448*m.b15*m.b16*m.b21*m.b22 + 384*m.b15*m.b16*m.b22*m.b23 + 320*m.b15*m.b16*m.b23*
                       m.b24 + 256*m.b15*m.b16*m.b24*m.b25 + 192*m.b15*m.b16*m.b25*m.b26 + 128*m.b15*m.b16*m.b26*m.b27
                        + 64*m.b15*m.b16*m.b27*m.b28 + 576*m.b15*m.b17*m.b18*m.b20 + 512*m.b15*m.b17*m.b19*m.b21 + 448*
                       m.b15*m.b17*m.b20*m.b22 + 384*m.b15*m.b17*m.b21*m.b23 + 320*m.b15*m.b17*m.b22*m.b24 + 256*m.b15*
                       m.b17*m.b23*m.b25 + 192*m.b15*m.b17*m.b24*m.b26 + 128*m.b15*m.b17*m.b25*m.b27 + 64*m.b15*m.b17*
                       m.b26*m.b28 + 448*m.b15*m.b18*m.b19*m.b22 + 384*m.b15*m.b18*m.b20*m.b23 + 320*m.b15*m.b18*m.b21*
                       m.b24 + 256*m.b15*m.b18*m.b22*m.b25 + 192*m.b15*m.b18*m.b23*m.b26 + 128*m.b15*m.b18*m.b24*m.b27
                        + 64*m.b15*m.b18*m.b25*m.b28 + 320*m.b15*m.b19*m.b20*m.b24 + 256*m.b15*m.b19*m.b21*m.b25 + 192*
                       m.b15*m.b19*m.b22*m.b26 + 128*m.b15*m.b19*m.b23*m.b27 + 64*m.b15*m.b19*m.b24*m.b28 + 192*m.b15*
                       m.b20*m.b21*m.b26 + 128*m.b15*m.b20*m.b22*m.b27 + 64*m.b15*m.b20*m.b23*m.b28 + 64*m.b15*m.b21*
                       m.b22*m.b28 + 704*m.b16*m.b17*m.b18*m.b19 + 640*m.b16*m.b17*m.b19*m.b20 + 576*m.b16*m.b17*m.b20*
                       m.b21 + 512*m.b16*m.b17*m.b21*m.b22 + 448*m.b16*m.b17*m.b22*m.b23 + 384*m.b16*m.b17*m.b23*m.b24
                        + 320*m.b16*m.b17*m.b24*m.b25 + 256*m.b16*m.b17*m.b25*m.b26 + 192*m.b16*m.b17*m.b26*m.b27 + 128*
                       m.b16*m.b17*m.b27*m.b28 + 64*m.b16*m.b17*m.b28*m.b29 + 576*m.b16*m.b18*m.b19*m.b21 + 512*m.b16*
                       m.b18*m.b20*m.b22 + 448*m.b16*m.b18*m.b21*m.b23 + 384*m.b16*m.b18*m.b22*m.b24 + 320*m.b16*m.b18*
                       m.b23*m.b25 + 256*m.b16*m.b18*m.b24*m.b26 + 192*m.b16*m.b18*m.b25*m.b27 + 128*m.b16*m.b18*m.b26*
                       m.b28 + 64*m.b16*m.b18*m.b27*m.b29 + 448*m.b16*m.b19*m.b20*m.b23 + 384*m.b16*m.b19*m.b21*m.b24 + 
                       320*m.b16*m.b19*m.b22*m.b25 + 256*m.b16*m.b19*m.b23*m.b26 + 192*m.b16*m.b19*m.b24*m.b27 + 128*
                       m.b16*m.b19*m.b25*m.b28 + 64*m.b16*m.b19*m.b26*m.b29 + 320*m.b16*m.b20*m.b21*m.b25 + 256*m.b16*
                       m.b20*m.b22*m.b26 + 192*m.b16*m.b20*m.b23*m.b27 + 128*m.b16*m.b20*m.b24*m.b28 + 64*m.b16*m.b20*
                       m.b25*m.b29 + 192*m.b16*m.b21*m.b22*m.b27 + 128*m.b16*m.b21*m.b23*m.b28 + 64*m.b16*m.b21*m.b24*
                       m.b29 + 64*m.b16*m.b22*m.b23*m.b29 + 704*m.b17*m.b18*m.b19*m.b20 + 640*m.b17*m.b18*m.b20*m.b21 + 
                       576*m.b17*m.b18*m.b21*m.b22 + 512*m.b17*m.b18*m.b22*m.b23 + 448*m.b17*m.b18*m.b23*m.b24 + 384*
                       m.b17*m.b18*m.b24*m.b25 + 320*m.b17*m.b18*m.b25*m.b26 + 256*m.b17*m.b18*m.b26*m.b27 + 192*m.b17*
                       m.b18*m.b27*m.b28 + 128*m.b17*m.b18*m.b28*m.b29 + 64*m.b17*m.b18*m.b29*m.b30 + 576*m.b17*m.b19*
                       m.b20*m.b22 + 512*m.b17*m.b19*m.b21*m.b23 + 448*m.b17*m.b19*m.b22*m.b24 + 384*m.b17*m.b19*m.b23*
                       m.b25 + 320*m.b17*m.b19*m.b24*m.b26 + 256*m.b17*m.b19*m.b25*m.b27 + 192*m.b17*m.b19*m.b26*m.b28
                        + 128*m.b17*m.b19*m.b27*m.b29 + 64*m.b17*m.b19*m.b28*m.b30 + 448*m.b17*m.b20*m.b21*m.b24 + 384*
                       m.b17*m.b20*m.b22*m.b25 + 320*m.b17*m.b20*m.b23*m.b26 + 256*m.b17*m.b20*m.b24*m.b27 + 192*m.b17*
                       m.b20*m.b25*m.b28 + 128*m.b17*m.b20*m.b26*m.b29 + 64*m.b17*m.b20*m.b27*m.b30 + 320*m.b17*m.b21*
                       m.b22*m.b26 + 256*m.b17*m.b21*m.b23*m.b27 + 192*m.b17*m.b21*m.b24*m.b28 + 128*m.b17*m.b21*m.b25*
                       m.b29 + 64*m.b17*m.b21*m.b26*m.b30 + 192*m.b17*m.b22*m.b23*m.b28 + 128*m.b17*m.b22*m.b24*m.b29 + 
                       64*m.b17*m.b22*m.b25*m.b30 + 64*m.b17*m.b23*m.b24*m.b30 + 704*m.b18*m.b19*m.b20*m.b21 + 640*m.b18
                       *m.b19*m.b21*m.b22 + 576*m.b18*m.b19*m.b22*m.b23 + 512*m.b18*m.b19*m.b23*m.b24 + 448*m.b18*m.b19*
                       m.b24*m.b25 + 384*m.b18*m.b19*m.b25*m.b26 + 320*m.b18*m.b19*m.b26*m.b27 + 256*m.b18*m.b19*m.b27*
                       m.b28 + 192*m.b18*m.b19*m.b28*m.b29 + 128*m.b18*m.b19*m.b29*m.b30 + 64*m.b18*m.b19*m.b30*m.b31 + 
                       576*m.b18*m.b20*m.b21*m.b23 + 512*m.b18*m.b20*m.b22*m.b24 + 448*m.b18*m.b20*m.b23*m.b25 + 384*
                       m.b18*m.b20*m.b24*m.b26 + 320*m.b18*m.b20*m.b25*m.b27 + 256*m.b18*m.b20*m.b26*m.b28 + 192*m.b18*
                       m.b20*m.b27*m.b29 + 128*m.b18*m.b20*m.b28*m.b30 + 64*m.b18*m.b20*m.b29*m.b31 + 448*m.b18*m.b21*
                       m.b22*m.b25 + 384*m.b18*m.b21*m.b23*m.b26 + 320*m.b18*m.b21*m.b24*m.b27 + 256*m.b18*m.b21*m.b25*
                       m.b28 + 192*m.b18*m.b21*m.b26*m.b29 + 128*m.b18*m.b21*m.b27*m.b30 + 64*m.b18*m.b21*m.b28*m.b31 + 
                       320*m.b18*m.b22*m.b23*m.b27 + 256*m.b18*m.b22*m.b24*m.b28 + 192*m.b18*m.b22*m.b25*m.b29 + 128*
                       m.b18*m.b22*m.b26*m.b30 + 64*m.b18*m.b22*m.b27*m.b31 + 192*m.b18*m.b23*m.b24*m.b29 + 128*m.b18*
                       m.b23*m.b25*m.b30 + 64*m.b18*m.b23*m.b26*m.b31 + 64*m.b18*m.b24*m.b25*m.b31 + 704*m.b19*m.b20*
                       m.b21*m.b22 + 640*m.b19*m.b20*m.b22*m.b23 + 576*m.b19*m.b20*m.b23*m.b24 + 512*m.b19*m.b20*m.b24*
                       m.b25 + 448*m.b19*m.b20*m.b25*m.b26 + 384*m.b19*m.b20*m.b26*m.b27 + 320*m.b19*m.b20*m.b27*m.b28
                        + 256*m.b19*m.b20*m.b28*m.b29 + 192*m.b19*m.b20*m.b29*m.b30 + 128*m.b19*m.b20*m.b30*m.b31 + 64*
                       m.b19*m.b20*m.b31*m.b32 + 576*m.b19*m.b21*m.b22*m.b24 + 512*m.b19*m.b21*m.b23*m.b25 + 448*m.b19*
                       m.b21*m.b24*m.b26 + 384*m.b19*m.b21*m.b25*m.b27 + 320*m.b19*m.b21*m.b26*m.b28 + 256*m.b19*m.b21*
                       m.b27*m.b29 + 192*m.b19*m.b21*m.b28*m.b30 + 128*m.b19*m.b21*m.b29*m.b31 + 64*m.b19*m.b21*m.b30*
                       m.b32 + 448*m.b19*m.b22*m.b23*m.b26 + 384*m.b19*m.b22*m.b24*m.b27 + 320*m.b19*m.b22*m.b25*m.b28
                        + 256*m.b19*m.b22*m.b26*m.b29 + 192*m.b19*m.b22*m.b27*m.b30 + 128*m.b19*m.b22*m.b28*m.b31 + 64*
                       m.b19*m.b22*m.b29*m.b32 + 320*m.b19*m.b23*m.b24*m.b28 + 256*m.b19*m.b23*m.b25*m.b29 + 192*m.b19*
                       m.b23*m.b26*m.b30 + 128*m.b19*m.b23*m.b27*m.b31 + 64*m.b19*m.b23*m.b28*m.b32 + 192*m.b19*m.b24*
                       m.b25*m.b30 + 128*m.b19*m.b24*m.b26*m.b31 + 64*m.b19*m.b24*m.b27*m.b32 + 64*m.b19*m.b25*m.b26*
                       m.b32 + 704*m.b20*m.b21*m.b22*m.b23 + 640*m.b20*m.b21*m.b23*m.b24 + 576*m.b20*m.b21*m.b24*m.b25
                        + 512*m.b20*m.b21*m.b25*m.b26 + 448*m.b20*m.b21*m.b26*m.b27 + 384*m.b20*m.b21*m.b27*m.b28 + 320*
                       m.b20*m.b21*m.b28*m.b29 + 256*m.b20*m.b21*m.b29*m.b30 + 192*m.b20*m.b21*m.b30*m.b31 + 128*m.b20*
                       m.b21*m.b31*m.b32 + 64*m.b20*m.b21*m.b32*m.b33 + 576*m.b20*m.b22*m.b23*m.b25 + 512*m.b20*m.b22*
                       m.b24*m.b26 + 448*m.b20*m.b22*m.b25*m.b27 + 384*m.b20*m.b22*m.b26*m.b28 + 320*m.b20*m.b22*m.b27*
                       m.b29 + 256*m.b20*m.b22*m.b28*m.b30 + 192*m.b20*m.b22*m.b29*m.b31 + 128*m.b20*m.b22*m.b30*m.b32
                        + 64*m.b20*m.b22*m.b31*m.b33 + 448*m.b20*m.b23*m.b24*m.b27 + 384*m.b20*m.b23*m.b25*m.b28 + 320*
                       m.b20*m.b23*m.b26*m.b29 + 256*m.b20*m.b23*m.b27*m.b30 + 192*m.b20*m.b23*m.b28*m.b31 + 128*m.b20*
                       m.b23*m.b29*m.b32 + 64*m.b20*m.b23*m.b30*m.b33 + 320*m.b20*m.b24*m.b25*m.b29 + 256*m.b20*m.b24*
                       m.b26*m.b30 + 192*m.b20*m.b24*m.b27*m.b31 + 128*m.b20*m.b24*m.b28*m.b32 + 64*m.b20*m.b24*m.b29*
                       m.b33 + 192*m.b20*m.b25*m.b26*m.b31 + 128*m.b20*m.b25*m.b27*m.b32 + 64*m.b20*m.b25*m.b28*m.b33 + 
                       64*m.b20*m.b26*m.b27*m.b33 + 704*m.b21*m.b22*m.b23*m.b24 + 640*m.b21*m.b22*m.b24*m.b25 + 576*
                       m.b21*m.b22*m.b25*m.b26 + 512*m.b21*m.b22*m.b26*m.b27 + 448*m.b21*m.b22*m.b27*m.b28 + 384*m.b21*
                       m.b22*m.b28*m.b29 + 320*m.b21*m.b22*m.b29*m.b30 + 256*m.b21*m.b22*m.b30*m.b31 + 192*m.b21*m.b22*
                       m.b31*m.b32 + 128*m.b21*m.b22*m.b32*m.b33 + 64*m.b21*m.b22*m.b33*m.b34 + 576*m.b21*m.b23*m.b24*
                       m.b26 + 512*m.b21*m.b23*m.b25*m.b27 + 448*m.b21*m.b23*m.b26*m.b28 + 384*m.b21*m.b23*m.b27*m.b29
                        + 320*m.b21*m.b23*m.b28*m.b30 + 256*m.b21*m.b23*m.b29*m.b31 + 192*m.b21*m.b23*m.b30*m.b32 + 128*
                       m.b21*m.b23*m.b31*m.b33 + 64*m.b21*m.b23*m.b32*m.b34 + 448*m.b21*m.b24*m.b25*m.b28 + 384*m.b21*
                       m.b24*m.b26*m.b29 + 320*m.b21*m.b24*m.b27*m.b30 + 256*m.b21*m.b24*m.b28*m.b31 + 192*m.b21*m.b24*
                       m.b29*m.b32 + 128*m.b21*m.b24*m.b30*m.b33 + 64*m.b21*m.b24*m.b31*m.b34 + 320*m.b21*m.b25*m.b26*
                       m.b30 + 256*m.b21*m.b25*m.b27*m.b31 + 192*m.b21*m.b25*m.b28*m.b32 + 128*m.b21*m.b25*m.b29*m.b33
                        + 64*m.b21*m.b25*m.b30*m.b34 + 192*m.b21*m.b26*m.b27*m.b32 + 128*m.b21*m.b26*m.b28*m.b33 + 64*
                       m.b21*m.b26*m.b29*m.b34 + 64*m.b21*m.b27*m.b28*m.b34 + 704*m.b22*m.b23*m.b24*m.b25 + 640*m.b22*
                       m.b23*m.b25*m.b26 + 576*m.b22*m.b23*m.b26*m.b27 + 512*m.b22*m.b23*m.b27*m.b28 + 448*m.b22*m.b23*
                       m.b28*m.b29 + 384*m.b22*m.b23*m.b29*m.b30 + 320*m.b22*m.b23*m.b30*m.b31 + 256*m.b22*m.b23*m.b31*
                       m.b32 + 192*m.b22*m.b23*m.b32*m.b33 + 128*m.b22*m.b23*m.b33*m.b34 + 64*m.b22*m.b23*m.b34*m.b35 + 
                       576*m.b22*m.b24*m.b25*m.b27 + 512*m.b22*m.b24*m.b26*m.b28 + 448*m.b22*m.b24*m.b27*m.b29 + 384*
                       m.b22*m.b24*m.b28*m.b30 + 320*m.b22*m.b24*m.b29*m.b31 + 256*m.b22*m.b24*m.b30*m.b32 + 192*m.b22*
                       m.b24*m.b31*m.b33 + 128*m.b22*m.b24*m.b32*m.b34 + 64*m.b22*m.b24*m.b33*m.b35 + 448*m.b22*m.b25*
                       m.b26*m.b29 + 384*m.b22*m.b25*m.b27*m.b30 + 320*m.b22*m.b25*m.b28*m.b31 + 256*m.b22*m.b25*m.b29*
                       m.b32 + 192*m.b22*m.b25*m.b30*m.b33 + 128*m.b22*m.b25*m.b31*m.b34 + 64*m.b22*m.b25*m.b32*m.b35 + 
                       320*m.b22*m.b26*m.b27*m.b31 + 256*m.b22*m.b26*m.b28*m.b32 + 192*m.b22*m.b26*m.b29*m.b33 + 128*
                       m.b22*m.b26*m.b30*m.b34 + 64*m.b22*m.b26*m.b31*m.b35 + 192*m.b22*m.b27*m.b28*m.b33 + 128*m.b22*
                       m.b27*m.b29*m.b34 + 64*m.b22*m.b27*m.b30*m.b35 + 64*m.b22*m.b28*m.b29*m.b35 + 704*m.b23*m.b24*
                       m.b25*m.b26 + 640*m.b23*m.b24*m.b26*m.b27 + 576*m.b23*m.b24*m.b27*m.b28 + 512*m.b23*m.b24*m.b28*
                       m.b29 + 448*m.b23*m.b24*m.b29*m.b30 + 384*m.b23*m.b24*m.b30*m.b31 + 320*m.b23*m.b24*m.b31*m.b32
                        + 256*m.b23*m.b24*m.b32*m.b33 + 192*m.b23*m.b24*m.b33*m.b34 + 128*m.b23*m.b24*m.b34*m.b35 + 64*
                       m.b23*m.b24*m.b35*m.b36 + 576*m.b23*m.b25*m.b26*m.b28 + 512*m.b23*m.b25*m.b27*m.b29 + 448*m.b23*
                       m.b25*m.b28*m.b30 + 384*m.b23*m.b25*m.b29*m.b31 + 320*m.b23*m.b25*m.b30*m.b32 + 256*m.b23*m.b25*
                       m.b31*m.b33 + 192*m.b23*m.b25*m.b32*m.b34 + 128*m.b23*m.b25*m.b33*m.b35 + 64*m.b23*m.b25*m.b34*
                       m.b36 + 448*m.b23*m.b26*m.b27*m.b30 + 384*m.b23*m.b26*m.b28*m.b31 + 320*m.b23*m.b26*m.b29*m.b32
                        + 256*m.b23*m.b26*m.b30*m.b33 + 192*m.b23*m.b26*m.b31*m.b34 + 128*m.b23*m.b26*m.b32*m.b35 + 64*
                       m.b23*m.b26*m.b33*m.b36 + 320*m.b23*m.b27*m.b28*m.b32 + 256*m.b23*m.b27*m.b29*m.b33 + 192*m.b23*
                       m.b27*m.b30*m.b34 + 128*m.b23*m.b27*m.b31*m.b35 + 64*m.b23*m.b27*m.b32*m.b36 + 192*m.b23*m.b28*
                       m.b29*m.b34 + 128*m.b23*m.b28*m.b30*m.b35 + 64*m.b23*m.b28*m.b31*m.b36 + 64*m.b23*m.b29*m.b30*
                       m.b36 + 704*m.b24*m.b25*m.b26*m.b27 + 640*m.b24*m.b25*m.b27*m.b28 + 576*m.b24*m.b25*m.b28*m.b29
                        + 512*m.b24*m.b25*m.b29*m.b30 + 448*m.b24*m.b25*m.b30*m.b31 + 384*m.b24*m.b25*m.b31*m.b32 + 320*
                       m.b24*m.b25*m.b32*m.b33 + 256*m.b24*m.b25*m.b33*m.b34 + 192*m.b24*m.b25*m.b34*m.b35 + 128*m.b24*
                       m.b25*m.b35*m.b36 + 64*m.b24*m.b25*m.b36*m.b37 + 576*m.b24*m.b26*m.b27*m.b29 + 512*m.b24*m.b26*
                       m.b28*m.b30 + 448*m.b24*m.b26*m.b29*m.b31 + 384*m.b24*m.b26*m.b30*m.b32 + 320*m.b24*m.b26*m.b31*
                       m.b33 + 256*m.b24*m.b26*m.b32*m.b34 + 192*m.b24*m.b26*m.b33*m.b35 + 128*m.b24*m.b26*m.b34*m.b36
                        + 64*m.b24*m.b26*m.b35*m.b37 + 448*m.b24*m.b27*m.b28*m.b31 + 384*m.b24*m.b27*m.b29*m.b32 + 320*
                       m.b24*m.b27*m.b30*m.b33 + 256*m.b24*m.b27*m.b31*m.b34 + 192*m.b24*m.b27*m.b32*m.b35 + 128*m.b24*
                       m.b27*m.b33*m.b36 + 64*m.b24*m.b27*m.b34*m.b37 + 320*m.b24*m.b28*m.b29*m.b33 + 256*m.b24*m.b28*
                       m.b30*m.b34 + 192*m.b24*m.b28*m.b31*m.b35 + 128*m.b24*m.b28*m.b32*m.b36 + 64*m.b24*m.b28*m.b33*
                       m.b37 + 192*m.b24*m.b29*m.b30*m.b35 + 128*m.b24*m.b29*m.b31*m.b36 + 64*m.b24*m.b29*m.b32*m.b37 + 
                       64*m.b24*m.b30*m.b31*m.b37 + 704*m.b25*m.b26*m.b27*m.b28 + 640*m.b25*m.b26*m.b28*m.b29 + 576*
                       m.b25*m.b26*m.b29*m.b30 + 512*m.b25*m.b26*m.b30*m.b31 + 448*m.b25*m.b26*m.b31*m.b32 + 384*m.b25*
                       m.b26*m.b32*m.b33 + 320*m.b25*m.b26*m.b33*m.b34 + 256*m.b25*m.b26*m.b34*m.b35 + 192*m.b25*m.b26*
                       m.b35*m.b36 + 128*m.b25*m.b26*m.b36*m.b37 + 64*m.b25*m.b26*m.b37*m.b38 + 576*m.b25*m.b27*m.b28*
                       m.b30 + 512*m.b25*m.b27*m.b29*m.b31 + 448*m.b25*m.b27*m.b30*m.b32 + 384*m.b25*m.b27*m.b31*m.b33
                        + 320*m.b25*m.b27*m.b32*m.b34 + 256*m.b25*m.b27*m.b33*m.b35 + 192*m.b25*m.b27*m.b34*m.b36 + 128*
                       m.b25*m.b27*m.b35*m.b37 + 64*m.b25*m.b27*m.b36*m.b38 + 448*m.b25*m.b28*m.b29*m.b32 + 384*m.b25*
                       m.b28*m.b30*m.b33 + 320*m.b25*m.b28*m.b31*m.b34 + 256*m.b25*m.b28*m.b32*m.b35 + 192*m.b25*m.b28*
                       m.b33*m.b36 + 128*m.b25*m.b28*m.b34*m.b37 + 64*m.b25*m.b28*m.b35*m.b38 + 320*m.b25*m.b29*m.b30*
                       m.b34 + 256*m.b25*m.b29*m.b31*m.b35 + 192*m.b25*m.b29*m.b32*m.b36 + 128*m.b25*m.b29*m.b33*m.b37
                        + 64*m.b25*m.b29*m.b34*m.b38 + 192*m.b25*m.b30*m.b31*m.b36 + 128*m.b25*m.b30*m.b32*m.b37 + 64*
                       m.b25*m.b30*m.b33*m.b38 + 64*m.b25*m.b31*m.b32*m.b38 + 704*m.b26*m.b27*m.b28*m.b29 + 640*m.b26*
                       m.b27*m.b29*m.b30 + 576*m.b26*m.b27*m.b30*m.b31 + 512*m.b26*m.b27*m.b31*m.b32 + 448*m.b26*m.b27*
                       m.b32*m.b33 + 384*m.b26*m.b27*m.b33*m.b34 + 320*m.b26*m.b27*m.b34*m.b35 + 256*m.b26*m.b27*m.b35*
                       m.b36 + 192*m.b26*m.b27*m.b36*m.b37 + 128*m.b26*m.b27*m.b37*m.b38 + 64*m.b26*m.b27*m.b38*m.b39 + 
                       576*m.b26*m.b28*m.b29*m.b31 + 512*m.b26*m.b28*m.b30*m.b32 + 448*m.b26*m.b28*m.b31*m.b33 + 384*
                       m.b26*m.b28*m.b32*m.b34 + 320*m.b26*m.b28*m.b33*m.b35 + 256*m.b26*m.b28*m.b34*m.b36 + 192*m.b26*
                       m.b28*m.b35*m.b37 + 128*m.b26*m.b28*m.b36*m.b38 + 64*m.b26*m.b28*m.b37*m.b39 + 448*m.b26*m.b29*
                       m.b30*m.b33 + 384*m.b26*m.b29*m.b31*m.b34 + 320*m.b26*m.b29*m.b32*m.b35 + 256*m.b26*m.b29*m.b33*
                       m.b36 + 192*m.b26*m.b29*m.b34*m.b37 + 128*m.b26*m.b29*m.b35*m.b38 + 64*m.b26*m.b29*m.b36*m.b39 + 
                       320*m.b26*m.b30*m.b31*m.b35 + 256*m.b26*m.b30*m.b32*m.b36 + 192*m.b26*m.b30*m.b33*m.b37 + 128*
                       m.b26*m.b30*m.b34*m.b38 + 64*m.b26*m.b30*m.b35*m.b39 + 192*m.b26*m.b31*m.b32*m.b37 + 128*m.b26*
                       m.b31*m.b33*m.b38 + 64*m.b26*m.b31*m.b34*m.b39 + 64*m.b26*m.b32*m.b33*m.b39 + 704*m.b27*m.b28*
                       m.b29*m.b30 + 640*m.b27*m.b28*m.b30*m.b31 + 576*m.b27*m.b28*m.b31*m.b32 + 512*m.b27*m.b28*m.b32*
                       m.b33 + 448*m.b27*m.b28*m.b33*m.b34 + 384*m.b27*m.b28*m.b34*m.b35 + 320*m.b27*m.b28*m.b35*m.b36
                        + 256*m.b27*m.b28*m.b36*m.b37 + 192*m.b27*m.b28*m.b37*m.b38 + 128*m.b27*m.b28*m.b38*m.b39 + 64*
                       m.b27*m.b28*m.b39*m.b40 + 576*m.b27*m.b29*m.b30*m.b32 + 512*m.b27*m.b29*m.b31*m.b33 + 448*m.b27*
                       m.b29*m.b32*m.b34 + 384*m.b27*m.b29*m.b33*m.b35 + 320*m.b27*m.b29*m.b34*m.b36 + 256*m.b27*m.b29*
                       m.b35*m.b37 + 192*m.b27*m.b29*m.b36*m.b38 + 128*m.b27*m.b29*m.b37*m.b39 + 64*m.b27*m.b29*m.b38*
                       m.b40 + 448*m.b27*m.b30*m.b31*m.b34 + 384*m.b27*m.b30*m.b32*m.b35 + 320*m.b27*m.b30*m.b33*m.b36
                        + 256*m.b27*m.b30*m.b34*m.b37 + 192*m.b27*m.b30*m.b35*m.b38 + 128*m.b27*m.b30*m.b36*m.b39 + 64*
                       m.b27*m.b30*m.b37*m.b40 + 320*m.b27*m.b31*m.b32*m.b36 + 256*m.b27*m.b31*m.b33*m.b37 + 192*m.b27*
                       m.b31*m.b34*m.b38 + 128*m.b27*m.b31*m.b35*m.b39 + 64*m.b27*m.b31*m.b36*m.b40 + 192*m.b27*m.b32*
                       m.b33*m.b38 + 128*m.b27*m.b32*m.b34*m.b39 + 64*m.b27*m.b32*m.b35*m.b40 + 64*m.b27*m.b33*m.b34*
                       m.b40 + 704*m.b28*m.b29*m.b30*m.b31 + 640*m.b28*m.b29*m.b31*m.b32 + 576*m.b28*m.b29*m.b32*m.b33
                        + 512*m.b28*m.b29*m.b33*m.b34 + 448*m.b28*m.b29*m.b34*m.b35 + 384*m.b28*m.b29*m.b35*m.b36 + 320*
                       m.b28*m.b29*m.b36*m.b37 + 256*m.b28*m.b29*m.b37*m.b38 + 192*m.b28*m.b29*m.b38*m.b39 + 128*m.b28*
                       m.b29*m.b39*m.b40 + 64*m.b28*m.b29*m.b40*m.b41 + 576*m.b28*m.b30*m.b31*m.b33 + 512*m.b28*m.b30*
                       m.b32*m.b34 + 448*m.b28*m.b30*m.b33*m.b35 + 384*m.b28*m.b30*m.b34*m.b36 + 320*m.b28*m.b30*m.b35*
                       m.b37 + 256*m.b28*m.b30*m.b36*m.b38 + 192*m.b28*m.b30*m.b37*m.b39 + 128*m.b28*m.b30*m.b38*m.b40
                        + 64*m.b28*m.b30*m.b39*m.b41 + 448*m.b28*m.b31*m.b32*m.b35 + 384*m.b28*m.b31*m.b33*m.b36 + 320*
                       m.b28*m.b31*m.b34*m.b37 + 256*m.b28*m.b31*m.b35*m.b38 + 192*m.b28*m.b31*m.b36*m.b39 + 128*m.b28*
                       m.b31*m.b37*m.b40 + 64*m.b28*m.b31*m.b38*m.b41 + 320*m.b28*m.b32*m.b33*m.b37 + 256*m.b28*m.b32*
                       m.b34*m.b38 + 192*m.b28*m.b32*m.b35*m.b39 + 128*m.b28*m.b32*m.b36*m.b40 + 64*m.b28*m.b32*m.b37*
                       m.b41 + 192*m.b28*m.b33*m.b34*m.b39 + 128*m.b28*m.b33*m.b35*m.b40 + 64*m.b28*m.b33*m.b36*m.b41 + 
                       64*m.b28*m.b34*m.b35*m.b41 + 704*m.b29*m.b30*m.b31*m.b32 + 640*m.b29*m.b30*m.b32*m.b33 + 576*
                       m.b29*m.b30*m.b33*m.b34 + 512*m.b29*m.b30*m.b34*m.b35 + 448*m.b29*m.b30*m.b35*m.b36 + 384*m.b29*
                       m.b30*m.b36*m.b37 + 320*m.b29*m.b30*m.b37*m.b38 + 256*m.b29*m.b30*m.b38*m.b39 + 192*m.b29*m.b30*
                       m.b39*m.b40 + 128*m.b29*m.b30*m.b40*m.b41 + 64*m.b29*m.b30*m.b41*m.b42 + 576*m.b29*m.b31*m.b32*
                       m.b34 + 512*m.b29*m.b31*m.b33*m.b35 + 448*m.b29*m.b31*m.b34*m.b36 + 384*m.b29*m.b31*m.b35*m.b37
                        + 320*m.b29*m.b31*m.b36*m.b38 + 256*m.b29*m.b31*m.b37*m.b39 + 192*m.b29*m.b31*m.b38*m.b40 + 128*
                       m.b29*m.b31*m.b39*m.b41 + 64*m.b29*m.b31*m.b40*m.b42 + 448*m.b29*m.b32*m.b33*m.b36 + 384*m.b29*
                       m.b32*m.b34*m.b37 + 320*m.b29*m.b32*m.b35*m.b38 + 256*m.b29*m.b32*m.b36*m.b39 + 192*m.b29*m.b32*
                       m.b37*m.b40 + 128*m.b29*m.b32*m.b38*m.b41 + 64*m.b29*m.b32*m.b39*m.b42 + 320*m.b29*m.b33*m.b34*
                       m.b38 + 256*m.b29*m.b33*m.b35*m.b39 + 192*m.b29*m.b33*m.b36*m.b40 + 128*m.b29*m.b33*m.b37*m.b41
                        + 64*m.b29*m.b33*m.b38*m.b42 + 192*m.b29*m.b34*m.b35*m.b40 + 128*m.b29*m.b34*m.b36*m.b41 + 64*
                       m.b29*m.b34*m.b37*m.b42 + 64*m.b29*m.b35*m.b36*m.b42 + 704*m.b30*m.b31*m.b32*m.b33 + 640*m.b30*
                       m.b31*m.b33*m.b34 + 576*m.b30*m.b31*m.b34*m.b35 + 512*m.b30*m.b31*m.b35*m.b36 + 448*m.b30*m.b31*
                       m.b36*m.b37 + 384*m.b30*m.b31*m.b37*m.b38 + 320*m.b30*m.b31*m.b38*m.b39 + 256*m.b30*m.b31*m.b39*
                       m.b40 + 192*m.b30*m.b31*m.b40*m.b41 + 128*m.b30*m.b31*m.b41*m.b42 + 64*m.b30*m.b31*m.b42*m.b43 + 
                       576*m.b30*m.b32*m.b33*m.b35 + 512*m.b30*m.b32*m.b34*m.b36 + 448*m.b30*m.b32*m.b35*m.b37 + 384*
                       m.b30*m.b32*m.b36*m.b38 + 320*m.b30*m.b32*m.b37*m.b39 + 256*m.b30*m.b32*m.b38*m.b40 + 192*m.b30*
                       m.b32*m.b39*m.b41 + 128*m.b30*m.b32*m.b40*m.b42 + 64*m.b30*m.b32*m.b41*m.b43 + 448*m.b30*m.b33*
                       m.b34*m.b37 + 384*m.b30*m.b33*m.b35*m.b38 + 320*m.b30*m.b33*m.b36*m.b39 + 256*m.b30*m.b33*m.b37*
                       m.b40 + 192*m.b30*m.b33*m.b38*m.b41 + 128*m.b30*m.b33*m.b39*m.b42 + 64*m.b30*m.b33*m.b40*m.b43 + 
                       320*m.b30*m.b34*m.b35*m.b39 + 256*m.b30*m.b34*m.b36*m.b40 + 192*m.b30*m.b34*m.b37*m.b41 + 128*
                       m.b30*m.b34*m.b38*m.b42 + 64*m.b30*m.b34*m.b39*m.b43 + 192*m.b30*m.b35*m.b36*m.b41 + 128*m.b30*
                       m.b35*m.b37*m.b42 + 64*m.b30*m.b35*m.b38*m.b43 + 64*m.b30*m.b36*m.b37*m.b43 + 704*m.b31*m.b32*
                       m.b33*m.b34 + 640*m.b31*m.b32*m.b34*m.b35 + 576*m.b31*m.b32*m.b35*m.b36 + 512*m.b31*m.b32*m.b36*
                       m.b37 + 448*m.b31*m.b32*m.b37*m.b38 + 384*m.b31*m.b32*m.b38*m.b39 + 320*m.b31*m.b32*m.b39*m.b40
                        + 256*m.b31*m.b32*m.b40*m.b41 + 192*m.b31*m.b32*m.b41*m.b42 + 128*m.b31*m.b32*m.b42*m.b43 + 64*
                       m.b31*m.b32*m.b43*m.b44 + 576*m.b31*m.b33*m.b34*m.b36 + 512*m.b31*m.b33*m.b35*m.b37 + 448*m.b31*
                       m.b33*m.b36*m.b38 + 384*m.b31*m.b33*m.b37*m.b39 + 320*m.b31*m.b33*m.b38*m.b40 + 256*m.b31*m.b33*
                       m.b39*m.b41 + 192*m.b31*m.b33*m.b40*m.b42 + 128*m.b31*m.b33*m.b41*m.b43 + 64*m.b31*m.b33*m.b42*
                       m.b44 + 448*m.b31*m.b34*m.b35*m.b38 + 384*m.b31*m.b34*m.b36*m.b39 + 320*m.b31*m.b34*m.b37*m.b40
                        + 256*m.b31*m.b34*m.b38*m.b41 + 192*m.b31*m.b34*m.b39*m.b42 + 128*m.b31*m.b34*m.b40*m.b43 + 64*
                       m.b31*m.b34*m.b41*m.b44 + 320*m.b31*m.b35*m.b36*m.b40 + 256*m.b31*m.b35*m.b37*m.b41 + 192*m.b31*
                       m.b35*m.b38*m.b42 + 128*m.b31*m.b35*m.b39*m.b43 + 64*m.b31*m.b35*m.b40*m.b44 + 192*m.b31*m.b36*
                       m.b37*m.b42 + 128*m.b31*m.b36*m.b38*m.b43 + 64*m.b31*m.b36*m.b39*m.b44 + 64*m.b31*m.b37*m.b38*
                       m.b44 + 704*m.b32*m.b33*m.b34*m.b35 + 640*m.b32*m.b33*m.b35*m.b36 + 576*m.b32*m.b33*m.b36*m.b37
                        + 512*m.b32*m.b33*m.b37*m.b38 + 448*m.b32*m.b33*m.b38*m.b39 + 384*m.b32*m.b33*m.b39*m.b40 + 320*
                       m.b32*m.b33*m.b40*m.b41 + 256*m.b32*m.b33*m.b41*m.b42 + 192*m.b32*m.b33*m.b42*m.b43 + 128*m.b32*
                       m.b33*m.b43*m.b44 + 64*m.b32*m.b33*m.b44*m.b45 + 576*m.b32*m.b34*m.b35*m.b37 + 512*m.b32*m.b34*
                       m.b36*m.b38 + 448*m.b32*m.b34*m.b37*m.b39 + 384*m.b32*m.b34*m.b38*m.b40 + 320*m.b32*m.b34*m.b39*
                       m.b41 + 256*m.b32*m.b34*m.b40*m.b42 + 192*m.b32*m.b34*m.b41*m.b43 + 128*m.b32*m.b34*m.b42*m.b44
                        + 64*m.b32*m.b34*m.b43*m.b45 + 448*m.b32*m.b35*m.b36*m.b39 + 384*m.b32*m.b35*m.b37*m.b40 + 320*
                       m.b32*m.b35*m.b38*m.b41 + 256*m.b32*m.b35*m.b39*m.b42 + 192*m.b32*m.b35*m.b40*m.b43 + 128*m.b32*
                       m.b35*m.b41*m.b44 + 64*m.b32*m.b35*m.b42*m.b45 + 320*m.b32*m.b36*m.b37*m.b41 + 256*m.b32*m.b36*
                       m.b38*m.b42 + 192*m.b32*m.b36*m.b39*m.b43 + 128*m.b32*m.b36*m.b40*m.b44 + 64*m.b32*m.b36*m.b41*
                       m.b45 + 192*m.b32*m.b37*m.b38*m.b43 + 128*m.b32*m.b37*m.b39*m.b44 + 64*m.b32*m.b37*m.b40*m.b45 + 
                       64*m.b32*m.b38*m.b39*m.b45 + 704*m.b33*m.b34*m.b35*m.b36 + 640*m.b33*m.b34*m.b36*m.b37 + 576*
                       m.b33*m.b34*m.b37*m.b38 + 512*m.b33*m.b34*m.b38*m.b39 + 448*m.b33*m.b34*m.b39*m.b40 + 384*m.b33*
                       m.b34*m.b40*m.b41 + 320*m.b33*m.b34*m.b41*m.b42 + 256*m.b33*m.b34*m.b42*m.b43 + 192*m.b33*m.b34*
                       m.b43*m.b44 + 128*m.b33*m.b34*m.b44*m.b45 + 64*m.b33*m.b34*m.b45*m.b46 + 576*m.b33*m.b35*m.b36*
                       m.b38 + 512*m.b33*m.b35*m.b37*m.b39 + 448*m.b33*m.b35*m.b38*m.b40 + 384*m.b33*m.b35*m.b39*m.b41
                        + 320*m.b33*m.b35*m.b40*m.b42 + 256*m.b33*m.b35*m.b41*m.b43 + 192*m.b33*m.b35*m.b42*m.b44 + 128*
                       m.b33*m.b35*m.b43*m.b45 + 64*m.b33*m.b35*m.b44*m.b46 + 448*m.b33*m.b36*m.b37*m.b40 + 384*m.b33*
                       m.b36*m.b38*m.b41 + 320*m.b33*m.b36*m.b39*m.b42 + 256*m.b33*m.b36*m.b40*m.b43 + 192*m.b33*m.b36*
                       m.b41*m.b44 + 128*m.b33*m.b36*m.b42*m.b45 + 64*m.b33*m.b36*m.b43*m.b46 + 320*m.b33*m.b37*m.b38*
                       m.b42 + 256*m.b33*m.b37*m.b39*m.b43 + 192*m.b33*m.b37*m.b40*m.b44 + 128*m.b33*m.b37*m.b41*m.b45
                        + 64*m.b33*m.b37*m.b42*m.b46 + 192*m.b33*m.b38*m.b39*m.b44 + 128*m.b33*m.b38*m.b40*m.b45 + 64*
                       m.b33*m.b38*m.b41*m.b46 + 64*m.b33*m.b39*m.b40*m.b46 + 704*m.b34*m.b35*m.b36*m.b37 + 640*m.b34*
                       m.b35*m.b37*m.b38 + 576*m.b34*m.b35*m.b38*m.b39 + 512*m.b34*m.b35*m.b39*m.b40 + 448*m.b34*m.b35*
                       m.b40*m.b41 + 384*m.b34*m.b35*m.b41*m.b42 + 320*m.b34*m.b35*m.b42*m.b43 + 256*m.b34*m.b35*m.b43*
                       m.b44 + 192*m.b34*m.b35*m.b44*m.b45 + 128*m.b34*m.b35*m.b45*m.b46 + 64*m.b34*m.b35*m.b46*m.b47 + 
                       576*m.b34*m.b36*m.b37*m.b39 + 512*m.b34*m.b36*m.b38*m.b40 + 448*m.b34*m.b36*m.b39*m.b41 + 384*
                       m.b34*m.b36*m.b40*m.b42 + 320*m.b34*m.b36*m.b41*m.b43 + 256*m.b34*m.b36*m.b42*m.b44 + 192*m.b34*
                       m.b36*m.b43*m.b45 + 128*m.b34*m.b36*m.b44*m.b46 + 64*m.b34*m.b36*m.b45*m.b47 + 448*m.b34*m.b37*
                       m.b38*m.b41 + 384*m.b34*m.b37*m.b39*m.b42 + 320*m.b34*m.b37*m.b40*m.b43 + 256*m.b34*m.b37*m.b41*
                       m.b44 + 192*m.b34*m.b37*m.b42*m.b45 + 128*m.b34*m.b37*m.b43*m.b46 + 64*m.b34*m.b37*m.b44*m.b47 + 
                       320*m.b34*m.b38*m.b39*m.b43 + 256*m.b34*m.b38*m.b40*m.b44 + 192*m.b34*m.b38*m.b41*m.b45 + 128*
                       m.b34*m.b38*m.b42*m.b46 + 64*m.b34*m.b38*m.b43*m.b47 + 192*m.b34*m.b39*m.b40*m.b45 + 128*m.b34*
                       m.b39*m.b41*m.b46 + 64*m.b34*m.b39*m.b42*m.b47 + 64*m.b34*m.b40*m.b41*m.b47 + 704*m.b35*m.b36*
                       m.b37*m.b38 + 640*m.b35*m.b36*m.b38*m.b39 + 576*m.b35*m.b36*m.b39*m.b40 + 512*m.b35*m.b36*m.b40*
                       m.b41 + 448*m.b35*m.b36*m.b41*m.b42 + 384*m.b35*m.b36*m.b42*m.b43 + 320*m.b35*m.b36*m.b43*m.b44
                        + 256*m.b35*m.b36*m.b44*m.b45 + 192*m.b35*m.b36*m.b45*m.b46 + 128*m.b35*m.b36*m.b46*m.b47 + 64*
                       m.b35*m.b36*m.b47*m.b48 + 576*m.b35*m.b37*m.b38*m.b40 + 512*m.b35*m.b37*m.b39*m.b41 + 448*m.b35*
                       m.b37*m.b40*m.b42 + 384*m.b35*m.b37*m.b41*m.b43 + 320*m.b35*m.b37*m.b42*m.b44 + 256*m.b35*m.b37*
                       m.b43*m.b45 + 192*m.b35*m.b37*m.b44*m.b46 + 128*m.b35*m.b37*m.b45*m.b47 + 64*m.b35*m.b37*m.b46*
                       m.b48 + 448*m.b35*m.b38*m.b39*m.b42 + 384*m.b35*m.b38*m.b40*m.b43 + 320*m.b35*m.b38*m.b41*m.b44
                        + 256*m.b35*m.b38*m.b42*m.b45 + 192*m.b35*m.b38*m.b43*m.b46 + 128*m.b35*m.b38*m.b44*m.b47 + 64*
                       m.b35*m.b38*m.b45*m.b48 + 320*m.b35*m.b39*m.b40*m.b44 + 256*m.b35*m.b39*m.b41*m.b45 + 192*m.b35*
                       m.b39*m.b42*m.b46 + 128*m.b35*m.b39*m.b43*m.b47 + 64*m.b35*m.b39*m.b44*m.b48 + 192*m.b35*m.b40*
                       m.b41*m.b46 + 128*m.b35*m.b40*m.b42*m.b47 + 64*m.b35*m.b40*m.b43*m.b48 + 64*m.b35*m.b41*m.b42*
                       m.b48 + 704*m.b36*m.b37*m.b38*m.b39 + 640*m.b36*m.b37*m.b39*m.b40 + 576*m.b36*m.b37*m.b40*m.b41
                        + 512*m.b36*m.b37*m.b41*m.b42 + 448*m.b36*m.b37*m.b42*m.b43 + 384*m.b36*m.b37*m.b43*m.b44 + 320*
                       m.b36*m.b37*m.b44*m.b45 + 256*m.b36*m.b37*m.b45*m.b46 + 192*m.b36*m.b37*m.b46*m.b47 + 128*m.b36*
                       m.b37*m.b47*m.b48 + 64*m.b36*m.b37*m.b48*m.b49 + 576*m.b36*m.b38*m.b39*m.b41 + 512*m.b36*m.b38*
                       m.b40*m.b42 + 448*m.b36*m.b38*m.b41*m.b43 + 384*m.b36*m.b38*m.b42*m.b44 + 320*m.b36*m.b38*m.b43*
                       m.b45 + 256*m.b36*m.b38*m.b44*m.b46 + 192*m.b36*m.b38*m.b45*m.b47 + 128*m.b36*m.b38*m.b46*m.b48
                        + 64*m.b36*m.b38*m.b47*m.b49 + 448*m.b36*m.b39*m.b40*m.b43 + 384*m.b36*m.b39*m.b41*m.b44 + 320*
                       m.b36*m.b39*m.b42*m.b45 + 256*m.b36*m.b39*m.b43*m.b46 + 192*m.b36*m.b39*m.b44*m.b47 + 128*m.b36*
                       m.b39*m.b45*m.b48 + 64*m.b36*m.b39*m.b46*m.b49 + 320*m.b36*m.b40*m.b41*m.b45 + 256*m.b36*m.b40*
                       m.b42*m.b46 + 192*m.b36*m.b40*m.b43*m.b47 + 128*m.b36*m.b40*m.b44*m.b48 + 64*m.b36*m.b40*m.b45*
                       m.b49 + 192*m.b36*m.b41*m.b42*m.b47 + 128*m.b36*m.b41*m.b43*m.b48 + 64*m.b36*m.b41*m.b44*m.b49 + 
                       64*m.b36*m.b42*m.b43*m.b49 + 704*m.b37*m.b38*m.b39*m.b40 + 640*m.b37*m.b38*m.b40*m.b41 + 576*
                       m.b37*m.b38*m.b41*m.b42 + 512*m.b37*m.b38*m.b42*m.b43 + 448*m.b37*m.b38*m.b43*m.b44 + 384*m.b37*
                       m.b38*m.b44*m.b45 + 320*m.b37*m.b38*m.b45*m.b46 + 256*m.b37*m.b38*m.b46*m.b47 + 192*m.b37*m.b38*
                       m.b47*m.b48 + 128*m.b37*m.b38*m.b48*m.b49 + 64*m.b37*m.b38*m.b49*m.b50 + 576*m.b37*m.b39*m.b40*
                       m.b42 + 512*m.b37*m.b39*m.b41*m.b43 + 448*m.b37*m.b39*m.b42*m.b44 + 384*m.b37*m.b39*m.b43*m.b45
                        + 320*m.b37*m.b39*m.b44*m.b46 + 256*m.b37*m.b39*m.b45*m.b47 + 192*m.b37*m.b39*m.b46*m.b48 + 128*
                       m.b37*m.b39*m.b47*m.b49 + 64*m.b37*m.b39*m.b48*m.b50 + 448*m.b37*m.b40*m.b41*m.b44 + 384*m.b37*
                       m.b40*m.b42*m.b45 + 320*m.b37*m.b40*m.b43*m.b46 + 256*m.b37*m.b40*m.b44*m.b47 + 192*m.b37*m.b40*
                       m.b45*m.b48 + 128*m.b37*m.b40*m.b46*m.b49 + 64*m.b37*m.b40*m.b47*m.b50 + 320*m.b37*m.b41*m.b42*
                       m.b46 + 256*m.b37*m.b41*m.b43*m.b47 + 192*m.b37*m.b41*m.b44*m.b48 + 128*m.b37*m.b41*m.b45*m.b49
                        + 64*m.b37*m.b41*m.b46*m.b50 + 192*m.b37*m.b42*m.b43*m.b48 + 128*m.b37*m.b42*m.b44*m.b49 + 64*
                       m.b37*m.b42*m.b45*m.b50 + 64*m.b37*m.b43*m.b44*m.b50 + 704*m.b38*m.b39*m.b40*m.b41 + 640*m.b38*
                       m.b39*m.b41*m.b42 + 576*m.b38*m.b39*m.b42*m.b43 + 512*m.b38*m.b39*m.b43*m.b44 + 448*m.b38*m.b39*
                       m.b44*m.b45 + 384*m.b38*m.b39*m.b45*m.b46 + 320*m.b38*m.b39*m.b46*m.b47 + 256*m.b38*m.b39*m.b47*
                       m.b48 + 192*m.b38*m.b39*m.b48*m.b49 + 128*m.b38*m.b39*m.b49*m.b50 + 64*m.b38*m.b39*m.b50*m.b51 + 
                       576*m.b38*m.b40*m.b41*m.b43 + 512*m.b38*m.b40*m.b42*m.b44 + 448*m.b38*m.b40*m.b43*m.b45 + 384*
                       m.b38*m.b40*m.b44*m.b46 + 320*m.b38*m.b40*m.b45*m.b47 + 256*m.b38*m.b40*m.b46*m.b48 + 192*m.b38*
                       m.b40*m.b47*m.b49 + 128*m.b38*m.b40*m.b48*m.b50 + 64*m.b38*m.b40*m.b49*m.b51 + 448*m.b38*m.b41*
                       m.b42*m.b45 + 384*m.b38*m.b41*m.b43*m.b46 + 320*m.b38*m.b41*m.b44*m.b47 + 256*m.b38*m.b41*m.b45*
                       m.b48 + 192*m.b38*m.b41*m.b46*m.b49 + 128*m.b38*m.b41*m.b47*m.b50 + 64*m.b38*m.b41*m.b48*m.b51 + 
                       320*m.b38*m.b42*m.b43*m.b47 + 256*m.b38*m.b42*m.b44*m.b48 + 192*m.b38*m.b42*m.b45*m.b49 + 128*
                       m.b38*m.b42*m.b46*m.b50 + 64*m.b38*m.b42*m.b47*m.b51 + 192*m.b38*m.b43*m.b44*m.b49 + 128*m.b38*
                       m.b43*m.b45*m.b50 + 64*m.b38*m.b43*m.b46*m.b51 + 64*m.b38*m.b44*m.b45*m.b51 + 704*m.b39*m.b40*
                       m.b41*m.b42 + 640*m.b39*m.b40*m.b42*m.b43 + 576*m.b39*m.b40*m.b43*m.b44 + 512*m.b39*m.b40*m.b44*
                       m.b45 + 448*m.b39*m.b40*m.b45*m.b46 + 384*m.b39*m.b40*m.b46*m.b47 + 320*m.b39*m.b40*m.b47*m.b48
                        + 256*m.b39*m.b40*m.b48*m.b49 + 192*m.b39*m.b40*m.b49*m.b50 + 128*m.b39*m.b40*m.b50*m.b51 + 64*
                       m.b39*m.b40*m.b51*m.b52 + 576*m.b39*m.b41*m.b42*m.b44 + 512*m.b39*m.b41*m.b43*m.b45 + 448*m.b39*
                       m.b41*m.b44*m.b46 + 384*m.b39*m.b41*m.b45*m.b47 + 320*m.b39*m.b41*m.b46*m.b48 + 256*m.b39*m.b41*
                       m.b47*m.b49 + 192*m.b39*m.b41*m.b48*m.b50 + 128*m.b39*m.b41*m.b49*m.b51 + 64*m.b39*m.b41*m.b50*
                       m.b52 + 448*m.b39*m.b42*m.b43*m.b46 + 384*m.b39*m.b42*m.b44*m.b47 + 320*m.b39*m.b42*m.b45*m.b48
                        + 256*m.b39*m.b42*m.b46*m.b49 + 192*m.b39*m.b42*m.b47*m.b50 + 128*m.b39*m.b42*m.b48*m.b51 + 64*
                       m.b39*m.b42*m.b49*m.b52 + 320*m.b39*m.b43*m.b44*m.b48 + 256*m.b39*m.b43*m.b45*m.b49 + 192*m.b39*
                       m.b43*m.b46*m.b50 + 128*m.b39*m.b43*m.b47*m.b51 + 64*m.b39*m.b43*m.b48*m.b52 + 192*m.b39*m.b44*
                       m.b45*m.b50 + 128*m.b39*m.b44*m.b46*m.b51 + 64*m.b39*m.b44*m.b47*m.b52 + 64*m.b39*m.b45*m.b46*
                       m.b52 + 704*m.b40*m.b41*m.b42*m.b43 + 640*m.b40*m.b41*m.b43*m.b44 + 576*m.b40*m.b41*m.b44*m.b45
                        + 512*m.b40*m.b41*m.b45*m.b46 + 448*m.b40*m.b41*m.b46*m.b47 + 384*m.b40*m.b41*m.b47*m.b48 + 320*
                       m.b40*m.b41*m.b48*m.b49 + 256*m.b40*m.b41*m.b49*m.b50 + 192*m.b40*m.b41*m.b50*m.b51 + 128*m.b40*
                       m.b41*m.b51*m.b52 + 64*m.b40*m.b41*m.b52*m.b53 + 576*m.b40*m.b42*m.b43*m.b45 + 512*m.b40*m.b42*
                       m.b44*m.b46 + 448*m.b40*m.b42*m.b45*m.b47 + 384*m.b40*m.b42*m.b46*m.b48 + 320*m.b40*m.b42*m.b47*
                       m.b49 + 256*m.b40*m.b42*m.b48*m.b50 + 192*m.b40*m.b42*m.b49*m.b51 + 128*m.b40*m.b42*m.b50*m.b52
                        + 64*m.b40*m.b42*m.b51*m.b53 + 448*m.b40*m.b43*m.b44*m.b47 + 384*m.b40*m.b43*m.b45*m.b48 + 320*
                       m.b40*m.b43*m.b46*m.b49 + 256*m.b40*m.b43*m.b47*m.b50 + 192*m.b40*m.b43*m.b48*m.b51 + 128*m.b40*
                       m.b43*m.b49*m.b52 + 64*m.b40*m.b43*m.b50*m.b53 + 320*m.b40*m.b44*m.b45*m.b49 + 256*m.b40*m.b44*
                       m.b46*m.b50 + 192*m.b40*m.b44*m.b47*m.b51 + 128*m.b40*m.b44*m.b48*m.b52 + 64*m.b40*m.b44*m.b49*
                       m.b53 + 192*m.b40*m.b45*m.b46*m.b51 + 128*m.b40*m.b45*m.b47*m.b52 + 64*m.b40*m.b45*m.b48*m.b53 + 
                       64*m.b40*m.b46*m.b47*m.b53 + 704*m.b41*m.b42*m.b43*m.b44 + 640*m.b41*m.b42*m.b44*m.b45 + 576*
                       m.b41*m.b42*m.b45*m.b46 + 512*m.b41*m.b42*m.b46*m.b47 + 448*m.b41*m.b42*m.b47*m.b48 + 384*m.b41*
                       m.b42*m.b48*m.b49 + 320*m.b41*m.b42*m.b49*m.b50 + 256*m.b41*m.b42*m.b50*m.b51 + 192*m.b41*m.b42*
                       m.b51*m.b52 + 128*m.b41*m.b42*m.b52*m.b53 + 64*m.b41*m.b42*m.b53*m.b54 + 576*m.b41*m.b43*m.b44*
                       m.b46 + 512*m.b41*m.b43*m.b45*m.b47 + 448*m.b41*m.b43*m.b46*m.b48 + 384*m.b41*m.b43*m.b47*m.b49
                        + 320*m.b41*m.b43*m.b48*m.b50 + 256*m.b41*m.b43*m.b49*m.b51 + 192*m.b41*m.b43*m.b50*m.b52 + 128*
                       m.b41*m.b43*m.b51*m.b53 + 64*m.b41*m.b43*m.b52*m.b54 + 448*m.b41*m.b44*m.b45*m.b48 + 384*m.b41*
                       m.b44*m.b46*m.b49 + 320*m.b41*m.b44*m.b47*m.b50 + 256*m.b41*m.b44*m.b48*m.b51 + 192*m.b41*m.b44*
                       m.b49*m.b52 + 128*m.b41*m.b44*m.b50*m.b53 + 64*m.b41*m.b44*m.b51*m.b54 + 320*m.b41*m.b45*m.b46*
                       m.b50 + 256*m.b41*m.b45*m.b47*m.b51 + 192*m.b41*m.b45*m.b48*m.b52 + 128*m.b41*m.b45*m.b49*m.b53
                        + 64*m.b41*m.b45*m.b50*m.b54 + 192*m.b41*m.b46*m.b47*m.b52 + 128*m.b41*m.b46*m.b48*m.b53 + 64*
                       m.b41*m.b46*m.b49*m.b54 + 64*m.b41*m.b47*m.b48*m.b54 + 704*m.b42*m.b43*m.b44*m.b45 + 640*m.b42*
                       m.b43*m.b45*m.b46 + 576*m.b42*m.b43*m.b46*m.b47 + 512*m.b42*m.b43*m.b47*m.b48 + 448*m.b42*m.b43*
                       m.b48*m.b49 + 384*m.b42*m.b43*m.b49*m.b50 + 320*m.b42*m.b43*m.b50*m.b51 + 256*m.b42*m.b43*m.b51*
                       m.b52 + 192*m.b42*m.b43*m.b52*m.b53 + 128*m.b42*m.b43*m.b53*m.b54 + 64*m.b42*m.b43*m.b54*m.b55 + 
                       576*m.b42*m.b44*m.b45*m.b47 + 512*m.b42*m.b44*m.b46*m.b48 + 448*m.b42*m.b44*m.b47*m.b49 + 384*
                       m.b42*m.b44*m.b48*m.b50 + 320*m.b42*m.b44*m.b49*m.b51 + 256*m.b42*m.b44*m.b50*m.b52 + 192*m.b42*
                       m.b44*m.b51*m.b53 + 128*m.b42*m.b44*m.b52*m.b54 + 64*m.b42*m.b44*m.b53*m.b55 + 448*m.b42*m.b45*
                       m.b46*m.b49 + 384*m.b42*m.b45*m.b47*m.b50 + 320*m.b42*m.b45*m.b48*m.b51 + 256*m.b42*m.b45*m.b49*
                       m.b52 + 192*m.b42*m.b45*m.b50*m.b53 + 128*m.b42*m.b45*m.b51*m.b54 + 64*m.b42*m.b45*m.b52*m.b55 + 
                       320*m.b42*m.b46*m.b47*m.b51 + 256*m.b42*m.b46*m.b48*m.b52 + 192*m.b42*m.b46*m.b49*m.b53 + 128*
                       m.b42*m.b46*m.b50*m.b54 + 64*m.b42*m.b46*m.b51*m.b55 + 192*m.b42*m.b47*m.b48*m.b53 + 128*m.b42*
                       m.b47*m.b49*m.b54 + 64*m.b42*m.b47*m.b50*m.b55 + 64*m.b42*m.b48*m.b49*m.b55 + 640*m.b43*m.b44*
                       m.b45*m.b46 + 576*m.b43*m.b44*m.b46*m.b47 + 512*m.b43*m.b44*m.b47*m.b48 + 448*m.b43*m.b44*m.b48*
                       m.b49 + 384*m.b43*m.b44*m.b49*m.b50 + 320*m.b43*m.b44*m.b50*m.b51 + 256*m.b43*m.b44*m.b51*m.b52
                        + 192*m.b43*m.b44*m.b52*m.b53 + 128*m.b43*m.b44*m.b53*m.b54 + 64*m.b43*m.b44*m.b54*m.b55 + 512*
                       m.b43*m.b45*m.b46*m.b48 + 448*m.b43*m.b45*m.b47*m.b49 + 384*m.b43*m.b45*m.b48*m.b50 + 320*m.b43*
                       m.b45*m.b49*m.b51 + 256*m.b43*m.b45*m.b50*m.b52 + 192*m.b43*m.b45*m.b51*m.b53 + 128*m.b43*m.b45*
                       m.b52*m.b54 + 64*m.b43*m.b45*m.b53*m.b55 + 384*m.b43*m.b46*m.b47*m.b50 + 320*m.b43*m.b46*m.b48*
                       m.b51 + 256*m.b43*m.b46*m.b49*m.b52 + 192*m.b43*m.b46*m.b50*m.b53 + 128*m.b43*m.b46*m.b51*m.b54
                        + 64*m.b43*m.b46*m.b52*m.b55 + 256*m.b43*m.b47*m.b48*m.b52 + 192*m.b43*m.b47*m.b49*m.b53 + 128*
                       m.b43*m.b47*m.b50*m.b54 + 64*m.b43*m.b47*m.b51*m.b55 + 128*m.b43*m.b48*m.b49*m.b54 + 64*m.b43*
                       m.b48*m.b50*m.b55 + 576*m.b44*m.b45*m.b46*m.b47 + 512*m.b44*m.b45*m.b47*m.b48 + 448*m.b44*m.b45*
                       m.b48*m.b49 + 384*m.b44*m.b45*m.b49*m.b50 + 320*m.b44*m.b45*m.b50*m.b51 + 256*m.b44*m.b45*m.b51*
                       m.b52 + 192*m.b44*m.b45*m.b52*m.b53 + 128*m.b44*m.b45*m.b53*m.b54 + 64*m.b44*m.b45*m.b54*m.b55 + 
                       448*m.b44*m.b46*m.b47*m.b49 + 384*m.b44*m.b46*m.b48*m.b50 + 320*m.b44*m.b46*m.b49*m.b51 + 256*
                       m.b44*m.b46*m.b50*m.b52 + 192*m.b44*m.b46*m.b51*m.b53 + 128*m.b44*m.b46*m.b52*m.b54 + 64*m.b44*
                       m.b46*m.b53*m.b55 + 320*m.b44*m.b47*m.b48*m.b51 + 256*m.b44*m.b47*m.b49*m.b52 + 192*m.b44*m.b47*
                       m.b50*m.b53 + 128*m.b44*m.b47*m.b51*m.b54 + 64*m.b44*m.b47*m.b52*m.b55 + 192*m.b44*m.b48*m.b49*
                       m.b53 + 128*m.b44*m.b48*m.b50*m.b54 + 64*m.b44*m.b48*m.b51*m.b55 + 64*m.b44*m.b49*m.b50*m.b55 + 
                       512*m.b45*m.b46*m.b47*m.b48 + 448*m.b45*m.b46*m.b48*m.b49 + 384*m.b45*m.b46*m.b49*m.b50 + 320*
                       m.b45*m.b46*m.b50*m.b51 + 256*m.b45*m.b46*m.b51*m.b52 + 192*m.b45*m.b46*m.b52*m.b53 + 128*m.b45*
                       m.b46*m.b53*m.b54 + 64*m.b45*m.b46*m.b54*m.b55 + 384*m.b45*m.b47*m.b48*m.b50 + 320*m.b45*m.b47*
                       m.b49*m.b51 + 256*m.b45*m.b47*m.b50*m.b52 + 192*m.b45*m.b47*m.b51*m.b53 + 128*m.b45*m.b47*m.b52*
                       m.b54 + 64*m.b45*m.b47*m.b53*m.b55 + 256*m.b45*m.b48*m.b49*m.b52 + 192*m.b45*m.b48*m.b50*m.b53 + 
                       128*m.b45*m.b48*m.b51*m.b54 + 64*m.b45*m.b48*m.b52*m.b55 + 128*m.b45*m.b49*m.b50*m.b54 + 64*m.b45
                       *m.b49*m.b51*m.b55 + 448*m.b46*m.b47*m.b48*m.b49 + 384*m.b46*m.b47*m.b49*m.b50 + 320*m.b46*m.b47*
                       m.b50*m.b51 + 256*m.b46*m.b47*m.b51*m.b52 + 192*m.b46*m.b47*m.b52*m.b53 + 128*m.b46*m.b47*m.b53*
                       m.b54 + 64*m.b46*m.b47*m.b54*m.b55 + 320*m.b46*m.b48*m.b49*m.b51 + 256*m.b46*m.b48*m.b50*m.b52 + 
                       192*m.b46*m.b48*m.b51*m.b53 + 128*m.b46*m.b48*m.b52*m.b54 + 64*m.b46*m.b48*m.b53*m.b55 + 192*
                       m.b46*m.b49*m.b50*m.b53 + 128*m.b46*m.b49*m.b51*m.b54 + 64*m.b46*m.b49*m.b52*m.b55 + 64*m.b46*
                       m.b50*m.b51*m.b55 + 384*m.b47*m.b48*m.b49*m.b50 + 320*m.b47*m.b48*m.b50*m.b51 + 256*m.b47*m.b48*
                       m.b51*m.b52 + 192*m.b47*m.b48*m.b52*m.b53 + 128*m.b47*m.b48*m.b53*m.b54 + 64*m.b47*m.b48*m.b54*
                       m.b55 + 256*m.b47*m.b49*m.b50*m.b52 + 192*m.b47*m.b49*m.b51*m.b53 + 128*m.b47*m.b49*m.b52*m.b54
                        + 64*m.b47*m.b49*m.b53*m.b55 + 128*m.b47*m.b50*m.b51*m.b54 + 64*m.b47*m.b50*m.b52*m.b55 + 320*
                       m.b48*m.b49*m.b50*m.b51 + 256*m.b48*m.b49*m.b51*m.b52 + 192*m.b48*m.b49*m.b52*m.b53 + 128*m.b48*
                       m.b49*m.b53*m.b54 + 64*m.b48*m.b49*m.b54*m.b55 + 192*m.b48*m.b50*m.b51*m.b53 + 128*m.b48*m.b50*
                       m.b52*m.b54 + 64*m.b48*m.b50*m.b53*m.b55 + 64*m.b48*m.b51*m.b52*m.b55 + 256*m.b49*m.b50*m.b51*
                       m.b52 + 192*m.b49*m.b50*m.b52*m.b53 + 128*m.b49*m.b50*m.b53*m.b54 + 64*m.b49*m.b50*m.b54*m.b55 + 
                       128*m.b49*m.b51*m.b52*m.b54 + 64*m.b49*m.b51*m.b53*m.b55 + 192*m.b50*m.b51*m.b52*m.b53 + 128*
                       m.b50*m.b51*m.b53*m.b54 + 64*m.b50*m.b51*m.b54*m.b55 + 64*m.b50*m.b52*m.b53*m.b55 + 128*m.b51*
                       m.b52*m.b53*m.b54 + 64*m.b51*m.b52*m.b54*m.b55 + 64*m.b52*m.b53*m.b54*m.b55 - 32*m.b1*m.b2*m.b3
                        - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*
                       m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1
                       *m.b2*m.b13 - 32*m.b1*m.b2*m.b14 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64
                       *m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*m.b11
                        - 64*m.b1*m.b3*m.b12 - 32*m.b1*m.b3*m.b13 - 32*m.b1*m.b3*m.b14 - 64*m.b1*m.b4*m.b5 - 64*m.b1*
                       m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*
                       m.b1*m.b4*m.b11 - 32*m.b1*m.b4*m.b12 - 32*m.b1*m.b4*m.b13 - 32*m.b1*m.b4*m.b14 - 64*m.b1*m.b5*
                       m.b6 - 64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 32*m.b1*
                       m.b5*m.b11 - 32*m.b1*m.b5*m.b12 - 32*m.b1*m.b5*m.b13 - 32*m.b1*m.b5*m.b14 - 64*m.b1*m.b6*m.b7 - 
                       64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 32*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*m.b12 - 32*m.b1*m.b6*
                       m.b13 - 32*m.b1*m.b6*m.b14 - 64*m.b1*m.b7*m.b8 - 32*m.b1*m.b7*m.b9 - 32*m.b1*m.b7*m.b10 - 32*m.b1
                       *m.b7*m.b11 - 32*m.b1*m.b7*m.b12 - 32*m.b1*m.b7*m.b14 - 32*m.b1*m.b8*m.b9 - 32*m.b1*m.b8*m.b10 - 
                       32*m.b1*m.b8*m.b11 - 32*m.b1*m.b8*m.b12 - 32*m.b1*m.b8*m.b13 - 32*m.b1*m.b8*m.b14 - 32*m.b1*m.b9*
                       m.b10 - 32*m.b1*m.b9*m.b11 - 32*m.b1*m.b9*m.b12 - 32*m.b1*m.b9*m.b13 - 32*m.b1*m.b9*m.b14 - 32*
                       m.b1*m.b10*m.b11 - 32*m.b1*m.b10*m.b12 - 32*m.b1*m.b10*m.b13 - 32*m.b1*m.b10*m.b14 - 32*m.b1*
                       m.b11*m.b12 - 32*m.b1*m.b11*m.b13 - 32*m.b1*m.b11*m.b14 - 32*m.b1*m.b12*m.b13 - 32*m.b1*m.b12*
                       m.b14 - 32*m.b1*m.b13*m.b14 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*
                       m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*
                       m.b11 - 128*m.b2*m.b3*m.b12 - 128*m.b2*m.b3*m.b13 - 96*m.b2*m.b3*m.b14 - 32*m.b2*m.b3*m.b15 - 160
                       *m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 128*m.b2*m.b4*
                       m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 96*m.b2*m.b4*m.b13 - 64*
                       m.b2*m.b4*m.b14 - 32*m.b2*m.b4*m.b15 - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*
                       m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 128*m.b2*m.b5*m.b11 - 96*m.b2*m.b5*m.b12 - 64*
                       m.b2*m.b5*m.b13 - 64*m.b2*m.b5*m.b14 - 32*m.b2*m.b5*m.b15 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*
                       m.b8 - 128*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b10 - 96*m.b2*m.b6*m.b11 - 64*m.b2*m.b6*m.b12 - 64*
                       m.b2*m.b6*m.b13 - 64*m.b2*m.b6*m.b14 - 32*m.b2*m.b6*m.b15 - 160*m.b2*m.b7*m.b8 - 128*m.b2*m.b7*
                       m.b9 - 96*m.b2*m.b7*m.b10 - 64*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b13 - 64*m.b2*m.b7*m.b14 - 32*
                       m.b2*m.b7*m.b15 - 128*m.b2*m.b8*m.b9 - 64*m.b2*m.b8*m.b10 - 64*m.b2*m.b8*m.b11 - 64*m.b2*m.b8*
                       m.b12 - 64*m.b2*m.b8*m.b13 - 32*m.b2*m.b8*m.b15 - 96*m.b2*m.b9*m.b10 - 64*m.b2*m.b9*m.b11 - 64*
                       m.b2*m.b9*m.b12 - 64*m.b2*m.b9*m.b13 - 64*m.b2*m.b9*m.b14 - 32*m.b2*m.b9*m.b15 - 96*m.b2*m.b10*
                       m.b11 - 64*m.b2*m.b10*m.b12 - 64*m.b2*m.b10*m.b13 - 64*m.b2*m.b10*m.b14 - 32*m.b2*m.b10*m.b15 - 
                       96*m.b2*m.b11*m.b12 - 64*m.b2*m.b11*m.b13 - 64*m.b2*m.b11*m.b14 - 32*m.b2*m.b11*m.b15 - 96*m.b2*
                       m.b12*m.b13 - 64*m.b2*m.b12*m.b14 - 32*m.b2*m.b12*m.b15 - 96*m.b2*m.b13*m.b14 - 32*m.b2*m.b13*
                       m.b15 - 32*m.b2*m.b14*m.b15 - 160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*
                       m.b3*m.b4*m.b8 - 192*m.b3*m.b4*m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*
                       m.b12 - 192*m.b3*m.b4*m.b13 - 160*m.b3*m.b4*m.b14 - 96*m.b3*m.b4*m.b15 - 32*m.b3*m.b4*m.b16 - 256
                       *m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*
                       m.b10 - 192*m.b3*m.b5*m.b11 - 192*m.b3*m.b5*m.b12 - 160*m.b3*m.b5*m.b13 - 128*m.b3*m.b5*m.b14 - 
                       64*m.b3*m.b5*m.b15 - 32*m.b3*m.b5*m.b16 - 256*m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*
                       m.b9 - 192*m.b3*m.b6*m.b10 - 192*m.b3*m.b6*m.b11 - 160*m.b3*m.b6*m.b12 - 128*m.b3*m.b6*m.b13 - 96
                       *m.b3*m.b6*m.b14 - 64*m.b3*m.b6*m.b15 - 32*m.b3*m.b6*m.b16 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*
                       m.b9 - 192*m.b3*m.b7*m.b10 - 64*m.b3*m.b7*m.b11 - 128*m.b3*m.b7*m.b12 - 96*m.b3*m.b7*m.b13 - 96*
                       m.b3*m.b7*m.b14 - 64*m.b3*m.b7*m.b15 - 32*m.b3*m.b7*m.b16 - 256*m.b3*m.b8*m.b9 - 192*m.b3*m.b8*
                       m.b10 - 128*m.b3*m.b8*m.b11 - 96*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*m.b14 - 64*m.b3*m.b8*m.b15 - 32*
                       m.b3*m.b8*m.b16 - 192*m.b3*m.b9*m.b10 - 128*m.b3*m.b9*m.b11 - 96*m.b3*m.b9*m.b12 - 96*m.b3*m.b9*
                       m.b13 - 96*m.b3*m.b9*m.b14 - 32*m.b3*m.b9*m.b16 - 160*m.b3*m.b10*m.b11 - 128*m.b3*m.b10*m.b12 - 
                       96*m.b3*m.b10*m.b13 - 96*m.b3*m.b10*m.b14 - 64*m.b3*m.b10*m.b15 - 32*m.b3*m.b10*m.b16 - 160*m.b3*
                       m.b11*m.b12 - 128*m.b3*m.b11*m.b13 - 96*m.b3*m.b11*m.b14 - 64*m.b3*m.b11*m.b15 - 32*m.b3*m.b11*
                       m.b16 - 160*m.b3*m.b12*m.b13 - 128*m.b3*m.b12*m.b14 - 64*m.b3*m.b12*m.b15 - 32*m.b3*m.b12*m.b16
                        - 160*m.b3*m.b13*m.b14 - 64*m.b3*m.b13*m.b15 - 32*m.b3*m.b13*m.b16 - 96*m.b3*m.b14*m.b15 - 32*
                       m.b3*m.b14*m.b16 - 32*m.b3*m.b15*m.b16 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*
                       m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256
                       *m.b4*m.b5*m.b13 - 224*m.b4*m.b5*m.b14 - 160*m.b4*m.b5*m.b15 - 96*m.b4*m.b5*m.b16 - 32*m.b4*m.b5*
                       m.b17 - 352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*
                       m.b4*m.b6*m.b11 - 256*m.b4*m.b6*m.b12 - 224*m.b4*m.b6*m.b13 - 192*m.b4*m.b6*m.b14 - 128*m.b4*m.b6
                       *m.b15 - 64*m.b4*m.b6*m.b16 - 32*m.b4*m.b6*m.b17 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*
                       m.b4*m.b7*m.b10 - 256*m.b4*m.b7*m.b11 - 224*m.b4*m.b7*m.b12 - 192*m.b4*m.b7*m.b13 - 160*m.b4*m.b7
                       *m.b14 - 96*m.b4*m.b7*m.b15 - 64*m.b4*m.b7*m.b16 - 32*m.b4*m.b7*m.b17 - 352*m.b4*m.b8*m.b9 - 320*
                       m.b4*m.b8*m.b10 - 256*m.b4*m.b8*m.b11 - 64*m.b4*m.b8*m.b12 - 160*m.b4*m.b8*m.b13 - 128*m.b4*m.b8*
                       m.b14 - 96*m.b4*m.b8*m.b15 - 64*m.b4*m.b8*m.b16 - 32*m.b4*m.b8*m.b17 - 320*m.b4*m.b9*m.b10 - 256*
                       m.b4*m.b9*m.b11 - 192*m.b4*m.b9*m.b12 - 128*m.b4*m.b9*m.b13 - 96*m.b4*m.b9*m.b15 - 64*m.b4*m.b9*
                       m.b16 - 32*m.b4*m.b9*m.b17 - 256*m.b4*m.b10*m.b11 - 192*m.b4*m.b10*m.b12 - 160*m.b4*m.b10*m.b13
                        - 128*m.b4*m.b10*m.b14 - 96*m.b4*m.b10*m.b15 - 32*m.b4*m.b10*m.b17 - 224*m.b4*m.b11*m.b12 - 192*
                       m.b4*m.b11*m.b13 - 160*m.b4*m.b11*m.b14 - 96*m.b4*m.b11*m.b15 - 64*m.b4*m.b11*m.b16 - 32*m.b4*
                       m.b11*m.b17 - 224*m.b4*m.b12*m.b13 - 192*m.b4*m.b12*m.b14 - 96*m.b4*m.b12*m.b15 - 64*m.b4*m.b12*
                       m.b16 - 32*m.b4*m.b12*m.b17 - 224*m.b4*m.b13*m.b14 - 128*m.b4*m.b13*m.b15 - 64*m.b4*m.b13*m.b16
                        - 32*m.b4*m.b13*m.b17 - 160*m.b4*m.b14*m.b15 - 64*m.b4*m.b14*m.b16 - 32*m.b4*m.b14*m.b17 - 96*
                       m.b4*m.b15*m.b16 - 32*m.b4*m.b15*m.b17 - 32*m.b4*m.b16*m.b17 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6
                       *m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*m.b6*m.b11 - 320*m.b5*m.b6*m.b12 - 
                       320*m.b5*m.b6*m.b13 - 288*m.b5*m.b6*m.b14 - 224*m.b5*m.b6*m.b15 - 160*m.b5*m.b6*m.b16 - 96*m.b5*
                       m.b6*m.b17 - 32*m.b5*m.b6*m.b18 - 448*m.b5*m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10
                        - 352*m.b5*m.b7*m.b11 - 320*m.b5*m.b7*m.b12 - 288*m.b5*m.b7*m.b13 - 256*m.b5*m.b7*m.b14 - 192*
                       m.b5*m.b7*m.b15 - 128*m.b5*m.b7*m.b16 - 64*m.b5*m.b7*m.b17 - 32*m.b5*m.b7*m.b18 - 448*m.b5*m.b8*
                       m.b9 - 416*m.b5*m.b8*m.b10 - 224*m.b5*m.b8*m.b11 - 320*m.b5*m.b8*m.b12 - 256*m.b5*m.b8*m.b13 - 
                       224*m.b5*m.b8*m.b14 - 160*m.b5*m.b8*m.b15 - 96*m.b5*m.b8*m.b16 - 64*m.b5*m.b8*m.b17 - 32*m.b5*
                       m.b8*m.b18 - 448*m.b5*m.b9*m.b10 - 384*m.b5*m.b9*m.b11 - 320*m.b5*m.b9*m.b12 - 96*m.b5*m.b9*m.b13
                        - 192*m.b5*m.b9*m.b14 - 128*m.b5*m.b9*m.b15 - 96*m.b5*m.b9*m.b16 - 64*m.b5*m.b9*m.b17 - 32*m.b5*
                       m.b9*m.b18 - 384*m.b5*m.b10*m.b11 - 320*m.b5*m.b10*m.b12 - 256*m.b5*m.b10*m.b13 - 192*m.b5*m.b10*
                       m.b14 - 96*m.b5*m.b10*m.b16 - 64*m.b5*m.b10*m.b17 - 32*m.b5*m.b10*m.b18 - 320*m.b5*m.b11*m.b12 - 
                       256*m.b5*m.b11*m.b13 - 224*m.b5*m.b11*m.b14 - 128*m.b5*m.b11*m.b15 - 96*m.b5*m.b11*m.b16 - 32*
                       m.b5*m.b11*m.b18 - 288*m.b5*m.b12*m.b13 - 256*m.b5*m.b12*m.b14 - 160*m.b5*m.b12*m.b15 - 96*m.b5*
                       m.b12*m.b16 - 64*m.b5*m.b12*m.b17 - 32*m.b5*m.b12*m.b18 - 288*m.b5*m.b13*m.b14 - 192*m.b5*m.b13*
                       m.b15 - 96*m.b5*m.b13*m.b16 - 64*m.b5*m.b13*m.b17 - 32*m.b5*m.b13*m.b18 - 224*m.b5*m.b14*m.b15 - 
                       128*m.b5*m.b14*m.b16 - 64*m.b5*m.b14*m.b17 - 32*m.b5*m.b14*m.b18 - 160*m.b5*m.b15*m.b16 - 64*m.b5
                       *m.b15*m.b17 - 32*m.b5*m.b15*m.b18 - 96*m.b5*m.b16*m.b17 - 32*m.b5*m.b16*m.b18 - 32*m.b5*m.b17*
                       m.b18 - 352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416
                       *m.b6*m.b7*m.b12 - 384*m.b6*m.b7*m.b13 - 352*m.b6*m.b7*m.b14 - 288*m.b6*m.b7*m.b15 - 224*m.b6*
                       m.b7*m.b16 - 160*m.b6*m.b7*m.b17 - 96*m.b6*m.b7*m.b18 - 32*m.b6*m.b7*m.b19 - 544*m.b6*m.b8*m.b9
                        - 320*m.b6*m.b8*m.b10 - 480*m.b6*m.b8*m.b11 - 448*m.b6*m.b8*m.b12 - 384*m.b6*m.b8*m.b13 - 320*
                       m.b6*m.b8*m.b14 - 256*m.b6*m.b8*m.b15 - 192*m.b6*m.b8*m.b16 - 128*m.b6*m.b8*m.b17 - 64*m.b6*m.b8*
                       m.b18 - 32*m.b6*m.b8*m.b19 - 544*m.b6*m.b9*m.b10 - 512*m.b6*m.b9*m.b11 - 256*m.b6*m.b9*m.b12 - 
                       384*m.b6*m.b9*m.b13 - 320*m.b6*m.b9*m.b14 - 224*m.b6*m.b9*m.b15 - 160*m.b6*m.b9*m.b16 - 96*m.b6*
                       m.b9*m.b17 - 64*m.b6*m.b9*m.b18 - 32*m.b6*m.b9*m.b19 - 512*m.b6*m.b10*m.b11 - 448*m.b6*m.b10*
                       m.b12 - 384*m.b6*m.b10*m.b13 - 128*m.b6*m.b10*m.b14 - 192*m.b6*m.b10*m.b15 - 128*m.b6*m.b10*m.b16
                        - 96*m.b6*m.b10*m.b17 - 64*m.b6*m.b10*m.b18 - 32*m.b6*m.b10*m.b19 - 448*m.b6*m.b11*m.b12 - 384*
                       m.b6*m.b11*m.b13 - 320*m.b6*m.b11*m.b14 - 192*m.b6*m.b11*m.b15 - 96*m.b6*m.b11*m.b17 - 64*m.b6*
                       m.b11*m.b18 - 32*m.b6*m.b11*m.b19 - 384*m.b6*m.b12*m.b13 - 320*m.b6*m.b12*m.b14 - 224*m.b6*m.b12*
                       m.b15 - 128*m.b6*m.b12*m.b16 - 96*m.b6*m.b12*m.b17 - 32*m.b6*m.b12*m.b19 - 352*m.b6*m.b13*m.b14
                        - 256*m.b6*m.b13*m.b15 - 160*m.b6*m.b13*m.b16 - 96*m.b6*m.b13*m.b17 - 64*m.b6*m.b13*m.b18 - 32*
                       m.b6*m.b13*m.b19 - 288*m.b6*m.b14*m.b15 - 192*m.b6*m.b14*m.b16 - 96*m.b6*m.b14*m.b17 - 64*m.b6*
                       m.b14*m.b18 - 32*m.b6*m.b14*m.b19 - 224*m.b6*m.b15*m.b16 - 128*m.b6*m.b15*m.b17 - 64*m.b6*m.b15*
                       m.b18 - 32*m.b6*m.b15*m.b19 - 160*m.b6*m.b16*m.b17 - 64*m.b6*m.b16*m.b18 - 32*m.b6*m.b16*m.b19 - 
                       96*m.b6*m.b17*m.b18 - 32*m.b6*m.b17*m.b19 - 32*m.b6*m.b18*m.b19 - 416*m.b7*m.b8*m.b9 - 608*m.b7*
                       m.b8*m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 512*m.b7*m.b8*m.b13 - 448*m.b7*m.b8*
                       m.b14 - 352*m.b7*m.b8*m.b15 - 288*m.b7*m.b8*m.b16 - 224*m.b7*m.b8*m.b17 - 160*m.b7*m.b8*m.b18 - 
                       96*m.b7*m.b8*m.b19 - 32*m.b7*m.b8*m.b20 - 640*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 576*m.b7*
                       m.b9*m.b12 - 512*m.b7*m.b9*m.b13 - 448*m.b7*m.b9*m.b14 - 320*m.b7*m.b9*m.b15 - 256*m.b7*m.b9*
                       m.b16 - 192*m.b7*m.b9*m.b17 - 128*m.b7*m.b9*m.b18 - 64*m.b7*m.b9*m.b19 - 32*m.b7*m.b9*m.b20 - 640
                       *m.b7*m.b10*m.b11 - 576*m.b7*m.b10*m.b12 - 288*m.b7*m.b10*m.b13 - 448*m.b7*m.b10*m.b14 - 320*m.b7
                       *m.b10*m.b15 - 224*m.b7*m.b10*m.b16 - 160*m.b7*m.b10*m.b17 - 96*m.b7*m.b10*m.b18 - 64*m.b7*m.b10*
                       m.b19 - 32*m.b7*m.b10*m.b20 - 576*m.b7*m.b11*m.b12 - 512*m.b7*m.b11*m.b13 - 448*m.b7*m.b11*m.b14
                        - 128*m.b7*m.b11*m.b15 - 192*m.b7*m.b11*m.b16 - 128*m.b7*m.b11*m.b17 - 96*m.b7*m.b11*m.b18 - 64*
                       m.b7*m.b11*m.b19 - 32*m.b7*m.b11*m.b20 - 512*m.b7*m.b12*m.b13 - 448*m.b7*m.b12*m.b14 - 320*m.b7*
                       m.b12*m.b15 - 192*m.b7*m.b12*m.b16 - 96*m.b7*m.b12*m.b18 - 64*m.b7*m.b12*m.b19 - 32*m.b7*m.b12*
                       m.b20 - 448*m.b7*m.b13*m.b14 - 320*m.b7*m.b13*m.b15 - 224*m.b7*m.b13*m.b16 - 128*m.b7*m.b13*m.b17
                        - 96*m.b7*m.b13*m.b18 - 32*m.b7*m.b13*m.b20 - 352*m.b7*m.b14*m.b15 - 256*m.b7*m.b14*m.b16 - 160*
                       m.b7*m.b14*m.b17 - 96*m.b7*m.b14*m.b18 - 64*m.b7*m.b14*m.b19 - 32*m.b7*m.b14*m.b20 - 288*m.b7*
                       m.b15*m.b16 - 192*m.b7*m.b15*m.b17 - 96*m.b7*m.b15*m.b18 - 64*m.b7*m.b15*m.b19 - 32*m.b7*m.b15*
                       m.b20 - 224*m.b7*m.b16*m.b17 - 128*m.b7*m.b16*m.b18 - 64*m.b7*m.b16*m.b19 - 32*m.b7*m.b16*m.b20
                        - 160*m.b7*m.b17*m.b18 - 64*m.b7*m.b17*m.b19 - 32*m.b7*m.b17*m.b20 - 96*m.b7*m.b18*m.b19 - 32*
                       m.b7*m.b18*m.b20 - 32*m.b7*m.b19*m.b20 - 480*m.b8*m.b9*m.b10 - 704*m.b8*m.b9*m.b11 - 672*m.b8*
                       m.b9*m.b12 - 640*m.b8*m.b9*m.b13 - 576*m.b8*m.b9*m.b14 - 448*m.b8*m.b9*m.b15 - 352*m.b8*m.b9*
                       m.b16 - 288*m.b8*m.b9*m.b17 - 224*m.b8*m.b9*m.b18 - 160*m.b8*m.b9*m.b19 - 96*m.b8*m.b9*m.b20 - 32
                       *m.b8*m.b9*m.b21 - 736*m.b8*m.b10*m.b11 - 448*m.b8*m.b10*m.b12 - 640*m.b8*m.b10*m.b13 - 576*m.b8*
                       m.b10*m.b14 - 448*m.b8*m.b10*m.b15 - 320*m.b8*m.b10*m.b16 - 256*m.b8*m.b10*m.b17 - 192*m.b8*m.b10
                       *m.b18 - 128*m.b8*m.b10*m.b19 - 64*m.b8*m.b10*m.b20 - 32*m.b8*m.b10*m.b21 - 704*m.b8*m.b11*m.b12
                        - 640*m.b8*m.b11*m.b13 - 320*m.b8*m.b11*m.b14 - 448*m.b8*m.b11*m.b15 - 320*m.b8*m.b11*m.b16 - 
                       224*m.b8*m.b11*m.b17 - 160*m.b8*m.b11*m.b18 - 96*m.b8*m.b11*m.b19 - 64*m.b8*m.b11*m.b20 - 32*m.b8
                       *m.b11*m.b21 - 640*m.b8*m.b12*m.b13 - 576*m.b8*m.b12*m.b14 - 448*m.b8*m.b12*m.b15 - 128*m.b8*
                       m.b12*m.b16 - 192*m.b8*m.b12*m.b17 - 128*m.b8*m.b12*m.b18 - 96*m.b8*m.b12*m.b19 - 64*m.b8*m.b12*
                       m.b20 - 32*m.b8*m.b12*m.b21 - 576*m.b8*m.b13*m.b14 - 448*m.b8*m.b13*m.b15 - 320*m.b8*m.b13*m.b16
                        - 192*m.b8*m.b13*m.b17 - 96*m.b8*m.b13*m.b19 - 64*m.b8*m.b13*m.b20 - 32*m.b8*m.b13*m.b21 - 448*
                       m.b8*m.b14*m.b15 - 320*m.b8*m.b14*m.b16 - 224*m.b8*m.b14*m.b17 - 128*m.b8*m.b14*m.b18 - 96*m.b8*
                       m.b14*m.b19 - 32*m.b8*m.b14*m.b21 - 352*m.b8*m.b15*m.b16 - 256*m.b8*m.b15*m.b17 - 160*m.b8*m.b15*
                       m.b18 - 96*m.b8*m.b15*m.b19 - 64*m.b8*m.b15*m.b20 - 32*m.b8*m.b15*m.b21 - 288*m.b8*m.b16*m.b17 - 
                       192*m.b8*m.b16*m.b18 - 96*m.b8*m.b16*m.b19 - 64*m.b8*m.b16*m.b20 - 32*m.b8*m.b16*m.b21 - 224*m.b8
                       *m.b17*m.b18 - 128*m.b8*m.b17*m.b19 - 64*m.b8*m.b17*m.b20 - 32*m.b8*m.b17*m.b21 - 160*m.b8*m.b18*
                       m.b19 - 64*m.b8*m.b18*m.b20 - 32*m.b8*m.b18*m.b21 - 96*m.b8*m.b19*m.b20 - 32*m.b8*m.b19*m.b21 - 
                       32*m.b8*m.b20*m.b21 - 544*m.b9*m.b10*m.b11 - 800*m.b9*m.b10*m.b12 - 768*m.b9*m.b10*m.b13 - 704*
                       m.b9*m.b10*m.b14 - 576*m.b9*m.b10*m.b15 - 448*m.b9*m.b10*m.b16 - 352*m.b9*m.b10*m.b17 - 288*m.b9*
                       m.b10*m.b18 - 224*m.b9*m.b10*m.b19 - 160*m.b9*m.b10*m.b20 - 96*m.b9*m.b10*m.b21 - 32*m.b9*m.b10*
                       m.b22 - 832*m.b9*m.b11*m.b12 - 480*m.b9*m.b11*m.b13 - 704*m.b9*m.b11*m.b14 - 576*m.b9*m.b11*m.b15
                        - 448*m.b9*m.b11*m.b16 - 320*m.b9*m.b11*m.b17 - 256*m.b9*m.b11*m.b18 - 192*m.b9*m.b11*m.b19 - 
                       128*m.b9*m.b11*m.b20 - 64*m.b9*m.b11*m.b21 - 32*m.b9*m.b11*m.b22 - 768*m.b9*m.b12*m.b13 - 704*
                       m.b9*m.b12*m.b14 - 320*m.b9*m.b12*m.b15 - 448*m.b9*m.b12*m.b16 - 320*m.b9*m.b12*m.b17 - 224*m.b9*
                       m.b12*m.b18 - 160*m.b9*m.b12*m.b19 - 96*m.b9*m.b12*m.b20 - 64*m.b9*m.b12*m.b21 - 32*m.b9*m.b12*
                       m.b22 - 704*m.b9*m.b13*m.b14 - 576*m.b9*m.b13*m.b15 - 448*m.b9*m.b13*m.b16 - 128*m.b9*m.b13*m.b17
                        - 192*m.b9*m.b13*m.b18 - 128*m.b9*m.b13*m.b19 - 96*m.b9*m.b13*m.b20 - 64*m.b9*m.b13*m.b21 - 32*
                       m.b9*m.b13*m.b22 - 576*m.b9*m.b14*m.b15 - 448*m.b9*m.b14*m.b16 - 320*m.b9*m.b14*m.b17 - 192*m.b9*
                       m.b14*m.b18 - 96*m.b9*m.b14*m.b20 - 64*m.b9*m.b14*m.b21 - 32*m.b9*m.b14*m.b22 - 448*m.b9*m.b15*
                       m.b16 - 320*m.b9*m.b15*m.b17 - 224*m.b9*m.b15*m.b18 - 128*m.b9*m.b15*m.b19 - 96*m.b9*m.b15*m.b20
                        - 32*m.b9*m.b15*m.b22 - 352*m.b9*m.b16*m.b17 - 256*m.b9*m.b16*m.b18 - 160*m.b9*m.b16*m.b19 - 96*
                       m.b9*m.b16*m.b20 - 64*m.b9*m.b16*m.b21 - 32*m.b9*m.b16*m.b22 - 288*m.b9*m.b17*m.b18 - 192*m.b9*
                       m.b17*m.b19 - 96*m.b9*m.b17*m.b20 - 64*m.b9*m.b17*m.b21 - 32*m.b9*m.b17*m.b22 - 224*m.b9*m.b18*
                       m.b19 - 128*m.b9*m.b18*m.b20 - 64*m.b9*m.b18*m.b21 - 32*m.b9*m.b18*m.b22 - 160*m.b9*m.b19*m.b20
                        - 64*m.b9*m.b19*m.b21 - 32*m.b9*m.b19*m.b22 - 96*m.b9*m.b20*m.b21 - 32*m.b9*m.b20*m.b22 - 32*
                       m.b9*m.b21*m.b22 - 608*m.b10*m.b11*m.b12 - 896*m.b10*m.b11*m.b13 - 832*m.b10*m.b11*m.b14 - 704*
                       m.b10*m.b11*m.b15 - 576*m.b10*m.b11*m.b16 - 448*m.b10*m.b11*m.b17 - 352*m.b10*m.b11*m.b18 - 288*
                       m.b10*m.b11*m.b19 - 224*m.b10*m.b11*m.b20 - 160*m.b10*m.b11*m.b21 - 96*m.b10*m.b11*m.b22 - 32*
                       m.b10*m.b11*m.b23 - 896*m.b10*m.b12*m.b13 - 512*m.b10*m.b12*m.b14 - 704*m.b10*m.b12*m.b15 - 576*
                       m.b10*m.b12*m.b16 - 448*m.b10*m.b12*m.b17 - 320*m.b10*m.b12*m.b18 - 256*m.b10*m.b12*m.b19 - 192*
                       m.b10*m.b12*m.b20 - 128*m.b10*m.b12*m.b21 - 64*m.b10*m.b12*m.b22 - 32*m.b10*m.b12*m.b23 - 832*
                       m.b10*m.b13*m.b14 - 704*m.b10*m.b13*m.b15 - 320*m.b10*m.b13*m.b16 - 448*m.b10*m.b13*m.b17 - 320*
                       m.b10*m.b13*m.b18 - 224*m.b10*m.b13*m.b19 - 160*m.b10*m.b13*m.b20 - 96*m.b10*m.b13*m.b21 - 64*
                       m.b10*m.b13*m.b22 - 32*m.b10*m.b13*m.b23 - 704*m.b10*m.b14*m.b15 - 576*m.b10*m.b14*m.b16 - 448*
                       m.b10*m.b14*m.b17 - 128*m.b10*m.b14*m.b18 - 192*m.b10*m.b14*m.b19 - 128*m.b10*m.b14*m.b20 - 96*
                       m.b10*m.b14*m.b21 - 64*m.b10*m.b14*m.b22 - 32*m.b10*m.b14*m.b23 - 576*m.b10*m.b15*m.b16 - 448*
                       m.b10*m.b15*m.b17 - 320*m.b10*m.b15*m.b18 - 192*m.b10*m.b15*m.b19 - 96*m.b10*m.b15*m.b21 - 64*
                       m.b10*m.b15*m.b22 - 32*m.b10*m.b15*m.b23 - 448*m.b10*m.b16*m.b17 - 320*m.b10*m.b16*m.b18 - 224*
                       m.b10*m.b16*m.b19 - 128*m.b10*m.b16*m.b20 - 96*m.b10*m.b16*m.b21 - 32*m.b10*m.b16*m.b23 - 352*
                       m.b10*m.b17*m.b18 - 256*m.b10*m.b17*m.b19 - 160*m.b10*m.b17*m.b20 - 96*m.b10*m.b17*m.b21 - 64*
                       m.b10*m.b17*m.b22 - 32*m.b10*m.b17*m.b23 - 288*m.b10*m.b18*m.b19 - 192*m.b10*m.b18*m.b20 - 96*
                       m.b10*m.b18*m.b21 - 64*m.b10*m.b18*m.b22 - 32*m.b10*m.b18*m.b23 - 224*m.b10*m.b19*m.b20 - 128*
                       m.b10*m.b19*m.b21 - 64*m.b10*m.b19*m.b22 - 32*m.b10*m.b19*m.b23 - 160*m.b10*m.b20*m.b21 - 64*
                       m.b10*m.b20*m.b22 - 32*m.b10*m.b20*m.b23 - 96*m.b10*m.b21*m.b22 - 32*m.b10*m.b21*m.b23 - 32*m.b10
                       *m.b22*m.b23 - 672*m.b11*m.b12*m.b13 - 960*m.b11*m.b12*m.b14 - 832*m.b11*m.b12*m.b15 - 704*m.b11*
                       m.b12*m.b16 - 576*m.b11*m.b12*m.b17 - 448*m.b11*m.b12*m.b18 - 352*m.b11*m.b12*m.b19 - 288*m.b11*
                       m.b12*m.b20 - 224*m.b11*m.b12*m.b21 - 160*m.b11*m.b12*m.b22 - 96*m.b11*m.b12*m.b23 - 32*m.b11*
                       m.b12*m.b24 - 960*m.b11*m.b13*m.b14 - 512*m.b11*m.b13*m.b15 - 704*m.b11*m.b13*m.b16 - 576*m.b11*
                       m.b13*m.b17 - 448*m.b11*m.b13*m.b18 - 320*m.b11*m.b13*m.b19 - 256*m.b11*m.b13*m.b20 - 192*m.b11*
                       m.b13*m.b21 - 128*m.b11*m.b13*m.b22 - 64*m.b11*m.b13*m.b23 - 32*m.b11*m.b13*m.b24 - 832*m.b11*
                       m.b14*m.b15 - 704*m.b11*m.b14*m.b16 - 320*m.b11*m.b14*m.b17 - 448*m.b11*m.b14*m.b18 - 320*m.b11*
                       m.b14*m.b19 - 224*m.b11*m.b14*m.b20 - 160*m.b11*m.b14*m.b21 - 96*m.b11*m.b14*m.b22 - 64*m.b11*
                       m.b14*m.b23 - 32*m.b11*m.b14*m.b24 - 704*m.b11*m.b15*m.b16 - 576*m.b11*m.b15*m.b17 - 448*m.b11*
                       m.b15*m.b18 - 128*m.b11*m.b15*m.b19 - 192*m.b11*m.b15*m.b20 - 128*m.b11*m.b15*m.b21 - 96*m.b11*
                       m.b15*m.b22 - 64*m.b11*m.b15*m.b23 - 32*m.b11*m.b15*m.b24 - 576*m.b11*m.b16*m.b17 - 448*m.b11*
                       m.b16*m.b18 - 320*m.b11*m.b16*m.b19 - 192*m.b11*m.b16*m.b20 - 96*m.b11*m.b16*m.b22 - 64*m.b11*
                       m.b16*m.b23 - 32*m.b11*m.b16*m.b24 - 448*m.b11*m.b17*m.b18 - 320*m.b11*m.b17*m.b19 - 224*m.b11*
                       m.b17*m.b20 - 128*m.b11*m.b17*m.b21 - 96*m.b11*m.b17*m.b22 - 32*m.b11*m.b17*m.b24 - 352*m.b11*
                       m.b18*m.b19 - 256*m.b11*m.b18*m.b20 - 160*m.b11*m.b18*m.b21 - 96*m.b11*m.b18*m.b22 - 64*m.b11*
                       m.b18*m.b23 - 32*m.b11*m.b18*m.b24 - 288*m.b11*m.b19*m.b20 - 192*m.b11*m.b19*m.b21 - 96*m.b11*
                       m.b19*m.b22 - 64*m.b11*m.b19*m.b23 - 32*m.b11*m.b19*m.b24 - 224*m.b11*m.b20*m.b21 - 128*m.b11*
                       m.b20*m.b22 - 64*m.b11*m.b20*m.b23 - 32*m.b11*m.b20*m.b24 - 160*m.b11*m.b21*m.b22 - 64*m.b11*
                       m.b21*m.b23 - 32*m.b11*m.b21*m.b24 - 96*m.b11*m.b22*m.b23 - 32*m.b11*m.b22*m.b24 - 32*m.b11*m.b23
                       *m.b24 - 704*m.b12*m.b13*m.b14 - 960*m.b12*m.b13*m.b15 - 832*m.b12*m.b13*m.b16 - 704*m.b12*m.b13*
                       m.b17 - 576*m.b12*m.b13*m.b18 - 448*m.b12*m.b13*m.b19 - 352*m.b12*m.b13*m.b20 - 288*m.b12*m.b13*
                       m.b21 - 224*m.b12*m.b13*m.b22 - 160*m.b12*m.b13*m.b23 - 96*m.b12*m.b13*m.b24 - 32*m.b12*m.b13*
                       m.b25 - 960*m.b12*m.b14*m.b15 - 512*m.b12*m.b14*m.b16 - 704*m.b12*m.b14*m.b17 - 576*m.b12*m.b14*
                       m.b18 - 448*m.b12*m.b14*m.b19 - 320*m.b12*m.b14*m.b20 - 256*m.b12*m.b14*m.b21 - 192*m.b12*m.b14*
                       m.b22 - 128*m.b12*m.b14*m.b23 - 64*m.b12*m.b14*m.b24 - 32*m.b12*m.b14*m.b25 - 832*m.b12*m.b15*
                       m.b16 - 704*m.b12*m.b15*m.b17 - 320*m.b12*m.b15*m.b18 - 448*m.b12*m.b15*m.b19 - 320*m.b12*m.b15*
                       m.b20 - 224*m.b12*m.b15*m.b21 - 160*m.b12*m.b15*m.b22 - 96*m.b12*m.b15*m.b23 - 64*m.b12*m.b15*
                       m.b24 - 32*m.b12*m.b15*m.b25 - 704*m.b12*m.b16*m.b17 - 576*m.b12*m.b16*m.b18 - 448*m.b12*m.b16*
                       m.b19 - 128*m.b12*m.b16*m.b20 - 192*m.b12*m.b16*m.b21 - 128*m.b12*m.b16*m.b22 - 96*m.b12*m.b16*
                       m.b23 - 64*m.b12*m.b16*m.b24 - 32*m.b12*m.b16*m.b25 - 576*m.b12*m.b17*m.b18 - 448*m.b12*m.b17*
                       m.b19 - 320*m.b12*m.b17*m.b20 - 192*m.b12*m.b17*m.b21 - 96*m.b12*m.b17*m.b23 - 64*m.b12*m.b17*
                       m.b24 - 32*m.b12*m.b17*m.b25 - 448*m.b12*m.b18*m.b19 - 320*m.b12*m.b18*m.b20 - 224*m.b12*m.b18*
                       m.b21 - 128*m.b12*m.b18*m.b22 - 96*m.b12*m.b18*m.b23 - 32*m.b12*m.b18*m.b25 - 352*m.b12*m.b19*
                       m.b20 - 256*m.b12*m.b19*m.b21 - 160*m.b12*m.b19*m.b22 - 96*m.b12*m.b19*m.b23 - 64*m.b12*m.b19*
                       m.b24 - 32*m.b12*m.b19*m.b25 - 288*m.b12*m.b20*m.b21 - 192*m.b12*m.b20*m.b22 - 96*m.b12*m.b20*
                       m.b23 - 64*m.b12*m.b20*m.b24 - 32*m.b12*m.b20*m.b25 - 224*m.b12*m.b21*m.b22 - 128*m.b12*m.b21*
                       m.b23 - 64*m.b12*m.b21*m.b24 - 32*m.b12*m.b21*m.b25 - 160*m.b12*m.b22*m.b23 - 64*m.b12*m.b22*
                       m.b24 - 32*m.b12*m.b22*m.b25 - 96*m.b12*m.b23*m.b24 - 32*m.b12*m.b23*m.b25 - 32*m.b12*m.b24*m.b25
                        - 704*m.b13*m.b14*m.b15 - 960*m.b13*m.b14*m.b16 - 832*m.b13*m.b14*m.b17 - 704*m.b13*m.b14*m.b18
                        - 576*m.b13*m.b14*m.b19 - 448*m.b13*m.b14*m.b20 - 352*m.b13*m.b14*m.b21 - 288*m.b13*m.b14*m.b22
                        - 224*m.b13*m.b14*m.b23 - 160*m.b13*m.b14*m.b24 - 96*m.b13*m.b14*m.b25 - 32*m.b13*m.b14*m.b26 - 
                       960*m.b13*m.b15*m.b16 - 512*m.b13*m.b15*m.b17 - 704*m.b13*m.b15*m.b18 - 576*m.b13*m.b15*m.b19 - 
                       448*m.b13*m.b15*m.b20 - 320*m.b13*m.b15*m.b21 - 256*m.b13*m.b15*m.b22 - 192*m.b13*m.b15*m.b23 - 
                       128*m.b13*m.b15*m.b24 - 64*m.b13*m.b15*m.b25 - 32*m.b13*m.b15*m.b26 - 832*m.b13*m.b16*m.b17 - 704
                       *m.b13*m.b16*m.b18 - 320*m.b13*m.b16*m.b19 - 448*m.b13*m.b16*m.b20 - 320*m.b13*m.b16*m.b21 - 224*
                       m.b13*m.b16*m.b22 - 160*m.b13*m.b16*m.b23 - 96*m.b13*m.b16*m.b24 - 64*m.b13*m.b16*m.b25 - 32*
                       m.b13*m.b16*m.b26 - 704*m.b13*m.b17*m.b18 - 576*m.b13*m.b17*m.b19 - 448*m.b13*m.b17*m.b20 - 128*
                       m.b13*m.b17*m.b21 - 192*m.b13*m.b17*m.b22 - 128*m.b13*m.b17*m.b23 - 96*m.b13*m.b17*m.b24 - 64*
                       m.b13*m.b17*m.b25 - 32*m.b13*m.b17*m.b26 - 576*m.b13*m.b18*m.b19 - 448*m.b13*m.b18*m.b20 - 320*
                       m.b13*m.b18*m.b21 - 192*m.b13*m.b18*m.b22 - 96*m.b13*m.b18*m.b24 - 64*m.b13*m.b18*m.b25 - 32*
                       m.b13*m.b18*m.b26 - 448*m.b13*m.b19*m.b20 - 320*m.b13*m.b19*m.b21 - 224*m.b13*m.b19*m.b22 - 128*
                       m.b13*m.b19*m.b23 - 96*m.b13*m.b19*m.b24 - 32*m.b13*m.b19*m.b26 - 352*m.b13*m.b20*m.b21 - 256*
                       m.b13*m.b20*m.b22 - 160*m.b13*m.b20*m.b23 - 96*m.b13*m.b20*m.b24 - 64*m.b13*m.b20*m.b25 - 32*
                       m.b13*m.b20*m.b26 - 288*m.b13*m.b21*m.b22 - 192*m.b13*m.b21*m.b23 - 96*m.b13*m.b21*m.b24 - 64*
                       m.b13*m.b21*m.b25 - 32*m.b13*m.b21*m.b26 - 224*m.b13*m.b22*m.b23 - 128*m.b13*m.b22*m.b24 - 64*
                       m.b13*m.b22*m.b25 - 32*m.b13*m.b22*m.b26 - 160*m.b13*m.b23*m.b24 - 64*m.b13*m.b23*m.b25 - 32*
                       m.b13*m.b23*m.b26 - 96*m.b13*m.b24*m.b25 - 32*m.b13*m.b24*m.b26 - 32*m.b13*m.b25*m.b26 - 704*
                       m.b14*m.b15*m.b16 - 960*m.b14*m.b15*m.b17 - 832*m.b14*m.b15*m.b18 - 704*m.b14*m.b15*m.b19 - 576*
                       m.b14*m.b15*m.b20 - 448*m.b14*m.b15*m.b21 - 352*m.b14*m.b15*m.b22 - 288*m.b14*m.b15*m.b23 - 224*
                       m.b14*m.b15*m.b24 - 160*m.b14*m.b15*m.b25 - 96*m.b14*m.b15*m.b26 - 32*m.b14*m.b15*m.b27 - 960*
                       m.b14*m.b16*m.b17 - 512*m.b14*m.b16*m.b18 - 704*m.b14*m.b16*m.b19 - 576*m.b14*m.b16*m.b20 - 448*
                       m.b14*m.b16*m.b21 - 320*m.b14*m.b16*m.b22 - 256*m.b14*m.b16*m.b23 - 192*m.b14*m.b16*m.b24 - 128*
                       m.b14*m.b16*m.b25 - 64*m.b14*m.b16*m.b26 - 32*m.b14*m.b16*m.b27 - 832*m.b14*m.b17*m.b18 - 704*
                       m.b14*m.b17*m.b19 - 320*m.b14*m.b17*m.b20 - 448*m.b14*m.b17*m.b21 - 320*m.b14*m.b17*m.b22 - 224*
                       m.b14*m.b17*m.b23 - 160*m.b14*m.b17*m.b24 - 96*m.b14*m.b17*m.b25 - 64*m.b14*m.b17*m.b26 - 32*
                       m.b14*m.b17*m.b27 - 704*m.b14*m.b18*m.b19 - 576*m.b14*m.b18*m.b20 - 448*m.b14*m.b18*m.b21 - 128*
                       m.b14*m.b18*m.b22 - 192*m.b14*m.b18*m.b23 - 128*m.b14*m.b18*m.b24 - 96*m.b14*m.b18*m.b25 - 64*
                       m.b14*m.b18*m.b26 - 32*m.b14*m.b18*m.b27 - 576*m.b14*m.b19*m.b20 - 448*m.b14*m.b19*m.b21 - 320*
                       m.b14*m.b19*m.b22 - 192*m.b14*m.b19*m.b23 - 96*m.b14*m.b19*m.b25 - 64*m.b14*m.b19*m.b26 - 32*
                       m.b14*m.b19*m.b27 - 448*m.b14*m.b20*m.b21 - 320*m.b14*m.b20*m.b22 - 224*m.b14*m.b20*m.b23 - 128*
                       m.b14*m.b20*m.b24 - 96*m.b14*m.b20*m.b25 - 32*m.b14*m.b20*m.b27 - 352*m.b14*m.b21*m.b22 - 256*
                       m.b14*m.b21*m.b23 - 160*m.b14*m.b21*m.b24 - 96*m.b14*m.b21*m.b25 - 64*m.b14*m.b21*m.b26 - 32*
                       m.b14*m.b21*m.b27 - 288*m.b14*m.b22*m.b23 - 192*m.b14*m.b22*m.b24 - 96*m.b14*m.b22*m.b25 - 64*
                       m.b14*m.b22*m.b26 - 32*m.b14*m.b22*m.b27 - 224*m.b14*m.b23*m.b24 - 128*m.b14*m.b23*m.b25 - 64*
                       m.b14*m.b23*m.b26 - 32*m.b14*m.b23*m.b27 - 160*m.b14*m.b24*m.b25 - 64*m.b14*m.b24*m.b26 - 32*
                       m.b14*m.b24*m.b27 - 96*m.b14*m.b25*m.b26 - 32*m.b14*m.b25*m.b27 - 32*m.b14*m.b26*m.b27 - 704*
                       m.b15*m.b16*m.b17 - 960*m.b15*m.b16*m.b18 - 832*m.b15*m.b16*m.b19 - 704*m.b15*m.b16*m.b20 - 576*
                       m.b15*m.b16*m.b21 - 448*m.b15*m.b16*m.b22 - 352*m.b15*m.b16*m.b23 - 288*m.b15*m.b16*m.b24 - 224*
                       m.b15*m.b16*m.b25 - 160*m.b15*m.b16*m.b26 - 96*m.b15*m.b16*m.b27 - 32*m.b15*m.b16*m.b28 - 960*
                       m.b15*m.b17*m.b18 - 512*m.b15*m.b17*m.b19 - 704*m.b15*m.b17*m.b20 - 576*m.b15*m.b17*m.b21 - 448*
                       m.b15*m.b17*m.b22 - 320*m.b15*m.b17*m.b23 - 256*m.b15*m.b17*m.b24 - 192*m.b15*m.b17*m.b25 - 128*
                       m.b15*m.b17*m.b26 - 64*m.b15*m.b17*m.b27 - 32*m.b15*m.b17*m.b28 - 832*m.b15*m.b18*m.b19 - 704*
                       m.b15*m.b18*m.b20 - 320*m.b15*m.b18*m.b21 - 448*m.b15*m.b18*m.b22 - 320*m.b15*m.b18*m.b23 - 224*
                       m.b15*m.b18*m.b24 - 160*m.b15*m.b18*m.b25 - 96*m.b15*m.b18*m.b26 - 64*m.b15*m.b18*m.b27 - 32*
                       m.b15*m.b18*m.b28 - 704*m.b15*m.b19*m.b20 - 576*m.b15*m.b19*m.b21 - 448*m.b15*m.b19*m.b22 - 128*
                       m.b15*m.b19*m.b23 - 192*m.b15*m.b19*m.b24 - 128*m.b15*m.b19*m.b25 - 96*m.b15*m.b19*m.b26 - 64*
                       m.b15*m.b19*m.b27 - 32*m.b15*m.b19*m.b28 - 576*m.b15*m.b20*m.b21 - 448*m.b15*m.b20*m.b22 - 320*
                       m.b15*m.b20*m.b23 - 192*m.b15*m.b20*m.b24 - 96*m.b15*m.b20*m.b26 - 64*m.b15*m.b20*m.b27 - 32*
                       m.b15*m.b20*m.b28 - 448*m.b15*m.b21*m.b22 - 320*m.b15*m.b21*m.b23 - 224*m.b15*m.b21*m.b24 - 128*
                       m.b15*m.b21*m.b25 - 96*m.b15*m.b21*m.b26 - 32*m.b15*m.b21*m.b28 - 352*m.b15*m.b22*m.b23 - 256*
                       m.b15*m.b22*m.b24 - 160*m.b15*m.b22*m.b25 - 96*m.b15*m.b22*m.b26 - 64*m.b15*m.b22*m.b27 - 32*
                       m.b15*m.b22*m.b28 - 288*m.b15*m.b23*m.b24 - 192*m.b15*m.b23*m.b25 - 96*m.b15*m.b23*m.b26 - 64*
                       m.b15*m.b23*m.b27 - 32*m.b15*m.b23*m.b28 - 224*m.b15*m.b24*m.b25 - 128*m.b15*m.b24*m.b26 - 64*
                       m.b15*m.b24*m.b27 - 32*m.b15*m.b24*m.b28 - 160*m.b15*m.b25*m.b26 - 64*m.b15*m.b25*m.b27 - 32*
                       m.b15*m.b25*m.b28 - 96*m.b15*m.b26*m.b27 - 32*m.b15*m.b26*m.b28 - 32*m.b15*m.b27*m.b28 - 704*
                       m.b16*m.b17*m.b18 - 960*m.b16*m.b17*m.b19 - 832*m.b16*m.b17*m.b20 - 704*m.b16*m.b17*m.b21 - 576*
                       m.b16*m.b17*m.b22 - 448*m.b16*m.b17*m.b23 - 352*m.b16*m.b17*m.b24 - 288*m.b16*m.b17*m.b25 - 224*
                       m.b16*m.b17*m.b26 - 160*m.b16*m.b17*m.b27 - 96*m.b16*m.b17*m.b28 - 32*m.b16*m.b17*m.b29 - 960*
                       m.b16*m.b18*m.b19 - 512*m.b16*m.b18*m.b20 - 704*m.b16*m.b18*m.b21 - 576*m.b16*m.b18*m.b22 - 448*
                       m.b16*m.b18*m.b23 - 320*m.b16*m.b18*m.b24 - 256*m.b16*m.b18*m.b25 - 192*m.b16*m.b18*m.b26 - 128*
                       m.b16*m.b18*m.b27 - 64*m.b16*m.b18*m.b28 - 32*m.b16*m.b18*m.b29 - 832*m.b16*m.b19*m.b20 - 704*
                       m.b16*m.b19*m.b21 - 320*m.b16*m.b19*m.b22 - 448*m.b16*m.b19*m.b23 - 320*m.b16*m.b19*m.b24 - 224*
                       m.b16*m.b19*m.b25 - 160*m.b16*m.b19*m.b26 - 96*m.b16*m.b19*m.b27 - 64*m.b16*m.b19*m.b28 - 32*
                       m.b16*m.b19*m.b29 - 704*m.b16*m.b20*m.b21 - 576*m.b16*m.b20*m.b22 - 448*m.b16*m.b20*m.b23 - 128*
                       m.b16*m.b20*m.b24 - 192*m.b16*m.b20*m.b25 - 128*m.b16*m.b20*m.b26 - 96*m.b16*m.b20*m.b27 - 64*
                       m.b16*m.b20*m.b28 - 32*m.b16*m.b20*m.b29 - 576*m.b16*m.b21*m.b22 - 448*m.b16*m.b21*m.b23 - 320*
                       m.b16*m.b21*m.b24 - 192*m.b16*m.b21*m.b25 - 96*m.b16*m.b21*m.b27 - 64*m.b16*m.b21*m.b28 - 32*
                       m.b16*m.b21*m.b29 - 448*m.b16*m.b22*m.b23 - 320*m.b16*m.b22*m.b24 - 224*m.b16*m.b22*m.b25 - 128*
                       m.b16*m.b22*m.b26 - 96*m.b16*m.b22*m.b27 - 32*m.b16*m.b22*m.b29 - 352*m.b16*m.b23*m.b24 - 256*
                       m.b16*m.b23*m.b25 - 160*m.b16*m.b23*m.b26 - 96*m.b16*m.b23*m.b27 - 64*m.b16*m.b23*m.b28 - 32*
                       m.b16*m.b23*m.b29 - 288*m.b16*m.b24*m.b25 - 192*m.b16*m.b24*m.b26 - 96*m.b16*m.b24*m.b27 - 64*
                       m.b16*m.b24*m.b28 - 32*m.b16*m.b24*m.b29 - 224*m.b16*m.b25*m.b26 - 128*m.b16*m.b25*m.b27 - 64*
                       m.b16*m.b25*m.b28 - 32*m.b16*m.b25*m.b29 - 160*m.b16*m.b26*m.b27 - 64*m.b16*m.b26*m.b28 - 32*
                       m.b16*m.b26*m.b29 - 96*m.b16*m.b27*m.b28 - 32*m.b16*m.b27*m.b29 - 32*m.b16*m.b28*m.b29 - 704*
                       m.b17*m.b18*m.b19 - 960*m.b17*m.b18*m.b20 - 832*m.b17*m.b18*m.b21 - 704*m.b17*m.b18*m.b22 - 576*
                       m.b17*m.b18*m.b23 - 448*m.b17*m.b18*m.b24 - 352*m.b17*m.b18*m.b25 - 288*m.b17*m.b18*m.b26 - 224*
                       m.b17*m.b18*m.b27 - 160*m.b17*m.b18*m.b28 - 96*m.b17*m.b18*m.b29 - 32*m.b17*m.b18*m.b30 - 960*
                       m.b17*m.b19*m.b20 - 512*m.b17*m.b19*m.b21 - 704*m.b17*m.b19*m.b22 - 576*m.b17*m.b19*m.b23 - 448*
                       m.b17*m.b19*m.b24 - 320*m.b17*m.b19*m.b25 - 256*m.b17*m.b19*m.b26 - 192*m.b17*m.b19*m.b27 - 128*
                       m.b17*m.b19*m.b28 - 64*m.b17*m.b19*m.b29 - 32*m.b17*m.b19*m.b30 - 832*m.b17*m.b20*m.b21 - 704*
                       m.b17*m.b20*m.b22 - 320*m.b17*m.b20*m.b23 - 448*m.b17*m.b20*m.b24 - 320*m.b17*m.b20*m.b25 - 224*
                       m.b17*m.b20*m.b26 - 160*m.b17*m.b20*m.b27 - 96*m.b17*m.b20*m.b28 - 64*m.b17*m.b20*m.b29 - 32*
                       m.b17*m.b20*m.b30 - 704*m.b17*m.b21*m.b22 - 576*m.b17*m.b21*m.b23 - 448*m.b17*m.b21*m.b24 - 128*
                       m.b17*m.b21*m.b25 - 192*m.b17*m.b21*m.b26 - 128*m.b17*m.b21*m.b27 - 96*m.b17*m.b21*m.b28 - 64*
                       m.b17*m.b21*m.b29 - 32*m.b17*m.b21*m.b30 - 576*m.b17*m.b22*m.b23 - 448*m.b17*m.b22*m.b24 - 320*
                       m.b17*m.b22*m.b25 - 192*m.b17*m.b22*m.b26 - 96*m.b17*m.b22*m.b28 - 64*m.b17*m.b22*m.b29 - 32*
                       m.b17*m.b22*m.b30 - 448*m.b17*m.b23*m.b24 - 320*m.b17*m.b23*m.b25 - 224*m.b17*m.b23*m.b26 - 128*
                       m.b17*m.b23*m.b27 - 96*m.b17*m.b23*m.b28 - 32*m.b17*m.b23*m.b30 - 352*m.b17*m.b24*m.b25 - 256*
                       m.b17*m.b24*m.b26 - 160*m.b17*m.b24*m.b27 - 96*m.b17*m.b24*m.b28 - 64*m.b17*m.b24*m.b29 - 32*
                       m.b17*m.b24*m.b30 - 288*m.b17*m.b25*m.b26 - 192*m.b17*m.b25*m.b27 - 96*m.b17*m.b25*m.b28 - 64*
                       m.b17*m.b25*m.b29 - 32*m.b17*m.b25*m.b30 - 224*m.b17*m.b26*m.b27 - 128*m.b17*m.b26*m.b28 - 64*
                       m.b17*m.b26*m.b29 - 32*m.b17*m.b26*m.b30 - 160*m.b17*m.b27*m.b28 - 64*m.b17*m.b27*m.b29 - 32*
                       m.b17*m.b27*m.b30 - 96*m.b17*m.b28*m.b29 - 32*m.b17*m.b28*m.b30 - 32*m.b17*m.b29*m.b30 - 704*
                       m.b18*m.b19*m.b20 - 960*m.b18*m.b19*m.b21 - 832*m.b18*m.b19*m.b22 - 704*m.b18*m.b19*m.b23 - 576*
                       m.b18*m.b19*m.b24 - 448*m.b18*m.b19*m.b25 - 352*m.b18*m.b19*m.b26 - 288*m.b18*m.b19*m.b27 - 224*
                       m.b18*m.b19*m.b28 - 160*m.b18*m.b19*m.b29 - 96*m.b18*m.b19*m.b30 - 32*m.b18*m.b19*m.b31 - 960*
                       m.b18*m.b20*m.b21 - 512*m.b18*m.b20*m.b22 - 704*m.b18*m.b20*m.b23 - 576*m.b18*m.b20*m.b24 - 448*
                       m.b18*m.b20*m.b25 - 320*m.b18*m.b20*m.b26 - 256*m.b18*m.b20*m.b27 - 192*m.b18*m.b20*m.b28 - 128*
                       m.b18*m.b20*m.b29 - 64*m.b18*m.b20*m.b30 - 32*m.b18*m.b20*m.b31 - 832*m.b18*m.b21*m.b22 - 704*
                       m.b18*m.b21*m.b23 - 320*m.b18*m.b21*m.b24 - 448*m.b18*m.b21*m.b25 - 320*m.b18*m.b21*m.b26 - 224*
                       m.b18*m.b21*m.b27 - 160*m.b18*m.b21*m.b28 - 96*m.b18*m.b21*m.b29 - 64*m.b18*m.b21*m.b30 - 32*
                       m.b18*m.b21*m.b31 - 704*m.b18*m.b22*m.b23 - 576*m.b18*m.b22*m.b24 - 448*m.b18*m.b22*m.b25 - 128*
                       m.b18*m.b22*m.b26 - 192*m.b18*m.b22*m.b27 - 128*m.b18*m.b22*m.b28 - 96*m.b18*m.b22*m.b29 - 64*
                       m.b18*m.b22*m.b30 - 32*m.b18*m.b22*m.b31 - 576*m.b18*m.b23*m.b24 - 448*m.b18*m.b23*m.b25 - 320*
                       m.b18*m.b23*m.b26 - 192*m.b18*m.b23*m.b27 - 96*m.b18*m.b23*m.b29 - 64*m.b18*m.b23*m.b30 - 32*
                       m.b18*m.b23*m.b31 - 448*m.b18*m.b24*m.b25 - 320*m.b18*m.b24*m.b26 - 224*m.b18*m.b24*m.b27 - 128*
                       m.b18*m.b24*m.b28 - 96*m.b18*m.b24*m.b29 - 32*m.b18*m.b24*m.b31 - 352*m.b18*m.b25*m.b26 - 256*
                       m.b18*m.b25*m.b27 - 160*m.b18*m.b25*m.b28 - 96*m.b18*m.b25*m.b29 - 64*m.b18*m.b25*m.b30 - 32*
                       m.b18*m.b25*m.b31 - 288*m.b18*m.b26*m.b27 - 192*m.b18*m.b26*m.b28 - 96*m.b18*m.b26*m.b29 - 64*
                       m.b18*m.b26*m.b30 - 32*m.b18*m.b26*m.b31 - 224*m.b18*m.b27*m.b28 - 128*m.b18*m.b27*m.b29 - 64*
                       m.b18*m.b27*m.b30 - 32*m.b18*m.b27*m.b31 - 160*m.b18*m.b28*m.b29 - 64*m.b18*m.b28*m.b30 - 32*
                       m.b18*m.b28*m.b31 - 96*m.b18*m.b29*m.b30 - 32*m.b18*m.b29*m.b31 - 32*m.b18*m.b30*m.b31 - 704*
                       m.b19*m.b20*m.b21 - 960*m.b19*m.b20*m.b22 - 832*m.b19*m.b20*m.b23 - 704*m.b19*m.b20*m.b24 - 576*
                       m.b19*m.b20*m.b25 - 448*m.b19*m.b20*m.b26 - 352*m.b19*m.b20*m.b27 - 288*m.b19*m.b20*m.b28 - 224*
                       m.b19*m.b20*m.b29 - 160*m.b19*m.b20*m.b30 - 96*m.b19*m.b20*m.b31 - 32*m.b19*m.b20*m.b32 - 960*
                       m.b19*m.b21*m.b22 - 512*m.b19*m.b21*m.b23 - 704*m.b19*m.b21*m.b24 - 576*m.b19*m.b21*m.b25 - 448*
                       m.b19*m.b21*m.b26 - 320*m.b19*m.b21*m.b27 - 256*m.b19*m.b21*m.b28 - 192*m.b19*m.b21*m.b29 - 128*
                       m.b19*m.b21*m.b30 - 64*m.b19*m.b21*m.b31 - 32*m.b19*m.b21*m.b32 - 832*m.b19*m.b22*m.b23 - 704*
                       m.b19*m.b22*m.b24 - 320*m.b19*m.b22*m.b25 - 448*m.b19*m.b22*m.b26 - 320*m.b19*m.b22*m.b27 - 224*
                       m.b19*m.b22*m.b28 - 160*m.b19*m.b22*m.b29 - 96*m.b19*m.b22*m.b30 - 64*m.b19*m.b22*m.b31 - 32*
                       m.b19*m.b22*m.b32 - 704*m.b19*m.b23*m.b24 - 576*m.b19*m.b23*m.b25 - 448*m.b19*m.b23*m.b26 - 128*
                       m.b19*m.b23*m.b27 - 192*m.b19*m.b23*m.b28 - 128*m.b19*m.b23*m.b29 - 96*m.b19*m.b23*m.b30 - 64*
                       m.b19*m.b23*m.b31 - 32*m.b19*m.b23*m.b32 - 576*m.b19*m.b24*m.b25 - 448*m.b19*m.b24*m.b26 - 320*
                       m.b19*m.b24*m.b27 - 192*m.b19*m.b24*m.b28 - 96*m.b19*m.b24*m.b30 - 64*m.b19*m.b24*m.b31 - 32*
                       m.b19*m.b24*m.b32 - 448*m.b19*m.b25*m.b26 - 320*m.b19*m.b25*m.b27 - 224*m.b19*m.b25*m.b28 - 128*
                       m.b19*m.b25*m.b29 - 96*m.b19*m.b25*m.b30 - 32*m.b19*m.b25*m.b32 - 352*m.b19*m.b26*m.b27 - 256*
                       m.b19*m.b26*m.b28 - 160*m.b19*m.b26*m.b29 - 96*m.b19*m.b26*m.b30 - 64*m.b19*m.b26*m.b31 - 32*
                       m.b19*m.b26*m.b32 - 288*m.b19*m.b27*m.b28 - 192*m.b19*m.b27*m.b29 - 96*m.b19*m.b27*m.b30 - 64*
                       m.b19*m.b27*m.b31 - 32*m.b19*m.b27*m.b32 - 224*m.b19*m.b28*m.b29 - 128*m.b19*m.b28*m.b30 - 64*
                       m.b19*m.b28*m.b31 - 32*m.b19*m.b28*m.b32 - 160*m.b19*m.b29*m.b30 - 64*m.b19*m.b29*m.b31 - 32*
                       m.b19*m.b29*m.b32 - 96*m.b19*m.b30*m.b31 - 32*m.b19*m.b30*m.b32 - 32*m.b19*m.b31*m.b32 - 704*
                       m.b20*m.b21*m.b22 - 960*m.b20*m.b21*m.b23 - 832*m.b20*m.b21*m.b24 - 704*m.b20*m.b21*m.b25 - 576*
                       m.b20*m.b21*m.b26 - 448*m.b20*m.b21*m.b27 - 352*m.b20*m.b21*m.b28 - 288*m.b20*m.b21*m.b29 - 224*
                       m.b20*m.b21*m.b30 - 160*m.b20*m.b21*m.b31 - 96*m.b20*m.b21*m.b32 - 32*m.b20*m.b21*m.b33 - 960*
                       m.b20*m.b22*m.b23 - 512*m.b20*m.b22*m.b24 - 704*m.b20*m.b22*m.b25 - 576*m.b20*m.b22*m.b26 - 448*
                       m.b20*m.b22*m.b27 - 320*m.b20*m.b22*m.b28 - 256*m.b20*m.b22*m.b29 - 192*m.b20*m.b22*m.b30 - 128*
                       m.b20*m.b22*m.b31 - 64*m.b20*m.b22*m.b32 - 32*m.b20*m.b22*m.b33 - 832*m.b20*m.b23*m.b24 - 704*
                       m.b20*m.b23*m.b25 - 320*m.b20*m.b23*m.b26 - 448*m.b20*m.b23*m.b27 - 320*m.b20*m.b23*m.b28 - 224*
                       m.b20*m.b23*m.b29 - 160*m.b20*m.b23*m.b30 - 96*m.b20*m.b23*m.b31 - 64*m.b20*m.b23*m.b32 - 32*
                       m.b20*m.b23*m.b33 - 704*m.b20*m.b24*m.b25 - 576*m.b20*m.b24*m.b26 - 448*m.b20*m.b24*m.b27 - 128*
                       m.b20*m.b24*m.b28 - 192*m.b20*m.b24*m.b29 - 128*m.b20*m.b24*m.b30 - 96*m.b20*m.b24*m.b31 - 64*
                       m.b20*m.b24*m.b32 - 32*m.b20*m.b24*m.b33 - 576*m.b20*m.b25*m.b26 - 448*m.b20*m.b25*m.b27 - 320*
                       m.b20*m.b25*m.b28 - 192*m.b20*m.b25*m.b29 - 96*m.b20*m.b25*m.b31 - 64*m.b20*m.b25*m.b32 - 32*
                       m.b20*m.b25*m.b33 - 448*m.b20*m.b26*m.b27 - 320*m.b20*m.b26*m.b28 - 224*m.b20*m.b26*m.b29 - 128*
                       m.b20*m.b26*m.b30 - 96*m.b20*m.b26*m.b31 - 32*m.b20*m.b26*m.b33 - 352*m.b20*m.b27*m.b28 - 256*
                       m.b20*m.b27*m.b29 - 160*m.b20*m.b27*m.b30 - 96*m.b20*m.b27*m.b31 - 64*m.b20*m.b27*m.b32 - 32*
                       m.b20*m.b27*m.b33 - 288*m.b20*m.b28*m.b29 - 192*m.b20*m.b28*m.b30 - 96*m.b20*m.b28*m.b31 - 64*
                       m.b20*m.b28*m.b32 - 32*m.b20*m.b28*m.b33 - 224*m.b20*m.b29*m.b30 - 128*m.b20*m.b29*m.b31 - 64*
                       m.b20*m.b29*m.b32 - 32*m.b20*m.b29*m.b33 - 160*m.b20*m.b30*m.b31 - 64*m.b20*m.b30*m.b32 - 32*
                       m.b20*m.b30*m.b33 - 96*m.b20*m.b31*m.b32 - 32*m.b20*m.b31*m.b33 - 32*m.b20*m.b32*m.b33 - 704*
                       m.b21*m.b22*m.b23 - 960*m.b21*m.b22*m.b24 - 832*m.b21*m.b22*m.b25 - 704*m.b21*m.b22*m.b26 - 576*
                       m.b21*m.b22*m.b27 - 448*m.b21*m.b22*m.b28 - 352*m.b21*m.b22*m.b29 - 288*m.b21*m.b22*m.b30 - 224*
                       m.b21*m.b22*m.b31 - 160*m.b21*m.b22*m.b32 - 96*m.b21*m.b22*m.b33 - 32*m.b21*m.b22*m.b34 - 960*
                       m.b21*m.b23*m.b24 - 512*m.b21*m.b23*m.b25 - 704*m.b21*m.b23*m.b26 - 576*m.b21*m.b23*m.b27 - 448*
                       m.b21*m.b23*m.b28 - 320*m.b21*m.b23*m.b29 - 256*m.b21*m.b23*m.b30 - 192*m.b21*m.b23*m.b31 - 128*
                       m.b21*m.b23*m.b32 - 64*m.b21*m.b23*m.b33 - 32*m.b21*m.b23*m.b34 - 832*m.b21*m.b24*m.b25 - 704*
                       m.b21*m.b24*m.b26 - 320*m.b21*m.b24*m.b27 - 448*m.b21*m.b24*m.b28 - 320*m.b21*m.b24*m.b29 - 224*
                       m.b21*m.b24*m.b30 - 160*m.b21*m.b24*m.b31 - 96*m.b21*m.b24*m.b32 - 64*m.b21*m.b24*m.b33 - 32*
                       m.b21*m.b24*m.b34 - 704*m.b21*m.b25*m.b26 - 576*m.b21*m.b25*m.b27 - 448*m.b21*m.b25*m.b28 - 128*
                       m.b21*m.b25*m.b29 - 192*m.b21*m.b25*m.b30 - 128*m.b21*m.b25*m.b31 - 96*m.b21*m.b25*m.b32 - 64*
                       m.b21*m.b25*m.b33 - 32*m.b21*m.b25*m.b34 - 576*m.b21*m.b26*m.b27 - 448*m.b21*m.b26*m.b28 - 320*
                       m.b21*m.b26*m.b29 - 192*m.b21*m.b26*m.b30 - 96*m.b21*m.b26*m.b32 - 64*m.b21*m.b26*m.b33 - 32*
                       m.b21*m.b26*m.b34 - 448*m.b21*m.b27*m.b28 - 320*m.b21*m.b27*m.b29 - 224*m.b21*m.b27*m.b30 - 128*
                       m.b21*m.b27*m.b31 - 96*m.b21*m.b27*m.b32 - 32*m.b21*m.b27*m.b34 - 352*m.b21*m.b28*m.b29 - 256*
                       m.b21*m.b28*m.b30 - 160*m.b21*m.b28*m.b31 - 96*m.b21*m.b28*m.b32 - 64*m.b21*m.b28*m.b33 - 32*
                       m.b21*m.b28*m.b34 - 288*m.b21*m.b29*m.b30 - 192*m.b21*m.b29*m.b31 - 96*m.b21*m.b29*m.b32 - 64*
                       m.b21*m.b29*m.b33 - 32*m.b21*m.b29*m.b34 - 224*m.b21*m.b30*m.b31 - 128*m.b21*m.b30*m.b32 - 64*
                       m.b21*m.b30*m.b33 - 32*m.b21*m.b30*m.b34 - 160*m.b21*m.b31*m.b32 - 64*m.b21*m.b31*m.b33 - 32*
                       m.b21*m.b31*m.b34 - 96*m.b21*m.b32*m.b33 - 32*m.b21*m.b32*m.b34 - 32*m.b21*m.b33*m.b34 - 704*
                       m.b22*m.b23*m.b24 - 960*m.b22*m.b23*m.b25 - 832*m.b22*m.b23*m.b26 - 704*m.b22*m.b23*m.b27 - 576*
                       m.b22*m.b23*m.b28 - 448*m.b22*m.b23*m.b29 - 352*m.b22*m.b23*m.b30 - 288*m.b22*m.b23*m.b31 - 224*
                       m.b22*m.b23*m.b32 - 160*m.b22*m.b23*m.b33 - 96*m.b22*m.b23*m.b34 - 32*m.b22*m.b23*m.b35 - 960*
                       m.b22*m.b24*m.b25 - 512*m.b22*m.b24*m.b26 - 704*m.b22*m.b24*m.b27 - 576*m.b22*m.b24*m.b28 - 448*
                       m.b22*m.b24*m.b29 - 320*m.b22*m.b24*m.b30 - 256*m.b22*m.b24*m.b31 - 192*m.b22*m.b24*m.b32 - 128*
                       m.b22*m.b24*m.b33 - 64*m.b22*m.b24*m.b34 - 32*m.b22*m.b24*m.b35 - 832*m.b22*m.b25*m.b26 - 704*
                       m.b22*m.b25*m.b27 - 320*m.b22*m.b25*m.b28 - 448*m.b22*m.b25*m.b29 - 320*m.b22*m.b25*m.b30 - 224*
                       m.b22*m.b25*m.b31 - 160*m.b22*m.b25*m.b32 - 96*m.b22*m.b25*m.b33 - 64*m.b22*m.b25*m.b34 - 32*
                       m.b22*m.b25*m.b35 - 704*m.b22*m.b26*m.b27 - 576*m.b22*m.b26*m.b28 - 448*m.b22*m.b26*m.b29 - 128*
                       m.b22*m.b26*m.b30 - 192*m.b22*m.b26*m.b31 - 128*m.b22*m.b26*m.b32 - 96*m.b22*m.b26*m.b33 - 64*
                       m.b22*m.b26*m.b34 - 32*m.b22*m.b26*m.b35 - 576*m.b22*m.b27*m.b28 - 448*m.b22*m.b27*m.b29 - 320*
                       m.b22*m.b27*m.b30 - 192*m.b22*m.b27*m.b31 - 96*m.b22*m.b27*m.b33 - 64*m.b22*m.b27*m.b34 - 32*
                       m.b22*m.b27*m.b35 - 448*m.b22*m.b28*m.b29 - 320*m.b22*m.b28*m.b30 - 224*m.b22*m.b28*m.b31 - 128*
                       m.b22*m.b28*m.b32 - 96*m.b22*m.b28*m.b33 - 32*m.b22*m.b28*m.b35 - 352*m.b22*m.b29*m.b30 - 256*
                       m.b22*m.b29*m.b31 - 160*m.b22*m.b29*m.b32 - 96*m.b22*m.b29*m.b33 - 64*m.b22*m.b29*m.b34 - 32*
                       m.b22*m.b29*m.b35 - 288*m.b22*m.b30*m.b31 - 192*m.b22*m.b30*m.b32 - 96*m.b22*m.b30*m.b33 - 64*
                       m.b22*m.b30*m.b34 - 32*m.b22*m.b30*m.b35 - 224*m.b22*m.b31*m.b32 - 128*m.b22*m.b31*m.b33 - 64*
                       m.b22*m.b31*m.b34 - 32*m.b22*m.b31*m.b35 - 160*m.b22*m.b32*m.b33 - 64*m.b22*m.b32*m.b34 - 32*
                       m.b22*m.b32*m.b35 - 96*m.b22*m.b33*m.b34 - 32*m.b22*m.b33*m.b35 - 32*m.b22*m.b34*m.b35 - 704*
                       m.b23*m.b24*m.b25 - 960*m.b23*m.b24*m.b26 - 832*m.b23*m.b24*m.b27 - 704*m.b23*m.b24*m.b28 - 576*
                       m.b23*m.b24*m.b29 - 448*m.b23*m.b24*m.b30 - 352*m.b23*m.b24*m.b31 - 288*m.b23*m.b24*m.b32 - 224*
                       m.b23*m.b24*m.b33 - 160*m.b23*m.b24*m.b34 - 96*m.b23*m.b24*m.b35 - 32*m.b23*m.b24*m.b36 - 960*
                       m.b23*m.b25*m.b26 - 512*m.b23*m.b25*m.b27 - 704*m.b23*m.b25*m.b28 - 576*m.b23*m.b25*m.b29 - 448*
                       m.b23*m.b25*m.b30 - 320*m.b23*m.b25*m.b31 - 256*m.b23*m.b25*m.b32 - 192*m.b23*m.b25*m.b33 - 128*
                       m.b23*m.b25*m.b34 - 64*m.b23*m.b25*m.b35 - 32*m.b23*m.b25*m.b36 - 832*m.b23*m.b26*m.b27 - 704*
                       m.b23*m.b26*m.b28 - 320*m.b23*m.b26*m.b29 - 448*m.b23*m.b26*m.b30 - 320*m.b23*m.b26*m.b31 - 224*
                       m.b23*m.b26*m.b32 - 160*m.b23*m.b26*m.b33 - 96*m.b23*m.b26*m.b34 - 64*m.b23*m.b26*m.b35 - 32*
                       m.b23*m.b26*m.b36 - 704*m.b23*m.b27*m.b28 - 576*m.b23*m.b27*m.b29 - 448*m.b23*m.b27*m.b30 - 128*
                       m.b23*m.b27*m.b31 - 192*m.b23*m.b27*m.b32 - 128*m.b23*m.b27*m.b33 - 96*m.b23*m.b27*m.b34 - 64*
                       m.b23*m.b27*m.b35 - 32*m.b23*m.b27*m.b36 - 576*m.b23*m.b28*m.b29 - 448*m.b23*m.b28*m.b30 - 320*
                       m.b23*m.b28*m.b31 - 192*m.b23*m.b28*m.b32 - 96*m.b23*m.b28*m.b34 - 64*m.b23*m.b28*m.b35 - 32*
                       m.b23*m.b28*m.b36 - 448*m.b23*m.b29*m.b30 - 320*m.b23*m.b29*m.b31 - 224*m.b23*m.b29*m.b32 - 128*
                       m.b23*m.b29*m.b33 - 96*m.b23*m.b29*m.b34 - 32*m.b23*m.b29*m.b36 - 352*m.b23*m.b30*m.b31 - 256*
                       m.b23*m.b30*m.b32 - 160*m.b23*m.b30*m.b33 - 96*m.b23*m.b30*m.b34 - 64*m.b23*m.b30*m.b35 - 32*
                       m.b23*m.b30*m.b36 - 288*m.b23*m.b31*m.b32 - 192*m.b23*m.b31*m.b33 - 96*m.b23*m.b31*m.b34 - 64*
                       m.b23*m.b31*m.b35 - 32*m.b23*m.b31*m.b36 - 224*m.b23*m.b32*m.b33 - 128*m.b23*m.b32*m.b34 - 64*
                       m.b23*m.b32*m.b35 - 32*m.b23*m.b32*m.b36 - 160*m.b23*m.b33*m.b34 - 64*m.b23*m.b33*m.b35 - 32*
                       m.b23*m.b33*m.b36 - 96*m.b23*m.b34*m.b35 - 32*m.b23*m.b34*m.b36 - 32*m.b23*m.b35*m.b36 - 704*
                       m.b24*m.b25*m.b26 - 960*m.b24*m.b25*m.b27 - 832*m.b24*m.b25*m.b28 - 704*m.b24*m.b25*m.b29 - 576*
                       m.b24*m.b25*m.b30 - 448*m.b24*m.b25*m.b31 - 352*m.b24*m.b25*m.b32 - 288*m.b24*m.b25*m.b33 - 224*
                       m.b24*m.b25*m.b34 - 160*m.b24*m.b25*m.b35 - 96*m.b24*m.b25*m.b36 - 32*m.b24*m.b25*m.b37 - 960*
                       m.b24*m.b26*m.b27 - 512*m.b24*m.b26*m.b28 - 704*m.b24*m.b26*m.b29 - 576*m.b24*m.b26*m.b30 - 448*
                       m.b24*m.b26*m.b31 - 320*m.b24*m.b26*m.b32 - 256*m.b24*m.b26*m.b33 - 192*m.b24*m.b26*m.b34 - 128*
                       m.b24*m.b26*m.b35 - 64*m.b24*m.b26*m.b36 - 32*m.b24*m.b26*m.b37 - 832*m.b24*m.b27*m.b28 - 704*
                       m.b24*m.b27*m.b29 - 320*m.b24*m.b27*m.b30 - 448*m.b24*m.b27*m.b31 - 320*m.b24*m.b27*m.b32 - 224*
                       m.b24*m.b27*m.b33 - 160*m.b24*m.b27*m.b34 - 96*m.b24*m.b27*m.b35 - 64*m.b24*m.b27*m.b36 - 32*
                       m.b24*m.b27*m.b37 - 704*m.b24*m.b28*m.b29 - 576*m.b24*m.b28*m.b30 - 448*m.b24*m.b28*m.b31 - 128*
                       m.b24*m.b28*m.b32 - 192*m.b24*m.b28*m.b33 - 128*m.b24*m.b28*m.b34 - 96*m.b24*m.b28*m.b35 - 64*
                       m.b24*m.b28*m.b36 - 32*m.b24*m.b28*m.b37 - 576*m.b24*m.b29*m.b30 - 448*m.b24*m.b29*m.b31 - 320*
                       m.b24*m.b29*m.b32 - 192*m.b24*m.b29*m.b33 - 96*m.b24*m.b29*m.b35 - 64*m.b24*m.b29*m.b36 - 32*
                       m.b24*m.b29*m.b37 - 448*m.b24*m.b30*m.b31 - 320*m.b24*m.b30*m.b32 - 224*m.b24*m.b30*m.b33 - 128*
                       m.b24*m.b30*m.b34 - 96*m.b24*m.b30*m.b35 - 32*m.b24*m.b30*m.b37 - 352*m.b24*m.b31*m.b32 - 256*
                       m.b24*m.b31*m.b33 - 160*m.b24*m.b31*m.b34 - 96*m.b24*m.b31*m.b35 - 64*m.b24*m.b31*m.b36 - 32*
                       m.b24*m.b31*m.b37 - 288*m.b24*m.b32*m.b33 - 192*m.b24*m.b32*m.b34 - 96*m.b24*m.b32*m.b35 - 64*
                       m.b24*m.b32*m.b36 - 32*m.b24*m.b32*m.b37 - 224*m.b24*m.b33*m.b34 - 128*m.b24*m.b33*m.b35 - 64*
                       m.b24*m.b33*m.b36 - 32*m.b24*m.b33*m.b37 - 160*m.b24*m.b34*m.b35 - 64*m.b24*m.b34*m.b36 - 32*
                       m.b24*m.b34*m.b37 - 96*m.b24*m.b35*m.b36 - 32*m.b24*m.b35*m.b37 - 32*m.b24*m.b36*m.b37 - 704*
                       m.b25*m.b26*m.b27 - 960*m.b25*m.b26*m.b28 - 832*m.b25*m.b26*m.b29 - 704*m.b25*m.b26*m.b30 - 576*
                       m.b25*m.b26*m.b31 - 448*m.b25*m.b26*m.b32 - 352*m.b25*m.b26*m.b33 - 288*m.b25*m.b26*m.b34 - 224*
                       m.b25*m.b26*m.b35 - 160*m.b25*m.b26*m.b36 - 96*m.b25*m.b26*m.b37 - 32*m.b25*m.b26*m.b38 - 960*
                       m.b25*m.b27*m.b28 - 512*m.b25*m.b27*m.b29 - 704*m.b25*m.b27*m.b30 - 576*m.b25*m.b27*m.b31 - 448*
                       m.b25*m.b27*m.b32 - 320*m.b25*m.b27*m.b33 - 256*m.b25*m.b27*m.b34 - 192*m.b25*m.b27*m.b35 - 128*
                       m.b25*m.b27*m.b36 - 64*m.b25*m.b27*m.b37 - 32*m.b25*m.b27*m.b38 - 832*m.b25*m.b28*m.b29 - 704*
                       m.b25*m.b28*m.b30 - 320*m.b25*m.b28*m.b31 - 448*m.b25*m.b28*m.b32 - 320*m.b25*m.b28*m.b33 - 224*
                       m.b25*m.b28*m.b34 - 160*m.b25*m.b28*m.b35 - 96*m.b25*m.b28*m.b36 - 64*m.b25*m.b28*m.b37 - 32*
                       m.b25*m.b28*m.b38 - 704*m.b25*m.b29*m.b30 - 576*m.b25*m.b29*m.b31 - 448*m.b25*m.b29*m.b32 - 128*
                       m.b25*m.b29*m.b33 - 192*m.b25*m.b29*m.b34 - 128*m.b25*m.b29*m.b35 - 96*m.b25*m.b29*m.b36 - 64*
                       m.b25*m.b29*m.b37 - 32*m.b25*m.b29*m.b38 - 576*m.b25*m.b30*m.b31 - 448*m.b25*m.b30*m.b32 - 320*
                       m.b25*m.b30*m.b33 - 192*m.b25*m.b30*m.b34 - 96*m.b25*m.b30*m.b36 - 64*m.b25*m.b30*m.b37 - 32*
                       m.b25*m.b30*m.b38 - 448*m.b25*m.b31*m.b32 - 320*m.b25*m.b31*m.b33 - 224*m.b25*m.b31*m.b34 - 128*
                       m.b25*m.b31*m.b35 - 96*m.b25*m.b31*m.b36 - 32*m.b25*m.b31*m.b38 - 352*m.b25*m.b32*m.b33 - 256*
                       m.b25*m.b32*m.b34 - 160*m.b25*m.b32*m.b35 - 96*m.b25*m.b32*m.b36 - 64*m.b25*m.b32*m.b37 - 32*
                       m.b25*m.b32*m.b38 - 288*m.b25*m.b33*m.b34 - 192*m.b25*m.b33*m.b35 - 96*m.b25*m.b33*m.b36 - 64*
                       m.b25*m.b33*m.b37 - 32*m.b25*m.b33*m.b38 - 224*m.b25*m.b34*m.b35 - 128*m.b25*m.b34*m.b36 - 64*
                       m.b25*m.b34*m.b37 - 32*m.b25*m.b34*m.b38 - 160*m.b25*m.b35*m.b36 - 64*m.b25*m.b35*m.b37 - 32*
                       m.b25*m.b35*m.b38 - 96*m.b25*m.b36*m.b37 - 32*m.b25*m.b36*m.b38 - 32*m.b25*m.b37*m.b38 - 704*
                       m.b26*m.b27*m.b28 - 960*m.b26*m.b27*m.b29 - 832*m.b26*m.b27*m.b30 - 704*m.b26*m.b27*m.b31 - 576*
                       m.b26*m.b27*m.b32 - 448*m.b26*m.b27*m.b33 - 352*m.b26*m.b27*m.b34 - 288*m.b26*m.b27*m.b35 - 224*
                       m.b26*m.b27*m.b36 - 160*m.b26*m.b27*m.b37 - 96*m.b26*m.b27*m.b38 - 32*m.b26*m.b27*m.b39 - 960*
                       m.b26*m.b28*m.b29 - 512*m.b26*m.b28*m.b30 - 704*m.b26*m.b28*m.b31 - 576*m.b26*m.b28*m.b32 - 448*
                       m.b26*m.b28*m.b33 - 320*m.b26*m.b28*m.b34 - 256*m.b26*m.b28*m.b35 - 192*m.b26*m.b28*m.b36 - 128*
                       m.b26*m.b28*m.b37 - 64*m.b26*m.b28*m.b38 - 32*m.b26*m.b28*m.b39 - 832*m.b26*m.b29*m.b30 - 704*
                       m.b26*m.b29*m.b31 - 320*m.b26*m.b29*m.b32 - 448*m.b26*m.b29*m.b33 - 320*m.b26*m.b29*m.b34 - 224*
                       m.b26*m.b29*m.b35 - 160*m.b26*m.b29*m.b36 - 96*m.b26*m.b29*m.b37 - 64*m.b26*m.b29*m.b38 - 32*
                       m.b26*m.b29*m.b39 - 704*m.b26*m.b30*m.b31 - 576*m.b26*m.b30*m.b32 - 448*m.b26*m.b30*m.b33 - 128*
                       m.b26*m.b30*m.b34 - 192*m.b26*m.b30*m.b35 - 128*m.b26*m.b30*m.b36 - 96*m.b26*m.b30*m.b37 - 64*
                       m.b26*m.b30*m.b38 - 32*m.b26*m.b30*m.b39 - 576*m.b26*m.b31*m.b32 - 448*m.b26*m.b31*m.b33 - 320*
                       m.b26*m.b31*m.b34 - 192*m.b26*m.b31*m.b35 - 96*m.b26*m.b31*m.b37 - 64*m.b26*m.b31*m.b38 - 32*
                       m.b26*m.b31*m.b39 - 448*m.b26*m.b32*m.b33 - 320*m.b26*m.b32*m.b34 - 224*m.b26*m.b32*m.b35 - 128*
                       m.b26*m.b32*m.b36 - 96*m.b26*m.b32*m.b37 - 32*m.b26*m.b32*m.b39 - 352*m.b26*m.b33*m.b34 - 256*
                       m.b26*m.b33*m.b35 - 160*m.b26*m.b33*m.b36 - 96*m.b26*m.b33*m.b37 - 64*m.b26*m.b33*m.b38 - 32*
                       m.b26*m.b33*m.b39 - 288*m.b26*m.b34*m.b35 - 192*m.b26*m.b34*m.b36 - 96*m.b26*m.b34*m.b37 - 64*
                       m.b26*m.b34*m.b38 - 32*m.b26*m.b34*m.b39 - 224*m.b26*m.b35*m.b36 - 128*m.b26*m.b35*m.b37 - 64*
                       m.b26*m.b35*m.b38 - 32*m.b26*m.b35*m.b39 - 160*m.b26*m.b36*m.b37 - 64*m.b26*m.b36*m.b38 - 32*
                       m.b26*m.b36*m.b39 - 96*m.b26*m.b37*m.b38 - 32*m.b26*m.b37*m.b39 - 32*m.b26*m.b38*m.b39 - 704*
                       m.b27*m.b28*m.b29 - 960*m.b27*m.b28*m.b30 - 832*m.b27*m.b28*m.b31 - 704*m.b27*m.b28*m.b32 - 576*
                       m.b27*m.b28*m.b33 - 448*m.b27*m.b28*m.b34 - 352*m.b27*m.b28*m.b35 - 288*m.b27*m.b28*m.b36 - 224*
                       m.b27*m.b28*m.b37 - 160*m.b27*m.b28*m.b38 - 96*m.b27*m.b28*m.b39 - 32*m.b27*m.b28*m.b40 - 960*
                       m.b27*m.b29*m.b30 - 512*m.b27*m.b29*m.b31 - 704*m.b27*m.b29*m.b32 - 576*m.b27*m.b29*m.b33 - 448*
                       m.b27*m.b29*m.b34 - 320*m.b27*m.b29*m.b35 - 256*m.b27*m.b29*m.b36 - 192*m.b27*m.b29*m.b37 - 128*
                       m.b27*m.b29*m.b38 - 64*m.b27*m.b29*m.b39 - 32*m.b27*m.b29*m.b40 - 832*m.b27*m.b30*m.b31 - 704*
                       m.b27*m.b30*m.b32 - 320*m.b27*m.b30*m.b33 - 448*m.b27*m.b30*m.b34 - 320*m.b27*m.b30*m.b35 - 224*
                       m.b27*m.b30*m.b36 - 160*m.b27*m.b30*m.b37 - 96*m.b27*m.b30*m.b38 - 64*m.b27*m.b30*m.b39 - 32*
                       m.b27*m.b30*m.b40 - 704*m.b27*m.b31*m.b32 - 576*m.b27*m.b31*m.b33 - 448*m.b27*m.b31*m.b34 - 128*
                       m.b27*m.b31*m.b35 - 192*m.b27*m.b31*m.b36 - 128*m.b27*m.b31*m.b37 - 96*m.b27*m.b31*m.b38 - 64*
                       m.b27*m.b31*m.b39 - 32*m.b27*m.b31*m.b40 - 576*m.b27*m.b32*m.b33 - 448*m.b27*m.b32*m.b34 - 320*
                       m.b27*m.b32*m.b35 - 192*m.b27*m.b32*m.b36 - 96*m.b27*m.b32*m.b38 - 64*m.b27*m.b32*m.b39 - 32*
                       m.b27*m.b32*m.b40 - 448*m.b27*m.b33*m.b34 - 320*m.b27*m.b33*m.b35 - 224*m.b27*m.b33*m.b36 - 128*
                       m.b27*m.b33*m.b37 - 96*m.b27*m.b33*m.b38 - 32*m.b27*m.b33*m.b40 - 352*m.b27*m.b34*m.b35 - 256*
                       m.b27*m.b34*m.b36 - 160*m.b27*m.b34*m.b37 - 96*m.b27*m.b34*m.b38 - 64*m.b27*m.b34*m.b39 - 32*
                       m.b27*m.b34*m.b40 - 288*m.b27*m.b35*m.b36 - 192*m.b27*m.b35*m.b37 - 96*m.b27*m.b35*m.b38 - 64*
                       m.b27*m.b35*m.b39 - 32*m.b27*m.b35*m.b40 - 224*m.b27*m.b36*m.b37 - 128*m.b27*m.b36*m.b38 - 64*
                       m.b27*m.b36*m.b39 - 32*m.b27*m.b36*m.b40 - 160*m.b27*m.b37*m.b38 - 64*m.b27*m.b37*m.b39 - 32*
                       m.b27*m.b37*m.b40 - 96*m.b27*m.b38*m.b39 - 32*m.b27*m.b38*m.b40 - 32*m.b27*m.b39*m.b40 - 704*
                       m.b28*m.b29*m.b30 - 960*m.b28*m.b29*m.b31 - 832*m.b28*m.b29*m.b32 - 704*m.b28*m.b29*m.b33 - 576*
                       m.b28*m.b29*m.b34 - 448*m.b28*m.b29*m.b35 - 352*m.b28*m.b29*m.b36 - 288*m.b28*m.b29*m.b37 - 224*
                       m.b28*m.b29*m.b38 - 160*m.b28*m.b29*m.b39 - 96*m.b28*m.b29*m.b40 - 32*m.b28*m.b29*m.b41 - 960*
                       m.b28*m.b30*m.b31 - 512*m.b28*m.b30*m.b32 - 704*m.b28*m.b30*m.b33 - 576*m.b28*m.b30*m.b34 - 448*
                       m.b28*m.b30*m.b35 - 320*m.b28*m.b30*m.b36 - 256*m.b28*m.b30*m.b37 - 192*m.b28*m.b30*m.b38 - 128*
                       m.b28*m.b30*m.b39 - 64*m.b28*m.b30*m.b40 - 32*m.b28*m.b30*m.b41 - 832*m.b28*m.b31*m.b32 - 704*
                       m.b28*m.b31*m.b33 - 320*m.b28*m.b31*m.b34 - 448*m.b28*m.b31*m.b35 - 320*m.b28*m.b31*m.b36 - 224*
                       m.b28*m.b31*m.b37 - 160*m.b28*m.b31*m.b38 - 96*m.b28*m.b31*m.b39 - 64*m.b28*m.b31*m.b40 - 32*
                       m.b28*m.b31*m.b41 - 704*m.b28*m.b32*m.b33 - 576*m.b28*m.b32*m.b34 - 448*m.b28*m.b32*m.b35 - 128*
                       m.b28*m.b32*m.b36 - 192*m.b28*m.b32*m.b37 - 128*m.b28*m.b32*m.b38 - 96*m.b28*m.b32*m.b39 - 64*
                       m.b28*m.b32*m.b40 - 32*m.b28*m.b32*m.b41 - 576*m.b28*m.b33*m.b34 - 448*m.b28*m.b33*m.b35 - 320*
                       m.b28*m.b33*m.b36 - 192*m.b28*m.b33*m.b37 - 96*m.b28*m.b33*m.b39 - 64*m.b28*m.b33*m.b40 - 32*
                       m.b28*m.b33*m.b41 - 448*m.b28*m.b34*m.b35 - 320*m.b28*m.b34*m.b36 - 224*m.b28*m.b34*m.b37 - 128*
                       m.b28*m.b34*m.b38 - 96*m.b28*m.b34*m.b39 - 32*m.b28*m.b34*m.b41 - 352*m.b28*m.b35*m.b36 - 256*
                       m.b28*m.b35*m.b37 - 160*m.b28*m.b35*m.b38 - 96*m.b28*m.b35*m.b39 - 64*m.b28*m.b35*m.b40 - 32*
                       m.b28*m.b35*m.b41 - 288*m.b28*m.b36*m.b37 - 192*m.b28*m.b36*m.b38 - 96*m.b28*m.b36*m.b39 - 64*
                       m.b28*m.b36*m.b40 - 32*m.b28*m.b36*m.b41 - 224*m.b28*m.b37*m.b38 - 128*m.b28*m.b37*m.b39 - 64*
                       m.b28*m.b37*m.b40 - 32*m.b28*m.b37*m.b41 - 160*m.b28*m.b38*m.b39 - 64*m.b28*m.b38*m.b40 - 32*
                       m.b28*m.b38*m.b41 - 96*m.b28*m.b39*m.b40 - 32*m.b28*m.b39*m.b41 - 32*m.b28*m.b40*m.b41 - 704*
                       m.b29*m.b30*m.b31 - 960*m.b29*m.b30*m.b32 - 832*m.b29*m.b30*m.b33 - 704*m.b29*m.b30*m.b34 - 576*
                       m.b29*m.b30*m.b35 - 448*m.b29*m.b30*m.b36 - 352*m.b29*m.b30*m.b37 - 288*m.b29*m.b30*m.b38 - 224*
                       m.b29*m.b30*m.b39 - 160*m.b29*m.b30*m.b40 - 96*m.b29*m.b30*m.b41 - 32*m.b29*m.b30*m.b42 - 960*
                       m.b29*m.b31*m.b32 - 512*m.b29*m.b31*m.b33 - 704*m.b29*m.b31*m.b34 - 576*m.b29*m.b31*m.b35 - 448*
                       m.b29*m.b31*m.b36 - 320*m.b29*m.b31*m.b37 - 256*m.b29*m.b31*m.b38 - 192*m.b29*m.b31*m.b39 - 128*
                       m.b29*m.b31*m.b40 - 64*m.b29*m.b31*m.b41 - 32*m.b29*m.b31*m.b42 - 832*m.b29*m.b32*m.b33 - 704*
                       m.b29*m.b32*m.b34 - 320*m.b29*m.b32*m.b35 - 448*m.b29*m.b32*m.b36 - 320*m.b29*m.b32*m.b37 - 224*
                       m.b29*m.b32*m.b38 - 160*m.b29*m.b32*m.b39 - 96*m.b29*m.b32*m.b40 - 64*m.b29*m.b32*m.b41 - 32*
                       m.b29*m.b32*m.b42 - 704*m.b29*m.b33*m.b34 - 576*m.b29*m.b33*m.b35 - 448*m.b29*m.b33*m.b36 - 128*
                       m.b29*m.b33*m.b37 - 192*m.b29*m.b33*m.b38 - 128*m.b29*m.b33*m.b39 - 96*m.b29*m.b33*m.b40 - 64*
                       m.b29*m.b33*m.b41 - 32*m.b29*m.b33*m.b42 - 576*m.b29*m.b34*m.b35 - 448*m.b29*m.b34*m.b36 - 320*
                       m.b29*m.b34*m.b37 - 192*m.b29*m.b34*m.b38 - 96*m.b29*m.b34*m.b40 - 64*m.b29*m.b34*m.b41 - 32*
                       m.b29*m.b34*m.b42 - 448*m.b29*m.b35*m.b36 - 320*m.b29*m.b35*m.b37 - 224*m.b29*m.b35*m.b38 - 128*
                       m.b29*m.b35*m.b39 - 96*m.b29*m.b35*m.b40 - 32*m.b29*m.b35*m.b42 - 352*m.b29*m.b36*m.b37 - 256*
                       m.b29*m.b36*m.b38 - 160*m.b29*m.b36*m.b39 - 96*m.b29*m.b36*m.b40 - 64*m.b29*m.b36*m.b41 - 32*
                       m.b29*m.b36*m.b42 - 288*m.b29*m.b37*m.b38 - 192*m.b29*m.b37*m.b39 - 96*m.b29*m.b37*m.b40 - 64*
                       m.b29*m.b37*m.b41 - 32*m.b29*m.b37*m.b42 - 224*m.b29*m.b38*m.b39 - 128*m.b29*m.b38*m.b40 - 64*
                       m.b29*m.b38*m.b41 - 32*m.b29*m.b38*m.b42 - 160*m.b29*m.b39*m.b40 - 64*m.b29*m.b39*m.b41 - 32*
                       m.b29*m.b39*m.b42 - 96*m.b29*m.b40*m.b41 - 32*m.b29*m.b40*m.b42 - 32*m.b29*m.b41*m.b42 - 704*
                       m.b30*m.b31*m.b32 - 960*m.b30*m.b31*m.b33 - 832*m.b30*m.b31*m.b34 - 704*m.b30*m.b31*m.b35 - 576*
                       m.b30*m.b31*m.b36 - 448*m.b30*m.b31*m.b37 - 352*m.b30*m.b31*m.b38 - 288*m.b30*m.b31*m.b39 - 224*
                       m.b30*m.b31*m.b40 - 160*m.b30*m.b31*m.b41 - 96*m.b30*m.b31*m.b42 - 32*m.b30*m.b31*m.b43 - 960*
                       m.b30*m.b32*m.b33 - 512*m.b30*m.b32*m.b34 - 704*m.b30*m.b32*m.b35 - 576*m.b30*m.b32*m.b36 - 448*
                       m.b30*m.b32*m.b37 - 320*m.b30*m.b32*m.b38 - 256*m.b30*m.b32*m.b39 - 192*m.b30*m.b32*m.b40 - 128*
                       m.b30*m.b32*m.b41 - 64*m.b30*m.b32*m.b42 - 32*m.b30*m.b32*m.b43 - 832*m.b30*m.b33*m.b34 - 704*
                       m.b30*m.b33*m.b35 - 320*m.b30*m.b33*m.b36 - 448*m.b30*m.b33*m.b37 - 320*m.b30*m.b33*m.b38 - 224*
                       m.b30*m.b33*m.b39 - 160*m.b30*m.b33*m.b40 - 96*m.b30*m.b33*m.b41 - 64*m.b30*m.b33*m.b42 - 32*
                       m.b30*m.b33*m.b43 - 704*m.b30*m.b34*m.b35 - 576*m.b30*m.b34*m.b36 - 448*m.b30*m.b34*m.b37 - 128*
                       m.b30*m.b34*m.b38 - 192*m.b30*m.b34*m.b39 - 128*m.b30*m.b34*m.b40 - 96*m.b30*m.b34*m.b41 - 64*
                       m.b30*m.b34*m.b42 - 32*m.b30*m.b34*m.b43 - 576*m.b30*m.b35*m.b36 - 448*m.b30*m.b35*m.b37 - 320*
                       m.b30*m.b35*m.b38 - 192*m.b30*m.b35*m.b39 - 96*m.b30*m.b35*m.b41 - 64*m.b30*m.b35*m.b42 - 32*
                       m.b30*m.b35*m.b43 - 448*m.b30*m.b36*m.b37 - 320*m.b30*m.b36*m.b38 - 224*m.b30*m.b36*m.b39 - 128*
                       m.b30*m.b36*m.b40 - 96*m.b30*m.b36*m.b41 - 32*m.b30*m.b36*m.b43 - 352*m.b30*m.b37*m.b38 - 256*
                       m.b30*m.b37*m.b39 - 160*m.b30*m.b37*m.b40 - 96*m.b30*m.b37*m.b41 - 64*m.b30*m.b37*m.b42 - 32*
                       m.b30*m.b37*m.b43 - 288*m.b30*m.b38*m.b39 - 192*m.b30*m.b38*m.b40 - 96*m.b30*m.b38*m.b41 - 64*
                       m.b30*m.b38*m.b42 - 32*m.b30*m.b38*m.b43 - 224*m.b30*m.b39*m.b40 - 128*m.b30*m.b39*m.b41 - 64*
                       m.b30*m.b39*m.b42 - 32*m.b30*m.b39*m.b43 - 160*m.b30*m.b40*m.b41 - 64*m.b30*m.b40*m.b42 - 32*
                       m.b30*m.b40*m.b43 - 96*m.b30*m.b41*m.b42 - 32*m.b30*m.b41*m.b43 - 32*m.b30*m.b42*m.b43 - 704*
                       m.b31*m.b32*m.b33 - 960*m.b31*m.b32*m.b34 - 832*m.b31*m.b32*m.b35 - 704*m.b31*m.b32*m.b36 - 576*
                       m.b31*m.b32*m.b37 - 448*m.b31*m.b32*m.b38 - 352*m.b31*m.b32*m.b39 - 288*m.b31*m.b32*m.b40 - 224*
                       m.b31*m.b32*m.b41 - 160*m.b31*m.b32*m.b42 - 96*m.b31*m.b32*m.b43 - 32*m.b31*m.b32*m.b44 - 960*
                       m.b31*m.b33*m.b34 - 512*m.b31*m.b33*m.b35 - 704*m.b31*m.b33*m.b36 - 576*m.b31*m.b33*m.b37 - 448*
                       m.b31*m.b33*m.b38 - 320*m.b31*m.b33*m.b39 - 256*m.b31*m.b33*m.b40 - 192*m.b31*m.b33*m.b41 - 128*
                       m.b31*m.b33*m.b42 - 64*m.b31*m.b33*m.b43 - 32*m.b31*m.b33*m.b44 - 832*m.b31*m.b34*m.b35 - 704*
                       m.b31*m.b34*m.b36 - 320*m.b31*m.b34*m.b37 - 448*m.b31*m.b34*m.b38 - 320*m.b31*m.b34*m.b39 - 224*
                       m.b31*m.b34*m.b40 - 160*m.b31*m.b34*m.b41 - 96*m.b31*m.b34*m.b42 - 64*m.b31*m.b34*m.b43 - 32*
                       m.b31*m.b34*m.b44 - 704*m.b31*m.b35*m.b36 - 576*m.b31*m.b35*m.b37 - 448*m.b31*m.b35*m.b38 - 128*
                       m.b31*m.b35*m.b39 - 192*m.b31*m.b35*m.b40 - 128*m.b31*m.b35*m.b41 - 96*m.b31*m.b35*m.b42 - 64*
                       m.b31*m.b35*m.b43 - 32*m.b31*m.b35*m.b44 - 576*m.b31*m.b36*m.b37 - 448*m.b31*m.b36*m.b38 - 320*
                       m.b31*m.b36*m.b39 - 192*m.b31*m.b36*m.b40 - 96*m.b31*m.b36*m.b42 - 64*m.b31*m.b36*m.b43 - 32*
                       m.b31*m.b36*m.b44 - 448*m.b31*m.b37*m.b38 - 320*m.b31*m.b37*m.b39 - 224*m.b31*m.b37*m.b40 - 128*
                       m.b31*m.b37*m.b41 - 96*m.b31*m.b37*m.b42 - 32*m.b31*m.b37*m.b44 - 352*m.b31*m.b38*m.b39 - 256*
                       m.b31*m.b38*m.b40 - 160*m.b31*m.b38*m.b41 - 96*m.b31*m.b38*m.b42 - 64*m.b31*m.b38*m.b43 - 32*
                       m.b31*m.b38*m.b44 - 288*m.b31*m.b39*m.b40 - 192*m.b31*m.b39*m.b41 - 96*m.b31*m.b39*m.b42 - 64*
                       m.b31*m.b39*m.b43 - 32*m.b31*m.b39*m.b44 - 224*m.b31*m.b40*m.b41 - 128*m.b31*m.b40*m.b42 - 64*
                       m.b31*m.b40*m.b43 - 32*m.b31*m.b40*m.b44 - 160*m.b31*m.b41*m.b42 - 64*m.b31*m.b41*m.b43 - 32*
                       m.b31*m.b41*m.b44 - 96*m.b31*m.b42*m.b43 - 32*m.b31*m.b42*m.b44 - 32*m.b31*m.b43*m.b44 - 704*
                       m.b32*m.b33*m.b34 - 960*m.b32*m.b33*m.b35 - 832*m.b32*m.b33*m.b36 - 704*m.b32*m.b33*m.b37 - 576*
                       m.b32*m.b33*m.b38 - 448*m.b32*m.b33*m.b39 - 352*m.b32*m.b33*m.b40 - 288*m.b32*m.b33*m.b41 - 224*
                       m.b32*m.b33*m.b42 - 160*m.b32*m.b33*m.b43 - 96*m.b32*m.b33*m.b44 - 32*m.b32*m.b33*m.b45 - 960*
                       m.b32*m.b34*m.b35 - 512*m.b32*m.b34*m.b36 - 704*m.b32*m.b34*m.b37 - 576*m.b32*m.b34*m.b38 - 448*
                       m.b32*m.b34*m.b39 - 320*m.b32*m.b34*m.b40 - 256*m.b32*m.b34*m.b41 - 192*m.b32*m.b34*m.b42 - 128*
                       m.b32*m.b34*m.b43 - 64*m.b32*m.b34*m.b44 - 32*m.b32*m.b34*m.b45 - 832*m.b32*m.b35*m.b36 - 704*
                       m.b32*m.b35*m.b37 - 320*m.b32*m.b35*m.b38 - 448*m.b32*m.b35*m.b39 - 320*m.b32*m.b35*m.b40 - 224*
                       m.b32*m.b35*m.b41 - 160*m.b32*m.b35*m.b42 - 96*m.b32*m.b35*m.b43 - 64*m.b32*m.b35*m.b44 - 32*
                       m.b32*m.b35*m.b45 - 704*m.b32*m.b36*m.b37 - 576*m.b32*m.b36*m.b38 - 448*m.b32*m.b36*m.b39 - 128*
                       m.b32*m.b36*m.b40 - 192*m.b32*m.b36*m.b41 - 128*m.b32*m.b36*m.b42 - 96*m.b32*m.b36*m.b43 - 64*
                       m.b32*m.b36*m.b44 - 32*m.b32*m.b36*m.b45 - 576*m.b32*m.b37*m.b38 - 448*m.b32*m.b37*m.b39 - 320*
                       m.b32*m.b37*m.b40 - 192*m.b32*m.b37*m.b41 - 96*m.b32*m.b37*m.b43 - 64*m.b32*m.b37*m.b44 - 32*
                       m.b32*m.b37*m.b45 - 448*m.b32*m.b38*m.b39 - 320*m.b32*m.b38*m.b40 - 224*m.b32*m.b38*m.b41 - 128*
                       m.b32*m.b38*m.b42 - 96*m.b32*m.b38*m.b43 - 32*m.b32*m.b38*m.b45 - 352*m.b32*m.b39*m.b40 - 256*
                       m.b32*m.b39*m.b41 - 160*m.b32*m.b39*m.b42 - 96*m.b32*m.b39*m.b43 - 64*m.b32*m.b39*m.b44 - 32*
                       m.b32*m.b39*m.b45 - 288*m.b32*m.b40*m.b41 - 192*m.b32*m.b40*m.b42 - 96*m.b32*m.b40*m.b43 - 64*
                       m.b32*m.b40*m.b44 - 32*m.b32*m.b40*m.b45 - 224*m.b32*m.b41*m.b42 - 128*m.b32*m.b41*m.b43 - 64*
                       m.b32*m.b41*m.b44 - 32*m.b32*m.b41*m.b45 - 160*m.b32*m.b42*m.b43 - 64*m.b32*m.b42*m.b44 - 32*
                       m.b32*m.b42*m.b45 - 96*m.b32*m.b43*m.b44 - 32*m.b32*m.b43*m.b45 - 32*m.b32*m.b44*m.b45 - 704*
                       m.b33*m.b34*m.b35 - 960*m.b33*m.b34*m.b36 - 832*m.b33*m.b34*m.b37 - 704*m.b33*m.b34*m.b38 - 576*
                       m.b33*m.b34*m.b39 - 448*m.b33*m.b34*m.b40 - 352*m.b33*m.b34*m.b41 - 288*m.b33*m.b34*m.b42 - 224*
                       m.b33*m.b34*m.b43 - 160*m.b33*m.b34*m.b44 - 96*m.b33*m.b34*m.b45 - 32*m.b33*m.b34*m.b46 - 960*
                       m.b33*m.b35*m.b36 - 512*m.b33*m.b35*m.b37 - 704*m.b33*m.b35*m.b38 - 576*m.b33*m.b35*m.b39 - 448*
                       m.b33*m.b35*m.b40 - 320*m.b33*m.b35*m.b41 - 256*m.b33*m.b35*m.b42 - 192*m.b33*m.b35*m.b43 - 128*
                       m.b33*m.b35*m.b44 - 64*m.b33*m.b35*m.b45 - 32*m.b33*m.b35*m.b46 - 832*m.b33*m.b36*m.b37 - 704*
                       m.b33*m.b36*m.b38 - 320*m.b33*m.b36*m.b39 - 448*m.b33*m.b36*m.b40 - 320*m.b33*m.b36*m.b41 - 224*
                       m.b33*m.b36*m.b42 - 160*m.b33*m.b36*m.b43 - 96*m.b33*m.b36*m.b44 - 64*m.b33*m.b36*m.b45 - 32*
                       m.b33*m.b36*m.b46 - 704*m.b33*m.b37*m.b38 - 576*m.b33*m.b37*m.b39 - 448*m.b33*m.b37*m.b40 - 128*
                       m.b33*m.b37*m.b41 - 192*m.b33*m.b37*m.b42 - 128*m.b33*m.b37*m.b43 - 96*m.b33*m.b37*m.b44 - 64*
                       m.b33*m.b37*m.b45 - 32*m.b33*m.b37*m.b46 - 576*m.b33*m.b38*m.b39 - 448*m.b33*m.b38*m.b40 - 320*
                       m.b33*m.b38*m.b41 - 192*m.b33*m.b38*m.b42 - 96*m.b33*m.b38*m.b44 - 64*m.b33*m.b38*m.b45 - 32*
                       m.b33*m.b38*m.b46 - 448*m.b33*m.b39*m.b40 - 320*m.b33*m.b39*m.b41 - 224*m.b33*m.b39*m.b42 - 128*
                       m.b33*m.b39*m.b43 - 96*m.b33*m.b39*m.b44 - 32*m.b33*m.b39*m.b46 - 352*m.b33*m.b40*m.b41 - 256*
                       m.b33*m.b40*m.b42 - 160*m.b33*m.b40*m.b43 - 96*m.b33*m.b40*m.b44 - 64*m.b33*m.b40*m.b45 - 32*
                       m.b33*m.b40*m.b46 - 288*m.b33*m.b41*m.b42 - 192*m.b33*m.b41*m.b43 - 96*m.b33*m.b41*m.b44 - 64*
                       m.b33*m.b41*m.b45 - 32*m.b33*m.b41*m.b46 - 224*m.b33*m.b42*m.b43 - 128*m.b33*m.b42*m.b44 - 64*
                       m.b33*m.b42*m.b45 - 32*m.b33*m.b42*m.b46 - 160*m.b33*m.b43*m.b44 - 64*m.b33*m.b43*m.b45 - 32*
                       m.b33*m.b43*m.b46 - 96*m.b33*m.b44*m.b45 - 32*m.b33*m.b44*m.b46 - 32*m.b33*m.b45*m.b46 - 704*
                       m.b34*m.b35*m.b36 - 960*m.b34*m.b35*m.b37 - 832*m.b34*m.b35*m.b38 - 704*m.b34*m.b35*m.b39 - 576*
                       m.b34*m.b35*m.b40 - 448*m.b34*m.b35*m.b41 - 352*m.b34*m.b35*m.b42 - 288*m.b34*m.b35*m.b43 - 224*
                       m.b34*m.b35*m.b44 - 160*m.b34*m.b35*m.b45 - 96*m.b34*m.b35*m.b46 - 32*m.b34*m.b35*m.b47 - 960*
                       m.b34*m.b36*m.b37 - 512*m.b34*m.b36*m.b38 - 704*m.b34*m.b36*m.b39 - 576*m.b34*m.b36*m.b40 - 448*
                       m.b34*m.b36*m.b41 - 320*m.b34*m.b36*m.b42 - 256*m.b34*m.b36*m.b43 - 192*m.b34*m.b36*m.b44 - 128*
                       m.b34*m.b36*m.b45 - 64*m.b34*m.b36*m.b46 - 32*m.b34*m.b36*m.b47 - 832*m.b34*m.b37*m.b38 - 704*
                       m.b34*m.b37*m.b39 - 320*m.b34*m.b37*m.b40 - 448*m.b34*m.b37*m.b41 - 320*m.b34*m.b37*m.b42 - 224*
                       m.b34*m.b37*m.b43 - 160*m.b34*m.b37*m.b44 - 96*m.b34*m.b37*m.b45 - 64*m.b34*m.b37*m.b46 - 32*
                       m.b34*m.b37*m.b47 - 704*m.b34*m.b38*m.b39 - 576*m.b34*m.b38*m.b40 - 448*m.b34*m.b38*m.b41 - 128*
                       m.b34*m.b38*m.b42 - 192*m.b34*m.b38*m.b43 - 128*m.b34*m.b38*m.b44 - 96*m.b34*m.b38*m.b45 - 64*
                       m.b34*m.b38*m.b46 - 32*m.b34*m.b38*m.b47 - 576*m.b34*m.b39*m.b40 - 448*m.b34*m.b39*m.b41 - 320*
                       m.b34*m.b39*m.b42 - 192*m.b34*m.b39*m.b43 - 96*m.b34*m.b39*m.b45 - 64*m.b34*m.b39*m.b46 - 32*
                       m.b34*m.b39*m.b47 - 448*m.b34*m.b40*m.b41 - 320*m.b34*m.b40*m.b42 - 224*m.b34*m.b40*m.b43 - 128*
                       m.b34*m.b40*m.b44 - 96*m.b34*m.b40*m.b45 - 32*m.b34*m.b40*m.b47 - 352*m.b34*m.b41*m.b42 - 256*
                       m.b34*m.b41*m.b43 - 160*m.b34*m.b41*m.b44 - 96*m.b34*m.b41*m.b45 - 64*m.b34*m.b41*m.b46 - 32*
                       m.b34*m.b41*m.b47 - 288*m.b34*m.b42*m.b43 - 192*m.b34*m.b42*m.b44 - 96*m.b34*m.b42*m.b45 - 64*
                       m.b34*m.b42*m.b46 - 32*m.b34*m.b42*m.b47 - 224*m.b34*m.b43*m.b44 - 128*m.b34*m.b43*m.b45 - 64*
                       m.b34*m.b43*m.b46 - 32*m.b34*m.b43*m.b47 - 160*m.b34*m.b44*m.b45 - 64*m.b34*m.b44*m.b46 - 32*
                       m.b34*m.b44*m.b47 - 96*m.b34*m.b45*m.b46 - 32*m.b34*m.b45*m.b47 - 32*m.b34*m.b46*m.b47 - 704*
                       m.b35*m.b36*m.b37 - 960*m.b35*m.b36*m.b38 - 832*m.b35*m.b36*m.b39 - 704*m.b35*m.b36*m.b40 - 576*
                       m.b35*m.b36*m.b41 - 448*m.b35*m.b36*m.b42 - 352*m.b35*m.b36*m.b43 - 288*m.b35*m.b36*m.b44 - 224*
                       m.b35*m.b36*m.b45 - 160*m.b35*m.b36*m.b46 - 96*m.b35*m.b36*m.b47 - 32*m.b35*m.b36*m.b48 - 960*
                       m.b35*m.b37*m.b38 - 512*m.b35*m.b37*m.b39 - 704*m.b35*m.b37*m.b40 - 576*m.b35*m.b37*m.b41 - 448*
                       m.b35*m.b37*m.b42 - 320*m.b35*m.b37*m.b43 - 256*m.b35*m.b37*m.b44 - 192*m.b35*m.b37*m.b45 - 128*
                       m.b35*m.b37*m.b46 - 64*m.b35*m.b37*m.b47 - 32*m.b35*m.b37*m.b48 - 832*m.b35*m.b38*m.b39 - 704*
                       m.b35*m.b38*m.b40 - 320*m.b35*m.b38*m.b41 - 448*m.b35*m.b38*m.b42 - 320*m.b35*m.b38*m.b43 - 224*
                       m.b35*m.b38*m.b44 - 160*m.b35*m.b38*m.b45 - 96*m.b35*m.b38*m.b46 - 64*m.b35*m.b38*m.b47 - 32*
                       m.b35*m.b38*m.b48 - 704*m.b35*m.b39*m.b40 - 576*m.b35*m.b39*m.b41 - 448*m.b35*m.b39*m.b42 - 128*
                       m.b35*m.b39*m.b43 - 192*m.b35*m.b39*m.b44 - 128*m.b35*m.b39*m.b45 - 96*m.b35*m.b39*m.b46 - 64*
                       m.b35*m.b39*m.b47 - 32*m.b35*m.b39*m.b48 - 576*m.b35*m.b40*m.b41 - 448*m.b35*m.b40*m.b42 - 320*
                       m.b35*m.b40*m.b43 - 192*m.b35*m.b40*m.b44 - 96*m.b35*m.b40*m.b46 - 64*m.b35*m.b40*m.b47 - 32*
                       m.b35*m.b40*m.b48 - 448*m.b35*m.b41*m.b42 - 320*m.b35*m.b41*m.b43 - 224*m.b35*m.b41*m.b44 - 128*
                       m.b35*m.b41*m.b45 - 96*m.b35*m.b41*m.b46 - 32*m.b35*m.b41*m.b48 - 352*m.b35*m.b42*m.b43 - 256*
                       m.b35*m.b42*m.b44 - 160*m.b35*m.b42*m.b45 - 96*m.b35*m.b42*m.b46 - 64*m.b35*m.b42*m.b47 - 32*
                       m.b35*m.b42*m.b48 - 288*m.b35*m.b43*m.b44 - 192*m.b35*m.b43*m.b45 - 96*m.b35*m.b43*m.b46 - 64*
                       m.b35*m.b43*m.b47 - 32*m.b35*m.b43*m.b48 - 224*m.b35*m.b44*m.b45 - 128*m.b35*m.b44*m.b46 - 64*
                       m.b35*m.b44*m.b47 - 32*m.b35*m.b44*m.b48 - 160*m.b35*m.b45*m.b46 - 64*m.b35*m.b45*m.b47 - 32*
                       m.b35*m.b45*m.b48 - 96*m.b35*m.b46*m.b47 - 32*m.b35*m.b46*m.b48 - 32*m.b35*m.b47*m.b48 - 704*
                       m.b36*m.b37*m.b38 - 960*m.b36*m.b37*m.b39 - 832*m.b36*m.b37*m.b40 - 704*m.b36*m.b37*m.b41 - 576*
                       m.b36*m.b37*m.b42 - 448*m.b36*m.b37*m.b43 - 352*m.b36*m.b37*m.b44 - 288*m.b36*m.b37*m.b45 - 224*
                       m.b36*m.b37*m.b46 - 160*m.b36*m.b37*m.b47 - 96*m.b36*m.b37*m.b48 - 32*m.b36*m.b37*m.b49 - 960*
                       m.b36*m.b38*m.b39 - 512*m.b36*m.b38*m.b40 - 704*m.b36*m.b38*m.b41 - 576*m.b36*m.b38*m.b42 - 448*
                       m.b36*m.b38*m.b43 - 320*m.b36*m.b38*m.b44 - 256*m.b36*m.b38*m.b45 - 192*m.b36*m.b38*m.b46 - 128*
                       m.b36*m.b38*m.b47 - 64*m.b36*m.b38*m.b48 - 32*m.b36*m.b38*m.b49 - 832*m.b36*m.b39*m.b40 - 704*
                       m.b36*m.b39*m.b41 - 320*m.b36*m.b39*m.b42 - 448*m.b36*m.b39*m.b43 - 320*m.b36*m.b39*m.b44 - 224*
                       m.b36*m.b39*m.b45 - 160*m.b36*m.b39*m.b46 - 96*m.b36*m.b39*m.b47 - 64*m.b36*m.b39*m.b48 - 32*
                       m.b36*m.b39*m.b49 - 704*m.b36*m.b40*m.b41 - 576*m.b36*m.b40*m.b42 - 448*m.b36*m.b40*m.b43 - 128*
                       m.b36*m.b40*m.b44 - 192*m.b36*m.b40*m.b45 - 128*m.b36*m.b40*m.b46 - 96*m.b36*m.b40*m.b47 - 64*
                       m.b36*m.b40*m.b48 - 32*m.b36*m.b40*m.b49 - 576*m.b36*m.b41*m.b42 - 448*m.b36*m.b41*m.b43 - 320*
                       m.b36*m.b41*m.b44 - 192*m.b36*m.b41*m.b45 - 96*m.b36*m.b41*m.b47 - 64*m.b36*m.b41*m.b48 - 32*
                       m.b36*m.b41*m.b49 - 448*m.b36*m.b42*m.b43 - 320*m.b36*m.b42*m.b44 - 224*m.b36*m.b42*m.b45 - 128*
                       m.b36*m.b42*m.b46 - 96*m.b36*m.b42*m.b47 - 32*m.b36*m.b42*m.b49 - 352*m.b36*m.b43*m.b44 - 256*
                       m.b36*m.b43*m.b45 - 160*m.b36*m.b43*m.b46 - 96*m.b36*m.b43*m.b47 - 64*m.b36*m.b43*m.b48 - 32*
                       m.b36*m.b43*m.b49 - 288*m.b36*m.b44*m.b45 - 192*m.b36*m.b44*m.b46 - 96*m.b36*m.b44*m.b47 - 64*
                       m.b36*m.b44*m.b48 - 32*m.b36*m.b44*m.b49 - 224*m.b36*m.b45*m.b46 - 128*m.b36*m.b45*m.b47 - 64*
                       m.b36*m.b45*m.b48 - 32*m.b36*m.b45*m.b49 - 160*m.b36*m.b46*m.b47 - 64*m.b36*m.b46*m.b48 - 32*
                       m.b36*m.b46*m.b49 - 96*m.b36*m.b47*m.b48 - 32*m.b36*m.b47*m.b49 - 32*m.b36*m.b48*m.b49 - 704*
                       m.b37*m.b38*m.b39 - 960*m.b37*m.b38*m.b40 - 832*m.b37*m.b38*m.b41 - 704*m.b37*m.b38*m.b42 - 576*
                       m.b37*m.b38*m.b43 - 448*m.b37*m.b38*m.b44 - 352*m.b37*m.b38*m.b45 - 288*m.b37*m.b38*m.b46 - 224*
                       m.b37*m.b38*m.b47 - 160*m.b37*m.b38*m.b48 - 96*m.b37*m.b38*m.b49 - 32*m.b37*m.b38*m.b50 - 960*
                       m.b37*m.b39*m.b40 - 512*m.b37*m.b39*m.b41 - 704*m.b37*m.b39*m.b42 - 576*m.b37*m.b39*m.b43 - 448*
                       m.b37*m.b39*m.b44 - 320*m.b37*m.b39*m.b45 - 256*m.b37*m.b39*m.b46 - 192*m.b37*m.b39*m.b47 - 128*
                       m.b37*m.b39*m.b48 - 64*m.b37*m.b39*m.b49 - 32*m.b37*m.b39*m.b50 - 832*m.b37*m.b40*m.b41 - 704*
                       m.b37*m.b40*m.b42 - 320*m.b37*m.b40*m.b43 - 448*m.b37*m.b40*m.b44 - 320*m.b37*m.b40*m.b45 - 224*
                       m.b37*m.b40*m.b46 - 160*m.b37*m.b40*m.b47 - 96*m.b37*m.b40*m.b48 - 64*m.b37*m.b40*m.b49 - 32*
                       m.b37*m.b40*m.b50 - 704*m.b37*m.b41*m.b42 - 576*m.b37*m.b41*m.b43 - 448*m.b37*m.b41*m.b44 - 128*
                       m.b37*m.b41*m.b45 - 192*m.b37*m.b41*m.b46 - 128*m.b37*m.b41*m.b47 - 96*m.b37*m.b41*m.b48 - 64*
                       m.b37*m.b41*m.b49 - 32*m.b37*m.b41*m.b50 - 576*m.b37*m.b42*m.b43 - 448*m.b37*m.b42*m.b44 - 320*
                       m.b37*m.b42*m.b45 - 192*m.b37*m.b42*m.b46 - 96*m.b37*m.b42*m.b48 - 64*m.b37*m.b42*m.b49 - 32*
                       m.b37*m.b42*m.b50 - 448*m.b37*m.b43*m.b44 - 320*m.b37*m.b43*m.b45 - 224*m.b37*m.b43*m.b46 - 128*
                       m.b37*m.b43*m.b47 - 96*m.b37*m.b43*m.b48 - 32*m.b37*m.b43*m.b50 - 352*m.b37*m.b44*m.b45 - 256*
                       m.b37*m.b44*m.b46 - 160*m.b37*m.b44*m.b47 - 96*m.b37*m.b44*m.b48 - 64*m.b37*m.b44*m.b49 - 32*
                       m.b37*m.b44*m.b50 - 288*m.b37*m.b45*m.b46 - 192*m.b37*m.b45*m.b47 - 96*m.b37*m.b45*m.b48 - 64*
                       m.b37*m.b45*m.b49 - 32*m.b37*m.b45*m.b50 - 224*m.b37*m.b46*m.b47 - 128*m.b37*m.b46*m.b48 - 64*
                       m.b37*m.b46*m.b49 - 32*m.b37*m.b46*m.b50 - 160*m.b37*m.b47*m.b48 - 64*m.b37*m.b47*m.b49 - 32*
                       m.b37*m.b47*m.b50 - 96*m.b37*m.b48*m.b49 - 32*m.b37*m.b48*m.b50 - 32*m.b37*m.b49*m.b50 - 704*
                       m.b38*m.b39*m.b40 - 960*m.b38*m.b39*m.b41 - 832*m.b38*m.b39*m.b42 - 704*m.b38*m.b39*m.b43 - 576*
                       m.b38*m.b39*m.b44 - 448*m.b38*m.b39*m.b45 - 352*m.b38*m.b39*m.b46 - 288*m.b38*m.b39*m.b47 - 224*
                       m.b38*m.b39*m.b48 - 160*m.b38*m.b39*m.b49 - 96*m.b38*m.b39*m.b50 - 32*m.b38*m.b39*m.b51 - 960*
                       m.b38*m.b40*m.b41 - 512*m.b38*m.b40*m.b42 - 704*m.b38*m.b40*m.b43 - 576*m.b38*m.b40*m.b44 - 448*
                       m.b38*m.b40*m.b45 - 320*m.b38*m.b40*m.b46 - 256*m.b38*m.b40*m.b47 - 192*m.b38*m.b40*m.b48 - 128*
                       m.b38*m.b40*m.b49 - 64*m.b38*m.b40*m.b50 - 32*m.b38*m.b40*m.b51 - 832*m.b38*m.b41*m.b42 - 704*
                       m.b38*m.b41*m.b43 - 320*m.b38*m.b41*m.b44 - 448*m.b38*m.b41*m.b45 - 320*m.b38*m.b41*m.b46 - 224*
                       m.b38*m.b41*m.b47 - 160*m.b38*m.b41*m.b48 - 96*m.b38*m.b41*m.b49 - 64*m.b38*m.b41*m.b50 - 32*
                       m.b38*m.b41*m.b51 - 704*m.b38*m.b42*m.b43 - 576*m.b38*m.b42*m.b44 - 448*m.b38*m.b42*m.b45 - 128*
                       m.b38*m.b42*m.b46 - 192*m.b38*m.b42*m.b47 - 128*m.b38*m.b42*m.b48 - 96*m.b38*m.b42*m.b49 - 64*
                       m.b38*m.b42*m.b50 - 32*m.b38*m.b42*m.b51 - 576*m.b38*m.b43*m.b44 - 448*m.b38*m.b43*m.b45 - 320*
                       m.b38*m.b43*m.b46 - 192*m.b38*m.b43*m.b47 - 96*m.b38*m.b43*m.b49 - 64*m.b38*m.b43*m.b50 - 32*
                       m.b38*m.b43*m.b51 - 448*m.b38*m.b44*m.b45 - 320*m.b38*m.b44*m.b46 - 224*m.b38*m.b44*m.b47 - 128*
                       m.b38*m.b44*m.b48 - 96*m.b38*m.b44*m.b49 - 32*m.b38*m.b44*m.b51 - 352*m.b38*m.b45*m.b46 - 256*
                       m.b38*m.b45*m.b47 - 160*m.b38*m.b45*m.b48 - 96*m.b38*m.b45*m.b49 - 64*m.b38*m.b45*m.b50 - 32*
                       m.b38*m.b45*m.b51 - 288*m.b38*m.b46*m.b47 - 192*m.b38*m.b46*m.b48 - 96*m.b38*m.b46*m.b49 - 64*
                       m.b38*m.b46*m.b50 - 32*m.b38*m.b46*m.b51 - 224*m.b38*m.b47*m.b48 - 128*m.b38*m.b47*m.b49 - 64*
                       m.b38*m.b47*m.b50 - 32*m.b38*m.b47*m.b51 - 160*m.b38*m.b48*m.b49 - 64*m.b38*m.b48*m.b50 - 32*
                       m.b38*m.b48*m.b51 - 96*m.b38*m.b49*m.b50 - 32*m.b38*m.b49*m.b51 - 32*m.b38*m.b50*m.b51 - 704*
                       m.b39*m.b40*m.b41 - 960*m.b39*m.b40*m.b42 - 832*m.b39*m.b40*m.b43 - 704*m.b39*m.b40*m.b44 - 576*
                       m.b39*m.b40*m.b45 - 448*m.b39*m.b40*m.b46 - 352*m.b39*m.b40*m.b47 - 288*m.b39*m.b40*m.b48 - 224*
                       m.b39*m.b40*m.b49 - 160*m.b39*m.b40*m.b50 - 96*m.b39*m.b40*m.b51 - 32*m.b39*m.b40*m.b52 - 960*
                       m.b39*m.b41*m.b42 - 512*m.b39*m.b41*m.b43 - 704*m.b39*m.b41*m.b44 - 576*m.b39*m.b41*m.b45 - 448*
                       m.b39*m.b41*m.b46 - 320*m.b39*m.b41*m.b47 - 256*m.b39*m.b41*m.b48 - 192*m.b39*m.b41*m.b49 - 128*
                       m.b39*m.b41*m.b50 - 64*m.b39*m.b41*m.b51 - 32*m.b39*m.b41*m.b52 - 832*m.b39*m.b42*m.b43 - 704*
                       m.b39*m.b42*m.b44 - 320*m.b39*m.b42*m.b45 - 448*m.b39*m.b42*m.b46 - 320*m.b39*m.b42*m.b47 - 224*
                       m.b39*m.b42*m.b48 - 160*m.b39*m.b42*m.b49 - 96*m.b39*m.b42*m.b50 - 64*m.b39*m.b42*m.b51 - 32*
                       m.b39*m.b42*m.b52 - 704*m.b39*m.b43*m.b44 - 576*m.b39*m.b43*m.b45 - 448*m.b39*m.b43*m.b46 - 128*
                       m.b39*m.b43*m.b47 - 192*m.b39*m.b43*m.b48 - 128*m.b39*m.b43*m.b49 - 96*m.b39*m.b43*m.b50 - 64*
                       m.b39*m.b43*m.b51 - 32*m.b39*m.b43*m.b52 - 576*m.b39*m.b44*m.b45 - 448*m.b39*m.b44*m.b46 - 320*
                       m.b39*m.b44*m.b47 - 192*m.b39*m.b44*m.b48 - 96*m.b39*m.b44*m.b50 - 64*m.b39*m.b44*m.b51 - 32*
                       m.b39*m.b44*m.b52 - 448*m.b39*m.b45*m.b46 - 320*m.b39*m.b45*m.b47 - 224*m.b39*m.b45*m.b48 - 128*
                       m.b39*m.b45*m.b49 - 96*m.b39*m.b45*m.b50 - 32*m.b39*m.b45*m.b52 - 352*m.b39*m.b46*m.b47 - 256*
                       m.b39*m.b46*m.b48 - 160*m.b39*m.b46*m.b49 - 96*m.b39*m.b46*m.b50 - 64*m.b39*m.b46*m.b51 - 32*
                       m.b39*m.b46*m.b52 - 288*m.b39*m.b47*m.b48 - 192*m.b39*m.b47*m.b49 - 96*m.b39*m.b47*m.b50 - 64*
                       m.b39*m.b47*m.b51 - 32*m.b39*m.b47*m.b52 - 224*m.b39*m.b48*m.b49 - 128*m.b39*m.b48*m.b50 - 64*
                       m.b39*m.b48*m.b51 - 32*m.b39*m.b48*m.b52 - 160*m.b39*m.b49*m.b50 - 64*m.b39*m.b49*m.b51 - 32*
                       m.b39*m.b49*m.b52 - 96*m.b39*m.b50*m.b51 - 32*m.b39*m.b50*m.b52 - 32*m.b39*m.b51*m.b52 - 704*
                       m.b40*m.b41*m.b42 - 960*m.b40*m.b41*m.b43 - 832*m.b40*m.b41*m.b44 - 704*m.b40*m.b41*m.b45 - 576*
                       m.b40*m.b41*m.b46 - 448*m.b40*m.b41*m.b47 - 352*m.b40*m.b41*m.b48 - 288*m.b40*m.b41*m.b49 - 224*
                       m.b40*m.b41*m.b50 - 160*m.b40*m.b41*m.b51 - 96*m.b40*m.b41*m.b52 - 32*m.b40*m.b41*m.b53 - 960*
                       m.b40*m.b42*m.b43 - 512*m.b40*m.b42*m.b44 - 704*m.b40*m.b42*m.b45 - 576*m.b40*m.b42*m.b46 - 448*
                       m.b40*m.b42*m.b47 - 320*m.b40*m.b42*m.b48 - 256*m.b40*m.b42*m.b49 - 192*m.b40*m.b42*m.b50 - 128*
                       m.b40*m.b42*m.b51 - 64*m.b40*m.b42*m.b52 - 32*m.b40*m.b42*m.b53 - 832*m.b40*m.b43*m.b44 - 704*
                       m.b40*m.b43*m.b45 - 320*m.b40*m.b43*m.b46 - 448*m.b40*m.b43*m.b47 - 320*m.b40*m.b43*m.b48 - 224*
                       m.b40*m.b43*m.b49 - 160*m.b40*m.b43*m.b50 - 96*m.b40*m.b43*m.b51 - 64*m.b40*m.b43*m.b52 - 32*
                       m.b40*m.b43*m.b53 - 704*m.b40*m.b44*m.b45 - 576*m.b40*m.b44*m.b46 - 448*m.b40*m.b44*m.b47 - 128*
                       m.b40*m.b44*m.b48 - 192*m.b40*m.b44*m.b49 - 128*m.b40*m.b44*m.b50 - 96*m.b40*m.b44*m.b51 - 64*
                       m.b40*m.b44*m.b52 - 32*m.b40*m.b44*m.b53 - 576*m.b40*m.b45*m.b46 - 448*m.b40*m.b45*m.b47 - 320*
                       m.b40*m.b45*m.b48 - 192*m.b40*m.b45*m.b49 - 96*m.b40*m.b45*m.b51 - 64*m.b40*m.b45*m.b52 - 32*
                       m.b40*m.b45*m.b53 - 448*m.b40*m.b46*m.b47 - 320*m.b40*m.b46*m.b48 - 224*m.b40*m.b46*m.b49 - 128*
                       m.b40*m.b46*m.b50 - 96*m.b40*m.b46*m.b51 - 32*m.b40*m.b46*m.b53 - 352*m.b40*m.b47*m.b48 - 256*
                       m.b40*m.b47*m.b49 - 160*m.b40*m.b47*m.b50 - 96*m.b40*m.b47*m.b51 - 64*m.b40*m.b47*m.b52 - 32*
                       m.b40*m.b47*m.b53 - 288*m.b40*m.b48*m.b49 - 192*m.b40*m.b48*m.b50 - 96*m.b40*m.b48*m.b51 - 64*
                       m.b40*m.b48*m.b52 - 32*m.b40*m.b48*m.b53 - 224*m.b40*m.b49*m.b50 - 128*m.b40*m.b49*m.b51 - 64*
                       m.b40*m.b49*m.b52 - 32*m.b40*m.b49*m.b53 - 160*m.b40*m.b50*m.b51 - 64*m.b40*m.b50*m.b52 - 32*
                       m.b40*m.b50*m.b53 - 96*m.b40*m.b51*m.b52 - 32*m.b40*m.b51*m.b53 - 32*m.b40*m.b52*m.b53 - 704*
                       m.b41*m.b42*m.b43 - 960*m.b41*m.b42*m.b44 - 832*m.b41*m.b42*m.b45 - 704*m.b41*m.b42*m.b46 - 576*
                       m.b41*m.b42*m.b47 - 448*m.b41*m.b42*m.b48 - 352*m.b41*m.b42*m.b49 - 288*m.b41*m.b42*m.b50 - 224*
                       m.b41*m.b42*m.b51 - 160*m.b41*m.b42*m.b52 - 96*m.b41*m.b42*m.b53 - 32*m.b41*m.b42*m.b54 - 960*
                       m.b41*m.b43*m.b44 - 512*m.b41*m.b43*m.b45 - 704*m.b41*m.b43*m.b46 - 576*m.b41*m.b43*m.b47 - 448*
                       m.b41*m.b43*m.b48 - 320*m.b41*m.b43*m.b49 - 256*m.b41*m.b43*m.b50 - 192*m.b41*m.b43*m.b51 - 128*
                       m.b41*m.b43*m.b52 - 64*m.b41*m.b43*m.b53 - 32*m.b41*m.b43*m.b54 - 832*m.b41*m.b44*m.b45 - 704*
                       m.b41*m.b44*m.b46 - 320*m.b41*m.b44*m.b47 - 448*m.b41*m.b44*m.b48 - 320*m.b41*m.b44*m.b49 - 224*
                       m.b41*m.b44*m.b50 - 160*m.b41*m.b44*m.b51 - 96*m.b41*m.b44*m.b52 - 64*m.b41*m.b44*m.b53 - 32*
                       m.b41*m.b44*m.b54 - 704*m.b41*m.b45*m.b46 - 576*m.b41*m.b45*m.b47 - 448*m.b41*m.b45*m.b48 - 128*
                       m.b41*m.b45*m.b49 - 192*m.b41*m.b45*m.b50 - 128*m.b41*m.b45*m.b51 - 96*m.b41*m.b45*m.b52 - 64*
                       m.b41*m.b45*m.b53 - 32*m.b41*m.b45*m.b54 - 576*m.b41*m.b46*m.b47 - 448*m.b41*m.b46*m.b48 - 320*
                       m.b41*m.b46*m.b49 - 192*m.b41*m.b46*m.b50 - 96*m.b41*m.b46*m.b52 - 64*m.b41*m.b46*m.b53 - 32*
                       m.b41*m.b46*m.b54 - 448*m.b41*m.b47*m.b48 - 320*m.b41*m.b47*m.b49 - 224*m.b41*m.b47*m.b50 - 128*
                       m.b41*m.b47*m.b51 - 96*m.b41*m.b47*m.b52 - 32*m.b41*m.b47*m.b54 - 352*m.b41*m.b48*m.b49 - 256*
                       m.b41*m.b48*m.b50 - 160*m.b41*m.b48*m.b51 - 96*m.b41*m.b48*m.b52 - 64*m.b41*m.b48*m.b53 - 32*
                       m.b41*m.b48*m.b54 - 288*m.b41*m.b49*m.b50 - 192*m.b41*m.b49*m.b51 - 96*m.b41*m.b49*m.b52 - 64*
                       m.b41*m.b49*m.b53 - 32*m.b41*m.b49*m.b54 - 224*m.b41*m.b50*m.b51 - 128*m.b41*m.b50*m.b52 - 64*
                       m.b41*m.b50*m.b53 - 32*m.b41*m.b50*m.b54 - 160*m.b41*m.b51*m.b52 - 64*m.b41*m.b51*m.b53 - 32*
                       m.b41*m.b51*m.b54 - 96*m.b41*m.b52*m.b53 - 32*m.b41*m.b52*m.b54 - 32*m.b41*m.b53*m.b54 - 704*
                       m.b42*m.b43*m.b44 - 960*m.b42*m.b43*m.b45 - 832*m.b42*m.b43*m.b46 - 704*m.b42*m.b43*m.b47 - 576*
                       m.b42*m.b43*m.b48 - 448*m.b42*m.b43*m.b49 - 352*m.b42*m.b43*m.b50 - 288*m.b42*m.b43*m.b51 - 224*
                       m.b42*m.b43*m.b52 - 160*m.b42*m.b43*m.b53 - 96*m.b42*m.b43*m.b54 - 32*m.b42*m.b43*m.b55 - 960*
                       m.b42*m.b44*m.b45 - 512*m.b42*m.b44*m.b46 - 704*m.b42*m.b44*m.b47 - 576*m.b42*m.b44*m.b48 - 448*
                       m.b42*m.b44*m.b49 - 320*m.b42*m.b44*m.b50 - 256*m.b42*m.b44*m.b51 - 192*m.b42*m.b44*m.b52 - 128*
                       m.b42*m.b44*m.b53 - 64*m.b42*m.b44*m.b54 - 32*m.b42*m.b44*m.b55 - 832*m.b42*m.b45*m.b46 - 704*
                       m.b42*m.b45*m.b47 - 320*m.b42*m.b45*m.b48 - 448*m.b42*m.b45*m.b49 - 320*m.b42*m.b45*m.b50 - 224*
                       m.b42*m.b45*m.b51 - 160*m.b42*m.b45*m.b52 - 96*m.b42*m.b45*m.b53 - 64*m.b42*m.b45*m.b54 - 32*
                       m.b42*m.b45*m.b55 - 704*m.b42*m.b46*m.b47 - 576*m.b42*m.b46*m.b48 - 448*m.b42*m.b46*m.b49 - 128*
                       m.b42*m.b46*m.b50 - 192*m.b42*m.b46*m.b51 - 128*m.b42*m.b46*m.b52 - 96*m.b42*m.b46*m.b53 - 64*
                       m.b42*m.b46*m.b54 - 32*m.b42*m.b46*m.b55 - 576*m.b42*m.b47*m.b48 - 448*m.b42*m.b47*m.b49 - 320*
                       m.b42*m.b47*m.b50 - 192*m.b42*m.b47*m.b51 - 96*m.b42*m.b47*m.b53 - 64*m.b42*m.b47*m.b54 - 32*
                       m.b42*m.b47*m.b55 - 448*m.b42*m.b48*m.b49 - 320*m.b42*m.b48*m.b50 - 224*m.b42*m.b48*m.b51 - 128*
                       m.b42*m.b48*m.b52 - 96*m.b42*m.b48*m.b53 - 32*m.b42*m.b48*m.b55 - 352*m.b42*m.b49*m.b50 - 256*
                       m.b42*m.b49*m.b51 - 160*m.b42*m.b49*m.b52 - 96*m.b42*m.b49*m.b53 - 64*m.b42*m.b49*m.b54 - 32*
                       m.b42*m.b49*m.b55 - 288*m.b42*m.b50*m.b51 - 192*m.b42*m.b50*m.b52 - 96*m.b42*m.b50*m.b53 - 64*
                       m.b42*m.b50*m.b54 - 32*m.b42*m.b50*m.b55 - 224*m.b42*m.b51*m.b52 - 128*m.b42*m.b51*m.b53 - 64*
                       m.b42*m.b51*m.b54 - 32*m.b42*m.b51*m.b55 - 160*m.b42*m.b52*m.b53 - 64*m.b42*m.b52*m.b54 - 32*
                       m.b42*m.b52*m.b55 - 96*m.b42*m.b53*m.b54 - 32*m.b42*m.b53*m.b55 - 32*m.b42*m.b54*m.b55 - 672*
                       m.b43*m.b44*m.b45 - 896*m.b43*m.b44*m.b46 - 768*m.b43*m.b44*m.b47 - 640*m.b43*m.b44*m.b48 - 512*
                       m.b43*m.b44*m.b49 - 384*m.b43*m.b44*m.b50 - 288*m.b43*m.b44*m.b51 - 224*m.b43*m.b44*m.b52 - 160*
                       m.b43*m.b44*m.b53 - 96*m.b43*m.b44*m.b54 - 32*m.b43*m.b44*m.b55 - 896*m.b43*m.b45*m.b46 - 480*
                       m.b43*m.b45*m.b47 - 640*m.b43*m.b45*m.b48 - 512*m.b43*m.b45*m.b49 - 384*m.b43*m.b45*m.b50 - 256*
                       m.b43*m.b45*m.b51 - 192*m.b43*m.b45*m.b52 - 128*m.b43*m.b45*m.b53 - 64*m.b43*m.b45*m.b54 - 32*
                       m.b43*m.b45*m.b55 - 768*m.b43*m.b46*m.b47 - 640*m.b43*m.b46*m.b48 - 288*m.b43*m.b46*m.b49 - 384*
                       m.b43*m.b46*m.b50 - 256*m.b43*m.b46*m.b51 - 160*m.b43*m.b46*m.b52 - 96*m.b43*m.b46*m.b53 - 64*
                       m.b43*m.b46*m.b54 - 32*m.b43*m.b46*m.b55 - 640*m.b43*m.b47*m.b48 - 512*m.b43*m.b47*m.b49 - 384*
                       m.b43*m.b47*m.b50 - 96*m.b43*m.b47*m.b51 - 128*m.b43*m.b47*m.b52 - 96*m.b43*m.b47*m.b53 - 64*
                       m.b43*m.b47*m.b54 - 32*m.b43*m.b47*m.b55 - 512*m.b43*m.b48*m.b49 - 384*m.b43*m.b48*m.b50 - 256*
                       m.b43*m.b48*m.b51 - 160*m.b43*m.b48*m.b52 - 64*m.b43*m.b48*m.b54 - 32*m.b43*m.b48*m.b55 - 384*
                       m.b43*m.b49*m.b50 - 288*m.b43*m.b49*m.b51 - 192*m.b43*m.b49*m.b52 - 96*m.b43*m.b49*m.b53 - 64*
                       m.b43*m.b49*m.b54 - 320*m.b43*m.b50*m.b51 - 224*m.b43*m.b50*m.b52 - 128*m.b43*m.b50*m.b53 - 64*
                       m.b43*m.b50*m.b54 - 32*m.b43*m.b50*m.b55 - 256*m.b43*m.b51*m.b52 - 160*m.b43*m.b51*m.b53 - 64*
                       m.b43*m.b51*m.b54 - 32*m.b43*m.b51*m.b55 - 192*m.b43*m.b52*m.b53 - 96*m.b43*m.b52*m.b54 - 32*
                       m.b43*m.b52*m.b55 - 128*m.b43*m.b53*m.b54 - 32*m.b43*m.b53*m.b55 - 64*m.b43*m.b54*m.b55 - 608*
                       m.b44*m.b45*m.b46 - 832*m.b44*m.b45*m.b47 - 704*m.b44*m.b45*m.b48 - 576*m.b44*m.b45*m.b49 - 448*
                       m.b44*m.b45*m.b50 - 320*m.b44*m.b45*m.b51 - 224*m.b44*m.b45*m.b52 - 160*m.b44*m.b45*m.b53 - 96*
                       m.b44*m.b45*m.b54 - 32*m.b44*m.b45*m.b55 - 800*m.b44*m.b46*m.b47 - 448*m.b44*m.b46*m.b48 - 576*
                       m.b44*m.b46*m.b49 - 448*m.b44*m.b46*m.b50 - 320*m.b44*m.b46*m.b51 - 192*m.b44*m.b46*m.b52 - 128*
                       m.b44*m.b46*m.b53 - 64*m.b44*m.b46*m.b54 - 32*m.b44*m.b46*m.b55 - 672*m.b44*m.b47*m.b48 - 576*
                       m.b44*m.b47*m.b49 - 256*m.b44*m.b47*m.b50 - 320*m.b44*m.b47*m.b51 - 192*m.b44*m.b47*m.b52 - 96*
                       m.b44*m.b47*m.b53 - 64*m.b44*m.b47*m.b54 - 32*m.b44*m.b47*m.b55 - 544*m.b44*m.b48*m.b49 - 448*
                       m.b44*m.b48*m.b50 - 320*m.b44*m.b48*m.b51 - 64*m.b44*m.b48*m.b52 - 96*m.b44*m.b48*m.b53 - 64*
                       m.b44*m.b48*m.b54 - 32*m.b44*m.b48*m.b55 - 416*m.b44*m.b49*m.b50 - 320*m.b44*m.b49*m.b51 - 224*
                       m.b44*m.b49*m.b52 - 128*m.b44*m.b49*m.b53 - 32*m.b44*m.b49*m.b55 - 320*m.b44*m.b50*m.b51 - 256*
                       m.b44*m.b50*m.b52 - 160*m.b44*m.b50*m.b53 - 64*m.b44*m.b50*m.b54 - 32*m.b44*m.b50*m.b55 - 256*
                       m.b44*m.b51*m.b52 - 192*m.b44*m.b51*m.b53 - 96*m.b44*m.b51*m.b54 - 32*m.b44*m.b51*m.b55 - 192*
                       m.b44*m.b52*m.b53 - 128*m.b44*m.b52*m.b54 - 32*m.b44*m.b52*m.b55 - 128*m.b44*m.b53*m.b54 - 64*
                       m.b44*m.b53*m.b55 - 64*m.b44*m.b54*m.b55 - 544*m.b45*m.b46*m.b47 - 736*m.b45*m.b46*m.b48 - 640*
                       m.b45*m.b46*m.b49 - 512*m.b45*m.b46*m.b50 - 384*m.b45*m.b46*m.b51 - 256*m.b45*m.b46*m.b52 - 160*
                       m.b45*m.b46*m.b53 - 96*m.b45*m.b46*m.b54 - 32*m.b45*m.b46*m.b55 - 704*m.b45*m.b47*m.b48 - 384*
                       m.b45*m.b47*m.b49 - 512*m.b45*m.b47*m.b50 - 384*m.b45*m.b47*m.b51 - 256*m.b45*m.b47*m.b52 - 128*
                       m.b45*m.b47*m.b53 - 64*m.b45*m.b47*m.b54 - 32*m.b45*m.b47*m.b55 - 576*m.b45*m.b48*m.b49 - 480*
                       m.b45*m.b48*m.b50 - 224*m.b45*m.b48*m.b51 - 256*m.b45*m.b48*m.b52 - 128*m.b45*m.b48*m.b53 - 64*
                       m.b45*m.b48*m.b54 - 32*m.b45*m.b48*m.b55 - 448*m.b45*m.b49*m.b50 - 352*m.b45*m.b49*m.b51 - 256*
                       m.b45*m.b49*m.b52 - 64*m.b45*m.b49*m.b53 - 64*m.b45*m.b49*m.b54 - 32*m.b45*m.b49*m.b55 - 320*
                       m.b45*m.b50*m.b51 - 256*m.b45*m.b50*m.b52 - 192*m.b45*m.b50*m.b53 - 96*m.b45*m.b50*m.b54 - 256*
                       m.b45*m.b51*m.b52 - 192*m.b45*m.b51*m.b53 - 128*m.b45*m.b51*m.b54 - 32*m.b45*m.b51*m.b55 - 192*
                       m.b45*m.b52*m.b53 - 128*m.b45*m.b52*m.b54 - 64*m.b45*m.b52*m.b55 - 128*m.b45*m.b53*m.b54 - 64*
                       m.b45*m.b53*m.b55 - 64*m.b45*m.b54*m.b55 - 480*m.b46*m.b47*m.b48 - 640*m.b46*m.b47*m.b49 - 544*
                       m.b46*m.b47*m.b50 - 448*m.b46*m.b47*m.b51 - 320*m.b46*m.b47*m.b52 - 192*m.b46*m.b47*m.b53 - 96*
                       m.b46*m.b47*m.b54 - 32*m.b46*m.b47*m.b55 - 608*m.b46*m.b48*m.b49 - 320*m.b46*m.b48*m.b50 - 416*
                       m.b46*m.b48*m.b51 - 320*m.b46*m.b48*m.b52 - 192*m.b46*m.b48*m.b53 - 64*m.b46*m.b48*m.b54 - 32*
                       m.b46*m.b48*m.b55 - 480*m.b46*m.b49*m.b50 - 384*m.b46*m.b49*m.b51 - 160*m.b46*m.b49*m.b52 - 192*
                       m.b46*m.b49*m.b53 - 96*m.b46*m.b49*m.b54 - 32*m.b46*m.b49*m.b55 - 352*m.b46*m.b50*m.b51 - 256*
                       m.b46*m.b50*m.b52 - 192*m.b46*m.b50*m.b53 - 64*m.b46*m.b50*m.b54 - 32*m.b46*m.b50*m.b55 - 256*
                       m.b46*m.b51*m.b52 - 192*m.b46*m.b51*m.b53 - 128*m.b46*m.b51*m.b54 - 64*m.b46*m.b51*m.b55 - 192*
                       m.b46*m.b52*m.b53 - 128*m.b46*m.b52*m.b54 - 64*m.b46*m.b52*m.b55 - 128*m.b46*m.b53*m.b54 - 64*
                       m.b46*m.b53*m.b55 - 64*m.b46*m.b54*m.b55 - 416*m.b47*m.b48*m.b49 - 544*m.b47*m.b48*m.b50 - 448*
                       m.b47*m.b48*m.b51 - 352*m.b47*m.b48*m.b52 - 256*m.b47*m.b48*m.b53 - 128*m.b47*m.b48*m.b54 - 32*
                       m.b47*m.b48*m.b55 - 512*m.b47*m.b49*m.b50 - 256*m.b47*m.b49*m.b51 - 320*m.b47*m.b49*m.b52 - 224*
                       m.b47*m.b49*m.b53 - 128*m.b47*m.b49*m.b54 - 32*m.b47*m.b49*m.b55 - 384*m.b47*m.b50*m.b51 - 288*
                       m.b47*m.b50*m.b52 - 96*m.b47*m.b50*m.b53 - 128*m.b47*m.b50*m.b54 - 64*m.b47*m.b50*m.b55 - 256*
                       m.b47*m.b51*m.b52 - 192*m.b47*m.b51*m.b53 - 128*m.b47*m.b51*m.b54 - 32*m.b47*m.b51*m.b55 - 192*
                       m.b47*m.b52*m.b53 - 128*m.b47*m.b52*m.b54 - 64*m.b47*m.b52*m.b55 - 128*m.b47*m.b53*m.b54 - 64*
                       m.b47*m.b53*m.b55 - 64*m.b47*m.b54*m.b55 - 352*m.b48*m.b49*m.b50 - 448*m.b48*m.b49*m.b51 - 352*
                       m.b48*m.b49*m.b52 - 256*m.b48*m.b49*m.b53 - 160*m.b48*m.b49*m.b54 - 64*m.b48*m.b49*m.b55 - 416*
                       m.b48*m.b50*m.b51 - 192*m.b48*m.b50*m.b52 - 224*m.b48*m.b50*m.b53 - 128*m.b48*m.b50*m.b54 - 64*
                       m.b48*m.b50*m.b55 - 288*m.b48*m.b51*m.b52 - 192*m.b48*m.b51*m.b53 - 64*m.b48*m.b51*m.b54 - 64*
                       m.b48*m.b51*m.b55 - 192*m.b48*m.b52*m.b53 - 128*m.b48*m.b52*m.b54 - 64*m.b48*m.b52*m.b55 - 128*
                       m.b48*m.b53*m.b54 - 64*m.b48*m.b53*m.b55 - 64*m.b48*m.b54*m.b55 - 288*m.b49*m.b50*m.b51 - 352*
                       m.b49*m.b50*m.b52 - 256*m.b49*m.b50*m.b53 - 160*m.b49*m.b50*m.b54 - 64*m.b49*m.b50*m.b55 - 320*
                       m.b49*m.b51*m.b52 - 128*m.b49*m.b51*m.b53 - 128*m.b49*m.b51*m.b54 - 64*m.b49*m.b51*m.b55 - 192*
                       m.b49*m.b52*m.b53 - 128*m.b49*m.b52*m.b54 - 32*m.b49*m.b52*m.b55 - 128*m.b49*m.b53*m.b54 - 64*
                       m.b49*m.b53*m.b55 - 64*m.b49*m.b54*m.b55 - 224*m.b50*m.b51*m.b52 - 256*m.b50*m.b51*m.b53 - 160*
                       m.b50*m.b51*m.b54 - 64*m.b50*m.b51*m.b55 - 224*m.b50*m.b52*m.b53 - 64*m.b50*m.b52*m.b54 - 64*
                       m.b50*m.b52*m.b55 - 128*m.b50*m.b53*m.b54 - 64*m.b50*m.b53*m.b55 - 64*m.b50*m.b54*m.b55 - 160*
                       m.b51*m.b52*m.b53 - 160*m.b51*m.b52*m.b54 - 64*m.b51*m.b52*m.b55 - 128*m.b51*m.b53*m.b54 - 32*
                       m.b51*m.b53*m.b55 - 64*m.b51*m.b54*m.b55 - 96*m.b52*m.b53*m.b54 - 64*m.b52*m.b53*m.b55 - 64*m.b52
                       *m.b54*m.b55 - 32*m.b53*m.b54*m.b55 + 176*m.b1*m.b2 + 168*m.b1*m.b3 + 160*m.b1*m.b4 + 152*m.b1*
                       m.b5 + 144*m.b1*m.b6 + 136*m.b1*m.b7 + 144*m.b1*m.b8 + 136*m.b1*m.b9 + 128*m.b1*m.b10 + 120*m.b1*
                       m.b11 + 112*m.b1*m.b12 + 104*m.b1*m.b13 + 96*m.b1*m.b14 + 352*m.b2*m.b3 + 352*m.b2*m.b4 + 336*
                       m.b2*m.b5 + 320*m.b2*m.b6 + 304*m.b2*m.b7 + 288*m.b2*m.b8 + 304*m.b2*m.b9 + 288*m.b2*m.b10 + 272*
                       m.b2*m.b11 + 256*m.b2*m.b12 + 240*m.b2*m.b13 + 208*m.b2*m.b14 + 96*m.b2*m.b15 + 544*m.b3*m.b4 + 
                       536*m.b3*m.b5 + 528*m.b3*m.b6 + 504*m.b3*m.b7 + 480*m.b3*m.b8 + 472*m.b3*m.b9 + 480*m.b3*m.b10 + 
                       456*m.b3*m.b11 + 432*m.b3*m.b12 + 392*m.b3*m.b13 + 352*m.b3*m.b14 + 208*m.b3*m.b15 + 96*m.b3*
                       m.b16 + 752*m.b4*m.b5 + 736*m.b4*m.b6 + 720*m.b4*m.b7 + 704*m.b4*m.b8 + 672*m.b4*m.b9 + 672*m.b4*
                       m.b10 + 672*m.b4*m.b11 + 624*m.b4*m.b12 + 576*m.b4*m.b13 + 512*m.b4*m.b14 + 352*m.b4*m.b15 + 208*
                       m.b4*m.b16 + 96*m.b4*m.b17 + 976*m.b5*m.b6 + 952*m.b5*m.b7 + 928*m.b5*m.b8 + 904*m.b5*m.b9 + 896*
                       m.b5*m.b10 + 872*m.b5*m.b11 + 848*m.b5*m.b12 + 776*m.b5*m.b13 + 704*m.b5*m.b14 + 512*m.b5*m.b15
                        + 352*m.b5*m.b16 + 208*m.b5*m.b17 + 96*m.b5*m.b18 + 1216*m.b6*m.b7 + 1184*m.b6*m.b8 + 1152*m.b6*
                       m.b9 + 1104*m.b6*m.b10 + 1088*m.b6*m.b11 + 1056*m.b6*m.b12 + 1008*m.b6*m.b13 + 912*m.b6*m.b14 + 
                       704*m.b6*m.b15 + 512*m.b6*m.b16 + 352*m.b6*m.b17 + 208*m.b6*m.b18 + 96*m.b6*m.b19 + 1472*m.b7*
                       m.b8 + 1416*m.b7*m.b9 + 1360*m.b7*m.b10 + 1304*m.b7*m.b11 + 1264*m.b7*m.b12 + 1208*m.b7*m.b13 + 
                       1152*m.b7*m.b14 + 912*m.b7*m.b15 + 704*m.b7*m.b16 + 512*m.b7*m.b17 + 352*m.b7*m.b18 + 208*m.b7*
                       m.b19 + 96*m.b7*m.b20 + 1712*m.b8*m.b9 + 1632*m.b8*m.b10 + 1552*m.b8*m.b11 + 1488*m.b8*m.b12 + 
                       1424*m.b8*m.b13 + 1344*m.b8*m.b14 + 1152*m.b8*m.b15 + 912*m.b8*m.b16 + 704*m.b8*m.b17 + 512*m.b8*
                       m.b18 + 352*m.b8*m.b19 + 208*m.b8*m.b20 + 96*m.b8*m.b21 + 1936*m.b9*m.b10 + 1832*m.b9*m.b11 + 
                       1744*m.b9*m.b12 + 1656*m.b9*m.b13 + 1568*m.b9*m.b14 + 1344*m.b9*m.b15 + 1152*m.b9*m.b16 + 912*
                       m.b9*m.b17 + 704*m.b9*m.b18 + 512*m.b9*m.b19 + 352*m.b9*m.b20 + 208*m.b9*m.b21 + 96*m.b9*m.b22 + 
                       2144*m.b10*m.b11 + 2016*m.b10*m.b12 + 1920*m.b10*m.b13 + 1808*m.b10*m.b14 + 1568*m.b10*m.b15 + 
                       1344*m.b10*m.b16 + 1152*m.b10*m.b17 + 912*m.b10*m.b18 + 704*m.b10*m.b19 + 512*m.b10*m.b20 + 352*
                       m.b10*m.b21 + 208*m.b10*m.b22 + 96*m.b10*m.b23 + 2336*m.b11*m.b12 + 2200*m.b11*m.b13 + 2080*m.b11
                       *m.b14 + 1808*m.b11*m.b15 + 1568*m.b11*m.b16 + 1344*m.b11*m.b17 + 1152*m.b11*m.b18 + 912*m.b11*
                       m.b19 + 704*m.b11*m.b20 + 512*m.b11*m.b21 + 352*m.b11*m.b22 + 208*m.b11*m.b23 + 96*m.b11*m.b24 + 
                       2512*m.b12*m.b13 + 2368*m.b12*m.b14 + 2080*m.b12*m.b15 + 1808*m.b12*m.b16 + 1568*m.b12*m.b17 + 
                       1344*m.b12*m.b18 + 1152*m.b12*m.b19 + 912*m.b12*m.b20 + 704*m.b12*m.b21 + 512*m.b12*m.b22 + 352*
                       m.b12*m.b23 + 208*m.b12*m.b24 + 96*m.b12*m.b25 + 2688*m.b13*m.b14 + 2368*m.b13*m.b15 + 2080*m.b13
                       *m.b16 + 1808*m.b13*m.b17 + 1568*m.b13*m.b18 + 1344*m.b13*m.b19 + 1152*m.b13*m.b20 + 912*m.b13*
                       m.b21 + 704*m.b13*m.b22 + 512*m.b13*m.b23 + 352*m.b13*m.b24 + 208*m.b13*m.b25 + 96*m.b13*m.b26 + 
                       2688*m.b14*m.b15 + 2368*m.b14*m.b16 + 2080*m.b14*m.b17 + 1808*m.b14*m.b18 + 1568*m.b14*m.b19 + 
                       1344*m.b14*m.b20 + 1152*m.b14*m.b21 + 912*m.b14*m.b22 + 704*m.b14*m.b23 + 512*m.b14*m.b24 + 352*
                       m.b14*m.b25 + 208*m.b14*m.b26 + 96*m.b14*m.b27 + 2688*m.b15*m.b16 + 2368*m.b15*m.b17 + 2080*m.b15
                       *m.b18 + 1808*m.b15*m.b19 + 1568*m.b15*m.b20 + 1344*m.b15*m.b21 + 1152*m.b15*m.b22 + 912*m.b15*
                       m.b23 + 704*m.b15*m.b24 + 512*m.b15*m.b25 + 352*m.b15*m.b26 + 208*m.b15*m.b27 + 96*m.b15*m.b28 + 
                       2688*m.b16*m.b17 + 2368*m.b16*m.b18 + 2080*m.b16*m.b19 + 1808*m.b16*m.b20 + 1568*m.b16*m.b21 + 
                       1344*m.b16*m.b22 + 1152*m.b16*m.b23 + 912*m.b16*m.b24 + 704*m.b16*m.b25 + 512*m.b16*m.b26 + 352*
                       m.b16*m.b27 + 208*m.b16*m.b28 + 96*m.b16*m.b29 + 2688*m.b17*m.b18 + 2368*m.b17*m.b19 + 2080*m.b17
                       *m.b20 + 1808*m.b17*m.b21 + 1568*m.b17*m.b22 + 1344*m.b17*m.b23 + 1152*m.b17*m.b24 + 912*m.b17*
                       m.b25 + 704*m.b17*m.b26 + 512*m.b17*m.b27 + 352*m.b17*m.b28 + 208*m.b17*m.b29 + 96*m.b17*m.b30 + 
                       2688*m.b18*m.b19 + 2368*m.b18*m.b20 + 2080*m.b18*m.b21 + 1808*m.b18*m.b22 + 1568*m.b18*m.b23 + 
                       1344*m.b18*m.b24 + 1152*m.b18*m.b25 + 912*m.b18*m.b26 + 704*m.b18*m.b27 + 512*m.b18*m.b28 + 352*
                       m.b18*m.b29 + 208*m.b18*m.b30 + 96*m.b18*m.b31 + 2688*m.b19*m.b20 + 2368*m.b19*m.b21 + 2080*m.b19
                       *m.b22 + 1808*m.b19*m.b23 + 1568*m.b19*m.b24 + 1344*m.b19*m.b25 + 1152*m.b19*m.b26 + 912*m.b19*
                       m.b27 + 704*m.b19*m.b28 + 512*m.b19*m.b29 + 352*m.b19*m.b30 + 208*m.b19*m.b31 + 96*m.b19*m.b32 + 
                       2688*m.b20*m.b21 + 2368*m.b20*m.b22 + 2080*m.b20*m.b23 + 1808*m.b20*m.b24 + 1568*m.b20*m.b25 + 
                       1344*m.b20*m.b26 + 1152*m.b20*m.b27 + 912*m.b20*m.b28 + 704*m.b20*m.b29 + 512*m.b20*m.b30 + 352*
                       m.b20*m.b31 + 208*m.b20*m.b32 + 96*m.b20*m.b33 + 2688*m.b21*m.b22 + 2368*m.b21*m.b23 + 2080*m.b21
                       *m.b24 + 1808*m.b21*m.b25 + 1568*m.b21*m.b26 + 1344*m.b21*m.b27 + 1152*m.b21*m.b28 + 912*m.b21*
                       m.b29 + 704*m.b21*m.b30 + 512*m.b21*m.b31 + 352*m.b21*m.b32 + 208*m.b21*m.b33 + 96*m.b21*m.b34 + 
                       2688*m.b22*m.b23 + 2368*m.b22*m.b24 + 2080*m.b22*m.b25 + 1808*m.b22*m.b26 + 1568*m.b22*m.b27 + 
                       1344*m.b22*m.b28 + 1152*m.b22*m.b29 + 912*m.b22*m.b30 + 704*m.b22*m.b31 + 512*m.b22*m.b32 + 352*
                       m.b22*m.b33 + 208*m.b22*m.b34 + 96*m.b22*m.b35 + 2688*m.b23*m.b24 + 2368*m.b23*m.b25 + 2080*m.b23
                       *m.b26 + 1808*m.b23*m.b27 + 1568*m.b23*m.b28 + 1344*m.b23*m.b29 + 1152*m.b23*m.b30 + 912*m.b23*
                       m.b31 + 704*m.b23*m.b32 + 512*m.b23*m.b33 + 352*m.b23*m.b34 + 208*m.b23*m.b35 + 96*m.b23*m.b36 + 
                       2688*m.b24*m.b25 + 2368*m.b24*m.b26 + 2080*m.b24*m.b27 + 1808*m.b24*m.b28 + 1568*m.b24*m.b29 + 
                       1344*m.b24*m.b30 + 1152*m.b24*m.b31 + 912*m.b24*m.b32 + 704*m.b24*m.b33 + 512*m.b24*m.b34 + 352*
                       m.b24*m.b35 + 208*m.b24*m.b36 + 96*m.b24*m.b37 + 2688*m.b25*m.b26 + 2368*m.b25*m.b27 + 2080*m.b25
                       *m.b28 + 1808*m.b25*m.b29 + 1568*m.b25*m.b30 + 1344*m.b25*m.b31 + 1152*m.b25*m.b32 + 912*m.b25*
                       m.b33 + 704*m.b25*m.b34 + 512*m.b25*m.b35 + 352*m.b25*m.b36 + 208*m.b25*m.b37 + 96*m.b25*m.b38 + 
                       2688*m.b26*m.b27 + 2368*m.b26*m.b28 + 2080*m.b26*m.b29 + 1808*m.b26*m.b30 + 1568*m.b26*m.b31 + 
                       1344*m.b26*m.b32 + 1152*m.b26*m.b33 + 912*m.b26*m.b34 + 704*m.b26*m.b35 + 512*m.b26*m.b36 + 352*
                       m.b26*m.b37 + 208*m.b26*m.b38 + 96*m.b26*m.b39 + 2688*m.b27*m.b28 + 2368*m.b27*m.b29 + 2080*m.b27
                       *m.b30 + 1808*m.b27*m.b31 + 1568*m.b27*m.b32 + 1344*m.b27*m.b33 + 1152*m.b27*m.b34 + 912*m.b27*
                       m.b35 + 704*m.b27*m.b36 + 512*m.b27*m.b37 + 352*m.b27*m.b38 + 208*m.b27*m.b39 + 96*m.b27*m.b40 + 
                       2688*m.b28*m.b29 + 2368*m.b28*m.b30 + 2080*m.b28*m.b31 + 1808*m.b28*m.b32 + 1568*m.b28*m.b33 + 
                       1344*m.b28*m.b34 + 1152*m.b28*m.b35 + 912*m.b28*m.b36 + 704*m.b28*m.b37 + 512*m.b28*m.b38 + 352*
                       m.b28*m.b39 + 208*m.b28*m.b40 + 96*m.b28*m.b41 + 2688*m.b29*m.b30 + 2368*m.b29*m.b31 + 2080*m.b29
                       *m.b32 + 1808*m.b29*m.b33 + 1568*m.b29*m.b34 + 1344*m.b29*m.b35 + 1152*m.b29*m.b36 + 912*m.b29*
                       m.b37 + 704*m.b29*m.b38 + 512*m.b29*m.b39 + 352*m.b29*m.b40 + 208*m.b29*m.b41 + 96*m.b29*m.b42 + 
                       2688*m.b30*m.b31 + 2368*m.b30*m.b32 + 2080*m.b30*m.b33 + 1808*m.b30*m.b34 + 1568*m.b30*m.b35 + 
                       1344*m.b30*m.b36 + 1152*m.b30*m.b37 + 912*m.b30*m.b38 + 704*m.b30*m.b39 + 512*m.b30*m.b40 + 352*
                       m.b30*m.b41 + 208*m.b30*m.b42 + 96*m.b30*m.b43 + 2688*m.b31*m.b32 + 2368*m.b31*m.b33 + 2080*m.b31
                       *m.b34 + 1808*m.b31*m.b35 + 1568*m.b31*m.b36 + 1344*m.b31*m.b37 + 1152*m.b31*m.b38 + 912*m.b31*
                       m.b39 + 704*m.b31*m.b40 + 512*m.b31*m.b41 + 352*m.b31*m.b42 + 208*m.b31*m.b43 + 96*m.b31*m.b44 + 
                       2688*m.b32*m.b33 + 2368*m.b32*m.b34 + 2080*m.b32*m.b35 + 1808*m.b32*m.b36 + 1568*m.b32*m.b37 + 
                       1344*m.b32*m.b38 + 1152*m.b32*m.b39 + 912*m.b32*m.b40 + 704*m.b32*m.b41 + 512*m.b32*m.b42 + 352*
                       m.b32*m.b43 + 208*m.b32*m.b44 + 96*m.b32*m.b45 + 2688*m.b33*m.b34 + 2368*m.b33*m.b35 + 2080*m.b33
                       *m.b36 + 1808*m.b33*m.b37 + 1568*m.b33*m.b38 + 1344*m.b33*m.b39 + 1152*m.b33*m.b40 + 912*m.b33*
                       m.b41 + 704*m.b33*m.b42 + 512*m.b33*m.b43 + 352*m.b33*m.b44 + 208*m.b33*m.b45 + 96*m.b33*m.b46 + 
                       2688*m.b34*m.b35 + 2368*m.b34*m.b36 + 2080*m.b34*m.b37 + 1808*m.b34*m.b38 + 1568*m.b34*m.b39 + 
                       1344*m.b34*m.b40 + 1152*m.b34*m.b41 + 912*m.b34*m.b42 + 704*m.b34*m.b43 + 512*m.b34*m.b44 + 352*
                       m.b34*m.b45 + 208*m.b34*m.b46 + 96*m.b34*m.b47 + 2688*m.b35*m.b36 + 2368*m.b35*m.b37 + 2080*m.b35
                       *m.b38 + 1808*m.b35*m.b39 + 1568*m.b35*m.b40 + 1344*m.b35*m.b41 + 1152*m.b35*m.b42 + 912*m.b35*
                       m.b43 + 704*m.b35*m.b44 + 512*m.b35*m.b45 + 352*m.b35*m.b46 + 208*m.b35*m.b47 + 96*m.b35*m.b48 + 
                       2688*m.b36*m.b37 + 2368*m.b36*m.b38 + 2080*m.b36*m.b39 + 1808*m.b36*m.b40 + 1568*m.b36*m.b41 + 
                       1344*m.b36*m.b42 + 1152*m.b36*m.b43 + 912*m.b36*m.b44 + 704*m.b36*m.b45 + 512*m.b36*m.b46 + 352*
                       m.b36*m.b47 + 208*m.b36*m.b48 + 96*m.b36*m.b49 + 2688*m.b37*m.b38 + 2368*m.b37*m.b39 + 2080*m.b37
                       *m.b40 + 1808*m.b37*m.b41 + 1568*m.b37*m.b42 + 1344*m.b37*m.b43 + 1152*m.b37*m.b44 + 912*m.b37*
                       m.b45 + 704*m.b37*m.b46 + 512*m.b37*m.b47 + 352*m.b37*m.b48 + 208*m.b37*m.b49 + 96*m.b37*m.b50 + 
                       2688*m.b38*m.b39 + 2368*m.b38*m.b40 + 2080*m.b38*m.b41 + 1808*m.b38*m.b42 + 1568*m.b38*m.b43 + 
                       1344*m.b38*m.b44 + 1152*m.b38*m.b45 + 912*m.b38*m.b46 + 704*m.b38*m.b47 + 512*m.b38*m.b48 + 352*
                       m.b38*m.b49 + 208*m.b38*m.b50 + 96*m.b38*m.b51 + 2688*m.b39*m.b40 + 2368*m.b39*m.b41 + 2080*m.b39
                       *m.b42 + 1808*m.b39*m.b43 + 1568*m.b39*m.b44 + 1344*m.b39*m.b45 + 1152*m.b39*m.b46 + 912*m.b39*
                       m.b47 + 704*m.b39*m.b48 + 512*m.b39*m.b49 + 352*m.b39*m.b50 + 208*m.b39*m.b51 + 96*m.b39*m.b52 + 
                       2688*m.b40*m.b41 + 2368*m.b40*m.b42 + 2080*m.b40*m.b43 + 1808*m.b40*m.b44 + 1568*m.b40*m.b45 + 
                       1344*m.b40*m.b46 + 1152*m.b40*m.b47 + 912*m.b40*m.b48 + 704*m.b40*m.b49 + 512*m.b40*m.b50 + 352*
                       m.b40*m.b51 + 208*m.b40*m.b52 + 96*m.b40*m.b53 + 2688*m.b41*m.b42 + 2368*m.b41*m.b43 + 2080*m.b41
                       *m.b44 + 1808*m.b41*m.b45 + 1568*m.b41*m.b46 + 1344*m.b41*m.b47 + 1152*m.b41*m.b48 + 912*m.b41*
                       m.b49 + 704*m.b41*m.b50 + 512*m.b41*m.b51 + 352*m.b41*m.b52 + 208*m.b41*m.b53 + 96*m.b41*m.b54 + 
                       2688*m.b42*m.b43 + 2368*m.b42*m.b44 + 2080*m.b42*m.b45 + 1808*m.b42*m.b46 + 1568*m.b42*m.b47 + 
                       1344*m.b42*m.b48 + 1152*m.b42*m.b49 + 912*m.b42*m.b50 + 704*m.b42*m.b51 + 512*m.b42*m.b52 + 352*
                       m.b42*m.b53 + 208*m.b42*m.b54 + 96*m.b42*m.b55 + 2512*m.b43*m.b44 + 2200*m.b43*m.b45 + 1920*m.b43
                       *m.b46 + 1656*m.b43*m.b47 + 1424*m.b43*m.b48 + 1208*m.b43*m.b49 + 1008*m.b43*m.b50 + 776*m.b43*
                       m.b51 + 576*m.b43*m.b52 + 392*m.b43*m.b53 + 240*m.b43*m.b54 + 104*m.b43*m.b55 + 2336*m.b44*m.b45
                        + 2016*m.b44*m.b46 + 1744*m.b44*m.b47 + 1488*m.b44*m.b48 + 1264*m.b44*m.b49 + 1056*m.b44*m.b50
                        + 848*m.b44*m.b51 + 624*m.b44*m.b52 + 432*m.b44*m.b53 + 256*m.b44*m.b54 + 112*m.b44*m.b55 + 2144
                       *m.b45*m.b46 + 1832*m.b45*m.b47 + 1552*m.b45*m.b48 + 1304*m.b45*m.b49 + 1088*m.b45*m.b50 + 872*
                       m.b45*m.b51 + 672*m.b45*m.b52 + 456*m.b45*m.b53 + 272*m.b45*m.b54 + 120*m.b45*m.b55 + 1936*m.b46*
                       m.b47 + 1632*m.b46*m.b48 + 1360*m.b46*m.b49 + 1104*m.b46*m.b50 + 896*m.b46*m.b51 + 672*m.b46*
                       m.b52 + 480*m.b46*m.b53 + 288*m.b46*m.b54 + 128*m.b46*m.b55 + 1712*m.b47*m.b48 + 1416*m.b47*m.b49
                        + 1152*m.b47*m.b50 + 904*m.b47*m.b51 + 672*m.b47*m.b52 + 472*m.b47*m.b53 + 304*m.b47*m.b54 + 136
                       *m.b47*m.b55 + 1472*m.b48*m.b49 + 1184*m.b48*m.b50 + 928*m.b48*m.b51 + 704*m.b48*m.b52 + 480*
                       m.b48*m.b53 + 288*m.b48*m.b54 + 144*m.b48*m.b55 + 1216*m.b49*m.b50 + 952*m.b49*m.b51 + 720*m.b49*
                       m.b52 + 504*m.b49*m.b53 + 304*m.b49*m.b54 + 136*m.b49*m.b55 + 976*m.b50*m.b51 + 736*m.b50*m.b52
                        + 528*m.b50*m.b53 + 320*m.b50*m.b54 + 144*m.b50*m.b55 + 752*m.b51*m.b52 + 536*m.b51*m.b53 + 336*
                       m.b51*m.b54 + 152*m.b51*m.b55 + 544*m.b52*m.b53 + 352*m.b52*m.b54 + 160*m.b52*m.b55 + 352*m.b53*
                       m.b54 + 168*m.b53*m.b55 + 176*m.b54*m.b55 - 312*m.b1 - 664*m.b2 - 1048*m.b3 - 1456*m.b4 - 1880*
                       m.b5 - 2312*m.b6 - 2744*m.b7 - 3176*m.b8 - 3608*m.b9 - 4032*m.b10 - 4440*m.b11 - 4824*m.b12 - 
                       5176*m.b13 - 5488*m.b14 - 5488*m.b15 - 5488*m.b16 - 5488*m.b17 - 5488*m.b18 - 5488*m.b19 - 5488*
                       m.b20 - 5488*m.b21 - 5488*m.b22 - 5488*m.b23 - 5488*m.b24 - 5488*m.b25 - 5488*m.b26 - 5488*m.b27
                        - 5488*m.b28 - 5488*m.b29 - 5488*m.b30 - 5488*m.b31 - 5488*m.b32 - 5488*m.b33 - 5488*m.b34 - 
                       5488*m.b35 - 5488*m.b36 - 5488*m.b37 - 5488*m.b38 - 5488*m.b39 - 5488*m.b40 - 5488*m.b41 - 5488*
                       m.b42 - 5176*m.b43 - 4824*m.b44 - 4440*m.b45 - 4032*m.b46 - 3608*m.b47 - 3176*m.b48 - 2744*m.b49
                        - 2312*m.b50 - 1880*m.b51 - 1456*m.b52 - 1048*m.b53 - 664*m.b54 - 312*m.b55 - m.x56 <= 0)
