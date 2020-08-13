#  MINLP written by GAMS Convert at 08/13/20 17:37:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         26        1       25        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         26        1       25        0


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
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x26, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b2*m.b15*m.b16 + 64*m.b1*m.b2*m.b16*m.b17 + 64*m.b1*m.b2*m.b17*
                       m.b18 + 64*m.b1*m.b2*m.b18*m.b19 + 64*m.b1*m.b2*m.b19*m.b20 + 64*m.b1*m.b2*m.b20*m.b21 + 64*m.b1*
                       m.b2*m.b21*m.b22 + 64*m.b1*m.b2*m.b22*m.b23 + 64*m.b1*m.b2*m.b23*m.b24 + 64*m.b1*m.b2*m.b24*m.b25
                        + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64*m.b1*m.b3*m.b7*
                       m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*m.b12 + 64*m.b1*
                       m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b3*m.b13*m.b15 + 64*m.b1*m.b3*m.b14*m.b16
                        + 64*m.b1*m.b3*m.b15*m.b17 + 64*m.b1*m.b3*m.b16*m.b18 + 64*m.b1*m.b3*m.b17*m.b19 + 64*m.b1*m.b3*
                       m.b18*m.b20 + 64*m.b1*m.b3*m.b19*m.b21 + 64*m.b1*m.b3*m.b20*m.b22 + 64*m.b1*m.b3*m.b21*m.b23 + 64
                       *m.b1*m.b3*m.b22*m.b24 + 64*m.b1*m.b3*m.b23*m.b25 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*
                       m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4
                       *m.b10*m.b13 + 64*m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b4*m.b12*m.b15 + 64*m.b1*m.b4*m.b13*m.b16 + 
                       64*m.b1*m.b4*m.b14*m.b17 + 64*m.b1*m.b4*m.b15*m.b18 + 64*m.b1*m.b4*m.b16*m.b19 + 64*m.b1*m.b4*
                       m.b17*m.b20 + 64*m.b1*m.b4*m.b18*m.b21 + 64*m.b1*m.b4*m.b19*m.b22 + 64*m.b1*m.b4*m.b20*m.b23 + 64
                       *m.b1*m.b4*m.b21*m.b24 + 64*m.b1*m.b4*m.b22*m.b25 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*
                       m.b11 + 64*m.b1*m.b5*m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 64*m.b1*
                       m.b5*m.b11*m.b15 + 64*m.b1*m.b5*m.b12*m.b16 + 64*m.b1*m.b5*m.b13*m.b17 + 64*m.b1*m.b5*m.b14*m.b18
                        + 64*m.b1*m.b5*m.b15*m.b19 + 64*m.b1*m.b5*m.b16*m.b20 + 64*m.b1*m.b5*m.b17*m.b21 + 64*m.b1*m.b5*
                       m.b18*m.b22 + 64*m.b1*m.b5*m.b19*m.b23 + 64*m.b1*m.b5*m.b20*m.b24 + 64*m.b1*m.b5*m.b21*m.b25 + 64
                       *m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b6*m.b10*
                       m.b15 + 64*m.b1*m.b6*m.b11*m.b16 + 64*m.b1*m.b6*m.b12*m.b17 + 64*m.b1*m.b6*m.b13*m.b18 + 64*m.b1*
                       m.b6*m.b14*m.b19 + 64*m.b1*m.b6*m.b15*m.b20 + 64*m.b1*m.b6*m.b16*m.b21 + 64*m.b1*m.b6*m.b17*m.b22
                        + 64*m.b1*m.b6*m.b18*m.b23 + 64*m.b1*m.b6*m.b19*m.b24 + 64*m.b1*m.b6*m.b20*m.b25 + 64*m.b1*m.b7*
                       m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 64*m.b1*m.b7*m.b10*m.b16 + 64*m.b1*m.b7*m.b11*m.b17 + 64*
                       m.b1*m.b7*m.b12*m.b18 + 64*m.b1*m.b7*m.b13*m.b19 + 64*m.b1*m.b7*m.b14*m.b20 + 64*m.b1*m.b7*m.b15*
                       m.b21 + 64*m.b1*m.b7*m.b16*m.b22 + 64*m.b1*m.b7*m.b17*m.b23 + 64*m.b1*m.b7*m.b18*m.b24 + 64*m.b1*
                       m.b7*m.b19*m.b25 + 64*m.b1*m.b8*m.b9*m.b16 + 64*m.b1*m.b8*m.b10*m.b17 + 64*m.b1*m.b8*m.b11*m.b18
                        + 64*m.b1*m.b8*m.b12*m.b19 + 64*m.b1*m.b8*m.b13*m.b20 + 64*m.b1*m.b8*m.b14*m.b21 + 64*m.b1*m.b8*
                       m.b15*m.b22 + 64*m.b1*m.b8*m.b16*m.b23 + 64*m.b1*m.b8*m.b17*m.b24 + 64*m.b1*m.b8*m.b18*m.b25 + 64
                       *m.b1*m.b9*m.b10*m.b18 + 64*m.b1*m.b9*m.b11*m.b19 + 64*m.b1*m.b9*m.b12*m.b20 + 64*m.b1*m.b9*m.b13
                       *m.b21 + 64*m.b1*m.b9*m.b14*m.b22 + 64*m.b1*m.b9*m.b15*m.b23 + 64*m.b1*m.b9*m.b16*m.b24 + 64*m.b1
                       *m.b9*m.b17*m.b25 + 64*m.b1*m.b10*m.b11*m.b20 + 64*m.b1*m.b10*m.b12*m.b21 + 64*m.b1*m.b10*m.b13*
                       m.b22 + 64*m.b1*m.b10*m.b14*m.b23 + 64*m.b1*m.b10*m.b15*m.b24 + 64*m.b1*m.b10*m.b16*m.b25 + 64*
                       m.b1*m.b11*m.b12*m.b22 + 64*m.b1*m.b11*m.b13*m.b23 + 64*m.b1*m.b11*m.b14*m.b24 + 64*m.b1*m.b11*
                       m.b15*m.b25 + 64*m.b1*m.b12*m.b13*m.b24 + 64*m.b1*m.b12*m.b14*m.b25 + 64*m.b2*m.b3*m.b4*m.b5 + 64
                       *m.b2*m.b3*m.b5*m.b6 + 64*m.b2*m.b3*m.b6*m.b7 + 64*m.b2*m.b3*m.b7*m.b8 + 64*m.b2*m.b3*m.b8*m.b9
                        + 64*m.b2*m.b3*m.b9*m.b10 + 64*m.b2*m.b3*m.b10*m.b11 + 64*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*
                       m.b12*m.b13 + 128*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 128*m.b2*m.b3*m.b15*m.b16
                        + 128*m.b2*m.b3*m.b16*m.b17 + 128*m.b2*m.b3*m.b17*m.b18 + 128*m.b2*m.b3*m.b18*m.b19 + 128*m.b2*
                       m.b3*m.b19*m.b20 + 128*m.b2*m.b3*m.b20*m.b21 + 128*m.b2*m.b3*m.b21*m.b22 + 128*m.b2*m.b3*m.b22*
                       m.b23 + 128*m.b2*m.b3*m.b23*m.b24 + 64*m.b2*m.b3*m.b24*m.b25 + 64*m.b2*m.b4*m.b5*m.b7 + 64*m.b2*
                       m.b4*m.b6*m.b8 + 64*m.b2*m.b4*m.b7*m.b9 + 64*m.b2*m.b4*m.b8*m.b10 + 64*m.b2*m.b4*m.b9*m.b11 + 64*
                       m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*m.b14 + 128*m.b2*m.b4*
                       m.b13*m.b15 + 128*m.b2*m.b4*m.b14*m.b16 + 128*m.b2*m.b4*m.b15*m.b17 + 128*m.b2*m.b4*m.b16*m.b18
                        + 128*m.b2*m.b4*m.b17*m.b19 + 128*m.b2*m.b4*m.b18*m.b20 + 128*m.b2*m.b4*m.b19*m.b21 + 128*m.b2*
                       m.b4*m.b20*m.b22 + 128*m.b2*m.b4*m.b21*m.b23 + 128*m.b2*m.b4*m.b22*m.b24 + 64*m.b2*m.b4*m.b23*
                       m.b25 + 64*m.b2*m.b5*m.b6*m.b9 + 64*m.b2*m.b5*m.b7*m.b10 + 64*m.b2*m.b5*m.b8*m.b11 + 64*m.b2*m.b5
                       *m.b9*m.b12 + 128*m.b2*m.b5*m.b10*m.b13 + 128*m.b2*m.b5*m.b11*m.b14 + 128*m.b2*m.b5*m.b12*m.b15
                        + 128*m.b2*m.b5*m.b13*m.b16 + 128*m.b2*m.b5*m.b14*m.b17 + 128*m.b2*m.b5*m.b15*m.b18 + 128*m.b2*
                       m.b5*m.b16*m.b19 + 128*m.b2*m.b5*m.b17*m.b20 + 128*m.b2*m.b5*m.b18*m.b21 + 128*m.b2*m.b5*m.b19*
                       m.b22 + 128*m.b2*m.b5*m.b20*m.b23 + 128*m.b2*m.b5*m.b21*m.b24 + 64*m.b2*m.b5*m.b22*m.b25 + 64*
                       m.b2*m.b6*m.b7*m.b11 + 64*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 128*m.b2*m.b6*m.b10*
                       m.b14 + 128*m.b2*m.b6*m.b11*m.b15 + 128*m.b2*m.b6*m.b12*m.b16 + 128*m.b2*m.b6*m.b13*m.b17 + 128*
                       m.b2*m.b6*m.b14*m.b18 + 128*m.b2*m.b6*m.b15*m.b19 + 128*m.b2*m.b6*m.b16*m.b20 + 128*m.b2*m.b6*
                       m.b17*m.b21 + 128*m.b2*m.b6*m.b18*m.b22 + 128*m.b2*m.b6*m.b19*m.b23 + 128*m.b2*m.b6*m.b20*m.b24
                        + 64*m.b2*m.b6*m.b21*m.b25 + 128*m.b2*m.b7*m.b8*m.b13 + 128*m.b2*m.b7*m.b9*m.b14 + 128*m.b2*m.b7
                       *m.b10*m.b15 + 128*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b7*m.b12*m.b17 + 128*m.b2*m.b7*m.b13*m.b18
                        + 128*m.b2*m.b7*m.b14*m.b19 + 128*m.b2*m.b7*m.b15*m.b20 + 128*m.b2*m.b7*m.b16*m.b21 + 128*m.b2*
                       m.b7*m.b17*m.b22 + 128*m.b2*m.b7*m.b18*m.b23 + 128*m.b2*m.b7*m.b19*m.b24 + 64*m.b2*m.b7*m.b20*
                       m.b25 + 128*m.b2*m.b8*m.b9*m.b15 + 128*m.b2*m.b8*m.b10*m.b16 + 128*m.b2*m.b8*m.b11*m.b17 + 128*
                       m.b2*m.b8*m.b12*m.b18 + 128*m.b2*m.b8*m.b13*m.b19 + 128*m.b2*m.b8*m.b14*m.b20 + 128*m.b2*m.b8*
                       m.b15*m.b21 + 128*m.b2*m.b8*m.b16*m.b22 + 128*m.b2*m.b8*m.b17*m.b23 + 128*m.b2*m.b8*m.b18*m.b24
                        + 64*m.b2*m.b8*m.b19*m.b25 + 128*m.b2*m.b9*m.b10*m.b17 + 128*m.b2*m.b9*m.b11*m.b18 + 128*m.b2*
                       m.b9*m.b12*m.b19 + 128*m.b2*m.b9*m.b13*m.b20 + 128*m.b2*m.b9*m.b14*m.b21 + 128*m.b2*m.b9*m.b15*
                       m.b22 + 128*m.b2*m.b9*m.b16*m.b23 + 128*m.b2*m.b9*m.b17*m.b24 + 64*m.b2*m.b9*m.b18*m.b25 + 128*
                       m.b2*m.b10*m.b11*m.b19 + 128*m.b2*m.b10*m.b12*m.b20 + 128*m.b2*m.b10*m.b13*m.b21 + 128*m.b2*m.b10
                       *m.b14*m.b22 + 128*m.b2*m.b10*m.b15*m.b23 + 128*m.b2*m.b10*m.b16*m.b24 + 64*m.b2*m.b10*m.b17*
                       m.b25 + 128*m.b2*m.b11*m.b12*m.b21 + 128*m.b2*m.b11*m.b13*m.b22 + 128*m.b2*m.b11*m.b14*m.b23 + 
                       128*m.b2*m.b11*m.b15*m.b24 + 64*m.b2*m.b11*m.b16*m.b25 + 128*m.b2*m.b12*m.b13*m.b23 + 128*m.b2*
                       m.b12*m.b14*m.b24 + 64*m.b2*m.b12*m.b15*m.b25 + 64*m.b2*m.b13*m.b14*m.b25 + 64*m.b3*m.b4*m.b5*
                       m.b6 + 64*m.b3*m.b4*m.b6*m.b7 + 64*m.b3*m.b4*m.b7*m.b8 + 64*m.b3*m.b4*m.b8*m.b9 + 64*m.b3*m.b4*
                       m.b9*m.b10 + 64*m.b3*m.b4*m.b10*m.b11 + 64*m.b3*m.b4*m.b11*m.b12 + 64*m.b3*m.b4*m.b12*m.b13 + 192
                       *m.b3*m.b4*m.b13*m.b14 + 192*m.b3*m.b4*m.b14*m.b15 + 192*m.b3*m.b4*m.b15*m.b16 + 192*m.b3*m.b4*
                       m.b16*m.b17 + 192*m.b3*m.b4*m.b17*m.b18 + 192*m.b3*m.b4*m.b18*m.b19 + 192*m.b3*m.b4*m.b19*m.b20
                        + 192*m.b3*m.b4*m.b20*m.b21 + 192*m.b3*m.b4*m.b21*m.b22 + 192*m.b3*m.b4*m.b22*m.b23 + 128*m.b3*
                       m.b4*m.b23*m.b24 + 64*m.b3*m.b4*m.b24*m.b25 + 64*m.b3*m.b5*m.b6*m.b8 + 64*m.b3*m.b5*m.b7*m.b9 + 
                       64*m.b3*m.b5*m.b8*m.b10 + 64*m.b3*m.b5*m.b9*m.b11 + 64*m.b3*m.b5*m.b10*m.b12 + 64*m.b3*m.b5*m.b11
                       *m.b13 + 192*m.b3*m.b5*m.b12*m.b14 + 192*m.b3*m.b5*m.b13*m.b15 + 192*m.b3*m.b5*m.b14*m.b16 + 192*
                       m.b3*m.b5*m.b15*m.b17 + 192*m.b3*m.b5*m.b16*m.b18 + 192*m.b3*m.b5*m.b17*m.b19 + 192*m.b3*m.b5*
                       m.b18*m.b20 + 192*m.b3*m.b5*m.b19*m.b21 + 192*m.b3*m.b5*m.b20*m.b22 + 192*m.b3*m.b5*m.b21*m.b23
                        + 128*m.b3*m.b5*m.b22*m.b24 + 64*m.b3*m.b5*m.b23*m.b25 + 64*m.b3*m.b6*m.b7*m.b10 + 64*m.b3*m.b6*
                       m.b8*m.b11 + 64*m.b3*m.b6*m.b9*m.b12 + 64*m.b3*m.b6*m.b10*m.b13 + 192*m.b3*m.b6*m.b11*m.b14 + 192
                       *m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b6*m.b13*m.b16 + 192*m.b3*m.b6*m.b14*m.b17 + 192*m.b3*m.b6*
                       m.b15*m.b18 + 192*m.b3*m.b6*m.b16*m.b19 + 192*m.b3*m.b6*m.b17*m.b20 + 192*m.b3*m.b6*m.b18*m.b21
                        + 192*m.b3*m.b6*m.b19*m.b22 + 192*m.b3*m.b6*m.b20*m.b23 + 128*m.b3*m.b6*m.b21*m.b24 + 64*m.b3*
                       m.b6*m.b22*m.b25 + 64*m.b3*m.b7*m.b8*m.b12 + 64*m.b3*m.b7*m.b9*m.b13 + 192*m.b3*m.b7*m.b10*m.b14
                        + 192*m.b3*m.b7*m.b11*m.b15 + 192*m.b3*m.b7*m.b12*m.b16 + 192*m.b3*m.b7*m.b13*m.b17 + 192*m.b3*
                       m.b7*m.b14*m.b18 + 192*m.b3*m.b7*m.b15*m.b19 + 192*m.b3*m.b7*m.b16*m.b20 + 192*m.b3*m.b7*m.b17*
                       m.b21 + 192*m.b3*m.b7*m.b18*m.b22 + 192*m.b3*m.b7*m.b19*m.b23 + 128*m.b3*m.b7*m.b20*m.b24 + 64*
                       m.b3*m.b7*m.b21*m.b25 + 192*m.b3*m.b8*m.b9*m.b14 + 192*m.b3*m.b8*m.b10*m.b15 + 192*m.b3*m.b8*
                       m.b11*m.b16 + 192*m.b3*m.b8*m.b12*m.b17 + 192*m.b3*m.b8*m.b13*m.b18 + 192*m.b3*m.b8*m.b14*m.b19
                        + 192*m.b3*m.b8*m.b15*m.b20 + 192*m.b3*m.b8*m.b16*m.b21 + 192*m.b3*m.b8*m.b17*m.b22 + 192*m.b3*
                       m.b8*m.b18*m.b23 + 128*m.b3*m.b8*m.b19*m.b24 + 64*m.b3*m.b8*m.b20*m.b25 + 192*m.b3*m.b9*m.b10*
                       m.b16 + 192*m.b3*m.b9*m.b11*m.b17 + 192*m.b3*m.b9*m.b12*m.b18 + 192*m.b3*m.b9*m.b13*m.b19 + 192*
                       m.b3*m.b9*m.b14*m.b20 + 192*m.b3*m.b9*m.b15*m.b21 + 192*m.b3*m.b9*m.b16*m.b22 + 192*m.b3*m.b9*
                       m.b17*m.b23 + 128*m.b3*m.b9*m.b18*m.b24 + 64*m.b3*m.b9*m.b19*m.b25 + 192*m.b3*m.b10*m.b11*m.b18
                        + 192*m.b3*m.b10*m.b12*m.b19 + 192*m.b3*m.b10*m.b13*m.b20 + 192*m.b3*m.b10*m.b14*m.b21 + 192*
                       m.b3*m.b10*m.b15*m.b22 + 192*m.b3*m.b10*m.b16*m.b23 + 128*m.b3*m.b10*m.b17*m.b24 + 64*m.b3*m.b10*
                       m.b18*m.b25 + 192*m.b3*m.b11*m.b12*m.b20 + 192*m.b3*m.b11*m.b13*m.b21 + 192*m.b3*m.b11*m.b14*
                       m.b22 + 192*m.b3*m.b11*m.b15*m.b23 + 128*m.b3*m.b11*m.b16*m.b24 + 64*m.b3*m.b11*m.b17*m.b25 + 192
                       *m.b3*m.b12*m.b13*m.b22 + 192*m.b3*m.b12*m.b14*m.b23 + 128*m.b3*m.b12*m.b15*m.b24 + 64*m.b3*m.b12
                       *m.b16*m.b25 + 128*m.b3*m.b13*m.b14*m.b24 + 64*m.b3*m.b13*m.b15*m.b25 + 64*m.b4*m.b5*m.b6*m.b7 + 
                       64*m.b4*m.b5*m.b7*m.b8 + 64*m.b4*m.b5*m.b8*m.b9 + 64*m.b4*m.b5*m.b9*m.b10 + 64*m.b4*m.b5*m.b10*
                       m.b11 + 64*m.b4*m.b5*m.b11*m.b12 + 64*m.b4*m.b5*m.b12*m.b13 + 64*m.b4*m.b5*m.b13*m.b14 + 256*m.b4
                       *m.b5*m.b14*m.b15 + 256*m.b4*m.b5*m.b15*m.b16 + 256*m.b4*m.b5*m.b16*m.b17 + 256*m.b4*m.b5*m.b17*
                       m.b18 + 256*m.b4*m.b5*m.b18*m.b19 + 256*m.b4*m.b5*m.b19*m.b20 + 256*m.b4*m.b5*m.b20*m.b21 + 256*
                       m.b4*m.b5*m.b21*m.b22 + 192*m.b4*m.b5*m.b22*m.b23 + 128*m.b4*m.b5*m.b23*m.b24 + 64*m.b4*m.b5*
                       m.b24*m.b25 + 64*m.b4*m.b6*m.b7*m.b9 + 64*m.b4*m.b6*m.b8*m.b10 + 64*m.b4*m.b6*m.b9*m.b11 + 64*
                       m.b4*m.b6*m.b10*m.b12 + 64*m.b4*m.b6*m.b11*m.b13 + 64*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*m.b6*m.b13
                       *m.b15 + 256*m.b4*m.b6*m.b14*m.b16 + 256*m.b4*m.b6*m.b15*m.b17 + 256*m.b4*m.b6*m.b16*m.b18 + 256*
                       m.b4*m.b6*m.b17*m.b19 + 256*m.b4*m.b6*m.b18*m.b20 + 256*m.b4*m.b6*m.b19*m.b21 + 256*m.b4*m.b6*
                       m.b20*m.b22 + 192*m.b4*m.b6*m.b21*m.b23 + 128*m.b4*m.b6*m.b22*m.b24 + 64*m.b4*m.b6*m.b23*m.b25 + 
                       64*m.b4*m.b7*m.b8*m.b11 + 64*m.b4*m.b7*m.b9*m.b12 + 64*m.b4*m.b7*m.b10*m.b13 + 64*m.b4*m.b7*m.b11
                       *m.b14 + 256*m.b4*m.b7*m.b12*m.b15 + 256*m.b4*m.b7*m.b13*m.b16 + 256*m.b4*m.b7*m.b14*m.b17 + 256*
                       m.b4*m.b7*m.b15*m.b18 + 256*m.b4*m.b7*m.b16*m.b19 + 256*m.b4*m.b7*m.b17*m.b20 + 256*m.b4*m.b7*
                       m.b18*m.b21 + 256*m.b4*m.b7*m.b19*m.b22 + 192*m.b4*m.b7*m.b20*m.b23 + 128*m.b4*m.b7*m.b21*m.b24
                        + 64*m.b4*m.b7*m.b22*m.b25 + 64*m.b4*m.b8*m.b9*m.b13 + 64*m.b4*m.b8*m.b10*m.b14 + 256*m.b4*m.b8*
                       m.b11*m.b15 + 256*m.b4*m.b8*m.b12*m.b16 + 256*m.b4*m.b8*m.b13*m.b17 + 256*m.b4*m.b8*m.b14*m.b18
                        + 256*m.b4*m.b8*m.b15*m.b19 + 256*m.b4*m.b8*m.b16*m.b20 + 256*m.b4*m.b8*m.b17*m.b21 + 256*m.b4*
                       m.b8*m.b18*m.b22 + 192*m.b4*m.b8*m.b19*m.b23 + 128*m.b4*m.b8*m.b20*m.b24 + 64*m.b4*m.b8*m.b21*
                       m.b25 + 256*m.b4*m.b9*m.b10*m.b15 + 256*m.b4*m.b9*m.b11*m.b16 + 256*m.b4*m.b9*m.b12*m.b17 + 256*
                       m.b4*m.b9*m.b13*m.b18 + 256*m.b4*m.b9*m.b14*m.b19 + 256*m.b4*m.b9*m.b15*m.b20 + 256*m.b4*m.b9*
                       m.b16*m.b21 + 256*m.b4*m.b9*m.b17*m.b22 + 192*m.b4*m.b9*m.b18*m.b23 + 128*m.b4*m.b9*m.b19*m.b24
                        + 64*m.b4*m.b9*m.b20*m.b25 + 256*m.b4*m.b10*m.b11*m.b17 + 256*m.b4*m.b10*m.b12*m.b18 + 256*m.b4*
                       m.b10*m.b13*m.b19 + 256*m.b4*m.b10*m.b14*m.b20 + 256*m.b4*m.b10*m.b15*m.b21 + 256*m.b4*m.b10*
                       m.b16*m.b22 + 192*m.b4*m.b10*m.b17*m.b23 + 128*m.b4*m.b10*m.b18*m.b24 + 64*m.b4*m.b10*m.b19*m.b25
                        + 256*m.b4*m.b11*m.b12*m.b19 + 256*m.b4*m.b11*m.b13*m.b20 + 256*m.b4*m.b11*m.b14*m.b21 + 256*
                       m.b4*m.b11*m.b15*m.b22 + 192*m.b4*m.b11*m.b16*m.b23 + 128*m.b4*m.b11*m.b17*m.b24 + 64*m.b4*m.b11*
                       m.b18*m.b25 + 256*m.b4*m.b12*m.b13*m.b21 + 256*m.b4*m.b12*m.b14*m.b22 + 192*m.b4*m.b12*m.b15*
                       m.b23 + 128*m.b4*m.b12*m.b16*m.b24 + 64*m.b4*m.b12*m.b17*m.b25 + 192*m.b4*m.b13*m.b14*m.b23 + 128
                       *m.b4*m.b13*m.b15*m.b24 + 64*m.b4*m.b13*m.b16*m.b25 + 64*m.b4*m.b14*m.b15*m.b25 + 64*m.b5*m.b6*
                       m.b7*m.b8 + 64*m.b5*m.b6*m.b8*m.b9 + 64*m.b5*m.b6*m.b9*m.b10 + 64*m.b5*m.b6*m.b10*m.b11 + 64*m.b5
                       *m.b6*m.b11*m.b12 + 64*m.b5*m.b6*m.b12*m.b13 + 64*m.b5*m.b6*m.b13*m.b14 + 64*m.b5*m.b6*m.b14*
                       m.b15 + 320*m.b5*m.b6*m.b15*m.b16 + 320*m.b5*m.b6*m.b16*m.b17 + 320*m.b5*m.b6*m.b17*m.b18 + 320*
                       m.b5*m.b6*m.b18*m.b19 + 320*m.b5*m.b6*m.b19*m.b20 + 320*m.b5*m.b6*m.b20*m.b21 + 256*m.b5*m.b6*
                       m.b21*m.b22 + 192*m.b5*m.b6*m.b22*m.b23 + 128*m.b5*m.b6*m.b23*m.b24 + 64*m.b5*m.b6*m.b24*m.b25 + 
                       64*m.b5*m.b7*m.b8*m.b10 + 64*m.b5*m.b7*m.b9*m.b11 + 64*m.b5*m.b7*m.b10*m.b12 + 64*m.b5*m.b7*m.b11
                       *m.b13 + 64*m.b5*m.b7*m.b12*m.b14 + 64*m.b5*m.b7*m.b13*m.b15 + 320*m.b5*m.b7*m.b14*m.b16 + 320*
                       m.b5*m.b7*m.b15*m.b17 + 320*m.b5*m.b7*m.b16*m.b18 + 320*m.b5*m.b7*m.b17*m.b19 + 320*m.b5*m.b7*
                       m.b18*m.b20 + 320*m.b5*m.b7*m.b19*m.b21 + 256*m.b5*m.b7*m.b20*m.b22 + 192*m.b5*m.b7*m.b21*m.b23
                        + 128*m.b5*m.b7*m.b22*m.b24 + 64*m.b5*m.b7*m.b23*m.b25 + 64*m.b5*m.b8*m.b9*m.b12 + 64*m.b5*m.b8*
                       m.b10*m.b13 + 64*m.b5*m.b8*m.b11*m.b14 + 64*m.b5*m.b8*m.b12*m.b15 + 320*m.b5*m.b8*m.b13*m.b16 + 
                       320*m.b5*m.b8*m.b14*m.b17 + 320*m.b5*m.b8*m.b15*m.b18 + 320*m.b5*m.b8*m.b16*m.b19 + 320*m.b5*m.b8
                       *m.b17*m.b20 + 320*m.b5*m.b8*m.b18*m.b21 + 256*m.b5*m.b8*m.b19*m.b22 + 192*m.b5*m.b8*m.b20*m.b23
                        + 128*m.b5*m.b8*m.b21*m.b24 + 64*m.b5*m.b8*m.b22*m.b25 + 64*m.b5*m.b9*m.b10*m.b14 + 64*m.b5*m.b9
                       *m.b11*m.b15 + 320*m.b5*m.b9*m.b12*m.b16 + 320*m.b5*m.b9*m.b13*m.b17 + 320*m.b5*m.b9*m.b14*m.b18
                        + 320*m.b5*m.b9*m.b15*m.b19 + 320*m.b5*m.b9*m.b16*m.b20 + 320*m.b5*m.b9*m.b17*m.b21 + 256*m.b5*
                       m.b9*m.b18*m.b22 + 192*m.b5*m.b9*m.b19*m.b23 + 128*m.b5*m.b9*m.b20*m.b24 + 64*m.b5*m.b9*m.b21*
                       m.b25 + 320*m.b5*m.b10*m.b11*m.b16 + 320*m.b5*m.b10*m.b12*m.b17 + 320*m.b5*m.b10*m.b13*m.b18 + 
                       320*m.b5*m.b10*m.b14*m.b19 + 320*m.b5*m.b10*m.b15*m.b20 + 320*m.b5*m.b10*m.b16*m.b21 + 256*m.b5*
                       m.b10*m.b17*m.b22 + 192*m.b5*m.b10*m.b18*m.b23 + 128*m.b5*m.b10*m.b19*m.b24 + 64*m.b5*m.b10*m.b20
                       *m.b25 + 320*m.b5*m.b11*m.b12*m.b18 + 320*m.b5*m.b11*m.b13*m.b19 + 320*m.b5*m.b11*m.b14*m.b20 + 
                       320*m.b5*m.b11*m.b15*m.b21 + 256*m.b5*m.b11*m.b16*m.b22 + 192*m.b5*m.b11*m.b17*m.b23 + 128*m.b5*
                       m.b11*m.b18*m.b24 + 64*m.b5*m.b11*m.b19*m.b25 + 320*m.b5*m.b12*m.b13*m.b20 + 320*m.b5*m.b12*m.b14
                       *m.b21 + 256*m.b5*m.b12*m.b15*m.b22 + 192*m.b5*m.b12*m.b16*m.b23 + 128*m.b5*m.b12*m.b17*m.b24 + 
                       64*m.b5*m.b12*m.b18*m.b25 + 256*m.b5*m.b13*m.b14*m.b22 + 192*m.b5*m.b13*m.b15*m.b23 + 128*m.b5*
                       m.b13*m.b16*m.b24 + 64*m.b5*m.b13*m.b17*m.b25 + 128*m.b5*m.b14*m.b15*m.b24 + 64*m.b5*m.b14*m.b16*
                       m.b25 + 64*m.b6*m.b7*m.b8*m.b9 + 64*m.b6*m.b7*m.b9*m.b10 + 64*m.b6*m.b7*m.b10*m.b11 + 64*m.b6*
                       m.b7*m.b11*m.b12 + 64*m.b6*m.b7*m.b12*m.b13 + 64*m.b6*m.b7*m.b13*m.b14 + 64*m.b6*m.b7*m.b14*m.b15
                        + 64*m.b6*m.b7*m.b15*m.b16 + 384*m.b6*m.b7*m.b16*m.b17 + 384*m.b6*m.b7*m.b17*m.b18 + 384*m.b6*
                       m.b7*m.b18*m.b19 + 384*m.b6*m.b7*m.b19*m.b20 + 320*m.b6*m.b7*m.b20*m.b21 + 256*m.b6*m.b7*m.b21*
                       m.b22 + 192*m.b6*m.b7*m.b22*m.b23 + 128*m.b6*m.b7*m.b23*m.b24 + 64*m.b6*m.b7*m.b24*m.b25 + 64*
                       m.b6*m.b8*m.b9*m.b11 + 64*m.b6*m.b8*m.b10*m.b12 + 64*m.b6*m.b8*m.b11*m.b13 + 64*m.b6*m.b8*m.b12*
                       m.b14 + 64*m.b6*m.b8*m.b13*m.b15 + 64*m.b6*m.b8*m.b14*m.b16 + 384*m.b6*m.b8*m.b15*m.b17 + 384*
                       m.b6*m.b8*m.b16*m.b18 + 384*m.b6*m.b8*m.b17*m.b19 + 384*m.b6*m.b8*m.b18*m.b20 + 320*m.b6*m.b8*
                       m.b19*m.b21 + 256*m.b6*m.b8*m.b20*m.b22 + 192*m.b6*m.b8*m.b21*m.b23 + 128*m.b6*m.b8*m.b22*m.b24
                        + 64*m.b6*m.b8*m.b23*m.b25 + 64*m.b6*m.b9*m.b10*m.b13 + 64*m.b6*m.b9*m.b11*m.b14 + 64*m.b6*m.b9*
                       m.b12*m.b15 + 64*m.b6*m.b9*m.b13*m.b16 + 384*m.b6*m.b9*m.b14*m.b17 + 384*m.b6*m.b9*m.b15*m.b18 + 
                       384*m.b6*m.b9*m.b16*m.b19 + 384*m.b6*m.b9*m.b17*m.b20 + 320*m.b6*m.b9*m.b18*m.b21 + 256*m.b6*m.b9
                       *m.b19*m.b22 + 192*m.b6*m.b9*m.b20*m.b23 + 128*m.b6*m.b9*m.b21*m.b24 + 64*m.b6*m.b9*m.b22*m.b25
                        + 64*m.b6*m.b10*m.b11*m.b15 + 64*m.b6*m.b10*m.b12*m.b16 + 384*m.b6*m.b10*m.b13*m.b17 + 384*m.b6*
                       m.b10*m.b14*m.b18 + 384*m.b6*m.b10*m.b15*m.b19 + 384*m.b6*m.b10*m.b16*m.b20 + 320*m.b6*m.b10*
                       m.b17*m.b21 + 256*m.b6*m.b10*m.b18*m.b22 + 192*m.b6*m.b10*m.b19*m.b23 + 128*m.b6*m.b10*m.b20*
                       m.b24 + 64*m.b6*m.b10*m.b21*m.b25 + 384*m.b6*m.b11*m.b12*m.b17 + 384*m.b6*m.b11*m.b13*m.b18 + 384
                       *m.b6*m.b11*m.b14*m.b19 + 384*m.b6*m.b11*m.b15*m.b20 + 320*m.b6*m.b11*m.b16*m.b21 + 256*m.b6*
                       m.b11*m.b17*m.b22 + 192*m.b6*m.b11*m.b18*m.b23 + 128*m.b6*m.b11*m.b19*m.b24 + 64*m.b6*m.b11*m.b20
                       *m.b25 + 384*m.b6*m.b12*m.b13*m.b19 + 384*m.b6*m.b12*m.b14*m.b20 + 320*m.b6*m.b12*m.b15*m.b21 + 
                       256*m.b6*m.b12*m.b16*m.b22 + 192*m.b6*m.b12*m.b17*m.b23 + 128*m.b6*m.b12*m.b18*m.b24 + 64*m.b6*
                       m.b12*m.b19*m.b25 + 320*m.b6*m.b13*m.b14*m.b21 + 256*m.b6*m.b13*m.b15*m.b22 + 192*m.b6*m.b13*
                       m.b16*m.b23 + 128*m.b6*m.b13*m.b17*m.b24 + 64*m.b6*m.b13*m.b18*m.b25 + 192*m.b6*m.b14*m.b15*m.b23
                        + 128*m.b6*m.b14*m.b16*m.b24 + 64*m.b6*m.b14*m.b17*m.b25 + 64*m.b6*m.b15*m.b16*m.b25 + 64*m.b7*
                       m.b8*m.b9*m.b10 + 64*m.b7*m.b8*m.b10*m.b11 + 64*m.b7*m.b8*m.b11*m.b12 + 64*m.b7*m.b8*m.b12*m.b13
                        + 64*m.b7*m.b8*m.b13*m.b14 + 64*m.b7*m.b8*m.b14*m.b15 + 64*m.b7*m.b8*m.b15*m.b16 + 64*m.b7*m.b8*
                       m.b16*m.b17 + 448*m.b7*m.b8*m.b17*m.b18 + 448*m.b7*m.b8*m.b18*m.b19 + 384*m.b7*m.b8*m.b19*m.b20
                        + 320*m.b7*m.b8*m.b20*m.b21 + 256*m.b7*m.b8*m.b21*m.b22 + 192*m.b7*m.b8*m.b22*m.b23 + 128*m.b7*
                       m.b8*m.b23*m.b24 + 64*m.b7*m.b8*m.b24*m.b25 + 64*m.b7*m.b9*m.b10*m.b12 + 64*m.b7*m.b9*m.b11*m.b13
                        + 64*m.b7*m.b9*m.b12*m.b14 + 64*m.b7*m.b9*m.b13*m.b15 + 64*m.b7*m.b9*m.b14*m.b16 + 64*m.b7*m.b9*
                       m.b15*m.b17 + 448*m.b7*m.b9*m.b16*m.b18 + 448*m.b7*m.b9*m.b17*m.b19 + 384*m.b7*m.b9*m.b18*m.b20
                        + 320*m.b7*m.b9*m.b19*m.b21 + 256*m.b7*m.b9*m.b20*m.b22 + 192*m.b7*m.b9*m.b21*m.b23 + 128*m.b7*
                       m.b9*m.b22*m.b24 + 64*m.b7*m.b9*m.b23*m.b25 + 64*m.b7*m.b10*m.b11*m.b14 + 64*m.b7*m.b10*m.b12*
                       m.b15 + 64*m.b7*m.b10*m.b13*m.b16 + 64*m.b7*m.b10*m.b14*m.b17 + 448*m.b7*m.b10*m.b15*m.b18 + 448*
                       m.b7*m.b10*m.b16*m.b19 + 384*m.b7*m.b10*m.b17*m.b20 + 320*m.b7*m.b10*m.b18*m.b21 + 256*m.b7*m.b10
                       *m.b19*m.b22 + 192*m.b7*m.b10*m.b20*m.b23 + 128*m.b7*m.b10*m.b21*m.b24 + 64*m.b7*m.b10*m.b22*
                       m.b25 + 64*m.b7*m.b11*m.b12*m.b16 + 64*m.b7*m.b11*m.b13*m.b17 + 448*m.b7*m.b11*m.b14*m.b18 + 448*
                       m.b7*m.b11*m.b15*m.b19 + 384*m.b7*m.b11*m.b16*m.b20 + 320*m.b7*m.b11*m.b17*m.b21 + 256*m.b7*m.b11
                       *m.b18*m.b22 + 192*m.b7*m.b11*m.b19*m.b23 + 128*m.b7*m.b11*m.b20*m.b24 + 64*m.b7*m.b11*m.b21*
                       m.b25 + 448*m.b7*m.b12*m.b13*m.b18 + 448*m.b7*m.b12*m.b14*m.b19 + 384*m.b7*m.b12*m.b15*m.b20 + 
                       320*m.b7*m.b12*m.b16*m.b21 + 256*m.b7*m.b12*m.b17*m.b22 + 192*m.b7*m.b12*m.b18*m.b23 + 128*m.b7*
                       m.b12*m.b19*m.b24 + 64*m.b7*m.b12*m.b20*m.b25 + 384*m.b7*m.b13*m.b14*m.b20 + 320*m.b7*m.b13*m.b15
                       *m.b21 + 256*m.b7*m.b13*m.b16*m.b22 + 192*m.b7*m.b13*m.b17*m.b23 + 128*m.b7*m.b13*m.b18*m.b24 + 
                       64*m.b7*m.b13*m.b19*m.b25 + 256*m.b7*m.b14*m.b15*m.b22 + 192*m.b7*m.b14*m.b16*m.b23 + 128*m.b7*
                       m.b14*m.b17*m.b24 + 64*m.b7*m.b14*m.b18*m.b25 + 128*m.b7*m.b15*m.b16*m.b24 + 64*m.b7*m.b15*m.b17*
                       m.b25 + 64*m.b8*m.b9*m.b10*m.b11 + 64*m.b8*m.b9*m.b11*m.b12 + 64*m.b8*m.b9*m.b12*m.b13 + 64*m.b8*
                       m.b9*m.b13*m.b14 + 64*m.b8*m.b9*m.b14*m.b15 + 64*m.b8*m.b9*m.b15*m.b16 + 64*m.b8*m.b9*m.b16*m.b17
                        + 64*m.b8*m.b9*m.b17*m.b18 + 448*m.b8*m.b9*m.b18*m.b19 + 384*m.b8*m.b9*m.b19*m.b20 + 320*m.b8*
                       m.b9*m.b20*m.b21 + 256*m.b8*m.b9*m.b21*m.b22 + 192*m.b8*m.b9*m.b22*m.b23 + 128*m.b8*m.b9*m.b23*
                       m.b24 + 64*m.b8*m.b9*m.b24*m.b25 + 64*m.b8*m.b10*m.b11*m.b13 + 64*m.b8*m.b10*m.b12*m.b14 + 64*
                       m.b8*m.b10*m.b13*m.b15 + 64*m.b8*m.b10*m.b14*m.b16 + 64*m.b8*m.b10*m.b15*m.b17 + 64*m.b8*m.b10*
                       m.b16*m.b18 + 448*m.b8*m.b10*m.b17*m.b19 + 384*m.b8*m.b10*m.b18*m.b20 + 320*m.b8*m.b10*m.b19*
                       m.b21 + 256*m.b8*m.b10*m.b20*m.b22 + 192*m.b8*m.b10*m.b21*m.b23 + 128*m.b8*m.b10*m.b22*m.b24 + 64
                       *m.b8*m.b10*m.b23*m.b25 + 64*m.b8*m.b11*m.b12*m.b15 + 64*m.b8*m.b11*m.b13*m.b16 + 64*m.b8*m.b11*
                       m.b14*m.b17 + 64*m.b8*m.b11*m.b15*m.b18 + 448*m.b8*m.b11*m.b16*m.b19 + 384*m.b8*m.b11*m.b17*m.b20
                        + 320*m.b8*m.b11*m.b18*m.b21 + 256*m.b8*m.b11*m.b19*m.b22 + 192*m.b8*m.b11*m.b20*m.b23 + 128*
                       m.b8*m.b11*m.b21*m.b24 + 64*m.b8*m.b11*m.b22*m.b25 + 64*m.b8*m.b12*m.b13*m.b17 + 64*m.b8*m.b12*
                       m.b14*m.b18 + 448*m.b8*m.b12*m.b15*m.b19 + 384*m.b8*m.b12*m.b16*m.b20 + 320*m.b8*m.b12*m.b17*
                       m.b21 + 256*m.b8*m.b12*m.b18*m.b22 + 192*m.b8*m.b12*m.b19*m.b23 + 128*m.b8*m.b12*m.b20*m.b24 + 64
                       *m.b8*m.b12*m.b21*m.b25 + 448*m.b8*m.b13*m.b14*m.b19 + 384*m.b8*m.b13*m.b15*m.b20 + 320*m.b8*
                       m.b13*m.b16*m.b21 + 256*m.b8*m.b13*m.b17*m.b22 + 192*m.b8*m.b13*m.b18*m.b23 + 128*m.b8*m.b13*
                       m.b19*m.b24 + 64*m.b8*m.b13*m.b20*m.b25 + 320*m.b8*m.b14*m.b15*m.b21 + 256*m.b8*m.b14*m.b16*m.b22
                        + 192*m.b8*m.b14*m.b17*m.b23 + 128*m.b8*m.b14*m.b18*m.b24 + 64*m.b8*m.b14*m.b19*m.b25 + 192*m.b8
                       *m.b15*m.b16*m.b23 + 128*m.b8*m.b15*m.b17*m.b24 + 64*m.b8*m.b15*m.b18*m.b25 + 64*m.b8*m.b16*m.b17
                       *m.b25 + 64*m.b9*m.b10*m.b11*m.b12 + 64*m.b9*m.b10*m.b12*m.b13 + 64*m.b9*m.b10*m.b13*m.b14 + 64*
                       m.b9*m.b10*m.b14*m.b15 + 64*m.b9*m.b10*m.b15*m.b16 + 64*m.b9*m.b10*m.b16*m.b17 + 64*m.b9*m.b10*
                       m.b17*m.b18 + 64*m.b9*m.b10*m.b18*m.b19 + 384*m.b9*m.b10*m.b19*m.b20 + 320*m.b9*m.b10*m.b20*m.b21
                        + 256*m.b9*m.b10*m.b21*m.b22 + 192*m.b9*m.b10*m.b22*m.b23 + 128*m.b9*m.b10*m.b23*m.b24 + 64*m.b9
                       *m.b10*m.b24*m.b25 + 64*m.b9*m.b11*m.b12*m.b14 + 64*m.b9*m.b11*m.b13*m.b15 + 64*m.b9*m.b11*m.b14*
                       m.b16 + 64*m.b9*m.b11*m.b15*m.b17 + 64*m.b9*m.b11*m.b16*m.b18 + 64*m.b9*m.b11*m.b17*m.b19 + 384*
                       m.b9*m.b11*m.b18*m.b20 + 320*m.b9*m.b11*m.b19*m.b21 + 256*m.b9*m.b11*m.b20*m.b22 + 192*m.b9*m.b11
                       *m.b21*m.b23 + 128*m.b9*m.b11*m.b22*m.b24 + 64*m.b9*m.b11*m.b23*m.b25 + 64*m.b9*m.b12*m.b13*m.b16
                        + 64*m.b9*m.b12*m.b14*m.b17 + 64*m.b9*m.b12*m.b15*m.b18 + 64*m.b9*m.b12*m.b16*m.b19 + 384*m.b9*
                       m.b12*m.b17*m.b20 + 320*m.b9*m.b12*m.b18*m.b21 + 256*m.b9*m.b12*m.b19*m.b22 + 192*m.b9*m.b12*
                       m.b20*m.b23 + 128*m.b9*m.b12*m.b21*m.b24 + 64*m.b9*m.b12*m.b22*m.b25 + 64*m.b9*m.b13*m.b14*m.b18
                        + 64*m.b9*m.b13*m.b15*m.b19 + 384*m.b9*m.b13*m.b16*m.b20 + 320*m.b9*m.b13*m.b17*m.b21 + 256*m.b9
                       *m.b13*m.b18*m.b22 + 192*m.b9*m.b13*m.b19*m.b23 + 128*m.b9*m.b13*m.b20*m.b24 + 64*m.b9*m.b13*
                       m.b21*m.b25 + 384*m.b9*m.b14*m.b15*m.b20 + 320*m.b9*m.b14*m.b16*m.b21 + 256*m.b9*m.b14*m.b17*
                       m.b22 + 192*m.b9*m.b14*m.b18*m.b23 + 128*m.b9*m.b14*m.b19*m.b24 + 64*m.b9*m.b14*m.b20*m.b25 + 256
                       *m.b9*m.b15*m.b16*m.b22 + 192*m.b9*m.b15*m.b17*m.b23 + 128*m.b9*m.b15*m.b18*m.b24 + 64*m.b9*m.b15
                       *m.b19*m.b25 + 128*m.b9*m.b16*m.b17*m.b24 + 64*m.b9*m.b16*m.b18*m.b25 + 64*m.b10*m.b11*m.b12*
                       m.b13 + 64*m.b10*m.b11*m.b13*m.b14 + 64*m.b10*m.b11*m.b14*m.b15 + 64*m.b10*m.b11*m.b15*m.b16 + 64
                       *m.b10*m.b11*m.b16*m.b17 + 64*m.b10*m.b11*m.b17*m.b18 + 64*m.b10*m.b11*m.b18*m.b19 + 64*m.b10*
                       m.b11*m.b19*m.b20 + 320*m.b10*m.b11*m.b20*m.b21 + 256*m.b10*m.b11*m.b21*m.b22 + 192*m.b10*m.b11*
                       m.b22*m.b23 + 128*m.b10*m.b11*m.b23*m.b24 + 64*m.b10*m.b11*m.b24*m.b25 + 64*m.b10*m.b12*m.b13*
                       m.b15 + 64*m.b10*m.b12*m.b14*m.b16 + 64*m.b10*m.b12*m.b15*m.b17 + 64*m.b10*m.b12*m.b16*m.b18 + 64
                       *m.b10*m.b12*m.b17*m.b19 + 64*m.b10*m.b12*m.b18*m.b20 + 320*m.b10*m.b12*m.b19*m.b21 + 256*m.b10*
                       m.b12*m.b20*m.b22 + 192*m.b10*m.b12*m.b21*m.b23 + 128*m.b10*m.b12*m.b22*m.b24 + 64*m.b10*m.b12*
                       m.b23*m.b25 + 64*m.b10*m.b13*m.b14*m.b17 + 64*m.b10*m.b13*m.b15*m.b18 + 64*m.b10*m.b13*m.b16*
                       m.b19 + 64*m.b10*m.b13*m.b17*m.b20 + 320*m.b10*m.b13*m.b18*m.b21 + 256*m.b10*m.b13*m.b19*m.b22 + 
                       192*m.b10*m.b13*m.b20*m.b23 + 128*m.b10*m.b13*m.b21*m.b24 + 64*m.b10*m.b13*m.b22*m.b25 + 64*m.b10
                       *m.b14*m.b15*m.b19 + 64*m.b10*m.b14*m.b16*m.b20 + 320*m.b10*m.b14*m.b17*m.b21 + 256*m.b10*m.b14*
                       m.b18*m.b22 + 192*m.b10*m.b14*m.b19*m.b23 + 128*m.b10*m.b14*m.b20*m.b24 + 64*m.b10*m.b14*m.b21*
                       m.b25 + 320*m.b10*m.b15*m.b16*m.b21 + 256*m.b10*m.b15*m.b17*m.b22 + 192*m.b10*m.b15*m.b18*m.b23
                        + 128*m.b10*m.b15*m.b19*m.b24 + 64*m.b10*m.b15*m.b20*m.b25 + 192*m.b10*m.b16*m.b17*m.b23 + 128*
                       m.b10*m.b16*m.b18*m.b24 + 64*m.b10*m.b16*m.b19*m.b25 + 64*m.b10*m.b17*m.b18*m.b25 + 64*m.b11*
                       m.b12*m.b13*m.b14 + 64*m.b11*m.b12*m.b14*m.b15 + 64*m.b11*m.b12*m.b15*m.b16 + 64*m.b11*m.b12*
                       m.b16*m.b17 + 64*m.b11*m.b12*m.b17*m.b18 + 64*m.b11*m.b12*m.b18*m.b19 + 64*m.b11*m.b12*m.b19*
                       m.b20 + 64*m.b11*m.b12*m.b20*m.b21 + 256*m.b11*m.b12*m.b21*m.b22 + 192*m.b11*m.b12*m.b22*m.b23 + 
                       128*m.b11*m.b12*m.b23*m.b24 + 64*m.b11*m.b12*m.b24*m.b25 + 64*m.b11*m.b13*m.b14*m.b16 + 64*m.b11*
                       m.b13*m.b15*m.b17 + 64*m.b11*m.b13*m.b16*m.b18 + 64*m.b11*m.b13*m.b17*m.b19 + 64*m.b11*m.b13*
                       m.b18*m.b20 + 64*m.b11*m.b13*m.b19*m.b21 + 256*m.b11*m.b13*m.b20*m.b22 + 192*m.b11*m.b13*m.b21*
                       m.b23 + 128*m.b11*m.b13*m.b22*m.b24 + 64*m.b11*m.b13*m.b23*m.b25 + 64*m.b11*m.b14*m.b15*m.b18 + 
                       64*m.b11*m.b14*m.b16*m.b19 + 64*m.b11*m.b14*m.b17*m.b20 + 64*m.b11*m.b14*m.b18*m.b21 + 256*m.b11*
                       m.b14*m.b19*m.b22 + 192*m.b11*m.b14*m.b20*m.b23 + 128*m.b11*m.b14*m.b21*m.b24 + 64*m.b11*m.b14*
                       m.b22*m.b25 + 64*m.b11*m.b15*m.b16*m.b20 + 64*m.b11*m.b15*m.b17*m.b21 + 256*m.b11*m.b15*m.b18*
                       m.b22 + 192*m.b11*m.b15*m.b19*m.b23 + 128*m.b11*m.b15*m.b20*m.b24 + 64*m.b11*m.b15*m.b21*m.b25 + 
                       256*m.b11*m.b16*m.b17*m.b22 + 192*m.b11*m.b16*m.b18*m.b23 + 128*m.b11*m.b16*m.b19*m.b24 + 64*
                       m.b11*m.b16*m.b20*m.b25 + 128*m.b11*m.b17*m.b18*m.b24 + 64*m.b11*m.b17*m.b19*m.b25 + 64*m.b12*
                       m.b13*m.b14*m.b15 + 64*m.b12*m.b13*m.b15*m.b16 + 64*m.b12*m.b13*m.b16*m.b17 + 64*m.b12*m.b13*
                       m.b17*m.b18 + 64*m.b12*m.b13*m.b18*m.b19 + 64*m.b12*m.b13*m.b19*m.b20 + 64*m.b12*m.b13*m.b20*
                       m.b21 + 64*m.b12*m.b13*m.b21*m.b22 + 192*m.b12*m.b13*m.b22*m.b23 + 128*m.b12*m.b13*m.b23*m.b24 + 
                       64*m.b12*m.b13*m.b24*m.b25 + 64*m.b12*m.b14*m.b15*m.b17 + 64*m.b12*m.b14*m.b16*m.b18 + 64*m.b12*
                       m.b14*m.b17*m.b19 + 64*m.b12*m.b14*m.b18*m.b20 + 64*m.b12*m.b14*m.b19*m.b21 + 64*m.b12*m.b14*
                       m.b20*m.b22 + 192*m.b12*m.b14*m.b21*m.b23 + 128*m.b12*m.b14*m.b22*m.b24 + 64*m.b12*m.b14*m.b23*
                       m.b25 + 64*m.b12*m.b15*m.b16*m.b19 + 64*m.b12*m.b15*m.b17*m.b20 + 64*m.b12*m.b15*m.b18*m.b21 + 64
                       *m.b12*m.b15*m.b19*m.b22 + 192*m.b12*m.b15*m.b20*m.b23 + 128*m.b12*m.b15*m.b21*m.b24 + 64*m.b12*
                       m.b15*m.b22*m.b25 + 64*m.b12*m.b16*m.b17*m.b21 + 64*m.b12*m.b16*m.b18*m.b22 + 192*m.b12*m.b16*
                       m.b19*m.b23 + 128*m.b12*m.b16*m.b20*m.b24 + 64*m.b12*m.b16*m.b21*m.b25 + 192*m.b12*m.b17*m.b18*
                       m.b23 + 128*m.b12*m.b17*m.b19*m.b24 + 64*m.b12*m.b17*m.b20*m.b25 + 64*m.b12*m.b18*m.b19*m.b25 + 
                       64*m.b13*m.b14*m.b15*m.b16 + 64*m.b13*m.b14*m.b16*m.b17 + 64*m.b13*m.b14*m.b17*m.b18 + 64*m.b13*
                       m.b14*m.b18*m.b19 + 64*m.b13*m.b14*m.b19*m.b20 + 64*m.b13*m.b14*m.b20*m.b21 + 64*m.b13*m.b14*
                       m.b21*m.b22 + 64*m.b13*m.b14*m.b22*m.b23 + 128*m.b13*m.b14*m.b23*m.b24 + 64*m.b13*m.b14*m.b24*
                       m.b25 + 64*m.b13*m.b15*m.b16*m.b18 + 64*m.b13*m.b15*m.b17*m.b19 + 64*m.b13*m.b15*m.b18*m.b20 + 64
                       *m.b13*m.b15*m.b19*m.b21 + 64*m.b13*m.b15*m.b20*m.b22 + 64*m.b13*m.b15*m.b21*m.b23 + 128*m.b13*
                       m.b15*m.b22*m.b24 + 64*m.b13*m.b15*m.b23*m.b25 + 64*m.b13*m.b16*m.b17*m.b20 + 64*m.b13*m.b16*
                       m.b18*m.b21 + 64*m.b13*m.b16*m.b19*m.b22 + 64*m.b13*m.b16*m.b20*m.b23 + 128*m.b13*m.b16*m.b21*
                       m.b24 + 64*m.b13*m.b16*m.b22*m.b25 + 64*m.b13*m.b17*m.b18*m.b22 + 64*m.b13*m.b17*m.b19*m.b23 + 
                       128*m.b13*m.b17*m.b20*m.b24 + 64*m.b13*m.b17*m.b21*m.b25 + 128*m.b13*m.b18*m.b19*m.b24 + 64*m.b13
                       *m.b18*m.b20*m.b25 + 64*m.b14*m.b15*m.b16*m.b17 + 64*m.b14*m.b15*m.b17*m.b18 + 64*m.b14*m.b15*
                       m.b18*m.b19 + 64*m.b14*m.b15*m.b19*m.b20 + 64*m.b14*m.b15*m.b20*m.b21 + 64*m.b14*m.b15*m.b21*
                       m.b22 + 64*m.b14*m.b15*m.b22*m.b23 + 64*m.b14*m.b15*m.b23*m.b24 + 64*m.b14*m.b15*m.b24*m.b25 + 64
                       *m.b14*m.b16*m.b17*m.b19 + 64*m.b14*m.b16*m.b18*m.b20 + 64*m.b14*m.b16*m.b19*m.b21 + 64*m.b14*
                       m.b16*m.b20*m.b22 + 64*m.b14*m.b16*m.b21*m.b23 + 64*m.b14*m.b16*m.b22*m.b24 + 64*m.b14*m.b16*
                       m.b23*m.b25 + 64*m.b14*m.b17*m.b18*m.b21 + 64*m.b14*m.b17*m.b19*m.b22 + 64*m.b14*m.b17*m.b20*
                       m.b23 + 64*m.b14*m.b17*m.b21*m.b24 + 64*m.b14*m.b17*m.b22*m.b25 + 64*m.b14*m.b18*m.b19*m.b23 + 64
                       *m.b14*m.b18*m.b20*m.b24 + 64*m.b14*m.b18*m.b21*m.b25 + 64*m.b14*m.b19*m.b20*m.b25 + 64*m.b15*
                       m.b16*m.b17*m.b18 + 64*m.b15*m.b16*m.b18*m.b19 + 64*m.b15*m.b16*m.b19*m.b20 + 64*m.b15*m.b16*
                       m.b20*m.b21 + 64*m.b15*m.b16*m.b21*m.b22 + 64*m.b15*m.b16*m.b22*m.b23 + 64*m.b15*m.b16*m.b23*
                       m.b24 + 64*m.b15*m.b16*m.b24*m.b25 + 64*m.b15*m.b17*m.b18*m.b20 + 64*m.b15*m.b17*m.b19*m.b21 + 64
                       *m.b15*m.b17*m.b20*m.b22 + 64*m.b15*m.b17*m.b21*m.b23 + 64*m.b15*m.b17*m.b22*m.b24 + 64*m.b15*
                       m.b17*m.b23*m.b25 + 64*m.b15*m.b18*m.b19*m.b22 + 64*m.b15*m.b18*m.b20*m.b23 + 64*m.b15*m.b18*
                       m.b21*m.b24 + 64*m.b15*m.b18*m.b22*m.b25 + 64*m.b15*m.b19*m.b20*m.b24 + 64*m.b15*m.b19*m.b21*
                       m.b25 + 64*m.b16*m.b17*m.b18*m.b19 + 64*m.b16*m.b17*m.b19*m.b20 + 64*m.b16*m.b17*m.b20*m.b21 + 64
                       *m.b16*m.b17*m.b21*m.b22 + 64*m.b16*m.b17*m.b22*m.b23 + 64*m.b16*m.b17*m.b23*m.b24 + 64*m.b16*
                       m.b17*m.b24*m.b25 + 64*m.b16*m.b18*m.b19*m.b21 + 64*m.b16*m.b18*m.b20*m.b22 + 64*m.b16*m.b18*
                       m.b21*m.b23 + 64*m.b16*m.b18*m.b22*m.b24 + 64*m.b16*m.b18*m.b23*m.b25 + 64*m.b16*m.b19*m.b20*
                       m.b23 + 64*m.b16*m.b19*m.b21*m.b24 + 64*m.b16*m.b19*m.b22*m.b25 + 64*m.b16*m.b20*m.b21*m.b25 + 64
                       *m.b17*m.b18*m.b19*m.b20 + 64*m.b17*m.b18*m.b20*m.b21 + 64*m.b17*m.b18*m.b21*m.b22 + 64*m.b17*
                       m.b18*m.b22*m.b23 + 64*m.b17*m.b18*m.b23*m.b24 + 64*m.b17*m.b18*m.b24*m.b25 + 64*m.b17*m.b19*
                       m.b20*m.b22 + 64*m.b17*m.b19*m.b21*m.b23 + 64*m.b17*m.b19*m.b22*m.b24 + 64*m.b17*m.b19*m.b23*
                       m.b25 + 64*m.b17*m.b20*m.b21*m.b24 + 64*m.b17*m.b20*m.b22*m.b25 + 64*m.b18*m.b19*m.b20*m.b21 + 64
                       *m.b18*m.b19*m.b21*m.b22 + 64*m.b18*m.b19*m.b22*m.b23 + 64*m.b18*m.b19*m.b23*m.b24 + 64*m.b18*
                       m.b19*m.b24*m.b25 + 64*m.b18*m.b20*m.b21*m.b23 + 64*m.b18*m.b20*m.b22*m.b24 + 64*m.b18*m.b20*
                       m.b23*m.b25 + 64*m.b18*m.b21*m.b22*m.b25 + 64*m.b19*m.b20*m.b21*m.b22 + 64*m.b19*m.b20*m.b22*
                       m.b23 + 64*m.b19*m.b20*m.b23*m.b24 + 64*m.b19*m.b20*m.b24*m.b25 + 64*m.b19*m.b21*m.b22*m.b24 + 64
                       *m.b19*m.b21*m.b23*m.b25 + 64*m.b20*m.b21*m.b22*m.b23 + 64*m.b20*m.b21*m.b23*m.b24 + 64*m.b20*
                       m.b21*m.b24*m.b25 + 64*m.b20*m.b22*m.b23*m.b25 + 64*m.b21*m.b22*m.b23*m.b24 + 64*m.b21*m.b22*
                       m.b24*m.b25 + 64*m.b22*m.b23*m.b24*m.b25 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*
                       m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*
                       m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*m.b13 - 64*m.b1*m.b2*m.b14 - 
                       64*m.b1*m.b2*m.b15 - 64*m.b1*m.b2*m.b16 - 64*m.b1*m.b2*m.b17 - 64*m.b1*m.b2*m.b18 - 64*m.b1*m.b2*
                       m.b19 - 64*m.b1*m.b2*m.b20 - 64*m.b1*m.b2*m.b21 - 64*m.b1*m.b2*m.b22 - 64*m.b1*m.b2*m.b23 - 64*
                       m.b1*m.b2*m.b24 - 32*m.b1*m.b2*m.b25 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6
                        - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*
                       m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 64*m.b1*m.b3*m.b14 - 64*m.b1*m.b3*m.b15 - 64*
                       m.b1*m.b3*m.b16 - 64*m.b1*m.b3*m.b17 - 64*m.b1*m.b3*m.b18 - 64*m.b1*m.b3*m.b19 - 64*m.b1*m.b3*
                       m.b20 - 64*m.b1*m.b3*m.b21 - 64*m.b1*m.b3*m.b22 - 64*m.b1*m.b3*m.b23 - 32*m.b1*m.b3*m.b24 - 32*
                       m.b1*m.b3*m.b25 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8
                        - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64*m.b1*m.b4*m.b12 - 64*m.b1*
                       m.b4*m.b13 - 64*m.b1*m.b4*m.b14 - 64*m.b1*m.b4*m.b15 - 64*m.b1*m.b4*m.b16 - 64*m.b1*m.b4*m.b17 - 
                       64*m.b1*m.b4*m.b18 - 64*m.b1*m.b4*m.b19 - 64*m.b1*m.b4*m.b20 - 64*m.b1*m.b4*m.b21 - 64*m.b1*m.b4*
                       m.b22 - 32*m.b1*m.b4*m.b23 - 32*m.b1*m.b4*m.b24 - 32*m.b1*m.b4*m.b25 - 64*m.b1*m.b5*m.b6 - 64*
                       m.b1*m.b5*m.b7 - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*m.b11
                        - 64*m.b1*m.b5*m.b12 - 64*m.b1*m.b5*m.b13 - 64*m.b1*m.b5*m.b14 - 64*m.b1*m.b5*m.b15 - 64*m.b1*
                       m.b5*m.b16 - 64*m.b1*m.b5*m.b17 - 64*m.b1*m.b5*m.b18 - 64*m.b1*m.b5*m.b19 - 64*m.b1*m.b5*m.b20 - 
                       64*m.b1*m.b5*m.b21 - 32*m.b1*m.b5*m.b22 - 32*m.b1*m.b5*m.b23 - 32*m.b1*m.b5*m.b24 - 32*m.b1*m.b5*
                       m.b25 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*
                       m.b6*m.b11 - 64*m.b1*m.b6*m.b12 - 64*m.b1*m.b6*m.b13 - 64*m.b1*m.b6*m.b14 - 64*m.b1*m.b6*m.b15 - 
                       64*m.b1*m.b6*m.b16 - 64*m.b1*m.b6*m.b17 - 64*m.b1*m.b6*m.b18 - 64*m.b1*m.b6*m.b19 - 64*m.b1*m.b6*
                       m.b20 - 32*m.b1*m.b6*m.b21 - 32*m.b1*m.b6*m.b22 - 32*m.b1*m.b6*m.b23 - 32*m.b1*m.b6*m.b24 - 32*
                       m.b1*m.b6*m.b25 - 64*m.b1*m.b7*m.b8 - 64*m.b1*m.b7*m.b9 - 64*m.b1*m.b7*m.b10 - 64*m.b1*m.b7*m.b11
                        - 64*m.b1*m.b7*m.b12 - 32*m.b1*m.b7*m.b13 - 64*m.b1*m.b7*m.b14 - 64*m.b1*m.b7*m.b15 - 64*m.b1*
                       m.b7*m.b16 - 64*m.b1*m.b7*m.b17 - 64*m.b1*m.b7*m.b18 - 64*m.b1*m.b7*m.b19 - 32*m.b1*m.b7*m.b20 - 
                       32*m.b1*m.b7*m.b21 - 32*m.b1*m.b7*m.b22 - 32*m.b1*m.b7*m.b23 - 32*m.b1*m.b7*m.b24 - 32*m.b1*m.b7*
                       m.b25 - 64*m.b1*m.b8*m.b9 - 64*m.b1*m.b8*m.b10 - 64*m.b1*m.b8*m.b11 - 64*m.b1*m.b8*m.b12 - 64*
                       m.b1*m.b8*m.b13 - 64*m.b1*m.b8*m.b14 - 32*m.b1*m.b8*m.b15 - 64*m.b1*m.b8*m.b16 - 64*m.b1*m.b8*
                       m.b17 - 64*m.b1*m.b8*m.b18 - 32*m.b1*m.b8*m.b19 - 32*m.b1*m.b8*m.b20 - 32*m.b1*m.b8*m.b21 - 32*
                       m.b1*m.b8*m.b22 - 32*m.b1*m.b8*m.b23 - 32*m.b1*m.b8*m.b24 - 32*m.b1*m.b8*m.b25 - 64*m.b1*m.b9*
                       m.b10 - 64*m.b1*m.b9*m.b11 - 64*m.b1*m.b9*m.b12 - 64*m.b1*m.b9*m.b13 - 64*m.b1*m.b9*m.b14 - 64*
                       m.b1*m.b9*m.b15 - 64*m.b1*m.b9*m.b16 - 32*m.b1*m.b9*m.b17 - 32*m.b1*m.b9*m.b18 - 32*m.b1*m.b9*
                       m.b19 - 32*m.b1*m.b9*m.b20 - 32*m.b1*m.b9*m.b21 - 32*m.b1*m.b9*m.b22 - 32*m.b1*m.b9*m.b23 - 32*
                       m.b1*m.b9*m.b24 - 32*m.b1*m.b9*m.b25 - 64*m.b1*m.b10*m.b11 - 64*m.b1*m.b10*m.b12 - 64*m.b1*m.b10*
                       m.b13 - 64*m.b1*m.b10*m.b14 - 64*m.b1*m.b10*m.b15 - 64*m.b1*m.b10*m.b16 - 32*m.b1*m.b10*m.b17 - 
                       32*m.b1*m.b10*m.b18 - 32*m.b1*m.b10*m.b20 - 32*m.b1*m.b10*m.b21 - 32*m.b1*m.b10*m.b22 - 32*m.b1*
                       m.b10*m.b23 - 32*m.b1*m.b10*m.b24 - 32*m.b1*m.b10*m.b25 - 64*m.b1*m.b11*m.b12 - 64*m.b1*m.b11*
                       m.b13 - 64*m.b1*m.b11*m.b14 - 64*m.b1*m.b11*m.b15 - 32*m.b1*m.b11*m.b16 - 32*m.b1*m.b11*m.b17 - 
                       32*m.b1*m.b11*m.b18 - 32*m.b1*m.b11*m.b19 - 32*m.b1*m.b11*m.b20 - 32*m.b1*m.b11*m.b22 - 32*m.b1*
                       m.b11*m.b23 - 32*m.b1*m.b11*m.b24 - 32*m.b1*m.b11*m.b25 - 64*m.b1*m.b12*m.b13 - 64*m.b1*m.b12*
                       m.b14 - 32*m.b1*m.b12*m.b15 - 32*m.b1*m.b12*m.b16 - 32*m.b1*m.b12*m.b17 - 32*m.b1*m.b12*m.b18 - 
                       32*m.b1*m.b12*m.b19 - 32*m.b1*m.b12*m.b20 - 32*m.b1*m.b12*m.b21 - 32*m.b1*m.b12*m.b22 - 32*m.b1*
                       m.b12*m.b24 - 32*m.b1*m.b12*m.b25 - 32*m.b1*m.b13*m.b14 - 32*m.b1*m.b13*m.b15 - 32*m.b1*m.b13*
                       m.b16 - 32*m.b1*m.b13*m.b17 - 32*m.b1*m.b13*m.b18 - 32*m.b1*m.b13*m.b19 - 32*m.b1*m.b13*m.b20 - 
                       32*m.b1*m.b13*m.b21 - 32*m.b1*m.b13*m.b22 - 32*m.b1*m.b13*m.b23 - 32*m.b1*m.b13*m.b24 - 32*m.b1*
                       m.b14*m.b15 - 32*m.b1*m.b14*m.b16 - 32*m.b1*m.b14*m.b17 - 32*m.b1*m.b14*m.b18 - 32*m.b1*m.b14*
                       m.b19 - 32*m.b1*m.b14*m.b20 - 32*m.b1*m.b14*m.b21 - 32*m.b1*m.b14*m.b22 - 32*m.b1*m.b14*m.b23 - 
                       32*m.b1*m.b14*m.b24 - 32*m.b1*m.b14*m.b25 - 32*m.b1*m.b15*m.b16 - 32*m.b1*m.b15*m.b17 - 32*m.b1*
                       m.b15*m.b18 - 32*m.b1*m.b15*m.b19 - 32*m.b1*m.b15*m.b20 - 32*m.b1*m.b15*m.b21 - 32*m.b1*m.b15*
                       m.b22 - 32*m.b1*m.b15*m.b23 - 32*m.b1*m.b15*m.b24 - 32*m.b1*m.b15*m.b25 - 32*m.b1*m.b16*m.b17 - 
                       32*m.b1*m.b16*m.b18 - 32*m.b1*m.b16*m.b19 - 32*m.b1*m.b16*m.b20 - 32*m.b1*m.b16*m.b21 - 32*m.b1*
                       m.b16*m.b22 - 32*m.b1*m.b16*m.b23 - 32*m.b1*m.b16*m.b24 - 32*m.b1*m.b16*m.b25 - 32*m.b1*m.b17*
                       m.b18 - 32*m.b1*m.b17*m.b19 - 32*m.b1*m.b17*m.b20 - 32*m.b1*m.b17*m.b21 - 32*m.b1*m.b17*m.b22 - 
                       32*m.b1*m.b17*m.b23 - 32*m.b1*m.b17*m.b24 - 32*m.b1*m.b17*m.b25 - 32*m.b1*m.b18*m.b19 - 32*m.b1*
                       m.b18*m.b20 - 32*m.b1*m.b18*m.b21 - 32*m.b1*m.b18*m.b22 - 32*m.b1*m.b18*m.b23 - 32*m.b1*m.b18*
                       m.b24 - 32*m.b1*m.b18*m.b25 - 32*m.b1*m.b19*m.b20 - 32*m.b1*m.b19*m.b21 - 32*m.b1*m.b19*m.b22 - 
                       32*m.b1*m.b19*m.b23 - 32*m.b1*m.b19*m.b24 - 32*m.b1*m.b19*m.b25 - 32*m.b1*m.b20*m.b21 - 32*m.b1*
                       m.b20*m.b22 - 32*m.b1*m.b20*m.b23 - 32*m.b1*m.b20*m.b24 - 32*m.b1*m.b20*m.b25 - 32*m.b1*m.b21*
                       m.b22 - 32*m.b1*m.b21*m.b23 - 32*m.b1*m.b21*m.b24 - 32*m.b1*m.b21*m.b25 - 32*m.b1*m.b22*m.b23 - 
                       32*m.b1*m.b22*m.b24 - 32*m.b1*m.b22*m.b25 - 32*m.b1*m.b23*m.b24 - 32*m.b1*m.b23*m.b25 - 32*m.b1*
                       m.b24*m.b25 - 64*m.b2*m.b3*m.b4 - 64*m.b2*m.b3*m.b5 - 64*m.b2*m.b3*m.b6 - 64*m.b2*m.b3*m.b7 - 64*
                       m.b2*m.b3*m.b8 - 64*m.b2*m.b3*m.b9 - 64*m.b2*m.b3*m.b10 - 64*m.b2*m.b3*m.b11 - 96*m.b2*m.b3*m.b12
                        - 128*m.b2*m.b3*m.b13 - 128*m.b2*m.b3*m.b14 - 128*m.b2*m.b3*m.b15 - 128*m.b2*m.b3*m.b16 - 128*
                       m.b2*m.b3*m.b17 - 128*m.b2*m.b3*m.b18 - 128*m.b2*m.b3*m.b19 - 128*m.b2*m.b3*m.b20 - 128*m.b2*m.b3
                       *m.b21 - 128*m.b2*m.b3*m.b22 - 128*m.b2*m.b3*m.b23 - 96*m.b2*m.b3*m.b24 - 32*m.b2*m.b3*m.b25 - 96
                       *m.b2*m.b4*m.b5 - 32*m.b2*m.b4*m.b6 - 64*m.b2*m.b4*m.b7 - 64*m.b2*m.b4*m.b8 - 64*m.b2*m.b4*m.b9
                        - 64*m.b2*m.b4*m.b10 - 96*m.b2*m.b4*m.b11 - 96*m.b2*m.b4*m.b12 - 128*m.b2*m.b4*m.b13 - 128*m.b2*
                       m.b4*m.b14 - 128*m.b2*m.b4*m.b15 - 128*m.b2*m.b4*m.b16 - 128*m.b2*m.b4*m.b17 - 128*m.b2*m.b4*
                       m.b18 - 128*m.b2*m.b4*m.b19 - 128*m.b2*m.b4*m.b20 - 128*m.b2*m.b4*m.b21 - 128*m.b2*m.b4*m.b22 - 
                       96*m.b2*m.b4*m.b23 - 64*m.b2*m.b4*m.b24 - 32*m.b2*m.b4*m.b25 - 96*m.b2*m.b5*m.b6 - 64*m.b2*m.b5*
                       m.b7 - 32*m.b2*m.b5*m.b8 - 64*m.b2*m.b5*m.b9 - 96*m.b2*m.b5*m.b10 - 96*m.b2*m.b5*m.b11 - 96*m.b2*
                       m.b5*m.b12 - 128*m.b2*m.b5*m.b13 - 128*m.b2*m.b5*m.b14 - 128*m.b2*m.b5*m.b15 - 128*m.b2*m.b5*
                       m.b16 - 128*m.b2*m.b5*m.b17 - 128*m.b2*m.b5*m.b18 - 128*m.b2*m.b5*m.b19 - 128*m.b2*m.b5*m.b20 - 
                       128*m.b2*m.b5*m.b21 - 96*m.b2*m.b5*m.b22 - 64*m.b2*m.b5*m.b23 - 64*m.b2*m.b5*m.b24 - 32*m.b2*m.b5
                       *m.b25 - 96*m.b2*m.b6*m.b7 - 64*m.b2*m.b6*m.b8 - 96*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b10 - 96*m.b2
                       *m.b6*m.b11 - 96*m.b2*m.b6*m.b12 - 128*m.b2*m.b6*m.b13 - 128*m.b2*m.b6*m.b14 - 128*m.b2*m.b6*
                       m.b15 - 128*m.b2*m.b6*m.b16 - 128*m.b2*m.b6*m.b17 - 128*m.b2*m.b6*m.b18 - 128*m.b2*m.b6*m.b19 - 
                       128*m.b2*m.b6*m.b20 - 96*m.b2*m.b6*m.b21 - 64*m.b2*m.b6*m.b22 - 64*m.b2*m.b6*m.b23 - 64*m.b2*m.b6
                       *m.b24 - 32*m.b2*m.b6*m.b25 - 128*m.b2*m.b7*m.b8 - 96*m.b2*m.b7*m.b9 - 96*m.b2*m.b7*m.b10 - 96*
                       m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b12 - 128*m.b2*m.b7*m.b13 - 128*m.b2*m.b7*m.b14 - 128*m.b2*m.b7*
                       m.b15 - 128*m.b2*m.b7*m.b16 - 128*m.b2*m.b7*m.b17 - 128*m.b2*m.b7*m.b18 - 128*m.b2*m.b7*m.b19 - 
                       96*m.b2*m.b7*m.b20 - 64*m.b2*m.b7*m.b21 - 64*m.b2*m.b7*m.b22 - 64*m.b2*m.b7*m.b23 - 64*m.b2*m.b7*
                       m.b24 - 32*m.b2*m.b7*m.b25 - 128*m.b2*m.b8*m.b9 - 96*m.b2*m.b8*m.b10 - 96*m.b2*m.b8*m.b11 - 96*
                       m.b2*m.b8*m.b12 - 128*m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b14 - 128*m.b2*m.b8*m.b15 - 128*m.b2*m.b8*
                       m.b16 - 128*m.b2*m.b8*m.b17 - 128*m.b2*m.b8*m.b18 - 96*m.b2*m.b8*m.b19 - 64*m.b2*m.b8*m.b20 - 64*
                       m.b2*m.b8*m.b21 - 64*m.b2*m.b8*m.b22 - 64*m.b2*m.b8*m.b23 - 64*m.b2*m.b8*m.b24 - 32*m.b2*m.b8*
                       m.b25 - 128*m.b2*m.b9*m.b10 - 96*m.b2*m.b9*m.b11 - 96*m.b2*m.b9*m.b12 - 128*m.b2*m.b9*m.b13 - 128
                       *m.b2*m.b9*m.b14 - 128*m.b2*m.b9*m.b15 - 64*m.b2*m.b9*m.b16 - 128*m.b2*m.b9*m.b17 - 96*m.b2*m.b9*
                       m.b18 - 64*m.b2*m.b9*m.b19 - 64*m.b2*m.b9*m.b20 - 64*m.b2*m.b9*m.b21 - 64*m.b2*m.b9*m.b22 - 64*
                       m.b2*m.b9*m.b23 - 64*m.b2*m.b9*m.b24 - 32*m.b2*m.b9*m.b25 - 128*m.b2*m.b10*m.b11 - 96*m.b2*m.b10*
                       m.b12 - 128*m.b2*m.b10*m.b13 - 128*m.b2*m.b10*m.b14 - 128*m.b2*m.b10*m.b15 - 128*m.b2*m.b10*m.b16
                        - 96*m.b2*m.b10*m.b17 - 64*m.b2*m.b10*m.b19 - 64*m.b2*m.b10*m.b20 - 64*m.b2*m.b10*m.b21 - 64*
                       m.b2*m.b10*m.b22 - 64*m.b2*m.b10*m.b23 - 64*m.b2*m.b10*m.b24 - 32*m.b2*m.b10*m.b25 - 128*m.b2*
                       m.b11*m.b12 - 128*m.b2*m.b11*m.b13 - 128*m.b2*m.b11*m.b14 - 128*m.b2*m.b11*m.b15 - 96*m.b2*m.b11*
                       m.b16 - 64*m.b2*m.b11*m.b17 - 64*m.b2*m.b11*m.b18 - 64*m.b2*m.b11*m.b19 - 64*m.b2*m.b11*m.b21 - 
                       64*m.b2*m.b11*m.b22 - 64*m.b2*m.b11*m.b23 - 64*m.b2*m.b11*m.b24 - 32*m.b2*m.b11*m.b25 - 160*m.b2*
                       m.b12*m.b13 - 128*m.b2*m.b12*m.b14 - 96*m.b2*m.b12*m.b15 - 64*m.b2*m.b12*m.b16 - 64*m.b2*m.b12*
                       m.b17 - 64*m.b2*m.b12*m.b18 - 64*m.b2*m.b12*m.b19 - 64*m.b2*m.b12*m.b20 - 64*m.b2*m.b12*m.b21 - 
                       64*m.b2*m.b12*m.b23 - 64*m.b2*m.b12*m.b24 - 32*m.b2*m.b12*m.b25 - 128*m.b2*m.b13*m.b14 - 64*m.b2*
                       m.b13*m.b15 - 64*m.b2*m.b13*m.b16 - 64*m.b2*m.b13*m.b17 - 64*m.b2*m.b13*m.b18 - 64*m.b2*m.b13*
                       m.b19 - 64*m.b2*m.b13*m.b20 - 64*m.b2*m.b13*m.b21 - 64*m.b2*m.b13*m.b22 - 64*m.b2*m.b13*m.b23 - 
                       32*m.b2*m.b13*m.b25 - 96*m.b2*m.b14*m.b15 - 64*m.b2*m.b14*m.b16 - 64*m.b2*m.b14*m.b17 - 64*m.b2*
                       m.b14*m.b18 - 64*m.b2*m.b14*m.b19 - 64*m.b2*m.b14*m.b20 - 64*m.b2*m.b14*m.b21 - 64*m.b2*m.b14*
                       m.b22 - 64*m.b2*m.b14*m.b23 - 64*m.b2*m.b14*m.b24 - 32*m.b2*m.b14*m.b25 - 96*m.b2*m.b15*m.b16 - 
                       64*m.b2*m.b15*m.b17 - 64*m.b2*m.b15*m.b18 - 64*m.b2*m.b15*m.b19 - 64*m.b2*m.b15*m.b20 - 64*m.b2*
                       m.b15*m.b21 - 64*m.b2*m.b15*m.b22 - 64*m.b2*m.b15*m.b23 - 64*m.b2*m.b15*m.b24 - 32*m.b2*m.b15*
                       m.b25 - 96*m.b2*m.b16*m.b17 - 64*m.b2*m.b16*m.b18 - 64*m.b2*m.b16*m.b19 - 64*m.b2*m.b16*m.b20 - 
                       64*m.b2*m.b16*m.b21 - 64*m.b2*m.b16*m.b22 - 64*m.b2*m.b16*m.b23 - 64*m.b2*m.b16*m.b24 - 32*m.b2*
                       m.b16*m.b25 - 96*m.b2*m.b17*m.b18 - 64*m.b2*m.b17*m.b19 - 64*m.b2*m.b17*m.b20 - 64*m.b2*m.b17*
                       m.b21 - 64*m.b2*m.b17*m.b22 - 64*m.b2*m.b17*m.b23 - 64*m.b2*m.b17*m.b24 - 32*m.b2*m.b17*m.b25 - 
                       96*m.b2*m.b18*m.b19 - 64*m.b2*m.b18*m.b20 - 64*m.b2*m.b18*m.b21 - 64*m.b2*m.b18*m.b22 - 64*m.b2*
                       m.b18*m.b23 - 64*m.b2*m.b18*m.b24 - 32*m.b2*m.b18*m.b25 - 96*m.b2*m.b19*m.b20 - 64*m.b2*m.b19*
                       m.b21 - 64*m.b2*m.b19*m.b22 - 64*m.b2*m.b19*m.b23 - 64*m.b2*m.b19*m.b24 - 32*m.b2*m.b19*m.b25 - 
                       96*m.b2*m.b20*m.b21 - 64*m.b2*m.b20*m.b22 - 64*m.b2*m.b20*m.b23 - 64*m.b2*m.b20*m.b24 - 32*m.b2*
                       m.b20*m.b25 - 96*m.b2*m.b21*m.b22 - 64*m.b2*m.b21*m.b23 - 64*m.b2*m.b21*m.b24 - 32*m.b2*m.b21*
                       m.b25 - 96*m.b2*m.b22*m.b23 - 64*m.b2*m.b22*m.b24 - 32*m.b2*m.b22*m.b25 - 96*m.b2*m.b23*m.b24 - 
                       32*m.b2*m.b23*m.b25 - 64*m.b2*m.b24*m.b25 - 64*m.b3*m.b4*m.b5 - 96*m.b3*m.b4*m.b6 - 64*m.b3*m.b4*
                       m.b7 - 64*m.b3*m.b4*m.b8 - 64*m.b3*m.b4*m.b9 - 64*m.b3*m.b4*m.b10 - 64*m.b3*m.b4*m.b11 - 64*m.b3*
                       m.b4*m.b12 - 128*m.b3*m.b4*m.b13 - 192*m.b3*m.b4*m.b14 - 192*m.b3*m.b4*m.b15 - 192*m.b3*m.b4*
                       m.b16 - 192*m.b3*m.b4*m.b17 - 192*m.b3*m.b4*m.b18 - 192*m.b3*m.b4*m.b19 - 192*m.b3*m.b4*m.b20 - 
                       192*m.b3*m.b4*m.b21 - 192*m.b3*m.b4*m.b22 - 160*m.b3*m.b4*m.b23 - 96*m.b3*m.b4*m.b24 - 32*m.b3*
                       m.b4*m.b25 - 96*m.b3*m.b5*m.b6 - 64*m.b3*m.b5*m.b7 - 64*m.b3*m.b5*m.b8 - 64*m.b3*m.b5*m.b9 - 64*
                       m.b3*m.b5*m.b10 - 64*m.b3*m.b5*m.b11 - 128*m.b3*m.b5*m.b12 - 128*m.b3*m.b5*m.b13 - 192*m.b3*m.b5*
                       m.b14 - 192*m.b3*m.b5*m.b15 - 192*m.b3*m.b5*m.b16 - 192*m.b3*m.b5*m.b17 - 192*m.b3*m.b5*m.b18 - 
                       192*m.b3*m.b5*m.b19 - 192*m.b3*m.b5*m.b20 - 192*m.b3*m.b5*m.b21 - 160*m.b3*m.b5*m.b22 - 128*m.b3*
                       m.b5*m.b23 - 64*m.b3*m.b5*m.b24 - 32*m.b3*m.b5*m.b25 - 96*m.b3*m.b6*m.b7 - 96*m.b3*m.b6*m.b8 - 32
                       *m.b3*m.b6*m.b9 - 64*m.b3*m.b6*m.b10 - 128*m.b3*m.b6*m.b11 - 128*m.b3*m.b6*m.b12 - 128*m.b3*m.b6*
                       m.b13 - 192*m.b3*m.b6*m.b14 - 192*m.b3*m.b6*m.b15 - 192*m.b3*m.b6*m.b16 - 192*m.b3*m.b6*m.b17 - 
                       192*m.b3*m.b6*m.b18 - 192*m.b3*m.b6*m.b19 - 192*m.b3*m.b6*m.b20 - 160*m.b3*m.b6*m.b21 - 128*m.b3*
                       m.b6*m.b22 - 96*m.b3*m.b6*m.b23 - 64*m.b3*m.b6*m.b24 - 32*m.b3*m.b6*m.b25 - 96*m.b3*m.b7*m.b8 - 
                       96*m.b3*m.b7*m.b9 - 128*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*m.b11 - 128*m.b3*m.b7*m.b12 - 128*m.b3*
                       m.b7*m.b13 - 192*m.b3*m.b7*m.b14 - 192*m.b3*m.b7*m.b15 - 192*m.b3*m.b7*m.b16 - 192*m.b3*m.b7*
                       m.b17 - 192*m.b3*m.b7*m.b18 - 192*m.b3*m.b7*m.b19 - 160*m.b3*m.b7*m.b20 - 128*m.b3*m.b7*m.b21 - 
                       96*m.b3*m.b7*m.b22 - 96*m.b3*m.b7*m.b23 - 64*m.b3*m.b7*m.b24 - 32*m.b3*m.b7*m.b25 - 160*m.b3*m.b8
                       *m.b9 - 160*m.b3*m.b8*m.b10 - 128*m.b3*m.b8*m.b11 - 128*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*m.b13 - 
                       192*m.b3*m.b8*m.b14 - 192*m.b3*m.b8*m.b15 - 192*m.b3*m.b8*m.b16 - 192*m.b3*m.b8*m.b17 - 192*m.b3*
                       m.b8*m.b18 - 160*m.b3*m.b8*m.b19 - 128*m.b3*m.b8*m.b20 - 96*m.b3*m.b8*m.b21 - 96*m.b3*m.b8*m.b22
                        - 96*m.b3*m.b8*m.b23 - 64*m.b3*m.b8*m.b24 - 32*m.b3*m.b8*m.b25 - 160*m.b3*m.b9*m.b10 - 160*m.b3*
                       m.b9*m.b11 - 128*m.b3*m.b9*m.b12 - 128*m.b3*m.b9*m.b13 - 192*m.b3*m.b9*m.b14 - 96*m.b3*m.b9*m.b15
                        - 192*m.b3*m.b9*m.b16 - 192*m.b3*m.b9*m.b17 - 160*m.b3*m.b9*m.b18 - 128*m.b3*m.b9*m.b19 - 96*
                       m.b3*m.b9*m.b20 - 96*m.b3*m.b9*m.b21 - 96*m.b3*m.b9*m.b22 - 96*m.b3*m.b9*m.b23 - 64*m.b3*m.b9*
                       m.b24 - 32*m.b3*m.b9*m.b25 - 160*m.b3*m.b10*m.b11 - 160*m.b3*m.b10*m.b12 - 128*m.b3*m.b10*m.b13
                        - 192*m.b3*m.b10*m.b14 - 192*m.b3*m.b10*m.b15 - 192*m.b3*m.b10*m.b16 - 64*m.b3*m.b10*m.b17 - 128
                       *m.b3*m.b10*m.b18 - 96*m.b3*m.b10*m.b19 - 96*m.b3*m.b10*m.b20 - 96*m.b3*m.b10*m.b21 - 96*m.b3*
                       m.b10*m.b22 - 96*m.b3*m.b10*m.b23 - 64*m.b3*m.b10*m.b24 - 32*m.b3*m.b10*m.b25 - 160*m.b3*m.b11*
                       m.b12 - 160*m.b3*m.b11*m.b13 - 192*m.b3*m.b11*m.b14 - 192*m.b3*m.b11*m.b15 - 160*m.b3*m.b11*m.b16
                        - 128*m.b3*m.b11*m.b17 - 96*m.b3*m.b11*m.b18 - 96*m.b3*m.b11*m.b20 - 96*m.b3*m.b11*m.b21 - 96*
                       m.b3*m.b11*m.b22 - 96*m.b3*m.b11*m.b23 - 64*m.b3*m.b11*m.b24 - 32*m.b3*m.b11*m.b25 - 192*m.b3*
                       m.b12*m.b13 - 224*m.b3*m.b12*m.b14 - 160*m.b3*m.b12*m.b15 - 128*m.b3*m.b12*m.b16 - 96*m.b3*m.b12*
                       m.b17 - 96*m.b3*m.b12*m.b18 - 96*m.b3*m.b12*m.b19 - 96*m.b3*m.b12*m.b20 - 96*m.b3*m.b12*m.b22 - 
                       96*m.b3*m.b12*m.b23 - 64*m.b3*m.b12*m.b24 - 32*m.b3*m.b12*m.b25 - 224*m.b3*m.b13*m.b14 - 160*m.b3
                       *m.b13*m.b15 - 96*m.b3*m.b13*m.b16 - 96*m.b3*m.b13*m.b17 - 96*m.b3*m.b13*m.b18 - 96*m.b3*m.b13*
                       m.b19 - 96*m.b3*m.b13*m.b20 - 96*m.b3*m.b13*m.b21 - 96*m.b3*m.b13*m.b22 - 64*m.b3*m.b13*m.b24 - 
                       32*m.b3*m.b13*m.b25 - 160*m.b3*m.b14*m.b15 - 128*m.b3*m.b14*m.b16 - 96*m.b3*m.b14*m.b17 - 96*m.b3
                       *m.b14*m.b18 - 96*m.b3*m.b14*m.b19 - 96*m.b3*m.b14*m.b20 - 96*m.b3*m.b14*m.b21 - 96*m.b3*m.b14*
                       m.b22 - 96*m.b3*m.b14*m.b23 - 64*m.b3*m.b14*m.b24 - 160*m.b3*m.b15*m.b16 - 128*m.b3*m.b15*m.b17
                        - 96*m.b3*m.b15*m.b18 - 96*m.b3*m.b15*m.b19 - 96*m.b3*m.b15*m.b20 - 96*m.b3*m.b15*m.b21 - 96*
                       m.b3*m.b15*m.b22 - 96*m.b3*m.b15*m.b23 - 64*m.b3*m.b15*m.b24 - 32*m.b3*m.b15*m.b25 - 160*m.b3*
                       m.b16*m.b17 - 128*m.b3*m.b16*m.b18 - 96*m.b3*m.b16*m.b19 - 96*m.b3*m.b16*m.b20 - 96*m.b3*m.b16*
                       m.b21 - 96*m.b3*m.b16*m.b22 - 96*m.b3*m.b16*m.b23 - 64*m.b3*m.b16*m.b24 - 32*m.b3*m.b16*m.b25 - 
                       160*m.b3*m.b17*m.b18 - 128*m.b3*m.b17*m.b19 - 96*m.b3*m.b17*m.b20 - 96*m.b3*m.b17*m.b21 - 96*m.b3
                       *m.b17*m.b22 - 96*m.b3*m.b17*m.b23 - 64*m.b3*m.b17*m.b24 - 32*m.b3*m.b17*m.b25 - 160*m.b3*m.b18*
                       m.b19 - 128*m.b3*m.b18*m.b20 - 96*m.b3*m.b18*m.b21 - 96*m.b3*m.b18*m.b22 - 96*m.b3*m.b18*m.b23 - 
                       64*m.b3*m.b18*m.b24 - 32*m.b3*m.b18*m.b25 - 160*m.b3*m.b19*m.b20 - 128*m.b3*m.b19*m.b21 - 96*m.b3
                       *m.b19*m.b22 - 96*m.b3*m.b19*m.b23 - 64*m.b3*m.b19*m.b24 - 32*m.b3*m.b19*m.b25 - 160*m.b3*m.b20*
                       m.b21 - 128*m.b3*m.b20*m.b22 - 96*m.b3*m.b20*m.b23 - 64*m.b3*m.b20*m.b24 - 32*m.b3*m.b20*m.b25 - 
                       160*m.b3*m.b21*m.b22 - 128*m.b3*m.b21*m.b23 - 64*m.b3*m.b21*m.b24 - 32*m.b3*m.b21*m.b25 - 160*
                       m.b3*m.b22*m.b23 - 96*m.b3*m.b22*m.b24 - 32*m.b3*m.b22*m.b25 - 128*m.b3*m.b23*m.b24 - 64*m.b3*
                       m.b23*m.b25 - 64*m.b3*m.b24*m.b25 - 64*m.b4*m.b5*m.b6 - 96*m.b4*m.b5*m.b7 - 96*m.b4*m.b5*m.b8 - 
                       64*m.b4*m.b5*m.b9 - 64*m.b4*m.b5*m.b10 - 64*m.b4*m.b5*m.b11 - 64*m.b4*m.b5*m.b12 - 64*m.b4*m.b5*
                       m.b13 - 160*m.b4*m.b5*m.b14 - 256*m.b4*m.b5*m.b15 - 256*m.b4*m.b5*m.b16 - 256*m.b4*m.b5*m.b17 - 
                       256*m.b4*m.b5*m.b18 - 256*m.b4*m.b5*m.b19 - 256*m.b4*m.b5*m.b20 - 256*m.b4*m.b5*m.b21 - 224*m.b4*
                       m.b5*m.b22 - 160*m.b4*m.b5*m.b23 - 96*m.b4*m.b5*m.b24 - 32*m.b4*m.b5*m.b25 - 96*m.b4*m.b6*m.b7 - 
                       64*m.b4*m.b6*m.b8 - 96*m.b4*m.b6*m.b9 - 64*m.b4*m.b6*m.b10 - 64*m.b4*m.b6*m.b11 - 64*m.b4*m.b6*
                       m.b12 - 160*m.b4*m.b6*m.b13 - 160*m.b4*m.b6*m.b14 - 256*m.b4*m.b6*m.b15 - 256*m.b4*m.b6*m.b16 - 
                       256*m.b4*m.b6*m.b17 - 256*m.b4*m.b6*m.b18 - 256*m.b4*m.b6*m.b19 - 256*m.b4*m.b6*m.b20 - 224*m.b4*
                       m.b6*m.b21 - 192*m.b4*m.b6*m.b22 - 128*m.b4*m.b6*m.b23 - 64*m.b4*m.b6*m.b24 - 32*m.b4*m.b6*m.b25
                        - 96*m.b4*m.b7*m.b8 - 96*m.b4*m.b7*m.b9 - 64*m.b4*m.b7*m.b10 - 64*m.b4*m.b7*m.b11 - 160*m.b4*
                       m.b7*m.b12 - 160*m.b4*m.b7*m.b13 - 160*m.b4*m.b7*m.b14 - 256*m.b4*m.b7*m.b15 - 256*m.b4*m.b7*
                       m.b16 - 256*m.b4*m.b7*m.b17 - 256*m.b4*m.b7*m.b18 - 256*m.b4*m.b7*m.b19 - 224*m.b4*m.b7*m.b20 - 
                       192*m.b4*m.b7*m.b21 - 160*m.b4*m.b7*m.b22 - 96*m.b4*m.b7*m.b23 - 64*m.b4*m.b7*m.b24 - 32*m.b4*
                       m.b7*m.b25 - 96*m.b4*m.b8*m.b9 - 96*m.b4*m.b8*m.b10 - 192*m.b4*m.b8*m.b11 - 128*m.b4*m.b8*m.b12
                        - 160*m.b4*m.b8*m.b13 - 160*m.b4*m.b8*m.b14 - 256*m.b4*m.b8*m.b15 - 256*m.b4*m.b8*m.b16 - 256*
                       m.b4*m.b8*m.b17 - 256*m.b4*m.b8*m.b18 - 224*m.b4*m.b8*m.b19 - 192*m.b4*m.b8*m.b20 - 160*m.b4*m.b8
                       *m.b21 - 128*m.b4*m.b8*m.b22 - 96*m.b4*m.b8*m.b23 - 64*m.b4*m.b8*m.b24 - 32*m.b4*m.b8*m.b25 - 192
                       *m.b4*m.b9*m.b10 - 192*m.b4*m.b9*m.b11 - 192*m.b4*m.b9*m.b12 - 160*m.b4*m.b9*m.b13 - 128*m.b4*
                       m.b9*m.b14 - 256*m.b4*m.b9*m.b15 - 256*m.b4*m.b9*m.b16 - 256*m.b4*m.b9*m.b17 - 224*m.b4*m.b9*
                       m.b18 - 192*m.b4*m.b9*m.b19 - 160*m.b4*m.b9*m.b20 - 128*m.b4*m.b9*m.b21 - 128*m.b4*m.b9*m.b22 - 
                       96*m.b4*m.b9*m.b23 - 64*m.b4*m.b9*m.b24 - 32*m.b4*m.b9*m.b25 - 192*m.b4*m.b10*m.b11 - 192*m.b4*
                       m.b10*m.b12 - 192*m.b4*m.b10*m.b13 - 160*m.b4*m.b10*m.b14 - 256*m.b4*m.b10*m.b15 - 128*m.b4*m.b10
                       *m.b16 - 224*m.b4*m.b10*m.b17 - 192*m.b4*m.b10*m.b18 - 160*m.b4*m.b10*m.b19 - 128*m.b4*m.b10*
                       m.b20 - 128*m.b4*m.b10*m.b21 - 128*m.b4*m.b10*m.b22 - 96*m.b4*m.b10*m.b23 - 64*m.b4*m.b10*m.b24
                        - 32*m.b4*m.b10*m.b25 - 192*m.b4*m.b11*m.b12 - 224*m.b4*m.b11*m.b13 - 192*m.b4*m.b11*m.b14 - 256
                       *m.b4*m.b11*m.b15 - 224*m.b4*m.b11*m.b16 - 192*m.b4*m.b11*m.b17 - 32*m.b4*m.b11*m.b18 - 128*m.b4*
                       m.b11*m.b19 - 128*m.b4*m.b11*m.b20 - 128*m.b4*m.b11*m.b21 - 128*m.b4*m.b11*m.b22 - 96*m.b4*m.b11*
                       m.b23 - 64*m.b4*m.b11*m.b24 - 32*m.b4*m.b11*m.b25 - 192*m.b4*m.b12*m.b13 - 224*m.b4*m.b12*m.b14
                        - 256*m.b4*m.b12*m.b15 - 192*m.b4*m.b12*m.b16 - 160*m.b4*m.b12*m.b17 - 128*m.b4*m.b12*m.b18 - 
                       128*m.b4*m.b12*m.b19 - 128*m.b4*m.b12*m.b21 - 128*m.b4*m.b12*m.b22 - 96*m.b4*m.b12*m.b23 - 64*
                       m.b4*m.b12*m.b24 - 32*m.b4*m.b12*m.b25 - 224*m.b4*m.b13*m.b14 - 256*m.b4*m.b13*m.b15 - 192*m.b4*
                       m.b13*m.b16 - 128*m.b4*m.b13*m.b17 - 128*m.b4*m.b13*m.b18 - 128*m.b4*m.b13*m.b19 - 128*m.b4*m.b13
                       *m.b20 - 128*m.b4*m.b13*m.b21 - 96*m.b4*m.b13*m.b23 - 64*m.b4*m.b13*m.b24 - 32*m.b4*m.b13*m.b25
                        - 256*m.b4*m.b14*m.b15 - 192*m.b4*m.b14*m.b16 - 160*m.b4*m.b14*m.b17 - 128*m.b4*m.b14*m.b18 - 
                       128*m.b4*m.b14*m.b19 - 128*m.b4*m.b14*m.b20 - 128*m.b4*m.b14*m.b21 - 128*m.b4*m.b14*m.b22 - 96*
                       m.b4*m.b14*m.b23 - 32*m.b4*m.b14*m.b25 - 224*m.b4*m.b15*m.b16 - 192*m.b4*m.b15*m.b17 - 160*m.b4*
                       m.b15*m.b18 - 128*m.b4*m.b15*m.b19 - 128*m.b4*m.b15*m.b20 - 128*m.b4*m.b15*m.b21 - 128*m.b4*m.b15
                       *m.b22 - 96*m.b4*m.b15*m.b23 - 64*m.b4*m.b15*m.b24 - 32*m.b4*m.b15*m.b25 - 224*m.b4*m.b16*m.b17
                        - 192*m.b4*m.b16*m.b18 - 160*m.b4*m.b16*m.b19 - 128*m.b4*m.b16*m.b20 - 128*m.b4*m.b16*m.b21 - 
                       128*m.b4*m.b16*m.b22 - 96*m.b4*m.b16*m.b23 - 64*m.b4*m.b16*m.b24 - 32*m.b4*m.b16*m.b25 - 224*m.b4
                       *m.b17*m.b18 - 192*m.b4*m.b17*m.b19 - 160*m.b4*m.b17*m.b20 - 128*m.b4*m.b17*m.b21 - 128*m.b4*
                       m.b17*m.b22 - 96*m.b4*m.b17*m.b23 - 64*m.b4*m.b17*m.b24 - 32*m.b4*m.b17*m.b25 - 224*m.b4*m.b18*
                       m.b19 - 192*m.b4*m.b18*m.b20 - 160*m.b4*m.b18*m.b21 - 128*m.b4*m.b18*m.b22 - 96*m.b4*m.b18*m.b23
                        - 64*m.b4*m.b18*m.b24 - 32*m.b4*m.b18*m.b25 - 224*m.b4*m.b19*m.b20 - 192*m.b4*m.b19*m.b21 - 160*
                       m.b4*m.b19*m.b22 - 96*m.b4*m.b19*m.b23 - 64*m.b4*m.b19*m.b24 - 32*m.b4*m.b19*m.b25 - 224*m.b4*
                       m.b20*m.b21 - 192*m.b4*m.b20*m.b22 - 128*m.b4*m.b20*m.b23 - 64*m.b4*m.b20*m.b24 - 32*m.b4*m.b20*
                       m.b25 - 224*m.b4*m.b21*m.b22 - 160*m.b4*m.b21*m.b23 - 96*m.b4*m.b21*m.b24 - 32*m.b4*m.b21*m.b25
                        - 192*m.b4*m.b22*m.b23 - 128*m.b4*m.b22*m.b24 - 64*m.b4*m.b22*m.b25 - 128*m.b4*m.b23*m.b24 - 64*
                       m.b4*m.b23*m.b25 - 64*m.b4*m.b24*m.b25 - 64*m.b5*m.b6*m.b7 - 96*m.b5*m.b6*m.b8 - 96*m.b5*m.b6*
                       m.b9 - 96*m.b5*m.b6*m.b10 - 64*m.b5*m.b6*m.b11 - 64*m.b5*m.b6*m.b12 - 64*m.b5*m.b6*m.b13 - 64*
                       m.b5*m.b6*m.b14 - 192*m.b5*m.b6*m.b15 - 320*m.b5*m.b6*m.b16 - 320*m.b5*m.b6*m.b17 - 320*m.b5*m.b6
                       *m.b18 - 320*m.b5*m.b6*m.b19 - 320*m.b5*m.b6*m.b20 - 288*m.b5*m.b6*m.b21 - 224*m.b5*m.b6*m.b22 - 
                       160*m.b5*m.b6*m.b23 - 96*m.b5*m.b6*m.b24 - 32*m.b5*m.b6*m.b25 - 96*m.b5*m.b7*m.b8 - 64*m.b5*m.b7*
                       m.b9 - 96*m.b5*m.b7*m.b10 - 96*m.b5*m.b7*m.b11 - 64*m.b5*m.b7*m.b12 - 64*m.b5*m.b7*m.b13 - 192*
                       m.b5*m.b7*m.b14 - 192*m.b5*m.b7*m.b15 - 320*m.b5*m.b7*m.b16 - 320*m.b5*m.b7*m.b17 - 320*m.b5*m.b7
                       *m.b18 - 320*m.b5*m.b7*m.b19 - 288*m.b5*m.b7*m.b20 - 256*m.b5*m.b7*m.b21 - 192*m.b5*m.b7*m.b22 - 
                       128*m.b5*m.b7*m.b23 - 64*m.b5*m.b7*m.b24 - 32*m.b5*m.b7*m.b25 - 96*m.b5*m.b8*m.b9 - 96*m.b5*m.b8*
                       m.b10 - 64*m.b5*m.b8*m.b11 - 96*m.b5*m.b8*m.b12 - 192*m.b5*m.b8*m.b13 - 192*m.b5*m.b8*m.b14 - 192
                       *m.b5*m.b8*m.b15 - 320*m.b5*m.b8*m.b16 - 320*m.b5*m.b8*m.b17 - 320*m.b5*m.b8*m.b18 - 288*m.b5*
                       m.b8*m.b19 - 256*m.b5*m.b8*m.b20 - 224*m.b5*m.b8*m.b21 - 160*m.b5*m.b8*m.b22 - 96*m.b5*m.b8*m.b23
                        - 64*m.b5*m.b8*m.b24 - 32*m.b5*m.b8*m.b25 - 96*m.b5*m.b9*m.b10 - 96*m.b5*m.b9*m.b11 - 224*m.b5*
                       m.b9*m.b12 - 192*m.b5*m.b9*m.b13 - 192*m.b5*m.b9*m.b14 - 192*m.b5*m.b9*m.b15 - 320*m.b5*m.b9*
                       m.b16 - 320*m.b5*m.b9*m.b17 - 288*m.b5*m.b9*m.b18 - 256*m.b5*m.b9*m.b19 - 224*m.b5*m.b9*m.b20 - 
                       192*m.b5*m.b9*m.b21 - 128*m.b5*m.b9*m.b22 - 96*m.b5*m.b9*m.b23 - 64*m.b5*m.b9*m.b24 - 32*m.b5*
                       m.b9*m.b25 - 224*m.b5*m.b10*m.b11 - 224*m.b5*m.b10*m.b12 - 256*m.b5*m.b10*m.b13 - 224*m.b5*m.b10*
                       m.b14 - 160*m.b5*m.b10*m.b15 - 320*m.b5*m.b10*m.b16 - 288*m.b5*m.b10*m.b17 - 256*m.b5*m.b10*m.b18
                        - 224*m.b5*m.b10*m.b19 - 192*m.b5*m.b10*m.b20 - 160*m.b5*m.b10*m.b21 - 128*m.b5*m.b10*m.b22 - 96
                       *m.b5*m.b10*m.b23 - 64*m.b5*m.b10*m.b24 - 32*m.b5*m.b10*m.b25 - 224*m.b5*m.b11*m.b12 - 224*m.b5*
                       m.b11*m.b13 - 256*m.b5*m.b11*m.b14 - 224*m.b5*m.b11*m.b15 - 288*m.b5*m.b11*m.b16 - 96*m.b5*m.b11*
                       m.b17 - 224*m.b5*m.b11*m.b18 - 192*m.b5*m.b11*m.b19 - 160*m.b5*m.b11*m.b20 - 160*m.b5*m.b11*m.b21
                        - 128*m.b5*m.b11*m.b22 - 96*m.b5*m.b11*m.b23 - 64*m.b5*m.b11*m.b24 - 32*m.b5*m.b11*m.b25 - 224*
                       m.b5*m.b12*m.b13 - 288*m.b5*m.b12*m.b14 - 224*m.b5*m.b12*m.b15 - 288*m.b5*m.b12*m.b16 - 224*m.b5*
                       m.b12*m.b17 - 192*m.b5*m.b12*m.b18 - 160*m.b5*m.b12*m.b20 - 160*m.b5*m.b12*m.b21 - 128*m.b5*m.b12
                       *m.b22 - 96*m.b5*m.b12*m.b23 - 64*m.b5*m.b12*m.b24 - 32*m.b5*m.b12*m.b25 - 192*m.b5*m.b13*m.b14
                        - 224*m.b5*m.b13*m.b15 - 288*m.b5*m.b13*m.b16 - 224*m.b5*m.b13*m.b17 - 160*m.b5*m.b13*m.b18 - 
                       160*m.b5*m.b13*m.b19 - 160*m.b5*m.b13*m.b20 - 128*m.b5*m.b13*m.b22 - 96*m.b5*m.b13*m.b23 - 64*
                       m.b5*m.b13*m.b24 - 32*m.b5*m.b13*m.b25 - 224*m.b5*m.b14*m.b15 - 288*m.b5*m.b14*m.b16 - 224*m.b5*
                       m.b14*m.b17 - 192*m.b5*m.b14*m.b18 - 160*m.b5*m.b14*m.b19 - 160*m.b5*m.b14*m.b20 - 160*m.b5*m.b14
                       *m.b21 - 128*m.b5*m.b14*m.b22 - 64*m.b5*m.b14*m.b24 - 32*m.b5*m.b14*m.b25 - 288*m.b5*m.b15*m.b16
                        - 256*m.b5*m.b15*m.b17 - 224*m.b5*m.b15*m.b18 - 192*m.b5*m.b15*m.b19 - 160*m.b5*m.b15*m.b20 - 
                       160*m.b5*m.b15*m.b21 - 128*m.b5*m.b15*m.b22 - 96*m.b5*m.b15*m.b23 - 64*m.b5*m.b15*m.b24 - 288*
                       m.b5*m.b16*m.b17 - 256*m.b5*m.b16*m.b18 - 224*m.b5*m.b16*m.b19 - 192*m.b5*m.b16*m.b20 - 160*m.b5*
                       m.b16*m.b21 - 128*m.b5*m.b16*m.b22 - 96*m.b5*m.b16*m.b23 - 64*m.b5*m.b16*m.b24 - 32*m.b5*m.b16*
                       m.b25 - 288*m.b5*m.b17*m.b18 - 256*m.b5*m.b17*m.b19 - 224*m.b5*m.b17*m.b20 - 192*m.b5*m.b17*m.b21
                        - 128*m.b5*m.b17*m.b22 - 96*m.b5*m.b17*m.b23 - 64*m.b5*m.b17*m.b24 - 32*m.b5*m.b17*m.b25 - 288*
                       m.b5*m.b18*m.b19 - 256*m.b5*m.b18*m.b20 - 224*m.b5*m.b18*m.b21 - 160*m.b5*m.b18*m.b22 - 96*m.b5*
                       m.b18*m.b23 - 64*m.b5*m.b18*m.b24 - 32*m.b5*m.b18*m.b25 - 288*m.b5*m.b19*m.b20 - 256*m.b5*m.b19*
                       m.b21 - 192*m.b5*m.b19*m.b22 - 128*m.b5*m.b19*m.b23 - 64*m.b5*m.b19*m.b24 - 32*m.b5*m.b19*m.b25
                        - 288*m.b5*m.b20*m.b21 - 224*m.b5*m.b20*m.b22 - 160*m.b5*m.b20*m.b23 - 96*m.b5*m.b20*m.b24 - 32*
                       m.b5*m.b20*m.b25 - 256*m.b5*m.b21*m.b22 - 192*m.b5*m.b21*m.b23 - 128*m.b5*m.b21*m.b24 - 64*m.b5*
                       m.b21*m.b25 - 192*m.b5*m.b22*m.b23 - 128*m.b5*m.b22*m.b24 - 64*m.b5*m.b22*m.b25 - 128*m.b5*m.b23*
                       m.b24 - 64*m.b5*m.b23*m.b25 - 64*m.b5*m.b24*m.b25 - 64*m.b6*m.b7*m.b8 - 96*m.b6*m.b7*m.b9 - 96*
                       m.b6*m.b7*m.b10 - 96*m.b6*m.b7*m.b11 - 96*m.b6*m.b7*m.b12 - 64*m.b6*m.b7*m.b13 - 64*m.b6*m.b7*
                       m.b14 - 64*m.b6*m.b7*m.b15 - 224*m.b6*m.b7*m.b16 - 384*m.b6*m.b7*m.b17 - 384*m.b6*m.b7*m.b18 - 
                       384*m.b6*m.b7*m.b19 - 352*m.b6*m.b7*m.b20 - 288*m.b6*m.b7*m.b21 - 224*m.b6*m.b7*m.b22 - 160*m.b6*
                       m.b7*m.b23 - 96*m.b6*m.b7*m.b24 - 32*m.b6*m.b7*m.b25 - 96*m.b6*m.b8*m.b9 - 64*m.b6*m.b8*m.b10 - 
                       96*m.b6*m.b8*m.b11 - 96*m.b6*m.b8*m.b12 - 96*m.b6*m.b8*m.b13 - 64*m.b6*m.b8*m.b14 - 224*m.b6*m.b8
                       *m.b15 - 224*m.b6*m.b8*m.b16 - 384*m.b6*m.b8*m.b17 - 384*m.b6*m.b8*m.b18 - 352*m.b6*m.b8*m.b19 - 
                       320*m.b6*m.b8*m.b20 - 256*m.b6*m.b8*m.b21 - 192*m.b6*m.b8*m.b22 - 128*m.b6*m.b8*m.b23 - 64*m.b6*
                       m.b8*m.b24 - 32*m.b6*m.b8*m.b25 - 96*m.b6*m.b9*m.b10 - 96*m.b6*m.b9*m.b11 - 64*m.b6*m.b9*m.b12 - 
                       128*m.b6*m.b9*m.b13 - 256*m.b6*m.b9*m.b14 - 224*m.b6*m.b9*m.b15 - 224*m.b6*m.b9*m.b16 - 384*m.b6*
                       m.b9*m.b17 - 352*m.b6*m.b9*m.b18 - 320*m.b6*m.b9*m.b19 - 288*m.b6*m.b9*m.b20 - 224*m.b6*m.b9*
                       m.b21 - 160*m.b6*m.b9*m.b22 - 96*m.b6*m.b9*m.b23 - 64*m.b6*m.b9*m.b24 - 32*m.b6*m.b9*m.b25 - 96*
                       m.b6*m.b10*m.b11 - 96*m.b6*m.b10*m.b12 - 256*m.b6*m.b10*m.b13 - 256*m.b6*m.b10*m.b14 - 256*m.b6*
                       m.b10*m.b15 - 224*m.b6*m.b10*m.b16 - 352*m.b6*m.b10*m.b17 - 320*m.b6*m.b10*m.b18 - 288*m.b6*m.b10
                       *m.b19 - 256*m.b6*m.b10*m.b20 - 192*m.b6*m.b10*m.b21 - 128*m.b6*m.b10*m.b22 - 96*m.b6*m.b10*m.b23
                        - 64*m.b6*m.b10*m.b24 - 32*m.b6*m.b10*m.b25 - 256*m.b6*m.b11*m.b12 - 256*m.b6*m.b11*m.b13 - 320*
                       m.b6*m.b11*m.b14 - 288*m.b6*m.b11*m.b15 - 192*m.b6*m.b11*m.b16 - 320*m.b6*m.b11*m.b17 - 288*m.b6*
                       m.b11*m.b18 - 256*m.b6*m.b11*m.b19 - 224*m.b6*m.b11*m.b20 - 160*m.b6*m.b11*m.b21 - 128*m.b6*m.b11
                       *m.b22 - 96*m.b6*m.b11*m.b23 - 64*m.b6*m.b11*m.b24 - 32*m.b6*m.b11*m.b25 - 256*m.b6*m.b12*m.b13
                        - 256*m.b6*m.b12*m.b14 - 288*m.b6*m.b12*m.b15 - 224*m.b6*m.b12*m.b16 - 320*m.b6*m.b12*m.b17 - 64
                       *m.b6*m.b12*m.b18 - 224*m.b6*m.b12*m.b19 - 192*m.b6*m.b12*m.b20 - 160*m.b6*m.b12*m.b21 - 128*m.b6
                       *m.b12*m.b22 - 96*m.b6*m.b12*m.b23 - 64*m.b6*m.b12*m.b24 - 32*m.b6*m.b12*m.b25 - 224*m.b6*m.b13*
                       m.b14 - 288*m.b6*m.b13*m.b15 - 224*m.b6*m.b13*m.b16 - 320*m.b6*m.b13*m.b17 - 256*m.b6*m.b13*m.b18
                        - 192*m.b6*m.b13*m.b19 - 160*m.b6*m.b13*m.b21 - 128*m.b6*m.b13*m.b22 - 96*m.b6*m.b13*m.b23 - 64*
                       m.b6*m.b13*m.b24 - 32*m.b6*m.b13*m.b25 - 160*m.b6*m.b14*m.b15 - 224*m.b6*m.b14*m.b16 - 320*m.b6*
                       m.b14*m.b17 - 256*m.b6*m.b14*m.b18 - 224*m.b6*m.b14*m.b19 - 192*m.b6*m.b14*m.b20 - 160*m.b6*m.b14
                       *m.b21 - 96*m.b6*m.b14*m.b23 - 64*m.b6*m.b14*m.b24 - 32*m.b6*m.b14*m.b25 - 224*m.b6*m.b15*m.b16
                        - 320*m.b6*m.b15*m.b17 - 288*m.b6*m.b15*m.b18 - 256*m.b6*m.b15*m.b19 - 224*m.b6*m.b15*m.b20 - 
                       160*m.b6*m.b15*m.b21 - 128*m.b6*m.b15*m.b22 - 96*m.b6*m.b15*m.b23 - 32*m.b6*m.b15*m.b25 - 352*
                       m.b6*m.b16*m.b17 - 320*m.b6*m.b16*m.b18 - 288*m.b6*m.b16*m.b19 - 256*m.b6*m.b16*m.b20 - 192*m.b6*
                       m.b16*m.b21 - 128*m.b6*m.b16*m.b22 - 96*m.b6*m.b16*m.b23 - 64*m.b6*m.b16*m.b24 - 32*m.b6*m.b16*
                       m.b25 - 352*m.b6*m.b17*m.b18 - 320*m.b6*m.b17*m.b19 - 288*m.b6*m.b17*m.b20 - 224*m.b6*m.b17*m.b21
                        - 160*m.b6*m.b17*m.b22 - 96*m.b6*m.b17*m.b23 - 64*m.b6*m.b17*m.b24 - 32*m.b6*m.b17*m.b25 - 352*
                       m.b6*m.b18*m.b19 - 320*m.b6*m.b18*m.b20 - 256*m.b6*m.b18*m.b21 - 192*m.b6*m.b18*m.b22 - 128*m.b6*
                       m.b18*m.b23 - 64*m.b6*m.b18*m.b24 - 32*m.b6*m.b18*m.b25 - 352*m.b6*m.b19*m.b20 - 288*m.b6*m.b19*
                       m.b21 - 224*m.b6*m.b19*m.b22 - 160*m.b6*m.b19*m.b23 - 96*m.b6*m.b19*m.b24 - 32*m.b6*m.b19*m.b25
                        - 320*m.b6*m.b20*m.b21 - 256*m.b6*m.b20*m.b22 - 192*m.b6*m.b20*m.b23 - 128*m.b6*m.b20*m.b24 - 64
                       *m.b6*m.b20*m.b25 - 256*m.b6*m.b21*m.b22 - 192*m.b6*m.b21*m.b23 - 128*m.b6*m.b21*m.b24 - 64*m.b6*
                       m.b21*m.b25 - 192*m.b6*m.b22*m.b23 - 128*m.b6*m.b22*m.b24 - 64*m.b6*m.b22*m.b25 - 128*m.b6*m.b23*
                       m.b24 - 64*m.b6*m.b23*m.b25 - 64*m.b6*m.b24*m.b25 - 64*m.b7*m.b8*m.b9 - 96*m.b7*m.b8*m.b10 - 96*
                       m.b7*m.b8*m.b11 - 96*m.b7*m.b8*m.b12 - 128*m.b7*m.b8*m.b13 - 96*m.b7*m.b8*m.b14 - 64*m.b7*m.b8*
                       m.b15 - 64*m.b7*m.b8*m.b16 - 256*m.b7*m.b8*m.b17 - 448*m.b7*m.b8*m.b18 - 416*m.b7*m.b8*m.b19 - 
                       352*m.b7*m.b8*m.b20 - 288*m.b7*m.b8*m.b21 - 224*m.b7*m.b8*m.b22 - 160*m.b7*m.b8*m.b23 - 96*m.b7*
                       m.b8*m.b24 - 32*m.b7*m.b8*m.b25 - 96*m.b7*m.b9*m.b10 - 64*m.b7*m.b9*m.b11 - 96*m.b7*m.b9*m.b12 - 
                       96*m.b7*m.b9*m.b13 - 128*m.b7*m.b9*m.b14 - 96*m.b7*m.b9*m.b15 - 256*m.b7*m.b9*m.b16 - 256*m.b7*
                       m.b9*m.b17 - 416*m.b7*m.b9*m.b18 - 384*m.b7*m.b9*m.b19 - 320*m.b7*m.b9*m.b20 - 256*m.b7*m.b9*
                       m.b21 - 192*m.b7*m.b9*m.b22 - 128*m.b7*m.b9*m.b23 - 64*m.b7*m.b9*m.b24 - 32*m.b7*m.b9*m.b25 - 96*
                       m.b7*m.b10*m.b11 - 96*m.b7*m.b10*m.b12 - 64*m.b7*m.b10*m.b13 - 160*m.b7*m.b10*m.b14 - 320*m.b7*
                       m.b10*m.b15 - 288*m.b7*m.b10*m.b16 - 224*m.b7*m.b10*m.b17 - 384*m.b7*m.b10*m.b18 - 352*m.b7*m.b10
                       *m.b19 - 288*m.b7*m.b10*m.b20 - 224*m.b7*m.b10*m.b21 - 160*m.b7*m.b10*m.b22 - 96*m.b7*m.b10*m.b23
                        - 64*m.b7*m.b10*m.b24 - 32*m.b7*m.b10*m.b25 - 96*m.b7*m.b11*m.b12 - 96*m.b7*m.b11*m.b13 - 288*
                       m.b7*m.b11*m.b14 - 320*m.b7*m.b11*m.b15 - 288*m.b7*m.b11*m.b16 - 224*m.b7*m.b11*m.b17 - 352*m.b7*
                       m.b11*m.b18 - 320*m.b7*m.b11*m.b19 - 256*m.b7*m.b11*m.b20 - 192*m.b7*m.b11*m.b21 - 128*m.b7*m.b11
                       *m.b22 - 96*m.b7*m.b11*m.b23 - 64*m.b7*m.b11*m.b24 - 32*m.b7*m.b11*m.b25 - 288*m.b7*m.b12*m.b13
                        - 288*m.b7*m.b12*m.b14 - 352*m.b7*m.b12*m.b15 - 288*m.b7*m.b12*m.b16 - 192*m.b7*m.b12*m.b17 - 
                       352*m.b7*m.b12*m.b18 - 288*m.b7*m.b12*m.b19 - 224*m.b7*m.b12*m.b20 - 160*m.b7*m.b12*m.b21 - 128*
                       m.b7*m.b12*m.b22 - 96*m.b7*m.b12*m.b23 - 64*m.b7*m.b12*m.b24 - 32*m.b7*m.b12*m.b25 - 256*m.b7*
                       m.b13*m.b14 - 224*m.b7*m.b13*m.b15 - 288*m.b7*m.b13*m.b16 - 224*m.b7*m.b13*m.b17 - 352*m.b7*m.b13
                       *m.b18 - 64*m.b7*m.b13*m.b19 - 192*m.b7*m.b13*m.b20 - 160*m.b7*m.b13*m.b21 - 128*m.b7*m.b13*m.b22
                        - 96*m.b7*m.b13*m.b23 - 64*m.b7*m.b13*m.b24 - 32*m.b7*m.b13*m.b25 - 192*m.b7*m.b14*m.b15 - 288*
                       m.b7*m.b14*m.b16 - 224*m.b7*m.b14*m.b17 - 352*m.b7*m.b14*m.b18 - 288*m.b7*m.b14*m.b19 - 224*m.b7*
                       m.b14*m.b20 - 128*m.b7*m.b14*m.b22 - 96*m.b7*m.b14*m.b23 - 64*m.b7*m.b14*m.b24 - 32*m.b7*m.b14*
                       m.b25 - 128*m.b7*m.b15*m.b16 - 224*m.b7*m.b15*m.b17 - 352*m.b7*m.b15*m.b18 - 320*m.b7*m.b15*m.b19
                        - 256*m.b7*m.b15*m.b20 - 192*m.b7*m.b15*m.b21 - 128*m.b7*m.b15*m.b22 - 64*m.b7*m.b15*m.b24 - 32*
                       m.b7*m.b15*m.b25 - 224*m.b7*m.b16*m.b17 - 384*m.b7*m.b16*m.b18 - 352*m.b7*m.b16*m.b19 - 288*m.b7*
                       m.b16*m.b20 - 224*m.b7*m.b16*m.b21 - 160*m.b7*m.b16*m.b22 - 96*m.b7*m.b16*m.b23 - 64*m.b7*m.b16*
                       m.b24 - 416*m.b7*m.b17*m.b18 - 384*m.b7*m.b17*m.b19 - 320*m.b7*m.b17*m.b20 - 256*m.b7*m.b17*m.b21
                        - 192*m.b7*m.b17*m.b22 - 128*m.b7*m.b17*m.b23 - 64*m.b7*m.b17*m.b24 - 32*m.b7*m.b17*m.b25 - 416*
                       m.b7*m.b18*m.b19 - 352*m.b7*m.b18*m.b20 - 288*m.b7*m.b18*m.b21 - 224*m.b7*m.b18*m.b22 - 160*m.b7*
                       m.b18*m.b23 - 96*m.b7*m.b18*m.b24 - 32*m.b7*m.b18*m.b25 - 384*m.b7*m.b19*m.b20 - 320*m.b7*m.b19*
                       m.b21 - 256*m.b7*m.b19*m.b22 - 192*m.b7*m.b19*m.b23 - 128*m.b7*m.b19*m.b24 - 64*m.b7*m.b19*m.b25
                        - 320*m.b7*m.b20*m.b21 - 256*m.b7*m.b20*m.b22 - 192*m.b7*m.b20*m.b23 - 128*m.b7*m.b20*m.b24 - 64
                       *m.b7*m.b20*m.b25 - 256*m.b7*m.b21*m.b22 - 192*m.b7*m.b21*m.b23 - 128*m.b7*m.b21*m.b24 - 64*m.b7*
                       m.b21*m.b25 - 192*m.b7*m.b22*m.b23 - 128*m.b7*m.b22*m.b24 - 64*m.b7*m.b22*m.b25 - 128*m.b7*m.b23*
                       m.b24 - 64*m.b7*m.b23*m.b25 - 64*m.b7*m.b24*m.b25 - 64*m.b8*m.b9*m.b10 - 96*m.b8*m.b9*m.b11 - 96*
                       m.b8*m.b9*m.b12 - 96*m.b8*m.b9*m.b13 - 160*m.b8*m.b9*m.b14 - 128*m.b8*m.b9*m.b15 - 96*m.b8*m.b9*
                       m.b16 - 64*m.b8*m.b9*m.b17 - 256*m.b8*m.b9*m.b18 - 416*m.b8*m.b9*m.b19 - 352*m.b8*m.b9*m.b20 - 
                       288*m.b8*m.b9*m.b21 - 224*m.b8*m.b9*m.b22 - 160*m.b8*m.b9*m.b23 - 96*m.b8*m.b9*m.b24 - 32*m.b8*
                       m.b9*m.b25 - 96*m.b8*m.b10*m.b11 - 64*m.b8*m.b10*m.b12 - 96*m.b8*m.b10*m.b13 - 96*m.b8*m.b10*
                       m.b14 - 160*m.b8*m.b10*m.b15 - 128*m.b8*m.b10*m.b16 - 288*m.b8*m.b10*m.b17 - 224*m.b8*m.b10*m.b18
                        - 384*m.b8*m.b10*m.b19 - 320*m.b8*m.b10*m.b20 - 256*m.b8*m.b10*m.b21 - 192*m.b8*m.b10*m.b22 - 
                       128*m.b8*m.b10*m.b23 - 64*m.b8*m.b10*m.b24 - 32*m.b8*m.b10*m.b25 - 96*m.b8*m.b11*m.b12 - 96*m.b8*
                       m.b11*m.b13 - 64*m.b8*m.b11*m.b14 - 192*m.b8*m.b11*m.b15 - 352*m.b8*m.b11*m.b16 - 288*m.b8*m.b11*
                       m.b17 - 224*m.b8*m.b11*m.b18 - 352*m.b8*m.b11*m.b19 - 288*m.b8*m.b11*m.b20 - 224*m.b8*m.b11*m.b21
                        - 160*m.b8*m.b11*m.b22 - 96*m.b8*m.b11*m.b23 - 64*m.b8*m.b11*m.b24 - 32*m.b8*m.b11*m.b25 - 96*
                       m.b8*m.b12*m.b13 - 96*m.b8*m.b12*m.b14 - 288*m.b8*m.b12*m.b15 - 320*m.b8*m.b12*m.b16 - 288*m.b8*
                       m.b12*m.b17 - 224*m.b8*m.b12*m.b18 - 352*m.b8*m.b12*m.b19 - 256*m.b8*m.b12*m.b20 - 192*m.b8*m.b12
                       *m.b21 - 128*m.b8*m.b12*m.b22 - 96*m.b8*m.b12*m.b23 - 64*m.b8*m.b12*m.b24 - 32*m.b8*m.b12*m.b25
                        - 288*m.b8*m.b13*m.b14 - 256*m.b8*m.b13*m.b15 - 352*m.b8*m.b13*m.b16 - 288*m.b8*m.b13*m.b17 - 
                       192*m.b8*m.b13*m.b18 - 352*m.b8*m.b13*m.b19 - 256*m.b8*m.b13*m.b20 - 160*m.b8*m.b13*m.b21 - 128*
                       m.b8*m.b13*m.b22 - 96*m.b8*m.b13*m.b23 - 64*m.b8*m.b13*m.b24 - 32*m.b8*m.b13*m.b25 - 224*m.b8*
                       m.b14*m.b15 - 192*m.b8*m.b14*m.b16 - 288*m.b8*m.b14*m.b17 - 224*m.b8*m.b14*m.b18 - 352*m.b8*m.b14
                       *m.b19 - 64*m.b8*m.b14*m.b20 - 192*m.b8*m.b14*m.b21 - 128*m.b8*m.b14*m.b22 - 96*m.b8*m.b14*m.b23
                        - 64*m.b8*m.b14*m.b24 - 32*m.b8*m.b14*m.b25 - 160*m.b8*m.b15*m.b16 - 288*m.b8*m.b15*m.b17 - 224*
                       m.b8*m.b15*m.b18 - 352*m.b8*m.b15*m.b19 - 288*m.b8*m.b15*m.b20 - 224*m.b8*m.b15*m.b21 - 32*m.b8*
                       m.b15*m.b22 - 96*m.b8*m.b15*m.b23 - 64*m.b8*m.b15*m.b24 - 32*m.b8*m.b15*m.b25 - 96*m.b8*m.b16*
                       m.b17 - 224*m.b8*m.b16*m.b18 - 384*m.b8*m.b16*m.b19 - 320*m.b8*m.b16*m.b20 - 256*m.b8*m.b16*m.b21
                        - 192*m.b8*m.b16*m.b22 - 128*m.b8*m.b16*m.b23 - 32*m.b8*m.b16*m.b25 - 256*m.b8*m.b17*m.b18 - 416
                       *m.b8*m.b17*m.b19 - 352*m.b8*m.b17*m.b20 - 288*m.b8*m.b17*m.b21 - 224*m.b8*m.b17*m.b22 - 160*m.b8
                       *m.b17*m.b23 - 96*m.b8*m.b17*m.b24 - 32*m.b8*m.b17*m.b25 - 448*m.b8*m.b18*m.b19 - 384*m.b8*m.b18*
                       m.b20 - 320*m.b8*m.b18*m.b21 - 256*m.b8*m.b18*m.b22 - 192*m.b8*m.b18*m.b23 - 128*m.b8*m.b18*m.b24
                        - 64*m.b8*m.b18*m.b25 - 384*m.b8*m.b19*m.b20 - 320*m.b8*m.b19*m.b21 - 256*m.b8*m.b19*m.b22 - 192
                       *m.b8*m.b19*m.b23 - 128*m.b8*m.b19*m.b24 - 64*m.b8*m.b19*m.b25 - 320*m.b8*m.b20*m.b21 - 256*m.b8*
                       m.b20*m.b22 - 192*m.b8*m.b20*m.b23 - 128*m.b8*m.b20*m.b24 - 64*m.b8*m.b20*m.b25 - 256*m.b8*m.b21*
                       m.b22 - 192*m.b8*m.b21*m.b23 - 128*m.b8*m.b21*m.b24 - 64*m.b8*m.b21*m.b25 - 192*m.b8*m.b22*m.b23
                        - 128*m.b8*m.b22*m.b24 - 64*m.b8*m.b22*m.b25 - 128*m.b8*m.b23*m.b24 - 64*m.b8*m.b23*m.b25 - 64*
                       m.b8*m.b24*m.b25 - 64*m.b9*m.b10*m.b11 - 96*m.b9*m.b10*m.b12 - 96*m.b9*m.b10*m.b13 - 96*m.b9*
                       m.b10*m.b14 - 192*m.b9*m.b10*m.b15 - 160*m.b9*m.b10*m.b16 - 128*m.b9*m.b10*m.b17 - 96*m.b9*m.b10*
                       m.b18 - 224*m.b9*m.b10*m.b19 - 352*m.b9*m.b10*m.b20 - 288*m.b9*m.b10*m.b21 - 224*m.b9*m.b10*m.b22
                        - 160*m.b9*m.b10*m.b23 - 96*m.b9*m.b10*m.b24 - 32*m.b9*m.b10*m.b25 - 96*m.b9*m.b11*m.b12 - 64*
                       m.b9*m.b11*m.b13 - 96*m.b9*m.b11*m.b14 - 96*m.b9*m.b11*m.b15 - 192*m.b9*m.b11*m.b16 - 160*m.b9*
                       m.b11*m.b17 - 288*m.b9*m.b11*m.b18 - 224*m.b9*m.b11*m.b19 - 320*m.b9*m.b11*m.b20 - 256*m.b9*m.b11
                       *m.b21 - 192*m.b9*m.b11*m.b22 - 128*m.b9*m.b11*m.b23 - 64*m.b9*m.b11*m.b24 - 32*m.b9*m.b11*m.b25
                        - 96*m.b9*m.b12*m.b13 - 96*m.b9*m.b12*m.b14 - 64*m.b9*m.b12*m.b15 - 224*m.b9*m.b12*m.b16 - 352*
                       m.b9*m.b12*m.b17 - 288*m.b9*m.b12*m.b18 - 224*m.b9*m.b12*m.b19 - 320*m.b9*m.b12*m.b20 - 224*m.b9*
                       m.b12*m.b21 - 160*m.b9*m.b12*m.b22 - 96*m.b9*m.b12*m.b23 - 64*m.b9*m.b12*m.b24 - 32*m.b9*m.b12*
                       m.b25 - 96*m.b9*m.b13*m.b14 - 96*m.b9*m.b13*m.b15 - 256*m.b9*m.b13*m.b16 - 320*m.b9*m.b13*m.b17
                        - 288*m.b9*m.b13*m.b18 - 224*m.b9*m.b13*m.b19 - 320*m.b9*m.b13*m.b20 - 224*m.b9*m.b13*m.b21 - 
                       128*m.b9*m.b13*m.b22 - 96*m.b9*m.b13*m.b23 - 64*m.b9*m.b13*m.b24 - 32*m.b9*m.b13*m.b25 - 256*m.b9
                       *m.b14*m.b15 - 224*m.b9*m.b14*m.b16 - 352*m.b9*m.b14*m.b17 - 288*m.b9*m.b14*m.b18 - 192*m.b9*
                       m.b14*m.b19 - 320*m.b9*m.b14*m.b20 - 224*m.b9*m.b14*m.b21 - 160*m.b9*m.b14*m.b22 - 96*m.b9*m.b14*
                       m.b23 - 64*m.b9*m.b14*m.b24 - 32*m.b9*m.b14*m.b25 - 192*m.b9*m.b15*m.b16 - 160*m.b9*m.b15*m.b17
                        - 288*m.b9*m.b15*m.b18 - 224*m.b9*m.b15*m.b19 - 320*m.b9*m.b15*m.b20 - 96*m.b9*m.b15*m.b21 - 192
                       *m.b9*m.b15*m.b22 - 128*m.b9*m.b15*m.b23 - 64*m.b9*m.b15*m.b24 - 32*m.b9*m.b15*m.b25 - 128*m.b9*
                       m.b16*m.b17 - 288*m.b9*m.b16*m.b18 - 224*m.b9*m.b16*m.b19 - 352*m.b9*m.b16*m.b20 - 288*m.b9*m.b16
                       *m.b21 - 224*m.b9*m.b16*m.b22 - 64*m.b9*m.b16*m.b23 - 96*m.b9*m.b16*m.b24 - 32*m.b9*m.b16*m.b25
                        - 64*m.b9*m.b17*m.b18 - 256*m.b9*m.b17*m.b19 - 384*m.b9*m.b17*m.b20 - 320*m.b9*m.b17*m.b21 - 256
                       *m.b9*m.b17*m.b22 - 192*m.b9*m.b17*m.b23 - 128*m.b9*m.b17*m.b24 - 32*m.b9*m.b17*m.b25 - 256*m.b9*
                       m.b18*m.b19 - 384*m.b9*m.b18*m.b20 - 320*m.b9*m.b18*m.b21 - 256*m.b9*m.b18*m.b22 - 192*m.b9*m.b18
                       *m.b23 - 128*m.b9*m.b18*m.b24 - 64*m.b9*m.b18*m.b25 - 384*m.b9*m.b19*m.b20 - 320*m.b9*m.b19*m.b21
                        - 256*m.b9*m.b19*m.b22 - 192*m.b9*m.b19*m.b23 - 128*m.b9*m.b19*m.b24 - 64*m.b9*m.b19*m.b25 - 320
                       *m.b9*m.b20*m.b21 - 256*m.b9*m.b20*m.b22 - 192*m.b9*m.b20*m.b23 - 128*m.b9*m.b20*m.b24 - 64*m.b9*
                       m.b20*m.b25 - 256*m.b9*m.b21*m.b22 - 192*m.b9*m.b21*m.b23 - 128*m.b9*m.b21*m.b24 - 64*m.b9*m.b21*
                       m.b25 - 192*m.b9*m.b22*m.b23 - 128*m.b9*m.b22*m.b24 - 64*m.b9*m.b22*m.b25 - 128*m.b9*m.b23*m.b24
                        - 64*m.b9*m.b23*m.b25 - 64*m.b9*m.b24*m.b25 - 64*m.b10*m.b11*m.b12 - 96*m.b10*m.b11*m.b13 - 96*
                       m.b10*m.b11*m.b14 - 96*m.b10*m.b11*m.b15 - 224*m.b10*m.b11*m.b16 - 192*m.b10*m.b11*m.b17 - 160*
                       m.b10*m.b11*m.b18 - 128*m.b10*m.b11*m.b19 - 224*m.b10*m.b11*m.b20 - 288*m.b10*m.b11*m.b21 - 224*
                       m.b10*m.b11*m.b22 - 160*m.b10*m.b11*m.b23 - 96*m.b10*m.b11*m.b24 - 32*m.b10*m.b11*m.b25 - 96*
                       m.b10*m.b12*m.b13 - 64*m.b10*m.b12*m.b14 - 96*m.b10*m.b12*m.b15 - 96*m.b10*m.b12*m.b16 - 224*
                       m.b10*m.b12*m.b17 - 192*m.b10*m.b12*m.b18 - 288*m.b10*m.b12*m.b19 - 224*m.b10*m.b12*m.b20 - 288*
                       m.b10*m.b12*m.b21 - 192*m.b10*m.b12*m.b22 - 128*m.b10*m.b12*m.b23 - 64*m.b10*m.b12*m.b24 - 32*
                       m.b10*m.b12*m.b25 - 96*m.b10*m.b13*m.b14 - 96*m.b10*m.b13*m.b15 - 64*m.b10*m.b13*m.b16 - 256*
                       m.b10*m.b13*m.b17 - 352*m.b10*m.b13*m.b18 - 288*m.b10*m.b13*m.b19 - 224*m.b10*m.b13*m.b20 - 288*
                       m.b10*m.b13*m.b21 - 192*m.b10*m.b13*m.b22 - 96*m.b10*m.b13*m.b23 - 64*m.b10*m.b13*m.b24 - 32*
                       m.b10*m.b13*m.b25 - 96*m.b10*m.b14*m.b15 - 96*m.b10*m.b14*m.b16 - 224*m.b10*m.b14*m.b17 - 320*
                       m.b10*m.b14*m.b18 - 288*m.b10*m.b14*m.b19 - 224*m.b10*m.b14*m.b20 - 288*m.b10*m.b14*m.b21 - 192*
                       m.b10*m.b14*m.b22 - 128*m.b10*m.b14*m.b23 - 64*m.b10*m.b14*m.b24 - 32*m.b10*m.b14*m.b25 - 224*
                       m.b10*m.b15*m.b16 - 192*m.b10*m.b15*m.b17 - 352*m.b10*m.b15*m.b18 - 288*m.b10*m.b15*m.b19 - 192*
                       m.b10*m.b15*m.b20 - 288*m.b10*m.b15*m.b21 - 224*m.b10*m.b15*m.b22 - 160*m.b10*m.b15*m.b23 - 96*
                       m.b10*m.b15*m.b24 - 32*m.b10*m.b15*m.b25 - 160*m.b10*m.b16*m.b17 - 128*m.b10*m.b16*m.b18 - 288*
                       m.b10*m.b16*m.b19 - 224*m.b10*m.b16*m.b20 - 320*m.b10*m.b16*m.b21 - 128*m.b10*m.b16*m.b22 - 192*
                       m.b10*m.b16*m.b23 - 128*m.b10*m.b16*m.b24 - 64*m.b10*m.b16*m.b25 - 96*m.b10*m.b17*m.b18 - 256*
                       m.b10*m.b17*m.b19 - 224*m.b10*m.b17*m.b20 - 320*m.b10*m.b17*m.b21 - 256*m.b10*m.b17*m.b22 - 192*
                       m.b10*m.b17*m.b23 - 64*m.b10*m.b17*m.b24 - 64*m.b10*m.b17*m.b25 - 64*m.b10*m.b18*m.b19 - 224*
                       m.b10*m.b18*m.b20 - 320*m.b10*m.b18*m.b21 - 256*m.b10*m.b18*m.b22 - 192*m.b10*m.b18*m.b23 - 128*
                       m.b10*m.b18*m.b24 - 64*m.b10*m.b18*m.b25 - 224*m.b10*m.b19*m.b20 - 320*m.b10*m.b19*m.b21 - 256*
                       m.b10*m.b19*m.b22 - 192*m.b10*m.b19*m.b23 - 128*m.b10*m.b19*m.b24 - 64*m.b10*m.b19*m.b25 - 320*
                       m.b10*m.b20*m.b21 - 256*m.b10*m.b20*m.b22 - 192*m.b10*m.b20*m.b23 - 128*m.b10*m.b20*m.b24 - 64*
                       m.b10*m.b20*m.b25 - 256*m.b10*m.b21*m.b22 - 192*m.b10*m.b21*m.b23 - 128*m.b10*m.b21*m.b24 - 64*
                       m.b10*m.b21*m.b25 - 192*m.b10*m.b22*m.b23 - 128*m.b10*m.b22*m.b24 - 64*m.b10*m.b22*m.b25 - 128*
                       m.b10*m.b23*m.b24 - 64*m.b10*m.b23*m.b25 - 64*m.b10*m.b24*m.b25 - 64*m.b11*m.b12*m.b13 - 96*m.b11
                       *m.b12*m.b14 - 96*m.b11*m.b12*m.b15 - 96*m.b11*m.b12*m.b16 - 256*m.b11*m.b12*m.b17 - 224*m.b11*
                       m.b12*m.b18 - 192*m.b11*m.b12*m.b19 - 160*m.b11*m.b12*m.b20 - 224*m.b11*m.b12*m.b21 - 256*m.b11*
                       m.b12*m.b22 - 160*m.b11*m.b12*m.b23 - 96*m.b11*m.b12*m.b24 - 32*m.b11*m.b12*m.b25 - 96*m.b11*
                       m.b13*m.b14 - 64*m.b11*m.b13*m.b15 - 96*m.b11*m.b13*m.b16 - 96*m.b11*m.b13*m.b17 - 256*m.b11*
                       m.b13*m.b18 - 224*m.b11*m.b13*m.b19 - 288*m.b11*m.b13*m.b20 - 224*m.b11*m.b13*m.b21 - 256*m.b11*
                       m.b13*m.b22 - 160*m.b11*m.b13*m.b23 - 64*m.b11*m.b13*m.b24 - 32*m.b11*m.b13*m.b25 - 96*m.b11*
                       m.b14*m.b15 - 96*m.b11*m.b14*m.b16 - 64*m.b11*m.b14*m.b17 - 288*m.b11*m.b14*m.b18 - 352*m.b11*
                       m.b14*m.b19 - 288*m.b11*m.b14*m.b20 - 224*m.b11*m.b14*m.b21 - 256*m.b11*m.b14*m.b22 - 160*m.b11*
                       m.b14*m.b23 - 96*m.b11*m.b14*m.b24 - 32*m.b11*m.b14*m.b25 - 96*m.b11*m.b15*m.b16 - 96*m.b11*m.b15
                       *m.b17 - 192*m.b11*m.b15*m.b18 - 320*m.b11*m.b15*m.b19 - 288*m.b11*m.b15*m.b20 - 224*m.b11*m.b15*
                       m.b21 - 256*m.b11*m.b15*m.b22 - 192*m.b11*m.b15*m.b23 - 128*m.b11*m.b15*m.b24 - 64*m.b11*m.b15*
                       m.b25 - 192*m.b11*m.b16*m.b17 - 160*m.b11*m.b16*m.b18 - 320*m.b11*m.b16*m.b19 - 256*m.b11*m.b16*
                       m.b20 - 160*m.b11*m.b16*m.b21 - 256*m.b11*m.b16*m.b22 - 192*m.b11*m.b16*m.b23 - 128*m.b11*m.b16*
                       m.b24 - 64*m.b11*m.b16*m.b25 - 128*m.b11*m.b17*m.b18 - 96*m.b11*m.b17*m.b19 - 224*m.b11*m.b17*
                       m.b20 - 192*m.b11*m.b17*m.b21 - 256*m.b11*m.b17*m.b22 - 96*m.b11*m.b17*m.b23 - 128*m.b11*m.b17*
                       m.b24 - 64*m.b11*m.b17*m.b25 - 64*m.b11*m.b18*m.b19 - 224*m.b11*m.b18*m.b20 - 192*m.b11*m.b18*
                       m.b21 - 256*m.b11*m.b18*m.b22 - 192*m.b11*m.b18*m.b23 - 128*m.b11*m.b18*m.b24 - 32*m.b11*m.b18*
                       m.b25 - 64*m.b11*m.b19*m.b20 - 192*m.b11*m.b19*m.b21 - 256*m.b11*m.b19*m.b22 - 192*m.b11*m.b19*
                       m.b23 - 128*m.b11*m.b19*m.b24 - 64*m.b11*m.b19*m.b25 - 192*m.b11*m.b20*m.b21 - 256*m.b11*m.b20*
                       m.b22 - 192*m.b11*m.b20*m.b23 - 128*m.b11*m.b20*m.b24 - 64*m.b11*m.b20*m.b25 - 256*m.b11*m.b21*
                       m.b22 - 192*m.b11*m.b21*m.b23 - 128*m.b11*m.b21*m.b24 - 64*m.b11*m.b21*m.b25 - 192*m.b11*m.b22*
                       m.b23 - 128*m.b11*m.b22*m.b24 - 64*m.b11*m.b22*m.b25 - 128*m.b11*m.b23*m.b24 - 64*m.b11*m.b23*
                       m.b25 - 64*m.b11*m.b24*m.b25 - 64*m.b12*m.b13*m.b14 - 96*m.b12*m.b13*m.b15 - 96*m.b12*m.b13*m.b16
                        - 96*m.b12*m.b13*m.b17 - 288*m.b12*m.b13*m.b18 - 256*m.b12*m.b13*m.b19 - 224*m.b12*m.b13*m.b20
                        - 192*m.b12*m.b13*m.b21 - 224*m.b12*m.b13*m.b22 - 224*m.b12*m.b13*m.b23 - 128*m.b12*m.b13*m.b24
                        - 32*m.b12*m.b13*m.b25 - 96*m.b12*m.b14*m.b15 - 64*m.b12*m.b14*m.b16 - 96*m.b12*m.b14*m.b17 - 96
                       *m.b12*m.b14*m.b18 - 288*m.b12*m.b14*m.b19 - 256*m.b12*m.b14*m.b20 - 288*m.b12*m.b14*m.b21 - 224*
                       m.b12*m.b14*m.b22 - 224*m.b12*m.b14*m.b23 - 128*m.b12*m.b14*m.b24 - 64*m.b12*m.b14*m.b25 - 96*
                       m.b12*m.b15*m.b16 - 96*m.b12*m.b15*m.b17 - 64*m.b12*m.b15*m.b18 - 288*m.b12*m.b15*m.b19 - 320*
                       m.b12*m.b15*m.b20 - 256*m.b12*m.b15*m.b21 - 192*m.b12*m.b15*m.b22 - 192*m.b12*m.b15*m.b23 - 128*
                       m.b12*m.b15*m.b24 - 64*m.b12*m.b15*m.b25 - 96*m.b12*m.b16*m.b17 - 96*m.b12*m.b16*m.b18 - 160*
                       m.b12*m.b16*m.b19 - 256*m.b12*m.b16*m.b20 - 224*m.b12*m.b16*m.b21 - 160*m.b12*m.b16*m.b22 - 192*
                       m.b12*m.b16*m.b23 - 128*m.b12*m.b16*m.b24 - 64*m.b12*m.b16*m.b25 - 160*m.b12*m.b17*m.b18 - 128*
                       m.b12*m.b17*m.b19 - 256*m.b12*m.b17*m.b20 - 192*m.b12*m.b17*m.b21 - 128*m.b12*m.b17*m.b22 - 192*
                       m.b12*m.b17*m.b23 - 128*m.b12*m.b17*m.b24 - 64*m.b12*m.b17*m.b25 - 96*m.b12*m.b18*m.b19 - 64*
                       m.b12*m.b18*m.b20 - 192*m.b12*m.b18*m.b21 - 160*m.b12*m.b18*m.b22 - 192*m.b12*m.b18*m.b23 - 64*
                       m.b12*m.b18*m.b24 - 64*m.b12*m.b18*m.b25 - 64*m.b12*m.b19*m.b20 - 192*m.b12*m.b19*m.b21 - 160*
                       m.b12*m.b19*m.b22 - 192*m.b12*m.b19*m.b23 - 128*m.b12*m.b19*m.b24 - 64*m.b12*m.b19*m.b25 - 64*
                       m.b12*m.b20*m.b21 - 160*m.b12*m.b20*m.b22 - 192*m.b12*m.b20*m.b23 - 128*m.b12*m.b20*m.b24 - 64*
                       m.b12*m.b20*m.b25 - 160*m.b12*m.b21*m.b22 - 192*m.b12*m.b21*m.b23 - 128*m.b12*m.b21*m.b24 - 64*
                       m.b12*m.b21*m.b25 - 192*m.b12*m.b22*m.b23 - 128*m.b12*m.b22*m.b24 - 64*m.b12*m.b22*m.b25 - 128*
                       m.b12*m.b23*m.b24 - 64*m.b12*m.b23*m.b25 - 64*m.b12*m.b24*m.b25 - 64*m.b13*m.b14*m.b15 - 96*m.b13
                       *m.b14*m.b16 - 96*m.b13*m.b14*m.b17 - 96*m.b13*m.b14*m.b18 - 288*m.b13*m.b14*m.b19 - 256*m.b13*
                       m.b14*m.b20 - 224*m.b13*m.b14*m.b21 - 192*m.b13*m.b14*m.b22 - 192*m.b13*m.b14*m.b23 - 160*m.b13*
                       m.b14*m.b24 - 64*m.b13*m.b14*m.b25 - 96*m.b13*m.b15*m.b16 - 64*m.b13*m.b15*m.b17 - 96*m.b13*m.b15
                       *m.b18 - 96*m.b13*m.b15*m.b19 - 256*m.b13*m.b15*m.b20 - 224*m.b13*m.b15*m.b21 - 224*m.b13*m.b15*
                       m.b22 - 160*m.b13*m.b15*m.b23 - 128*m.b13*m.b15*m.b24 - 64*m.b13*m.b15*m.b25 - 96*m.b13*m.b16*
                       m.b17 - 96*m.b13*m.b16*m.b18 - 64*m.b13*m.b16*m.b19 - 256*m.b13*m.b16*m.b20 - 256*m.b13*m.b16*
                       m.b21 - 192*m.b13*m.b16*m.b22 - 128*m.b13*m.b16*m.b23 - 128*m.b13*m.b16*m.b24 - 64*m.b13*m.b16*
                       m.b25 - 96*m.b13*m.b17*m.b18 - 96*m.b13*m.b17*m.b19 - 128*m.b13*m.b17*m.b20 - 192*m.b13*m.b17*
                       m.b21 - 160*m.b13*m.b17*m.b22 - 128*m.b13*m.b17*m.b23 - 128*m.b13*m.b17*m.b24 - 64*m.b13*m.b17*
                       m.b25 - 128*m.b13*m.b18*m.b19 - 96*m.b13*m.b18*m.b20 - 192*m.b13*m.b18*m.b21 - 160*m.b13*m.b18*
                       m.b22 - 96*m.b13*m.b18*m.b23 - 128*m.b13*m.b18*m.b24 - 64*m.b13*m.b18*m.b25 - 64*m.b13*m.b19*
                       m.b20 - 64*m.b13*m.b19*m.b21 - 160*m.b13*m.b19*m.b22 - 128*m.b13*m.b19*m.b23 - 128*m.b13*m.b19*
                       m.b24 - 32*m.b13*m.b19*m.b25 - 64*m.b13*m.b20*m.b21 - 160*m.b13*m.b20*m.b22 - 128*m.b13*m.b20*
                       m.b23 - 128*m.b13*m.b20*m.b24 - 64*m.b13*m.b20*m.b25 - 64*m.b13*m.b21*m.b22 - 128*m.b13*m.b21*
                       m.b23 - 128*m.b13*m.b21*m.b24 - 64*m.b13*m.b21*m.b25 - 128*m.b13*m.b22*m.b23 - 128*m.b13*m.b22*
                       m.b24 - 64*m.b13*m.b22*m.b25 - 128*m.b13*m.b23*m.b24 - 64*m.b13*m.b23*m.b25 - 64*m.b13*m.b24*
                       m.b25 - 64*m.b14*m.b15*m.b16 - 96*m.b14*m.b15*m.b17 - 96*m.b14*m.b15*m.b18 - 96*m.b14*m.b15*m.b19
                        - 256*m.b14*m.b15*m.b20 - 224*m.b14*m.b15*m.b21 - 192*m.b14*m.b15*m.b22 - 160*m.b14*m.b15*m.b23
                        - 128*m.b14*m.b15*m.b24 - 64*m.b14*m.b15*m.b25 - 96*m.b14*m.b16*m.b17 - 64*m.b14*m.b16*m.b18 - 
                       96*m.b14*m.b16*m.b19 - 96*m.b14*m.b16*m.b20 - 224*m.b14*m.b16*m.b21 - 192*m.b14*m.b16*m.b22 - 160
                       *m.b14*m.b16*m.b23 - 96*m.b14*m.b16*m.b24 - 64*m.b14*m.b16*m.b25 - 96*m.b14*m.b17*m.b18 - 96*
                       m.b14*m.b17*m.b19 - 64*m.b14*m.b17*m.b20 - 224*m.b14*m.b17*m.b21 - 192*m.b14*m.b17*m.b22 - 128*
                       m.b14*m.b17*m.b23 - 96*m.b14*m.b17*m.b24 - 64*m.b14*m.b17*m.b25 - 96*m.b14*m.b18*m.b19 - 96*m.b14
                       *m.b18*m.b20 - 96*m.b14*m.b18*m.b21 - 128*m.b14*m.b18*m.b22 - 128*m.b14*m.b18*m.b23 - 96*m.b14*
                       m.b18*m.b24 - 64*m.b14*m.b18*m.b25 - 96*m.b14*m.b19*m.b20 - 64*m.b14*m.b19*m.b21 - 160*m.b14*
                       m.b19*m.b22 - 128*m.b14*m.b19*m.b23 - 64*m.b14*m.b19*m.b24 - 64*m.b14*m.b19*m.b25 - 64*m.b14*
                       m.b20*m.b21 - 64*m.b14*m.b20*m.b22 - 128*m.b14*m.b20*m.b23 - 96*m.b14*m.b20*m.b24 - 64*m.b14*
                       m.b20*m.b25 - 64*m.b14*m.b21*m.b22 - 128*m.b14*m.b21*m.b23 - 96*m.b14*m.b21*m.b24 - 64*m.b14*
                       m.b21*m.b25 - 64*m.b14*m.b22*m.b23 - 96*m.b14*m.b22*m.b24 - 64*m.b14*m.b22*m.b25 - 96*m.b14*m.b23
                       *m.b24 - 64*m.b14*m.b23*m.b25 - 64*m.b14*m.b24*m.b25 - 64*m.b15*m.b16*m.b17 - 96*m.b15*m.b16*
                       m.b18 - 96*m.b15*m.b16*m.b19 - 96*m.b15*m.b16*m.b20 - 224*m.b15*m.b16*m.b21 - 192*m.b15*m.b16*
                       m.b22 - 160*m.b15*m.b16*m.b23 - 128*m.b15*m.b16*m.b24 - 64*m.b15*m.b16*m.b25 - 96*m.b15*m.b17*
                       m.b18 - 64*m.b15*m.b17*m.b19 - 96*m.b15*m.b17*m.b20 - 96*m.b15*m.b17*m.b21 - 192*m.b15*m.b17*
                       m.b22 - 160*m.b15*m.b17*m.b23 - 96*m.b15*m.b17*m.b24 - 64*m.b15*m.b17*m.b25 - 96*m.b15*m.b18*
                       m.b19 - 96*m.b15*m.b18*m.b20 - 64*m.b15*m.b18*m.b21 - 192*m.b15*m.b18*m.b22 - 128*m.b15*m.b18*
                       m.b23 - 96*m.b15*m.b18*m.b24 - 64*m.b15*m.b18*m.b25 - 96*m.b15*m.b19*m.b20 - 96*m.b15*m.b19*m.b21
                        - 64*m.b15*m.b19*m.b22 - 96*m.b15*m.b19*m.b23 - 96*m.b15*m.b19*m.b24 - 64*m.b15*m.b19*m.b25 - 64
                       *m.b15*m.b20*m.b21 - 64*m.b15*m.b20*m.b22 - 128*m.b15*m.b20*m.b23 - 96*m.b15*m.b20*m.b24 - 32*
                       m.b15*m.b20*m.b25 - 64*m.b15*m.b21*m.b22 - 64*m.b15*m.b21*m.b23 - 96*m.b15*m.b21*m.b24 - 64*m.b15
                       *m.b21*m.b25 - 64*m.b15*m.b22*m.b23 - 96*m.b15*m.b22*m.b24 - 64*m.b15*m.b22*m.b25 - 64*m.b15*
                       m.b23*m.b24 - 64*m.b15*m.b23*m.b25 - 64*m.b15*m.b24*m.b25 - 64*m.b16*m.b17*m.b18 - 96*m.b16*m.b17
                       *m.b19 - 96*m.b16*m.b17*m.b20 - 96*m.b16*m.b17*m.b21 - 192*m.b16*m.b17*m.b22 - 160*m.b16*m.b17*
                       m.b23 - 128*m.b16*m.b17*m.b24 - 64*m.b16*m.b17*m.b25 - 96*m.b16*m.b18*m.b19 - 64*m.b16*m.b18*
                       m.b20 - 96*m.b16*m.b18*m.b21 - 96*m.b16*m.b18*m.b22 - 160*m.b16*m.b18*m.b23 - 96*m.b16*m.b18*
                       m.b24 - 64*m.b16*m.b18*m.b25 - 96*m.b16*m.b19*m.b20 - 96*m.b16*m.b19*m.b21 - 64*m.b16*m.b19*m.b22
                        - 128*m.b16*m.b19*m.b23 - 96*m.b16*m.b19*m.b24 - 64*m.b16*m.b19*m.b25 - 96*m.b16*m.b20*m.b21 - 
                       64*m.b16*m.b20*m.b22 - 64*m.b16*m.b20*m.b23 - 64*m.b16*m.b20*m.b24 - 64*m.b16*m.b20*m.b25 - 64*
                       m.b16*m.b21*m.b22 - 64*m.b16*m.b21*m.b23 - 96*m.b16*m.b21*m.b24 - 64*m.b16*m.b21*m.b25 - 64*m.b16
                       *m.b22*m.b23 - 64*m.b16*m.b22*m.b24 - 64*m.b16*m.b22*m.b25 - 64*m.b16*m.b23*m.b24 - 64*m.b16*
                       m.b23*m.b25 - 64*m.b16*m.b24*m.b25 - 64*m.b17*m.b18*m.b19 - 96*m.b17*m.b18*m.b20 - 96*m.b17*m.b18
                       *m.b21 - 96*m.b17*m.b18*m.b22 - 160*m.b17*m.b18*m.b23 - 128*m.b17*m.b18*m.b24 - 64*m.b17*m.b18*
                       m.b25 - 96*m.b17*m.b19*m.b20 - 64*m.b17*m.b19*m.b21 - 96*m.b17*m.b19*m.b22 - 96*m.b17*m.b19*m.b23
                        - 96*m.b17*m.b19*m.b24 - 64*m.b17*m.b19*m.b25 - 96*m.b17*m.b20*m.b21 - 96*m.b17*m.b20*m.b22 - 32
                       *m.b17*m.b20*m.b23 - 96*m.b17*m.b20*m.b24 - 64*m.b17*m.b20*m.b25 - 64*m.b17*m.b21*m.b22 - 64*
                       m.b17*m.b21*m.b23 - 64*m.b17*m.b21*m.b24 - 32*m.b17*m.b21*m.b25 - 64*m.b17*m.b22*m.b23 - 64*m.b17
                       *m.b22*m.b24 - 64*m.b17*m.b22*m.b25 - 64*m.b17*m.b23*m.b24 - 64*m.b17*m.b23*m.b25 - 64*m.b17*
                       m.b24*m.b25 - 64*m.b18*m.b19*m.b20 - 96*m.b18*m.b19*m.b21 - 96*m.b18*m.b19*m.b22 - 96*m.b18*m.b19
                       *m.b23 - 128*m.b18*m.b19*m.b24 - 64*m.b18*m.b19*m.b25 - 96*m.b18*m.b20*m.b21 - 64*m.b18*m.b20*
                       m.b22 - 96*m.b18*m.b20*m.b23 - 64*m.b18*m.b20*m.b24 - 64*m.b18*m.b20*m.b25 - 96*m.b18*m.b21*m.b22
                        - 64*m.b18*m.b21*m.b23 - 32*m.b18*m.b21*m.b24 - 64*m.b18*m.b21*m.b25 - 64*m.b18*m.b22*m.b23 - 64
                       *m.b18*m.b22*m.b24 - 64*m.b18*m.b22*m.b25 - 64*m.b18*m.b23*m.b24 - 64*m.b18*m.b23*m.b25 - 64*
                       m.b18*m.b24*m.b25 - 64*m.b19*m.b20*m.b21 - 96*m.b19*m.b20*m.b22 - 96*m.b19*m.b20*m.b23 - 96*m.b19
                       *m.b20*m.b24 - 64*m.b19*m.b20*m.b25 - 96*m.b19*m.b21*m.b22 - 64*m.b19*m.b21*m.b23 - 64*m.b19*
                       m.b21*m.b24 - 64*m.b19*m.b21*m.b25 - 64*m.b19*m.b22*m.b23 - 64*m.b19*m.b22*m.b24 - 32*m.b19*m.b22
                       *m.b25 - 64*m.b19*m.b23*m.b24 - 64*m.b19*m.b23*m.b25 - 64*m.b19*m.b24*m.b25 - 64*m.b20*m.b21*
                       m.b22 - 96*m.b20*m.b21*m.b23 - 96*m.b20*m.b21*m.b24 - 64*m.b20*m.b21*m.b25 - 96*m.b20*m.b22*m.b23
                        - 32*m.b20*m.b22*m.b24 - 64*m.b20*m.b22*m.b25 - 64*m.b20*m.b23*m.b24 - 64*m.b20*m.b23*m.b25 - 64
                       *m.b20*m.b24*m.b25 - 64*m.b21*m.b22*m.b23 - 96*m.b21*m.b22*m.b24 - 64*m.b21*m.b22*m.b25 - 64*
                       m.b21*m.b23*m.b24 - 32*m.b21*m.b23*m.b25 - 64*m.b21*m.b24*m.b25 - 64*m.b22*m.b23*m.b24 - 64*m.b22
                       *m.b23*m.b25 - 64*m.b22*m.b24*m.b25 - 32*m.b23*m.b24*m.b25 + 352*m.b1*m.b2 + 344*m.b1*m.b3 + 336*
                       m.b1*m.b4 + 328*m.b1*m.b5 + 320*m.b1*m.b6 + 312*m.b1*m.b7 + 304*m.b1*m.b8 + 296*m.b1*m.b9 + 288*
                       m.b1*m.b10 + 280*m.b1*m.b11 + 272*m.b1*m.b12 + 264*m.b1*m.b13 + 272*m.b1*m.b14 + 264*m.b1*m.b15
                        + 256*m.b1*m.b16 + 248*m.b1*m.b17 + 240*m.b1*m.b18 + 232*m.b1*m.b19 + 224*m.b1*m.b20 + 216*m.b1*
                       m.b21 + 208*m.b1*m.b22 + 200*m.b1*m.b23 + 192*m.b1*m.b24 + 184*m.b1*m.b25 + 544*m.b2*m.b3 + 552*
                       m.b2*m.b4 + 544*m.b2*m.b5 + 536*m.b2*m.b6 + 528*m.b2*m.b7 + 504*m.b2*m.b8 + 496*m.b2*m.b9 + 488*
                       m.b2*m.b10 + 480*m.b2*m.b11 + 472*m.b2*m.b12 + 528*m.b2*m.b13 + 536*m.b2*m.b14 + 528*m.b2*m.b15
                        + 504*m.b2*m.b16 + 496*m.b2*m.b17 + 472*m.b2*m.b18 + 464*m.b2*m.b19 + 440*m.b2*m.b20 + 432*m.b2*
                       m.b21 + 408*m.b2*m.b22 + 400*m.b2*m.b23 + 376*m.b2*m.b24 + 192*m.b2*m.b25 + 704*m.b3*m.b4 + 696*
                       m.b3*m.b5 + 704*m.b3*m.b6 + 696*m.b3*m.b7 + 688*m.b3*m.b8 + 648*m.b3*m.b9 + 640*m.b3*m.b10 + 632*
                       m.b3*m.b11 + 640*m.b3*m.b12 + 648*m.b3*m.b13 + 800*m.b3*m.b14 + 776*m.b3*m.b15 + 768*m.b3*m.b16
                        + 728*m.b3*m.b17 + 720*m.b3*m.b18 + 680*m.b3*m.b19 + 672*m.b3*m.b20 + 632*m.b3*m.b21 + 624*m.b3*
                       m.b22 + 584*m.b3*m.b23 + 400*m.b3*m.b24 + 200*m.b3*m.b25 + 816*m.b4*m.b5 + 808*m.b4*m.b6 + 800*
                       m.b4*m.b7 + 808*m.b4*m.b8 + 800*m.b4*m.b9 + 744*m.b4*m.b10 + 752*m.b4*m.b11 + 744*m.b4*m.b12 + 
                       784*m.b4*m.b13 + 840*m.b4*m.b14 + 1056*m.b4*m.b15 + 1000*m.b4*m.b16 + 992*m.b4*m.b17 + 936*m.b4*
                       m.b18 + 928*m.b4*m.b19 + 872*m.b4*m.b20 + 864*m.b4*m.b21 + 808*m.b4*m.b22 + 624*m.b4*m.b23 + 408*
                       m.b4*m.b24 + 208*m.b4*m.b25 + 880*m.b5*m.b6 + 872*m.b5*m.b7 + 864*m.b5*m.b8 + 856*m.b5*m.b9 + 880
                       *m.b5*m.b10 + 808*m.b5*m.b11 + 832*m.b5*m.b12 + 840*m.b5*m.b13 + 944*m.b5*m.b14 + 1016*m.b5*m.b15
                        + 1280*m.b5*m.b16 + 1208*m.b5*m.b17 + 1200*m.b5*m.b18 + 1128*m.b5*m.b19 + 1120*m.b5*m.b20 + 1048
                       *m.b5*m.b21 + 864*m.b5*m.b22 + 632*m.b5*m.b23 + 432*m.b5*m.b24 + 216*m.b5*m.b25 + 896*m.b6*m.b7
                        + 888*m.b6*m.b8 + 896*m.b6*m.b9 + 888*m.b6*m.b10 + 912*m.b6*m.b11 + 840*m.b6*m.b12 + 896*m.b6*
                       m.b13 + 952*m.b6*m.b14 + 1088*m.b6*m.b15 + 1176*m.b6*m.b16 + 1488*m.b6*m.b17 + 1400*m.b6*m.b18 + 
                       1392*m.b6*m.b19 + 1304*m.b6*m.b20 + 1120*m.b6*m.b21 + 872*m.b6*m.b22 + 672*m.b6*m.b23 + 440*m.b6*
                       m.b24 + 224*m.b6*m.b25 + 880*m.b7*m.b8 + 872*m.b7*m.b9 + 896*m.b7*m.b10 + 888*m.b7*m.b11 + 928*
                       m.b7*m.b12 + 840*m.b7*m.b13 + 976*m.b7*m.b14 + 1048*m.b7*m.b15 + 1216*m.b7*m.b16 + 1304*m.b7*
                       m.b17 + 1680*m.b7*m.b18 + 1576*m.b7*m.b19 + 1392*m.b7*m.b20 + 1128*m.b7*m.b21 + 928*m.b7*m.b22 + 
                       680*m.b7*m.b23 + 464*m.b7*m.b24 + 232*m.b7*m.b25 + 832*m.b8*m.b9 + 824*m.b8*m.b10 + 864*m.b8*
                       m.b11 + 856*m.b8*m.b12 + 928*m.b8*m.b13 + 856*m.b8*m.b14 + 1024*m.b8*m.b15 + 1128*m.b8*m.b16 + 
                       1328*m.b8*m.b17 + 1416*m.b8*m.b18 + 1680*m.b8*m.b19 + 1400*m.b8*m.b20 + 1200*m.b8*m.b21 + 936*
                       m.b8*m.b22 + 720*m.b8*m.b23 + 472*m.b8*m.b24 + 240*m.b8*m.b25 + 800*m.b9*m.b10 + 792*m.b9*m.b11
                        + 848*m.b9*m.b12 + 856*m.b9*m.b13 + 960*m.b9*m.b14 + 904*m.b9*m.b15 + 1104*m.b9*m.b16 + 1224*
                       m.b9*m.b17 + 1328*m.b9*m.b18 + 1304*m.b9*m.b19 + 1488*m.b9*m.b20 + 1208*m.b9*m.b21 + 992*m.b9*
                       m.b22 + 728*m.b9*m.b23 + 496*m.b9*m.b24 + 248*m.b9*m.b25 + 800*m.b10*m.b11 + 792*m.b10*m.b12 + 
                       880*m.b10*m.b13 + 904*m.b10*m.b14 + 1040*m.b10*m.b15 + 1000*m.b10*m.b16 + 1104*m.b10*m.b17 + 1128
                       *m.b10*m.b18 + 1216*m.b10*m.b19 + 1176*m.b10*m.b20 + 1280*m.b10*m.b21 + 1000*m.b10*m.b22 + 768*
                       m.b10*m.b23 + 504*m.b10*m.b24 + 256*m.b10*m.b25 + 832*m.b11*m.b12 + 840*m.b11*m.b13 + 960*m.b11*
                       m.b14 + 1000*m.b11*m.b15 + 1040*m.b11*m.b16 + 904*m.b11*m.b17 + 1024*m.b11*m.b18 + 1048*m.b11*
                       m.b19 + 1088*m.b11*m.b20 + 1016*m.b11*m.b21 + 1056*m.b11*m.b22 + 776*m.b11*m.b23 + 528*m.b11*
                       m.b24 + 264*m.b11*m.b25 + 912*m.b12*m.b13 + 936*m.b12*m.b14 + 960*m.b12*m.b15 + 904*m.b12*m.b16
                        + 960*m.b12*m.b17 + 856*m.b12*m.b18 + 976*m.b12*m.b19 + 952*m.b12*m.b20 + 944*m.b12*m.b21 + 840*
                       m.b12*m.b22 + 800*m.b12*m.b23 + 536*m.b12*m.b24 + 272*m.b12*m.b25 + 912*m.b13*m.b14 + 840*m.b13*
                       m.b15 + 880*m.b13*m.b16 + 856*m.b13*m.b17 + 928*m.b13*m.b18 + 840*m.b13*m.b19 + 896*m.b13*m.b20
                        + 840*m.b13*m.b21 + 784*m.b13*m.b22 + 648*m.b13*m.b23 + 528*m.b13*m.b24 + 264*m.b13*m.b25 + 832*
                       m.b14*m.b15 + 792*m.b14*m.b16 + 848*m.b14*m.b17 + 856*m.b14*m.b18 + 928*m.b14*m.b19 + 840*m.b14*
                       m.b20 + 832*m.b14*m.b21 + 744*m.b14*m.b22 + 640*m.b14*m.b23 + 472*m.b14*m.b24 + 272*m.b14*m.b25
                        + 800*m.b15*m.b16 + 792*m.b15*m.b17 + 864*m.b15*m.b18 + 888*m.b15*m.b19 + 912*m.b15*m.b20 + 808*
                       m.b15*m.b21 + 752*m.b15*m.b22 + 632*m.b15*m.b23 + 480*m.b15*m.b24 + 280*m.b15*m.b25 + 800*m.b16*
                       m.b17 + 824*m.b16*m.b18 + 896*m.b16*m.b19 + 888*m.b16*m.b20 + 880*m.b16*m.b21 + 744*m.b16*m.b22
                        + 640*m.b16*m.b23 + 488*m.b16*m.b24 + 288*m.b16*m.b25 + 832*m.b17*m.b18 + 872*m.b17*m.b19 + 896*
                       m.b17*m.b20 + 856*m.b17*m.b21 + 800*m.b17*m.b22 + 648*m.b17*m.b23 + 496*m.b17*m.b24 + 296*m.b17*
                       m.b25 + 880*m.b18*m.b19 + 888*m.b18*m.b20 + 864*m.b18*m.b21 + 808*m.b18*m.b22 + 688*m.b18*m.b23
                        + 504*m.b18*m.b24 + 304*m.b18*m.b25 + 896*m.b19*m.b20 + 872*m.b19*m.b21 + 800*m.b19*m.b22 + 696*
                       m.b19*m.b23 + 528*m.b19*m.b24 + 312*m.b19*m.b25 + 880*m.b20*m.b21 + 808*m.b20*m.b22 + 704*m.b20*
                       m.b23 + 536*m.b20*m.b24 + 320*m.b20*m.b25 + 816*m.b21*m.b22 + 696*m.b21*m.b23 + 544*m.b21*m.b24
                        + 328*m.b21*m.b25 + 704*m.b22*m.b23 + 552*m.b22*m.b24 + 336*m.b22*m.b25 + 544*m.b23*m.b24 + 344*
                       m.b23*m.b25 + 352*m.b24*m.b25 - 1104*m.b1 - 1908*m.b2 - 2560*m.b3 - 3060*m.b4 - 3416*m.b5 - 3628*
                       m.b6 - 3704*m.b7 - 3636*m.b8 - 3528*m.b9 - 3412*m.b10 - 3296*m.b11 - 3180*m.b12 - 3104*m.b13 - 
                       3180*m.b14 - 3296*m.b15 - 3412*m.b16 - 3528*m.b17 - 3636*m.b18 - 3704*m.b19 - 3628*m.b20 - 3416*
                       m.b21 - 3060*m.b22 - 2560*m.b23 - 1908*m.b24 - 1104*m.b25 - m.x26 <= 0)
