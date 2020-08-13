#  MINLP written by GAMS Convert at 08/13/20 17:37:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         36        1       35        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         36        1       35        0


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
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x36, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*
                       m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*
                       m.b6*m.b9 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*
                       m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 64*m.b2*m.b3*m.b9*m.b10 + 128*m.b2*m.b4*m.b5*m.b7
                        + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 64*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*m.b5*
                       m.b6*m.b9 + 64*m.b2*m.b5*m.b7*m.b10 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 192*
                       m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 128*m.b3*m.b4*m.b9*m.b10 + 64*m.b3*m.b4*m.b10*
                       m.b11 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 128*m.b3*m.b5*m.b8*m.b10 + 64*m.b3*
                       m.b5*m.b9*m.b11 + 128*m.b3*m.b6*m.b7*m.b10 + 64*m.b3*m.b6*m.b8*m.b11 + 256*m.b4*m.b5*m.b6*m.b7 + 
                       256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4*m.b5*m.b8*m.b9 + 192*m.b4*m.b5*m.b9*m.b10 + 128*m.b4*m.b5*
                       m.b10*m.b11 + 64*m.b4*m.b5*m.b11*m.b12 + 256*m.b4*m.b6*m.b7*m.b9 + 192*m.b4*m.b6*m.b8*m.b10 + 128
                       *m.b4*m.b6*m.b9*m.b11 + 64*m.b4*m.b6*m.b10*m.b12 + 128*m.b4*m.b7*m.b8*m.b11 + 64*m.b4*m.b7*m.b9*
                       m.b12 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 256*m.b5*m.b6*m.b9*m.b10 + 192*m.b5*
                       m.b6*m.b10*m.b11 + 128*m.b5*m.b6*m.b11*m.b12 + 64*m.b5*m.b6*m.b12*m.b13 + 256*m.b5*m.b7*m.b8*
                       m.b10 + 192*m.b5*m.b7*m.b9*m.b11 + 128*m.b5*m.b7*m.b10*m.b12 + 64*m.b5*m.b7*m.b11*m.b13 + 128*
                       m.b5*m.b8*m.b9*m.b12 + 64*m.b5*m.b8*m.b10*m.b13 + 384*m.b6*m.b7*m.b8*m.b9 + 320*m.b6*m.b7*m.b9*
                       m.b10 + 256*m.b6*m.b7*m.b10*m.b11 + 192*m.b6*m.b7*m.b11*m.b12 + 128*m.b6*m.b7*m.b12*m.b13 + 64*
                       m.b6*m.b7*m.b13*m.b14 + 256*m.b6*m.b8*m.b9*m.b11 + 192*m.b6*m.b8*m.b10*m.b12 + 128*m.b6*m.b8*
                       m.b11*m.b13 + 64*m.b6*m.b8*m.b12*m.b14 + 128*m.b6*m.b9*m.b10*m.b13 + 64*m.b6*m.b9*m.b11*m.b14 + 
                       384*m.b7*m.b8*m.b9*m.b10 + 320*m.b7*m.b8*m.b10*m.b11 + 256*m.b7*m.b8*m.b11*m.b12 + 192*m.b7*m.b8*
                       m.b12*m.b13 + 128*m.b7*m.b8*m.b13*m.b14 + 64*m.b7*m.b8*m.b14*m.b15 + 256*m.b7*m.b9*m.b10*m.b12 + 
                       192*m.b7*m.b9*m.b11*m.b13 + 128*m.b7*m.b9*m.b12*m.b14 + 64*m.b7*m.b9*m.b13*m.b15 + 128*m.b7*m.b10
                       *m.b11*m.b14 + 64*m.b7*m.b10*m.b12*m.b15 + 384*m.b8*m.b9*m.b10*m.b11 + 320*m.b8*m.b9*m.b11*m.b12
                        + 256*m.b8*m.b9*m.b12*m.b13 + 192*m.b8*m.b9*m.b13*m.b14 + 128*m.b8*m.b9*m.b14*m.b15 + 64*m.b8*
                       m.b9*m.b15*m.b16 + 256*m.b8*m.b10*m.b11*m.b13 + 192*m.b8*m.b10*m.b12*m.b14 + 128*m.b8*m.b10*m.b13
                       *m.b15 + 64*m.b8*m.b10*m.b14*m.b16 + 128*m.b8*m.b11*m.b12*m.b15 + 64*m.b8*m.b11*m.b13*m.b16 + 384
                       *m.b9*m.b10*m.b11*m.b12 + 320*m.b9*m.b10*m.b12*m.b13 + 256*m.b9*m.b10*m.b13*m.b14 + 192*m.b9*
                       m.b10*m.b14*m.b15 + 128*m.b9*m.b10*m.b15*m.b16 + 64*m.b9*m.b10*m.b16*m.b17 + 256*m.b9*m.b11*m.b12
                       *m.b14 + 192*m.b9*m.b11*m.b13*m.b15 + 128*m.b9*m.b11*m.b14*m.b16 + 64*m.b9*m.b11*m.b15*m.b17 + 
                       128*m.b9*m.b12*m.b13*m.b16 + 64*m.b9*m.b12*m.b14*m.b17 + 384*m.b10*m.b11*m.b12*m.b13 + 320*m.b10*
                       m.b11*m.b13*m.b14 + 256*m.b10*m.b11*m.b14*m.b15 + 192*m.b10*m.b11*m.b15*m.b16 + 128*m.b10*m.b11*
                       m.b16*m.b17 + 64*m.b10*m.b11*m.b17*m.b18 + 256*m.b10*m.b12*m.b13*m.b15 + 192*m.b10*m.b12*m.b14*
                       m.b16 + 128*m.b10*m.b12*m.b15*m.b17 + 64*m.b10*m.b12*m.b16*m.b18 + 128*m.b10*m.b13*m.b14*m.b17 + 
                       64*m.b10*m.b13*m.b15*m.b18 + 384*m.b11*m.b12*m.b13*m.b14 + 320*m.b11*m.b12*m.b14*m.b15 + 256*
                       m.b11*m.b12*m.b15*m.b16 + 192*m.b11*m.b12*m.b16*m.b17 + 128*m.b11*m.b12*m.b17*m.b18 + 64*m.b11*
                       m.b12*m.b18*m.b19 + 256*m.b11*m.b13*m.b14*m.b16 + 192*m.b11*m.b13*m.b15*m.b17 + 128*m.b11*m.b13*
                       m.b16*m.b18 + 64*m.b11*m.b13*m.b17*m.b19 + 128*m.b11*m.b14*m.b15*m.b18 + 64*m.b11*m.b14*m.b16*
                       m.b19 + 384*m.b12*m.b13*m.b14*m.b15 + 320*m.b12*m.b13*m.b15*m.b16 + 256*m.b12*m.b13*m.b16*m.b17
                        + 192*m.b12*m.b13*m.b17*m.b18 + 128*m.b12*m.b13*m.b18*m.b19 + 64*m.b12*m.b13*m.b19*m.b20 + 256*
                       m.b12*m.b14*m.b15*m.b17 + 192*m.b12*m.b14*m.b16*m.b18 + 128*m.b12*m.b14*m.b17*m.b19 + 64*m.b12*
                       m.b14*m.b18*m.b20 + 128*m.b12*m.b15*m.b16*m.b19 + 64*m.b12*m.b15*m.b17*m.b20 + 384*m.b13*m.b14*
                       m.b15*m.b16 + 320*m.b13*m.b14*m.b16*m.b17 + 256*m.b13*m.b14*m.b17*m.b18 + 192*m.b13*m.b14*m.b18*
                       m.b19 + 128*m.b13*m.b14*m.b19*m.b20 + 64*m.b13*m.b14*m.b20*m.b21 + 256*m.b13*m.b15*m.b16*m.b18 + 
                       192*m.b13*m.b15*m.b17*m.b19 + 128*m.b13*m.b15*m.b18*m.b20 + 64*m.b13*m.b15*m.b19*m.b21 + 128*
                       m.b13*m.b16*m.b17*m.b20 + 64*m.b13*m.b16*m.b18*m.b21 + 384*m.b14*m.b15*m.b16*m.b17 + 320*m.b14*
                       m.b15*m.b17*m.b18 + 256*m.b14*m.b15*m.b18*m.b19 + 192*m.b14*m.b15*m.b19*m.b20 + 128*m.b14*m.b15*
                       m.b20*m.b21 + 64*m.b14*m.b15*m.b21*m.b22 + 256*m.b14*m.b16*m.b17*m.b19 + 192*m.b14*m.b16*m.b18*
                       m.b20 + 128*m.b14*m.b16*m.b19*m.b21 + 64*m.b14*m.b16*m.b20*m.b22 + 128*m.b14*m.b17*m.b18*m.b21 + 
                       64*m.b14*m.b17*m.b19*m.b22 + 384*m.b15*m.b16*m.b17*m.b18 + 320*m.b15*m.b16*m.b18*m.b19 + 256*
                       m.b15*m.b16*m.b19*m.b20 + 192*m.b15*m.b16*m.b20*m.b21 + 128*m.b15*m.b16*m.b21*m.b22 + 64*m.b15*
                       m.b16*m.b22*m.b23 + 256*m.b15*m.b17*m.b18*m.b20 + 192*m.b15*m.b17*m.b19*m.b21 + 128*m.b15*m.b17*
                       m.b20*m.b22 + 64*m.b15*m.b17*m.b21*m.b23 + 128*m.b15*m.b18*m.b19*m.b22 + 64*m.b15*m.b18*m.b20*
                       m.b23 + 384*m.b16*m.b17*m.b18*m.b19 + 320*m.b16*m.b17*m.b19*m.b20 + 256*m.b16*m.b17*m.b20*m.b21
                        + 192*m.b16*m.b17*m.b21*m.b22 + 128*m.b16*m.b17*m.b22*m.b23 + 64*m.b16*m.b17*m.b23*m.b24 + 256*
                       m.b16*m.b18*m.b19*m.b21 + 192*m.b16*m.b18*m.b20*m.b22 + 128*m.b16*m.b18*m.b21*m.b23 + 64*m.b16*
                       m.b18*m.b22*m.b24 + 128*m.b16*m.b19*m.b20*m.b23 + 64*m.b16*m.b19*m.b21*m.b24 + 384*m.b17*m.b18*
                       m.b19*m.b20 + 320*m.b17*m.b18*m.b20*m.b21 + 256*m.b17*m.b18*m.b21*m.b22 + 192*m.b17*m.b18*m.b22*
                       m.b23 + 128*m.b17*m.b18*m.b23*m.b24 + 64*m.b17*m.b18*m.b24*m.b25 + 256*m.b17*m.b19*m.b20*m.b22 + 
                       192*m.b17*m.b19*m.b21*m.b23 + 128*m.b17*m.b19*m.b22*m.b24 + 64*m.b17*m.b19*m.b23*m.b25 + 128*
                       m.b17*m.b20*m.b21*m.b24 + 64*m.b17*m.b20*m.b22*m.b25 + 384*m.b18*m.b19*m.b20*m.b21 + 320*m.b18*
                       m.b19*m.b21*m.b22 + 256*m.b18*m.b19*m.b22*m.b23 + 192*m.b18*m.b19*m.b23*m.b24 + 128*m.b18*m.b19*
                       m.b24*m.b25 + 64*m.b18*m.b19*m.b25*m.b26 + 256*m.b18*m.b20*m.b21*m.b23 + 192*m.b18*m.b20*m.b22*
                       m.b24 + 128*m.b18*m.b20*m.b23*m.b25 + 64*m.b18*m.b20*m.b24*m.b26 + 128*m.b18*m.b21*m.b22*m.b25 + 
                       64*m.b18*m.b21*m.b23*m.b26 + 384*m.b19*m.b20*m.b21*m.b22 + 320*m.b19*m.b20*m.b22*m.b23 + 256*
                       m.b19*m.b20*m.b23*m.b24 + 192*m.b19*m.b20*m.b24*m.b25 + 128*m.b19*m.b20*m.b25*m.b26 + 64*m.b19*
                       m.b20*m.b26*m.b27 + 256*m.b19*m.b21*m.b22*m.b24 + 192*m.b19*m.b21*m.b23*m.b25 + 128*m.b19*m.b21*
                       m.b24*m.b26 + 64*m.b19*m.b21*m.b25*m.b27 + 128*m.b19*m.b22*m.b23*m.b26 + 64*m.b19*m.b22*m.b24*
                       m.b27 + 384*m.b20*m.b21*m.b22*m.b23 + 320*m.b20*m.b21*m.b23*m.b24 + 256*m.b20*m.b21*m.b24*m.b25
                        + 192*m.b20*m.b21*m.b25*m.b26 + 128*m.b20*m.b21*m.b26*m.b27 + 64*m.b20*m.b21*m.b27*m.b28 + 256*
                       m.b20*m.b22*m.b23*m.b25 + 192*m.b20*m.b22*m.b24*m.b26 + 128*m.b20*m.b22*m.b25*m.b27 + 64*m.b20*
                       m.b22*m.b26*m.b28 + 128*m.b20*m.b23*m.b24*m.b27 + 64*m.b20*m.b23*m.b25*m.b28 + 384*m.b21*m.b22*
                       m.b23*m.b24 + 320*m.b21*m.b22*m.b24*m.b25 + 256*m.b21*m.b22*m.b25*m.b26 + 192*m.b21*m.b22*m.b26*
                       m.b27 + 128*m.b21*m.b22*m.b27*m.b28 + 64*m.b21*m.b22*m.b28*m.b29 + 256*m.b21*m.b23*m.b24*m.b26 + 
                       192*m.b21*m.b23*m.b25*m.b27 + 128*m.b21*m.b23*m.b26*m.b28 + 64*m.b21*m.b23*m.b27*m.b29 + 128*
                       m.b21*m.b24*m.b25*m.b28 + 64*m.b21*m.b24*m.b26*m.b29 + 384*m.b22*m.b23*m.b24*m.b25 + 320*m.b22*
                       m.b23*m.b25*m.b26 + 256*m.b22*m.b23*m.b26*m.b27 + 192*m.b22*m.b23*m.b27*m.b28 + 128*m.b22*m.b23*
                       m.b28*m.b29 + 64*m.b22*m.b23*m.b29*m.b30 + 256*m.b22*m.b24*m.b25*m.b27 + 192*m.b22*m.b24*m.b26*
                       m.b28 + 128*m.b22*m.b24*m.b27*m.b29 + 64*m.b22*m.b24*m.b28*m.b30 + 128*m.b22*m.b25*m.b26*m.b29 + 
                       64*m.b22*m.b25*m.b27*m.b30 + 384*m.b23*m.b24*m.b25*m.b26 + 320*m.b23*m.b24*m.b26*m.b27 + 256*
                       m.b23*m.b24*m.b27*m.b28 + 192*m.b23*m.b24*m.b28*m.b29 + 128*m.b23*m.b24*m.b29*m.b30 + 64*m.b23*
                       m.b24*m.b30*m.b31 + 256*m.b23*m.b25*m.b26*m.b28 + 192*m.b23*m.b25*m.b27*m.b29 + 128*m.b23*m.b25*
                       m.b28*m.b30 + 64*m.b23*m.b25*m.b29*m.b31 + 128*m.b23*m.b26*m.b27*m.b30 + 64*m.b23*m.b26*m.b28*
                       m.b31 + 384*m.b24*m.b25*m.b26*m.b27 + 320*m.b24*m.b25*m.b27*m.b28 + 256*m.b24*m.b25*m.b28*m.b29
                        + 192*m.b24*m.b25*m.b29*m.b30 + 128*m.b24*m.b25*m.b30*m.b31 + 64*m.b24*m.b25*m.b31*m.b32 + 256*
                       m.b24*m.b26*m.b27*m.b29 + 192*m.b24*m.b26*m.b28*m.b30 + 128*m.b24*m.b26*m.b29*m.b31 + 64*m.b24*
                       m.b26*m.b30*m.b32 + 128*m.b24*m.b27*m.b28*m.b31 + 64*m.b24*m.b27*m.b29*m.b32 + 384*m.b25*m.b26*
                       m.b27*m.b28 + 320*m.b25*m.b26*m.b28*m.b29 + 256*m.b25*m.b26*m.b29*m.b30 + 192*m.b25*m.b26*m.b30*
                       m.b31 + 128*m.b25*m.b26*m.b31*m.b32 + 64*m.b25*m.b26*m.b32*m.b33 + 256*m.b25*m.b27*m.b28*m.b30 + 
                       192*m.b25*m.b27*m.b29*m.b31 + 128*m.b25*m.b27*m.b30*m.b32 + 64*m.b25*m.b27*m.b31*m.b33 + 128*
                       m.b25*m.b28*m.b29*m.b32 + 64*m.b25*m.b28*m.b30*m.b33 + 384*m.b26*m.b27*m.b28*m.b29 + 320*m.b26*
                       m.b27*m.b29*m.b30 + 256*m.b26*m.b27*m.b30*m.b31 + 192*m.b26*m.b27*m.b31*m.b32 + 128*m.b26*m.b27*
                       m.b32*m.b33 + 64*m.b26*m.b27*m.b33*m.b34 + 256*m.b26*m.b28*m.b29*m.b31 + 192*m.b26*m.b28*m.b30*
                       m.b32 + 128*m.b26*m.b28*m.b31*m.b33 + 64*m.b26*m.b28*m.b32*m.b34 + 128*m.b26*m.b29*m.b30*m.b33 + 
                       64*m.b26*m.b29*m.b31*m.b34 + 384*m.b27*m.b28*m.b29*m.b30 + 320*m.b27*m.b28*m.b30*m.b31 + 256*
                       m.b27*m.b28*m.b31*m.b32 + 192*m.b27*m.b28*m.b32*m.b33 + 128*m.b27*m.b28*m.b33*m.b34 + 64*m.b27*
                       m.b28*m.b34*m.b35 + 256*m.b27*m.b29*m.b30*m.b32 + 192*m.b27*m.b29*m.b31*m.b33 + 128*m.b27*m.b29*
                       m.b32*m.b34 + 64*m.b27*m.b29*m.b33*m.b35 + 128*m.b27*m.b30*m.b31*m.b34 + 64*m.b27*m.b30*m.b32*
                       m.b35 + 320*m.b28*m.b29*m.b30*m.b31 + 256*m.b28*m.b29*m.b31*m.b32 + 192*m.b28*m.b29*m.b32*m.b33
                        + 128*m.b28*m.b29*m.b33*m.b34 + 64*m.b28*m.b29*m.b34*m.b35 + 192*m.b28*m.b30*m.b31*m.b33 + 128*
                       m.b28*m.b30*m.b32*m.b34 + 64*m.b28*m.b30*m.b33*m.b35 + 64*m.b28*m.b31*m.b32*m.b35 + 256*m.b29*
                       m.b30*m.b31*m.b32 + 192*m.b29*m.b30*m.b32*m.b33 + 128*m.b29*m.b30*m.b33*m.b34 + 64*m.b29*m.b30*
                       m.b34*m.b35 + 128*m.b29*m.b31*m.b32*m.b34 + 64*m.b29*m.b31*m.b33*m.b35 + 192*m.b30*m.b31*m.b32*
                       m.b33 + 128*m.b30*m.b31*m.b33*m.b34 + 64*m.b30*m.b31*m.b34*m.b35 + 64*m.b30*m.b32*m.b33*m.b35 + 
                       128*m.b31*m.b32*m.b33*m.b34 + 64*m.b31*m.b32*m.b34*m.b35 + 64*m.b32*m.b33*m.b34*m.b35 - 32*m.b1*
                       m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*
                       m.b1*m.b2*m.b8 - 32*m.b1*m.b2*m.b9 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 
                       64*m.b1*m.b3*m.b7 - 32*m.b1*m.b3*m.b8 - 32*m.b1*m.b3*m.b9 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6
                        - 32*m.b1*m.b4*m.b8 - 32*m.b1*m.b4*m.b9 - 32*m.b1*m.b5*m.b6 - 32*m.b1*m.b5*m.b7 - 32*m.b1*m.b5*
                       m.b8 - 32*m.b1*m.b6*m.b7 - 32*m.b1*m.b6*m.b8 - 32*m.b1*m.b6*m.b9 - 32*m.b1*m.b7*m.b8 - 32*m.b1*
                       m.b7*m.b9 - 32*m.b1*m.b8*m.b9 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128
                       *m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 96*m.b2*m.b3*m.b9 - 32*m.b2*m.b3*m.b10 - 160*m.b2*m.b4*
                       m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 96*m.b2*m.b4*m.b8 - 64*m.b2*m.b4*m.b9 - 32*m.b2*
                       m.b4*m.b10 - 160*m.b2*m.b5*m.b6 - 96*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*m.b9 - 32*m.b2*m.b5*m.b10 - 96
                       *m.b2*m.b6*m.b7 - 64*m.b2*m.b6*m.b8 - 64*m.b2*m.b6*m.b9 - 96*m.b2*m.b7*m.b8 - 64*m.b2*m.b7*m.b9
                        - 32*m.b2*m.b7*m.b10 - 96*m.b2*m.b8*m.b9 - 32*m.b2*m.b8*m.b10 - 32*m.b2*m.b9*m.b10 - 160*m.b3*
                       m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 160*m.b3*m.b4*m.b9 - 
                       96*m.b3*m.b4*m.b10 - 32*m.b3*m.b4*m.b11 - 256*m.b3*m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 160*m.b3*m.b5
                       *m.b8 - 128*m.b3*m.b5*m.b9 - 64*m.b3*m.b5*m.b10 - 32*m.b3*m.b5*m.b11 - 224*m.b3*m.b6*m.b7 - 160*
                       m.b3*m.b6*m.b8 - 64*m.b3*m.b6*m.b10 - 32*m.b3*m.b6*m.b11 - 160*m.b3*m.b7*m.b8 - 128*m.b3*m.b7*
                       m.b9 - 64*m.b3*m.b7*m.b10 - 160*m.b3*m.b8*m.b9 - 64*m.b3*m.b8*m.b10 - 32*m.b3*m.b8*m.b11 - 96*
                       m.b3*m.b9*m.b10 - 32*m.b3*m.b9*m.b11 - 32*m.b3*m.b10*m.b11 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*
                       m.b7 - 288*m.b4*m.b5*m.b8 - 224*m.b4*m.b5*m.b9 - 160*m.b4*m.b5*m.b10 - 96*m.b4*m.b5*m.b11 - 32*
                       m.b4*m.b5*m.b12 - 352*m.b4*m.b6*m.b7 - 160*m.b4*m.b6*m.b8 - 224*m.b4*m.b6*m.b9 - 128*m.b4*m.b6*
                       m.b10 - 64*m.b4*m.b6*m.b11 - 32*m.b4*m.b6*m.b12 - 288*m.b4*m.b7*m.b8 - 224*m.b4*m.b7*m.b9 - 64*
                       m.b4*m.b7*m.b11 - 32*m.b4*m.b7*m.b12 - 224*m.b4*m.b8*m.b9 - 128*m.b4*m.b8*m.b10 - 64*m.b4*m.b8*
                       m.b11 - 160*m.b4*m.b9*m.b10 - 64*m.b4*m.b9*m.b11 - 32*m.b4*m.b9*m.b12 - 96*m.b4*m.b10*m.b11 - 32*
                       m.b4*m.b10*m.b12 - 32*m.b4*m.b11*m.b12 - 288*m.b5*m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 352*m.b5*m.b6*
                       m.b9 - 224*m.b5*m.b6*m.b10 - 160*m.b5*m.b6*m.b11 - 96*m.b5*m.b6*m.b12 - 32*m.b5*m.b6*m.b13 - 416*
                       m.b5*m.b7*m.b8 - 192*m.b5*m.b7*m.b9 - 224*m.b5*m.b7*m.b10 - 128*m.b5*m.b7*m.b11 - 64*m.b5*m.b7*
                       m.b12 - 32*m.b5*m.b7*m.b13 - 352*m.b5*m.b8*m.b9 - 224*m.b5*m.b8*m.b10 - 64*m.b5*m.b8*m.b12 - 32*
                       m.b5*m.b8*m.b13 - 224*m.b5*m.b9*m.b10 - 128*m.b5*m.b9*m.b11 - 64*m.b5*m.b9*m.b12 - 160*m.b5*m.b10
                       *m.b11 - 64*m.b5*m.b10*m.b12 - 32*m.b5*m.b10*m.b13 - 96*m.b5*m.b11*m.b12 - 32*m.b5*m.b11*m.b13 - 
                       32*m.b5*m.b12*m.b13 - 352*m.b6*m.b7*m.b8 - 480*m.b6*m.b7*m.b9 - 352*m.b6*m.b7*m.b10 - 224*m.b6*
                       m.b7*m.b11 - 160*m.b6*m.b7*m.b12 - 96*m.b6*m.b7*m.b13 - 32*m.b6*m.b7*m.b14 - 480*m.b6*m.b8*m.b9
                        - 192*m.b6*m.b8*m.b10 - 224*m.b6*m.b8*m.b11 - 128*m.b6*m.b8*m.b12 - 64*m.b6*m.b8*m.b13 - 32*m.b6
                       *m.b8*m.b14 - 352*m.b6*m.b9*m.b10 - 224*m.b6*m.b9*m.b11 - 64*m.b6*m.b9*m.b13 - 32*m.b6*m.b9*m.b14
                        - 224*m.b6*m.b10*m.b11 - 128*m.b6*m.b10*m.b12 - 64*m.b6*m.b10*m.b13 - 160*m.b6*m.b11*m.b12 - 64*
                       m.b6*m.b11*m.b13 - 32*m.b6*m.b11*m.b14 - 96*m.b6*m.b12*m.b13 - 32*m.b6*m.b12*m.b14 - 32*m.b6*
                       m.b13*m.b14 - 384*m.b7*m.b8*m.b9 - 480*m.b7*m.b8*m.b10 - 352*m.b7*m.b8*m.b11 - 224*m.b7*m.b8*
                       m.b12 - 160*m.b7*m.b8*m.b13 - 96*m.b7*m.b8*m.b14 - 32*m.b7*m.b8*m.b15 - 480*m.b7*m.b9*m.b10 - 192
                       *m.b7*m.b9*m.b11 - 224*m.b7*m.b9*m.b12 - 128*m.b7*m.b9*m.b13 - 64*m.b7*m.b9*m.b14 - 32*m.b7*m.b9*
                       m.b15 - 352*m.b7*m.b10*m.b11 - 224*m.b7*m.b10*m.b12 - 64*m.b7*m.b10*m.b14 - 32*m.b7*m.b10*m.b15
                        - 224*m.b7*m.b11*m.b12 - 128*m.b7*m.b11*m.b13 - 64*m.b7*m.b11*m.b14 - 160*m.b7*m.b12*m.b13 - 64*
                       m.b7*m.b12*m.b14 - 32*m.b7*m.b12*m.b15 - 96*m.b7*m.b13*m.b14 - 32*m.b7*m.b13*m.b15 - 32*m.b7*
                       m.b14*m.b15 - 384*m.b8*m.b9*m.b10 - 480*m.b8*m.b9*m.b11 - 352*m.b8*m.b9*m.b12 - 224*m.b8*m.b9*
                       m.b13 - 160*m.b8*m.b9*m.b14 - 96*m.b8*m.b9*m.b15 - 32*m.b8*m.b9*m.b16 - 480*m.b8*m.b10*m.b11 - 
                       192*m.b8*m.b10*m.b12 - 224*m.b8*m.b10*m.b13 - 128*m.b8*m.b10*m.b14 - 64*m.b8*m.b10*m.b15 - 32*
                       m.b8*m.b10*m.b16 - 352*m.b8*m.b11*m.b12 - 224*m.b8*m.b11*m.b13 - 64*m.b8*m.b11*m.b15 - 32*m.b8*
                       m.b11*m.b16 - 224*m.b8*m.b12*m.b13 - 128*m.b8*m.b12*m.b14 - 64*m.b8*m.b12*m.b15 - 160*m.b8*m.b13*
                       m.b14 - 64*m.b8*m.b13*m.b15 - 32*m.b8*m.b13*m.b16 - 96*m.b8*m.b14*m.b15 - 32*m.b8*m.b14*m.b16 - 
                       32*m.b8*m.b15*m.b16 - 384*m.b9*m.b10*m.b11 - 480*m.b9*m.b10*m.b12 - 352*m.b9*m.b10*m.b13 - 224*
                       m.b9*m.b10*m.b14 - 160*m.b9*m.b10*m.b15 - 96*m.b9*m.b10*m.b16 - 32*m.b9*m.b10*m.b17 - 480*m.b9*
                       m.b11*m.b12 - 192*m.b9*m.b11*m.b13 - 224*m.b9*m.b11*m.b14 - 128*m.b9*m.b11*m.b15 - 64*m.b9*m.b11*
                       m.b16 - 32*m.b9*m.b11*m.b17 - 352*m.b9*m.b12*m.b13 - 224*m.b9*m.b12*m.b14 - 64*m.b9*m.b12*m.b16
                        - 32*m.b9*m.b12*m.b17 - 224*m.b9*m.b13*m.b14 - 128*m.b9*m.b13*m.b15 - 64*m.b9*m.b13*m.b16 - 160*
                       m.b9*m.b14*m.b15 - 64*m.b9*m.b14*m.b16 - 32*m.b9*m.b14*m.b17 - 96*m.b9*m.b15*m.b16 - 32*m.b9*
                       m.b15*m.b17 - 32*m.b9*m.b16*m.b17 - 384*m.b10*m.b11*m.b12 - 480*m.b10*m.b11*m.b13 - 352*m.b10*
                       m.b11*m.b14 - 224*m.b10*m.b11*m.b15 - 160*m.b10*m.b11*m.b16 - 96*m.b10*m.b11*m.b17 - 32*m.b10*
                       m.b11*m.b18 - 480*m.b10*m.b12*m.b13 - 192*m.b10*m.b12*m.b14 - 224*m.b10*m.b12*m.b15 - 128*m.b10*
                       m.b12*m.b16 - 64*m.b10*m.b12*m.b17 - 32*m.b10*m.b12*m.b18 - 352*m.b10*m.b13*m.b14 - 224*m.b10*
                       m.b13*m.b15 - 64*m.b10*m.b13*m.b17 - 32*m.b10*m.b13*m.b18 - 224*m.b10*m.b14*m.b15 - 128*m.b10*
                       m.b14*m.b16 - 64*m.b10*m.b14*m.b17 - 160*m.b10*m.b15*m.b16 - 64*m.b10*m.b15*m.b17 - 32*m.b10*
                       m.b15*m.b18 - 96*m.b10*m.b16*m.b17 - 32*m.b10*m.b16*m.b18 - 32*m.b10*m.b17*m.b18 - 384*m.b11*
                       m.b12*m.b13 - 480*m.b11*m.b12*m.b14 - 352*m.b11*m.b12*m.b15 - 224*m.b11*m.b12*m.b16 - 160*m.b11*
                       m.b12*m.b17 - 96*m.b11*m.b12*m.b18 - 32*m.b11*m.b12*m.b19 - 480*m.b11*m.b13*m.b14 - 192*m.b11*
                       m.b13*m.b15 - 224*m.b11*m.b13*m.b16 - 128*m.b11*m.b13*m.b17 - 64*m.b11*m.b13*m.b18 - 32*m.b11*
                       m.b13*m.b19 - 352*m.b11*m.b14*m.b15 - 224*m.b11*m.b14*m.b16 - 64*m.b11*m.b14*m.b18 - 32*m.b11*
                       m.b14*m.b19 - 224*m.b11*m.b15*m.b16 - 128*m.b11*m.b15*m.b17 - 64*m.b11*m.b15*m.b18 - 160*m.b11*
                       m.b16*m.b17 - 64*m.b11*m.b16*m.b18 - 32*m.b11*m.b16*m.b19 - 96*m.b11*m.b17*m.b18 - 32*m.b11*m.b17
                       *m.b19 - 32*m.b11*m.b18*m.b19 - 384*m.b12*m.b13*m.b14 - 480*m.b12*m.b13*m.b15 - 352*m.b12*m.b13*
                       m.b16 - 224*m.b12*m.b13*m.b17 - 160*m.b12*m.b13*m.b18 - 96*m.b12*m.b13*m.b19 - 32*m.b12*m.b13*
                       m.b20 - 480*m.b12*m.b14*m.b15 - 192*m.b12*m.b14*m.b16 - 224*m.b12*m.b14*m.b17 - 128*m.b12*m.b14*
                       m.b18 - 64*m.b12*m.b14*m.b19 - 32*m.b12*m.b14*m.b20 - 352*m.b12*m.b15*m.b16 - 224*m.b12*m.b15*
                       m.b17 - 64*m.b12*m.b15*m.b19 - 32*m.b12*m.b15*m.b20 - 224*m.b12*m.b16*m.b17 - 128*m.b12*m.b16*
                       m.b18 - 64*m.b12*m.b16*m.b19 - 160*m.b12*m.b17*m.b18 - 64*m.b12*m.b17*m.b19 - 32*m.b12*m.b17*
                       m.b20 - 96*m.b12*m.b18*m.b19 - 32*m.b12*m.b18*m.b20 - 32*m.b12*m.b19*m.b20 - 384*m.b13*m.b14*
                       m.b15 - 480*m.b13*m.b14*m.b16 - 352*m.b13*m.b14*m.b17 - 224*m.b13*m.b14*m.b18 - 160*m.b13*m.b14*
                       m.b19 - 96*m.b13*m.b14*m.b20 - 32*m.b13*m.b14*m.b21 - 480*m.b13*m.b15*m.b16 - 192*m.b13*m.b15*
                       m.b17 - 224*m.b13*m.b15*m.b18 - 128*m.b13*m.b15*m.b19 - 64*m.b13*m.b15*m.b20 - 32*m.b13*m.b15*
                       m.b21 - 352*m.b13*m.b16*m.b17 - 224*m.b13*m.b16*m.b18 - 64*m.b13*m.b16*m.b20 - 32*m.b13*m.b16*
                       m.b21 - 224*m.b13*m.b17*m.b18 - 128*m.b13*m.b17*m.b19 - 64*m.b13*m.b17*m.b20 - 160*m.b13*m.b18*
                       m.b19 - 64*m.b13*m.b18*m.b20 - 32*m.b13*m.b18*m.b21 - 96*m.b13*m.b19*m.b20 - 32*m.b13*m.b19*m.b21
                        - 32*m.b13*m.b20*m.b21 - 384*m.b14*m.b15*m.b16 - 480*m.b14*m.b15*m.b17 - 352*m.b14*m.b15*m.b18
                        - 224*m.b14*m.b15*m.b19 - 160*m.b14*m.b15*m.b20 - 96*m.b14*m.b15*m.b21 - 32*m.b14*m.b15*m.b22 - 
                       480*m.b14*m.b16*m.b17 - 192*m.b14*m.b16*m.b18 - 224*m.b14*m.b16*m.b19 - 128*m.b14*m.b16*m.b20 - 
                       64*m.b14*m.b16*m.b21 - 32*m.b14*m.b16*m.b22 - 352*m.b14*m.b17*m.b18 - 224*m.b14*m.b17*m.b19 - 64*
                       m.b14*m.b17*m.b21 - 32*m.b14*m.b17*m.b22 - 224*m.b14*m.b18*m.b19 - 128*m.b14*m.b18*m.b20 - 64*
                       m.b14*m.b18*m.b21 - 160*m.b14*m.b19*m.b20 - 64*m.b14*m.b19*m.b21 - 32*m.b14*m.b19*m.b22 - 96*
                       m.b14*m.b20*m.b21 - 32*m.b14*m.b20*m.b22 - 32*m.b14*m.b21*m.b22 - 384*m.b15*m.b16*m.b17 - 480*
                       m.b15*m.b16*m.b18 - 352*m.b15*m.b16*m.b19 - 224*m.b15*m.b16*m.b20 - 160*m.b15*m.b16*m.b21 - 96*
                       m.b15*m.b16*m.b22 - 32*m.b15*m.b16*m.b23 - 480*m.b15*m.b17*m.b18 - 192*m.b15*m.b17*m.b19 - 224*
                       m.b15*m.b17*m.b20 - 128*m.b15*m.b17*m.b21 - 64*m.b15*m.b17*m.b22 - 32*m.b15*m.b17*m.b23 - 352*
                       m.b15*m.b18*m.b19 - 224*m.b15*m.b18*m.b20 - 64*m.b15*m.b18*m.b22 - 32*m.b15*m.b18*m.b23 - 224*
                       m.b15*m.b19*m.b20 - 128*m.b15*m.b19*m.b21 - 64*m.b15*m.b19*m.b22 - 160*m.b15*m.b20*m.b21 - 64*
                       m.b15*m.b20*m.b22 - 32*m.b15*m.b20*m.b23 - 96*m.b15*m.b21*m.b22 - 32*m.b15*m.b21*m.b23 - 32*m.b15
                       *m.b22*m.b23 - 384*m.b16*m.b17*m.b18 - 480*m.b16*m.b17*m.b19 - 352*m.b16*m.b17*m.b20 - 224*m.b16*
                       m.b17*m.b21 - 160*m.b16*m.b17*m.b22 - 96*m.b16*m.b17*m.b23 - 32*m.b16*m.b17*m.b24 - 480*m.b16*
                       m.b18*m.b19 - 192*m.b16*m.b18*m.b20 - 224*m.b16*m.b18*m.b21 - 128*m.b16*m.b18*m.b22 - 64*m.b16*
                       m.b18*m.b23 - 32*m.b16*m.b18*m.b24 - 352*m.b16*m.b19*m.b20 - 224*m.b16*m.b19*m.b21 - 64*m.b16*
                       m.b19*m.b23 - 32*m.b16*m.b19*m.b24 - 224*m.b16*m.b20*m.b21 - 128*m.b16*m.b20*m.b22 - 64*m.b16*
                       m.b20*m.b23 - 160*m.b16*m.b21*m.b22 - 64*m.b16*m.b21*m.b23 - 32*m.b16*m.b21*m.b24 - 96*m.b16*
                       m.b22*m.b23 - 32*m.b16*m.b22*m.b24 - 32*m.b16*m.b23*m.b24 - 384*m.b17*m.b18*m.b19 - 480*m.b17*
                       m.b18*m.b20 - 352*m.b17*m.b18*m.b21 - 224*m.b17*m.b18*m.b22 - 160*m.b17*m.b18*m.b23 - 96*m.b17*
                       m.b18*m.b24 - 32*m.b17*m.b18*m.b25 - 480*m.b17*m.b19*m.b20 - 192*m.b17*m.b19*m.b21 - 224*m.b17*
                       m.b19*m.b22 - 128*m.b17*m.b19*m.b23 - 64*m.b17*m.b19*m.b24 - 32*m.b17*m.b19*m.b25 - 352*m.b17*
                       m.b20*m.b21 - 224*m.b17*m.b20*m.b22 - 64*m.b17*m.b20*m.b24 - 32*m.b17*m.b20*m.b25 - 224*m.b17*
                       m.b21*m.b22 - 128*m.b17*m.b21*m.b23 - 64*m.b17*m.b21*m.b24 - 160*m.b17*m.b22*m.b23 - 64*m.b17*
                       m.b22*m.b24 - 32*m.b17*m.b22*m.b25 - 96*m.b17*m.b23*m.b24 - 32*m.b17*m.b23*m.b25 - 32*m.b17*m.b24
                       *m.b25 - 384*m.b18*m.b19*m.b20 - 480*m.b18*m.b19*m.b21 - 352*m.b18*m.b19*m.b22 - 224*m.b18*m.b19*
                       m.b23 - 160*m.b18*m.b19*m.b24 - 96*m.b18*m.b19*m.b25 - 32*m.b18*m.b19*m.b26 - 480*m.b18*m.b20*
                       m.b21 - 192*m.b18*m.b20*m.b22 - 224*m.b18*m.b20*m.b23 - 128*m.b18*m.b20*m.b24 - 64*m.b18*m.b20*
                       m.b25 - 32*m.b18*m.b20*m.b26 - 352*m.b18*m.b21*m.b22 - 224*m.b18*m.b21*m.b23 - 64*m.b18*m.b21*
                       m.b25 - 32*m.b18*m.b21*m.b26 - 224*m.b18*m.b22*m.b23 - 128*m.b18*m.b22*m.b24 - 64*m.b18*m.b22*
                       m.b25 - 160*m.b18*m.b23*m.b24 - 64*m.b18*m.b23*m.b25 - 32*m.b18*m.b23*m.b26 - 96*m.b18*m.b24*
                       m.b25 - 32*m.b18*m.b24*m.b26 - 32*m.b18*m.b25*m.b26 - 384*m.b19*m.b20*m.b21 - 480*m.b19*m.b20*
                       m.b22 - 352*m.b19*m.b20*m.b23 - 224*m.b19*m.b20*m.b24 - 160*m.b19*m.b20*m.b25 - 96*m.b19*m.b20*
                       m.b26 - 32*m.b19*m.b20*m.b27 - 480*m.b19*m.b21*m.b22 - 192*m.b19*m.b21*m.b23 - 224*m.b19*m.b21*
                       m.b24 - 128*m.b19*m.b21*m.b25 - 64*m.b19*m.b21*m.b26 - 32*m.b19*m.b21*m.b27 - 352*m.b19*m.b22*
                       m.b23 - 224*m.b19*m.b22*m.b24 - 64*m.b19*m.b22*m.b26 - 32*m.b19*m.b22*m.b27 - 224*m.b19*m.b23*
                       m.b24 - 128*m.b19*m.b23*m.b25 - 64*m.b19*m.b23*m.b26 - 160*m.b19*m.b24*m.b25 - 64*m.b19*m.b24*
                       m.b26 - 32*m.b19*m.b24*m.b27 - 96*m.b19*m.b25*m.b26 - 32*m.b19*m.b25*m.b27 - 32*m.b19*m.b26*m.b27
                        - 384*m.b20*m.b21*m.b22 - 480*m.b20*m.b21*m.b23 - 352*m.b20*m.b21*m.b24 - 224*m.b20*m.b21*m.b25
                        - 160*m.b20*m.b21*m.b26 - 96*m.b20*m.b21*m.b27 - 32*m.b20*m.b21*m.b28 - 480*m.b20*m.b22*m.b23 - 
                       192*m.b20*m.b22*m.b24 - 224*m.b20*m.b22*m.b25 - 128*m.b20*m.b22*m.b26 - 64*m.b20*m.b22*m.b27 - 32
                       *m.b20*m.b22*m.b28 - 352*m.b20*m.b23*m.b24 - 224*m.b20*m.b23*m.b25 - 64*m.b20*m.b23*m.b27 - 32*
                       m.b20*m.b23*m.b28 - 224*m.b20*m.b24*m.b25 - 128*m.b20*m.b24*m.b26 - 64*m.b20*m.b24*m.b27 - 160*
                       m.b20*m.b25*m.b26 - 64*m.b20*m.b25*m.b27 - 32*m.b20*m.b25*m.b28 - 96*m.b20*m.b26*m.b27 - 32*m.b20
                       *m.b26*m.b28 - 32*m.b20*m.b27*m.b28 - 384*m.b21*m.b22*m.b23 - 480*m.b21*m.b22*m.b24 - 352*m.b21*
                       m.b22*m.b25 - 224*m.b21*m.b22*m.b26 - 160*m.b21*m.b22*m.b27 - 96*m.b21*m.b22*m.b28 - 32*m.b21*
                       m.b22*m.b29 - 480*m.b21*m.b23*m.b24 - 192*m.b21*m.b23*m.b25 - 224*m.b21*m.b23*m.b26 - 128*m.b21*
                       m.b23*m.b27 - 64*m.b21*m.b23*m.b28 - 32*m.b21*m.b23*m.b29 - 352*m.b21*m.b24*m.b25 - 224*m.b21*
                       m.b24*m.b26 - 64*m.b21*m.b24*m.b28 - 32*m.b21*m.b24*m.b29 - 224*m.b21*m.b25*m.b26 - 128*m.b21*
                       m.b25*m.b27 - 64*m.b21*m.b25*m.b28 - 160*m.b21*m.b26*m.b27 - 64*m.b21*m.b26*m.b28 - 32*m.b21*
                       m.b26*m.b29 - 96*m.b21*m.b27*m.b28 - 32*m.b21*m.b27*m.b29 - 32*m.b21*m.b28*m.b29 - 384*m.b22*
                       m.b23*m.b24 - 480*m.b22*m.b23*m.b25 - 352*m.b22*m.b23*m.b26 - 224*m.b22*m.b23*m.b27 - 160*m.b22*
                       m.b23*m.b28 - 96*m.b22*m.b23*m.b29 - 32*m.b22*m.b23*m.b30 - 480*m.b22*m.b24*m.b25 - 192*m.b22*
                       m.b24*m.b26 - 224*m.b22*m.b24*m.b27 - 128*m.b22*m.b24*m.b28 - 64*m.b22*m.b24*m.b29 - 32*m.b22*
                       m.b24*m.b30 - 352*m.b22*m.b25*m.b26 - 224*m.b22*m.b25*m.b27 - 64*m.b22*m.b25*m.b29 - 32*m.b22*
                       m.b25*m.b30 - 224*m.b22*m.b26*m.b27 - 128*m.b22*m.b26*m.b28 - 64*m.b22*m.b26*m.b29 - 160*m.b22*
                       m.b27*m.b28 - 64*m.b22*m.b27*m.b29 - 32*m.b22*m.b27*m.b30 - 96*m.b22*m.b28*m.b29 - 32*m.b22*m.b28
                       *m.b30 - 32*m.b22*m.b29*m.b30 - 384*m.b23*m.b24*m.b25 - 480*m.b23*m.b24*m.b26 - 352*m.b23*m.b24*
                       m.b27 - 224*m.b23*m.b24*m.b28 - 160*m.b23*m.b24*m.b29 - 96*m.b23*m.b24*m.b30 - 32*m.b23*m.b24*
                       m.b31 - 480*m.b23*m.b25*m.b26 - 192*m.b23*m.b25*m.b27 - 224*m.b23*m.b25*m.b28 - 128*m.b23*m.b25*
                       m.b29 - 64*m.b23*m.b25*m.b30 - 32*m.b23*m.b25*m.b31 - 352*m.b23*m.b26*m.b27 - 224*m.b23*m.b26*
                       m.b28 - 64*m.b23*m.b26*m.b30 - 32*m.b23*m.b26*m.b31 - 224*m.b23*m.b27*m.b28 - 128*m.b23*m.b27*
                       m.b29 - 64*m.b23*m.b27*m.b30 - 160*m.b23*m.b28*m.b29 - 64*m.b23*m.b28*m.b30 - 32*m.b23*m.b28*
                       m.b31 - 96*m.b23*m.b29*m.b30 - 32*m.b23*m.b29*m.b31 - 32*m.b23*m.b30*m.b31 - 384*m.b24*m.b25*
                       m.b26 - 480*m.b24*m.b25*m.b27 - 352*m.b24*m.b25*m.b28 - 224*m.b24*m.b25*m.b29 - 160*m.b24*m.b25*
                       m.b30 - 96*m.b24*m.b25*m.b31 - 32*m.b24*m.b25*m.b32 - 480*m.b24*m.b26*m.b27 - 192*m.b24*m.b26*
                       m.b28 - 224*m.b24*m.b26*m.b29 - 128*m.b24*m.b26*m.b30 - 64*m.b24*m.b26*m.b31 - 32*m.b24*m.b26*
                       m.b32 - 352*m.b24*m.b27*m.b28 - 224*m.b24*m.b27*m.b29 - 64*m.b24*m.b27*m.b31 - 32*m.b24*m.b27*
                       m.b32 - 224*m.b24*m.b28*m.b29 - 128*m.b24*m.b28*m.b30 - 64*m.b24*m.b28*m.b31 - 160*m.b24*m.b29*
                       m.b30 - 64*m.b24*m.b29*m.b31 - 32*m.b24*m.b29*m.b32 - 96*m.b24*m.b30*m.b31 - 32*m.b24*m.b30*m.b32
                        - 32*m.b24*m.b31*m.b32 - 384*m.b25*m.b26*m.b27 - 480*m.b25*m.b26*m.b28 - 352*m.b25*m.b26*m.b29
                        - 224*m.b25*m.b26*m.b30 - 160*m.b25*m.b26*m.b31 - 96*m.b25*m.b26*m.b32 - 32*m.b25*m.b26*m.b33 - 
                       480*m.b25*m.b27*m.b28 - 192*m.b25*m.b27*m.b29 - 224*m.b25*m.b27*m.b30 - 128*m.b25*m.b27*m.b31 - 
                       64*m.b25*m.b27*m.b32 - 32*m.b25*m.b27*m.b33 - 352*m.b25*m.b28*m.b29 - 224*m.b25*m.b28*m.b30 - 64*
                       m.b25*m.b28*m.b32 - 32*m.b25*m.b28*m.b33 - 224*m.b25*m.b29*m.b30 - 128*m.b25*m.b29*m.b31 - 64*
                       m.b25*m.b29*m.b32 - 160*m.b25*m.b30*m.b31 - 64*m.b25*m.b30*m.b32 - 32*m.b25*m.b30*m.b33 - 96*
                       m.b25*m.b31*m.b32 - 32*m.b25*m.b31*m.b33 - 32*m.b25*m.b32*m.b33 - 384*m.b26*m.b27*m.b28 - 480*
                       m.b26*m.b27*m.b29 - 352*m.b26*m.b27*m.b30 - 224*m.b26*m.b27*m.b31 - 160*m.b26*m.b27*m.b32 - 96*
                       m.b26*m.b27*m.b33 - 32*m.b26*m.b27*m.b34 - 480*m.b26*m.b28*m.b29 - 192*m.b26*m.b28*m.b30 - 224*
                       m.b26*m.b28*m.b31 - 128*m.b26*m.b28*m.b32 - 64*m.b26*m.b28*m.b33 - 32*m.b26*m.b28*m.b34 - 352*
                       m.b26*m.b29*m.b30 - 224*m.b26*m.b29*m.b31 - 64*m.b26*m.b29*m.b33 - 32*m.b26*m.b29*m.b34 - 224*
                       m.b26*m.b30*m.b31 - 128*m.b26*m.b30*m.b32 - 64*m.b26*m.b30*m.b33 - 160*m.b26*m.b31*m.b32 - 64*
                       m.b26*m.b31*m.b33 - 32*m.b26*m.b31*m.b34 - 96*m.b26*m.b32*m.b33 - 32*m.b26*m.b32*m.b34 - 32*m.b26
                       *m.b33*m.b34 - 384*m.b27*m.b28*m.b29 - 480*m.b27*m.b28*m.b30 - 352*m.b27*m.b28*m.b31 - 224*m.b27*
                       m.b28*m.b32 - 160*m.b27*m.b28*m.b33 - 96*m.b27*m.b28*m.b34 - 32*m.b27*m.b28*m.b35 - 480*m.b27*
                       m.b29*m.b30 - 192*m.b27*m.b29*m.b31 - 224*m.b27*m.b29*m.b32 - 128*m.b27*m.b29*m.b33 - 64*m.b27*
                       m.b29*m.b34 - 32*m.b27*m.b29*m.b35 - 352*m.b27*m.b30*m.b31 - 224*m.b27*m.b30*m.b32 - 64*m.b27*
                       m.b30*m.b34 - 32*m.b27*m.b30*m.b35 - 224*m.b27*m.b31*m.b32 - 128*m.b27*m.b31*m.b33 - 64*m.b27*
                       m.b31*m.b34 - 160*m.b27*m.b32*m.b33 - 64*m.b27*m.b32*m.b34 - 32*m.b27*m.b32*m.b35 - 96*m.b27*
                       m.b33*m.b34 - 32*m.b27*m.b33*m.b35 - 32*m.b27*m.b34*m.b35 - 352*m.b28*m.b29*m.b30 - 416*m.b28*
                       m.b29*m.b31 - 288*m.b28*m.b29*m.b32 - 160*m.b28*m.b29*m.b33 - 96*m.b28*m.b29*m.b34 - 32*m.b28*
                       m.b29*m.b35 - 416*m.b28*m.b30*m.b31 - 160*m.b28*m.b30*m.b32 - 160*m.b28*m.b30*m.b33 - 64*m.b28*
                       m.b30*m.b34 - 32*m.b28*m.b30*m.b35 - 288*m.b28*m.b31*m.b32 - 160*m.b28*m.b31*m.b33 - 32*m.b28*
                       m.b31*m.b35 - 192*m.b28*m.b32*m.b33 - 96*m.b28*m.b32*m.b34 - 32*m.b28*m.b32*m.b35 - 128*m.b28*
                       m.b33*m.b34 - 32*m.b28*m.b33*m.b35 - 64*m.b28*m.b34*m.b35 - 288*m.b29*m.b30*m.b31 - 352*m.b29*
                       m.b30*m.b32 - 224*m.b29*m.b30*m.b33 - 96*m.b29*m.b30*m.b34 - 32*m.b29*m.b30*m.b35 - 320*m.b29*
                       m.b31*m.b32 - 128*m.b29*m.b31*m.b33 - 96*m.b29*m.b31*m.b34 - 32*m.b29*m.b31*m.b35 - 192*m.b29*
                       m.b32*m.b33 - 128*m.b29*m.b32*m.b34 - 128*m.b29*m.b33*m.b34 - 64*m.b29*m.b33*m.b35 - 64*m.b29*
                       m.b34*m.b35 - 224*m.b30*m.b31*m.b32 - 256*m.b30*m.b31*m.b33 - 160*m.b30*m.b31*m.b34 - 32*m.b30*
                       m.b31*m.b35 - 224*m.b30*m.b32*m.b33 - 64*m.b30*m.b32*m.b34 - 64*m.b30*m.b32*m.b35 - 128*m.b30*
                       m.b33*m.b34 - 64*m.b30*m.b33*m.b35 - 64*m.b30*m.b34*m.b35 - 160*m.b31*m.b32*m.b33 - 160*m.b31*
                       m.b32*m.b34 - 64*m.b31*m.b32*m.b35 - 128*m.b31*m.b33*m.b34 - 32*m.b31*m.b33*m.b35 - 64*m.b31*
                       m.b34*m.b35 - 96*m.b32*m.b33*m.b34 - 64*m.b32*m.b33*m.b35 - 64*m.b32*m.b34*m.b35 - 32*m.b33*m.b34
                       *m.b35 + 96*m.b1*m.b2 + 88*m.b1*m.b3 + 80*m.b1*m.b4 + 72*m.b1*m.b5 + 80*m.b1*m.b6 + 72*m.b1*m.b7
                        + 64*m.b1*m.b8 + 56*m.b1*m.b9 + 192*m.b2*m.b3 + 192*m.b2*m.b4 + 176*m.b2*m.b5 + 176*m.b2*m.b6 + 
                       176*m.b2*m.b7 + 160*m.b2*m.b8 + 128*m.b2*m.b9 + 56*m.b2*m.b10 + 304*m.b3*m.b4 + 296*m.b3*m.b5 + 
                       288*m.b3*m.b6 + 296*m.b3*m.b7 + 272*m.b3*m.b8 + 232*m.b3*m.b9 + 128*m.b3*m.b10 + 56*m.b3*m.b11 + 
                       432*m.b4*m.b5 + 416*m.b4*m.b6 + 400*m.b4*m.b7 + 400*m.b4*m.b8 + 352*m.b4*m.b9 + 232*m.b4*m.b10 + 
                       128*m.b4*m.b11 + 56*m.b4*m.b12 + 560*m.b5*m.b6 + 520*m.b5*m.b7 + 496*m.b5*m.b8 + 472*m.b5*m.b9 + 
                       352*m.b5*m.b10 + 232*m.b5*m.b11 + 128*m.b5*m.b12 + 56*m.b5*m.b13 + 672*m.b6*m.b7 + 624*m.b6*m.b8
                        + 576*m.b6*m.b9 + 472*m.b6*m.b10 + 352*m.b6*m.b11 + 232*m.b6*m.b12 + 128*m.b6*m.b13 + 56*m.b6*
                       m.b14 + 768*m.b7*m.b8 + 712*m.b7*m.b9 + 576*m.b7*m.b10 + 472*m.b7*m.b11 + 352*m.b7*m.b12 + 232*
                       m.b7*m.b13 + 128*m.b7*m.b14 + 56*m.b7*m.b15 + 864*m.b8*m.b9 + 712*m.b8*m.b10 + 576*m.b8*m.b11 + 
                       472*m.b8*m.b12 + 352*m.b8*m.b13 + 232*m.b8*m.b14 + 128*m.b8*m.b15 + 56*m.b8*m.b16 + 864*m.b9*
                       m.b10 + 712*m.b9*m.b11 + 576*m.b9*m.b12 + 472*m.b9*m.b13 + 352*m.b9*m.b14 + 232*m.b9*m.b15 + 128*
                       m.b9*m.b16 + 56*m.b9*m.b17 + 864*m.b10*m.b11 + 712*m.b10*m.b12 + 576*m.b10*m.b13 + 472*m.b10*
                       m.b14 + 352*m.b10*m.b15 + 232*m.b10*m.b16 + 128*m.b10*m.b17 + 56*m.b10*m.b18 + 864*m.b11*m.b12 + 
                       712*m.b11*m.b13 + 576*m.b11*m.b14 + 472*m.b11*m.b15 + 352*m.b11*m.b16 + 232*m.b11*m.b17 + 128*
                       m.b11*m.b18 + 56*m.b11*m.b19 + 864*m.b12*m.b13 + 712*m.b12*m.b14 + 576*m.b12*m.b15 + 472*m.b12*
                       m.b16 + 352*m.b12*m.b17 + 232*m.b12*m.b18 + 128*m.b12*m.b19 + 56*m.b12*m.b20 + 864*m.b13*m.b14 + 
                       712*m.b13*m.b15 + 576*m.b13*m.b16 + 472*m.b13*m.b17 + 352*m.b13*m.b18 + 232*m.b13*m.b19 + 128*
                       m.b13*m.b20 + 56*m.b13*m.b21 + 864*m.b14*m.b15 + 712*m.b14*m.b16 + 576*m.b14*m.b17 + 472*m.b14*
                       m.b18 + 352*m.b14*m.b19 + 232*m.b14*m.b20 + 128*m.b14*m.b21 + 56*m.b14*m.b22 + 864*m.b15*m.b16 + 
                       712*m.b15*m.b17 + 576*m.b15*m.b18 + 472*m.b15*m.b19 + 352*m.b15*m.b20 + 232*m.b15*m.b21 + 128*
                       m.b15*m.b22 + 56*m.b15*m.b23 + 864*m.b16*m.b17 + 712*m.b16*m.b18 + 576*m.b16*m.b19 + 472*m.b16*
                       m.b20 + 352*m.b16*m.b21 + 232*m.b16*m.b22 + 128*m.b16*m.b23 + 56*m.b16*m.b24 + 864*m.b17*m.b18 + 
                       712*m.b17*m.b19 + 576*m.b17*m.b20 + 472*m.b17*m.b21 + 352*m.b17*m.b22 + 232*m.b17*m.b23 + 128*
                       m.b17*m.b24 + 56*m.b17*m.b25 + 864*m.b18*m.b19 + 712*m.b18*m.b20 + 576*m.b18*m.b21 + 472*m.b18*
                       m.b22 + 352*m.b18*m.b23 + 232*m.b18*m.b24 + 128*m.b18*m.b25 + 56*m.b18*m.b26 + 864*m.b19*m.b20 + 
                       712*m.b19*m.b21 + 576*m.b19*m.b22 + 472*m.b19*m.b23 + 352*m.b19*m.b24 + 232*m.b19*m.b25 + 128*
                       m.b19*m.b26 + 56*m.b19*m.b27 + 864*m.b20*m.b21 + 712*m.b20*m.b22 + 576*m.b20*m.b23 + 472*m.b20*
                       m.b24 + 352*m.b20*m.b25 + 232*m.b20*m.b26 + 128*m.b20*m.b27 + 56*m.b20*m.b28 + 864*m.b21*m.b22 + 
                       712*m.b21*m.b23 + 576*m.b21*m.b24 + 472*m.b21*m.b25 + 352*m.b21*m.b26 + 232*m.b21*m.b27 + 128*
                       m.b21*m.b28 + 56*m.b21*m.b29 + 864*m.b22*m.b23 + 712*m.b22*m.b24 + 576*m.b22*m.b25 + 472*m.b22*
                       m.b26 + 352*m.b22*m.b27 + 232*m.b22*m.b28 + 128*m.b22*m.b29 + 56*m.b22*m.b30 + 864*m.b23*m.b24 + 
                       712*m.b23*m.b25 + 576*m.b23*m.b26 + 472*m.b23*m.b27 + 352*m.b23*m.b28 + 232*m.b23*m.b29 + 128*
                       m.b23*m.b30 + 56*m.b23*m.b31 + 864*m.b24*m.b25 + 712*m.b24*m.b26 + 576*m.b24*m.b27 + 472*m.b24*
                       m.b28 + 352*m.b24*m.b29 + 232*m.b24*m.b30 + 128*m.b24*m.b31 + 56*m.b24*m.b32 + 864*m.b25*m.b26 + 
                       712*m.b25*m.b27 + 576*m.b25*m.b28 + 472*m.b25*m.b29 + 352*m.b25*m.b30 + 232*m.b25*m.b31 + 128*
                       m.b25*m.b32 + 56*m.b25*m.b33 + 864*m.b26*m.b27 + 712*m.b26*m.b28 + 576*m.b26*m.b29 + 472*m.b26*
                       m.b30 + 352*m.b26*m.b31 + 232*m.b26*m.b32 + 128*m.b26*m.b33 + 56*m.b26*m.b34 + 864*m.b27*m.b28 + 
                       712*m.b27*m.b29 + 576*m.b27*m.b30 + 472*m.b27*m.b31 + 352*m.b27*m.b32 + 232*m.b27*m.b33 + 128*
                       m.b27*m.b34 + 56*m.b27*m.b35 + 768*m.b28*m.b29 + 624*m.b28*m.b30 + 496*m.b28*m.b31 + 400*m.b28*
                       m.b32 + 272*m.b28*m.b33 + 160*m.b28*m.b34 + 64*m.b28*m.b35 + 672*m.b29*m.b30 + 520*m.b29*m.b31 + 
                       400*m.b29*m.b32 + 296*m.b29*m.b33 + 176*m.b29*m.b34 + 72*m.b29*m.b35 + 560*m.b30*m.b31 + 416*
                       m.b30*m.b32 + 288*m.b30*m.b33 + 176*m.b30*m.b34 + 80*m.b30*m.b35 + 432*m.b31*m.b32 + 296*m.b31*
                       m.b33 + 176*m.b31*m.b34 + 72*m.b31*m.b35 + 304*m.b32*m.b33 + 192*m.b32*m.b34 + 80*m.b32*m.b35 + 
                       192*m.b33*m.b34 + 88*m.b33*m.b35 + 96*m.b34*m.b35 - 112*m.b1 - 244*m.b2 - 388*m.b3 - 536*m.b4 - 
                       680*m.b5 - 828*m.b6 - 972*m.b7 - 1104*m.b8 - 1216*m.b9 - 1216*m.b10 - 1216*m.b11 - 1216*m.b12 - 
                       1216*m.b13 - 1216*m.b14 - 1216*m.b15 - 1216*m.b16 - 1216*m.b17 - 1216*m.b18 - 1216*m.b19 - 1216*
                       m.b20 - 1216*m.b21 - 1216*m.b22 - 1216*m.b23 - 1216*m.b24 - 1216*m.b25 - 1216*m.b26 - 1216*m.b27
                        - 1104*m.b28 - 972*m.b29 - 828*m.b30 - 680*m.b31 - 536*m.b32 - 388*m.b33 - 244*m.b34 - 112*m.b35
                        - m.x36 <= 0)
