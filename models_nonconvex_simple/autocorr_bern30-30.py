#  MINLP written by GAMS Convert at 08/13/20 17:37:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31        1       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         31        1       30        0


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
m.x31 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x31, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b2*m.b15*m.b16 + 64*m.b1*m.b2*m.b16*m.b17 + 64*m.b1*m.b2*m.b17*
                       m.b18 + 64*m.b1*m.b2*m.b18*m.b19 + 64*m.b1*m.b2*m.b19*m.b20 + 64*m.b1*m.b2*m.b20*m.b21 + 64*m.b1*
                       m.b2*m.b21*m.b22 + 64*m.b1*m.b2*m.b22*m.b23 + 64*m.b1*m.b2*m.b23*m.b24 + 64*m.b1*m.b2*m.b24*m.b25
                        + 64*m.b1*m.b2*m.b25*m.b26 + 64*m.b1*m.b2*m.b26*m.b27 + 64*m.b1*m.b2*m.b27*m.b28 + 64*m.b1*m.b2*
                       m.b28*m.b29 + 64*m.b1*m.b2*m.b29*m.b30 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*
                       m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11
                        + 64*m.b1*m.b3*m.b10*m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b3*
                       m.b13*m.b15 + 64*m.b1*m.b3*m.b14*m.b16 + 64*m.b1*m.b3*m.b15*m.b17 + 64*m.b1*m.b3*m.b16*m.b18 + 64
                       *m.b1*m.b3*m.b17*m.b19 + 64*m.b1*m.b3*m.b18*m.b20 + 64*m.b1*m.b3*m.b19*m.b21 + 64*m.b1*m.b3*m.b20
                       *m.b22 + 64*m.b1*m.b3*m.b21*m.b23 + 64*m.b1*m.b3*m.b22*m.b24 + 64*m.b1*m.b3*m.b23*m.b25 + 64*m.b1
                       *m.b3*m.b24*m.b26 + 64*m.b1*m.b3*m.b25*m.b27 + 64*m.b1*m.b3*m.b26*m.b28 + 64*m.b1*m.b3*m.b27*
                       m.b29 + 64*m.b1*m.b3*m.b28*m.b30 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4
                       *m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*
                       m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b4*m.b12*m.b15 + 64*m.b1*m.b4*m.b13*m.b16 + 64*m.b1*m.b4*m.b14*
                       m.b17 + 64*m.b1*m.b4*m.b15*m.b18 + 64*m.b1*m.b4*m.b16*m.b19 + 64*m.b1*m.b4*m.b17*m.b20 + 64*m.b1*
                       m.b4*m.b18*m.b21 + 64*m.b1*m.b4*m.b19*m.b22 + 64*m.b1*m.b4*m.b20*m.b23 + 64*m.b1*m.b4*m.b21*m.b24
                        + 64*m.b1*m.b4*m.b22*m.b25 + 64*m.b1*m.b4*m.b23*m.b26 + 64*m.b1*m.b4*m.b24*m.b27 + 64*m.b1*m.b4*
                       m.b25*m.b28 + 64*m.b1*m.b4*m.b26*m.b29 + 64*m.b1*m.b4*m.b27*m.b30 + 64*m.b1*m.b5*m.b6*m.b10 + 64*
                       m.b1*m.b5*m.b7*m.b11 + 64*m.b1*m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*
                       m.b14 + 64*m.b1*m.b5*m.b11*m.b15 + 64*m.b1*m.b5*m.b12*m.b16 + 64*m.b1*m.b5*m.b13*m.b17 + 64*m.b1*
                       m.b5*m.b14*m.b18 + 64*m.b1*m.b5*m.b15*m.b19 + 64*m.b1*m.b5*m.b16*m.b20 + 64*m.b1*m.b5*m.b17*m.b21
                        + 64*m.b1*m.b5*m.b18*m.b22 + 64*m.b1*m.b5*m.b19*m.b23 + 64*m.b1*m.b5*m.b20*m.b24 + 64*m.b1*m.b5*
                       m.b21*m.b25 + 64*m.b1*m.b5*m.b22*m.b26 + 64*m.b1*m.b5*m.b23*m.b27 + 64*m.b1*m.b5*m.b24*m.b28 + 64
                       *m.b1*m.b5*m.b25*m.b29 + 64*m.b1*m.b5*m.b26*m.b30 + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*
                       m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b6*m.b10*m.b15 + 64*m.b1*m.b6*m.b11*m.b16 + 64*m.b1*
                       m.b6*m.b12*m.b17 + 64*m.b1*m.b6*m.b13*m.b18 + 64*m.b1*m.b6*m.b14*m.b19 + 64*m.b1*m.b6*m.b15*m.b20
                        + 64*m.b1*m.b6*m.b16*m.b21 + 64*m.b1*m.b6*m.b17*m.b22 + 64*m.b1*m.b6*m.b18*m.b23 + 64*m.b1*m.b6*
                       m.b19*m.b24 + 64*m.b1*m.b6*m.b20*m.b25 + 64*m.b1*m.b6*m.b21*m.b26 + 64*m.b1*m.b6*m.b22*m.b27 + 64
                       *m.b1*m.b6*m.b23*m.b28 + 64*m.b1*m.b6*m.b24*m.b29 + 64*m.b1*m.b6*m.b25*m.b30 + 64*m.b1*m.b7*m.b8*
                       m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 64*m.b1*m.b7*m.b10*m.b16 + 64*m.b1*m.b7*m.b11*m.b17 + 64*m.b1*
                       m.b7*m.b12*m.b18 + 64*m.b1*m.b7*m.b13*m.b19 + 64*m.b1*m.b7*m.b14*m.b20 + 64*m.b1*m.b7*m.b15*m.b21
                        + 64*m.b1*m.b7*m.b16*m.b22 + 64*m.b1*m.b7*m.b17*m.b23 + 64*m.b1*m.b7*m.b18*m.b24 + 64*m.b1*m.b7*
                       m.b19*m.b25 + 64*m.b1*m.b7*m.b20*m.b26 + 64*m.b1*m.b7*m.b21*m.b27 + 64*m.b1*m.b7*m.b22*m.b28 + 64
                       *m.b1*m.b7*m.b23*m.b29 + 64*m.b1*m.b7*m.b24*m.b30 + 64*m.b1*m.b8*m.b9*m.b16 + 64*m.b1*m.b8*m.b10*
                       m.b17 + 64*m.b1*m.b8*m.b11*m.b18 + 64*m.b1*m.b8*m.b12*m.b19 + 64*m.b1*m.b8*m.b13*m.b20 + 64*m.b1*
                       m.b8*m.b14*m.b21 + 64*m.b1*m.b8*m.b15*m.b22 + 64*m.b1*m.b8*m.b16*m.b23 + 64*m.b1*m.b8*m.b17*m.b24
                        + 64*m.b1*m.b8*m.b18*m.b25 + 64*m.b1*m.b8*m.b19*m.b26 + 64*m.b1*m.b8*m.b20*m.b27 + 64*m.b1*m.b8*
                       m.b21*m.b28 + 64*m.b1*m.b8*m.b22*m.b29 + 64*m.b1*m.b8*m.b23*m.b30 + 64*m.b1*m.b9*m.b10*m.b18 + 64
                       *m.b1*m.b9*m.b11*m.b19 + 64*m.b1*m.b9*m.b12*m.b20 + 64*m.b1*m.b9*m.b13*m.b21 + 64*m.b1*m.b9*m.b14
                       *m.b22 + 64*m.b1*m.b9*m.b15*m.b23 + 64*m.b1*m.b9*m.b16*m.b24 + 64*m.b1*m.b9*m.b17*m.b25 + 64*m.b1
                       *m.b9*m.b18*m.b26 + 64*m.b1*m.b9*m.b19*m.b27 + 64*m.b1*m.b9*m.b20*m.b28 + 64*m.b1*m.b9*m.b21*
                       m.b29 + 64*m.b1*m.b9*m.b22*m.b30 + 64*m.b1*m.b10*m.b11*m.b20 + 64*m.b1*m.b10*m.b12*m.b21 + 64*
                       m.b1*m.b10*m.b13*m.b22 + 64*m.b1*m.b10*m.b14*m.b23 + 64*m.b1*m.b10*m.b15*m.b24 + 64*m.b1*m.b10*
                       m.b16*m.b25 + 64*m.b1*m.b10*m.b17*m.b26 + 64*m.b1*m.b10*m.b18*m.b27 + 64*m.b1*m.b10*m.b19*m.b28
                        + 64*m.b1*m.b10*m.b20*m.b29 + 64*m.b1*m.b10*m.b21*m.b30 + 64*m.b1*m.b11*m.b12*m.b22 + 64*m.b1*
                       m.b11*m.b13*m.b23 + 64*m.b1*m.b11*m.b14*m.b24 + 64*m.b1*m.b11*m.b15*m.b25 + 64*m.b1*m.b11*m.b16*
                       m.b26 + 64*m.b1*m.b11*m.b17*m.b27 + 64*m.b1*m.b11*m.b18*m.b28 + 64*m.b1*m.b11*m.b19*m.b29 + 64*
                       m.b1*m.b11*m.b20*m.b30 + 64*m.b1*m.b12*m.b13*m.b24 + 64*m.b1*m.b12*m.b14*m.b25 + 64*m.b1*m.b12*
                       m.b15*m.b26 + 64*m.b1*m.b12*m.b16*m.b27 + 64*m.b1*m.b12*m.b17*m.b28 + 64*m.b1*m.b12*m.b18*m.b29
                        + 64*m.b1*m.b12*m.b19*m.b30 + 64*m.b1*m.b13*m.b14*m.b26 + 64*m.b1*m.b13*m.b15*m.b27 + 64*m.b1*
                       m.b13*m.b16*m.b28 + 64*m.b1*m.b13*m.b17*m.b29 + 64*m.b1*m.b13*m.b18*m.b30 + 64*m.b1*m.b14*m.b15*
                       m.b28 + 64*m.b1*m.b14*m.b16*m.b29 + 64*m.b1*m.b14*m.b17*m.b30 + 64*m.b1*m.b15*m.b16*m.b30 + 64*
                       m.b2*m.b3*m.b4*m.b5 + 64*m.b2*m.b3*m.b5*m.b6 + 64*m.b2*m.b3*m.b6*m.b7 + 64*m.b2*m.b3*m.b7*m.b8 + 
                       64*m.b2*m.b3*m.b8*m.b9 + 64*m.b2*m.b3*m.b9*m.b10 + 64*m.b2*m.b3*m.b10*m.b11 + 64*m.b2*m.b3*m.b11*
                       m.b12 + 64*m.b2*m.b3*m.b12*m.b13 + 128*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 128*
                       m.b2*m.b3*m.b15*m.b16 + 128*m.b2*m.b3*m.b16*m.b17 + 128*m.b2*m.b3*m.b17*m.b18 + 128*m.b2*m.b3*
                       m.b18*m.b19 + 128*m.b2*m.b3*m.b19*m.b20 + 128*m.b2*m.b3*m.b20*m.b21 + 128*m.b2*m.b3*m.b21*m.b22
                        + 128*m.b2*m.b3*m.b22*m.b23 + 128*m.b2*m.b3*m.b23*m.b24 + 128*m.b2*m.b3*m.b24*m.b25 + 128*m.b2*
                       m.b3*m.b25*m.b26 + 128*m.b2*m.b3*m.b26*m.b27 + 128*m.b2*m.b3*m.b27*m.b28 + 128*m.b2*m.b3*m.b28*
                       m.b29 + 64*m.b2*m.b3*m.b29*m.b30 + 64*m.b2*m.b4*m.b5*m.b7 + 64*m.b2*m.b4*m.b6*m.b8 + 64*m.b2*m.b4
                       *m.b7*m.b9 + 64*m.b2*m.b4*m.b8*m.b10 + 64*m.b2*m.b4*m.b9*m.b11 + 64*m.b2*m.b4*m.b10*m.b12 + 64*
                       m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*m.b14 + 128*m.b2*m.b4*m.b13*m.b15 + 128*m.b2*m.b4*
                       m.b14*m.b16 + 128*m.b2*m.b4*m.b15*m.b17 + 128*m.b2*m.b4*m.b16*m.b18 + 128*m.b2*m.b4*m.b17*m.b19
                        + 128*m.b2*m.b4*m.b18*m.b20 + 128*m.b2*m.b4*m.b19*m.b21 + 128*m.b2*m.b4*m.b20*m.b22 + 128*m.b2*
                       m.b4*m.b21*m.b23 + 128*m.b2*m.b4*m.b22*m.b24 + 128*m.b2*m.b4*m.b23*m.b25 + 128*m.b2*m.b4*m.b24*
                       m.b26 + 128*m.b2*m.b4*m.b25*m.b27 + 128*m.b2*m.b4*m.b26*m.b28 + 128*m.b2*m.b4*m.b27*m.b29 + 64*
                       m.b2*m.b4*m.b28*m.b30 + 64*m.b2*m.b5*m.b6*m.b9 + 64*m.b2*m.b5*m.b7*m.b10 + 64*m.b2*m.b5*m.b8*
                       m.b11 + 64*m.b2*m.b5*m.b9*m.b12 + 64*m.b2*m.b5*m.b10*m.b13 + 128*m.b2*m.b5*m.b11*m.b14 + 128*m.b2
                       *m.b5*m.b12*m.b15 + 128*m.b2*m.b5*m.b13*m.b16 + 128*m.b2*m.b5*m.b14*m.b17 + 128*m.b2*m.b5*m.b15*
                       m.b18 + 128*m.b2*m.b5*m.b16*m.b19 + 128*m.b2*m.b5*m.b17*m.b20 + 128*m.b2*m.b5*m.b18*m.b21 + 128*
                       m.b2*m.b5*m.b19*m.b22 + 128*m.b2*m.b5*m.b20*m.b23 + 128*m.b2*m.b5*m.b21*m.b24 + 128*m.b2*m.b5*
                       m.b22*m.b25 + 128*m.b2*m.b5*m.b23*m.b26 + 128*m.b2*m.b5*m.b24*m.b27 + 128*m.b2*m.b5*m.b25*m.b28
                        + 128*m.b2*m.b5*m.b26*m.b29 + 64*m.b2*m.b5*m.b27*m.b30 + 64*m.b2*m.b6*m.b7*m.b11 + 64*m.b2*m.b6*
                       m.b8*m.b12 + 64*m.b2*m.b6*m.b9*m.b13 + 128*m.b2*m.b6*m.b10*m.b14 + 128*m.b2*m.b6*m.b11*m.b15 + 
                       128*m.b2*m.b6*m.b12*m.b16 + 128*m.b2*m.b6*m.b13*m.b17 + 128*m.b2*m.b6*m.b14*m.b18 + 128*m.b2*m.b6
                       *m.b15*m.b19 + 128*m.b2*m.b6*m.b16*m.b20 + 128*m.b2*m.b6*m.b17*m.b21 + 128*m.b2*m.b6*m.b18*m.b22
                        + 128*m.b2*m.b6*m.b19*m.b23 + 128*m.b2*m.b6*m.b20*m.b24 + 128*m.b2*m.b6*m.b21*m.b25 + 128*m.b2*
                       m.b6*m.b22*m.b26 + 128*m.b2*m.b6*m.b23*m.b27 + 128*m.b2*m.b6*m.b24*m.b28 + 128*m.b2*m.b6*m.b25*
                       m.b29 + 64*m.b2*m.b6*m.b26*m.b30 + 64*m.b2*m.b7*m.b8*m.b13 + 128*m.b2*m.b7*m.b9*m.b14 + 128*m.b2*
                       m.b7*m.b10*m.b15 + 128*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b7*m.b12*m.b17 + 128*m.b2*m.b7*m.b13*
                       m.b18 + 128*m.b2*m.b7*m.b14*m.b19 + 128*m.b2*m.b7*m.b15*m.b20 + 128*m.b2*m.b7*m.b16*m.b21 + 128*
                       m.b2*m.b7*m.b17*m.b22 + 128*m.b2*m.b7*m.b18*m.b23 + 128*m.b2*m.b7*m.b19*m.b24 + 128*m.b2*m.b7*
                       m.b20*m.b25 + 128*m.b2*m.b7*m.b21*m.b26 + 128*m.b2*m.b7*m.b22*m.b27 + 128*m.b2*m.b7*m.b23*m.b28
                        + 128*m.b2*m.b7*m.b24*m.b29 + 64*m.b2*m.b7*m.b25*m.b30 + 128*m.b2*m.b8*m.b9*m.b15 + 128*m.b2*
                       m.b8*m.b10*m.b16 + 128*m.b2*m.b8*m.b11*m.b17 + 128*m.b2*m.b8*m.b12*m.b18 + 128*m.b2*m.b8*m.b13*
                       m.b19 + 128*m.b2*m.b8*m.b14*m.b20 + 128*m.b2*m.b8*m.b15*m.b21 + 128*m.b2*m.b8*m.b16*m.b22 + 128*
                       m.b2*m.b8*m.b17*m.b23 + 128*m.b2*m.b8*m.b18*m.b24 + 128*m.b2*m.b8*m.b19*m.b25 + 128*m.b2*m.b8*
                       m.b20*m.b26 + 128*m.b2*m.b8*m.b21*m.b27 + 128*m.b2*m.b8*m.b22*m.b28 + 128*m.b2*m.b8*m.b23*m.b29
                        + 64*m.b2*m.b8*m.b24*m.b30 + 128*m.b2*m.b9*m.b10*m.b17 + 128*m.b2*m.b9*m.b11*m.b18 + 128*m.b2*
                       m.b9*m.b12*m.b19 + 128*m.b2*m.b9*m.b13*m.b20 + 128*m.b2*m.b9*m.b14*m.b21 + 128*m.b2*m.b9*m.b15*
                       m.b22 + 128*m.b2*m.b9*m.b16*m.b23 + 128*m.b2*m.b9*m.b17*m.b24 + 128*m.b2*m.b9*m.b18*m.b25 + 128*
                       m.b2*m.b9*m.b19*m.b26 + 128*m.b2*m.b9*m.b20*m.b27 + 128*m.b2*m.b9*m.b21*m.b28 + 128*m.b2*m.b9*
                       m.b22*m.b29 + 64*m.b2*m.b9*m.b23*m.b30 + 128*m.b2*m.b10*m.b11*m.b19 + 128*m.b2*m.b10*m.b12*m.b20
                        + 128*m.b2*m.b10*m.b13*m.b21 + 128*m.b2*m.b10*m.b14*m.b22 + 128*m.b2*m.b10*m.b15*m.b23 + 128*
                       m.b2*m.b10*m.b16*m.b24 + 128*m.b2*m.b10*m.b17*m.b25 + 128*m.b2*m.b10*m.b18*m.b26 + 128*m.b2*m.b10
                       *m.b19*m.b27 + 128*m.b2*m.b10*m.b20*m.b28 + 128*m.b2*m.b10*m.b21*m.b29 + 64*m.b2*m.b10*m.b22*
                       m.b30 + 128*m.b2*m.b11*m.b12*m.b21 + 128*m.b2*m.b11*m.b13*m.b22 + 128*m.b2*m.b11*m.b14*m.b23 + 
                       128*m.b2*m.b11*m.b15*m.b24 + 128*m.b2*m.b11*m.b16*m.b25 + 128*m.b2*m.b11*m.b17*m.b26 + 128*m.b2*
                       m.b11*m.b18*m.b27 + 128*m.b2*m.b11*m.b19*m.b28 + 128*m.b2*m.b11*m.b20*m.b29 + 64*m.b2*m.b11*m.b21
                       *m.b30 + 128*m.b2*m.b12*m.b13*m.b23 + 128*m.b2*m.b12*m.b14*m.b24 + 128*m.b2*m.b12*m.b15*m.b25 + 
                       128*m.b2*m.b12*m.b16*m.b26 + 128*m.b2*m.b12*m.b17*m.b27 + 128*m.b2*m.b12*m.b18*m.b28 + 128*m.b2*
                       m.b12*m.b19*m.b29 + 64*m.b2*m.b12*m.b20*m.b30 + 128*m.b2*m.b13*m.b14*m.b25 + 128*m.b2*m.b13*m.b15
                       *m.b26 + 128*m.b2*m.b13*m.b16*m.b27 + 128*m.b2*m.b13*m.b17*m.b28 + 128*m.b2*m.b13*m.b18*m.b29 + 
                       64*m.b2*m.b13*m.b19*m.b30 + 128*m.b2*m.b14*m.b15*m.b27 + 128*m.b2*m.b14*m.b16*m.b28 + 128*m.b2*
                       m.b14*m.b17*m.b29 + 64*m.b2*m.b14*m.b18*m.b30 + 128*m.b2*m.b15*m.b16*m.b29 + 64*m.b2*m.b15*m.b17*
                       m.b30 + 64*m.b3*m.b4*m.b5*m.b6 + 64*m.b3*m.b4*m.b6*m.b7 + 64*m.b3*m.b4*m.b7*m.b8 + 64*m.b3*m.b4*
                       m.b8*m.b9 + 64*m.b3*m.b4*m.b9*m.b10 + 64*m.b3*m.b4*m.b10*m.b11 + 64*m.b3*m.b4*m.b11*m.b12 + 64*
                       m.b3*m.b4*m.b12*m.b13 + 64*m.b3*m.b4*m.b13*m.b14 + 192*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b4*
                       m.b15*m.b16 + 192*m.b3*m.b4*m.b16*m.b17 + 192*m.b3*m.b4*m.b17*m.b18 + 192*m.b3*m.b4*m.b18*m.b19
                        + 192*m.b3*m.b4*m.b19*m.b20 + 192*m.b3*m.b4*m.b20*m.b21 + 192*m.b3*m.b4*m.b21*m.b22 + 192*m.b3*
                       m.b4*m.b22*m.b23 + 192*m.b3*m.b4*m.b23*m.b24 + 192*m.b3*m.b4*m.b24*m.b25 + 192*m.b3*m.b4*m.b25*
                       m.b26 + 192*m.b3*m.b4*m.b26*m.b27 + 192*m.b3*m.b4*m.b27*m.b28 + 128*m.b3*m.b4*m.b28*m.b29 + 64*
                       m.b3*m.b4*m.b29*m.b30 + 64*m.b3*m.b5*m.b6*m.b8 + 64*m.b3*m.b5*m.b7*m.b9 + 64*m.b3*m.b5*m.b8*m.b10
                        + 64*m.b3*m.b5*m.b9*m.b11 + 64*m.b3*m.b5*m.b10*m.b12 + 64*m.b3*m.b5*m.b11*m.b13 + 64*m.b3*m.b5*
                       m.b12*m.b14 + 192*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b5*m.b14*m.b16 + 192*m.b3*m.b5*m.b15*m.b17
                        + 192*m.b3*m.b5*m.b16*m.b18 + 192*m.b3*m.b5*m.b17*m.b19 + 192*m.b3*m.b5*m.b18*m.b20 + 192*m.b3*
                       m.b5*m.b19*m.b21 + 192*m.b3*m.b5*m.b20*m.b22 + 192*m.b3*m.b5*m.b21*m.b23 + 192*m.b3*m.b5*m.b22*
                       m.b24 + 192*m.b3*m.b5*m.b23*m.b25 + 192*m.b3*m.b5*m.b24*m.b26 + 192*m.b3*m.b5*m.b25*m.b27 + 192*
                       m.b3*m.b5*m.b26*m.b28 + 128*m.b3*m.b5*m.b27*m.b29 + 64*m.b3*m.b5*m.b28*m.b30 + 64*m.b3*m.b6*m.b7*
                       m.b10 + 64*m.b3*m.b6*m.b8*m.b11 + 64*m.b3*m.b6*m.b9*m.b12 + 64*m.b3*m.b6*m.b10*m.b13 + 64*m.b3*
                       m.b6*m.b11*m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b6*m.b13*m.b16 + 192*m.b3*m.b6*m.b14*
                       m.b17 + 192*m.b3*m.b6*m.b15*m.b18 + 192*m.b3*m.b6*m.b16*m.b19 + 192*m.b3*m.b6*m.b17*m.b20 + 192*
                       m.b3*m.b6*m.b18*m.b21 + 192*m.b3*m.b6*m.b19*m.b22 + 192*m.b3*m.b6*m.b20*m.b23 + 192*m.b3*m.b6*
                       m.b21*m.b24 + 192*m.b3*m.b6*m.b22*m.b25 + 192*m.b3*m.b6*m.b23*m.b26 + 192*m.b3*m.b6*m.b24*m.b27
                        + 192*m.b3*m.b6*m.b25*m.b28 + 128*m.b3*m.b6*m.b26*m.b29 + 64*m.b3*m.b6*m.b27*m.b30 + 64*m.b3*
                       m.b7*m.b8*m.b12 + 64*m.b3*m.b7*m.b9*m.b13 + 64*m.b3*m.b7*m.b10*m.b14 + 192*m.b3*m.b7*m.b11*m.b15
                        + 192*m.b3*m.b7*m.b12*m.b16 + 192*m.b3*m.b7*m.b13*m.b17 + 192*m.b3*m.b7*m.b14*m.b18 + 192*m.b3*
                       m.b7*m.b15*m.b19 + 192*m.b3*m.b7*m.b16*m.b20 + 192*m.b3*m.b7*m.b17*m.b21 + 192*m.b3*m.b7*m.b18*
                       m.b22 + 192*m.b3*m.b7*m.b19*m.b23 + 192*m.b3*m.b7*m.b20*m.b24 + 192*m.b3*m.b7*m.b21*m.b25 + 192*
                       m.b3*m.b7*m.b22*m.b26 + 192*m.b3*m.b7*m.b23*m.b27 + 192*m.b3*m.b7*m.b24*m.b28 + 128*m.b3*m.b7*
                       m.b25*m.b29 + 64*m.b3*m.b7*m.b26*m.b30 + 64*m.b3*m.b8*m.b9*m.b14 + 192*m.b3*m.b8*m.b10*m.b15 + 
                       192*m.b3*m.b8*m.b11*m.b16 + 192*m.b3*m.b8*m.b12*m.b17 + 192*m.b3*m.b8*m.b13*m.b18 + 192*m.b3*m.b8
                       *m.b14*m.b19 + 192*m.b3*m.b8*m.b15*m.b20 + 192*m.b3*m.b8*m.b16*m.b21 + 192*m.b3*m.b8*m.b17*m.b22
                        + 192*m.b3*m.b8*m.b18*m.b23 + 192*m.b3*m.b8*m.b19*m.b24 + 192*m.b3*m.b8*m.b20*m.b25 + 192*m.b3*
                       m.b8*m.b21*m.b26 + 192*m.b3*m.b8*m.b22*m.b27 + 192*m.b3*m.b8*m.b23*m.b28 + 128*m.b3*m.b8*m.b24*
                       m.b29 + 64*m.b3*m.b8*m.b25*m.b30 + 192*m.b3*m.b9*m.b10*m.b16 + 192*m.b3*m.b9*m.b11*m.b17 + 192*
                       m.b3*m.b9*m.b12*m.b18 + 192*m.b3*m.b9*m.b13*m.b19 + 192*m.b3*m.b9*m.b14*m.b20 + 192*m.b3*m.b9*
                       m.b15*m.b21 + 192*m.b3*m.b9*m.b16*m.b22 + 192*m.b3*m.b9*m.b17*m.b23 + 192*m.b3*m.b9*m.b18*m.b24
                        + 192*m.b3*m.b9*m.b19*m.b25 + 192*m.b3*m.b9*m.b20*m.b26 + 192*m.b3*m.b9*m.b21*m.b27 + 192*m.b3*
                       m.b9*m.b22*m.b28 + 128*m.b3*m.b9*m.b23*m.b29 + 64*m.b3*m.b9*m.b24*m.b30 + 192*m.b3*m.b10*m.b11*
                       m.b18 + 192*m.b3*m.b10*m.b12*m.b19 + 192*m.b3*m.b10*m.b13*m.b20 + 192*m.b3*m.b10*m.b14*m.b21 + 
                       192*m.b3*m.b10*m.b15*m.b22 + 192*m.b3*m.b10*m.b16*m.b23 + 192*m.b3*m.b10*m.b17*m.b24 + 192*m.b3*
                       m.b10*m.b18*m.b25 + 192*m.b3*m.b10*m.b19*m.b26 + 192*m.b3*m.b10*m.b20*m.b27 + 192*m.b3*m.b10*
                       m.b21*m.b28 + 128*m.b3*m.b10*m.b22*m.b29 + 64*m.b3*m.b10*m.b23*m.b30 + 192*m.b3*m.b11*m.b12*m.b20
                        + 192*m.b3*m.b11*m.b13*m.b21 + 192*m.b3*m.b11*m.b14*m.b22 + 192*m.b3*m.b11*m.b15*m.b23 + 192*
                       m.b3*m.b11*m.b16*m.b24 + 192*m.b3*m.b11*m.b17*m.b25 + 192*m.b3*m.b11*m.b18*m.b26 + 192*m.b3*m.b11
                       *m.b19*m.b27 + 192*m.b3*m.b11*m.b20*m.b28 + 128*m.b3*m.b11*m.b21*m.b29 + 64*m.b3*m.b11*m.b22*
                       m.b30 + 192*m.b3*m.b12*m.b13*m.b22 + 192*m.b3*m.b12*m.b14*m.b23 + 192*m.b3*m.b12*m.b15*m.b24 + 
                       192*m.b3*m.b12*m.b16*m.b25 + 192*m.b3*m.b12*m.b17*m.b26 + 192*m.b3*m.b12*m.b18*m.b27 + 192*m.b3*
                       m.b12*m.b19*m.b28 + 128*m.b3*m.b12*m.b20*m.b29 + 64*m.b3*m.b12*m.b21*m.b30 + 192*m.b3*m.b13*m.b14
                       *m.b24 + 192*m.b3*m.b13*m.b15*m.b25 + 192*m.b3*m.b13*m.b16*m.b26 + 192*m.b3*m.b13*m.b17*m.b27 + 
                       192*m.b3*m.b13*m.b18*m.b28 + 128*m.b3*m.b13*m.b19*m.b29 + 64*m.b3*m.b13*m.b20*m.b30 + 192*m.b3*
                       m.b14*m.b15*m.b26 + 192*m.b3*m.b14*m.b16*m.b27 + 192*m.b3*m.b14*m.b17*m.b28 + 128*m.b3*m.b14*
                       m.b18*m.b29 + 64*m.b3*m.b14*m.b19*m.b30 + 192*m.b3*m.b15*m.b16*m.b28 + 128*m.b3*m.b15*m.b17*m.b29
                        + 64*m.b3*m.b15*m.b18*m.b30 + 64*m.b3*m.b16*m.b17*m.b30 + 64*m.b4*m.b5*m.b6*m.b7 + 64*m.b4*m.b5*
                       m.b7*m.b8 + 64*m.b4*m.b5*m.b8*m.b9 + 64*m.b4*m.b5*m.b9*m.b10 + 64*m.b4*m.b5*m.b10*m.b11 + 64*m.b4
                       *m.b5*m.b11*m.b12 + 64*m.b4*m.b5*m.b12*m.b13 + 64*m.b4*m.b5*m.b13*m.b14 + 64*m.b4*m.b5*m.b14*
                       m.b15 + 256*m.b4*m.b5*m.b15*m.b16 + 256*m.b4*m.b5*m.b16*m.b17 + 256*m.b4*m.b5*m.b17*m.b18 + 256*
                       m.b4*m.b5*m.b18*m.b19 + 256*m.b4*m.b5*m.b19*m.b20 + 256*m.b4*m.b5*m.b20*m.b21 + 256*m.b4*m.b5*
                       m.b21*m.b22 + 256*m.b4*m.b5*m.b22*m.b23 + 256*m.b4*m.b5*m.b23*m.b24 + 256*m.b4*m.b5*m.b24*m.b25
                        + 256*m.b4*m.b5*m.b25*m.b26 + 256*m.b4*m.b5*m.b26*m.b27 + 192*m.b4*m.b5*m.b27*m.b28 + 128*m.b4*
                       m.b5*m.b28*m.b29 + 64*m.b4*m.b5*m.b29*m.b30 + 64*m.b4*m.b6*m.b7*m.b9 + 64*m.b4*m.b6*m.b8*m.b10 + 
                       64*m.b4*m.b6*m.b9*m.b11 + 64*m.b4*m.b6*m.b10*m.b12 + 64*m.b4*m.b6*m.b11*m.b13 + 64*m.b4*m.b6*
                       m.b12*m.b14 + 64*m.b4*m.b6*m.b13*m.b15 + 256*m.b4*m.b6*m.b14*m.b16 + 256*m.b4*m.b6*m.b15*m.b17 + 
                       256*m.b4*m.b6*m.b16*m.b18 + 256*m.b4*m.b6*m.b17*m.b19 + 256*m.b4*m.b6*m.b18*m.b20 + 256*m.b4*m.b6
                       *m.b19*m.b21 + 256*m.b4*m.b6*m.b20*m.b22 + 256*m.b4*m.b6*m.b21*m.b23 + 256*m.b4*m.b6*m.b22*m.b24
                        + 256*m.b4*m.b6*m.b23*m.b25 + 256*m.b4*m.b6*m.b24*m.b26 + 256*m.b4*m.b6*m.b25*m.b27 + 192*m.b4*
                       m.b6*m.b26*m.b28 + 128*m.b4*m.b6*m.b27*m.b29 + 64*m.b4*m.b6*m.b28*m.b30 + 64*m.b4*m.b7*m.b8*m.b11
                        + 64*m.b4*m.b7*m.b9*m.b12 + 64*m.b4*m.b7*m.b10*m.b13 + 64*m.b4*m.b7*m.b11*m.b14 + 64*m.b4*m.b7*
                       m.b12*m.b15 + 256*m.b4*m.b7*m.b13*m.b16 + 256*m.b4*m.b7*m.b14*m.b17 + 256*m.b4*m.b7*m.b15*m.b18
                        + 256*m.b4*m.b7*m.b16*m.b19 + 256*m.b4*m.b7*m.b17*m.b20 + 256*m.b4*m.b7*m.b18*m.b21 + 256*m.b4*
                       m.b7*m.b19*m.b22 + 256*m.b4*m.b7*m.b20*m.b23 + 256*m.b4*m.b7*m.b21*m.b24 + 256*m.b4*m.b7*m.b22*
                       m.b25 + 256*m.b4*m.b7*m.b23*m.b26 + 256*m.b4*m.b7*m.b24*m.b27 + 192*m.b4*m.b7*m.b25*m.b28 + 128*
                       m.b4*m.b7*m.b26*m.b29 + 64*m.b4*m.b7*m.b27*m.b30 + 64*m.b4*m.b8*m.b9*m.b13 + 64*m.b4*m.b8*m.b10*
                       m.b14 + 64*m.b4*m.b8*m.b11*m.b15 + 256*m.b4*m.b8*m.b12*m.b16 + 256*m.b4*m.b8*m.b13*m.b17 + 256*
                       m.b4*m.b8*m.b14*m.b18 + 256*m.b4*m.b8*m.b15*m.b19 + 256*m.b4*m.b8*m.b16*m.b20 + 256*m.b4*m.b8*
                       m.b17*m.b21 + 256*m.b4*m.b8*m.b18*m.b22 + 256*m.b4*m.b8*m.b19*m.b23 + 256*m.b4*m.b8*m.b20*m.b24
                        + 256*m.b4*m.b8*m.b21*m.b25 + 256*m.b4*m.b8*m.b22*m.b26 + 256*m.b4*m.b8*m.b23*m.b27 + 192*m.b4*
                       m.b8*m.b24*m.b28 + 128*m.b4*m.b8*m.b25*m.b29 + 64*m.b4*m.b8*m.b26*m.b30 + 64*m.b4*m.b9*m.b10*
                       m.b15 + 256*m.b4*m.b9*m.b11*m.b16 + 256*m.b4*m.b9*m.b12*m.b17 + 256*m.b4*m.b9*m.b13*m.b18 + 256*
                       m.b4*m.b9*m.b14*m.b19 + 256*m.b4*m.b9*m.b15*m.b20 + 256*m.b4*m.b9*m.b16*m.b21 + 256*m.b4*m.b9*
                       m.b17*m.b22 + 256*m.b4*m.b9*m.b18*m.b23 + 256*m.b4*m.b9*m.b19*m.b24 + 256*m.b4*m.b9*m.b20*m.b25
                        + 256*m.b4*m.b9*m.b21*m.b26 + 256*m.b4*m.b9*m.b22*m.b27 + 192*m.b4*m.b9*m.b23*m.b28 + 128*m.b4*
                       m.b9*m.b24*m.b29 + 64*m.b4*m.b9*m.b25*m.b30 + 256*m.b4*m.b10*m.b11*m.b17 + 256*m.b4*m.b10*m.b12*
                       m.b18 + 256*m.b4*m.b10*m.b13*m.b19 + 256*m.b4*m.b10*m.b14*m.b20 + 256*m.b4*m.b10*m.b15*m.b21 + 
                       256*m.b4*m.b10*m.b16*m.b22 + 256*m.b4*m.b10*m.b17*m.b23 + 256*m.b4*m.b10*m.b18*m.b24 + 256*m.b4*
                       m.b10*m.b19*m.b25 + 256*m.b4*m.b10*m.b20*m.b26 + 256*m.b4*m.b10*m.b21*m.b27 + 192*m.b4*m.b10*
                       m.b22*m.b28 + 128*m.b4*m.b10*m.b23*m.b29 + 64*m.b4*m.b10*m.b24*m.b30 + 256*m.b4*m.b11*m.b12*m.b19
                        + 256*m.b4*m.b11*m.b13*m.b20 + 256*m.b4*m.b11*m.b14*m.b21 + 256*m.b4*m.b11*m.b15*m.b22 + 256*
                       m.b4*m.b11*m.b16*m.b23 + 256*m.b4*m.b11*m.b17*m.b24 + 256*m.b4*m.b11*m.b18*m.b25 + 256*m.b4*m.b11
                       *m.b19*m.b26 + 256*m.b4*m.b11*m.b20*m.b27 + 192*m.b4*m.b11*m.b21*m.b28 + 128*m.b4*m.b11*m.b22*
                       m.b29 + 64*m.b4*m.b11*m.b23*m.b30 + 256*m.b4*m.b12*m.b13*m.b21 + 256*m.b4*m.b12*m.b14*m.b22 + 256
                       *m.b4*m.b12*m.b15*m.b23 + 256*m.b4*m.b12*m.b16*m.b24 + 256*m.b4*m.b12*m.b17*m.b25 + 256*m.b4*
                       m.b12*m.b18*m.b26 + 256*m.b4*m.b12*m.b19*m.b27 + 192*m.b4*m.b12*m.b20*m.b28 + 128*m.b4*m.b12*
                       m.b21*m.b29 + 64*m.b4*m.b12*m.b22*m.b30 + 256*m.b4*m.b13*m.b14*m.b23 + 256*m.b4*m.b13*m.b15*m.b24
                        + 256*m.b4*m.b13*m.b16*m.b25 + 256*m.b4*m.b13*m.b17*m.b26 + 256*m.b4*m.b13*m.b18*m.b27 + 192*
                       m.b4*m.b13*m.b19*m.b28 + 128*m.b4*m.b13*m.b20*m.b29 + 64*m.b4*m.b13*m.b21*m.b30 + 256*m.b4*m.b14*
                       m.b15*m.b25 + 256*m.b4*m.b14*m.b16*m.b26 + 256*m.b4*m.b14*m.b17*m.b27 + 192*m.b4*m.b14*m.b18*
                       m.b28 + 128*m.b4*m.b14*m.b19*m.b29 + 64*m.b4*m.b14*m.b20*m.b30 + 256*m.b4*m.b15*m.b16*m.b27 + 192
                       *m.b4*m.b15*m.b17*m.b28 + 128*m.b4*m.b15*m.b18*m.b29 + 64*m.b4*m.b15*m.b19*m.b30 + 128*m.b4*m.b16
                       *m.b17*m.b29 + 64*m.b4*m.b16*m.b18*m.b30 + 64*m.b5*m.b6*m.b7*m.b8 + 64*m.b5*m.b6*m.b8*m.b9 + 64*
                       m.b5*m.b6*m.b9*m.b10 + 64*m.b5*m.b6*m.b10*m.b11 + 64*m.b5*m.b6*m.b11*m.b12 + 64*m.b5*m.b6*m.b12*
                       m.b13 + 64*m.b5*m.b6*m.b13*m.b14 + 64*m.b5*m.b6*m.b14*m.b15 + 64*m.b5*m.b6*m.b15*m.b16 + 320*m.b5
                       *m.b6*m.b16*m.b17 + 320*m.b5*m.b6*m.b17*m.b18 + 320*m.b5*m.b6*m.b18*m.b19 + 320*m.b5*m.b6*m.b19*
                       m.b20 + 320*m.b5*m.b6*m.b20*m.b21 + 320*m.b5*m.b6*m.b21*m.b22 + 320*m.b5*m.b6*m.b22*m.b23 + 320*
                       m.b5*m.b6*m.b23*m.b24 + 320*m.b5*m.b6*m.b24*m.b25 + 320*m.b5*m.b6*m.b25*m.b26 + 256*m.b5*m.b6*
                       m.b26*m.b27 + 192*m.b5*m.b6*m.b27*m.b28 + 128*m.b5*m.b6*m.b28*m.b29 + 64*m.b5*m.b6*m.b29*m.b30 + 
                       64*m.b5*m.b7*m.b8*m.b10 + 64*m.b5*m.b7*m.b9*m.b11 + 64*m.b5*m.b7*m.b10*m.b12 + 64*m.b5*m.b7*m.b11
                       *m.b13 + 64*m.b5*m.b7*m.b12*m.b14 + 64*m.b5*m.b7*m.b13*m.b15 + 64*m.b5*m.b7*m.b14*m.b16 + 320*
                       m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b7*m.b16*m.b18 + 320*m.b5*m.b7*m.b17*m.b19 + 320*m.b5*m.b7*
                       m.b18*m.b20 + 320*m.b5*m.b7*m.b19*m.b21 + 320*m.b5*m.b7*m.b20*m.b22 + 320*m.b5*m.b7*m.b21*m.b23
                        + 320*m.b5*m.b7*m.b22*m.b24 + 320*m.b5*m.b7*m.b23*m.b25 + 320*m.b5*m.b7*m.b24*m.b26 + 256*m.b5*
                       m.b7*m.b25*m.b27 + 192*m.b5*m.b7*m.b26*m.b28 + 128*m.b5*m.b7*m.b27*m.b29 + 64*m.b5*m.b7*m.b28*
                       m.b30 + 64*m.b5*m.b8*m.b9*m.b12 + 64*m.b5*m.b8*m.b10*m.b13 + 64*m.b5*m.b8*m.b11*m.b14 + 64*m.b5*
                       m.b8*m.b12*m.b15 + 64*m.b5*m.b8*m.b13*m.b16 + 320*m.b5*m.b8*m.b14*m.b17 + 320*m.b5*m.b8*m.b15*
                       m.b18 + 320*m.b5*m.b8*m.b16*m.b19 + 320*m.b5*m.b8*m.b17*m.b20 + 320*m.b5*m.b8*m.b18*m.b21 + 320*
                       m.b5*m.b8*m.b19*m.b22 + 320*m.b5*m.b8*m.b20*m.b23 + 320*m.b5*m.b8*m.b21*m.b24 + 320*m.b5*m.b8*
                       m.b22*m.b25 + 320*m.b5*m.b8*m.b23*m.b26 + 256*m.b5*m.b8*m.b24*m.b27 + 192*m.b5*m.b8*m.b25*m.b28
                        + 128*m.b5*m.b8*m.b26*m.b29 + 64*m.b5*m.b8*m.b27*m.b30 + 64*m.b5*m.b9*m.b10*m.b14 + 64*m.b5*m.b9
                       *m.b11*m.b15 + 64*m.b5*m.b9*m.b12*m.b16 + 320*m.b5*m.b9*m.b13*m.b17 + 320*m.b5*m.b9*m.b14*m.b18
                        + 320*m.b5*m.b9*m.b15*m.b19 + 320*m.b5*m.b9*m.b16*m.b20 + 320*m.b5*m.b9*m.b17*m.b21 + 320*m.b5*
                       m.b9*m.b18*m.b22 + 320*m.b5*m.b9*m.b19*m.b23 + 320*m.b5*m.b9*m.b20*m.b24 + 320*m.b5*m.b9*m.b21*
                       m.b25 + 320*m.b5*m.b9*m.b22*m.b26 + 256*m.b5*m.b9*m.b23*m.b27 + 192*m.b5*m.b9*m.b24*m.b28 + 128*
                       m.b5*m.b9*m.b25*m.b29 + 64*m.b5*m.b9*m.b26*m.b30 + 64*m.b5*m.b10*m.b11*m.b16 + 320*m.b5*m.b10*
                       m.b12*m.b17 + 320*m.b5*m.b10*m.b13*m.b18 + 320*m.b5*m.b10*m.b14*m.b19 + 320*m.b5*m.b10*m.b15*
                       m.b20 + 320*m.b5*m.b10*m.b16*m.b21 + 320*m.b5*m.b10*m.b17*m.b22 + 320*m.b5*m.b10*m.b18*m.b23 + 
                       320*m.b5*m.b10*m.b19*m.b24 + 320*m.b5*m.b10*m.b20*m.b25 + 320*m.b5*m.b10*m.b21*m.b26 + 256*m.b5*
                       m.b10*m.b22*m.b27 + 192*m.b5*m.b10*m.b23*m.b28 + 128*m.b5*m.b10*m.b24*m.b29 + 64*m.b5*m.b10*m.b25
                       *m.b30 + 320*m.b5*m.b11*m.b12*m.b18 + 320*m.b5*m.b11*m.b13*m.b19 + 320*m.b5*m.b11*m.b14*m.b20 + 
                       320*m.b5*m.b11*m.b15*m.b21 + 320*m.b5*m.b11*m.b16*m.b22 + 320*m.b5*m.b11*m.b17*m.b23 + 320*m.b5*
                       m.b11*m.b18*m.b24 + 320*m.b5*m.b11*m.b19*m.b25 + 320*m.b5*m.b11*m.b20*m.b26 + 256*m.b5*m.b11*
                       m.b21*m.b27 + 192*m.b5*m.b11*m.b22*m.b28 + 128*m.b5*m.b11*m.b23*m.b29 + 64*m.b5*m.b11*m.b24*m.b30
                        + 320*m.b5*m.b12*m.b13*m.b20 + 320*m.b5*m.b12*m.b14*m.b21 + 320*m.b5*m.b12*m.b15*m.b22 + 320*
                       m.b5*m.b12*m.b16*m.b23 + 320*m.b5*m.b12*m.b17*m.b24 + 320*m.b5*m.b12*m.b18*m.b25 + 320*m.b5*m.b12
                       *m.b19*m.b26 + 256*m.b5*m.b12*m.b20*m.b27 + 192*m.b5*m.b12*m.b21*m.b28 + 128*m.b5*m.b12*m.b22*
                       m.b29 + 64*m.b5*m.b12*m.b23*m.b30 + 320*m.b5*m.b13*m.b14*m.b22 + 320*m.b5*m.b13*m.b15*m.b23 + 320
                       *m.b5*m.b13*m.b16*m.b24 + 320*m.b5*m.b13*m.b17*m.b25 + 320*m.b5*m.b13*m.b18*m.b26 + 256*m.b5*
                       m.b13*m.b19*m.b27 + 192*m.b5*m.b13*m.b20*m.b28 + 128*m.b5*m.b13*m.b21*m.b29 + 64*m.b5*m.b13*m.b22
                       *m.b30 + 320*m.b5*m.b14*m.b15*m.b24 + 320*m.b5*m.b14*m.b16*m.b25 + 320*m.b5*m.b14*m.b17*m.b26 + 
                       256*m.b5*m.b14*m.b18*m.b27 + 192*m.b5*m.b14*m.b19*m.b28 + 128*m.b5*m.b14*m.b20*m.b29 + 64*m.b5*
                       m.b14*m.b21*m.b30 + 320*m.b5*m.b15*m.b16*m.b26 + 256*m.b5*m.b15*m.b17*m.b27 + 192*m.b5*m.b15*
                       m.b18*m.b28 + 128*m.b5*m.b15*m.b19*m.b29 + 64*m.b5*m.b15*m.b20*m.b30 + 192*m.b5*m.b16*m.b17*m.b28
                        + 128*m.b5*m.b16*m.b18*m.b29 + 64*m.b5*m.b16*m.b19*m.b30 + 64*m.b5*m.b17*m.b18*m.b30 + 64*m.b6*
                       m.b7*m.b8*m.b9 + 64*m.b6*m.b7*m.b9*m.b10 + 64*m.b6*m.b7*m.b10*m.b11 + 64*m.b6*m.b7*m.b11*m.b12 + 
                       64*m.b6*m.b7*m.b12*m.b13 + 64*m.b6*m.b7*m.b13*m.b14 + 64*m.b6*m.b7*m.b14*m.b15 + 64*m.b6*m.b7*
                       m.b15*m.b16 + 64*m.b6*m.b7*m.b16*m.b17 + 384*m.b6*m.b7*m.b17*m.b18 + 384*m.b6*m.b7*m.b18*m.b19 + 
                       384*m.b6*m.b7*m.b19*m.b20 + 384*m.b6*m.b7*m.b20*m.b21 + 384*m.b6*m.b7*m.b21*m.b22 + 384*m.b6*m.b7
                       *m.b22*m.b23 + 384*m.b6*m.b7*m.b23*m.b24 + 384*m.b6*m.b7*m.b24*m.b25 + 320*m.b6*m.b7*m.b25*m.b26
                        + 256*m.b6*m.b7*m.b26*m.b27 + 192*m.b6*m.b7*m.b27*m.b28 + 128*m.b6*m.b7*m.b28*m.b29 + 64*m.b6*
                       m.b7*m.b29*m.b30 + 64*m.b6*m.b8*m.b9*m.b11 + 64*m.b6*m.b8*m.b10*m.b12 + 64*m.b6*m.b8*m.b11*m.b13
                        + 64*m.b6*m.b8*m.b12*m.b14 + 64*m.b6*m.b8*m.b13*m.b15 + 64*m.b6*m.b8*m.b14*m.b16 + 64*m.b6*m.b8*
                       m.b15*m.b17 + 384*m.b6*m.b8*m.b16*m.b18 + 384*m.b6*m.b8*m.b17*m.b19 + 384*m.b6*m.b8*m.b18*m.b20
                        + 384*m.b6*m.b8*m.b19*m.b21 + 384*m.b6*m.b8*m.b20*m.b22 + 384*m.b6*m.b8*m.b21*m.b23 + 384*m.b6*
                       m.b8*m.b22*m.b24 + 384*m.b6*m.b8*m.b23*m.b25 + 320*m.b6*m.b8*m.b24*m.b26 + 256*m.b6*m.b8*m.b25*
                       m.b27 + 192*m.b6*m.b8*m.b26*m.b28 + 128*m.b6*m.b8*m.b27*m.b29 + 64*m.b6*m.b8*m.b28*m.b30 + 64*
                       m.b6*m.b9*m.b10*m.b13 + 64*m.b6*m.b9*m.b11*m.b14 + 64*m.b6*m.b9*m.b12*m.b15 + 64*m.b6*m.b9*m.b13*
                       m.b16 + 64*m.b6*m.b9*m.b14*m.b17 + 384*m.b6*m.b9*m.b15*m.b18 + 384*m.b6*m.b9*m.b16*m.b19 + 384*
                       m.b6*m.b9*m.b17*m.b20 + 384*m.b6*m.b9*m.b18*m.b21 + 384*m.b6*m.b9*m.b19*m.b22 + 384*m.b6*m.b9*
                       m.b20*m.b23 + 384*m.b6*m.b9*m.b21*m.b24 + 384*m.b6*m.b9*m.b22*m.b25 + 320*m.b6*m.b9*m.b23*m.b26
                        + 256*m.b6*m.b9*m.b24*m.b27 + 192*m.b6*m.b9*m.b25*m.b28 + 128*m.b6*m.b9*m.b26*m.b29 + 64*m.b6*
                       m.b9*m.b27*m.b30 + 64*m.b6*m.b10*m.b11*m.b15 + 64*m.b6*m.b10*m.b12*m.b16 + 64*m.b6*m.b10*m.b13*
                       m.b17 + 384*m.b6*m.b10*m.b14*m.b18 + 384*m.b6*m.b10*m.b15*m.b19 + 384*m.b6*m.b10*m.b16*m.b20 + 
                       384*m.b6*m.b10*m.b17*m.b21 + 384*m.b6*m.b10*m.b18*m.b22 + 384*m.b6*m.b10*m.b19*m.b23 + 384*m.b6*
                       m.b10*m.b20*m.b24 + 384*m.b6*m.b10*m.b21*m.b25 + 320*m.b6*m.b10*m.b22*m.b26 + 256*m.b6*m.b10*
                       m.b23*m.b27 + 192*m.b6*m.b10*m.b24*m.b28 + 128*m.b6*m.b10*m.b25*m.b29 + 64*m.b6*m.b10*m.b26*m.b30
                        + 64*m.b6*m.b11*m.b12*m.b17 + 384*m.b6*m.b11*m.b13*m.b18 + 384*m.b6*m.b11*m.b14*m.b19 + 384*m.b6
                       *m.b11*m.b15*m.b20 + 384*m.b6*m.b11*m.b16*m.b21 + 384*m.b6*m.b11*m.b17*m.b22 + 384*m.b6*m.b11*
                       m.b18*m.b23 + 384*m.b6*m.b11*m.b19*m.b24 + 384*m.b6*m.b11*m.b20*m.b25 + 320*m.b6*m.b11*m.b21*
                       m.b26 + 256*m.b6*m.b11*m.b22*m.b27 + 192*m.b6*m.b11*m.b23*m.b28 + 128*m.b6*m.b11*m.b24*m.b29 + 64
                       *m.b6*m.b11*m.b25*m.b30 + 384*m.b6*m.b12*m.b13*m.b19 + 384*m.b6*m.b12*m.b14*m.b20 + 384*m.b6*
                       m.b12*m.b15*m.b21 + 384*m.b6*m.b12*m.b16*m.b22 + 384*m.b6*m.b12*m.b17*m.b23 + 384*m.b6*m.b12*
                       m.b18*m.b24 + 384*m.b6*m.b12*m.b19*m.b25 + 320*m.b6*m.b12*m.b20*m.b26 + 256*m.b6*m.b12*m.b21*
                       m.b27 + 192*m.b6*m.b12*m.b22*m.b28 + 128*m.b6*m.b12*m.b23*m.b29 + 64*m.b6*m.b12*m.b24*m.b30 + 384
                       *m.b6*m.b13*m.b14*m.b21 + 384*m.b6*m.b13*m.b15*m.b22 + 384*m.b6*m.b13*m.b16*m.b23 + 384*m.b6*
                       m.b13*m.b17*m.b24 + 384*m.b6*m.b13*m.b18*m.b25 + 320*m.b6*m.b13*m.b19*m.b26 + 256*m.b6*m.b13*
                       m.b20*m.b27 + 192*m.b6*m.b13*m.b21*m.b28 + 128*m.b6*m.b13*m.b22*m.b29 + 64*m.b6*m.b13*m.b23*m.b30
                        + 384*m.b6*m.b14*m.b15*m.b23 + 384*m.b6*m.b14*m.b16*m.b24 + 384*m.b6*m.b14*m.b17*m.b25 + 320*
                       m.b6*m.b14*m.b18*m.b26 + 256*m.b6*m.b14*m.b19*m.b27 + 192*m.b6*m.b14*m.b20*m.b28 + 128*m.b6*m.b14
                       *m.b21*m.b29 + 64*m.b6*m.b14*m.b22*m.b30 + 384*m.b6*m.b15*m.b16*m.b25 + 320*m.b6*m.b15*m.b17*
                       m.b26 + 256*m.b6*m.b15*m.b18*m.b27 + 192*m.b6*m.b15*m.b19*m.b28 + 128*m.b6*m.b15*m.b20*m.b29 + 64
                       *m.b6*m.b15*m.b21*m.b30 + 256*m.b6*m.b16*m.b17*m.b27 + 192*m.b6*m.b16*m.b18*m.b28 + 128*m.b6*
                       m.b16*m.b19*m.b29 + 64*m.b6*m.b16*m.b20*m.b30 + 128*m.b6*m.b17*m.b18*m.b29 + 64*m.b6*m.b17*m.b19*
                       m.b30 + 64*m.b7*m.b8*m.b9*m.b10 + 64*m.b7*m.b8*m.b10*m.b11 + 64*m.b7*m.b8*m.b11*m.b12 + 64*m.b7*
                       m.b8*m.b12*m.b13 + 64*m.b7*m.b8*m.b13*m.b14 + 64*m.b7*m.b8*m.b14*m.b15 + 64*m.b7*m.b8*m.b15*m.b16
                        + 64*m.b7*m.b8*m.b16*m.b17 + 64*m.b7*m.b8*m.b17*m.b18 + 448*m.b7*m.b8*m.b18*m.b19 + 448*m.b7*
                       m.b8*m.b19*m.b20 + 448*m.b7*m.b8*m.b20*m.b21 + 448*m.b7*m.b8*m.b21*m.b22 + 448*m.b7*m.b8*m.b22*
                       m.b23 + 448*m.b7*m.b8*m.b23*m.b24 + 384*m.b7*m.b8*m.b24*m.b25 + 320*m.b7*m.b8*m.b25*m.b26 + 256*
                       m.b7*m.b8*m.b26*m.b27 + 192*m.b7*m.b8*m.b27*m.b28 + 128*m.b7*m.b8*m.b28*m.b29 + 64*m.b7*m.b8*
                       m.b29*m.b30 + 64*m.b7*m.b9*m.b10*m.b12 + 64*m.b7*m.b9*m.b11*m.b13 + 64*m.b7*m.b9*m.b12*m.b14 + 64
                       *m.b7*m.b9*m.b13*m.b15 + 64*m.b7*m.b9*m.b14*m.b16 + 64*m.b7*m.b9*m.b15*m.b17 + 64*m.b7*m.b9*m.b16
                       *m.b18 + 448*m.b7*m.b9*m.b17*m.b19 + 448*m.b7*m.b9*m.b18*m.b20 + 448*m.b7*m.b9*m.b19*m.b21 + 448*
                       m.b7*m.b9*m.b20*m.b22 + 448*m.b7*m.b9*m.b21*m.b23 + 448*m.b7*m.b9*m.b22*m.b24 + 384*m.b7*m.b9*
                       m.b23*m.b25 + 320*m.b7*m.b9*m.b24*m.b26 + 256*m.b7*m.b9*m.b25*m.b27 + 192*m.b7*m.b9*m.b26*m.b28
                        + 128*m.b7*m.b9*m.b27*m.b29 + 64*m.b7*m.b9*m.b28*m.b30 + 64*m.b7*m.b10*m.b11*m.b14 + 64*m.b7*
                       m.b10*m.b12*m.b15 + 64*m.b7*m.b10*m.b13*m.b16 + 64*m.b7*m.b10*m.b14*m.b17 + 64*m.b7*m.b10*m.b15*
                       m.b18 + 448*m.b7*m.b10*m.b16*m.b19 + 448*m.b7*m.b10*m.b17*m.b20 + 448*m.b7*m.b10*m.b18*m.b21 + 
                       448*m.b7*m.b10*m.b19*m.b22 + 448*m.b7*m.b10*m.b20*m.b23 + 448*m.b7*m.b10*m.b21*m.b24 + 384*m.b7*
                       m.b10*m.b22*m.b25 + 320*m.b7*m.b10*m.b23*m.b26 + 256*m.b7*m.b10*m.b24*m.b27 + 192*m.b7*m.b10*
                       m.b25*m.b28 + 128*m.b7*m.b10*m.b26*m.b29 + 64*m.b7*m.b10*m.b27*m.b30 + 64*m.b7*m.b11*m.b12*m.b16
                        + 64*m.b7*m.b11*m.b13*m.b17 + 64*m.b7*m.b11*m.b14*m.b18 + 448*m.b7*m.b11*m.b15*m.b19 + 448*m.b7*
                       m.b11*m.b16*m.b20 + 448*m.b7*m.b11*m.b17*m.b21 + 448*m.b7*m.b11*m.b18*m.b22 + 448*m.b7*m.b11*
                       m.b19*m.b23 + 448*m.b7*m.b11*m.b20*m.b24 + 384*m.b7*m.b11*m.b21*m.b25 + 320*m.b7*m.b11*m.b22*
                       m.b26 + 256*m.b7*m.b11*m.b23*m.b27 + 192*m.b7*m.b11*m.b24*m.b28 + 128*m.b7*m.b11*m.b25*m.b29 + 64
                       *m.b7*m.b11*m.b26*m.b30 + 64*m.b7*m.b12*m.b13*m.b18 + 448*m.b7*m.b12*m.b14*m.b19 + 448*m.b7*m.b12
                       *m.b15*m.b20 + 448*m.b7*m.b12*m.b16*m.b21 + 448*m.b7*m.b12*m.b17*m.b22 + 448*m.b7*m.b12*m.b18*
                       m.b23 + 448*m.b7*m.b12*m.b19*m.b24 + 384*m.b7*m.b12*m.b20*m.b25 + 320*m.b7*m.b12*m.b21*m.b26 + 
                       256*m.b7*m.b12*m.b22*m.b27 + 192*m.b7*m.b12*m.b23*m.b28 + 128*m.b7*m.b12*m.b24*m.b29 + 64*m.b7*
                       m.b12*m.b25*m.b30 + 448*m.b7*m.b13*m.b14*m.b20 + 448*m.b7*m.b13*m.b15*m.b21 + 448*m.b7*m.b13*
                       m.b16*m.b22 + 448*m.b7*m.b13*m.b17*m.b23 + 448*m.b7*m.b13*m.b18*m.b24 + 384*m.b7*m.b13*m.b19*
                       m.b25 + 320*m.b7*m.b13*m.b20*m.b26 + 256*m.b7*m.b13*m.b21*m.b27 + 192*m.b7*m.b13*m.b22*m.b28 + 
                       128*m.b7*m.b13*m.b23*m.b29 + 64*m.b7*m.b13*m.b24*m.b30 + 448*m.b7*m.b14*m.b15*m.b22 + 448*m.b7*
                       m.b14*m.b16*m.b23 + 448*m.b7*m.b14*m.b17*m.b24 + 384*m.b7*m.b14*m.b18*m.b25 + 320*m.b7*m.b14*
                       m.b19*m.b26 + 256*m.b7*m.b14*m.b20*m.b27 + 192*m.b7*m.b14*m.b21*m.b28 + 128*m.b7*m.b14*m.b22*
                       m.b29 + 64*m.b7*m.b14*m.b23*m.b30 + 448*m.b7*m.b15*m.b16*m.b24 + 384*m.b7*m.b15*m.b17*m.b25 + 320
                       *m.b7*m.b15*m.b18*m.b26 + 256*m.b7*m.b15*m.b19*m.b27 + 192*m.b7*m.b15*m.b20*m.b28 + 128*m.b7*
                       m.b15*m.b21*m.b29 + 64*m.b7*m.b15*m.b22*m.b30 + 320*m.b7*m.b16*m.b17*m.b26 + 256*m.b7*m.b16*m.b18
                       *m.b27 + 192*m.b7*m.b16*m.b19*m.b28 + 128*m.b7*m.b16*m.b20*m.b29 + 64*m.b7*m.b16*m.b21*m.b30 + 
                       192*m.b7*m.b17*m.b18*m.b28 + 128*m.b7*m.b17*m.b19*m.b29 + 64*m.b7*m.b17*m.b20*m.b30 + 64*m.b7*
                       m.b18*m.b19*m.b30 + 64*m.b8*m.b9*m.b10*m.b11 + 64*m.b8*m.b9*m.b11*m.b12 + 64*m.b8*m.b9*m.b12*
                       m.b13 + 64*m.b8*m.b9*m.b13*m.b14 + 64*m.b8*m.b9*m.b14*m.b15 + 64*m.b8*m.b9*m.b15*m.b16 + 64*m.b8*
                       m.b9*m.b16*m.b17 + 64*m.b8*m.b9*m.b17*m.b18 + 64*m.b8*m.b9*m.b18*m.b19 + 512*m.b8*m.b9*m.b19*
                       m.b20 + 512*m.b8*m.b9*m.b20*m.b21 + 512*m.b8*m.b9*m.b21*m.b22 + 512*m.b8*m.b9*m.b22*m.b23 + 448*
                       m.b8*m.b9*m.b23*m.b24 + 384*m.b8*m.b9*m.b24*m.b25 + 320*m.b8*m.b9*m.b25*m.b26 + 256*m.b8*m.b9*
                       m.b26*m.b27 + 192*m.b8*m.b9*m.b27*m.b28 + 128*m.b8*m.b9*m.b28*m.b29 + 64*m.b8*m.b9*m.b29*m.b30 + 
                       64*m.b8*m.b10*m.b11*m.b13 + 64*m.b8*m.b10*m.b12*m.b14 + 64*m.b8*m.b10*m.b13*m.b15 + 64*m.b8*m.b10
                       *m.b14*m.b16 + 64*m.b8*m.b10*m.b15*m.b17 + 64*m.b8*m.b10*m.b16*m.b18 + 64*m.b8*m.b10*m.b17*m.b19
                        + 512*m.b8*m.b10*m.b18*m.b20 + 512*m.b8*m.b10*m.b19*m.b21 + 512*m.b8*m.b10*m.b20*m.b22 + 512*
                       m.b8*m.b10*m.b21*m.b23 + 448*m.b8*m.b10*m.b22*m.b24 + 384*m.b8*m.b10*m.b23*m.b25 + 320*m.b8*m.b10
                       *m.b24*m.b26 + 256*m.b8*m.b10*m.b25*m.b27 + 192*m.b8*m.b10*m.b26*m.b28 + 128*m.b8*m.b10*m.b27*
                       m.b29 + 64*m.b8*m.b10*m.b28*m.b30 + 64*m.b8*m.b11*m.b12*m.b15 + 64*m.b8*m.b11*m.b13*m.b16 + 64*
                       m.b8*m.b11*m.b14*m.b17 + 64*m.b8*m.b11*m.b15*m.b18 + 64*m.b8*m.b11*m.b16*m.b19 + 512*m.b8*m.b11*
                       m.b17*m.b20 + 512*m.b8*m.b11*m.b18*m.b21 + 512*m.b8*m.b11*m.b19*m.b22 + 512*m.b8*m.b11*m.b20*
                       m.b23 + 448*m.b8*m.b11*m.b21*m.b24 + 384*m.b8*m.b11*m.b22*m.b25 + 320*m.b8*m.b11*m.b23*m.b26 + 
                       256*m.b8*m.b11*m.b24*m.b27 + 192*m.b8*m.b11*m.b25*m.b28 + 128*m.b8*m.b11*m.b26*m.b29 + 64*m.b8*
                       m.b11*m.b27*m.b30 + 64*m.b8*m.b12*m.b13*m.b17 + 64*m.b8*m.b12*m.b14*m.b18 + 64*m.b8*m.b12*m.b15*
                       m.b19 + 512*m.b8*m.b12*m.b16*m.b20 + 512*m.b8*m.b12*m.b17*m.b21 + 512*m.b8*m.b12*m.b18*m.b22 + 
                       512*m.b8*m.b12*m.b19*m.b23 + 448*m.b8*m.b12*m.b20*m.b24 + 384*m.b8*m.b12*m.b21*m.b25 + 320*m.b8*
                       m.b12*m.b22*m.b26 + 256*m.b8*m.b12*m.b23*m.b27 + 192*m.b8*m.b12*m.b24*m.b28 + 128*m.b8*m.b12*
                       m.b25*m.b29 + 64*m.b8*m.b12*m.b26*m.b30 + 64*m.b8*m.b13*m.b14*m.b19 + 512*m.b8*m.b13*m.b15*m.b20
                        + 512*m.b8*m.b13*m.b16*m.b21 + 512*m.b8*m.b13*m.b17*m.b22 + 512*m.b8*m.b13*m.b18*m.b23 + 448*
                       m.b8*m.b13*m.b19*m.b24 + 384*m.b8*m.b13*m.b20*m.b25 + 320*m.b8*m.b13*m.b21*m.b26 + 256*m.b8*m.b13
                       *m.b22*m.b27 + 192*m.b8*m.b13*m.b23*m.b28 + 128*m.b8*m.b13*m.b24*m.b29 + 64*m.b8*m.b13*m.b25*
                       m.b30 + 512*m.b8*m.b14*m.b15*m.b21 + 512*m.b8*m.b14*m.b16*m.b22 + 512*m.b8*m.b14*m.b17*m.b23 + 
                       448*m.b8*m.b14*m.b18*m.b24 + 384*m.b8*m.b14*m.b19*m.b25 + 320*m.b8*m.b14*m.b20*m.b26 + 256*m.b8*
                       m.b14*m.b21*m.b27 + 192*m.b8*m.b14*m.b22*m.b28 + 128*m.b8*m.b14*m.b23*m.b29 + 64*m.b8*m.b14*m.b24
                       *m.b30 + 512*m.b8*m.b15*m.b16*m.b23 + 448*m.b8*m.b15*m.b17*m.b24 + 384*m.b8*m.b15*m.b18*m.b25 + 
                       320*m.b8*m.b15*m.b19*m.b26 + 256*m.b8*m.b15*m.b20*m.b27 + 192*m.b8*m.b15*m.b21*m.b28 + 128*m.b8*
                       m.b15*m.b22*m.b29 + 64*m.b8*m.b15*m.b23*m.b30 + 384*m.b8*m.b16*m.b17*m.b25 + 320*m.b8*m.b16*m.b18
                       *m.b26 + 256*m.b8*m.b16*m.b19*m.b27 + 192*m.b8*m.b16*m.b20*m.b28 + 128*m.b8*m.b16*m.b21*m.b29 + 
                       64*m.b8*m.b16*m.b22*m.b30 + 256*m.b8*m.b17*m.b18*m.b27 + 192*m.b8*m.b17*m.b19*m.b28 + 128*m.b8*
                       m.b17*m.b20*m.b29 + 64*m.b8*m.b17*m.b21*m.b30 + 128*m.b8*m.b18*m.b19*m.b29 + 64*m.b8*m.b18*m.b20*
                       m.b30 + 64*m.b9*m.b10*m.b11*m.b12 + 64*m.b9*m.b10*m.b12*m.b13 + 64*m.b9*m.b10*m.b13*m.b14 + 64*
                       m.b9*m.b10*m.b14*m.b15 + 64*m.b9*m.b10*m.b15*m.b16 + 64*m.b9*m.b10*m.b16*m.b17 + 64*m.b9*m.b10*
                       m.b17*m.b18 + 64*m.b9*m.b10*m.b18*m.b19 + 64*m.b9*m.b10*m.b19*m.b20 + 576*m.b9*m.b10*m.b20*m.b21
                        + 576*m.b9*m.b10*m.b21*m.b22 + 512*m.b9*m.b10*m.b22*m.b23 + 448*m.b9*m.b10*m.b23*m.b24 + 384*
                       m.b9*m.b10*m.b24*m.b25 + 320*m.b9*m.b10*m.b25*m.b26 + 256*m.b9*m.b10*m.b26*m.b27 + 192*m.b9*m.b10
                       *m.b27*m.b28 + 128*m.b9*m.b10*m.b28*m.b29 + 64*m.b9*m.b10*m.b29*m.b30 + 64*m.b9*m.b11*m.b12*m.b14
                        + 64*m.b9*m.b11*m.b13*m.b15 + 64*m.b9*m.b11*m.b14*m.b16 + 64*m.b9*m.b11*m.b15*m.b17 + 64*m.b9*
                       m.b11*m.b16*m.b18 + 64*m.b9*m.b11*m.b17*m.b19 + 64*m.b9*m.b11*m.b18*m.b20 + 576*m.b9*m.b11*m.b19*
                       m.b21 + 576*m.b9*m.b11*m.b20*m.b22 + 512*m.b9*m.b11*m.b21*m.b23 + 448*m.b9*m.b11*m.b22*m.b24 + 
                       384*m.b9*m.b11*m.b23*m.b25 + 320*m.b9*m.b11*m.b24*m.b26 + 256*m.b9*m.b11*m.b25*m.b27 + 192*m.b9*
                       m.b11*m.b26*m.b28 + 128*m.b9*m.b11*m.b27*m.b29 + 64*m.b9*m.b11*m.b28*m.b30 + 64*m.b9*m.b12*m.b13*
                       m.b16 + 64*m.b9*m.b12*m.b14*m.b17 + 64*m.b9*m.b12*m.b15*m.b18 + 64*m.b9*m.b12*m.b16*m.b19 + 64*
                       m.b9*m.b12*m.b17*m.b20 + 576*m.b9*m.b12*m.b18*m.b21 + 576*m.b9*m.b12*m.b19*m.b22 + 512*m.b9*m.b12
                       *m.b20*m.b23 + 448*m.b9*m.b12*m.b21*m.b24 + 384*m.b9*m.b12*m.b22*m.b25 + 320*m.b9*m.b12*m.b23*
                       m.b26 + 256*m.b9*m.b12*m.b24*m.b27 + 192*m.b9*m.b12*m.b25*m.b28 + 128*m.b9*m.b12*m.b26*m.b29 + 64
                       *m.b9*m.b12*m.b27*m.b30 + 64*m.b9*m.b13*m.b14*m.b18 + 64*m.b9*m.b13*m.b15*m.b19 + 64*m.b9*m.b13*
                       m.b16*m.b20 + 576*m.b9*m.b13*m.b17*m.b21 + 576*m.b9*m.b13*m.b18*m.b22 + 512*m.b9*m.b13*m.b19*
                       m.b23 + 448*m.b9*m.b13*m.b20*m.b24 + 384*m.b9*m.b13*m.b21*m.b25 + 320*m.b9*m.b13*m.b22*m.b26 + 
                       256*m.b9*m.b13*m.b23*m.b27 + 192*m.b9*m.b13*m.b24*m.b28 + 128*m.b9*m.b13*m.b25*m.b29 + 64*m.b9*
                       m.b13*m.b26*m.b30 + 64*m.b9*m.b14*m.b15*m.b20 + 576*m.b9*m.b14*m.b16*m.b21 + 576*m.b9*m.b14*m.b17
                       *m.b22 + 512*m.b9*m.b14*m.b18*m.b23 + 448*m.b9*m.b14*m.b19*m.b24 + 384*m.b9*m.b14*m.b20*m.b25 + 
                       320*m.b9*m.b14*m.b21*m.b26 + 256*m.b9*m.b14*m.b22*m.b27 + 192*m.b9*m.b14*m.b23*m.b28 + 128*m.b9*
                       m.b14*m.b24*m.b29 + 64*m.b9*m.b14*m.b25*m.b30 + 576*m.b9*m.b15*m.b16*m.b22 + 512*m.b9*m.b15*m.b17
                       *m.b23 + 448*m.b9*m.b15*m.b18*m.b24 + 384*m.b9*m.b15*m.b19*m.b25 + 320*m.b9*m.b15*m.b20*m.b26 + 
                       256*m.b9*m.b15*m.b21*m.b27 + 192*m.b9*m.b15*m.b22*m.b28 + 128*m.b9*m.b15*m.b23*m.b29 + 64*m.b9*
                       m.b15*m.b24*m.b30 + 448*m.b9*m.b16*m.b17*m.b24 + 384*m.b9*m.b16*m.b18*m.b25 + 320*m.b9*m.b16*
                       m.b19*m.b26 + 256*m.b9*m.b16*m.b20*m.b27 + 192*m.b9*m.b16*m.b21*m.b28 + 128*m.b9*m.b16*m.b22*
                       m.b29 + 64*m.b9*m.b16*m.b23*m.b30 + 320*m.b9*m.b17*m.b18*m.b26 + 256*m.b9*m.b17*m.b19*m.b27 + 192
                       *m.b9*m.b17*m.b20*m.b28 + 128*m.b9*m.b17*m.b21*m.b29 + 64*m.b9*m.b17*m.b22*m.b30 + 192*m.b9*m.b18
                       *m.b19*m.b28 + 128*m.b9*m.b18*m.b20*m.b29 + 64*m.b9*m.b18*m.b21*m.b30 + 64*m.b9*m.b19*m.b20*m.b30
                        + 64*m.b10*m.b11*m.b12*m.b13 + 64*m.b10*m.b11*m.b13*m.b14 + 64*m.b10*m.b11*m.b14*m.b15 + 64*
                       m.b10*m.b11*m.b15*m.b16 + 64*m.b10*m.b11*m.b16*m.b17 + 64*m.b10*m.b11*m.b17*m.b18 + 64*m.b10*
                       m.b11*m.b18*m.b19 + 64*m.b10*m.b11*m.b19*m.b20 + 64*m.b10*m.b11*m.b20*m.b21 + 576*m.b10*m.b11*
                       m.b21*m.b22 + 512*m.b10*m.b11*m.b22*m.b23 + 448*m.b10*m.b11*m.b23*m.b24 + 384*m.b10*m.b11*m.b24*
                       m.b25 + 320*m.b10*m.b11*m.b25*m.b26 + 256*m.b10*m.b11*m.b26*m.b27 + 192*m.b10*m.b11*m.b27*m.b28
                        + 128*m.b10*m.b11*m.b28*m.b29 + 64*m.b10*m.b11*m.b29*m.b30 + 64*m.b10*m.b12*m.b13*m.b15 + 64*
                       m.b10*m.b12*m.b14*m.b16 + 64*m.b10*m.b12*m.b15*m.b17 + 64*m.b10*m.b12*m.b16*m.b18 + 64*m.b10*
                       m.b12*m.b17*m.b19 + 64*m.b10*m.b12*m.b18*m.b20 + 64*m.b10*m.b12*m.b19*m.b21 + 576*m.b10*m.b12*
                       m.b20*m.b22 + 512*m.b10*m.b12*m.b21*m.b23 + 448*m.b10*m.b12*m.b22*m.b24 + 384*m.b10*m.b12*m.b23*
                       m.b25 + 320*m.b10*m.b12*m.b24*m.b26 + 256*m.b10*m.b12*m.b25*m.b27 + 192*m.b10*m.b12*m.b26*m.b28
                        + 128*m.b10*m.b12*m.b27*m.b29 + 64*m.b10*m.b12*m.b28*m.b30 + 64*m.b10*m.b13*m.b14*m.b17 + 64*
                       m.b10*m.b13*m.b15*m.b18 + 64*m.b10*m.b13*m.b16*m.b19 + 64*m.b10*m.b13*m.b17*m.b20 + 64*m.b10*
                       m.b13*m.b18*m.b21 + 576*m.b10*m.b13*m.b19*m.b22 + 512*m.b10*m.b13*m.b20*m.b23 + 448*m.b10*m.b13*
                       m.b21*m.b24 + 384*m.b10*m.b13*m.b22*m.b25 + 320*m.b10*m.b13*m.b23*m.b26 + 256*m.b10*m.b13*m.b24*
                       m.b27 + 192*m.b10*m.b13*m.b25*m.b28 + 128*m.b10*m.b13*m.b26*m.b29 + 64*m.b10*m.b13*m.b27*m.b30 + 
                       64*m.b10*m.b14*m.b15*m.b19 + 64*m.b10*m.b14*m.b16*m.b20 + 64*m.b10*m.b14*m.b17*m.b21 + 576*m.b10*
                       m.b14*m.b18*m.b22 + 512*m.b10*m.b14*m.b19*m.b23 + 448*m.b10*m.b14*m.b20*m.b24 + 384*m.b10*m.b14*
                       m.b21*m.b25 + 320*m.b10*m.b14*m.b22*m.b26 + 256*m.b10*m.b14*m.b23*m.b27 + 192*m.b10*m.b14*m.b24*
                       m.b28 + 128*m.b10*m.b14*m.b25*m.b29 + 64*m.b10*m.b14*m.b26*m.b30 + 64*m.b10*m.b15*m.b16*m.b21 + 
                       576*m.b10*m.b15*m.b17*m.b22 + 512*m.b10*m.b15*m.b18*m.b23 + 448*m.b10*m.b15*m.b19*m.b24 + 384*
                       m.b10*m.b15*m.b20*m.b25 + 320*m.b10*m.b15*m.b21*m.b26 + 256*m.b10*m.b15*m.b22*m.b27 + 192*m.b10*
                       m.b15*m.b23*m.b28 + 128*m.b10*m.b15*m.b24*m.b29 + 64*m.b10*m.b15*m.b25*m.b30 + 512*m.b10*m.b16*
                       m.b17*m.b23 + 448*m.b10*m.b16*m.b18*m.b24 + 384*m.b10*m.b16*m.b19*m.b25 + 320*m.b10*m.b16*m.b20*
                       m.b26 + 256*m.b10*m.b16*m.b21*m.b27 + 192*m.b10*m.b16*m.b22*m.b28 + 128*m.b10*m.b16*m.b23*m.b29
                        + 64*m.b10*m.b16*m.b24*m.b30 + 384*m.b10*m.b17*m.b18*m.b25 + 320*m.b10*m.b17*m.b19*m.b26 + 256*
                       m.b10*m.b17*m.b20*m.b27 + 192*m.b10*m.b17*m.b21*m.b28 + 128*m.b10*m.b17*m.b22*m.b29 + 64*m.b10*
                       m.b17*m.b23*m.b30 + 256*m.b10*m.b18*m.b19*m.b27 + 192*m.b10*m.b18*m.b20*m.b28 + 128*m.b10*m.b18*
                       m.b21*m.b29 + 64*m.b10*m.b18*m.b22*m.b30 + 128*m.b10*m.b19*m.b20*m.b29 + 64*m.b10*m.b19*m.b21*
                       m.b30 + 64*m.b11*m.b12*m.b13*m.b14 + 64*m.b11*m.b12*m.b14*m.b15 + 64*m.b11*m.b12*m.b15*m.b16 + 64
                       *m.b11*m.b12*m.b16*m.b17 + 64*m.b11*m.b12*m.b17*m.b18 + 64*m.b11*m.b12*m.b18*m.b19 + 64*m.b11*
                       m.b12*m.b19*m.b20 + 64*m.b11*m.b12*m.b20*m.b21 + 64*m.b11*m.b12*m.b21*m.b22 + 512*m.b11*m.b12*
                       m.b22*m.b23 + 448*m.b11*m.b12*m.b23*m.b24 + 384*m.b11*m.b12*m.b24*m.b25 + 320*m.b11*m.b12*m.b25*
                       m.b26 + 256*m.b11*m.b12*m.b26*m.b27 + 192*m.b11*m.b12*m.b27*m.b28 + 128*m.b11*m.b12*m.b28*m.b29
                        + 64*m.b11*m.b12*m.b29*m.b30 + 64*m.b11*m.b13*m.b14*m.b16 + 64*m.b11*m.b13*m.b15*m.b17 + 64*
                       m.b11*m.b13*m.b16*m.b18 + 64*m.b11*m.b13*m.b17*m.b19 + 64*m.b11*m.b13*m.b18*m.b20 + 64*m.b11*
                       m.b13*m.b19*m.b21 + 64*m.b11*m.b13*m.b20*m.b22 + 512*m.b11*m.b13*m.b21*m.b23 + 448*m.b11*m.b13*
                       m.b22*m.b24 + 384*m.b11*m.b13*m.b23*m.b25 + 320*m.b11*m.b13*m.b24*m.b26 + 256*m.b11*m.b13*m.b25*
                       m.b27 + 192*m.b11*m.b13*m.b26*m.b28 + 128*m.b11*m.b13*m.b27*m.b29 + 64*m.b11*m.b13*m.b28*m.b30 + 
                       64*m.b11*m.b14*m.b15*m.b18 + 64*m.b11*m.b14*m.b16*m.b19 + 64*m.b11*m.b14*m.b17*m.b20 + 64*m.b11*
                       m.b14*m.b18*m.b21 + 64*m.b11*m.b14*m.b19*m.b22 + 512*m.b11*m.b14*m.b20*m.b23 + 448*m.b11*m.b14*
                       m.b21*m.b24 + 384*m.b11*m.b14*m.b22*m.b25 + 320*m.b11*m.b14*m.b23*m.b26 + 256*m.b11*m.b14*m.b24*
                       m.b27 + 192*m.b11*m.b14*m.b25*m.b28 + 128*m.b11*m.b14*m.b26*m.b29 + 64*m.b11*m.b14*m.b27*m.b30 + 
                       64*m.b11*m.b15*m.b16*m.b20 + 64*m.b11*m.b15*m.b17*m.b21 + 64*m.b11*m.b15*m.b18*m.b22 + 512*m.b11*
                       m.b15*m.b19*m.b23 + 448*m.b11*m.b15*m.b20*m.b24 + 384*m.b11*m.b15*m.b21*m.b25 + 320*m.b11*m.b15*
                       m.b22*m.b26 + 256*m.b11*m.b15*m.b23*m.b27 + 192*m.b11*m.b15*m.b24*m.b28 + 128*m.b11*m.b15*m.b25*
                       m.b29 + 64*m.b11*m.b15*m.b26*m.b30 + 64*m.b11*m.b16*m.b17*m.b22 + 512*m.b11*m.b16*m.b18*m.b23 + 
                       448*m.b11*m.b16*m.b19*m.b24 + 384*m.b11*m.b16*m.b20*m.b25 + 320*m.b11*m.b16*m.b21*m.b26 + 256*
                       m.b11*m.b16*m.b22*m.b27 + 192*m.b11*m.b16*m.b23*m.b28 + 128*m.b11*m.b16*m.b24*m.b29 + 64*m.b11*
                       m.b16*m.b25*m.b30 + 448*m.b11*m.b17*m.b18*m.b24 + 384*m.b11*m.b17*m.b19*m.b25 + 320*m.b11*m.b17*
                       m.b20*m.b26 + 256*m.b11*m.b17*m.b21*m.b27 + 192*m.b11*m.b17*m.b22*m.b28 + 128*m.b11*m.b17*m.b23*
                       m.b29 + 64*m.b11*m.b17*m.b24*m.b30 + 320*m.b11*m.b18*m.b19*m.b26 + 256*m.b11*m.b18*m.b20*m.b27 + 
                       192*m.b11*m.b18*m.b21*m.b28 + 128*m.b11*m.b18*m.b22*m.b29 + 64*m.b11*m.b18*m.b23*m.b30 + 192*
                       m.b11*m.b19*m.b20*m.b28 + 128*m.b11*m.b19*m.b21*m.b29 + 64*m.b11*m.b19*m.b22*m.b30 + 64*m.b11*
                       m.b20*m.b21*m.b30 + 64*m.b12*m.b13*m.b14*m.b15 + 64*m.b12*m.b13*m.b15*m.b16 + 64*m.b12*m.b13*
                       m.b16*m.b17 + 64*m.b12*m.b13*m.b17*m.b18 + 64*m.b12*m.b13*m.b18*m.b19 + 64*m.b12*m.b13*m.b19*
                       m.b20 + 64*m.b12*m.b13*m.b20*m.b21 + 64*m.b12*m.b13*m.b21*m.b22 + 64*m.b12*m.b13*m.b22*m.b23 + 
                       448*m.b12*m.b13*m.b23*m.b24 + 384*m.b12*m.b13*m.b24*m.b25 + 320*m.b12*m.b13*m.b25*m.b26 + 256*
                       m.b12*m.b13*m.b26*m.b27 + 192*m.b12*m.b13*m.b27*m.b28 + 128*m.b12*m.b13*m.b28*m.b29 + 64*m.b12*
                       m.b13*m.b29*m.b30 + 64*m.b12*m.b14*m.b15*m.b17 + 64*m.b12*m.b14*m.b16*m.b18 + 64*m.b12*m.b14*
                       m.b17*m.b19 + 64*m.b12*m.b14*m.b18*m.b20 + 64*m.b12*m.b14*m.b19*m.b21 + 64*m.b12*m.b14*m.b20*
                       m.b22 + 64*m.b12*m.b14*m.b21*m.b23 + 448*m.b12*m.b14*m.b22*m.b24 + 384*m.b12*m.b14*m.b23*m.b25 + 
                       320*m.b12*m.b14*m.b24*m.b26 + 256*m.b12*m.b14*m.b25*m.b27 + 192*m.b12*m.b14*m.b26*m.b28 + 128*
                       m.b12*m.b14*m.b27*m.b29 + 64*m.b12*m.b14*m.b28*m.b30 + 64*m.b12*m.b15*m.b16*m.b19 + 64*m.b12*
                       m.b15*m.b17*m.b20 + 64*m.b12*m.b15*m.b18*m.b21 + 64*m.b12*m.b15*m.b19*m.b22 + 64*m.b12*m.b15*
                       m.b20*m.b23 + 448*m.b12*m.b15*m.b21*m.b24 + 384*m.b12*m.b15*m.b22*m.b25 + 320*m.b12*m.b15*m.b23*
                       m.b26 + 256*m.b12*m.b15*m.b24*m.b27 + 192*m.b12*m.b15*m.b25*m.b28 + 128*m.b12*m.b15*m.b26*m.b29
                        + 64*m.b12*m.b15*m.b27*m.b30 + 64*m.b12*m.b16*m.b17*m.b21 + 64*m.b12*m.b16*m.b18*m.b22 + 64*
                       m.b12*m.b16*m.b19*m.b23 + 448*m.b12*m.b16*m.b20*m.b24 + 384*m.b12*m.b16*m.b21*m.b25 + 320*m.b12*
                       m.b16*m.b22*m.b26 + 256*m.b12*m.b16*m.b23*m.b27 + 192*m.b12*m.b16*m.b24*m.b28 + 128*m.b12*m.b16*
                       m.b25*m.b29 + 64*m.b12*m.b16*m.b26*m.b30 + 64*m.b12*m.b17*m.b18*m.b23 + 448*m.b12*m.b17*m.b19*
                       m.b24 + 384*m.b12*m.b17*m.b20*m.b25 + 320*m.b12*m.b17*m.b21*m.b26 + 256*m.b12*m.b17*m.b22*m.b27
                        + 192*m.b12*m.b17*m.b23*m.b28 + 128*m.b12*m.b17*m.b24*m.b29 + 64*m.b12*m.b17*m.b25*m.b30 + 384*
                       m.b12*m.b18*m.b19*m.b25 + 320*m.b12*m.b18*m.b20*m.b26 + 256*m.b12*m.b18*m.b21*m.b27 + 192*m.b12*
                       m.b18*m.b22*m.b28 + 128*m.b12*m.b18*m.b23*m.b29 + 64*m.b12*m.b18*m.b24*m.b30 + 256*m.b12*m.b19*
                       m.b20*m.b27 + 192*m.b12*m.b19*m.b21*m.b28 + 128*m.b12*m.b19*m.b22*m.b29 + 64*m.b12*m.b19*m.b23*
                       m.b30 + 128*m.b12*m.b20*m.b21*m.b29 + 64*m.b12*m.b20*m.b22*m.b30 + 64*m.b13*m.b14*m.b15*m.b16 + 
                       64*m.b13*m.b14*m.b16*m.b17 + 64*m.b13*m.b14*m.b17*m.b18 + 64*m.b13*m.b14*m.b18*m.b19 + 64*m.b13*
                       m.b14*m.b19*m.b20 + 64*m.b13*m.b14*m.b20*m.b21 + 64*m.b13*m.b14*m.b21*m.b22 + 64*m.b13*m.b14*
                       m.b22*m.b23 + 64*m.b13*m.b14*m.b23*m.b24 + 384*m.b13*m.b14*m.b24*m.b25 + 320*m.b13*m.b14*m.b25*
                       m.b26 + 256*m.b13*m.b14*m.b26*m.b27 + 192*m.b13*m.b14*m.b27*m.b28 + 128*m.b13*m.b14*m.b28*m.b29
                        + 64*m.b13*m.b14*m.b29*m.b30 + 64*m.b13*m.b15*m.b16*m.b18 + 64*m.b13*m.b15*m.b17*m.b19 + 64*
                       m.b13*m.b15*m.b18*m.b20 + 64*m.b13*m.b15*m.b19*m.b21 + 64*m.b13*m.b15*m.b20*m.b22 + 64*m.b13*
                       m.b15*m.b21*m.b23 + 64*m.b13*m.b15*m.b22*m.b24 + 384*m.b13*m.b15*m.b23*m.b25 + 320*m.b13*m.b15*
                       m.b24*m.b26 + 256*m.b13*m.b15*m.b25*m.b27 + 192*m.b13*m.b15*m.b26*m.b28 + 128*m.b13*m.b15*m.b27*
                       m.b29 + 64*m.b13*m.b15*m.b28*m.b30 + 64*m.b13*m.b16*m.b17*m.b20 + 64*m.b13*m.b16*m.b18*m.b21 + 64
                       *m.b13*m.b16*m.b19*m.b22 + 64*m.b13*m.b16*m.b20*m.b23 + 64*m.b13*m.b16*m.b21*m.b24 + 384*m.b13*
                       m.b16*m.b22*m.b25 + 320*m.b13*m.b16*m.b23*m.b26 + 256*m.b13*m.b16*m.b24*m.b27 + 192*m.b13*m.b16*
                       m.b25*m.b28 + 128*m.b13*m.b16*m.b26*m.b29 + 64*m.b13*m.b16*m.b27*m.b30 + 64*m.b13*m.b17*m.b18*
                       m.b22 + 64*m.b13*m.b17*m.b19*m.b23 + 64*m.b13*m.b17*m.b20*m.b24 + 384*m.b13*m.b17*m.b21*m.b25 + 
                       320*m.b13*m.b17*m.b22*m.b26 + 256*m.b13*m.b17*m.b23*m.b27 + 192*m.b13*m.b17*m.b24*m.b28 + 128*
                       m.b13*m.b17*m.b25*m.b29 + 64*m.b13*m.b17*m.b26*m.b30 + 64*m.b13*m.b18*m.b19*m.b24 + 384*m.b13*
                       m.b18*m.b20*m.b25 + 320*m.b13*m.b18*m.b21*m.b26 + 256*m.b13*m.b18*m.b22*m.b27 + 192*m.b13*m.b18*
                       m.b23*m.b28 + 128*m.b13*m.b18*m.b24*m.b29 + 64*m.b13*m.b18*m.b25*m.b30 + 320*m.b13*m.b19*m.b20*
                       m.b26 + 256*m.b13*m.b19*m.b21*m.b27 + 192*m.b13*m.b19*m.b22*m.b28 + 128*m.b13*m.b19*m.b23*m.b29
                        + 64*m.b13*m.b19*m.b24*m.b30 + 192*m.b13*m.b20*m.b21*m.b28 + 128*m.b13*m.b20*m.b22*m.b29 + 64*
                       m.b13*m.b20*m.b23*m.b30 + 64*m.b13*m.b21*m.b22*m.b30 + 64*m.b14*m.b15*m.b16*m.b17 + 64*m.b14*
                       m.b15*m.b17*m.b18 + 64*m.b14*m.b15*m.b18*m.b19 + 64*m.b14*m.b15*m.b19*m.b20 + 64*m.b14*m.b15*
                       m.b20*m.b21 + 64*m.b14*m.b15*m.b21*m.b22 + 64*m.b14*m.b15*m.b22*m.b23 + 64*m.b14*m.b15*m.b23*
                       m.b24 + 64*m.b14*m.b15*m.b24*m.b25 + 320*m.b14*m.b15*m.b25*m.b26 + 256*m.b14*m.b15*m.b26*m.b27 + 
                       192*m.b14*m.b15*m.b27*m.b28 + 128*m.b14*m.b15*m.b28*m.b29 + 64*m.b14*m.b15*m.b29*m.b30 + 64*m.b14
                       *m.b16*m.b17*m.b19 + 64*m.b14*m.b16*m.b18*m.b20 + 64*m.b14*m.b16*m.b19*m.b21 + 64*m.b14*m.b16*
                       m.b20*m.b22 + 64*m.b14*m.b16*m.b21*m.b23 + 64*m.b14*m.b16*m.b22*m.b24 + 64*m.b14*m.b16*m.b23*
                       m.b25 + 320*m.b14*m.b16*m.b24*m.b26 + 256*m.b14*m.b16*m.b25*m.b27 + 192*m.b14*m.b16*m.b26*m.b28
                        + 128*m.b14*m.b16*m.b27*m.b29 + 64*m.b14*m.b16*m.b28*m.b30 + 64*m.b14*m.b17*m.b18*m.b21 + 64*
                       m.b14*m.b17*m.b19*m.b22 + 64*m.b14*m.b17*m.b20*m.b23 + 64*m.b14*m.b17*m.b21*m.b24 + 64*m.b14*
                       m.b17*m.b22*m.b25 + 320*m.b14*m.b17*m.b23*m.b26 + 256*m.b14*m.b17*m.b24*m.b27 + 192*m.b14*m.b17*
                       m.b25*m.b28 + 128*m.b14*m.b17*m.b26*m.b29 + 64*m.b14*m.b17*m.b27*m.b30 + 64*m.b14*m.b18*m.b19*
                       m.b23 + 64*m.b14*m.b18*m.b20*m.b24 + 64*m.b14*m.b18*m.b21*m.b25 + 320*m.b14*m.b18*m.b22*m.b26 + 
                       256*m.b14*m.b18*m.b23*m.b27 + 192*m.b14*m.b18*m.b24*m.b28 + 128*m.b14*m.b18*m.b25*m.b29 + 64*
                       m.b14*m.b18*m.b26*m.b30 + 64*m.b14*m.b19*m.b20*m.b25 + 320*m.b14*m.b19*m.b21*m.b26 + 256*m.b14*
                       m.b19*m.b22*m.b27 + 192*m.b14*m.b19*m.b23*m.b28 + 128*m.b14*m.b19*m.b24*m.b29 + 64*m.b14*m.b19*
                       m.b25*m.b30 + 256*m.b14*m.b20*m.b21*m.b27 + 192*m.b14*m.b20*m.b22*m.b28 + 128*m.b14*m.b20*m.b23*
                       m.b29 + 64*m.b14*m.b20*m.b24*m.b30 + 128*m.b14*m.b21*m.b22*m.b29 + 64*m.b14*m.b21*m.b23*m.b30 + 
                       64*m.b15*m.b16*m.b17*m.b18 + 64*m.b15*m.b16*m.b18*m.b19 + 64*m.b15*m.b16*m.b19*m.b20 + 64*m.b15*
                       m.b16*m.b20*m.b21 + 64*m.b15*m.b16*m.b21*m.b22 + 64*m.b15*m.b16*m.b22*m.b23 + 64*m.b15*m.b16*
                       m.b23*m.b24 + 64*m.b15*m.b16*m.b24*m.b25 + 64*m.b15*m.b16*m.b25*m.b26 + 256*m.b15*m.b16*m.b26*
                       m.b27 + 192*m.b15*m.b16*m.b27*m.b28 + 128*m.b15*m.b16*m.b28*m.b29 + 64*m.b15*m.b16*m.b29*m.b30 + 
                       64*m.b15*m.b17*m.b18*m.b20 + 64*m.b15*m.b17*m.b19*m.b21 + 64*m.b15*m.b17*m.b20*m.b22 + 64*m.b15*
                       m.b17*m.b21*m.b23 + 64*m.b15*m.b17*m.b22*m.b24 + 64*m.b15*m.b17*m.b23*m.b25 + 64*m.b15*m.b17*
                       m.b24*m.b26 + 256*m.b15*m.b17*m.b25*m.b27 + 192*m.b15*m.b17*m.b26*m.b28 + 128*m.b15*m.b17*m.b27*
                       m.b29 + 64*m.b15*m.b17*m.b28*m.b30 + 64*m.b15*m.b18*m.b19*m.b22 + 64*m.b15*m.b18*m.b20*m.b23 + 64
                       *m.b15*m.b18*m.b21*m.b24 + 64*m.b15*m.b18*m.b22*m.b25 + 64*m.b15*m.b18*m.b23*m.b26 + 256*m.b15*
                       m.b18*m.b24*m.b27 + 192*m.b15*m.b18*m.b25*m.b28 + 128*m.b15*m.b18*m.b26*m.b29 + 64*m.b15*m.b18*
                       m.b27*m.b30 + 64*m.b15*m.b19*m.b20*m.b24 + 64*m.b15*m.b19*m.b21*m.b25 + 64*m.b15*m.b19*m.b22*
                       m.b26 + 256*m.b15*m.b19*m.b23*m.b27 + 192*m.b15*m.b19*m.b24*m.b28 + 128*m.b15*m.b19*m.b25*m.b29
                        + 64*m.b15*m.b19*m.b26*m.b30 + 64*m.b15*m.b20*m.b21*m.b26 + 256*m.b15*m.b20*m.b22*m.b27 + 192*
                       m.b15*m.b20*m.b23*m.b28 + 128*m.b15*m.b20*m.b24*m.b29 + 64*m.b15*m.b20*m.b25*m.b30 + 192*m.b15*
                       m.b21*m.b22*m.b28 + 128*m.b15*m.b21*m.b23*m.b29 + 64*m.b15*m.b21*m.b24*m.b30 + 64*m.b15*m.b22*
                       m.b23*m.b30 + 64*m.b16*m.b17*m.b18*m.b19 + 64*m.b16*m.b17*m.b19*m.b20 + 64*m.b16*m.b17*m.b20*
                       m.b21 + 64*m.b16*m.b17*m.b21*m.b22 + 64*m.b16*m.b17*m.b22*m.b23 + 64*m.b16*m.b17*m.b23*m.b24 + 64
                       *m.b16*m.b17*m.b24*m.b25 + 64*m.b16*m.b17*m.b25*m.b26 + 64*m.b16*m.b17*m.b26*m.b27 + 192*m.b16*
                       m.b17*m.b27*m.b28 + 128*m.b16*m.b17*m.b28*m.b29 + 64*m.b16*m.b17*m.b29*m.b30 + 64*m.b16*m.b18*
                       m.b19*m.b21 + 64*m.b16*m.b18*m.b20*m.b22 + 64*m.b16*m.b18*m.b21*m.b23 + 64*m.b16*m.b18*m.b22*
                       m.b24 + 64*m.b16*m.b18*m.b23*m.b25 + 64*m.b16*m.b18*m.b24*m.b26 + 64*m.b16*m.b18*m.b25*m.b27 + 
                       192*m.b16*m.b18*m.b26*m.b28 + 128*m.b16*m.b18*m.b27*m.b29 + 64*m.b16*m.b18*m.b28*m.b30 + 64*m.b16
                       *m.b19*m.b20*m.b23 + 64*m.b16*m.b19*m.b21*m.b24 + 64*m.b16*m.b19*m.b22*m.b25 + 64*m.b16*m.b19*
                       m.b23*m.b26 + 64*m.b16*m.b19*m.b24*m.b27 + 192*m.b16*m.b19*m.b25*m.b28 + 128*m.b16*m.b19*m.b26*
                       m.b29 + 64*m.b16*m.b19*m.b27*m.b30 + 64*m.b16*m.b20*m.b21*m.b25 + 64*m.b16*m.b20*m.b22*m.b26 + 64
                       *m.b16*m.b20*m.b23*m.b27 + 192*m.b16*m.b20*m.b24*m.b28 + 128*m.b16*m.b20*m.b25*m.b29 + 64*m.b16*
                       m.b20*m.b26*m.b30 + 64*m.b16*m.b21*m.b22*m.b27 + 192*m.b16*m.b21*m.b23*m.b28 + 128*m.b16*m.b21*
                       m.b24*m.b29 + 64*m.b16*m.b21*m.b25*m.b30 + 128*m.b16*m.b22*m.b23*m.b29 + 64*m.b16*m.b22*m.b24*
                       m.b30 + 64*m.b17*m.b18*m.b19*m.b20 + 64*m.b17*m.b18*m.b20*m.b21 + 64*m.b17*m.b18*m.b21*m.b22 + 64
                       *m.b17*m.b18*m.b22*m.b23 + 64*m.b17*m.b18*m.b23*m.b24 + 64*m.b17*m.b18*m.b24*m.b25 + 64*m.b17*
                       m.b18*m.b25*m.b26 + 64*m.b17*m.b18*m.b26*m.b27 + 64*m.b17*m.b18*m.b27*m.b28 + 128*m.b17*m.b18*
                       m.b28*m.b29 + 64*m.b17*m.b18*m.b29*m.b30 + 64*m.b17*m.b19*m.b20*m.b22 + 64*m.b17*m.b19*m.b21*
                       m.b23 + 64*m.b17*m.b19*m.b22*m.b24 + 64*m.b17*m.b19*m.b23*m.b25 + 64*m.b17*m.b19*m.b24*m.b26 + 64
                       *m.b17*m.b19*m.b25*m.b27 + 64*m.b17*m.b19*m.b26*m.b28 + 128*m.b17*m.b19*m.b27*m.b29 + 64*m.b17*
                       m.b19*m.b28*m.b30 + 64*m.b17*m.b20*m.b21*m.b24 + 64*m.b17*m.b20*m.b22*m.b25 + 64*m.b17*m.b20*
                       m.b23*m.b26 + 64*m.b17*m.b20*m.b24*m.b27 + 64*m.b17*m.b20*m.b25*m.b28 + 128*m.b17*m.b20*m.b26*
                       m.b29 + 64*m.b17*m.b20*m.b27*m.b30 + 64*m.b17*m.b21*m.b22*m.b26 + 64*m.b17*m.b21*m.b23*m.b27 + 64
                       *m.b17*m.b21*m.b24*m.b28 + 128*m.b17*m.b21*m.b25*m.b29 + 64*m.b17*m.b21*m.b26*m.b30 + 64*m.b17*
                       m.b22*m.b23*m.b28 + 128*m.b17*m.b22*m.b24*m.b29 + 64*m.b17*m.b22*m.b25*m.b30 + 64*m.b17*m.b23*
                       m.b24*m.b30 + 64*m.b18*m.b19*m.b20*m.b21 + 64*m.b18*m.b19*m.b21*m.b22 + 64*m.b18*m.b19*m.b22*
                       m.b23 + 64*m.b18*m.b19*m.b23*m.b24 + 64*m.b18*m.b19*m.b24*m.b25 + 64*m.b18*m.b19*m.b25*m.b26 + 64
                       *m.b18*m.b19*m.b26*m.b27 + 64*m.b18*m.b19*m.b27*m.b28 + 64*m.b18*m.b19*m.b28*m.b29 + 64*m.b18*
                       m.b19*m.b29*m.b30 + 64*m.b18*m.b20*m.b21*m.b23 + 64*m.b18*m.b20*m.b22*m.b24 + 64*m.b18*m.b20*
                       m.b23*m.b25 + 64*m.b18*m.b20*m.b24*m.b26 + 64*m.b18*m.b20*m.b25*m.b27 + 64*m.b18*m.b20*m.b26*
                       m.b28 + 64*m.b18*m.b20*m.b27*m.b29 + 64*m.b18*m.b20*m.b28*m.b30 + 64*m.b18*m.b21*m.b22*m.b25 + 64
                       *m.b18*m.b21*m.b23*m.b26 + 64*m.b18*m.b21*m.b24*m.b27 + 64*m.b18*m.b21*m.b25*m.b28 + 64*m.b18*
                       m.b21*m.b26*m.b29 + 64*m.b18*m.b21*m.b27*m.b30 + 64*m.b18*m.b22*m.b23*m.b27 + 64*m.b18*m.b22*
                       m.b24*m.b28 + 64*m.b18*m.b22*m.b25*m.b29 + 64*m.b18*m.b22*m.b26*m.b30 + 64*m.b18*m.b23*m.b24*
                       m.b29 + 64*m.b18*m.b23*m.b25*m.b30 + 64*m.b19*m.b20*m.b21*m.b22 + 64*m.b19*m.b20*m.b22*m.b23 + 64
                       *m.b19*m.b20*m.b23*m.b24 + 64*m.b19*m.b20*m.b24*m.b25 + 64*m.b19*m.b20*m.b25*m.b26 + 64*m.b19*
                       m.b20*m.b26*m.b27 + 64*m.b19*m.b20*m.b27*m.b28 + 64*m.b19*m.b20*m.b28*m.b29 + 64*m.b19*m.b20*
                       m.b29*m.b30 + 64*m.b19*m.b21*m.b22*m.b24 + 64*m.b19*m.b21*m.b23*m.b25 + 64*m.b19*m.b21*m.b24*
                       m.b26 + 64*m.b19*m.b21*m.b25*m.b27 + 64*m.b19*m.b21*m.b26*m.b28 + 64*m.b19*m.b21*m.b27*m.b29 + 64
                       *m.b19*m.b21*m.b28*m.b30 + 64*m.b19*m.b22*m.b23*m.b26 + 64*m.b19*m.b22*m.b24*m.b27 + 64*m.b19*
                       m.b22*m.b25*m.b28 + 64*m.b19*m.b22*m.b26*m.b29 + 64*m.b19*m.b22*m.b27*m.b30 + 64*m.b19*m.b23*
                       m.b24*m.b28 + 64*m.b19*m.b23*m.b25*m.b29 + 64*m.b19*m.b23*m.b26*m.b30 + 64*m.b19*m.b24*m.b25*
                       m.b30 + 64*m.b20*m.b21*m.b22*m.b23 + 64*m.b20*m.b21*m.b23*m.b24 + 64*m.b20*m.b21*m.b24*m.b25 + 64
                       *m.b20*m.b21*m.b25*m.b26 + 64*m.b20*m.b21*m.b26*m.b27 + 64*m.b20*m.b21*m.b27*m.b28 + 64*m.b20*
                       m.b21*m.b28*m.b29 + 64*m.b20*m.b21*m.b29*m.b30 + 64*m.b20*m.b22*m.b23*m.b25 + 64*m.b20*m.b22*
                       m.b24*m.b26 + 64*m.b20*m.b22*m.b25*m.b27 + 64*m.b20*m.b22*m.b26*m.b28 + 64*m.b20*m.b22*m.b27*
                       m.b29 + 64*m.b20*m.b22*m.b28*m.b30 + 64*m.b20*m.b23*m.b24*m.b27 + 64*m.b20*m.b23*m.b25*m.b28 + 64
                       *m.b20*m.b23*m.b26*m.b29 + 64*m.b20*m.b23*m.b27*m.b30 + 64*m.b20*m.b24*m.b25*m.b29 + 64*m.b20*
                       m.b24*m.b26*m.b30 + 64*m.b21*m.b22*m.b23*m.b24 + 64*m.b21*m.b22*m.b24*m.b25 + 64*m.b21*m.b22*
                       m.b25*m.b26 + 64*m.b21*m.b22*m.b26*m.b27 + 64*m.b21*m.b22*m.b27*m.b28 + 64*m.b21*m.b22*m.b28*
                       m.b29 + 64*m.b21*m.b22*m.b29*m.b30 + 64*m.b21*m.b23*m.b24*m.b26 + 64*m.b21*m.b23*m.b25*m.b27 + 64
                       *m.b21*m.b23*m.b26*m.b28 + 64*m.b21*m.b23*m.b27*m.b29 + 64*m.b21*m.b23*m.b28*m.b30 + 64*m.b21*
                       m.b24*m.b25*m.b28 + 64*m.b21*m.b24*m.b26*m.b29 + 64*m.b21*m.b24*m.b27*m.b30 + 64*m.b21*m.b25*
                       m.b26*m.b30 + 64*m.b22*m.b23*m.b24*m.b25 + 64*m.b22*m.b23*m.b25*m.b26 + 64*m.b22*m.b23*m.b26*
                       m.b27 + 64*m.b22*m.b23*m.b27*m.b28 + 64*m.b22*m.b23*m.b28*m.b29 + 64*m.b22*m.b23*m.b29*m.b30 + 64
                       *m.b22*m.b24*m.b25*m.b27 + 64*m.b22*m.b24*m.b26*m.b28 + 64*m.b22*m.b24*m.b27*m.b29 + 64*m.b22*
                       m.b24*m.b28*m.b30 + 64*m.b22*m.b25*m.b26*m.b29 + 64*m.b22*m.b25*m.b27*m.b30 + 64*m.b23*m.b24*
                       m.b25*m.b26 + 64*m.b23*m.b24*m.b26*m.b27 + 64*m.b23*m.b24*m.b27*m.b28 + 64*m.b23*m.b24*m.b28*
                       m.b29 + 64*m.b23*m.b24*m.b29*m.b30 + 64*m.b23*m.b25*m.b26*m.b28 + 64*m.b23*m.b25*m.b27*m.b29 + 64
                       *m.b23*m.b25*m.b28*m.b30 + 64*m.b23*m.b26*m.b27*m.b30 + 64*m.b24*m.b25*m.b26*m.b27 + 64*m.b24*
                       m.b25*m.b27*m.b28 + 64*m.b24*m.b25*m.b28*m.b29 + 64*m.b24*m.b25*m.b29*m.b30 + 64*m.b24*m.b26*
                       m.b27*m.b29 + 64*m.b24*m.b26*m.b28*m.b30 + 64*m.b25*m.b26*m.b27*m.b28 + 64*m.b25*m.b26*m.b28*
                       m.b29 + 64*m.b25*m.b26*m.b29*m.b30 + 64*m.b25*m.b27*m.b28*m.b30 + 64*m.b26*m.b27*m.b28*m.b29 + 64
                       *m.b26*m.b27*m.b29*m.b30 + 64*m.b27*m.b28*m.b29*m.b30 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 
                       64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9
                        - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*m.b13 - 64*m.b1*
                       m.b2*m.b14 - 64*m.b1*m.b2*m.b15 - 64*m.b1*m.b2*m.b16 - 64*m.b1*m.b2*m.b17 - 64*m.b1*m.b2*m.b18 - 
                       64*m.b1*m.b2*m.b19 - 64*m.b1*m.b2*m.b20 - 64*m.b1*m.b2*m.b21 - 64*m.b1*m.b2*m.b22 - 64*m.b1*m.b2*
                       m.b23 - 64*m.b1*m.b2*m.b24 - 64*m.b1*m.b2*m.b25 - 64*m.b1*m.b2*m.b26 - 64*m.b1*m.b2*m.b27 - 64*
                       m.b1*m.b2*m.b28 - 64*m.b1*m.b2*m.b29 - 32*m.b1*m.b2*m.b30 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5
                        - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*
                       m.b10 - 64*m.b1*m.b3*m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 64*m.b1*m.b3*m.b14 - 64*
                       m.b1*m.b3*m.b15 - 64*m.b1*m.b3*m.b16 - 64*m.b1*m.b3*m.b17 - 64*m.b1*m.b3*m.b18 - 64*m.b1*m.b3*
                       m.b19 - 64*m.b1*m.b3*m.b20 - 64*m.b1*m.b3*m.b21 - 64*m.b1*m.b3*m.b22 - 64*m.b1*m.b3*m.b23 - 64*
                       m.b1*m.b3*m.b24 - 64*m.b1*m.b3*m.b25 - 64*m.b1*m.b3*m.b26 - 64*m.b1*m.b3*m.b27 - 64*m.b1*m.b3*
                       m.b28 - 32*m.b1*m.b3*m.b29 - 32*m.b1*m.b3*m.b30 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1
                       *m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64
                       *m.b1*m.b4*m.b12 - 64*m.b1*m.b4*m.b13 - 64*m.b1*m.b4*m.b14 - 64*m.b1*m.b4*m.b15 - 64*m.b1*m.b4*
                       m.b16 - 64*m.b1*m.b4*m.b17 - 64*m.b1*m.b4*m.b18 - 64*m.b1*m.b4*m.b19 - 64*m.b1*m.b4*m.b20 - 64*
                       m.b1*m.b4*m.b21 - 64*m.b1*m.b4*m.b22 - 64*m.b1*m.b4*m.b23 - 64*m.b1*m.b4*m.b24 - 64*m.b1*m.b4*
                       m.b25 - 64*m.b1*m.b4*m.b26 - 64*m.b1*m.b4*m.b27 - 32*m.b1*m.b4*m.b28 - 32*m.b1*m.b4*m.b29 - 32*
                       m.b1*m.b4*m.b30 - 64*m.b1*m.b5*m.b6 - 64*m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9
                        - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*m.b11 - 64*m.b1*m.b5*m.b12 - 64*m.b1*m.b5*m.b13 - 64*m.b1*
                       m.b5*m.b14 - 64*m.b1*m.b5*m.b15 - 64*m.b1*m.b5*m.b16 - 64*m.b1*m.b5*m.b17 - 64*m.b1*m.b5*m.b18 - 
                       64*m.b1*m.b5*m.b19 - 64*m.b1*m.b5*m.b20 - 64*m.b1*m.b5*m.b21 - 64*m.b1*m.b5*m.b22 - 64*m.b1*m.b5*
                       m.b23 - 64*m.b1*m.b5*m.b24 - 64*m.b1*m.b5*m.b25 - 64*m.b1*m.b5*m.b26 - 32*m.b1*m.b5*m.b27 - 32*
                       m.b1*m.b5*m.b28 - 32*m.b1*m.b5*m.b29 - 32*m.b1*m.b5*m.b30 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8
                        - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*m.b11 - 64*m.b1*m.b6*m.b12 - 64*m.b1*
                       m.b6*m.b13 - 64*m.b1*m.b6*m.b14 - 64*m.b1*m.b6*m.b15 - 64*m.b1*m.b6*m.b16 - 64*m.b1*m.b6*m.b17 - 
                       64*m.b1*m.b6*m.b18 - 64*m.b1*m.b6*m.b19 - 64*m.b1*m.b6*m.b20 - 64*m.b1*m.b6*m.b21 - 64*m.b1*m.b6*
                       m.b22 - 64*m.b1*m.b6*m.b23 - 64*m.b1*m.b6*m.b24 - 64*m.b1*m.b6*m.b25 - 32*m.b1*m.b6*m.b26 - 32*
                       m.b1*m.b6*m.b27 - 32*m.b1*m.b6*m.b28 - 32*m.b1*m.b6*m.b29 - 32*m.b1*m.b6*m.b30 - 64*m.b1*m.b7*
                       m.b8 - 64*m.b1*m.b7*m.b9 - 64*m.b1*m.b7*m.b10 - 64*m.b1*m.b7*m.b11 - 64*m.b1*m.b7*m.b12 - 32*m.b1
                       *m.b7*m.b13 - 64*m.b1*m.b7*m.b14 - 64*m.b1*m.b7*m.b15 - 64*m.b1*m.b7*m.b16 - 64*m.b1*m.b7*m.b17
                        - 64*m.b1*m.b7*m.b18 - 64*m.b1*m.b7*m.b19 - 64*m.b1*m.b7*m.b20 - 64*m.b1*m.b7*m.b21 - 64*m.b1*
                       m.b7*m.b22 - 64*m.b1*m.b7*m.b23 - 64*m.b1*m.b7*m.b24 - 32*m.b1*m.b7*m.b25 - 32*m.b1*m.b7*m.b26 - 
                       32*m.b1*m.b7*m.b27 - 32*m.b1*m.b7*m.b28 - 32*m.b1*m.b7*m.b29 - 32*m.b1*m.b7*m.b30 - 64*m.b1*m.b8*
                       m.b9 - 64*m.b1*m.b8*m.b10 - 64*m.b1*m.b8*m.b11 - 64*m.b1*m.b8*m.b12 - 64*m.b1*m.b8*m.b13 - 64*
                       m.b1*m.b8*m.b14 - 32*m.b1*m.b8*m.b15 - 64*m.b1*m.b8*m.b16 - 64*m.b1*m.b8*m.b17 - 64*m.b1*m.b8*
                       m.b18 - 64*m.b1*m.b8*m.b19 - 64*m.b1*m.b8*m.b20 - 64*m.b1*m.b8*m.b21 - 64*m.b1*m.b8*m.b22 - 64*
                       m.b1*m.b8*m.b23 - 32*m.b1*m.b8*m.b24 - 32*m.b1*m.b8*m.b25 - 32*m.b1*m.b8*m.b26 - 32*m.b1*m.b8*
                       m.b27 - 32*m.b1*m.b8*m.b28 - 32*m.b1*m.b8*m.b29 - 32*m.b1*m.b8*m.b30 - 64*m.b1*m.b9*m.b10 - 64*
                       m.b1*m.b9*m.b11 - 64*m.b1*m.b9*m.b12 - 64*m.b1*m.b9*m.b13 - 64*m.b1*m.b9*m.b14 - 64*m.b1*m.b9*
                       m.b15 - 64*m.b1*m.b9*m.b16 - 32*m.b1*m.b9*m.b17 - 64*m.b1*m.b9*m.b18 - 64*m.b1*m.b9*m.b19 - 64*
                       m.b1*m.b9*m.b20 - 64*m.b1*m.b9*m.b21 - 64*m.b1*m.b9*m.b22 - 32*m.b1*m.b9*m.b23 - 32*m.b1*m.b9*
                       m.b24 - 32*m.b1*m.b9*m.b25 - 32*m.b1*m.b9*m.b26 - 32*m.b1*m.b9*m.b27 - 32*m.b1*m.b9*m.b28 - 32*
                       m.b1*m.b9*m.b29 - 32*m.b1*m.b9*m.b30 - 64*m.b1*m.b10*m.b11 - 64*m.b1*m.b10*m.b12 - 64*m.b1*m.b10*
                       m.b13 - 64*m.b1*m.b10*m.b14 - 64*m.b1*m.b10*m.b15 - 64*m.b1*m.b10*m.b16 - 64*m.b1*m.b10*m.b17 - 
                       64*m.b1*m.b10*m.b18 - 32*m.b1*m.b10*m.b19 - 64*m.b1*m.b10*m.b20 - 64*m.b1*m.b10*m.b21 - 32*m.b1*
                       m.b10*m.b22 - 32*m.b1*m.b10*m.b23 - 32*m.b1*m.b10*m.b24 - 32*m.b1*m.b10*m.b25 - 32*m.b1*m.b10*
                       m.b26 - 32*m.b1*m.b10*m.b27 - 32*m.b1*m.b10*m.b28 - 32*m.b1*m.b10*m.b29 - 32*m.b1*m.b10*m.b30 - 
                       64*m.b1*m.b11*m.b12 - 64*m.b1*m.b11*m.b13 - 64*m.b1*m.b11*m.b14 - 64*m.b1*m.b11*m.b15 - 64*m.b1*
                       m.b11*m.b16 - 64*m.b1*m.b11*m.b17 - 64*m.b1*m.b11*m.b18 - 64*m.b1*m.b11*m.b19 - 64*m.b1*m.b11*
                       m.b20 - 32*m.b1*m.b11*m.b22 - 32*m.b1*m.b11*m.b23 - 32*m.b1*m.b11*m.b24 - 32*m.b1*m.b11*m.b25 - 
                       32*m.b1*m.b11*m.b26 - 32*m.b1*m.b11*m.b27 - 32*m.b1*m.b11*m.b28 - 32*m.b1*m.b11*m.b29 - 32*m.b1*
                       m.b11*m.b30 - 64*m.b1*m.b12*m.b13 - 64*m.b1*m.b12*m.b14 - 64*m.b1*m.b12*m.b15 - 64*m.b1*m.b12*
                       m.b16 - 64*m.b1*m.b12*m.b17 - 64*m.b1*m.b12*m.b18 - 64*m.b1*m.b12*m.b19 - 32*m.b1*m.b12*m.b20 - 
                       32*m.b1*m.b12*m.b21 - 32*m.b1*m.b12*m.b22 - 32*m.b1*m.b12*m.b24 - 32*m.b1*m.b12*m.b25 - 32*m.b1*
                       m.b12*m.b26 - 32*m.b1*m.b12*m.b27 - 32*m.b1*m.b12*m.b28 - 32*m.b1*m.b12*m.b29 - 32*m.b1*m.b12*
                       m.b30 - 64*m.b1*m.b13*m.b14 - 64*m.b1*m.b13*m.b15 - 64*m.b1*m.b13*m.b16 - 64*m.b1*m.b13*m.b17 - 
                       64*m.b1*m.b13*m.b18 - 32*m.b1*m.b13*m.b19 - 32*m.b1*m.b13*m.b20 - 32*m.b1*m.b13*m.b21 - 32*m.b1*
                       m.b13*m.b22 - 32*m.b1*m.b13*m.b23 - 32*m.b1*m.b13*m.b24 - 32*m.b1*m.b13*m.b26 - 32*m.b1*m.b13*
                       m.b27 - 32*m.b1*m.b13*m.b28 - 32*m.b1*m.b13*m.b29 - 32*m.b1*m.b13*m.b30 - 64*m.b1*m.b14*m.b15 - 
                       64*m.b1*m.b14*m.b16 - 64*m.b1*m.b14*m.b17 - 32*m.b1*m.b14*m.b18 - 32*m.b1*m.b14*m.b19 - 32*m.b1*
                       m.b14*m.b20 - 32*m.b1*m.b14*m.b21 - 32*m.b1*m.b14*m.b22 - 32*m.b1*m.b14*m.b23 - 32*m.b1*m.b14*
                       m.b24 - 32*m.b1*m.b14*m.b25 - 32*m.b1*m.b14*m.b26 - 32*m.b1*m.b14*m.b28 - 32*m.b1*m.b14*m.b29 - 
                       32*m.b1*m.b14*m.b30 - 64*m.b1*m.b15*m.b16 - 32*m.b1*m.b15*m.b17 - 32*m.b1*m.b15*m.b18 - 32*m.b1*
                       m.b15*m.b19 - 32*m.b1*m.b15*m.b20 - 32*m.b1*m.b15*m.b21 - 32*m.b1*m.b15*m.b22 - 32*m.b1*m.b15*
                       m.b23 - 32*m.b1*m.b15*m.b24 - 32*m.b1*m.b15*m.b25 - 32*m.b1*m.b15*m.b26 - 32*m.b1*m.b15*m.b27 - 
                       32*m.b1*m.b15*m.b28 - 32*m.b1*m.b15*m.b30 - 32*m.b1*m.b16*m.b17 - 32*m.b1*m.b16*m.b18 - 32*m.b1*
                       m.b16*m.b19 - 32*m.b1*m.b16*m.b20 - 32*m.b1*m.b16*m.b21 - 32*m.b1*m.b16*m.b22 - 32*m.b1*m.b16*
                       m.b23 - 32*m.b1*m.b16*m.b24 - 32*m.b1*m.b16*m.b25 - 32*m.b1*m.b16*m.b26 - 32*m.b1*m.b16*m.b27 - 
                       32*m.b1*m.b16*m.b28 - 32*m.b1*m.b16*m.b29 - 32*m.b1*m.b16*m.b30 - 32*m.b1*m.b17*m.b18 - 32*m.b1*
                       m.b17*m.b19 - 32*m.b1*m.b17*m.b20 - 32*m.b1*m.b17*m.b21 - 32*m.b1*m.b17*m.b22 - 32*m.b1*m.b17*
                       m.b23 - 32*m.b1*m.b17*m.b24 - 32*m.b1*m.b17*m.b25 - 32*m.b1*m.b17*m.b26 - 32*m.b1*m.b17*m.b27 - 
                       32*m.b1*m.b17*m.b28 - 32*m.b1*m.b17*m.b29 - 32*m.b1*m.b17*m.b30 - 32*m.b1*m.b18*m.b19 - 32*m.b1*
                       m.b18*m.b20 - 32*m.b1*m.b18*m.b21 - 32*m.b1*m.b18*m.b22 - 32*m.b1*m.b18*m.b23 - 32*m.b1*m.b18*
                       m.b24 - 32*m.b1*m.b18*m.b25 - 32*m.b1*m.b18*m.b26 - 32*m.b1*m.b18*m.b27 - 32*m.b1*m.b18*m.b28 - 
                       32*m.b1*m.b18*m.b29 - 32*m.b1*m.b18*m.b30 - 32*m.b1*m.b19*m.b20 - 32*m.b1*m.b19*m.b21 - 32*m.b1*
                       m.b19*m.b22 - 32*m.b1*m.b19*m.b23 - 32*m.b1*m.b19*m.b24 - 32*m.b1*m.b19*m.b25 - 32*m.b1*m.b19*
                       m.b26 - 32*m.b1*m.b19*m.b27 - 32*m.b1*m.b19*m.b28 - 32*m.b1*m.b19*m.b29 - 32*m.b1*m.b19*m.b30 - 
                       32*m.b1*m.b20*m.b21 - 32*m.b1*m.b20*m.b22 - 32*m.b1*m.b20*m.b23 - 32*m.b1*m.b20*m.b24 - 32*m.b1*
                       m.b20*m.b25 - 32*m.b1*m.b20*m.b26 - 32*m.b1*m.b20*m.b27 - 32*m.b1*m.b20*m.b28 - 32*m.b1*m.b20*
                       m.b29 - 32*m.b1*m.b20*m.b30 - 32*m.b1*m.b21*m.b22 - 32*m.b1*m.b21*m.b23 - 32*m.b1*m.b21*m.b24 - 
                       32*m.b1*m.b21*m.b25 - 32*m.b1*m.b21*m.b26 - 32*m.b1*m.b21*m.b27 - 32*m.b1*m.b21*m.b28 - 32*m.b1*
                       m.b21*m.b29 - 32*m.b1*m.b21*m.b30 - 32*m.b1*m.b22*m.b23 - 32*m.b1*m.b22*m.b24 - 32*m.b1*m.b22*
                       m.b25 - 32*m.b1*m.b22*m.b26 - 32*m.b1*m.b22*m.b27 - 32*m.b1*m.b22*m.b28 - 32*m.b1*m.b22*m.b29 - 
                       32*m.b1*m.b22*m.b30 - 32*m.b1*m.b23*m.b24 - 32*m.b1*m.b23*m.b25 - 32*m.b1*m.b23*m.b26 - 32*m.b1*
                       m.b23*m.b27 - 32*m.b1*m.b23*m.b28 - 32*m.b1*m.b23*m.b29 - 32*m.b1*m.b23*m.b30 - 32*m.b1*m.b24*
                       m.b25 - 32*m.b1*m.b24*m.b26 - 32*m.b1*m.b24*m.b27 - 32*m.b1*m.b24*m.b28 - 32*m.b1*m.b24*m.b29 - 
                       32*m.b1*m.b24*m.b30 - 32*m.b1*m.b25*m.b26 - 32*m.b1*m.b25*m.b27 - 32*m.b1*m.b25*m.b28 - 32*m.b1*
                       m.b25*m.b29 - 32*m.b1*m.b25*m.b30 - 32*m.b1*m.b26*m.b27 - 32*m.b1*m.b26*m.b28 - 32*m.b1*m.b26*
                       m.b29 - 32*m.b1*m.b26*m.b30 - 32*m.b1*m.b27*m.b28 - 32*m.b1*m.b27*m.b29 - 32*m.b1*m.b27*m.b30 - 
                       32*m.b1*m.b28*m.b29 - 32*m.b1*m.b28*m.b30 - 32*m.b1*m.b29*m.b30 - 64*m.b2*m.b3*m.b4 - 64*m.b2*
                       m.b3*m.b5 - 64*m.b2*m.b3*m.b6 - 64*m.b2*m.b3*m.b7 - 64*m.b2*m.b3*m.b8 - 64*m.b2*m.b3*m.b9 - 64*
                       m.b2*m.b3*m.b10 - 64*m.b2*m.b3*m.b11 - 64*m.b2*m.b3*m.b12 - 96*m.b2*m.b3*m.b13 - 128*m.b2*m.b3*
                       m.b14 - 128*m.b2*m.b3*m.b15 - 128*m.b2*m.b3*m.b16 - 128*m.b2*m.b3*m.b17 - 128*m.b2*m.b3*m.b18 - 
                       128*m.b2*m.b3*m.b19 - 128*m.b2*m.b3*m.b20 - 128*m.b2*m.b3*m.b21 - 128*m.b2*m.b3*m.b22 - 128*m.b2*
                       m.b3*m.b23 - 128*m.b2*m.b3*m.b24 - 128*m.b2*m.b3*m.b25 - 128*m.b2*m.b3*m.b26 - 128*m.b2*m.b3*
                       m.b27 - 128*m.b2*m.b3*m.b28 - 96*m.b2*m.b3*m.b29 - 32*m.b2*m.b3*m.b30 - 96*m.b2*m.b4*m.b5 - 32*
                       m.b2*m.b4*m.b6 - 64*m.b2*m.b4*m.b7 - 64*m.b2*m.b4*m.b8 - 64*m.b2*m.b4*m.b9 - 64*m.b2*m.b4*m.b10
                        - 64*m.b2*m.b4*m.b11 - 96*m.b2*m.b4*m.b12 - 96*m.b2*m.b4*m.b13 - 128*m.b2*m.b4*m.b14 - 128*m.b2*
                       m.b4*m.b15 - 128*m.b2*m.b4*m.b16 - 128*m.b2*m.b4*m.b17 - 128*m.b2*m.b4*m.b18 - 128*m.b2*m.b4*
                       m.b19 - 128*m.b2*m.b4*m.b20 - 128*m.b2*m.b4*m.b21 - 128*m.b2*m.b4*m.b22 - 128*m.b2*m.b4*m.b23 - 
                       128*m.b2*m.b4*m.b24 - 128*m.b2*m.b4*m.b25 - 128*m.b2*m.b4*m.b26 - 128*m.b2*m.b4*m.b27 - 96*m.b2*
                       m.b4*m.b28 - 64*m.b2*m.b4*m.b29 - 32*m.b2*m.b4*m.b30 - 96*m.b2*m.b5*m.b6 - 64*m.b2*m.b5*m.b7 - 32
                       *m.b2*m.b5*m.b8 - 64*m.b2*m.b5*m.b9 - 64*m.b2*m.b5*m.b10 - 96*m.b2*m.b5*m.b11 - 96*m.b2*m.b5*
                       m.b12 - 96*m.b2*m.b5*m.b13 - 128*m.b2*m.b5*m.b14 - 128*m.b2*m.b5*m.b15 - 128*m.b2*m.b5*m.b16 - 
                       128*m.b2*m.b5*m.b17 - 128*m.b2*m.b5*m.b18 - 128*m.b2*m.b5*m.b19 - 128*m.b2*m.b5*m.b20 - 128*m.b2*
                       m.b5*m.b21 - 128*m.b2*m.b5*m.b22 - 128*m.b2*m.b5*m.b23 - 128*m.b2*m.b5*m.b24 - 128*m.b2*m.b5*
                       m.b25 - 128*m.b2*m.b5*m.b26 - 96*m.b2*m.b5*m.b27 - 64*m.b2*m.b5*m.b28 - 64*m.b2*m.b5*m.b29 - 32*
                       m.b2*m.b5*m.b30 - 96*m.b2*m.b6*m.b7 - 64*m.b2*m.b6*m.b8 - 64*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b10
                        - 96*m.b2*m.b6*m.b11 - 96*m.b2*m.b6*m.b12 - 96*m.b2*m.b6*m.b13 - 128*m.b2*m.b6*m.b14 - 128*m.b2*
                       m.b6*m.b15 - 128*m.b2*m.b6*m.b16 - 128*m.b2*m.b6*m.b17 - 128*m.b2*m.b6*m.b18 - 128*m.b2*m.b6*
                       m.b19 - 128*m.b2*m.b6*m.b20 - 128*m.b2*m.b6*m.b21 - 128*m.b2*m.b6*m.b22 - 128*m.b2*m.b6*m.b23 - 
                       128*m.b2*m.b6*m.b24 - 128*m.b2*m.b6*m.b25 - 96*m.b2*m.b6*m.b26 - 64*m.b2*m.b6*m.b27 - 64*m.b2*
                       m.b6*m.b28 - 64*m.b2*m.b6*m.b29 - 32*m.b2*m.b6*m.b30 - 96*m.b2*m.b7*m.b8 - 96*m.b2*m.b7*m.b9 - 96
                       *m.b2*m.b7*m.b10 - 96*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b12 - 96*m.b2*m.b7*m.b13 - 128*m.b2*m.b7*
                       m.b14 - 128*m.b2*m.b7*m.b15 - 128*m.b2*m.b7*m.b16 - 128*m.b2*m.b7*m.b17 - 128*m.b2*m.b7*m.b18 - 
                       128*m.b2*m.b7*m.b19 - 128*m.b2*m.b7*m.b20 - 128*m.b2*m.b7*m.b21 - 128*m.b2*m.b7*m.b22 - 128*m.b2*
                       m.b7*m.b23 - 128*m.b2*m.b7*m.b24 - 96*m.b2*m.b7*m.b25 - 64*m.b2*m.b7*m.b26 - 64*m.b2*m.b7*m.b27
                        - 64*m.b2*m.b7*m.b28 - 64*m.b2*m.b7*m.b29 - 32*m.b2*m.b7*m.b30 - 128*m.b2*m.b8*m.b9 - 96*m.b2*
                       m.b8*m.b10 - 96*m.b2*m.b8*m.b11 - 96*m.b2*m.b8*m.b12 - 96*m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b14 - 
                       128*m.b2*m.b8*m.b15 - 128*m.b2*m.b8*m.b16 - 128*m.b2*m.b8*m.b17 - 128*m.b2*m.b8*m.b18 - 128*m.b2*
                       m.b8*m.b19 - 128*m.b2*m.b8*m.b20 - 128*m.b2*m.b8*m.b21 - 128*m.b2*m.b8*m.b22 - 128*m.b2*m.b8*
                       m.b23 - 96*m.b2*m.b8*m.b24 - 64*m.b2*m.b8*m.b25 - 64*m.b2*m.b8*m.b26 - 64*m.b2*m.b8*m.b27 - 64*
                       m.b2*m.b8*m.b28 - 64*m.b2*m.b8*m.b29 - 32*m.b2*m.b8*m.b30 - 128*m.b2*m.b9*m.b10 - 96*m.b2*m.b9*
                       m.b11 - 96*m.b2*m.b9*m.b12 - 96*m.b2*m.b9*m.b13 - 128*m.b2*m.b9*m.b14 - 128*m.b2*m.b9*m.b15 - 64*
                       m.b2*m.b9*m.b16 - 128*m.b2*m.b9*m.b17 - 128*m.b2*m.b9*m.b18 - 128*m.b2*m.b9*m.b19 - 128*m.b2*m.b9
                       *m.b20 - 128*m.b2*m.b9*m.b21 - 128*m.b2*m.b9*m.b22 - 96*m.b2*m.b9*m.b23 - 64*m.b2*m.b9*m.b24 - 64
                       *m.b2*m.b9*m.b25 - 64*m.b2*m.b9*m.b26 - 64*m.b2*m.b9*m.b27 - 64*m.b2*m.b9*m.b28 - 64*m.b2*m.b9*
                       m.b29 - 32*m.b2*m.b9*m.b30 - 128*m.b2*m.b10*m.b11 - 96*m.b2*m.b10*m.b12 - 96*m.b2*m.b10*m.b13 - 
                       128*m.b2*m.b10*m.b14 - 128*m.b2*m.b10*m.b15 - 128*m.b2*m.b10*m.b16 - 128*m.b2*m.b10*m.b17 - 64*
                       m.b2*m.b10*m.b18 - 128*m.b2*m.b10*m.b19 - 128*m.b2*m.b10*m.b20 - 128*m.b2*m.b10*m.b21 - 96*m.b2*
                       m.b10*m.b22 - 64*m.b2*m.b10*m.b23 - 64*m.b2*m.b10*m.b24 - 64*m.b2*m.b10*m.b25 - 64*m.b2*m.b10*
                       m.b26 - 64*m.b2*m.b10*m.b27 - 64*m.b2*m.b10*m.b28 - 64*m.b2*m.b10*m.b29 - 32*m.b2*m.b10*m.b30 - 
                       128*m.b2*m.b11*m.b12 - 96*m.b2*m.b11*m.b13 - 128*m.b2*m.b11*m.b14 - 128*m.b2*m.b11*m.b15 - 128*
                       m.b2*m.b11*m.b16 - 128*m.b2*m.b11*m.b17 - 128*m.b2*m.b11*m.b18 - 128*m.b2*m.b11*m.b19 - 64*m.b2*
                       m.b11*m.b20 - 96*m.b2*m.b11*m.b21 - 64*m.b2*m.b11*m.b22 - 64*m.b2*m.b11*m.b23 - 64*m.b2*m.b11*
                       m.b24 - 64*m.b2*m.b11*m.b25 - 64*m.b2*m.b11*m.b26 - 64*m.b2*m.b11*m.b27 - 64*m.b2*m.b11*m.b28 - 
                       64*m.b2*m.b11*m.b29 - 32*m.b2*m.b11*m.b30 - 128*m.b2*m.b12*m.b13 - 128*m.b2*m.b12*m.b14 - 128*
                       m.b2*m.b12*m.b15 - 128*m.b2*m.b12*m.b16 - 128*m.b2*m.b12*m.b17 - 128*m.b2*m.b12*m.b18 - 128*m.b2*
                       m.b12*m.b19 - 96*m.b2*m.b12*m.b20 - 64*m.b2*m.b12*m.b21 - 64*m.b2*m.b12*m.b23 - 64*m.b2*m.b12*
                       m.b24 - 64*m.b2*m.b12*m.b25 - 64*m.b2*m.b12*m.b26 - 64*m.b2*m.b12*m.b27 - 64*m.b2*m.b12*m.b28 - 
                       64*m.b2*m.b12*m.b29 - 32*m.b2*m.b12*m.b30 - 160*m.b2*m.b13*m.b14 - 128*m.b2*m.b13*m.b15 - 128*
                       m.b2*m.b13*m.b16 - 128*m.b2*m.b13*m.b17 - 128*m.b2*m.b13*m.b18 - 96*m.b2*m.b13*m.b19 - 64*m.b2*
                       m.b13*m.b20 - 64*m.b2*m.b13*m.b21 - 64*m.b2*m.b13*m.b22 - 64*m.b2*m.b13*m.b23 - 64*m.b2*m.b13*
                       m.b25 - 64*m.b2*m.b13*m.b26 - 64*m.b2*m.b13*m.b27 - 64*m.b2*m.b13*m.b28 - 64*m.b2*m.b13*m.b29 - 
                       32*m.b2*m.b13*m.b30 - 160*m.b2*m.b14*m.b15 - 128*m.b2*m.b14*m.b16 - 128*m.b2*m.b14*m.b17 - 96*
                       m.b2*m.b14*m.b18 - 64*m.b2*m.b14*m.b19 - 64*m.b2*m.b14*m.b20 - 64*m.b2*m.b14*m.b21 - 64*m.b2*
                       m.b14*m.b22 - 64*m.b2*m.b14*m.b23 - 64*m.b2*m.b14*m.b24 - 64*m.b2*m.b14*m.b25 - 64*m.b2*m.b14*
                       m.b27 - 64*m.b2*m.b14*m.b28 - 64*m.b2*m.b14*m.b29 - 32*m.b2*m.b14*m.b30 - 160*m.b2*m.b15*m.b16 - 
                       96*m.b2*m.b15*m.b17 - 64*m.b2*m.b15*m.b18 - 64*m.b2*m.b15*m.b19 - 64*m.b2*m.b15*m.b20 - 64*m.b2*
                       m.b15*m.b21 - 64*m.b2*m.b15*m.b22 - 64*m.b2*m.b15*m.b23 - 64*m.b2*m.b15*m.b24 - 64*m.b2*m.b15*
                       m.b25 - 64*m.b2*m.b15*m.b26 - 64*m.b2*m.b15*m.b27 - 64*m.b2*m.b15*m.b29 - 32*m.b2*m.b15*m.b30 - 
                       96*m.b2*m.b16*m.b17 - 64*m.b2*m.b16*m.b18 - 64*m.b2*m.b16*m.b19 - 64*m.b2*m.b16*m.b20 - 64*m.b2*
                       m.b16*m.b21 - 64*m.b2*m.b16*m.b22 - 64*m.b2*m.b16*m.b23 - 64*m.b2*m.b16*m.b24 - 64*m.b2*m.b16*
                       m.b25 - 64*m.b2*m.b16*m.b26 - 64*m.b2*m.b16*m.b27 - 64*m.b2*m.b16*m.b28 - 64*m.b2*m.b16*m.b29 - 
                       96*m.b2*m.b17*m.b18 - 64*m.b2*m.b17*m.b19 - 64*m.b2*m.b17*m.b20 - 64*m.b2*m.b17*m.b21 - 64*m.b2*
                       m.b17*m.b22 - 64*m.b2*m.b17*m.b23 - 64*m.b2*m.b17*m.b24 - 64*m.b2*m.b17*m.b25 - 64*m.b2*m.b17*
                       m.b26 - 64*m.b2*m.b17*m.b27 - 64*m.b2*m.b17*m.b28 - 64*m.b2*m.b17*m.b29 - 32*m.b2*m.b17*m.b30 - 
                       96*m.b2*m.b18*m.b19 - 64*m.b2*m.b18*m.b20 - 64*m.b2*m.b18*m.b21 - 64*m.b2*m.b18*m.b22 - 64*m.b2*
                       m.b18*m.b23 - 64*m.b2*m.b18*m.b24 - 64*m.b2*m.b18*m.b25 - 64*m.b2*m.b18*m.b26 - 64*m.b2*m.b18*
                       m.b27 - 64*m.b2*m.b18*m.b28 - 64*m.b2*m.b18*m.b29 - 32*m.b2*m.b18*m.b30 - 96*m.b2*m.b19*m.b20 - 
                       64*m.b2*m.b19*m.b21 - 64*m.b2*m.b19*m.b22 - 64*m.b2*m.b19*m.b23 - 64*m.b2*m.b19*m.b24 - 64*m.b2*
                       m.b19*m.b25 - 64*m.b2*m.b19*m.b26 - 64*m.b2*m.b19*m.b27 - 64*m.b2*m.b19*m.b28 - 64*m.b2*m.b19*
                       m.b29 - 32*m.b2*m.b19*m.b30 - 96*m.b2*m.b20*m.b21 - 64*m.b2*m.b20*m.b22 - 64*m.b2*m.b20*m.b23 - 
                       64*m.b2*m.b20*m.b24 - 64*m.b2*m.b20*m.b25 - 64*m.b2*m.b20*m.b26 - 64*m.b2*m.b20*m.b27 - 64*m.b2*
                       m.b20*m.b28 - 64*m.b2*m.b20*m.b29 - 32*m.b2*m.b20*m.b30 - 96*m.b2*m.b21*m.b22 - 64*m.b2*m.b21*
                       m.b23 - 64*m.b2*m.b21*m.b24 - 64*m.b2*m.b21*m.b25 - 64*m.b2*m.b21*m.b26 - 64*m.b2*m.b21*m.b27 - 
                       64*m.b2*m.b21*m.b28 - 64*m.b2*m.b21*m.b29 - 32*m.b2*m.b21*m.b30 - 96*m.b2*m.b22*m.b23 - 64*m.b2*
                       m.b22*m.b24 - 64*m.b2*m.b22*m.b25 - 64*m.b2*m.b22*m.b26 - 64*m.b2*m.b22*m.b27 - 64*m.b2*m.b22*
                       m.b28 - 64*m.b2*m.b22*m.b29 - 32*m.b2*m.b22*m.b30 - 96*m.b2*m.b23*m.b24 - 64*m.b2*m.b23*m.b25 - 
                       64*m.b2*m.b23*m.b26 - 64*m.b2*m.b23*m.b27 - 64*m.b2*m.b23*m.b28 - 64*m.b2*m.b23*m.b29 - 32*m.b2*
                       m.b23*m.b30 - 96*m.b2*m.b24*m.b25 - 64*m.b2*m.b24*m.b26 - 64*m.b2*m.b24*m.b27 - 64*m.b2*m.b24*
                       m.b28 - 64*m.b2*m.b24*m.b29 - 32*m.b2*m.b24*m.b30 - 96*m.b2*m.b25*m.b26 - 64*m.b2*m.b25*m.b27 - 
                       64*m.b2*m.b25*m.b28 - 64*m.b2*m.b25*m.b29 - 32*m.b2*m.b25*m.b30 - 96*m.b2*m.b26*m.b27 - 64*m.b2*
                       m.b26*m.b28 - 64*m.b2*m.b26*m.b29 - 32*m.b2*m.b26*m.b30 - 96*m.b2*m.b27*m.b28 - 64*m.b2*m.b27*
                       m.b29 - 32*m.b2*m.b27*m.b30 - 96*m.b2*m.b28*m.b29 - 32*m.b2*m.b28*m.b30 - 64*m.b2*m.b29*m.b30 - 
                       64*m.b3*m.b4*m.b5 - 96*m.b3*m.b4*m.b6 - 64*m.b3*m.b4*m.b7 - 64*m.b3*m.b4*m.b8 - 64*m.b3*m.b4*m.b9
                        - 64*m.b3*m.b4*m.b10 - 64*m.b3*m.b4*m.b11 - 64*m.b3*m.b4*m.b12 - 64*m.b3*m.b4*m.b13 - 128*m.b3*
                       m.b4*m.b14 - 192*m.b3*m.b4*m.b15 - 192*m.b3*m.b4*m.b16 - 192*m.b3*m.b4*m.b17 - 192*m.b3*m.b4*
                       m.b18 - 192*m.b3*m.b4*m.b19 - 192*m.b3*m.b4*m.b20 - 192*m.b3*m.b4*m.b21 - 192*m.b3*m.b4*m.b22 - 
                       192*m.b3*m.b4*m.b23 - 192*m.b3*m.b4*m.b24 - 192*m.b3*m.b4*m.b25 - 192*m.b3*m.b4*m.b26 - 192*m.b3*
                       m.b4*m.b27 - 160*m.b3*m.b4*m.b28 - 96*m.b3*m.b4*m.b29 - 32*m.b3*m.b4*m.b30 - 96*m.b3*m.b5*m.b6 - 
                       64*m.b3*m.b5*m.b7 - 64*m.b3*m.b5*m.b8 - 64*m.b3*m.b5*m.b9 - 64*m.b3*m.b5*m.b10 - 64*m.b3*m.b5*
                       m.b11 - 64*m.b3*m.b5*m.b12 - 128*m.b3*m.b5*m.b13 - 128*m.b3*m.b5*m.b14 - 192*m.b3*m.b5*m.b15 - 
                       192*m.b3*m.b5*m.b16 - 192*m.b3*m.b5*m.b17 - 192*m.b3*m.b5*m.b18 - 192*m.b3*m.b5*m.b19 - 192*m.b3*
                       m.b5*m.b20 - 192*m.b3*m.b5*m.b21 - 192*m.b3*m.b5*m.b22 - 192*m.b3*m.b5*m.b23 - 192*m.b3*m.b5*
                       m.b24 - 192*m.b3*m.b5*m.b25 - 192*m.b3*m.b5*m.b26 - 160*m.b3*m.b5*m.b27 - 128*m.b3*m.b5*m.b28 - 
                       64*m.b3*m.b5*m.b29 - 32*m.b3*m.b5*m.b30 - 96*m.b3*m.b6*m.b7 - 96*m.b3*m.b6*m.b8 - 32*m.b3*m.b6*
                       m.b9 - 64*m.b3*m.b6*m.b10 - 64*m.b3*m.b6*m.b11 - 128*m.b3*m.b6*m.b12 - 128*m.b3*m.b6*m.b13 - 128*
                       m.b3*m.b6*m.b14 - 192*m.b3*m.b6*m.b15 - 192*m.b3*m.b6*m.b16 - 192*m.b3*m.b6*m.b17 - 192*m.b3*m.b6
                       *m.b18 - 192*m.b3*m.b6*m.b19 - 192*m.b3*m.b6*m.b20 - 192*m.b3*m.b6*m.b21 - 192*m.b3*m.b6*m.b22 - 
                       192*m.b3*m.b6*m.b23 - 192*m.b3*m.b6*m.b24 - 192*m.b3*m.b6*m.b25 - 160*m.b3*m.b6*m.b26 - 128*m.b3*
                       m.b6*m.b27 - 96*m.b3*m.b6*m.b28 - 64*m.b3*m.b6*m.b29 - 32*m.b3*m.b6*m.b30 - 96*m.b3*m.b7*m.b8 - 
                       96*m.b3*m.b7*m.b9 - 64*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*m.b11 - 128*m.b3*m.b7*m.b12 - 128*m.b3*m.b7
                       *m.b13 - 128*m.b3*m.b7*m.b14 - 192*m.b3*m.b7*m.b15 - 192*m.b3*m.b7*m.b16 - 192*m.b3*m.b7*m.b17 - 
                       192*m.b3*m.b7*m.b18 - 192*m.b3*m.b7*m.b19 - 192*m.b3*m.b7*m.b20 - 192*m.b3*m.b7*m.b21 - 192*m.b3*
                       m.b7*m.b22 - 192*m.b3*m.b7*m.b23 - 192*m.b3*m.b7*m.b24 - 160*m.b3*m.b7*m.b25 - 128*m.b3*m.b7*
                       m.b26 - 96*m.b3*m.b7*m.b27 - 96*m.b3*m.b7*m.b28 - 64*m.b3*m.b7*m.b29 - 32*m.b3*m.b7*m.b30 - 96*
                       m.b3*m.b8*m.b9 - 160*m.b3*m.b8*m.b10 - 128*m.b3*m.b8*m.b11 - 128*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*
                       m.b13 - 128*m.b3*m.b8*m.b14 - 192*m.b3*m.b8*m.b15 - 192*m.b3*m.b8*m.b16 - 192*m.b3*m.b8*m.b17 - 
                       192*m.b3*m.b8*m.b18 - 192*m.b3*m.b8*m.b19 - 192*m.b3*m.b8*m.b20 - 192*m.b3*m.b8*m.b21 - 192*m.b3*
                       m.b8*m.b22 - 192*m.b3*m.b8*m.b23 - 160*m.b3*m.b8*m.b24 - 128*m.b3*m.b8*m.b25 - 96*m.b3*m.b8*m.b26
                        - 96*m.b3*m.b8*m.b27 - 96*m.b3*m.b8*m.b28 - 64*m.b3*m.b8*m.b29 - 32*m.b3*m.b8*m.b30 - 160*m.b3*
                       m.b9*m.b10 - 160*m.b3*m.b9*m.b11 - 128*m.b3*m.b9*m.b12 - 128*m.b3*m.b9*m.b13 - 128*m.b3*m.b9*
                       m.b14 - 96*m.b3*m.b9*m.b15 - 192*m.b3*m.b9*m.b16 - 192*m.b3*m.b9*m.b17 - 192*m.b3*m.b9*m.b18 - 
                       192*m.b3*m.b9*m.b19 - 192*m.b3*m.b9*m.b20 - 192*m.b3*m.b9*m.b21 - 192*m.b3*m.b9*m.b22 - 160*m.b3*
                       m.b9*m.b23 - 128*m.b3*m.b9*m.b24 - 96*m.b3*m.b9*m.b25 - 96*m.b3*m.b9*m.b26 - 96*m.b3*m.b9*m.b27
                        - 96*m.b3*m.b9*m.b28 - 64*m.b3*m.b9*m.b29 - 32*m.b3*m.b9*m.b30 - 160*m.b3*m.b10*m.b11 - 160*m.b3
                       *m.b10*m.b12 - 128*m.b3*m.b10*m.b13 - 128*m.b3*m.b10*m.b14 - 192*m.b3*m.b10*m.b15 - 192*m.b3*
                       m.b10*m.b16 - 96*m.b3*m.b10*m.b17 - 192*m.b3*m.b10*m.b18 - 192*m.b3*m.b10*m.b19 - 192*m.b3*m.b10*
                       m.b20 - 192*m.b3*m.b10*m.b21 - 160*m.b3*m.b10*m.b22 - 128*m.b3*m.b10*m.b23 - 96*m.b3*m.b10*m.b24
                        - 96*m.b3*m.b10*m.b25 - 96*m.b3*m.b10*m.b26 - 96*m.b3*m.b10*m.b27 - 96*m.b3*m.b10*m.b28 - 64*
                       m.b3*m.b10*m.b29 - 32*m.b3*m.b10*m.b30 - 160*m.b3*m.b11*m.b12 - 160*m.b3*m.b11*m.b13 - 128*m.b3*
                       m.b11*m.b14 - 192*m.b3*m.b11*m.b15 - 192*m.b3*m.b11*m.b16 - 192*m.b3*m.b11*m.b17 - 192*m.b3*m.b11
                       *m.b18 - 96*m.b3*m.b11*m.b19 - 192*m.b3*m.b11*m.b20 - 160*m.b3*m.b11*m.b21 - 128*m.b3*m.b11*m.b22
                        - 96*m.b3*m.b11*m.b23 - 96*m.b3*m.b11*m.b24 - 96*m.b3*m.b11*m.b25 - 96*m.b3*m.b11*m.b26 - 96*
                       m.b3*m.b11*m.b27 - 96*m.b3*m.b11*m.b28 - 64*m.b3*m.b11*m.b29 - 32*m.b3*m.b11*m.b30 - 160*m.b3*
                       m.b12*m.b13 - 160*m.b3*m.b12*m.b14 - 192*m.b3*m.b12*m.b15 - 192*m.b3*m.b12*m.b16 - 192*m.b3*m.b12
                       *m.b17 - 192*m.b3*m.b12*m.b18 - 192*m.b3*m.b12*m.b19 - 160*m.b3*m.b12*m.b20 - 32*m.b3*m.b12*m.b21
                        - 96*m.b3*m.b12*m.b22 - 96*m.b3*m.b12*m.b23 - 96*m.b3*m.b12*m.b24 - 96*m.b3*m.b12*m.b25 - 96*
                       m.b3*m.b12*m.b26 - 96*m.b3*m.b12*m.b27 - 96*m.b3*m.b12*m.b28 - 64*m.b3*m.b12*m.b29 - 32*m.b3*
                       m.b12*m.b30 - 192*m.b3*m.b13*m.b14 - 224*m.b3*m.b13*m.b15 - 192*m.b3*m.b13*m.b16 - 192*m.b3*m.b13
                       *m.b17 - 192*m.b3*m.b13*m.b18 - 160*m.b3*m.b13*m.b19 - 128*m.b3*m.b13*m.b20 - 96*m.b3*m.b13*m.b21
                        - 96*m.b3*m.b13*m.b22 - 96*m.b3*m.b13*m.b24 - 96*m.b3*m.b13*m.b25 - 96*m.b3*m.b13*m.b26 - 96*
                       m.b3*m.b13*m.b27 - 96*m.b3*m.b13*m.b28 - 64*m.b3*m.b13*m.b29 - 32*m.b3*m.b13*m.b30 - 256*m.b3*
                       m.b14*m.b15 - 224*m.b3*m.b14*m.b16 - 192*m.b3*m.b14*m.b17 - 160*m.b3*m.b14*m.b18 - 128*m.b3*m.b14
                       *m.b19 - 96*m.b3*m.b14*m.b20 - 96*m.b3*m.b14*m.b21 - 96*m.b3*m.b14*m.b22 - 96*m.b3*m.b14*m.b23 - 
                       96*m.b3*m.b14*m.b24 - 96*m.b3*m.b14*m.b26 - 96*m.b3*m.b14*m.b27 - 96*m.b3*m.b14*m.b28 - 64*m.b3*
                       m.b14*m.b29 - 32*m.b3*m.b14*m.b30 - 256*m.b3*m.b15*m.b16 - 192*m.b3*m.b15*m.b17 - 128*m.b3*m.b15*
                       m.b18 - 96*m.b3*m.b15*m.b19 - 96*m.b3*m.b15*m.b20 - 96*m.b3*m.b15*m.b21 - 96*m.b3*m.b15*m.b22 - 
                       96*m.b3*m.b15*m.b23 - 96*m.b3*m.b15*m.b24 - 96*m.b3*m.b15*m.b25 - 96*m.b3*m.b15*m.b26 - 96*m.b3*
                       m.b15*m.b28 - 64*m.b3*m.b15*m.b29 - 32*m.b3*m.b15*m.b30 - 192*m.b3*m.b16*m.b17 - 128*m.b3*m.b16*
                       m.b18 - 96*m.b3*m.b16*m.b19 - 96*m.b3*m.b16*m.b20 - 96*m.b3*m.b16*m.b21 - 96*m.b3*m.b16*m.b22 - 
                       96*m.b3*m.b16*m.b23 - 96*m.b3*m.b16*m.b24 - 96*m.b3*m.b16*m.b25 - 96*m.b3*m.b16*m.b26 - 96*m.b3*
                       m.b16*m.b27 - 96*m.b3*m.b16*m.b28 - 32*m.b3*m.b16*m.b30 - 160*m.b3*m.b17*m.b18 - 128*m.b3*m.b17*
                       m.b19 - 96*m.b3*m.b17*m.b20 - 96*m.b3*m.b17*m.b21 - 96*m.b3*m.b17*m.b22 - 96*m.b3*m.b17*m.b23 - 
                       96*m.b3*m.b17*m.b24 - 96*m.b3*m.b17*m.b25 - 96*m.b3*m.b17*m.b26 - 96*m.b3*m.b17*m.b27 - 96*m.b3*
                       m.b17*m.b28 - 64*m.b3*m.b17*m.b29 - 32*m.b3*m.b17*m.b30 - 160*m.b3*m.b18*m.b19 - 128*m.b3*m.b18*
                       m.b20 - 96*m.b3*m.b18*m.b21 - 96*m.b3*m.b18*m.b22 - 96*m.b3*m.b18*m.b23 - 96*m.b3*m.b18*m.b24 - 
                       96*m.b3*m.b18*m.b25 - 96*m.b3*m.b18*m.b26 - 96*m.b3*m.b18*m.b27 - 96*m.b3*m.b18*m.b28 - 64*m.b3*
                       m.b18*m.b29 - 32*m.b3*m.b18*m.b30 - 160*m.b3*m.b19*m.b20 - 128*m.b3*m.b19*m.b21 - 96*m.b3*m.b19*
                       m.b22 - 96*m.b3*m.b19*m.b23 - 96*m.b3*m.b19*m.b24 - 96*m.b3*m.b19*m.b25 - 96*m.b3*m.b19*m.b26 - 
                       96*m.b3*m.b19*m.b27 - 96*m.b3*m.b19*m.b28 - 64*m.b3*m.b19*m.b29 - 32*m.b3*m.b19*m.b30 - 160*m.b3*
                       m.b20*m.b21 - 128*m.b3*m.b20*m.b22 - 96*m.b3*m.b20*m.b23 - 96*m.b3*m.b20*m.b24 - 96*m.b3*m.b20*
                       m.b25 - 96*m.b3*m.b20*m.b26 - 96*m.b3*m.b20*m.b27 - 96*m.b3*m.b20*m.b28 - 64*m.b3*m.b20*m.b29 - 
                       32*m.b3*m.b20*m.b30 - 160*m.b3*m.b21*m.b22 - 128*m.b3*m.b21*m.b23 - 96*m.b3*m.b21*m.b24 - 96*m.b3
                       *m.b21*m.b25 - 96*m.b3*m.b21*m.b26 - 96*m.b3*m.b21*m.b27 - 96*m.b3*m.b21*m.b28 - 64*m.b3*m.b21*
                       m.b29 - 32*m.b3*m.b21*m.b30 - 160*m.b3*m.b22*m.b23 - 128*m.b3*m.b22*m.b24 - 96*m.b3*m.b22*m.b25
                        - 96*m.b3*m.b22*m.b26 - 96*m.b3*m.b22*m.b27 - 96*m.b3*m.b22*m.b28 - 64*m.b3*m.b22*m.b29 - 32*
                       m.b3*m.b22*m.b30 - 160*m.b3*m.b23*m.b24 - 128*m.b3*m.b23*m.b25 - 96*m.b3*m.b23*m.b26 - 96*m.b3*
                       m.b23*m.b27 - 96*m.b3*m.b23*m.b28 - 64*m.b3*m.b23*m.b29 - 32*m.b3*m.b23*m.b30 - 160*m.b3*m.b24*
                       m.b25 - 128*m.b3*m.b24*m.b26 - 96*m.b3*m.b24*m.b27 - 96*m.b3*m.b24*m.b28 - 64*m.b3*m.b24*m.b29 - 
                       32*m.b3*m.b24*m.b30 - 160*m.b3*m.b25*m.b26 - 128*m.b3*m.b25*m.b27 - 96*m.b3*m.b25*m.b28 - 64*m.b3
                       *m.b25*m.b29 - 32*m.b3*m.b25*m.b30 - 160*m.b3*m.b26*m.b27 - 128*m.b3*m.b26*m.b28 - 64*m.b3*m.b26*
                       m.b29 - 32*m.b3*m.b26*m.b30 - 160*m.b3*m.b27*m.b28 - 96*m.b3*m.b27*m.b29 - 32*m.b3*m.b27*m.b30 - 
                       128*m.b3*m.b28*m.b29 - 64*m.b3*m.b28*m.b30 - 64*m.b3*m.b29*m.b30 - 64*m.b4*m.b5*m.b6 - 96*m.b4*
                       m.b5*m.b7 - 96*m.b4*m.b5*m.b8 - 64*m.b4*m.b5*m.b9 - 64*m.b4*m.b5*m.b10 - 64*m.b4*m.b5*m.b11 - 64*
                       m.b4*m.b5*m.b12 - 64*m.b4*m.b5*m.b13 - 64*m.b4*m.b5*m.b14 - 160*m.b4*m.b5*m.b15 - 256*m.b4*m.b5*
                       m.b16 - 256*m.b4*m.b5*m.b17 - 256*m.b4*m.b5*m.b18 - 256*m.b4*m.b5*m.b19 - 256*m.b4*m.b5*m.b20 - 
                       256*m.b4*m.b5*m.b21 - 256*m.b4*m.b5*m.b22 - 256*m.b4*m.b5*m.b23 - 256*m.b4*m.b5*m.b24 - 256*m.b4*
                       m.b5*m.b25 - 256*m.b4*m.b5*m.b26 - 224*m.b4*m.b5*m.b27 - 160*m.b4*m.b5*m.b28 - 96*m.b4*m.b5*m.b29
                        - 32*m.b4*m.b5*m.b30 - 96*m.b4*m.b6*m.b7 - 64*m.b4*m.b6*m.b8 - 96*m.b4*m.b6*m.b9 - 64*m.b4*m.b6*
                       m.b10 - 64*m.b4*m.b6*m.b11 - 64*m.b4*m.b6*m.b12 - 64*m.b4*m.b6*m.b13 - 160*m.b4*m.b6*m.b14 - 160*
                       m.b4*m.b6*m.b15 - 256*m.b4*m.b6*m.b16 - 256*m.b4*m.b6*m.b17 - 256*m.b4*m.b6*m.b18 - 256*m.b4*m.b6
                       *m.b19 - 256*m.b4*m.b6*m.b20 - 256*m.b4*m.b6*m.b21 - 256*m.b4*m.b6*m.b22 - 256*m.b4*m.b6*m.b23 - 
                       256*m.b4*m.b6*m.b24 - 256*m.b4*m.b6*m.b25 - 224*m.b4*m.b6*m.b26 - 192*m.b4*m.b6*m.b27 - 128*m.b4*
                       m.b6*m.b28 - 64*m.b4*m.b6*m.b29 - 32*m.b4*m.b6*m.b30 - 96*m.b4*m.b7*m.b8 - 96*m.b4*m.b7*m.b9 - 64
                       *m.b4*m.b7*m.b10 - 64*m.b4*m.b7*m.b11 - 64*m.b4*m.b7*m.b12 - 160*m.b4*m.b7*m.b13 - 160*m.b4*m.b7*
                       m.b14 - 160*m.b4*m.b7*m.b15 - 256*m.b4*m.b7*m.b16 - 256*m.b4*m.b7*m.b17 - 256*m.b4*m.b7*m.b18 - 
                       256*m.b4*m.b7*m.b19 - 256*m.b4*m.b7*m.b20 - 256*m.b4*m.b7*m.b21 - 256*m.b4*m.b7*m.b22 - 256*m.b4*
                       m.b7*m.b23 - 256*m.b4*m.b7*m.b24 - 224*m.b4*m.b7*m.b25 - 192*m.b4*m.b7*m.b26 - 160*m.b4*m.b7*
                       m.b27 - 96*m.b4*m.b7*m.b28 - 64*m.b4*m.b7*m.b29 - 32*m.b4*m.b7*m.b30 - 96*m.b4*m.b8*m.b9 - 96*
                       m.b4*m.b8*m.b10 - 96*m.b4*m.b8*m.b11 - 128*m.b4*m.b8*m.b12 - 160*m.b4*m.b8*m.b13 - 160*m.b4*m.b8*
                       m.b14 - 160*m.b4*m.b8*m.b15 - 256*m.b4*m.b8*m.b16 - 256*m.b4*m.b8*m.b17 - 256*m.b4*m.b8*m.b18 - 
                       256*m.b4*m.b8*m.b19 - 256*m.b4*m.b8*m.b20 - 256*m.b4*m.b8*m.b21 - 256*m.b4*m.b8*m.b22 - 256*m.b4*
                       m.b8*m.b23 - 224*m.b4*m.b8*m.b24 - 192*m.b4*m.b8*m.b25 - 160*m.b4*m.b8*m.b26 - 128*m.b4*m.b8*
                       m.b27 - 96*m.b4*m.b8*m.b28 - 64*m.b4*m.b8*m.b29 - 32*m.b4*m.b8*m.b30 - 96*m.b4*m.b9*m.b10 - 192*
                       m.b4*m.b9*m.b11 - 192*m.b4*m.b9*m.b12 - 160*m.b4*m.b9*m.b13 - 128*m.b4*m.b9*m.b14 - 160*m.b4*m.b9
                       *m.b15 - 256*m.b4*m.b9*m.b16 - 256*m.b4*m.b9*m.b17 - 256*m.b4*m.b9*m.b18 - 256*m.b4*m.b9*m.b19 - 
                       256*m.b4*m.b9*m.b20 - 256*m.b4*m.b9*m.b21 - 256*m.b4*m.b9*m.b22 - 224*m.b4*m.b9*m.b23 - 192*m.b4*
                       m.b9*m.b24 - 160*m.b4*m.b9*m.b25 - 128*m.b4*m.b9*m.b26 - 128*m.b4*m.b9*m.b27 - 96*m.b4*m.b9*m.b28
                        - 64*m.b4*m.b9*m.b29 - 32*m.b4*m.b9*m.b30 - 192*m.b4*m.b10*m.b11 - 192*m.b4*m.b10*m.b12 - 192*
                       m.b4*m.b10*m.b13 - 160*m.b4*m.b10*m.b14 - 160*m.b4*m.b10*m.b15 - 128*m.b4*m.b10*m.b16 - 256*m.b4*
                       m.b10*m.b17 - 256*m.b4*m.b10*m.b18 - 256*m.b4*m.b10*m.b19 - 256*m.b4*m.b10*m.b20 - 256*m.b4*m.b10
                       *m.b21 - 224*m.b4*m.b10*m.b22 - 192*m.b4*m.b10*m.b23 - 160*m.b4*m.b10*m.b24 - 128*m.b4*m.b10*
                       m.b25 - 128*m.b4*m.b10*m.b26 - 128*m.b4*m.b10*m.b27 - 96*m.b4*m.b10*m.b28 - 64*m.b4*m.b10*m.b29
                        - 32*m.b4*m.b10*m.b30 - 192*m.b4*m.b11*m.b12 - 192*m.b4*m.b11*m.b13 - 192*m.b4*m.b11*m.b14 - 160
                       *m.b4*m.b11*m.b15 - 256*m.b4*m.b11*m.b16 - 256*m.b4*m.b11*m.b17 - 128*m.b4*m.b11*m.b18 - 256*m.b4
                       *m.b11*m.b19 - 256*m.b4*m.b11*m.b20 - 224*m.b4*m.b11*m.b21 - 192*m.b4*m.b11*m.b22 - 160*m.b4*
                       m.b11*m.b23 - 128*m.b4*m.b11*m.b24 - 128*m.b4*m.b11*m.b25 - 128*m.b4*m.b11*m.b26 - 128*m.b4*m.b11
                       *m.b27 - 96*m.b4*m.b11*m.b28 - 64*m.b4*m.b11*m.b29 - 32*m.b4*m.b11*m.b30 - 192*m.b4*m.b12*m.b13
                        - 224*m.b4*m.b12*m.b14 - 192*m.b4*m.b12*m.b15 - 256*m.b4*m.b12*m.b16 - 256*m.b4*m.b12*m.b17 - 
                       256*m.b4*m.b12*m.b18 - 256*m.b4*m.b12*m.b19 - 96*m.b4*m.b12*m.b20 - 192*m.b4*m.b12*m.b21 - 160*
                       m.b4*m.b12*m.b22 - 128*m.b4*m.b12*m.b23 - 128*m.b4*m.b12*m.b24 - 128*m.b4*m.b12*m.b25 - 128*m.b4*
                       m.b12*m.b26 - 128*m.b4*m.b12*m.b27 - 96*m.b4*m.b12*m.b28 - 64*m.b4*m.b12*m.b29 - 32*m.b4*m.b12*
                       m.b30 - 192*m.b4*m.b13*m.b14 - 224*m.b4*m.b13*m.b15 - 288*m.b4*m.b13*m.b16 - 256*m.b4*m.b13*m.b17
                        - 256*m.b4*m.b13*m.b18 - 224*m.b4*m.b13*m.b19 - 192*m.b4*m.b13*m.b20 - 160*m.b4*m.b13*m.b21 - 
                       128*m.b4*m.b13*m.b23 - 128*m.b4*m.b13*m.b24 - 128*m.b4*m.b13*m.b25 - 128*m.b4*m.b13*m.b26 - 128*
                       m.b4*m.b13*m.b27 - 96*m.b4*m.b13*m.b28 - 64*m.b4*m.b13*m.b29 - 32*m.b4*m.b13*m.b30 - 256*m.b4*
                       m.b14*m.b15 - 320*m.b4*m.b14*m.b16 - 288*m.b4*m.b14*m.b17 - 224*m.b4*m.b14*m.b18 - 192*m.b4*m.b14
                       *m.b19 - 160*m.b4*m.b14*m.b20 - 128*m.b4*m.b14*m.b21 - 128*m.b4*m.b14*m.b22 - 128*m.b4*m.b14*
                       m.b23 - 128*m.b4*m.b14*m.b25 - 128*m.b4*m.b14*m.b26 - 128*m.b4*m.b14*m.b27 - 96*m.b4*m.b14*m.b28
                        - 64*m.b4*m.b14*m.b29 - 32*m.b4*m.b14*m.b30 - 352*m.b4*m.b15*m.b16 - 288*m.b4*m.b15*m.b17 - 224*
                       m.b4*m.b15*m.b18 - 160*m.b4*m.b15*m.b19 - 128*m.b4*m.b15*m.b20 - 128*m.b4*m.b15*m.b21 - 128*m.b4*
                       m.b15*m.b22 - 128*m.b4*m.b15*m.b23 - 128*m.b4*m.b15*m.b24 - 128*m.b4*m.b15*m.b25 - 128*m.b4*m.b15
                       *m.b27 - 96*m.b4*m.b15*m.b28 - 64*m.b4*m.b15*m.b29 - 32*m.b4*m.b15*m.b30 - 288*m.b4*m.b16*m.b17
                        - 224*m.b4*m.b16*m.b18 - 160*m.b4*m.b16*m.b19 - 128*m.b4*m.b16*m.b20 - 128*m.b4*m.b16*m.b21 - 
                       128*m.b4*m.b16*m.b22 - 128*m.b4*m.b16*m.b23 - 128*m.b4*m.b16*m.b24 - 128*m.b4*m.b16*m.b25 - 128*
                       m.b4*m.b16*m.b26 - 128*m.b4*m.b16*m.b27 - 64*m.b4*m.b16*m.b29 - 32*m.b4*m.b16*m.b30 - 224*m.b4*
                       m.b17*m.b18 - 192*m.b4*m.b17*m.b19 - 160*m.b4*m.b17*m.b20 - 128*m.b4*m.b17*m.b21 - 128*m.b4*m.b17
                       *m.b22 - 128*m.b4*m.b17*m.b23 - 128*m.b4*m.b17*m.b24 - 128*m.b4*m.b17*m.b25 - 128*m.b4*m.b17*
                       m.b26 - 128*m.b4*m.b17*m.b27 - 96*m.b4*m.b17*m.b28 - 64*m.b4*m.b17*m.b29 - 224*m.b4*m.b18*m.b19
                        - 192*m.b4*m.b18*m.b20 - 160*m.b4*m.b18*m.b21 - 128*m.b4*m.b18*m.b22 - 128*m.b4*m.b18*m.b23 - 
                       128*m.b4*m.b18*m.b24 - 128*m.b4*m.b18*m.b25 - 128*m.b4*m.b18*m.b26 - 128*m.b4*m.b18*m.b27 - 96*
                       m.b4*m.b18*m.b28 - 64*m.b4*m.b18*m.b29 - 32*m.b4*m.b18*m.b30 - 224*m.b4*m.b19*m.b20 - 192*m.b4*
                       m.b19*m.b21 - 160*m.b4*m.b19*m.b22 - 128*m.b4*m.b19*m.b23 - 128*m.b4*m.b19*m.b24 - 128*m.b4*m.b19
                       *m.b25 - 128*m.b4*m.b19*m.b26 - 128*m.b4*m.b19*m.b27 - 96*m.b4*m.b19*m.b28 - 64*m.b4*m.b19*m.b29
                        - 32*m.b4*m.b19*m.b30 - 224*m.b4*m.b20*m.b21 - 192*m.b4*m.b20*m.b22 - 160*m.b4*m.b20*m.b23 - 128
                       *m.b4*m.b20*m.b24 - 128*m.b4*m.b20*m.b25 - 128*m.b4*m.b20*m.b26 - 128*m.b4*m.b20*m.b27 - 96*m.b4*
                       m.b20*m.b28 - 64*m.b4*m.b20*m.b29 - 32*m.b4*m.b20*m.b30 - 224*m.b4*m.b21*m.b22 - 192*m.b4*m.b21*
                       m.b23 - 160*m.b4*m.b21*m.b24 - 128*m.b4*m.b21*m.b25 - 128*m.b4*m.b21*m.b26 - 128*m.b4*m.b21*m.b27
                        - 96*m.b4*m.b21*m.b28 - 64*m.b4*m.b21*m.b29 - 32*m.b4*m.b21*m.b30 - 224*m.b4*m.b22*m.b23 - 192*
                       m.b4*m.b22*m.b24 - 160*m.b4*m.b22*m.b25 - 128*m.b4*m.b22*m.b26 - 128*m.b4*m.b22*m.b27 - 96*m.b4*
                       m.b22*m.b28 - 64*m.b4*m.b22*m.b29 - 32*m.b4*m.b22*m.b30 - 224*m.b4*m.b23*m.b24 - 192*m.b4*m.b23*
                       m.b25 - 160*m.b4*m.b23*m.b26 - 128*m.b4*m.b23*m.b27 - 96*m.b4*m.b23*m.b28 - 64*m.b4*m.b23*m.b29
                        - 32*m.b4*m.b23*m.b30 - 224*m.b4*m.b24*m.b25 - 192*m.b4*m.b24*m.b26 - 160*m.b4*m.b24*m.b27 - 96*
                       m.b4*m.b24*m.b28 - 64*m.b4*m.b24*m.b29 - 32*m.b4*m.b24*m.b30 - 224*m.b4*m.b25*m.b26 - 192*m.b4*
                       m.b25*m.b27 - 128*m.b4*m.b25*m.b28 - 64*m.b4*m.b25*m.b29 - 32*m.b4*m.b25*m.b30 - 224*m.b4*m.b26*
                       m.b27 - 160*m.b4*m.b26*m.b28 - 96*m.b4*m.b26*m.b29 - 32*m.b4*m.b26*m.b30 - 192*m.b4*m.b27*m.b28
                        - 128*m.b4*m.b27*m.b29 - 64*m.b4*m.b27*m.b30 - 128*m.b4*m.b28*m.b29 - 64*m.b4*m.b28*m.b30 - 64*
                       m.b4*m.b29*m.b30 - 64*m.b5*m.b6*m.b7 - 96*m.b5*m.b6*m.b8 - 96*m.b5*m.b6*m.b9 - 96*m.b5*m.b6*m.b10
                        - 64*m.b5*m.b6*m.b11 - 64*m.b5*m.b6*m.b12 - 64*m.b5*m.b6*m.b13 - 64*m.b5*m.b6*m.b14 - 64*m.b5*
                       m.b6*m.b15 - 192*m.b5*m.b6*m.b16 - 320*m.b5*m.b6*m.b17 - 320*m.b5*m.b6*m.b18 - 320*m.b5*m.b6*
                       m.b19 - 320*m.b5*m.b6*m.b20 - 320*m.b5*m.b6*m.b21 - 320*m.b5*m.b6*m.b22 - 320*m.b5*m.b6*m.b23 - 
                       320*m.b5*m.b6*m.b24 - 320*m.b5*m.b6*m.b25 - 288*m.b5*m.b6*m.b26 - 224*m.b5*m.b6*m.b27 - 160*m.b5*
                       m.b6*m.b28 - 96*m.b5*m.b6*m.b29 - 32*m.b5*m.b6*m.b30 - 96*m.b5*m.b7*m.b8 - 64*m.b5*m.b7*m.b9 - 96
                       *m.b5*m.b7*m.b10 - 96*m.b5*m.b7*m.b11 - 64*m.b5*m.b7*m.b12 - 64*m.b5*m.b7*m.b13 - 64*m.b5*m.b7*
                       m.b14 - 192*m.b5*m.b7*m.b15 - 192*m.b5*m.b7*m.b16 - 320*m.b5*m.b7*m.b17 - 320*m.b5*m.b7*m.b18 - 
                       320*m.b5*m.b7*m.b19 - 320*m.b5*m.b7*m.b20 - 320*m.b5*m.b7*m.b21 - 320*m.b5*m.b7*m.b22 - 320*m.b5*
                       m.b7*m.b23 - 320*m.b5*m.b7*m.b24 - 288*m.b5*m.b7*m.b25 - 256*m.b5*m.b7*m.b26 - 192*m.b5*m.b7*
                       m.b27 - 128*m.b5*m.b7*m.b28 - 64*m.b5*m.b7*m.b29 - 32*m.b5*m.b7*m.b30 - 96*m.b5*m.b8*m.b9 - 96*
                       m.b5*m.b8*m.b10 - 64*m.b5*m.b8*m.b11 - 96*m.b5*m.b8*m.b12 - 64*m.b5*m.b8*m.b13 - 192*m.b5*m.b8*
                       m.b14 - 192*m.b5*m.b8*m.b15 - 192*m.b5*m.b8*m.b16 - 320*m.b5*m.b8*m.b17 - 320*m.b5*m.b8*m.b18 - 
                       320*m.b5*m.b8*m.b19 - 320*m.b5*m.b8*m.b20 - 320*m.b5*m.b8*m.b21 - 320*m.b5*m.b8*m.b22 - 320*m.b5*
                       m.b8*m.b23 - 288*m.b5*m.b8*m.b24 - 256*m.b5*m.b8*m.b25 - 224*m.b5*m.b8*m.b26 - 160*m.b5*m.b8*
                       m.b27 - 96*m.b5*m.b8*m.b28 - 64*m.b5*m.b8*m.b29 - 32*m.b5*m.b8*m.b30 - 96*m.b5*m.b9*m.b10 - 96*
                       m.b5*m.b9*m.b11 - 96*m.b5*m.b9*m.b12 - 192*m.b5*m.b9*m.b13 - 192*m.b5*m.b9*m.b14 - 192*m.b5*m.b9*
                       m.b15 - 192*m.b5*m.b9*m.b16 - 320*m.b5*m.b9*m.b17 - 320*m.b5*m.b9*m.b18 - 320*m.b5*m.b9*m.b19 - 
                       320*m.b5*m.b9*m.b20 - 320*m.b5*m.b9*m.b21 - 320*m.b5*m.b9*m.b22 - 288*m.b5*m.b9*m.b23 - 256*m.b5*
                       m.b9*m.b24 - 224*m.b5*m.b9*m.b25 - 192*m.b5*m.b9*m.b26 - 128*m.b5*m.b9*m.b27 - 96*m.b5*m.b9*m.b28
                        - 64*m.b5*m.b9*m.b29 - 32*m.b5*m.b9*m.b30 - 96*m.b5*m.b10*m.b11 - 224*m.b5*m.b10*m.b12 - 224*
                       m.b5*m.b10*m.b13 - 224*m.b5*m.b10*m.b14 - 160*m.b5*m.b10*m.b15 - 192*m.b5*m.b10*m.b16 - 320*m.b5*
                       m.b10*m.b17 - 320*m.b5*m.b10*m.b18 - 320*m.b5*m.b10*m.b19 - 320*m.b5*m.b10*m.b20 - 320*m.b5*m.b10
                       *m.b21 - 288*m.b5*m.b10*m.b22 - 256*m.b5*m.b10*m.b23 - 224*m.b5*m.b10*m.b24 - 192*m.b5*m.b10*
                       m.b25 - 160*m.b5*m.b10*m.b26 - 128*m.b5*m.b10*m.b27 - 96*m.b5*m.b10*m.b28 - 64*m.b5*m.b10*m.b29
                        - 32*m.b5*m.b10*m.b30 - 224*m.b5*m.b11*m.b12 - 224*m.b5*m.b11*m.b13 - 256*m.b5*m.b11*m.b14 - 224
                       *m.b5*m.b11*m.b15 - 192*m.b5*m.b11*m.b16 - 160*m.b5*m.b11*m.b17 - 320*m.b5*m.b11*m.b18 - 320*m.b5
                       *m.b11*m.b19 - 320*m.b5*m.b11*m.b20 - 288*m.b5*m.b11*m.b21 - 256*m.b5*m.b11*m.b22 - 224*m.b5*
                       m.b11*m.b23 - 192*m.b5*m.b11*m.b24 - 160*m.b5*m.b11*m.b25 - 160*m.b5*m.b11*m.b26 - 128*m.b5*m.b11
                       *m.b27 - 96*m.b5*m.b11*m.b28 - 64*m.b5*m.b11*m.b29 - 32*m.b5*m.b11*m.b30 - 224*m.b5*m.b12*m.b13
                        - 224*m.b5*m.b12*m.b14 - 256*m.b5*m.b12*m.b15 - 224*m.b5*m.b12*m.b16 - 320*m.b5*m.b12*m.b17 - 
                       320*m.b5*m.b12*m.b18 - 160*m.b5*m.b12*m.b19 - 288*m.b5*m.b12*m.b20 - 256*m.b5*m.b12*m.b21 - 224*
                       m.b5*m.b12*m.b22 - 192*m.b5*m.b12*m.b23 - 160*m.b5*m.b12*m.b24 - 160*m.b5*m.b12*m.b25 - 160*m.b5*
                       m.b12*m.b26 - 128*m.b5*m.b12*m.b27 - 96*m.b5*m.b12*m.b28 - 64*m.b5*m.b12*m.b29 - 32*m.b5*m.b12*
                       m.b30 - 224*m.b5*m.b13*m.b14 - 288*m.b5*m.b13*m.b15 - 256*m.b5*m.b13*m.b16 - 352*m.b5*m.b13*m.b17
                        - 320*m.b5*m.b13*m.b18 - 288*m.b5*m.b13*m.b19 - 256*m.b5*m.b13*m.b20 - 64*m.b5*m.b13*m.b21 - 192
                       *m.b5*m.b13*m.b22 - 160*m.b5*m.b13*m.b23 - 160*m.b5*m.b13*m.b24 - 160*m.b5*m.b13*m.b25 - 160*m.b5
                       *m.b13*m.b26 - 128*m.b5*m.b13*m.b27 - 96*m.b5*m.b13*m.b28 - 64*m.b5*m.b13*m.b29 - 32*m.b5*m.b13*
                       m.b30 - 224*m.b5*m.b14*m.b15 - 288*m.b5*m.b14*m.b16 - 384*m.b5*m.b14*m.b17 - 320*m.b5*m.b14*m.b18
                        - 256*m.b5*m.b14*m.b19 - 224*m.b5*m.b14*m.b20 - 192*m.b5*m.b14*m.b21 - 160*m.b5*m.b14*m.b22 - 
                       160*m.b5*m.b14*m.b24 - 160*m.b5*m.b14*m.b25 - 160*m.b5*m.b14*m.b26 - 128*m.b5*m.b14*m.b27 - 96*
                       m.b5*m.b14*m.b28 - 64*m.b5*m.b14*m.b29 - 32*m.b5*m.b14*m.b30 - 320*m.b5*m.b15*m.b16 - 384*m.b5*
                       m.b15*m.b17 - 320*m.b5*m.b15*m.b18 - 256*m.b5*m.b15*m.b19 - 192*m.b5*m.b15*m.b20 - 160*m.b5*m.b15
                       *m.b21 - 160*m.b5*m.b15*m.b22 - 160*m.b5*m.b15*m.b23 - 160*m.b5*m.b15*m.b24 - 160*m.b5*m.b15*
                       m.b26 - 128*m.b5*m.b15*m.b27 - 96*m.b5*m.b15*m.b28 - 64*m.b5*m.b15*m.b29 - 32*m.b5*m.b15*m.b30 - 
                       384*m.b5*m.b16*m.b17 - 320*m.b5*m.b16*m.b18 - 256*m.b5*m.b16*m.b19 - 192*m.b5*m.b16*m.b20 - 160*
                       m.b5*m.b16*m.b21 - 160*m.b5*m.b16*m.b22 - 160*m.b5*m.b16*m.b23 - 160*m.b5*m.b16*m.b24 - 160*m.b5*
                       m.b16*m.b25 - 160*m.b5*m.b16*m.b26 - 96*m.b5*m.b16*m.b28 - 64*m.b5*m.b16*m.b29 - 32*m.b5*m.b16*
                       m.b30 - 320*m.b5*m.b17*m.b18 - 256*m.b5*m.b17*m.b19 - 224*m.b5*m.b17*m.b20 - 192*m.b5*m.b17*m.b21
                        - 160*m.b5*m.b17*m.b22 - 160*m.b5*m.b17*m.b23 - 160*m.b5*m.b17*m.b24 - 160*m.b5*m.b17*m.b25 - 
                       160*m.b5*m.b17*m.b26 - 128*m.b5*m.b17*m.b27 - 96*m.b5*m.b17*m.b28 - 32*m.b5*m.b17*m.b30 - 288*
                       m.b5*m.b18*m.b19 - 256*m.b5*m.b18*m.b20 - 224*m.b5*m.b18*m.b21 - 192*m.b5*m.b18*m.b22 - 160*m.b5*
                       m.b18*m.b23 - 160*m.b5*m.b18*m.b24 - 160*m.b5*m.b18*m.b25 - 160*m.b5*m.b18*m.b26 - 128*m.b5*m.b18
                       *m.b27 - 96*m.b5*m.b18*m.b28 - 64*m.b5*m.b18*m.b29 - 32*m.b5*m.b18*m.b30 - 288*m.b5*m.b19*m.b20
                        - 256*m.b5*m.b19*m.b21 - 224*m.b5*m.b19*m.b22 - 192*m.b5*m.b19*m.b23 - 160*m.b5*m.b19*m.b24 - 
                       160*m.b5*m.b19*m.b25 - 160*m.b5*m.b19*m.b26 - 128*m.b5*m.b19*m.b27 - 96*m.b5*m.b19*m.b28 - 64*
                       m.b5*m.b19*m.b29 - 32*m.b5*m.b19*m.b30 - 288*m.b5*m.b20*m.b21 - 256*m.b5*m.b20*m.b22 - 224*m.b5*
                       m.b20*m.b23 - 192*m.b5*m.b20*m.b24 - 160*m.b5*m.b20*m.b25 - 160*m.b5*m.b20*m.b26 - 128*m.b5*m.b20
                       *m.b27 - 96*m.b5*m.b20*m.b28 - 64*m.b5*m.b20*m.b29 - 32*m.b5*m.b20*m.b30 - 288*m.b5*m.b21*m.b22
                        - 256*m.b5*m.b21*m.b23 - 224*m.b5*m.b21*m.b24 - 192*m.b5*m.b21*m.b25 - 160*m.b5*m.b21*m.b26 - 
                       128*m.b5*m.b21*m.b27 - 96*m.b5*m.b21*m.b28 - 64*m.b5*m.b21*m.b29 - 32*m.b5*m.b21*m.b30 - 288*m.b5
                       *m.b22*m.b23 - 256*m.b5*m.b22*m.b24 - 224*m.b5*m.b22*m.b25 - 192*m.b5*m.b22*m.b26 - 128*m.b5*
                       m.b22*m.b27 - 96*m.b5*m.b22*m.b28 - 64*m.b5*m.b22*m.b29 - 32*m.b5*m.b22*m.b30 - 288*m.b5*m.b23*
                       m.b24 - 256*m.b5*m.b23*m.b25 - 224*m.b5*m.b23*m.b26 - 160*m.b5*m.b23*m.b27 - 96*m.b5*m.b23*m.b28
                        - 64*m.b5*m.b23*m.b29 - 32*m.b5*m.b23*m.b30 - 288*m.b5*m.b24*m.b25 - 256*m.b5*m.b24*m.b26 - 192*
                       m.b5*m.b24*m.b27 - 128*m.b5*m.b24*m.b28 - 64*m.b5*m.b24*m.b29 - 32*m.b5*m.b24*m.b30 - 288*m.b5*
                       m.b25*m.b26 - 224*m.b5*m.b25*m.b27 - 160*m.b5*m.b25*m.b28 - 96*m.b5*m.b25*m.b29 - 32*m.b5*m.b25*
                       m.b30 - 256*m.b5*m.b26*m.b27 - 192*m.b5*m.b26*m.b28 - 128*m.b5*m.b26*m.b29 - 64*m.b5*m.b26*m.b30
                        - 192*m.b5*m.b27*m.b28 - 128*m.b5*m.b27*m.b29 - 64*m.b5*m.b27*m.b30 - 128*m.b5*m.b28*m.b29 - 64*
                       m.b5*m.b28*m.b30 - 64*m.b5*m.b29*m.b30 - 64*m.b6*m.b7*m.b8 - 96*m.b6*m.b7*m.b9 - 96*m.b6*m.b7*
                       m.b10 - 96*m.b6*m.b7*m.b11 - 96*m.b6*m.b7*m.b12 - 64*m.b6*m.b7*m.b13 - 64*m.b6*m.b7*m.b14 - 64*
                       m.b6*m.b7*m.b15 - 64*m.b6*m.b7*m.b16 - 224*m.b6*m.b7*m.b17 - 384*m.b6*m.b7*m.b18 - 384*m.b6*m.b7*
                       m.b19 - 384*m.b6*m.b7*m.b20 - 384*m.b6*m.b7*m.b21 - 384*m.b6*m.b7*m.b22 - 384*m.b6*m.b7*m.b23 - 
                       384*m.b6*m.b7*m.b24 - 352*m.b6*m.b7*m.b25 - 288*m.b6*m.b7*m.b26 - 224*m.b6*m.b7*m.b27 - 160*m.b6*
                       m.b7*m.b28 - 96*m.b6*m.b7*m.b29 - 32*m.b6*m.b7*m.b30 - 96*m.b6*m.b8*m.b9 - 64*m.b6*m.b8*m.b10 - 
                       96*m.b6*m.b8*m.b11 - 96*m.b6*m.b8*m.b12 - 96*m.b6*m.b8*m.b13 - 64*m.b6*m.b8*m.b14 - 64*m.b6*m.b8*
                       m.b15 - 224*m.b6*m.b8*m.b16 - 224*m.b6*m.b8*m.b17 - 384*m.b6*m.b8*m.b18 - 384*m.b6*m.b8*m.b19 - 
                       384*m.b6*m.b8*m.b20 - 384*m.b6*m.b8*m.b21 - 384*m.b6*m.b8*m.b22 - 384*m.b6*m.b8*m.b23 - 352*m.b6*
                       m.b8*m.b24 - 320*m.b6*m.b8*m.b25 - 256*m.b6*m.b8*m.b26 - 192*m.b6*m.b8*m.b27 - 128*m.b6*m.b8*
                       m.b28 - 64*m.b6*m.b8*m.b29 - 32*m.b6*m.b8*m.b30 - 96*m.b6*m.b9*m.b10 - 96*m.b6*m.b9*m.b11 - 64*
                       m.b6*m.b9*m.b12 - 96*m.b6*m.b9*m.b13 - 96*m.b6*m.b9*m.b14 - 224*m.b6*m.b9*m.b15 - 224*m.b6*m.b9*
                       m.b16 - 224*m.b6*m.b9*m.b17 - 384*m.b6*m.b9*m.b18 - 384*m.b6*m.b9*m.b19 - 384*m.b6*m.b9*m.b20 - 
                       384*m.b6*m.b9*m.b21 - 384*m.b6*m.b9*m.b22 - 352*m.b6*m.b9*m.b23 - 320*m.b6*m.b9*m.b24 - 288*m.b6*
                       m.b9*m.b25 - 224*m.b6*m.b9*m.b26 - 160*m.b6*m.b9*m.b27 - 96*m.b6*m.b9*m.b28 - 64*m.b6*m.b9*m.b29
                        - 32*m.b6*m.b9*m.b30 - 96*m.b6*m.b10*m.b11 - 96*m.b6*m.b10*m.b12 - 96*m.b6*m.b10*m.b13 - 256*
                       m.b6*m.b10*m.b14 - 256*m.b6*m.b10*m.b15 - 224*m.b6*m.b10*m.b16 - 224*m.b6*m.b10*m.b17 - 384*m.b6*
                       m.b10*m.b18 - 384*m.b6*m.b10*m.b19 - 384*m.b6*m.b10*m.b20 - 384*m.b6*m.b10*m.b21 - 352*m.b6*m.b10
                       *m.b22 - 320*m.b6*m.b10*m.b23 - 288*m.b6*m.b10*m.b24 - 256*m.b6*m.b10*m.b25 - 192*m.b6*m.b10*
                       m.b26 - 128*m.b6*m.b10*m.b27 - 96*m.b6*m.b10*m.b28 - 64*m.b6*m.b10*m.b29 - 32*m.b6*m.b10*m.b30 - 
                       96*m.b6*m.b11*m.b12 - 256*m.b6*m.b11*m.b13 - 256*m.b6*m.b11*m.b14 - 288*m.b6*m.b11*m.b15 - 224*
                       m.b6*m.b11*m.b16 - 224*m.b6*m.b11*m.b17 - 384*m.b6*m.b11*m.b18 - 384*m.b6*m.b11*m.b19 - 384*m.b6*
                       m.b11*m.b20 - 352*m.b6*m.b11*m.b21 - 320*m.b6*m.b11*m.b22 - 288*m.b6*m.b11*m.b23 - 256*m.b6*m.b11
                       *m.b24 - 224*m.b6*m.b11*m.b25 - 160*m.b6*m.b11*m.b26 - 128*m.b6*m.b11*m.b27 - 96*m.b6*m.b11*m.b28
                        - 64*m.b6*m.b11*m.b29 - 32*m.b6*m.b11*m.b30 - 256*m.b6*m.b12*m.b13 - 256*m.b6*m.b12*m.b14 - 320*
                       m.b6*m.b12*m.b15 - 288*m.b6*m.b12*m.b16 - 256*m.b6*m.b12*m.b17 - 192*m.b6*m.b12*m.b18 - 384*m.b6*
                       m.b12*m.b19 - 352*m.b6*m.b12*m.b20 - 320*m.b6*m.b12*m.b21 - 288*m.b6*m.b12*m.b22 - 256*m.b6*m.b12
                       *m.b23 - 224*m.b6*m.b12*m.b24 - 192*m.b6*m.b12*m.b25 - 160*m.b6*m.b12*m.b26 - 128*m.b6*m.b12*
                       m.b27 - 96*m.b6*m.b12*m.b28 - 64*m.b6*m.b12*m.b29 - 32*m.b6*m.b12*m.b30 - 256*m.b6*m.b13*m.b14 - 
                       256*m.b6*m.b13*m.b15 - 320*m.b6*m.b13*m.b16 - 288*m.b6*m.b13*m.b17 - 416*m.b6*m.b13*m.b18 - 352*
                       m.b6*m.b13*m.b19 - 128*m.b6*m.b13*m.b20 - 288*m.b6*m.b13*m.b21 - 256*m.b6*m.b13*m.b22 - 224*m.b6*
                       m.b13*m.b23 - 192*m.b6*m.b13*m.b24 - 192*m.b6*m.b13*m.b25 - 160*m.b6*m.b13*m.b26 - 128*m.b6*m.b13
                       *m.b27 - 96*m.b6*m.b13*m.b28 - 64*m.b6*m.b13*m.b29 - 32*m.b6*m.b13*m.b30 - 256*m.b6*m.b14*m.b15
                        - 352*m.b6*m.b14*m.b16 - 320*m.b6*m.b14*m.b17 - 416*m.b6*m.b14*m.b18 - 352*m.b6*m.b14*m.b19 - 
                       288*m.b6*m.b14*m.b20 - 256*m.b6*m.b14*m.b21 - 32*m.b6*m.b14*m.b22 - 192*m.b6*m.b14*m.b23 - 192*
                       m.b6*m.b14*m.b24 - 192*m.b6*m.b14*m.b25 - 160*m.b6*m.b14*m.b26 - 128*m.b6*m.b14*m.b27 - 96*m.b6*
                       m.b14*m.b28 - 64*m.b6*m.b14*m.b29 - 32*m.b6*m.b14*m.b30 - 256*m.b6*m.b15*m.b16 - 320*m.b6*m.b15*
                       m.b17 - 416*m.b6*m.b15*m.b18 - 352*m.b6*m.b15*m.b19 - 288*m.b6*m.b15*m.b20 - 224*m.b6*m.b15*m.b21
                        - 192*m.b6*m.b15*m.b22 - 192*m.b6*m.b15*m.b23 - 192*m.b6*m.b15*m.b25 - 160*m.b6*m.b15*m.b26 - 
                       128*m.b6*m.b15*m.b27 - 96*m.b6*m.b15*m.b28 - 64*m.b6*m.b15*m.b29 - 32*m.b6*m.b15*m.b30 - 320*m.b6
                       *m.b16*m.b17 - 416*m.b6*m.b16*m.b18 - 352*m.b6*m.b16*m.b19 - 288*m.b6*m.b16*m.b20 - 224*m.b6*
                       m.b16*m.b21 - 192*m.b6*m.b16*m.b22 - 192*m.b6*m.b16*m.b23 - 192*m.b6*m.b16*m.b24 - 192*m.b6*m.b16
                       *m.b25 - 128*m.b6*m.b16*m.b27 - 96*m.b6*m.b16*m.b28 - 64*m.b6*m.b16*m.b29 - 32*m.b6*m.b16*m.b30
                        - 416*m.b6*m.b17*m.b18 - 352*m.b6*m.b17*m.b19 - 288*m.b6*m.b17*m.b20 - 256*m.b6*m.b17*m.b21 - 
                       224*m.b6*m.b17*m.b22 - 192*m.b6*m.b17*m.b23 - 192*m.b6*m.b17*m.b24 - 192*m.b6*m.b17*m.b25 - 160*
                       m.b6*m.b17*m.b26 - 128*m.b6*m.b17*m.b27 - 64*m.b6*m.b17*m.b29 - 32*m.b6*m.b17*m.b30 - 352*m.b6*
                       m.b18*m.b19 - 320*m.b6*m.b18*m.b20 - 288*m.b6*m.b18*m.b21 - 256*m.b6*m.b18*m.b22 - 224*m.b6*m.b18
                       *m.b23 - 192*m.b6*m.b18*m.b24 - 192*m.b6*m.b18*m.b25 - 160*m.b6*m.b18*m.b26 - 128*m.b6*m.b18*
                       m.b27 - 96*m.b6*m.b18*m.b28 - 64*m.b6*m.b18*m.b29 - 352*m.b6*m.b19*m.b20 - 320*m.b6*m.b19*m.b21
                        - 288*m.b6*m.b19*m.b22 - 256*m.b6*m.b19*m.b23 - 224*m.b6*m.b19*m.b24 - 192*m.b6*m.b19*m.b25 - 
                       160*m.b6*m.b19*m.b26 - 128*m.b6*m.b19*m.b27 - 96*m.b6*m.b19*m.b28 - 64*m.b6*m.b19*m.b29 - 32*m.b6
                       *m.b19*m.b30 - 352*m.b6*m.b20*m.b21 - 320*m.b6*m.b20*m.b22 - 288*m.b6*m.b20*m.b23 - 256*m.b6*
                       m.b20*m.b24 - 224*m.b6*m.b20*m.b25 - 160*m.b6*m.b20*m.b26 - 128*m.b6*m.b20*m.b27 - 96*m.b6*m.b20*
                       m.b28 - 64*m.b6*m.b20*m.b29 - 32*m.b6*m.b20*m.b30 - 352*m.b6*m.b21*m.b22 - 320*m.b6*m.b21*m.b23
                        - 288*m.b6*m.b21*m.b24 - 256*m.b6*m.b21*m.b25 - 192*m.b6*m.b21*m.b26 - 128*m.b6*m.b21*m.b27 - 96
                       *m.b6*m.b21*m.b28 - 64*m.b6*m.b21*m.b29 - 32*m.b6*m.b21*m.b30 - 352*m.b6*m.b22*m.b23 - 320*m.b6*
                       m.b22*m.b24 - 288*m.b6*m.b22*m.b25 - 224*m.b6*m.b22*m.b26 - 160*m.b6*m.b22*m.b27 - 96*m.b6*m.b22*
                       m.b28 - 64*m.b6*m.b22*m.b29 - 32*m.b6*m.b22*m.b30 - 352*m.b6*m.b23*m.b24 - 320*m.b6*m.b23*m.b25
                        - 256*m.b6*m.b23*m.b26 - 192*m.b6*m.b23*m.b27 - 128*m.b6*m.b23*m.b28 - 64*m.b6*m.b23*m.b29 - 32*
                       m.b6*m.b23*m.b30 - 352*m.b6*m.b24*m.b25 - 288*m.b6*m.b24*m.b26 - 224*m.b6*m.b24*m.b27 - 160*m.b6*
                       m.b24*m.b28 - 96*m.b6*m.b24*m.b29 - 32*m.b6*m.b24*m.b30 - 320*m.b6*m.b25*m.b26 - 256*m.b6*m.b25*
                       m.b27 - 192*m.b6*m.b25*m.b28 - 128*m.b6*m.b25*m.b29 - 64*m.b6*m.b25*m.b30 - 256*m.b6*m.b26*m.b27
                        - 192*m.b6*m.b26*m.b28 - 128*m.b6*m.b26*m.b29 - 64*m.b6*m.b26*m.b30 - 192*m.b6*m.b27*m.b28 - 128
                       *m.b6*m.b27*m.b29 - 64*m.b6*m.b27*m.b30 - 128*m.b6*m.b28*m.b29 - 64*m.b6*m.b28*m.b30 - 64*m.b6*
                       m.b29*m.b30 - 64*m.b7*m.b8*m.b9 - 96*m.b7*m.b8*m.b10 - 96*m.b7*m.b8*m.b11 - 96*m.b7*m.b8*m.b12 - 
                       96*m.b7*m.b8*m.b13 - 96*m.b7*m.b8*m.b14 - 64*m.b7*m.b8*m.b15 - 64*m.b7*m.b8*m.b16 - 64*m.b7*m.b8*
                       m.b17 - 256*m.b7*m.b8*m.b18 - 448*m.b7*m.b8*m.b19 - 448*m.b7*m.b8*m.b20 - 448*m.b7*m.b8*m.b21 - 
                       448*m.b7*m.b8*m.b22 - 448*m.b7*m.b8*m.b23 - 416*m.b7*m.b8*m.b24 - 352*m.b7*m.b8*m.b25 - 288*m.b7*
                       m.b8*m.b26 - 224*m.b7*m.b8*m.b27 - 160*m.b7*m.b8*m.b28 - 96*m.b7*m.b8*m.b29 - 32*m.b7*m.b8*m.b30
                        - 96*m.b7*m.b9*m.b10 - 64*m.b7*m.b9*m.b11 - 96*m.b7*m.b9*m.b12 - 96*m.b7*m.b9*m.b13 - 128*m.b7*
                       m.b9*m.b14 - 96*m.b7*m.b9*m.b15 - 64*m.b7*m.b9*m.b16 - 256*m.b7*m.b9*m.b17 - 256*m.b7*m.b9*m.b18
                        - 448*m.b7*m.b9*m.b19 - 448*m.b7*m.b9*m.b20 - 448*m.b7*m.b9*m.b21 - 448*m.b7*m.b9*m.b22 - 416*
                       m.b7*m.b9*m.b23 - 384*m.b7*m.b9*m.b24 - 320*m.b7*m.b9*m.b25 - 256*m.b7*m.b9*m.b26 - 192*m.b7*m.b9
                       *m.b27 - 128*m.b7*m.b9*m.b28 - 64*m.b7*m.b9*m.b29 - 32*m.b7*m.b9*m.b30 - 96*m.b7*m.b10*m.b11 - 96
                       *m.b7*m.b10*m.b12 - 64*m.b7*m.b10*m.b13 - 96*m.b7*m.b10*m.b14 - 128*m.b7*m.b10*m.b15 - 288*m.b7*
                       m.b10*m.b16 - 256*m.b7*m.b10*m.b17 - 256*m.b7*m.b10*m.b18 - 448*m.b7*m.b10*m.b19 - 448*m.b7*m.b10
                       *m.b20 - 448*m.b7*m.b10*m.b21 - 416*m.b7*m.b10*m.b22 - 384*m.b7*m.b10*m.b23 - 352*m.b7*m.b10*
                       m.b24 - 288*m.b7*m.b10*m.b25 - 224*m.b7*m.b10*m.b26 - 160*m.b7*m.b10*m.b27 - 96*m.b7*m.b10*m.b28
                        - 64*m.b7*m.b10*m.b29 - 32*m.b7*m.b10*m.b30 - 96*m.b7*m.b11*m.b12 - 96*m.b7*m.b11*m.b13 - 96*
                       m.b7*m.b11*m.b14 - 320*m.b7*m.b11*m.b15 - 320*m.b7*m.b11*m.b16 - 288*m.b7*m.b11*m.b17 - 256*m.b7*
                       m.b11*m.b18 - 448*m.b7*m.b11*m.b19 - 448*m.b7*m.b11*m.b20 - 416*m.b7*m.b11*m.b21 - 384*m.b7*m.b11
                       *m.b22 - 352*m.b7*m.b11*m.b23 - 320*m.b7*m.b11*m.b24 - 256*m.b7*m.b11*m.b25 - 192*m.b7*m.b11*
                       m.b26 - 128*m.b7*m.b11*m.b27 - 96*m.b7*m.b11*m.b28 - 64*m.b7*m.b11*m.b29 - 32*m.b7*m.b11*m.b30 - 
                       96*m.b7*m.b12*m.b13 - 288*m.b7*m.b12*m.b14 - 288*m.b7*m.b12*m.b15 - 352*m.b7*m.b12*m.b16 - 288*
                       m.b7*m.b12*m.b17 - 288*m.b7*m.b12*m.b18 - 448*m.b7*m.b12*m.b19 - 416*m.b7*m.b12*m.b20 - 384*m.b7*
                       m.b12*m.b21 - 352*m.b7*m.b12*m.b22 - 320*m.b7*m.b12*m.b23 - 288*m.b7*m.b12*m.b24 - 224*m.b7*m.b12
                       *m.b25 - 160*m.b7*m.b12*m.b26 - 128*m.b7*m.b12*m.b27 - 96*m.b7*m.b12*m.b28 - 64*m.b7*m.b12*m.b29
                        - 32*m.b7*m.b12*m.b30 - 288*m.b7*m.b13*m.b14 - 288*m.b7*m.b13*m.b15 - 384*m.b7*m.b13*m.b16 - 352
                       *m.b7*m.b13*m.b17 - 320*m.b7*m.b13*m.b18 - 224*m.b7*m.b13*m.b19 - 384*m.b7*m.b13*m.b20 - 352*m.b7
                       *m.b13*m.b21 - 320*m.b7*m.b13*m.b22 - 288*m.b7*m.b13*m.b23 - 256*m.b7*m.b13*m.b24 - 192*m.b7*
                       m.b13*m.b25 - 160*m.b7*m.b13*m.b26 - 128*m.b7*m.b13*m.b27 - 96*m.b7*m.b13*m.b28 - 64*m.b7*m.b13*
                       m.b29 - 32*m.b7*m.b13*m.b30 - 288*m.b7*m.b14*m.b15 - 288*m.b7*m.b14*m.b16 - 384*m.b7*m.b14*m.b17
                        - 320*m.b7*m.b14*m.b18 - 448*m.b7*m.b14*m.b19 - 384*m.b7*m.b14*m.b20 - 96*m.b7*m.b14*m.b21 - 288
                       *m.b7*m.b14*m.b22 - 256*m.b7*m.b14*m.b23 - 224*m.b7*m.b14*m.b24 - 192*m.b7*m.b14*m.b25 - 160*m.b7
                       *m.b14*m.b26 - 128*m.b7*m.b14*m.b27 - 96*m.b7*m.b14*m.b28 - 64*m.b7*m.b14*m.b29 - 32*m.b7*m.b14*
                       m.b30 - 288*m.b7*m.b15*m.b16 - 384*m.b7*m.b15*m.b17 - 320*m.b7*m.b15*m.b18 - 448*m.b7*m.b15*m.b19
                        - 384*m.b7*m.b15*m.b20 - 320*m.b7*m.b15*m.b21 - 256*m.b7*m.b15*m.b22 - 224*m.b7*m.b15*m.b24 - 
                       192*m.b7*m.b15*m.b25 - 160*m.b7*m.b15*m.b26 - 128*m.b7*m.b15*m.b27 - 96*m.b7*m.b15*m.b28 - 64*
                       m.b7*m.b15*m.b29 - 32*m.b7*m.b15*m.b30 - 224*m.b7*m.b16*m.b17 - 320*m.b7*m.b16*m.b18 - 448*m.b7*
                       m.b16*m.b19 - 384*m.b7*m.b16*m.b20 - 320*m.b7*m.b16*m.b21 - 256*m.b7*m.b16*m.b22 - 224*m.b7*m.b16
                       *m.b23 - 224*m.b7*m.b16*m.b24 - 160*m.b7*m.b16*m.b26 - 128*m.b7*m.b16*m.b27 - 96*m.b7*m.b16*m.b28
                        - 64*m.b7*m.b16*m.b29 - 32*m.b7*m.b16*m.b30 - 320*m.b7*m.b17*m.b18 - 448*m.b7*m.b17*m.b19 - 384*
                       m.b7*m.b17*m.b20 - 320*m.b7*m.b17*m.b21 - 288*m.b7*m.b17*m.b22 - 256*m.b7*m.b17*m.b23 - 224*m.b7*
                       m.b17*m.b24 - 192*m.b7*m.b17*m.b25 - 160*m.b7*m.b17*m.b26 - 96*m.b7*m.b17*m.b28 - 64*m.b7*m.b17*
                       m.b29 - 32*m.b7*m.b17*m.b30 - 448*m.b7*m.b18*m.b19 - 384*m.b7*m.b18*m.b20 - 352*m.b7*m.b18*m.b21
                        - 320*m.b7*m.b18*m.b22 - 288*m.b7*m.b18*m.b23 - 256*m.b7*m.b18*m.b24 - 192*m.b7*m.b18*m.b25 - 
                       160*m.b7*m.b18*m.b26 - 128*m.b7*m.b18*m.b27 - 96*m.b7*m.b18*m.b28 - 32*m.b7*m.b18*m.b30 - 416*
                       m.b7*m.b19*m.b20 - 384*m.b7*m.b19*m.b21 - 352*m.b7*m.b19*m.b22 - 320*m.b7*m.b19*m.b23 - 288*m.b7*
                       m.b19*m.b24 - 224*m.b7*m.b19*m.b25 - 160*m.b7*m.b19*m.b26 - 128*m.b7*m.b19*m.b27 - 96*m.b7*m.b19*
                       m.b28 - 64*m.b7*m.b19*m.b29 - 32*m.b7*m.b19*m.b30 - 416*m.b7*m.b20*m.b21 - 384*m.b7*m.b20*m.b22
                        - 352*m.b7*m.b20*m.b23 - 320*m.b7*m.b20*m.b24 - 256*m.b7*m.b20*m.b25 - 192*m.b7*m.b20*m.b26 - 
                       128*m.b7*m.b20*m.b27 - 96*m.b7*m.b20*m.b28 - 64*m.b7*m.b20*m.b29 - 32*m.b7*m.b20*m.b30 - 416*m.b7
                       *m.b21*m.b22 - 384*m.b7*m.b21*m.b23 - 352*m.b7*m.b21*m.b24 - 288*m.b7*m.b21*m.b25 - 224*m.b7*
                       m.b21*m.b26 - 160*m.b7*m.b21*m.b27 - 96*m.b7*m.b21*m.b28 - 64*m.b7*m.b21*m.b29 - 32*m.b7*m.b21*
                       m.b30 - 416*m.b7*m.b22*m.b23 - 384*m.b7*m.b22*m.b24 - 320*m.b7*m.b22*m.b25 - 256*m.b7*m.b22*m.b26
                        - 192*m.b7*m.b22*m.b27 - 128*m.b7*m.b22*m.b28 - 64*m.b7*m.b22*m.b29 - 32*m.b7*m.b22*m.b30 - 416*
                       m.b7*m.b23*m.b24 - 352*m.b7*m.b23*m.b25 - 288*m.b7*m.b23*m.b26 - 224*m.b7*m.b23*m.b27 - 160*m.b7*
                       m.b23*m.b28 - 96*m.b7*m.b23*m.b29 - 32*m.b7*m.b23*m.b30 - 384*m.b7*m.b24*m.b25 - 320*m.b7*m.b24*
                       m.b26 - 256*m.b7*m.b24*m.b27 - 192*m.b7*m.b24*m.b28 - 128*m.b7*m.b24*m.b29 - 64*m.b7*m.b24*m.b30
                        - 320*m.b7*m.b25*m.b26 - 256*m.b7*m.b25*m.b27 - 192*m.b7*m.b25*m.b28 - 128*m.b7*m.b25*m.b29 - 64
                       *m.b7*m.b25*m.b30 - 256*m.b7*m.b26*m.b27 - 192*m.b7*m.b26*m.b28 - 128*m.b7*m.b26*m.b29 - 64*m.b7*
                       m.b26*m.b30 - 192*m.b7*m.b27*m.b28 - 128*m.b7*m.b27*m.b29 - 64*m.b7*m.b27*m.b30 - 128*m.b7*m.b28*
                       m.b29 - 64*m.b7*m.b28*m.b30 - 64*m.b7*m.b29*m.b30 - 64*m.b8*m.b9*m.b10 - 96*m.b8*m.b9*m.b11 - 96*
                       m.b8*m.b9*m.b12 - 96*m.b8*m.b9*m.b13 - 96*m.b8*m.b9*m.b14 - 128*m.b8*m.b9*m.b15 - 96*m.b8*m.b9*
                       m.b16 - 64*m.b8*m.b9*m.b17 - 64*m.b8*m.b9*m.b18 - 288*m.b8*m.b9*m.b19 - 512*m.b8*m.b9*m.b20 - 512
                       *m.b8*m.b9*m.b21 - 512*m.b8*m.b9*m.b22 - 480*m.b8*m.b9*m.b23 - 416*m.b8*m.b9*m.b24 - 352*m.b8*
                       m.b9*m.b25 - 288*m.b8*m.b9*m.b26 - 224*m.b8*m.b9*m.b27 - 160*m.b8*m.b9*m.b28 - 96*m.b8*m.b9*m.b29
                        - 32*m.b8*m.b9*m.b30 - 96*m.b8*m.b10*m.b11 - 64*m.b8*m.b10*m.b12 - 96*m.b8*m.b10*m.b13 - 96*m.b8
                       *m.b10*m.b14 - 160*m.b8*m.b10*m.b15 - 128*m.b8*m.b10*m.b16 - 96*m.b8*m.b10*m.b17 - 288*m.b8*m.b10
                       *m.b18 - 288*m.b8*m.b10*m.b19 - 512*m.b8*m.b10*m.b20 - 512*m.b8*m.b10*m.b21 - 480*m.b8*m.b10*
                       m.b22 - 448*m.b8*m.b10*m.b23 - 384*m.b8*m.b10*m.b24 - 320*m.b8*m.b10*m.b25 - 256*m.b8*m.b10*m.b26
                        - 192*m.b8*m.b10*m.b27 - 128*m.b8*m.b10*m.b28 - 64*m.b8*m.b10*m.b29 - 32*m.b8*m.b10*m.b30 - 96*
                       m.b8*m.b11*m.b12 - 96*m.b8*m.b11*m.b13 - 64*m.b8*m.b11*m.b14 - 96*m.b8*m.b11*m.b15 - 160*m.b8*
                       m.b11*m.b16 - 352*m.b8*m.b11*m.b17 - 320*m.b8*m.b11*m.b18 - 288*m.b8*m.b11*m.b19 - 512*m.b8*m.b11
                       *m.b20 - 480*m.b8*m.b11*m.b21 - 448*m.b8*m.b11*m.b22 - 416*m.b8*m.b11*m.b23 - 352*m.b8*m.b11*
                       m.b24 - 288*m.b8*m.b11*m.b25 - 224*m.b8*m.b11*m.b26 - 160*m.b8*m.b11*m.b27 - 96*m.b8*m.b11*m.b28
                        - 64*m.b8*m.b11*m.b29 - 32*m.b8*m.b11*m.b30 - 96*m.b8*m.b12*m.b13 - 96*m.b8*m.b12*m.b14 - 96*
                       m.b8*m.b12*m.b15 - 384*m.b8*m.b12*m.b16 - 384*m.b8*m.b12*m.b17 - 352*m.b8*m.b12*m.b18 - 320*m.b8*
                       m.b12*m.b19 - 480*m.b8*m.b12*m.b20 - 448*m.b8*m.b12*m.b21 - 416*m.b8*m.b12*m.b22 - 384*m.b8*m.b12
                       *m.b23 - 320*m.b8*m.b12*m.b24 - 256*m.b8*m.b12*m.b25 - 192*m.b8*m.b12*m.b26 - 128*m.b8*m.b12*
                       m.b27 - 96*m.b8*m.b12*m.b28 - 64*m.b8*m.b12*m.b29 - 32*m.b8*m.b12*m.b30 - 96*m.b8*m.b13*m.b14 - 
                       320*m.b8*m.b13*m.b15 - 320*m.b8*m.b13*m.b16 - 416*m.b8*m.b13*m.b17 - 352*m.b8*m.b13*m.b18 - 320*
                       m.b8*m.b13*m.b19 - 480*m.b8*m.b13*m.b20 - 416*m.b8*m.b13*m.b21 - 384*m.b8*m.b13*m.b22 - 352*m.b8*
                       m.b13*m.b23 - 288*m.b8*m.b13*m.b24 - 224*m.b8*m.b13*m.b25 - 160*m.b8*m.b13*m.b26 - 128*m.b8*m.b13
                       *m.b27 - 96*m.b8*m.b13*m.b28 - 64*m.b8*m.b13*m.b29 - 32*m.b8*m.b13*m.b30 - 320*m.b8*m.b14*m.b15
                        - 320*m.b8*m.b14*m.b16 - 448*m.b8*m.b14*m.b17 - 384*m.b8*m.b14*m.b18 - 320*m.b8*m.b14*m.b19 - 
                       224*m.b8*m.b14*m.b20 - 416*m.b8*m.b14*m.b21 - 352*m.b8*m.b14*m.b22 - 320*m.b8*m.b14*m.b23 - 256*
                       m.b8*m.b14*m.b24 - 192*m.b8*m.b14*m.b25 - 160*m.b8*m.b14*m.b26 - 128*m.b8*m.b14*m.b27 - 96*m.b8*
                       m.b14*m.b28 - 64*m.b8*m.b14*m.b29 - 32*m.b8*m.b14*m.b30 - 320*m.b8*m.b15*m.b16 - 288*m.b8*m.b15*
                       m.b17 - 384*m.b8*m.b15*m.b18 - 320*m.b8*m.b15*m.b19 - 480*m.b8*m.b15*m.b20 - 416*m.b8*m.b15*m.b21
                        - 96*m.b8*m.b15*m.b22 - 288*m.b8*m.b15*m.b23 - 224*m.b8*m.b15*m.b24 - 192*m.b8*m.b15*m.b25 - 160
                       *m.b8*m.b15*m.b26 - 128*m.b8*m.b15*m.b27 - 96*m.b8*m.b15*m.b28 - 64*m.b8*m.b15*m.b29 - 32*m.b8*
                       m.b15*m.b30 - 256*m.b8*m.b16*m.b17 - 384*m.b8*m.b16*m.b18 - 320*m.b8*m.b16*m.b19 - 480*m.b8*m.b16
                       *m.b20 - 416*m.b8*m.b16*m.b21 - 352*m.b8*m.b16*m.b22 - 288*m.b8*m.b16*m.b23 - 192*m.b8*m.b16*
                       m.b25 - 160*m.b8*m.b16*m.b26 - 128*m.b8*m.b16*m.b27 - 96*m.b8*m.b16*m.b28 - 64*m.b8*m.b16*m.b29
                        - 32*m.b8*m.b16*m.b30 - 192*m.b8*m.b17*m.b18 - 320*m.b8*m.b17*m.b19 - 480*m.b8*m.b17*m.b20 - 416
                       *m.b8*m.b17*m.b21 - 352*m.b8*m.b17*m.b22 - 320*m.b8*m.b17*m.b23 - 256*m.b8*m.b17*m.b24 - 192*m.b8
                       *m.b17*m.b25 - 128*m.b8*m.b17*m.b27 - 96*m.b8*m.b17*m.b28 - 64*m.b8*m.b17*m.b29 - 32*m.b8*m.b17*
                       m.b30 - 320*m.b8*m.b18*m.b19 - 480*m.b8*m.b18*m.b20 - 416*m.b8*m.b18*m.b21 - 384*m.b8*m.b18*m.b22
                        - 352*m.b8*m.b18*m.b23 - 288*m.b8*m.b18*m.b24 - 224*m.b8*m.b18*m.b25 - 160*m.b8*m.b18*m.b26 - 
                       128*m.b8*m.b18*m.b27 - 64*m.b8*m.b18*m.b29 - 32*m.b8*m.b18*m.b30 - 480*m.b8*m.b19*m.b20 - 448*
                       m.b8*m.b19*m.b21 - 416*m.b8*m.b19*m.b22 - 384*m.b8*m.b19*m.b23 - 320*m.b8*m.b19*m.b24 - 256*m.b8*
                       m.b19*m.b25 - 192*m.b8*m.b19*m.b26 - 128*m.b8*m.b19*m.b27 - 96*m.b8*m.b19*m.b28 - 64*m.b8*m.b19*
                       m.b29 - 480*m.b8*m.b20*m.b21 - 448*m.b8*m.b20*m.b22 - 416*m.b8*m.b20*m.b23 - 352*m.b8*m.b20*m.b24
                        - 288*m.b8*m.b20*m.b25 - 224*m.b8*m.b20*m.b26 - 160*m.b8*m.b20*m.b27 - 96*m.b8*m.b20*m.b28 - 64*
                       m.b8*m.b20*m.b29 - 32*m.b8*m.b20*m.b30 - 480*m.b8*m.b21*m.b22 - 448*m.b8*m.b21*m.b23 - 384*m.b8*
                       m.b21*m.b24 - 320*m.b8*m.b21*m.b25 - 256*m.b8*m.b21*m.b26 - 192*m.b8*m.b21*m.b27 - 128*m.b8*m.b21
                       *m.b28 - 64*m.b8*m.b21*m.b29 - 32*m.b8*m.b21*m.b30 - 480*m.b8*m.b22*m.b23 - 416*m.b8*m.b22*m.b24
                        - 352*m.b8*m.b22*m.b25 - 288*m.b8*m.b22*m.b26 - 224*m.b8*m.b22*m.b27 - 160*m.b8*m.b22*m.b28 - 96
                       *m.b8*m.b22*m.b29 - 32*m.b8*m.b22*m.b30 - 448*m.b8*m.b23*m.b24 - 384*m.b8*m.b23*m.b25 - 320*m.b8*
                       m.b23*m.b26 - 256*m.b8*m.b23*m.b27 - 192*m.b8*m.b23*m.b28 - 128*m.b8*m.b23*m.b29 - 64*m.b8*m.b23*
                       m.b30 - 384*m.b8*m.b24*m.b25 - 320*m.b8*m.b24*m.b26 - 256*m.b8*m.b24*m.b27 - 192*m.b8*m.b24*m.b28
                        - 128*m.b8*m.b24*m.b29 - 64*m.b8*m.b24*m.b30 - 320*m.b8*m.b25*m.b26 - 256*m.b8*m.b25*m.b27 - 192
                       *m.b8*m.b25*m.b28 - 128*m.b8*m.b25*m.b29 - 64*m.b8*m.b25*m.b30 - 256*m.b8*m.b26*m.b27 - 192*m.b8*
                       m.b26*m.b28 - 128*m.b8*m.b26*m.b29 - 64*m.b8*m.b26*m.b30 - 192*m.b8*m.b27*m.b28 - 128*m.b8*m.b27*
                       m.b29 - 64*m.b8*m.b27*m.b30 - 128*m.b8*m.b28*m.b29 - 64*m.b8*m.b28*m.b30 - 64*m.b8*m.b29*m.b30 - 
                       64*m.b9*m.b10*m.b11 - 96*m.b9*m.b10*m.b12 - 96*m.b9*m.b10*m.b13 - 96*m.b9*m.b10*m.b14 - 96*m.b9*
                       m.b10*m.b15 - 160*m.b9*m.b10*m.b16 - 128*m.b9*m.b10*m.b17 - 96*m.b9*m.b10*m.b18 - 64*m.b9*m.b10*
                       m.b19 - 320*m.b9*m.b10*m.b20 - 576*m.b9*m.b10*m.b21 - 544*m.b9*m.b10*m.b22 - 480*m.b9*m.b10*m.b23
                        - 416*m.b9*m.b10*m.b24 - 352*m.b9*m.b10*m.b25 - 288*m.b9*m.b10*m.b26 - 224*m.b9*m.b10*m.b27 - 
                       160*m.b9*m.b10*m.b28 - 96*m.b9*m.b10*m.b29 - 32*m.b9*m.b10*m.b30 - 96*m.b9*m.b11*m.b12 - 64*m.b9*
                       m.b11*m.b13 - 96*m.b9*m.b11*m.b14 - 96*m.b9*m.b11*m.b15 - 192*m.b9*m.b11*m.b16 - 160*m.b9*m.b11*
                       m.b17 - 128*m.b9*m.b11*m.b18 - 352*m.b9*m.b11*m.b19 - 320*m.b9*m.b11*m.b20 - 544*m.b9*m.b11*m.b21
                        - 512*m.b9*m.b11*m.b22 - 448*m.b9*m.b11*m.b23 - 384*m.b9*m.b11*m.b24 - 320*m.b9*m.b11*m.b25 - 
                       256*m.b9*m.b11*m.b26 - 192*m.b9*m.b11*m.b27 - 128*m.b9*m.b11*m.b28 - 64*m.b9*m.b11*m.b29 - 32*
                       m.b9*m.b11*m.b30 - 96*m.b9*m.b12*m.b13 - 96*m.b9*m.b12*m.b14 - 64*m.b9*m.b12*m.b15 - 96*m.b9*
                       m.b12*m.b16 - 192*m.b9*m.b12*m.b17 - 416*m.b9*m.b12*m.b18 - 384*m.b9*m.b12*m.b19 - 320*m.b9*m.b12
                       *m.b20 - 512*m.b9*m.b12*m.b21 - 480*m.b9*m.b12*m.b22 - 416*m.b9*m.b12*m.b23 - 352*m.b9*m.b12*
                       m.b24 - 288*m.b9*m.b12*m.b25 - 224*m.b9*m.b12*m.b26 - 160*m.b9*m.b12*m.b27 - 96*m.b9*m.b12*m.b28
                        - 64*m.b9*m.b12*m.b29 - 32*m.b9*m.b12*m.b30 - 96*m.b9*m.b13*m.b14 - 96*m.b9*m.b13*m.b15 - 96*
                       m.b9*m.b13*m.b16 - 448*m.b9*m.b13*m.b17 - 448*m.b9*m.b13*m.b18 - 384*m.b9*m.b13*m.b19 - 320*m.b9*
                       m.b13*m.b20 - 512*m.b9*m.b13*m.b21 - 448*m.b9*m.b13*m.b22 - 384*m.b9*m.b13*m.b23 - 320*m.b9*m.b13
                       *m.b24 - 256*m.b9*m.b13*m.b25 - 192*m.b9*m.b13*m.b26 - 128*m.b9*m.b13*m.b27 - 96*m.b9*m.b13*m.b28
                        - 64*m.b9*m.b13*m.b29 - 32*m.b9*m.b13*m.b30 - 96*m.b9*m.b14*m.b15 - 352*m.b9*m.b14*m.b16 - 352*
                       m.b9*m.b14*m.b17 - 448*m.b9*m.b14*m.b18 - 352*m.b9*m.b14*m.b19 - 320*m.b9*m.b14*m.b20 - 512*m.b9*
                       m.b14*m.b21 - 448*m.b9*m.b14*m.b22 - 352*m.b9*m.b14*m.b23 - 288*m.b9*m.b14*m.b24 - 224*m.b9*m.b14
                       *m.b25 - 160*m.b9*m.b14*m.b26 - 128*m.b9*m.b14*m.b27 - 96*m.b9*m.b14*m.b28 - 64*m.b9*m.b14*m.b29
                        - 32*m.b9*m.b14*m.b30 - 352*m.b9*m.b15*m.b16 - 320*m.b9*m.b15*m.b17 - 448*m.b9*m.b15*m.b18 - 384
                       *m.b9*m.b15*m.b19 - 320*m.b9*m.b15*m.b20 - 224*m.b9*m.b15*m.b21 - 448*m.b9*m.b15*m.b22 - 352*m.b9
                       *m.b15*m.b23 - 256*m.b9*m.b15*m.b24 - 192*m.b9*m.b15*m.b25 - 160*m.b9*m.b15*m.b26 - 128*m.b9*
                       m.b15*m.b27 - 96*m.b9*m.b15*m.b28 - 64*m.b9*m.b15*m.b29 - 32*m.b9*m.b15*m.b30 - 288*m.b9*m.b16*
                       m.b17 - 256*m.b9*m.b16*m.b18 - 384*m.b9*m.b16*m.b19 - 320*m.b9*m.b16*m.b20 - 512*m.b9*m.b16*m.b21
                        - 448*m.b9*m.b16*m.b22 - 96*m.b9*m.b16*m.b23 - 256*m.b9*m.b16*m.b24 - 192*m.b9*m.b16*m.b25 - 160
                       *m.b9*m.b16*m.b26 - 128*m.b9*m.b16*m.b27 - 96*m.b9*m.b16*m.b28 - 64*m.b9*m.b16*m.b29 - 32*m.b9*
                       m.b16*m.b30 - 224*m.b9*m.b17*m.b18 - 384*m.b9*m.b17*m.b19 - 320*m.b9*m.b17*m.b20 - 512*m.b9*m.b17
                       *m.b21 - 448*m.b9*m.b17*m.b22 - 352*m.b9*m.b17*m.b23 - 288*m.b9*m.b17*m.b24 - 32*m.b9*m.b17*m.b25
                        - 160*m.b9*m.b17*m.b26 - 128*m.b9*m.b17*m.b27 - 96*m.b9*m.b17*m.b28 - 64*m.b9*m.b17*m.b29 - 32*
                       m.b9*m.b17*m.b30 - 160*m.b9*m.b18*m.b19 - 320*m.b9*m.b18*m.b20 - 512*m.b9*m.b18*m.b21 - 448*m.b9*
                       m.b18*m.b22 - 384*m.b9*m.b18*m.b23 - 320*m.b9*m.b18*m.b24 - 256*m.b9*m.b18*m.b25 - 192*m.b9*m.b18
                       *m.b26 - 96*m.b9*m.b18*m.b28 - 64*m.b9*m.b18*m.b29 - 32*m.b9*m.b18*m.b30 - 320*m.b9*m.b19*m.b20
                        - 512*m.b9*m.b19*m.b21 - 480*m.b9*m.b19*m.b22 - 416*m.b9*m.b19*m.b23 - 352*m.b9*m.b19*m.b24 - 
                       288*m.b9*m.b19*m.b25 - 224*m.b9*m.b19*m.b26 - 160*m.b9*m.b19*m.b27 - 96*m.b9*m.b19*m.b28 - 32*
                       m.b9*m.b19*m.b30 - 544*m.b9*m.b20*m.b21 - 512*m.b9*m.b20*m.b22 - 448*m.b9*m.b20*m.b23 - 384*m.b9*
                       m.b20*m.b24 - 320*m.b9*m.b20*m.b25 - 256*m.b9*m.b20*m.b26 - 192*m.b9*m.b20*m.b27 - 128*m.b9*m.b20
                       *m.b28 - 64*m.b9*m.b20*m.b29 - 32*m.b9*m.b20*m.b30 - 544*m.b9*m.b21*m.b22 - 480*m.b9*m.b21*m.b23
                        - 416*m.b9*m.b21*m.b24 - 352*m.b9*m.b21*m.b25 - 288*m.b9*m.b21*m.b26 - 224*m.b9*m.b21*m.b27 - 
                       160*m.b9*m.b21*m.b28 - 96*m.b9*m.b21*m.b29 - 32*m.b9*m.b21*m.b30 - 512*m.b9*m.b22*m.b23 - 448*
                       m.b9*m.b22*m.b24 - 384*m.b9*m.b22*m.b25 - 320*m.b9*m.b22*m.b26 - 256*m.b9*m.b22*m.b27 - 192*m.b9*
                       m.b22*m.b28 - 128*m.b9*m.b22*m.b29 - 64*m.b9*m.b22*m.b30 - 448*m.b9*m.b23*m.b24 - 384*m.b9*m.b23*
                       m.b25 - 320*m.b9*m.b23*m.b26 - 256*m.b9*m.b23*m.b27 - 192*m.b9*m.b23*m.b28 - 128*m.b9*m.b23*m.b29
                        - 64*m.b9*m.b23*m.b30 - 384*m.b9*m.b24*m.b25 - 320*m.b9*m.b24*m.b26 - 256*m.b9*m.b24*m.b27 - 192
                       *m.b9*m.b24*m.b28 - 128*m.b9*m.b24*m.b29 - 64*m.b9*m.b24*m.b30 - 320*m.b9*m.b25*m.b26 - 256*m.b9*
                       m.b25*m.b27 - 192*m.b9*m.b25*m.b28 - 128*m.b9*m.b25*m.b29 - 64*m.b9*m.b25*m.b30 - 256*m.b9*m.b26*
                       m.b27 - 192*m.b9*m.b26*m.b28 - 128*m.b9*m.b26*m.b29 - 64*m.b9*m.b26*m.b30 - 192*m.b9*m.b27*m.b28
                        - 128*m.b9*m.b27*m.b29 - 64*m.b9*m.b27*m.b30 - 128*m.b9*m.b28*m.b29 - 64*m.b9*m.b28*m.b30 - 64*
                       m.b9*m.b29*m.b30 - 64*m.b10*m.b11*m.b12 - 96*m.b10*m.b11*m.b13 - 96*m.b10*m.b11*m.b14 - 96*m.b10*
                       m.b11*m.b15 - 96*m.b10*m.b11*m.b16 - 192*m.b10*m.b11*m.b17 - 160*m.b10*m.b11*m.b18 - 128*m.b10*
                       m.b11*m.b19 - 96*m.b10*m.b11*m.b20 - 320*m.b10*m.b11*m.b21 - 544*m.b10*m.b11*m.b22 - 480*m.b10*
                       m.b11*m.b23 - 416*m.b10*m.b11*m.b24 - 352*m.b10*m.b11*m.b25 - 288*m.b10*m.b11*m.b26 - 224*m.b10*
                       m.b11*m.b27 - 160*m.b10*m.b11*m.b28 - 96*m.b10*m.b11*m.b29 - 32*m.b10*m.b11*m.b30 - 96*m.b10*
                       m.b12*m.b13 - 64*m.b10*m.b12*m.b14 - 96*m.b10*m.b12*m.b15 - 96*m.b10*m.b12*m.b16 - 224*m.b10*
                       m.b12*m.b17 - 192*m.b10*m.b12*m.b18 - 160*m.b10*m.b12*m.b19 - 384*m.b10*m.b12*m.b20 - 320*m.b10*
                       m.b12*m.b21 - 512*m.b10*m.b12*m.b22 - 448*m.b10*m.b12*m.b23 - 384*m.b10*m.b12*m.b24 - 320*m.b10*
                       m.b12*m.b25 - 256*m.b10*m.b12*m.b26 - 192*m.b10*m.b12*m.b27 - 128*m.b10*m.b12*m.b28 - 64*m.b10*
                       m.b12*m.b29 - 32*m.b10*m.b12*m.b30 - 96*m.b10*m.b13*m.b14 - 96*m.b10*m.b13*m.b15 - 64*m.b10*m.b13
                       *m.b16 - 96*m.b10*m.b13*m.b17 - 224*m.b10*m.b13*m.b18 - 448*m.b10*m.b13*m.b19 - 384*m.b10*m.b13*
                       m.b20 - 320*m.b10*m.b13*m.b21 - 512*m.b10*m.b13*m.b22 - 416*m.b10*m.b13*m.b23 - 352*m.b10*m.b13*
                       m.b24 - 288*m.b10*m.b13*m.b25 - 224*m.b10*m.b13*m.b26 - 160*m.b10*m.b13*m.b27 - 96*m.b10*m.b13*
                       m.b28 - 64*m.b10*m.b13*m.b29 - 32*m.b10*m.b13*m.b30 - 96*m.b10*m.b14*m.b15 - 96*m.b10*m.b14*m.b16
                        - 96*m.b10*m.b14*m.b17 - 480*m.b10*m.b14*m.b18 - 448*m.b10*m.b14*m.b19 - 384*m.b10*m.b14*m.b20
                        - 320*m.b10*m.b14*m.b21 - 512*m.b10*m.b14*m.b22 - 416*m.b10*m.b14*m.b23 - 320*m.b10*m.b14*m.b24
                        - 256*m.b10*m.b14*m.b25 - 192*m.b10*m.b14*m.b26 - 128*m.b10*m.b14*m.b27 - 96*m.b10*m.b14*m.b28
                        - 64*m.b10*m.b14*m.b29 - 32*m.b10*m.b14*m.b30 - 96*m.b10*m.b15*m.b16 - 352*m.b10*m.b15*m.b17 - 
                       320*m.b10*m.b15*m.b18 - 448*m.b10*m.b15*m.b19 - 352*m.b10*m.b15*m.b20 - 320*m.b10*m.b15*m.b21 - 
                       512*m.b10*m.b15*m.b22 - 416*m.b10*m.b15*m.b23 - 320*m.b10*m.b15*m.b24 - 224*m.b10*m.b15*m.b25 - 
                       160*m.b10*m.b15*m.b26 - 128*m.b10*m.b15*m.b27 - 96*m.b10*m.b15*m.b28 - 64*m.b10*m.b15*m.b29 - 32*
                       m.b10*m.b15*m.b30 - 320*m.b10*m.b16*m.b17 - 288*m.b10*m.b16*m.b18 - 448*m.b10*m.b16*m.b19 - 384*
                       m.b10*m.b16*m.b20 - 320*m.b10*m.b16*m.b21 - 224*m.b10*m.b16*m.b22 - 416*m.b10*m.b16*m.b23 - 320*
                       m.b10*m.b16*m.b24 - 224*m.b10*m.b16*m.b25 - 160*m.b10*m.b16*m.b26 - 128*m.b10*m.b16*m.b27 - 96*
                       m.b10*m.b16*m.b28 - 64*m.b10*m.b16*m.b29 - 32*m.b10*m.b16*m.b30 - 256*m.b10*m.b17*m.b18 - 224*
                       m.b10*m.b17*m.b19 - 384*m.b10*m.b17*m.b20 - 320*m.b10*m.b17*m.b21 - 512*m.b10*m.b17*m.b22 - 416*
                       m.b10*m.b17*m.b23 - 96*m.b10*m.b17*m.b24 - 256*m.b10*m.b17*m.b25 - 192*m.b10*m.b17*m.b26 - 128*
                       m.b10*m.b17*m.b27 - 96*m.b10*m.b17*m.b28 - 64*m.b10*m.b17*m.b29 - 32*m.b10*m.b17*m.b30 - 192*
                       m.b10*m.b18*m.b19 - 384*m.b10*m.b18*m.b20 - 320*m.b10*m.b18*m.b21 - 512*m.b10*m.b18*m.b22 - 416*
                       m.b10*m.b18*m.b23 - 352*m.b10*m.b18*m.b24 - 288*m.b10*m.b18*m.b25 - 64*m.b10*m.b18*m.b26 - 160*
                       m.b10*m.b18*m.b27 - 96*m.b10*m.b18*m.b28 - 64*m.b10*m.b18*m.b29 - 32*m.b10*m.b18*m.b30 - 128*
                       m.b10*m.b19*m.b20 - 320*m.b10*m.b19*m.b21 - 512*m.b10*m.b19*m.b22 - 448*m.b10*m.b19*m.b23 - 384*
                       m.b10*m.b19*m.b24 - 320*m.b10*m.b19*m.b25 - 256*m.b10*m.b19*m.b26 - 192*m.b10*m.b19*m.b27 - 32*
                       m.b10*m.b19*m.b28 - 64*m.b10*m.b19*m.b29 - 32*m.b10*m.b19*m.b30 - 320*m.b10*m.b20*m.b21 - 544*
                       m.b10*m.b20*m.b22 - 480*m.b10*m.b20*m.b23 - 416*m.b10*m.b20*m.b24 - 352*m.b10*m.b20*m.b25 - 288*
                       m.b10*m.b20*m.b26 - 224*m.b10*m.b20*m.b27 - 160*m.b10*m.b20*m.b28 - 96*m.b10*m.b20*m.b29 - 576*
                       m.b10*m.b21*m.b22 - 512*m.b10*m.b21*m.b23 - 448*m.b10*m.b21*m.b24 - 384*m.b10*m.b21*m.b25 - 320*
                       m.b10*m.b21*m.b26 - 256*m.b10*m.b21*m.b27 - 192*m.b10*m.b21*m.b28 - 128*m.b10*m.b21*m.b29 - 64*
                       m.b10*m.b21*m.b30 - 512*m.b10*m.b22*m.b23 - 448*m.b10*m.b22*m.b24 - 384*m.b10*m.b22*m.b25 - 320*
                       m.b10*m.b22*m.b26 - 256*m.b10*m.b22*m.b27 - 192*m.b10*m.b22*m.b28 - 128*m.b10*m.b22*m.b29 - 64*
                       m.b10*m.b22*m.b30 - 448*m.b10*m.b23*m.b24 - 384*m.b10*m.b23*m.b25 - 320*m.b10*m.b23*m.b26 - 256*
                       m.b10*m.b23*m.b27 - 192*m.b10*m.b23*m.b28 - 128*m.b10*m.b23*m.b29 - 64*m.b10*m.b23*m.b30 - 384*
                       m.b10*m.b24*m.b25 - 320*m.b10*m.b24*m.b26 - 256*m.b10*m.b24*m.b27 - 192*m.b10*m.b24*m.b28 - 128*
                       m.b10*m.b24*m.b29 - 64*m.b10*m.b24*m.b30 - 320*m.b10*m.b25*m.b26 - 256*m.b10*m.b25*m.b27 - 192*
                       m.b10*m.b25*m.b28 - 128*m.b10*m.b25*m.b29 - 64*m.b10*m.b25*m.b30 - 256*m.b10*m.b26*m.b27 - 192*
                       m.b10*m.b26*m.b28 - 128*m.b10*m.b26*m.b29 - 64*m.b10*m.b26*m.b30 - 192*m.b10*m.b27*m.b28 - 128*
                       m.b10*m.b27*m.b29 - 64*m.b10*m.b27*m.b30 - 128*m.b10*m.b28*m.b29 - 64*m.b10*m.b28*m.b30 - 64*
                       m.b10*m.b29*m.b30 - 64*m.b11*m.b12*m.b13 - 96*m.b11*m.b12*m.b14 - 96*m.b11*m.b12*m.b15 - 96*m.b11
                       *m.b12*m.b16 - 96*m.b11*m.b12*m.b17 - 224*m.b11*m.b12*m.b18 - 192*m.b11*m.b12*m.b19 - 160*m.b11*
                       m.b12*m.b20 - 128*m.b11*m.b12*m.b21 - 320*m.b11*m.b12*m.b22 - 480*m.b11*m.b12*m.b23 - 416*m.b11*
                       m.b12*m.b24 - 352*m.b11*m.b12*m.b25 - 288*m.b11*m.b12*m.b26 - 224*m.b11*m.b12*m.b27 - 160*m.b11*
                       m.b12*m.b28 - 96*m.b11*m.b12*m.b29 - 32*m.b11*m.b12*m.b30 - 96*m.b11*m.b13*m.b14 - 64*m.b11*m.b13
                       *m.b15 - 96*m.b11*m.b13*m.b16 - 96*m.b11*m.b13*m.b17 - 256*m.b11*m.b13*m.b18 - 224*m.b11*m.b13*
                       m.b19 - 192*m.b11*m.b13*m.b20 - 384*m.b11*m.b13*m.b21 - 320*m.b11*m.b13*m.b22 - 480*m.b11*m.b13*
                       m.b23 - 384*m.b11*m.b13*m.b24 - 320*m.b11*m.b13*m.b25 - 256*m.b11*m.b13*m.b26 - 192*m.b11*m.b13*
                       m.b27 - 128*m.b11*m.b13*m.b28 - 64*m.b11*m.b13*m.b29 - 32*m.b11*m.b13*m.b30 - 96*m.b11*m.b14*
                       m.b15 - 96*m.b11*m.b14*m.b16 - 64*m.b11*m.b14*m.b17 - 96*m.b11*m.b14*m.b18 - 256*m.b11*m.b14*
                       m.b19 - 448*m.b11*m.b14*m.b20 - 384*m.b11*m.b14*m.b21 - 320*m.b11*m.b14*m.b22 - 480*m.b11*m.b14*
                       m.b23 - 384*m.b11*m.b14*m.b24 - 288*m.b11*m.b14*m.b25 - 224*m.b11*m.b14*m.b26 - 160*m.b11*m.b14*
                       m.b27 - 96*m.b11*m.b14*m.b28 - 64*m.b11*m.b14*m.b29 - 32*m.b11*m.b14*m.b30 - 96*m.b11*m.b15*m.b16
                        - 96*m.b11*m.b15*m.b17 - 96*m.b11*m.b15*m.b18 - 480*m.b11*m.b15*m.b19 - 448*m.b11*m.b15*m.b20 - 
                       384*m.b11*m.b15*m.b21 - 320*m.b11*m.b15*m.b22 - 480*m.b11*m.b15*m.b23 - 384*m.b11*m.b15*m.b24 - 
                       288*m.b11*m.b15*m.b25 - 192*m.b11*m.b15*m.b26 - 128*m.b11*m.b15*m.b27 - 96*m.b11*m.b15*m.b28 - 64
                       *m.b11*m.b15*m.b29 - 32*m.b11*m.b15*m.b30 - 96*m.b11*m.b16*m.b17 - 320*m.b11*m.b16*m.b18 - 288*
                       m.b11*m.b16*m.b19 - 448*m.b11*m.b16*m.b20 - 352*m.b11*m.b16*m.b21 - 320*m.b11*m.b16*m.b22 - 480*
                       m.b11*m.b16*m.b23 - 384*m.b11*m.b16*m.b24 - 288*m.b11*m.b16*m.b25 - 192*m.b11*m.b16*m.b26 - 128*
                       m.b11*m.b16*m.b27 - 96*m.b11*m.b16*m.b28 - 64*m.b11*m.b16*m.b29 - 32*m.b11*m.b16*m.b30 - 288*
                       m.b11*m.b17*m.b18 - 256*m.b11*m.b17*m.b19 - 448*m.b11*m.b17*m.b20 - 384*m.b11*m.b17*m.b21 - 320*
                       m.b11*m.b17*m.b22 - 224*m.b11*m.b17*m.b23 - 384*m.b11*m.b17*m.b24 - 288*m.b11*m.b17*m.b25 - 224*
                       m.b11*m.b17*m.b26 - 160*m.b11*m.b17*m.b27 - 96*m.b11*m.b17*m.b28 - 64*m.b11*m.b17*m.b29 - 32*
                       m.b11*m.b17*m.b30 - 224*m.b11*m.b18*m.b19 - 192*m.b11*m.b18*m.b20 - 384*m.b11*m.b18*m.b21 - 320*
                       m.b11*m.b18*m.b22 - 480*m.b11*m.b18*m.b23 - 384*m.b11*m.b18*m.b24 - 128*m.b11*m.b18*m.b25 - 256*
                       m.b11*m.b18*m.b26 - 192*m.b11*m.b18*m.b27 - 128*m.b11*m.b18*m.b28 - 64*m.b11*m.b18*m.b29 - 32*
                       m.b11*m.b18*m.b30 - 160*m.b11*m.b19*m.b20 - 384*m.b11*m.b19*m.b21 - 320*m.b11*m.b19*m.b22 - 480*
                       m.b11*m.b19*m.b23 - 416*m.b11*m.b19*m.b24 - 352*m.b11*m.b19*m.b25 - 288*m.b11*m.b19*m.b26 - 96*
                       m.b11*m.b19*m.b27 - 160*m.b11*m.b19*m.b28 - 96*m.b11*m.b19*m.b29 - 32*m.b11*m.b19*m.b30 - 96*
                       m.b11*m.b20*m.b21 - 320*m.b11*m.b20*m.b22 - 512*m.b11*m.b20*m.b23 - 448*m.b11*m.b20*m.b24 - 384*
                       m.b11*m.b20*m.b25 - 320*m.b11*m.b20*m.b26 - 256*m.b11*m.b20*m.b27 - 192*m.b11*m.b20*m.b28 - 64*
                       m.b11*m.b20*m.b29 - 64*m.b11*m.b20*m.b30 - 320*m.b11*m.b21*m.b22 - 512*m.b11*m.b21*m.b23 - 448*
                       m.b11*m.b21*m.b24 - 384*m.b11*m.b21*m.b25 - 320*m.b11*m.b21*m.b26 - 256*m.b11*m.b21*m.b27 - 192*
                       m.b11*m.b21*m.b28 - 128*m.b11*m.b21*m.b29 - 64*m.b11*m.b21*m.b30 - 512*m.b11*m.b22*m.b23 - 448*
                       m.b11*m.b22*m.b24 - 384*m.b11*m.b22*m.b25 - 320*m.b11*m.b22*m.b26 - 256*m.b11*m.b22*m.b27 - 192*
                       m.b11*m.b22*m.b28 - 128*m.b11*m.b22*m.b29 - 64*m.b11*m.b22*m.b30 - 448*m.b11*m.b23*m.b24 - 384*
                       m.b11*m.b23*m.b25 - 320*m.b11*m.b23*m.b26 - 256*m.b11*m.b23*m.b27 - 192*m.b11*m.b23*m.b28 - 128*
                       m.b11*m.b23*m.b29 - 64*m.b11*m.b23*m.b30 - 384*m.b11*m.b24*m.b25 - 320*m.b11*m.b24*m.b26 - 256*
                       m.b11*m.b24*m.b27 - 192*m.b11*m.b24*m.b28 - 128*m.b11*m.b24*m.b29 - 64*m.b11*m.b24*m.b30 - 320*
                       m.b11*m.b25*m.b26 - 256*m.b11*m.b25*m.b27 - 192*m.b11*m.b25*m.b28 - 128*m.b11*m.b25*m.b29 - 64*
                       m.b11*m.b25*m.b30 - 256*m.b11*m.b26*m.b27 - 192*m.b11*m.b26*m.b28 - 128*m.b11*m.b26*m.b29 - 64*
                       m.b11*m.b26*m.b30 - 192*m.b11*m.b27*m.b28 - 128*m.b11*m.b27*m.b29 - 64*m.b11*m.b27*m.b30 - 128*
                       m.b11*m.b28*m.b29 - 64*m.b11*m.b28*m.b30 - 64*m.b11*m.b29*m.b30 - 64*m.b12*m.b13*m.b14 - 96*m.b12
                       *m.b13*m.b15 - 96*m.b12*m.b13*m.b16 - 96*m.b12*m.b13*m.b17 - 96*m.b12*m.b13*m.b18 - 256*m.b12*
                       m.b13*m.b19 - 224*m.b12*m.b13*m.b20 - 192*m.b12*m.b13*m.b21 - 160*m.b12*m.b13*m.b22 - 320*m.b12*
                       m.b13*m.b23 - 448*m.b12*m.b13*m.b24 - 352*m.b12*m.b13*m.b25 - 288*m.b12*m.b13*m.b26 - 224*m.b12*
                       m.b13*m.b27 - 160*m.b12*m.b13*m.b28 - 96*m.b12*m.b13*m.b29 - 32*m.b12*m.b13*m.b30 - 96*m.b12*
                       m.b14*m.b15 - 64*m.b12*m.b14*m.b16 - 96*m.b12*m.b14*m.b17 - 96*m.b12*m.b14*m.b18 - 288*m.b12*
                       m.b14*m.b19 - 256*m.b12*m.b14*m.b20 - 224*m.b12*m.b14*m.b21 - 384*m.b12*m.b14*m.b22 - 320*m.b12*
                       m.b14*m.b23 - 448*m.b12*m.b14*m.b24 - 352*m.b12*m.b14*m.b25 - 256*m.b12*m.b14*m.b26 - 192*m.b12*
                       m.b14*m.b27 - 128*m.b12*m.b14*m.b28 - 64*m.b12*m.b14*m.b29 - 32*m.b12*m.b14*m.b30 - 96*m.b12*
                       m.b15*m.b16 - 96*m.b12*m.b15*m.b17 - 64*m.b12*m.b15*m.b18 - 96*m.b12*m.b15*m.b19 - 288*m.b12*
                       m.b15*m.b20 - 448*m.b12*m.b15*m.b21 - 384*m.b12*m.b15*m.b22 - 320*m.b12*m.b15*m.b23 - 448*m.b12*
                       m.b15*m.b24 - 352*m.b12*m.b15*m.b25 - 256*m.b12*m.b15*m.b26 - 160*m.b12*m.b15*m.b27 - 96*m.b12*
                       m.b15*m.b28 - 64*m.b12*m.b15*m.b29 - 32*m.b12*m.b15*m.b30 - 96*m.b12*m.b16*m.b17 - 96*m.b12*m.b16
                       *m.b18 - 96*m.b12*m.b16*m.b19 - 480*m.b12*m.b16*m.b20 - 448*m.b12*m.b16*m.b21 - 384*m.b12*m.b16*
                       m.b22 - 320*m.b12*m.b16*m.b23 - 448*m.b12*m.b16*m.b24 - 352*m.b12*m.b16*m.b25 - 256*m.b12*m.b16*
                       m.b26 - 160*m.b12*m.b16*m.b27 - 96*m.b12*m.b16*m.b28 - 64*m.b12*m.b16*m.b29 - 32*m.b12*m.b16*
                       m.b30 - 96*m.b12*m.b17*m.b18 - 288*m.b12*m.b17*m.b19 - 256*m.b12*m.b17*m.b20 - 448*m.b12*m.b17*
                       m.b21 - 352*m.b12*m.b17*m.b22 - 320*m.b12*m.b17*m.b23 - 448*m.b12*m.b17*m.b24 - 352*m.b12*m.b17*
                       m.b25 - 256*m.b12*m.b17*m.b26 - 192*m.b12*m.b17*m.b27 - 128*m.b12*m.b17*m.b28 - 64*m.b12*m.b17*
                       m.b29 - 32*m.b12*m.b17*m.b30 - 256*m.b12*m.b18*m.b19 - 224*m.b12*m.b18*m.b20 - 448*m.b12*m.b18*
                       m.b21 - 384*m.b12*m.b18*m.b22 - 320*m.b12*m.b18*m.b23 - 224*m.b12*m.b18*m.b24 - 352*m.b12*m.b18*
                       m.b25 - 288*m.b12*m.b18*m.b26 - 224*m.b12*m.b18*m.b27 - 160*m.b12*m.b18*m.b28 - 96*m.b12*m.b18*
                       m.b29 - 32*m.b12*m.b18*m.b30 - 192*m.b12*m.b19*m.b20 - 160*m.b12*m.b19*m.b21 - 384*m.b12*m.b19*
                       m.b22 - 320*m.b12*m.b19*m.b23 - 448*m.b12*m.b19*m.b24 - 384*m.b12*m.b19*m.b25 - 160*m.b12*m.b19*
                       m.b26 - 256*m.b12*m.b19*m.b27 - 192*m.b12*m.b19*m.b28 - 128*m.b12*m.b19*m.b29 - 64*m.b12*m.b19*
                       m.b30 - 128*m.b12*m.b20*m.b21 - 352*m.b12*m.b20*m.b22 - 288*m.b12*m.b20*m.b23 - 448*m.b12*m.b20*
                       m.b24 - 384*m.b12*m.b20*m.b25 - 320*m.b12*m.b20*m.b26 - 256*m.b12*m.b20*m.b27 - 96*m.b12*m.b20*
                       m.b28 - 128*m.b12*m.b20*m.b29 - 64*m.b12*m.b20*m.b30 - 64*m.b12*m.b21*m.b22 - 288*m.b12*m.b21*
                       m.b23 - 448*m.b12*m.b21*m.b24 - 384*m.b12*m.b21*m.b25 - 320*m.b12*m.b21*m.b26 - 256*m.b12*m.b21*
                       m.b27 - 192*m.b12*m.b21*m.b28 - 128*m.b12*m.b21*m.b29 - 32*m.b12*m.b21*m.b30 - 288*m.b12*m.b22*
                       m.b23 - 448*m.b12*m.b22*m.b24 - 384*m.b12*m.b22*m.b25 - 320*m.b12*m.b22*m.b26 - 256*m.b12*m.b22*
                       m.b27 - 192*m.b12*m.b22*m.b28 - 128*m.b12*m.b22*m.b29 - 64*m.b12*m.b22*m.b30 - 448*m.b12*m.b23*
                       m.b24 - 384*m.b12*m.b23*m.b25 - 320*m.b12*m.b23*m.b26 - 256*m.b12*m.b23*m.b27 - 192*m.b12*m.b23*
                       m.b28 - 128*m.b12*m.b23*m.b29 - 64*m.b12*m.b23*m.b30 - 384*m.b12*m.b24*m.b25 - 320*m.b12*m.b24*
                       m.b26 - 256*m.b12*m.b24*m.b27 - 192*m.b12*m.b24*m.b28 - 128*m.b12*m.b24*m.b29 - 64*m.b12*m.b24*
                       m.b30 - 320*m.b12*m.b25*m.b26 - 256*m.b12*m.b25*m.b27 - 192*m.b12*m.b25*m.b28 - 128*m.b12*m.b25*
                       m.b29 - 64*m.b12*m.b25*m.b30 - 256*m.b12*m.b26*m.b27 - 192*m.b12*m.b26*m.b28 - 128*m.b12*m.b26*
                       m.b29 - 64*m.b12*m.b26*m.b30 - 192*m.b12*m.b27*m.b28 - 128*m.b12*m.b27*m.b29 - 64*m.b12*m.b27*
                       m.b30 - 128*m.b12*m.b28*m.b29 - 64*m.b12*m.b28*m.b30 - 64*m.b12*m.b29*m.b30 - 64*m.b13*m.b14*
                       m.b15 - 96*m.b13*m.b14*m.b16 - 96*m.b13*m.b14*m.b17 - 96*m.b13*m.b14*m.b18 - 96*m.b13*m.b14*m.b19
                        - 288*m.b13*m.b14*m.b20 - 256*m.b13*m.b14*m.b21 - 224*m.b13*m.b14*m.b22 - 192*m.b13*m.b14*m.b23
                        - 320*m.b13*m.b14*m.b24 - 416*m.b13*m.b14*m.b25 - 320*m.b13*m.b14*m.b26 - 224*m.b13*m.b14*m.b27
                        - 160*m.b13*m.b14*m.b28 - 96*m.b13*m.b14*m.b29 - 32*m.b13*m.b14*m.b30 - 96*m.b13*m.b15*m.b16 - 
                       64*m.b13*m.b15*m.b17 - 96*m.b13*m.b15*m.b18 - 96*m.b13*m.b15*m.b19 - 320*m.b13*m.b15*m.b20 - 288*
                       m.b13*m.b15*m.b21 - 256*m.b13*m.b15*m.b22 - 384*m.b13*m.b15*m.b23 - 320*m.b13*m.b15*m.b24 - 416*
                       m.b13*m.b15*m.b25 - 320*m.b13*m.b15*m.b26 - 224*m.b13*m.b15*m.b27 - 128*m.b13*m.b15*m.b28 - 64*
                       m.b13*m.b15*m.b29 - 32*m.b13*m.b15*m.b30 - 96*m.b13*m.b16*m.b17 - 96*m.b13*m.b16*m.b18 - 64*m.b13
                       *m.b16*m.b19 - 96*m.b13*m.b16*m.b20 - 320*m.b13*m.b16*m.b21 - 448*m.b13*m.b16*m.b22 - 384*m.b13*
                       m.b16*m.b23 - 320*m.b13*m.b16*m.b24 - 416*m.b13*m.b16*m.b25 - 320*m.b13*m.b16*m.b26 - 224*m.b13*
                       m.b16*m.b27 - 128*m.b13*m.b16*m.b28 - 64*m.b13*m.b16*m.b29 - 32*m.b13*m.b16*m.b30 - 96*m.b13*
                       m.b17*m.b18 - 96*m.b13*m.b17*m.b19 - 96*m.b13*m.b17*m.b20 - 480*m.b13*m.b17*m.b21 - 448*m.b13*
                       m.b17*m.b22 - 384*m.b13*m.b17*m.b23 - 320*m.b13*m.b17*m.b24 - 416*m.b13*m.b17*m.b25 - 320*m.b13*
                       m.b17*m.b26 - 224*m.b13*m.b17*m.b27 - 160*m.b13*m.b17*m.b28 - 96*m.b13*m.b17*m.b29 - 32*m.b13*
                       m.b17*m.b30 - 96*m.b13*m.b18*m.b19 - 256*m.b13*m.b18*m.b20 - 224*m.b13*m.b18*m.b21 - 448*m.b13*
                       m.b18*m.b22 - 352*m.b13*m.b18*m.b23 - 320*m.b13*m.b18*m.b24 - 416*m.b13*m.b18*m.b25 - 320*m.b13*
                       m.b18*m.b26 - 256*m.b13*m.b18*m.b27 - 192*m.b13*m.b18*m.b28 - 128*m.b13*m.b18*m.b29 - 64*m.b13*
                       m.b18*m.b30 - 224*m.b13*m.b19*m.b20 - 192*m.b13*m.b19*m.b21 - 416*m.b13*m.b19*m.b22 - 352*m.b13*
                       m.b19*m.b23 - 288*m.b13*m.b19*m.b24 - 192*m.b13*m.b19*m.b25 - 320*m.b13*m.b19*m.b26 - 256*m.b13*
                       m.b19*m.b27 - 192*m.b13*m.b19*m.b28 - 128*m.b13*m.b19*m.b29 - 64*m.b13*m.b19*m.b30 - 160*m.b13*
                       m.b20*m.b21 - 128*m.b13*m.b20*m.b22 - 320*m.b13*m.b20*m.b23 - 256*m.b13*m.b20*m.b24 - 384*m.b13*
                       m.b20*m.b25 - 320*m.b13*m.b20*m.b26 - 128*m.b13*m.b20*m.b27 - 192*m.b13*m.b20*m.b28 - 128*m.b13*
                       m.b20*m.b29 - 64*m.b13*m.b20*m.b30 - 96*m.b13*m.b21*m.b22 - 288*m.b13*m.b21*m.b23 - 256*m.b13*
                       m.b21*m.b24 - 384*m.b13*m.b21*m.b25 - 320*m.b13*m.b21*m.b26 - 256*m.b13*m.b21*m.b27 - 192*m.b13*
                       m.b21*m.b28 - 64*m.b13*m.b21*m.b29 - 64*m.b13*m.b21*m.b30 - 64*m.b13*m.b22*m.b23 - 256*m.b13*
                       m.b22*m.b24 - 384*m.b13*m.b22*m.b25 - 320*m.b13*m.b22*m.b26 - 256*m.b13*m.b22*m.b27 - 192*m.b13*
                       m.b22*m.b28 - 128*m.b13*m.b22*m.b29 - 64*m.b13*m.b22*m.b30 - 256*m.b13*m.b23*m.b24 - 384*m.b13*
                       m.b23*m.b25 - 320*m.b13*m.b23*m.b26 - 256*m.b13*m.b23*m.b27 - 192*m.b13*m.b23*m.b28 - 128*m.b13*
                       m.b23*m.b29 - 64*m.b13*m.b23*m.b30 - 384*m.b13*m.b24*m.b25 - 320*m.b13*m.b24*m.b26 - 256*m.b13*
                       m.b24*m.b27 - 192*m.b13*m.b24*m.b28 - 128*m.b13*m.b24*m.b29 - 64*m.b13*m.b24*m.b30 - 320*m.b13*
                       m.b25*m.b26 - 256*m.b13*m.b25*m.b27 - 192*m.b13*m.b25*m.b28 - 128*m.b13*m.b25*m.b29 - 64*m.b13*
                       m.b25*m.b30 - 256*m.b13*m.b26*m.b27 - 192*m.b13*m.b26*m.b28 - 128*m.b13*m.b26*m.b29 - 64*m.b13*
                       m.b26*m.b30 - 192*m.b13*m.b27*m.b28 - 128*m.b13*m.b27*m.b29 - 64*m.b13*m.b27*m.b30 - 128*m.b13*
                       m.b28*m.b29 - 64*m.b13*m.b28*m.b30 - 64*m.b13*m.b29*m.b30 - 64*m.b14*m.b15*m.b16 - 96*m.b14*m.b15
                       *m.b17 - 96*m.b14*m.b15*m.b18 - 96*m.b14*m.b15*m.b19 - 96*m.b14*m.b15*m.b20 - 320*m.b14*m.b15*
                       m.b21 - 288*m.b14*m.b15*m.b22 - 256*m.b14*m.b15*m.b23 - 224*m.b14*m.b15*m.b24 - 320*m.b14*m.b15*
                       m.b25 - 384*m.b14*m.b15*m.b26 - 288*m.b14*m.b15*m.b27 - 192*m.b14*m.b15*m.b28 - 96*m.b14*m.b15*
                       m.b29 - 32*m.b14*m.b15*m.b30 - 96*m.b14*m.b16*m.b17 - 64*m.b14*m.b16*m.b18 - 96*m.b14*m.b16*m.b19
                        - 96*m.b14*m.b16*m.b20 - 352*m.b14*m.b16*m.b21 - 320*m.b14*m.b16*m.b22 - 288*m.b14*m.b16*m.b23
                        - 384*m.b14*m.b16*m.b24 - 320*m.b14*m.b16*m.b25 - 384*m.b14*m.b16*m.b26 - 288*m.b14*m.b16*m.b27
                        - 192*m.b14*m.b16*m.b28 - 96*m.b14*m.b16*m.b29 - 32*m.b14*m.b16*m.b30 - 96*m.b14*m.b17*m.b18 - 
                       96*m.b14*m.b17*m.b19 - 64*m.b14*m.b17*m.b20 - 96*m.b14*m.b17*m.b21 - 352*m.b14*m.b17*m.b22 - 448*
                       m.b14*m.b17*m.b23 - 384*m.b14*m.b17*m.b24 - 320*m.b14*m.b17*m.b25 - 384*m.b14*m.b17*m.b26 - 288*
                       m.b14*m.b17*m.b27 - 192*m.b14*m.b17*m.b28 - 128*m.b14*m.b17*m.b29 - 64*m.b14*m.b17*m.b30 - 96*
                       m.b14*m.b18*m.b19 - 96*m.b14*m.b18*m.b20 - 96*m.b14*m.b18*m.b21 - 448*m.b14*m.b18*m.b22 - 416*
                       m.b14*m.b18*m.b23 - 352*m.b14*m.b18*m.b24 - 288*m.b14*m.b18*m.b25 - 352*m.b14*m.b18*m.b26 - 256*
                       m.b14*m.b18*m.b27 - 192*m.b14*m.b18*m.b28 - 128*m.b14*m.b18*m.b29 - 64*m.b14*m.b18*m.b30 - 96*
                       m.b14*m.b19*m.b20 - 224*m.b14*m.b19*m.b21 - 192*m.b14*m.b19*m.b22 - 384*m.b14*m.b19*m.b23 - 288*
                       m.b14*m.b19*m.b24 - 256*m.b14*m.b19*m.b25 - 320*m.b14*m.b19*m.b26 - 256*m.b14*m.b19*m.b27 - 192*
                       m.b14*m.b19*m.b28 - 128*m.b14*m.b19*m.b29 - 64*m.b14*m.b19*m.b30 - 192*m.b14*m.b20*m.b21 - 160*
                       m.b14*m.b20*m.b22 - 352*m.b14*m.b20*m.b23 - 288*m.b14*m.b20*m.b24 - 224*m.b14*m.b20*m.b25 - 160*
                       m.b14*m.b20*m.b26 - 256*m.b14*m.b20*m.b27 - 192*m.b14*m.b20*m.b28 - 128*m.b14*m.b20*m.b29 - 64*
                       m.b14*m.b20*m.b30 - 128*m.b14*m.b21*m.b22 - 96*m.b14*m.b21*m.b23 - 256*m.b14*m.b21*m.b24 - 224*
                       m.b14*m.b21*m.b25 - 320*m.b14*m.b21*m.b26 - 256*m.b14*m.b21*m.b27 - 96*m.b14*m.b21*m.b28 - 128*
                       m.b14*m.b21*m.b29 - 64*m.b14*m.b21*m.b30 - 64*m.b14*m.b22*m.b23 - 256*m.b14*m.b22*m.b24 - 224*
                       m.b14*m.b22*m.b25 - 320*m.b14*m.b22*m.b26 - 256*m.b14*m.b22*m.b27 - 192*m.b14*m.b22*m.b28 - 128*
                       m.b14*m.b22*m.b29 - 32*m.b14*m.b22*m.b30 - 64*m.b14*m.b23*m.b24 - 224*m.b14*m.b23*m.b25 - 320*
                       m.b14*m.b23*m.b26 - 256*m.b14*m.b23*m.b27 - 192*m.b14*m.b23*m.b28 - 128*m.b14*m.b23*m.b29 - 64*
                       m.b14*m.b23*m.b30 - 224*m.b14*m.b24*m.b25 - 320*m.b14*m.b24*m.b26 - 256*m.b14*m.b24*m.b27 - 192*
                       m.b14*m.b24*m.b28 - 128*m.b14*m.b24*m.b29 - 64*m.b14*m.b24*m.b30 - 320*m.b14*m.b25*m.b26 - 256*
                       m.b14*m.b25*m.b27 - 192*m.b14*m.b25*m.b28 - 128*m.b14*m.b25*m.b29 - 64*m.b14*m.b25*m.b30 - 256*
                       m.b14*m.b26*m.b27 - 192*m.b14*m.b26*m.b28 - 128*m.b14*m.b26*m.b29 - 64*m.b14*m.b26*m.b30 - 192*
                       m.b14*m.b27*m.b28 - 128*m.b14*m.b27*m.b29 - 64*m.b14*m.b27*m.b30 - 128*m.b14*m.b28*m.b29 - 64*
                       m.b14*m.b28*m.b30 - 64*m.b14*m.b29*m.b30 - 64*m.b15*m.b16*m.b17 - 96*m.b15*m.b16*m.b18 - 96*m.b15
                       *m.b16*m.b19 - 96*m.b15*m.b16*m.b20 - 96*m.b15*m.b16*m.b21 - 352*m.b15*m.b16*m.b22 - 320*m.b15*
                       m.b16*m.b23 - 288*m.b15*m.b16*m.b24 - 256*m.b15*m.b16*m.b25 - 320*m.b15*m.b16*m.b26 - 352*m.b15*
                       m.b16*m.b27 - 256*m.b15*m.b16*m.b28 - 160*m.b15*m.b16*m.b29 - 64*m.b15*m.b16*m.b30 - 96*m.b15*
                       m.b17*m.b18 - 64*m.b15*m.b17*m.b19 - 96*m.b15*m.b17*m.b20 - 96*m.b15*m.b17*m.b21 - 352*m.b15*
                       m.b17*m.b22 - 320*m.b15*m.b17*m.b23 - 288*m.b15*m.b17*m.b24 - 352*m.b15*m.b17*m.b25 - 288*m.b15*
                       m.b17*m.b26 - 320*m.b15*m.b17*m.b27 - 224*m.b15*m.b17*m.b28 - 128*m.b15*m.b17*m.b29 - 64*m.b15*
                       m.b17*m.b30 - 96*m.b15*m.b18*m.b19 - 96*m.b15*m.b18*m.b20 - 64*m.b15*m.b18*m.b21 - 96*m.b15*m.b18
                       *m.b22 - 320*m.b15*m.b18*m.b23 - 384*m.b15*m.b18*m.b24 - 320*m.b15*m.b18*m.b25 - 256*m.b15*m.b18*
                       m.b26 - 288*m.b15*m.b18*m.b27 - 192*m.b15*m.b18*m.b28 - 128*m.b15*m.b18*m.b29 - 64*m.b15*m.b18*
                       m.b30 - 96*m.b15*m.b19*m.b20 - 96*m.b15*m.b19*m.b21 - 96*m.b15*m.b19*m.b22 - 384*m.b15*m.b19*
                       m.b23 - 352*m.b15*m.b19*m.b24 - 288*m.b15*m.b19*m.b25 - 224*m.b15*m.b19*m.b26 - 256*m.b15*m.b19*
                       m.b27 - 192*m.b15*m.b19*m.b28 - 128*m.b15*m.b19*m.b29 - 64*m.b15*m.b19*m.b30 - 96*m.b15*m.b20*
                       m.b21 - 192*m.b15*m.b20*m.b22 - 160*m.b15*m.b20*m.b23 - 320*m.b15*m.b20*m.b24 - 224*m.b15*m.b20*
                       m.b25 - 192*m.b15*m.b20*m.b26 - 256*m.b15*m.b20*m.b27 - 192*m.b15*m.b20*m.b28 - 128*m.b15*m.b20*
                       m.b29 - 64*m.b15*m.b20*m.b30 - 160*m.b15*m.b21*m.b22 - 128*m.b15*m.b21*m.b23 - 288*m.b15*m.b21*
                       m.b24 - 224*m.b15*m.b21*m.b25 - 192*m.b15*m.b21*m.b26 - 128*m.b15*m.b21*m.b27 - 192*m.b15*m.b21*
                       m.b28 - 128*m.b15*m.b21*m.b29 - 64*m.b15*m.b21*m.b30 - 96*m.b15*m.b22*m.b23 - 64*m.b15*m.b22*
                       m.b24 - 224*m.b15*m.b22*m.b25 - 192*m.b15*m.b22*m.b26 - 256*m.b15*m.b22*m.b27 - 192*m.b15*m.b22*
                       m.b28 - 64*m.b15*m.b22*m.b29 - 64*m.b15*m.b22*m.b30 - 64*m.b15*m.b23*m.b24 - 224*m.b15*m.b23*
                       m.b25 - 192*m.b15*m.b23*m.b26 - 256*m.b15*m.b23*m.b27 - 192*m.b15*m.b23*m.b28 - 128*m.b15*m.b23*
                       m.b29 - 64*m.b15*m.b23*m.b30 - 64*m.b15*m.b24*m.b25 - 192*m.b15*m.b24*m.b26 - 256*m.b15*m.b24*
                       m.b27 - 192*m.b15*m.b24*m.b28 - 128*m.b15*m.b24*m.b29 - 64*m.b15*m.b24*m.b30 - 192*m.b15*m.b25*
                       m.b26 - 256*m.b15*m.b25*m.b27 - 192*m.b15*m.b25*m.b28 - 128*m.b15*m.b25*m.b29 - 64*m.b15*m.b25*
                       m.b30 - 256*m.b15*m.b26*m.b27 - 192*m.b15*m.b26*m.b28 - 128*m.b15*m.b26*m.b29 - 64*m.b15*m.b26*
                       m.b30 - 192*m.b15*m.b27*m.b28 - 128*m.b15*m.b27*m.b29 - 64*m.b15*m.b27*m.b30 - 128*m.b15*m.b28*
                       m.b29 - 64*m.b15*m.b28*m.b30 - 64*m.b15*m.b29*m.b30 - 64*m.b16*m.b17*m.b18 - 96*m.b16*m.b17*m.b19
                        - 96*m.b16*m.b17*m.b20 - 96*m.b16*m.b17*m.b21 - 96*m.b16*m.b17*m.b22 - 320*m.b16*m.b17*m.b23 - 
                       288*m.b16*m.b17*m.b24 - 256*m.b16*m.b17*m.b25 - 224*m.b16*m.b17*m.b26 - 256*m.b16*m.b17*m.b27 - 
                       256*m.b16*m.b17*m.b28 - 160*m.b16*m.b17*m.b29 - 64*m.b16*m.b17*m.b30 - 96*m.b16*m.b18*m.b19 - 64*
                       m.b16*m.b18*m.b20 - 96*m.b16*m.b18*m.b21 - 96*m.b16*m.b18*m.b22 - 320*m.b16*m.b18*m.b23 - 288*
                       m.b16*m.b18*m.b24 - 256*m.b16*m.b18*m.b25 - 288*m.b16*m.b18*m.b26 - 224*m.b16*m.b18*m.b27 - 224*
                       m.b16*m.b18*m.b28 - 128*m.b16*m.b18*m.b29 - 64*m.b16*m.b18*m.b30 - 96*m.b16*m.b19*m.b20 - 96*
                       m.b16*m.b19*m.b21 - 64*m.b16*m.b19*m.b22 - 96*m.b16*m.b19*m.b23 - 288*m.b16*m.b19*m.b24 - 320*
                       m.b16*m.b19*m.b25 - 256*m.b16*m.b19*m.b26 - 192*m.b16*m.b19*m.b27 - 192*m.b16*m.b19*m.b28 - 128*
                       m.b16*m.b19*m.b29 - 64*m.b16*m.b19*m.b30 - 96*m.b16*m.b20*m.b21 - 96*m.b16*m.b20*m.b22 - 96*m.b16
                       *m.b20*m.b23 - 320*m.b16*m.b20*m.b24 - 288*m.b16*m.b20*m.b25 - 224*m.b16*m.b20*m.b26 - 160*m.b16*
                       m.b20*m.b27 - 192*m.b16*m.b20*m.b28 - 128*m.b16*m.b20*m.b29 - 64*m.b16*m.b20*m.b30 - 96*m.b16*
                       m.b21*m.b22 - 160*m.b16*m.b21*m.b23 - 128*m.b16*m.b21*m.b24 - 256*m.b16*m.b21*m.b25 - 160*m.b16*
                       m.b21*m.b26 - 160*m.b16*m.b21*m.b27 - 192*m.b16*m.b21*m.b28 - 128*m.b16*m.b21*m.b29 - 64*m.b16*
                       m.b21*m.b30 - 128*m.b16*m.b22*m.b23 - 96*m.b16*m.b22*m.b24 - 224*m.b16*m.b22*m.b25 - 192*m.b16*
                       m.b22*m.b26 - 160*m.b16*m.b22*m.b27 - 96*m.b16*m.b22*m.b28 - 128*m.b16*m.b22*m.b29 - 64*m.b16*
                       m.b22*m.b30 - 64*m.b16*m.b23*m.b24 - 64*m.b16*m.b23*m.b25 - 192*m.b16*m.b23*m.b26 - 160*m.b16*
                       m.b23*m.b27 - 192*m.b16*m.b23*m.b28 - 128*m.b16*m.b23*m.b29 - 32*m.b16*m.b23*m.b30 - 64*m.b16*
                       m.b24*m.b25 - 192*m.b16*m.b24*m.b26 - 160*m.b16*m.b24*m.b27 - 192*m.b16*m.b24*m.b28 - 128*m.b16*
                       m.b24*m.b29 - 64*m.b16*m.b24*m.b30 - 64*m.b16*m.b25*m.b26 - 160*m.b16*m.b25*m.b27 - 192*m.b16*
                       m.b25*m.b28 - 128*m.b16*m.b25*m.b29 - 64*m.b16*m.b25*m.b30 - 160*m.b16*m.b26*m.b27 - 192*m.b16*
                       m.b26*m.b28 - 128*m.b16*m.b26*m.b29 - 64*m.b16*m.b26*m.b30 - 192*m.b16*m.b27*m.b28 - 128*m.b16*
                       m.b27*m.b29 - 64*m.b16*m.b27*m.b30 - 128*m.b16*m.b28*m.b29 - 64*m.b16*m.b28*m.b30 - 64*m.b16*
                       m.b29*m.b30 - 64*m.b17*m.b18*m.b19 - 96*m.b17*m.b18*m.b20 - 96*m.b17*m.b18*m.b21 - 96*m.b17*m.b18
                       *m.b22 - 96*m.b17*m.b18*m.b23 - 288*m.b17*m.b18*m.b24 - 256*m.b17*m.b18*m.b25 - 224*m.b17*m.b18*
                       m.b26 - 192*m.b17*m.b18*m.b27 - 192*m.b17*m.b18*m.b28 - 160*m.b17*m.b18*m.b29 - 64*m.b17*m.b18*
                       m.b30 - 96*m.b17*m.b19*m.b20 - 64*m.b17*m.b19*m.b21 - 96*m.b17*m.b19*m.b22 - 96*m.b17*m.b19*m.b23
                        - 288*m.b17*m.b19*m.b24 - 256*m.b17*m.b19*m.b25 - 224*m.b17*m.b19*m.b26 - 224*m.b17*m.b19*m.b27
                        - 160*m.b17*m.b19*m.b28 - 128*m.b17*m.b19*m.b29 - 64*m.b17*m.b19*m.b30 - 96*m.b17*m.b20*m.b21 - 
                       96*m.b17*m.b20*m.b22 - 64*m.b17*m.b20*m.b23 - 96*m.b17*m.b20*m.b24 - 256*m.b17*m.b20*m.b25 - 256*
                       m.b17*m.b20*m.b26 - 192*m.b17*m.b20*m.b27 - 128*m.b17*m.b20*m.b28 - 128*m.b17*m.b20*m.b29 - 64*
                       m.b17*m.b20*m.b30 - 96*m.b17*m.b21*m.b22 - 96*m.b17*m.b21*m.b23 - 96*m.b17*m.b21*m.b24 - 256*
                       m.b17*m.b21*m.b25 - 224*m.b17*m.b21*m.b26 - 160*m.b17*m.b21*m.b27 - 128*m.b17*m.b21*m.b28 - 128*
                       m.b17*m.b21*m.b29 - 64*m.b17*m.b21*m.b30 - 96*m.b17*m.b22*m.b23 - 128*m.b17*m.b22*m.b24 - 96*
                       m.b17*m.b22*m.b25 - 192*m.b17*m.b22*m.b26 - 128*m.b17*m.b22*m.b27 - 128*m.b17*m.b22*m.b28 - 128*
                       m.b17*m.b22*m.b29 - 64*m.b17*m.b22*m.b30 - 96*m.b17*m.b23*m.b24 - 64*m.b17*m.b23*m.b25 - 192*
                       m.b17*m.b23*m.b26 - 160*m.b17*m.b23*m.b27 - 128*m.b17*m.b23*m.b28 - 64*m.b17*m.b23*m.b29 - 64*
                       m.b17*m.b23*m.b30 - 64*m.b17*m.b24*m.b25 - 64*m.b17*m.b24*m.b26 - 160*m.b17*m.b24*m.b27 - 128*
                       m.b17*m.b24*m.b28 - 128*m.b17*m.b24*m.b29 - 64*m.b17*m.b24*m.b30 - 64*m.b17*m.b25*m.b26 - 160*
                       m.b17*m.b25*m.b27 - 128*m.b17*m.b25*m.b28 - 128*m.b17*m.b25*m.b29 - 64*m.b17*m.b25*m.b30 - 64*
                       m.b17*m.b26*m.b27 - 128*m.b17*m.b26*m.b28 - 128*m.b17*m.b26*m.b29 - 64*m.b17*m.b26*m.b30 - 128*
                       m.b17*m.b27*m.b28 - 128*m.b17*m.b27*m.b29 - 64*m.b17*m.b27*m.b30 - 128*m.b17*m.b28*m.b29 - 64*
                       m.b17*m.b28*m.b30 - 64*m.b17*m.b29*m.b30 - 64*m.b18*m.b19*m.b20 - 96*m.b18*m.b19*m.b21 - 96*m.b18
                       *m.b19*m.b22 - 96*m.b18*m.b19*m.b23 - 96*m.b18*m.b19*m.b24 - 256*m.b18*m.b19*m.b25 - 224*m.b18*
                       m.b19*m.b26 - 192*m.b18*m.b19*m.b27 - 160*m.b18*m.b19*m.b28 - 128*m.b18*m.b19*m.b29 - 64*m.b18*
                       m.b19*m.b30 - 96*m.b18*m.b20*m.b21 - 64*m.b18*m.b20*m.b22 - 96*m.b18*m.b20*m.b23 - 96*m.b18*m.b20
                       *m.b24 - 256*m.b18*m.b20*m.b25 - 224*m.b18*m.b20*m.b26 - 192*m.b18*m.b20*m.b27 - 160*m.b18*m.b20*
                       m.b28 - 96*m.b18*m.b20*m.b29 - 64*m.b18*m.b20*m.b30 - 96*m.b18*m.b21*m.b22 - 96*m.b18*m.b21*m.b23
                        - 64*m.b18*m.b21*m.b24 - 96*m.b18*m.b21*m.b25 - 224*m.b18*m.b21*m.b26 - 192*m.b18*m.b21*m.b27 - 
                       128*m.b18*m.b21*m.b28 - 96*m.b18*m.b21*m.b29 - 64*m.b18*m.b21*m.b30 - 96*m.b18*m.b22*m.b23 - 96*
                       m.b18*m.b22*m.b24 - 96*m.b18*m.b22*m.b25 - 192*m.b18*m.b22*m.b26 - 160*m.b18*m.b22*m.b27 - 128*
                       m.b18*m.b22*m.b28 - 96*m.b18*m.b22*m.b29 - 64*m.b18*m.b22*m.b30 - 96*m.b18*m.b23*m.b24 - 96*m.b18
                       *m.b23*m.b25 - 64*m.b18*m.b23*m.b26 - 160*m.b18*m.b23*m.b27 - 96*m.b18*m.b23*m.b28 - 96*m.b18*
                       m.b23*m.b29 - 64*m.b18*m.b23*m.b30 - 64*m.b18*m.b24*m.b25 - 64*m.b18*m.b24*m.b26 - 160*m.b18*
                       m.b24*m.b27 - 128*m.b18*m.b24*m.b28 - 96*m.b18*m.b24*m.b29 - 32*m.b18*m.b24*m.b30 - 64*m.b18*
                       m.b25*m.b26 - 64*m.b18*m.b25*m.b27 - 128*m.b18*m.b25*m.b28 - 96*m.b18*m.b25*m.b29 - 64*m.b18*
                       m.b25*m.b30 - 64*m.b18*m.b26*m.b27 - 128*m.b18*m.b26*m.b28 - 96*m.b18*m.b26*m.b29 - 64*m.b18*
                       m.b26*m.b30 - 64*m.b18*m.b27*m.b28 - 96*m.b18*m.b27*m.b29 - 64*m.b18*m.b27*m.b30 - 96*m.b18*m.b28
                       *m.b29 - 64*m.b18*m.b28*m.b30 - 64*m.b18*m.b29*m.b30 - 64*m.b19*m.b20*m.b21 - 96*m.b19*m.b20*
                       m.b22 - 96*m.b19*m.b20*m.b23 - 96*m.b19*m.b20*m.b24 - 96*m.b19*m.b20*m.b25 - 224*m.b19*m.b20*
                       m.b26 - 192*m.b19*m.b20*m.b27 - 160*m.b19*m.b20*m.b28 - 128*m.b19*m.b20*m.b29 - 64*m.b19*m.b20*
                       m.b30 - 96*m.b19*m.b21*m.b22 - 64*m.b19*m.b21*m.b23 - 96*m.b19*m.b21*m.b24 - 96*m.b19*m.b21*m.b25
                        - 224*m.b19*m.b21*m.b26 - 192*m.b19*m.b21*m.b27 - 160*m.b19*m.b21*m.b28 - 96*m.b19*m.b21*m.b29
                        - 64*m.b19*m.b21*m.b30 - 96*m.b19*m.b22*m.b23 - 96*m.b19*m.b22*m.b24 - 64*m.b19*m.b22*m.b25 - 96
                       *m.b19*m.b22*m.b26 - 192*m.b19*m.b22*m.b27 - 128*m.b19*m.b22*m.b28 - 96*m.b19*m.b22*m.b29 - 64*
                       m.b19*m.b22*m.b30 - 96*m.b19*m.b23*m.b24 - 96*m.b19*m.b23*m.b25 - 96*m.b19*m.b23*m.b26 - 128*
                       m.b19*m.b23*m.b27 - 128*m.b19*m.b23*m.b28 - 96*m.b19*m.b23*m.b29 - 64*m.b19*m.b23*m.b30 - 96*
                       m.b19*m.b24*m.b25 - 64*m.b19*m.b24*m.b26 - 64*m.b19*m.b24*m.b27 - 128*m.b19*m.b24*m.b28 - 64*
                       m.b19*m.b24*m.b29 - 64*m.b19*m.b24*m.b30 - 64*m.b19*m.b25*m.b26 - 64*m.b19*m.b25*m.b27 - 128*
                       m.b19*m.b25*m.b28 - 96*m.b19*m.b25*m.b29 - 64*m.b19*m.b25*m.b30 - 64*m.b19*m.b26*m.b27 - 64*m.b19
                       *m.b26*m.b28 - 96*m.b19*m.b26*m.b29 - 64*m.b19*m.b26*m.b30 - 64*m.b19*m.b27*m.b28 - 96*m.b19*
                       m.b27*m.b29 - 64*m.b19*m.b27*m.b30 - 64*m.b19*m.b28*m.b29 - 64*m.b19*m.b28*m.b30 - 64*m.b19*m.b29
                       *m.b30 - 64*m.b20*m.b21*m.b22 - 96*m.b20*m.b21*m.b23 - 96*m.b20*m.b21*m.b24 - 96*m.b20*m.b21*
                       m.b25 - 96*m.b20*m.b21*m.b26 - 192*m.b20*m.b21*m.b27 - 160*m.b20*m.b21*m.b28 - 128*m.b20*m.b21*
                       m.b29 - 64*m.b20*m.b21*m.b30 - 96*m.b20*m.b22*m.b23 - 64*m.b20*m.b22*m.b24 - 96*m.b20*m.b22*m.b25
                        - 96*m.b20*m.b22*m.b26 - 192*m.b20*m.b22*m.b27 - 160*m.b20*m.b22*m.b28 - 96*m.b20*m.b22*m.b29 - 
                       64*m.b20*m.b22*m.b30 - 96*m.b20*m.b23*m.b24 - 96*m.b20*m.b23*m.b25 - 64*m.b20*m.b23*m.b26 - 96*
                       m.b20*m.b23*m.b27 - 128*m.b20*m.b23*m.b28 - 96*m.b20*m.b23*m.b29 - 64*m.b20*m.b23*m.b30 - 96*
                       m.b20*m.b24*m.b25 - 96*m.b20*m.b24*m.b26 - 64*m.b20*m.b24*m.b27 - 96*m.b20*m.b24*m.b28 - 96*m.b20
                       *m.b24*m.b29 - 64*m.b20*m.b24*m.b30 - 64*m.b20*m.b25*m.b26 - 64*m.b20*m.b25*m.b27 - 64*m.b20*
                       m.b25*m.b28 - 96*m.b20*m.b25*m.b29 - 32*m.b20*m.b25*m.b30 - 64*m.b20*m.b26*m.b27 - 64*m.b20*m.b26
                       *m.b28 - 96*m.b20*m.b26*m.b29 - 64*m.b20*m.b26*m.b30 - 64*m.b20*m.b27*m.b28 - 64*m.b20*m.b27*
                       m.b29 - 64*m.b20*m.b27*m.b30 - 64*m.b20*m.b28*m.b29 - 64*m.b20*m.b28*m.b30 - 64*m.b20*m.b29*m.b30
                        - 64*m.b21*m.b22*m.b23 - 96*m.b21*m.b22*m.b24 - 96*m.b21*m.b22*m.b25 - 96*m.b21*m.b22*m.b26 - 96
                       *m.b21*m.b22*m.b27 - 160*m.b21*m.b22*m.b28 - 128*m.b21*m.b22*m.b29 - 64*m.b21*m.b22*m.b30 - 96*
                       m.b21*m.b23*m.b24 - 64*m.b21*m.b23*m.b25 - 96*m.b21*m.b23*m.b26 - 96*m.b21*m.b23*m.b27 - 160*
                       m.b21*m.b23*m.b28 - 96*m.b21*m.b23*m.b29 - 64*m.b21*m.b23*m.b30 - 96*m.b21*m.b24*m.b25 - 96*m.b21
                       *m.b24*m.b26 - 64*m.b21*m.b24*m.b27 - 64*m.b21*m.b24*m.b28 - 96*m.b21*m.b24*m.b29 - 64*m.b21*
                       m.b24*m.b30 - 96*m.b21*m.b25*m.b26 - 64*m.b21*m.b25*m.b27 - 64*m.b21*m.b25*m.b28 - 64*m.b21*m.b25
                       *m.b29 - 64*m.b21*m.b25*m.b30 - 64*m.b21*m.b26*m.b27 - 64*m.b21*m.b26*m.b28 - 64*m.b21*m.b26*
                       m.b29 - 64*m.b21*m.b26*m.b30 - 64*m.b21*m.b27*m.b28 - 64*m.b21*m.b27*m.b29 - 64*m.b21*m.b27*m.b30
                        - 64*m.b21*m.b28*m.b29 - 64*m.b21*m.b28*m.b30 - 64*m.b21*m.b29*m.b30 - 64*m.b22*m.b23*m.b24 - 96
                       *m.b22*m.b23*m.b25 - 96*m.b22*m.b23*m.b26 - 96*m.b22*m.b23*m.b27 - 96*m.b22*m.b23*m.b28 - 128*
                       m.b22*m.b23*m.b29 - 64*m.b22*m.b23*m.b30 - 96*m.b22*m.b24*m.b25 - 64*m.b22*m.b24*m.b26 - 96*m.b22
                       *m.b24*m.b27 - 96*m.b22*m.b24*m.b28 - 96*m.b22*m.b24*m.b29 - 64*m.b22*m.b24*m.b30 - 96*m.b22*
                       m.b25*m.b26 - 96*m.b22*m.b25*m.b27 - 32*m.b22*m.b25*m.b28 - 64*m.b22*m.b25*m.b29 - 64*m.b22*m.b25
                       *m.b30 - 64*m.b22*m.b26*m.b27 - 64*m.b22*m.b26*m.b28 - 64*m.b22*m.b26*m.b29 - 32*m.b22*m.b26*
                       m.b30 - 64*m.b22*m.b27*m.b28 - 64*m.b22*m.b27*m.b29 - 64*m.b22*m.b27*m.b30 - 64*m.b22*m.b28*m.b29
                        - 64*m.b22*m.b28*m.b30 - 64*m.b22*m.b29*m.b30 - 64*m.b23*m.b24*m.b25 - 96*m.b23*m.b24*m.b26 - 96
                       *m.b23*m.b24*m.b27 - 96*m.b23*m.b24*m.b28 - 96*m.b23*m.b24*m.b29 - 64*m.b23*m.b24*m.b30 - 96*
                       m.b23*m.b25*m.b26 - 64*m.b23*m.b25*m.b27 - 96*m.b23*m.b25*m.b28 - 64*m.b23*m.b25*m.b29 - 64*m.b23
                       *m.b25*m.b30 - 96*m.b23*m.b26*m.b27 - 64*m.b23*m.b26*m.b28 - 32*m.b23*m.b26*m.b29 - 64*m.b23*
                       m.b26*m.b30 - 64*m.b23*m.b27*m.b28 - 64*m.b23*m.b27*m.b29 - 64*m.b23*m.b27*m.b30 - 64*m.b23*m.b28
                       *m.b29 - 64*m.b23*m.b28*m.b30 - 64*m.b23*m.b29*m.b30 - 64*m.b24*m.b25*m.b26 - 96*m.b24*m.b25*
                       m.b27 - 96*m.b24*m.b25*m.b28 - 96*m.b24*m.b25*m.b29 - 64*m.b24*m.b25*m.b30 - 96*m.b24*m.b26*m.b27
                        - 64*m.b24*m.b26*m.b28 - 64*m.b24*m.b26*m.b29 - 64*m.b24*m.b26*m.b30 - 64*m.b24*m.b27*m.b28 - 64
                       *m.b24*m.b27*m.b29 - 32*m.b24*m.b27*m.b30 - 64*m.b24*m.b28*m.b29 - 64*m.b24*m.b28*m.b30 - 64*
                       m.b24*m.b29*m.b30 - 64*m.b25*m.b26*m.b27 - 96*m.b25*m.b26*m.b28 - 96*m.b25*m.b26*m.b29 - 64*m.b25
                       *m.b26*m.b30 - 96*m.b25*m.b27*m.b28 - 32*m.b25*m.b27*m.b29 - 64*m.b25*m.b27*m.b30 - 64*m.b25*
                       m.b28*m.b29 - 64*m.b25*m.b28*m.b30 - 64*m.b25*m.b29*m.b30 - 64*m.b26*m.b27*m.b28 - 96*m.b26*m.b27
                       *m.b29 - 64*m.b26*m.b27*m.b30 - 64*m.b26*m.b28*m.b29 - 32*m.b26*m.b28*m.b30 - 64*m.b26*m.b29*
                       m.b30 - 64*m.b27*m.b28*m.b29 - 64*m.b27*m.b28*m.b30 - 64*m.b27*m.b29*m.b30 - 32*m.b28*m.b29*m.b30
                        + 432*m.b1*m.b2 + 424*m.b1*m.b3 + 416*m.b1*m.b4 + 408*m.b1*m.b5 + 400*m.b1*m.b6 + 392*m.b1*m.b7
                        + 384*m.b1*m.b8 + 376*m.b1*m.b9 + 368*m.b1*m.b10 + 360*m.b1*m.b11 + 352*m.b1*m.b12 + 344*m.b1*
                       m.b13 + 336*m.b1*m.b14 + 328*m.b1*m.b15 + 336*m.b1*m.b16 + 328*m.b1*m.b17 + 320*m.b1*m.b18 + 312*
                       m.b1*m.b19 + 304*m.b1*m.b20 + 296*m.b1*m.b21 + 288*m.b1*m.b22 + 280*m.b1*m.b23 + 272*m.b1*m.b24
                        + 264*m.b1*m.b25 + 256*m.b1*m.b26 + 248*m.b1*m.b27 + 240*m.b1*m.b28 + 232*m.b1*m.b29 + 224*m.b1*
                       m.b30 + 688*m.b2*m.b3 + 696*m.b2*m.b4 + 688*m.b2*m.b5 + 680*m.b2*m.b6 + 672*m.b2*m.b7 + 648*m.b2*
                       m.b8 + 640*m.b2*m.b9 + 632*m.b2*m.b10 + 624*m.b2*m.b11 + 616*m.b2*m.b12 + 608*m.b2*m.b13 + 664*
                       m.b2*m.b14 + 656*m.b2*m.b15 + 648*m.b2*m.b16 + 656*m.b2*m.b17 + 632*m.b2*m.b18 + 624*m.b2*m.b19
                        + 600*m.b2*m.b20 + 592*m.b2*m.b21 + 568*m.b2*m.b22 + 560*m.b2*m.b23 + 536*m.b2*m.b24 + 528*m.b2*
                       m.b25 + 504*m.b2*m.b26 + 496*m.b2*m.b27 + 472*m.b2*m.b28 + 464*m.b2*m.b29 + 232*m.b2*m.b30 + 912*
                       m.b3*m.b4 + 904*m.b3*m.b5 + 912*m.b3*m.b6 + 904*m.b3*m.b7 + 896*m.b3*m.b8 + 856*m.b3*m.b9 + 848*
                       m.b3*m.b10 + 840*m.b3*m.b11 + 832*m.b3*m.b12 + 840*m.b3*m.b13 + 848*m.b3*m.b14 + 968*m.b3*m.b15
                        + 976*m.b3*m.b16 + 968*m.b3*m.b17 + 960*m.b3*m.b18 + 920*m.b3*m.b19 + 912*m.b3*m.b20 + 872*m.b3*
                       m.b21 + 864*m.b3*m.b22 + 824*m.b3*m.b23 + 816*m.b3*m.b24 + 776*m.b3*m.b25 + 768*m.b3*m.b26 + 728*
                       m.b3*m.b27 + 720*m.b3*m.b28 + 472*m.b3*m.b29 + 240*m.b3*m.b30 + 1088*m.b4*m.b5 + 1080*m.b4*m.b6
                        + 1072*m.b4*m.b7 + 1080*m.b4*m.b8 + 1072*m.b4*m.b9 + 1016*m.b4*m.b10 + 1008*m.b4*m.b11 + 1016*
                       m.b4*m.b12 + 1008*m.b4*m.b13 + 1048*m.b4*m.b14 + 1072*m.b4*m.b15 + 1272*m.b4*m.b16 + 1296*m.b4*
                       m.b17 + 1256*m.b4*m.b18 + 1248*m.b4*m.b19 + 1192*m.b4*m.b20 + 1184*m.b4*m.b21 + 1128*m.b4*m.b22
                        + 1120*m.b4*m.b23 + 1064*m.b4*m.b24 + 1056*m.b4*m.b25 + 1000*m.b4*m.b26 + 992*m.b4*m.b27 + 728*
                       m.b4*m.b28 + 496*m.b4*m.b29 + 248*m.b4*m.b30 + 1216*m.b5*m.b6 + 1208*m.b5*m.b7 + 1200*m.b5*m.b8
                        + 1192*m.b5*m.b9 + 1200*m.b5*m.b10 + 1144*m.b5*m.b11 + 1136*m.b5*m.b12 + 1160*m.b5*m.b13 + 1168*
                       m.b5*m.b14 + 1240*m.b5*m.b15 + 1296*m.b5*m.b16 + 1576*m.b5*m.b17 + 1600*m.b5*m.b18 + 1528*m.b5*
                       m.b19 + 1520*m.b5*m.b20 + 1448*m.b5*m.b21 + 1440*m.b5*m.b22 + 1368*m.b5*m.b23 + 1360*m.b5*m.b24
                        + 1288*m.b5*m.b25 + 1280*m.b5*m.b26 + 1000*m.b5*m.b27 + 768*m.b5*m.b28 + 504*m.b5*m.b29 + 256*
                       m.b5*m.b30 + 1296*m.b6*m.b7 + 1288*m.b6*m.b8 + 1280*m.b6*m.b9 + 1288*m.b6*m.b10 + 1280*m.b6*m.b11
                        + 1240*m.b6*m.b12 + 1232*m.b6*m.b13 + 1288*m.b6*m.b14 + 1312*m.b6*m.b15 + 1432*m.b6*m.b16 + 1520
                       *m.b6*m.b17 + 1864*m.b6*m.b18 + 1872*m.b6*m.b19 + 1784*m.b6*m.b20 + 1776*m.b6*m.b21 + 1688*m.b6*
                       m.b22 + 1680*m.b6*m.b23 + 1592*m.b6*m.b24 + 1584*m.b6*m.b25 + 1288*m.b6*m.b26 + 1056*m.b6*m.b27
                        + 776*m.b6*m.b28 + 528*m.b6*m.b29 + 264*m.b6*m.b30 + 1328*m.b7*m.b8 + 1336*m.b7*m.b9 + 1328*m.b7
                       *m.b10 + 1352*m.b7*m.b11 + 1344*m.b7*m.b12 + 1288*m.b7*m.b13 + 1312*m.b7*m.b14 + 1400*m.b7*m.b15
                        + 1456*m.b7*m.b16 + 1624*m.b7*m.b17 + 1728*m.b7*m.b18 + 2136*m.b7*m.b19 + 2128*m.b7*m.b20 + 2024
                       *m.b7*m.b21 + 2016*m.b7*m.b22 + 1912*m.b7*m.b23 + 1904*m.b7*m.b24 + 1592*m.b7*m.b25 + 1360*m.b7*
                       m.b26 + 1064*m.b7*m.b27 + 816*m.b7*m.b28 + 536*m.b7*m.b29 + 272*m.b7*m.b30 + 1328*m.b8*m.b9 + 
                       1352*m.b8*m.b10 + 1344*m.b8*m.b11 + 1384*m.b8*m.b12 + 1376*m.b8*m.b13 + 1320*m.b8*m.b14 + 1360*
                       m.b8*m.b15 + 1512*m.b8*m.b16 + 1600*m.b8*m.b17 + 1800*m.b8*m.b18 + 1920*m.b8*m.b19 + 2376*m.b8*
                       m.b20 + 2368*m.b8*m.b21 + 2248*m.b8*m.b22 + 2240*m.b8*m.b23 + 1912*m.b8*m.b24 + 1680*m.b8*m.b25
                        + 1368*m.b8*m.b26 + 1120*m.b8*m.b27 + 824*m.b8*m.b28 + 560*m.b8*m.b29 + 280*m.b8*m.b30 + 1296*
                       m.b9*m.b10 + 1336*m.b9*m.b11 + 1328*m.b9*m.b12 + 1384*m.b9*m.b13 + 1392*m.b9*m.b14 + 1336*m.b9*
                       m.b15 + 1408*m.b9*m.b16 + 1608*m.b9*m.b17 + 1728*m.b9*m.b18 + 1960*m.b9*m.b19 + 2096*m.b9*m.b20
                        + 2600*m.b9*m.b21 + 2592*m.b9*m.b22 + 2248*m.b9*m.b23 + 2016*m.b9*m.b24 + 1688*m.b9*m.b25 + 1440
                       *m.b9*m.b26 + 1128*m.b9*m.b27 + 864*m.b9*m.b28 + 568*m.b9*m.b29 + 288*m.b9*m.b30 + 1232*m.b10*
                       m.b11 + 1288*m.b10*m.b12 + 1280*m.b10*m.b13 + 1368*m.b10*m.b14 + 1392*m.b10*m.b15 + 1352*m.b10*
                       m.b16 + 1456*m.b10*m.b17 + 1688*m.b10*m.b18 + 1824*m.b10*m.b19 + 2104*m.b10*m.b20 + 2240*m.b10*
                       m.b21 + 2600*m.b10*m.b22 + 2368*m.b10*m.b23 + 2024*m.b10*m.b24 + 1776*m.b10*m.b25 + 1448*m.b10*
                       m.b26 + 1184*m.b10*m.b27 + 872*m.b10*m.b28 + 592*m.b10*m.b29 + 296*m.b10*m.b30 + 1184*m.b11*m.b12
                        + 1256*m.b11*m.b13 + 1264*m.b11*m.b14 + 1384*m.b11*m.b15 + 1424*m.b11*m.b16 + 1416*m.b11*m.b17
                        + 1536*m.b11*m.b18 + 1800*m.b11*m.b19 + 1952*m.b11*m.b20 + 2104*m.b11*m.b21 + 2096*m.b11*m.b22
                        + 2376*m.b11*m.b23 + 2128*m.b11*m.b24 + 1784*m.b11*m.b25 + 1520*m.b11*m.b26 + 1192*m.b11*m.b27
                        + 912*m.b11*m.b28 + 600*m.b11*m.b29 + 304*m.b11*m.b30 + 1168*m.b12*m.b13 + 1272*m.b12*m.b14 + 
                       1296*m.b12*m.b15 + 1448*m.b12*m.b16 + 1504*m.b12*m.b17 + 1528*m.b12*m.b18 + 1664*m.b12*m.b19 + 
                       1800*m.b12*m.b20 + 1824*m.b12*m.b21 + 1960*m.b12*m.b22 + 1920*m.b12*m.b23 + 2136*m.b12*m.b24 + 
                       1872*m.b12*m.b25 + 1528*m.b12*m.b26 + 1248*m.b12*m.b27 + 920*m.b12*m.b28 + 624*m.b12*m.b29 + 312*
                       m.b12*m.b30 + 1200*m.b13*m.b14 + 1336*m.b13*m.b15 + 1376*m.b13*m.b16 + 1560*m.b13*m.b17 + 1632*
                       m.b13*m.b18 + 1528*m.b13*m.b19 + 1536*m.b13*m.b20 + 1688*m.b13*m.b21 + 1728*m.b13*m.b22 + 1800*
                       m.b13*m.b23 + 1728*m.b13*m.b24 + 1864*m.b13*m.b25 + 1600*m.b13*m.b26 + 1256*m.b13*m.b27 + 960*
                       m.b13*m.b28 + 632*m.b13*m.b29 + 320*m.b13*m.b30 + 1280*m.b14*m.b15 + 1448*m.b14*m.b16 + 1504*
                       m.b14*m.b17 + 1560*m.b14*m.b18 + 1504*m.b14*m.b19 + 1416*m.b14*m.b20 + 1456*m.b14*m.b21 + 1608*
                       m.b14*m.b22 + 1600*m.b14*m.b23 + 1624*m.b14*m.b24 + 1520*m.b14*m.b25 + 1576*m.b14*m.b26 + 1296*
                       m.b14*m.b27 + 968*m.b14*m.b28 + 656*m.b14*m.b29 + 328*m.b14*m.b30 + 1408*m.b15*m.b16 + 1448*m.b15
                       *m.b17 + 1376*m.b15*m.b18 + 1448*m.b15*m.b19 + 1424*m.b15*m.b20 + 1352*m.b15*m.b21 + 1408*m.b15*
                       m.b22 + 1512*m.b15*m.b23 + 1456*m.b15*m.b24 + 1432*m.b15*m.b25 + 1296*m.b15*m.b26 + 1272*m.b15*
                       m.b27 + 976*m.b15*m.b28 + 648*m.b15*m.b29 + 336*m.b15*m.b30 + 1280*m.b16*m.b17 + 1336*m.b16*m.b18
                        + 1296*m.b16*m.b19 + 1384*m.b16*m.b20 + 1392*m.b16*m.b21 + 1336*m.b16*m.b22 + 1360*m.b16*m.b23
                        + 1400*m.b16*m.b24 + 1312*m.b16*m.b25 + 1240*m.b16*m.b26 + 1072*m.b16*m.b27 + 968*m.b16*m.b28 + 
                       656*m.b16*m.b29 + 328*m.b16*m.b30 + 1200*m.b17*m.b18 + 1272*m.b17*m.b19 + 1264*m.b17*m.b20 + 1368
                       *m.b17*m.b21 + 1392*m.b17*m.b22 + 1320*m.b17*m.b23 + 1312*m.b17*m.b24 + 1288*m.b17*m.b25 + 1168*
                       m.b17*m.b26 + 1048*m.b17*m.b27 + 848*m.b17*m.b28 + 664*m.b17*m.b29 + 336*m.b17*m.b30 + 1168*m.b18
                       *m.b19 + 1256*m.b18*m.b20 + 1280*m.b18*m.b21 + 1384*m.b18*m.b22 + 1376*m.b18*m.b23 + 1288*m.b18*
                       m.b24 + 1232*m.b18*m.b25 + 1160*m.b18*m.b26 + 1008*m.b18*m.b27 + 840*m.b18*m.b28 + 608*m.b18*
                       m.b29 + 344*m.b18*m.b30 + 1184*m.b19*m.b20 + 1288*m.b19*m.b21 + 1328*m.b19*m.b22 + 1384*m.b19*
                       m.b23 + 1344*m.b19*m.b24 + 1240*m.b19*m.b25 + 1136*m.b19*m.b26 + 1016*m.b19*m.b27 + 832*m.b19*
                       m.b28 + 616*m.b19*m.b29 + 352*m.b19*m.b30 + 1232*m.b20*m.b21 + 1336*m.b20*m.b22 + 1344*m.b20*
                       m.b23 + 1352*m.b20*m.b24 + 1280*m.b20*m.b25 + 1144*m.b20*m.b26 + 1008*m.b20*m.b27 + 840*m.b20*
                       m.b28 + 624*m.b20*m.b29 + 360*m.b20*m.b30 + 1296*m.b21*m.b22 + 1352*m.b21*m.b23 + 1328*m.b21*
                       m.b24 + 1288*m.b21*m.b25 + 1200*m.b21*m.b26 + 1016*m.b21*m.b27 + 848*m.b21*m.b28 + 632*m.b21*
                       m.b29 + 368*m.b21*m.b30 + 1328*m.b22*m.b23 + 1336*m.b22*m.b24 + 1280*m.b22*m.b25 + 1192*m.b22*
                       m.b26 + 1072*m.b22*m.b27 + 856*m.b22*m.b28 + 640*m.b22*m.b29 + 376*m.b22*m.b30 + 1328*m.b23*m.b24
                        + 1288*m.b23*m.b25 + 1200*m.b23*m.b26 + 1080*m.b23*m.b27 + 896*m.b23*m.b28 + 648*m.b23*m.b29 + 
                       384*m.b23*m.b30 + 1296*m.b24*m.b25 + 1208*m.b24*m.b26 + 1072*m.b24*m.b27 + 904*m.b24*m.b28 + 672*
                       m.b24*m.b29 + 392*m.b24*m.b30 + 1216*m.b25*m.b26 + 1080*m.b25*m.b27 + 912*m.b25*m.b28 + 680*m.b25
                       *m.b29 + 400*m.b25*m.b30 + 1088*m.b26*m.b27 + 904*m.b26*m.b28 + 688*m.b26*m.b29 + 408*m.b26*m.b30
                        + 912*m.b27*m.b28 + 696*m.b27*m.b29 + 416*m.b27*m.b30 + 688*m.b28*m.b29 + 424*m.b28*m.b30 + 432*
                       m.b29*m.b30 - 1624*m.b1 - 2880*m.b2 - 3952*m.b3 - 4848*m.b4 - 5568*m.b5 - 6120*m.b6 - 6504*m.b7
                        - 6720*m.b8 - 6768*m.b9 - 6656*m.b10 - 6496*m.b11 - 6328*m.b12 - 6152*m.b13 - 6008*m.b14 - 5896*
                       m.b15 - 5896*m.b16 - 6008*m.b17 - 6152*m.b18 - 6328*m.b19 - 6496*m.b20 - 6656*m.b21 - 6768*m.b22
                        - 6720*m.b23 - 6504*m.b24 - 6120*m.b25 - 5568*m.b26 - 4848*m.b27 - 3952*m.b28 - 2880*m.b29 - 
                       1624*m.b30 - m.x31 <= 0)
