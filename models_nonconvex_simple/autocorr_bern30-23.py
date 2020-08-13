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
                       m.b2*m.b21*m.b22 + 64*m.b1*m.b2*m.b22*m.b23 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 
                       64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*
                       m.b11 + 64*m.b1*m.b3*m.b10*m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*
                       m.b3*m.b13*m.b15 + 64*m.b1*m.b3*m.b14*m.b16 + 64*m.b1*m.b3*m.b15*m.b17 + 64*m.b1*m.b3*m.b16*m.b18
                        + 64*m.b1*m.b3*m.b17*m.b19 + 64*m.b1*m.b3*m.b18*m.b20 + 64*m.b1*m.b3*m.b19*m.b21 + 64*m.b1*m.b3*
                       m.b20*m.b22 + 64*m.b1*m.b3*m.b21*m.b23 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*
                       m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4*m.b10*
                       m.b13 + 64*m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b4*m.b12*m.b15 + 64*m.b1*m.b4*m.b13*m.b16 + 64*m.b1*
                       m.b4*m.b14*m.b17 + 64*m.b1*m.b4*m.b15*m.b18 + 64*m.b1*m.b4*m.b16*m.b19 + 64*m.b1*m.b4*m.b17*m.b20
                        + 64*m.b1*m.b4*m.b18*m.b21 + 64*m.b1*m.b4*m.b19*m.b22 + 64*m.b1*m.b4*m.b20*m.b23 + 64*m.b1*m.b5*
                       m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*m.b1*m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*
                       m.b1*m.b5*m.b10*m.b14 + 64*m.b1*m.b5*m.b11*m.b15 + 64*m.b1*m.b5*m.b12*m.b16 + 64*m.b1*m.b5*m.b13*
                       m.b17 + 64*m.b1*m.b5*m.b14*m.b18 + 64*m.b1*m.b5*m.b15*m.b19 + 64*m.b1*m.b5*m.b16*m.b20 + 64*m.b1*
                       m.b5*m.b17*m.b21 + 64*m.b1*m.b5*m.b18*m.b22 + 64*m.b1*m.b5*m.b19*m.b23 + 64*m.b1*m.b6*m.b7*m.b12
                        + 64*m.b1*m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b6*m.b10*m.b15 + 64*m.b1*m.b6*
                       m.b11*m.b16 + 64*m.b1*m.b6*m.b12*m.b17 + 64*m.b1*m.b6*m.b13*m.b18 + 64*m.b1*m.b6*m.b14*m.b19 + 64
                       *m.b1*m.b6*m.b15*m.b20 + 64*m.b1*m.b6*m.b16*m.b21 + 64*m.b1*m.b6*m.b17*m.b22 + 64*m.b1*m.b6*m.b18
                       *m.b23 + 64*m.b1*m.b7*m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 64*m.b1*m.b7*m.b10*m.b16 + 64*m.b1*
                       m.b7*m.b11*m.b17 + 64*m.b1*m.b7*m.b12*m.b18 + 64*m.b1*m.b7*m.b13*m.b19 + 64*m.b1*m.b7*m.b14*m.b20
                        + 64*m.b1*m.b7*m.b15*m.b21 + 64*m.b1*m.b7*m.b16*m.b22 + 64*m.b1*m.b7*m.b17*m.b23 + 64*m.b1*m.b8*
                       m.b9*m.b16 + 64*m.b1*m.b8*m.b10*m.b17 + 64*m.b1*m.b8*m.b11*m.b18 + 64*m.b1*m.b8*m.b12*m.b19 + 64*
                       m.b1*m.b8*m.b13*m.b20 + 64*m.b1*m.b8*m.b14*m.b21 + 64*m.b1*m.b8*m.b15*m.b22 + 64*m.b1*m.b8*m.b16*
                       m.b23 + 64*m.b1*m.b9*m.b10*m.b18 + 64*m.b1*m.b9*m.b11*m.b19 + 64*m.b1*m.b9*m.b12*m.b20 + 64*m.b1*
                       m.b9*m.b13*m.b21 + 64*m.b1*m.b9*m.b14*m.b22 + 64*m.b1*m.b9*m.b15*m.b23 + 64*m.b1*m.b10*m.b11*
                       m.b20 + 64*m.b1*m.b10*m.b12*m.b21 + 64*m.b1*m.b10*m.b13*m.b22 + 64*m.b1*m.b10*m.b14*m.b23 + 64*
                       m.b1*m.b11*m.b12*m.b22 + 64*m.b1*m.b11*m.b13*m.b23 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5
                       *m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*
                       m.b3*m.b9*m.b10 + 128*m.b2*m.b3*m.b10*m.b11 + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*m.b12*
                       m.b13 + 128*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 128*m.b2*m.b3*m.b15*m.b16 + 128*
                       m.b2*m.b3*m.b16*m.b17 + 128*m.b2*m.b3*m.b17*m.b18 + 128*m.b2*m.b3*m.b18*m.b19 + 128*m.b2*m.b3*
                       m.b19*m.b20 + 128*m.b2*m.b3*m.b20*m.b21 + 128*m.b2*m.b3*m.b21*m.b22 + 128*m.b2*m.b3*m.b22*m.b23
                        + 64*m.b2*m.b3*m.b23*m.b24 + 128*m.b2*m.b4*m.b5*m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*
                       m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128
                       *m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*m.b14 + 128*m.b2*m.b4*m.b13*m.b15 + 128*m.b2*m.b4*
                       m.b14*m.b16 + 128*m.b2*m.b4*m.b15*m.b17 + 128*m.b2*m.b4*m.b16*m.b18 + 128*m.b2*m.b4*m.b17*m.b19
                        + 128*m.b2*m.b4*m.b18*m.b20 + 128*m.b2*m.b4*m.b19*m.b21 + 128*m.b2*m.b4*m.b20*m.b22 + 128*m.b2*
                       m.b4*m.b21*m.b23 + 64*m.b2*m.b4*m.b22*m.b24 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2*m.b5*m.b7*m.b10
                        + 128*m.b2*m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 128*m.b2*
                       m.b5*m.b11*m.b14 + 128*m.b2*m.b5*m.b12*m.b15 + 128*m.b2*m.b5*m.b13*m.b16 + 128*m.b2*m.b5*m.b14*
                       m.b17 + 128*m.b2*m.b5*m.b15*m.b18 + 128*m.b2*m.b5*m.b16*m.b19 + 128*m.b2*m.b5*m.b17*m.b20 + 128*
                       m.b2*m.b5*m.b18*m.b21 + 128*m.b2*m.b5*m.b19*m.b22 + 128*m.b2*m.b5*m.b20*m.b23 + 64*m.b2*m.b5*
                       m.b21*m.b24 + 128*m.b2*m.b6*m.b7*m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 
                       128*m.b2*m.b6*m.b10*m.b14 + 128*m.b2*m.b6*m.b11*m.b15 + 128*m.b2*m.b6*m.b12*m.b16 + 128*m.b2*m.b6
                       *m.b13*m.b17 + 128*m.b2*m.b6*m.b14*m.b18 + 128*m.b2*m.b6*m.b15*m.b19 + 128*m.b2*m.b6*m.b16*m.b20
                        + 128*m.b2*m.b6*m.b17*m.b21 + 128*m.b2*m.b6*m.b18*m.b22 + 128*m.b2*m.b6*m.b19*m.b23 + 64*m.b2*
                       m.b6*m.b20*m.b24 + 128*m.b2*m.b7*m.b8*m.b13 + 128*m.b2*m.b7*m.b9*m.b14 + 128*m.b2*m.b7*m.b10*
                       m.b15 + 128*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b7*m.b12*m.b17 + 128*m.b2*m.b7*m.b13*m.b18 + 128*
                       m.b2*m.b7*m.b14*m.b19 + 128*m.b2*m.b7*m.b15*m.b20 + 128*m.b2*m.b7*m.b16*m.b21 + 128*m.b2*m.b7*
                       m.b17*m.b22 + 128*m.b2*m.b7*m.b18*m.b23 + 64*m.b2*m.b7*m.b19*m.b24 + 128*m.b2*m.b8*m.b9*m.b15 + 
                       128*m.b2*m.b8*m.b10*m.b16 + 128*m.b2*m.b8*m.b11*m.b17 + 128*m.b2*m.b8*m.b12*m.b18 + 128*m.b2*m.b8
                       *m.b13*m.b19 + 128*m.b2*m.b8*m.b14*m.b20 + 128*m.b2*m.b8*m.b15*m.b21 + 128*m.b2*m.b8*m.b16*m.b22
                        + 128*m.b2*m.b8*m.b17*m.b23 + 64*m.b2*m.b8*m.b18*m.b24 + 128*m.b2*m.b9*m.b10*m.b17 + 128*m.b2*
                       m.b9*m.b11*m.b18 + 128*m.b2*m.b9*m.b12*m.b19 + 128*m.b2*m.b9*m.b13*m.b20 + 128*m.b2*m.b9*m.b14*
                       m.b21 + 128*m.b2*m.b9*m.b15*m.b22 + 128*m.b2*m.b9*m.b16*m.b23 + 64*m.b2*m.b9*m.b17*m.b24 + 128*
                       m.b2*m.b10*m.b11*m.b19 + 128*m.b2*m.b10*m.b12*m.b20 + 128*m.b2*m.b10*m.b13*m.b21 + 128*m.b2*m.b10
                       *m.b14*m.b22 + 128*m.b2*m.b10*m.b15*m.b23 + 64*m.b2*m.b10*m.b16*m.b24 + 128*m.b2*m.b11*m.b12*
                       m.b21 + 128*m.b2*m.b11*m.b13*m.b22 + 128*m.b2*m.b11*m.b14*m.b23 + 64*m.b2*m.b11*m.b15*m.b24 + 128
                       *m.b2*m.b12*m.b13*m.b23 + 64*m.b2*m.b12*m.b14*m.b24 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*
                       m.b6*m.b7 + 192*m.b3*m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 192*
                       m.b3*m.b4*m.b10*m.b11 + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 192*m.b3*m.b4*
                       m.b13*m.b14 + 192*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b4*m.b15*m.b16 + 192*m.b3*m.b4*m.b16*m.b17
                        + 192*m.b3*m.b4*m.b17*m.b18 + 192*m.b3*m.b4*m.b18*m.b19 + 192*m.b3*m.b4*m.b19*m.b20 + 192*m.b3*
                       m.b4*m.b20*m.b21 + 192*m.b3*m.b4*m.b21*m.b22 + 192*m.b3*m.b4*m.b22*m.b23 + 128*m.b3*m.b4*m.b23*
                       m.b24 + 64*m.b3*m.b4*m.b24*m.b25 + 192*m.b3*m.b5*m.b6*m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*
                       m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*m.b5*m.b10*m.b12 + 192*m.b3*m.b5*m.b11*
                       m.b13 + 192*m.b3*m.b5*m.b12*m.b14 + 192*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b5*m.b14*m.b16 + 192*
                       m.b3*m.b5*m.b15*m.b17 + 192*m.b3*m.b5*m.b16*m.b18 + 192*m.b3*m.b5*m.b17*m.b19 + 192*m.b3*m.b5*
                       m.b18*m.b20 + 192*m.b3*m.b5*m.b19*m.b21 + 192*m.b3*m.b5*m.b20*m.b22 + 192*m.b3*m.b5*m.b21*m.b23
                        + 128*m.b3*m.b5*m.b22*m.b24 + 64*m.b3*m.b5*m.b23*m.b25 + 192*m.b3*m.b6*m.b7*m.b10 + 192*m.b3*
                       m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13 + 192*m.b3*m.b6*m.b11*
                       m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b6*m.b13*m.b16 + 192*m.b3*m.b6*m.b14*m.b17 + 192*
                       m.b3*m.b6*m.b15*m.b18 + 192*m.b3*m.b6*m.b16*m.b19 + 192*m.b3*m.b6*m.b17*m.b20 + 192*m.b3*m.b6*
                       m.b18*m.b21 + 192*m.b3*m.b6*m.b19*m.b22 + 192*m.b3*m.b6*m.b20*m.b23 + 128*m.b3*m.b6*m.b21*m.b24
                        + 64*m.b3*m.b6*m.b22*m.b25 + 192*m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*m.b13 + 192*m.b3*m.b7
                       *m.b10*m.b14 + 192*m.b3*m.b7*m.b11*m.b15 + 192*m.b3*m.b7*m.b12*m.b16 + 192*m.b3*m.b7*m.b13*m.b17
                        + 192*m.b3*m.b7*m.b14*m.b18 + 192*m.b3*m.b7*m.b15*m.b19 + 192*m.b3*m.b7*m.b16*m.b20 + 192*m.b3*
                       m.b7*m.b17*m.b21 + 192*m.b3*m.b7*m.b18*m.b22 + 192*m.b3*m.b7*m.b19*m.b23 + 128*m.b3*m.b7*m.b20*
                       m.b24 + 64*m.b3*m.b7*m.b21*m.b25 + 192*m.b3*m.b8*m.b9*m.b14 + 192*m.b3*m.b8*m.b10*m.b15 + 192*
                       m.b3*m.b8*m.b11*m.b16 + 192*m.b3*m.b8*m.b12*m.b17 + 192*m.b3*m.b8*m.b13*m.b18 + 192*m.b3*m.b8*
                       m.b14*m.b19 + 192*m.b3*m.b8*m.b15*m.b20 + 192*m.b3*m.b8*m.b16*m.b21 + 192*m.b3*m.b8*m.b17*m.b22
                        + 192*m.b3*m.b8*m.b18*m.b23 + 128*m.b3*m.b8*m.b19*m.b24 + 64*m.b3*m.b8*m.b20*m.b25 + 192*m.b3*
                       m.b9*m.b10*m.b16 + 192*m.b3*m.b9*m.b11*m.b17 + 192*m.b3*m.b9*m.b12*m.b18 + 192*m.b3*m.b9*m.b13*
                       m.b19 + 192*m.b3*m.b9*m.b14*m.b20 + 192*m.b3*m.b9*m.b15*m.b21 + 192*m.b3*m.b9*m.b16*m.b22 + 192*
                       m.b3*m.b9*m.b17*m.b23 + 128*m.b3*m.b9*m.b18*m.b24 + 64*m.b3*m.b9*m.b19*m.b25 + 192*m.b3*m.b10*
                       m.b11*m.b18 + 192*m.b3*m.b10*m.b12*m.b19 + 192*m.b3*m.b10*m.b13*m.b20 + 192*m.b3*m.b10*m.b14*
                       m.b21 + 192*m.b3*m.b10*m.b15*m.b22 + 192*m.b3*m.b10*m.b16*m.b23 + 128*m.b3*m.b10*m.b17*m.b24 + 64
                       *m.b3*m.b10*m.b18*m.b25 + 192*m.b3*m.b11*m.b12*m.b20 + 192*m.b3*m.b11*m.b13*m.b21 + 192*m.b3*
                       m.b11*m.b14*m.b22 + 192*m.b3*m.b11*m.b15*m.b23 + 128*m.b3*m.b11*m.b16*m.b24 + 64*m.b3*m.b11*m.b17
                       *m.b25 + 192*m.b3*m.b12*m.b13*m.b22 + 192*m.b3*m.b12*m.b14*m.b23 + 128*m.b3*m.b12*m.b15*m.b24 + 
                       64*m.b3*m.b12*m.b16*m.b25 + 128*m.b3*m.b13*m.b14*m.b24 + 64*m.b3*m.b13*m.b15*m.b25 + 256*m.b4*
                       m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*m.b4*m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 
                       256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*m.b12 + 256*m.b4*m.b5*m.b12*m.b13 + 256*m.b4*m.b5
                       *m.b13*m.b14 + 256*m.b4*m.b5*m.b14*m.b15 + 256*m.b4*m.b5*m.b15*m.b16 + 256*m.b4*m.b5*m.b16*m.b17
                        + 256*m.b4*m.b5*m.b17*m.b18 + 256*m.b4*m.b5*m.b18*m.b19 + 256*m.b4*m.b5*m.b19*m.b20 + 256*m.b4*
                       m.b5*m.b20*m.b21 + 256*m.b4*m.b5*m.b21*m.b22 + 256*m.b4*m.b5*m.b22*m.b23 + 192*m.b4*m.b5*m.b23*
                       m.b24 + 128*m.b4*m.b5*m.b24*m.b25 + 64*m.b4*m.b5*m.b25*m.b26 + 256*m.b4*m.b6*m.b7*m.b9 + 256*m.b4
                       *m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 256*m.b4*m.b6*m.b10*m.b12 + 256*m.b4*m.b6*m.b11*
                       m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*m.b6*m.b13*m.b15 + 256*m.b4*m.b6*m.b14*m.b16 + 256*
                       m.b4*m.b6*m.b15*m.b17 + 256*m.b4*m.b6*m.b16*m.b18 + 256*m.b4*m.b6*m.b17*m.b19 + 256*m.b4*m.b6*
                       m.b18*m.b20 + 256*m.b4*m.b6*m.b19*m.b21 + 256*m.b4*m.b6*m.b20*m.b22 + 256*m.b4*m.b6*m.b21*m.b23
                        + 192*m.b4*m.b6*m.b22*m.b24 + 128*m.b4*m.b6*m.b23*m.b25 + 64*m.b4*m.b6*m.b24*m.b26 + 256*m.b4*
                       m.b7*m.b8*m.b11 + 256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7*m.b10*m.b13 + 256*m.b4*m.b7*m.b11*
                       m.b14 + 256*m.b4*m.b7*m.b12*m.b15 + 256*m.b4*m.b7*m.b13*m.b16 + 256*m.b4*m.b7*m.b14*m.b17 + 256*
                       m.b4*m.b7*m.b15*m.b18 + 256*m.b4*m.b7*m.b16*m.b19 + 256*m.b4*m.b7*m.b17*m.b20 + 256*m.b4*m.b7*
                       m.b18*m.b21 + 256*m.b4*m.b7*m.b19*m.b22 + 256*m.b4*m.b7*m.b20*m.b23 + 192*m.b4*m.b7*m.b21*m.b24
                        + 128*m.b4*m.b7*m.b22*m.b25 + 64*m.b4*m.b7*m.b23*m.b26 + 256*m.b4*m.b8*m.b9*m.b13 + 256*m.b4*
                       m.b8*m.b10*m.b14 + 256*m.b4*m.b8*m.b11*m.b15 + 256*m.b4*m.b8*m.b12*m.b16 + 256*m.b4*m.b8*m.b13*
                       m.b17 + 256*m.b4*m.b8*m.b14*m.b18 + 256*m.b4*m.b8*m.b15*m.b19 + 256*m.b4*m.b8*m.b16*m.b20 + 256*
                       m.b4*m.b8*m.b17*m.b21 + 256*m.b4*m.b8*m.b18*m.b22 + 256*m.b4*m.b8*m.b19*m.b23 + 192*m.b4*m.b8*
                       m.b20*m.b24 + 128*m.b4*m.b8*m.b21*m.b25 + 64*m.b4*m.b8*m.b22*m.b26 + 256*m.b4*m.b9*m.b10*m.b15 + 
                       256*m.b4*m.b9*m.b11*m.b16 + 256*m.b4*m.b9*m.b12*m.b17 + 256*m.b4*m.b9*m.b13*m.b18 + 256*m.b4*m.b9
                       *m.b14*m.b19 + 256*m.b4*m.b9*m.b15*m.b20 + 256*m.b4*m.b9*m.b16*m.b21 + 256*m.b4*m.b9*m.b17*m.b22
                        + 256*m.b4*m.b9*m.b18*m.b23 + 192*m.b4*m.b9*m.b19*m.b24 + 128*m.b4*m.b9*m.b20*m.b25 + 64*m.b4*
                       m.b9*m.b21*m.b26 + 256*m.b4*m.b10*m.b11*m.b17 + 256*m.b4*m.b10*m.b12*m.b18 + 256*m.b4*m.b10*m.b13
                       *m.b19 + 256*m.b4*m.b10*m.b14*m.b20 + 256*m.b4*m.b10*m.b15*m.b21 + 256*m.b4*m.b10*m.b16*m.b22 + 
                       256*m.b4*m.b10*m.b17*m.b23 + 192*m.b4*m.b10*m.b18*m.b24 + 128*m.b4*m.b10*m.b19*m.b25 + 64*m.b4*
                       m.b10*m.b20*m.b26 + 256*m.b4*m.b11*m.b12*m.b19 + 256*m.b4*m.b11*m.b13*m.b20 + 256*m.b4*m.b11*
                       m.b14*m.b21 + 256*m.b4*m.b11*m.b15*m.b22 + 256*m.b4*m.b11*m.b16*m.b23 + 192*m.b4*m.b11*m.b17*
                       m.b24 + 128*m.b4*m.b11*m.b18*m.b25 + 64*m.b4*m.b11*m.b19*m.b26 + 256*m.b4*m.b12*m.b13*m.b21 + 256
                       *m.b4*m.b12*m.b14*m.b22 + 256*m.b4*m.b12*m.b15*m.b23 + 192*m.b4*m.b12*m.b16*m.b24 + 128*m.b4*
                       m.b12*m.b17*m.b25 + 64*m.b4*m.b12*m.b18*m.b26 + 256*m.b4*m.b13*m.b14*m.b23 + 192*m.b4*m.b13*m.b15
                       *m.b24 + 128*m.b4*m.b13*m.b16*m.b25 + 64*m.b4*m.b13*m.b17*m.b26 + 128*m.b4*m.b14*m.b15*m.b25 + 64
                       *m.b4*m.b14*m.b16*m.b26 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 320*m.b5*m.b6*m.b9*
                       m.b10 + 320*m.b5*m.b6*m.b10*m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*m.b5*m.b6*m.b12*m.b13 + 320*
                       m.b5*m.b6*m.b13*m.b14 + 320*m.b5*m.b6*m.b14*m.b15 + 320*m.b5*m.b6*m.b15*m.b16 + 320*m.b5*m.b6*
                       m.b16*m.b17 + 320*m.b5*m.b6*m.b17*m.b18 + 320*m.b5*m.b6*m.b18*m.b19 + 320*m.b5*m.b6*m.b19*m.b20
                        + 320*m.b5*m.b6*m.b20*m.b21 + 320*m.b5*m.b6*m.b21*m.b22 + 320*m.b5*m.b6*m.b22*m.b23 + 256*m.b5*
                       m.b6*m.b23*m.b24 + 192*m.b5*m.b6*m.b24*m.b25 + 128*m.b5*m.b6*m.b25*m.b26 + 64*m.b5*m.b6*m.b26*
                       m.b27 + 320*m.b5*m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*
                       m.b5*m.b7*m.b11*m.b13 + 320*m.b5*m.b7*m.b12*m.b14 + 320*m.b5*m.b7*m.b13*m.b15 + 320*m.b5*m.b7*
                       m.b14*m.b16 + 320*m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b7*m.b16*m.b18 + 320*m.b5*m.b7*m.b17*m.b19
                        + 320*m.b5*m.b7*m.b18*m.b20 + 320*m.b5*m.b7*m.b19*m.b21 + 320*m.b5*m.b7*m.b20*m.b22 + 320*m.b5*
                       m.b7*m.b21*m.b23 + 256*m.b5*m.b7*m.b22*m.b24 + 192*m.b5*m.b7*m.b23*m.b25 + 128*m.b5*m.b7*m.b24*
                       m.b26 + 64*m.b5*m.b7*m.b25*m.b27 + 320*m.b5*m.b8*m.b9*m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*
                       m.b5*m.b8*m.b11*m.b14 + 320*m.b5*m.b8*m.b12*m.b15 + 320*m.b5*m.b8*m.b13*m.b16 + 320*m.b5*m.b8*
                       m.b14*m.b17 + 320*m.b5*m.b8*m.b15*m.b18 + 320*m.b5*m.b8*m.b16*m.b19 + 320*m.b5*m.b8*m.b17*m.b20
                        + 320*m.b5*m.b8*m.b18*m.b21 + 320*m.b5*m.b8*m.b19*m.b22 + 320*m.b5*m.b8*m.b20*m.b23 + 256*m.b5*
                       m.b8*m.b21*m.b24 + 192*m.b5*m.b8*m.b22*m.b25 + 128*m.b5*m.b8*m.b23*m.b26 + 64*m.b5*m.b8*m.b24*
                       m.b27 + 320*m.b5*m.b9*m.b10*m.b14 + 320*m.b5*m.b9*m.b11*m.b15 + 320*m.b5*m.b9*m.b12*m.b16 + 320*
                       m.b5*m.b9*m.b13*m.b17 + 320*m.b5*m.b9*m.b14*m.b18 + 320*m.b5*m.b9*m.b15*m.b19 + 320*m.b5*m.b9*
                       m.b16*m.b20 + 320*m.b5*m.b9*m.b17*m.b21 + 320*m.b5*m.b9*m.b18*m.b22 + 320*m.b5*m.b9*m.b19*m.b23
                        + 256*m.b5*m.b9*m.b20*m.b24 + 192*m.b5*m.b9*m.b21*m.b25 + 128*m.b5*m.b9*m.b22*m.b26 + 64*m.b5*
                       m.b9*m.b23*m.b27 + 320*m.b5*m.b10*m.b11*m.b16 + 320*m.b5*m.b10*m.b12*m.b17 + 320*m.b5*m.b10*m.b13
                       *m.b18 + 320*m.b5*m.b10*m.b14*m.b19 + 320*m.b5*m.b10*m.b15*m.b20 + 320*m.b5*m.b10*m.b16*m.b21 + 
                       320*m.b5*m.b10*m.b17*m.b22 + 320*m.b5*m.b10*m.b18*m.b23 + 256*m.b5*m.b10*m.b19*m.b24 + 192*m.b5*
                       m.b10*m.b20*m.b25 + 128*m.b5*m.b10*m.b21*m.b26 + 64*m.b5*m.b10*m.b22*m.b27 + 320*m.b5*m.b11*m.b12
                       *m.b18 + 320*m.b5*m.b11*m.b13*m.b19 + 320*m.b5*m.b11*m.b14*m.b20 + 320*m.b5*m.b11*m.b15*m.b21 + 
                       320*m.b5*m.b11*m.b16*m.b22 + 320*m.b5*m.b11*m.b17*m.b23 + 256*m.b5*m.b11*m.b18*m.b24 + 192*m.b5*
                       m.b11*m.b19*m.b25 + 128*m.b5*m.b11*m.b20*m.b26 + 64*m.b5*m.b11*m.b21*m.b27 + 320*m.b5*m.b12*m.b13
                       *m.b20 + 320*m.b5*m.b12*m.b14*m.b21 + 320*m.b5*m.b12*m.b15*m.b22 + 320*m.b5*m.b12*m.b16*m.b23 + 
                       256*m.b5*m.b12*m.b17*m.b24 + 192*m.b5*m.b12*m.b18*m.b25 + 128*m.b5*m.b12*m.b19*m.b26 + 64*m.b5*
                       m.b12*m.b20*m.b27 + 320*m.b5*m.b13*m.b14*m.b22 + 320*m.b5*m.b13*m.b15*m.b23 + 256*m.b5*m.b13*
                       m.b16*m.b24 + 192*m.b5*m.b13*m.b17*m.b25 + 128*m.b5*m.b13*m.b18*m.b26 + 64*m.b5*m.b13*m.b19*m.b27
                        + 256*m.b5*m.b14*m.b15*m.b24 + 192*m.b5*m.b14*m.b16*m.b25 + 128*m.b5*m.b14*m.b17*m.b26 + 64*m.b5
                       *m.b14*m.b18*m.b27 + 128*m.b5*m.b15*m.b16*m.b26 + 64*m.b5*m.b15*m.b17*m.b27 + 384*m.b6*m.b7*m.b8*
                       m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 384*
                       m.b6*m.b7*m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 384*m.b6*m.b7*m.b14*m.b15 + 384*m.b6*m.b7*
                       m.b15*m.b16 + 384*m.b6*m.b7*m.b16*m.b17 + 384*m.b6*m.b7*m.b17*m.b18 + 384*m.b6*m.b7*m.b18*m.b19
                        + 384*m.b6*m.b7*m.b19*m.b20 + 384*m.b6*m.b7*m.b20*m.b21 + 384*m.b6*m.b7*m.b21*m.b22 + 384*m.b6*
                       m.b7*m.b22*m.b23 + 320*m.b6*m.b7*m.b23*m.b24 + 256*m.b6*m.b7*m.b24*m.b25 + 192*m.b6*m.b7*m.b25*
                       m.b26 + 128*m.b6*m.b7*m.b26*m.b27 + 64*m.b6*m.b7*m.b27*m.b28 + 384*m.b6*m.b8*m.b9*m.b11 + 384*
                       m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*m.b13 + 384*m.b6*m.b8*m.b12*m.b14 + 384*m.b6*m.b8*
                       m.b13*m.b15 + 384*m.b6*m.b8*m.b14*m.b16 + 384*m.b6*m.b8*m.b15*m.b17 + 384*m.b6*m.b8*m.b16*m.b18
                        + 384*m.b6*m.b8*m.b17*m.b19 + 384*m.b6*m.b8*m.b18*m.b20 + 384*m.b6*m.b8*m.b19*m.b21 + 384*m.b6*
                       m.b8*m.b20*m.b22 + 384*m.b6*m.b8*m.b21*m.b23 + 320*m.b6*m.b8*m.b22*m.b24 + 256*m.b6*m.b8*m.b23*
                       m.b25 + 192*m.b6*m.b8*m.b24*m.b26 + 128*m.b6*m.b8*m.b25*m.b27 + 64*m.b6*m.b8*m.b26*m.b28 + 384*
                       m.b6*m.b9*m.b10*m.b13 + 384*m.b6*m.b9*m.b11*m.b14 + 384*m.b6*m.b9*m.b12*m.b15 + 384*m.b6*m.b9*
                       m.b13*m.b16 + 384*m.b6*m.b9*m.b14*m.b17 + 384*m.b6*m.b9*m.b15*m.b18 + 384*m.b6*m.b9*m.b16*m.b19
                        + 384*m.b6*m.b9*m.b17*m.b20 + 384*m.b6*m.b9*m.b18*m.b21 + 384*m.b6*m.b9*m.b19*m.b22 + 384*m.b6*
                       m.b9*m.b20*m.b23 + 320*m.b6*m.b9*m.b21*m.b24 + 256*m.b6*m.b9*m.b22*m.b25 + 192*m.b6*m.b9*m.b23*
                       m.b26 + 128*m.b6*m.b9*m.b24*m.b27 + 64*m.b6*m.b9*m.b25*m.b28 + 384*m.b6*m.b10*m.b11*m.b15 + 384*
                       m.b6*m.b10*m.b12*m.b16 + 384*m.b6*m.b10*m.b13*m.b17 + 384*m.b6*m.b10*m.b14*m.b18 + 384*m.b6*m.b10
                       *m.b15*m.b19 + 384*m.b6*m.b10*m.b16*m.b20 + 384*m.b6*m.b10*m.b17*m.b21 + 384*m.b6*m.b10*m.b18*
                       m.b22 + 384*m.b6*m.b10*m.b19*m.b23 + 320*m.b6*m.b10*m.b20*m.b24 + 256*m.b6*m.b10*m.b21*m.b25 + 
                       192*m.b6*m.b10*m.b22*m.b26 + 128*m.b6*m.b10*m.b23*m.b27 + 64*m.b6*m.b10*m.b24*m.b28 + 384*m.b6*
                       m.b11*m.b12*m.b17 + 384*m.b6*m.b11*m.b13*m.b18 + 384*m.b6*m.b11*m.b14*m.b19 + 384*m.b6*m.b11*
                       m.b15*m.b20 + 384*m.b6*m.b11*m.b16*m.b21 + 384*m.b6*m.b11*m.b17*m.b22 + 384*m.b6*m.b11*m.b18*
                       m.b23 + 320*m.b6*m.b11*m.b19*m.b24 + 256*m.b6*m.b11*m.b20*m.b25 + 192*m.b6*m.b11*m.b21*m.b26 + 
                       128*m.b6*m.b11*m.b22*m.b27 + 64*m.b6*m.b11*m.b23*m.b28 + 384*m.b6*m.b12*m.b13*m.b19 + 384*m.b6*
                       m.b12*m.b14*m.b20 + 384*m.b6*m.b12*m.b15*m.b21 + 384*m.b6*m.b12*m.b16*m.b22 + 384*m.b6*m.b12*
                       m.b17*m.b23 + 320*m.b6*m.b12*m.b18*m.b24 + 256*m.b6*m.b12*m.b19*m.b25 + 192*m.b6*m.b12*m.b20*
                       m.b26 + 128*m.b6*m.b12*m.b21*m.b27 + 64*m.b6*m.b12*m.b22*m.b28 + 384*m.b6*m.b13*m.b14*m.b21 + 384
                       *m.b6*m.b13*m.b15*m.b22 + 384*m.b6*m.b13*m.b16*m.b23 + 320*m.b6*m.b13*m.b17*m.b24 + 256*m.b6*
                       m.b13*m.b18*m.b25 + 192*m.b6*m.b13*m.b19*m.b26 + 128*m.b6*m.b13*m.b20*m.b27 + 64*m.b6*m.b13*m.b21
                       *m.b28 + 384*m.b6*m.b14*m.b15*m.b23 + 320*m.b6*m.b14*m.b16*m.b24 + 256*m.b6*m.b14*m.b17*m.b25 + 
                       192*m.b6*m.b14*m.b18*m.b26 + 128*m.b6*m.b14*m.b19*m.b27 + 64*m.b6*m.b14*m.b20*m.b28 + 256*m.b6*
                       m.b15*m.b16*m.b25 + 192*m.b6*m.b15*m.b17*m.b26 + 128*m.b6*m.b15*m.b18*m.b27 + 64*m.b6*m.b15*m.b19
                       *m.b28 + 128*m.b6*m.b16*m.b17*m.b27 + 64*m.b6*m.b16*m.b18*m.b28 + 448*m.b7*m.b8*m.b9*m.b10 + 448*
                       m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*m.b7*m.b8*m.b12*m.b13 + 448*m.b7*m.b8*
                       m.b13*m.b14 + 448*m.b7*m.b8*m.b14*m.b15 + 448*m.b7*m.b8*m.b15*m.b16 + 448*m.b7*m.b8*m.b16*m.b17
                        + 448*m.b7*m.b8*m.b17*m.b18 + 448*m.b7*m.b8*m.b18*m.b19 + 448*m.b7*m.b8*m.b19*m.b20 + 448*m.b7*
                       m.b8*m.b20*m.b21 + 448*m.b7*m.b8*m.b21*m.b22 + 448*m.b7*m.b8*m.b22*m.b23 + 384*m.b7*m.b8*m.b23*
                       m.b24 + 320*m.b7*m.b8*m.b24*m.b25 + 256*m.b7*m.b8*m.b25*m.b26 + 192*m.b7*m.b8*m.b26*m.b27 + 128*
                       m.b7*m.b8*m.b27*m.b28 + 64*m.b7*m.b8*m.b28*m.b29 + 448*m.b7*m.b9*m.b10*m.b12 + 448*m.b7*m.b9*
                       m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 448*m.b7*m.b9*m.b13*m.b15 + 448*m.b7*m.b9*m.b14*m.b16
                        + 448*m.b7*m.b9*m.b15*m.b17 + 448*m.b7*m.b9*m.b16*m.b18 + 448*m.b7*m.b9*m.b17*m.b19 + 448*m.b7*
                       m.b9*m.b18*m.b20 + 448*m.b7*m.b9*m.b19*m.b21 + 448*m.b7*m.b9*m.b20*m.b22 + 448*m.b7*m.b9*m.b21*
                       m.b23 + 384*m.b7*m.b9*m.b22*m.b24 + 320*m.b7*m.b9*m.b23*m.b25 + 256*m.b7*m.b9*m.b24*m.b26 + 192*
                       m.b7*m.b9*m.b25*m.b27 + 128*m.b7*m.b9*m.b26*m.b28 + 64*m.b7*m.b9*m.b27*m.b29 + 448*m.b7*m.b10*
                       m.b11*m.b14 + 448*m.b7*m.b10*m.b12*m.b15 + 448*m.b7*m.b10*m.b13*m.b16 + 448*m.b7*m.b10*m.b14*
                       m.b17 + 448*m.b7*m.b10*m.b15*m.b18 + 448*m.b7*m.b10*m.b16*m.b19 + 448*m.b7*m.b10*m.b17*m.b20 + 
                       448*m.b7*m.b10*m.b18*m.b21 + 448*m.b7*m.b10*m.b19*m.b22 + 448*m.b7*m.b10*m.b20*m.b23 + 384*m.b7*
                       m.b10*m.b21*m.b24 + 320*m.b7*m.b10*m.b22*m.b25 + 256*m.b7*m.b10*m.b23*m.b26 + 192*m.b7*m.b10*
                       m.b24*m.b27 + 128*m.b7*m.b10*m.b25*m.b28 + 64*m.b7*m.b10*m.b26*m.b29 + 448*m.b7*m.b11*m.b12*m.b16
                        + 448*m.b7*m.b11*m.b13*m.b17 + 448*m.b7*m.b11*m.b14*m.b18 + 448*m.b7*m.b11*m.b15*m.b19 + 448*
                       m.b7*m.b11*m.b16*m.b20 + 448*m.b7*m.b11*m.b17*m.b21 + 448*m.b7*m.b11*m.b18*m.b22 + 448*m.b7*m.b11
                       *m.b19*m.b23 + 384*m.b7*m.b11*m.b20*m.b24 + 320*m.b7*m.b11*m.b21*m.b25 + 256*m.b7*m.b11*m.b22*
                       m.b26 + 192*m.b7*m.b11*m.b23*m.b27 + 128*m.b7*m.b11*m.b24*m.b28 + 64*m.b7*m.b11*m.b25*m.b29 + 448
                       *m.b7*m.b12*m.b13*m.b18 + 448*m.b7*m.b12*m.b14*m.b19 + 448*m.b7*m.b12*m.b15*m.b20 + 448*m.b7*
                       m.b12*m.b16*m.b21 + 448*m.b7*m.b12*m.b17*m.b22 + 448*m.b7*m.b12*m.b18*m.b23 + 384*m.b7*m.b12*
                       m.b19*m.b24 + 320*m.b7*m.b12*m.b20*m.b25 + 256*m.b7*m.b12*m.b21*m.b26 + 192*m.b7*m.b12*m.b22*
                       m.b27 + 128*m.b7*m.b12*m.b23*m.b28 + 64*m.b7*m.b12*m.b24*m.b29 + 448*m.b7*m.b13*m.b14*m.b20 + 448
                       *m.b7*m.b13*m.b15*m.b21 + 448*m.b7*m.b13*m.b16*m.b22 + 448*m.b7*m.b13*m.b17*m.b23 + 384*m.b7*
                       m.b13*m.b18*m.b24 + 320*m.b7*m.b13*m.b19*m.b25 + 256*m.b7*m.b13*m.b20*m.b26 + 192*m.b7*m.b13*
                       m.b21*m.b27 + 128*m.b7*m.b13*m.b22*m.b28 + 64*m.b7*m.b13*m.b23*m.b29 + 448*m.b7*m.b14*m.b15*m.b22
                        + 448*m.b7*m.b14*m.b16*m.b23 + 384*m.b7*m.b14*m.b17*m.b24 + 320*m.b7*m.b14*m.b18*m.b25 + 256*
                       m.b7*m.b14*m.b19*m.b26 + 192*m.b7*m.b14*m.b20*m.b27 + 128*m.b7*m.b14*m.b21*m.b28 + 64*m.b7*m.b14*
                       m.b22*m.b29 + 384*m.b7*m.b15*m.b16*m.b24 + 320*m.b7*m.b15*m.b17*m.b25 + 256*m.b7*m.b15*m.b18*
                       m.b26 + 192*m.b7*m.b15*m.b19*m.b27 + 128*m.b7*m.b15*m.b20*m.b28 + 64*m.b7*m.b15*m.b21*m.b29 + 256
                       *m.b7*m.b16*m.b17*m.b26 + 192*m.b7*m.b16*m.b18*m.b27 + 128*m.b7*m.b16*m.b19*m.b28 + 64*m.b7*m.b16
                       *m.b20*m.b29 + 128*m.b7*m.b17*m.b18*m.b28 + 64*m.b7*m.b17*m.b19*m.b29 + 512*m.b8*m.b9*m.b10*m.b11
                        + 512*m.b8*m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*m.b13 + 512*m.b8*m.b9*m.b13*m.b14 + 512*m.b8*
                       m.b9*m.b14*m.b15 + 512*m.b8*m.b9*m.b15*m.b16 + 512*m.b8*m.b9*m.b16*m.b17 + 512*m.b8*m.b9*m.b17*
                       m.b18 + 512*m.b8*m.b9*m.b18*m.b19 + 512*m.b8*m.b9*m.b19*m.b20 + 512*m.b8*m.b9*m.b20*m.b21 + 512*
                       m.b8*m.b9*m.b21*m.b22 + 512*m.b8*m.b9*m.b22*m.b23 + 448*m.b8*m.b9*m.b23*m.b24 + 384*m.b8*m.b9*
                       m.b24*m.b25 + 320*m.b8*m.b9*m.b25*m.b26 + 256*m.b8*m.b9*m.b26*m.b27 + 192*m.b8*m.b9*m.b27*m.b28
                        + 128*m.b8*m.b9*m.b28*m.b29 + 64*m.b8*m.b9*m.b29*m.b30 + 512*m.b8*m.b10*m.b11*m.b13 + 512*m.b8*
                       m.b10*m.b12*m.b14 + 512*m.b8*m.b10*m.b13*m.b15 + 512*m.b8*m.b10*m.b14*m.b16 + 512*m.b8*m.b10*
                       m.b15*m.b17 + 512*m.b8*m.b10*m.b16*m.b18 + 512*m.b8*m.b10*m.b17*m.b19 + 512*m.b8*m.b10*m.b18*
                       m.b20 + 512*m.b8*m.b10*m.b19*m.b21 + 512*m.b8*m.b10*m.b20*m.b22 + 512*m.b8*m.b10*m.b21*m.b23 + 
                       448*m.b8*m.b10*m.b22*m.b24 + 384*m.b8*m.b10*m.b23*m.b25 + 320*m.b8*m.b10*m.b24*m.b26 + 256*m.b8*
                       m.b10*m.b25*m.b27 + 192*m.b8*m.b10*m.b26*m.b28 + 128*m.b8*m.b10*m.b27*m.b29 + 64*m.b8*m.b10*m.b28
                       *m.b30 + 512*m.b8*m.b11*m.b12*m.b15 + 512*m.b8*m.b11*m.b13*m.b16 + 512*m.b8*m.b11*m.b14*m.b17 + 
                       512*m.b8*m.b11*m.b15*m.b18 + 512*m.b8*m.b11*m.b16*m.b19 + 512*m.b8*m.b11*m.b17*m.b20 + 512*m.b8*
                       m.b11*m.b18*m.b21 + 512*m.b8*m.b11*m.b19*m.b22 + 512*m.b8*m.b11*m.b20*m.b23 + 448*m.b8*m.b11*
                       m.b21*m.b24 + 384*m.b8*m.b11*m.b22*m.b25 + 320*m.b8*m.b11*m.b23*m.b26 + 256*m.b8*m.b11*m.b24*
                       m.b27 + 192*m.b8*m.b11*m.b25*m.b28 + 128*m.b8*m.b11*m.b26*m.b29 + 64*m.b8*m.b11*m.b27*m.b30 + 512
                       *m.b8*m.b12*m.b13*m.b17 + 512*m.b8*m.b12*m.b14*m.b18 + 512*m.b8*m.b12*m.b15*m.b19 + 512*m.b8*
                       m.b12*m.b16*m.b20 + 512*m.b8*m.b12*m.b17*m.b21 + 512*m.b8*m.b12*m.b18*m.b22 + 512*m.b8*m.b12*
                       m.b19*m.b23 + 448*m.b8*m.b12*m.b20*m.b24 + 384*m.b8*m.b12*m.b21*m.b25 + 320*m.b8*m.b12*m.b22*
                       m.b26 + 256*m.b8*m.b12*m.b23*m.b27 + 192*m.b8*m.b12*m.b24*m.b28 + 128*m.b8*m.b12*m.b25*m.b29 + 64
                       *m.b8*m.b12*m.b26*m.b30 + 512*m.b8*m.b13*m.b14*m.b19 + 512*m.b8*m.b13*m.b15*m.b20 + 512*m.b8*
                       m.b13*m.b16*m.b21 + 512*m.b8*m.b13*m.b17*m.b22 + 512*m.b8*m.b13*m.b18*m.b23 + 448*m.b8*m.b13*
                       m.b19*m.b24 + 384*m.b8*m.b13*m.b20*m.b25 + 320*m.b8*m.b13*m.b21*m.b26 + 256*m.b8*m.b13*m.b22*
                       m.b27 + 192*m.b8*m.b13*m.b23*m.b28 + 128*m.b8*m.b13*m.b24*m.b29 + 64*m.b8*m.b13*m.b25*m.b30 + 512
                       *m.b8*m.b14*m.b15*m.b21 + 512*m.b8*m.b14*m.b16*m.b22 + 512*m.b8*m.b14*m.b17*m.b23 + 448*m.b8*
                       m.b14*m.b18*m.b24 + 384*m.b8*m.b14*m.b19*m.b25 + 320*m.b8*m.b14*m.b20*m.b26 + 256*m.b8*m.b14*
                       m.b21*m.b27 + 192*m.b8*m.b14*m.b22*m.b28 + 128*m.b8*m.b14*m.b23*m.b29 + 64*m.b8*m.b14*m.b24*m.b30
                        + 512*m.b8*m.b15*m.b16*m.b23 + 448*m.b8*m.b15*m.b17*m.b24 + 384*m.b8*m.b15*m.b18*m.b25 + 320*
                       m.b8*m.b15*m.b19*m.b26 + 256*m.b8*m.b15*m.b20*m.b27 + 192*m.b8*m.b15*m.b21*m.b28 + 128*m.b8*m.b15
                       *m.b22*m.b29 + 64*m.b8*m.b15*m.b23*m.b30 + 384*m.b8*m.b16*m.b17*m.b25 + 320*m.b8*m.b16*m.b18*
                       m.b26 + 256*m.b8*m.b16*m.b19*m.b27 + 192*m.b8*m.b16*m.b20*m.b28 + 128*m.b8*m.b16*m.b21*m.b29 + 64
                       *m.b8*m.b16*m.b22*m.b30 + 256*m.b8*m.b17*m.b18*m.b27 + 192*m.b8*m.b17*m.b19*m.b28 + 128*m.b8*
                       m.b17*m.b20*m.b29 + 64*m.b8*m.b17*m.b21*m.b30 + 128*m.b8*m.b18*m.b19*m.b29 + 64*m.b8*m.b18*m.b20*
                       m.b30 + 512*m.b9*m.b10*m.b11*m.b12 + 512*m.b9*m.b10*m.b12*m.b13 + 512*m.b9*m.b10*m.b13*m.b14 + 
                       512*m.b9*m.b10*m.b14*m.b15 + 512*m.b9*m.b10*m.b15*m.b16 + 576*m.b9*m.b10*m.b16*m.b17 + 576*m.b9*
                       m.b10*m.b17*m.b18 + 576*m.b9*m.b10*m.b18*m.b19 + 576*m.b9*m.b10*m.b19*m.b20 + 576*m.b9*m.b10*
                       m.b20*m.b21 + 576*m.b9*m.b10*m.b21*m.b22 + 512*m.b9*m.b10*m.b22*m.b23 + 448*m.b9*m.b10*m.b23*
                       m.b24 + 384*m.b9*m.b10*m.b24*m.b25 + 320*m.b9*m.b10*m.b25*m.b26 + 256*m.b9*m.b10*m.b26*m.b27 + 
                       192*m.b9*m.b10*m.b27*m.b28 + 128*m.b9*m.b10*m.b28*m.b29 + 64*m.b9*m.b10*m.b29*m.b30 + 512*m.b9*
                       m.b11*m.b12*m.b14 + 512*m.b9*m.b11*m.b13*m.b15 + 512*m.b9*m.b11*m.b14*m.b16 + 576*m.b9*m.b11*
                       m.b15*m.b17 + 576*m.b9*m.b11*m.b16*m.b18 + 576*m.b9*m.b11*m.b17*m.b19 + 576*m.b9*m.b11*m.b18*
                       m.b20 + 576*m.b9*m.b11*m.b19*m.b21 + 576*m.b9*m.b11*m.b20*m.b22 + 512*m.b9*m.b11*m.b21*m.b23 + 
                       448*m.b9*m.b11*m.b22*m.b24 + 384*m.b9*m.b11*m.b23*m.b25 + 320*m.b9*m.b11*m.b24*m.b26 + 256*m.b9*
                       m.b11*m.b25*m.b27 + 192*m.b9*m.b11*m.b26*m.b28 + 128*m.b9*m.b11*m.b27*m.b29 + 64*m.b9*m.b11*m.b28
                       *m.b30 + 512*m.b9*m.b12*m.b13*m.b16 + 576*m.b9*m.b12*m.b14*m.b17 + 576*m.b9*m.b12*m.b15*m.b18 + 
                       576*m.b9*m.b12*m.b16*m.b19 + 576*m.b9*m.b12*m.b17*m.b20 + 576*m.b9*m.b12*m.b18*m.b21 + 576*m.b9*
                       m.b12*m.b19*m.b22 + 512*m.b9*m.b12*m.b20*m.b23 + 448*m.b9*m.b12*m.b21*m.b24 + 384*m.b9*m.b12*
                       m.b22*m.b25 + 320*m.b9*m.b12*m.b23*m.b26 + 256*m.b9*m.b12*m.b24*m.b27 + 192*m.b9*m.b12*m.b25*
                       m.b28 + 128*m.b9*m.b12*m.b26*m.b29 + 64*m.b9*m.b12*m.b27*m.b30 + 576*m.b9*m.b13*m.b14*m.b18 + 576
                       *m.b9*m.b13*m.b15*m.b19 + 576*m.b9*m.b13*m.b16*m.b20 + 576*m.b9*m.b13*m.b17*m.b21 + 576*m.b9*
                       m.b13*m.b18*m.b22 + 512*m.b9*m.b13*m.b19*m.b23 + 448*m.b9*m.b13*m.b20*m.b24 + 384*m.b9*m.b13*
                       m.b21*m.b25 + 320*m.b9*m.b13*m.b22*m.b26 + 256*m.b9*m.b13*m.b23*m.b27 + 192*m.b9*m.b13*m.b24*
                       m.b28 + 128*m.b9*m.b13*m.b25*m.b29 + 64*m.b9*m.b13*m.b26*m.b30 + 576*m.b9*m.b14*m.b15*m.b20 + 576
                       *m.b9*m.b14*m.b16*m.b21 + 576*m.b9*m.b14*m.b17*m.b22 + 512*m.b9*m.b14*m.b18*m.b23 + 448*m.b9*
                       m.b14*m.b19*m.b24 + 384*m.b9*m.b14*m.b20*m.b25 + 320*m.b9*m.b14*m.b21*m.b26 + 256*m.b9*m.b14*
                       m.b22*m.b27 + 192*m.b9*m.b14*m.b23*m.b28 + 128*m.b9*m.b14*m.b24*m.b29 + 64*m.b9*m.b14*m.b25*m.b30
                        + 576*m.b9*m.b15*m.b16*m.b22 + 512*m.b9*m.b15*m.b17*m.b23 + 448*m.b9*m.b15*m.b18*m.b24 + 384*
                       m.b9*m.b15*m.b19*m.b25 + 320*m.b9*m.b15*m.b20*m.b26 + 256*m.b9*m.b15*m.b21*m.b27 + 192*m.b9*m.b15
                       *m.b22*m.b28 + 128*m.b9*m.b15*m.b23*m.b29 + 64*m.b9*m.b15*m.b24*m.b30 + 448*m.b9*m.b16*m.b17*
                       m.b24 + 384*m.b9*m.b16*m.b18*m.b25 + 320*m.b9*m.b16*m.b19*m.b26 + 256*m.b9*m.b16*m.b20*m.b27 + 
                       192*m.b9*m.b16*m.b21*m.b28 + 128*m.b9*m.b16*m.b22*m.b29 + 64*m.b9*m.b16*m.b23*m.b30 + 320*m.b9*
                       m.b17*m.b18*m.b26 + 256*m.b9*m.b17*m.b19*m.b27 + 192*m.b9*m.b17*m.b20*m.b28 + 128*m.b9*m.b17*
                       m.b21*m.b29 + 64*m.b9*m.b17*m.b22*m.b30 + 192*m.b9*m.b18*m.b19*m.b28 + 128*m.b9*m.b18*m.b20*m.b29
                        + 64*m.b9*m.b18*m.b21*m.b30 + 64*m.b9*m.b19*m.b20*m.b30 + 512*m.b10*m.b11*m.b12*m.b13 + 512*
                       m.b10*m.b11*m.b13*m.b14 + 512*m.b10*m.b11*m.b14*m.b15 + 512*m.b10*m.b11*m.b15*m.b16 + 512*m.b10*
                       m.b11*m.b16*m.b17 + 640*m.b10*m.b11*m.b17*m.b18 + 640*m.b10*m.b11*m.b18*m.b19 + 640*m.b10*m.b11*
                       m.b19*m.b20 + 640*m.b10*m.b11*m.b20*m.b21 + 576*m.b10*m.b11*m.b21*m.b22 + 512*m.b10*m.b11*m.b22*
                       m.b23 + 448*m.b10*m.b11*m.b23*m.b24 + 384*m.b10*m.b11*m.b24*m.b25 + 320*m.b10*m.b11*m.b25*m.b26
                        + 256*m.b10*m.b11*m.b26*m.b27 + 192*m.b10*m.b11*m.b27*m.b28 + 128*m.b10*m.b11*m.b28*m.b29 + 64*
                       m.b10*m.b11*m.b29*m.b30 + 512*m.b10*m.b12*m.b13*m.b15 + 512*m.b10*m.b12*m.b14*m.b16 + 512*m.b10*
                       m.b12*m.b15*m.b17 + 640*m.b10*m.b12*m.b16*m.b18 + 640*m.b10*m.b12*m.b17*m.b19 + 640*m.b10*m.b12*
                       m.b18*m.b20 + 640*m.b10*m.b12*m.b19*m.b21 + 576*m.b10*m.b12*m.b20*m.b22 + 512*m.b10*m.b12*m.b21*
                       m.b23 + 448*m.b10*m.b12*m.b22*m.b24 + 384*m.b10*m.b12*m.b23*m.b25 + 320*m.b10*m.b12*m.b24*m.b26
                        + 256*m.b10*m.b12*m.b25*m.b27 + 192*m.b10*m.b12*m.b26*m.b28 + 128*m.b10*m.b12*m.b27*m.b29 + 64*
                       m.b10*m.b12*m.b28*m.b30 + 512*m.b10*m.b13*m.b14*m.b17 + 640*m.b10*m.b13*m.b15*m.b18 + 640*m.b10*
                       m.b13*m.b16*m.b19 + 640*m.b10*m.b13*m.b17*m.b20 + 640*m.b10*m.b13*m.b18*m.b21 + 576*m.b10*m.b13*
                       m.b19*m.b22 + 512*m.b10*m.b13*m.b20*m.b23 + 448*m.b10*m.b13*m.b21*m.b24 + 384*m.b10*m.b13*m.b22*
                       m.b25 + 320*m.b10*m.b13*m.b23*m.b26 + 256*m.b10*m.b13*m.b24*m.b27 + 192*m.b10*m.b13*m.b25*m.b28
                        + 128*m.b10*m.b13*m.b26*m.b29 + 64*m.b10*m.b13*m.b27*m.b30 + 640*m.b10*m.b14*m.b15*m.b19 + 640*
                       m.b10*m.b14*m.b16*m.b20 + 640*m.b10*m.b14*m.b17*m.b21 + 576*m.b10*m.b14*m.b18*m.b22 + 512*m.b10*
                       m.b14*m.b19*m.b23 + 448*m.b10*m.b14*m.b20*m.b24 + 384*m.b10*m.b14*m.b21*m.b25 + 320*m.b10*m.b14*
                       m.b22*m.b26 + 256*m.b10*m.b14*m.b23*m.b27 + 192*m.b10*m.b14*m.b24*m.b28 + 128*m.b10*m.b14*m.b25*
                       m.b29 + 64*m.b10*m.b14*m.b26*m.b30 + 640*m.b10*m.b15*m.b16*m.b21 + 576*m.b10*m.b15*m.b17*m.b22 + 
                       512*m.b10*m.b15*m.b18*m.b23 + 448*m.b10*m.b15*m.b19*m.b24 + 384*m.b10*m.b15*m.b20*m.b25 + 320*
                       m.b10*m.b15*m.b21*m.b26 + 256*m.b10*m.b15*m.b22*m.b27 + 192*m.b10*m.b15*m.b23*m.b28 + 128*m.b10*
                       m.b15*m.b24*m.b29 + 64*m.b10*m.b15*m.b25*m.b30 + 512*m.b10*m.b16*m.b17*m.b23 + 448*m.b10*m.b16*
                       m.b18*m.b24 + 384*m.b10*m.b16*m.b19*m.b25 + 320*m.b10*m.b16*m.b20*m.b26 + 256*m.b10*m.b16*m.b21*
                       m.b27 + 192*m.b10*m.b16*m.b22*m.b28 + 128*m.b10*m.b16*m.b23*m.b29 + 64*m.b10*m.b16*m.b24*m.b30 + 
                       384*m.b10*m.b17*m.b18*m.b25 + 320*m.b10*m.b17*m.b19*m.b26 + 256*m.b10*m.b17*m.b20*m.b27 + 192*
                       m.b10*m.b17*m.b21*m.b28 + 128*m.b10*m.b17*m.b22*m.b29 + 64*m.b10*m.b17*m.b23*m.b30 + 256*m.b10*
                       m.b18*m.b19*m.b27 + 192*m.b10*m.b18*m.b20*m.b28 + 128*m.b10*m.b18*m.b21*m.b29 + 64*m.b10*m.b18*
                       m.b22*m.b30 + 128*m.b10*m.b19*m.b20*m.b29 + 64*m.b10*m.b19*m.b21*m.b30 + 512*m.b11*m.b12*m.b13*
                       m.b14 + 512*m.b11*m.b12*m.b14*m.b15 + 512*m.b11*m.b12*m.b15*m.b16 + 512*m.b11*m.b12*m.b16*m.b17
                        + 512*m.b11*m.b12*m.b17*m.b18 + 704*m.b11*m.b12*m.b18*m.b19 + 704*m.b11*m.b12*m.b19*m.b20 + 640*
                       m.b11*m.b12*m.b20*m.b21 + 576*m.b11*m.b12*m.b21*m.b22 + 512*m.b11*m.b12*m.b22*m.b23 + 448*m.b11*
                       m.b12*m.b23*m.b24 + 384*m.b11*m.b12*m.b24*m.b25 + 320*m.b11*m.b12*m.b25*m.b26 + 256*m.b11*m.b12*
                       m.b26*m.b27 + 192*m.b11*m.b12*m.b27*m.b28 + 128*m.b11*m.b12*m.b28*m.b29 + 64*m.b11*m.b12*m.b29*
                       m.b30 + 512*m.b11*m.b13*m.b14*m.b16 + 512*m.b11*m.b13*m.b15*m.b17 + 512*m.b11*m.b13*m.b16*m.b18
                        + 704*m.b11*m.b13*m.b17*m.b19 + 704*m.b11*m.b13*m.b18*m.b20 + 640*m.b11*m.b13*m.b19*m.b21 + 576*
                       m.b11*m.b13*m.b20*m.b22 + 512*m.b11*m.b13*m.b21*m.b23 + 448*m.b11*m.b13*m.b22*m.b24 + 384*m.b11*
                       m.b13*m.b23*m.b25 + 320*m.b11*m.b13*m.b24*m.b26 + 256*m.b11*m.b13*m.b25*m.b27 + 192*m.b11*m.b13*
                       m.b26*m.b28 + 128*m.b11*m.b13*m.b27*m.b29 + 64*m.b11*m.b13*m.b28*m.b30 + 512*m.b11*m.b14*m.b15*
                       m.b18 + 704*m.b11*m.b14*m.b16*m.b19 + 704*m.b11*m.b14*m.b17*m.b20 + 640*m.b11*m.b14*m.b18*m.b21
                        + 576*m.b11*m.b14*m.b19*m.b22 + 512*m.b11*m.b14*m.b20*m.b23 + 448*m.b11*m.b14*m.b21*m.b24 + 384*
                       m.b11*m.b14*m.b22*m.b25 + 320*m.b11*m.b14*m.b23*m.b26 + 256*m.b11*m.b14*m.b24*m.b27 + 192*m.b11*
                       m.b14*m.b25*m.b28 + 128*m.b11*m.b14*m.b26*m.b29 + 64*m.b11*m.b14*m.b27*m.b30 + 704*m.b11*m.b15*
                       m.b16*m.b20 + 640*m.b11*m.b15*m.b17*m.b21 + 576*m.b11*m.b15*m.b18*m.b22 + 512*m.b11*m.b15*m.b19*
                       m.b23 + 448*m.b11*m.b15*m.b20*m.b24 + 384*m.b11*m.b15*m.b21*m.b25 + 320*m.b11*m.b15*m.b22*m.b26
                        + 256*m.b11*m.b15*m.b23*m.b27 + 192*m.b11*m.b15*m.b24*m.b28 + 128*m.b11*m.b15*m.b25*m.b29 + 64*
                       m.b11*m.b15*m.b26*m.b30 + 576*m.b11*m.b16*m.b17*m.b22 + 512*m.b11*m.b16*m.b18*m.b23 + 448*m.b11*
                       m.b16*m.b19*m.b24 + 384*m.b11*m.b16*m.b20*m.b25 + 320*m.b11*m.b16*m.b21*m.b26 + 256*m.b11*m.b16*
                       m.b22*m.b27 + 192*m.b11*m.b16*m.b23*m.b28 + 128*m.b11*m.b16*m.b24*m.b29 + 64*m.b11*m.b16*m.b25*
                       m.b30 + 448*m.b11*m.b17*m.b18*m.b24 + 384*m.b11*m.b17*m.b19*m.b25 + 320*m.b11*m.b17*m.b20*m.b26
                        + 256*m.b11*m.b17*m.b21*m.b27 + 192*m.b11*m.b17*m.b22*m.b28 + 128*m.b11*m.b17*m.b23*m.b29 + 64*
                       m.b11*m.b17*m.b24*m.b30 + 320*m.b11*m.b18*m.b19*m.b26 + 256*m.b11*m.b18*m.b20*m.b27 + 192*m.b11*
                       m.b18*m.b21*m.b28 + 128*m.b11*m.b18*m.b22*m.b29 + 64*m.b11*m.b18*m.b23*m.b30 + 192*m.b11*m.b19*
                       m.b20*m.b28 + 128*m.b11*m.b19*m.b21*m.b29 + 64*m.b11*m.b19*m.b22*m.b30 + 64*m.b11*m.b20*m.b21*
                       m.b30 + 512*m.b12*m.b13*m.b14*m.b15 + 512*m.b12*m.b13*m.b15*m.b16 + 512*m.b12*m.b13*m.b16*m.b17
                        + 512*m.b12*m.b13*m.b17*m.b18 + 512*m.b12*m.b13*m.b18*m.b19 + 704*m.b12*m.b13*m.b19*m.b20 + 640*
                       m.b12*m.b13*m.b20*m.b21 + 576*m.b12*m.b13*m.b21*m.b22 + 512*m.b12*m.b13*m.b22*m.b23 + 448*m.b12*
                       m.b13*m.b23*m.b24 + 384*m.b12*m.b13*m.b24*m.b25 + 320*m.b12*m.b13*m.b25*m.b26 + 256*m.b12*m.b13*
                       m.b26*m.b27 + 192*m.b12*m.b13*m.b27*m.b28 + 128*m.b12*m.b13*m.b28*m.b29 + 64*m.b12*m.b13*m.b29*
                       m.b30 + 512*m.b12*m.b14*m.b15*m.b17 + 512*m.b12*m.b14*m.b16*m.b18 + 512*m.b12*m.b14*m.b17*m.b19
                        + 704*m.b12*m.b14*m.b18*m.b20 + 640*m.b12*m.b14*m.b19*m.b21 + 576*m.b12*m.b14*m.b20*m.b22 + 512*
                       m.b12*m.b14*m.b21*m.b23 + 448*m.b12*m.b14*m.b22*m.b24 + 384*m.b12*m.b14*m.b23*m.b25 + 320*m.b12*
                       m.b14*m.b24*m.b26 + 256*m.b12*m.b14*m.b25*m.b27 + 192*m.b12*m.b14*m.b26*m.b28 + 128*m.b12*m.b14*
                       m.b27*m.b29 + 64*m.b12*m.b14*m.b28*m.b30 + 512*m.b12*m.b15*m.b16*m.b19 + 704*m.b12*m.b15*m.b17*
                       m.b20 + 640*m.b12*m.b15*m.b18*m.b21 + 576*m.b12*m.b15*m.b19*m.b22 + 512*m.b12*m.b15*m.b20*m.b23
                        + 448*m.b12*m.b15*m.b21*m.b24 + 384*m.b12*m.b15*m.b22*m.b25 + 320*m.b12*m.b15*m.b23*m.b26 + 256*
                       m.b12*m.b15*m.b24*m.b27 + 192*m.b12*m.b15*m.b25*m.b28 + 128*m.b12*m.b15*m.b26*m.b29 + 64*m.b12*
                       m.b15*m.b27*m.b30 + 640*m.b12*m.b16*m.b17*m.b21 + 576*m.b12*m.b16*m.b18*m.b22 + 512*m.b12*m.b16*
                       m.b19*m.b23 + 448*m.b12*m.b16*m.b20*m.b24 + 384*m.b12*m.b16*m.b21*m.b25 + 320*m.b12*m.b16*m.b22*
                       m.b26 + 256*m.b12*m.b16*m.b23*m.b27 + 192*m.b12*m.b16*m.b24*m.b28 + 128*m.b12*m.b16*m.b25*m.b29
                        + 64*m.b12*m.b16*m.b26*m.b30 + 512*m.b12*m.b17*m.b18*m.b23 + 448*m.b12*m.b17*m.b19*m.b24 + 384*
                       m.b12*m.b17*m.b20*m.b25 + 320*m.b12*m.b17*m.b21*m.b26 + 256*m.b12*m.b17*m.b22*m.b27 + 192*m.b12*
                       m.b17*m.b23*m.b28 + 128*m.b12*m.b17*m.b24*m.b29 + 64*m.b12*m.b17*m.b25*m.b30 + 384*m.b12*m.b18*
                       m.b19*m.b25 + 320*m.b12*m.b18*m.b20*m.b26 + 256*m.b12*m.b18*m.b21*m.b27 + 192*m.b12*m.b18*m.b22*
                       m.b28 + 128*m.b12*m.b18*m.b23*m.b29 + 64*m.b12*m.b18*m.b24*m.b30 + 256*m.b12*m.b19*m.b20*m.b27 + 
                       192*m.b12*m.b19*m.b21*m.b28 + 128*m.b12*m.b19*m.b22*m.b29 + 64*m.b12*m.b19*m.b23*m.b30 + 128*
                       m.b12*m.b20*m.b21*m.b29 + 64*m.b12*m.b20*m.b22*m.b30 + 512*m.b13*m.b14*m.b15*m.b16 + 512*m.b13*
                       m.b14*m.b16*m.b17 + 512*m.b13*m.b14*m.b17*m.b18 + 512*m.b13*m.b14*m.b18*m.b19 + 512*m.b13*m.b14*
                       m.b19*m.b20 + 640*m.b13*m.b14*m.b20*m.b21 + 576*m.b13*m.b14*m.b21*m.b22 + 512*m.b13*m.b14*m.b22*
                       m.b23 + 448*m.b13*m.b14*m.b23*m.b24 + 384*m.b13*m.b14*m.b24*m.b25 + 320*m.b13*m.b14*m.b25*m.b26
                        + 256*m.b13*m.b14*m.b26*m.b27 + 192*m.b13*m.b14*m.b27*m.b28 + 128*m.b13*m.b14*m.b28*m.b29 + 64*
                       m.b13*m.b14*m.b29*m.b30 + 512*m.b13*m.b15*m.b16*m.b18 + 512*m.b13*m.b15*m.b17*m.b19 + 512*m.b13*
                       m.b15*m.b18*m.b20 + 640*m.b13*m.b15*m.b19*m.b21 + 576*m.b13*m.b15*m.b20*m.b22 + 512*m.b13*m.b15*
                       m.b21*m.b23 + 448*m.b13*m.b15*m.b22*m.b24 + 384*m.b13*m.b15*m.b23*m.b25 + 320*m.b13*m.b15*m.b24*
                       m.b26 + 256*m.b13*m.b15*m.b25*m.b27 + 192*m.b13*m.b15*m.b26*m.b28 + 128*m.b13*m.b15*m.b27*m.b29
                        + 64*m.b13*m.b15*m.b28*m.b30 + 512*m.b13*m.b16*m.b17*m.b20 + 640*m.b13*m.b16*m.b18*m.b21 + 576*
                       m.b13*m.b16*m.b19*m.b22 + 512*m.b13*m.b16*m.b20*m.b23 + 448*m.b13*m.b16*m.b21*m.b24 + 384*m.b13*
                       m.b16*m.b22*m.b25 + 320*m.b13*m.b16*m.b23*m.b26 + 256*m.b13*m.b16*m.b24*m.b27 + 192*m.b13*m.b16*
                       m.b25*m.b28 + 128*m.b13*m.b16*m.b26*m.b29 + 64*m.b13*m.b16*m.b27*m.b30 + 576*m.b13*m.b17*m.b18*
                       m.b22 + 512*m.b13*m.b17*m.b19*m.b23 + 448*m.b13*m.b17*m.b20*m.b24 + 384*m.b13*m.b17*m.b21*m.b25
                        + 320*m.b13*m.b17*m.b22*m.b26 + 256*m.b13*m.b17*m.b23*m.b27 + 192*m.b13*m.b17*m.b24*m.b28 + 128*
                       m.b13*m.b17*m.b25*m.b29 + 64*m.b13*m.b17*m.b26*m.b30 + 448*m.b13*m.b18*m.b19*m.b24 + 384*m.b13*
                       m.b18*m.b20*m.b25 + 320*m.b13*m.b18*m.b21*m.b26 + 256*m.b13*m.b18*m.b22*m.b27 + 192*m.b13*m.b18*
                       m.b23*m.b28 + 128*m.b13*m.b18*m.b24*m.b29 + 64*m.b13*m.b18*m.b25*m.b30 + 320*m.b13*m.b19*m.b20*
                       m.b26 + 256*m.b13*m.b19*m.b21*m.b27 + 192*m.b13*m.b19*m.b22*m.b28 + 128*m.b13*m.b19*m.b23*m.b29
                        + 64*m.b13*m.b19*m.b24*m.b30 + 192*m.b13*m.b20*m.b21*m.b28 + 128*m.b13*m.b20*m.b22*m.b29 + 64*
                       m.b13*m.b20*m.b23*m.b30 + 64*m.b13*m.b21*m.b22*m.b30 + 512*m.b14*m.b15*m.b16*m.b17 + 512*m.b14*
                       m.b15*m.b17*m.b18 + 512*m.b14*m.b15*m.b18*m.b19 + 512*m.b14*m.b15*m.b19*m.b20 + 512*m.b14*m.b15*
                       m.b20*m.b21 + 576*m.b14*m.b15*m.b21*m.b22 + 512*m.b14*m.b15*m.b22*m.b23 + 448*m.b14*m.b15*m.b23*
                       m.b24 + 384*m.b14*m.b15*m.b24*m.b25 + 320*m.b14*m.b15*m.b25*m.b26 + 256*m.b14*m.b15*m.b26*m.b27
                        + 192*m.b14*m.b15*m.b27*m.b28 + 128*m.b14*m.b15*m.b28*m.b29 + 64*m.b14*m.b15*m.b29*m.b30 + 512*
                       m.b14*m.b16*m.b17*m.b19 + 512*m.b14*m.b16*m.b18*m.b20 + 512*m.b14*m.b16*m.b19*m.b21 + 576*m.b14*
                       m.b16*m.b20*m.b22 + 512*m.b14*m.b16*m.b21*m.b23 + 448*m.b14*m.b16*m.b22*m.b24 + 384*m.b14*m.b16*
                       m.b23*m.b25 + 320*m.b14*m.b16*m.b24*m.b26 + 256*m.b14*m.b16*m.b25*m.b27 + 192*m.b14*m.b16*m.b26*
                       m.b28 + 128*m.b14*m.b16*m.b27*m.b29 + 64*m.b14*m.b16*m.b28*m.b30 + 512*m.b14*m.b17*m.b18*m.b21 + 
                       576*m.b14*m.b17*m.b19*m.b22 + 512*m.b14*m.b17*m.b20*m.b23 + 448*m.b14*m.b17*m.b21*m.b24 + 384*
                       m.b14*m.b17*m.b22*m.b25 + 320*m.b14*m.b17*m.b23*m.b26 + 256*m.b14*m.b17*m.b24*m.b27 + 192*m.b14*
                       m.b17*m.b25*m.b28 + 128*m.b14*m.b17*m.b26*m.b29 + 64*m.b14*m.b17*m.b27*m.b30 + 512*m.b14*m.b18*
                       m.b19*m.b23 + 448*m.b14*m.b18*m.b20*m.b24 + 384*m.b14*m.b18*m.b21*m.b25 + 320*m.b14*m.b18*m.b22*
                       m.b26 + 256*m.b14*m.b18*m.b23*m.b27 + 192*m.b14*m.b18*m.b24*m.b28 + 128*m.b14*m.b18*m.b25*m.b29
                        + 64*m.b14*m.b18*m.b26*m.b30 + 384*m.b14*m.b19*m.b20*m.b25 + 320*m.b14*m.b19*m.b21*m.b26 + 256*
                       m.b14*m.b19*m.b22*m.b27 + 192*m.b14*m.b19*m.b23*m.b28 + 128*m.b14*m.b19*m.b24*m.b29 + 64*m.b14*
                       m.b19*m.b25*m.b30 + 256*m.b14*m.b20*m.b21*m.b27 + 192*m.b14*m.b20*m.b22*m.b28 + 128*m.b14*m.b20*
                       m.b23*m.b29 + 64*m.b14*m.b20*m.b24*m.b30 + 128*m.b14*m.b21*m.b22*m.b29 + 64*m.b14*m.b21*m.b23*
                       m.b30 + 512*m.b15*m.b16*m.b17*m.b18 + 512*m.b15*m.b16*m.b18*m.b19 + 512*m.b15*m.b16*m.b19*m.b20
                        + 512*m.b15*m.b16*m.b20*m.b21 + 512*m.b15*m.b16*m.b21*m.b22 + 512*m.b15*m.b16*m.b22*m.b23 + 448*
                       m.b15*m.b16*m.b23*m.b24 + 384*m.b15*m.b16*m.b24*m.b25 + 320*m.b15*m.b16*m.b25*m.b26 + 256*m.b15*
                       m.b16*m.b26*m.b27 + 192*m.b15*m.b16*m.b27*m.b28 + 128*m.b15*m.b16*m.b28*m.b29 + 64*m.b15*m.b16*
                       m.b29*m.b30 + 512*m.b15*m.b17*m.b18*m.b20 + 512*m.b15*m.b17*m.b19*m.b21 + 512*m.b15*m.b17*m.b20*
                       m.b22 + 512*m.b15*m.b17*m.b21*m.b23 + 448*m.b15*m.b17*m.b22*m.b24 + 384*m.b15*m.b17*m.b23*m.b25
                        + 320*m.b15*m.b17*m.b24*m.b26 + 256*m.b15*m.b17*m.b25*m.b27 + 192*m.b15*m.b17*m.b26*m.b28 + 128*
                       m.b15*m.b17*m.b27*m.b29 + 64*m.b15*m.b17*m.b28*m.b30 + 512*m.b15*m.b18*m.b19*m.b22 + 512*m.b15*
                       m.b18*m.b20*m.b23 + 448*m.b15*m.b18*m.b21*m.b24 + 384*m.b15*m.b18*m.b22*m.b25 + 320*m.b15*m.b18*
                       m.b23*m.b26 + 256*m.b15*m.b18*m.b24*m.b27 + 192*m.b15*m.b18*m.b25*m.b28 + 128*m.b15*m.b18*m.b26*
                       m.b29 + 64*m.b15*m.b18*m.b27*m.b30 + 448*m.b15*m.b19*m.b20*m.b24 + 384*m.b15*m.b19*m.b21*m.b25 + 
                       320*m.b15*m.b19*m.b22*m.b26 + 256*m.b15*m.b19*m.b23*m.b27 + 192*m.b15*m.b19*m.b24*m.b28 + 128*
                       m.b15*m.b19*m.b25*m.b29 + 64*m.b15*m.b19*m.b26*m.b30 + 320*m.b15*m.b20*m.b21*m.b26 + 256*m.b15*
                       m.b20*m.b22*m.b27 + 192*m.b15*m.b20*m.b23*m.b28 + 128*m.b15*m.b20*m.b24*m.b29 + 64*m.b15*m.b20*
                       m.b25*m.b30 + 192*m.b15*m.b21*m.b22*m.b28 + 128*m.b15*m.b21*m.b23*m.b29 + 64*m.b15*m.b21*m.b24*
                       m.b30 + 64*m.b15*m.b22*m.b23*m.b30 + 512*m.b16*m.b17*m.b18*m.b19 + 512*m.b16*m.b17*m.b19*m.b20 + 
                       512*m.b16*m.b17*m.b20*m.b21 + 512*m.b16*m.b17*m.b21*m.b22 + 512*m.b16*m.b17*m.b22*m.b23 + 448*
                       m.b16*m.b17*m.b23*m.b24 + 384*m.b16*m.b17*m.b24*m.b25 + 320*m.b16*m.b17*m.b25*m.b26 + 256*m.b16*
                       m.b17*m.b26*m.b27 + 192*m.b16*m.b17*m.b27*m.b28 + 128*m.b16*m.b17*m.b28*m.b29 + 64*m.b16*m.b17*
                       m.b29*m.b30 + 512*m.b16*m.b18*m.b19*m.b21 + 512*m.b16*m.b18*m.b20*m.b22 + 512*m.b16*m.b18*m.b21*
                       m.b23 + 448*m.b16*m.b18*m.b22*m.b24 + 384*m.b16*m.b18*m.b23*m.b25 + 320*m.b16*m.b18*m.b24*m.b26
                        + 256*m.b16*m.b18*m.b25*m.b27 + 192*m.b16*m.b18*m.b26*m.b28 + 128*m.b16*m.b18*m.b27*m.b29 + 64*
                       m.b16*m.b18*m.b28*m.b30 + 512*m.b16*m.b19*m.b20*m.b23 + 448*m.b16*m.b19*m.b21*m.b24 + 384*m.b16*
                       m.b19*m.b22*m.b25 + 320*m.b16*m.b19*m.b23*m.b26 + 256*m.b16*m.b19*m.b24*m.b27 + 192*m.b16*m.b19*
                       m.b25*m.b28 + 128*m.b16*m.b19*m.b26*m.b29 + 64*m.b16*m.b19*m.b27*m.b30 + 384*m.b16*m.b20*m.b21*
                       m.b25 + 320*m.b16*m.b20*m.b22*m.b26 + 256*m.b16*m.b20*m.b23*m.b27 + 192*m.b16*m.b20*m.b24*m.b28
                        + 128*m.b16*m.b20*m.b25*m.b29 + 64*m.b16*m.b20*m.b26*m.b30 + 256*m.b16*m.b21*m.b22*m.b27 + 192*
                       m.b16*m.b21*m.b23*m.b28 + 128*m.b16*m.b21*m.b24*m.b29 + 64*m.b16*m.b21*m.b25*m.b30 + 128*m.b16*
                       m.b22*m.b23*m.b29 + 64*m.b16*m.b22*m.b24*m.b30 + 512*m.b17*m.b18*m.b19*m.b20 + 512*m.b17*m.b18*
                       m.b20*m.b21 + 512*m.b17*m.b18*m.b21*m.b22 + 512*m.b17*m.b18*m.b22*m.b23 + 448*m.b17*m.b18*m.b23*
                       m.b24 + 384*m.b17*m.b18*m.b24*m.b25 + 320*m.b17*m.b18*m.b25*m.b26 + 256*m.b17*m.b18*m.b26*m.b27
                        + 192*m.b17*m.b18*m.b27*m.b28 + 128*m.b17*m.b18*m.b28*m.b29 + 64*m.b17*m.b18*m.b29*m.b30 + 512*
                       m.b17*m.b19*m.b20*m.b22 + 512*m.b17*m.b19*m.b21*m.b23 + 448*m.b17*m.b19*m.b22*m.b24 + 384*m.b17*
                       m.b19*m.b23*m.b25 + 320*m.b17*m.b19*m.b24*m.b26 + 256*m.b17*m.b19*m.b25*m.b27 + 192*m.b17*m.b19*
                       m.b26*m.b28 + 128*m.b17*m.b19*m.b27*m.b29 + 64*m.b17*m.b19*m.b28*m.b30 + 448*m.b17*m.b20*m.b21*
                       m.b24 + 384*m.b17*m.b20*m.b22*m.b25 + 320*m.b17*m.b20*m.b23*m.b26 + 256*m.b17*m.b20*m.b24*m.b27
                        + 192*m.b17*m.b20*m.b25*m.b28 + 128*m.b17*m.b20*m.b26*m.b29 + 64*m.b17*m.b20*m.b27*m.b30 + 320*
                       m.b17*m.b21*m.b22*m.b26 + 256*m.b17*m.b21*m.b23*m.b27 + 192*m.b17*m.b21*m.b24*m.b28 + 128*m.b17*
                       m.b21*m.b25*m.b29 + 64*m.b17*m.b21*m.b26*m.b30 + 192*m.b17*m.b22*m.b23*m.b28 + 128*m.b17*m.b22*
                       m.b24*m.b29 + 64*m.b17*m.b22*m.b25*m.b30 + 64*m.b17*m.b23*m.b24*m.b30 + 512*m.b18*m.b19*m.b20*
                       m.b21 + 512*m.b18*m.b19*m.b21*m.b22 + 512*m.b18*m.b19*m.b22*m.b23 + 448*m.b18*m.b19*m.b23*m.b24
                        + 384*m.b18*m.b19*m.b24*m.b25 + 320*m.b18*m.b19*m.b25*m.b26 + 256*m.b18*m.b19*m.b26*m.b27 + 192*
                       m.b18*m.b19*m.b27*m.b28 + 128*m.b18*m.b19*m.b28*m.b29 + 64*m.b18*m.b19*m.b29*m.b30 + 512*m.b18*
                       m.b20*m.b21*m.b23 + 448*m.b18*m.b20*m.b22*m.b24 + 384*m.b18*m.b20*m.b23*m.b25 + 320*m.b18*m.b20*
                       m.b24*m.b26 + 256*m.b18*m.b20*m.b25*m.b27 + 192*m.b18*m.b20*m.b26*m.b28 + 128*m.b18*m.b20*m.b27*
                       m.b29 + 64*m.b18*m.b20*m.b28*m.b30 + 384*m.b18*m.b21*m.b22*m.b25 + 320*m.b18*m.b21*m.b23*m.b26 + 
                       256*m.b18*m.b21*m.b24*m.b27 + 192*m.b18*m.b21*m.b25*m.b28 + 128*m.b18*m.b21*m.b26*m.b29 + 64*
                       m.b18*m.b21*m.b27*m.b30 + 256*m.b18*m.b22*m.b23*m.b27 + 192*m.b18*m.b22*m.b24*m.b28 + 128*m.b18*
                       m.b22*m.b25*m.b29 + 64*m.b18*m.b22*m.b26*m.b30 + 128*m.b18*m.b23*m.b24*m.b29 + 64*m.b18*m.b23*
                       m.b25*m.b30 + 512*m.b19*m.b20*m.b21*m.b22 + 512*m.b19*m.b20*m.b22*m.b23 + 448*m.b19*m.b20*m.b23*
                       m.b24 + 384*m.b19*m.b20*m.b24*m.b25 + 320*m.b19*m.b20*m.b25*m.b26 + 256*m.b19*m.b20*m.b26*m.b27
                        + 192*m.b19*m.b20*m.b27*m.b28 + 128*m.b19*m.b20*m.b28*m.b29 + 64*m.b19*m.b20*m.b29*m.b30 + 448*
                       m.b19*m.b21*m.b22*m.b24 + 384*m.b19*m.b21*m.b23*m.b25 + 320*m.b19*m.b21*m.b24*m.b26 + 256*m.b19*
                       m.b21*m.b25*m.b27 + 192*m.b19*m.b21*m.b26*m.b28 + 128*m.b19*m.b21*m.b27*m.b29 + 64*m.b19*m.b21*
                       m.b28*m.b30 + 320*m.b19*m.b22*m.b23*m.b26 + 256*m.b19*m.b22*m.b24*m.b27 + 192*m.b19*m.b22*m.b25*
                       m.b28 + 128*m.b19*m.b22*m.b26*m.b29 + 64*m.b19*m.b22*m.b27*m.b30 + 192*m.b19*m.b23*m.b24*m.b28 + 
                       128*m.b19*m.b23*m.b25*m.b29 + 64*m.b19*m.b23*m.b26*m.b30 + 64*m.b19*m.b24*m.b25*m.b30 + 512*m.b20
                       *m.b21*m.b22*m.b23 + 448*m.b20*m.b21*m.b23*m.b24 + 384*m.b20*m.b21*m.b24*m.b25 + 320*m.b20*m.b21*
                       m.b25*m.b26 + 256*m.b20*m.b21*m.b26*m.b27 + 192*m.b20*m.b21*m.b27*m.b28 + 128*m.b20*m.b21*m.b28*
                       m.b29 + 64*m.b20*m.b21*m.b29*m.b30 + 384*m.b20*m.b22*m.b23*m.b25 + 320*m.b20*m.b22*m.b24*m.b26 + 
                       256*m.b20*m.b22*m.b25*m.b27 + 192*m.b20*m.b22*m.b26*m.b28 + 128*m.b20*m.b22*m.b27*m.b29 + 64*
                       m.b20*m.b22*m.b28*m.b30 + 256*m.b20*m.b23*m.b24*m.b27 + 192*m.b20*m.b23*m.b25*m.b28 + 128*m.b20*
                       m.b23*m.b26*m.b29 + 64*m.b20*m.b23*m.b27*m.b30 + 128*m.b20*m.b24*m.b25*m.b29 + 64*m.b20*m.b24*
                       m.b26*m.b30 + 448*m.b21*m.b22*m.b23*m.b24 + 384*m.b21*m.b22*m.b24*m.b25 + 320*m.b21*m.b22*m.b25*
                       m.b26 + 256*m.b21*m.b22*m.b26*m.b27 + 192*m.b21*m.b22*m.b27*m.b28 + 128*m.b21*m.b22*m.b28*m.b29
                        + 64*m.b21*m.b22*m.b29*m.b30 + 320*m.b21*m.b23*m.b24*m.b26 + 256*m.b21*m.b23*m.b25*m.b27 + 192*
                       m.b21*m.b23*m.b26*m.b28 + 128*m.b21*m.b23*m.b27*m.b29 + 64*m.b21*m.b23*m.b28*m.b30 + 192*m.b21*
                       m.b24*m.b25*m.b28 + 128*m.b21*m.b24*m.b26*m.b29 + 64*m.b21*m.b24*m.b27*m.b30 + 64*m.b21*m.b25*
                       m.b26*m.b30 + 384*m.b22*m.b23*m.b24*m.b25 + 320*m.b22*m.b23*m.b25*m.b26 + 256*m.b22*m.b23*m.b26*
                       m.b27 + 192*m.b22*m.b23*m.b27*m.b28 + 128*m.b22*m.b23*m.b28*m.b29 + 64*m.b22*m.b23*m.b29*m.b30 + 
                       256*m.b22*m.b24*m.b25*m.b27 + 192*m.b22*m.b24*m.b26*m.b28 + 128*m.b22*m.b24*m.b27*m.b29 + 64*
                       m.b22*m.b24*m.b28*m.b30 + 128*m.b22*m.b25*m.b26*m.b29 + 64*m.b22*m.b25*m.b27*m.b30 + 320*m.b23*
                       m.b24*m.b25*m.b26 + 256*m.b23*m.b24*m.b26*m.b27 + 192*m.b23*m.b24*m.b27*m.b28 + 128*m.b23*m.b24*
                       m.b28*m.b29 + 64*m.b23*m.b24*m.b29*m.b30 + 192*m.b23*m.b25*m.b26*m.b28 + 128*m.b23*m.b25*m.b27*
                       m.b29 + 64*m.b23*m.b25*m.b28*m.b30 + 64*m.b23*m.b26*m.b27*m.b30 + 256*m.b24*m.b25*m.b26*m.b27 + 
                       192*m.b24*m.b25*m.b27*m.b28 + 128*m.b24*m.b25*m.b28*m.b29 + 64*m.b24*m.b25*m.b29*m.b30 + 128*
                       m.b24*m.b26*m.b27*m.b29 + 64*m.b24*m.b26*m.b28*m.b30 + 192*m.b25*m.b26*m.b27*m.b28 + 128*m.b25*
                       m.b26*m.b28*m.b29 + 64*m.b25*m.b26*m.b29*m.b30 + 64*m.b25*m.b27*m.b28*m.b30 + 128*m.b26*m.b27*
                       m.b28*m.b29 + 64*m.b26*m.b27*m.b29*m.b30 + 64*m.b27*m.b28*m.b29*m.b30 - 32*m.b1*m.b2*m.b3 - 64*
                       m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 
                       64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*
                       m.b13 - 64*m.b1*m.b2*m.b14 - 64*m.b1*m.b2*m.b15 - 64*m.b1*m.b2*m.b16 - 64*m.b1*m.b2*m.b17 - 64*
                       m.b1*m.b2*m.b18 - 64*m.b1*m.b2*m.b19 - 64*m.b1*m.b2*m.b20 - 64*m.b1*m.b2*m.b21 - 64*m.b1*m.b2*
                       m.b22 - 32*m.b1*m.b2*m.b23 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*m.b1*
                       m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*m.b11 - 64*
                       m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 64*m.b1*m.b3*m.b14 - 64*m.b1*m.b3*m.b15 - 64*m.b1*m.b3*
                       m.b16 - 64*m.b1*m.b3*m.b17 - 64*m.b1*m.b3*m.b18 - 64*m.b1*m.b3*m.b19 - 64*m.b1*m.b3*m.b20 - 64*
                       m.b1*m.b3*m.b21 - 32*m.b1*m.b3*m.b22 - 32*m.b1*m.b3*m.b23 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6
                        - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*
                       m.b11 - 64*m.b1*m.b4*m.b12 - 64*m.b1*m.b4*m.b13 - 64*m.b1*m.b4*m.b14 - 64*m.b1*m.b4*m.b15 - 64*
                       m.b1*m.b4*m.b16 - 64*m.b1*m.b4*m.b17 - 64*m.b1*m.b4*m.b18 - 64*m.b1*m.b4*m.b19 - 64*m.b1*m.b4*
                       m.b20 - 32*m.b1*m.b4*m.b21 - 32*m.b1*m.b4*m.b22 - 32*m.b1*m.b4*m.b23 - 64*m.b1*m.b5*m.b6 - 64*
                       m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*m.b11
                        - 64*m.b1*m.b5*m.b12 - 64*m.b1*m.b5*m.b13 - 64*m.b1*m.b5*m.b14 - 64*m.b1*m.b5*m.b15 - 64*m.b1*
                       m.b5*m.b16 - 64*m.b1*m.b5*m.b17 - 64*m.b1*m.b5*m.b18 - 64*m.b1*m.b5*m.b19 - 32*m.b1*m.b5*m.b20 - 
                       32*m.b1*m.b5*m.b21 - 32*m.b1*m.b5*m.b22 - 32*m.b1*m.b5*m.b23 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*
                       m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*m.b11 - 64*m.b1*m.b6*m.b12 - 64*m.b1
                       *m.b6*m.b13 - 64*m.b1*m.b6*m.b14 - 64*m.b1*m.b6*m.b15 - 64*m.b1*m.b6*m.b16 - 64*m.b1*m.b6*m.b17
                        - 64*m.b1*m.b6*m.b18 - 32*m.b1*m.b6*m.b19 - 32*m.b1*m.b6*m.b20 - 32*m.b1*m.b6*m.b21 - 32*m.b1*
                       m.b6*m.b22 - 32*m.b1*m.b6*m.b23 - 64*m.b1*m.b7*m.b8 - 64*m.b1*m.b7*m.b9 - 64*m.b1*m.b7*m.b10 - 64
                       *m.b1*m.b7*m.b11 - 64*m.b1*m.b7*m.b12 - 32*m.b1*m.b7*m.b13 - 64*m.b1*m.b7*m.b14 - 64*m.b1*m.b7*
                       m.b15 - 64*m.b1*m.b7*m.b16 - 64*m.b1*m.b7*m.b17 - 32*m.b1*m.b7*m.b18 - 32*m.b1*m.b7*m.b19 - 32*
                       m.b1*m.b7*m.b20 - 32*m.b1*m.b7*m.b21 - 32*m.b1*m.b7*m.b22 - 32*m.b1*m.b7*m.b23 - 64*m.b1*m.b8*
                       m.b9 - 64*m.b1*m.b8*m.b10 - 64*m.b1*m.b8*m.b11 - 64*m.b1*m.b8*m.b12 - 64*m.b1*m.b8*m.b13 - 64*
                       m.b1*m.b8*m.b14 - 32*m.b1*m.b8*m.b15 - 64*m.b1*m.b8*m.b16 - 32*m.b1*m.b8*m.b17 - 32*m.b1*m.b8*
                       m.b18 - 32*m.b1*m.b8*m.b19 - 32*m.b1*m.b8*m.b20 - 32*m.b1*m.b8*m.b21 - 32*m.b1*m.b8*m.b22 - 32*
                       m.b1*m.b8*m.b23 - 64*m.b1*m.b9*m.b10 - 64*m.b1*m.b9*m.b11 - 64*m.b1*m.b9*m.b12 - 64*m.b1*m.b9*
                       m.b13 - 64*m.b1*m.b9*m.b14 - 64*m.b1*m.b9*m.b15 - 32*m.b1*m.b9*m.b16 - 32*m.b1*m.b9*m.b18 - 32*
                       m.b1*m.b9*m.b19 - 32*m.b1*m.b9*m.b20 - 32*m.b1*m.b9*m.b21 - 32*m.b1*m.b9*m.b22 - 32*m.b1*m.b9*
                       m.b23 - 64*m.b1*m.b10*m.b11 - 64*m.b1*m.b10*m.b12 - 64*m.b1*m.b10*m.b13 - 64*m.b1*m.b10*m.b14 - 
                       32*m.b1*m.b10*m.b15 - 32*m.b1*m.b10*m.b16 - 32*m.b1*m.b10*m.b17 - 32*m.b1*m.b10*m.b18 - 32*m.b1*
                       m.b10*m.b20 - 32*m.b1*m.b10*m.b21 - 32*m.b1*m.b10*m.b22 - 32*m.b1*m.b10*m.b23 - 64*m.b1*m.b11*
                       m.b12 - 64*m.b1*m.b11*m.b13 - 32*m.b1*m.b11*m.b14 - 32*m.b1*m.b11*m.b15 - 32*m.b1*m.b11*m.b16 - 
                       32*m.b1*m.b11*m.b17 - 32*m.b1*m.b11*m.b18 - 32*m.b1*m.b11*m.b19 - 32*m.b1*m.b11*m.b20 - 32*m.b1*
                       m.b11*m.b22 - 32*m.b1*m.b11*m.b23 - 32*m.b1*m.b12*m.b13 - 32*m.b1*m.b12*m.b14 - 32*m.b1*m.b12*
                       m.b15 - 32*m.b1*m.b12*m.b16 - 32*m.b1*m.b12*m.b17 - 32*m.b1*m.b12*m.b18 - 32*m.b1*m.b12*m.b19 - 
                       32*m.b1*m.b12*m.b20 - 32*m.b1*m.b12*m.b21 - 32*m.b1*m.b12*m.b22 - 32*m.b1*m.b13*m.b14 - 32*m.b1*
                       m.b13*m.b15 - 32*m.b1*m.b13*m.b16 - 32*m.b1*m.b13*m.b17 - 32*m.b1*m.b13*m.b18 - 32*m.b1*m.b13*
                       m.b19 - 32*m.b1*m.b13*m.b20 - 32*m.b1*m.b13*m.b21 - 32*m.b1*m.b13*m.b22 - 32*m.b1*m.b13*m.b23 - 
                       32*m.b1*m.b14*m.b15 - 32*m.b1*m.b14*m.b16 - 32*m.b1*m.b14*m.b17 - 32*m.b1*m.b14*m.b18 - 32*m.b1*
                       m.b14*m.b19 - 32*m.b1*m.b14*m.b20 - 32*m.b1*m.b14*m.b21 - 32*m.b1*m.b14*m.b22 - 32*m.b1*m.b14*
                       m.b23 - 32*m.b1*m.b15*m.b16 - 32*m.b1*m.b15*m.b17 - 32*m.b1*m.b15*m.b18 - 32*m.b1*m.b15*m.b19 - 
                       32*m.b1*m.b15*m.b20 - 32*m.b1*m.b15*m.b21 - 32*m.b1*m.b15*m.b22 - 32*m.b1*m.b15*m.b23 - 32*m.b1*
                       m.b16*m.b17 - 32*m.b1*m.b16*m.b18 - 32*m.b1*m.b16*m.b19 - 32*m.b1*m.b16*m.b20 - 32*m.b1*m.b16*
                       m.b21 - 32*m.b1*m.b16*m.b22 - 32*m.b1*m.b16*m.b23 - 32*m.b1*m.b17*m.b18 - 32*m.b1*m.b17*m.b19 - 
                       32*m.b1*m.b17*m.b20 - 32*m.b1*m.b17*m.b21 - 32*m.b1*m.b17*m.b22 - 32*m.b1*m.b17*m.b23 - 32*m.b1*
                       m.b18*m.b19 - 32*m.b1*m.b18*m.b20 - 32*m.b1*m.b18*m.b21 - 32*m.b1*m.b18*m.b22 - 32*m.b1*m.b18*
                       m.b23 - 32*m.b1*m.b19*m.b20 - 32*m.b1*m.b19*m.b21 - 32*m.b1*m.b19*m.b22 - 32*m.b1*m.b19*m.b23 - 
                       32*m.b1*m.b20*m.b21 - 32*m.b1*m.b20*m.b22 - 32*m.b1*m.b20*m.b23 - 32*m.b1*m.b21*m.b22 - 32*m.b1*
                       m.b21*m.b23 - 32*m.b1*m.b22*m.b23 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6
                        - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*
                       m.b3*m.b11 - 128*m.b2*m.b3*m.b12 - 128*m.b2*m.b3*m.b13 - 128*m.b2*m.b3*m.b14 - 128*m.b2*m.b3*
                       m.b15 - 128*m.b2*m.b3*m.b16 - 128*m.b2*m.b3*m.b17 - 128*m.b2*m.b3*m.b18 - 128*m.b2*m.b3*m.b19 - 
                       128*m.b2*m.b3*m.b20 - 128*m.b2*m.b3*m.b21 - 128*m.b2*m.b3*m.b22 - 96*m.b2*m.b3*m.b23 - 32*m.b2*
                       m.b3*m.b24 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 
                       128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 128*m.b2*
                       m.b4*m.b13 - 128*m.b2*m.b4*m.b14 - 128*m.b2*m.b4*m.b15 - 128*m.b2*m.b4*m.b16 - 128*m.b2*m.b4*
                       m.b17 - 128*m.b2*m.b4*m.b18 - 128*m.b2*m.b4*m.b19 - 128*m.b2*m.b4*m.b20 - 128*m.b2*m.b4*m.b21 - 
                       96*m.b2*m.b4*m.b22 - 64*m.b2*m.b4*m.b23 - 32*m.b2*m.b4*m.b24 - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5
                       *m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 128*m.b2*m.b5*m.b11 - 128*
                       m.b2*m.b5*m.b12 - 128*m.b2*m.b5*m.b13 - 128*m.b2*m.b5*m.b14 - 128*m.b2*m.b5*m.b15 - 128*m.b2*m.b5
                       *m.b16 - 128*m.b2*m.b5*m.b17 - 128*m.b2*m.b5*m.b18 - 128*m.b2*m.b5*m.b19 - 128*m.b2*m.b5*m.b20 - 
                       96*m.b2*m.b5*m.b21 - 64*m.b2*m.b5*m.b22 - 64*m.b2*m.b5*m.b23 - 32*m.b2*m.b5*m.b24 - 160*m.b2*m.b6
                       *m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b10 - 128*m.b2*m.b6*m.b11 - 128*
                       m.b2*m.b6*m.b12 - 128*m.b2*m.b6*m.b13 - 128*m.b2*m.b6*m.b14 - 128*m.b2*m.b6*m.b15 - 128*m.b2*m.b6
                       *m.b16 - 128*m.b2*m.b6*m.b17 - 128*m.b2*m.b6*m.b18 - 128*m.b2*m.b6*m.b19 - 96*m.b2*m.b6*m.b20 - 
                       64*m.b2*m.b6*m.b21 - 64*m.b2*m.b6*m.b22 - 64*m.b2*m.b6*m.b23 - 32*m.b2*m.b6*m.b24 - 160*m.b2*m.b7
                       *m.b8 - 128*m.b2*m.b7*m.b9 - 128*m.b2*m.b7*m.b10 - 128*m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b12 - 128
                       *m.b2*m.b7*m.b13 - 128*m.b2*m.b7*m.b14 - 128*m.b2*m.b7*m.b15 - 128*m.b2*m.b7*m.b16 - 128*m.b2*
                       m.b7*m.b17 - 128*m.b2*m.b7*m.b18 - 96*m.b2*m.b7*m.b19 - 64*m.b2*m.b7*m.b20 - 64*m.b2*m.b7*m.b21
                        - 64*m.b2*m.b7*m.b22 - 64*m.b2*m.b7*m.b23 - 32*m.b2*m.b7*m.b24 - 160*m.b2*m.b8*m.b9 - 128*m.b2*
                       m.b8*m.b10 - 128*m.b2*m.b8*m.b11 - 128*m.b2*m.b8*m.b12 - 128*m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b14
                        - 128*m.b2*m.b8*m.b15 - 128*m.b2*m.b8*m.b16 - 128*m.b2*m.b8*m.b17 - 96*m.b2*m.b8*m.b18 - 64*m.b2
                       *m.b8*m.b19 - 64*m.b2*m.b8*m.b20 - 64*m.b2*m.b8*m.b21 - 64*m.b2*m.b8*m.b22 - 64*m.b2*m.b8*m.b23
                        - 32*m.b2*m.b8*m.b24 - 160*m.b2*m.b9*m.b10 - 128*m.b2*m.b9*m.b11 - 128*m.b2*m.b9*m.b12 - 128*
                       m.b2*m.b9*m.b13 - 128*m.b2*m.b9*m.b14 - 128*m.b2*m.b9*m.b15 - 64*m.b2*m.b9*m.b16 - 96*m.b2*m.b9*
                       m.b17 - 64*m.b2*m.b9*m.b18 - 64*m.b2*m.b9*m.b19 - 64*m.b2*m.b9*m.b20 - 64*m.b2*m.b9*m.b21 - 64*
                       m.b2*m.b9*m.b22 - 64*m.b2*m.b9*m.b23 - 32*m.b2*m.b9*m.b24 - 160*m.b2*m.b10*m.b11 - 128*m.b2*m.b10
                       *m.b12 - 128*m.b2*m.b10*m.b13 - 128*m.b2*m.b10*m.b14 - 128*m.b2*m.b10*m.b15 - 96*m.b2*m.b10*m.b16
                        - 64*m.b2*m.b10*m.b17 - 64*m.b2*m.b10*m.b19 - 64*m.b2*m.b10*m.b20 - 64*m.b2*m.b10*m.b21 - 64*
                       m.b2*m.b10*m.b22 - 64*m.b2*m.b10*m.b23 - 32*m.b2*m.b10*m.b24 - 160*m.b2*m.b11*m.b12 - 128*m.b2*
                       m.b11*m.b13 - 128*m.b2*m.b11*m.b14 - 96*m.b2*m.b11*m.b15 - 64*m.b2*m.b11*m.b16 - 64*m.b2*m.b11*
                       m.b17 - 64*m.b2*m.b11*m.b18 - 64*m.b2*m.b11*m.b19 - 64*m.b2*m.b11*m.b21 - 64*m.b2*m.b11*m.b22 - 
                       64*m.b2*m.b11*m.b23 - 32*m.b2*m.b11*m.b24 - 160*m.b2*m.b12*m.b13 - 96*m.b2*m.b12*m.b14 - 64*m.b2*
                       m.b12*m.b15 - 64*m.b2*m.b12*m.b16 - 64*m.b2*m.b12*m.b17 - 64*m.b2*m.b12*m.b18 - 64*m.b2*m.b12*
                       m.b19 - 64*m.b2*m.b12*m.b20 - 64*m.b2*m.b12*m.b21 - 64*m.b2*m.b12*m.b23 - 32*m.b2*m.b12*m.b24 - 
                       96*m.b2*m.b13*m.b14 - 64*m.b2*m.b13*m.b15 - 64*m.b2*m.b13*m.b16 - 64*m.b2*m.b13*m.b17 - 64*m.b2*
                       m.b13*m.b18 - 64*m.b2*m.b13*m.b19 - 64*m.b2*m.b13*m.b20 - 64*m.b2*m.b13*m.b21 - 64*m.b2*m.b13*
                       m.b22 - 64*m.b2*m.b13*m.b23 - 96*m.b2*m.b14*m.b15 - 64*m.b2*m.b14*m.b16 - 64*m.b2*m.b14*m.b17 - 
                       64*m.b2*m.b14*m.b18 - 64*m.b2*m.b14*m.b19 - 64*m.b2*m.b14*m.b20 - 64*m.b2*m.b14*m.b21 - 64*m.b2*
                       m.b14*m.b22 - 64*m.b2*m.b14*m.b23 - 32*m.b2*m.b14*m.b24 - 96*m.b2*m.b15*m.b16 - 64*m.b2*m.b15*
                       m.b17 - 64*m.b2*m.b15*m.b18 - 64*m.b2*m.b15*m.b19 - 64*m.b2*m.b15*m.b20 - 64*m.b2*m.b15*m.b21 - 
                       64*m.b2*m.b15*m.b22 - 64*m.b2*m.b15*m.b23 - 32*m.b2*m.b15*m.b24 - 96*m.b2*m.b16*m.b17 - 64*m.b2*
                       m.b16*m.b18 - 64*m.b2*m.b16*m.b19 - 64*m.b2*m.b16*m.b20 - 64*m.b2*m.b16*m.b21 - 64*m.b2*m.b16*
                       m.b22 - 64*m.b2*m.b16*m.b23 - 32*m.b2*m.b16*m.b24 - 96*m.b2*m.b17*m.b18 - 64*m.b2*m.b17*m.b19 - 
                       64*m.b2*m.b17*m.b20 - 64*m.b2*m.b17*m.b21 - 64*m.b2*m.b17*m.b22 - 64*m.b2*m.b17*m.b23 - 32*m.b2*
                       m.b17*m.b24 - 96*m.b2*m.b18*m.b19 - 64*m.b2*m.b18*m.b20 - 64*m.b2*m.b18*m.b21 - 64*m.b2*m.b18*
                       m.b22 - 64*m.b2*m.b18*m.b23 - 32*m.b2*m.b18*m.b24 - 96*m.b2*m.b19*m.b20 - 64*m.b2*m.b19*m.b21 - 
                       64*m.b2*m.b19*m.b22 - 64*m.b2*m.b19*m.b23 - 32*m.b2*m.b19*m.b24 - 96*m.b2*m.b20*m.b21 - 64*m.b2*
                       m.b20*m.b22 - 64*m.b2*m.b20*m.b23 - 32*m.b2*m.b20*m.b24 - 96*m.b2*m.b21*m.b22 - 64*m.b2*m.b21*
                       m.b23 - 32*m.b2*m.b21*m.b24 - 96*m.b2*m.b22*m.b23 - 32*m.b2*m.b22*m.b24 - 32*m.b2*m.b23*m.b24 - 
                       160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4
                       *m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 192*m.b3*m.b4*m.b13 - 
                       192*m.b3*m.b4*m.b14 - 192*m.b3*m.b4*m.b15 - 192*m.b3*m.b4*m.b16 - 192*m.b3*m.b4*m.b17 - 192*m.b3*
                       m.b4*m.b18 - 192*m.b3*m.b4*m.b19 - 192*m.b3*m.b4*m.b20 - 192*m.b3*m.b4*m.b21 - 192*m.b3*m.b4*
                       m.b22 - 160*m.b3*m.b4*m.b23 - 96*m.b3*m.b4*m.b24 - 32*m.b3*m.b4*m.b25 - 256*m.b3*m.b5*m.b6 - 128*
                       m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10 - 192*m.b3*m.b5*
                       m.b11 - 192*m.b3*m.b5*m.b12 - 192*m.b3*m.b5*m.b13 - 192*m.b3*m.b5*m.b14 - 192*m.b3*m.b5*m.b15 - 
                       192*m.b3*m.b5*m.b16 - 192*m.b3*m.b5*m.b17 - 192*m.b3*m.b5*m.b18 - 192*m.b3*m.b5*m.b19 - 192*m.b3*
                       m.b5*m.b20 - 192*m.b3*m.b5*m.b21 - 160*m.b3*m.b5*m.b22 - 128*m.b3*m.b5*m.b23 - 64*m.b3*m.b5*m.b24
                        - 32*m.b3*m.b5*m.b25 - 256*m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*
                       m.b6*m.b10 - 192*m.b3*m.b6*m.b11 - 192*m.b3*m.b6*m.b12 - 192*m.b3*m.b6*m.b13 - 192*m.b3*m.b6*
                       m.b14 - 192*m.b3*m.b6*m.b15 - 192*m.b3*m.b6*m.b16 - 192*m.b3*m.b6*m.b17 - 192*m.b3*m.b6*m.b18 - 
                       192*m.b3*m.b6*m.b19 - 192*m.b3*m.b6*m.b20 - 160*m.b3*m.b6*m.b21 - 128*m.b3*m.b6*m.b22 - 96*m.b3*
                       m.b6*m.b23 - 64*m.b3*m.b6*m.b24 - 32*m.b3*m.b6*m.b25 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 
                       192*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*m.b11 - 192*m.b3*m.b7*m.b12 - 192*m.b3*m.b7*m.b13 - 192*m.b3*
                       m.b7*m.b14 - 192*m.b3*m.b7*m.b15 - 192*m.b3*m.b7*m.b16 - 192*m.b3*m.b7*m.b17 - 192*m.b3*m.b7*
                       m.b18 - 192*m.b3*m.b7*m.b19 - 160*m.b3*m.b7*m.b20 - 128*m.b3*m.b7*m.b21 - 96*m.b3*m.b7*m.b22 - 96
                       *m.b3*m.b7*m.b23 - 64*m.b3*m.b7*m.b24 - 32*m.b3*m.b7*m.b25 - 256*m.b3*m.b8*m.b9 - 224*m.b3*m.b8*
                       m.b10 - 192*m.b3*m.b8*m.b11 - 192*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*m.b13 - 192*m.b3*m.b8*m.b14 - 
                       192*m.b3*m.b8*m.b15 - 192*m.b3*m.b8*m.b16 - 192*m.b3*m.b8*m.b17 - 192*m.b3*m.b8*m.b18 - 160*m.b3*
                       m.b8*m.b19 - 128*m.b3*m.b8*m.b20 - 96*m.b3*m.b8*m.b21 - 96*m.b3*m.b8*m.b22 - 96*m.b3*m.b8*m.b23
                        - 64*m.b3*m.b8*m.b24 - 32*m.b3*m.b8*m.b25 - 256*m.b3*m.b9*m.b10 - 224*m.b3*m.b9*m.b11 - 192*m.b3
                       *m.b9*m.b12 - 192*m.b3*m.b9*m.b13 - 192*m.b3*m.b9*m.b14 - 96*m.b3*m.b9*m.b15 - 192*m.b3*m.b9*
                       m.b16 - 192*m.b3*m.b9*m.b17 - 160*m.b3*m.b9*m.b18 - 128*m.b3*m.b9*m.b19 - 96*m.b3*m.b9*m.b20 - 96
                       *m.b3*m.b9*m.b21 - 96*m.b3*m.b9*m.b22 - 96*m.b3*m.b9*m.b23 - 64*m.b3*m.b9*m.b24 - 32*m.b3*m.b9*
                       m.b25 - 256*m.b3*m.b10*m.b11 - 224*m.b3*m.b10*m.b12 - 192*m.b3*m.b10*m.b13 - 192*m.b3*m.b10*m.b14
                        - 192*m.b3*m.b10*m.b15 - 192*m.b3*m.b10*m.b16 - 64*m.b3*m.b10*m.b17 - 128*m.b3*m.b10*m.b18 - 96*
                       m.b3*m.b10*m.b19 - 96*m.b3*m.b10*m.b20 - 96*m.b3*m.b10*m.b21 - 96*m.b3*m.b10*m.b22 - 96*m.b3*
                       m.b10*m.b23 - 64*m.b3*m.b10*m.b24 - 32*m.b3*m.b10*m.b25 - 256*m.b3*m.b11*m.b12 - 224*m.b3*m.b11*
                       m.b13 - 192*m.b3*m.b11*m.b14 - 192*m.b3*m.b11*m.b15 - 160*m.b3*m.b11*m.b16 - 128*m.b3*m.b11*m.b17
                        - 96*m.b3*m.b11*m.b18 - 96*m.b3*m.b11*m.b20 - 96*m.b3*m.b11*m.b21 - 96*m.b3*m.b11*m.b22 - 96*
                       m.b3*m.b11*m.b23 - 64*m.b3*m.b11*m.b24 - 32*m.b3*m.b11*m.b25 - 256*m.b3*m.b12*m.b13 - 224*m.b3*
                       m.b12*m.b14 - 160*m.b3*m.b12*m.b15 - 128*m.b3*m.b12*m.b16 - 96*m.b3*m.b12*m.b17 - 96*m.b3*m.b12*
                       m.b18 - 96*m.b3*m.b12*m.b19 - 96*m.b3*m.b12*m.b20 - 96*m.b3*m.b12*m.b22 - 96*m.b3*m.b12*m.b23 - 
                       64*m.b3*m.b12*m.b24 - 32*m.b3*m.b12*m.b25 - 224*m.b3*m.b13*m.b14 - 160*m.b3*m.b13*m.b15 - 96*m.b3
                       *m.b13*m.b16 - 96*m.b3*m.b13*m.b17 - 96*m.b3*m.b13*m.b18 - 96*m.b3*m.b13*m.b19 - 96*m.b3*m.b13*
                       m.b20 - 96*m.b3*m.b13*m.b21 - 96*m.b3*m.b13*m.b22 - 64*m.b3*m.b13*m.b24 - 32*m.b3*m.b13*m.b25 - 
                       160*m.b3*m.b14*m.b15 - 128*m.b3*m.b14*m.b16 - 96*m.b3*m.b14*m.b17 - 96*m.b3*m.b14*m.b18 - 96*m.b3
                       *m.b14*m.b19 - 96*m.b3*m.b14*m.b20 - 96*m.b3*m.b14*m.b21 - 96*m.b3*m.b14*m.b22 - 96*m.b3*m.b14*
                       m.b23 - 64*m.b3*m.b14*m.b24 - 160*m.b3*m.b15*m.b16 - 128*m.b3*m.b15*m.b17 - 96*m.b3*m.b15*m.b18
                        - 96*m.b3*m.b15*m.b19 - 96*m.b3*m.b15*m.b20 - 96*m.b3*m.b15*m.b21 - 96*m.b3*m.b15*m.b22 - 96*
                       m.b3*m.b15*m.b23 - 64*m.b3*m.b15*m.b24 - 32*m.b3*m.b15*m.b25 - 160*m.b3*m.b16*m.b17 - 128*m.b3*
                       m.b16*m.b18 - 96*m.b3*m.b16*m.b19 - 96*m.b3*m.b16*m.b20 - 96*m.b3*m.b16*m.b21 - 96*m.b3*m.b16*
                       m.b22 - 96*m.b3*m.b16*m.b23 - 64*m.b3*m.b16*m.b24 - 32*m.b3*m.b16*m.b25 - 160*m.b3*m.b17*m.b18 - 
                       128*m.b3*m.b17*m.b19 - 96*m.b3*m.b17*m.b20 - 96*m.b3*m.b17*m.b21 - 96*m.b3*m.b17*m.b22 - 96*m.b3*
                       m.b17*m.b23 - 64*m.b3*m.b17*m.b24 - 32*m.b3*m.b17*m.b25 - 160*m.b3*m.b18*m.b19 - 128*m.b3*m.b18*
                       m.b20 - 96*m.b3*m.b18*m.b21 - 96*m.b3*m.b18*m.b22 - 96*m.b3*m.b18*m.b23 - 64*m.b3*m.b18*m.b24 - 
                       32*m.b3*m.b18*m.b25 - 160*m.b3*m.b19*m.b20 - 128*m.b3*m.b19*m.b21 - 96*m.b3*m.b19*m.b22 - 96*m.b3
                       *m.b19*m.b23 - 64*m.b3*m.b19*m.b24 - 32*m.b3*m.b19*m.b25 - 160*m.b3*m.b20*m.b21 - 128*m.b3*m.b20*
                       m.b22 - 96*m.b3*m.b20*m.b23 - 64*m.b3*m.b20*m.b24 - 32*m.b3*m.b20*m.b25 - 160*m.b3*m.b21*m.b22 - 
                       128*m.b3*m.b21*m.b23 - 64*m.b3*m.b21*m.b24 - 32*m.b3*m.b21*m.b25 - 160*m.b3*m.b22*m.b23 - 64*m.b3
                       *m.b22*m.b24 - 32*m.b3*m.b22*m.b25 - 96*m.b3*m.b23*m.b24 - 32*m.b3*m.b23*m.b25 - 32*m.b3*m.b24*
                       m.b25 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*
                       m.b4*m.b5*m.b10 - 256*m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256*m.b4*m.b5*m.b13 - 256*m.b4*m.b5
                       *m.b14 - 256*m.b4*m.b5*m.b15 - 256*m.b4*m.b5*m.b16 - 256*m.b4*m.b5*m.b17 - 256*m.b4*m.b5*m.b18 - 
                       256*m.b4*m.b5*m.b19 - 256*m.b4*m.b5*m.b20 - 256*m.b4*m.b5*m.b21 - 256*m.b4*m.b5*m.b22 - 224*m.b4*
                       m.b5*m.b23 - 160*m.b4*m.b5*m.b24 - 96*m.b4*m.b5*m.b25 - 32*m.b4*m.b5*m.b26 - 352*m.b4*m.b6*m.b7
                        - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*m.b4*m.b6*m.b11 - 256*m.b4
                       *m.b6*m.b12 - 256*m.b4*m.b6*m.b13 - 256*m.b4*m.b6*m.b14 - 256*m.b4*m.b6*m.b15 - 256*m.b4*m.b6*
                       m.b16 - 256*m.b4*m.b6*m.b17 - 256*m.b4*m.b6*m.b18 - 256*m.b4*m.b6*m.b19 - 256*m.b4*m.b6*m.b20 - 
                       256*m.b4*m.b6*m.b21 - 224*m.b4*m.b6*m.b22 - 192*m.b4*m.b6*m.b23 - 128*m.b4*m.b6*m.b24 - 64*m.b4*
                       m.b6*m.b25 - 32*m.b4*m.b6*m.b26 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*m.b4*m.b7*m.b10
                        - 256*m.b4*m.b7*m.b11 - 256*m.b4*m.b7*m.b12 - 256*m.b4*m.b7*m.b13 - 256*m.b4*m.b7*m.b14 - 256*
                       m.b4*m.b7*m.b15 - 256*m.b4*m.b7*m.b16 - 256*m.b4*m.b7*m.b17 - 256*m.b4*m.b7*m.b18 - 256*m.b4*m.b7
                       *m.b19 - 256*m.b4*m.b7*m.b20 - 224*m.b4*m.b7*m.b21 - 192*m.b4*m.b7*m.b22 - 160*m.b4*m.b7*m.b23 - 
                       96*m.b4*m.b7*m.b24 - 64*m.b4*m.b7*m.b25 - 32*m.b4*m.b7*m.b26 - 352*m.b4*m.b8*m.b9 - 320*m.b4*m.b8
                       *m.b10 - 288*m.b4*m.b8*m.b11 - 128*m.b4*m.b8*m.b12 - 256*m.b4*m.b8*m.b13 - 256*m.b4*m.b8*m.b14 - 
                       256*m.b4*m.b8*m.b15 - 256*m.b4*m.b8*m.b16 - 256*m.b4*m.b8*m.b17 - 256*m.b4*m.b8*m.b18 - 256*m.b4*
                       m.b8*m.b19 - 224*m.b4*m.b8*m.b20 - 192*m.b4*m.b8*m.b21 - 160*m.b4*m.b8*m.b22 - 128*m.b4*m.b8*
                       m.b23 - 96*m.b4*m.b8*m.b24 - 64*m.b4*m.b8*m.b25 - 32*m.b4*m.b8*m.b26 - 352*m.b4*m.b9*m.b10 - 320*
                       m.b4*m.b9*m.b11 - 288*m.b4*m.b9*m.b12 - 256*m.b4*m.b9*m.b13 - 128*m.b4*m.b9*m.b14 - 256*m.b4*m.b9
                       *m.b15 - 256*m.b4*m.b9*m.b16 - 256*m.b4*m.b9*m.b17 - 256*m.b4*m.b9*m.b18 - 224*m.b4*m.b9*m.b19 - 
                       192*m.b4*m.b9*m.b20 - 160*m.b4*m.b9*m.b21 - 128*m.b4*m.b9*m.b22 - 128*m.b4*m.b9*m.b23 - 96*m.b4*
                       m.b9*m.b24 - 64*m.b4*m.b9*m.b25 - 32*m.b4*m.b9*m.b26 - 352*m.b4*m.b10*m.b11 - 320*m.b4*m.b10*
                       m.b12 - 288*m.b4*m.b10*m.b13 - 256*m.b4*m.b10*m.b14 - 256*m.b4*m.b10*m.b15 - 128*m.b4*m.b10*m.b16
                        - 256*m.b4*m.b10*m.b17 - 224*m.b4*m.b10*m.b18 - 192*m.b4*m.b10*m.b19 - 160*m.b4*m.b10*m.b20 - 
                       128*m.b4*m.b10*m.b21 - 128*m.b4*m.b10*m.b22 - 128*m.b4*m.b10*m.b23 - 96*m.b4*m.b10*m.b24 - 64*
                       m.b4*m.b10*m.b25 - 32*m.b4*m.b10*m.b26 - 352*m.b4*m.b11*m.b12 - 320*m.b4*m.b11*m.b13 - 288*m.b4*
                       m.b11*m.b14 - 256*m.b4*m.b11*m.b15 - 256*m.b4*m.b11*m.b16 - 224*m.b4*m.b11*m.b17 - 64*m.b4*m.b11*
                       m.b18 - 160*m.b4*m.b11*m.b19 - 128*m.b4*m.b11*m.b20 - 128*m.b4*m.b11*m.b21 - 128*m.b4*m.b11*m.b22
                        - 128*m.b4*m.b11*m.b23 - 96*m.b4*m.b11*m.b24 - 64*m.b4*m.b11*m.b25 - 32*m.b4*m.b11*m.b26 - 352*
                       m.b4*m.b12*m.b13 - 320*m.b4*m.b12*m.b14 - 288*m.b4*m.b12*m.b15 - 224*m.b4*m.b12*m.b16 - 192*m.b4*
                       m.b12*m.b17 - 160*m.b4*m.b12*m.b18 - 128*m.b4*m.b12*m.b19 - 128*m.b4*m.b12*m.b21 - 128*m.b4*m.b12
                       *m.b22 - 128*m.b4*m.b12*m.b23 - 96*m.b4*m.b12*m.b24 - 64*m.b4*m.b12*m.b25 - 32*m.b4*m.b12*m.b26
                        - 352*m.b4*m.b13*m.b14 - 288*m.b4*m.b13*m.b15 - 224*m.b4*m.b13*m.b16 - 160*m.b4*m.b13*m.b17 - 
                       128*m.b4*m.b13*m.b18 - 128*m.b4*m.b13*m.b19 - 128*m.b4*m.b13*m.b20 - 128*m.b4*m.b13*m.b21 - 128*
                       m.b4*m.b13*m.b23 - 96*m.b4*m.b13*m.b24 - 64*m.b4*m.b13*m.b25 - 32*m.b4*m.b13*m.b26 - 288*m.b4*
                       m.b14*m.b15 - 224*m.b4*m.b14*m.b16 - 160*m.b4*m.b14*m.b17 - 128*m.b4*m.b14*m.b18 - 128*m.b4*m.b14
                       *m.b19 - 128*m.b4*m.b14*m.b20 - 128*m.b4*m.b14*m.b21 - 128*m.b4*m.b14*m.b22 - 128*m.b4*m.b14*
                       m.b23 - 64*m.b4*m.b14*m.b25 - 32*m.b4*m.b14*m.b26 - 224*m.b4*m.b15*m.b16 - 192*m.b4*m.b15*m.b17
                        - 160*m.b4*m.b15*m.b18 - 128*m.b4*m.b15*m.b19 - 128*m.b4*m.b15*m.b20 - 128*m.b4*m.b15*m.b21 - 
                       128*m.b4*m.b15*m.b22 - 128*m.b4*m.b15*m.b23 - 96*m.b4*m.b15*m.b24 - 64*m.b4*m.b15*m.b25 - 224*
                       m.b4*m.b16*m.b17 - 192*m.b4*m.b16*m.b18 - 160*m.b4*m.b16*m.b19 - 128*m.b4*m.b16*m.b20 - 128*m.b4*
                       m.b16*m.b21 - 128*m.b4*m.b16*m.b22 - 128*m.b4*m.b16*m.b23 - 96*m.b4*m.b16*m.b24 - 64*m.b4*m.b16*
                       m.b25 - 32*m.b4*m.b16*m.b26 - 224*m.b4*m.b17*m.b18 - 192*m.b4*m.b17*m.b19 - 160*m.b4*m.b17*m.b20
                        - 128*m.b4*m.b17*m.b21 - 128*m.b4*m.b17*m.b22 - 128*m.b4*m.b17*m.b23 - 96*m.b4*m.b17*m.b24 - 64*
                       m.b4*m.b17*m.b25 - 32*m.b4*m.b17*m.b26 - 224*m.b4*m.b18*m.b19 - 192*m.b4*m.b18*m.b20 - 160*m.b4*
                       m.b18*m.b21 - 128*m.b4*m.b18*m.b22 - 128*m.b4*m.b18*m.b23 - 96*m.b4*m.b18*m.b24 - 64*m.b4*m.b18*
                       m.b25 - 32*m.b4*m.b18*m.b26 - 224*m.b4*m.b19*m.b20 - 192*m.b4*m.b19*m.b21 - 160*m.b4*m.b19*m.b22
                        - 128*m.b4*m.b19*m.b23 - 96*m.b4*m.b19*m.b24 - 64*m.b4*m.b19*m.b25 - 32*m.b4*m.b19*m.b26 - 224*
                       m.b4*m.b20*m.b21 - 192*m.b4*m.b20*m.b22 - 160*m.b4*m.b20*m.b23 - 96*m.b4*m.b20*m.b24 - 64*m.b4*
                       m.b20*m.b25 - 32*m.b4*m.b20*m.b26 - 224*m.b4*m.b21*m.b22 - 192*m.b4*m.b21*m.b23 - 96*m.b4*m.b21*
                       m.b24 - 64*m.b4*m.b21*m.b25 - 32*m.b4*m.b21*m.b26 - 224*m.b4*m.b22*m.b23 - 128*m.b4*m.b22*m.b24
                        - 64*m.b4*m.b22*m.b25 - 32*m.b4*m.b22*m.b26 - 160*m.b4*m.b23*m.b24 - 64*m.b4*m.b23*m.b25 - 32*
                       m.b4*m.b23*m.b26 - 96*m.b4*m.b24*m.b25 - 32*m.b4*m.b24*m.b26 - 32*m.b4*m.b25*m.b26 - 288*m.b5*
                       m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*m.b6*m.b11
                        - 320*m.b5*m.b6*m.b12 - 320*m.b5*m.b6*m.b13 - 320*m.b5*m.b6*m.b14 - 320*m.b5*m.b6*m.b15 - 320*
                       m.b5*m.b6*m.b16 - 320*m.b5*m.b6*m.b17 - 320*m.b5*m.b6*m.b18 - 320*m.b5*m.b6*m.b19 - 320*m.b5*m.b6
                       *m.b20 - 320*m.b5*m.b6*m.b21 - 320*m.b5*m.b6*m.b22 - 288*m.b5*m.b6*m.b23 - 224*m.b5*m.b6*m.b24 - 
                       160*m.b5*m.b6*m.b25 - 96*m.b5*m.b6*m.b26 - 32*m.b5*m.b6*m.b27 - 448*m.b5*m.b7*m.b8 - 256*m.b5*
                       m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11 - 320*m.b5*m.b7*m.b12 - 320*m.b5*m.b7*m.b13
                        - 320*m.b5*m.b7*m.b14 - 320*m.b5*m.b7*m.b15 - 320*m.b5*m.b7*m.b16 - 320*m.b5*m.b7*m.b17 - 320*
                       m.b5*m.b7*m.b18 - 320*m.b5*m.b7*m.b19 - 320*m.b5*m.b7*m.b20 - 320*m.b5*m.b7*m.b21 - 288*m.b5*m.b7
                       *m.b22 - 256*m.b5*m.b7*m.b23 - 192*m.b5*m.b7*m.b24 - 128*m.b5*m.b7*m.b25 - 64*m.b5*m.b7*m.b26 - 
                       32*m.b5*m.b7*m.b27 - 448*m.b5*m.b8*m.b9 - 416*m.b5*m.b8*m.b10 - 224*m.b5*m.b8*m.b11 - 352*m.b5*
                       m.b8*m.b12 - 320*m.b5*m.b8*m.b13 - 320*m.b5*m.b8*m.b14 - 320*m.b5*m.b8*m.b15 - 320*m.b5*m.b8*
                       m.b16 - 320*m.b5*m.b8*m.b17 - 320*m.b5*m.b8*m.b18 - 320*m.b5*m.b8*m.b19 - 320*m.b5*m.b8*m.b20 - 
                       288*m.b5*m.b8*m.b21 - 256*m.b5*m.b8*m.b22 - 224*m.b5*m.b8*m.b23 - 160*m.b5*m.b8*m.b24 - 96*m.b5*
                       m.b8*m.b25 - 64*m.b5*m.b8*m.b26 - 32*m.b5*m.b8*m.b27 - 448*m.b5*m.b9*m.b10 - 416*m.b5*m.b9*m.b11
                        - 384*m.b5*m.b9*m.b12 - 192*m.b5*m.b9*m.b13 - 320*m.b5*m.b9*m.b14 - 320*m.b5*m.b9*m.b15 - 320*
                       m.b5*m.b9*m.b16 - 320*m.b5*m.b9*m.b17 - 320*m.b5*m.b9*m.b18 - 320*m.b5*m.b9*m.b19 - 288*m.b5*m.b9
                       *m.b20 - 256*m.b5*m.b9*m.b21 - 224*m.b5*m.b9*m.b22 - 192*m.b5*m.b9*m.b23 - 128*m.b5*m.b9*m.b24 - 
                       96*m.b5*m.b9*m.b25 - 64*m.b5*m.b9*m.b26 - 32*m.b5*m.b9*m.b27 - 448*m.b5*m.b10*m.b11 - 416*m.b5*
                       m.b10*m.b12 - 384*m.b5*m.b10*m.b13 - 352*m.b5*m.b10*m.b14 - 160*m.b5*m.b10*m.b15 - 320*m.b5*m.b10
                       *m.b16 - 320*m.b5*m.b10*m.b17 - 320*m.b5*m.b10*m.b18 - 288*m.b5*m.b10*m.b19 - 256*m.b5*m.b10*
                       m.b20 - 224*m.b5*m.b10*m.b21 - 192*m.b5*m.b10*m.b22 - 160*m.b5*m.b10*m.b23 - 128*m.b5*m.b10*m.b24
                        - 96*m.b5*m.b10*m.b25 - 64*m.b5*m.b10*m.b26 - 32*m.b5*m.b10*m.b27 - 448*m.b5*m.b11*m.b12 - 416*
                       m.b5*m.b11*m.b13 - 384*m.b5*m.b11*m.b14 - 352*m.b5*m.b11*m.b15 - 320*m.b5*m.b11*m.b16 - 160*m.b5*
                       m.b11*m.b17 - 288*m.b5*m.b11*m.b18 - 256*m.b5*m.b11*m.b19 - 224*m.b5*m.b11*m.b20 - 192*m.b5*m.b11
                       *m.b21 - 160*m.b5*m.b11*m.b22 - 160*m.b5*m.b11*m.b23 - 128*m.b5*m.b11*m.b24 - 96*m.b5*m.b11*m.b25
                        - 64*m.b5*m.b11*m.b26 - 32*m.b5*m.b11*m.b27 - 448*m.b5*m.b12*m.b13 - 416*m.b5*m.b12*m.b14 - 384*
                       m.b5*m.b12*m.b15 - 352*m.b5*m.b12*m.b16 - 288*m.b5*m.b12*m.b17 - 256*m.b5*m.b12*m.b18 - 64*m.b5*
                       m.b12*m.b19 - 192*m.b5*m.b12*m.b20 - 160*m.b5*m.b12*m.b21 - 160*m.b5*m.b12*m.b22 - 160*m.b5*m.b12
                       *m.b23 - 128*m.b5*m.b12*m.b24 - 96*m.b5*m.b12*m.b25 - 64*m.b5*m.b12*m.b26 - 32*m.b5*m.b12*m.b27
                        - 448*m.b5*m.b13*m.b14 - 416*m.b5*m.b13*m.b15 - 352*m.b5*m.b13*m.b16 - 288*m.b5*m.b13*m.b17 - 
                       224*m.b5*m.b13*m.b18 - 192*m.b5*m.b13*m.b19 - 160*m.b5*m.b13*m.b20 - 160*m.b5*m.b13*m.b22 - 160*
                       m.b5*m.b13*m.b23 - 128*m.b5*m.b13*m.b24 - 96*m.b5*m.b13*m.b25 - 64*m.b5*m.b13*m.b26 - 32*m.b5*
                       m.b13*m.b27 - 416*m.b5*m.b14*m.b15 - 352*m.b5*m.b14*m.b16 - 288*m.b5*m.b14*m.b17 - 224*m.b5*m.b14
                       *m.b18 - 160*m.b5*m.b14*m.b19 - 160*m.b5*m.b14*m.b20 - 160*m.b5*m.b14*m.b21 - 160*m.b5*m.b14*
                       m.b22 - 128*m.b5*m.b14*m.b24 - 96*m.b5*m.b14*m.b25 - 64*m.b5*m.b14*m.b26 - 32*m.b5*m.b14*m.b27 - 
                       352*m.b5*m.b15*m.b16 - 288*m.b5*m.b15*m.b17 - 224*m.b5*m.b15*m.b18 - 192*m.b5*m.b15*m.b19 - 160*
                       m.b5*m.b15*m.b20 - 160*m.b5*m.b15*m.b21 - 160*m.b5*m.b15*m.b22 - 160*m.b5*m.b15*m.b23 - 128*m.b5*
                       m.b15*m.b24 - 64*m.b5*m.b15*m.b26 - 32*m.b5*m.b15*m.b27 - 288*m.b5*m.b16*m.b17 - 256*m.b5*m.b16*
                       m.b18 - 224*m.b5*m.b16*m.b19 - 192*m.b5*m.b16*m.b20 - 160*m.b5*m.b16*m.b21 - 160*m.b5*m.b16*m.b22
                        - 160*m.b5*m.b16*m.b23 - 128*m.b5*m.b16*m.b24 - 96*m.b5*m.b16*m.b25 - 64*m.b5*m.b16*m.b26 - 288*
                       m.b5*m.b17*m.b18 - 256*m.b5*m.b17*m.b19 - 224*m.b5*m.b17*m.b20 - 192*m.b5*m.b17*m.b21 - 160*m.b5*
                       m.b17*m.b22 - 160*m.b5*m.b17*m.b23 - 128*m.b5*m.b17*m.b24 - 96*m.b5*m.b17*m.b25 - 64*m.b5*m.b17*
                       m.b26 - 32*m.b5*m.b17*m.b27 - 288*m.b5*m.b18*m.b19 - 256*m.b5*m.b18*m.b20 - 224*m.b5*m.b18*m.b21
                        - 192*m.b5*m.b18*m.b22 - 160*m.b5*m.b18*m.b23 - 128*m.b5*m.b18*m.b24 - 96*m.b5*m.b18*m.b25 - 64*
                       m.b5*m.b18*m.b26 - 32*m.b5*m.b18*m.b27 - 288*m.b5*m.b19*m.b20 - 256*m.b5*m.b19*m.b21 - 224*m.b5*
                       m.b19*m.b22 - 192*m.b5*m.b19*m.b23 - 128*m.b5*m.b19*m.b24 - 96*m.b5*m.b19*m.b25 - 64*m.b5*m.b19*
                       m.b26 - 32*m.b5*m.b19*m.b27 - 288*m.b5*m.b20*m.b21 - 256*m.b5*m.b20*m.b22 - 224*m.b5*m.b20*m.b23
                        - 128*m.b5*m.b20*m.b24 - 96*m.b5*m.b20*m.b25 - 64*m.b5*m.b20*m.b26 - 32*m.b5*m.b20*m.b27 - 288*
                       m.b5*m.b21*m.b22 - 256*m.b5*m.b21*m.b23 - 160*m.b5*m.b21*m.b24 - 96*m.b5*m.b21*m.b25 - 64*m.b5*
                       m.b21*m.b26 - 32*m.b5*m.b21*m.b27 - 288*m.b5*m.b22*m.b23 - 192*m.b5*m.b22*m.b24 - 96*m.b5*m.b22*
                       m.b25 - 64*m.b5*m.b22*m.b26 - 32*m.b5*m.b22*m.b27 - 224*m.b5*m.b23*m.b24 - 128*m.b5*m.b23*m.b25
                        - 64*m.b5*m.b23*m.b26 - 32*m.b5*m.b23*m.b27 - 160*m.b5*m.b24*m.b25 - 64*m.b5*m.b24*m.b26 - 32*
                       m.b5*m.b24*m.b27 - 96*m.b5*m.b25*m.b26 - 32*m.b5*m.b25*m.b27 - 32*m.b5*m.b26*m.b27 - 352*m.b6*
                       m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416*m.b6*m.b7*m.b12
                        - 384*m.b6*m.b7*m.b13 - 384*m.b6*m.b7*m.b14 - 384*m.b6*m.b7*m.b15 - 384*m.b6*m.b7*m.b16 - 384*
                       m.b6*m.b7*m.b17 - 384*m.b6*m.b7*m.b18 - 384*m.b6*m.b7*m.b19 - 384*m.b6*m.b7*m.b20 - 384*m.b6*m.b7
                       *m.b21 - 384*m.b6*m.b7*m.b22 - 352*m.b6*m.b7*m.b23 - 288*m.b6*m.b7*m.b24 - 224*m.b6*m.b7*m.b25 - 
                       160*m.b6*m.b7*m.b26 - 96*m.b6*m.b7*m.b27 - 32*m.b6*m.b7*m.b28 - 544*m.b6*m.b8*m.b9 - 320*m.b6*
                       m.b8*m.b10 - 480*m.b6*m.b8*m.b11 - 448*m.b6*m.b8*m.b12 - 416*m.b6*m.b8*m.b13 - 384*m.b6*m.b8*
                       m.b14 - 384*m.b6*m.b8*m.b15 - 384*m.b6*m.b8*m.b16 - 384*m.b6*m.b8*m.b17 - 384*m.b6*m.b8*m.b18 - 
                       384*m.b6*m.b8*m.b19 - 384*m.b6*m.b8*m.b20 - 384*m.b6*m.b8*m.b21 - 352*m.b6*m.b8*m.b22 - 320*m.b6*
                       m.b8*m.b23 - 256*m.b6*m.b8*m.b24 - 192*m.b6*m.b8*m.b25 - 128*m.b6*m.b8*m.b26 - 64*m.b6*m.b8*m.b27
                        - 32*m.b6*m.b8*m.b28 - 544*m.b6*m.b9*m.b10 - 512*m.b6*m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 448*
                       m.b6*m.b9*m.b13 - 416*m.b6*m.b9*m.b14 - 384*m.b6*m.b9*m.b15 - 384*m.b6*m.b9*m.b16 - 384*m.b6*m.b9
                       *m.b17 - 384*m.b6*m.b9*m.b18 - 384*m.b6*m.b9*m.b19 - 384*m.b6*m.b9*m.b20 - 352*m.b6*m.b9*m.b21 - 
                       320*m.b6*m.b9*m.b22 - 288*m.b6*m.b9*m.b23 - 224*m.b6*m.b9*m.b24 - 160*m.b6*m.b9*m.b25 - 96*m.b6*
                       m.b9*m.b26 - 64*m.b6*m.b9*m.b27 - 32*m.b6*m.b9*m.b28 - 544*m.b6*m.b10*m.b11 - 512*m.b6*m.b10*
                       m.b12 - 480*m.b6*m.b10*m.b13 - 256*m.b6*m.b10*m.b14 - 416*m.b6*m.b10*m.b15 - 384*m.b6*m.b10*m.b16
                        - 384*m.b6*m.b10*m.b17 - 384*m.b6*m.b10*m.b18 - 384*m.b6*m.b10*m.b19 - 352*m.b6*m.b10*m.b20 - 
                       320*m.b6*m.b10*m.b21 - 288*m.b6*m.b10*m.b22 - 256*m.b6*m.b10*m.b23 - 192*m.b6*m.b10*m.b24 - 128*
                       m.b6*m.b10*m.b25 - 96*m.b6*m.b10*m.b26 - 64*m.b6*m.b10*m.b27 - 32*m.b6*m.b10*m.b28 - 544*m.b6*
                       m.b11*m.b12 - 512*m.b6*m.b11*m.b13 - 480*m.b6*m.b11*m.b14 - 448*m.b6*m.b11*m.b15 - 224*m.b6*m.b11
                       *m.b16 - 384*m.b6*m.b11*m.b17 - 384*m.b6*m.b11*m.b18 - 352*m.b6*m.b11*m.b19 - 320*m.b6*m.b11*
                       m.b20 - 288*m.b6*m.b11*m.b21 - 256*m.b6*m.b11*m.b22 - 224*m.b6*m.b11*m.b23 - 160*m.b6*m.b11*m.b24
                        - 128*m.b6*m.b11*m.b25 - 96*m.b6*m.b11*m.b26 - 64*m.b6*m.b11*m.b27 - 32*m.b6*m.b11*m.b28 - 544*
                       m.b6*m.b12*m.b13 - 512*m.b6*m.b12*m.b14 - 480*m.b6*m.b12*m.b15 - 448*m.b6*m.b12*m.b16 - 416*m.b6*
                       m.b12*m.b17 - 160*m.b6*m.b12*m.b18 - 320*m.b6*m.b12*m.b19 - 288*m.b6*m.b12*m.b20 - 256*m.b6*m.b12
                       *m.b21 - 224*m.b6*m.b12*m.b22 - 192*m.b6*m.b12*m.b23 - 160*m.b6*m.b12*m.b24 - 128*m.b6*m.b12*
                       m.b25 - 96*m.b6*m.b12*m.b26 - 64*m.b6*m.b12*m.b27 - 32*m.b6*m.b12*m.b28 - 544*m.b6*m.b13*m.b14 - 
                       512*m.b6*m.b13*m.b15 - 480*m.b6*m.b13*m.b16 - 416*m.b6*m.b13*m.b17 - 352*m.b6*m.b13*m.b18 - 288*
                       m.b6*m.b13*m.b19 - 64*m.b6*m.b13*m.b20 - 224*m.b6*m.b13*m.b21 - 192*m.b6*m.b13*m.b22 - 192*m.b6*
                       m.b13*m.b23 - 160*m.b6*m.b13*m.b24 - 128*m.b6*m.b13*m.b25 - 96*m.b6*m.b13*m.b26 - 64*m.b6*m.b13*
                       m.b27 - 32*m.b6*m.b13*m.b28 - 544*m.b6*m.b14*m.b15 - 480*m.b6*m.b14*m.b16 - 416*m.b6*m.b14*m.b17
                        - 352*m.b6*m.b14*m.b18 - 288*m.b6*m.b14*m.b19 - 224*m.b6*m.b14*m.b20 - 192*m.b6*m.b14*m.b21 - 
                       192*m.b6*m.b14*m.b23 - 160*m.b6*m.b14*m.b24 - 128*m.b6*m.b14*m.b25 - 96*m.b6*m.b14*m.b26 - 64*
                       m.b6*m.b14*m.b27 - 32*m.b6*m.b14*m.b28 - 480*m.b6*m.b15*m.b16 - 416*m.b6*m.b15*m.b17 - 352*m.b6*
                       m.b15*m.b18 - 288*m.b6*m.b15*m.b19 - 224*m.b6*m.b15*m.b20 - 192*m.b6*m.b15*m.b21 - 192*m.b6*m.b15
                       *m.b22 - 192*m.b6*m.b15*m.b23 - 128*m.b6*m.b15*m.b25 - 96*m.b6*m.b15*m.b26 - 64*m.b6*m.b15*m.b27
                        - 32*m.b6*m.b15*m.b28 - 416*m.b6*m.b16*m.b17 - 352*m.b6*m.b16*m.b18 - 288*m.b6*m.b16*m.b19 - 256
                       *m.b6*m.b16*m.b20 - 224*m.b6*m.b16*m.b21 - 192*m.b6*m.b16*m.b22 - 192*m.b6*m.b16*m.b23 - 160*m.b6
                       *m.b16*m.b24 - 128*m.b6*m.b16*m.b25 - 64*m.b6*m.b16*m.b27 - 32*m.b6*m.b16*m.b28 - 352*m.b6*m.b17*
                       m.b18 - 320*m.b6*m.b17*m.b19 - 288*m.b6*m.b17*m.b20 - 256*m.b6*m.b17*m.b21 - 224*m.b6*m.b17*m.b22
                        - 192*m.b6*m.b17*m.b23 - 160*m.b6*m.b17*m.b24 - 128*m.b6*m.b17*m.b25 - 96*m.b6*m.b17*m.b26 - 64*
                       m.b6*m.b17*m.b27 - 352*m.b6*m.b18*m.b19 - 320*m.b6*m.b18*m.b20 - 288*m.b6*m.b18*m.b21 - 256*m.b6*
                       m.b18*m.b22 - 224*m.b6*m.b18*m.b23 - 160*m.b6*m.b18*m.b24 - 128*m.b6*m.b18*m.b25 - 96*m.b6*m.b18*
                       m.b26 - 64*m.b6*m.b18*m.b27 - 32*m.b6*m.b18*m.b28 - 352*m.b6*m.b19*m.b20 - 320*m.b6*m.b19*m.b21
                        - 288*m.b6*m.b19*m.b22 - 256*m.b6*m.b19*m.b23 - 160*m.b6*m.b19*m.b24 - 128*m.b6*m.b19*m.b25 - 96
                       *m.b6*m.b19*m.b26 - 64*m.b6*m.b19*m.b27 - 32*m.b6*m.b19*m.b28 - 352*m.b6*m.b20*m.b21 - 320*m.b6*
                       m.b20*m.b22 - 288*m.b6*m.b20*m.b23 - 192*m.b6*m.b20*m.b24 - 128*m.b6*m.b20*m.b25 - 96*m.b6*m.b20*
                       m.b26 - 64*m.b6*m.b20*m.b27 - 32*m.b6*m.b20*m.b28 - 352*m.b6*m.b21*m.b22 - 320*m.b6*m.b21*m.b23
                        - 224*m.b6*m.b21*m.b24 - 128*m.b6*m.b21*m.b25 - 96*m.b6*m.b21*m.b26 - 64*m.b6*m.b21*m.b27 - 32*
                       m.b6*m.b21*m.b28 - 352*m.b6*m.b22*m.b23 - 256*m.b6*m.b22*m.b24 - 160*m.b6*m.b22*m.b25 - 96*m.b6*
                       m.b22*m.b26 - 64*m.b6*m.b22*m.b27 - 32*m.b6*m.b22*m.b28 - 288*m.b6*m.b23*m.b24 - 192*m.b6*m.b23*
                       m.b25 - 96*m.b6*m.b23*m.b26 - 64*m.b6*m.b23*m.b27 - 32*m.b6*m.b23*m.b28 - 224*m.b6*m.b24*m.b25 - 
                       128*m.b6*m.b24*m.b26 - 64*m.b6*m.b24*m.b27 - 32*m.b6*m.b24*m.b28 - 160*m.b6*m.b25*m.b26 - 64*m.b6
                       *m.b25*m.b27 - 32*m.b6*m.b25*m.b28 - 96*m.b6*m.b26*m.b27 - 32*m.b6*m.b26*m.b28 - 32*m.b6*m.b27*
                       m.b28 - 416*m.b7*m.b8*m.b9 - 608*m.b7*m.b8*m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 
                       512*m.b7*m.b8*m.b13 - 480*m.b7*m.b8*m.b14 - 448*m.b7*m.b8*m.b15 - 448*m.b7*m.b8*m.b16 - 448*m.b7*
                       m.b8*m.b17 - 448*m.b7*m.b8*m.b18 - 448*m.b7*m.b8*m.b19 - 448*m.b7*m.b8*m.b20 - 448*m.b7*m.b8*
                       m.b21 - 448*m.b7*m.b8*m.b22 - 416*m.b7*m.b8*m.b23 - 352*m.b7*m.b8*m.b24 - 288*m.b7*m.b8*m.b25 - 
                       224*m.b7*m.b8*m.b26 - 160*m.b7*m.b8*m.b27 - 96*m.b7*m.b8*m.b28 - 32*m.b7*m.b8*m.b29 - 640*m.b7*
                       m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 576*m.b7*m.b9*m.b12 - 544*m.b7*m.b9*m.b13 - 512*m.b7*m.b9*
                       m.b14 - 480*m.b7*m.b9*m.b15 - 448*m.b7*m.b9*m.b16 - 448*m.b7*m.b9*m.b17 - 448*m.b7*m.b9*m.b18 - 
                       448*m.b7*m.b9*m.b19 - 448*m.b7*m.b9*m.b20 - 448*m.b7*m.b9*m.b21 - 416*m.b7*m.b9*m.b22 - 384*m.b7*
                       m.b9*m.b23 - 320*m.b7*m.b9*m.b24 - 256*m.b7*m.b9*m.b25 - 192*m.b7*m.b9*m.b26 - 128*m.b7*m.b9*
                       m.b27 - 64*m.b7*m.b9*m.b28 - 32*m.b7*m.b9*m.b29 - 640*m.b7*m.b10*m.b11 - 608*m.b7*m.b10*m.b12 - 
                       352*m.b7*m.b10*m.b13 - 544*m.b7*m.b10*m.b14 - 512*m.b7*m.b10*m.b15 - 480*m.b7*m.b10*m.b16 - 448*
                       m.b7*m.b10*m.b17 - 448*m.b7*m.b10*m.b18 - 448*m.b7*m.b10*m.b19 - 448*m.b7*m.b10*m.b20 - 416*m.b7*
                       m.b10*m.b21 - 384*m.b7*m.b10*m.b22 - 352*m.b7*m.b10*m.b23 - 288*m.b7*m.b10*m.b24 - 224*m.b7*m.b10
                       *m.b25 - 160*m.b7*m.b10*m.b26 - 96*m.b7*m.b10*m.b27 - 64*m.b7*m.b10*m.b28 - 32*m.b7*m.b10*m.b29
                        - 640*m.b7*m.b11*m.b12 - 608*m.b7*m.b11*m.b13 - 576*m.b7*m.b11*m.b14 - 320*m.b7*m.b11*m.b15 - 
                       512*m.b7*m.b11*m.b16 - 480*m.b7*m.b11*m.b17 - 448*m.b7*m.b11*m.b18 - 448*m.b7*m.b11*m.b19 - 416*
                       m.b7*m.b11*m.b20 - 384*m.b7*m.b11*m.b21 - 352*m.b7*m.b11*m.b22 - 320*m.b7*m.b11*m.b23 - 256*m.b7*
                       m.b11*m.b24 - 192*m.b7*m.b11*m.b25 - 128*m.b7*m.b11*m.b26 - 96*m.b7*m.b11*m.b27 - 64*m.b7*m.b11*
                       m.b28 - 32*m.b7*m.b11*m.b29 - 640*m.b7*m.b12*m.b13 - 608*m.b7*m.b12*m.b14 - 576*m.b7*m.b12*m.b15
                        - 544*m.b7*m.b12*m.b16 - 288*m.b7*m.b12*m.b17 - 480*m.b7*m.b12*m.b18 - 416*m.b7*m.b12*m.b19 - 
                       384*m.b7*m.b12*m.b20 - 352*m.b7*m.b12*m.b21 - 320*m.b7*m.b12*m.b22 - 288*m.b7*m.b12*m.b23 - 224*
                       m.b7*m.b12*m.b24 - 160*m.b7*m.b12*m.b25 - 128*m.b7*m.b12*m.b26 - 96*m.b7*m.b12*m.b27 - 64*m.b7*
                       m.b12*m.b28 - 32*m.b7*m.b12*m.b29 - 640*m.b7*m.b13*m.b14 - 608*m.b7*m.b13*m.b15 - 576*m.b7*m.b13*
                       m.b16 - 544*m.b7*m.b13*m.b17 - 480*m.b7*m.b13*m.b18 - 192*m.b7*m.b13*m.b19 - 352*m.b7*m.b13*m.b20
                        - 320*m.b7*m.b13*m.b21 - 288*m.b7*m.b13*m.b22 - 256*m.b7*m.b13*m.b23 - 192*m.b7*m.b13*m.b24 - 
                       160*m.b7*m.b13*m.b25 - 128*m.b7*m.b13*m.b26 - 96*m.b7*m.b13*m.b27 - 64*m.b7*m.b13*m.b28 - 32*m.b7
                       *m.b13*m.b29 - 640*m.b7*m.b14*m.b15 - 608*m.b7*m.b14*m.b16 - 544*m.b7*m.b14*m.b17 - 480*m.b7*
                       m.b14*m.b18 - 416*m.b7*m.b14*m.b19 - 352*m.b7*m.b14*m.b20 - 64*m.b7*m.b14*m.b21 - 256*m.b7*m.b14*
                       m.b22 - 224*m.b7*m.b14*m.b23 - 192*m.b7*m.b14*m.b24 - 160*m.b7*m.b14*m.b25 - 128*m.b7*m.b14*m.b26
                        - 96*m.b7*m.b14*m.b27 - 64*m.b7*m.b14*m.b28 - 32*m.b7*m.b14*m.b29 - 608*m.b7*m.b15*m.b16 - 544*
                       m.b7*m.b15*m.b17 - 480*m.b7*m.b15*m.b18 - 416*m.b7*m.b15*m.b19 - 352*m.b7*m.b15*m.b20 - 288*m.b7*
                       m.b15*m.b21 - 224*m.b7*m.b15*m.b22 - 192*m.b7*m.b15*m.b24 - 160*m.b7*m.b15*m.b25 - 128*m.b7*m.b15
                       *m.b26 - 96*m.b7*m.b15*m.b27 - 64*m.b7*m.b15*m.b28 - 32*m.b7*m.b15*m.b29 - 544*m.b7*m.b16*m.b17
                        - 480*m.b7*m.b16*m.b18 - 416*m.b7*m.b16*m.b19 - 352*m.b7*m.b16*m.b20 - 288*m.b7*m.b16*m.b21 - 
                       256*m.b7*m.b16*m.b22 - 224*m.b7*m.b16*m.b23 - 192*m.b7*m.b16*m.b24 - 128*m.b7*m.b16*m.b26 - 96*
                       m.b7*m.b16*m.b27 - 64*m.b7*m.b16*m.b28 - 32*m.b7*m.b16*m.b29 - 480*m.b7*m.b17*m.b18 - 416*m.b7*
                       m.b17*m.b19 - 352*m.b7*m.b17*m.b20 - 320*m.b7*m.b17*m.b21 - 288*m.b7*m.b17*m.b22 - 256*m.b7*m.b17
                       *m.b23 - 192*m.b7*m.b17*m.b24 - 160*m.b7*m.b17*m.b25 - 128*m.b7*m.b17*m.b26 - 64*m.b7*m.b17*m.b28
                        - 32*m.b7*m.b17*m.b29 - 416*m.b7*m.b18*m.b19 - 384*m.b7*m.b18*m.b20 - 352*m.b7*m.b18*m.b21 - 320
                       *m.b7*m.b18*m.b22 - 288*m.b7*m.b18*m.b23 - 192*m.b7*m.b18*m.b24 - 160*m.b7*m.b18*m.b25 - 128*m.b7
                       *m.b18*m.b26 - 96*m.b7*m.b18*m.b27 - 64*m.b7*m.b18*m.b28 - 416*m.b7*m.b19*m.b20 - 384*m.b7*m.b19*
                       m.b21 - 352*m.b7*m.b19*m.b22 - 320*m.b7*m.b19*m.b23 - 224*m.b7*m.b19*m.b24 - 160*m.b7*m.b19*m.b25
                        - 128*m.b7*m.b19*m.b26 - 96*m.b7*m.b19*m.b27 - 64*m.b7*m.b19*m.b28 - 32*m.b7*m.b19*m.b29 - 416*
                       m.b7*m.b20*m.b21 - 384*m.b7*m.b20*m.b22 - 352*m.b7*m.b20*m.b23 - 256*m.b7*m.b20*m.b24 - 160*m.b7*
                       m.b20*m.b25 - 128*m.b7*m.b20*m.b26 - 96*m.b7*m.b20*m.b27 - 64*m.b7*m.b20*m.b28 - 32*m.b7*m.b20*
                       m.b29 - 416*m.b7*m.b21*m.b22 - 384*m.b7*m.b21*m.b23 - 288*m.b7*m.b21*m.b24 - 192*m.b7*m.b21*m.b25
                        - 128*m.b7*m.b21*m.b26 - 96*m.b7*m.b21*m.b27 - 64*m.b7*m.b21*m.b28 - 32*m.b7*m.b21*m.b29 - 416*
                       m.b7*m.b22*m.b23 - 320*m.b7*m.b22*m.b24 - 224*m.b7*m.b22*m.b25 - 128*m.b7*m.b22*m.b26 - 96*m.b7*
                       m.b22*m.b27 - 64*m.b7*m.b22*m.b28 - 32*m.b7*m.b22*m.b29 - 352*m.b7*m.b23*m.b24 - 256*m.b7*m.b23*
                       m.b25 - 160*m.b7*m.b23*m.b26 - 96*m.b7*m.b23*m.b27 - 64*m.b7*m.b23*m.b28 - 32*m.b7*m.b23*m.b29 - 
                       288*m.b7*m.b24*m.b25 - 192*m.b7*m.b24*m.b26 - 96*m.b7*m.b24*m.b27 - 64*m.b7*m.b24*m.b28 - 32*m.b7
                       *m.b24*m.b29 - 224*m.b7*m.b25*m.b26 - 128*m.b7*m.b25*m.b27 - 64*m.b7*m.b25*m.b28 - 32*m.b7*m.b25*
                       m.b29 - 160*m.b7*m.b26*m.b27 - 64*m.b7*m.b26*m.b28 - 32*m.b7*m.b26*m.b29 - 96*m.b7*m.b27*m.b28 - 
                       32*m.b7*m.b27*m.b29 - 32*m.b7*m.b28*m.b29 - 480*m.b8*m.b9*m.b10 - 704*m.b8*m.b9*m.b11 - 672*m.b8*
                       m.b9*m.b12 - 640*m.b8*m.b9*m.b13 - 608*m.b8*m.b9*m.b14 - 576*m.b8*m.b9*m.b15 - 544*m.b8*m.b9*
                       m.b16 - 512*m.b8*m.b9*m.b17 - 512*m.b8*m.b9*m.b18 - 512*m.b8*m.b9*m.b19 - 512*m.b8*m.b9*m.b20 - 
                       512*m.b8*m.b9*m.b21 - 512*m.b8*m.b9*m.b22 - 480*m.b8*m.b9*m.b23 - 416*m.b8*m.b9*m.b24 - 352*m.b8*
                       m.b9*m.b25 - 288*m.b8*m.b9*m.b26 - 224*m.b8*m.b9*m.b27 - 160*m.b8*m.b9*m.b28 - 96*m.b8*m.b9*m.b29
                        - 32*m.b8*m.b9*m.b30 - 736*m.b8*m.b10*m.b11 - 448*m.b8*m.b10*m.b12 - 672*m.b8*m.b10*m.b13 - 640*
                       m.b8*m.b10*m.b14 - 608*m.b8*m.b10*m.b15 - 576*m.b8*m.b10*m.b16 - 544*m.b8*m.b10*m.b17 - 512*m.b8*
                       m.b10*m.b18 - 512*m.b8*m.b10*m.b19 - 512*m.b8*m.b10*m.b20 - 512*m.b8*m.b10*m.b21 - 480*m.b8*m.b10
                       *m.b22 - 448*m.b8*m.b10*m.b23 - 384*m.b8*m.b10*m.b24 - 320*m.b8*m.b10*m.b25 - 256*m.b8*m.b10*
                       m.b26 - 192*m.b8*m.b10*m.b27 - 128*m.b8*m.b10*m.b28 - 64*m.b8*m.b10*m.b29 - 32*m.b8*m.b10*m.b30
                        - 736*m.b8*m.b11*m.b12 - 704*m.b8*m.b11*m.b13 - 416*m.b8*m.b11*m.b14 - 640*m.b8*m.b11*m.b15 - 
                       608*m.b8*m.b11*m.b16 - 576*m.b8*m.b11*m.b17 - 544*m.b8*m.b11*m.b18 - 512*m.b8*m.b11*m.b19 - 512*
                       m.b8*m.b11*m.b20 - 480*m.b8*m.b11*m.b21 - 448*m.b8*m.b11*m.b22 - 416*m.b8*m.b11*m.b23 - 352*m.b8*
                       m.b11*m.b24 - 288*m.b8*m.b11*m.b25 - 224*m.b8*m.b11*m.b26 - 160*m.b8*m.b11*m.b27 - 96*m.b8*m.b11*
                       m.b28 - 64*m.b8*m.b11*m.b29 - 32*m.b8*m.b11*m.b30 - 736*m.b8*m.b12*m.b13 - 704*m.b8*m.b12*m.b14
                        - 672*m.b8*m.b12*m.b15 - 384*m.b8*m.b12*m.b16 - 608*m.b8*m.b12*m.b17 - 576*m.b8*m.b12*m.b18 - 
                       544*m.b8*m.b12*m.b19 - 480*m.b8*m.b12*m.b20 - 448*m.b8*m.b12*m.b21 - 416*m.b8*m.b12*m.b22 - 384*
                       m.b8*m.b12*m.b23 - 320*m.b8*m.b12*m.b24 - 256*m.b8*m.b12*m.b25 - 192*m.b8*m.b12*m.b26 - 128*m.b8*
                       m.b12*m.b27 - 96*m.b8*m.b12*m.b28 - 64*m.b8*m.b12*m.b29 - 32*m.b8*m.b12*m.b30 - 736*m.b8*m.b13*
                       m.b14 - 704*m.b8*m.b13*m.b15 - 672*m.b8*m.b13*m.b16 - 640*m.b8*m.b13*m.b17 - 352*m.b8*m.b13*m.b18
                        - 544*m.b8*m.b13*m.b19 - 480*m.b8*m.b13*m.b20 - 416*m.b8*m.b13*m.b21 - 384*m.b8*m.b13*m.b22 - 
                       352*m.b8*m.b13*m.b23 - 288*m.b8*m.b13*m.b24 - 224*m.b8*m.b13*m.b25 - 160*m.b8*m.b13*m.b26 - 128*
                       m.b8*m.b13*m.b27 - 96*m.b8*m.b13*m.b28 - 64*m.b8*m.b13*m.b29 - 32*m.b8*m.b13*m.b30 - 736*m.b8*
                       m.b14*m.b15 - 704*m.b8*m.b14*m.b16 - 672*m.b8*m.b14*m.b17 - 608*m.b8*m.b14*m.b18 - 544*m.b8*m.b14
                       *m.b19 - 224*m.b8*m.b14*m.b20 - 416*m.b8*m.b14*m.b21 - 352*m.b8*m.b14*m.b22 - 320*m.b8*m.b14*
                       m.b23 - 256*m.b8*m.b14*m.b24 - 192*m.b8*m.b14*m.b25 - 160*m.b8*m.b14*m.b26 - 128*m.b8*m.b14*m.b27
                        - 96*m.b8*m.b14*m.b28 - 64*m.b8*m.b14*m.b29 - 32*m.b8*m.b14*m.b30 - 736*m.b8*m.b15*m.b16 - 672*
                       m.b8*m.b15*m.b17 - 608*m.b8*m.b15*m.b18 - 544*m.b8*m.b15*m.b19 - 480*m.b8*m.b15*m.b20 - 416*m.b8*
                       m.b15*m.b21 - 96*m.b8*m.b15*m.b22 - 288*m.b8*m.b15*m.b23 - 224*m.b8*m.b15*m.b24 - 192*m.b8*m.b15*
                       m.b25 - 160*m.b8*m.b15*m.b26 - 128*m.b8*m.b15*m.b27 - 96*m.b8*m.b15*m.b28 - 64*m.b8*m.b15*m.b29
                        - 32*m.b8*m.b15*m.b30 - 672*m.b8*m.b16*m.b17 - 608*m.b8*m.b16*m.b18 - 544*m.b8*m.b16*m.b19 - 480
                       *m.b8*m.b16*m.b20 - 416*m.b8*m.b16*m.b21 - 352*m.b8*m.b16*m.b22 - 288*m.b8*m.b16*m.b23 - 192*m.b8
                       *m.b16*m.b25 - 160*m.b8*m.b16*m.b26 - 128*m.b8*m.b16*m.b27 - 96*m.b8*m.b16*m.b28 - 64*m.b8*m.b16*
                       m.b29 - 32*m.b8*m.b16*m.b30 - 608*m.b8*m.b17*m.b18 - 544*m.b8*m.b17*m.b19 - 480*m.b8*m.b17*m.b20
                        - 416*m.b8*m.b17*m.b21 - 352*m.b8*m.b17*m.b22 - 320*m.b8*m.b17*m.b23 - 224*m.b8*m.b17*m.b24 - 
                       192*m.b8*m.b17*m.b25 - 128*m.b8*m.b17*m.b27 - 96*m.b8*m.b17*m.b28 - 64*m.b8*m.b17*m.b29 - 32*m.b8
                       *m.b17*m.b30 - 544*m.b8*m.b18*m.b19 - 480*m.b8*m.b18*m.b20 - 416*m.b8*m.b18*m.b21 - 384*m.b8*
                       m.b18*m.b22 - 352*m.b8*m.b18*m.b23 - 256*m.b8*m.b18*m.b24 - 192*m.b8*m.b18*m.b25 - 160*m.b8*m.b18
                       *m.b26 - 128*m.b8*m.b18*m.b27 - 64*m.b8*m.b18*m.b29 - 32*m.b8*m.b18*m.b30 - 480*m.b8*m.b19*m.b20
                        - 448*m.b8*m.b19*m.b21 - 416*m.b8*m.b19*m.b22 - 384*m.b8*m.b19*m.b23 - 288*m.b8*m.b19*m.b24 - 
                       192*m.b8*m.b19*m.b25 - 160*m.b8*m.b19*m.b26 - 128*m.b8*m.b19*m.b27 - 96*m.b8*m.b19*m.b28 - 64*
                       m.b8*m.b19*m.b29 - 480*m.b8*m.b20*m.b21 - 448*m.b8*m.b20*m.b22 - 416*m.b8*m.b20*m.b23 - 320*m.b8*
                       m.b20*m.b24 - 224*m.b8*m.b20*m.b25 - 160*m.b8*m.b20*m.b26 - 128*m.b8*m.b20*m.b27 - 96*m.b8*m.b20*
                       m.b28 - 64*m.b8*m.b20*m.b29 - 32*m.b8*m.b20*m.b30 - 480*m.b8*m.b21*m.b22 - 448*m.b8*m.b21*m.b23
                        - 352*m.b8*m.b21*m.b24 - 256*m.b8*m.b21*m.b25 - 160*m.b8*m.b21*m.b26 - 128*m.b8*m.b21*m.b27 - 96
                       *m.b8*m.b21*m.b28 - 64*m.b8*m.b21*m.b29 - 32*m.b8*m.b21*m.b30 - 480*m.b8*m.b22*m.b23 - 384*m.b8*
                       m.b22*m.b24 - 288*m.b8*m.b22*m.b25 - 192*m.b8*m.b22*m.b26 - 128*m.b8*m.b22*m.b27 - 96*m.b8*m.b22*
                       m.b28 - 64*m.b8*m.b22*m.b29 - 32*m.b8*m.b22*m.b30 - 416*m.b8*m.b23*m.b24 - 320*m.b8*m.b23*m.b25
                        - 224*m.b8*m.b23*m.b26 - 128*m.b8*m.b23*m.b27 - 96*m.b8*m.b23*m.b28 - 64*m.b8*m.b23*m.b29 - 32*
                       m.b8*m.b23*m.b30 - 352*m.b8*m.b24*m.b25 - 256*m.b8*m.b24*m.b26 - 160*m.b8*m.b24*m.b27 - 96*m.b8*
                       m.b24*m.b28 - 64*m.b8*m.b24*m.b29 - 32*m.b8*m.b24*m.b30 - 288*m.b8*m.b25*m.b26 - 192*m.b8*m.b25*
                       m.b27 - 96*m.b8*m.b25*m.b28 - 64*m.b8*m.b25*m.b29 - 32*m.b8*m.b25*m.b30 - 224*m.b8*m.b26*m.b27 - 
                       128*m.b8*m.b26*m.b28 - 64*m.b8*m.b26*m.b29 - 32*m.b8*m.b26*m.b30 - 160*m.b8*m.b27*m.b28 - 64*m.b8
                       *m.b27*m.b29 - 32*m.b8*m.b27*m.b30 - 96*m.b8*m.b28*m.b29 - 32*m.b8*m.b28*m.b30 - 32*m.b8*m.b29*
                       m.b30 - 512*m.b9*m.b10*m.b11 - 736*m.b9*m.b10*m.b12 - 704*m.b9*m.b10*m.b13 - 672*m.b9*m.b10*m.b14
                        - 640*m.b9*m.b10*m.b15 - 640*m.b9*m.b10*m.b16 - 640*m.b9*m.b10*m.b17 - 608*m.b9*m.b10*m.b18 - 
                       576*m.b9*m.b10*m.b19 - 576*m.b9*m.b10*m.b20 - 576*m.b9*m.b10*m.b21 - 544*m.b9*m.b10*m.b22 - 480*
                       m.b9*m.b10*m.b23 - 416*m.b9*m.b10*m.b24 - 352*m.b9*m.b10*m.b25 - 288*m.b9*m.b10*m.b26 - 224*m.b9*
                       m.b10*m.b27 - 160*m.b9*m.b10*m.b28 - 96*m.b9*m.b10*m.b29 - 32*m.b9*m.b10*m.b30 - 768*m.b9*m.b11*
                       m.b12 - 480*m.b9*m.b11*m.b13 - 704*m.b9*m.b11*m.b14 - 704*m.b9*m.b11*m.b15 - 672*m.b9*m.b11*m.b16
                        - 672*m.b9*m.b11*m.b17 - 640*m.b9*m.b11*m.b18 - 608*m.b9*m.b11*m.b19 - 576*m.b9*m.b11*m.b20 - 
                       544*m.b9*m.b11*m.b21 - 512*m.b9*m.b11*m.b22 - 448*m.b9*m.b11*m.b23 - 384*m.b9*m.b11*m.b24 - 320*
                       m.b9*m.b11*m.b25 - 256*m.b9*m.b11*m.b26 - 192*m.b9*m.b11*m.b27 - 128*m.b9*m.b11*m.b28 - 64*m.b9*
                       m.b11*m.b29 - 32*m.b9*m.b11*m.b30 - 768*m.b9*m.b12*m.b13 - 768*m.b9*m.b12*m.b14 - 480*m.b9*m.b12*
                       m.b15 - 704*m.b9*m.b12*m.b16 - 704*m.b9*m.b12*m.b17 - 672*m.b9*m.b12*m.b18 - 640*m.b9*m.b12*m.b19
                        - 576*m.b9*m.b12*m.b20 - 512*m.b9*m.b12*m.b21 - 480*m.b9*m.b12*m.b22 - 416*m.b9*m.b12*m.b23 - 
                       352*m.b9*m.b12*m.b24 - 288*m.b9*m.b12*m.b25 - 224*m.b9*m.b12*m.b26 - 160*m.b9*m.b12*m.b27 - 96*
                       m.b9*m.b12*m.b28 - 64*m.b9*m.b12*m.b29 - 32*m.b9*m.b12*m.b30 - 800*m.b9*m.b13*m.b14 - 768*m.b9*
                       m.b13*m.b15 - 736*m.b9*m.b13*m.b16 - 448*m.b9*m.b13*m.b17 - 704*m.b9*m.b13*m.b18 - 640*m.b9*m.b13
                       *m.b19 - 576*m.b9*m.b13*m.b20 - 512*m.b9*m.b13*m.b21 - 448*m.b9*m.b13*m.b22 - 384*m.b9*m.b13*
                       m.b23 - 320*m.b9*m.b13*m.b24 - 256*m.b9*m.b13*m.b25 - 192*m.b9*m.b13*m.b26 - 128*m.b9*m.b13*m.b27
                        - 96*m.b9*m.b13*m.b28 - 64*m.b9*m.b13*m.b29 - 32*m.b9*m.b13*m.b30 - 800*m.b9*m.b14*m.b15 - 768*
                       m.b9*m.b14*m.b16 - 768*m.b9*m.b14*m.b17 - 704*m.b9*m.b14*m.b18 - 352*m.b9*m.b14*m.b19 - 576*m.b9*
                       m.b14*m.b20 - 512*m.b9*m.b14*m.b21 - 448*m.b9*m.b14*m.b22 - 352*m.b9*m.b14*m.b23 - 288*m.b9*m.b14
                       *m.b24 - 224*m.b9*m.b14*m.b25 - 160*m.b9*m.b14*m.b26 - 128*m.b9*m.b14*m.b27 - 96*m.b9*m.b14*m.b28
                        - 64*m.b9*m.b14*m.b29 - 32*m.b9*m.b14*m.b30 - 800*m.b9*m.b15*m.b16 - 768*m.b9*m.b15*m.b17 - 704*
                       m.b9*m.b15*m.b18 - 640*m.b9*m.b15*m.b19 - 576*m.b9*m.b15*m.b20 - 224*m.b9*m.b15*m.b21 - 448*m.b9*
                       m.b15*m.b22 - 352*m.b9*m.b15*m.b23 - 256*m.b9*m.b15*m.b24 - 192*m.b9*m.b15*m.b25 - 160*m.b9*m.b15
                       *m.b26 - 128*m.b9*m.b15*m.b27 - 96*m.b9*m.b15*m.b28 - 64*m.b9*m.b15*m.b29 - 32*m.b9*m.b15*m.b30
                        - 768*m.b9*m.b16*m.b17 - 704*m.b9*m.b16*m.b18 - 640*m.b9*m.b16*m.b19 - 576*m.b9*m.b16*m.b20 - 
                       512*m.b9*m.b16*m.b21 - 448*m.b9*m.b16*m.b22 - 96*m.b9*m.b16*m.b23 - 224*m.b9*m.b16*m.b24 - 192*
                       m.b9*m.b16*m.b25 - 160*m.b9*m.b16*m.b26 - 128*m.b9*m.b16*m.b27 - 96*m.b9*m.b16*m.b28 - 64*m.b9*
                       m.b16*m.b29 - 32*m.b9*m.b16*m.b30 - 704*m.b9*m.b17*m.b18 - 640*m.b9*m.b17*m.b19 - 576*m.b9*m.b17*
                       m.b20 - 512*m.b9*m.b17*m.b21 - 448*m.b9*m.b17*m.b22 - 352*m.b9*m.b17*m.b23 - 256*m.b9*m.b17*m.b24
                        - 160*m.b9*m.b17*m.b26 - 128*m.b9*m.b17*m.b27 - 96*m.b9*m.b17*m.b28 - 64*m.b9*m.b17*m.b29 - 32*
                       m.b9*m.b17*m.b30 - 640*m.b9*m.b18*m.b19 - 576*m.b9*m.b18*m.b20 - 512*m.b9*m.b18*m.b21 - 448*m.b9*
                       m.b18*m.b22 - 384*m.b9*m.b18*m.b23 - 288*m.b9*m.b18*m.b24 - 192*m.b9*m.b18*m.b25 - 160*m.b9*m.b18
                       *m.b26 - 96*m.b9*m.b18*m.b28 - 64*m.b9*m.b18*m.b29 - 32*m.b9*m.b18*m.b30 - 576*m.b9*m.b19*m.b20
                        - 512*m.b9*m.b19*m.b21 - 480*m.b9*m.b19*m.b22 - 416*m.b9*m.b19*m.b23 - 320*m.b9*m.b19*m.b24 - 
                       224*m.b9*m.b19*m.b25 - 160*m.b9*m.b19*m.b26 - 128*m.b9*m.b19*m.b27 - 96*m.b9*m.b19*m.b28 - 32*
                       m.b9*m.b19*m.b30 - 544*m.b9*m.b20*m.b21 - 512*m.b9*m.b20*m.b22 - 448*m.b9*m.b20*m.b23 - 352*m.b9*
                       m.b20*m.b24 - 256*m.b9*m.b20*m.b25 - 160*m.b9*m.b20*m.b26 - 128*m.b9*m.b20*m.b27 - 96*m.b9*m.b20*
                       m.b28 - 64*m.b9*m.b20*m.b29 - 32*m.b9*m.b20*m.b30 - 544*m.b9*m.b21*m.b22 - 480*m.b9*m.b21*m.b23
                        - 384*m.b9*m.b21*m.b24 - 288*m.b9*m.b21*m.b25 - 192*m.b9*m.b21*m.b26 - 128*m.b9*m.b21*m.b27 - 96
                       *m.b9*m.b21*m.b28 - 64*m.b9*m.b21*m.b29 - 32*m.b9*m.b21*m.b30 - 512*m.b9*m.b22*m.b23 - 416*m.b9*
                       m.b22*m.b24 - 320*m.b9*m.b22*m.b25 - 224*m.b9*m.b22*m.b26 - 128*m.b9*m.b22*m.b27 - 96*m.b9*m.b22*
                       m.b28 - 64*m.b9*m.b22*m.b29 - 32*m.b9*m.b22*m.b30 - 448*m.b9*m.b23*m.b24 - 352*m.b9*m.b23*m.b25
                        - 256*m.b9*m.b23*m.b26 - 160*m.b9*m.b23*m.b27 - 96*m.b9*m.b23*m.b28 - 64*m.b9*m.b23*m.b29 - 32*
                       m.b9*m.b23*m.b30 - 384*m.b9*m.b24*m.b25 - 288*m.b9*m.b24*m.b26 - 192*m.b9*m.b24*m.b27 - 96*m.b9*
                       m.b24*m.b28 - 64*m.b9*m.b24*m.b29 - 32*m.b9*m.b24*m.b30 - 320*m.b9*m.b25*m.b26 - 224*m.b9*m.b25*
                       m.b27 - 128*m.b9*m.b25*m.b28 - 64*m.b9*m.b25*m.b29 - 32*m.b9*m.b25*m.b30 - 256*m.b9*m.b26*m.b27
                        - 160*m.b9*m.b26*m.b28 - 64*m.b9*m.b26*m.b29 - 32*m.b9*m.b26*m.b30 - 192*m.b9*m.b27*m.b28 - 96*
                       m.b9*m.b27*m.b29 - 32*m.b9*m.b27*m.b30 - 128*m.b9*m.b28*m.b29 - 32*m.b9*m.b28*m.b30 - 64*m.b9*
                       m.b29*m.b30 - 512*m.b10*m.b11*m.b12 - 768*m.b10*m.b11*m.b13 - 736*m.b10*m.b11*m.b14 - 704*m.b10*
                       m.b11*m.b15 - 672*m.b10*m.b11*m.b16 - 704*m.b10*m.b11*m.b17 - 736*m.b10*m.b11*m.b18 - 704*m.b10*
                       m.b11*m.b19 - 672*m.b10*m.b11*m.b20 - 608*m.b10*m.b11*m.b21 - 544*m.b10*m.b11*m.b22 - 480*m.b10*
                       m.b11*m.b23 - 416*m.b10*m.b11*m.b24 - 352*m.b10*m.b11*m.b25 - 288*m.b10*m.b11*m.b26 - 224*m.b10*
                       m.b11*m.b27 - 160*m.b10*m.b11*m.b28 - 96*m.b10*m.b11*m.b29 - 32*m.b10*m.b11*m.b30 - 768*m.b10*
                       m.b12*m.b13 - 512*m.b10*m.b12*m.b14 - 736*m.b10*m.b12*m.b15 - 768*m.b10*m.b12*m.b16 - 736*m.b10*
                       m.b12*m.b17 - 768*m.b10*m.b12*m.b18 - 736*m.b10*m.b12*m.b19 - 672*m.b10*m.b12*m.b20 - 608*m.b10*
                       m.b12*m.b21 - 512*m.b10*m.b12*m.b22 - 448*m.b10*m.b12*m.b23 - 384*m.b10*m.b12*m.b24 - 320*m.b10*
                       m.b12*m.b25 - 256*m.b10*m.b12*m.b26 - 192*m.b10*m.b12*m.b27 - 128*m.b10*m.b12*m.b28 - 64*m.b10*
                       m.b12*m.b29 - 32*m.b10*m.b12*m.b30 - 768*m.b10*m.b13*m.b14 - 832*m.b10*m.b13*m.b15 - 544*m.b10*
                       m.b13*m.b16 - 768*m.b10*m.b13*m.b17 - 800*m.b10*m.b13*m.b18 - 736*m.b10*m.b13*m.b19 - 672*m.b10*
                       m.b13*m.b20 - 608*m.b10*m.b13*m.b21 - 512*m.b10*m.b13*m.b22 - 416*m.b10*m.b13*m.b23 - 352*m.b10*
                       m.b13*m.b24 - 288*m.b10*m.b13*m.b25 - 224*m.b10*m.b13*m.b26 - 160*m.b10*m.b13*m.b27 - 96*m.b10*
                       m.b13*m.b28 - 64*m.b10*m.b13*m.b29 - 32*m.b10*m.b13*m.b30 - 832*m.b10*m.b14*m.b15 - 832*m.b10*
                       m.b14*m.b16 - 800*m.b10*m.b14*m.b17 - 480*m.b10*m.b14*m.b18 - 736*m.b10*m.b14*m.b19 - 672*m.b10*
                       m.b14*m.b20 - 608*m.b10*m.b14*m.b21 - 512*m.b10*m.b14*m.b22 - 416*m.b10*m.b14*m.b23 - 320*m.b10*
                       m.b14*m.b24 - 256*m.b10*m.b14*m.b25 - 192*m.b10*m.b14*m.b26 - 128*m.b10*m.b14*m.b27 - 96*m.b10*
                       m.b14*m.b28 - 64*m.b10*m.b14*m.b29 - 32*m.b10*m.b14*m.b30 - 832*m.b10*m.b15*m.b16 - 800*m.b10*
                       m.b15*m.b17 - 800*m.b10*m.b15*m.b18 - 736*m.b10*m.b15*m.b19 - 352*m.b10*m.b15*m.b20 - 608*m.b10*
                       m.b15*m.b21 - 512*m.b10*m.b15*m.b22 - 416*m.b10*m.b15*m.b23 - 288*m.b10*m.b15*m.b24 - 224*m.b10*
                       m.b15*m.b25 - 160*m.b10*m.b15*m.b26 - 128*m.b10*m.b15*m.b27 - 96*m.b10*m.b15*m.b28 - 64*m.b10*
                       m.b15*m.b29 - 32*m.b10*m.b15*m.b30 - 800*m.b10*m.b16*m.b17 - 800*m.b10*m.b16*m.b18 - 736*m.b10*
                       m.b16*m.b19 - 672*m.b10*m.b16*m.b20 - 608*m.b10*m.b16*m.b21 - 224*m.b10*m.b16*m.b22 - 416*m.b10*
                       m.b16*m.b23 - 288*m.b10*m.b16*m.b24 - 192*m.b10*m.b16*m.b25 - 160*m.b10*m.b16*m.b26 - 128*m.b10*
                       m.b16*m.b27 - 96*m.b10*m.b16*m.b28 - 64*m.b10*m.b16*m.b29 - 32*m.b10*m.b16*m.b30 - 800*m.b10*
                       m.b17*m.b18 - 736*m.b10*m.b17*m.b19 - 672*m.b10*m.b17*m.b20 - 608*m.b10*m.b17*m.b21 - 512*m.b10*
                       m.b17*m.b22 - 416*m.b10*m.b17*m.b23 - 64*m.b10*m.b17*m.b24 - 192*m.b10*m.b17*m.b25 - 160*m.b10*
                       m.b17*m.b26 - 128*m.b10*m.b17*m.b27 - 96*m.b10*m.b17*m.b28 - 64*m.b10*m.b17*m.b29 - 32*m.b10*
                       m.b17*m.b30 - 736*m.b10*m.b18*m.b19 - 672*m.b10*m.b18*m.b20 - 608*m.b10*m.b18*m.b21 - 512*m.b10*
                       m.b18*m.b22 - 416*m.b10*m.b18*m.b23 - 320*m.b10*m.b18*m.b24 - 224*m.b10*m.b18*m.b25 - 128*m.b10*
                       m.b18*m.b27 - 96*m.b10*m.b18*m.b28 - 64*m.b10*m.b18*m.b29 - 32*m.b10*m.b18*m.b30 - 672*m.b10*
                       m.b19*m.b20 - 608*m.b10*m.b19*m.b21 - 512*m.b10*m.b19*m.b22 - 448*m.b10*m.b19*m.b23 - 352*m.b10*
                       m.b19*m.b24 - 256*m.b10*m.b19*m.b25 - 160*m.b10*m.b19*m.b26 - 128*m.b10*m.b19*m.b27 - 64*m.b10*
                       m.b19*m.b29 - 32*m.b10*m.b19*m.b30 - 608*m.b10*m.b20*m.b21 - 544*m.b10*m.b20*m.b22 - 480*m.b10*
                       m.b20*m.b23 - 384*m.b10*m.b20*m.b24 - 288*m.b10*m.b20*m.b25 - 192*m.b10*m.b20*m.b26 - 128*m.b10*
                       m.b20*m.b27 - 96*m.b10*m.b20*m.b28 - 64*m.b10*m.b20*m.b29 - 576*m.b10*m.b21*m.b22 - 512*m.b10*
                       m.b21*m.b23 - 416*m.b10*m.b21*m.b24 - 320*m.b10*m.b21*m.b25 - 224*m.b10*m.b21*m.b26 - 128*m.b10*
                       m.b21*m.b27 - 96*m.b10*m.b21*m.b28 - 64*m.b10*m.b21*m.b29 - 32*m.b10*m.b21*m.b30 - 512*m.b10*
                       m.b22*m.b23 - 448*m.b10*m.b22*m.b24 - 352*m.b10*m.b22*m.b25 - 256*m.b10*m.b22*m.b26 - 160*m.b10*
                       m.b22*m.b27 - 96*m.b10*m.b22*m.b28 - 64*m.b10*m.b22*m.b29 - 32*m.b10*m.b22*m.b30 - 448*m.b10*
                       m.b23*m.b24 - 384*m.b10*m.b23*m.b25 - 288*m.b10*m.b23*m.b26 - 192*m.b10*m.b23*m.b27 - 96*m.b10*
                       m.b23*m.b28 - 64*m.b10*m.b23*m.b29 - 32*m.b10*m.b23*m.b30 - 384*m.b10*m.b24*m.b25 - 320*m.b10*
                       m.b24*m.b26 - 224*m.b10*m.b24*m.b27 - 128*m.b10*m.b24*m.b28 - 64*m.b10*m.b24*m.b29 - 32*m.b10*
                       m.b24*m.b30 - 320*m.b10*m.b25*m.b26 - 256*m.b10*m.b25*m.b27 - 160*m.b10*m.b25*m.b28 - 64*m.b10*
                       m.b25*m.b29 - 32*m.b10*m.b25*m.b30 - 256*m.b10*m.b26*m.b27 - 192*m.b10*m.b26*m.b28 - 96*m.b10*
                       m.b26*m.b29 - 32*m.b10*m.b26*m.b30 - 192*m.b10*m.b27*m.b28 - 128*m.b10*m.b27*m.b29 - 32*m.b10*
                       m.b27*m.b30 - 128*m.b10*m.b28*m.b29 - 64*m.b10*m.b28*m.b30 - 64*m.b10*m.b29*m.b30 - 512*m.b11*
                       m.b12*m.b13 - 768*m.b11*m.b12*m.b14 - 768*m.b11*m.b12*m.b15 - 736*m.b11*m.b12*m.b16 - 704*m.b11*
                       m.b12*m.b17 - 768*m.b11*m.b12*m.b18 - 832*m.b11*m.b12*m.b19 - 768*m.b11*m.b12*m.b20 - 672*m.b11*
                       m.b12*m.b21 - 576*m.b11*m.b12*m.b22 - 480*m.b11*m.b12*m.b23 - 416*m.b11*m.b12*m.b24 - 352*m.b11*
                       m.b12*m.b25 - 288*m.b11*m.b12*m.b26 - 224*m.b11*m.b12*m.b27 - 160*m.b11*m.b12*m.b28 - 96*m.b11*
                       m.b12*m.b29 - 32*m.b11*m.b12*m.b30 - 768*m.b11*m.b13*m.b14 - 512*m.b11*m.b13*m.b15 - 768*m.b11*
                       m.b13*m.b16 - 832*m.b11*m.b13*m.b17 - 800*m.b11*m.b13*m.b18 - 832*m.b11*m.b13*m.b19 - 768*m.b11*
                       m.b13*m.b20 - 672*m.b11*m.b13*m.b21 - 576*m.b11*m.b13*m.b22 - 480*m.b11*m.b13*m.b23 - 384*m.b11*
                       m.b13*m.b24 - 320*m.b11*m.b13*m.b25 - 256*m.b11*m.b13*m.b26 - 192*m.b11*m.b13*m.b27 - 128*m.b11*
                       m.b13*m.b28 - 64*m.b11*m.b13*m.b29 - 32*m.b11*m.b13*m.b30 - 768*m.b11*m.b14*m.b15 - 864*m.b11*
                       m.b14*m.b16 - 608*m.b11*m.b14*m.b17 - 800*m.b11*m.b14*m.b18 - 832*m.b11*m.b14*m.b19 - 768*m.b11*
                       m.b14*m.b20 - 672*m.b11*m.b14*m.b21 - 576*m.b11*m.b14*m.b22 - 480*m.b11*m.b14*m.b23 - 352*m.b11*
                       m.b14*m.b24 - 288*m.b11*m.b14*m.b25 - 224*m.b11*m.b14*m.b26 - 160*m.b11*m.b14*m.b27 - 96*m.b11*
                       m.b14*m.b28 - 64*m.b11*m.b14*m.b29 - 32*m.b11*m.b14*m.b30 - 864*m.b11*m.b15*m.b16 - 864*m.b11*
                       m.b15*m.b17 - 800*m.b11*m.b15*m.b18 - 480*m.b11*m.b15*m.b19 - 768*m.b11*m.b15*m.b20 - 672*m.b11*
                       m.b15*m.b21 - 576*m.b11*m.b15*m.b22 - 480*m.b11*m.b15*m.b23 - 352*m.b11*m.b15*m.b24 - 256*m.b11*
                       m.b15*m.b25 - 192*m.b11*m.b15*m.b26 - 128*m.b11*m.b15*m.b27 - 96*m.b11*m.b15*m.b28 - 64*m.b11*
                       m.b15*m.b29 - 32*m.b11*m.b15*m.b30 - 800*m.b11*m.b16*m.b17 - 800*m.b11*m.b16*m.b18 - 832*m.b11*
                       m.b16*m.b19 - 768*m.b11*m.b16*m.b20 - 352*m.b11*m.b16*m.b21 - 576*m.b11*m.b16*m.b22 - 480*m.b11*
                       m.b16*m.b23 - 352*m.b11*m.b16*m.b24 - 224*m.b11*m.b16*m.b25 - 160*m.b11*m.b16*m.b26 - 128*m.b11*
                       m.b16*m.b27 - 96*m.b11*m.b16*m.b28 - 64*m.b11*m.b16*m.b29 - 32*m.b11*m.b16*m.b30 - 800*m.b11*
                       m.b17*m.b18 - 832*m.b11*m.b17*m.b19 - 768*m.b11*m.b17*m.b20 - 672*m.b11*m.b17*m.b21 - 576*m.b11*
                       m.b17*m.b22 - 224*m.b11*m.b17*m.b23 - 352*m.b11*m.b17*m.b24 - 224*m.b11*m.b17*m.b25 - 160*m.b11*
                       m.b17*m.b26 - 128*m.b11*m.b17*m.b27 - 96*m.b11*m.b17*m.b28 - 64*m.b11*m.b17*m.b29 - 32*m.b11*
                       m.b17*m.b30 - 832*m.b11*m.b18*m.b19 - 768*m.b11*m.b18*m.b20 - 672*m.b11*m.b18*m.b21 - 576*m.b11*
                       m.b18*m.b22 - 480*m.b11*m.b18*m.b23 - 352*m.b11*m.b18*m.b24 - 64*m.b11*m.b18*m.b25 - 160*m.b11*
                       m.b18*m.b26 - 128*m.b11*m.b18*m.b27 - 96*m.b11*m.b18*m.b28 - 64*m.b11*m.b18*m.b29 - 32*m.b11*
                       m.b18*m.b30 - 768*m.b11*m.b19*m.b20 - 672*m.b11*m.b19*m.b21 - 576*m.b11*m.b19*m.b22 - 480*m.b11*
                       m.b19*m.b23 - 384*m.b11*m.b19*m.b24 - 288*m.b11*m.b19*m.b25 - 192*m.b11*m.b19*m.b26 - 96*m.b11*
                       m.b19*m.b28 - 64*m.b11*m.b19*m.b29 - 32*m.b11*m.b19*m.b30 - 672*m.b11*m.b20*m.b21 - 576*m.b11*
                       m.b20*m.b22 - 512*m.b11*m.b20*m.b23 - 416*m.b11*m.b20*m.b24 - 320*m.b11*m.b20*m.b25 - 224*m.b11*
                       m.b20*m.b26 - 128*m.b11*m.b20*m.b27 - 96*m.b11*m.b20*m.b28 - 32*m.b11*m.b20*m.b30 - 576*m.b11*
                       m.b21*m.b22 - 512*m.b11*m.b21*m.b23 - 448*m.b11*m.b21*m.b24 - 352*m.b11*m.b21*m.b25 - 256*m.b11*
                       m.b21*m.b26 - 160*m.b11*m.b21*m.b27 - 96*m.b11*m.b21*m.b28 - 64*m.b11*m.b21*m.b29 - 32*m.b11*
                       m.b21*m.b30 - 512*m.b11*m.b22*m.b23 - 448*m.b11*m.b22*m.b24 - 384*m.b11*m.b22*m.b25 - 288*m.b11*
                       m.b22*m.b26 - 192*m.b11*m.b22*m.b27 - 96*m.b11*m.b22*m.b28 - 64*m.b11*m.b22*m.b29 - 32*m.b11*
                       m.b22*m.b30 - 448*m.b11*m.b23*m.b24 - 384*m.b11*m.b23*m.b25 - 320*m.b11*m.b23*m.b26 - 224*m.b11*
                       m.b23*m.b27 - 128*m.b11*m.b23*m.b28 - 64*m.b11*m.b23*m.b29 - 32*m.b11*m.b23*m.b30 - 384*m.b11*
                       m.b24*m.b25 - 320*m.b11*m.b24*m.b26 - 256*m.b11*m.b24*m.b27 - 160*m.b11*m.b24*m.b28 - 64*m.b11*
                       m.b24*m.b29 - 32*m.b11*m.b24*m.b30 - 320*m.b11*m.b25*m.b26 - 256*m.b11*m.b25*m.b27 - 192*m.b11*
                       m.b25*m.b28 - 96*m.b11*m.b25*m.b29 - 32*m.b11*m.b25*m.b30 - 256*m.b11*m.b26*m.b27 - 192*m.b11*
                       m.b26*m.b28 - 128*m.b11*m.b26*m.b29 - 32*m.b11*m.b26*m.b30 - 192*m.b11*m.b27*m.b28 - 128*m.b11*
                       m.b27*m.b29 - 64*m.b11*m.b27*m.b30 - 128*m.b11*m.b28*m.b29 - 64*m.b11*m.b28*m.b30 - 64*m.b11*
                       m.b29*m.b30 - 512*m.b12*m.b13*m.b14 - 768*m.b12*m.b13*m.b15 - 768*m.b12*m.b13*m.b16 - 768*m.b12*
                       m.b13*m.b17 - 736*m.b12*m.b13*m.b18 - 800*m.b12*m.b13*m.b19 - 832*m.b12*m.b13*m.b20 - 736*m.b12*
                       m.b13*m.b21 - 640*m.b12*m.b13*m.b22 - 544*m.b12*m.b13*m.b23 - 416*m.b12*m.b13*m.b24 - 352*m.b12*
                       m.b13*m.b25 - 288*m.b12*m.b13*m.b26 - 224*m.b12*m.b13*m.b27 - 160*m.b12*m.b13*m.b28 - 96*m.b12*
                       m.b13*m.b29 - 32*m.b12*m.b13*m.b30 - 768*m.b12*m.b14*m.b15 - 512*m.b12*m.b14*m.b16 - 800*m.b12*
                       m.b14*m.b17 - 864*m.b12*m.b14*m.b18 - 800*m.b12*m.b14*m.b19 - 832*m.b12*m.b14*m.b20 - 736*m.b12*
                       m.b14*m.b21 - 640*m.b12*m.b14*m.b22 - 544*m.b12*m.b14*m.b23 - 416*m.b12*m.b14*m.b24 - 320*m.b12*
                       m.b14*m.b25 - 256*m.b12*m.b14*m.b26 - 192*m.b12*m.b14*m.b27 - 128*m.b12*m.b14*m.b28 - 64*m.b12*
                       m.b14*m.b29 - 32*m.b12*m.b14*m.b30 - 768*m.b12*m.b15*m.b16 - 864*m.b12*m.b15*m.b17 - 608*m.b12*
                       m.b15*m.b18 - 800*m.b12*m.b15*m.b19 - 832*m.b12*m.b15*m.b20 - 736*m.b12*m.b15*m.b21 - 640*m.b12*
                       m.b15*m.b22 - 544*m.b12*m.b15*m.b23 - 416*m.b12*m.b15*m.b24 - 288*m.b12*m.b15*m.b25 - 224*m.b12*
                       m.b15*m.b26 - 160*m.b12*m.b15*m.b27 - 96*m.b12*m.b15*m.b28 - 64*m.b12*m.b15*m.b29 - 32*m.b12*
                       m.b15*m.b30 - 832*m.b12*m.b16*m.b17 - 864*m.b12*m.b16*m.b18 - 800*m.b12*m.b16*m.b19 - 480*m.b12*
                       m.b16*m.b20 - 736*m.b12*m.b16*m.b21 - 640*m.b12*m.b16*m.b22 - 544*m.b12*m.b16*m.b23 - 416*m.b12*
                       m.b16*m.b24 - 288*m.b12*m.b16*m.b25 - 192*m.b12*m.b16*m.b26 - 128*m.b12*m.b16*m.b27 - 96*m.b12*
                       m.b16*m.b28 - 64*m.b12*m.b16*m.b29 - 32*m.b12*m.b16*m.b30 - 768*m.b12*m.b17*m.b18 - 800*m.b12*
                       m.b17*m.b19 - 832*m.b12*m.b17*m.b20 - 736*m.b12*m.b17*m.b21 - 352*m.b12*m.b17*m.b22 - 544*m.b12*
                       m.b17*m.b23 - 416*m.b12*m.b17*m.b24 - 288*m.b12*m.b17*m.b25 - 160*m.b12*m.b17*m.b26 - 128*m.b12*
                       m.b17*m.b27 - 96*m.b12*m.b17*m.b28 - 64*m.b12*m.b17*m.b29 - 32*m.b12*m.b17*m.b30 - 800*m.b12*
                       m.b18*m.b19 - 832*m.b12*m.b18*m.b20 - 736*m.b12*m.b18*m.b21 - 640*m.b12*m.b18*m.b22 - 544*m.b12*
                       m.b18*m.b23 - 192*m.b12*m.b18*m.b24 - 288*m.b12*m.b18*m.b25 - 192*m.b12*m.b18*m.b26 - 128*m.b12*
                       m.b18*m.b27 - 96*m.b12*m.b18*m.b28 - 64*m.b12*m.b18*m.b29 - 32*m.b12*m.b18*m.b30 - 832*m.b12*
                       m.b19*m.b20 - 736*m.b12*m.b19*m.b21 - 640*m.b12*m.b19*m.b22 - 544*m.b12*m.b19*m.b23 - 416*m.b12*
                       m.b19*m.b24 - 320*m.b12*m.b19*m.b25 - 64*m.b12*m.b19*m.b26 - 128*m.b12*m.b19*m.b27 - 96*m.b12*
                       m.b19*m.b28 - 64*m.b12*m.b19*m.b29 - 32*m.b12*m.b19*m.b30 - 704*m.b12*m.b20*m.b21 - 608*m.b12*
                       m.b20*m.b22 - 512*m.b12*m.b20*m.b23 - 448*m.b12*m.b20*m.b24 - 352*m.b12*m.b20*m.b25 - 256*m.b12*
                       m.b20*m.b26 - 160*m.b12*m.b20*m.b27 - 64*m.b12*m.b20*m.b29 - 32*m.b12*m.b20*m.b30 - 576*m.b12*
                       m.b21*m.b22 - 512*m.b12*m.b21*m.b23 - 448*m.b12*m.b21*m.b24 - 384*m.b12*m.b21*m.b25 - 288*m.b12*
                       m.b21*m.b26 - 192*m.b12*m.b21*m.b27 - 96*m.b12*m.b21*m.b28 - 64*m.b12*m.b21*m.b29 - 512*m.b12*
                       m.b22*m.b23 - 448*m.b12*m.b22*m.b24 - 384*m.b12*m.b22*m.b25 - 320*m.b12*m.b22*m.b26 - 224*m.b12*
                       m.b22*m.b27 - 128*m.b12*m.b22*m.b28 - 64*m.b12*m.b22*m.b29 - 32*m.b12*m.b22*m.b30 - 448*m.b12*
                       m.b23*m.b24 - 384*m.b12*m.b23*m.b25 - 320*m.b12*m.b23*m.b26 - 256*m.b12*m.b23*m.b27 - 160*m.b12*
                       m.b23*m.b28 - 64*m.b12*m.b23*m.b29 - 32*m.b12*m.b23*m.b30 - 384*m.b12*m.b24*m.b25 - 320*m.b12*
                       m.b24*m.b26 - 256*m.b12*m.b24*m.b27 - 192*m.b12*m.b24*m.b28 - 96*m.b12*m.b24*m.b29 - 32*m.b12*
                       m.b24*m.b30 - 320*m.b12*m.b25*m.b26 - 256*m.b12*m.b25*m.b27 - 192*m.b12*m.b25*m.b28 - 128*m.b12*
                       m.b25*m.b29 - 32*m.b12*m.b25*m.b30 - 256*m.b12*m.b26*m.b27 - 192*m.b12*m.b26*m.b28 - 128*m.b12*
                       m.b26*m.b29 - 64*m.b12*m.b26*m.b30 - 192*m.b12*m.b27*m.b28 - 128*m.b12*m.b27*m.b29 - 64*m.b12*
                       m.b27*m.b30 - 128*m.b12*m.b28*m.b29 - 64*m.b12*m.b28*m.b30 - 64*m.b12*m.b29*m.b30 - 512*m.b13*
                       m.b14*m.b15 - 768*m.b13*m.b14*m.b16 - 768*m.b13*m.b14*m.b17 - 800*m.b13*m.b14*m.b18 - 768*m.b13*
                       m.b14*m.b19 - 800*m.b13*m.b14*m.b20 - 800*m.b13*m.b14*m.b21 - 704*m.b13*m.b14*m.b22 - 608*m.b13*
                       m.b14*m.b23 - 480*m.b13*m.b14*m.b24 - 352*m.b13*m.b14*m.b25 - 288*m.b13*m.b14*m.b26 - 224*m.b13*
                       m.b14*m.b27 - 160*m.b13*m.b14*m.b28 - 96*m.b13*m.b14*m.b29 - 32*m.b13*m.b14*m.b30 - 768*m.b13*
                       m.b15*m.b16 - 512*m.b13*m.b15*m.b17 - 832*m.b13*m.b15*m.b18 - 864*m.b13*m.b15*m.b19 - 800*m.b13*
                       m.b15*m.b20 - 800*m.b13*m.b15*m.b21 - 704*m.b13*m.b15*m.b22 - 608*m.b13*m.b15*m.b23 - 480*m.b13*
                       m.b15*m.b24 - 352*m.b13*m.b15*m.b25 - 256*m.b13*m.b15*m.b26 - 192*m.b13*m.b15*m.b27 - 128*m.b13*
                       m.b15*m.b28 - 64*m.b13*m.b15*m.b29 - 32*m.b13*m.b15*m.b30 - 768*m.b13*m.b16*m.b17 - 832*m.b13*
                       m.b16*m.b18 - 608*m.b13*m.b16*m.b19 - 800*m.b13*m.b16*m.b20 - 800*m.b13*m.b16*m.b21 - 704*m.b13*
                       m.b16*m.b22 - 608*m.b13*m.b16*m.b23 - 480*m.b13*m.b16*m.b24 - 352*m.b13*m.b16*m.b25 - 224*m.b13*
                       m.b16*m.b26 - 160*m.b13*m.b16*m.b27 - 96*m.b13*m.b16*m.b28 - 64*m.b13*m.b16*m.b29 - 32*m.b13*
                       m.b16*m.b30 - 800*m.b13*m.b17*m.b18 - 864*m.b13*m.b17*m.b19 - 800*m.b13*m.b17*m.b20 - 480*m.b13*
                       m.b17*m.b21 - 704*m.b13*m.b17*m.b22 - 608*m.b13*m.b17*m.b23 - 480*m.b13*m.b17*m.b24 - 352*m.b13*
                       m.b17*m.b25 - 224*m.b13*m.b17*m.b26 - 128*m.b13*m.b17*m.b27 - 96*m.b13*m.b17*m.b28 - 64*m.b13*
                       m.b17*m.b29 - 32*m.b13*m.b17*m.b30 - 736*m.b13*m.b18*m.b19 - 800*m.b13*m.b18*m.b20 - 800*m.b13*
                       m.b18*m.b21 - 704*m.b13*m.b18*m.b22 - 352*m.b13*m.b18*m.b23 - 480*m.b13*m.b18*m.b24 - 352*m.b13*
                       m.b18*m.b25 - 224*m.b13*m.b18*m.b26 - 128*m.b13*m.b18*m.b27 - 96*m.b13*m.b18*m.b28 - 64*m.b13*
                       m.b18*m.b29 - 32*m.b13*m.b18*m.b30 - 768*m.b13*m.b19*m.b20 - 768*m.b13*m.b19*m.b21 - 672*m.b13*
                       m.b19*m.b22 - 576*m.b13*m.b19*m.b23 - 480*m.b13*m.b19*m.b24 - 160*m.b13*m.b19*m.b25 - 256*m.b13*
                       m.b19*m.b26 - 160*m.b13*m.b19*m.b27 - 96*m.b13*m.b19*m.b28 - 64*m.b13*m.b19*m.b29 - 32*m.b13*
                       m.b19*m.b30 - 736*m.b13*m.b20*m.b21 - 640*m.b13*m.b20*m.b22 - 544*m.b13*m.b20*m.b23 - 448*m.b13*
                       m.b20*m.b24 - 384*m.b13*m.b20*m.b25 - 288*m.b13*m.b20*m.b26 - 64*m.b13*m.b20*m.b27 - 96*m.b13*
                       m.b20*m.b28 - 64*m.b13*m.b20*m.b29 - 32*m.b13*m.b20*m.b30 - 608*m.b13*m.b21*m.b22 - 512*m.b13*
                       m.b21*m.b23 - 448*m.b13*m.b21*m.b24 - 384*m.b13*m.b21*m.b25 - 320*m.b13*m.b21*m.b26 - 224*m.b13*
                       m.b21*m.b27 - 128*m.b13*m.b21*m.b28 - 32*m.b13*m.b21*m.b30 - 512*m.b13*m.b22*m.b23 - 448*m.b13*
                       m.b22*m.b24 - 384*m.b13*m.b22*m.b25 - 320*m.b13*m.b22*m.b26 - 256*m.b13*m.b22*m.b27 - 160*m.b13*
                       m.b22*m.b28 - 64*m.b13*m.b22*m.b29 - 32*m.b13*m.b22*m.b30 - 448*m.b13*m.b23*m.b24 - 384*m.b13*
                       m.b23*m.b25 - 320*m.b13*m.b23*m.b26 - 256*m.b13*m.b23*m.b27 - 192*m.b13*m.b23*m.b28 - 96*m.b13*
                       m.b23*m.b29 - 32*m.b13*m.b23*m.b30 - 384*m.b13*m.b24*m.b25 - 320*m.b13*m.b24*m.b26 - 256*m.b13*
                       m.b24*m.b27 - 192*m.b13*m.b24*m.b28 - 128*m.b13*m.b24*m.b29 - 32*m.b13*m.b24*m.b30 - 320*m.b13*
                       m.b25*m.b26 - 256*m.b13*m.b25*m.b27 - 192*m.b13*m.b25*m.b28 - 128*m.b13*m.b25*m.b29 - 64*m.b13*
                       m.b25*m.b30 - 256*m.b13*m.b26*m.b27 - 192*m.b13*m.b26*m.b28 - 128*m.b13*m.b26*m.b29 - 64*m.b13*
                       m.b26*m.b30 - 192*m.b13*m.b27*m.b28 - 128*m.b13*m.b27*m.b29 - 64*m.b13*m.b27*m.b30 - 128*m.b13*
                       m.b28*m.b29 - 64*m.b13*m.b28*m.b30 - 64*m.b13*m.b29*m.b30 - 512*m.b14*m.b15*m.b16 - 768*m.b14*
                       m.b15*m.b17 - 768*m.b14*m.b15*m.b18 - 832*m.b14*m.b15*m.b19 - 800*m.b14*m.b15*m.b20 - 800*m.b14*
                       m.b15*m.b21 - 768*m.b14*m.b15*m.b22 - 672*m.b14*m.b15*m.b23 - 544*m.b14*m.b15*m.b24 - 416*m.b14*
                       m.b15*m.b25 - 288*m.b14*m.b15*m.b26 - 224*m.b14*m.b15*m.b27 - 160*m.b14*m.b15*m.b28 - 96*m.b14*
                       m.b15*m.b29 - 32*m.b14*m.b15*m.b30 - 768*m.b14*m.b16*m.b17 - 512*m.b14*m.b16*m.b18 - 864*m.b14*
                       m.b16*m.b19 - 864*m.b14*m.b16*m.b20 - 800*m.b14*m.b16*m.b21 - 768*m.b14*m.b16*m.b22 - 672*m.b14*
                       m.b16*m.b23 - 544*m.b14*m.b16*m.b24 - 416*m.b14*m.b16*m.b25 - 288*m.b14*m.b16*m.b26 - 192*m.b14*
                       m.b16*m.b27 - 128*m.b14*m.b16*m.b28 - 64*m.b14*m.b16*m.b29 - 32*m.b14*m.b16*m.b30 - 768*m.b14*
                       m.b17*m.b18 - 800*m.b14*m.b17*m.b19 - 608*m.b14*m.b17*m.b20 - 800*m.b14*m.b17*m.b21 - 768*m.b14*
                       m.b17*m.b22 - 672*m.b14*m.b17*m.b23 - 544*m.b14*m.b17*m.b24 - 416*m.b14*m.b17*m.b25 - 288*m.b14*
                       m.b17*m.b26 - 160*m.b14*m.b17*m.b27 - 96*m.b14*m.b17*m.b28 - 64*m.b14*m.b17*m.b29 - 32*m.b14*
                       m.b17*m.b30 - 768*m.b14*m.b18*m.b19 - 832*m.b14*m.b18*m.b20 - 768*m.b14*m.b18*m.b21 - 448*m.b14*
                       m.b18*m.b22 - 640*m.b14*m.b18*m.b23 - 544*m.b14*m.b18*m.b24 - 416*m.b14*m.b18*m.b25 - 288*m.b14*
                       m.b18*m.b26 - 160*m.b14*m.b18*m.b27 - 96*m.b14*m.b18*m.b28 - 64*m.b14*m.b18*m.b29 - 32*m.b14*
                       m.b18*m.b30 - 704*m.b14*m.b19*m.b20 - 736*m.b14*m.b19*m.b21 - 704*m.b14*m.b19*m.b22 - 608*m.b14*
                       m.b19*m.b23 - 288*m.b14*m.b19*m.b24 - 416*m.b14*m.b19*m.b25 - 288*m.b14*m.b19*m.b26 - 192*m.b14*
                       m.b19*m.b27 - 96*m.b14*m.b19*m.b28 - 64*m.b14*m.b19*m.b29 - 32*m.b14*m.b19*m.b30 - 704*m.b14*
                       m.b20*m.b21 - 672*m.b14*m.b20*m.b22 - 576*m.b14*m.b20*m.b23 - 480*m.b14*m.b20*m.b24 - 384*m.b14*
                       m.b20*m.b25 - 160*m.b14*m.b20*m.b26 - 224*m.b14*m.b20*m.b27 - 128*m.b14*m.b20*m.b28 - 64*m.b14*
                       m.b20*m.b29 - 32*m.b14*m.b20*m.b30 - 640*m.b14*m.b21*m.b22 - 544*m.b14*m.b21*m.b23 - 448*m.b14*
                       m.b21*m.b24 - 384*m.b14*m.b21*m.b25 - 320*m.b14*m.b21*m.b26 - 256*m.b14*m.b21*m.b27 - 64*m.b14*
                       m.b21*m.b28 - 64*m.b14*m.b21*m.b29 - 32*m.b14*m.b21*m.b30 - 512*m.b14*m.b22*m.b23 - 448*m.b14*
                       m.b22*m.b24 - 384*m.b14*m.b22*m.b25 - 320*m.b14*m.b22*m.b26 - 256*m.b14*m.b22*m.b27 - 192*m.b14*
                       m.b22*m.b28 - 96*m.b14*m.b22*m.b29 - 448*m.b14*m.b23*m.b24 - 384*m.b14*m.b23*m.b25 - 320*m.b14*
                       m.b23*m.b26 - 256*m.b14*m.b23*m.b27 - 192*m.b14*m.b23*m.b28 - 128*m.b14*m.b23*m.b29 - 32*m.b14*
                       m.b23*m.b30 - 384*m.b14*m.b24*m.b25 - 320*m.b14*m.b24*m.b26 - 256*m.b14*m.b24*m.b27 - 192*m.b14*
                       m.b24*m.b28 - 128*m.b14*m.b24*m.b29 - 64*m.b14*m.b24*m.b30 - 320*m.b14*m.b25*m.b26 - 256*m.b14*
                       m.b25*m.b27 - 192*m.b14*m.b25*m.b28 - 128*m.b14*m.b25*m.b29 - 64*m.b14*m.b25*m.b30 - 256*m.b14*
                       m.b26*m.b27 - 192*m.b14*m.b26*m.b28 - 128*m.b14*m.b26*m.b29 - 64*m.b14*m.b26*m.b30 - 192*m.b14*
                       m.b27*m.b28 - 128*m.b14*m.b27*m.b29 - 64*m.b14*m.b27*m.b30 - 128*m.b14*m.b28*m.b29 - 64*m.b14*
                       m.b28*m.b30 - 64*m.b14*m.b29*m.b30 - 512*m.b15*m.b16*m.b17 - 768*m.b15*m.b16*m.b18 - 768*m.b15*
                       m.b16*m.b19 - 864*m.b15*m.b16*m.b20 - 832*m.b15*m.b16*m.b21 - 800*m.b15*m.b16*m.b22 - 736*m.b15*
                       m.b16*m.b23 - 608*m.b15*m.b16*m.b24 - 480*m.b15*m.b16*m.b25 - 352*m.b15*m.b16*m.b26 - 224*m.b15*
                       m.b16*m.b27 - 160*m.b15*m.b16*m.b28 - 96*m.b15*m.b16*m.b29 - 32*m.b15*m.b16*m.b30 - 768*m.b15*
                       m.b17*m.b18 - 512*m.b15*m.b17*m.b19 - 864*m.b15*m.b17*m.b20 - 832*m.b15*m.b17*m.b21 - 768*m.b15*
                       m.b17*m.b22 - 704*m.b15*m.b17*m.b23 - 608*m.b15*m.b17*m.b24 - 480*m.b15*m.b17*m.b25 - 352*m.b15*
                       m.b17*m.b26 - 224*m.b15*m.b17*m.b27 - 128*m.b15*m.b17*m.b28 - 64*m.b15*m.b17*m.b29 - 32*m.b15*
                       m.b17*m.b30 - 768*m.b15*m.b18*m.b19 - 768*m.b15*m.b18*m.b20 - 544*m.b15*m.b18*m.b21 - 736*m.b15*
                       m.b18*m.b22 - 672*m.b15*m.b18*m.b23 - 576*m.b15*m.b18*m.b24 - 480*m.b15*m.b18*m.b25 - 352*m.b15*
                       m.b18*m.b26 - 224*m.b15*m.b18*m.b27 - 96*m.b15*m.b18*m.b28 - 64*m.b15*m.b18*m.b29 - 32*m.b15*
                       m.b18*m.b30 - 736*m.b15*m.b19*m.b20 - 768*m.b15*m.b19*m.b21 - 704*m.b15*m.b19*m.b22 - 384*m.b15*
                       m.b19*m.b23 - 544*m.b15*m.b19*m.b24 - 448*m.b15*m.b19*m.b25 - 352*m.b15*m.b19*m.b26 - 224*m.b15*
                       m.b19*m.b27 - 128*m.b15*m.b19*m.b28 - 64*m.b15*m.b19*m.b29 - 32*m.b15*m.b19*m.b30 - 672*m.b15*
                       m.b20*m.b21 - 672*m.b15*m.b20*m.b22 - 608*m.b15*m.b20*m.b23 - 512*m.b15*m.b20*m.b24 - 224*m.b15*
                       m.b20*m.b25 - 320*m.b15*m.b20*m.b26 - 256*m.b15*m.b20*m.b27 - 160*m.b15*m.b20*m.b28 - 64*m.b15*
                       m.b20*m.b29 - 32*m.b15*m.b20*m.b30 - 640*m.b15*m.b21*m.b22 - 576*m.b15*m.b21*m.b23 - 480*m.b15*
                       m.b21*m.b24 - 384*m.b15*m.b21*m.b25 - 320*m.b15*m.b21*m.b26 - 128*m.b15*m.b21*m.b27 - 192*m.b15*
                       m.b21*m.b28 - 96*m.b15*m.b21*m.b29 - 32*m.b15*m.b21*m.b30 - 544*m.b15*m.b22*m.b23 - 448*m.b15*
                       m.b22*m.b24 - 384*m.b15*m.b22*m.b25 - 320*m.b15*m.b22*m.b26 - 256*m.b15*m.b22*m.b27 - 192*m.b15*
                       m.b22*m.b28 - 64*m.b15*m.b22*m.b29 - 32*m.b15*m.b22*m.b30 - 448*m.b15*m.b23*m.b24 - 384*m.b15*
                       m.b23*m.b25 - 320*m.b15*m.b23*m.b26 - 256*m.b15*m.b23*m.b27 - 192*m.b15*m.b23*m.b28 - 128*m.b15*
                       m.b23*m.b29 - 64*m.b15*m.b23*m.b30 - 384*m.b15*m.b24*m.b25 - 320*m.b15*m.b24*m.b26 - 256*m.b15*
                       m.b24*m.b27 - 192*m.b15*m.b24*m.b28 - 128*m.b15*m.b24*m.b29 - 64*m.b15*m.b24*m.b30 - 320*m.b15*
                       m.b25*m.b26 - 256*m.b15*m.b25*m.b27 - 192*m.b15*m.b25*m.b28 - 128*m.b15*m.b25*m.b29 - 64*m.b15*
                       m.b25*m.b30 - 256*m.b15*m.b26*m.b27 - 192*m.b15*m.b26*m.b28 - 128*m.b15*m.b26*m.b29 - 64*m.b15*
                       m.b26*m.b30 - 192*m.b15*m.b27*m.b28 - 128*m.b15*m.b27*m.b29 - 64*m.b15*m.b27*m.b30 - 128*m.b15*
                       m.b28*m.b29 - 64*m.b15*m.b28*m.b30 - 64*m.b15*m.b29*m.b30 - 512*m.b16*m.b17*m.b18 - 768*m.b16*
                       m.b17*m.b19 - 768*m.b16*m.b17*m.b20 - 832*m.b16*m.b17*m.b21 - 800*m.b16*m.b17*m.b22 - 736*m.b16*
                       m.b17*m.b23 - 640*m.b16*m.b17*m.b24 - 544*m.b16*m.b17*m.b25 - 416*m.b16*m.b17*m.b26 - 288*m.b16*
                       m.b17*m.b27 - 160*m.b16*m.b17*m.b28 - 96*m.b16*m.b17*m.b29 - 32*m.b16*m.b17*m.b30 - 768*m.b16*
                       m.b18*m.b19 - 512*m.b16*m.b18*m.b20 - 832*m.b16*m.b18*m.b21 - 768*m.b16*m.b18*m.b22 - 704*m.b16*
                       m.b18*m.b23 - 608*m.b16*m.b18*m.b24 - 512*m.b16*m.b18*m.b25 - 416*m.b16*m.b18*m.b26 - 288*m.b16*
                       m.b18*m.b27 - 160*m.b16*m.b18*m.b28 - 64*m.b16*m.b18*m.b29 - 32*m.b16*m.b18*m.b30 - 768*m.b16*
                       m.b19*m.b20 - 736*m.b16*m.b19*m.b21 - 480*m.b16*m.b19*m.b22 - 672*m.b16*m.b19*m.b23 - 576*m.b16*
                       m.b19*m.b24 - 480*m.b16*m.b19*m.b25 - 384*m.b16*m.b19*m.b26 - 288*m.b16*m.b19*m.b27 - 160*m.b16*
                       m.b19*m.b28 - 64*m.b16*m.b19*m.b29 - 32*m.b16*m.b19*m.b30 - 704*m.b16*m.b20*m.b21 - 704*m.b16*
                       m.b20*m.b22 - 640*m.b16*m.b20*m.b23 - 320*m.b16*m.b20*m.b24 - 448*m.b16*m.b20*m.b25 - 352*m.b16*
                       m.b20*m.b26 - 256*m.b16*m.b20*m.b27 - 192*m.b16*m.b20*m.b28 - 96*m.b16*m.b20*m.b29 - 32*m.b16*
                       m.b20*m.b30 - 640*m.b16*m.b21*m.b22 - 608*m.b16*m.b21*m.b23 - 512*m.b16*m.b21*m.b24 - 416*m.b16*
                       m.b21*m.b25 - 160*m.b16*m.b21*m.b26 - 256*m.b16*m.b21*m.b27 - 192*m.b16*m.b21*m.b28 - 128*m.b16*
                       m.b21*m.b29 - 32*m.b16*m.b21*m.b30 - 576*m.b16*m.b22*m.b23 - 480*m.b16*m.b22*m.b24 - 384*m.b16*
                       m.b22*m.b25 - 320*m.b16*m.b22*m.b26 - 256*m.b16*m.b22*m.b27 - 96*m.b16*m.b22*m.b28 - 128*m.b16*
                       m.b22*m.b29 - 64*m.b16*m.b22*m.b30 - 448*m.b16*m.b23*m.b24 - 384*m.b16*m.b23*m.b25 - 320*m.b16*
                       m.b23*m.b26 - 256*m.b16*m.b23*m.b27 - 192*m.b16*m.b23*m.b28 - 128*m.b16*m.b23*m.b29 - 32*m.b16*
                       m.b23*m.b30 - 384*m.b16*m.b24*m.b25 - 320*m.b16*m.b24*m.b26 - 256*m.b16*m.b24*m.b27 - 192*m.b16*
                       m.b24*m.b28 - 128*m.b16*m.b24*m.b29 - 64*m.b16*m.b24*m.b30 - 320*m.b16*m.b25*m.b26 - 256*m.b16*
                       m.b25*m.b27 - 192*m.b16*m.b25*m.b28 - 128*m.b16*m.b25*m.b29 - 64*m.b16*m.b25*m.b30 - 256*m.b16*
                       m.b26*m.b27 - 192*m.b16*m.b26*m.b28 - 128*m.b16*m.b26*m.b29 - 64*m.b16*m.b26*m.b30 - 192*m.b16*
                       m.b27*m.b28 - 128*m.b16*m.b27*m.b29 - 64*m.b16*m.b27*m.b30 - 128*m.b16*m.b28*m.b29 - 64*m.b16*
                       m.b28*m.b30 - 64*m.b16*m.b29*m.b30 - 512*m.b17*m.b18*m.b19 - 768*m.b17*m.b18*m.b20 - 768*m.b17*
                       m.b18*m.b21 - 800*m.b17*m.b18*m.b22 - 736*m.b17*m.b18*m.b23 - 640*m.b17*m.b18*m.b24 - 544*m.b17*
                       m.b18*m.b25 - 448*m.b17*m.b18*m.b26 - 352*m.b17*m.b18*m.b27 - 224*m.b17*m.b18*m.b28 - 96*m.b17*
                       m.b18*m.b29 - 32*m.b17*m.b18*m.b30 - 768*m.b17*m.b19*m.b20 - 512*m.b17*m.b19*m.b21 - 768*m.b17*
                       m.b19*m.b22 - 704*m.b17*m.b19*m.b23 - 608*m.b17*m.b19*m.b24 - 512*m.b17*m.b19*m.b25 - 416*m.b17*
                       m.b19*m.b26 - 320*m.b17*m.b19*m.b27 - 224*m.b17*m.b19*m.b28 - 96*m.b17*m.b19*m.b29 - 32*m.b17*
                       m.b19*m.b30 - 736*m.b17*m.b20*m.b21 - 704*m.b17*m.b20*m.b22 - 416*m.b17*m.b20*m.b23 - 576*m.b17*
                       m.b20*m.b24 - 480*m.b17*m.b20*m.b25 - 384*m.b17*m.b20*m.b26 - 288*m.b17*m.b20*m.b27 - 192*m.b17*
                       m.b20*m.b28 - 128*m.b17*m.b20*m.b29 - 32*m.b17*m.b20*m.b30 - 672*m.b17*m.b21*m.b22 - 640*m.b17*
                       m.b21*m.b23 - 544*m.b17*m.b21*m.b24 - 256*m.b17*m.b21*m.b25 - 352*m.b17*m.b21*m.b26 - 256*m.b17*
                       m.b21*m.b27 - 192*m.b17*m.b21*m.b28 - 128*m.b17*m.b21*m.b29 - 64*m.b17*m.b21*m.b30 - 608*m.b17*
                       m.b22*m.b23 - 512*m.b17*m.b22*m.b24 - 416*m.b17*m.b22*m.b25 - 320*m.b17*m.b22*m.b26 - 128*m.b17*
                       m.b22*m.b27 - 192*m.b17*m.b22*m.b28 - 128*m.b17*m.b22*m.b29 - 64*m.b17*m.b22*m.b30 - 480*m.b17*
                       m.b23*m.b24 - 384*m.b17*m.b23*m.b25 - 320*m.b17*m.b23*m.b26 - 256*m.b17*m.b23*m.b27 - 192*m.b17*
                       m.b23*m.b28 - 64*m.b17*m.b23*m.b29 - 64*m.b17*m.b23*m.b30 - 384*m.b17*m.b24*m.b25 - 320*m.b17*
                       m.b24*m.b26 - 256*m.b17*m.b24*m.b27 - 192*m.b17*m.b24*m.b28 - 128*m.b17*m.b24*m.b29 - 64*m.b17*
                       m.b24*m.b30 - 320*m.b17*m.b25*m.b26 - 256*m.b17*m.b25*m.b27 - 192*m.b17*m.b25*m.b28 - 128*m.b17*
                       m.b25*m.b29 - 64*m.b17*m.b25*m.b30 - 256*m.b17*m.b26*m.b27 - 192*m.b17*m.b26*m.b28 - 128*m.b17*
                       m.b26*m.b29 - 64*m.b17*m.b26*m.b30 - 192*m.b17*m.b27*m.b28 - 128*m.b17*m.b27*m.b29 - 64*m.b17*
                       m.b27*m.b30 - 128*m.b17*m.b28*m.b29 - 64*m.b17*m.b28*m.b30 - 64*m.b17*m.b29*m.b30 - 512*m.b18*
                       m.b19*m.b20 - 768*m.b18*m.b19*m.b21 - 768*m.b18*m.b19*m.b22 - 736*m.b18*m.b19*m.b23 - 640*m.b18*
                       m.b19*m.b24 - 544*m.b18*m.b19*m.b25 - 448*m.b18*m.b19*m.b26 - 352*m.b18*m.b19*m.b27 - 256*m.b18*
                       m.b19*m.b28 - 160*m.b18*m.b19*m.b29 - 32*m.b18*m.b19*m.b30 - 768*m.b18*m.b20*m.b21 - 480*m.b18*
                       m.b20*m.b22 - 704*m.b18*m.b20*m.b23 - 608*m.b18*m.b20*m.b24 - 512*m.b18*m.b20*m.b25 - 416*m.b18*
                       m.b20*m.b26 - 320*m.b18*m.b20*m.b27 - 224*m.b18*m.b20*m.b28 - 128*m.b18*m.b20*m.b29 - 64*m.b18*
                       m.b20*m.b30 - 704*m.b18*m.b21*m.b22 - 672*m.b18*m.b21*m.b23 - 352*m.b18*m.b21*m.b24 - 480*m.b18*
                       m.b21*m.b25 - 384*m.b18*m.b21*m.b26 - 288*m.b18*m.b21*m.b27 - 192*m.b18*m.b21*m.b28 - 128*m.b18*
                       m.b21*m.b29 - 64*m.b18*m.b21*m.b30 - 640*m.b18*m.b22*m.b23 - 544*m.b18*m.b22*m.b24 - 448*m.b18*
                       m.b22*m.b25 - 192*m.b18*m.b22*m.b26 - 256*m.b18*m.b22*m.b27 - 192*m.b18*m.b22*m.b28 - 128*m.b18*
                       m.b22*m.b29 - 64*m.b18*m.b22*m.b30 - 512*m.b18*m.b23*m.b24 - 416*m.b18*m.b23*m.b25 - 320*m.b18*
                       m.b23*m.b26 - 256*m.b18*m.b23*m.b27 - 96*m.b18*m.b23*m.b28 - 128*m.b18*m.b23*m.b29 - 64*m.b18*
                       m.b23*m.b30 - 384*m.b18*m.b24*m.b25 - 320*m.b18*m.b24*m.b26 - 256*m.b18*m.b24*m.b27 - 192*m.b18*
                       m.b24*m.b28 - 128*m.b18*m.b24*m.b29 - 32*m.b18*m.b24*m.b30 - 320*m.b18*m.b25*m.b26 - 256*m.b18*
                       m.b25*m.b27 - 192*m.b18*m.b25*m.b28 - 128*m.b18*m.b25*m.b29 - 64*m.b18*m.b25*m.b30 - 256*m.b18*
                       m.b26*m.b27 - 192*m.b18*m.b26*m.b28 - 128*m.b18*m.b26*m.b29 - 64*m.b18*m.b26*m.b30 - 192*m.b18*
                       m.b27*m.b28 - 128*m.b18*m.b27*m.b29 - 64*m.b18*m.b27*m.b30 - 128*m.b18*m.b28*m.b29 - 64*m.b18*
                       m.b28*m.b30 - 64*m.b18*m.b29*m.b30 - 512*m.b19*m.b20*m.b21 - 768*m.b19*m.b20*m.b22 - 736*m.b19*
                       m.b20*m.b23 - 640*m.b19*m.b20*m.b24 - 544*m.b19*m.b20*m.b25 - 448*m.b19*m.b20*m.b26 - 352*m.b19*
                       m.b20*m.b27 - 256*m.b19*m.b20*m.b28 - 160*m.b19*m.b20*m.b29 - 64*m.b19*m.b20*m.b30 - 736*m.b19*
                       m.b21*m.b22 - 448*m.b19*m.b21*m.b23 - 608*m.b19*m.b21*m.b24 - 512*m.b19*m.b21*m.b25 - 416*m.b19*
                       m.b21*m.b26 - 320*m.b19*m.b21*m.b27 - 224*m.b19*m.b21*m.b28 - 128*m.b19*m.b21*m.b29 - 64*m.b19*
                       m.b21*m.b30 - 672*m.b19*m.b22*m.b23 - 576*m.b19*m.b22*m.b24 - 288*m.b19*m.b22*m.b25 - 384*m.b19*
                       m.b22*m.b26 - 288*m.b19*m.b22*m.b27 - 192*m.b19*m.b22*m.b28 - 128*m.b19*m.b22*m.b29 - 64*m.b19*
                       m.b22*m.b30 - 544*m.b19*m.b23*m.b24 - 448*m.b19*m.b23*m.b25 - 352*m.b19*m.b23*m.b26 - 128*m.b19*
                       m.b23*m.b27 - 192*m.b19*m.b23*m.b28 - 128*m.b19*m.b23*m.b29 - 64*m.b19*m.b23*m.b30 - 416*m.b19*
                       m.b24*m.b25 - 320*m.b19*m.b24*m.b26 - 256*m.b19*m.b24*m.b27 - 192*m.b19*m.b24*m.b28 - 64*m.b19*
                       m.b24*m.b29 - 64*m.b19*m.b24*m.b30 - 320*m.b19*m.b25*m.b26 - 256*m.b19*m.b25*m.b27 - 192*m.b19*
                       m.b25*m.b28 - 128*m.b19*m.b25*m.b29 - 64*m.b19*m.b25*m.b30 - 256*m.b19*m.b26*m.b27 - 192*m.b19*
                       m.b26*m.b28 - 128*m.b19*m.b26*m.b29 - 64*m.b19*m.b26*m.b30 - 192*m.b19*m.b27*m.b28 - 128*m.b19*
                       m.b27*m.b29 - 64*m.b19*m.b27*m.b30 - 128*m.b19*m.b28*m.b29 - 64*m.b19*m.b28*m.b30 - 64*m.b19*
                       m.b29*m.b30 - 512*m.b20*m.b21*m.b22 - 736*m.b20*m.b21*m.b23 - 640*m.b20*m.b21*m.b24 - 544*m.b20*
                       m.b21*m.b25 - 448*m.b20*m.b21*m.b26 - 352*m.b20*m.b21*m.b27 - 256*m.b20*m.b21*m.b28 - 160*m.b20*
                       m.b21*m.b29 - 64*m.b20*m.b21*m.b30 - 704*m.b20*m.b22*m.b23 - 384*m.b20*m.b22*m.b24 - 512*m.b20*
                       m.b22*m.b25 - 416*m.b20*m.b22*m.b26 - 320*m.b20*m.b22*m.b27 - 224*m.b20*m.b22*m.b28 - 128*m.b20*
                       m.b22*m.b29 - 64*m.b20*m.b22*m.b30 - 576*m.b20*m.b23*m.b24 - 480*m.b20*m.b23*m.b25 - 224*m.b20*
                       m.b23*m.b26 - 288*m.b20*m.b23*m.b27 - 192*m.b20*m.b23*m.b28 - 128*m.b20*m.b23*m.b29 - 64*m.b20*
                       m.b23*m.b30 - 448*m.b20*m.b24*m.b25 - 352*m.b20*m.b24*m.b26 - 256*m.b20*m.b24*m.b27 - 96*m.b20*
                       m.b24*m.b28 - 128*m.b20*m.b24*m.b29 - 64*m.b20*m.b24*m.b30 - 320*m.b20*m.b25*m.b26 - 256*m.b20*
                       m.b25*m.b27 - 192*m.b20*m.b25*m.b28 - 128*m.b20*m.b25*m.b29 - 32*m.b20*m.b25*m.b30 - 256*m.b20*
                       m.b26*m.b27 - 192*m.b20*m.b26*m.b28 - 128*m.b20*m.b26*m.b29 - 64*m.b20*m.b26*m.b30 - 192*m.b20*
                       m.b27*m.b28 - 128*m.b20*m.b27*m.b29 - 64*m.b20*m.b27*m.b30 - 128*m.b20*m.b28*m.b29 - 64*m.b20*
                       m.b28*m.b30 - 64*m.b20*m.b29*m.b30 - 480*m.b21*m.b22*m.b23 - 640*m.b21*m.b22*m.b24 - 544*m.b21*
                       m.b22*m.b25 - 448*m.b21*m.b22*m.b26 - 352*m.b21*m.b22*m.b27 - 256*m.b21*m.b22*m.b28 - 160*m.b21*
                       m.b22*m.b29 - 64*m.b21*m.b22*m.b30 - 608*m.b21*m.b23*m.b24 - 320*m.b21*m.b23*m.b25 - 416*m.b21*
                       m.b23*m.b26 - 320*m.b21*m.b23*m.b27 - 224*m.b21*m.b23*m.b28 - 128*m.b21*m.b23*m.b29 - 64*m.b21*
                       m.b23*m.b30 - 480*m.b21*m.b24*m.b25 - 384*m.b21*m.b24*m.b26 - 160*m.b21*m.b24*m.b27 - 192*m.b21*
                       m.b24*m.b28 - 128*m.b21*m.b24*m.b29 - 64*m.b21*m.b24*m.b30 - 352*m.b21*m.b25*m.b26 - 256*m.b21*
                       m.b25*m.b27 - 192*m.b21*m.b25*m.b28 - 64*m.b21*m.b25*m.b29 - 64*m.b21*m.b25*m.b30 - 256*m.b21*
                       m.b26*m.b27 - 192*m.b21*m.b26*m.b28 - 128*m.b21*m.b26*m.b29 - 64*m.b21*m.b26*m.b30 - 192*m.b21*
                       m.b27*m.b28 - 128*m.b21*m.b27*m.b29 - 64*m.b21*m.b27*m.b30 - 128*m.b21*m.b28*m.b29 - 64*m.b21*
                       m.b28*m.b30 - 64*m.b21*m.b29*m.b30 - 416*m.b22*m.b23*m.b24 - 544*m.b22*m.b23*m.b25 - 448*m.b22*
                       m.b23*m.b26 - 352*m.b22*m.b23*m.b27 - 256*m.b22*m.b23*m.b28 - 160*m.b22*m.b23*m.b29 - 64*m.b22*
                       m.b23*m.b30 - 512*m.b22*m.b24*m.b25 - 256*m.b22*m.b24*m.b26 - 320*m.b22*m.b24*m.b27 - 224*m.b22*
                       m.b24*m.b28 - 128*m.b22*m.b24*m.b29 - 64*m.b22*m.b24*m.b30 - 384*m.b22*m.b25*m.b26 - 288*m.b22*
                       m.b25*m.b27 - 96*m.b22*m.b25*m.b28 - 128*m.b22*m.b25*m.b29 - 64*m.b22*m.b25*m.b30 - 256*m.b22*
                       m.b26*m.b27 - 192*m.b22*m.b26*m.b28 - 128*m.b22*m.b26*m.b29 - 32*m.b22*m.b26*m.b30 - 192*m.b22*
                       m.b27*m.b28 - 128*m.b22*m.b27*m.b29 - 64*m.b22*m.b27*m.b30 - 128*m.b22*m.b28*m.b29 - 64*m.b22*
                       m.b28*m.b30 - 64*m.b22*m.b29*m.b30 - 352*m.b23*m.b24*m.b25 - 448*m.b23*m.b24*m.b26 - 352*m.b23*
                       m.b24*m.b27 - 256*m.b23*m.b24*m.b28 - 160*m.b23*m.b24*m.b29 - 64*m.b23*m.b24*m.b30 - 416*m.b23*
                       m.b25*m.b26 - 192*m.b23*m.b25*m.b27 - 224*m.b23*m.b25*m.b28 - 128*m.b23*m.b25*m.b29 - 64*m.b23*
                       m.b25*m.b30 - 288*m.b23*m.b26*m.b27 - 192*m.b23*m.b26*m.b28 - 64*m.b23*m.b26*m.b29 - 64*m.b23*
                       m.b26*m.b30 - 192*m.b23*m.b27*m.b28 - 128*m.b23*m.b27*m.b29 - 64*m.b23*m.b27*m.b30 - 128*m.b23*
                       m.b28*m.b29 - 64*m.b23*m.b28*m.b30 - 64*m.b23*m.b29*m.b30 - 288*m.b24*m.b25*m.b26 - 352*m.b24*
                       m.b25*m.b27 - 256*m.b24*m.b25*m.b28 - 160*m.b24*m.b25*m.b29 - 64*m.b24*m.b25*m.b30 - 320*m.b24*
                       m.b26*m.b27 - 128*m.b24*m.b26*m.b28 - 128*m.b24*m.b26*m.b29 - 64*m.b24*m.b26*m.b30 - 192*m.b24*
                       m.b27*m.b28 - 128*m.b24*m.b27*m.b29 - 32*m.b24*m.b27*m.b30 - 128*m.b24*m.b28*m.b29 - 64*m.b24*
                       m.b28*m.b30 - 64*m.b24*m.b29*m.b30 - 224*m.b25*m.b26*m.b27 - 256*m.b25*m.b26*m.b28 - 160*m.b25*
                       m.b26*m.b29 - 64*m.b25*m.b26*m.b30 - 224*m.b25*m.b27*m.b28 - 64*m.b25*m.b27*m.b29 - 64*m.b25*
                       m.b27*m.b30 - 128*m.b25*m.b28*m.b29 - 64*m.b25*m.b28*m.b30 - 64*m.b25*m.b29*m.b30 - 160*m.b26*
                       m.b27*m.b28 - 160*m.b26*m.b27*m.b29 - 64*m.b26*m.b27*m.b30 - 128*m.b26*m.b28*m.b29 - 32*m.b26*
                       m.b28*m.b30 - 64*m.b26*m.b29*m.b30 - 96*m.b27*m.b28*m.b29 - 64*m.b27*m.b28*m.b30 - 64*m.b27*m.b29
                       *m.b30 - 32*m.b28*m.b29*m.b30 + 320*m.b1*m.b2 + 312*m.b1*m.b3 + 304*m.b1*m.b4 + 296*m.b1*m.b5 + 
                       288*m.b1*m.b6 + 280*m.b1*m.b7 + 272*m.b1*m.b8 + 264*m.b1*m.b9 + 256*m.b1*m.b10 + 248*m.b1*m.b11
                        + 240*m.b1*m.b12 + 248*m.b1*m.b13 + 240*m.b1*m.b14 + 232*m.b1*m.b15 + 224*m.b1*m.b16 + 216*m.b1*
                       m.b17 + 208*m.b1*m.b18 + 200*m.b1*m.b19 + 192*m.b1*m.b20 + 184*m.b1*m.b21 + 176*m.b1*m.b22 + 168*
                       m.b1*m.b23 + 640*m.b2*m.b3 + 640*m.b2*m.b4 + 624*m.b2*m.b5 + 608*m.b2*m.b6 + 592*m.b2*m.b7 + 576*
                       m.b2*m.b8 + 560*m.b2*m.b9 + 544*m.b2*m.b10 + 528*m.b2*m.b11 + 512*m.b2*m.b12 + 512*m.b2*m.b13 + 
                       512*m.b2*m.b14 + 496*m.b2*m.b15 + 480*m.b2*m.b16 + 464*m.b2*m.b17 + 448*m.b2*m.b18 + 432*m.b2*
                       m.b19 + 416*m.b2*m.b20 + 400*m.b2*m.b21 + 384*m.b2*m.b22 + 352*m.b2*m.b23 + 168*m.b2*m.b24 + 976*
                       m.b3*m.b4 + 968*m.b3*m.b5 + 960*m.b3*m.b6 + 936*m.b3*m.b7 + 912*m.b3*m.b8 + 888*m.b3*m.b9 + 864*
                       m.b3*m.b10 + 840*m.b3*m.b11 + 816*m.b3*m.b12 + 792*m.b3*m.b13 + 800*m.b3*m.b14 + 792*m.b3*m.b15
                        + 768*m.b3*m.b16 + 744*m.b3*m.b17 + 720*m.b3*m.b18 + 696*m.b3*m.b19 + 672*m.b3*m.b20 + 648*m.b3*
                       m.b21 + 608*m.b3*m.b22 + 568*m.b3*m.b23 + 352*m.b3*m.b24 + 168*m.b3*m.b25 + 1328*m.b4*m.b5 + 1312
                       *m.b4*m.b6 + 1296*m.b4*m.b7 + 1280*m.b4*m.b8 + 1248*m.b4*m.b9 + 1216*m.b4*m.b10 + 1184*m.b4*m.b11
                        + 1152*m.b4*m.b12 + 1120*m.b4*m.b13 + 1104*m.b4*m.b14 + 1104*m.b4*m.b15 + 1088*m.b4*m.b16 + 1056
                       *m.b4*m.b17 + 1024*m.b4*m.b18 + 992*m.b4*m.b19 + 960*m.b4*m.b20 + 912*m.b4*m.b21 + 864*m.b4*m.b22
                        + 800*m.b4*m.b23 + 568*m.b4*m.b24 + 352*m.b4*m.b25 + 168*m.b4*m.b26 + 1696*m.b5*m.b6 + 1672*m.b5
                       *m.b7 + 1648*m.b5*m.b8 + 1624*m.b5*m.b9 + 1600*m.b5*m.b10 + 1560*m.b5*m.b11 + 1520*m.b5*m.b12 + 
                       1480*m.b5*m.b13 + 1440*m.b5*m.b14 + 1432*m.b5*m.b15 + 1424*m.b5*m.b16 + 1400*m.b5*m.b17 + 1360*
                       m.b5*m.b18 + 1320*m.b5*m.b19 + 1264*m.b5*m.b20 + 1208*m.b5*m.b21 + 1136*m.b5*m.b22 + 1064*m.b5*
                       m.b23 + 800*m.b5*m.b24 + 568*m.b5*m.b25 + 352*m.b5*m.b26 + 168*m.b5*m.b27 + 2080*m.b6*m.b7 + 2048
                       *m.b6*m.b8 + 2016*m.b6*m.b9 + 1984*m.b6*m.b10 + 1952*m.b6*m.b11 + 1920*m.b6*m.b12 + 1872*m.b6*
                       m.b13 + 1824*m.b6*m.b14 + 1792*m.b6*m.b15 + 1776*m.b6*m.b16 + 1760*m.b6*m.b17 + 1728*m.b6*m.b18
                        + 1664*m.b6*m.b19 + 1600*m.b6*m.b20 + 1520*m.b6*m.b21 + 1440*m.b6*m.b22 + 1344*m.b6*m.b23 + 1064
                       *m.b6*m.b24 + 800*m.b6*m.b25 + 568*m.b6*m.b26 + 352*m.b6*m.b27 + 168*m.b6*m.b28 + 2480*m.b7*m.b8
                        + 2440*m.b7*m.b9 + 2400*m.b7*m.b10 + 2360*m.b7*m.b11 + 2320*m.b7*m.b12 + 2280*m.b7*m.b13 + 2240*
                       m.b7*m.b14 + 2184*m.b7*m.b15 + 2160*m.b7*m.b16 + 2136*m.b7*m.b17 + 2096*m.b7*m.b18 + 2040*m.b7*
                       m.b19 + 1952*m.b7*m.b20 + 1864*m.b7*m.b21 + 1760*m.b7*m.b22 + 1656*m.b7*m.b23 + 1344*m.b7*m.b24
                        + 1064*m.b7*m.b25 + 800*m.b7*m.b26 + 568*m.b7*m.b27 + 352*m.b7*m.b28 + 168*m.b7*m.b29 + 2896*
                       m.b8*m.b9 + 2848*m.b8*m.b10 + 2800*m.b8*m.b11 + 2752*m.b8*m.b12 + 2704*m.b8*m.b13 + 2656*m.b8*
                       m.b14 + 2608*m.b8*m.b15 + 2576*m.b8*m.b16 + 2528*m.b8*m.b17 + 2480*m.b8*m.b18 + 2416*m.b8*m.b19
                        + 2336*m.b8*m.b20 + 2224*m.b8*m.b21 + 2112*m.b8*m.b22 + 1984*m.b8*m.b23 + 1656*m.b8*m.b24 + 1344
                       *m.b8*m.b25 + 1064*m.b8*m.b26 + 800*m.b8*m.b27 + 568*m.b8*m.b28 + 352*m.b8*m.b29 + 168*m.b8*m.b30
                        + 3104*m.b9*m.b10 + 3056*m.b9*m.b11 + 3008*m.b9*m.b12 + 2944*m.b9*m.b13 + 2896*m.b9*m.b14 + 2848
                       *m.b9*m.b15 + 2800*m.b9*m.b16 + 2800*m.b9*m.b17 + 2752*m.b9*m.b18 + 2672*m.b9*m.b19 + 2592*m.b9*
                       m.b20 + 2464*m.b9*m.b21 + 2336*m.b9*m.b22 + 2112*m.b9*m.b23 + 1760*m.b9*m.b24 + 1440*m.b9*m.b25
                        + 1136*m.b9*m.b26 + 864*m.b9*m.b27 + 608*m.b9*m.b28 + 384*m.b9*m.b29 + 176*m.b9*m.b30 + 3280*
                       m.b10*m.b11 + 3216*m.b10*m.b12 + 3168*m.b10*m.b13 + 3088*m.b10*m.b14 + 3024*m.b10*m.b15 + 2992*
                       m.b10*m.b16 + 2960*m.b10*m.b17 + 2976*m.b10*m.b18 + 2912*m.b10*m.b19 + 2816*m.b10*m.b20 + 2704*
                       m.b10*m.b21 + 2464*m.b10*m.b22 + 2224*m.b10*m.b23 + 1864*m.b10*m.b24 + 1520*m.b10*m.b25 + 1208*
                       m.b10*m.b26 + 912*m.b10*m.b27 + 648*m.b10*m.b28 + 400*m.b10*m.b29 + 184*m.b10*m.b30 + 3408*m.b11*
                       m.b12 + 3344*m.b11*m.b13 + 3264*m.b11*m.b14 + 3168*m.b11*m.b15 + 3104*m.b11*m.b16 + 3104*m.b11*
                       m.b17 + 3072*m.b11*m.b18 + 3104*m.b11*m.b19 + 3024*m.b11*m.b20 + 2816*m.b11*m.b21 + 2592*m.b11*
                       m.b22 + 2336*m.b11*m.b23 + 1952*m.b11*m.b24 + 1600*m.b11*m.b25 + 1264*m.b11*m.b26 + 960*m.b11*
                       m.b27 + 672*m.b11*m.b28 + 416*m.b11*m.b29 + 192*m.b11*m.b30 + 3472*m.b12*m.b13 + 3408*m.b12*m.b14
                        + 3312*m.b12*m.b15 + 3200*m.b12*m.b16 + 3152*m.b12*m.b17 + 3168*m.b12*m.b18 + 3136*m.b12*m.b19
                        + 3104*m.b12*m.b20 + 2912*m.b12*m.b21 + 2672*m.b12*m.b22 + 2416*m.b12*m.b23 + 2040*m.b12*m.b24
                        + 1664*m.b12*m.b25 + 1320*m.b12*m.b26 + 992*m.b12*m.b27 + 696*m.b12*m.b28 + 432*m.b12*m.b29 + 
                       200*m.b12*m.b30 + 3520*m.b13*m.b14 + 3456*m.b13*m.b15 + 3344*m.b13*m.b16 + 3248*m.b13*m.b17 + 
                       3200*m.b13*m.b18 + 3168*m.b13*m.b19 + 3072*m.b13*m.b20 + 2976*m.b13*m.b21 + 2752*m.b13*m.b22 + 
                       2480*m.b13*m.b23 + 2096*m.b13*m.b24 + 1728*m.b13*m.b25 + 1360*m.b13*m.b26 + 1024*m.b13*m.b27 + 
                       720*m.b13*m.b28 + 448*m.b13*m.b29 + 208*m.b13*m.b30 + 3568*m.b14*m.b15 + 3504*m.b14*m.b16 + 3392*
                       m.b14*m.b17 + 3248*m.b14*m.b18 + 3152*m.b14*m.b19 + 3104*m.b14*m.b20 + 2960*m.b14*m.b21 + 2800*
                       m.b14*m.b22 + 2528*m.b14*m.b23 + 2136*m.b14*m.b24 + 1760*m.b14*m.b25 + 1400*m.b14*m.b26 + 1056*
                       m.b14*m.b27 + 744*m.b14*m.b28 + 464*m.b14*m.b29 + 216*m.b14*m.b30 + 3616*m.b15*m.b16 + 3504*m.b15
                       *m.b17 + 3344*m.b15*m.b18 + 3200*m.b15*m.b19 + 3104*m.b15*m.b20 + 2992*m.b15*m.b21 + 2800*m.b15*
                       m.b22 + 2576*m.b15*m.b23 + 2160*m.b15*m.b24 + 1776*m.b15*m.b25 + 1424*m.b15*m.b26 + 1088*m.b15*
                       m.b27 + 768*m.b15*m.b28 + 480*m.b15*m.b29 + 224*m.b15*m.b30 + 3568*m.b16*m.b17 + 3456*m.b16*m.b18
                        + 3312*m.b16*m.b19 + 3168*m.b16*m.b20 + 3024*m.b16*m.b21 + 2848*m.b16*m.b22 + 2608*m.b16*m.b23
                        + 2184*m.b16*m.b24 + 1792*m.b16*m.b25 + 1432*m.b16*m.b26 + 1104*m.b16*m.b27 + 792*m.b16*m.b28 + 
                       496*m.b16*m.b29 + 232*m.b16*m.b30 + 3520*m.b17*m.b18 + 3408*m.b17*m.b19 + 3264*m.b17*m.b20 + 3088
                       *m.b17*m.b21 + 2896*m.b17*m.b22 + 2656*m.b17*m.b23 + 2240*m.b17*m.b24 + 1824*m.b17*m.b25 + 1440*
                       m.b17*m.b26 + 1104*m.b17*m.b27 + 800*m.b17*m.b28 + 512*m.b17*m.b29 + 240*m.b17*m.b30 + 3472*m.b18
                       *m.b19 + 3344*m.b18*m.b20 + 3168*m.b18*m.b21 + 2944*m.b18*m.b22 + 2704*m.b18*m.b23 + 2280*m.b18*
                       m.b24 + 1872*m.b18*m.b25 + 1480*m.b18*m.b26 + 1120*m.b18*m.b27 + 792*m.b18*m.b28 + 512*m.b18*
                       m.b29 + 248*m.b18*m.b30 + 3408*m.b19*m.b20 + 3216*m.b19*m.b21 + 3008*m.b19*m.b22 + 2752*m.b19*
                       m.b23 + 2320*m.b19*m.b24 + 1920*m.b19*m.b25 + 1520*m.b19*m.b26 + 1152*m.b19*m.b27 + 816*m.b19*
                       m.b28 + 512*m.b19*m.b29 + 240*m.b19*m.b30 + 3280*m.b20*m.b21 + 3056*m.b20*m.b22 + 2800*m.b20*
                       m.b23 + 2360*m.b20*m.b24 + 1952*m.b20*m.b25 + 1560*m.b20*m.b26 + 1184*m.b20*m.b27 + 840*m.b20*
                       m.b28 + 528*m.b20*m.b29 + 248*m.b20*m.b30 + 3104*m.b21*m.b22 + 2848*m.b21*m.b23 + 2400*m.b21*
                       m.b24 + 1984*m.b21*m.b25 + 1600*m.b21*m.b26 + 1216*m.b21*m.b27 + 864*m.b21*m.b28 + 544*m.b21*
                       m.b29 + 256*m.b21*m.b30 + 2896*m.b22*m.b23 + 2440*m.b22*m.b24 + 2016*m.b22*m.b25 + 1624*m.b22*
                       m.b26 + 1248*m.b22*m.b27 + 888*m.b22*m.b28 + 560*m.b22*m.b29 + 264*m.b22*m.b30 + 2480*m.b23*m.b24
                        + 2048*m.b23*m.b25 + 1648*m.b23*m.b26 + 1280*m.b23*m.b27 + 912*m.b23*m.b28 + 576*m.b23*m.b29 + 
                       272*m.b23*m.b30 + 2080*m.b24*m.b25 + 1672*m.b24*m.b26 + 1296*m.b24*m.b27 + 936*m.b24*m.b28 + 592*
                       m.b24*m.b29 + 280*m.b24*m.b30 + 1696*m.b25*m.b26 + 1312*m.b25*m.b27 + 960*m.b25*m.b28 + 608*m.b25
                       *m.b29 + 288*m.b25*m.b30 + 1328*m.b26*m.b27 + 968*m.b26*m.b28 + 624*m.b26*m.b29 + 296*m.b26*m.b30
                        + 976*m.b27*m.b28 + 640*m.b27*m.b29 + 304*m.b27*m.b30 + 640*m.b28*m.b29 + 312*m.b28*m.b30 + 320*
                       m.b29*m.b30 - 924*m.b1 - 1924*m.b2 - 2992*m.b3 - 4120*m.b4 - 5300*m.b5 - 6524*m.b6 - 7784*m.b7 - 
                       9072*m.b8 - 9672*m.b9 - 10120*m.b10 - 10424*m.b11 - 10584*m.b12 - 10680*m.b13 - 10728*m.b14 - 
                       10736*m.b15 - 10736*m.b16 - 10728*m.b17 - 10680*m.b18 - 10584*m.b19 - 10424*m.b20 - 10120*m.b21
                        - 9672*m.b22 - 9072*m.b23 - 7784*m.b24 - 6524*m.b25 - 5300*m.b26 - 4120*m.b27 - 2992*m.b28 - 
                       1924*m.b29 - 924*m.b30 - m.x31 <= 0)
