#  MINLP written by GAMS Convert at 08/13/20 17:37:45
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

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b2*m.b3*m.b4*m.b5 + 64*m.b3*m.b4*m.b5*m.b6 + 64*m.b4*m.b5*m.b6*m.b7
                        + 64*m.b5*m.b6*m.b7*m.b8 + 64*m.b6*m.b7*m.b8*m.b9 + 64*m.b7*m.b8*m.b9*m.b10 + 64*m.b8*m.b9*m.b10
                       *m.b11 + 64*m.b9*m.b10*m.b11*m.b12 + 64*m.b10*m.b11*m.b12*m.b13 + 64*m.b11*m.b12*m.b13*m.b14 + 64
                       *m.b12*m.b13*m.b14*m.b15 + 64*m.b13*m.b14*m.b15*m.b16 + 64*m.b14*m.b15*m.b16*m.b17 + 64*m.b15*
                       m.b16*m.b17*m.b18 + 64*m.b16*m.b17*m.b18*m.b19 + 64*m.b17*m.b18*m.b19*m.b20 + 64*m.b18*m.b19*
                       m.b20*m.b21 + 64*m.b19*m.b20*m.b21*m.b22 + 64*m.b20*m.b21*m.b22*m.b23 + 64*m.b21*m.b22*m.b23*
                       m.b24 + 64*m.b22*m.b23*m.b24*m.b25 + 64*m.b23*m.b24*m.b25*m.b26 + 64*m.b24*m.b25*m.b26*m.b27 + 64
                       *m.b25*m.b26*m.b27*m.b28 + 64*m.b26*m.b27*m.b28*m.b29 + 64*m.b27*m.b28*m.b29*m.b30 - 32*m.b1*m.b2
                       *m.b3 - 32*m.b1*m.b2*m.b4 - 32*m.b1*m.b3*m.b4 - 64*m.b2*m.b3*m.b4 - 32*m.b2*m.b3*m.b5 - 32*m.b2*
                       m.b4*m.b5 - 64*m.b3*m.b4*m.b5 - 32*m.b3*m.b4*m.b6 - 32*m.b3*m.b5*m.b6 - 64*m.b4*m.b5*m.b6 - 32*
                       m.b4*m.b5*m.b7 - 32*m.b4*m.b6*m.b7 - 64*m.b5*m.b6*m.b7 - 32*m.b5*m.b6*m.b8 - 32*m.b5*m.b7*m.b8 - 
                       64*m.b6*m.b7*m.b8 - 32*m.b6*m.b7*m.b9 - 32*m.b6*m.b8*m.b9 - 64*m.b7*m.b8*m.b9 - 32*m.b7*m.b8*
                       m.b10 - 32*m.b7*m.b9*m.b10 - 64*m.b8*m.b9*m.b10 - 32*m.b8*m.b9*m.b11 - 32*m.b8*m.b10*m.b11 - 64*
                       m.b9*m.b10*m.b11 - 32*m.b9*m.b10*m.b12 - 32*m.b9*m.b11*m.b12 - 64*m.b10*m.b11*m.b12 - 32*m.b10*
                       m.b11*m.b13 - 32*m.b10*m.b12*m.b13 - 64*m.b11*m.b12*m.b13 - 32*m.b11*m.b12*m.b14 - 32*m.b11*m.b13
                       *m.b14 - 64*m.b12*m.b13*m.b14 - 32*m.b12*m.b13*m.b15 - 32*m.b12*m.b14*m.b15 - 64*m.b13*m.b14*
                       m.b15 - 32*m.b13*m.b14*m.b16 - 32*m.b13*m.b15*m.b16 - 64*m.b14*m.b15*m.b16 - 32*m.b14*m.b15*m.b17
                        - 32*m.b14*m.b16*m.b17 - 64*m.b15*m.b16*m.b17 - 32*m.b15*m.b16*m.b18 - 32*m.b15*m.b17*m.b18 - 64
                       *m.b16*m.b17*m.b18 - 32*m.b16*m.b17*m.b19 - 32*m.b16*m.b18*m.b19 - 64*m.b17*m.b18*m.b19 - 32*
                       m.b17*m.b18*m.b20 - 32*m.b17*m.b19*m.b20 - 64*m.b18*m.b19*m.b20 - 32*m.b18*m.b19*m.b21 - 32*m.b18
                       *m.b20*m.b21 - 64*m.b19*m.b20*m.b21 - 32*m.b19*m.b20*m.b22 - 32*m.b19*m.b21*m.b22 - 64*m.b20*
                       m.b21*m.b22 - 32*m.b20*m.b21*m.b23 - 32*m.b20*m.b22*m.b23 - 64*m.b21*m.b22*m.b23 - 32*m.b21*m.b22
                       *m.b24 - 32*m.b21*m.b23*m.b24 - 64*m.b22*m.b23*m.b24 - 32*m.b22*m.b23*m.b25 - 32*m.b22*m.b24*
                       m.b25 - 64*m.b23*m.b24*m.b25 - 32*m.b23*m.b24*m.b26 - 32*m.b23*m.b25*m.b26 - 64*m.b24*m.b25*m.b26
                        - 32*m.b24*m.b25*m.b27 - 32*m.b24*m.b26*m.b27 - 64*m.b25*m.b26*m.b27 - 32*m.b25*m.b26*m.b28 - 32
                       *m.b25*m.b27*m.b28 - 64*m.b26*m.b27*m.b28 - 32*m.b26*m.b27*m.b29 - 32*m.b26*m.b28*m.b29 - 64*
                       m.b27*m.b28*m.b29 - 32*m.b27*m.b28*m.b30 - 32*m.b27*m.b29*m.b30 - 32*m.b28*m.b29*m.b30 + 16*m.b1*
                       m.b2 + 24*m.b1*m.b3 + 16*m.b1*m.b4 + 32*m.b2*m.b3 + 48*m.b2*m.b4 + 16*m.b2*m.b5 + 48*m.b3*m.b4 + 
                       48*m.b3*m.b5 + 16*m.b3*m.b6 + 48*m.b4*m.b5 + 48*m.b4*m.b6 + 16*m.b4*m.b7 + 48*m.b5*m.b6 + 48*m.b5
                       *m.b7 + 16*m.b5*m.b8 + 48*m.b6*m.b7 + 48*m.b6*m.b8 + 16*m.b6*m.b9 + 48*m.b7*m.b8 + 48*m.b7*m.b9
                        + 16*m.b7*m.b10 + 48*m.b8*m.b9 + 48*m.b8*m.b10 + 16*m.b8*m.b11 + 48*m.b9*m.b10 + 48*m.b9*m.b11
                        + 16*m.b9*m.b12 + 48*m.b10*m.b11 + 48*m.b10*m.b12 + 16*m.b10*m.b13 + 48*m.b11*m.b12 + 48*m.b11*
                       m.b13 + 16*m.b11*m.b14 + 48*m.b12*m.b13 + 48*m.b12*m.b14 + 16*m.b12*m.b15 + 48*m.b13*m.b14 + 48*
                       m.b13*m.b15 + 16*m.b13*m.b16 + 48*m.b14*m.b15 + 48*m.b14*m.b16 + 16*m.b14*m.b17 + 48*m.b15*m.b16
                        + 48*m.b15*m.b17 + 16*m.b15*m.b18 + 48*m.b16*m.b17 + 48*m.b16*m.b18 + 16*m.b16*m.b19 + 48*m.b17*
                       m.b18 + 48*m.b17*m.b19 + 16*m.b17*m.b20 + 48*m.b18*m.b19 + 48*m.b18*m.b20 + 16*m.b18*m.b21 + 48*
                       m.b19*m.b20 + 48*m.b19*m.b21 + 16*m.b19*m.b22 + 48*m.b20*m.b21 + 48*m.b20*m.b22 + 16*m.b20*m.b23
                        + 48*m.b21*m.b22 + 48*m.b21*m.b23 + 16*m.b21*m.b24 + 48*m.b22*m.b23 + 48*m.b22*m.b24 + 16*m.b22*
                       m.b25 + 48*m.b23*m.b24 + 48*m.b23*m.b25 + 16*m.b23*m.b26 + 48*m.b24*m.b25 + 48*m.b24*m.b26 + 16*
                       m.b24*m.b27 + 48*m.b25*m.b26 + 48*m.b25*m.b27 + 16*m.b25*m.b28 + 48*m.b26*m.b27 + 48*m.b26*m.b28
                        + 16*m.b26*m.b29 + 48*m.b27*m.b28 + 48*m.b27*m.b29 + 16*m.b27*m.b30 + 32*m.b28*m.b29 + 24*m.b28*
                       m.b30 + 16*m.b29*m.b30 - 12*m.b1 - 24*m.b2 - 36*m.b3 - 48*m.b4 - 48*m.b5 - 48*m.b6 - 48*m.b7 - 48
                       *m.b8 - 48*m.b9 - 48*m.b10 - 48*m.b11 - 48*m.b12 - 48*m.b13 - 48*m.b14 - 48*m.b15 - 48*m.b16 - 48
                       *m.b17 - 48*m.b18 - 48*m.b19 - 48*m.b20 - 48*m.b21 - 48*m.b22 - 48*m.b23 - 48*m.b24 - 48*m.b25 - 
                       48*m.b26 - 48*m.b27 - 36*m.b28 - 24*m.b29 - 12*m.b30 - m.x31 <= 0)
