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
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b2*m.b15*m.b16 + 64*m.b1*m.b2*m.b16*m.b17 + 64*m.b1*m.b2*m.b17*
                       m.b18 + 64*m.b1*m.b2*m.b18*m.b19 + 64*m.b1*m.b2*m.b19*m.b20 + 64*m.b1*m.b2*m.b20*m.b21 + 64*m.b1*
                       m.b2*m.b21*m.b22 + 64*m.b1*m.b2*m.b22*m.b23 + 64*m.b1*m.b2*m.b23*m.b24 + 64*m.b1*m.b2*m.b24*m.b25
                        + 64*m.b1*m.b2*m.b25*m.b26 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6
                       *m.b8 + 64*m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3
                       *m.b10*m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b3*m.b13*m.b15 + 
                       64*m.b1*m.b3*m.b14*m.b16 + 64*m.b1*m.b3*m.b15*m.b17 + 64*m.b1*m.b3*m.b16*m.b18 + 64*m.b1*m.b3*
                       m.b17*m.b19 + 64*m.b1*m.b3*m.b18*m.b20 + 64*m.b1*m.b3*m.b19*m.b21 + 64*m.b1*m.b3*m.b20*m.b22 + 64
                       *m.b1*m.b3*m.b21*m.b23 + 64*m.b1*m.b3*m.b22*m.b24 + 64*m.b1*m.b3*m.b23*m.b25 + 64*m.b1*m.b3*m.b24
                       *m.b26 + 64*m.b1*m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4
                       *m.b8*m.b11 + 64*m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b4*m.b11*m.b14 + 64*
                       m.b1*m.b4*m.b12*m.b15 + 64*m.b1*m.b4*m.b13*m.b16 + 64*m.b1*m.b4*m.b14*m.b17 + 64*m.b1*m.b4*m.b15*
                       m.b18 + 64*m.b1*m.b4*m.b16*m.b19 + 64*m.b1*m.b4*m.b17*m.b20 + 64*m.b1*m.b4*m.b18*m.b21 + 64*m.b1*
                       m.b4*m.b19*m.b22 + 64*m.b1*m.b4*m.b20*m.b23 + 64*m.b1*m.b4*m.b21*m.b24 + 64*m.b1*m.b4*m.b22*m.b25
                        + 64*m.b1*m.b4*m.b23*m.b26 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*m.b1*m.b5*
                       m.b8*m.b12 + 64*m.b1*m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 64*m.b1*m.b5*m.b11*m.b15 + 64*
                       m.b1*m.b5*m.b12*m.b16 + 64*m.b1*m.b5*m.b13*m.b17 + 64*m.b1*m.b5*m.b14*m.b18 + 64*m.b1*m.b5*m.b15*
                       m.b19 + 64*m.b1*m.b5*m.b16*m.b20 + 64*m.b1*m.b5*m.b17*m.b21 + 64*m.b1*m.b5*m.b18*m.b22 + 64*m.b1*
                       m.b5*m.b19*m.b23 + 64*m.b1*m.b5*m.b20*m.b24 + 64*m.b1*m.b5*m.b21*m.b25 + 64*m.b1*m.b5*m.b22*m.b26
                        + 64*m.b1*m.b6*m.b7*m.b12 + 64*m.b1*m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b6*
                       m.b10*m.b15 + 64*m.b1*m.b6*m.b11*m.b16 + 64*m.b1*m.b6*m.b12*m.b17 + 64*m.b1*m.b6*m.b13*m.b18 + 64
                       *m.b1*m.b6*m.b14*m.b19 + 64*m.b1*m.b6*m.b15*m.b20 + 64*m.b1*m.b6*m.b16*m.b21 + 64*m.b1*m.b6*m.b17
                       *m.b22 + 64*m.b1*m.b6*m.b18*m.b23 + 64*m.b1*m.b6*m.b19*m.b24 + 64*m.b1*m.b6*m.b20*m.b25 + 64*m.b1
                       *m.b6*m.b21*m.b26 + 64*m.b1*m.b7*m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 64*m.b1*m.b7*m.b10*m.b16
                        + 64*m.b1*m.b7*m.b11*m.b17 + 64*m.b1*m.b7*m.b12*m.b18 + 64*m.b1*m.b7*m.b13*m.b19 + 64*m.b1*m.b7*
                       m.b14*m.b20 + 64*m.b1*m.b7*m.b15*m.b21 + 64*m.b1*m.b7*m.b16*m.b22 + 64*m.b1*m.b7*m.b17*m.b23 + 64
                       *m.b1*m.b7*m.b18*m.b24 + 64*m.b1*m.b7*m.b19*m.b25 + 64*m.b1*m.b7*m.b20*m.b26 + 64*m.b1*m.b8*m.b9*
                       m.b16 + 64*m.b1*m.b8*m.b10*m.b17 + 64*m.b1*m.b8*m.b11*m.b18 + 64*m.b1*m.b8*m.b12*m.b19 + 64*m.b1*
                       m.b8*m.b13*m.b20 + 64*m.b1*m.b8*m.b14*m.b21 + 64*m.b1*m.b8*m.b15*m.b22 + 64*m.b1*m.b8*m.b16*m.b23
                        + 64*m.b1*m.b8*m.b17*m.b24 + 64*m.b1*m.b8*m.b18*m.b25 + 64*m.b1*m.b8*m.b19*m.b26 + 64*m.b1*m.b9*
                       m.b10*m.b18 + 64*m.b1*m.b9*m.b11*m.b19 + 64*m.b1*m.b9*m.b12*m.b20 + 64*m.b1*m.b9*m.b13*m.b21 + 64
                       *m.b1*m.b9*m.b14*m.b22 + 64*m.b1*m.b9*m.b15*m.b23 + 64*m.b1*m.b9*m.b16*m.b24 + 64*m.b1*m.b9*m.b17
                       *m.b25 + 64*m.b1*m.b9*m.b18*m.b26 + 64*m.b1*m.b10*m.b11*m.b20 + 64*m.b1*m.b10*m.b12*m.b21 + 64*
                       m.b1*m.b10*m.b13*m.b22 + 64*m.b1*m.b10*m.b14*m.b23 + 64*m.b1*m.b10*m.b15*m.b24 + 64*m.b1*m.b10*
                       m.b16*m.b25 + 64*m.b1*m.b10*m.b17*m.b26 + 64*m.b1*m.b11*m.b12*m.b22 + 64*m.b1*m.b11*m.b13*m.b23
                        + 64*m.b1*m.b11*m.b14*m.b24 + 64*m.b1*m.b11*m.b15*m.b25 + 64*m.b1*m.b11*m.b16*m.b26 + 64*m.b1*
                       m.b12*m.b13*m.b24 + 64*m.b1*m.b12*m.b14*m.b25 + 64*m.b1*m.b12*m.b15*m.b26 + 64*m.b1*m.b13*m.b14*
                       m.b26 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*m.b2*m.b3*m.b6*m.b7 + 128*m.b2*
                       m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*m.b10 + 128*m.b2*m.b3*m.b10*m.b11
                        + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*m.b12*m.b13 + 128*m.b2*m.b3*m.b13*m.b14 + 128*m.b2*
                       m.b3*m.b14*m.b15 + 128*m.b2*m.b3*m.b15*m.b16 + 128*m.b2*m.b3*m.b16*m.b17 + 128*m.b2*m.b3*m.b17*
                       m.b18 + 128*m.b2*m.b3*m.b18*m.b19 + 128*m.b2*m.b3*m.b19*m.b20 + 128*m.b2*m.b3*m.b20*m.b21 + 128*
                       m.b2*m.b3*m.b21*m.b22 + 128*m.b2*m.b3*m.b22*m.b23 + 128*m.b2*m.b3*m.b23*m.b24 + 128*m.b2*m.b3*
                       m.b24*m.b25 + 128*m.b2*m.b3*m.b25*m.b26 + 64*m.b2*m.b3*m.b26*m.b27 + 128*m.b2*m.b4*m.b5*m.b7 + 
                       128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*m.b4*m.b9
                       *m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*m.b14 + 128*
                       m.b2*m.b4*m.b13*m.b15 + 128*m.b2*m.b4*m.b14*m.b16 + 128*m.b2*m.b4*m.b15*m.b17 + 128*m.b2*m.b4*
                       m.b16*m.b18 + 128*m.b2*m.b4*m.b17*m.b19 + 128*m.b2*m.b4*m.b18*m.b20 + 128*m.b2*m.b4*m.b19*m.b21
                        + 128*m.b2*m.b4*m.b20*m.b22 + 128*m.b2*m.b4*m.b21*m.b23 + 128*m.b2*m.b4*m.b22*m.b24 + 128*m.b2*
                       m.b4*m.b23*m.b25 + 128*m.b2*m.b4*m.b24*m.b26 + 64*m.b2*m.b4*m.b25*m.b27 + 128*m.b2*m.b5*m.b6*m.b9
                        + 128*m.b2*m.b5*m.b7*m.b10 + 128*m.b2*m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5
                       *m.b10*m.b13 + 128*m.b2*m.b5*m.b11*m.b14 + 128*m.b2*m.b5*m.b12*m.b15 + 128*m.b2*m.b5*m.b13*m.b16
                        + 128*m.b2*m.b5*m.b14*m.b17 + 128*m.b2*m.b5*m.b15*m.b18 + 128*m.b2*m.b5*m.b16*m.b19 + 128*m.b2*
                       m.b5*m.b17*m.b20 + 128*m.b2*m.b5*m.b18*m.b21 + 128*m.b2*m.b5*m.b19*m.b22 + 128*m.b2*m.b5*m.b20*
                       m.b23 + 128*m.b2*m.b5*m.b21*m.b24 + 128*m.b2*m.b5*m.b22*m.b25 + 128*m.b2*m.b5*m.b23*m.b26 + 64*
                       m.b2*m.b5*m.b24*m.b27 + 128*m.b2*m.b6*m.b7*m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*
                       m.b13 + 128*m.b2*m.b6*m.b10*m.b14 + 128*m.b2*m.b6*m.b11*m.b15 + 128*m.b2*m.b6*m.b12*m.b16 + 128*
                       m.b2*m.b6*m.b13*m.b17 + 128*m.b2*m.b6*m.b14*m.b18 + 128*m.b2*m.b6*m.b15*m.b19 + 128*m.b2*m.b6*
                       m.b16*m.b20 + 128*m.b2*m.b6*m.b17*m.b21 + 128*m.b2*m.b6*m.b18*m.b22 + 128*m.b2*m.b6*m.b19*m.b23
                        + 128*m.b2*m.b6*m.b20*m.b24 + 128*m.b2*m.b6*m.b21*m.b25 + 128*m.b2*m.b6*m.b22*m.b26 + 64*m.b2*
                       m.b6*m.b23*m.b27 + 128*m.b2*m.b7*m.b8*m.b13 + 128*m.b2*m.b7*m.b9*m.b14 + 128*m.b2*m.b7*m.b10*
                       m.b15 + 128*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b7*m.b12*m.b17 + 128*m.b2*m.b7*m.b13*m.b18 + 128*
                       m.b2*m.b7*m.b14*m.b19 + 128*m.b2*m.b7*m.b15*m.b20 + 128*m.b2*m.b7*m.b16*m.b21 + 128*m.b2*m.b7*
                       m.b17*m.b22 + 128*m.b2*m.b7*m.b18*m.b23 + 128*m.b2*m.b7*m.b19*m.b24 + 128*m.b2*m.b7*m.b20*m.b25
                        + 128*m.b2*m.b7*m.b21*m.b26 + 64*m.b2*m.b7*m.b22*m.b27 + 128*m.b2*m.b8*m.b9*m.b15 + 128*m.b2*
                       m.b8*m.b10*m.b16 + 128*m.b2*m.b8*m.b11*m.b17 + 128*m.b2*m.b8*m.b12*m.b18 + 128*m.b2*m.b8*m.b13*
                       m.b19 + 128*m.b2*m.b8*m.b14*m.b20 + 128*m.b2*m.b8*m.b15*m.b21 + 128*m.b2*m.b8*m.b16*m.b22 + 128*
                       m.b2*m.b8*m.b17*m.b23 + 128*m.b2*m.b8*m.b18*m.b24 + 128*m.b2*m.b8*m.b19*m.b25 + 128*m.b2*m.b8*
                       m.b20*m.b26 + 64*m.b2*m.b8*m.b21*m.b27 + 128*m.b2*m.b9*m.b10*m.b17 + 128*m.b2*m.b9*m.b11*m.b18 + 
                       128*m.b2*m.b9*m.b12*m.b19 + 128*m.b2*m.b9*m.b13*m.b20 + 128*m.b2*m.b9*m.b14*m.b21 + 128*m.b2*m.b9
                       *m.b15*m.b22 + 128*m.b2*m.b9*m.b16*m.b23 + 128*m.b2*m.b9*m.b17*m.b24 + 128*m.b2*m.b9*m.b18*m.b25
                        + 128*m.b2*m.b9*m.b19*m.b26 + 64*m.b2*m.b9*m.b20*m.b27 + 128*m.b2*m.b10*m.b11*m.b19 + 128*m.b2*
                       m.b10*m.b12*m.b20 + 128*m.b2*m.b10*m.b13*m.b21 + 128*m.b2*m.b10*m.b14*m.b22 + 128*m.b2*m.b10*
                       m.b15*m.b23 + 128*m.b2*m.b10*m.b16*m.b24 + 128*m.b2*m.b10*m.b17*m.b25 + 128*m.b2*m.b10*m.b18*
                       m.b26 + 64*m.b2*m.b10*m.b19*m.b27 + 128*m.b2*m.b11*m.b12*m.b21 + 128*m.b2*m.b11*m.b13*m.b22 + 128
                       *m.b2*m.b11*m.b14*m.b23 + 128*m.b2*m.b11*m.b15*m.b24 + 128*m.b2*m.b11*m.b16*m.b25 + 128*m.b2*
                       m.b11*m.b17*m.b26 + 64*m.b2*m.b11*m.b18*m.b27 + 128*m.b2*m.b12*m.b13*m.b23 + 128*m.b2*m.b12*m.b14
                       *m.b24 + 128*m.b2*m.b12*m.b15*m.b25 + 128*m.b2*m.b12*m.b16*m.b26 + 64*m.b2*m.b12*m.b17*m.b27 + 
                       128*m.b2*m.b13*m.b14*m.b25 + 128*m.b2*m.b13*m.b15*m.b26 + 64*m.b2*m.b13*m.b16*m.b27 + 64*m.b2*
                       m.b14*m.b15*m.b27 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*m.b4*m.b7*m.b8
                        + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*m.b4*m.b10*m.b11 + 192*m.b3*m.b4
                       *m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 192*m.b3*m.b4*m.b13*m.b14 + 192*m.b3*m.b4*m.b14*m.b15
                        + 192*m.b3*m.b4*m.b15*m.b16 + 192*m.b3*m.b4*m.b16*m.b17 + 192*m.b3*m.b4*m.b17*m.b18 + 192*m.b3*
                       m.b4*m.b18*m.b19 + 192*m.b3*m.b4*m.b19*m.b20 + 192*m.b3*m.b4*m.b20*m.b21 + 192*m.b3*m.b4*m.b21*
                       m.b22 + 192*m.b3*m.b4*m.b22*m.b23 + 192*m.b3*m.b4*m.b23*m.b24 + 192*m.b3*m.b4*m.b24*m.b25 + 192*
                       m.b3*m.b4*m.b25*m.b26 + 128*m.b3*m.b4*m.b26*m.b27 + 64*m.b3*m.b4*m.b27*m.b28 + 192*m.b3*m.b5*m.b6
                       *m.b8 + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*
                       m.b5*m.b10*m.b12 + 192*m.b3*m.b5*m.b11*m.b13 + 192*m.b3*m.b5*m.b12*m.b14 + 192*m.b3*m.b5*m.b13*
                       m.b15 + 192*m.b3*m.b5*m.b14*m.b16 + 192*m.b3*m.b5*m.b15*m.b17 + 192*m.b3*m.b5*m.b16*m.b18 + 192*
                       m.b3*m.b5*m.b17*m.b19 + 192*m.b3*m.b5*m.b18*m.b20 + 192*m.b3*m.b5*m.b19*m.b21 + 192*m.b3*m.b5*
                       m.b20*m.b22 + 192*m.b3*m.b5*m.b21*m.b23 + 192*m.b3*m.b5*m.b22*m.b24 + 192*m.b3*m.b5*m.b23*m.b25
                        + 192*m.b3*m.b5*m.b24*m.b26 + 128*m.b3*m.b5*m.b25*m.b27 + 64*m.b3*m.b5*m.b26*m.b28 + 192*m.b3*
                       m.b6*m.b7*m.b10 + 192*m.b3*m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13
                        + 192*m.b3*m.b6*m.b11*m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 192*m.b3*m.b6*m.b13*m.b16 + 192*m.b3*
                       m.b6*m.b14*m.b17 + 192*m.b3*m.b6*m.b15*m.b18 + 192*m.b3*m.b6*m.b16*m.b19 + 192*m.b3*m.b6*m.b17*
                       m.b20 + 192*m.b3*m.b6*m.b18*m.b21 + 192*m.b3*m.b6*m.b19*m.b22 + 192*m.b3*m.b6*m.b20*m.b23 + 192*
                       m.b3*m.b6*m.b21*m.b24 + 192*m.b3*m.b6*m.b22*m.b25 + 192*m.b3*m.b6*m.b23*m.b26 + 128*m.b3*m.b6*
                       m.b24*m.b27 + 64*m.b3*m.b6*m.b25*m.b28 + 192*m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*m.b13 + 
                       192*m.b3*m.b7*m.b10*m.b14 + 192*m.b3*m.b7*m.b11*m.b15 + 192*m.b3*m.b7*m.b12*m.b16 + 192*m.b3*m.b7
                       *m.b13*m.b17 + 192*m.b3*m.b7*m.b14*m.b18 + 192*m.b3*m.b7*m.b15*m.b19 + 192*m.b3*m.b7*m.b16*m.b20
                        + 192*m.b3*m.b7*m.b17*m.b21 + 192*m.b3*m.b7*m.b18*m.b22 + 192*m.b3*m.b7*m.b19*m.b23 + 192*m.b3*
                       m.b7*m.b20*m.b24 + 192*m.b3*m.b7*m.b21*m.b25 + 192*m.b3*m.b7*m.b22*m.b26 + 128*m.b3*m.b7*m.b23*
                       m.b27 + 64*m.b3*m.b7*m.b24*m.b28 + 192*m.b3*m.b8*m.b9*m.b14 + 192*m.b3*m.b8*m.b10*m.b15 + 192*
                       m.b3*m.b8*m.b11*m.b16 + 192*m.b3*m.b8*m.b12*m.b17 + 192*m.b3*m.b8*m.b13*m.b18 + 192*m.b3*m.b8*
                       m.b14*m.b19 + 192*m.b3*m.b8*m.b15*m.b20 + 192*m.b3*m.b8*m.b16*m.b21 + 192*m.b3*m.b8*m.b17*m.b22
                        + 192*m.b3*m.b8*m.b18*m.b23 + 192*m.b3*m.b8*m.b19*m.b24 + 192*m.b3*m.b8*m.b20*m.b25 + 192*m.b3*
                       m.b8*m.b21*m.b26 + 128*m.b3*m.b8*m.b22*m.b27 + 64*m.b3*m.b8*m.b23*m.b28 + 192*m.b3*m.b9*m.b10*
                       m.b16 + 192*m.b3*m.b9*m.b11*m.b17 + 192*m.b3*m.b9*m.b12*m.b18 + 192*m.b3*m.b9*m.b13*m.b19 + 192*
                       m.b3*m.b9*m.b14*m.b20 + 192*m.b3*m.b9*m.b15*m.b21 + 192*m.b3*m.b9*m.b16*m.b22 + 192*m.b3*m.b9*
                       m.b17*m.b23 + 192*m.b3*m.b9*m.b18*m.b24 + 192*m.b3*m.b9*m.b19*m.b25 + 192*m.b3*m.b9*m.b20*m.b26
                        + 128*m.b3*m.b9*m.b21*m.b27 + 64*m.b3*m.b9*m.b22*m.b28 + 192*m.b3*m.b10*m.b11*m.b18 + 192*m.b3*
                       m.b10*m.b12*m.b19 + 192*m.b3*m.b10*m.b13*m.b20 + 192*m.b3*m.b10*m.b14*m.b21 + 192*m.b3*m.b10*
                       m.b15*m.b22 + 192*m.b3*m.b10*m.b16*m.b23 + 192*m.b3*m.b10*m.b17*m.b24 + 192*m.b3*m.b10*m.b18*
                       m.b25 + 192*m.b3*m.b10*m.b19*m.b26 + 128*m.b3*m.b10*m.b20*m.b27 + 64*m.b3*m.b10*m.b21*m.b28 + 192
                       *m.b3*m.b11*m.b12*m.b20 + 192*m.b3*m.b11*m.b13*m.b21 + 192*m.b3*m.b11*m.b14*m.b22 + 192*m.b3*
                       m.b11*m.b15*m.b23 + 192*m.b3*m.b11*m.b16*m.b24 + 192*m.b3*m.b11*m.b17*m.b25 + 192*m.b3*m.b11*
                       m.b18*m.b26 + 128*m.b3*m.b11*m.b19*m.b27 + 64*m.b3*m.b11*m.b20*m.b28 + 192*m.b3*m.b12*m.b13*m.b22
                        + 192*m.b3*m.b12*m.b14*m.b23 + 192*m.b3*m.b12*m.b15*m.b24 + 192*m.b3*m.b12*m.b16*m.b25 + 192*
                       m.b3*m.b12*m.b17*m.b26 + 128*m.b3*m.b12*m.b18*m.b27 + 64*m.b3*m.b12*m.b19*m.b28 + 192*m.b3*m.b13*
                       m.b14*m.b24 + 192*m.b3*m.b13*m.b15*m.b25 + 192*m.b3*m.b13*m.b16*m.b26 + 128*m.b3*m.b13*m.b17*
                       m.b27 + 64*m.b3*m.b13*m.b18*m.b28 + 192*m.b3*m.b14*m.b15*m.b26 + 128*m.b3*m.b14*m.b16*m.b27 + 64*
                       m.b3*m.b14*m.b17*m.b28 + 64*m.b3*m.b15*m.b16*m.b28 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7
                       *m.b8 + 256*m.b4*m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4
                       *m.b5*m.b11*m.b12 + 256*m.b4*m.b5*m.b12*m.b13 + 256*m.b4*m.b5*m.b13*m.b14 + 256*m.b4*m.b5*m.b14*
                       m.b15 + 256*m.b4*m.b5*m.b15*m.b16 + 256*m.b4*m.b5*m.b16*m.b17 + 256*m.b4*m.b5*m.b17*m.b18 + 256*
                       m.b4*m.b5*m.b18*m.b19 + 256*m.b4*m.b5*m.b19*m.b20 + 256*m.b4*m.b5*m.b20*m.b21 + 256*m.b4*m.b5*
                       m.b21*m.b22 + 256*m.b4*m.b5*m.b22*m.b23 + 256*m.b4*m.b5*m.b23*m.b24 + 256*m.b4*m.b5*m.b24*m.b25
                        + 256*m.b4*m.b5*m.b25*m.b26 + 192*m.b4*m.b5*m.b26*m.b27 + 128*m.b4*m.b5*m.b27*m.b28 + 64*m.b4*
                       m.b5*m.b28*m.b29 + 256*m.b4*m.b6*m.b7*m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11
                        + 256*m.b4*m.b6*m.b10*m.b12 + 256*m.b4*m.b6*m.b11*m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*
                       m.b6*m.b13*m.b15 + 256*m.b4*m.b6*m.b14*m.b16 + 256*m.b4*m.b6*m.b15*m.b17 + 256*m.b4*m.b6*m.b16*
                       m.b18 + 256*m.b4*m.b6*m.b17*m.b19 + 256*m.b4*m.b6*m.b18*m.b20 + 256*m.b4*m.b6*m.b19*m.b21 + 256*
                       m.b4*m.b6*m.b20*m.b22 + 256*m.b4*m.b6*m.b21*m.b23 + 256*m.b4*m.b6*m.b22*m.b24 + 256*m.b4*m.b6*
                       m.b23*m.b25 + 256*m.b4*m.b6*m.b24*m.b26 + 192*m.b4*m.b6*m.b25*m.b27 + 128*m.b4*m.b6*m.b26*m.b28
                        + 64*m.b4*m.b6*m.b27*m.b29 + 256*m.b4*m.b7*m.b8*m.b11 + 256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7
                       *m.b10*m.b13 + 256*m.b4*m.b7*m.b11*m.b14 + 256*m.b4*m.b7*m.b12*m.b15 + 256*m.b4*m.b7*m.b13*m.b16
                        + 256*m.b4*m.b7*m.b14*m.b17 + 256*m.b4*m.b7*m.b15*m.b18 + 256*m.b4*m.b7*m.b16*m.b19 + 256*m.b4*
                       m.b7*m.b17*m.b20 + 256*m.b4*m.b7*m.b18*m.b21 + 256*m.b4*m.b7*m.b19*m.b22 + 256*m.b4*m.b7*m.b20*
                       m.b23 + 256*m.b4*m.b7*m.b21*m.b24 + 256*m.b4*m.b7*m.b22*m.b25 + 256*m.b4*m.b7*m.b23*m.b26 + 192*
                       m.b4*m.b7*m.b24*m.b27 + 128*m.b4*m.b7*m.b25*m.b28 + 64*m.b4*m.b7*m.b26*m.b29 + 256*m.b4*m.b8*m.b9
                       *m.b13 + 256*m.b4*m.b8*m.b10*m.b14 + 256*m.b4*m.b8*m.b11*m.b15 + 256*m.b4*m.b8*m.b12*m.b16 + 256*
                       m.b4*m.b8*m.b13*m.b17 + 256*m.b4*m.b8*m.b14*m.b18 + 256*m.b4*m.b8*m.b15*m.b19 + 256*m.b4*m.b8*
                       m.b16*m.b20 + 256*m.b4*m.b8*m.b17*m.b21 + 256*m.b4*m.b8*m.b18*m.b22 + 256*m.b4*m.b8*m.b19*m.b23
                        + 256*m.b4*m.b8*m.b20*m.b24 + 256*m.b4*m.b8*m.b21*m.b25 + 256*m.b4*m.b8*m.b22*m.b26 + 192*m.b4*
                       m.b8*m.b23*m.b27 + 128*m.b4*m.b8*m.b24*m.b28 + 64*m.b4*m.b8*m.b25*m.b29 + 256*m.b4*m.b9*m.b10*
                       m.b15 + 256*m.b4*m.b9*m.b11*m.b16 + 256*m.b4*m.b9*m.b12*m.b17 + 256*m.b4*m.b9*m.b13*m.b18 + 256*
                       m.b4*m.b9*m.b14*m.b19 + 256*m.b4*m.b9*m.b15*m.b20 + 256*m.b4*m.b9*m.b16*m.b21 + 256*m.b4*m.b9*
                       m.b17*m.b22 + 256*m.b4*m.b9*m.b18*m.b23 + 256*m.b4*m.b9*m.b19*m.b24 + 256*m.b4*m.b9*m.b20*m.b25
                        + 256*m.b4*m.b9*m.b21*m.b26 + 192*m.b4*m.b9*m.b22*m.b27 + 128*m.b4*m.b9*m.b23*m.b28 + 64*m.b4*
                       m.b9*m.b24*m.b29 + 256*m.b4*m.b10*m.b11*m.b17 + 256*m.b4*m.b10*m.b12*m.b18 + 256*m.b4*m.b10*m.b13
                       *m.b19 + 256*m.b4*m.b10*m.b14*m.b20 + 256*m.b4*m.b10*m.b15*m.b21 + 256*m.b4*m.b10*m.b16*m.b22 + 
                       256*m.b4*m.b10*m.b17*m.b23 + 256*m.b4*m.b10*m.b18*m.b24 + 256*m.b4*m.b10*m.b19*m.b25 + 256*m.b4*
                       m.b10*m.b20*m.b26 + 192*m.b4*m.b10*m.b21*m.b27 + 128*m.b4*m.b10*m.b22*m.b28 + 64*m.b4*m.b10*m.b23
                       *m.b29 + 256*m.b4*m.b11*m.b12*m.b19 + 256*m.b4*m.b11*m.b13*m.b20 + 256*m.b4*m.b11*m.b14*m.b21 + 
                       256*m.b4*m.b11*m.b15*m.b22 + 256*m.b4*m.b11*m.b16*m.b23 + 256*m.b4*m.b11*m.b17*m.b24 + 256*m.b4*
                       m.b11*m.b18*m.b25 + 256*m.b4*m.b11*m.b19*m.b26 + 192*m.b4*m.b11*m.b20*m.b27 + 128*m.b4*m.b11*
                       m.b21*m.b28 + 64*m.b4*m.b11*m.b22*m.b29 + 256*m.b4*m.b12*m.b13*m.b21 + 256*m.b4*m.b12*m.b14*m.b22
                        + 256*m.b4*m.b12*m.b15*m.b23 + 256*m.b4*m.b12*m.b16*m.b24 + 256*m.b4*m.b12*m.b17*m.b25 + 256*
                       m.b4*m.b12*m.b18*m.b26 + 192*m.b4*m.b12*m.b19*m.b27 + 128*m.b4*m.b12*m.b20*m.b28 + 64*m.b4*m.b12*
                       m.b21*m.b29 + 256*m.b4*m.b13*m.b14*m.b23 + 256*m.b4*m.b13*m.b15*m.b24 + 256*m.b4*m.b13*m.b16*
                       m.b25 + 256*m.b4*m.b13*m.b17*m.b26 + 192*m.b4*m.b13*m.b18*m.b27 + 128*m.b4*m.b13*m.b19*m.b28 + 64
                       *m.b4*m.b13*m.b20*m.b29 + 256*m.b4*m.b14*m.b15*m.b25 + 256*m.b4*m.b14*m.b16*m.b26 + 192*m.b4*
                       m.b14*m.b17*m.b27 + 128*m.b4*m.b14*m.b18*m.b28 + 64*m.b4*m.b14*m.b19*m.b29 + 192*m.b4*m.b15*m.b16
                       *m.b27 + 128*m.b4*m.b15*m.b17*m.b28 + 64*m.b4*m.b15*m.b18*m.b29 + 64*m.b4*m.b16*m.b17*m.b29 + 320
                       *m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*
                       m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*m.b5*m.b6*m.b12*m.b13 + 320*m.b5*m.b6*m.b13*m.b14 + 320*
                       m.b5*m.b6*m.b14*m.b15 + 320*m.b5*m.b6*m.b15*m.b16 + 320*m.b5*m.b6*m.b16*m.b17 + 320*m.b5*m.b6*
                       m.b17*m.b18 + 320*m.b5*m.b6*m.b18*m.b19 + 320*m.b5*m.b6*m.b19*m.b20 + 320*m.b5*m.b6*m.b20*m.b21
                        + 320*m.b5*m.b6*m.b21*m.b22 + 320*m.b5*m.b6*m.b22*m.b23 + 320*m.b5*m.b6*m.b23*m.b24 + 320*m.b5*
                       m.b6*m.b24*m.b25 + 320*m.b5*m.b6*m.b25*m.b26 + 256*m.b5*m.b6*m.b26*m.b27 + 192*m.b5*m.b6*m.b27*
                       m.b28 + 128*m.b5*m.b6*m.b28*m.b29 + 64*m.b5*m.b6*m.b29*m.b30 + 320*m.b5*m.b7*m.b8*m.b10 + 320*
                       m.b5*m.b7*m.b9*m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*m.b13 + 320*m.b5*m.b7*
                       m.b12*m.b14 + 320*m.b5*m.b7*m.b13*m.b15 + 320*m.b5*m.b7*m.b14*m.b16 + 320*m.b5*m.b7*m.b15*m.b17
                        + 320*m.b5*m.b7*m.b16*m.b18 + 320*m.b5*m.b7*m.b17*m.b19 + 320*m.b5*m.b7*m.b18*m.b20 + 320*m.b5*
                       m.b7*m.b19*m.b21 + 320*m.b5*m.b7*m.b20*m.b22 + 320*m.b5*m.b7*m.b21*m.b23 + 320*m.b5*m.b7*m.b22*
                       m.b24 + 320*m.b5*m.b7*m.b23*m.b25 + 320*m.b5*m.b7*m.b24*m.b26 + 256*m.b5*m.b7*m.b25*m.b27 + 192*
                       m.b5*m.b7*m.b26*m.b28 + 128*m.b5*m.b7*m.b27*m.b29 + 64*m.b5*m.b7*m.b28*m.b30 + 320*m.b5*m.b8*m.b9
                       *m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*m.b5*m.b8*m.b11*m.b14 + 320*m.b5*m.b8*m.b12*m.b15 + 320*
                       m.b5*m.b8*m.b13*m.b16 + 320*m.b5*m.b8*m.b14*m.b17 + 320*m.b5*m.b8*m.b15*m.b18 + 320*m.b5*m.b8*
                       m.b16*m.b19 + 320*m.b5*m.b8*m.b17*m.b20 + 320*m.b5*m.b8*m.b18*m.b21 + 320*m.b5*m.b8*m.b19*m.b22
                        + 320*m.b5*m.b8*m.b20*m.b23 + 320*m.b5*m.b8*m.b21*m.b24 + 320*m.b5*m.b8*m.b22*m.b25 + 320*m.b5*
                       m.b8*m.b23*m.b26 + 256*m.b5*m.b8*m.b24*m.b27 + 192*m.b5*m.b8*m.b25*m.b28 + 128*m.b5*m.b8*m.b26*
                       m.b29 + 64*m.b5*m.b8*m.b27*m.b30 + 320*m.b5*m.b9*m.b10*m.b14 + 320*m.b5*m.b9*m.b11*m.b15 + 320*
                       m.b5*m.b9*m.b12*m.b16 + 320*m.b5*m.b9*m.b13*m.b17 + 320*m.b5*m.b9*m.b14*m.b18 + 320*m.b5*m.b9*
                       m.b15*m.b19 + 320*m.b5*m.b9*m.b16*m.b20 + 320*m.b5*m.b9*m.b17*m.b21 + 320*m.b5*m.b9*m.b18*m.b22
                        + 320*m.b5*m.b9*m.b19*m.b23 + 320*m.b5*m.b9*m.b20*m.b24 + 320*m.b5*m.b9*m.b21*m.b25 + 320*m.b5*
                       m.b9*m.b22*m.b26 + 256*m.b5*m.b9*m.b23*m.b27 + 192*m.b5*m.b9*m.b24*m.b28 + 128*m.b5*m.b9*m.b25*
                       m.b29 + 64*m.b5*m.b9*m.b26*m.b30 + 320*m.b5*m.b10*m.b11*m.b16 + 320*m.b5*m.b10*m.b12*m.b17 + 320*
                       m.b5*m.b10*m.b13*m.b18 + 320*m.b5*m.b10*m.b14*m.b19 + 320*m.b5*m.b10*m.b15*m.b20 + 320*m.b5*m.b10
                       *m.b16*m.b21 + 320*m.b5*m.b10*m.b17*m.b22 + 320*m.b5*m.b10*m.b18*m.b23 + 320*m.b5*m.b10*m.b19*
                       m.b24 + 320*m.b5*m.b10*m.b20*m.b25 + 320*m.b5*m.b10*m.b21*m.b26 + 256*m.b5*m.b10*m.b22*m.b27 + 
                       192*m.b5*m.b10*m.b23*m.b28 + 128*m.b5*m.b10*m.b24*m.b29 + 64*m.b5*m.b10*m.b25*m.b30 + 320*m.b5*
                       m.b11*m.b12*m.b18 + 320*m.b5*m.b11*m.b13*m.b19 + 320*m.b5*m.b11*m.b14*m.b20 + 320*m.b5*m.b11*
                       m.b15*m.b21 + 320*m.b5*m.b11*m.b16*m.b22 + 320*m.b5*m.b11*m.b17*m.b23 + 320*m.b5*m.b11*m.b18*
                       m.b24 + 320*m.b5*m.b11*m.b19*m.b25 + 320*m.b5*m.b11*m.b20*m.b26 + 256*m.b5*m.b11*m.b21*m.b27 + 
                       192*m.b5*m.b11*m.b22*m.b28 + 128*m.b5*m.b11*m.b23*m.b29 + 64*m.b5*m.b11*m.b24*m.b30 + 320*m.b5*
                       m.b12*m.b13*m.b20 + 320*m.b5*m.b12*m.b14*m.b21 + 320*m.b5*m.b12*m.b15*m.b22 + 320*m.b5*m.b12*
                       m.b16*m.b23 + 320*m.b5*m.b12*m.b17*m.b24 + 320*m.b5*m.b12*m.b18*m.b25 + 320*m.b5*m.b12*m.b19*
                       m.b26 + 256*m.b5*m.b12*m.b20*m.b27 + 192*m.b5*m.b12*m.b21*m.b28 + 128*m.b5*m.b12*m.b22*m.b29 + 64
                       *m.b5*m.b12*m.b23*m.b30 + 320*m.b5*m.b13*m.b14*m.b22 + 320*m.b5*m.b13*m.b15*m.b23 + 320*m.b5*
                       m.b13*m.b16*m.b24 + 320*m.b5*m.b13*m.b17*m.b25 + 320*m.b5*m.b13*m.b18*m.b26 + 256*m.b5*m.b13*
                       m.b19*m.b27 + 192*m.b5*m.b13*m.b20*m.b28 + 128*m.b5*m.b13*m.b21*m.b29 + 64*m.b5*m.b13*m.b22*m.b30
                        + 320*m.b5*m.b14*m.b15*m.b24 + 320*m.b5*m.b14*m.b16*m.b25 + 320*m.b5*m.b14*m.b17*m.b26 + 256*
                       m.b5*m.b14*m.b18*m.b27 + 192*m.b5*m.b14*m.b19*m.b28 + 128*m.b5*m.b14*m.b20*m.b29 + 64*m.b5*m.b14*
                       m.b21*m.b30 + 320*m.b5*m.b15*m.b16*m.b26 + 256*m.b5*m.b15*m.b17*m.b27 + 192*m.b5*m.b15*m.b18*
                       m.b28 + 128*m.b5*m.b15*m.b19*m.b29 + 64*m.b5*m.b15*m.b20*m.b30 + 192*m.b5*m.b16*m.b17*m.b28 + 128
                       *m.b5*m.b16*m.b18*m.b29 + 64*m.b5*m.b16*m.b19*m.b30 + 64*m.b5*m.b17*m.b18*m.b30 + 384*m.b6*m.b7*
                       m.b8*m.b9 + 384*m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 
                       384*m.b6*m.b7*m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 384*m.b6*m.b7*m.b14*m.b15 + 384*m.b6*m.b7
                       *m.b15*m.b16 + 384*m.b6*m.b7*m.b16*m.b17 + 384*m.b6*m.b7*m.b17*m.b18 + 384*m.b6*m.b7*m.b18*m.b19
                        + 384*m.b6*m.b7*m.b19*m.b20 + 384*m.b6*m.b7*m.b20*m.b21 + 384*m.b6*m.b7*m.b21*m.b22 + 384*m.b6*
                       m.b7*m.b22*m.b23 + 384*m.b6*m.b7*m.b23*m.b24 + 384*m.b6*m.b7*m.b24*m.b25 + 384*m.b6*m.b7*m.b25*
                       m.b26 + 320*m.b6*m.b7*m.b26*m.b27 + 256*m.b6*m.b7*m.b27*m.b28 + 192*m.b6*m.b7*m.b28*m.b29 + 128*
                       m.b6*m.b7*m.b29*m.b30 + 64*m.b6*m.b7*m.b30*m.b31 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10
                       *m.b12 + 384*m.b6*m.b8*m.b11*m.b13 + 384*m.b6*m.b8*m.b12*m.b14 + 384*m.b6*m.b8*m.b13*m.b15 + 384*
                       m.b6*m.b8*m.b14*m.b16 + 384*m.b6*m.b8*m.b15*m.b17 + 384*m.b6*m.b8*m.b16*m.b18 + 384*m.b6*m.b8*
                       m.b17*m.b19 + 384*m.b6*m.b8*m.b18*m.b20 + 384*m.b6*m.b8*m.b19*m.b21 + 384*m.b6*m.b8*m.b20*m.b22
                        + 384*m.b6*m.b8*m.b21*m.b23 + 384*m.b6*m.b8*m.b22*m.b24 + 384*m.b6*m.b8*m.b23*m.b25 + 384*m.b6*
                       m.b8*m.b24*m.b26 + 320*m.b6*m.b8*m.b25*m.b27 + 256*m.b6*m.b8*m.b26*m.b28 + 192*m.b6*m.b8*m.b27*
                       m.b29 + 128*m.b6*m.b8*m.b28*m.b30 + 64*m.b6*m.b8*m.b29*m.b31 + 384*m.b6*m.b9*m.b10*m.b13 + 384*
                       m.b6*m.b9*m.b11*m.b14 + 384*m.b6*m.b9*m.b12*m.b15 + 384*m.b6*m.b9*m.b13*m.b16 + 384*m.b6*m.b9*
                       m.b14*m.b17 + 384*m.b6*m.b9*m.b15*m.b18 + 384*m.b6*m.b9*m.b16*m.b19 + 384*m.b6*m.b9*m.b17*m.b20
                        + 384*m.b6*m.b9*m.b18*m.b21 + 384*m.b6*m.b9*m.b19*m.b22 + 384*m.b6*m.b9*m.b20*m.b23 + 384*m.b6*
                       m.b9*m.b21*m.b24 + 384*m.b6*m.b9*m.b22*m.b25 + 384*m.b6*m.b9*m.b23*m.b26 + 320*m.b6*m.b9*m.b24*
                       m.b27 + 256*m.b6*m.b9*m.b25*m.b28 + 192*m.b6*m.b9*m.b26*m.b29 + 128*m.b6*m.b9*m.b27*m.b30 + 64*
                       m.b6*m.b9*m.b28*m.b31 + 384*m.b6*m.b10*m.b11*m.b15 + 384*m.b6*m.b10*m.b12*m.b16 + 384*m.b6*m.b10*
                       m.b13*m.b17 + 384*m.b6*m.b10*m.b14*m.b18 + 384*m.b6*m.b10*m.b15*m.b19 + 384*m.b6*m.b10*m.b16*
                       m.b20 + 384*m.b6*m.b10*m.b17*m.b21 + 384*m.b6*m.b10*m.b18*m.b22 + 384*m.b6*m.b10*m.b19*m.b23 + 
                       384*m.b6*m.b10*m.b20*m.b24 + 384*m.b6*m.b10*m.b21*m.b25 + 384*m.b6*m.b10*m.b22*m.b26 + 320*m.b6*
                       m.b10*m.b23*m.b27 + 256*m.b6*m.b10*m.b24*m.b28 + 192*m.b6*m.b10*m.b25*m.b29 + 128*m.b6*m.b10*
                       m.b26*m.b30 + 64*m.b6*m.b10*m.b27*m.b31 + 384*m.b6*m.b11*m.b12*m.b17 + 384*m.b6*m.b11*m.b13*m.b18
                        + 384*m.b6*m.b11*m.b14*m.b19 + 384*m.b6*m.b11*m.b15*m.b20 + 384*m.b6*m.b11*m.b16*m.b21 + 384*
                       m.b6*m.b11*m.b17*m.b22 + 384*m.b6*m.b11*m.b18*m.b23 + 384*m.b6*m.b11*m.b19*m.b24 + 384*m.b6*m.b11
                       *m.b20*m.b25 + 384*m.b6*m.b11*m.b21*m.b26 + 320*m.b6*m.b11*m.b22*m.b27 + 256*m.b6*m.b11*m.b23*
                       m.b28 + 192*m.b6*m.b11*m.b24*m.b29 + 128*m.b6*m.b11*m.b25*m.b30 + 64*m.b6*m.b11*m.b26*m.b31 + 384
                       *m.b6*m.b12*m.b13*m.b19 + 384*m.b6*m.b12*m.b14*m.b20 + 384*m.b6*m.b12*m.b15*m.b21 + 384*m.b6*
                       m.b12*m.b16*m.b22 + 384*m.b6*m.b12*m.b17*m.b23 + 384*m.b6*m.b12*m.b18*m.b24 + 384*m.b6*m.b12*
                       m.b19*m.b25 + 384*m.b6*m.b12*m.b20*m.b26 + 320*m.b6*m.b12*m.b21*m.b27 + 256*m.b6*m.b12*m.b22*
                       m.b28 + 192*m.b6*m.b12*m.b23*m.b29 + 128*m.b6*m.b12*m.b24*m.b30 + 64*m.b6*m.b12*m.b25*m.b31 + 384
                       *m.b6*m.b13*m.b14*m.b21 + 384*m.b6*m.b13*m.b15*m.b22 + 384*m.b6*m.b13*m.b16*m.b23 + 384*m.b6*
                       m.b13*m.b17*m.b24 + 384*m.b6*m.b13*m.b18*m.b25 + 384*m.b6*m.b13*m.b19*m.b26 + 320*m.b6*m.b13*
                       m.b20*m.b27 + 256*m.b6*m.b13*m.b21*m.b28 + 192*m.b6*m.b13*m.b22*m.b29 + 128*m.b6*m.b13*m.b23*
                       m.b30 + 64*m.b6*m.b13*m.b24*m.b31 + 384*m.b6*m.b14*m.b15*m.b23 + 384*m.b6*m.b14*m.b16*m.b24 + 384
                       *m.b6*m.b14*m.b17*m.b25 + 384*m.b6*m.b14*m.b18*m.b26 + 320*m.b6*m.b14*m.b19*m.b27 + 256*m.b6*
                       m.b14*m.b20*m.b28 + 192*m.b6*m.b14*m.b21*m.b29 + 128*m.b6*m.b14*m.b22*m.b30 + 64*m.b6*m.b14*m.b23
                       *m.b31 + 384*m.b6*m.b15*m.b16*m.b25 + 384*m.b6*m.b15*m.b17*m.b26 + 320*m.b6*m.b15*m.b18*m.b27 + 
                       256*m.b6*m.b15*m.b19*m.b28 + 192*m.b6*m.b15*m.b20*m.b29 + 128*m.b6*m.b15*m.b21*m.b30 + 64*m.b6*
                       m.b15*m.b22*m.b31 + 320*m.b6*m.b16*m.b17*m.b27 + 256*m.b6*m.b16*m.b18*m.b28 + 192*m.b6*m.b16*
                       m.b19*m.b29 + 128*m.b6*m.b16*m.b20*m.b30 + 64*m.b6*m.b16*m.b21*m.b31 + 192*m.b6*m.b17*m.b18*m.b29
                        + 128*m.b6*m.b17*m.b19*m.b30 + 64*m.b6*m.b17*m.b20*m.b31 + 64*m.b6*m.b18*m.b19*m.b31 + 448*m.b7*
                       m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*m.b7*m.b8*m.b12*
                       m.b13 + 448*m.b7*m.b8*m.b13*m.b14 + 448*m.b7*m.b8*m.b14*m.b15 + 448*m.b7*m.b8*m.b15*m.b16 + 448*
                       m.b7*m.b8*m.b16*m.b17 + 448*m.b7*m.b8*m.b17*m.b18 + 448*m.b7*m.b8*m.b18*m.b19 + 448*m.b7*m.b8*
                       m.b19*m.b20 + 448*m.b7*m.b8*m.b20*m.b21 + 448*m.b7*m.b8*m.b21*m.b22 + 448*m.b7*m.b8*m.b22*m.b23
                        + 448*m.b7*m.b8*m.b23*m.b24 + 448*m.b7*m.b8*m.b24*m.b25 + 448*m.b7*m.b8*m.b25*m.b26 + 384*m.b7*
                       m.b8*m.b26*m.b27 + 320*m.b7*m.b8*m.b27*m.b28 + 256*m.b7*m.b8*m.b28*m.b29 + 192*m.b7*m.b8*m.b29*
                       m.b30 + 128*m.b7*m.b8*m.b30*m.b31 + 64*m.b7*m.b8*m.b31*m.b32 + 448*m.b7*m.b9*m.b10*m.b12 + 448*
                       m.b7*m.b9*m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 448*m.b7*m.b9*m.b13*m.b15 + 448*m.b7*m.b9*
                       m.b14*m.b16 + 448*m.b7*m.b9*m.b15*m.b17 + 448*m.b7*m.b9*m.b16*m.b18 + 448*m.b7*m.b9*m.b17*m.b19
                        + 448*m.b7*m.b9*m.b18*m.b20 + 448*m.b7*m.b9*m.b19*m.b21 + 448*m.b7*m.b9*m.b20*m.b22 + 448*m.b7*
                       m.b9*m.b21*m.b23 + 448*m.b7*m.b9*m.b22*m.b24 + 448*m.b7*m.b9*m.b23*m.b25 + 448*m.b7*m.b9*m.b24*
                       m.b26 + 384*m.b7*m.b9*m.b25*m.b27 + 320*m.b7*m.b9*m.b26*m.b28 + 256*m.b7*m.b9*m.b27*m.b29 + 192*
                       m.b7*m.b9*m.b28*m.b30 + 128*m.b7*m.b9*m.b29*m.b31 + 64*m.b7*m.b9*m.b30*m.b32 + 448*m.b7*m.b10*
                       m.b11*m.b14 + 448*m.b7*m.b10*m.b12*m.b15 + 448*m.b7*m.b10*m.b13*m.b16 + 448*m.b7*m.b10*m.b14*
                       m.b17 + 448*m.b7*m.b10*m.b15*m.b18 + 448*m.b7*m.b10*m.b16*m.b19 + 448*m.b7*m.b10*m.b17*m.b20 + 
                       448*m.b7*m.b10*m.b18*m.b21 + 448*m.b7*m.b10*m.b19*m.b22 + 448*m.b7*m.b10*m.b20*m.b23 + 448*m.b7*
                       m.b10*m.b21*m.b24 + 448*m.b7*m.b10*m.b22*m.b25 + 448*m.b7*m.b10*m.b23*m.b26 + 384*m.b7*m.b10*
                       m.b24*m.b27 + 320*m.b7*m.b10*m.b25*m.b28 + 256*m.b7*m.b10*m.b26*m.b29 + 192*m.b7*m.b10*m.b27*
                       m.b30 + 128*m.b7*m.b10*m.b28*m.b31 + 64*m.b7*m.b10*m.b29*m.b32 + 448*m.b7*m.b11*m.b12*m.b16 + 448
                       *m.b7*m.b11*m.b13*m.b17 + 448*m.b7*m.b11*m.b14*m.b18 + 448*m.b7*m.b11*m.b15*m.b19 + 448*m.b7*
                       m.b11*m.b16*m.b20 + 448*m.b7*m.b11*m.b17*m.b21 + 448*m.b7*m.b11*m.b18*m.b22 + 448*m.b7*m.b11*
                       m.b19*m.b23 + 448*m.b7*m.b11*m.b20*m.b24 + 448*m.b7*m.b11*m.b21*m.b25 + 448*m.b7*m.b11*m.b22*
                       m.b26 + 384*m.b7*m.b11*m.b23*m.b27 + 320*m.b7*m.b11*m.b24*m.b28 + 256*m.b7*m.b11*m.b25*m.b29 + 
                       192*m.b7*m.b11*m.b26*m.b30 + 128*m.b7*m.b11*m.b27*m.b31 + 64*m.b7*m.b11*m.b28*m.b32 + 448*m.b7*
                       m.b12*m.b13*m.b18 + 448*m.b7*m.b12*m.b14*m.b19 + 448*m.b7*m.b12*m.b15*m.b20 + 448*m.b7*m.b12*
                       m.b16*m.b21 + 448*m.b7*m.b12*m.b17*m.b22 + 448*m.b7*m.b12*m.b18*m.b23 + 448*m.b7*m.b12*m.b19*
                       m.b24 + 448*m.b7*m.b12*m.b20*m.b25 + 448*m.b7*m.b12*m.b21*m.b26 + 384*m.b7*m.b12*m.b22*m.b27 + 
                       320*m.b7*m.b12*m.b23*m.b28 + 256*m.b7*m.b12*m.b24*m.b29 + 192*m.b7*m.b12*m.b25*m.b30 + 128*m.b7*
                       m.b12*m.b26*m.b31 + 64*m.b7*m.b12*m.b27*m.b32 + 448*m.b7*m.b13*m.b14*m.b20 + 448*m.b7*m.b13*m.b15
                       *m.b21 + 448*m.b7*m.b13*m.b16*m.b22 + 448*m.b7*m.b13*m.b17*m.b23 + 448*m.b7*m.b13*m.b18*m.b24 + 
                       448*m.b7*m.b13*m.b19*m.b25 + 448*m.b7*m.b13*m.b20*m.b26 + 384*m.b7*m.b13*m.b21*m.b27 + 320*m.b7*
                       m.b13*m.b22*m.b28 + 256*m.b7*m.b13*m.b23*m.b29 + 192*m.b7*m.b13*m.b24*m.b30 + 128*m.b7*m.b13*
                       m.b25*m.b31 + 64*m.b7*m.b13*m.b26*m.b32 + 448*m.b7*m.b14*m.b15*m.b22 + 448*m.b7*m.b14*m.b16*m.b23
                        + 448*m.b7*m.b14*m.b17*m.b24 + 448*m.b7*m.b14*m.b18*m.b25 + 448*m.b7*m.b14*m.b19*m.b26 + 384*
                       m.b7*m.b14*m.b20*m.b27 + 320*m.b7*m.b14*m.b21*m.b28 + 256*m.b7*m.b14*m.b22*m.b29 + 192*m.b7*m.b14
                       *m.b23*m.b30 + 128*m.b7*m.b14*m.b24*m.b31 + 64*m.b7*m.b14*m.b25*m.b32 + 448*m.b7*m.b15*m.b16*
                       m.b24 + 448*m.b7*m.b15*m.b17*m.b25 + 448*m.b7*m.b15*m.b18*m.b26 + 384*m.b7*m.b15*m.b19*m.b27 + 
                       320*m.b7*m.b15*m.b20*m.b28 + 256*m.b7*m.b15*m.b21*m.b29 + 192*m.b7*m.b15*m.b22*m.b30 + 128*m.b7*
                       m.b15*m.b23*m.b31 + 64*m.b7*m.b15*m.b24*m.b32 + 448*m.b7*m.b16*m.b17*m.b26 + 384*m.b7*m.b16*m.b18
                       *m.b27 + 320*m.b7*m.b16*m.b19*m.b28 + 256*m.b7*m.b16*m.b20*m.b29 + 192*m.b7*m.b16*m.b21*m.b30 + 
                       128*m.b7*m.b16*m.b22*m.b31 + 64*m.b7*m.b16*m.b23*m.b32 + 320*m.b7*m.b17*m.b18*m.b28 + 256*m.b7*
                       m.b17*m.b19*m.b29 + 192*m.b7*m.b17*m.b20*m.b30 + 128*m.b7*m.b17*m.b21*m.b31 + 64*m.b7*m.b17*m.b22
                       *m.b32 + 192*m.b7*m.b18*m.b19*m.b30 + 128*m.b7*m.b18*m.b20*m.b31 + 64*m.b7*m.b18*m.b21*m.b32 + 64
                       *m.b7*m.b19*m.b20*m.b32 + 512*m.b8*m.b9*m.b10*m.b11 + 512*m.b8*m.b9*m.b11*m.b12 + 512*m.b8*m.b9*
                       m.b12*m.b13 + 512*m.b8*m.b9*m.b13*m.b14 + 512*m.b8*m.b9*m.b14*m.b15 + 512*m.b8*m.b9*m.b15*m.b16
                        + 512*m.b8*m.b9*m.b16*m.b17 + 512*m.b8*m.b9*m.b17*m.b18 + 512*m.b8*m.b9*m.b18*m.b19 + 512*m.b8*
                       m.b9*m.b19*m.b20 + 512*m.b8*m.b9*m.b20*m.b21 + 512*m.b8*m.b9*m.b21*m.b22 + 512*m.b8*m.b9*m.b22*
                       m.b23 + 512*m.b8*m.b9*m.b23*m.b24 + 512*m.b8*m.b9*m.b24*m.b25 + 512*m.b8*m.b9*m.b25*m.b26 + 448*
                       m.b8*m.b9*m.b26*m.b27 + 384*m.b8*m.b9*m.b27*m.b28 + 320*m.b8*m.b9*m.b28*m.b29 + 256*m.b8*m.b9*
                       m.b29*m.b30 + 192*m.b8*m.b9*m.b30*m.b31 + 128*m.b8*m.b9*m.b31*m.b32 + 64*m.b8*m.b9*m.b32*m.b33 + 
                       512*m.b8*m.b10*m.b11*m.b13 + 512*m.b8*m.b10*m.b12*m.b14 + 512*m.b8*m.b10*m.b13*m.b15 + 512*m.b8*
                       m.b10*m.b14*m.b16 + 512*m.b8*m.b10*m.b15*m.b17 + 512*m.b8*m.b10*m.b16*m.b18 + 512*m.b8*m.b10*
                       m.b17*m.b19 + 512*m.b8*m.b10*m.b18*m.b20 + 512*m.b8*m.b10*m.b19*m.b21 + 512*m.b8*m.b10*m.b20*
                       m.b22 + 512*m.b8*m.b10*m.b21*m.b23 + 512*m.b8*m.b10*m.b22*m.b24 + 512*m.b8*m.b10*m.b23*m.b25 + 
                       512*m.b8*m.b10*m.b24*m.b26 + 448*m.b8*m.b10*m.b25*m.b27 + 384*m.b8*m.b10*m.b26*m.b28 + 320*m.b8*
                       m.b10*m.b27*m.b29 + 256*m.b8*m.b10*m.b28*m.b30 + 192*m.b8*m.b10*m.b29*m.b31 + 128*m.b8*m.b10*
                       m.b30*m.b32 + 64*m.b8*m.b10*m.b31*m.b33 + 512*m.b8*m.b11*m.b12*m.b15 + 512*m.b8*m.b11*m.b13*m.b16
                        + 512*m.b8*m.b11*m.b14*m.b17 + 512*m.b8*m.b11*m.b15*m.b18 + 512*m.b8*m.b11*m.b16*m.b19 + 512*
                       m.b8*m.b11*m.b17*m.b20 + 512*m.b8*m.b11*m.b18*m.b21 + 512*m.b8*m.b11*m.b19*m.b22 + 512*m.b8*m.b11
                       *m.b20*m.b23 + 512*m.b8*m.b11*m.b21*m.b24 + 512*m.b8*m.b11*m.b22*m.b25 + 512*m.b8*m.b11*m.b23*
                       m.b26 + 448*m.b8*m.b11*m.b24*m.b27 + 384*m.b8*m.b11*m.b25*m.b28 + 320*m.b8*m.b11*m.b26*m.b29 + 
                       256*m.b8*m.b11*m.b27*m.b30 + 192*m.b8*m.b11*m.b28*m.b31 + 128*m.b8*m.b11*m.b29*m.b32 + 64*m.b8*
                       m.b11*m.b30*m.b33 + 512*m.b8*m.b12*m.b13*m.b17 + 512*m.b8*m.b12*m.b14*m.b18 + 512*m.b8*m.b12*
                       m.b15*m.b19 + 512*m.b8*m.b12*m.b16*m.b20 + 512*m.b8*m.b12*m.b17*m.b21 + 512*m.b8*m.b12*m.b18*
                       m.b22 + 512*m.b8*m.b12*m.b19*m.b23 + 512*m.b8*m.b12*m.b20*m.b24 + 512*m.b8*m.b12*m.b21*m.b25 + 
                       512*m.b8*m.b12*m.b22*m.b26 + 448*m.b8*m.b12*m.b23*m.b27 + 384*m.b8*m.b12*m.b24*m.b28 + 320*m.b8*
                       m.b12*m.b25*m.b29 + 256*m.b8*m.b12*m.b26*m.b30 + 192*m.b8*m.b12*m.b27*m.b31 + 128*m.b8*m.b12*
                       m.b28*m.b32 + 64*m.b8*m.b12*m.b29*m.b33 + 512*m.b8*m.b13*m.b14*m.b19 + 512*m.b8*m.b13*m.b15*m.b20
                        + 512*m.b8*m.b13*m.b16*m.b21 + 512*m.b8*m.b13*m.b17*m.b22 + 512*m.b8*m.b13*m.b18*m.b23 + 512*
                       m.b8*m.b13*m.b19*m.b24 + 512*m.b8*m.b13*m.b20*m.b25 + 512*m.b8*m.b13*m.b21*m.b26 + 448*m.b8*m.b13
                       *m.b22*m.b27 + 384*m.b8*m.b13*m.b23*m.b28 + 320*m.b8*m.b13*m.b24*m.b29 + 256*m.b8*m.b13*m.b25*
                       m.b30 + 192*m.b8*m.b13*m.b26*m.b31 + 128*m.b8*m.b13*m.b27*m.b32 + 64*m.b8*m.b13*m.b28*m.b33 + 512
                       *m.b8*m.b14*m.b15*m.b21 + 512*m.b8*m.b14*m.b16*m.b22 + 512*m.b8*m.b14*m.b17*m.b23 + 512*m.b8*
                       m.b14*m.b18*m.b24 + 512*m.b8*m.b14*m.b19*m.b25 + 512*m.b8*m.b14*m.b20*m.b26 + 448*m.b8*m.b14*
                       m.b21*m.b27 + 384*m.b8*m.b14*m.b22*m.b28 + 320*m.b8*m.b14*m.b23*m.b29 + 256*m.b8*m.b14*m.b24*
                       m.b30 + 192*m.b8*m.b14*m.b25*m.b31 + 128*m.b8*m.b14*m.b26*m.b32 + 64*m.b8*m.b14*m.b27*m.b33 + 512
                       *m.b8*m.b15*m.b16*m.b23 + 512*m.b8*m.b15*m.b17*m.b24 + 512*m.b8*m.b15*m.b18*m.b25 + 512*m.b8*
                       m.b15*m.b19*m.b26 + 448*m.b8*m.b15*m.b20*m.b27 + 384*m.b8*m.b15*m.b21*m.b28 + 320*m.b8*m.b15*
                       m.b22*m.b29 + 256*m.b8*m.b15*m.b23*m.b30 + 192*m.b8*m.b15*m.b24*m.b31 + 128*m.b8*m.b15*m.b25*
                       m.b32 + 64*m.b8*m.b15*m.b26*m.b33 + 512*m.b8*m.b16*m.b17*m.b25 + 512*m.b8*m.b16*m.b18*m.b26 + 448
                       *m.b8*m.b16*m.b19*m.b27 + 384*m.b8*m.b16*m.b20*m.b28 + 320*m.b8*m.b16*m.b21*m.b29 + 256*m.b8*
                       m.b16*m.b22*m.b30 + 192*m.b8*m.b16*m.b23*m.b31 + 128*m.b8*m.b16*m.b24*m.b32 + 64*m.b8*m.b16*m.b25
                       *m.b33 + 448*m.b8*m.b17*m.b18*m.b27 + 384*m.b8*m.b17*m.b19*m.b28 + 320*m.b8*m.b17*m.b20*m.b29 + 
                       256*m.b8*m.b17*m.b21*m.b30 + 192*m.b8*m.b17*m.b22*m.b31 + 128*m.b8*m.b17*m.b23*m.b32 + 64*m.b8*
                       m.b17*m.b24*m.b33 + 320*m.b8*m.b18*m.b19*m.b29 + 256*m.b8*m.b18*m.b20*m.b30 + 192*m.b8*m.b18*
                       m.b21*m.b31 + 128*m.b8*m.b18*m.b22*m.b32 + 64*m.b8*m.b18*m.b23*m.b33 + 192*m.b8*m.b19*m.b20*m.b31
                        + 128*m.b8*m.b19*m.b21*m.b32 + 64*m.b8*m.b19*m.b22*m.b33 + 64*m.b8*m.b20*m.b21*m.b33 + 576*m.b9*
                       m.b10*m.b11*m.b12 + 576*m.b9*m.b10*m.b12*m.b13 + 576*m.b9*m.b10*m.b13*m.b14 + 576*m.b9*m.b10*
                       m.b14*m.b15 + 576*m.b9*m.b10*m.b15*m.b16 + 576*m.b9*m.b10*m.b16*m.b17 + 576*m.b9*m.b10*m.b17*
                       m.b18 + 576*m.b9*m.b10*m.b18*m.b19 + 576*m.b9*m.b10*m.b19*m.b20 + 576*m.b9*m.b10*m.b20*m.b21 + 
                       576*m.b9*m.b10*m.b21*m.b22 + 576*m.b9*m.b10*m.b22*m.b23 + 576*m.b9*m.b10*m.b23*m.b24 + 576*m.b9*
                       m.b10*m.b24*m.b25 + 576*m.b9*m.b10*m.b25*m.b26 + 512*m.b9*m.b10*m.b26*m.b27 + 448*m.b9*m.b10*
                       m.b27*m.b28 + 384*m.b9*m.b10*m.b28*m.b29 + 320*m.b9*m.b10*m.b29*m.b30 + 256*m.b9*m.b10*m.b30*
                       m.b31 + 192*m.b9*m.b10*m.b31*m.b32 + 128*m.b9*m.b10*m.b32*m.b33 + 64*m.b9*m.b10*m.b33*m.b34 + 576
                       *m.b9*m.b11*m.b12*m.b14 + 576*m.b9*m.b11*m.b13*m.b15 + 576*m.b9*m.b11*m.b14*m.b16 + 576*m.b9*
                       m.b11*m.b15*m.b17 + 576*m.b9*m.b11*m.b16*m.b18 + 576*m.b9*m.b11*m.b17*m.b19 + 576*m.b9*m.b11*
                       m.b18*m.b20 + 576*m.b9*m.b11*m.b19*m.b21 + 576*m.b9*m.b11*m.b20*m.b22 + 576*m.b9*m.b11*m.b21*
                       m.b23 + 576*m.b9*m.b11*m.b22*m.b24 + 576*m.b9*m.b11*m.b23*m.b25 + 576*m.b9*m.b11*m.b24*m.b26 + 
                       512*m.b9*m.b11*m.b25*m.b27 + 448*m.b9*m.b11*m.b26*m.b28 + 384*m.b9*m.b11*m.b27*m.b29 + 320*m.b9*
                       m.b11*m.b28*m.b30 + 256*m.b9*m.b11*m.b29*m.b31 + 192*m.b9*m.b11*m.b30*m.b32 + 128*m.b9*m.b11*
                       m.b31*m.b33 + 64*m.b9*m.b11*m.b32*m.b34 + 576*m.b9*m.b12*m.b13*m.b16 + 576*m.b9*m.b12*m.b14*m.b17
                        + 576*m.b9*m.b12*m.b15*m.b18 + 576*m.b9*m.b12*m.b16*m.b19 + 576*m.b9*m.b12*m.b17*m.b20 + 576*
                       m.b9*m.b12*m.b18*m.b21 + 576*m.b9*m.b12*m.b19*m.b22 + 576*m.b9*m.b12*m.b20*m.b23 + 576*m.b9*m.b12
                       *m.b21*m.b24 + 576*m.b9*m.b12*m.b22*m.b25 + 576*m.b9*m.b12*m.b23*m.b26 + 512*m.b9*m.b12*m.b24*
                       m.b27 + 448*m.b9*m.b12*m.b25*m.b28 + 384*m.b9*m.b12*m.b26*m.b29 + 320*m.b9*m.b12*m.b27*m.b30 + 
                       256*m.b9*m.b12*m.b28*m.b31 + 192*m.b9*m.b12*m.b29*m.b32 + 128*m.b9*m.b12*m.b30*m.b33 + 64*m.b9*
                       m.b12*m.b31*m.b34 + 576*m.b9*m.b13*m.b14*m.b18 + 576*m.b9*m.b13*m.b15*m.b19 + 576*m.b9*m.b13*
                       m.b16*m.b20 + 576*m.b9*m.b13*m.b17*m.b21 + 576*m.b9*m.b13*m.b18*m.b22 + 576*m.b9*m.b13*m.b19*
                       m.b23 + 576*m.b9*m.b13*m.b20*m.b24 + 576*m.b9*m.b13*m.b21*m.b25 + 576*m.b9*m.b13*m.b22*m.b26 + 
                       512*m.b9*m.b13*m.b23*m.b27 + 448*m.b9*m.b13*m.b24*m.b28 + 384*m.b9*m.b13*m.b25*m.b29 + 320*m.b9*
                       m.b13*m.b26*m.b30 + 256*m.b9*m.b13*m.b27*m.b31 + 192*m.b9*m.b13*m.b28*m.b32 + 128*m.b9*m.b13*
                       m.b29*m.b33 + 64*m.b9*m.b13*m.b30*m.b34 + 576*m.b9*m.b14*m.b15*m.b20 + 576*m.b9*m.b14*m.b16*m.b21
                        + 576*m.b9*m.b14*m.b17*m.b22 + 576*m.b9*m.b14*m.b18*m.b23 + 576*m.b9*m.b14*m.b19*m.b24 + 576*
                       m.b9*m.b14*m.b20*m.b25 + 576*m.b9*m.b14*m.b21*m.b26 + 512*m.b9*m.b14*m.b22*m.b27 + 448*m.b9*m.b14
                       *m.b23*m.b28 + 384*m.b9*m.b14*m.b24*m.b29 + 320*m.b9*m.b14*m.b25*m.b30 + 256*m.b9*m.b14*m.b26*
                       m.b31 + 192*m.b9*m.b14*m.b27*m.b32 + 128*m.b9*m.b14*m.b28*m.b33 + 64*m.b9*m.b14*m.b29*m.b34 + 576
                       *m.b9*m.b15*m.b16*m.b22 + 576*m.b9*m.b15*m.b17*m.b23 + 576*m.b9*m.b15*m.b18*m.b24 + 576*m.b9*
                       m.b15*m.b19*m.b25 + 576*m.b9*m.b15*m.b20*m.b26 + 512*m.b9*m.b15*m.b21*m.b27 + 448*m.b9*m.b15*
                       m.b22*m.b28 + 384*m.b9*m.b15*m.b23*m.b29 + 320*m.b9*m.b15*m.b24*m.b30 + 256*m.b9*m.b15*m.b25*
                       m.b31 + 192*m.b9*m.b15*m.b26*m.b32 + 128*m.b9*m.b15*m.b27*m.b33 + 64*m.b9*m.b15*m.b28*m.b34 + 576
                       *m.b9*m.b16*m.b17*m.b24 + 576*m.b9*m.b16*m.b18*m.b25 + 576*m.b9*m.b16*m.b19*m.b26 + 512*m.b9*
                       m.b16*m.b20*m.b27 + 448*m.b9*m.b16*m.b21*m.b28 + 384*m.b9*m.b16*m.b22*m.b29 + 320*m.b9*m.b16*
                       m.b23*m.b30 + 256*m.b9*m.b16*m.b24*m.b31 + 192*m.b9*m.b16*m.b25*m.b32 + 128*m.b9*m.b16*m.b26*
                       m.b33 + 64*m.b9*m.b16*m.b27*m.b34 + 576*m.b9*m.b17*m.b18*m.b26 + 512*m.b9*m.b17*m.b19*m.b27 + 448
                       *m.b9*m.b17*m.b20*m.b28 + 384*m.b9*m.b17*m.b21*m.b29 + 320*m.b9*m.b17*m.b22*m.b30 + 256*m.b9*
                       m.b17*m.b23*m.b31 + 192*m.b9*m.b17*m.b24*m.b32 + 128*m.b9*m.b17*m.b25*m.b33 + 64*m.b9*m.b17*m.b26
                       *m.b34 + 448*m.b9*m.b18*m.b19*m.b28 + 384*m.b9*m.b18*m.b20*m.b29 + 320*m.b9*m.b18*m.b21*m.b30 + 
                       256*m.b9*m.b18*m.b22*m.b31 + 192*m.b9*m.b18*m.b23*m.b32 + 128*m.b9*m.b18*m.b24*m.b33 + 64*m.b9*
                       m.b18*m.b25*m.b34 + 320*m.b9*m.b19*m.b20*m.b30 + 256*m.b9*m.b19*m.b21*m.b31 + 192*m.b9*m.b19*
                       m.b22*m.b32 + 128*m.b9*m.b19*m.b23*m.b33 + 64*m.b9*m.b19*m.b24*m.b34 + 192*m.b9*m.b20*m.b21*m.b32
                        + 128*m.b9*m.b20*m.b22*m.b33 + 64*m.b9*m.b20*m.b23*m.b34 + 64*m.b9*m.b21*m.b22*m.b34 + 640*m.b10
                       *m.b11*m.b12*m.b13 + 640*m.b10*m.b11*m.b13*m.b14 + 640*m.b10*m.b11*m.b14*m.b15 + 640*m.b10*m.b11*
                       m.b15*m.b16 + 640*m.b10*m.b11*m.b16*m.b17 + 640*m.b10*m.b11*m.b17*m.b18 + 640*m.b10*m.b11*m.b18*
                       m.b19 + 640*m.b10*m.b11*m.b19*m.b20 + 640*m.b10*m.b11*m.b20*m.b21 + 640*m.b10*m.b11*m.b21*m.b22
                        + 640*m.b10*m.b11*m.b22*m.b23 + 640*m.b10*m.b11*m.b23*m.b24 + 640*m.b10*m.b11*m.b24*m.b25 + 640*
                       m.b10*m.b11*m.b25*m.b26 + 576*m.b10*m.b11*m.b26*m.b27 + 512*m.b10*m.b11*m.b27*m.b28 + 448*m.b10*
                       m.b11*m.b28*m.b29 + 384*m.b10*m.b11*m.b29*m.b30 + 320*m.b10*m.b11*m.b30*m.b31 + 256*m.b10*m.b11*
                       m.b31*m.b32 + 192*m.b10*m.b11*m.b32*m.b33 + 128*m.b10*m.b11*m.b33*m.b34 + 64*m.b10*m.b11*m.b34*
                       m.b35 + 640*m.b10*m.b12*m.b13*m.b15 + 640*m.b10*m.b12*m.b14*m.b16 + 640*m.b10*m.b12*m.b15*m.b17
                        + 640*m.b10*m.b12*m.b16*m.b18 + 640*m.b10*m.b12*m.b17*m.b19 + 640*m.b10*m.b12*m.b18*m.b20 + 640*
                       m.b10*m.b12*m.b19*m.b21 + 640*m.b10*m.b12*m.b20*m.b22 + 640*m.b10*m.b12*m.b21*m.b23 + 640*m.b10*
                       m.b12*m.b22*m.b24 + 640*m.b10*m.b12*m.b23*m.b25 + 640*m.b10*m.b12*m.b24*m.b26 + 576*m.b10*m.b12*
                       m.b25*m.b27 + 512*m.b10*m.b12*m.b26*m.b28 + 448*m.b10*m.b12*m.b27*m.b29 + 384*m.b10*m.b12*m.b28*
                       m.b30 + 320*m.b10*m.b12*m.b29*m.b31 + 256*m.b10*m.b12*m.b30*m.b32 + 192*m.b10*m.b12*m.b31*m.b33
                        + 128*m.b10*m.b12*m.b32*m.b34 + 64*m.b10*m.b12*m.b33*m.b35 + 640*m.b10*m.b13*m.b14*m.b17 + 640*
                       m.b10*m.b13*m.b15*m.b18 + 640*m.b10*m.b13*m.b16*m.b19 + 640*m.b10*m.b13*m.b17*m.b20 + 640*m.b10*
                       m.b13*m.b18*m.b21 + 640*m.b10*m.b13*m.b19*m.b22 + 640*m.b10*m.b13*m.b20*m.b23 + 640*m.b10*m.b13*
                       m.b21*m.b24 + 640*m.b10*m.b13*m.b22*m.b25 + 640*m.b10*m.b13*m.b23*m.b26 + 576*m.b10*m.b13*m.b24*
                       m.b27 + 512*m.b10*m.b13*m.b25*m.b28 + 448*m.b10*m.b13*m.b26*m.b29 + 384*m.b10*m.b13*m.b27*m.b30
                        + 320*m.b10*m.b13*m.b28*m.b31 + 256*m.b10*m.b13*m.b29*m.b32 + 192*m.b10*m.b13*m.b30*m.b33 + 128*
                       m.b10*m.b13*m.b31*m.b34 + 64*m.b10*m.b13*m.b32*m.b35 + 640*m.b10*m.b14*m.b15*m.b19 + 640*m.b10*
                       m.b14*m.b16*m.b20 + 640*m.b10*m.b14*m.b17*m.b21 + 640*m.b10*m.b14*m.b18*m.b22 + 640*m.b10*m.b14*
                       m.b19*m.b23 + 640*m.b10*m.b14*m.b20*m.b24 + 640*m.b10*m.b14*m.b21*m.b25 + 640*m.b10*m.b14*m.b22*
                       m.b26 + 576*m.b10*m.b14*m.b23*m.b27 + 512*m.b10*m.b14*m.b24*m.b28 + 448*m.b10*m.b14*m.b25*m.b29
                        + 384*m.b10*m.b14*m.b26*m.b30 + 320*m.b10*m.b14*m.b27*m.b31 + 256*m.b10*m.b14*m.b28*m.b32 + 192*
                       m.b10*m.b14*m.b29*m.b33 + 128*m.b10*m.b14*m.b30*m.b34 + 64*m.b10*m.b14*m.b31*m.b35 + 640*m.b10*
                       m.b15*m.b16*m.b21 + 640*m.b10*m.b15*m.b17*m.b22 + 640*m.b10*m.b15*m.b18*m.b23 + 640*m.b10*m.b15*
                       m.b19*m.b24 + 640*m.b10*m.b15*m.b20*m.b25 + 640*m.b10*m.b15*m.b21*m.b26 + 576*m.b10*m.b15*m.b22*
                       m.b27 + 512*m.b10*m.b15*m.b23*m.b28 + 448*m.b10*m.b15*m.b24*m.b29 + 384*m.b10*m.b15*m.b25*m.b30
                        + 320*m.b10*m.b15*m.b26*m.b31 + 256*m.b10*m.b15*m.b27*m.b32 + 192*m.b10*m.b15*m.b28*m.b33 + 128*
                       m.b10*m.b15*m.b29*m.b34 + 64*m.b10*m.b15*m.b30*m.b35 + 640*m.b10*m.b16*m.b17*m.b23 + 640*m.b10*
                       m.b16*m.b18*m.b24 + 640*m.b10*m.b16*m.b19*m.b25 + 640*m.b10*m.b16*m.b20*m.b26 + 576*m.b10*m.b16*
                       m.b21*m.b27 + 512*m.b10*m.b16*m.b22*m.b28 + 448*m.b10*m.b16*m.b23*m.b29 + 384*m.b10*m.b16*m.b24*
                       m.b30 + 320*m.b10*m.b16*m.b25*m.b31 + 256*m.b10*m.b16*m.b26*m.b32 + 192*m.b10*m.b16*m.b27*m.b33
                        + 128*m.b10*m.b16*m.b28*m.b34 + 64*m.b10*m.b16*m.b29*m.b35 + 640*m.b10*m.b17*m.b18*m.b25 + 640*
                       m.b10*m.b17*m.b19*m.b26 + 576*m.b10*m.b17*m.b20*m.b27 + 512*m.b10*m.b17*m.b21*m.b28 + 448*m.b10*
                       m.b17*m.b22*m.b29 + 384*m.b10*m.b17*m.b23*m.b30 + 320*m.b10*m.b17*m.b24*m.b31 + 256*m.b10*m.b17*
                       m.b25*m.b32 + 192*m.b10*m.b17*m.b26*m.b33 + 128*m.b10*m.b17*m.b27*m.b34 + 64*m.b10*m.b17*m.b28*
                       m.b35 + 576*m.b10*m.b18*m.b19*m.b27 + 512*m.b10*m.b18*m.b20*m.b28 + 448*m.b10*m.b18*m.b21*m.b29
                        + 384*m.b10*m.b18*m.b22*m.b30 + 320*m.b10*m.b18*m.b23*m.b31 + 256*m.b10*m.b18*m.b24*m.b32 + 192*
                       m.b10*m.b18*m.b25*m.b33 + 128*m.b10*m.b18*m.b26*m.b34 + 64*m.b10*m.b18*m.b27*m.b35 + 448*m.b10*
                       m.b19*m.b20*m.b29 + 384*m.b10*m.b19*m.b21*m.b30 + 320*m.b10*m.b19*m.b22*m.b31 + 256*m.b10*m.b19*
                       m.b23*m.b32 + 192*m.b10*m.b19*m.b24*m.b33 + 128*m.b10*m.b19*m.b25*m.b34 + 64*m.b10*m.b19*m.b26*
                       m.b35 + 320*m.b10*m.b20*m.b21*m.b31 + 256*m.b10*m.b20*m.b22*m.b32 + 192*m.b10*m.b20*m.b23*m.b33
                        + 128*m.b10*m.b20*m.b24*m.b34 + 64*m.b10*m.b20*m.b25*m.b35 + 192*m.b10*m.b21*m.b22*m.b33 + 128*
                       m.b10*m.b21*m.b23*m.b34 + 64*m.b10*m.b21*m.b24*m.b35 + 64*m.b10*m.b22*m.b23*m.b35 + 640*m.b11*
                       m.b12*m.b13*m.b14 + 640*m.b11*m.b12*m.b14*m.b15 + 640*m.b11*m.b12*m.b15*m.b16 + 640*m.b11*m.b12*
                       m.b16*m.b17 + 640*m.b11*m.b12*m.b17*m.b18 + 704*m.b11*m.b12*m.b18*m.b19 + 704*m.b11*m.b12*m.b19*
                       m.b20 + 704*m.b11*m.b12*m.b20*m.b21 + 704*m.b11*m.b12*m.b21*m.b22 + 704*m.b11*m.b12*m.b22*m.b23
                        + 704*m.b11*m.b12*m.b23*m.b24 + 704*m.b11*m.b12*m.b24*m.b25 + 640*m.b11*m.b12*m.b25*m.b26 + 576*
                       m.b11*m.b12*m.b26*m.b27 + 512*m.b11*m.b12*m.b27*m.b28 + 448*m.b11*m.b12*m.b28*m.b29 + 384*m.b11*
                       m.b12*m.b29*m.b30 + 320*m.b11*m.b12*m.b30*m.b31 + 256*m.b11*m.b12*m.b31*m.b32 + 192*m.b11*m.b12*
                       m.b32*m.b33 + 128*m.b11*m.b12*m.b33*m.b34 + 64*m.b11*m.b12*m.b34*m.b35 + 640*m.b11*m.b13*m.b14*
                       m.b16 + 640*m.b11*m.b13*m.b15*m.b17 + 640*m.b11*m.b13*m.b16*m.b18 + 704*m.b11*m.b13*m.b17*m.b19
                        + 704*m.b11*m.b13*m.b18*m.b20 + 704*m.b11*m.b13*m.b19*m.b21 + 704*m.b11*m.b13*m.b20*m.b22 + 704*
                       m.b11*m.b13*m.b21*m.b23 + 704*m.b11*m.b13*m.b22*m.b24 + 704*m.b11*m.b13*m.b23*m.b25 + 640*m.b11*
                       m.b13*m.b24*m.b26 + 576*m.b11*m.b13*m.b25*m.b27 + 512*m.b11*m.b13*m.b26*m.b28 + 448*m.b11*m.b13*
                       m.b27*m.b29 + 384*m.b11*m.b13*m.b28*m.b30 + 320*m.b11*m.b13*m.b29*m.b31 + 256*m.b11*m.b13*m.b30*
                       m.b32 + 192*m.b11*m.b13*m.b31*m.b33 + 128*m.b11*m.b13*m.b32*m.b34 + 64*m.b11*m.b13*m.b33*m.b35 + 
                       640*m.b11*m.b14*m.b15*m.b18 + 704*m.b11*m.b14*m.b16*m.b19 + 704*m.b11*m.b14*m.b17*m.b20 + 704*
                       m.b11*m.b14*m.b18*m.b21 + 704*m.b11*m.b14*m.b19*m.b22 + 704*m.b11*m.b14*m.b20*m.b23 + 704*m.b11*
                       m.b14*m.b21*m.b24 + 704*m.b11*m.b14*m.b22*m.b25 + 640*m.b11*m.b14*m.b23*m.b26 + 576*m.b11*m.b14*
                       m.b24*m.b27 + 512*m.b11*m.b14*m.b25*m.b28 + 448*m.b11*m.b14*m.b26*m.b29 + 384*m.b11*m.b14*m.b27*
                       m.b30 + 320*m.b11*m.b14*m.b28*m.b31 + 256*m.b11*m.b14*m.b29*m.b32 + 192*m.b11*m.b14*m.b30*m.b33
                        + 128*m.b11*m.b14*m.b31*m.b34 + 64*m.b11*m.b14*m.b32*m.b35 + 704*m.b11*m.b15*m.b16*m.b20 + 704*
                       m.b11*m.b15*m.b17*m.b21 + 704*m.b11*m.b15*m.b18*m.b22 + 704*m.b11*m.b15*m.b19*m.b23 + 704*m.b11*
                       m.b15*m.b20*m.b24 + 704*m.b11*m.b15*m.b21*m.b25 + 640*m.b11*m.b15*m.b22*m.b26 + 576*m.b11*m.b15*
                       m.b23*m.b27 + 512*m.b11*m.b15*m.b24*m.b28 + 448*m.b11*m.b15*m.b25*m.b29 + 384*m.b11*m.b15*m.b26*
                       m.b30 + 320*m.b11*m.b15*m.b27*m.b31 + 256*m.b11*m.b15*m.b28*m.b32 + 192*m.b11*m.b15*m.b29*m.b33
                        + 128*m.b11*m.b15*m.b30*m.b34 + 64*m.b11*m.b15*m.b31*m.b35 + 704*m.b11*m.b16*m.b17*m.b22 + 704*
                       m.b11*m.b16*m.b18*m.b23 + 704*m.b11*m.b16*m.b19*m.b24 + 704*m.b11*m.b16*m.b20*m.b25 + 640*m.b11*
                       m.b16*m.b21*m.b26 + 576*m.b11*m.b16*m.b22*m.b27 + 512*m.b11*m.b16*m.b23*m.b28 + 448*m.b11*m.b16*
                       m.b24*m.b29 + 384*m.b11*m.b16*m.b25*m.b30 + 320*m.b11*m.b16*m.b26*m.b31 + 256*m.b11*m.b16*m.b27*
                       m.b32 + 192*m.b11*m.b16*m.b28*m.b33 + 128*m.b11*m.b16*m.b29*m.b34 + 64*m.b11*m.b16*m.b30*m.b35 + 
                       704*m.b11*m.b17*m.b18*m.b24 + 704*m.b11*m.b17*m.b19*m.b25 + 640*m.b11*m.b17*m.b20*m.b26 + 576*
                       m.b11*m.b17*m.b21*m.b27 + 512*m.b11*m.b17*m.b22*m.b28 + 448*m.b11*m.b17*m.b23*m.b29 + 384*m.b11*
                       m.b17*m.b24*m.b30 + 320*m.b11*m.b17*m.b25*m.b31 + 256*m.b11*m.b17*m.b26*m.b32 + 192*m.b11*m.b17*
                       m.b27*m.b33 + 128*m.b11*m.b17*m.b28*m.b34 + 64*m.b11*m.b17*m.b29*m.b35 + 640*m.b11*m.b18*m.b19*
                       m.b26 + 576*m.b11*m.b18*m.b20*m.b27 + 512*m.b11*m.b18*m.b21*m.b28 + 448*m.b11*m.b18*m.b22*m.b29
                        + 384*m.b11*m.b18*m.b23*m.b30 + 320*m.b11*m.b18*m.b24*m.b31 + 256*m.b11*m.b18*m.b25*m.b32 + 192*
                       m.b11*m.b18*m.b26*m.b33 + 128*m.b11*m.b18*m.b27*m.b34 + 64*m.b11*m.b18*m.b28*m.b35 + 512*m.b11*
                       m.b19*m.b20*m.b28 + 448*m.b11*m.b19*m.b21*m.b29 + 384*m.b11*m.b19*m.b22*m.b30 + 320*m.b11*m.b19*
                       m.b23*m.b31 + 256*m.b11*m.b19*m.b24*m.b32 + 192*m.b11*m.b19*m.b25*m.b33 + 128*m.b11*m.b19*m.b26*
                       m.b34 + 64*m.b11*m.b19*m.b27*m.b35 + 384*m.b11*m.b20*m.b21*m.b30 + 320*m.b11*m.b20*m.b22*m.b31 + 
                       256*m.b11*m.b20*m.b23*m.b32 + 192*m.b11*m.b20*m.b24*m.b33 + 128*m.b11*m.b20*m.b25*m.b34 + 64*
                       m.b11*m.b20*m.b26*m.b35 + 256*m.b11*m.b21*m.b22*m.b32 + 192*m.b11*m.b21*m.b23*m.b33 + 128*m.b11*
                       m.b21*m.b24*m.b34 + 64*m.b11*m.b21*m.b25*m.b35 + 128*m.b11*m.b22*m.b23*m.b34 + 64*m.b11*m.b22*
                       m.b24*m.b35 + 640*m.b12*m.b13*m.b14*m.b15 + 640*m.b12*m.b13*m.b15*m.b16 + 640*m.b12*m.b13*m.b16*
                       m.b17 + 640*m.b12*m.b13*m.b17*m.b18 + 640*m.b12*m.b13*m.b18*m.b19 + 768*m.b12*m.b13*m.b19*m.b20
                        + 768*m.b12*m.b13*m.b20*m.b21 + 768*m.b12*m.b13*m.b21*m.b22 + 768*m.b12*m.b13*m.b22*m.b23 + 768*
                       m.b12*m.b13*m.b23*m.b24 + 704*m.b12*m.b13*m.b24*m.b25 + 640*m.b12*m.b13*m.b25*m.b26 + 576*m.b12*
                       m.b13*m.b26*m.b27 + 512*m.b12*m.b13*m.b27*m.b28 + 448*m.b12*m.b13*m.b28*m.b29 + 384*m.b12*m.b13*
                       m.b29*m.b30 + 320*m.b12*m.b13*m.b30*m.b31 + 256*m.b12*m.b13*m.b31*m.b32 + 192*m.b12*m.b13*m.b32*
                       m.b33 + 128*m.b12*m.b13*m.b33*m.b34 + 64*m.b12*m.b13*m.b34*m.b35 + 640*m.b12*m.b14*m.b15*m.b17 + 
                       640*m.b12*m.b14*m.b16*m.b18 + 640*m.b12*m.b14*m.b17*m.b19 + 768*m.b12*m.b14*m.b18*m.b20 + 768*
                       m.b12*m.b14*m.b19*m.b21 + 768*m.b12*m.b14*m.b20*m.b22 + 768*m.b12*m.b14*m.b21*m.b23 + 768*m.b12*
                       m.b14*m.b22*m.b24 + 704*m.b12*m.b14*m.b23*m.b25 + 640*m.b12*m.b14*m.b24*m.b26 + 576*m.b12*m.b14*
                       m.b25*m.b27 + 512*m.b12*m.b14*m.b26*m.b28 + 448*m.b12*m.b14*m.b27*m.b29 + 384*m.b12*m.b14*m.b28*
                       m.b30 + 320*m.b12*m.b14*m.b29*m.b31 + 256*m.b12*m.b14*m.b30*m.b32 + 192*m.b12*m.b14*m.b31*m.b33
                        + 128*m.b12*m.b14*m.b32*m.b34 + 64*m.b12*m.b14*m.b33*m.b35 + 640*m.b12*m.b15*m.b16*m.b19 + 768*
                       m.b12*m.b15*m.b17*m.b20 + 768*m.b12*m.b15*m.b18*m.b21 + 768*m.b12*m.b15*m.b19*m.b22 + 768*m.b12*
                       m.b15*m.b20*m.b23 + 768*m.b12*m.b15*m.b21*m.b24 + 704*m.b12*m.b15*m.b22*m.b25 + 640*m.b12*m.b15*
                       m.b23*m.b26 + 576*m.b12*m.b15*m.b24*m.b27 + 512*m.b12*m.b15*m.b25*m.b28 + 448*m.b12*m.b15*m.b26*
                       m.b29 + 384*m.b12*m.b15*m.b27*m.b30 + 320*m.b12*m.b15*m.b28*m.b31 + 256*m.b12*m.b15*m.b29*m.b32
                        + 192*m.b12*m.b15*m.b30*m.b33 + 128*m.b12*m.b15*m.b31*m.b34 + 64*m.b12*m.b15*m.b32*m.b35 + 768*
                       m.b12*m.b16*m.b17*m.b21 + 768*m.b12*m.b16*m.b18*m.b22 + 768*m.b12*m.b16*m.b19*m.b23 + 768*m.b12*
                       m.b16*m.b20*m.b24 + 704*m.b12*m.b16*m.b21*m.b25 + 640*m.b12*m.b16*m.b22*m.b26 + 576*m.b12*m.b16*
                       m.b23*m.b27 + 512*m.b12*m.b16*m.b24*m.b28 + 448*m.b12*m.b16*m.b25*m.b29 + 384*m.b12*m.b16*m.b26*
                       m.b30 + 320*m.b12*m.b16*m.b27*m.b31 + 256*m.b12*m.b16*m.b28*m.b32 + 192*m.b12*m.b16*m.b29*m.b33
                        + 128*m.b12*m.b16*m.b30*m.b34 + 64*m.b12*m.b16*m.b31*m.b35 + 768*m.b12*m.b17*m.b18*m.b23 + 768*
                       m.b12*m.b17*m.b19*m.b24 + 704*m.b12*m.b17*m.b20*m.b25 + 640*m.b12*m.b17*m.b21*m.b26 + 576*m.b12*
                       m.b17*m.b22*m.b27 + 512*m.b12*m.b17*m.b23*m.b28 + 448*m.b12*m.b17*m.b24*m.b29 + 384*m.b12*m.b17*
                       m.b25*m.b30 + 320*m.b12*m.b17*m.b26*m.b31 + 256*m.b12*m.b17*m.b27*m.b32 + 192*m.b12*m.b17*m.b28*
                       m.b33 + 128*m.b12*m.b17*m.b29*m.b34 + 64*m.b12*m.b17*m.b30*m.b35 + 704*m.b12*m.b18*m.b19*m.b25 + 
                       640*m.b12*m.b18*m.b20*m.b26 + 576*m.b12*m.b18*m.b21*m.b27 + 512*m.b12*m.b18*m.b22*m.b28 + 448*
                       m.b12*m.b18*m.b23*m.b29 + 384*m.b12*m.b18*m.b24*m.b30 + 320*m.b12*m.b18*m.b25*m.b31 + 256*m.b12*
                       m.b18*m.b26*m.b32 + 192*m.b12*m.b18*m.b27*m.b33 + 128*m.b12*m.b18*m.b28*m.b34 + 64*m.b12*m.b18*
                       m.b29*m.b35 + 576*m.b12*m.b19*m.b20*m.b27 + 512*m.b12*m.b19*m.b21*m.b28 + 448*m.b12*m.b19*m.b22*
                       m.b29 + 384*m.b12*m.b19*m.b23*m.b30 + 320*m.b12*m.b19*m.b24*m.b31 + 256*m.b12*m.b19*m.b25*m.b32
                        + 192*m.b12*m.b19*m.b26*m.b33 + 128*m.b12*m.b19*m.b27*m.b34 + 64*m.b12*m.b19*m.b28*m.b35 + 448*
                       m.b12*m.b20*m.b21*m.b29 + 384*m.b12*m.b20*m.b22*m.b30 + 320*m.b12*m.b20*m.b23*m.b31 + 256*m.b12*
                       m.b20*m.b24*m.b32 + 192*m.b12*m.b20*m.b25*m.b33 + 128*m.b12*m.b20*m.b26*m.b34 + 64*m.b12*m.b20*
                       m.b27*m.b35 + 320*m.b12*m.b21*m.b22*m.b31 + 256*m.b12*m.b21*m.b23*m.b32 + 192*m.b12*m.b21*m.b24*
                       m.b33 + 128*m.b12*m.b21*m.b25*m.b34 + 64*m.b12*m.b21*m.b26*m.b35 + 192*m.b12*m.b22*m.b23*m.b33 + 
                       128*m.b12*m.b22*m.b24*m.b34 + 64*m.b12*m.b22*m.b25*m.b35 + 64*m.b12*m.b23*m.b24*m.b35 + 640*m.b13
                       *m.b14*m.b15*m.b16 + 640*m.b13*m.b14*m.b16*m.b17 + 640*m.b13*m.b14*m.b17*m.b18 + 640*m.b13*m.b14*
                       m.b18*m.b19 + 640*m.b13*m.b14*m.b19*m.b20 + 832*m.b13*m.b14*m.b20*m.b21 + 832*m.b13*m.b14*m.b21*
                       m.b22 + 832*m.b13*m.b14*m.b22*m.b23 + 768*m.b13*m.b14*m.b23*m.b24 + 704*m.b13*m.b14*m.b24*m.b25
                        + 640*m.b13*m.b14*m.b25*m.b26 + 576*m.b13*m.b14*m.b26*m.b27 + 512*m.b13*m.b14*m.b27*m.b28 + 448*
                       m.b13*m.b14*m.b28*m.b29 + 384*m.b13*m.b14*m.b29*m.b30 + 320*m.b13*m.b14*m.b30*m.b31 + 256*m.b13*
                       m.b14*m.b31*m.b32 + 192*m.b13*m.b14*m.b32*m.b33 + 128*m.b13*m.b14*m.b33*m.b34 + 64*m.b13*m.b14*
                       m.b34*m.b35 + 640*m.b13*m.b15*m.b16*m.b18 + 640*m.b13*m.b15*m.b17*m.b19 + 640*m.b13*m.b15*m.b18*
                       m.b20 + 832*m.b13*m.b15*m.b19*m.b21 + 832*m.b13*m.b15*m.b20*m.b22 + 832*m.b13*m.b15*m.b21*m.b23
                        + 768*m.b13*m.b15*m.b22*m.b24 + 704*m.b13*m.b15*m.b23*m.b25 + 640*m.b13*m.b15*m.b24*m.b26 + 576*
                       m.b13*m.b15*m.b25*m.b27 + 512*m.b13*m.b15*m.b26*m.b28 + 448*m.b13*m.b15*m.b27*m.b29 + 384*m.b13*
                       m.b15*m.b28*m.b30 + 320*m.b13*m.b15*m.b29*m.b31 + 256*m.b13*m.b15*m.b30*m.b32 + 192*m.b13*m.b15*
                       m.b31*m.b33 + 128*m.b13*m.b15*m.b32*m.b34 + 64*m.b13*m.b15*m.b33*m.b35 + 640*m.b13*m.b16*m.b17*
                       m.b20 + 832*m.b13*m.b16*m.b18*m.b21 + 832*m.b13*m.b16*m.b19*m.b22 + 832*m.b13*m.b16*m.b20*m.b23
                        + 768*m.b13*m.b16*m.b21*m.b24 + 704*m.b13*m.b16*m.b22*m.b25 + 640*m.b13*m.b16*m.b23*m.b26 + 576*
                       m.b13*m.b16*m.b24*m.b27 + 512*m.b13*m.b16*m.b25*m.b28 + 448*m.b13*m.b16*m.b26*m.b29 + 384*m.b13*
                       m.b16*m.b27*m.b30 + 320*m.b13*m.b16*m.b28*m.b31 + 256*m.b13*m.b16*m.b29*m.b32 + 192*m.b13*m.b16*
                       m.b30*m.b33 + 128*m.b13*m.b16*m.b31*m.b34 + 64*m.b13*m.b16*m.b32*m.b35 + 832*m.b13*m.b17*m.b18*
                       m.b22 + 832*m.b13*m.b17*m.b19*m.b23 + 768*m.b13*m.b17*m.b20*m.b24 + 704*m.b13*m.b17*m.b21*m.b25
                        + 640*m.b13*m.b17*m.b22*m.b26 + 576*m.b13*m.b17*m.b23*m.b27 + 512*m.b13*m.b17*m.b24*m.b28 + 448*
                       m.b13*m.b17*m.b25*m.b29 + 384*m.b13*m.b17*m.b26*m.b30 + 320*m.b13*m.b17*m.b27*m.b31 + 256*m.b13*
                       m.b17*m.b28*m.b32 + 192*m.b13*m.b17*m.b29*m.b33 + 128*m.b13*m.b17*m.b30*m.b34 + 64*m.b13*m.b17*
                       m.b31*m.b35 + 768*m.b13*m.b18*m.b19*m.b24 + 704*m.b13*m.b18*m.b20*m.b25 + 640*m.b13*m.b18*m.b21*
                       m.b26 + 576*m.b13*m.b18*m.b22*m.b27 + 512*m.b13*m.b18*m.b23*m.b28 + 448*m.b13*m.b18*m.b24*m.b29
                        + 384*m.b13*m.b18*m.b25*m.b30 + 320*m.b13*m.b18*m.b26*m.b31 + 256*m.b13*m.b18*m.b27*m.b32 + 192*
                       m.b13*m.b18*m.b28*m.b33 + 128*m.b13*m.b18*m.b29*m.b34 + 64*m.b13*m.b18*m.b30*m.b35 + 640*m.b13*
                       m.b19*m.b20*m.b26 + 576*m.b13*m.b19*m.b21*m.b27 + 512*m.b13*m.b19*m.b22*m.b28 + 448*m.b13*m.b19*
                       m.b23*m.b29 + 384*m.b13*m.b19*m.b24*m.b30 + 320*m.b13*m.b19*m.b25*m.b31 + 256*m.b13*m.b19*m.b26*
                       m.b32 + 192*m.b13*m.b19*m.b27*m.b33 + 128*m.b13*m.b19*m.b28*m.b34 + 64*m.b13*m.b19*m.b29*m.b35 + 
                       512*m.b13*m.b20*m.b21*m.b28 + 448*m.b13*m.b20*m.b22*m.b29 + 384*m.b13*m.b20*m.b23*m.b30 + 320*
                       m.b13*m.b20*m.b24*m.b31 + 256*m.b13*m.b20*m.b25*m.b32 + 192*m.b13*m.b20*m.b26*m.b33 + 128*m.b13*
                       m.b20*m.b27*m.b34 + 64*m.b13*m.b20*m.b28*m.b35 + 384*m.b13*m.b21*m.b22*m.b30 + 320*m.b13*m.b21*
                       m.b23*m.b31 + 256*m.b13*m.b21*m.b24*m.b32 + 192*m.b13*m.b21*m.b25*m.b33 + 128*m.b13*m.b21*m.b26*
                       m.b34 + 64*m.b13*m.b21*m.b27*m.b35 + 256*m.b13*m.b22*m.b23*m.b32 + 192*m.b13*m.b22*m.b24*m.b33 + 
                       128*m.b13*m.b22*m.b25*m.b34 + 64*m.b13*m.b22*m.b26*m.b35 + 128*m.b13*m.b23*m.b24*m.b34 + 64*m.b13
                       *m.b23*m.b25*m.b35 + 640*m.b14*m.b15*m.b16*m.b17 + 640*m.b14*m.b15*m.b17*m.b18 + 640*m.b14*m.b15*
                       m.b18*m.b19 + 640*m.b14*m.b15*m.b19*m.b20 + 640*m.b14*m.b15*m.b20*m.b21 + 896*m.b14*m.b15*m.b21*
                       m.b22 + 832*m.b14*m.b15*m.b22*m.b23 + 768*m.b14*m.b15*m.b23*m.b24 + 704*m.b14*m.b15*m.b24*m.b25
                        + 640*m.b14*m.b15*m.b25*m.b26 + 576*m.b14*m.b15*m.b26*m.b27 + 512*m.b14*m.b15*m.b27*m.b28 + 448*
                       m.b14*m.b15*m.b28*m.b29 + 384*m.b14*m.b15*m.b29*m.b30 + 320*m.b14*m.b15*m.b30*m.b31 + 256*m.b14*
                       m.b15*m.b31*m.b32 + 192*m.b14*m.b15*m.b32*m.b33 + 128*m.b14*m.b15*m.b33*m.b34 + 64*m.b14*m.b15*
                       m.b34*m.b35 + 640*m.b14*m.b16*m.b17*m.b19 + 640*m.b14*m.b16*m.b18*m.b20 + 640*m.b14*m.b16*m.b19*
                       m.b21 + 896*m.b14*m.b16*m.b20*m.b22 + 832*m.b14*m.b16*m.b21*m.b23 + 768*m.b14*m.b16*m.b22*m.b24
                        + 704*m.b14*m.b16*m.b23*m.b25 + 640*m.b14*m.b16*m.b24*m.b26 + 576*m.b14*m.b16*m.b25*m.b27 + 512*
                       m.b14*m.b16*m.b26*m.b28 + 448*m.b14*m.b16*m.b27*m.b29 + 384*m.b14*m.b16*m.b28*m.b30 + 320*m.b14*
                       m.b16*m.b29*m.b31 + 256*m.b14*m.b16*m.b30*m.b32 + 192*m.b14*m.b16*m.b31*m.b33 + 128*m.b14*m.b16*
                       m.b32*m.b34 + 64*m.b14*m.b16*m.b33*m.b35 + 640*m.b14*m.b17*m.b18*m.b21 + 896*m.b14*m.b17*m.b19*
                       m.b22 + 832*m.b14*m.b17*m.b20*m.b23 + 768*m.b14*m.b17*m.b21*m.b24 + 704*m.b14*m.b17*m.b22*m.b25
                        + 640*m.b14*m.b17*m.b23*m.b26 + 576*m.b14*m.b17*m.b24*m.b27 + 512*m.b14*m.b17*m.b25*m.b28 + 448*
                       m.b14*m.b17*m.b26*m.b29 + 384*m.b14*m.b17*m.b27*m.b30 + 320*m.b14*m.b17*m.b28*m.b31 + 256*m.b14*
                       m.b17*m.b29*m.b32 + 192*m.b14*m.b17*m.b30*m.b33 + 128*m.b14*m.b17*m.b31*m.b34 + 64*m.b14*m.b17*
                       m.b32*m.b35 + 832*m.b14*m.b18*m.b19*m.b23 + 768*m.b14*m.b18*m.b20*m.b24 + 704*m.b14*m.b18*m.b21*
                       m.b25 + 640*m.b14*m.b18*m.b22*m.b26 + 576*m.b14*m.b18*m.b23*m.b27 + 512*m.b14*m.b18*m.b24*m.b28
                        + 448*m.b14*m.b18*m.b25*m.b29 + 384*m.b14*m.b18*m.b26*m.b30 + 320*m.b14*m.b18*m.b27*m.b31 + 256*
                       m.b14*m.b18*m.b28*m.b32 + 192*m.b14*m.b18*m.b29*m.b33 + 128*m.b14*m.b18*m.b30*m.b34 + 64*m.b14*
                       m.b18*m.b31*m.b35 + 704*m.b14*m.b19*m.b20*m.b25 + 640*m.b14*m.b19*m.b21*m.b26 + 576*m.b14*m.b19*
                       m.b22*m.b27 + 512*m.b14*m.b19*m.b23*m.b28 + 448*m.b14*m.b19*m.b24*m.b29 + 384*m.b14*m.b19*m.b25*
                       m.b30 + 320*m.b14*m.b19*m.b26*m.b31 + 256*m.b14*m.b19*m.b27*m.b32 + 192*m.b14*m.b19*m.b28*m.b33
                        + 128*m.b14*m.b19*m.b29*m.b34 + 64*m.b14*m.b19*m.b30*m.b35 + 576*m.b14*m.b20*m.b21*m.b27 + 512*
                       m.b14*m.b20*m.b22*m.b28 + 448*m.b14*m.b20*m.b23*m.b29 + 384*m.b14*m.b20*m.b24*m.b30 + 320*m.b14*
                       m.b20*m.b25*m.b31 + 256*m.b14*m.b20*m.b26*m.b32 + 192*m.b14*m.b20*m.b27*m.b33 + 128*m.b14*m.b20*
                       m.b28*m.b34 + 64*m.b14*m.b20*m.b29*m.b35 + 448*m.b14*m.b21*m.b22*m.b29 + 384*m.b14*m.b21*m.b23*
                       m.b30 + 320*m.b14*m.b21*m.b24*m.b31 + 256*m.b14*m.b21*m.b25*m.b32 + 192*m.b14*m.b21*m.b26*m.b33
                        + 128*m.b14*m.b21*m.b27*m.b34 + 64*m.b14*m.b21*m.b28*m.b35 + 320*m.b14*m.b22*m.b23*m.b31 + 256*
                       m.b14*m.b22*m.b24*m.b32 + 192*m.b14*m.b22*m.b25*m.b33 + 128*m.b14*m.b22*m.b26*m.b34 + 64*m.b14*
                       m.b22*m.b27*m.b35 + 192*m.b14*m.b23*m.b24*m.b33 + 128*m.b14*m.b23*m.b25*m.b34 + 64*m.b14*m.b23*
                       m.b26*m.b35 + 64*m.b14*m.b24*m.b25*m.b35 + 640*m.b15*m.b16*m.b17*m.b18 + 640*m.b15*m.b16*m.b18*
                       m.b19 + 640*m.b15*m.b16*m.b19*m.b20 + 640*m.b15*m.b16*m.b20*m.b21 + 640*m.b15*m.b16*m.b21*m.b22
                        + 832*m.b15*m.b16*m.b22*m.b23 + 768*m.b15*m.b16*m.b23*m.b24 + 704*m.b15*m.b16*m.b24*m.b25 + 640*
                       m.b15*m.b16*m.b25*m.b26 + 576*m.b15*m.b16*m.b26*m.b27 + 512*m.b15*m.b16*m.b27*m.b28 + 448*m.b15*
                       m.b16*m.b28*m.b29 + 384*m.b15*m.b16*m.b29*m.b30 + 320*m.b15*m.b16*m.b30*m.b31 + 256*m.b15*m.b16*
                       m.b31*m.b32 + 192*m.b15*m.b16*m.b32*m.b33 + 128*m.b15*m.b16*m.b33*m.b34 + 64*m.b15*m.b16*m.b34*
                       m.b35 + 640*m.b15*m.b17*m.b18*m.b20 + 640*m.b15*m.b17*m.b19*m.b21 + 640*m.b15*m.b17*m.b20*m.b22
                        + 832*m.b15*m.b17*m.b21*m.b23 + 768*m.b15*m.b17*m.b22*m.b24 + 704*m.b15*m.b17*m.b23*m.b25 + 640*
                       m.b15*m.b17*m.b24*m.b26 + 576*m.b15*m.b17*m.b25*m.b27 + 512*m.b15*m.b17*m.b26*m.b28 + 448*m.b15*
                       m.b17*m.b27*m.b29 + 384*m.b15*m.b17*m.b28*m.b30 + 320*m.b15*m.b17*m.b29*m.b31 + 256*m.b15*m.b17*
                       m.b30*m.b32 + 192*m.b15*m.b17*m.b31*m.b33 + 128*m.b15*m.b17*m.b32*m.b34 + 64*m.b15*m.b17*m.b33*
                       m.b35 + 640*m.b15*m.b18*m.b19*m.b22 + 832*m.b15*m.b18*m.b20*m.b23 + 768*m.b15*m.b18*m.b21*m.b24
                        + 704*m.b15*m.b18*m.b22*m.b25 + 640*m.b15*m.b18*m.b23*m.b26 + 576*m.b15*m.b18*m.b24*m.b27 + 512*
                       m.b15*m.b18*m.b25*m.b28 + 448*m.b15*m.b18*m.b26*m.b29 + 384*m.b15*m.b18*m.b27*m.b30 + 320*m.b15*
                       m.b18*m.b28*m.b31 + 256*m.b15*m.b18*m.b29*m.b32 + 192*m.b15*m.b18*m.b30*m.b33 + 128*m.b15*m.b18*
                       m.b31*m.b34 + 64*m.b15*m.b18*m.b32*m.b35 + 768*m.b15*m.b19*m.b20*m.b24 + 704*m.b15*m.b19*m.b21*
                       m.b25 + 640*m.b15*m.b19*m.b22*m.b26 + 576*m.b15*m.b19*m.b23*m.b27 + 512*m.b15*m.b19*m.b24*m.b28
                        + 448*m.b15*m.b19*m.b25*m.b29 + 384*m.b15*m.b19*m.b26*m.b30 + 320*m.b15*m.b19*m.b27*m.b31 + 256*
                       m.b15*m.b19*m.b28*m.b32 + 192*m.b15*m.b19*m.b29*m.b33 + 128*m.b15*m.b19*m.b30*m.b34 + 64*m.b15*
                       m.b19*m.b31*m.b35 + 640*m.b15*m.b20*m.b21*m.b26 + 576*m.b15*m.b20*m.b22*m.b27 + 512*m.b15*m.b20*
                       m.b23*m.b28 + 448*m.b15*m.b20*m.b24*m.b29 + 384*m.b15*m.b20*m.b25*m.b30 + 320*m.b15*m.b20*m.b26*
                       m.b31 + 256*m.b15*m.b20*m.b27*m.b32 + 192*m.b15*m.b20*m.b28*m.b33 + 128*m.b15*m.b20*m.b29*m.b34
                        + 64*m.b15*m.b20*m.b30*m.b35 + 512*m.b15*m.b21*m.b22*m.b28 + 448*m.b15*m.b21*m.b23*m.b29 + 384*
                       m.b15*m.b21*m.b24*m.b30 + 320*m.b15*m.b21*m.b25*m.b31 + 256*m.b15*m.b21*m.b26*m.b32 + 192*m.b15*
                       m.b21*m.b27*m.b33 + 128*m.b15*m.b21*m.b28*m.b34 + 64*m.b15*m.b21*m.b29*m.b35 + 384*m.b15*m.b22*
                       m.b23*m.b30 + 320*m.b15*m.b22*m.b24*m.b31 + 256*m.b15*m.b22*m.b25*m.b32 + 192*m.b15*m.b22*m.b26*
                       m.b33 + 128*m.b15*m.b22*m.b27*m.b34 + 64*m.b15*m.b22*m.b28*m.b35 + 256*m.b15*m.b23*m.b24*m.b32 + 
                       192*m.b15*m.b23*m.b25*m.b33 + 128*m.b15*m.b23*m.b26*m.b34 + 64*m.b15*m.b23*m.b27*m.b35 + 128*
                       m.b15*m.b24*m.b25*m.b34 + 64*m.b15*m.b24*m.b26*m.b35 + 640*m.b16*m.b17*m.b18*m.b19 + 640*m.b16*
                       m.b17*m.b19*m.b20 + 640*m.b16*m.b17*m.b20*m.b21 + 640*m.b16*m.b17*m.b21*m.b22 + 640*m.b16*m.b17*
                       m.b22*m.b23 + 768*m.b16*m.b17*m.b23*m.b24 + 704*m.b16*m.b17*m.b24*m.b25 + 640*m.b16*m.b17*m.b25*
                       m.b26 + 576*m.b16*m.b17*m.b26*m.b27 + 512*m.b16*m.b17*m.b27*m.b28 + 448*m.b16*m.b17*m.b28*m.b29
                        + 384*m.b16*m.b17*m.b29*m.b30 + 320*m.b16*m.b17*m.b30*m.b31 + 256*m.b16*m.b17*m.b31*m.b32 + 192*
                       m.b16*m.b17*m.b32*m.b33 + 128*m.b16*m.b17*m.b33*m.b34 + 64*m.b16*m.b17*m.b34*m.b35 + 640*m.b16*
                       m.b18*m.b19*m.b21 + 640*m.b16*m.b18*m.b20*m.b22 + 640*m.b16*m.b18*m.b21*m.b23 + 768*m.b16*m.b18*
                       m.b22*m.b24 + 704*m.b16*m.b18*m.b23*m.b25 + 640*m.b16*m.b18*m.b24*m.b26 + 576*m.b16*m.b18*m.b25*
                       m.b27 + 512*m.b16*m.b18*m.b26*m.b28 + 448*m.b16*m.b18*m.b27*m.b29 + 384*m.b16*m.b18*m.b28*m.b30
                        + 320*m.b16*m.b18*m.b29*m.b31 + 256*m.b16*m.b18*m.b30*m.b32 + 192*m.b16*m.b18*m.b31*m.b33 + 128*
                       m.b16*m.b18*m.b32*m.b34 + 64*m.b16*m.b18*m.b33*m.b35 + 640*m.b16*m.b19*m.b20*m.b23 + 768*m.b16*
                       m.b19*m.b21*m.b24 + 704*m.b16*m.b19*m.b22*m.b25 + 640*m.b16*m.b19*m.b23*m.b26 + 576*m.b16*m.b19*
                       m.b24*m.b27 + 512*m.b16*m.b19*m.b25*m.b28 + 448*m.b16*m.b19*m.b26*m.b29 + 384*m.b16*m.b19*m.b27*
                       m.b30 + 320*m.b16*m.b19*m.b28*m.b31 + 256*m.b16*m.b19*m.b29*m.b32 + 192*m.b16*m.b19*m.b30*m.b33
                        + 128*m.b16*m.b19*m.b31*m.b34 + 64*m.b16*m.b19*m.b32*m.b35 + 704*m.b16*m.b20*m.b21*m.b25 + 640*
                       m.b16*m.b20*m.b22*m.b26 + 576*m.b16*m.b20*m.b23*m.b27 + 512*m.b16*m.b20*m.b24*m.b28 + 448*m.b16*
                       m.b20*m.b25*m.b29 + 384*m.b16*m.b20*m.b26*m.b30 + 320*m.b16*m.b20*m.b27*m.b31 + 256*m.b16*m.b20*
                       m.b28*m.b32 + 192*m.b16*m.b20*m.b29*m.b33 + 128*m.b16*m.b20*m.b30*m.b34 + 64*m.b16*m.b20*m.b31*
                       m.b35 + 576*m.b16*m.b21*m.b22*m.b27 + 512*m.b16*m.b21*m.b23*m.b28 + 448*m.b16*m.b21*m.b24*m.b29
                        + 384*m.b16*m.b21*m.b25*m.b30 + 320*m.b16*m.b21*m.b26*m.b31 + 256*m.b16*m.b21*m.b27*m.b32 + 192*
                       m.b16*m.b21*m.b28*m.b33 + 128*m.b16*m.b21*m.b29*m.b34 + 64*m.b16*m.b21*m.b30*m.b35 + 448*m.b16*
                       m.b22*m.b23*m.b29 + 384*m.b16*m.b22*m.b24*m.b30 + 320*m.b16*m.b22*m.b25*m.b31 + 256*m.b16*m.b22*
                       m.b26*m.b32 + 192*m.b16*m.b22*m.b27*m.b33 + 128*m.b16*m.b22*m.b28*m.b34 + 64*m.b16*m.b22*m.b29*
                       m.b35 + 320*m.b16*m.b23*m.b24*m.b31 + 256*m.b16*m.b23*m.b25*m.b32 + 192*m.b16*m.b23*m.b26*m.b33
                        + 128*m.b16*m.b23*m.b27*m.b34 + 64*m.b16*m.b23*m.b28*m.b35 + 192*m.b16*m.b24*m.b25*m.b33 + 128*
                       m.b16*m.b24*m.b26*m.b34 + 64*m.b16*m.b24*m.b27*m.b35 + 64*m.b16*m.b25*m.b26*m.b35 + 640*m.b17*
                       m.b18*m.b19*m.b20 + 640*m.b17*m.b18*m.b20*m.b21 + 640*m.b17*m.b18*m.b21*m.b22 + 640*m.b17*m.b18*
                       m.b22*m.b23 + 640*m.b17*m.b18*m.b23*m.b24 + 704*m.b17*m.b18*m.b24*m.b25 + 640*m.b17*m.b18*m.b25*
                       m.b26 + 576*m.b17*m.b18*m.b26*m.b27 + 512*m.b17*m.b18*m.b27*m.b28 + 448*m.b17*m.b18*m.b28*m.b29
                        + 384*m.b17*m.b18*m.b29*m.b30 + 320*m.b17*m.b18*m.b30*m.b31 + 256*m.b17*m.b18*m.b31*m.b32 + 192*
                       m.b17*m.b18*m.b32*m.b33 + 128*m.b17*m.b18*m.b33*m.b34 + 64*m.b17*m.b18*m.b34*m.b35 + 640*m.b17*
                       m.b19*m.b20*m.b22 + 640*m.b17*m.b19*m.b21*m.b23 + 640*m.b17*m.b19*m.b22*m.b24 + 704*m.b17*m.b19*
                       m.b23*m.b25 + 640*m.b17*m.b19*m.b24*m.b26 + 576*m.b17*m.b19*m.b25*m.b27 + 512*m.b17*m.b19*m.b26*
                       m.b28 + 448*m.b17*m.b19*m.b27*m.b29 + 384*m.b17*m.b19*m.b28*m.b30 + 320*m.b17*m.b19*m.b29*m.b31
                        + 256*m.b17*m.b19*m.b30*m.b32 + 192*m.b17*m.b19*m.b31*m.b33 + 128*m.b17*m.b19*m.b32*m.b34 + 64*
                       m.b17*m.b19*m.b33*m.b35 + 640*m.b17*m.b20*m.b21*m.b24 + 704*m.b17*m.b20*m.b22*m.b25 + 640*m.b17*
                       m.b20*m.b23*m.b26 + 576*m.b17*m.b20*m.b24*m.b27 + 512*m.b17*m.b20*m.b25*m.b28 + 448*m.b17*m.b20*
                       m.b26*m.b29 + 384*m.b17*m.b20*m.b27*m.b30 + 320*m.b17*m.b20*m.b28*m.b31 + 256*m.b17*m.b20*m.b29*
                       m.b32 + 192*m.b17*m.b20*m.b30*m.b33 + 128*m.b17*m.b20*m.b31*m.b34 + 64*m.b17*m.b20*m.b32*m.b35 + 
                       640*m.b17*m.b21*m.b22*m.b26 + 576*m.b17*m.b21*m.b23*m.b27 + 512*m.b17*m.b21*m.b24*m.b28 + 448*
                       m.b17*m.b21*m.b25*m.b29 + 384*m.b17*m.b21*m.b26*m.b30 + 320*m.b17*m.b21*m.b27*m.b31 + 256*m.b17*
                       m.b21*m.b28*m.b32 + 192*m.b17*m.b21*m.b29*m.b33 + 128*m.b17*m.b21*m.b30*m.b34 + 64*m.b17*m.b21*
                       m.b31*m.b35 + 512*m.b17*m.b22*m.b23*m.b28 + 448*m.b17*m.b22*m.b24*m.b29 + 384*m.b17*m.b22*m.b25*
                       m.b30 + 320*m.b17*m.b22*m.b26*m.b31 + 256*m.b17*m.b22*m.b27*m.b32 + 192*m.b17*m.b22*m.b28*m.b33
                        + 128*m.b17*m.b22*m.b29*m.b34 + 64*m.b17*m.b22*m.b30*m.b35 + 384*m.b17*m.b23*m.b24*m.b30 + 320*
                       m.b17*m.b23*m.b25*m.b31 + 256*m.b17*m.b23*m.b26*m.b32 + 192*m.b17*m.b23*m.b27*m.b33 + 128*m.b17*
                       m.b23*m.b28*m.b34 + 64*m.b17*m.b23*m.b29*m.b35 + 256*m.b17*m.b24*m.b25*m.b32 + 192*m.b17*m.b24*
                       m.b26*m.b33 + 128*m.b17*m.b24*m.b27*m.b34 + 64*m.b17*m.b24*m.b28*m.b35 + 128*m.b17*m.b25*m.b26*
                       m.b34 + 64*m.b17*m.b25*m.b27*m.b35 + 640*m.b18*m.b19*m.b20*m.b21 + 640*m.b18*m.b19*m.b21*m.b22 + 
                       640*m.b18*m.b19*m.b22*m.b23 + 640*m.b18*m.b19*m.b23*m.b24 + 640*m.b18*m.b19*m.b24*m.b25 + 640*
                       m.b18*m.b19*m.b25*m.b26 + 576*m.b18*m.b19*m.b26*m.b27 + 512*m.b18*m.b19*m.b27*m.b28 + 448*m.b18*
                       m.b19*m.b28*m.b29 + 384*m.b18*m.b19*m.b29*m.b30 + 320*m.b18*m.b19*m.b30*m.b31 + 256*m.b18*m.b19*
                       m.b31*m.b32 + 192*m.b18*m.b19*m.b32*m.b33 + 128*m.b18*m.b19*m.b33*m.b34 + 64*m.b18*m.b19*m.b34*
                       m.b35 + 640*m.b18*m.b20*m.b21*m.b23 + 640*m.b18*m.b20*m.b22*m.b24 + 640*m.b18*m.b20*m.b23*m.b25
                        + 640*m.b18*m.b20*m.b24*m.b26 + 576*m.b18*m.b20*m.b25*m.b27 + 512*m.b18*m.b20*m.b26*m.b28 + 448*
                       m.b18*m.b20*m.b27*m.b29 + 384*m.b18*m.b20*m.b28*m.b30 + 320*m.b18*m.b20*m.b29*m.b31 + 256*m.b18*
                       m.b20*m.b30*m.b32 + 192*m.b18*m.b20*m.b31*m.b33 + 128*m.b18*m.b20*m.b32*m.b34 + 64*m.b18*m.b20*
                       m.b33*m.b35 + 640*m.b18*m.b21*m.b22*m.b25 + 640*m.b18*m.b21*m.b23*m.b26 + 576*m.b18*m.b21*m.b24*
                       m.b27 + 512*m.b18*m.b21*m.b25*m.b28 + 448*m.b18*m.b21*m.b26*m.b29 + 384*m.b18*m.b21*m.b27*m.b30
                        + 320*m.b18*m.b21*m.b28*m.b31 + 256*m.b18*m.b21*m.b29*m.b32 + 192*m.b18*m.b21*m.b30*m.b33 + 128*
                       m.b18*m.b21*m.b31*m.b34 + 64*m.b18*m.b21*m.b32*m.b35 + 576*m.b18*m.b22*m.b23*m.b27 + 512*m.b18*
                       m.b22*m.b24*m.b28 + 448*m.b18*m.b22*m.b25*m.b29 + 384*m.b18*m.b22*m.b26*m.b30 + 320*m.b18*m.b22*
                       m.b27*m.b31 + 256*m.b18*m.b22*m.b28*m.b32 + 192*m.b18*m.b22*m.b29*m.b33 + 128*m.b18*m.b22*m.b30*
                       m.b34 + 64*m.b18*m.b22*m.b31*m.b35 + 448*m.b18*m.b23*m.b24*m.b29 + 384*m.b18*m.b23*m.b25*m.b30 + 
                       320*m.b18*m.b23*m.b26*m.b31 + 256*m.b18*m.b23*m.b27*m.b32 + 192*m.b18*m.b23*m.b28*m.b33 + 128*
                       m.b18*m.b23*m.b29*m.b34 + 64*m.b18*m.b23*m.b30*m.b35 + 320*m.b18*m.b24*m.b25*m.b31 + 256*m.b18*
                       m.b24*m.b26*m.b32 + 192*m.b18*m.b24*m.b27*m.b33 + 128*m.b18*m.b24*m.b28*m.b34 + 64*m.b18*m.b24*
                       m.b29*m.b35 + 192*m.b18*m.b25*m.b26*m.b33 + 128*m.b18*m.b25*m.b27*m.b34 + 64*m.b18*m.b25*m.b28*
                       m.b35 + 64*m.b18*m.b26*m.b27*m.b35 + 640*m.b19*m.b20*m.b21*m.b22 + 640*m.b19*m.b20*m.b22*m.b23 + 
                       640*m.b19*m.b20*m.b23*m.b24 + 640*m.b19*m.b20*m.b24*m.b25 + 640*m.b19*m.b20*m.b25*m.b26 + 576*
                       m.b19*m.b20*m.b26*m.b27 + 512*m.b19*m.b20*m.b27*m.b28 + 448*m.b19*m.b20*m.b28*m.b29 + 384*m.b19*
                       m.b20*m.b29*m.b30 + 320*m.b19*m.b20*m.b30*m.b31 + 256*m.b19*m.b20*m.b31*m.b32 + 192*m.b19*m.b20*
                       m.b32*m.b33 + 128*m.b19*m.b20*m.b33*m.b34 + 64*m.b19*m.b20*m.b34*m.b35 + 640*m.b19*m.b21*m.b22*
                       m.b24 + 640*m.b19*m.b21*m.b23*m.b25 + 640*m.b19*m.b21*m.b24*m.b26 + 576*m.b19*m.b21*m.b25*m.b27
                        + 512*m.b19*m.b21*m.b26*m.b28 + 448*m.b19*m.b21*m.b27*m.b29 + 384*m.b19*m.b21*m.b28*m.b30 + 320*
                       m.b19*m.b21*m.b29*m.b31 + 256*m.b19*m.b21*m.b30*m.b32 + 192*m.b19*m.b21*m.b31*m.b33 + 128*m.b19*
                       m.b21*m.b32*m.b34 + 64*m.b19*m.b21*m.b33*m.b35 + 640*m.b19*m.b22*m.b23*m.b26 + 576*m.b19*m.b22*
                       m.b24*m.b27 + 512*m.b19*m.b22*m.b25*m.b28 + 448*m.b19*m.b22*m.b26*m.b29 + 384*m.b19*m.b22*m.b27*
                       m.b30 + 320*m.b19*m.b22*m.b28*m.b31 + 256*m.b19*m.b22*m.b29*m.b32 + 192*m.b19*m.b22*m.b30*m.b33
                        + 128*m.b19*m.b22*m.b31*m.b34 + 64*m.b19*m.b22*m.b32*m.b35 + 512*m.b19*m.b23*m.b24*m.b28 + 448*
                       m.b19*m.b23*m.b25*m.b29 + 384*m.b19*m.b23*m.b26*m.b30 + 320*m.b19*m.b23*m.b27*m.b31 + 256*m.b19*
                       m.b23*m.b28*m.b32 + 192*m.b19*m.b23*m.b29*m.b33 + 128*m.b19*m.b23*m.b30*m.b34 + 64*m.b19*m.b23*
                       m.b31*m.b35 + 384*m.b19*m.b24*m.b25*m.b30 + 320*m.b19*m.b24*m.b26*m.b31 + 256*m.b19*m.b24*m.b27*
                       m.b32 + 192*m.b19*m.b24*m.b28*m.b33 + 128*m.b19*m.b24*m.b29*m.b34 + 64*m.b19*m.b24*m.b30*m.b35 + 
                       256*m.b19*m.b25*m.b26*m.b32 + 192*m.b19*m.b25*m.b27*m.b33 + 128*m.b19*m.b25*m.b28*m.b34 + 64*
                       m.b19*m.b25*m.b29*m.b35 + 128*m.b19*m.b26*m.b27*m.b34 + 64*m.b19*m.b26*m.b28*m.b35 + 640*m.b20*
                       m.b21*m.b22*m.b23 + 640*m.b20*m.b21*m.b23*m.b24 + 640*m.b20*m.b21*m.b24*m.b25 + 640*m.b20*m.b21*
                       m.b25*m.b26 + 576*m.b20*m.b21*m.b26*m.b27 + 512*m.b20*m.b21*m.b27*m.b28 + 448*m.b20*m.b21*m.b28*
                       m.b29 + 384*m.b20*m.b21*m.b29*m.b30 + 320*m.b20*m.b21*m.b30*m.b31 + 256*m.b20*m.b21*m.b31*m.b32
                        + 192*m.b20*m.b21*m.b32*m.b33 + 128*m.b20*m.b21*m.b33*m.b34 + 64*m.b20*m.b21*m.b34*m.b35 + 640*
                       m.b20*m.b22*m.b23*m.b25 + 640*m.b20*m.b22*m.b24*m.b26 + 576*m.b20*m.b22*m.b25*m.b27 + 512*m.b20*
                       m.b22*m.b26*m.b28 + 448*m.b20*m.b22*m.b27*m.b29 + 384*m.b20*m.b22*m.b28*m.b30 + 320*m.b20*m.b22*
                       m.b29*m.b31 + 256*m.b20*m.b22*m.b30*m.b32 + 192*m.b20*m.b22*m.b31*m.b33 + 128*m.b20*m.b22*m.b32*
                       m.b34 + 64*m.b20*m.b22*m.b33*m.b35 + 576*m.b20*m.b23*m.b24*m.b27 + 512*m.b20*m.b23*m.b25*m.b28 + 
                       448*m.b20*m.b23*m.b26*m.b29 + 384*m.b20*m.b23*m.b27*m.b30 + 320*m.b20*m.b23*m.b28*m.b31 + 256*
                       m.b20*m.b23*m.b29*m.b32 + 192*m.b20*m.b23*m.b30*m.b33 + 128*m.b20*m.b23*m.b31*m.b34 + 64*m.b20*
                       m.b23*m.b32*m.b35 + 448*m.b20*m.b24*m.b25*m.b29 + 384*m.b20*m.b24*m.b26*m.b30 + 320*m.b20*m.b24*
                       m.b27*m.b31 + 256*m.b20*m.b24*m.b28*m.b32 + 192*m.b20*m.b24*m.b29*m.b33 + 128*m.b20*m.b24*m.b30*
                       m.b34 + 64*m.b20*m.b24*m.b31*m.b35 + 320*m.b20*m.b25*m.b26*m.b31 + 256*m.b20*m.b25*m.b27*m.b32 + 
                       192*m.b20*m.b25*m.b28*m.b33 + 128*m.b20*m.b25*m.b29*m.b34 + 64*m.b20*m.b25*m.b30*m.b35 + 192*
                       m.b20*m.b26*m.b27*m.b33 + 128*m.b20*m.b26*m.b28*m.b34 + 64*m.b20*m.b26*m.b29*m.b35 + 64*m.b20*
                       m.b27*m.b28*m.b35 + 640*m.b21*m.b22*m.b23*m.b24 + 640*m.b21*m.b22*m.b24*m.b25 + 640*m.b21*m.b22*
                       m.b25*m.b26 + 576*m.b21*m.b22*m.b26*m.b27 + 512*m.b21*m.b22*m.b27*m.b28 + 448*m.b21*m.b22*m.b28*
                       m.b29 + 384*m.b21*m.b22*m.b29*m.b30 + 320*m.b21*m.b22*m.b30*m.b31 + 256*m.b21*m.b22*m.b31*m.b32
                        + 192*m.b21*m.b22*m.b32*m.b33 + 128*m.b21*m.b22*m.b33*m.b34 + 64*m.b21*m.b22*m.b34*m.b35 + 640*
                       m.b21*m.b23*m.b24*m.b26 + 576*m.b21*m.b23*m.b25*m.b27 + 512*m.b21*m.b23*m.b26*m.b28 + 448*m.b21*
                       m.b23*m.b27*m.b29 + 384*m.b21*m.b23*m.b28*m.b30 + 320*m.b21*m.b23*m.b29*m.b31 + 256*m.b21*m.b23*
                       m.b30*m.b32 + 192*m.b21*m.b23*m.b31*m.b33 + 128*m.b21*m.b23*m.b32*m.b34 + 64*m.b21*m.b23*m.b33*
                       m.b35 + 512*m.b21*m.b24*m.b25*m.b28 + 448*m.b21*m.b24*m.b26*m.b29 + 384*m.b21*m.b24*m.b27*m.b30
                        + 320*m.b21*m.b24*m.b28*m.b31 + 256*m.b21*m.b24*m.b29*m.b32 + 192*m.b21*m.b24*m.b30*m.b33 + 128*
                       m.b21*m.b24*m.b31*m.b34 + 64*m.b21*m.b24*m.b32*m.b35 + 384*m.b21*m.b25*m.b26*m.b30 + 320*m.b21*
                       m.b25*m.b27*m.b31 + 256*m.b21*m.b25*m.b28*m.b32 + 192*m.b21*m.b25*m.b29*m.b33 + 128*m.b21*m.b25*
                       m.b30*m.b34 + 64*m.b21*m.b25*m.b31*m.b35 + 256*m.b21*m.b26*m.b27*m.b32 + 192*m.b21*m.b26*m.b28*
                       m.b33 + 128*m.b21*m.b26*m.b29*m.b34 + 64*m.b21*m.b26*m.b30*m.b35 + 128*m.b21*m.b27*m.b28*m.b34 + 
                       64*m.b21*m.b27*m.b29*m.b35 + 640*m.b22*m.b23*m.b24*m.b25 + 640*m.b22*m.b23*m.b25*m.b26 + 576*
                       m.b22*m.b23*m.b26*m.b27 + 512*m.b22*m.b23*m.b27*m.b28 + 448*m.b22*m.b23*m.b28*m.b29 + 384*m.b22*
                       m.b23*m.b29*m.b30 + 320*m.b22*m.b23*m.b30*m.b31 + 256*m.b22*m.b23*m.b31*m.b32 + 192*m.b22*m.b23*
                       m.b32*m.b33 + 128*m.b22*m.b23*m.b33*m.b34 + 64*m.b22*m.b23*m.b34*m.b35 + 576*m.b22*m.b24*m.b25*
                       m.b27 + 512*m.b22*m.b24*m.b26*m.b28 + 448*m.b22*m.b24*m.b27*m.b29 + 384*m.b22*m.b24*m.b28*m.b30
                        + 320*m.b22*m.b24*m.b29*m.b31 + 256*m.b22*m.b24*m.b30*m.b32 + 192*m.b22*m.b24*m.b31*m.b33 + 128*
                       m.b22*m.b24*m.b32*m.b34 + 64*m.b22*m.b24*m.b33*m.b35 + 448*m.b22*m.b25*m.b26*m.b29 + 384*m.b22*
                       m.b25*m.b27*m.b30 + 320*m.b22*m.b25*m.b28*m.b31 + 256*m.b22*m.b25*m.b29*m.b32 + 192*m.b22*m.b25*
                       m.b30*m.b33 + 128*m.b22*m.b25*m.b31*m.b34 + 64*m.b22*m.b25*m.b32*m.b35 + 320*m.b22*m.b26*m.b27*
                       m.b31 + 256*m.b22*m.b26*m.b28*m.b32 + 192*m.b22*m.b26*m.b29*m.b33 + 128*m.b22*m.b26*m.b30*m.b34
                        + 64*m.b22*m.b26*m.b31*m.b35 + 192*m.b22*m.b27*m.b28*m.b33 + 128*m.b22*m.b27*m.b29*m.b34 + 64*
                       m.b22*m.b27*m.b30*m.b35 + 64*m.b22*m.b28*m.b29*m.b35 + 640*m.b23*m.b24*m.b25*m.b26 + 576*m.b23*
                       m.b24*m.b26*m.b27 + 512*m.b23*m.b24*m.b27*m.b28 + 448*m.b23*m.b24*m.b28*m.b29 + 384*m.b23*m.b24*
                       m.b29*m.b30 + 320*m.b23*m.b24*m.b30*m.b31 + 256*m.b23*m.b24*m.b31*m.b32 + 192*m.b23*m.b24*m.b32*
                       m.b33 + 128*m.b23*m.b24*m.b33*m.b34 + 64*m.b23*m.b24*m.b34*m.b35 + 512*m.b23*m.b25*m.b26*m.b28 + 
                       448*m.b23*m.b25*m.b27*m.b29 + 384*m.b23*m.b25*m.b28*m.b30 + 320*m.b23*m.b25*m.b29*m.b31 + 256*
                       m.b23*m.b25*m.b30*m.b32 + 192*m.b23*m.b25*m.b31*m.b33 + 128*m.b23*m.b25*m.b32*m.b34 + 64*m.b23*
                       m.b25*m.b33*m.b35 + 384*m.b23*m.b26*m.b27*m.b30 + 320*m.b23*m.b26*m.b28*m.b31 + 256*m.b23*m.b26*
                       m.b29*m.b32 + 192*m.b23*m.b26*m.b30*m.b33 + 128*m.b23*m.b26*m.b31*m.b34 + 64*m.b23*m.b26*m.b32*
                       m.b35 + 256*m.b23*m.b27*m.b28*m.b32 + 192*m.b23*m.b27*m.b29*m.b33 + 128*m.b23*m.b27*m.b30*m.b34
                        + 64*m.b23*m.b27*m.b31*m.b35 + 128*m.b23*m.b28*m.b29*m.b34 + 64*m.b23*m.b28*m.b30*m.b35 + 576*
                       m.b24*m.b25*m.b26*m.b27 + 512*m.b24*m.b25*m.b27*m.b28 + 448*m.b24*m.b25*m.b28*m.b29 + 384*m.b24*
                       m.b25*m.b29*m.b30 + 320*m.b24*m.b25*m.b30*m.b31 + 256*m.b24*m.b25*m.b31*m.b32 + 192*m.b24*m.b25*
                       m.b32*m.b33 + 128*m.b24*m.b25*m.b33*m.b34 + 64*m.b24*m.b25*m.b34*m.b35 + 448*m.b24*m.b26*m.b27*
                       m.b29 + 384*m.b24*m.b26*m.b28*m.b30 + 320*m.b24*m.b26*m.b29*m.b31 + 256*m.b24*m.b26*m.b30*m.b32
                        + 192*m.b24*m.b26*m.b31*m.b33 + 128*m.b24*m.b26*m.b32*m.b34 + 64*m.b24*m.b26*m.b33*m.b35 + 320*
                       m.b24*m.b27*m.b28*m.b31 + 256*m.b24*m.b27*m.b29*m.b32 + 192*m.b24*m.b27*m.b30*m.b33 + 128*m.b24*
                       m.b27*m.b31*m.b34 + 64*m.b24*m.b27*m.b32*m.b35 + 192*m.b24*m.b28*m.b29*m.b33 + 128*m.b24*m.b28*
                       m.b30*m.b34 + 64*m.b24*m.b28*m.b31*m.b35 + 64*m.b24*m.b29*m.b30*m.b35 + 512*m.b25*m.b26*m.b27*
                       m.b28 + 448*m.b25*m.b26*m.b28*m.b29 + 384*m.b25*m.b26*m.b29*m.b30 + 320*m.b25*m.b26*m.b30*m.b31
                        + 256*m.b25*m.b26*m.b31*m.b32 + 192*m.b25*m.b26*m.b32*m.b33 + 128*m.b25*m.b26*m.b33*m.b34 + 64*
                       m.b25*m.b26*m.b34*m.b35 + 384*m.b25*m.b27*m.b28*m.b30 + 320*m.b25*m.b27*m.b29*m.b31 + 256*m.b25*
                       m.b27*m.b30*m.b32 + 192*m.b25*m.b27*m.b31*m.b33 + 128*m.b25*m.b27*m.b32*m.b34 + 64*m.b25*m.b27*
                       m.b33*m.b35 + 256*m.b25*m.b28*m.b29*m.b32 + 192*m.b25*m.b28*m.b30*m.b33 + 128*m.b25*m.b28*m.b31*
                       m.b34 + 64*m.b25*m.b28*m.b32*m.b35 + 128*m.b25*m.b29*m.b30*m.b34 + 64*m.b25*m.b29*m.b31*m.b35 + 
                       448*m.b26*m.b27*m.b28*m.b29 + 384*m.b26*m.b27*m.b29*m.b30 + 320*m.b26*m.b27*m.b30*m.b31 + 256*
                       m.b26*m.b27*m.b31*m.b32 + 192*m.b26*m.b27*m.b32*m.b33 + 128*m.b26*m.b27*m.b33*m.b34 + 64*m.b26*
                       m.b27*m.b34*m.b35 + 320*m.b26*m.b28*m.b29*m.b31 + 256*m.b26*m.b28*m.b30*m.b32 + 192*m.b26*m.b28*
                       m.b31*m.b33 + 128*m.b26*m.b28*m.b32*m.b34 + 64*m.b26*m.b28*m.b33*m.b35 + 192*m.b26*m.b29*m.b30*
                       m.b33 + 128*m.b26*m.b29*m.b31*m.b34 + 64*m.b26*m.b29*m.b32*m.b35 + 64*m.b26*m.b30*m.b31*m.b35 + 
                       384*m.b27*m.b28*m.b29*m.b30 + 320*m.b27*m.b28*m.b30*m.b31 + 256*m.b27*m.b28*m.b31*m.b32 + 192*
                       m.b27*m.b28*m.b32*m.b33 + 128*m.b27*m.b28*m.b33*m.b34 + 64*m.b27*m.b28*m.b34*m.b35 + 256*m.b27*
                       m.b29*m.b30*m.b32 + 192*m.b27*m.b29*m.b31*m.b33 + 128*m.b27*m.b29*m.b32*m.b34 + 64*m.b27*m.b29*
                       m.b33*m.b35 + 128*m.b27*m.b30*m.b31*m.b34 + 64*m.b27*m.b30*m.b32*m.b35 + 320*m.b28*m.b29*m.b30*
                       m.b31 + 256*m.b28*m.b29*m.b31*m.b32 + 192*m.b28*m.b29*m.b32*m.b33 + 128*m.b28*m.b29*m.b33*m.b34
                        + 64*m.b28*m.b29*m.b34*m.b35 + 192*m.b28*m.b30*m.b31*m.b33 + 128*m.b28*m.b30*m.b32*m.b34 + 64*
                       m.b28*m.b30*m.b33*m.b35 + 64*m.b28*m.b31*m.b32*m.b35 + 256*m.b29*m.b30*m.b31*m.b32 + 192*m.b29*
                       m.b30*m.b32*m.b33 + 128*m.b29*m.b30*m.b33*m.b34 + 64*m.b29*m.b30*m.b34*m.b35 + 128*m.b29*m.b31*
                       m.b32*m.b34 + 64*m.b29*m.b31*m.b33*m.b35 + 192*m.b30*m.b31*m.b32*m.b33 + 128*m.b30*m.b31*m.b33*
                       m.b34 + 64*m.b30*m.b31*m.b34*m.b35 + 64*m.b30*m.b32*m.b33*m.b35 + 128*m.b31*m.b32*m.b33*m.b34 + 
                       64*m.b31*m.b32*m.b34*m.b35 + 64*m.b32*m.b33*m.b34*m.b35 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4
                        - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*m.b8 - 64*m.b1*m.b2*
                       m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1*m.b2*m.b13 - 64*
                       m.b1*m.b2*m.b14 - 64*m.b1*m.b2*m.b15 - 64*m.b1*m.b2*m.b16 - 64*m.b1*m.b2*m.b17 - 64*m.b1*m.b2*
                       m.b18 - 64*m.b1*m.b2*m.b19 - 64*m.b1*m.b2*m.b20 - 64*m.b1*m.b2*m.b21 - 64*m.b1*m.b2*m.b22 - 64*
                       m.b1*m.b2*m.b23 - 64*m.b1*m.b2*m.b24 - 64*m.b1*m.b2*m.b25 - 32*m.b1*m.b2*m.b26 - 64*m.b1*m.b3*
                       m.b4 - 32*m.b1*m.b3*m.b5 - 64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*
                       m.b3*m.b9 - 64*m.b1*m.b3*m.b10 - 64*m.b1*m.b3*m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 
                       64*m.b1*m.b3*m.b14 - 64*m.b1*m.b3*m.b15 - 64*m.b1*m.b3*m.b16 - 64*m.b1*m.b3*m.b17 - 64*m.b1*m.b3*
                       m.b18 - 64*m.b1*m.b3*m.b19 - 64*m.b1*m.b3*m.b20 - 64*m.b1*m.b3*m.b21 - 64*m.b1*m.b3*m.b22 - 64*
                       m.b1*m.b3*m.b23 - 64*m.b1*m.b3*m.b24 - 32*m.b1*m.b3*m.b25 - 32*m.b1*m.b3*m.b26 - 64*m.b1*m.b4*
                       m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8 - 64*m.b1*m.b4*m.b9 - 64*m.b1*
                       m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64*m.b1*m.b4*m.b12 - 64*m.b1*m.b4*m.b13 - 64*m.b1*m.b4*m.b14 - 
                       64*m.b1*m.b4*m.b15 - 64*m.b1*m.b4*m.b16 - 64*m.b1*m.b4*m.b17 - 64*m.b1*m.b4*m.b18 - 64*m.b1*m.b4*
                       m.b19 - 64*m.b1*m.b4*m.b20 - 64*m.b1*m.b4*m.b21 - 64*m.b1*m.b4*m.b22 - 64*m.b1*m.b4*m.b23 - 32*
                       m.b1*m.b4*m.b24 - 32*m.b1*m.b4*m.b25 - 32*m.b1*m.b4*m.b26 - 64*m.b1*m.b5*m.b6 - 64*m.b1*m.b5*m.b7
                        - 64*m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*m.b11 - 64*m.b1*m.b5
                       *m.b12 - 64*m.b1*m.b5*m.b13 - 64*m.b1*m.b5*m.b14 - 64*m.b1*m.b5*m.b15 - 64*m.b1*m.b5*m.b16 - 64*
                       m.b1*m.b5*m.b17 - 64*m.b1*m.b5*m.b18 - 64*m.b1*m.b5*m.b19 - 64*m.b1*m.b5*m.b20 - 64*m.b1*m.b5*
                       m.b21 - 64*m.b1*m.b5*m.b22 - 32*m.b1*m.b5*m.b23 - 32*m.b1*m.b5*m.b24 - 32*m.b1*m.b5*m.b25 - 32*
                       m.b1*m.b5*m.b26 - 64*m.b1*m.b6*m.b7 - 64*m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10
                        - 32*m.b1*m.b6*m.b11 - 64*m.b1*m.b6*m.b12 - 64*m.b1*m.b6*m.b13 - 64*m.b1*m.b6*m.b14 - 64*m.b1*
                       m.b6*m.b15 - 64*m.b1*m.b6*m.b16 - 64*m.b1*m.b6*m.b17 - 64*m.b1*m.b6*m.b18 - 64*m.b1*m.b6*m.b19 - 
                       64*m.b1*m.b6*m.b20 - 64*m.b1*m.b6*m.b21 - 32*m.b1*m.b6*m.b22 - 32*m.b1*m.b6*m.b23 - 32*m.b1*m.b6*
                       m.b24 - 32*m.b1*m.b6*m.b25 - 32*m.b1*m.b6*m.b26 - 64*m.b1*m.b7*m.b8 - 64*m.b1*m.b7*m.b9 - 64*m.b1
                       *m.b7*m.b10 - 64*m.b1*m.b7*m.b11 - 64*m.b1*m.b7*m.b12 - 32*m.b1*m.b7*m.b13 - 64*m.b1*m.b7*m.b14
                        - 64*m.b1*m.b7*m.b15 - 64*m.b1*m.b7*m.b16 - 64*m.b1*m.b7*m.b17 - 64*m.b1*m.b7*m.b18 - 64*m.b1*
                       m.b7*m.b19 - 64*m.b1*m.b7*m.b20 - 32*m.b1*m.b7*m.b21 - 32*m.b1*m.b7*m.b22 - 32*m.b1*m.b7*m.b23 - 
                       32*m.b1*m.b7*m.b24 - 32*m.b1*m.b7*m.b25 - 32*m.b1*m.b7*m.b26 - 64*m.b1*m.b8*m.b9 - 64*m.b1*m.b8*
                       m.b10 - 64*m.b1*m.b8*m.b11 - 64*m.b1*m.b8*m.b12 - 64*m.b1*m.b8*m.b13 - 64*m.b1*m.b8*m.b14 - 32*
                       m.b1*m.b8*m.b15 - 64*m.b1*m.b8*m.b16 - 64*m.b1*m.b8*m.b17 - 64*m.b1*m.b8*m.b18 - 64*m.b1*m.b8*
                       m.b19 - 32*m.b1*m.b8*m.b20 - 32*m.b1*m.b8*m.b21 - 32*m.b1*m.b8*m.b22 - 32*m.b1*m.b8*m.b23 - 32*
                       m.b1*m.b8*m.b24 - 32*m.b1*m.b8*m.b25 - 32*m.b1*m.b8*m.b26 - 64*m.b1*m.b9*m.b10 - 64*m.b1*m.b9*
                       m.b11 - 64*m.b1*m.b9*m.b12 - 64*m.b1*m.b9*m.b13 - 64*m.b1*m.b9*m.b14 - 64*m.b1*m.b9*m.b15 - 64*
                       m.b1*m.b9*m.b16 - 32*m.b1*m.b9*m.b17 - 64*m.b1*m.b9*m.b18 - 32*m.b1*m.b9*m.b19 - 32*m.b1*m.b9*
                       m.b20 - 32*m.b1*m.b9*m.b21 - 32*m.b1*m.b9*m.b22 - 32*m.b1*m.b9*m.b23 - 32*m.b1*m.b9*m.b24 - 32*
                       m.b1*m.b9*m.b25 - 32*m.b1*m.b9*m.b26 - 64*m.b1*m.b10*m.b11 - 64*m.b1*m.b10*m.b12 - 64*m.b1*m.b10*
                       m.b13 - 64*m.b1*m.b10*m.b14 - 64*m.b1*m.b10*m.b15 - 64*m.b1*m.b10*m.b16 - 64*m.b1*m.b10*m.b17 - 
                       32*m.b1*m.b10*m.b18 - 32*m.b1*m.b10*m.b20 - 32*m.b1*m.b10*m.b21 - 32*m.b1*m.b10*m.b22 - 32*m.b1*
                       m.b10*m.b23 - 32*m.b1*m.b10*m.b24 - 32*m.b1*m.b10*m.b25 - 32*m.b1*m.b10*m.b26 - 64*m.b1*m.b11*
                       m.b12 - 64*m.b1*m.b11*m.b13 - 64*m.b1*m.b11*m.b14 - 64*m.b1*m.b11*m.b15 - 64*m.b1*m.b11*m.b16 - 
                       32*m.b1*m.b11*m.b17 - 32*m.b1*m.b11*m.b18 - 32*m.b1*m.b11*m.b19 - 32*m.b1*m.b11*m.b20 - 32*m.b1*
                       m.b11*m.b22 - 32*m.b1*m.b11*m.b23 - 32*m.b1*m.b11*m.b24 - 32*m.b1*m.b11*m.b25 - 32*m.b1*m.b11*
                       m.b26 - 64*m.b1*m.b12*m.b13 - 64*m.b1*m.b12*m.b14 - 64*m.b1*m.b12*m.b15 - 32*m.b1*m.b12*m.b16 - 
                       32*m.b1*m.b12*m.b17 - 32*m.b1*m.b12*m.b18 - 32*m.b1*m.b12*m.b19 - 32*m.b1*m.b12*m.b20 - 32*m.b1*
                       m.b12*m.b21 - 32*m.b1*m.b12*m.b22 - 32*m.b1*m.b12*m.b24 - 32*m.b1*m.b12*m.b25 - 32*m.b1*m.b12*
                       m.b26 - 64*m.b1*m.b13*m.b14 - 32*m.b1*m.b13*m.b15 - 32*m.b1*m.b13*m.b16 - 32*m.b1*m.b13*m.b17 - 
                       32*m.b1*m.b13*m.b18 - 32*m.b1*m.b13*m.b19 - 32*m.b1*m.b13*m.b20 - 32*m.b1*m.b13*m.b21 - 32*m.b1*
                       m.b13*m.b22 - 32*m.b1*m.b13*m.b23 - 32*m.b1*m.b13*m.b24 - 32*m.b1*m.b13*m.b26 - 32*m.b1*m.b14*
                       m.b15 - 32*m.b1*m.b14*m.b16 - 32*m.b1*m.b14*m.b17 - 32*m.b1*m.b14*m.b18 - 32*m.b1*m.b14*m.b19 - 
                       32*m.b1*m.b14*m.b20 - 32*m.b1*m.b14*m.b21 - 32*m.b1*m.b14*m.b22 - 32*m.b1*m.b14*m.b23 - 32*m.b1*
                       m.b14*m.b24 - 32*m.b1*m.b14*m.b25 - 32*m.b1*m.b14*m.b26 - 32*m.b1*m.b15*m.b16 - 32*m.b1*m.b15*
                       m.b17 - 32*m.b1*m.b15*m.b18 - 32*m.b1*m.b15*m.b19 - 32*m.b1*m.b15*m.b20 - 32*m.b1*m.b15*m.b21 - 
                       32*m.b1*m.b15*m.b22 - 32*m.b1*m.b15*m.b23 - 32*m.b1*m.b15*m.b24 - 32*m.b1*m.b15*m.b25 - 32*m.b1*
                       m.b15*m.b26 - 32*m.b1*m.b16*m.b17 - 32*m.b1*m.b16*m.b18 - 32*m.b1*m.b16*m.b19 - 32*m.b1*m.b16*
                       m.b20 - 32*m.b1*m.b16*m.b21 - 32*m.b1*m.b16*m.b22 - 32*m.b1*m.b16*m.b23 - 32*m.b1*m.b16*m.b24 - 
                       32*m.b1*m.b16*m.b25 - 32*m.b1*m.b16*m.b26 - 32*m.b1*m.b17*m.b18 - 32*m.b1*m.b17*m.b19 - 32*m.b1*
                       m.b17*m.b20 - 32*m.b1*m.b17*m.b21 - 32*m.b1*m.b17*m.b22 - 32*m.b1*m.b17*m.b23 - 32*m.b1*m.b17*
                       m.b24 - 32*m.b1*m.b17*m.b25 - 32*m.b1*m.b17*m.b26 - 32*m.b1*m.b18*m.b19 - 32*m.b1*m.b18*m.b20 - 
                       32*m.b1*m.b18*m.b21 - 32*m.b1*m.b18*m.b22 - 32*m.b1*m.b18*m.b23 - 32*m.b1*m.b18*m.b24 - 32*m.b1*
                       m.b18*m.b25 - 32*m.b1*m.b18*m.b26 - 32*m.b1*m.b19*m.b20 - 32*m.b1*m.b19*m.b21 - 32*m.b1*m.b19*
                       m.b22 - 32*m.b1*m.b19*m.b23 - 32*m.b1*m.b19*m.b24 - 32*m.b1*m.b19*m.b25 - 32*m.b1*m.b19*m.b26 - 
                       32*m.b1*m.b20*m.b21 - 32*m.b1*m.b20*m.b22 - 32*m.b1*m.b20*m.b23 - 32*m.b1*m.b20*m.b24 - 32*m.b1*
                       m.b20*m.b25 - 32*m.b1*m.b20*m.b26 - 32*m.b1*m.b21*m.b22 - 32*m.b1*m.b21*m.b23 - 32*m.b1*m.b21*
                       m.b24 - 32*m.b1*m.b21*m.b25 - 32*m.b1*m.b21*m.b26 - 32*m.b1*m.b22*m.b23 - 32*m.b1*m.b22*m.b24 - 
                       32*m.b1*m.b22*m.b25 - 32*m.b1*m.b22*m.b26 - 32*m.b1*m.b23*m.b24 - 32*m.b1*m.b23*m.b25 - 32*m.b1*
                       m.b23*m.b26 - 32*m.b1*m.b24*m.b25 - 32*m.b1*m.b24*m.b26 - 32*m.b1*m.b25*m.b26 - 96*m.b2*m.b3*m.b4
                        - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*m.b2*m.b3*m.b8 - 128*m.b2*
                       m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*m.b11 - 128*m.b2*m.b3*m.b12 - 128*m.b2*m.b3*m.b13
                        - 128*m.b2*m.b3*m.b14 - 128*m.b2*m.b3*m.b15 - 128*m.b2*m.b3*m.b16 - 128*m.b2*m.b3*m.b17 - 128*
                       m.b2*m.b3*m.b18 - 128*m.b2*m.b3*m.b19 - 128*m.b2*m.b3*m.b20 - 128*m.b2*m.b3*m.b21 - 128*m.b2*m.b3
                       *m.b22 - 128*m.b2*m.b3*m.b23 - 128*m.b2*m.b3*m.b24 - 128*m.b2*m.b3*m.b25 - 96*m.b2*m.b3*m.b26 - 
                       32*m.b2*m.b3*m.b27 - 160*m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*
                       m.b8 - 128*m.b2*m.b4*m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 128
                       *m.b2*m.b4*m.b13 - 128*m.b2*m.b4*m.b14 - 128*m.b2*m.b4*m.b15 - 128*m.b2*m.b4*m.b16 - 128*m.b2*
                       m.b4*m.b17 - 128*m.b2*m.b4*m.b18 - 128*m.b2*m.b4*m.b19 - 128*m.b2*m.b4*m.b20 - 128*m.b2*m.b4*
                       m.b21 - 128*m.b2*m.b4*m.b22 - 128*m.b2*m.b4*m.b23 - 128*m.b2*m.b4*m.b24 - 96*m.b2*m.b4*m.b25 - 64
                       *m.b2*m.b4*m.b26 - 32*m.b2*m.b4*m.b27 - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*m.b7 - 64*m.b2*m.b5*
                       m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 128*m.b2*m.b5*m.b11 - 128*m.b2*m.b5*m.b12 - 128
                       *m.b2*m.b5*m.b13 - 128*m.b2*m.b5*m.b14 - 128*m.b2*m.b5*m.b15 - 128*m.b2*m.b5*m.b16 - 128*m.b2*
                       m.b5*m.b17 - 128*m.b2*m.b5*m.b18 - 128*m.b2*m.b5*m.b19 - 128*m.b2*m.b5*m.b20 - 128*m.b2*m.b5*
                       m.b21 - 128*m.b2*m.b5*m.b22 - 128*m.b2*m.b5*m.b23 - 96*m.b2*m.b5*m.b24 - 64*m.b2*m.b5*m.b25 - 64*
                       m.b2*m.b5*m.b26 - 32*m.b2*m.b5*m.b27 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*m.b6*
                       m.b9 - 64*m.b2*m.b6*m.b10 - 128*m.b2*m.b6*m.b11 - 128*m.b2*m.b6*m.b12 - 128*m.b2*m.b6*m.b13 - 128
                       *m.b2*m.b6*m.b14 - 128*m.b2*m.b6*m.b15 - 128*m.b2*m.b6*m.b16 - 128*m.b2*m.b6*m.b17 - 128*m.b2*
                       m.b6*m.b18 - 128*m.b2*m.b6*m.b19 - 128*m.b2*m.b6*m.b20 - 128*m.b2*m.b6*m.b21 - 128*m.b2*m.b6*
                       m.b22 - 96*m.b2*m.b6*m.b23 - 64*m.b2*m.b6*m.b24 - 64*m.b2*m.b6*m.b25 - 64*m.b2*m.b6*m.b26 - 32*
                       m.b2*m.b6*m.b27 - 160*m.b2*m.b7*m.b8 - 128*m.b2*m.b7*m.b9 - 128*m.b2*m.b7*m.b10 - 128*m.b2*m.b7*
                       m.b11 - 64*m.b2*m.b7*m.b12 - 128*m.b2*m.b7*m.b13 - 128*m.b2*m.b7*m.b14 - 128*m.b2*m.b7*m.b15 - 
                       128*m.b2*m.b7*m.b16 - 128*m.b2*m.b7*m.b17 - 128*m.b2*m.b7*m.b18 - 128*m.b2*m.b7*m.b19 - 128*m.b2*
                       m.b7*m.b20 - 128*m.b2*m.b7*m.b21 - 96*m.b2*m.b7*m.b22 - 64*m.b2*m.b7*m.b23 - 64*m.b2*m.b7*m.b24
                        - 64*m.b2*m.b7*m.b25 - 64*m.b2*m.b7*m.b26 - 32*m.b2*m.b7*m.b27 - 160*m.b2*m.b8*m.b9 - 128*m.b2*
                       m.b8*m.b10 - 128*m.b2*m.b8*m.b11 - 128*m.b2*m.b8*m.b12 - 128*m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b14
                        - 128*m.b2*m.b8*m.b15 - 128*m.b2*m.b8*m.b16 - 128*m.b2*m.b8*m.b17 - 128*m.b2*m.b8*m.b18 - 128*
                       m.b2*m.b8*m.b19 - 128*m.b2*m.b8*m.b20 - 96*m.b2*m.b8*m.b21 - 64*m.b2*m.b8*m.b22 - 64*m.b2*m.b8*
                       m.b23 - 64*m.b2*m.b8*m.b24 - 64*m.b2*m.b8*m.b25 - 64*m.b2*m.b8*m.b26 - 32*m.b2*m.b8*m.b27 - 160*
                       m.b2*m.b9*m.b10 - 128*m.b2*m.b9*m.b11 - 128*m.b2*m.b9*m.b12 - 128*m.b2*m.b9*m.b13 - 128*m.b2*m.b9
                       *m.b14 - 128*m.b2*m.b9*m.b15 - 64*m.b2*m.b9*m.b16 - 128*m.b2*m.b9*m.b17 - 128*m.b2*m.b9*m.b18 - 
                       128*m.b2*m.b9*m.b19 - 96*m.b2*m.b9*m.b20 - 64*m.b2*m.b9*m.b21 - 64*m.b2*m.b9*m.b22 - 64*m.b2*m.b9
                       *m.b23 - 64*m.b2*m.b9*m.b24 - 64*m.b2*m.b9*m.b25 - 64*m.b2*m.b9*m.b26 - 32*m.b2*m.b9*m.b27 - 160*
                       m.b2*m.b10*m.b11 - 128*m.b2*m.b10*m.b12 - 128*m.b2*m.b10*m.b13 - 128*m.b2*m.b10*m.b14 - 128*m.b2*
                       m.b10*m.b15 - 128*m.b2*m.b10*m.b16 - 128*m.b2*m.b10*m.b17 - 64*m.b2*m.b10*m.b18 - 96*m.b2*m.b10*
                       m.b19 - 64*m.b2*m.b10*m.b20 - 64*m.b2*m.b10*m.b21 - 64*m.b2*m.b10*m.b22 - 64*m.b2*m.b10*m.b23 - 
                       64*m.b2*m.b10*m.b24 - 64*m.b2*m.b10*m.b25 - 64*m.b2*m.b10*m.b26 - 32*m.b2*m.b10*m.b27 - 160*m.b2*
                       m.b11*m.b12 - 128*m.b2*m.b11*m.b13 - 128*m.b2*m.b11*m.b14 - 128*m.b2*m.b11*m.b15 - 128*m.b2*m.b11
                       *m.b16 - 128*m.b2*m.b11*m.b17 - 96*m.b2*m.b11*m.b18 - 64*m.b2*m.b11*m.b19 - 64*m.b2*m.b11*m.b21
                        - 64*m.b2*m.b11*m.b22 - 64*m.b2*m.b11*m.b23 - 64*m.b2*m.b11*m.b24 - 64*m.b2*m.b11*m.b25 - 64*
                       m.b2*m.b11*m.b26 - 32*m.b2*m.b11*m.b27 - 160*m.b2*m.b12*m.b13 - 128*m.b2*m.b12*m.b14 - 128*m.b2*
                       m.b12*m.b15 - 128*m.b2*m.b12*m.b16 - 96*m.b2*m.b12*m.b17 - 64*m.b2*m.b12*m.b18 - 64*m.b2*m.b12*
                       m.b19 - 64*m.b2*m.b12*m.b20 - 64*m.b2*m.b12*m.b21 - 64*m.b2*m.b12*m.b23 - 64*m.b2*m.b12*m.b24 - 
                       64*m.b2*m.b12*m.b25 - 64*m.b2*m.b12*m.b26 - 32*m.b2*m.b12*m.b27 - 160*m.b2*m.b13*m.b14 - 128*m.b2
                       *m.b13*m.b15 - 96*m.b2*m.b13*m.b16 - 64*m.b2*m.b13*m.b17 - 64*m.b2*m.b13*m.b18 - 64*m.b2*m.b13*
                       m.b19 - 64*m.b2*m.b13*m.b20 - 64*m.b2*m.b13*m.b21 - 64*m.b2*m.b13*m.b22 - 64*m.b2*m.b13*m.b23 - 
                       64*m.b2*m.b13*m.b25 - 64*m.b2*m.b13*m.b26 - 32*m.b2*m.b13*m.b27 - 128*m.b2*m.b14*m.b15 - 64*m.b2*
                       m.b14*m.b16 - 64*m.b2*m.b14*m.b17 - 64*m.b2*m.b14*m.b18 - 64*m.b2*m.b14*m.b19 - 64*m.b2*m.b14*
                       m.b20 - 64*m.b2*m.b14*m.b21 - 64*m.b2*m.b14*m.b22 - 64*m.b2*m.b14*m.b23 - 64*m.b2*m.b14*m.b24 - 
                       64*m.b2*m.b14*m.b25 - 32*m.b2*m.b14*m.b27 - 96*m.b2*m.b15*m.b16 - 64*m.b2*m.b15*m.b17 - 64*m.b2*
                       m.b15*m.b18 - 64*m.b2*m.b15*m.b19 - 64*m.b2*m.b15*m.b20 - 64*m.b2*m.b15*m.b21 - 64*m.b2*m.b15*
                       m.b22 - 64*m.b2*m.b15*m.b23 - 64*m.b2*m.b15*m.b24 - 64*m.b2*m.b15*m.b25 - 64*m.b2*m.b15*m.b26 - 
                       32*m.b2*m.b15*m.b27 - 96*m.b2*m.b16*m.b17 - 64*m.b2*m.b16*m.b18 - 64*m.b2*m.b16*m.b19 - 64*m.b2*
                       m.b16*m.b20 - 64*m.b2*m.b16*m.b21 - 64*m.b2*m.b16*m.b22 - 64*m.b2*m.b16*m.b23 - 64*m.b2*m.b16*
                       m.b24 - 64*m.b2*m.b16*m.b25 - 64*m.b2*m.b16*m.b26 - 32*m.b2*m.b16*m.b27 - 96*m.b2*m.b17*m.b18 - 
                       64*m.b2*m.b17*m.b19 - 64*m.b2*m.b17*m.b20 - 64*m.b2*m.b17*m.b21 - 64*m.b2*m.b17*m.b22 - 64*m.b2*
                       m.b17*m.b23 - 64*m.b2*m.b17*m.b24 - 64*m.b2*m.b17*m.b25 - 64*m.b2*m.b17*m.b26 - 32*m.b2*m.b17*
                       m.b27 - 96*m.b2*m.b18*m.b19 - 64*m.b2*m.b18*m.b20 - 64*m.b2*m.b18*m.b21 - 64*m.b2*m.b18*m.b22 - 
                       64*m.b2*m.b18*m.b23 - 64*m.b2*m.b18*m.b24 - 64*m.b2*m.b18*m.b25 - 64*m.b2*m.b18*m.b26 - 32*m.b2*
                       m.b18*m.b27 - 96*m.b2*m.b19*m.b20 - 64*m.b2*m.b19*m.b21 - 64*m.b2*m.b19*m.b22 - 64*m.b2*m.b19*
                       m.b23 - 64*m.b2*m.b19*m.b24 - 64*m.b2*m.b19*m.b25 - 64*m.b2*m.b19*m.b26 - 32*m.b2*m.b19*m.b27 - 
                       96*m.b2*m.b20*m.b21 - 64*m.b2*m.b20*m.b22 - 64*m.b2*m.b20*m.b23 - 64*m.b2*m.b20*m.b24 - 64*m.b2*
                       m.b20*m.b25 - 64*m.b2*m.b20*m.b26 - 32*m.b2*m.b20*m.b27 - 96*m.b2*m.b21*m.b22 - 64*m.b2*m.b21*
                       m.b23 - 64*m.b2*m.b21*m.b24 - 64*m.b2*m.b21*m.b25 - 64*m.b2*m.b21*m.b26 - 32*m.b2*m.b21*m.b27 - 
                       96*m.b2*m.b22*m.b23 - 64*m.b2*m.b22*m.b24 - 64*m.b2*m.b22*m.b25 - 64*m.b2*m.b22*m.b26 - 32*m.b2*
                       m.b22*m.b27 - 96*m.b2*m.b23*m.b24 - 64*m.b2*m.b23*m.b25 - 64*m.b2*m.b23*m.b26 - 32*m.b2*m.b23*
                       m.b27 - 96*m.b2*m.b24*m.b25 - 64*m.b2*m.b24*m.b26 - 32*m.b2*m.b24*m.b27 - 96*m.b2*m.b25*m.b26 - 
                       32*m.b2*m.b25*m.b27 - 32*m.b2*m.b26*m.b27 - 160*m.b3*m.b4*m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*
                       m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4*m.b9 - 192*m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11
                        - 192*m.b3*m.b4*m.b12 - 192*m.b3*m.b4*m.b13 - 192*m.b3*m.b4*m.b14 - 192*m.b3*m.b4*m.b15 - 192*
                       m.b3*m.b4*m.b16 - 192*m.b3*m.b4*m.b17 - 192*m.b3*m.b4*m.b18 - 192*m.b3*m.b4*m.b19 - 192*m.b3*m.b4
                       *m.b20 - 192*m.b3*m.b4*m.b21 - 192*m.b3*m.b4*m.b22 - 192*m.b3*m.b4*m.b23 - 192*m.b3*m.b4*m.b24 - 
                       192*m.b3*m.b4*m.b25 - 160*m.b3*m.b4*m.b26 - 96*m.b3*m.b4*m.b27 - 32*m.b3*m.b4*m.b28 - 256*m.b3*
                       m.b5*m.b6 - 128*m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10 - 
                       192*m.b3*m.b5*m.b11 - 192*m.b3*m.b5*m.b12 - 192*m.b3*m.b5*m.b13 - 192*m.b3*m.b5*m.b14 - 192*m.b3*
                       m.b5*m.b15 - 192*m.b3*m.b5*m.b16 - 192*m.b3*m.b5*m.b17 - 192*m.b3*m.b5*m.b18 - 192*m.b3*m.b5*
                       m.b19 - 192*m.b3*m.b5*m.b20 - 192*m.b3*m.b5*m.b21 - 192*m.b3*m.b5*m.b22 - 192*m.b3*m.b5*m.b23 - 
                       192*m.b3*m.b5*m.b24 - 160*m.b3*m.b5*m.b25 - 128*m.b3*m.b5*m.b26 - 64*m.b3*m.b5*m.b27 - 32*m.b3*
                       m.b5*m.b28 - 256*m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*m.b9 - 192*m.b3*m.b6*m.b10 - 
                       192*m.b3*m.b6*m.b11 - 192*m.b3*m.b6*m.b12 - 192*m.b3*m.b6*m.b13 - 192*m.b3*m.b6*m.b14 - 192*m.b3*
                       m.b6*m.b15 - 192*m.b3*m.b6*m.b16 - 192*m.b3*m.b6*m.b17 - 192*m.b3*m.b6*m.b18 - 192*m.b3*m.b6*
                       m.b19 - 192*m.b3*m.b6*m.b20 - 192*m.b3*m.b6*m.b21 - 192*m.b3*m.b6*m.b22 - 192*m.b3*m.b6*m.b23 - 
                       160*m.b3*m.b6*m.b24 - 128*m.b3*m.b6*m.b25 - 96*m.b3*m.b6*m.b26 - 64*m.b3*m.b6*m.b27 - 32*m.b3*
                       m.b6*m.b28 - 256*m.b3*m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 192*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*m.b11
                        - 192*m.b3*m.b7*m.b12 - 192*m.b3*m.b7*m.b13 - 192*m.b3*m.b7*m.b14 - 192*m.b3*m.b7*m.b15 - 192*
                       m.b3*m.b7*m.b16 - 192*m.b3*m.b7*m.b17 - 192*m.b3*m.b7*m.b18 - 192*m.b3*m.b7*m.b19 - 192*m.b3*m.b7
                       *m.b20 - 192*m.b3*m.b7*m.b21 - 192*m.b3*m.b7*m.b22 - 160*m.b3*m.b7*m.b23 - 128*m.b3*m.b7*m.b24 - 
                       96*m.b3*m.b7*m.b25 - 96*m.b3*m.b7*m.b26 - 64*m.b3*m.b7*m.b27 - 32*m.b3*m.b7*m.b28 - 256*m.b3*m.b8
                       *m.b9 - 224*m.b3*m.b8*m.b10 - 192*m.b3*m.b8*m.b11 - 192*m.b3*m.b8*m.b12 - 96*m.b3*m.b8*m.b13 - 
                       192*m.b3*m.b8*m.b14 - 192*m.b3*m.b8*m.b15 - 192*m.b3*m.b8*m.b16 - 192*m.b3*m.b8*m.b17 - 192*m.b3*
                       m.b8*m.b18 - 192*m.b3*m.b8*m.b19 - 192*m.b3*m.b8*m.b20 - 192*m.b3*m.b8*m.b21 - 160*m.b3*m.b8*
                       m.b22 - 128*m.b3*m.b8*m.b23 - 96*m.b3*m.b8*m.b24 - 96*m.b3*m.b8*m.b25 - 96*m.b3*m.b8*m.b26 - 64*
                       m.b3*m.b8*m.b27 - 32*m.b3*m.b8*m.b28 - 256*m.b3*m.b9*m.b10 - 224*m.b3*m.b9*m.b11 - 192*m.b3*m.b9*
                       m.b12 - 192*m.b3*m.b9*m.b13 - 192*m.b3*m.b9*m.b14 - 96*m.b3*m.b9*m.b15 - 192*m.b3*m.b9*m.b16 - 
                       192*m.b3*m.b9*m.b17 - 192*m.b3*m.b9*m.b18 - 192*m.b3*m.b9*m.b19 - 192*m.b3*m.b9*m.b20 - 160*m.b3*
                       m.b9*m.b21 - 128*m.b3*m.b9*m.b22 - 96*m.b3*m.b9*m.b23 - 96*m.b3*m.b9*m.b24 - 96*m.b3*m.b9*m.b25
                        - 96*m.b3*m.b9*m.b26 - 64*m.b3*m.b9*m.b27 - 32*m.b3*m.b9*m.b28 - 256*m.b3*m.b10*m.b11 - 224*m.b3
                       *m.b10*m.b12 - 192*m.b3*m.b10*m.b13 - 192*m.b3*m.b10*m.b14 - 192*m.b3*m.b10*m.b15 - 192*m.b3*
                       m.b10*m.b16 - 96*m.b3*m.b10*m.b17 - 192*m.b3*m.b10*m.b18 - 192*m.b3*m.b10*m.b19 - 160*m.b3*m.b10*
                       m.b20 - 128*m.b3*m.b10*m.b21 - 96*m.b3*m.b10*m.b22 - 96*m.b3*m.b10*m.b23 - 96*m.b3*m.b10*m.b24 - 
                       96*m.b3*m.b10*m.b25 - 96*m.b3*m.b10*m.b26 - 64*m.b3*m.b10*m.b27 - 32*m.b3*m.b10*m.b28 - 256*m.b3*
                       m.b11*m.b12 - 224*m.b3*m.b11*m.b13 - 192*m.b3*m.b11*m.b14 - 192*m.b3*m.b11*m.b15 - 192*m.b3*m.b11
                       *m.b16 - 192*m.b3*m.b11*m.b17 - 192*m.b3*m.b11*m.b18 - 64*m.b3*m.b11*m.b19 - 128*m.b3*m.b11*m.b20
                        - 96*m.b3*m.b11*m.b21 - 96*m.b3*m.b11*m.b22 - 96*m.b3*m.b11*m.b23 - 96*m.b3*m.b11*m.b24 - 96*
                       m.b3*m.b11*m.b25 - 96*m.b3*m.b11*m.b26 - 64*m.b3*m.b11*m.b27 - 32*m.b3*m.b11*m.b28 - 256*m.b3*
                       m.b12*m.b13 - 224*m.b3*m.b12*m.b14 - 192*m.b3*m.b12*m.b15 - 192*m.b3*m.b12*m.b16 - 192*m.b3*m.b12
                       *m.b17 - 160*m.b3*m.b12*m.b18 - 128*m.b3*m.b12*m.b19 - 96*m.b3*m.b12*m.b20 - 96*m.b3*m.b12*m.b22
                        - 96*m.b3*m.b12*m.b23 - 96*m.b3*m.b12*m.b24 - 96*m.b3*m.b12*m.b25 - 96*m.b3*m.b12*m.b26 - 64*
                       m.b3*m.b12*m.b27 - 32*m.b3*m.b12*m.b28 - 256*m.b3*m.b13*m.b14 - 224*m.b3*m.b13*m.b15 - 192*m.b3*
                       m.b13*m.b16 - 160*m.b3*m.b13*m.b17 - 128*m.b3*m.b13*m.b18 - 96*m.b3*m.b13*m.b19 - 96*m.b3*m.b13*
                       m.b20 - 96*m.b3*m.b13*m.b21 - 96*m.b3*m.b13*m.b22 - 96*m.b3*m.b13*m.b24 - 96*m.b3*m.b13*m.b25 - 
                       96*m.b3*m.b13*m.b26 - 64*m.b3*m.b13*m.b27 - 32*m.b3*m.b13*m.b28 - 256*m.b3*m.b14*m.b15 - 192*m.b3
                       *m.b14*m.b16 - 128*m.b3*m.b14*m.b17 - 96*m.b3*m.b14*m.b18 - 96*m.b3*m.b14*m.b19 - 96*m.b3*m.b14*
                       m.b20 - 96*m.b3*m.b14*m.b21 - 96*m.b3*m.b14*m.b22 - 96*m.b3*m.b14*m.b23 - 96*m.b3*m.b14*m.b24 - 
                       96*m.b3*m.b14*m.b26 - 64*m.b3*m.b14*m.b27 - 32*m.b3*m.b14*m.b28 - 192*m.b3*m.b15*m.b16 - 128*m.b3
                       *m.b15*m.b17 - 96*m.b3*m.b15*m.b18 - 96*m.b3*m.b15*m.b19 - 96*m.b3*m.b15*m.b20 - 96*m.b3*m.b15*
                       m.b21 - 96*m.b3*m.b15*m.b22 - 96*m.b3*m.b15*m.b23 - 96*m.b3*m.b15*m.b24 - 96*m.b3*m.b15*m.b25 - 
                       96*m.b3*m.b15*m.b26 - 32*m.b3*m.b15*m.b28 - 160*m.b3*m.b16*m.b17 - 128*m.b3*m.b16*m.b18 - 96*m.b3
                       *m.b16*m.b19 - 96*m.b3*m.b16*m.b20 - 96*m.b3*m.b16*m.b21 - 96*m.b3*m.b16*m.b22 - 96*m.b3*m.b16*
                       m.b23 - 96*m.b3*m.b16*m.b24 - 96*m.b3*m.b16*m.b25 - 96*m.b3*m.b16*m.b26 - 64*m.b3*m.b16*m.b27 - 
                       32*m.b3*m.b16*m.b28 - 160*m.b3*m.b17*m.b18 - 128*m.b3*m.b17*m.b19 - 96*m.b3*m.b17*m.b20 - 96*m.b3
                       *m.b17*m.b21 - 96*m.b3*m.b17*m.b22 - 96*m.b3*m.b17*m.b23 - 96*m.b3*m.b17*m.b24 - 96*m.b3*m.b17*
                       m.b25 - 96*m.b3*m.b17*m.b26 - 64*m.b3*m.b17*m.b27 - 32*m.b3*m.b17*m.b28 - 160*m.b3*m.b18*m.b19 - 
                       128*m.b3*m.b18*m.b20 - 96*m.b3*m.b18*m.b21 - 96*m.b3*m.b18*m.b22 - 96*m.b3*m.b18*m.b23 - 96*m.b3*
                       m.b18*m.b24 - 96*m.b3*m.b18*m.b25 - 96*m.b3*m.b18*m.b26 - 64*m.b3*m.b18*m.b27 - 32*m.b3*m.b18*
                       m.b28 - 160*m.b3*m.b19*m.b20 - 128*m.b3*m.b19*m.b21 - 96*m.b3*m.b19*m.b22 - 96*m.b3*m.b19*m.b23
                        - 96*m.b3*m.b19*m.b24 - 96*m.b3*m.b19*m.b25 - 96*m.b3*m.b19*m.b26 - 64*m.b3*m.b19*m.b27 - 32*
                       m.b3*m.b19*m.b28 - 160*m.b3*m.b20*m.b21 - 128*m.b3*m.b20*m.b22 - 96*m.b3*m.b20*m.b23 - 96*m.b3*
                       m.b20*m.b24 - 96*m.b3*m.b20*m.b25 - 96*m.b3*m.b20*m.b26 - 64*m.b3*m.b20*m.b27 - 32*m.b3*m.b20*
                       m.b28 - 160*m.b3*m.b21*m.b22 - 128*m.b3*m.b21*m.b23 - 96*m.b3*m.b21*m.b24 - 96*m.b3*m.b21*m.b25
                        - 96*m.b3*m.b21*m.b26 - 64*m.b3*m.b21*m.b27 - 32*m.b3*m.b21*m.b28 - 160*m.b3*m.b22*m.b23 - 128*
                       m.b3*m.b22*m.b24 - 96*m.b3*m.b22*m.b25 - 96*m.b3*m.b22*m.b26 - 64*m.b3*m.b22*m.b27 - 32*m.b3*
                       m.b22*m.b28 - 160*m.b3*m.b23*m.b24 - 128*m.b3*m.b23*m.b25 - 96*m.b3*m.b23*m.b26 - 64*m.b3*m.b23*
                       m.b27 - 32*m.b3*m.b23*m.b28 - 160*m.b3*m.b24*m.b25 - 128*m.b3*m.b24*m.b26 - 64*m.b3*m.b24*m.b27
                        - 32*m.b3*m.b24*m.b28 - 160*m.b3*m.b25*m.b26 - 64*m.b3*m.b25*m.b27 - 32*m.b3*m.b25*m.b28 - 96*
                       m.b3*m.b26*m.b27 - 32*m.b3*m.b26*m.b28 - 32*m.b3*m.b27*m.b28 - 224*m.b4*m.b5*m.b6 - 320*m.b4*m.b5
                       *m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 256*m.b4*m.b5*m.b11 - 256
                       *m.b4*m.b5*m.b12 - 256*m.b4*m.b5*m.b13 - 256*m.b4*m.b5*m.b14 - 256*m.b4*m.b5*m.b15 - 256*m.b4*
                       m.b5*m.b16 - 256*m.b4*m.b5*m.b17 - 256*m.b4*m.b5*m.b18 - 256*m.b4*m.b5*m.b19 - 256*m.b4*m.b5*
                       m.b20 - 256*m.b4*m.b5*m.b21 - 256*m.b4*m.b5*m.b22 - 256*m.b4*m.b5*m.b23 - 256*m.b4*m.b5*m.b24 - 
                       256*m.b4*m.b5*m.b25 - 224*m.b4*m.b5*m.b26 - 160*m.b4*m.b5*m.b27 - 96*m.b4*m.b5*m.b28 - 32*m.b4*
                       m.b5*m.b29 - 352*m.b4*m.b6*m.b7 - 192*m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10
                        - 256*m.b4*m.b6*m.b11 - 256*m.b4*m.b6*m.b12 - 256*m.b4*m.b6*m.b13 - 256*m.b4*m.b6*m.b14 - 256*
                       m.b4*m.b6*m.b15 - 256*m.b4*m.b6*m.b16 - 256*m.b4*m.b6*m.b17 - 256*m.b4*m.b6*m.b18 - 256*m.b4*m.b6
                       *m.b19 - 256*m.b4*m.b6*m.b20 - 256*m.b4*m.b6*m.b21 - 256*m.b4*m.b6*m.b22 - 256*m.b4*m.b6*m.b23 - 
                       256*m.b4*m.b6*m.b24 - 224*m.b4*m.b6*m.b25 - 192*m.b4*m.b6*m.b26 - 128*m.b4*m.b6*m.b27 - 64*m.b4*
                       m.b6*m.b28 - 32*m.b4*m.b6*m.b29 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*m.b4*m.b7*m.b10
                        - 256*m.b4*m.b7*m.b11 - 256*m.b4*m.b7*m.b12 - 256*m.b4*m.b7*m.b13 - 256*m.b4*m.b7*m.b14 - 256*
                       m.b4*m.b7*m.b15 - 256*m.b4*m.b7*m.b16 - 256*m.b4*m.b7*m.b17 - 256*m.b4*m.b7*m.b18 - 256*m.b4*m.b7
                       *m.b19 - 256*m.b4*m.b7*m.b20 - 256*m.b4*m.b7*m.b21 - 256*m.b4*m.b7*m.b22 - 256*m.b4*m.b7*m.b23 - 
                       224*m.b4*m.b7*m.b24 - 192*m.b4*m.b7*m.b25 - 160*m.b4*m.b7*m.b26 - 96*m.b4*m.b7*m.b27 - 64*m.b4*
                       m.b7*m.b28 - 32*m.b4*m.b7*m.b29 - 352*m.b4*m.b8*m.b9 - 320*m.b4*m.b8*m.b10 - 288*m.b4*m.b8*m.b11
                        - 128*m.b4*m.b8*m.b12 - 256*m.b4*m.b8*m.b13 - 256*m.b4*m.b8*m.b14 - 256*m.b4*m.b8*m.b15 - 256*
                       m.b4*m.b8*m.b16 - 256*m.b4*m.b8*m.b17 - 256*m.b4*m.b8*m.b18 - 256*m.b4*m.b8*m.b19 - 256*m.b4*m.b8
                       *m.b20 - 256*m.b4*m.b8*m.b21 - 256*m.b4*m.b8*m.b22 - 224*m.b4*m.b8*m.b23 - 192*m.b4*m.b8*m.b24 - 
                       160*m.b4*m.b8*m.b25 - 128*m.b4*m.b8*m.b26 - 96*m.b4*m.b8*m.b27 - 64*m.b4*m.b8*m.b28 - 32*m.b4*
                       m.b8*m.b29 - 352*m.b4*m.b9*m.b10 - 320*m.b4*m.b9*m.b11 - 288*m.b4*m.b9*m.b12 - 256*m.b4*m.b9*
                       m.b13 - 128*m.b4*m.b9*m.b14 - 256*m.b4*m.b9*m.b15 - 256*m.b4*m.b9*m.b16 - 256*m.b4*m.b9*m.b17 - 
                       256*m.b4*m.b9*m.b18 - 256*m.b4*m.b9*m.b19 - 256*m.b4*m.b9*m.b20 - 256*m.b4*m.b9*m.b21 - 224*m.b4*
                       m.b9*m.b22 - 192*m.b4*m.b9*m.b23 - 160*m.b4*m.b9*m.b24 - 128*m.b4*m.b9*m.b25 - 128*m.b4*m.b9*
                       m.b26 - 96*m.b4*m.b9*m.b27 - 64*m.b4*m.b9*m.b28 - 32*m.b4*m.b9*m.b29 - 352*m.b4*m.b10*m.b11 - 320
                       *m.b4*m.b10*m.b12 - 288*m.b4*m.b10*m.b13 - 256*m.b4*m.b10*m.b14 - 256*m.b4*m.b10*m.b15 - 128*m.b4
                       *m.b10*m.b16 - 256*m.b4*m.b10*m.b17 - 256*m.b4*m.b10*m.b18 - 256*m.b4*m.b10*m.b19 - 256*m.b4*
                       m.b10*m.b20 - 224*m.b4*m.b10*m.b21 - 192*m.b4*m.b10*m.b22 - 160*m.b4*m.b10*m.b23 - 128*m.b4*m.b10
                       *m.b24 - 128*m.b4*m.b10*m.b25 - 128*m.b4*m.b10*m.b26 - 96*m.b4*m.b10*m.b27 - 64*m.b4*m.b10*m.b28
                        - 32*m.b4*m.b10*m.b29 - 352*m.b4*m.b11*m.b12 - 320*m.b4*m.b11*m.b13 - 288*m.b4*m.b11*m.b14 - 256
                       *m.b4*m.b11*m.b15 - 256*m.b4*m.b11*m.b16 - 256*m.b4*m.b11*m.b17 - 128*m.b4*m.b11*m.b18 - 256*m.b4
                       *m.b11*m.b19 - 224*m.b4*m.b11*m.b20 - 192*m.b4*m.b11*m.b21 - 160*m.b4*m.b11*m.b22 - 128*m.b4*
                       m.b11*m.b23 - 128*m.b4*m.b11*m.b24 - 128*m.b4*m.b11*m.b25 - 128*m.b4*m.b11*m.b26 - 96*m.b4*m.b11*
                       m.b27 - 64*m.b4*m.b11*m.b28 - 32*m.b4*m.b11*m.b29 - 352*m.b4*m.b12*m.b13 - 320*m.b4*m.b12*m.b14
                        - 288*m.b4*m.b12*m.b15 - 256*m.b4*m.b12*m.b16 - 256*m.b4*m.b12*m.b17 - 256*m.b4*m.b12*m.b18 - 
                       224*m.b4*m.b12*m.b19 - 64*m.b4*m.b12*m.b20 - 160*m.b4*m.b12*m.b21 - 128*m.b4*m.b12*m.b22 - 128*
                       m.b4*m.b12*m.b23 - 128*m.b4*m.b12*m.b24 - 128*m.b4*m.b12*m.b25 - 128*m.b4*m.b12*m.b26 - 96*m.b4*
                       m.b12*m.b27 - 64*m.b4*m.b12*m.b28 - 32*m.b4*m.b12*m.b29 - 352*m.b4*m.b13*m.b14 - 320*m.b4*m.b13*
                       m.b15 - 288*m.b4*m.b13*m.b16 - 256*m.b4*m.b13*m.b17 - 224*m.b4*m.b13*m.b18 - 192*m.b4*m.b13*m.b19
                        - 160*m.b4*m.b13*m.b20 - 128*m.b4*m.b13*m.b21 - 128*m.b4*m.b13*m.b23 - 128*m.b4*m.b13*m.b24 - 
                       128*m.b4*m.b13*m.b25 - 128*m.b4*m.b13*m.b26 - 96*m.b4*m.b13*m.b27 - 64*m.b4*m.b13*m.b28 - 32*m.b4
                       *m.b13*m.b29 - 352*m.b4*m.b14*m.b15 - 320*m.b4*m.b14*m.b16 - 256*m.b4*m.b14*m.b17 - 192*m.b4*
                       m.b14*m.b18 - 160*m.b4*m.b14*m.b19 - 128*m.b4*m.b14*m.b20 - 128*m.b4*m.b14*m.b21 - 128*m.b4*m.b14
                       *m.b22 - 128*m.b4*m.b14*m.b23 - 128*m.b4*m.b14*m.b25 - 128*m.b4*m.b14*m.b26 - 96*m.b4*m.b14*m.b27
                        - 64*m.b4*m.b14*m.b28 - 32*m.b4*m.b14*m.b29 - 320*m.b4*m.b15*m.b16 - 256*m.b4*m.b15*m.b17 - 192*
                       m.b4*m.b15*m.b18 - 128*m.b4*m.b15*m.b19 - 128*m.b4*m.b15*m.b20 - 128*m.b4*m.b15*m.b21 - 128*m.b4*
                       m.b15*m.b22 - 128*m.b4*m.b15*m.b23 - 128*m.b4*m.b15*m.b24 - 128*m.b4*m.b15*m.b25 - 96*m.b4*m.b15*
                       m.b27 - 64*m.b4*m.b15*m.b28 - 32*m.b4*m.b15*m.b29 - 256*m.b4*m.b16*m.b17 - 192*m.b4*m.b16*m.b18
                        - 160*m.b4*m.b16*m.b19 - 128*m.b4*m.b16*m.b20 - 128*m.b4*m.b16*m.b21 - 128*m.b4*m.b16*m.b22 - 
                       128*m.b4*m.b16*m.b23 - 128*m.b4*m.b16*m.b24 - 128*m.b4*m.b16*m.b25 - 128*m.b4*m.b16*m.b26 - 96*
                       m.b4*m.b16*m.b27 - 32*m.b4*m.b16*m.b29 - 224*m.b4*m.b17*m.b18 - 192*m.b4*m.b17*m.b19 - 160*m.b4*
                       m.b17*m.b20 - 128*m.b4*m.b17*m.b21 - 128*m.b4*m.b17*m.b22 - 128*m.b4*m.b17*m.b23 - 128*m.b4*m.b17
                       *m.b24 - 128*m.b4*m.b17*m.b25 - 128*m.b4*m.b17*m.b26 - 96*m.b4*m.b17*m.b27 - 64*m.b4*m.b17*m.b28
                        - 32*m.b4*m.b17*m.b29 - 224*m.b4*m.b18*m.b19 - 192*m.b4*m.b18*m.b20 - 160*m.b4*m.b18*m.b21 - 128
                       *m.b4*m.b18*m.b22 - 128*m.b4*m.b18*m.b23 - 128*m.b4*m.b18*m.b24 - 128*m.b4*m.b18*m.b25 - 128*m.b4
                       *m.b18*m.b26 - 96*m.b4*m.b18*m.b27 - 64*m.b4*m.b18*m.b28 - 32*m.b4*m.b18*m.b29 - 224*m.b4*m.b19*
                       m.b20 - 192*m.b4*m.b19*m.b21 - 160*m.b4*m.b19*m.b22 - 128*m.b4*m.b19*m.b23 - 128*m.b4*m.b19*m.b24
                        - 128*m.b4*m.b19*m.b25 - 128*m.b4*m.b19*m.b26 - 96*m.b4*m.b19*m.b27 - 64*m.b4*m.b19*m.b28 - 32*
                       m.b4*m.b19*m.b29 - 224*m.b4*m.b20*m.b21 - 192*m.b4*m.b20*m.b22 - 160*m.b4*m.b20*m.b23 - 128*m.b4*
                       m.b20*m.b24 - 128*m.b4*m.b20*m.b25 - 128*m.b4*m.b20*m.b26 - 96*m.b4*m.b20*m.b27 - 64*m.b4*m.b20*
                       m.b28 - 32*m.b4*m.b20*m.b29 - 224*m.b4*m.b21*m.b22 - 192*m.b4*m.b21*m.b23 - 160*m.b4*m.b21*m.b24
                        - 128*m.b4*m.b21*m.b25 - 128*m.b4*m.b21*m.b26 - 96*m.b4*m.b21*m.b27 - 64*m.b4*m.b21*m.b28 - 32*
                       m.b4*m.b21*m.b29 - 224*m.b4*m.b22*m.b23 - 192*m.b4*m.b22*m.b24 - 160*m.b4*m.b22*m.b25 - 128*m.b4*
                       m.b22*m.b26 - 96*m.b4*m.b22*m.b27 - 64*m.b4*m.b22*m.b28 - 32*m.b4*m.b22*m.b29 - 224*m.b4*m.b23*
                       m.b24 - 192*m.b4*m.b23*m.b25 - 160*m.b4*m.b23*m.b26 - 96*m.b4*m.b23*m.b27 - 64*m.b4*m.b23*m.b28
                        - 32*m.b4*m.b23*m.b29 - 224*m.b4*m.b24*m.b25 - 192*m.b4*m.b24*m.b26 - 96*m.b4*m.b24*m.b27 - 64*
                       m.b4*m.b24*m.b28 - 32*m.b4*m.b24*m.b29 - 224*m.b4*m.b25*m.b26 - 128*m.b4*m.b25*m.b27 - 64*m.b4*
                       m.b25*m.b28 - 32*m.b4*m.b25*m.b29 - 160*m.b4*m.b26*m.b27 - 64*m.b4*m.b26*m.b28 - 32*m.b4*m.b26*
                       m.b29 - 96*m.b4*m.b27*m.b28 - 32*m.b4*m.b27*m.b29 - 32*m.b4*m.b28*m.b29 - 288*m.b5*m.b6*m.b7 - 
                       416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*m.b6*m.b11 - 320*m.b5*
                       m.b6*m.b12 - 320*m.b5*m.b6*m.b13 - 320*m.b5*m.b6*m.b14 - 320*m.b5*m.b6*m.b15 - 320*m.b5*m.b6*
                       m.b16 - 320*m.b5*m.b6*m.b17 - 320*m.b5*m.b6*m.b18 - 320*m.b5*m.b6*m.b19 - 320*m.b5*m.b6*m.b20 - 
                       320*m.b5*m.b6*m.b21 - 320*m.b5*m.b6*m.b22 - 320*m.b5*m.b6*m.b23 - 320*m.b5*m.b6*m.b24 - 320*m.b5*
                       m.b6*m.b25 - 288*m.b5*m.b6*m.b26 - 224*m.b5*m.b6*m.b27 - 160*m.b5*m.b6*m.b28 - 96*m.b5*m.b6*m.b29
                        - 32*m.b5*m.b6*m.b30 - 448*m.b5*m.b7*m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*
                       m.b7*m.b11 - 320*m.b5*m.b7*m.b12 - 320*m.b5*m.b7*m.b13 - 320*m.b5*m.b7*m.b14 - 320*m.b5*m.b7*
                       m.b15 - 320*m.b5*m.b7*m.b16 - 320*m.b5*m.b7*m.b17 - 320*m.b5*m.b7*m.b18 - 320*m.b5*m.b7*m.b19 - 
                       320*m.b5*m.b7*m.b20 - 320*m.b5*m.b7*m.b21 - 320*m.b5*m.b7*m.b22 - 320*m.b5*m.b7*m.b23 - 320*m.b5*
                       m.b7*m.b24 - 288*m.b5*m.b7*m.b25 - 256*m.b5*m.b7*m.b26 - 192*m.b5*m.b7*m.b27 - 128*m.b5*m.b7*
                       m.b28 - 64*m.b5*m.b7*m.b29 - 32*m.b5*m.b7*m.b30 - 448*m.b5*m.b8*m.b9 - 416*m.b5*m.b8*m.b10 - 224*
                       m.b5*m.b8*m.b11 - 352*m.b5*m.b8*m.b12 - 320*m.b5*m.b8*m.b13 - 320*m.b5*m.b8*m.b14 - 320*m.b5*m.b8
                       *m.b15 - 320*m.b5*m.b8*m.b16 - 320*m.b5*m.b8*m.b17 - 320*m.b5*m.b8*m.b18 - 320*m.b5*m.b8*m.b19 - 
                       320*m.b5*m.b8*m.b20 - 320*m.b5*m.b8*m.b21 - 320*m.b5*m.b8*m.b22 - 320*m.b5*m.b8*m.b23 - 288*m.b5*
                       m.b8*m.b24 - 256*m.b5*m.b8*m.b25 - 224*m.b5*m.b8*m.b26 - 160*m.b5*m.b8*m.b27 - 96*m.b5*m.b8*m.b28
                        - 64*m.b5*m.b8*m.b29 - 32*m.b5*m.b8*m.b30 - 448*m.b5*m.b9*m.b10 - 416*m.b5*m.b9*m.b11 - 384*m.b5
                       *m.b9*m.b12 - 192*m.b5*m.b9*m.b13 - 320*m.b5*m.b9*m.b14 - 320*m.b5*m.b9*m.b15 - 320*m.b5*m.b9*
                       m.b16 - 320*m.b5*m.b9*m.b17 - 320*m.b5*m.b9*m.b18 - 320*m.b5*m.b9*m.b19 - 320*m.b5*m.b9*m.b20 - 
                       320*m.b5*m.b9*m.b21 - 320*m.b5*m.b9*m.b22 - 288*m.b5*m.b9*m.b23 - 256*m.b5*m.b9*m.b24 - 224*m.b5*
                       m.b9*m.b25 - 192*m.b5*m.b9*m.b26 - 128*m.b5*m.b9*m.b27 - 96*m.b5*m.b9*m.b28 - 64*m.b5*m.b9*m.b29
                        - 32*m.b5*m.b9*m.b30 - 448*m.b5*m.b10*m.b11 - 416*m.b5*m.b10*m.b12 - 384*m.b5*m.b10*m.b13 - 352*
                       m.b5*m.b10*m.b14 - 160*m.b5*m.b10*m.b15 - 320*m.b5*m.b10*m.b16 - 320*m.b5*m.b10*m.b17 - 320*m.b5*
                       m.b10*m.b18 - 320*m.b5*m.b10*m.b19 - 320*m.b5*m.b10*m.b20 - 320*m.b5*m.b10*m.b21 - 288*m.b5*m.b10
                       *m.b22 - 256*m.b5*m.b10*m.b23 - 224*m.b5*m.b10*m.b24 - 192*m.b5*m.b10*m.b25 - 160*m.b5*m.b10*
                       m.b26 - 128*m.b5*m.b10*m.b27 - 96*m.b5*m.b10*m.b28 - 64*m.b5*m.b10*m.b29 - 32*m.b5*m.b10*m.b30 - 
                       448*m.b5*m.b11*m.b12 - 416*m.b5*m.b11*m.b13 - 384*m.b5*m.b11*m.b14 - 352*m.b5*m.b11*m.b15 - 320*
                       m.b5*m.b11*m.b16 - 160*m.b5*m.b11*m.b17 - 320*m.b5*m.b11*m.b18 - 320*m.b5*m.b11*m.b19 - 320*m.b5*
                       m.b11*m.b20 - 288*m.b5*m.b11*m.b21 - 256*m.b5*m.b11*m.b22 - 224*m.b5*m.b11*m.b23 - 192*m.b5*m.b11
                       *m.b24 - 160*m.b5*m.b11*m.b25 - 160*m.b5*m.b11*m.b26 - 128*m.b5*m.b11*m.b27 - 96*m.b5*m.b11*m.b28
                        - 64*m.b5*m.b11*m.b29 - 32*m.b5*m.b11*m.b30 - 448*m.b5*m.b12*m.b13 - 416*m.b5*m.b12*m.b14 - 384*
                       m.b5*m.b12*m.b15 - 352*m.b5*m.b12*m.b16 - 320*m.b5*m.b12*m.b17 - 320*m.b5*m.b12*m.b18 - 160*m.b5*
                       m.b12*m.b19 - 288*m.b5*m.b12*m.b20 - 256*m.b5*m.b12*m.b21 - 224*m.b5*m.b12*m.b22 - 192*m.b5*m.b12
                       *m.b23 - 160*m.b5*m.b12*m.b24 - 160*m.b5*m.b12*m.b25 - 160*m.b5*m.b12*m.b26 - 128*m.b5*m.b12*
                       m.b27 - 96*m.b5*m.b12*m.b28 - 64*m.b5*m.b12*m.b29 - 32*m.b5*m.b12*m.b30 - 448*m.b5*m.b13*m.b14 - 
                       416*m.b5*m.b13*m.b15 - 384*m.b5*m.b13*m.b16 - 352*m.b5*m.b13*m.b17 - 320*m.b5*m.b13*m.b18 - 288*
                       m.b5*m.b13*m.b19 - 256*m.b5*m.b13*m.b20 - 64*m.b5*m.b13*m.b21 - 192*m.b5*m.b13*m.b22 - 160*m.b5*
                       m.b13*m.b23 - 160*m.b5*m.b13*m.b24 - 160*m.b5*m.b13*m.b25 - 160*m.b5*m.b13*m.b26 - 128*m.b5*m.b13
                       *m.b27 - 96*m.b5*m.b13*m.b28 - 64*m.b5*m.b13*m.b29 - 32*m.b5*m.b13*m.b30 - 448*m.b5*m.b14*m.b15
                        - 416*m.b5*m.b14*m.b16 - 384*m.b5*m.b14*m.b17 - 320*m.b5*m.b14*m.b18 - 256*m.b5*m.b14*m.b19 - 
                       224*m.b5*m.b14*m.b20 - 192*m.b5*m.b14*m.b21 - 160*m.b5*m.b14*m.b22 - 160*m.b5*m.b14*m.b24 - 160*
                       m.b5*m.b14*m.b25 - 160*m.b5*m.b14*m.b26 - 128*m.b5*m.b14*m.b27 - 96*m.b5*m.b14*m.b28 - 64*m.b5*
                       m.b14*m.b29 - 32*m.b5*m.b14*m.b30 - 448*m.b5*m.b15*m.b16 - 384*m.b5*m.b15*m.b17 - 320*m.b5*m.b15*
                       m.b18 - 256*m.b5*m.b15*m.b19 - 192*m.b5*m.b15*m.b20 - 160*m.b5*m.b15*m.b21 - 160*m.b5*m.b15*m.b22
                        - 160*m.b5*m.b15*m.b23 - 160*m.b5*m.b15*m.b24 - 160*m.b5*m.b15*m.b26 - 128*m.b5*m.b15*m.b27 - 96
                       *m.b5*m.b15*m.b28 - 64*m.b5*m.b15*m.b29 - 32*m.b5*m.b15*m.b30 - 384*m.b5*m.b16*m.b17 - 320*m.b5*
                       m.b16*m.b18 - 256*m.b5*m.b16*m.b19 - 192*m.b5*m.b16*m.b20 - 160*m.b5*m.b16*m.b21 - 160*m.b5*m.b16
                       *m.b22 - 160*m.b5*m.b16*m.b23 - 160*m.b5*m.b16*m.b24 - 160*m.b5*m.b16*m.b25 - 160*m.b5*m.b16*
                       m.b26 - 96*m.b5*m.b16*m.b28 - 64*m.b5*m.b16*m.b29 - 32*m.b5*m.b16*m.b30 - 320*m.b5*m.b17*m.b18 - 
                       256*m.b5*m.b17*m.b19 - 224*m.b5*m.b17*m.b20 - 192*m.b5*m.b17*m.b21 - 160*m.b5*m.b17*m.b22 - 160*
                       m.b5*m.b17*m.b23 - 160*m.b5*m.b17*m.b24 - 160*m.b5*m.b17*m.b25 - 160*m.b5*m.b17*m.b26 - 128*m.b5*
                       m.b17*m.b27 - 96*m.b5*m.b17*m.b28 - 32*m.b5*m.b17*m.b30 - 288*m.b5*m.b18*m.b19 - 256*m.b5*m.b18*
                       m.b20 - 224*m.b5*m.b18*m.b21 - 192*m.b5*m.b18*m.b22 - 160*m.b5*m.b18*m.b23 - 160*m.b5*m.b18*m.b24
                        - 160*m.b5*m.b18*m.b25 - 160*m.b5*m.b18*m.b26 - 128*m.b5*m.b18*m.b27 - 96*m.b5*m.b18*m.b28 - 64*
                       m.b5*m.b18*m.b29 - 32*m.b5*m.b18*m.b30 - 288*m.b5*m.b19*m.b20 - 256*m.b5*m.b19*m.b21 - 224*m.b5*
                       m.b19*m.b22 - 192*m.b5*m.b19*m.b23 - 160*m.b5*m.b19*m.b24 - 160*m.b5*m.b19*m.b25 - 160*m.b5*m.b19
                       *m.b26 - 128*m.b5*m.b19*m.b27 - 96*m.b5*m.b19*m.b28 - 64*m.b5*m.b19*m.b29 - 32*m.b5*m.b19*m.b30
                        - 288*m.b5*m.b20*m.b21 - 256*m.b5*m.b20*m.b22 - 224*m.b5*m.b20*m.b23 - 192*m.b5*m.b20*m.b24 - 
                       160*m.b5*m.b20*m.b25 - 160*m.b5*m.b20*m.b26 - 128*m.b5*m.b20*m.b27 - 96*m.b5*m.b20*m.b28 - 64*
                       m.b5*m.b20*m.b29 - 32*m.b5*m.b20*m.b30 - 288*m.b5*m.b21*m.b22 - 256*m.b5*m.b21*m.b23 - 224*m.b5*
                       m.b21*m.b24 - 192*m.b5*m.b21*m.b25 - 160*m.b5*m.b21*m.b26 - 128*m.b5*m.b21*m.b27 - 96*m.b5*m.b21*
                       m.b28 - 64*m.b5*m.b21*m.b29 - 32*m.b5*m.b21*m.b30 - 288*m.b5*m.b22*m.b23 - 256*m.b5*m.b22*m.b24
                        - 224*m.b5*m.b22*m.b25 - 192*m.b5*m.b22*m.b26 - 128*m.b5*m.b22*m.b27 - 96*m.b5*m.b22*m.b28 - 64*
                       m.b5*m.b22*m.b29 - 32*m.b5*m.b22*m.b30 - 288*m.b5*m.b23*m.b24 - 256*m.b5*m.b23*m.b25 - 224*m.b5*
                       m.b23*m.b26 - 128*m.b5*m.b23*m.b27 - 96*m.b5*m.b23*m.b28 - 64*m.b5*m.b23*m.b29 - 32*m.b5*m.b23*
                       m.b30 - 288*m.b5*m.b24*m.b25 - 256*m.b5*m.b24*m.b26 - 160*m.b5*m.b24*m.b27 - 96*m.b5*m.b24*m.b28
                        - 64*m.b5*m.b24*m.b29 - 32*m.b5*m.b24*m.b30 - 288*m.b5*m.b25*m.b26 - 192*m.b5*m.b25*m.b27 - 96*
                       m.b5*m.b25*m.b28 - 64*m.b5*m.b25*m.b29 - 32*m.b5*m.b25*m.b30 - 224*m.b5*m.b26*m.b27 - 128*m.b5*
                       m.b26*m.b28 - 64*m.b5*m.b26*m.b29 - 32*m.b5*m.b26*m.b30 - 160*m.b5*m.b27*m.b28 - 64*m.b5*m.b27*
                       m.b29 - 32*m.b5*m.b27*m.b30 - 96*m.b5*m.b28*m.b29 - 32*m.b5*m.b28*m.b30 - 32*m.b5*m.b29*m.b30 - 
                       352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*m.b7*m.b11 - 416*m.b6*
                       m.b7*m.b12 - 384*m.b6*m.b7*m.b13 - 384*m.b6*m.b7*m.b14 - 384*m.b6*m.b7*m.b15 - 384*m.b6*m.b7*
                       m.b16 - 384*m.b6*m.b7*m.b17 - 384*m.b6*m.b7*m.b18 - 384*m.b6*m.b7*m.b19 - 384*m.b6*m.b7*m.b20 - 
                       384*m.b6*m.b7*m.b21 - 384*m.b6*m.b7*m.b22 - 384*m.b6*m.b7*m.b23 - 384*m.b6*m.b7*m.b24 - 384*m.b6*
                       m.b7*m.b25 - 352*m.b6*m.b7*m.b26 - 288*m.b6*m.b7*m.b27 - 224*m.b6*m.b7*m.b28 - 160*m.b6*m.b7*
                       m.b29 - 96*m.b6*m.b7*m.b30 - 32*m.b6*m.b7*m.b31 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*
                       m.b6*m.b8*m.b11 - 448*m.b6*m.b8*m.b12 - 416*m.b6*m.b8*m.b13 - 384*m.b6*m.b8*m.b14 - 384*m.b6*m.b8
                       *m.b15 - 384*m.b6*m.b8*m.b16 - 384*m.b6*m.b8*m.b17 - 384*m.b6*m.b8*m.b18 - 384*m.b6*m.b8*m.b19 - 
                       384*m.b6*m.b8*m.b20 - 384*m.b6*m.b8*m.b21 - 384*m.b6*m.b8*m.b22 - 384*m.b6*m.b8*m.b23 - 384*m.b6*
                       m.b8*m.b24 - 352*m.b6*m.b8*m.b25 - 320*m.b6*m.b8*m.b26 - 256*m.b6*m.b8*m.b27 - 192*m.b6*m.b8*
                       m.b28 - 128*m.b6*m.b8*m.b29 - 64*m.b6*m.b8*m.b30 - 32*m.b6*m.b8*m.b31 - 544*m.b6*m.b9*m.b10 - 512
                       *m.b6*m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 448*m.b6*m.b9*m.b13 - 416*m.b6*m.b9*m.b14 - 384*m.b6*
                       m.b9*m.b15 - 384*m.b6*m.b9*m.b16 - 384*m.b6*m.b9*m.b17 - 384*m.b6*m.b9*m.b18 - 384*m.b6*m.b9*
                       m.b19 - 384*m.b6*m.b9*m.b20 - 384*m.b6*m.b9*m.b21 - 384*m.b6*m.b9*m.b22 - 384*m.b6*m.b9*m.b23 - 
                       352*m.b6*m.b9*m.b24 - 320*m.b6*m.b9*m.b25 - 288*m.b6*m.b9*m.b26 - 224*m.b6*m.b9*m.b27 - 160*m.b6*
                       m.b9*m.b28 - 96*m.b6*m.b9*m.b29 - 64*m.b6*m.b9*m.b30 - 32*m.b6*m.b9*m.b31 - 544*m.b6*m.b10*m.b11
                        - 512*m.b6*m.b10*m.b12 - 480*m.b6*m.b10*m.b13 - 256*m.b6*m.b10*m.b14 - 416*m.b6*m.b10*m.b15 - 
                       384*m.b6*m.b10*m.b16 - 384*m.b6*m.b10*m.b17 - 384*m.b6*m.b10*m.b18 - 384*m.b6*m.b10*m.b19 - 384*
                       m.b6*m.b10*m.b20 - 384*m.b6*m.b10*m.b21 - 384*m.b6*m.b10*m.b22 - 352*m.b6*m.b10*m.b23 - 320*m.b6*
                       m.b10*m.b24 - 288*m.b6*m.b10*m.b25 - 256*m.b6*m.b10*m.b26 - 192*m.b6*m.b10*m.b27 - 128*m.b6*m.b10
                       *m.b28 - 96*m.b6*m.b10*m.b29 - 64*m.b6*m.b10*m.b30 - 32*m.b6*m.b10*m.b31 - 544*m.b6*m.b11*m.b12
                        - 512*m.b6*m.b11*m.b13 - 480*m.b6*m.b11*m.b14 - 448*m.b6*m.b11*m.b15 - 224*m.b6*m.b11*m.b16 - 
                       384*m.b6*m.b11*m.b17 - 384*m.b6*m.b11*m.b18 - 384*m.b6*m.b11*m.b19 - 384*m.b6*m.b11*m.b20 - 384*
                       m.b6*m.b11*m.b21 - 352*m.b6*m.b11*m.b22 - 320*m.b6*m.b11*m.b23 - 288*m.b6*m.b11*m.b24 - 256*m.b6*
                       m.b11*m.b25 - 224*m.b6*m.b11*m.b26 - 160*m.b6*m.b11*m.b27 - 128*m.b6*m.b11*m.b28 - 96*m.b6*m.b11*
                       m.b29 - 64*m.b6*m.b11*m.b30 - 32*m.b6*m.b11*m.b31 - 544*m.b6*m.b12*m.b13 - 512*m.b6*m.b12*m.b14
                        - 480*m.b6*m.b12*m.b15 - 448*m.b6*m.b12*m.b16 - 416*m.b6*m.b12*m.b17 - 192*m.b6*m.b12*m.b18 - 
                       384*m.b6*m.b12*m.b19 - 384*m.b6*m.b12*m.b20 - 352*m.b6*m.b12*m.b21 - 320*m.b6*m.b12*m.b22 - 288*
                       m.b6*m.b12*m.b23 - 256*m.b6*m.b12*m.b24 - 224*m.b6*m.b12*m.b25 - 192*m.b6*m.b12*m.b26 - 160*m.b6*
                       m.b12*m.b27 - 128*m.b6*m.b12*m.b28 - 96*m.b6*m.b12*m.b29 - 64*m.b6*m.b12*m.b30 - 32*m.b6*m.b12*
                       m.b31 - 544*m.b6*m.b13*m.b14 - 512*m.b6*m.b13*m.b15 - 480*m.b6*m.b13*m.b16 - 448*m.b6*m.b13*m.b17
                        - 416*m.b6*m.b13*m.b18 - 384*m.b6*m.b13*m.b19 - 160*m.b6*m.b13*m.b20 - 320*m.b6*m.b13*m.b21 - 
                       288*m.b6*m.b13*m.b22 - 256*m.b6*m.b13*m.b23 - 224*m.b6*m.b13*m.b24 - 192*m.b6*m.b13*m.b25 - 192*
                       m.b6*m.b13*m.b26 - 160*m.b6*m.b13*m.b27 - 128*m.b6*m.b13*m.b28 - 96*m.b6*m.b13*m.b29 - 64*m.b6*
                       m.b13*m.b30 - 32*m.b6*m.b13*m.b31 - 544*m.b6*m.b14*m.b15 - 512*m.b6*m.b14*m.b16 - 480*m.b6*m.b14*
                       m.b17 - 448*m.b6*m.b14*m.b18 - 384*m.b6*m.b14*m.b19 - 320*m.b6*m.b14*m.b20 - 288*m.b6*m.b14*m.b21
                        - 64*m.b6*m.b14*m.b22 - 224*m.b6*m.b14*m.b23 - 192*m.b6*m.b14*m.b24 - 192*m.b6*m.b14*m.b25 - 192
                       *m.b6*m.b14*m.b26 - 160*m.b6*m.b14*m.b27 - 128*m.b6*m.b14*m.b28 - 96*m.b6*m.b14*m.b29 - 64*m.b6*
                       m.b14*m.b30 - 32*m.b6*m.b14*m.b31 - 544*m.b6*m.b15*m.b16 - 512*m.b6*m.b15*m.b17 - 448*m.b6*m.b15*
                       m.b18 - 384*m.b6*m.b15*m.b19 - 320*m.b6*m.b15*m.b20 - 256*m.b6*m.b15*m.b21 - 224*m.b6*m.b15*m.b22
                        - 192*m.b6*m.b15*m.b23 - 192*m.b6*m.b15*m.b25 - 192*m.b6*m.b15*m.b26 - 160*m.b6*m.b15*m.b27 - 
                       128*m.b6*m.b15*m.b28 - 96*m.b6*m.b15*m.b29 - 64*m.b6*m.b15*m.b30 - 32*m.b6*m.b15*m.b31 - 512*m.b6
                       *m.b16*m.b17 - 448*m.b6*m.b16*m.b18 - 384*m.b6*m.b16*m.b19 - 320*m.b6*m.b16*m.b20 - 256*m.b6*
                       m.b16*m.b21 - 192*m.b6*m.b16*m.b22 - 192*m.b6*m.b16*m.b23 - 192*m.b6*m.b16*m.b24 - 192*m.b6*m.b16
                       *m.b25 - 160*m.b6*m.b16*m.b27 - 128*m.b6*m.b16*m.b28 - 96*m.b6*m.b16*m.b29 - 64*m.b6*m.b16*m.b30
                        - 32*m.b6*m.b16*m.b31 - 448*m.b6*m.b17*m.b18 - 384*m.b6*m.b17*m.b19 - 320*m.b6*m.b17*m.b20 - 256
                       *m.b6*m.b17*m.b21 - 224*m.b6*m.b17*m.b22 - 192*m.b6*m.b17*m.b23 - 192*m.b6*m.b17*m.b24 - 192*m.b6
                       *m.b17*m.b25 - 192*m.b6*m.b17*m.b26 - 160*m.b6*m.b17*m.b27 - 96*m.b6*m.b17*m.b29 - 64*m.b6*m.b17*
                       m.b30 - 32*m.b6*m.b17*m.b31 - 384*m.b6*m.b18*m.b19 - 320*m.b6*m.b18*m.b20 - 288*m.b6*m.b18*m.b21
                        - 256*m.b6*m.b18*m.b22 - 224*m.b6*m.b18*m.b23 - 192*m.b6*m.b18*m.b24 - 192*m.b6*m.b18*m.b25 - 
                       192*m.b6*m.b18*m.b26 - 160*m.b6*m.b18*m.b27 - 128*m.b6*m.b18*m.b28 - 96*m.b6*m.b18*m.b29 - 32*
                       m.b6*m.b18*m.b31 - 352*m.b6*m.b19*m.b20 - 320*m.b6*m.b19*m.b21 - 288*m.b6*m.b19*m.b22 - 256*m.b6*
                       m.b19*m.b23 - 224*m.b6*m.b19*m.b24 - 192*m.b6*m.b19*m.b25 - 192*m.b6*m.b19*m.b26 - 160*m.b6*m.b19
                       *m.b27 - 128*m.b6*m.b19*m.b28 - 96*m.b6*m.b19*m.b29 - 64*m.b6*m.b19*m.b30 - 32*m.b6*m.b19*m.b31
                        - 352*m.b6*m.b20*m.b21 - 320*m.b6*m.b20*m.b22 - 288*m.b6*m.b20*m.b23 - 256*m.b6*m.b20*m.b24 - 
                       224*m.b6*m.b20*m.b25 - 192*m.b6*m.b20*m.b26 - 160*m.b6*m.b20*m.b27 - 128*m.b6*m.b20*m.b28 - 96*
                       m.b6*m.b20*m.b29 - 64*m.b6*m.b20*m.b30 - 32*m.b6*m.b20*m.b31 - 352*m.b6*m.b21*m.b22 - 320*m.b6*
                       m.b21*m.b23 - 288*m.b6*m.b21*m.b24 - 256*m.b6*m.b21*m.b25 - 224*m.b6*m.b21*m.b26 - 160*m.b6*m.b21
                       *m.b27 - 128*m.b6*m.b21*m.b28 - 96*m.b6*m.b21*m.b29 - 64*m.b6*m.b21*m.b30 - 32*m.b6*m.b21*m.b31
                        - 352*m.b6*m.b22*m.b23 - 320*m.b6*m.b22*m.b24 - 288*m.b6*m.b22*m.b25 - 256*m.b6*m.b22*m.b26 - 
                       160*m.b6*m.b22*m.b27 - 128*m.b6*m.b22*m.b28 - 96*m.b6*m.b22*m.b29 - 64*m.b6*m.b22*m.b30 - 32*m.b6
                       *m.b22*m.b31 - 352*m.b6*m.b23*m.b24 - 320*m.b6*m.b23*m.b25 - 288*m.b6*m.b23*m.b26 - 192*m.b6*
                       m.b23*m.b27 - 128*m.b6*m.b23*m.b28 - 96*m.b6*m.b23*m.b29 - 64*m.b6*m.b23*m.b30 - 32*m.b6*m.b23*
                       m.b31 - 352*m.b6*m.b24*m.b25 - 320*m.b6*m.b24*m.b26 - 224*m.b6*m.b24*m.b27 - 128*m.b6*m.b24*m.b28
                        - 96*m.b6*m.b24*m.b29 - 64*m.b6*m.b24*m.b30 - 32*m.b6*m.b24*m.b31 - 352*m.b6*m.b25*m.b26 - 256*
                       m.b6*m.b25*m.b27 - 160*m.b6*m.b25*m.b28 - 96*m.b6*m.b25*m.b29 - 64*m.b6*m.b25*m.b30 - 32*m.b6*
                       m.b25*m.b31 - 288*m.b6*m.b26*m.b27 - 192*m.b6*m.b26*m.b28 - 96*m.b6*m.b26*m.b29 - 64*m.b6*m.b26*
                       m.b30 - 32*m.b6*m.b26*m.b31 - 224*m.b6*m.b27*m.b28 - 128*m.b6*m.b27*m.b29 - 64*m.b6*m.b27*m.b30
                        - 32*m.b6*m.b27*m.b31 - 160*m.b6*m.b28*m.b29 - 64*m.b6*m.b28*m.b30 - 32*m.b6*m.b28*m.b31 - 96*
                       m.b6*m.b29*m.b30 - 32*m.b6*m.b29*m.b31 - 32*m.b6*m.b30*m.b31 - 416*m.b7*m.b8*m.b9 - 608*m.b7*m.b8
                       *m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 512*m.b7*m.b8*m.b13 - 480*m.b7*m.b8*m.b14 - 
                       448*m.b7*m.b8*m.b15 - 448*m.b7*m.b8*m.b16 - 448*m.b7*m.b8*m.b17 - 448*m.b7*m.b8*m.b18 - 448*m.b7*
                       m.b8*m.b19 - 448*m.b7*m.b8*m.b20 - 448*m.b7*m.b8*m.b21 - 448*m.b7*m.b8*m.b22 - 448*m.b7*m.b8*
                       m.b23 - 448*m.b7*m.b8*m.b24 - 448*m.b7*m.b8*m.b25 - 416*m.b7*m.b8*m.b26 - 352*m.b7*m.b8*m.b27 - 
                       288*m.b7*m.b8*m.b28 - 224*m.b7*m.b8*m.b29 - 160*m.b7*m.b8*m.b30 - 96*m.b7*m.b8*m.b31 - 32*m.b7*
                       m.b8*m.b32 - 640*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11 - 576*m.b7*m.b9*m.b12 - 544*m.b7*m.b9*
                       m.b13 - 512*m.b7*m.b9*m.b14 - 480*m.b7*m.b9*m.b15 - 448*m.b7*m.b9*m.b16 - 448*m.b7*m.b9*m.b17 - 
                       448*m.b7*m.b9*m.b18 - 448*m.b7*m.b9*m.b19 - 448*m.b7*m.b9*m.b20 - 448*m.b7*m.b9*m.b21 - 448*m.b7*
                       m.b9*m.b22 - 448*m.b7*m.b9*m.b23 - 448*m.b7*m.b9*m.b24 - 416*m.b7*m.b9*m.b25 - 384*m.b7*m.b9*
                       m.b26 - 320*m.b7*m.b9*m.b27 - 256*m.b7*m.b9*m.b28 - 192*m.b7*m.b9*m.b29 - 128*m.b7*m.b9*m.b30 - 
                       64*m.b7*m.b9*m.b31 - 32*m.b7*m.b9*m.b32 - 640*m.b7*m.b10*m.b11 - 608*m.b7*m.b10*m.b12 - 352*m.b7*
                       m.b10*m.b13 - 544*m.b7*m.b10*m.b14 - 512*m.b7*m.b10*m.b15 - 480*m.b7*m.b10*m.b16 - 448*m.b7*m.b10
                       *m.b17 - 448*m.b7*m.b10*m.b18 - 448*m.b7*m.b10*m.b19 - 448*m.b7*m.b10*m.b20 - 448*m.b7*m.b10*
                       m.b21 - 448*m.b7*m.b10*m.b22 - 448*m.b7*m.b10*m.b23 - 416*m.b7*m.b10*m.b24 - 384*m.b7*m.b10*m.b25
                        - 352*m.b7*m.b10*m.b26 - 288*m.b7*m.b10*m.b27 - 224*m.b7*m.b10*m.b28 - 160*m.b7*m.b10*m.b29 - 96
                       *m.b7*m.b10*m.b30 - 64*m.b7*m.b10*m.b31 - 32*m.b7*m.b10*m.b32 - 640*m.b7*m.b11*m.b12 - 608*m.b7*
                       m.b11*m.b13 - 576*m.b7*m.b11*m.b14 - 320*m.b7*m.b11*m.b15 - 512*m.b7*m.b11*m.b16 - 480*m.b7*m.b11
                       *m.b17 - 448*m.b7*m.b11*m.b18 - 448*m.b7*m.b11*m.b19 - 448*m.b7*m.b11*m.b20 - 448*m.b7*m.b11*
                       m.b21 - 448*m.b7*m.b11*m.b22 - 416*m.b7*m.b11*m.b23 - 384*m.b7*m.b11*m.b24 - 352*m.b7*m.b11*m.b25
                        - 320*m.b7*m.b11*m.b26 - 256*m.b7*m.b11*m.b27 - 192*m.b7*m.b11*m.b28 - 128*m.b7*m.b11*m.b29 - 96
                       *m.b7*m.b11*m.b30 - 64*m.b7*m.b11*m.b31 - 32*m.b7*m.b11*m.b32 - 640*m.b7*m.b12*m.b13 - 608*m.b7*
                       m.b12*m.b14 - 576*m.b7*m.b12*m.b15 - 544*m.b7*m.b12*m.b16 - 288*m.b7*m.b12*m.b17 - 480*m.b7*m.b12
                       *m.b18 - 448*m.b7*m.b12*m.b19 - 448*m.b7*m.b12*m.b20 - 448*m.b7*m.b12*m.b21 - 416*m.b7*m.b12*
                       m.b22 - 384*m.b7*m.b12*m.b23 - 352*m.b7*m.b12*m.b24 - 320*m.b7*m.b12*m.b25 - 288*m.b7*m.b12*m.b26
                        - 224*m.b7*m.b12*m.b27 - 160*m.b7*m.b12*m.b28 - 128*m.b7*m.b12*m.b29 - 96*m.b7*m.b12*m.b30 - 64*
                       m.b7*m.b12*m.b31 - 32*m.b7*m.b12*m.b32 - 640*m.b7*m.b13*m.b14 - 608*m.b7*m.b13*m.b15 - 576*m.b7*
                       m.b13*m.b16 - 544*m.b7*m.b13*m.b17 - 512*m.b7*m.b13*m.b18 - 256*m.b7*m.b13*m.b19 - 448*m.b7*m.b13
                       *m.b20 - 416*m.b7*m.b13*m.b21 - 384*m.b7*m.b13*m.b22 - 352*m.b7*m.b13*m.b23 - 320*m.b7*m.b13*
                       m.b24 - 288*m.b7*m.b13*m.b25 - 256*m.b7*m.b13*m.b26 - 192*m.b7*m.b13*m.b27 - 160*m.b7*m.b13*m.b28
                        - 128*m.b7*m.b13*m.b29 - 96*m.b7*m.b13*m.b30 - 64*m.b7*m.b13*m.b31 - 32*m.b7*m.b13*m.b32 - 640*
                       m.b7*m.b14*m.b15 - 608*m.b7*m.b14*m.b16 - 576*m.b7*m.b14*m.b17 - 544*m.b7*m.b14*m.b18 - 512*m.b7*
                       m.b14*m.b19 - 448*m.b7*m.b14*m.b20 - 160*m.b7*m.b14*m.b21 - 352*m.b7*m.b14*m.b22 - 320*m.b7*m.b14
                       *m.b23 - 288*m.b7*m.b14*m.b24 - 256*m.b7*m.b14*m.b25 - 224*m.b7*m.b14*m.b26 - 192*m.b7*m.b14*
                       m.b27 - 160*m.b7*m.b14*m.b28 - 128*m.b7*m.b14*m.b29 - 96*m.b7*m.b14*m.b30 - 64*m.b7*m.b14*m.b31
                        - 32*m.b7*m.b14*m.b32 - 640*m.b7*m.b15*m.b16 - 608*m.b7*m.b15*m.b17 - 576*m.b7*m.b15*m.b18 - 512
                       *m.b7*m.b15*m.b19 - 448*m.b7*m.b15*m.b20 - 384*m.b7*m.b15*m.b21 - 320*m.b7*m.b15*m.b22 - 64*m.b7*
                       m.b15*m.b23 - 256*m.b7*m.b15*m.b24 - 224*m.b7*m.b15*m.b25 - 224*m.b7*m.b15*m.b26 - 192*m.b7*m.b15
                       *m.b27 - 160*m.b7*m.b15*m.b28 - 128*m.b7*m.b15*m.b29 - 96*m.b7*m.b15*m.b30 - 64*m.b7*m.b15*m.b31
                        - 32*m.b7*m.b15*m.b32 - 640*m.b7*m.b16*m.b17 - 576*m.b7*m.b16*m.b18 - 512*m.b7*m.b16*m.b19 - 448
                       *m.b7*m.b16*m.b20 - 384*m.b7*m.b16*m.b21 - 320*m.b7*m.b16*m.b22 - 256*m.b7*m.b16*m.b23 - 224*m.b7
                       *m.b16*m.b24 - 224*m.b7*m.b16*m.b26 - 192*m.b7*m.b16*m.b27 - 160*m.b7*m.b16*m.b28 - 128*m.b7*
                       m.b16*m.b29 - 96*m.b7*m.b16*m.b30 - 64*m.b7*m.b16*m.b31 - 32*m.b7*m.b16*m.b32 - 576*m.b7*m.b17*
                       m.b18 - 512*m.b7*m.b17*m.b19 - 448*m.b7*m.b17*m.b20 - 384*m.b7*m.b17*m.b21 - 320*m.b7*m.b17*m.b22
                        - 256*m.b7*m.b17*m.b23 - 224*m.b7*m.b17*m.b24 - 224*m.b7*m.b17*m.b25 - 224*m.b7*m.b17*m.b26 - 
                       160*m.b7*m.b17*m.b28 - 128*m.b7*m.b17*m.b29 - 96*m.b7*m.b17*m.b30 - 64*m.b7*m.b17*m.b31 - 32*m.b7
                       *m.b17*m.b32 - 512*m.b7*m.b18*m.b19 - 448*m.b7*m.b18*m.b20 - 384*m.b7*m.b18*m.b21 - 320*m.b7*
                       m.b18*m.b22 - 288*m.b7*m.b18*m.b23 - 256*m.b7*m.b18*m.b24 - 224*m.b7*m.b18*m.b25 - 224*m.b7*m.b18
                       *m.b26 - 192*m.b7*m.b18*m.b27 - 160*m.b7*m.b18*m.b28 - 96*m.b7*m.b18*m.b30 - 64*m.b7*m.b18*m.b31
                        - 32*m.b7*m.b18*m.b32 - 448*m.b7*m.b19*m.b20 - 384*m.b7*m.b19*m.b21 - 352*m.b7*m.b19*m.b22 - 320
                       *m.b7*m.b19*m.b23 - 288*m.b7*m.b19*m.b24 - 256*m.b7*m.b19*m.b25 - 224*m.b7*m.b19*m.b26 - 192*m.b7
                       *m.b19*m.b27 - 160*m.b7*m.b19*m.b28 - 128*m.b7*m.b19*m.b29 - 96*m.b7*m.b19*m.b30 - 32*m.b7*m.b19*
                       m.b32 - 416*m.b7*m.b20*m.b21 - 384*m.b7*m.b20*m.b22 - 352*m.b7*m.b20*m.b23 - 320*m.b7*m.b20*m.b24
                        - 288*m.b7*m.b20*m.b25 - 256*m.b7*m.b20*m.b26 - 192*m.b7*m.b20*m.b27 - 160*m.b7*m.b20*m.b28 - 
                       128*m.b7*m.b20*m.b29 - 96*m.b7*m.b20*m.b30 - 64*m.b7*m.b20*m.b31 - 32*m.b7*m.b20*m.b32 - 416*m.b7
                       *m.b21*m.b22 - 384*m.b7*m.b21*m.b23 - 352*m.b7*m.b21*m.b24 - 320*m.b7*m.b21*m.b25 - 288*m.b7*
                       m.b21*m.b26 - 192*m.b7*m.b21*m.b27 - 160*m.b7*m.b21*m.b28 - 128*m.b7*m.b21*m.b29 - 96*m.b7*m.b21*
                       m.b30 - 64*m.b7*m.b21*m.b31 - 32*m.b7*m.b21*m.b32 - 416*m.b7*m.b22*m.b23 - 384*m.b7*m.b22*m.b24
                        - 352*m.b7*m.b22*m.b25 - 320*m.b7*m.b22*m.b26 - 224*m.b7*m.b22*m.b27 - 160*m.b7*m.b22*m.b28 - 
                       128*m.b7*m.b22*m.b29 - 96*m.b7*m.b22*m.b30 - 64*m.b7*m.b22*m.b31 - 32*m.b7*m.b22*m.b32 - 416*m.b7
                       *m.b23*m.b24 - 384*m.b7*m.b23*m.b25 - 352*m.b7*m.b23*m.b26 - 256*m.b7*m.b23*m.b27 - 160*m.b7*
                       m.b23*m.b28 - 128*m.b7*m.b23*m.b29 - 96*m.b7*m.b23*m.b30 - 64*m.b7*m.b23*m.b31 - 32*m.b7*m.b23*
                       m.b32 - 416*m.b7*m.b24*m.b25 - 384*m.b7*m.b24*m.b26 - 288*m.b7*m.b24*m.b27 - 192*m.b7*m.b24*m.b28
                        - 128*m.b7*m.b24*m.b29 - 96*m.b7*m.b24*m.b30 - 64*m.b7*m.b24*m.b31 - 32*m.b7*m.b24*m.b32 - 416*
                       m.b7*m.b25*m.b26 - 320*m.b7*m.b25*m.b27 - 224*m.b7*m.b25*m.b28 - 128*m.b7*m.b25*m.b29 - 96*m.b7*
                       m.b25*m.b30 - 64*m.b7*m.b25*m.b31 - 32*m.b7*m.b25*m.b32 - 352*m.b7*m.b26*m.b27 - 256*m.b7*m.b26*
                       m.b28 - 160*m.b7*m.b26*m.b29 - 96*m.b7*m.b26*m.b30 - 64*m.b7*m.b26*m.b31 - 32*m.b7*m.b26*m.b32 - 
                       288*m.b7*m.b27*m.b28 - 192*m.b7*m.b27*m.b29 - 96*m.b7*m.b27*m.b30 - 64*m.b7*m.b27*m.b31 - 32*m.b7
                       *m.b27*m.b32 - 224*m.b7*m.b28*m.b29 - 128*m.b7*m.b28*m.b30 - 64*m.b7*m.b28*m.b31 - 32*m.b7*m.b28*
                       m.b32 - 160*m.b7*m.b29*m.b30 - 64*m.b7*m.b29*m.b31 - 32*m.b7*m.b29*m.b32 - 96*m.b7*m.b30*m.b31 - 
                       32*m.b7*m.b30*m.b32 - 32*m.b7*m.b31*m.b32 - 480*m.b8*m.b9*m.b10 - 704*m.b8*m.b9*m.b11 - 672*m.b8*
                       m.b9*m.b12 - 640*m.b8*m.b9*m.b13 - 608*m.b8*m.b9*m.b14 - 576*m.b8*m.b9*m.b15 - 544*m.b8*m.b9*
                       m.b16 - 512*m.b8*m.b9*m.b17 - 512*m.b8*m.b9*m.b18 - 512*m.b8*m.b9*m.b19 - 512*m.b8*m.b9*m.b20 - 
                       512*m.b8*m.b9*m.b21 - 512*m.b8*m.b9*m.b22 - 512*m.b8*m.b9*m.b23 - 512*m.b8*m.b9*m.b24 - 512*m.b8*
                       m.b9*m.b25 - 480*m.b8*m.b9*m.b26 - 416*m.b8*m.b9*m.b27 - 352*m.b8*m.b9*m.b28 - 288*m.b8*m.b9*
                       m.b29 - 224*m.b8*m.b9*m.b30 - 160*m.b8*m.b9*m.b31 - 96*m.b8*m.b9*m.b32 - 32*m.b8*m.b9*m.b33 - 736
                       *m.b8*m.b10*m.b11 - 448*m.b8*m.b10*m.b12 - 672*m.b8*m.b10*m.b13 - 640*m.b8*m.b10*m.b14 - 608*m.b8
                       *m.b10*m.b15 - 576*m.b8*m.b10*m.b16 - 544*m.b8*m.b10*m.b17 - 512*m.b8*m.b10*m.b18 - 512*m.b8*
                       m.b10*m.b19 - 512*m.b8*m.b10*m.b20 - 512*m.b8*m.b10*m.b21 - 512*m.b8*m.b10*m.b22 - 512*m.b8*m.b10
                       *m.b23 - 512*m.b8*m.b10*m.b24 - 480*m.b8*m.b10*m.b25 - 448*m.b8*m.b10*m.b26 - 384*m.b8*m.b10*
                       m.b27 - 320*m.b8*m.b10*m.b28 - 256*m.b8*m.b10*m.b29 - 192*m.b8*m.b10*m.b30 - 128*m.b8*m.b10*m.b31
                        - 64*m.b8*m.b10*m.b32 - 32*m.b8*m.b10*m.b33 - 736*m.b8*m.b11*m.b12 - 704*m.b8*m.b11*m.b13 - 416*
                       m.b8*m.b11*m.b14 - 640*m.b8*m.b11*m.b15 - 608*m.b8*m.b11*m.b16 - 576*m.b8*m.b11*m.b17 - 544*m.b8*
                       m.b11*m.b18 - 512*m.b8*m.b11*m.b19 - 512*m.b8*m.b11*m.b20 - 512*m.b8*m.b11*m.b21 - 512*m.b8*m.b11
                       *m.b22 - 512*m.b8*m.b11*m.b23 - 480*m.b8*m.b11*m.b24 - 448*m.b8*m.b11*m.b25 - 416*m.b8*m.b11*
                       m.b26 - 352*m.b8*m.b11*m.b27 - 288*m.b8*m.b11*m.b28 - 224*m.b8*m.b11*m.b29 - 160*m.b8*m.b11*m.b30
                        - 96*m.b8*m.b11*m.b31 - 64*m.b8*m.b11*m.b32 - 32*m.b8*m.b11*m.b33 - 736*m.b8*m.b12*m.b13 - 704*
                       m.b8*m.b12*m.b14 - 672*m.b8*m.b12*m.b15 - 384*m.b8*m.b12*m.b16 - 608*m.b8*m.b12*m.b17 - 576*m.b8*
                       m.b12*m.b18 - 544*m.b8*m.b12*m.b19 - 512*m.b8*m.b12*m.b20 - 512*m.b8*m.b12*m.b21 - 512*m.b8*m.b12
                       *m.b22 - 480*m.b8*m.b12*m.b23 - 448*m.b8*m.b12*m.b24 - 416*m.b8*m.b12*m.b25 - 384*m.b8*m.b12*
                       m.b26 - 320*m.b8*m.b12*m.b27 - 256*m.b8*m.b12*m.b28 - 192*m.b8*m.b12*m.b29 - 128*m.b8*m.b12*m.b30
                        - 96*m.b8*m.b12*m.b31 - 64*m.b8*m.b12*m.b32 - 32*m.b8*m.b12*m.b33 - 736*m.b8*m.b13*m.b14 - 704*
                       m.b8*m.b13*m.b15 - 672*m.b8*m.b13*m.b16 - 640*m.b8*m.b13*m.b17 - 352*m.b8*m.b13*m.b18 - 576*m.b8*
                       m.b13*m.b19 - 544*m.b8*m.b13*m.b20 - 512*m.b8*m.b13*m.b21 - 480*m.b8*m.b13*m.b22 - 448*m.b8*m.b13
                       *m.b23 - 416*m.b8*m.b13*m.b24 - 384*m.b8*m.b13*m.b25 - 352*m.b8*m.b13*m.b26 - 288*m.b8*m.b13*
                       m.b27 - 224*m.b8*m.b13*m.b28 - 160*m.b8*m.b13*m.b29 - 128*m.b8*m.b13*m.b30 - 96*m.b8*m.b13*m.b31
                        - 64*m.b8*m.b13*m.b32 - 32*m.b8*m.b13*m.b33 - 736*m.b8*m.b14*m.b15 - 704*m.b8*m.b14*m.b16 - 672*
                       m.b8*m.b14*m.b17 - 640*m.b8*m.b14*m.b18 - 608*m.b8*m.b14*m.b19 - 320*m.b8*m.b14*m.b20 - 512*m.b8*
                       m.b14*m.b21 - 448*m.b8*m.b14*m.b22 - 416*m.b8*m.b14*m.b23 - 384*m.b8*m.b14*m.b24 - 352*m.b8*m.b14
                       *m.b25 - 320*m.b8*m.b14*m.b26 - 256*m.b8*m.b14*m.b27 - 192*m.b8*m.b14*m.b28 - 160*m.b8*m.b14*
                       m.b29 - 128*m.b8*m.b14*m.b30 - 96*m.b8*m.b14*m.b31 - 64*m.b8*m.b14*m.b32 - 32*m.b8*m.b14*m.b33 - 
                       736*m.b8*m.b15*m.b16 - 704*m.b8*m.b15*m.b17 - 672*m.b8*m.b15*m.b18 - 640*m.b8*m.b15*m.b19 - 576*
                       m.b8*m.b15*m.b20 - 512*m.b8*m.b15*m.b21 - 192*m.b8*m.b15*m.b22 - 384*m.b8*m.b15*m.b23 - 352*m.b8*
                       m.b15*m.b24 - 320*m.b8*m.b15*m.b25 - 288*m.b8*m.b15*m.b26 - 224*m.b8*m.b15*m.b27 - 192*m.b8*m.b15
                       *m.b28 - 160*m.b8*m.b15*m.b29 - 128*m.b8*m.b15*m.b30 - 96*m.b8*m.b15*m.b31 - 64*m.b8*m.b15*m.b32
                        - 32*m.b8*m.b15*m.b33 - 736*m.b8*m.b16*m.b17 - 704*m.b8*m.b16*m.b18 - 640*m.b8*m.b16*m.b19 - 576
                       *m.b8*m.b16*m.b20 - 512*m.b8*m.b16*m.b21 - 448*m.b8*m.b16*m.b22 - 384*m.b8*m.b16*m.b23 - 64*m.b8*
                       m.b16*m.b24 - 288*m.b8*m.b16*m.b25 - 256*m.b8*m.b16*m.b26 - 224*m.b8*m.b16*m.b27 - 192*m.b8*m.b16
                       *m.b28 - 160*m.b8*m.b16*m.b29 - 128*m.b8*m.b16*m.b30 - 96*m.b8*m.b16*m.b31 - 64*m.b8*m.b16*m.b32
                        - 32*m.b8*m.b16*m.b33 - 704*m.b8*m.b17*m.b18 - 640*m.b8*m.b17*m.b19 - 576*m.b8*m.b17*m.b20 - 512
                       *m.b8*m.b17*m.b21 - 448*m.b8*m.b17*m.b22 - 384*m.b8*m.b17*m.b23 - 320*m.b8*m.b17*m.b24 - 256*m.b8
                       *m.b17*m.b25 - 224*m.b8*m.b17*m.b27 - 192*m.b8*m.b17*m.b28 - 160*m.b8*m.b17*m.b29 - 128*m.b8*
                       m.b17*m.b30 - 96*m.b8*m.b17*m.b31 - 64*m.b8*m.b17*m.b32 - 32*m.b8*m.b17*m.b33 - 640*m.b8*m.b18*
                       m.b19 - 576*m.b8*m.b18*m.b20 - 512*m.b8*m.b18*m.b21 - 448*m.b8*m.b18*m.b22 - 384*m.b8*m.b18*m.b23
                        - 320*m.b8*m.b18*m.b24 - 288*m.b8*m.b18*m.b25 - 256*m.b8*m.b18*m.b26 - 224*m.b8*m.b18*m.b27 - 
                       160*m.b8*m.b18*m.b29 - 128*m.b8*m.b18*m.b30 - 96*m.b8*m.b18*m.b31 - 64*m.b8*m.b18*m.b32 - 32*m.b8
                       *m.b18*m.b33 - 576*m.b8*m.b19*m.b20 - 512*m.b8*m.b19*m.b21 - 448*m.b8*m.b19*m.b22 - 384*m.b8*
                       m.b19*m.b23 - 352*m.b8*m.b19*m.b24 - 320*m.b8*m.b19*m.b25 - 288*m.b8*m.b19*m.b26 - 224*m.b8*m.b19
                       *m.b27 - 192*m.b8*m.b19*m.b28 - 160*m.b8*m.b19*m.b29 - 96*m.b8*m.b19*m.b31 - 64*m.b8*m.b19*m.b32
                        - 32*m.b8*m.b19*m.b33 - 512*m.b8*m.b20*m.b21 - 448*m.b8*m.b20*m.b22 - 416*m.b8*m.b20*m.b23 - 384
                       *m.b8*m.b20*m.b24 - 352*m.b8*m.b20*m.b25 - 320*m.b8*m.b20*m.b26 - 224*m.b8*m.b20*m.b27 - 192*m.b8
                       *m.b20*m.b28 - 160*m.b8*m.b20*m.b29 - 128*m.b8*m.b20*m.b30 - 96*m.b8*m.b20*m.b31 - 32*m.b8*m.b20*
                       m.b33 - 480*m.b8*m.b21*m.b22 - 448*m.b8*m.b21*m.b23 - 416*m.b8*m.b21*m.b24 - 384*m.b8*m.b21*m.b25
                        - 352*m.b8*m.b21*m.b26 - 256*m.b8*m.b21*m.b27 - 192*m.b8*m.b21*m.b28 - 160*m.b8*m.b21*m.b29 - 
                       128*m.b8*m.b21*m.b30 - 96*m.b8*m.b21*m.b31 - 64*m.b8*m.b21*m.b32 - 32*m.b8*m.b21*m.b33 - 480*m.b8
                       *m.b22*m.b23 - 448*m.b8*m.b22*m.b24 - 416*m.b8*m.b22*m.b25 - 384*m.b8*m.b22*m.b26 - 288*m.b8*
                       m.b22*m.b27 - 192*m.b8*m.b22*m.b28 - 160*m.b8*m.b22*m.b29 - 128*m.b8*m.b22*m.b30 - 96*m.b8*m.b22*
                       m.b31 - 64*m.b8*m.b22*m.b32 - 32*m.b8*m.b22*m.b33 - 480*m.b8*m.b23*m.b24 - 448*m.b8*m.b23*m.b25
                        - 416*m.b8*m.b23*m.b26 - 320*m.b8*m.b23*m.b27 - 224*m.b8*m.b23*m.b28 - 160*m.b8*m.b23*m.b29 - 
                       128*m.b8*m.b23*m.b30 - 96*m.b8*m.b23*m.b31 - 64*m.b8*m.b23*m.b32 - 32*m.b8*m.b23*m.b33 - 480*m.b8
                       *m.b24*m.b25 - 448*m.b8*m.b24*m.b26 - 352*m.b8*m.b24*m.b27 - 256*m.b8*m.b24*m.b28 - 160*m.b8*
                       m.b24*m.b29 - 128*m.b8*m.b24*m.b30 - 96*m.b8*m.b24*m.b31 - 64*m.b8*m.b24*m.b32 - 32*m.b8*m.b24*
                       m.b33 - 480*m.b8*m.b25*m.b26 - 384*m.b8*m.b25*m.b27 - 288*m.b8*m.b25*m.b28 - 192*m.b8*m.b25*m.b29
                        - 128*m.b8*m.b25*m.b30 - 96*m.b8*m.b25*m.b31 - 64*m.b8*m.b25*m.b32 - 32*m.b8*m.b25*m.b33 - 416*
                       m.b8*m.b26*m.b27 - 320*m.b8*m.b26*m.b28 - 224*m.b8*m.b26*m.b29 - 128*m.b8*m.b26*m.b30 - 96*m.b8*
                       m.b26*m.b31 - 64*m.b8*m.b26*m.b32 - 32*m.b8*m.b26*m.b33 - 352*m.b8*m.b27*m.b28 - 256*m.b8*m.b27*
                       m.b29 - 160*m.b8*m.b27*m.b30 - 96*m.b8*m.b27*m.b31 - 64*m.b8*m.b27*m.b32 - 32*m.b8*m.b27*m.b33 - 
                       288*m.b8*m.b28*m.b29 - 192*m.b8*m.b28*m.b30 - 96*m.b8*m.b28*m.b31 - 64*m.b8*m.b28*m.b32 - 32*m.b8
                       *m.b28*m.b33 - 224*m.b8*m.b29*m.b30 - 128*m.b8*m.b29*m.b31 - 64*m.b8*m.b29*m.b32 - 32*m.b8*m.b29*
                       m.b33 - 160*m.b8*m.b30*m.b31 - 64*m.b8*m.b30*m.b32 - 32*m.b8*m.b30*m.b33 - 96*m.b8*m.b31*m.b32 - 
                       32*m.b8*m.b31*m.b33 - 32*m.b8*m.b32*m.b33 - 544*m.b9*m.b10*m.b11 - 800*m.b9*m.b10*m.b12 - 768*
                       m.b9*m.b10*m.b13 - 736*m.b9*m.b10*m.b14 - 704*m.b9*m.b10*m.b15 - 672*m.b9*m.b10*m.b16 - 640*m.b9*
                       m.b10*m.b17 - 608*m.b9*m.b10*m.b18 - 576*m.b9*m.b10*m.b19 - 576*m.b9*m.b10*m.b20 - 576*m.b9*m.b10
                       *m.b21 - 576*m.b9*m.b10*m.b22 - 576*m.b9*m.b10*m.b23 - 576*m.b9*m.b10*m.b24 - 576*m.b9*m.b10*
                       m.b25 - 544*m.b9*m.b10*m.b26 - 480*m.b9*m.b10*m.b27 - 416*m.b9*m.b10*m.b28 - 352*m.b9*m.b10*m.b29
                        - 288*m.b9*m.b10*m.b30 - 224*m.b9*m.b10*m.b31 - 160*m.b9*m.b10*m.b32 - 96*m.b9*m.b10*m.b33 - 32*
                       m.b9*m.b10*m.b34 - 832*m.b9*m.b11*m.b12 - 512*m.b9*m.b11*m.b13 - 768*m.b9*m.b11*m.b14 - 736*m.b9*
                       m.b11*m.b15 - 704*m.b9*m.b11*m.b16 - 672*m.b9*m.b11*m.b17 - 640*m.b9*m.b11*m.b18 - 608*m.b9*m.b11
                       *m.b19 - 576*m.b9*m.b11*m.b20 - 576*m.b9*m.b11*m.b21 - 576*m.b9*m.b11*m.b22 - 576*m.b9*m.b11*
                       m.b23 - 576*m.b9*m.b11*m.b24 - 544*m.b9*m.b11*m.b25 - 512*m.b9*m.b11*m.b26 - 448*m.b9*m.b11*m.b27
                        - 384*m.b9*m.b11*m.b28 - 320*m.b9*m.b11*m.b29 - 256*m.b9*m.b11*m.b30 - 192*m.b9*m.b11*m.b31 - 
                       128*m.b9*m.b11*m.b32 - 64*m.b9*m.b11*m.b33 - 32*m.b9*m.b11*m.b34 - 832*m.b9*m.b12*m.b13 - 800*
                       m.b9*m.b12*m.b14 - 480*m.b9*m.b12*m.b15 - 736*m.b9*m.b12*m.b16 - 704*m.b9*m.b12*m.b17 - 672*m.b9*
                       m.b12*m.b18 - 640*m.b9*m.b12*m.b19 - 608*m.b9*m.b12*m.b20 - 576*m.b9*m.b12*m.b21 - 576*m.b9*m.b12
                       *m.b22 - 576*m.b9*m.b12*m.b23 - 544*m.b9*m.b12*m.b24 - 512*m.b9*m.b12*m.b25 - 480*m.b9*m.b12*
                       m.b26 - 416*m.b9*m.b12*m.b27 - 352*m.b9*m.b12*m.b28 - 288*m.b9*m.b12*m.b29 - 224*m.b9*m.b12*m.b30
                        - 160*m.b9*m.b12*m.b31 - 96*m.b9*m.b12*m.b32 - 64*m.b9*m.b12*m.b33 - 32*m.b9*m.b12*m.b34 - 832*
                       m.b9*m.b13*m.b14 - 800*m.b9*m.b13*m.b15 - 768*m.b9*m.b13*m.b16 - 448*m.b9*m.b13*m.b17 - 704*m.b9*
                       m.b13*m.b18 - 672*m.b9*m.b13*m.b19 - 640*m.b9*m.b13*m.b20 - 608*m.b9*m.b13*m.b21 - 576*m.b9*m.b13
                       *m.b22 - 544*m.b9*m.b13*m.b23 - 512*m.b9*m.b13*m.b24 - 480*m.b9*m.b13*m.b25 - 448*m.b9*m.b13*
                       m.b26 - 384*m.b9*m.b13*m.b27 - 320*m.b9*m.b13*m.b28 - 256*m.b9*m.b13*m.b29 - 192*m.b9*m.b13*m.b30
                        - 128*m.b9*m.b13*m.b31 - 96*m.b9*m.b13*m.b32 - 64*m.b9*m.b13*m.b33 - 32*m.b9*m.b13*m.b34 - 832*
                       m.b9*m.b14*m.b15 - 800*m.b9*m.b14*m.b16 - 768*m.b9*m.b14*m.b17 - 736*m.b9*m.b14*m.b18 - 416*m.b9*
                       m.b14*m.b19 - 672*m.b9*m.b14*m.b20 - 640*m.b9*m.b14*m.b21 - 576*m.b9*m.b14*m.b22 - 512*m.b9*m.b14
                       *m.b23 - 480*m.b9*m.b14*m.b24 - 448*m.b9*m.b14*m.b25 - 416*m.b9*m.b14*m.b26 - 352*m.b9*m.b14*
                       m.b27 - 288*m.b9*m.b14*m.b28 - 224*m.b9*m.b14*m.b29 - 160*m.b9*m.b14*m.b30 - 128*m.b9*m.b14*m.b31
                        - 96*m.b9*m.b14*m.b32 - 64*m.b9*m.b14*m.b33 - 32*m.b9*m.b14*m.b34 - 832*m.b9*m.b15*m.b16 - 800*
                       m.b9*m.b15*m.b17 - 768*m.b9*m.b15*m.b18 - 736*m.b9*m.b15*m.b19 - 704*m.b9*m.b15*m.b20 - 352*m.b9*
                       m.b15*m.b21 - 576*m.b9*m.b15*m.b22 - 512*m.b9*m.b15*m.b23 - 448*m.b9*m.b15*m.b24 - 416*m.b9*m.b15
                       *m.b25 - 384*m.b9*m.b15*m.b26 - 320*m.b9*m.b15*m.b27 - 256*m.b9*m.b15*m.b28 - 192*m.b9*m.b15*
                       m.b29 - 160*m.b9*m.b15*m.b30 - 128*m.b9*m.b15*m.b31 - 96*m.b9*m.b15*m.b32 - 64*m.b9*m.b15*m.b33
                        - 32*m.b9*m.b15*m.b34 - 832*m.b9*m.b16*m.b17 - 800*m.b9*m.b16*m.b18 - 768*m.b9*m.b16*m.b19 - 704
                       *m.b9*m.b16*m.b20 - 640*m.b9*m.b16*m.b21 - 576*m.b9*m.b16*m.b22 - 224*m.b9*m.b16*m.b23 - 448*m.b9
                       *m.b16*m.b24 - 384*m.b9*m.b16*m.b25 - 352*m.b9*m.b16*m.b26 - 288*m.b9*m.b16*m.b27 - 224*m.b9*
                       m.b16*m.b28 - 192*m.b9*m.b16*m.b29 - 160*m.b9*m.b16*m.b30 - 128*m.b9*m.b16*m.b31 - 96*m.b9*m.b16*
                       m.b32 - 64*m.b9*m.b16*m.b33 - 32*m.b9*m.b16*m.b34 - 832*m.b9*m.b17*m.b18 - 768*m.b9*m.b17*m.b19
                        - 704*m.b9*m.b17*m.b20 - 640*m.b9*m.b17*m.b21 - 576*m.b9*m.b17*m.b22 - 512*m.b9*m.b17*m.b23 - 
                       448*m.b9*m.b17*m.b24 - 96*m.b9*m.b17*m.b25 - 320*m.b9*m.b17*m.b26 - 256*m.b9*m.b17*m.b27 - 224*
                       m.b9*m.b17*m.b28 - 192*m.b9*m.b17*m.b29 - 160*m.b9*m.b17*m.b30 - 128*m.b9*m.b17*m.b31 - 96*m.b9*
                       m.b17*m.b32 - 64*m.b9*m.b17*m.b33 - 32*m.b9*m.b17*m.b34 - 768*m.b9*m.b18*m.b19 - 704*m.b9*m.b18*
                       m.b20 - 640*m.b9*m.b18*m.b21 - 576*m.b9*m.b18*m.b22 - 512*m.b9*m.b18*m.b23 - 448*m.b9*m.b18*m.b24
                        - 384*m.b9*m.b18*m.b25 - 320*m.b9*m.b18*m.b26 - 224*m.b9*m.b18*m.b28 - 192*m.b9*m.b18*m.b29 - 
                       160*m.b9*m.b18*m.b30 - 128*m.b9*m.b18*m.b31 - 96*m.b9*m.b18*m.b32 - 64*m.b9*m.b18*m.b33 - 32*m.b9
                       *m.b18*m.b34 - 704*m.b9*m.b19*m.b20 - 640*m.b9*m.b19*m.b21 - 576*m.b9*m.b19*m.b22 - 512*m.b9*
                       m.b19*m.b23 - 448*m.b9*m.b19*m.b24 - 384*m.b9*m.b19*m.b25 - 352*m.b9*m.b19*m.b26 - 256*m.b9*m.b19
                       *m.b27 - 224*m.b9*m.b19*m.b28 - 160*m.b9*m.b19*m.b30 - 128*m.b9*m.b19*m.b31 - 96*m.b9*m.b19*m.b32
                        - 64*m.b9*m.b19*m.b33 - 32*m.b9*m.b19*m.b34 - 640*m.b9*m.b20*m.b21 - 576*m.b9*m.b20*m.b22 - 512*
                       m.b9*m.b20*m.b23 - 448*m.b9*m.b20*m.b24 - 416*m.b9*m.b20*m.b25 - 384*m.b9*m.b20*m.b26 - 288*m.b9*
                       m.b20*m.b27 - 224*m.b9*m.b20*m.b28 - 192*m.b9*m.b20*m.b29 - 160*m.b9*m.b20*m.b30 - 96*m.b9*m.b20*
                       m.b32 - 64*m.b9*m.b20*m.b33 - 32*m.b9*m.b20*m.b34 - 576*m.b9*m.b21*m.b22 - 512*m.b9*m.b21*m.b23
                        - 480*m.b9*m.b21*m.b24 - 448*m.b9*m.b21*m.b25 - 416*m.b9*m.b21*m.b26 - 320*m.b9*m.b21*m.b27 - 
                       224*m.b9*m.b21*m.b28 - 192*m.b9*m.b21*m.b29 - 160*m.b9*m.b21*m.b30 - 128*m.b9*m.b21*m.b31 - 96*
                       m.b9*m.b21*m.b32 - 32*m.b9*m.b21*m.b34 - 544*m.b9*m.b22*m.b23 - 512*m.b9*m.b22*m.b24 - 480*m.b9*
                       m.b22*m.b25 - 448*m.b9*m.b22*m.b26 - 352*m.b9*m.b22*m.b27 - 256*m.b9*m.b22*m.b28 - 192*m.b9*m.b22
                       *m.b29 - 160*m.b9*m.b22*m.b30 - 128*m.b9*m.b22*m.b31 - 96*m.b9*m.b22*m.b32 - 64*m.b9*m.b22*m.b33
                        - 32*m.b9*m.b22*m.b34 - 544*m.b9*m.b23*m.b24 - 512*m.b9*m.b23*m.b25 - 480*m.b9*m.b23*m.b26 - 384
                       *m.b9*m.b23*m.b27 - 288*m.b9*m.b23*m.b28 - 192*m.b9*m.b23*m.b29 - 160*m.b9*m.b23*m.b30 - 128*m.b9
                       *m.b23*m.b31 - 96*m.b9*m.b23*m.b32 - 64*m.b9*m.b23*m.b33 - 32*m.b9*m.b23*m.b34 - 544*m.b9*m.b24*
                       m.b25 - 512*m.b9*m.b24*m.b26 - 416*m.b9*m.b24*m.b27 - 320*m.b9*m.b24*m.b28 - 224*m.b9*m.b24*m.b29
                        - 160*m.b9*m.b24*m.b30 - 128*m.b9*m.b24*m.b31 - 96*m.b9*m.b24*m.b32 - 64*m.b9*m.b24*m.b33 - 32*
                       m.b9*m.b24*m.b34 - 544*m.b9*m.b25*m.b26 - 448*m.b9*m.b25*m.b27 - 352*m.b9*m.b25*m.b28 - 256*m.b9*
                       m.b25*m.b29 - 160*m.b9*m.b25*m.b30 - 128*m.b9*m.b25*m.b31 - 96*m.b9*m.b25*m.b32 - 64*m.b9*m.b25*
                       m.b33 - 32*m.b9*m.b25*m.b34 - 480*m.b9*m.b26*m.b27 - 384*m.b9*m.b26*m.b28 - 288*m.b9*m.b26*m.b29
                        - 192*m.b9*m.b26*m.b30 - 128*m.b9*m.b26*m.b31 - 96*m.b9*m.b26*m.b32 - 64*m.b9*m.b26*m.b33 - 32*
                       m.b9*m.b26*m.b34 - 416*m.b9*m.b27*m.b28 - 320*m.b9*m.b27*m.b29 - 224*m.b9*m.b27*m.b30 - 128*m.b9*
                       m.b27*m.b31 - 96*m.b9*m.b27*m.b32 - 64*m.b9*m.b27*m.b33 - 32*m.b9*m.b27*m.b34 - 352*m.b9*m.b28*
                       m.b29 - 256*m.b9*m.b28*m.b30 - 160*m.b9*m.b28*m.b31 - 96*m.b9*m.b28*m.b32 - 64*m.b9*m.b28*m.b33
                        - 32*m.b9*m.b28*m.b34 - 288*m.b9*m.b29*m.b30 - 192*m.b9*m.b29*m.b31 - 96*m.b9*m.b29*m.b32 - 64*
                       m.b9*m.b29*m.b33 - 32*m.b9*m.b29*m.b34 - 224*m.b9*m.b30*m.b31 - 128*m.b9*m.b30*m.b32 - 64*m.b9*
                       m.b30*m.b33 - 32*m.b9*m.b30*m.b34 - 160*m.b9*m.b31*m.b32 - 64*m.b9*m.b31*m.b33 - 32*m.b9*m.b31*
                       m.b34 - 96*m.b9*m.b32*m.b33 - 32*m.b9*m.b32*m.b34 - 32*m.b9*m.b33*m.b34 - 608*m.b10*m.b11*m.b12
                        - 896*m.b10*m.b11*m.b13 - 864*m.b10*m.b11*m.b14 - 832*m.b10*m.b11*m.b15 - 800*m.b10*m.b11*m.b16
                        - 768*m.b10*m.b11*m.b17 - 736*m.b10*m.b11*m.b18 - 704*m.b10*m.b11*m.b19 - 672*m.b10*m.b11*m.b20
                        - 640*m.b10*m.b11*m.b21 - 640*m.b10*m.b11*m.b22 - 640*m.b10*m.b11*m.b23 - 640*m.b10*m.b11*m.b24
                        - 640*m.b10*m.b11*m.b25 - 608*m.b10*m.b11*m.b26 - 544*m.b10*m.b11*m.b27 - 480*m.b10*m.b11*m.b28
                        - 416*m.b10*m.b11*m.b29 - 352*m.b10*m.b11*m.b30 - 288*m.b10*m.b11*m.b31 - 224*m.b10*m.b11*m.b32
                        - 160*m.b10*m.b11*m.b33 - 96*m.b10*m.b11*m.b34 - 32*m.b10*m.b11*m.b35 - 928*m.b10*m.b12*m.b13 - 
                       576*m.b10*m.b12*m.b14 - 864*m.b10*m.b12*m.b15 - 832*m.b10*m.b12*m.b16 - 800*m.b10*m.b12*m.b17 - 
                       768*m.b10*m.b12*m.b18 - 736*m.b10*m.b12*m.b19 - 704*m.b10*m.b12*m.b20 - 672*m.b10*m.b12*m.b21 - 
                       640*m.b10*m.b12*m.b22 - 640*m.b10*m.b12*m.b23 - 640*m.b10*m.b12*m.b24 - 608*m.b10*m.b12*m.b25 - 
                       576*m.b10*m.b12*m.b26 - 512*m.b10*m.b12*m.b27 - 448*m.b10*m.b12*m.b28 - 384*m.b10*m.b12*m.b29 - 
                       320*m.b10*m.b12*m.b30 - 256*m.b10*m.b12*m.b31 - 192*m.b10*m.b12*m.b32 - 128*m.b10*m.b12*m.b33 - 
                       64*m.b10*m.b12*m.b34 - 32*m.b10*m.b12*m.b35 - 928*m.b10*m.b13*m.b14 - 896*m.b10*m.b13*m.b15 - 544
                       *m.b10*m.b13*m.b16 - 832*m.b10*m.b13*m.b17 - 800*m.b10*m.b13*m.b18 - 768*m.b10*m.b13*m.b19 - 736*
                       m.b10*m.b13*m.b20 - 704*m.b10*m.b13*m.b21 - 672*m.b10*m.b13*m.b22 - 640*m.b10*m.b13*m.b23 - 608*
                       m.b10*m.b13*m.b24 - 576*m.b10*m.b13*m.b25 - 544*m.b10*m.b13*m.b26 - 480*m.b10*m.b13*m.b27 - 416*
                       m.b10*m.b13*m.b28 - 352*m.b10*m.b13*m.b29 - 288*m.b10*m.b13*m.b30 - 224*m.b10*m.b13*m.b31 - 160*
                       m.b10*m.b13*m.b32 - 96*m.b10*m.b13*m.b33 - 64*m.b10*m.b13*m.b34 - 32*m.b10*m.b13*m.b35 - 928*
                       m.b10*m.b14*m.b15 - 896*m.b10*m.b14*m.b16 - 864*m.b10*m.b14*m.b17 - 512*m.b10*m.b14*m.b18 - 800*
                       m.b10*m.b14*m.b19 - 768*m.b10*m.b14*m.b20 - 736*m.b10*m.b14*m.b21 - 704*m.b10*m.b14*m.b22 - 640*
                       m.b10*m.b14*m.b23 - 576*m.b10*m.b14*m.b24 - 544*m.b10*m.b14*m.b25 - 512*m.b10*m.b14*m.b26 - 448*
                       m.b10*m.b14*m.b27 - 384*m.b10*m.b14*m.b28 - 320*m.b10*m.b14*m.b29 - 256*m.b10*m.b14*m.b30 - 192*
                       m.b10*m.b14*m.b31 - 128*m.b10*m.b14*m.b32 - 96*m.b10*m.b14*m.b33 - 64*m.b10*m.b14*m.b34 - 32*
                       m.b10*m.b14*m.b35 - 928*m.b10*m.b15*m.b16 - 896*m.b10*m.b15*m.b17 - 864*m.b10*m.b15*m.b18 - 832*
                       m.b10*m.b15*m.b19 - 480*m.b10*m.b15*m.b20 - 768*m.b10*m.b15*m.b21 - 704*m.b10*m.b15*m.b22 - 640*
                       m.b10*m.b15*m.b23 - 576*m.b10*m.b15*m.b24 - 512*m.b10*m.b15*m.b25 - 480*m.b10*m.b15*m.b26 - 416*
                       m.b10*m.b15*m.b27 - 352*m.b10*m.b15*m.b28 - 288*m.b10*m.b15*m.b29 - 224*m.b10*m.b15*m.b30 - 160*
                       m.b10*m.b15*m.b31 - 128*m.b10*m.b15*m.b32 - 96*m.b10*m.b15*m.b33 - 64*m.b10*m.b15*m.b34 - 32*
                       m.b10*m.b15*m.b35 - 928*m.b10*m.b16*m.b17 - 896*m.b10*m.b16*m.b18 - 864*m.b10*m.b16*m.b19 - 832*
                       m.b10*m.b16*m.b20 - 768*m.b10*m.b16*m.b21 - 384*m.b10*m.b16*m.b22 - 640*m.b10*m.b16*m.b23 - 576*
                       m.b10*m.b16*m.b24 - 512*m.b10*m.b16*m.b25 - 448*m.b10*m.b16*m.b26 - 384*m.b10*m.b16*m.b27 - 320*
                       m.b10*m.b16*m.b28 - 256*m.b10*m.b16*m.b29 - 192*m.b10*m.b16*m.b30 - 160*m.b10*m.b16*m.b31 - 128*
                       m.b10*m.b16*m.b32 - 96*m.b10*m.b16*m.b33 - 64*m.b10*m.b16*m.b34 - 32*m.b10*m.b16*m.b35 - 928*
                       m.b10*m.b17*m.b18 - 896*m.b10*m.b17*m.b19 - 832*m.b10*m.b17*m.b20 - 768*m.b10*m.b17*m.b21 - 704*
                       m.b10*m.b17*m.b22 - 640*m.b10*m.b17*m.b23 - 256*m.b10*m.b17*m.b24 - 512*m.b10*m.b17*m.b25 - 448*
                       m.b10*m.b17*m.b26 - 352*m.b10*m.b17*m.b27 - 288*m.b10*m.b17*m.b28 - 224*m.b10*m.b17*m.b29 - 192*
                       m.b10*m.b17*m.b30 - 160*m.b10*m.b17*m.b31 - 128*m.b10*m.b17*m.b32 - 96*m.b10*m.b17*m.b33 - 64*
                       m.b10*m.b17*m.b34 - 32*m.b10*m.b17*m.b35 - 896*m.b10*m.b18*m.b19 - 832*m.b10*m.b18*m.b20 - 768*
                       m.b10*m.b18*m.b21 - 704*m.b10*m.b18*m.b22 - 640*m.b10*m.b18*m.b23 - 576*m.b10*m.b18*m.b24 - 512*
                       m.b10*m.b18*m.b25 - 128*m.b10*m.b18*m.b26 - 320*m.b10*m.b18*m.b27 - 256*m.b10*m.b18*m.b28 - 224*
                       m.b10*m.b18*m.b29 - 192*m.b10*m.b18*m.b30 - 160*m.b10*m.b18*m.b31 - 128*m.b10*m.b18*m.b32 - 96*
                       m.b10*m.b18*m.b33 - 64*m.b10*m.b18*m.b34 - 32*m.b10*m.b18*m.b35 - 832*m.b10*m.b19*m.b20 - 768*
                       m.b10*m.b19*m.b21 - 704*m.b10*m.b19*m.b22 - 640*m.b10*m.b19*m.b23 - 576*m.b10*m.b19*m.b24 - 512*
                       m.b10*m.b19*m.b25 - 448*m.b10*m.b19*m.b26 - 320*m.b10*m.b19*m.b27 - 224*m.b10*m.b19*m.b29 - 192*
                       m.b10*m.b19*m.b30 - 160*m.b10*m.b19*m.b31 - 128*m.b10*m.b19*m.b32 - 96*m.b10*m.b19*m.b33 - 64*
                       m.b10*m.b19*m.b34 - 32*m.b10*m.b19*m.b35 - 768*m.b10*m.b20*m.b21 - 704*m.b10*m.b20*m.b22 - 640*
                       m.b10*m.b20*m.b23 - 576*m.b10*m.b20*m.b24 - 512*m.b10*m.b20*m.b25 - 448*m.b10*m.b20*m.b26 - 352*
                       m.b10*m.b20*m.b27 - 256*m.b10*m.b20*m.b28 - 224*m.b10*m.b20*m.b29 - 160*m.b10*m.b20*m.b31 - 128*
                       m.b10*m.b20*m.b32 - 96*m.b10*m.b20*m.b33 - 64*m.b10*m.b20*m.b34 - 32*m.b10*m.b20*m.b35 - 704*
                       m.b10*m.b21*m.b22 - 640*m.b10*m.b21*m.b23 - 576*m.b10*m.b21*m.b24 - 512*m.b10*m.b21*m.b25 - 480*
                       m.b10*m.b21*m.b26 - 384*m.b10*m.b21*m.b27 - 288*m.b10*m.b21*m.b28 - 224*m.b10*m.b21*m.b29 - 192*
                       m.b10*m.b21*m.b30 - 160*m.b10*m.b21*m.b31 - 96*m.b10*m.b21*m.b33 - 64*m.b10*m.b21*m.b34 - 32*
                       m.b10*m.b21*m.b35 - 640*m.b10*m.b22*m.b23 - 576*m.b10*m.b22*m.b24 - 544*m.b10*m.b22*m.b25 - 512*
                       m.b10*m.b22*m.b26 - 416*m.b10*m.b22*m.b27 - 320*m.b10*m.b22*m.b28 - 224*m.b10*m.b22*m.b29 - 192*
                       m.b10*m.b22*m.b30 - 160*m.b10*m.b22*m.b31 - 128*m.b10*m.b22*m.b32 - 96*m.b10*m.b22*m.b33 - 32*
                       m.b10*m.b22*m.b35 - 608*m.b10*m.b23*m.b24 - 576*m.b10*m.b23*m.b25 - 544*m.b10*m.b23*m.b26 - 448*
                       m.b10*m.b23*m.b27 - 352*m.b10*m.b23*m.b28 - 256*m.b10*m.b23*m.b29 - 192*m.b10*m.b23*m.b30 - 160*
                       m.b10*m.b23*m.b31 - 128*m.b10*m.b23*m.b32 - 96*m.b10*m.b23*m.b33 - 64*m.b10*m.b23*m.b34 - 32*
                       m.b10*m.b23*m.b35 - 608*m.b10*m.b24*m.b25 - 576*m.b10*m.b24*m.b26 - 480*m.b10*m.b24*m.b27 - 384*
                       m.b10*m.b24*m.b28 - 288*m.b10*m.b24*m.b29 - 192*m.b10*m.b24*m.b30 - 160*m.b10*m.b24*m.b31 - 128*
                       m.b10*m.b24*m.b32 - 96*m.b10*m.b24*m.b33 - 64*m.b10*m.b24*m.b34 - 32*m.b10*m.b24*m.b35 - 608*
                       m.b10*m.b25*m.b26 - 512*m.b10*m.b25*m.b27 - 416*m.b10*m.b25*m.b28 - 320*m.b10*m.b25*m.b29 - 224*
                       m.b10*m.b25*m.b30 - 160*m.b10*m.b25*m.b31 - 128*m.b10*m.b25*m.b32 - 96*m.b10*m.b25*m.b33 - 64*
                       m.b10*m.b25*m.b34 - 32*m.b10*m.b25*m.b35 - 544*m.b10*m.b26*m.b27 - 448*m.b10*m.b26*m.b28 - 352*
                       m.b10*m.b26*m.b29 - 256*m.b10*m.b26*m.b30 - 160*m.b10*m.b26*m.b31 - 128*m.b10*m.b26*m.b32 - 96*
                       m.b10*m.b26*m.b33 - 64*m.b10*m.b26*m.b34 - 32*m.b10*m.b26*m.b35 - 480*m.b10*m.b27*m.b28 - 384*
                       m.b10*m.b27*m.b29 - 288*m.b10*m.b27*m.b30 - 192*m.b10*m.b27*m.b31 - 128*m.b10*m.b27*m.b32 - 96*
                       m.b10*m.b27*m.b33 - 64*m.b10*m.b27*m.b34 - 32*m.b10*m.b27*m.b35 - 416*m.b10*m.b28*m.b29 - 320*
                       m.b10*m.b28*m.b30 - 224*m.b10*m.b28*m.b31 - 128*m.b10*m.b28*m.b32 - 96*m.b10*m.b28*m.b33 - 64*
                       m.b10*m.b28*m.b34 - 32*m.b10*m.b28*m.b35 - 352*m.b10*m.b29*m.b30 - 256*m.b10*m.b29*m.b31 - 160*
                       m.b10*m.b29*m.b32 - 96*m.b10*m.b29*m.b33 - 64*m.b10*m.b29*m.b34 - 32*m.b10*m.b29*m.b35 - 288*
                       m.b10*m.b30*m.b31 - 192*m.b10*m.b30*m.b32 - 96*m.b10*m.b30*m.b33 - 64*m.b10*m.b30*m.b34 - 32*
                       m.b10*m.b30*m.b35 - 224*m.b10*m.b31*m.b32 - 128*m.b10*m.b31*m.b33 - 64*m.b10*m.b31*m.b34 - 32*
                       m.b10*m.b31*m.b35 - 160*m.b10*m.b32*m.b33 - 64*m.b10*m.b32*m.b34 - 32*m.b10*m.b32*m.b35 - 96*
                       m.b10*m.b33*m.b34 - 32*m.b10*m.b33*m.b35 - 32*m.b10*m.b34*m.b35 - 640*m.b11*m.b12*m.b13 - 928*
                       m.b11*m.b12*m.b14 - 896*m.b11*m.b12*m.b15 - 864*m.b11*m.b12*m.b16 - 832*m.b11*m.b12*m.b17 - 832*
                       m.b11*m.b12*m.b18 - 832*m.b11*m.b12*m.b19 - 800*m.b11*m.b12*m.b20 - 768*m.b11*m.b12*m.b21 - 736*
                       m.b11*m.b12*m.b22 - 704*m.b11*m.b12*m.b23 - 704*m.b11*m.b12*m.b24 - 672*m.b11*m.b12*m.b25 - 608*
                       m.b11*m.b12*m.b26 - 544*m.b11*m.b12*m.b27 - 480*m.b11*m.b12*m.b28 - 416*m.b11*m.b12*m.b29 - 352*
                       m.b11*m.b12*m.b30 - 288*m.b11*m.b12*m.b31 - 224*m.b11*m.b12*m.b32 - 160*m.b11*m.b12*m.b33 - 96*
                       m.b11*m.b12*m.b34 - 32*m.b11*m.b12*m.b35 - 960*m.b11*m.b13*m.b14 - 608*m.b11*m.b13*m.b15 - 896*
                       m.b11*m.b13*m.b16 - 896*m.b11*m.b13*m.b17 - 864*m.b11*m.b13*m.b18 - 864*m.b11*m.b13*m.b19 - 832*
                       m.b11*m.b13*m.b20 - 800*m.b11*m.b13*m.b21 - 768*m.b11*m.b13*m.b22 - 736*m.b11*m.b13*m.b23 - 672*
                       m.b11*m.b13*m.b24 - 640*m.b11*m.b13*m.b25 - 576*m.b11*m.b13*m.b26 - 512*m.b11*m.b13*m.b27 - 448*
                       m.b11*m.b13*m.b28 - 384*m.b11*m.b13*m.b29 - 320*m.b11*m.b13*m.b30 - 256*m.b11*m.b13*m.b31 - 192*
                       m.b11*m.b13*m.b32 - 128*m.b11*m.b13*m.b33 - 64*m.b11*m.b13*m.b34 - 32*m.b11*m.b13*m.b35 - 960*
                       m.b11*m.b14*m.b15 - 960*m.b11*m.b14*m.b16 - 608*m.b11*m.b14*m.b17 - 896*m.b11*m.b14*m.b18 - 896*
                       m.b11*m.b14*m.b19 - 864*m.b11*m.b14*m.b20 - 832*m.b11*m.b14*m.b21 - 800*m.b11*m.b14*m.b22 - 736*
                       m.b11*m.b14*m.b23 - 672*m.b11*m.b14*m.b24 - 608*m.b11*m.b14*m.b25 - 544*m.b11*m.b14*m.b26 - 480*
                       m.b11*m.b14*m.b27 - 416*m.b11*m.b14*m.b28 - 352*m.b11*m.b14*m.b29 - 288*m.b11*m.b14*m.b30 - 224*
                       m.b11*m.b14*m.b31 - 160*m.b11*m.b14*m.b32 - 96*m.b11*m.b14*m.b33 - 64*m.b11*m.b14*m.b34 - 32*
                       m.b11*m.b14*m.b35 - 992*m.b11*m.b15*m.b16 - 960*m.b11*m.b15*m.b17 - 928*m.b11*m.b15*m.b18 - 576*
                       m.b11*m.b15*m.b19 - 896*m.b11*m.b15*m.b20 - 864*m.b11*m.b15*m.b21 - 800*m.b11*m.b15*m.b22 - 736*
                       m.b11*m.b15*m.b23 - 672*m.b11*m.b15*m.b24 - 608*m.b11*m.b15*m.b25 - 512*m.b11*m.b15*m.b26 - 448*
                       m.b11*m.b15*m.b27 - 384*m.b11*m.b15*m.b28 - 320*m.b11*m.b15*m.b29 - 256*m.b11*m.b15*m.b30 - 192*
                       m.b11*m.b15*m.b31 - 128*m.b11*m.b15*m.b32 - 96*m.b11*m.b15*m.b33 - 64*m.b11*m.b15*m.b34 - 32*
                       m.b11*m.b15*m.b35 - 992*m.b11*m.b16*m.b17 - 960*m.b11*m.b16*m.b18 - 960*m.b11*m.b16*m.b19 - 928*
                       m.b11*m.b16*m.b20 - 512*m.b11*m.b16*m.b21 - 800*m.b11*m.b16*m.b22 - 736*m.b11*m.b16*m.b23 - 672*
                       m.b11*m.b16*m.b24 - 608*m.b11*m.b16*m.b25 - 512*m.b11*m.b16*m.b26 - 416*m.b11*m.b16*m.b27 - 352*
                       m.b11*m.b16*m.b28 - 288*m.b11*m.b16*m.b29 - 224*m.b11*m.b16*m.b30 - 160*m.b11*m.b16*m.b31 - 128*
                       m.b11*m.b16*m.b32 - 96*m.b11*m.b16*m.b33 - 64*m.b11*m.b16*m.b34 - 32*m.b11*m.b16*m.b35 - 992*
                       m.b11*m.b17*m.b18 - 992*m.b11*m.b17*m.b19 - 928*m.b11*m.b17*m.b20 - 864*m.b11*m.b17*m.b21 - 800*
                       m.b11*m.b17*m.b22 - 384*m.b11*m.b17*m.b23 - 672*m.b11*m.b17*m.b24 - 608*m.b11*m.b17*m.b25 - 512*
                       m.b11*m.b17*m.b26 - 384*m.b11*m.b17*m.b27 - 320*m.b11*m.b17*m.b28 - 256*m.b11*m.b17*m.b29 - 192*
                       m.b11*m.b17*m.b30 - 160*m.b11*m.b17*m.b31 - 128*m.b11*m.b17*m.b32 - 96*m.b11*m.b17*m.b33 - 64*
                       m.b11*m.b17*m.b34 - 32*m.b11*m.b17*m.b35 - 992*m.b11*m.b18*m.b19 - 928*m.b11*m.b18*m.b20 - 864*
                       m.b11*m.b18*m.b21 - 800*m.b11*m.b18*m.b22 - 736*m.b11*m.b18*m.b23 - 672*m.b11*m.b18*m.b24 - 256*
                       m.b11*m.b18*m.b25 - 512*m.b11*m.b18*m.b26 - 384*m.b11*m.b18*m.b27 - 288*m.b11*m.b18*m.b28 - 224*
                       m.b11*m.b18*m.b29 - 192*m.b11*m.b18*m.b30 - 160*m.b11*m.b18*m.b31 - 128*m.b11*m.b18*m.b32 - 96*
                       m.b11*m.b18*m.b33 - 64*m.b11*m.b18*m.b34 - 32*m.b11*m.b18*m.b35 - 928*m.b11*m.b19*m.b20 - 864*
                       m.b11*m.b19*m.b21 - 800*m.b11*m.b19*m.b22 - 736*m.b11*m.b19*m.b23 - 672*m.b11*m.b19*m.b24 - 608*
                       m.b11*m.b19*m.b25 - 512*m.b11*m.b19*m.b26 - 96*m.b11*m.b19*m.b27 - 256*m.b11*m.b19*m.b28 - 224*
                       m.b11*m.b19*m.b29 - 192*m.b11*m.b19*m.b30 - 160*m.b11*m.b19*m.b31 - 128*m.b11*m.b19*m.b32 - 96*
                       m.b11*m.b19*m.b33 - 64*m.b11*m.b19*m.b34 - 32*m.b11*m.b19*m.b35 - 864*m.b11*m.b20*m.b21 - 800*
                       m.b11*m.b20*m.b22 - 736*m.b11*m.b20*m.b23 - 672*m.b11*m.b20*m.b24 - 608*m.b11*m.b20*m.b25 - 512*
                       m.b11*m.b20*m.b26 - 384*m.b11*m.b20*m.b27 - 288*m.b11*m.b20*m.b28 - 192*m.b11*m.b20*m.b30 - 160*
                       m.b11*m.b20*m.b31 - 128*m.b11*m.b20*m.b32 - 96*m.b11*m.b20*m.b33 - 64*m.b11*m.b20*m.b34 - 32*
                       m.b11*m.b20*m.b35 - 800*m.b11*m.b21*m.b22 - 736*m.b11*m.b21*m.b23 - 672*m.b11*m.b21*m.b24 - 608*
                       m.b11*m.b21*m.b25 - 512*m.b11*m.b21*m.b26 - 416*m.b11*m.b21*m.b27 - 320*m.b11*m.b21*m.b28 - 224*
                       m.b11*m.b21*m.b29 - 192*m.b11*m.b21*m.b30 - 128*m.b11*m.b21*m.b32 - 96*m.b11*m.b21*m.b33 - 64*
                       m.b11*m.b21*m.b34 - 32*m.b11*m.b21*m.b35 - 736*m.b11*m.b22*m.b23 - 672*m.b11*m.b22*m.b24 - 608*
                       m.b11*m.b22*m.b25 - 544*m.b11*m.b22*m.b26 - 448*m.b11*m.b22*m.b27 - 352*m.b11*m.b22*m.b28 - 256*
                       m.b11*m.b22*m.b29 - 192*m.b11*m.b22*m.b30 - 160*m.b11*m.b22*m.b31 - 128*m.b11*m.b22*m.b32 - 64*
                       m.b11*m.b22*m.b34 - 32*m.b11*m.b22*m.b35 - 672*m.b11*m.b23*m.b24 - 640*m.b11*m.b23*m.b25 - 576*
                       m.b11*m.b23*m.b26 - 480*m.b11*m.b23*m.b27 - 384*m.b11*m.b23*m.b28 - 288*m.b11*m.b23*m.b29 - 192*
                       m.b11*m.b23*m.b30 - 160*m.b11*m.b23*m.b31 - 128*m.b11*m.b23*m.b32 - 96*m.b11*m.b23*m.b33 - 64*
                       m.b11*m.b23*m.b34 - 672*m.b11*m.b24*m.b25 - 608*m.b11*m.b24*m.b26 - 512*m.b11*m.b24*m.b27 - 416*
                       m.b11*m.b24*m.b28 - 320*m.b11*m.b24*m.b29 - 224*m.b11*m.b24*m.b30 - 160*m.b11*m.b24*m.b31 - 128*
                       m.b11*m.b24*m.b32 - 96*m.b11*m.b24*m.b33 - 64*m.b11*m.b24*m.b34 - 32*m.b11*m.b24*m.b35 - 640*
                       m.b11*m.b25*m.b26 - 544*m.b11*m.b25*m.b27 - 448*m.b11*m.b25*m.b28 - 352*m.b11*m.b25*m.b29 - 256*
                       m.b11*m.b25*m.b30 - 160*m.b11*m.b25*m.b31 - 128*m.b11*m.b25*m.b32 - 96*m.b11*m.b25*m.b33 - 64*
                       m.b11*m.b25*m.b34 - 32*m.b11*m.b25*m.b35 - 576*m.b11*m.b26*m.b27 - 480*m.b11*m.b26*m.b28 - 384*
                       m.b11*m.b26*m.b29 - 288*m.b11*m.b26*m.b30 - 192*m.b11*m.b26*m.b31 - 128*m.b11*m.b26*m.b32 - 96*
                       m.b11*m.b26*m.b33 - 64*m.b11*m.b26*m.b34 - 32*m.b11*m.b26*m.b35 - 512*m.b11*m.b27*m.b28 - 416*
                       m.b11*m.b27*m.b29 - 320*m.b11*m.b27*m.b30 - 224*m.b11*m.b27*m.b31 - 128*m.b11*m.b27*m.b32 - 96*
                       m.b11*m.b27*m.b33 - 64*m.b11*m.b27*m.b34 - 32*m.b11*m.b27*m.b35 - 448*m.b11*m.b28*m.b29 - 352*
                       m.b11*m.b28*m.b30 - 256*m.b11*m.b28*m.b31 - 160*m.b11*m.b28*m.b32 - 96*m.b11*m.b28*m.b33 - 64*
                       m.b11*m.b28*m.b34 - 32*m.b11*m.b28*m.b35 - 384*m.b11*m.b29*m.b30 - 288*m.b11*m.b29*m.b31 - 192*
                       m.b11*m.b29*m.b32 - 96*m.b11*m.b29*m.b33 - 64*m.b11*m.b29*m.b34 - 32*m.b11*m.b29*m.b35 - 320*
                       m.b11*m.b30*m.b31 - 224*m.b11*m.b30*m.b32 - 128*m.b11*m.b30*m.b33 - 64*m.b11*m.b30*m.b34 - 32*
                       m.b11*m.b30*m.b35 - 256*m.b11*m.b31*m.b32 - 160*m.b11*m.b31*m.b33 - 64*m.b11*m.b31*m.b34 - 32*
                       m.b11*m.b31*m.b35 - 192*m.b11*m.b32*m.b33 - 96*m.b11*m.b32*m.b34 - 32*m.b11*m.b32*m.b35 - 128*
                       m.b11*m.b33*m.b34 - 32*m.b11*m.b33*m.b35 - 64*m.b11*m.b34*m.b35 - 640*m.b12*m.b13*m.b14 - 960*
                       m.b12*m.b13*m.b15 - 928*m.b12*m.b13*m.b16 - 896*m.b12*m.b13*m.b17 - 864*m.b12*m.b13*m.b18 - 896*
                       m.b12*m.b13*m.b19 - 928*m.b12*m.b13*m.b20 - 896*m.b12*m.b13*m.b21 - 864*m.b12*m.b13*m.b22 - 832*
                       m.b12*m.b13*m.b23 - 768*m.b12*m.b13*m.b24 - 672*m.b12*m.b13*m.b25 - 608*m.b12*m.b13*m.b26 - 544*
                       m.b12*m.b13*m.b27 - 480*m.b12*m.b13*m.b28 - 416*m.b12*m.b13*m.b29 - 352*m.b12*m.b13*m.b30 - 288*
                       m.b12*m.b13*m.b31 - 224*m.b12*m.b13*m.b32 - 160*m.b12*m.b13*m.b33 - 96*m.b12*m.b13*m.b34 - 32*
                       m.b12*m.b13*m.b35 - 960*m.b12*m.b14*m.b15 - 640*m.b12*m.b14*m.b16 - 928*m.b12*m.b14*m.b17 - 960*
                       m.b12*m.b14*m.b18 - 928*m.b12*m.b14*m.b19 - 960*m.b12*m.b14*m.b20 - 928*m.b12*m.b14*m.b21 - 896*
                       m.b12*m.b14*m.b22 - 832*m.b12*m.b14*m.b23 - 768*m.b12*m.b14*m.b24 - 672*m.b12*m.b14*m.b25 - 576*
                       m.b12*m.b14*m.b26 - 512*m.b12*m.b14*m.b27 - 448*m.b12*m.b14*m.b28 - 384*m.b12*m.b14*m.b29 - 320*
                       m.b12*m.b14*m.b30 - 256*m.b12*m.b14*m.b31 - 192*m.b12*m.b14*m.b32 - 128*m.b12*m.b14*m.b33 - 64*
                       m.b12*m.b14*m.b34 - 32*m.b12*m.b14*m.b35 - 960*m.b12*m.b15*m.b16 - 1024*m.b12*m.b15*m.b17 - 672*
                       m.b12*m.b15*m.b18 - 960*m.b12*m.b15*m.b19 - 992*m.b12*m.b15*m.b20 - 960*m.b12*m.b15*m.b21 - 896*
                       m.b12*m.b15*m.b22 - 832*m.b12*m.b15*m.b23 - 768*m.b12*m.b15*m.b24 - 672*m.b12*m.b15*m.b25 - 576*
                       m.b12*m.b15*m.b26 - 480*m.b12*m.b15*m.b27 - 416*m.b12*m.b15*m.b28 - 352*m.b12*m.b15*m.b29 - 288*
                       m.b12*m.b15*m.b30 - 224*m.b12*m.b15*m.b31 - 160*m.b12*m.b15*m.b32 - 96*m.b12*m.b15*m.b33 - 64*
                       m.b12*m.b15*m.b34 - 32*m.b12*m.b15*m.b35 - 1024*m.b12*m.b16*m.b17 - 1024*m.b12*m.b16*m.b18 - 992*
                       m.b12*m.b16*m.b19 - 640*m.b12*m.b16*m.b20 - 960*m.b12*m.b16*m.b21 - 896*m.b12*m.b16*m.b22 - 832*
                       m.b12*m.b16*m.b23 - 768*m.b12*m.b16*m.b24 - 672*m.b12*m.b16*m.b25 - 576*m.b12*m.b16*m.b26 - 448*
                       m.b12*m.b16*m.b27 - 384*m.b12*m.b16*m.b28 - 320*m.b12*m.b16*m.b29 - 256*m.b12*m.b16*m.b30 - 192*
                       m.b12*m.b16*m.b31 - 128*m.b12*m.b16*m.b32 - 96*m.b12*m.b16*m.b33 - 64*m.b12*m.b16*m.b34 - 32*
                       m.b12*m.b16*m.b35 - 1024*m.b12*m.b17*m.b18 - 1024*m.b12*m.b17*m.b19 - 1024*m.b12*m.b17*m.b20 - 
                       960*m.b12*m.b17*m.b21 - 512*m.b12*m.b17*m.b22 - 832*m.b12*m.b17*m.b23 - 768*m.b12*m.b17*m.b24 - 
                       672*m.b12*m.b17*m.b25 - 576*m.b12*m.b17*m.b26 - 448*m.b12*m.b17*m.b27 - 352*m.b12*m.b17*m.b28 - 
                       288*m.b12*m.b17*m.b29 - 224*m.b12*m.b17*m.b30 - 160*m.b12*m.b17*m.b31 - 128*m.b12*m.b17*m.b32 - 
                       96*m.b12*m.b17*m.b33 - 64*m.b12*m.b17*m.b34 - 32*m.b12*m.b17*m.b35 - 1024*m.b12*m.b18*m.b19 - 
                       1024*m.b12*m.b18*m.b20 - 960*m.b12*m.b18*m.b21 - 896*m.b12*m.b18*m.b22 - 832*m.b12*m.b18*m.b23 - 
                       384*m.b12*m.b18*m.b24 - 672*m.b12*m.b18*m.b25 - 576*m.b12*m.b18*m.b26 - 448*m.b12*m.b18*m.b27 - 
                       320*m.b12*m.b18*m.b28 - 256*m.b12*m.b18*m.b29 - 192*m.b12*m.b18*m.b30 - 160*m.b12*m.b18*m.b31 - 
                       128*m.b12*m.b18*m.b32 - 96*m.b12*m.b18*m.b33 - 64*m.b12*m.b18*m.b34 - 32*m.b12*m.b18*m.b35 - 1024
                       *m.b12*m.b19*m.b20 - 960*m.b12*m.b19*m.b21 - 896*m.b12*m.b19*m.b22 - 832*m.b12*m.b19*m.b23 - 768*
                       m.b12*m.b19*m.b24 - 672*m.b12*m.b19*m.b25 - 256*m.b12*m.b19*m.b26 - 448*m.b12*m.b19*m.b27 - 320*
                       m.b12*m.b19*m.b28 - 224*m.b12*m.b19*m.b29 - 192*m.b12*m.b19*m.b30 - 160*m.b12*m.b19*m.b31 - 128*
                       m.b12*m.b19*m.b32 - 96*m.b12*m.b19*m.b33 - 64*m.b12*m.b19*m.b34 - 32*m.b12*m.b19*m.b35 - 960*
                       m.b12*m.b20*m.b21 - 896*m.b12*m.b20*m.b22 - 832*m.b12*m.b20*m.b23 - 768*m.b12*m.b20*m.b24 - 672*
                       m.b12*m.b20*m.b25 - 576*m.b12*m.b20*m.b26 - 448*m.b12*m.b20*m.b27 - 64*m.b12*m.b20*m.b28 - 224*
                       m.b12*m.b20*m.b29 - 192*m.b12*m.b20*m.b30 - 160*m.b12*m.b20*m.b31 - 128*m.b12*m.b20*m.b32 - 96*
                       m.b12*m.b20*m.b33 - 64*m.b12*m.b20*m.b34 - 32*m.b12*m.b20*m.b35 - 896*m.b12*m.b21*m.b22 - 832*
                       m.b12*m.b21*m.b23 - 768*m.b12*m.b21*m.b24 - 672*m.b12*m.b21*m.b25 - 576*m.b12*m.b21*m.b26 - 448*
                       m.b12*m.b21*m.b27 - 352*m.b12*m.b21*m.b28 - 256*m.b12*m.b21*m.b29 - 160*m.b12*m.b21*m.b31 - 128*
                       m.b12*m.b21*m.b32 - 96*m.b12*m.b21*m.b33 - 64*m.b12*m.b21*m.b34 - 32*m.b12*m.b21*m.b35 - 832*
                       m.b12*m.b22*m.b23 - 768*m.b12*m.b22*m.b24 - 672*m.b12*m.b22*m.b25 - 576*m.b12*m.b22*m.b26 - 480*
                       m.b12*m.b22*m.b27 - 384*m.b12*m.b22*m.b28 - 288*m.b12*m.b22*m.b29 - 192*m.b12*m.b22*m.b30 - 160*
                       m.b12*m.b22*m.b31 - 96*m.b12*m.b22*m.b33 - 64*m.b12*m.b22*m.b34 - 32*m.b12*m.b22*m.b35 - 768*
                       m.b12*m.b23*m.b24 - 672*m.b12*m.b23*m.b25 - 608*m.b12*m.b23*m.b26 - 512*m.b12*m.b23*m.b27 - 416*
                       m.b12*m.b23*m.b28 - 320*m.b12*m.b23*m.b29 - 224*m.b12*m.b23*m.b30 - 160*m.b12*m.b23*m.b31 - 128*
                       m.b12*m.b23*m.b32 - 96*m.b12*m.b23*m.b33 - 32*m.b12*m.b23*m.b35 - 704*m.b12*m.b24*m.b25 - 640*
                       m.b12*m.b24*m.b26 - 544*m.b12*m.b24*m.b27 - 448*m.b12*m.b24*m.b28 - 352*m.b12*m.b24*m.b29 - 256*
                       m.b12*m.b24*m.b30 - 160*m.b12*m.b24*m.b31 - 128*m.b12*m.b24*m.b32 - 96*m.b12*m.b24*m.b33 - 64*
                       m.b12*m.b24*m.b34 - 32*m.b12*m.b24*m.b35 - 640*m.b12*m.b25*m.b26 - 576*m.b12*m.b25*m.b27 - 480*
                       m.b12*m.b25*m.b28 - 384*m.b12*m.b25*m.b29 - 288*m.b12*m.b25*m.b30 - 192*m.b12*m.b25*m.b31 - 128*
                       m.b12*m.b25*m.b32 - 96*m.b12*m.b25*m.b33 - 64*m.b12*m.b25*m.b34 - 32*m.b12*m.b25*m.b35 - 576*
                       m.b12*m.b26*m.b27 - 512*m.b12*m.b26*m.b28 - 416*m.b12*m.b26*m.b29 - 320*m.b12*m.b26*m.b30 - 224*
                       m.b12*m.b26*m.b31 - 128*m.b12*m.b26*m.b32 - 96*m.b12*m.b26*m.b33 - 64*m.b12*m.b26*m.b34 - 32*
                       m.b12*m.b26*m.b35 - 512*m.b12*m.b27*m.b28 - 448*m.b12*m.b27*m.b29 - 352*m.b12*m.b27*m.b30 - 256*
                       m.b12*m.b27*m.b31 - 160*m.b12*m.b27*m.b32 - 96*m.b12*m.b27*m.b33 - 64*m.b12*m.b27*m.b34 - 32*
                       m.b12*m.b27*m.b35 - 448*m.b12*m.b28*m.b29 - 384*m.b12*m.b28*m.b30 - 288*m.b12*m.b28*m.b31 - 192*
                       m.b12*m.b28*m.b32 - 96*m.b12*m.b28*m.b33 - 64*m.b12*m.b28*m.b34 - 32*m.b12*m.b28*m.b35 - 384*
                       m.b12*m.b29*m.b30 - 320*m.b12*m.b29*m.b31 - 224*m.b12*m.b29*m.b32 - 128*m.b12*m.b29*m.b33 - 64*
                       m.b12*m.b29*m.b34 - 32*m.b12*m.b29*m.b35 - 320*m.b12*m.b30*m.b31 - 256*m.b12*m.b30*m.b32 - 160*
                       m.b12*m.b30*m.b33 - 64*m.b12*m.b30*m.b34 - 32*m.b12*m.b30*m.b35 - 256*m.b12*m.b31*m.b32 - 192*
                       m.b12*m.b31*m.b33 - 96*m.b12*m.b31*m.b34 - 32*m.b12*m.b31*m.b35 - 192*m.b12*m.b32*m.b33 - 128*
                       m.b12*m.b32*m.b34 - 32*m.b12*m.b32*m.b35 - 128*m.b12*m.b33*m.b34 - 64*m.b12*m.b33*m.b35 - 64*
                       m.b12*m.b34*m.b35 - 640*m.b13*m.b14*m.b15 - 960*m.b13*m.b14*m.b16 - 960*m.b13*m.b14*m.b17 - 928*
                       m.b13*m.b14*m.b18 - 896*m.b13*m.b14*m.b19 - 960*m.b13*m.b14*m.b20 - 1024*m.b13*m.b14*m.b21 - 992*
                       m.b13*m.b14*m.b22 - 928*m.b13*m.b14*m.b23 - 832*m.b13*m.b14*m.b24 - 736*m.b13*m.b14*m.b25 - 640*
                       m.b13*m.b14*m.b26 - 544*m.b13*m.b14*m.b27 - 480*m.b13*m.b14*m.b28 - 416*m.b13*m.b14*m.b29 - 352*
                       m.b13*m.b14*m.b30 - 288*m.b13*m.b14*m.b31 - 224*m.b13*m.b14*m.b32 - 160*m.b13*m.b14*m.b33 - 96*
                       m.b13*m.b14*m.b34 - 32*m.b13*m.b14*m.b35 - 960*m.b13*m.b15*m.b16 - 640*m.b13*m.b15*m.b17 - 960*
                       m.b13*m.b15*m.b18 - 1024*m.b13*m.b15*m.b19 - 992*m.b13*m.b15*m.b20 - 1056*m.b13*m.b15*m.b21 - 992
                       *m.b13*m.b15*m.b22 - 928*m.b13*m.b15*m.b23 - 832*m.b13*m.b15*m.b24 - 736*m.b13*m.b15*m.b25 - 640*
                       m.b13*m.b15*m.b26 - 512*m.b13*m.b15*m.b27 - 448*m.b13*m.b15*m.b28 - 384*m.b13*m.b15*m.b29 - 320*
                       m.b13*m.b15*m.b30 - 256*m.b13*m.b15*m.b31 - 192*m.b13*m.b15*m.b32 - 128*m.b13*m.b15*m.b33 - 64*
                       m.b13*m.b15*m.b34 - 32*m.b13*m.b15*m.b35 - 960*m.b13*m.b16*m.b17 - 1056*m.b13*m.b16*m.b18 - 736*
                       m.b13*m.b16*m.b19 - 1024*m.b13*m.b16*m.b20 - 1056*m.b13*m.b16*m.b21 - 992*m.b13*m.b16*m.b22 - 928
                       *m.b13*m.b16*m.b23 - 832*m.b13*m.b16*m.b24 - 736*m.b13*m.b16*m.b25 - 640*m.b13*m.b16*m.b26 - 512*
                       m.b13*m.b16*m.b27 - 416*m.b13*m.b16*m.b28 - 352*m.b13*m.b16*m.b29 - 288*m.b13*m.b16*m.b30 - 224*
                       m.b13*m.b16*m.b31 - 160*m.b13*m.b16*m.b32 - 96*m.b13*m.b16*m.b33 - 64*m.b13*m.b16*m.b34 - 32*
                       m.b13*m.b16*m.b35 - 1056*m.b13*m.b17*m.b18 - 1088*m.b13*m.b17*m.b19 - 1024*m.b13*m.b17*m.b20 - 
                       640*m.b13*m.b17*m.b21 - 992*m.b13*m.b17*m.b22 - 928*m.b13*m.b17*m.b23 - 832*m.b13*m.b17*m.b24 - 
                       736*m.b13*m.b17*m.b25 - 640*m.b13*m.b17*m.b26 - 512*m.b13*m.b17*m.b27 - 384*m.b13*m.b17*m.b28 - 
                       320*m.b13*m.b17*m.b29 - 256*m.b13*m.b17*m.b30 - 192*m.b13*m.b17*m.b31 - 128*m.b13*m.b17*m.b32 - 
                       96*m.b13*m.b17*m.b33 - 64*m.b13*m.b17*m.b34 - 32*m.b13*m.b17*m.b35 - 1024*m.b13*m.b18*m.b19 - 
                       1024*m.b13*m.b18*m.b20 - 1056*m.b13*m.b18*m.b21 - 992*m.b13*m.b18*m.b22 - 512*m.b13*m.b18*m.b23
                        - 832*m.b13*m.b18*m.b24 - 736*m.b13*m.b18*m.b25 - 640*m.b13*m.b18*m.b26 - 512*m.b13*m.b18*m.b27
                        - 384*m.b13*m.b18*m.b28 - 288*m.b13*m.b18*m.b29 - 224*m.b13*m.b18*m.b30 - 160*m.b13*m.b18*m.b31
                        - 128*m.b13*m.b18*m.b32 - 96*m.b13*m.b18*m.b33 - 64*m.b13*m.b18*m.b34 - 32*m.b13*m.b18*m.b35 - 
                       1024*m.b13*m.b19*m.b20 - 1056*m.b13*m.b19*m.b21 - 992*m.b13*m.b19*m.b22 - 928*m.b13*m.b19*m.b23
                        - 832*m.b13*m.b19*m.b24 - 384*m.b13*m.b19*m.b25 - 640*m.b13*m.b19*m.b26 - 512*m.b13*m.b19*m.b27
                        - 384*m.b13*m.b19*m.b28 - 256*m.b13*m.b19*m.b29 - 192*m.b13*m.b19*m.b30 - 160*m.b13*m.b19*m.b31
                        - 128*m.b13*m.b19*m.b32 - 96*m.b13*m.b19*m.b33 - 64*m.b13*m.b19*m.b34 - 32*m.b13*m.b19*m.b35 - 
                       1056*m.b13*m.b20*m.b21 - 992*m.b13*m.b20*m.b22 - 928*m.b13*m.b20*m.b23 - 832*m.b13*m.b20*m.b24 - 
                       736*m.b13*m.b20*m.b25 - 640*m.b13*m.b20*m.b26 - 224*m.b13*m.b20*m.b27 - 384*m.b13*m.b20*m.b28 - 
                       256*m.b13*m.b20*m.b29 - 192*m.b13*m.b20*m.b30 - 160*m.b13*m.b20*m.b31 - 128*m.b13*m.b20*m.b32 - 
                       96*m.b13*m.b20*m.b33 - 64*m.b13*m.b20*m.b34 - 32*m.b13*m.b20*m.b35 - 992*m.b13*m.b21*m.b22 - 928*
                       m.b13*m.b21*m.b23 - 832*m.b13*m.b21*m.b24 - 736*m.b13*m.b21*m.b25 - 640*m.b13*m.b21*m.b26 - 512*
                       m.b13*m.b21*m.b27 - 384*m.b13*m.b21*m.b28 - 64*m.b13*m.b21*m.b29 - 192*m.b13*m.b21*m.b30 - 160*
                       m.b13*m.b21*m.b31 - 128*m.b13*m.b21*m.b32 - 96*m.b13*m.b21*m.b33 - 64*m.b13*m.b21*m.b34 - 32*
                       m.b13*m.b21*m.b35 - 928*m.b13*m.b22*m.b23 - 832*m.b13*m.b22*m.b24 - 736*m.b13*m.b22*m.b25 - 640*
                       m.b13*m.b22*m.b26 - 512*m.b13*m.b22*m.b27 - 416*m.b13*m.b22*m.b28 - 320*m.b13*m.b22*m.b29 - 224*
                       m.b13*m.b22*m.b30 - 128*m.b13*m.b22*m.b32 - 96*m.b13*m.b22*m.b33 - 64*m.b13*m.b22*m.b34 - 32*
                       m.b13*m.b22*m.b35 - 832*m.b13*m.b23*m.b24 - 736*m.b13*m.b23*m.b25 - 640*m.b13*m.b23*m.b26 - 544*
                       m.b13*m.b23*m.b27 - 448*m.b13*m.b23*m.b28 - 352*m.b13*m.b23*m.b29 - 256*m.b13*m.b23*m.b30 - 160*
                       m.b13*m.b23*m.b31 - 128*m.b13*m.b23*m.b32 - 64*m.b13*m.b23*m.b34 - 32*m.b13*m.b23*m.b35 - 704*
                       m.b13*m.b24*m.b25 - 640*m.b13*m.b24*m.b26 - 576*m.b13*m.b24*m.b27 - 480*m.b13*m.b24*m.b28 - 384*
                       m.b13*m.b24*m.b29 - 288*m.b13*m.b24*m.b30 - 192*m.b13*m.b24*m.b31 - 128*m.b13*m.b24*m.b32 - 96*
                       m.b13*m.b24*m.b33 - 64*m.b13*m.b24*m.b34 - 640*m.b13*m.b25*m.b26 - 576*m.b13*m.b25*m.b27 - 512*
                       m.b13*m.b25*m.b28 - 416*m.b13*m.b25*m.b29 - 320*m.b13*m.b25*m.b30 - 224*m.b13*m.b25*m.b31 - 128*
                       m.b13*m.b25*m.b32 - 96*m.b13*m.b25*m.b33 - 64*m.b13*m.b25*m.b34 - 32*m.b13*m.b25*m.b35 - 576*
                       m.b13*m.b26*m.b27 - 512*m.b13*m.b26*m.b28 - 448*m.b13*m.b26*m.b29 - 352*m.b13*m.b26*m.b30 - 256*
                       m.b13*m.b26*m.b31 - 160*m.b13*m.b26*m.b32 - 96*m.b13*m.b26*m.b33 - 64*m.b13*m.b26*m.b34 - 32*
                       m.b13*m.b26*m.b35 - 512*m.b13*m.b27*m.b28 - 448*m.b13*m.b27*m.b29 - 384*m.b13*m.b27*m.b30 - 288*
                       m.b13*m.b27*m.b31 - 192*m.b13*m.b27*m.b32 - 96*m.b13*m.b27*m.b33 - 64*m.b13*m.b27*m.b34 - 32*
                       m.b13*m.b27*m.b35 - 448*m.b13*m.b28*m.b29 - 384*m.b13*m.b28*m.b30 - 320*m.b13*m.b28*m.b31 - 224*
                       m.b13*m.b28*m.b32 - 128*m.b13*m.b28*m.b33 - 64*m.b13*m.b28*m.b34 - 32*m.b13*m.b28*m.b35 - 384*
                       m.b13*m.b29*m.b30 - 320*m.b13*m.b29*m.b31 - 256*m.b13*m.b29*m.b32 - 160*m.b13*m.b29*m.b33 - 64*
                       m.b13*m.b29*m.b34 - 32*m.b13*m.b29*m.b35 - 320*m.b13*m.b30*m.b31 - 256*m.b13*m.b30*m.b32 - 192*
                       m.b13*m.b30*m.b33 - 96*m.b13*m.b30*m.b34 - 32*m.b13*m.b30*m.b35 - 256*m.b13*m.b31*m.b32 - 192*
                       m.b13*m.b31*m.b33 - 128*m.b13*m.b31*m.b34 - 32*m.b13*m.b31*m.b35 - 192*m.b13*m.b32*m.b33 - 128*
                       m.b13*m.b32*m.b34 - 64*m.b13*m.b32*m.b35 - 128*m.b13*m.b33*m.b34 - 64*m.b13*m.b33*m.b35 - 64*
                       m.b13*m.b34*m.b35 - 640*m.b14*m.b15*m.b16 - 960*m.b14*m.b15*m.b17 - 960*m.b14*m.b15*m.b18 - 960*
                       m.b14*m.b15*m.b19 - 928*m.b14*m.b15*m.b20 - 1024*m.b14*m.b15*m.b21 - 1088*m.b14*m.b15*m.b22 - 992
                       *m.b14*m.b15*m.b23 - 896*m.b14*m.b15*m.b24 - 800*m.b14*m.b15*m.b25 - 704*m.b14*m.b15*m.b26 - 576*
                       m.b14*m.b15*m.b27 - 480*m.b14*m.b15*m.b28 - 416*m.b14*m.b15*m.b29 - 352*m.b14*m.b15*m.b30 - 288*
                       m.b14*m.b15*m.b31 - 224*m.b14*m.b15*m.b32 - 160*m.b14*m.b15*m.b33 - 96*m.b14*m.b15*m.b34 - 32*
                       m.b14*m.b15*m.b35 - 960*m.b14*m.b16*m.b17 - 640*m.b14*m.b16*m.b18 - 992*m.b14*m.b16*m.b19 - 1088*
                       m.b14*m.b16*m.b20 - 1024*m.b14*m.b16*m.b21 - 1088*m.b14*m.b16*m.b22 - 992*m.b14*m.b16*m.b23 - 896
                       *m.b14*m.b16*m.b24 - 800*m.b14*m.b16*m.b25 - 704*m.b14*m.b16*m.b26 - 576*m.b14*m.b16*m.b27 - 448*
                       m.b14*m.b16*m.b28 - 384*m.b14*m.b16*m.b29 - 320*m.b14*m.b16*m.b30 - 256*m.b14*m.b16*m.b31 - 192*
                       m.b14*m.b16*m.b32 - 128*m.b14*m.b16*m.b33 - 64*m.b14*m.b16*m.b34 - 32*m.b14*m.b16*m.b35 - 960*
                       m.b14*m.b17*m.b18 - 1088*m.b14*m.b17*m.b19 - 768*m.b14*m.b17*m.b20 - 1024*m.b14*m.b17*m.b21 - 
                       1088*m.b14*m.b17*m.b22 - 992*m.b14*m.b17*m.b23 - 896*m.b14*m.b17*m.b24 - 800*m.b14*m.b17*m.b25 - 
                       704*m.b14*m.b17*m.b26 - 576*m.b14*m.b17*m.b27 - 448*m.b14*m.b17*m.b28 - 352*m.b14*m.b17*m.b29 - 
                       288*m.b14*m.b17*m.b30 - 224*m.b14*m.b17*m.b31 - 160*m.b14*m.b17*m.b32 - 96*m.b14*m.b17*m.b33 - 64
                       *m.b14*m.b17*m.b34 - 32*m.b14*m.b17*m.b35 - 1056*m.b14*m.b18*m.b19 - 1088*m.b14*m.b18*m.b20 - 
                       1024*m.b14*m.b18*m.b21 - 640*m.b14*m.b18*m.b22 - 992*m.b14*m.b18*m.b23 - 896*m.b14*m.b18*m.b24 - 
                       800*m.b14*m.b18*m.b25 - 704*m.b14*m.b18*m.b26 - 576*m.b14*m.b18*m.b27 - 448*m.b14*m.b18*m.b28 - 
                       320*m.b14*m.b18*m.b29 - 256*m.b14*m.b18*m.b30 - 192*m.b14*m.b18*m.b31 - 128*m.b14*m.b18*m.b32 - 
                       96*m.b14*m.b18*m.b33 - 64*m.b14*m.b18*m.b34 - 32*m.b14*m.b18*m.b35 - 992*m.b14*m.b19*m.b20 - 1024
                       *m.b14*m.b19*m.b21 - 1088*m.b14*m.b19*m.b22 - 992*m.b14*m.b19*m.b23 - 512*m.b14*m.b19*m.b24 - 800
                       *m.b14*m.b19*m.b25 - 704*m.b14*m.b19*m.b26 - 576*m.b14*m.b19*m.b27 - 448*m.b14*m.b19*m.b28 - 320*
                       m.b14*m.b19*m.b29 - 224*m.b14*m.b19*m.b30 - 160*m.b14*m.b19*m.b31 - 128*m.b14*m.b19*m.b32 - 96*
                       m.b14*m.b19*m.b33 - 64*m.b14*m.b19*m.b34 - 32*m.b14*m.b19*m.b35 - 1024*m.b14*m.b20*m.b21 - 1088*
                       m.b14*m.b20*m.b22 - 992*m.b14*m.b20*m.b23 - 896*m.b14*m.b20*m.b24 - 800*m.b14*m.b20*m.b25 - 384*
                       m.b14*m.b20*m.b26 - 576*m.b14*m.b20*m.b27 - 448*m.b14*m.b20*m.b28 - 320*m.b14*m.b20*m.b29 - 192*
                       m.b14*m.b20*m.b30 - 160*m.b14*m.b20*m.b31 - 128*m.b14*m.b20*m.b32 - 96*m.b14*m.b20*m.b33 - 64*
                       m.b14*m.b20*m.b34 - 32*m.b14*m.b20*m.b35 - 1088*m.b14*m.b21*m.b22 - 992*m.b14*m.b21*m.b23 - 896*
                       m.b14*m.b21*m.b24 - 800*m.b14*m.b21*m.b25 - 704*m.b14*m.b21*m.b26 - 576*m.b14*m.b21*m.b27 - 192*
                       m.b14*m.b21*m.b28 - 320*m.b14*m.b21*m.b29 - 224*m.b14*m.b21*m.b30 - 160*m.b14*m.b21*m.b31 - 128*
                       m.b14*m.b21*m.b32 - 96*m.b14*m.b21*m.b33 - 64*m.b14*m.b21*m.b34 - 32*m.b14*m.b21*m.b35 - 992*
                       m.b14*m.b22*m.b23 - 896*m.b14*m.b22*m.b24 - 800*m.b14*m.b22*m.b25 - 704*m.b14*m.b22*m.b26 - 576*
                       m.b14*m.b22*m.b27 - 448*m.b14*m.b22*m.b28 - 352*m.b14*m.b22*m.b29 - 64*m.b14*m.b22*m.b30 - 160*
                       m.b14*m.b22*m.b31 - 128*m.b14*m.b22*m.b32 - 96*m.b14*m.b22*m.b33 - 64*m.b14*m.b22*m.b34 - 32*
                       m.b14*m.b22*m.b35 - 864*m.b14*m.b23*m.b24 - 768*m.b14*m.b23*m.b25 - 672*m.b14*m.b23*m.b26 - 576*
                       m.b14*m.b23*m.b27 - 480*m.b14*m.b23*m.b28 - 384*m.b14*m.b23*m.b29 - 288*m.b14*m.b23*m.b30 - 192*
                       m.b14*m.b23*m.b31 - 96*m.b14*m.b23*m.b33 - 64*m.b14*m.b23*m.b34 - 32*m.b14*m.b23*m.b35 - 736*
                       m.b14*m.b24*m.b25 - 640*m.b14*m.b24*m.b26 - 576*m.b14*m.b24*m.b27 - 512*m.b14*m.b24*m.b28 - 416*
                       m.b14*m.b24*m.b29 - 320*m.b14*m.b24*m.b30 - 224*m.b14*m.b24*m.b31 - 128*m.b14*m.b24*m.b32 - 96*
                       m.b14*m.b24*m.b33 - 32*m.b14*m.b24*m.b35 - 640*m.b14*m.b25*m.b26 - 576*m.b14*m.b25*m.b27 - 512*
                       m.b14*m.b25*m.b28 - 448*m.b14*m.b25*m.b29 - 352*m.b14*m.b25*m.b30 - 256*m.b14*m.b25*m.b31 - 160*
                       m.b14*m.b25*m.b32 - 96*m.b14*m.b25*m.b33 - 64*m.b14*m.b25*m.b34 - 32*m.b14*m.b25*m.b35 - 576*
                       m.b14*m.b26*m.b27 - 512*m.b14*m.b26*m.b28 - 448*m.b14*m.b26*m.b29 - 384*m.b14*m.b26*m.b30 - 288*
                       m.b14*m.b26*m.b31 - 192*m.b14*m.b26*m.b32 - 96*m.b14*m.b26*m.b33 - 64*m.b14*m.b26*m.b34 - 32*
                       m.b14*m.b26*m.b35 - 512*m.b14*m.b27*m.b28 - 448*m.b14*m.b27*m.b29 - 384*m.b14*m.b27*m.b30 - 320*
                       m.b14*m.b27*m.b31 - 224*m.b14*m.b27*m.b32 - 128*m.b14*m.b27*m.b33 - 64*m.b14*m.b27*m.b34 - 32*
                       m.b14*m.b27*m.b35 - 448*m.b14*m.b28*m.b29 - 384*m.b14*m.b28*m.b30 - 320*m.b14*m.b28*m.b31 - 256*
                       m.b14*m.b28*m.b32 - 160*m.b14*m.b28*m.b33 - 64*m.b14*m.b28*m.b34 - 32*m.b14*m.b28*m.b35 - 384*
                       m.b14*m.b29*m.b30 - 320*m.b14*m.b29*m.b31 - 256*m.b14*m.b29*m.b32 - 192*m.b14*m.b29*m.b33 - 96*
                       m.b14*m.b29*m.b34 - 32*m.b14*m.b29*m.b35 - 320*m.b14*m.b30*m.b31 - 256*m.b14*m.b30*m.b32 - 192*
                       m.b14*m.b30*m.b33 - 128*m.b14*m.b30*m.b34 - 32*m.b14*m.b30*m.b35 - 256*m.b14*m.b31*m.b32 - 192*
                       m.b14*m.b31*m.b33 - 128*m.b14*m.b31*m.b34 - 64*m.b14*m.b31*m.b35 - 192*m.b14*m.b32*m.b33 - 128*
                       m.b14*m.b32*m.b34 - 64*m.b14*m.b32*m.b35 - 128*m.b14*m.b33*m.b34 - 64*m.b14*m.b33*m.b35 - 64*
                       m.b14*m.b34*m.b35 - 640*m.b15*m.b16*m.b17 - 960*m.b15*m.b16*m.b18 - 960*m.b15*m.b16*m.b19 - 992*
                       m.b15*m.b16*m.b20 - 960*m.b15*m.b16*m.b21 - 1024*m.b15*m.b16*m.b22 - 1056*m.b15*m.b16*m.b23 - 960
                       *m.b15*m.b16*m.b24 - 864*m.b15*m.b16*m.b25 - 768*m.b15*m.b16*m.b26 - 640*m.b15*m.b16*m.b27 - 512*
                       m.b15*m.b16*m.b28 - 416*m.b15*m.b16*m.b29 - 352*m.b15*m.b16*m.b30 - 288*m.b15*m.b16*m.b31 - 224*
                       m.b15*m.b16*m.b32 - 160*m.b15*m.b16*m.b33 - 96*m.b15*m.b16*m.b34 - 32*m.b15*m.b16*m.b35 - 960*
                       m.b15*m.b17*m.b18 - 640*m.b15*m.b17*m.b19 - 1024*m.b15*m.b17*m.b20 - 1088*m.b15*m.b17*m.b21 - 
                       1024*m.b15*m.b17*m.b22 - 1056*m.b15*m.b17*m.b23 - 960*m.b15*m.b17*m.b24 - 864*m.b15*m.b17*m.b25
                        - 768*m.b15*m.b17*m.b26 - 640*m.b15*m.b17*m.b27 - 512*m.b15*m.b17*m.b28 - 384*m.b15*m.b17*m.b29
                        - 320*m.b15*m.b17*m.b30 - 256*m.b15*m.b17*m.b31 - 192*m.b15*m.b17*m.b32 - 128*m.b15*m.b17*m.b33
                        - 64*m.b15*m.b17*m.b34 - 32*m.b15*m.b17*m.b35 - 960*m.b15*m.b18*m.b19 - 1056*m.b15*m.b18*m.b20
                        - 768*m.b15*m.b18*m.b21 - 1024*m.b15*m.b18*m.b22 - 1056*m.b15*m.b18*m.b23 - 960*m.b15*m.b18*
                       m.b24 - 864*m.b15*m.b18*m.b25 - 768*m.b15*m.b18*m.b26 - 640*m.b15*m.b18*m.b27 - 512*m.b15*m.b18*
                       m.b28 - 384*m.b15*m.b18*m.b29 - 288*m.b15*m.b18*m.b30 - 224*m.b15*m.b18*m.b31 - 160*m.b15*m.b18*
                       m.b32 - 96*m.b15*m.b18*m.b33 - 64*m.b15*m.b18*m.b34 - 32*m.b15*m.b18*m.b35 - 1024*m.b15*m.b19*
                       m.b20 - 1088*m.b15*m.b19*m.b21 - 1024*m.b15*m.b19*m.b22 - 640*m.b15*m.b19*m.b23 - 960*m.b15*m.b19
                       *m.b24 - 864*m.b15*m.b19*m.b25 - 768*m.b15*m.b19*m.b26 - 640*m.b15*m.b19*m.b27 - 512*m.b15*m.b19*
                       m.b28 - 384*m.b15*m.b19*m.b29 - 256*m.b15*m.b19*m.b30 - 192*m.b15*m.b19*m.b31 - 128*m.b15*m.b19*
                       m.b32 - 96*m.b15*m.b19*m.b33 - 64*m.b15*m.b19*m.b34 - 32*m.b15*m.b19*m.b35 - 960*m.b15*m.b20*
                       m.b21 - 1024*m.b15*m.b20*m.b22 - 1056*m.b15*m.b20*m.b23 - 960*m.b15*m.b20*m.b24 - 512*m.b15*m.b20
                       *m.b25 - 768*m.b15*m.b20*m.b26 - 640*m.b15*m.b20*m.b27 - 512*m.b15*m.b20*m.b28 - 384*m.b15*m.b20*
                       m.b29 - 256*m.b15*m.b20*m.b30 - 160*m.b15*m.b20*m.b31 - 128*m.b15*m.b20*m.b32 - 96*m.b15*m.b20*
                       m.b33 - 64*m.b15*m.b20*m.b34 - 32*m.b15*m.b20*m.b35 - 1024*m.b15*m.b21*m.b22 - 1056*m.b15*m.b21*
                       m.b23 - 960*m.b15*m.b21*m.b24 - 864*m.b15*m.b21*m.b25 - 768*m.b15*m.b21*m.b26 - 352*m.b15*m.b21*
                       m.b27 - 512*m.b15*m.b21*m.b28 - 384*m.b15*m.b21*m.b29 - 256*m.b15*m.b21*m.b30 - 160*m.b15*m.b21*
                       m.b31 - 128*m.b15*m.b21*m.b32 - 96*m.b15*m.b21*m.b33 - 64*m.b15*m.b21*m.b34 - 32*m.b15*m.b21*
                       m.b35 - 1024*m.b15*m.b22*m.b23 - 928*m.b15*m.b22*m.b24 - 832*m.b15*m.b22*m.b25 - 736*m.b15*m.b22*
                       m.b26 - 640*m.b15*m.b22*m.b27 - 512*m.b15*m.b22*m.b28 - 160*m.b15*m.b22*m.b29 - 288*m.b15*m.b22*
                       m.b30 - 192*m.b15*m.b22*m.b31 - 128*m.b15*m.b22*m.b32 - 96*m.b15*m.b22*m.b33 - 64*m.b15*m.b22*
                       m.b34 - 32*m.b15*m.b22*m.b35 - 896*m.b15*m.b23*m.b24 - 800*m.b15*m.b23*m.b25 - 704*m.b15*m.b23*
                       m.b26 - 608*m.b15*m.b23*m.b27 - 512*m.b15*m.b23*m.b28 - 416*m.b15*m.b23*m.b29 - 320*m.b15*m.b23*
                       m.b30 - 64*m.b15*m.b23*m.b31 - 128*m.b15*m.b23*m.b32 - 96*m.b15*m.b23*m.b33 - 64*m.b15*m.b23*
                       m.b34 - 32*m.b15*m.b23*m.b35 - 768*m.b15*m.b24*m.b25 - 672*m.b15*m.b24*m.b26 - 576*m.b15*m.b24*
                       m.b27 - 512*m.b15*m.b24*m.b28 - 448*m.b15*m.b24*m.b29 - 352*m.b15*m.b24*m.b30 - 256*m.b15*m.b24*
                       m.b31 - 160*m.b15*m.b24*m.b32 - 64*m.b15*m.b24*m.b34 - 32*m.b15*m.b24*m.b35 - 640*m.b15*m.b25*
                       m.b26 - 576*m.b15*m.b25*m.b27 - 512*m.b15*m.b25*m.b28 - 448*m.b15*m.b25*m.b29 - 384*m.b15*m.b25*
                       m.b30 - 288*m.b15*m.b25*m.b31 - 192*m.b15*m.b25*m.b32 - 96*m.b15*m.b25*m.b33 - 64*m.b15*m.b25*
                       m.b34 - 576*m.b15*m.b26*m.b27 - 512*m.b15*m.b26*m.b28 - 448*m.b15*m.b26*m.b29 - 384*m.b15*m.b26*
                       m.b30 - 320*m.b15*m.b26*m.b31 - 224*m.b15*m.b26*m.b32 - 128*m.b15*m.b26*m.b33 - 64*m.b15*m.b26*
                       m.b34 - 32*m.b15*m.b26*m.b35 - 512*m.b15*m.b27*m.b28 - 448*m.b15*m.b27*m.b29 - 384*m.b15*m.b27*
                       m.b30 - 320*m.b15*m.b27*m.b31 - 256*m.b15*m.b27*m.b32 - 160*m.b15*m.b27*m.b33 - 64*m.b15*m.b27*
                       m.b34 - 32*m.b15*m.b27*m.b35 - 448*m.b15*m.b28*m.b29 - 384*m.b15*m.b28*m.b30 - 320*m.b15*m.b28*
                       m.b31 - 256*m.b15*m.b28*m.b32 - 192*m.b15*m.b28*m.b33 - 96*m.b15*m.b28*m.b34 - 32*m.b15*m.b28*
                       m.b35 - 384*m.b15*m.b29*m.b30 - 320*m.b15*m.b29*m.b31 - 256*m.b15*m.b29*m.b32 - 192*m.b15*m.b29*
                       m.b33 - 128*m.b15*m.b29*m.b34 - 32*m.b15*m.b29*m.b35 - 320*m.b15*m.b30*m.b31 - 256*m.b15*m.b30*
                       m.b32 - 192*m.b15*m.b30*m.b33 - 128*m.b15*m.b30*m.b34 - 64*m.b15*m.b30*m.b35 - 256*m.b15*m.b31*
                       m.b32 - 192*m.b15*m.b31*m.b33 - 128*m.b15*m.b31*m.b34 - 64*m.b15*m.b31*m.b35 - 192*m.b15*m.b32*
                       m.b33 - 128*m.b15*m.b32*m.b34 - 64*m.b15*m.b32*m.b35 - 128*m.b15*m.b33*m.b34 - 64*m.b15*m.b33*
                       m.b35 - 64*m.b15*m.b34*m.b35 - 640*m.b16*m.b17*m.b18 - 960*m.b16*m.b17*m.b19 - 960*m.b16*m.b17*
                       m.b20 - 1024*m.b16*m.b17*m.b21 - 992*m.b16*m.b17*m.b22 - 1024*m.b16*m.b17*m.b23 - 1024*m.b16*
                       m.b17*m.b24 - 928*m.b16*m.b17*m.b25 - 832*m.b16*m.b17*m.b26 - 704*m.b16*m.b17*m.b27 - 576*m.b16*
                       m.b17*m.b28 - 448*m.b16*m.b17*m.b29 - 352*m.b16*m.b17*m.b30 - 288*m.b16*m.b17*m.b31 - 224*m.b16*
                       m.b17*m.b32 - 160*m.b16*m.b17*m.b33 - 96*m.b16*m.b17*m.b34 - 32*m.b16*m.b17*m.b35 - 960*m.b16*
                       m.b18*m.b19 - 640*m.b16*m.b18*m.b20 - 1056*m.b16*m.b18*m.b21 - 1088*m.b16*m.b18*m.b22 - 1024*
                       m.b16*m.b18*m.b23 - 1024*m.b16*m.b18*m.b24 - 928*m.b16*m.b18*m.b25 - 832*m.b16*m.b18*m.b26 - 704*
                       m.b16*m.b18*m.b27 - 576*m.b16*m.b18*m.b28 - 448*m.b16*m.b18*m.b29 - 320*m.b16*m.b18*m.b30 - 256*
                       m.b16*m.b18*m.b31 - 192*m.b16*m.b18*m.b32 - 128*m.b16*m.b18*m.b33 - 64*m.b16*m.b18*m.b34 - 32*
                       m.b16*m.b18*m.b35 - 960*m.b16*m.b19*m.b20 - 1024*m.b16*m.b19*m.b21 - 768*m.b16*m.b19*m.b22 - 1024
                       *m.b16*m.b19*m.b23 - 1024*m.b16*m.b19*m.b24 - 928*m.b16*m.b19*m.b25 - 832*m.b16*m.b19*m.b26 - 704
                       *m.b16*m.b19*m.b27 - 576*m.b16*m.b19*m.b28 - 448*m.b16*m.b19*m.b29 - 320*m.b16*m.b19*m.b30 - 224*
                       m.b16*m.b19*m.b31 - 160*m.b16*m.b19*m.b32 - 96*m.b16*m.b19*m.b33 - 64*m.b16*m.b19*m.b34 - 32*
                       m.b16*m.b19*m.b35 - 992*m.b16*m.b20*m.b21 - 1088*m.b16*m.b20*m.b22 - 1024*m.b16*m.b20*m.b23 - 640
                       *m.b16*m.b20*m.b24 - 928*m.b16*m.b20*m.b25 - 832*m.b16*m.b20*m.b26 - 704*m.b16*m.b20*m.b27 - 576*
                       m.b16*m.b20*m.b28 - 448*m.b16*m.b20*m.b29 - 320*m.b16*m.b20*m.b30 - 192*m.b16*m.b20*m.b31 - 128*
                       m.b16*m.b20*m.b32 - 96*m.b16*m.b20*m.b33 - 64*m.b16*m.b20*m.b34 - 32*m.b16*m.b20*m.b35 - 928*
                       m.b16*m.b21*m.b22 - 992*m.b16*m.b21*m.b23 - 992*m.b16*m.b21*m.b24 - 896*m.b16*m.b21*m.b25 - 480*
                       m.b16*m.b21*m.b26 - 704*m.b16*m.b21*m.b27 - 576*m.b16*m.b21*m.b28 - 448*m.b16*m.b21*m.b29 - 320*
                       m.b16*m.b21*m.b30 - 192*m.b16*m.b21*m.b31 - 128*m.b16*m.b21*m.b32 - 96*m.b16*m.b21*m.b33 - 64*
                       m.b16*m.b21*m.b34 - 32*m.b16*m.b21*m.b35 - 960*m.b16*m.b22*m.b23 - 960*m.b16*m.b22*m.b24 - 864*
                       m.b16*m.b22*m.b25 - 768*m.b16*m.b22*m.b26 - 672*m.b16*m.b22*m.b27 - 320*m.b16*m.b22*m.b28 - 448*
                       m.b16*m.b22*m.b29 - 320*m.b16*m.b22*m.b30 - 224*m.b16*m.b22*m.b31 - 128*m.b16*m.b22*m.b32 - 96*
                       m.b16*m.b22*m.b33 - 64*m.b16*m.b22*m.b34 - 32*m.b16*m.b22*m.b35 - 928*m.b16*m.b23*m.b24 - 832*
                       m.b16*m.b23*m.b25 - 736*m.b16*m.b23*m.b26 - 640*m.b16*m.b23*m.b27 - 544*m.b16*m.b23*m.b28 - 448*
                       m.b16*m.b23*m.b29 - 160*m.b16*m.b23*m.b30 - 256*m.b16*m.b23*m.b31 - 160*m.b16*m.b23*m.b32 - 96*
                       m.b16*m.b23*m.b33 - 64*m.b16*m.b23*m.b34 - 32*m.b16*m.b23*m.b35 - 800*m.b16*m.b24*m.b25 - 704*
                       m.b16*m.b24*m.b26 - 608*m.b16*m.b24*m.b27 - 512*m.b16*m.b24*m.b28 - 448*m.b16*m.b24*m.b29 - 384*
                       m.b16*m.b24*m.b30 - 288*m.b16*m.b24*m.b31 - 64*m.b16*m.b24*m.b32 - 96*m.b16*m.b24*m.b33 - 64*
                       m.b16*m.b24*m.b34 - 32*m.b16*m.b24*m.b35 - 672*m.b16*m.b25*m.b26 - 576*m.b16*m.b25*m.b27 - 512*
                       m.b16*m.b25*m.b28 - 448*m.b16*m.b25*m.b29 - 384*m.b16*m.b25*m.b30 - 320*m.b16*m.b25*m.b31 - 224*
                       m.b16*m.b25*m.b32 - 128*m.b16*m.b25*m.b33 - 32*m.b16*m.b25*m.b35 - 576*m.b16*m.b26*m.b27 - 512*
                       m.b16*m.b26*m.b28 - 448*m.b16*m.b26*m.b29 - 384*m.b16*m.b26*m.b30 - 320*m.b16*m.b26*m.b31 - 256*
                       m.b16*m.b26*m.b32 - 160*m.b16*m.b26*m.b33 - 64*m.b16*m.b26*m.b34 - 32*m.b16*m.b26*m.b35 - 512*
                       m.b16*m.b27*m.b28 - 448*m.b16*m.b27*m.b29 - 384*m.b16*m.b27*m.b30 - 320*m.b16*m.b27*m.b31 - 256*
                       m.b16*m.b27*m.b32 - 192*m.b16*m.b27*m.b33 - 96*m.b16*m.b27*m.b34 - 32*m.b16*m.b27*m.b35 - 448*
                       m.b16*m.b28*m.b29 - 384*m.b16*m.b28*m.b30 - 320*m.b16*m.b28*m.b31 - 256*m.b16*m.b28*m.b32 - 192*
                       m.b16*m.b28*m.b33 - 128*m.b16*m.b28*m.b34 - 32*m.b16*m.b28*m.b35 - 384*m.b16*m.b29*m.b30 - 320*
                       m.b16*m.b29*m.b31 - 256*m.b16*m.b29*m.b32 - 192*m.b16*m.b29*m.b33 - 128*m.b16*m.b29*m.b34 - 64*
                       m.b16*m.b29*m.b35 - 320*m.b16*m.b30*m.b31 - 256*m.b16*m.b30*m.b32 - 192*m.b16*m.b30*m.b33 - 128*
                       m.b16*m.b30*m.b34 - 64*m.b16*m.b30*m.b35 - 256*m.b16*m.b31*m.b32 - 192*m.b16*m.b31*m.b33 - 128*
                       m.b16*m.b31*m.b34 - 64*m.b16*m.b31*m.b35 - 192*m.b16*m.b32*m.b33 - 128*m.b16*m.b32*m.b34 - 64*
                       m.b16*m.b32*m.b35 - 128*m.b16*m.b33*m.b34 - 64*m.b16*m.b33*m.b35 - 64*m.b16*m.b34*m.b35 - 640*
                       m.b17*m.b18*m.b19 - 960*m.b17*m.b18*m.b20 - 960*m.b17*m.b18*m.b21 - 1056*m.b17*m.b18*m.b22 - 1024
                       *m.b17*m.b18*m.b23 - 1024*m.b17*m.b18*m.b24 - 992*m.b17*m.b18*m.b25 - 896*m.b17*m.b18*m.b26 - 768
                       *m.b17*m.b18*m.b27 - 640*m.b17*m.b18*m.b28 - 512*m.b17*m.b18*m.b29 - 384*m.b17*m.b18*m.b30 - 288*
                       m.b17*m.b18*m.b31 - 224*m.b17*m.b18*m.b32 - 160*m.b17*m.b18*m.b33 - 96*m.b17*m.b18*m.b34 - 32*
                       m.b17*m.b18*m.b35 - 960*m.b17*m.b19*m.b20 - 640*m.b17*m.b19*m.b21 - 1088*m.b17*m.b19*m.b22 - 1088
                       *m.b17*m.b19*m.b23 - 1024*m.b17*m.b19*m.b24 - 992*m.b17*m.b19*m.b25 - 896*m.b17*m.b19*m.b26 - 768
                       *m.b17*m.b19*m.b27 - 640*m.b17*m.b19*m.b28 - 512*m.b17*m.b19*m.b29 - 384*m.b17*m.b19*m.b30 - 256*
                       m.b17*m.b19*m.b31 - 192*m.b17*m.b19*m.b32 - 128*m.b17*m.b19*m.b33 - 64*m.b17*m.b19*m.b34 - 32*
                       m.b17*m.b19*m.b35 - 960*m.b17*m.b20*m.b21 - 992*m.b17*m.b20*m.b22 - 736*m.b17*m.b20*m.b23 - 992*
                       m.b17*m.b20*m.b24 - 960*m.b17*m.b20*m.b25 - 864*m.b17*m.b20*m.b26 - 768*m.b17*m.b20*m.b27 - 640*
                       m.b17*m.b20*m.b28 - 512*m.b17*m.b20*m.b29 - 384*m.b17*m.b20*m.b30 - 256*m.b17*m.b20*m.b31 - 160*
                       m.b17*m.b20*m.b32 - 96*m.b17*m.b20*m.b33 - 64*m.b17*m.b20*m.b34 - 32*m.b17*m.b20*m.b35 - 960*
                       m.b17*m.b21*m.b22 - 1024*m.b17*m.b21*m.b23 - 960*m.b17*m.b21*m.b24 - 576*m.b17*m.b21*m.b25 - 832*
                       m.b17*m.b21*m.b26 - 736*m.b17*m.b21*m.b27 - 640*m.b17*m.b21*m.b28 - 512*m.b17*m.b21*m.b29 - 384*
                       m.b17*m.b21*m.b30 - 256*m.b17*m.b21*m.b31 - 128*m.b17*m.b21*m.b32 - 96*m.b17*m.b21*m.b33 - 64*
                       m.b17*m.b21*m.b34 - 32*m.b17*m.b21*m.b35 - 896*m.b17*m.b22*m.b23 - 928*m.b17*m.b22*m.b24 - 896*
                       m.b17*m.b22*m.b25 - 800*m.b17*m.b22*m.b26 - 416*m.b17*m.b22*m.b27 - 608*m.b17*m.b22*m.b28 - 512*
                       m.b17*m.b22*m.b29 - 384*m.b17*m.b22*m.b30 - 256*m.b17*m.b22*m.b31 - 160*m.b17*m.b22*m.b32 - 96*
                       m.b17*m.b22*m.b33 - 64*m.b17*m.b22*m.b34 - 32*m.b17*m.b22*m.b35 - 896*m.b17*m.b23*m.b24 - 864*
                       m.b17*m.b23*m.b25 - 768*m.b17*m.b23*m.b26 - 672*m.b17*m.b23*m.b27 - 576*m.b17*m.b23*m.b28 - 256*
                       m.b17*m.b23*m.b29 - 384*m.b17*m.b23*m.b30 - 288*m.b17*m.b23*m.b31 - 192*m.b17*m.b23*m.b32 - 96*
                       m.b17*m.b23*m.b33 - 64*m.b17*m.b23*m.b34 - 32*m.b17*m.b23*m.b35 - 832*m.b17*m.b24*m.b25 - 736*
                       m.b17*m.b24*m.b26 - 640*m.b17*m.b24*m.b27 - 544*m.b17*m.b24*m.b28 - 448*m.b17*m.b24*m.b29 - 384*
                       m.b17*m.b24*m.b30 - 160*m.b17*m.b24*m.b31 - 224*m.b17*m.b24*m.b32 - 128*m.b17*m.b24*m.b33 - 64*
                       m.b17*m.b24*m.b34 - 32*m.b17*m.b24*m.b35 - 704*m.b17*m.b25*m.b26 - 608*m.b17*m.b25*m.b27 - 512*
                       m.b17*m.b25*m.b28 - 448*m.b17*m.b25*m.b29 - 384*m.b17*m.b25*m.b30 - 320*m.b17*m.b25*m.b31 - 256*
                       m.b17*m.b25*m.b32 - 64*m.b17*m.b25*m.b33 - 64*m.b17*m.b25*m.b34 - 32*m.b17*m.b25*m.b35 - 576*
                       m.b17*m.b26*m.b27 - 512*m.b17*m.b26*m.b28 - 448*m.b17*m.b26*m.b29 - 384*m.b17*m.b26*m.b30 - 320*
                       m.b17*m.b26*m.b31 - 256*m.b17*m.b26*m.b32 - 192*m.b17*m.b26*m.b33 - 96*m.b17*m.b26*m.b34 - 512*
                       m.b17*m.b27*m.b28 - 448*m.b17*m.b27*m.b29 - 384*m.b17*m.b27*m.b30 - 320*m.b17*m.b27*m.b31 - 256*
                       m.b17*m.b27*m.b32 - 192*m.b17*m.b27*m.b33 - 128*m.b17*m.b27*m.b34 - 32*m.b17*m.b27*m.b35 - 448*
                       m.b17*m.b28*m.b29 - 384*m.b17*m.b28*m.b30 - 320*m.b17*m.b28*m.b31 - 256*m.b17*m.b28*m.b32 - 192*
                       m.b17*m.b28*m.b33 - 128*m.b17*m.b28*m.b34 - 64*m.b17*m.b28*m.b35 - 384*m.b17*m.b29*m.b30 - 320*
                       m.b17*m.b29*m.b31 - 256*m.b17*m.b29*m.b32 - 192*m.b17*m.b29*m.b33 - 128*m.b17*m.b29*m.b34 - 64*
                       m.b17*m.b29*m.b35 - 320*m.b17*m.b30*m.b31 - 256*m.b17*m.b30*m.b32 - 192*m.b17*m.b30*m.b33 - 128*
                       m.b17*m.b30*m.b34 - 64*m.b17*m.b30*m.b35 - 256*m.b17*m.b31*m.b32 - 192*m.b17*m.b31*m.b33 - 128*
                       m.b17*m.b31*m.b34 - 64*m.b17*m.b31*m.b35 - 192*m.b17*m.b32*m.b33 - 128*m.b17*m.b32*m.b34 - 64*
                       m.b17*m.b32*m.b35 - 128*m.b17*m.b33*m.b34 - 64*m.b17*m.b33*m.b35 - 64*m.b17*m.b34*m.b35 - 640*
                       m.b18*m.b19*m.b20 - 960*m.b18*m.b19*m.b21 - 960*m.b18*m.b19*m.b22 - 1056*m.b18*m.b19*m.b23 - 1024
                       *m.b18*m.b19*m.b24 - 992*m.b18*m.b19*m.b25 - 928*m.b18*m.b19*m.b26 - 832*m.b18*m.b19*m.b27 - 704*
                       m.b18*m.b19*m.b28 - 576*m.b18*m.b19*m.b29 - 448*m.b18*m.b19*m.b30 - 320*m.b18*m.b19*m.b31 - 224*
                       m.b18*m.b19*m.b32 - 160*m.b18*m.b19*m.b33 - 96*m.b18*m.b19*m.b34 - 32*m.b18*m.b19*m.b35 - 960*
                       m.b18*m.b20*m.b21 - 640*m.b18*m.b20*m.b22 - 1056*m.b18*m.b20*m.b23 - 1024*m.b18*m.b20*m.b24 - 960
                       *m.b18*m.b20*m.b25 - 896*m.b18*m.b20*m.b26 - 800*m.b18*m.b20*m.b27 - 704*m.b18*m.b20*m.b28 - 576*
                       m.b18*m.b20*m.b29 - 448*m.b18*m.b20*m.b30 - 320*m.b18*m.b20*m.b31 - 192*m.b18*m.b20*m.b32 - 128*
                       m.b18*m.b20*m.b33 - 64*m.b18*m.b20*m.b34 - 32*m.b18*m.b20*m.b35 - 960*m.b18*m.b21*m.b22 - 960*
                       m.b18*m.b21*m.b23 - 672*m.b18*m.b21*m.b24 - 928*m.b18*m.b21*m.b25 - 864*m.b18*m.b21*m.b26 - 768*
                       m.b18*m.b21*m.b27 - 672*m.b18*m.b21*m.b28 - 576*m.b18*m.b21*m.b29 - 448*m.b18*m.b21*m.b30 - 320*
                       m.b18*m.b21*m.b31 - 192*m.b18*m.b21*m.b32 - 96*m.b18*m.b21*m.b33 - 64*m.b18*m.b21*m.b34 - 32*
                       m.b18*m.b21*m.b35 - 928*m.b18*m.b22*m.b23 - 960*m.b18*m.b22*m.b24 - 896*m.b18*m.b22*m.b25 - 512*
                       m.b18*m.b22*m.b26 - 736*m.b18*m.b22*m.b27 - 640*m.b18*m.b22*m.b28 - 544*m.b18*m.b22*m.b29 - 448*
                       m.b18*m.b22*m.b30 - 320*m.b18*m.b22*m.b31 - 192*m.b18*m.b22*m.b32 - 96*m.b18*m.b22*m.b33 - 64*
                       m.b18*m.b22*m.b34 - 32*m.b18*m.b22*m.b35 - 864*m.b18*m.b23*m.b24 - 864*m.b18*m.b23*m.b25 - 800*
                       m.b18*m.b23*m.b26 - 704*m.b18*m.b23*m.b27 - 352*m.b18*m.b23*m.b28 - 512*m.b18*m.b23*m.b29 - 416*
                       m.b18*m.b23*m.b30 - 320*m.b18*m.b23*m.b31 - 224*m.b18*m.b23*m.b32 - 128*m.b18*m.b23*m.b33 - 64*
                       m.b18*m.b23*m.b34 - 32*m.b18*m.b23*m.b35 - 832*m.b18*m.b24*m.b25 - 768*m.b18*m.b24*m.b26 - 672*
                       m.b18*m.b24*m.b27 - 576*m.b18*m.b24*m.b28 - 480*m.b18*m.b24*m.b29 - 192*m.b18*m.b24*m.b30 - 320*
                       m.b18*m.b24*m.b31 - 256*m.b18*m.b24*m.b32 - 160*m.b18*m.b24*m.b33 - 64*m.b18*m.b24*m.b34 - 32*
                       m.b18*m.b24*m.b35 - 736*m.b18*m.b25*m.b26 - 640*m.b18*m.b25*m.b27 - 544*m.b18*m.b25*m.b28 - 448*
                       m.b18*m.b25*m.b29 - 384*m.b18*m.b25*m.b30 - 320*m.b18*m.b25*m.b31 - 128*m.b18*m.b25*m.b32 - 192*
                       m.b18*m.b25*m.b33 - 96*m.b18*m.b25*m.b34 - 32*m.b18*m.b25*m.b35 - 608*m.b18*m.b26*m.b27 - 512*
                       m.b18*m.b26*m.b28 - 448*m.b18*m.b26*m.b29 - 384*m.b18*m.b26*m.b30 - 320*m.b18*m.b26*m.b31 - 256*
                       m.b18*m.b26*m.b32 - 192*m.b18*m.b26*m.b33 - 64*m.b18*m.b26*m.b34 - 32*m.b18*m.b26*m.b35 - 512*
                       m.b18*m.b27*m.b28 - 448*m.b18*m.b27*m.b29 - 384*m.b18*m.b27*m.b30 - 320*m.b18*m.b27*m.b31 - 256*
                       m.b18*m.b27*m.b32 - 192*m.b18*m.b27*m.b33 - 128*m.b18*m.b27*m.b34 - 64*m.b18*m.b27*m.b35 - 448*
                       m.b18*m.b28*m.b29 - 384*m.b18*m.b28*m.b30 - 320*m.b18*m.b28*m.b31 - 256*m.b18*m.b28*m.b32 - 192*
                       m.b18*m.b28*m.b33 - 128*m.b18*m.b28*m.b34 - 64*m.b18*m.b28*m.b35 - 384*m.b18*m.b29*m.b30 - 320*
                       m.b18*m.b29*m.b31 - 256*m.b18*m.b29*m.b32 - 192*m.b18*m.b29*m.b33 - 128*m.b18*m.b29*m.b34 - 64*
                       m.b18*m.b29*m.b35 - 320*m.b18*m.b30*m.b31 - 256*m.b18*m.b30*m.b32 - 192*m.b18*m.b30*m.b33 - 128*
                       m.b18*m.b30*m.b34 - 64*m.b18*m.b30*m.b35 - 256*m.b18*m.b31*m.b32 - 192*m.b18*m.b31*m.b33 - 128*
                       m.b18*m.b31*m.b34 - 64*m.b18*m.b31*m.b35 - 192*m.b18*m.b32*m.b33 - 128*m.b18*m.b32*m.b34 - 64*
                       m.b18*m.b32*m.b35 - 128*m.b18*m.b33*m.b34 - 64*m.b18*m.b33*m.b35 - 64*m.b18*m.b34*m.b35 - 640*
                       m.b19*m.b20*m.b21 - 960*m.b19*m.b20*m.b22 - 960*m.b19*m.b20*m.b23 - 1024*m.b19*m.b20*m.b24 - 992*
                       m.b19*m.b20*m.b25 - 928*m.b19*m.b20*m.b26 - 832*m.b19*m.b20*m.b27 - 736*m.b19*m.b20*m.b28 - 640*
                       m.b19*m.b20*m.b29 - 512*m.b19*m.b20*m.b30 - 384*m.b19*m.b20*m.b31 - 256*m.b19*m.b20*m.b32 - 160*
                       m.b19*m.b20*m.b33 - 96*m.b19*m.b20*m.b34 - 32*m.b19*m.b20*m.b35 - 960*m.b19*m.b21*m.b22 - 640*
                       m.b19*m.b21*m.b23 - 1024*m.b19*m.b21*m.b24 - 960*m.b19*m.b21*m.b25 - 896*m.b19*m.b21*m.b26 - 800*
                       m.b19*m.b21*m.b27 - 704*m.b19*m.b21*m.b28 - 608*m.b19*m.b21*m.b29 - 512*m.b19*m.b21*m.b30 - 384*
                       m.b19*m.b21*m.b31 - 256*m.b19*m.b21*m.b32 - 128*m.b19*m.b21*m.b33 - 64*m.b19*m.b21*m.b34 - 32*
                       m.b19*m.b21*m.b35 - 960*m.b19*m.b22*m.b23 - 928*m.b19*m.b22*m.b24 - 608*m.b19*m.b22*m.b25 - 864*
                       m.b19*m.b22*m.b26 - 768*m.b19*m.b22*m.b27 - 672*m.b19*m.b22*m.b28 - 576*m.b19*m.b22*m.b29 - 480*
                       m.b19*m.b22*m.b30 - 384*m.b19*m.b22*m.b31 - 256*m.b19*m.b22*m.b32 - 128*m.b19*m.b22*m.b33 - 64*
                       m.b19*m.b22*m.b34 - 32*m.b19*m.b22*m.b35 - 896*m.b19*m.b23*m.b24 - 896*m.b19*m.b23*m.b25 - 832*
                       m.b19*m.b23*m.b26 - 448*m.b19*m.b23*m.b27 - 640*m.b19*m.b23*m.b28 - 544*m.b19*m.b23*m.b29 - 448*
                       m.b19*m.b23*m.b30 - 352*m.b19*m.b23*m.b31 - 256*m.b19*m.b23*m.b32 - 160*m.b19*m.b23*m.b33 - 64*
                       m.b19*m.b23*m.b34 - 32*m.b19*m.b23*m.b35 - 832*m.b19*m.b24*m.b25 - 800*m.b19*m.b24*m.b26 - 704*
                       m.b19*m.b24*m.b27 - 608*m.b19*m.b24*m.b28 - 288*m.b19*m.b24*m.b29 - 416*m.b19*m.b24*m.b30 - 320*
                       m.b19*m.b24*m.b31 - 256*m.b19*m.b24*m.b32 - 192*m.b19*m.b24*m.b33 - 96*m.b19*m.b24*m.b34 - 32*
                       m.b19*m.b24*m.b35 - 768*m.b19*m.b25*m.b26 - 672*m.b19*m.b25*m.b27 - 576*m.b19*m.b25*m.b28 - 480*
                       m.b19*m.b25*m.b29 - 384*m.b19*m.b25*m.b30 - 160*m.b19*m.b25*m.b31 - 256*m.b19*m.b25*m.b32 - 192*
                       m.b19*m.b25*m.b33 - 128*m.b19*m.b25*m.b34 - 32*m.b19*m.b25*m.b35 - 640*m.b19*m.b26*m.b27 - 544*
                       m.b19*m.b26*m.b28 - 448*m.b19*m.b26*m.b29 - 384*m.b19*m.b26*m.b30 - 320*m.b19*m.b26*m.b31 - 256*
                       m.b19*m.b26*m.b32 - 96*m.b19*m.b26*m.b33 - 128*m.b19*m.b26*m.b34 - 64*m.b19*m.b26*m.b35 - 512*
                       m.b19*m.b27*m.b28 - 448*m.b19*m.b27*m.b29 - 384*m.b19*m.b27*m.b30 - 320*m.b19*m.b27*m.b31 - 256*
                       m.b19*m.b27*m.b32 - 192*m.b19*m.b27*m.b33 - 128*m.b19*m.b27*m.b34 - 32*m.b19*m.b27*m.b35 - 448*
                       m.b19*m.b28*m.b29 - 384*m.b19*m.b28*m.b30 - 320*m.b19*m.b28*m.b31 - 256*m.b19*m.b28*m.b32 - 192*
                       m.b19*m.b28*m.b33 - 128*m.b19*m.b28*m.b34 - 64*m.b19*m.b28*m.b35 - 384*m.b19*m.b29*m.b30 - 320*
                       m.b19*m.b29*m.b31 - 256*m.b19*m.b29*m.b32 - 192*m.b19*m.b29*m.b33 - 128*m.b19*m.b29*m.b34 - 64*
                       m.b19*m.b29*m.b35 - 320*m.b19*m.b30*m.b31 - 256*m.b19*m.b30*m.b32 - 192*m.b19*m.b30*m.b33 - 128*
                       m.b19*m.b30*m.b34 - 64*m.b19*m.b30*m.b35 - 256*m.b19*m.b31*m.b32 - 192*m.b19*m.b31*m.b33 - 128*
                       m.b19*m.b31*m.b34 - 64*m.b19*m.b31*m.b35 - 192*m.b19*m.b32*m.b33 - 128*m.b19*m.b32*m.b34 - 64*
                       m.b19*m.b32*m.b35 - 128*m.b19*m.b33*m.b34 - 64*m.b19*m.b33*m.b35 - 64*m.b19*m.b34*m.b35 - 640*
                       m.b20*m.b21*m.b22 - 960*m.b20*m.b21*m.b23 - 960*m.b20*m.b21*m.b24 - 992*m.b20*m.b21*m.b25 - 928*
                       m.b20*m.b21*m.b26 - 832*m.b20*m.b21*m.b27 - 736*m.b20*m.b21*m.b28 - 640*m.b20*m.b21*m.b29 - 544*
                       m.b20*m.b21*m.b30 - 448*m.b20*m.b21*m.b31 - 320*m.b20*m.b21*m.b32 - 192*m.b20*m.b21*m.b33 - 96*
                       m.b20*m.b21*m.b34 - 32*m.b20*m.b21*m.b35 - 960*m.b20*m.b22*m.b23 - 640*m.b20*m.b22*m.b24 - 960*
                       m.b20*m.b22*m.b25 - 896*m.b20*m.b22*m.b26 - 800*m.b20*m.b22*m.b27 - 704*m.b20*m.b22*m.b28 - 608*
                       m.b20*m.b22*m.b29 - 512*m.b20*m.b22*m.b30 - 416*m.b20*m.b22*m.b31 - 320*m.b20*m.b22*m.b32 - 192*
                       m.b20*m.b22*m.b33 - 64*m.b20*m.b22*m.b34 - 32*m.b20*m.b22*m.b35 - 928*m.b20*m.b23*m.b24 - 896*
                       m.b20*m.b23*m.b25 - 544*m.b20*m.b23*m.b26 - 768*m.b20*m.b23*m.b27 - 672*m.b20*m.b23*m.b28 - 576*
                       m.b20*m.b23*m.b29 - 480*m.b20*m.b23*m.b30 - 384*m.b20*m.b23*m.b31 - 288*m.b20*m.b23*m.b32 - 192*
                       m.b20*m.b23*m.b33 - 96*m.b20*m.b23*m.b34 - 32*m.b20*m.b23*m.b35 - 864*m.b20*m.b24*m.b25 - 832*
                       m.b20*m.b24*m.b26 - 736*m.b20*m.b24*m.b27 - 384*m.b20*m.b24*m.b28 - 544*m.b20*m.b24*m.b29 - 448*
                       m.b20*m.b24*m.b30 - 352*m.b20*m.b24*m.b31 - 256*m.b20*m.b24*m.b32 - 192*m.b20*m.b24*m.b33 - 128*
                       m.b20*m.b24*m.b34 - 32*m.b20*m.b24*m.b35 - 800*m.b20*m.b25*m.b26 - 704*m.b20*m.b25*m.b27 - 608*
                       m.b20*m.b25*m.b28 - 512*m.b20*m.b25*m.b29 - 224*m.b20*m.b25*m.b30 - 320*m.b20*m.b25*m.b31 - 256*
                       m.b20*m.b25*m.b32 - 192*m.b20*m.b25*m.b33 - 128*m.b20*m.b25*m.b34 - 64*m.b20*m.b25*m.b35 - 672*
                       m.b20*m.b26*m.b27 - 576*m.b20*m.b26*m.b28 - 480*m.b20*m.b26*m.b29 - 384*m.b20*m.b26*m.b30 - 320*
                       m.b20*m.b26*m.b31 - 128*m.b20*m.b26*m.b32 - 192*m.b20*m.b26*m.b33 - 128*m.b20*m.b26*m.b34 - 64*
                       m.b20*m.b26*m.b35 - 544*m.b20*m.b27*m.b28 - 448*m.b20*m.b27*m.b29 - 384*m.b20*m.b27*m.b30 - 320*
                       m.b20*m.b27*m.b31 - 256*m.b20*m.b27*m.b32 - 192*m.b20*m.b27*m.b33 - 64*m.b20*m.b27*m.b34 - 64*
                       m.b20*m.b27*m.b35 - 448*m.b20*m.b28*m.b29 - 384*m.b20*m.b28*m.b30 - 320*m.b20*m.b28*m.b31 - 256*
                       m.b20*m.b28*m.b32 - 192*m.b20*m.b28*m.b33 - 128*m.b20*m.b28*m.b34 - 64*m.b20*m.b28*m.b35 - 384*
                       m.b20*m.b29*m.b30 - 320*m.b20*m.b29*m.b31 - 256*m.b20*m.b29*m.b32 - 192*m.b20*m.b29*m.b33 - 128*
                       m.b20*m.b29*m.b34 - 64*m.b20*m.b29*m.b35 - 320*m.b20*m.b30*m.b31 - 256*m.b20*m.b30*m.b32 - 192*
                       m.b20*m.b30*m.b33 - 128*m.b20*m.b30*m.b34 - 64*m.b20*m.b30*m.b35 - 256*m.b20*m.b31*m.b32 - 192*
                       m.b20*m.b31*m.b33 - 128*m.b20*m.b31*m.b34 - 64*m.b20*m.b31*m.b35 - 192*m.b20*m.b32*m.b33 - 128*
                       m.b20*m.b32*m.b34 - 64*m.b20*m.b32*m.b35 - 128*m.b20*m.b33*m.b34 - 64*m.b20*m.b33*m.b35 - 64*
                       m.b20*m.b34*m.b35 - 640*m.b21*m.b22*m.b23 - 960*m.b21*m.b22*m.b24 - 960*m.b21*m.b22*m.b25 - 928*
                       m.b21*m.b22*m.b26 - 832*m.b21*m.b22*m.b27 - 736*m.b21*m.b22*m.b28 - 640*m.b21*m.b22*m.b29 - 544*
                       m.b21*m.b22*m.b30 - 448*m.b21*m.b22*m.b31 - 352*m.b21*m.b22*m.b32 - 256*m.b21*m.b22*m.b33 - 128*
                       m.b21*m.b22*m.b34 - 32*m.b21*m.b22*m.b35 - 960*m.b21*m.b23*m.b24 - 608*m.b21*m.b23*m.b25 - 896*
                       m.b21*m.b23*m.b26 - 800*m.b21*m.b23*m.b27 - 704*m.b21*m.b23*m.b28 - 608*m.b21*m.b23*m.b29 - 512*
                       m.b21*m.b23*m.b30 - 416*m.b21*m.b23*m.b31 - 320*m.b21*m.b23*m.b32 - 224*m.b21*m.b23*m.b33 - 128*
                       m.b21*m.b23*m.b34 - 32*m.b21*m.b23*m.b35 - 896*m.b21*m.b24*m.b25 - 864*m.b21*m.b24*m.b26 - 480*
                       m.b21*m.b24*m.b27 - 672*m.b21*m.b24*m.b28 - 576*m.b21*m.b24*m.b29 - 480*m.b21*m.b24*m.b30 - 384*
                       m.b21*m.b24*m.b31 - 288*m.b21*m.b24*m.b32 - 192*m.b21*m.b24*m.b33 - 128*m.b21*m.b24*m.b34 - 64*
                       m.b21*m.b24*m.b35 - 832*m.b21*m.b25*m.b26 - 736*m.b21*m.b25*m.b27 - 640*m.b21*m.b25*m.b28 - 320*
                       m.b21*m.b25*m.b29 - 448*m.b21*m.b25*m.b30 - 352*m.b21*m.b25*m.b31 - 256*m.b21*m.b25*m.b32 - 192*
                       m.b21*m.b25*m.b33 - 128*m.b21*m.b25*m.b34 - 64*m.b21*m.b25*m.b35 - 704*m.b21*m.b26*m.b27 - 608*
                       m.b21*m.b26*m.b28 - 512*m.b21*m.b26*m.b29 - 416*m.b21*m.b26*m.b30 - 160*m.b21*m.b26*m.b31 - 256*
                       m.b21*m.b26*m.b32 - 192*m.b21*m.b26*m.b33 - 128*m.b21*m.b26*m.b34 - 64*m.b21*m.b26*m.b35 - 576*
                       m.b21*m.b27*m.b28 - 480*m.b21*m.b27*m.b29 - 384*m.b21*m.b27*m.b30 - 320*m.b21*m.b27*m.b31 - 256*
                       m.b21*m.b27*m.b32 - 96*m.b21*m.b27*m.b33 - 128*m.b21*m.b27*m.b34 - 64*m.b21*m.b27*m.b35 - 448*
                       m.b21*m.b28*m.b29 - 384*m.b21*m.b28*m.b30 - 320*m.b21*m.b28*m.b31 - 256*m.b21*m.b28*m.b32 - 192*
                       m.b21*m.b28*m.b33 - 128*m.b21*m.b28*m.b34 - 32*m.b21*m.b28*m.b35 - 384*m.b21*m.b29*m.b30 - 320*
                       m.b21*m.b29*m.b31 - 256*m.b21*m.b29*m.b32 - 192*m.b21*m.b29*m.b33 - 128*m.b21*m.b29*m.b34 - 64*
                       m.b21*m.b29*m.b35 - 320*m.b21*m.b30*m.b31 - 256*m.b21*m.b30*m.b32 - 192*m.b21*m.b30*m.b33 - 128*
                       m.b21*m.b30*m.b34 - 64*m.b21*m.b30*m.b35 - 256*m.b21*m.b31*m.b32 - 192*m.b21*m.b31*m.b33 - 128*
                       m.b21*m.b31*m.b34 - 64*m.b21*m.b31*m.b35 - 192*m.b21*m.b32*m.b33 - 128*m.b21*m.b32*m.b34 - 64*
                       m.b21*m.b32*m.b35 - 128*m.b21*m.b33*m.b34 - 64*m.b21*m.b33*m.b35 - 64*m.b21*m.b34*m.b35 - 640*
                       m.b22*m.b23*m.b24 - 960*m.b22*m.b23*m.b25 - 928*m.b22*m.b23*m.b26 - 832*m.b22*m.b23*m.b27 - 736*
                       m.b22*m.b23*m.b28 - 640*m.b22*m.b23*m.b29 - 544*m.b22*m.b23*m.b30 - 448*m.b22*m.b23*m.b31 - 352*
                       m.b22*m.b23*m.b32 - 256*m.b22*m.b23*m.b33 - 160*m.b22*m.b23*m.b34 - 64*m.b22*m.b23*m.b35 - 928*
                       m.b22*m.b24*m.b25 - 576*m.b22*m.b24*m.b26 - 800*m.b22*m.b24*m.b27 - 704*m.b22*m.b24*m.b28 - 608*
                       m.b22*m.b24*m.b29 - 512*m.b22*m.b24*m.b30 - 416*m.b22*m.b24*m.b31 - 320*m.b22*m.b24*m.b32 - 224*
                       m.b22*m.b24*m.b33 - 128*m.b22*m.b24*m.b34 - 64*m.b22*m.b24*m.b35 - 864*m.b22*m.b25*m.b26 - 768*
                       m.b22*m.b25*m.b27 - 416*m.b22*m.b25*m.b28 - 576*m.b22*m.b25*m.b29 - 480*m.b22*m.b25*m.b30 - 384*
                       m.b22*m.b25*m.b31 - 288*m.b22*m.b25*m.b32 - 192*m.b22*m.b25*m.b33 - 128*m.b22*m.b25*m.b34 - 64*
                       m.b22*m.b25*m.b35 - 736*m.b22*m.b26*m.b27 - 640*m.b22*m.b26*m.b28 - 544*m.b22*m.b26*m.b29 - 256*
                       m.b22*m.b26*m.b30 - 352*m.b22*m.b26*m.b31 - 256*m.b22*m.b26*m.b32 - 192*m.b22*m.b26*m.b33 - 128*
                       m.b22*m.b26*m.b34 - 64*m.b22*m.b26*m.b35 - 608*m.b22*m.b27*m.b28 - 512*m.b22*m.b27*m.b29 - 416*
                       m.b22*m.b27*m.b30 - 320*m.b22*m.b27*m.b31 - 128*m.b22*m.b27*m.b32 - 192*m.b22*m.b27*m.b33 - 128*
                       m.b22*m.b27*m.b34 - 64*m.b22*m.b27*m.b35 - 480*m.b22*m.b28*m.b29 - 384*m.b22*m.b28*m.b30 - 320*
                       m.b22*m.b28*m.b31 - 256*m.b22*m.b28*m.b32 - 192*m.b22*m.b28*m.b33 - 64*m.b22*m.b28*m.b34 - 64*
                       m.b22*m.b28*m.b35 - 384*m.b22*m.b29*m.b30 - 320*m.b22*m.b29*m.b31 - 256*m.b22*m.b29*m.b32 - 192*
                       m.b22*m.b29*m.b33 - 128*m.b22*m.b29*m.b34 - 64*m.b22*m.b29*m.b35 - 320*m.b22*m.b30*m.b31 - 256*
                       m.b22*m.b30*m.b32 - 192*m.b22*m.b30*m.b33 - 128*m.b22*m.b30*m.b34 - 64*m.b22*m.b30*m.b35 - 256*
                       m.b22*m.b31*m.b32 - 192*m.b22*m.b31*m.b33 - 128*m.b22*m.b31*m.b34 - 64*m.b22*m.b31*m.b35 - 192*
                       m.b22*m.b32*m.b33 - 128*m.b22*m.b32*m.b34 - 64*m.b22*m.b32*m.b35 - 128*m.b22*m.b33*m.b34 - 64*
                       m.b22*m.b33*m.b35 - 64*m.b22*m.b34*m.b35 - 640*m.b23*m.b24*m.b25 - 928*m.b23*m.b24*m.b26 - 832*
                       m.b23*m.b24*m.b27 - 736*m.b23*m.b24*m.b28 - 640*m.b23*m.b24*m.b29 - 544*m.b23*m.b24*m.b30 - 448*
                       m.b23*m.b24*m.b31 - 352*m.b23*m.b24*m.b32 - 256*m.b23*m.b24*m.b33 - 160*m.b23*m.b24*m.b34 - 64*
                       m.b23*m.b24*m.b35 - 896*m.b23*m.b25*m.b26 - 512*m.b23*m.b25*m.b27 - 704*m.b23*m.b25*m.b28 - 608*
                       m.b23*m.b25*m.b29 - 512*m.b23*m.b25*m.b30 - 416*m.b23*m.b25*m.b31 - 320*m.b23*m.b25*m.b32 - 224*
                       m.b23*m.b25*m.b33 - 128*m.b23*m.b25*m.b34 - 64*m.b23*m.b25*m.b35 - 768*m.b23*m.b26*m.b27 - 672*
                       m.b23*m.b26*m.b28 - 352*m.b23*m.b26*m.b29 - 480*m.b23*m.b26*m.b30 - 384*m.b23*m.b26*m.b31 - 288*
                       m.b23*m.b26*m.b32 - 192*m.b23*m.b26*m.b33 - 128*m.b23*m.b26*m.b34 - 64*m.b23*m.b26*m.b35 - 640*
                       m.b23*m.b27*m.b28 - 544*m.b23*m.b27*m.b29 - 448*m.b23*m.b27*m.b30 - 192*m.b23*m.b27*m.b31 - 256*
                       m.b23*m.b27*m.b32 - 192*m.b23*m.b27*m.b33 - 128*m.b23*m.b27*m.b34 - 64*m.b23*m.b27*m.b35 - 512*
                       m.b23*m.b28*m.b29 - 416*m.b23*m.b28*m.b30 - 320*m.b23*m.b28*m.b31 - 256*m.b23*m.b28*m.b32 - 96*
                       m.b23*m.b28*m.b33 - 128*m.b23*m.b28*m.b34 - 64*m.b23*m.b28*m.b35 - 384*m.b23*m.b29*m.b30 - 320*
                       m.b23*m.b29*m.b31 - 256*m.b23*m.b29*m.b32 - 192*m.b23*m.b29*m.b33 - 128*m.b23*m.b29*m.b34 - 32*
                       m.b23*m.b29*m.b35 - 320*m.b23*m.b30*m.b31 - 256*m.b23*m.b30*m.b32 - 192*m.b23*m.b30*m.b33 - 128*
                       m.b23*m.b30*m.b34 - 64*m.b23*m.b30*m.b35 - 256*m.b23*m.b31*m.b32 - 192*m.b23*m.b31*m.b33 - 128*
                       m.b23*m.b31*m.b34 - 64*m.b23*m.b31*m.b35 - 192*m.b23*m.b32*m.b33 - 128*m.b23*m.b32*m.b34 - 64*
                       m.b23*m.b32*m.b35 - 128*m.b23*m.b33*m.b34 - 64*m.b23*m.b33*m.b35 - 64*m.b23*m.b34*m.b35 - 608*
                       m.b24*m.b25*m.b26 - 832*m.b24*m.b25*m.b27 - 736*m.b24*m.b25*m.b28 - 640*m.b24*m.b25*m.b29 - 544*
                       m.b24*m.b25*m.b30 - 448*m.b24*m.b25*m.b31 - 352*m.b24*m.b25*m.b32 - 256*m.b24*m.b25*m.b33 - 160*
                       m.b24*m.b25*m.b34 - 64*m.b24*m.b25*m.b35 - 800*m.b24*m.b26*m.b27 - 448*m.b24*m.b26*m.b28 - 608*
                       m.b24*m.b26*m.b29 - 512*m.b24*m.b26*m.b30 - 416*m.b24*m.b26*m.b31 - 320*m.b24*m.b26*m.b32 - 224*
                       m.b24*m.b26*m.b33 - 128*m.b24*m.b26*m.b34 - 64*m.b24*m.b26*m.b35 - 672*m.b24*m.b27*m.b28 - 576*
                       m.b24*m.b27*m.b29 - 288*m.b24*m.b27*m.b30 - 384*m.b24*m.b27*m.b31 - 288*m.b24*m.b27*m.b32 - 192*
                       m.b24*m.b27*m.b33 - 128*m.b24*m.b27*m.b34 - 64*m.b24*m.b27*m.b35 - 544*m.b24*m.b28*m.b29 - 448*
                       m.b24*m.b28*m.b30 - 352*m.b24*m.b28*m.b31 - 128*m.b24*m.b28*m.b32 - 192*m.b24*m.b28*m.b33 - 128*
                       m.b24*m.b28*m.b34 - 64*m.b24*m.b28*m.b35 - 416*m.b24*m.b29*m.b30 - 320*m.b24*m.b29*m.b31 - 256*
                       m.b24*m.b29*m.b32 - 192*m.b24*m.b29*m.b33 - 64*m.b24*m.b29*m.b34 - 64*m.b24*m.b29*m.b35 - 320*
                       m.b24*m.b30*m.b31 - 256*m.b24*m.b30*m.b32 - 192*m.b24*m.b30*m.b33 - 128*m.b24*m.b30*m.b34 - 64*
                       m.b24*m.b30*m.b35 - 256*m.b24*m.b31*m.b32 - 192*m.b24*m.b31*m.b33 - 128*m.b24*m.b31*m.b34 - 64*
                       m.b24*m.b31*m.b35 - 192*m.b24*m.b32*m.b33 - 128*m.b24*m.b32*m.b34 - 64*m.b24*m.b32*m.b35 - 128*
                       m.b24*m.b33*m.b34 - 64*m.b24*m.b33*m.b35 - 64*m.b24*m.b34*m.b35 - 544*m.b25*m.b26*m.b27 - 736*
                       m.b25*m.b26*m.b28 - 640*m.b25*m.b26*m.b29 - 544*m.b25*m.b26*m.b30 - 448*m.b25*m.b26*m.b31 - 352*
                       m.b25*m.b26*m.b32 - 256*m.b25*m.b26*m.b33 - 160*m.b25*m.b26*m.b34 - 64*m.b25*m.b26*m.b35 - 704*
                       m.b25*m.b27*m.b28 - 384*m.b25*m.b27*m.b29 - 512*m.b25*m.b27*m.b30 - 416*m.b25*m.b27*m.b31 - 320*
                       m.b25*m.b27*m.b32 - 224*m.b25*m.b27*m.b33 - 128*m.b25*m.b27*m.b34 - 64*m.b25*m.b27*m.b35 - 576*
                       m.b25*m.b28*m.b29 - 480*m.b25*m.b28*m.b30 - 224*m.b25*m.b28*m.b31 - 288*m.b25*m.b28*m.b32 - 192*
                       m.b25*m.b28*m.b33 - 128*m.b25*m.b28*m.b34 - 64*m.b25*m.b28*m.b35 - 448*m.b25*m.b29*m.b30 - 352*
                       m.b25*m.b29*m.b31 - 256*m.b25*m.b29*m.b32 - 96*m.b25*m.b29*m.b33 - 128*m.b25*m.b29*m.b34 - 64*
                       m.b25*m.b29*m.b35 - 320*m.b25*m.b30*m.b31 - 256*m.b25*m.b30*m.b32 - 192*m.b25*m.b30*m.b33 - 128*
                       m.b25*m.b30*m.b34 - 32*m.b25*m.b30*m.b35 - 256*m.b25*m.b31*m.b32 - 192*m.b25*m.b31*m.b33 - 128*
                       m.b25*m.b31*m.b34 - 64*m.b25*m.b31*m.b35 - 192*m.b25*m.b32*m.b33 - 128*m.b25*m.b32*m.b34 - 64*
                       m.b25*m.b32*m.b35 - 128*m.b25*m.b33*m.b34 - 64*m.b25*m.b33*m.b35 - 64*m.b25*m.b34*m.b35 - 480*
                       m.b26*m.b27*m.b28 - 640*m.b26*m.b27*m.b29 - 544*m.b26*m.b27*m.b30 - 448*m.b26*m.b27*m.b31 - 352*
                       m.b26*m.b27*m.b32 - 256*m.b26*m.b27*m.b33 - 160*m.b26*m.b27*m.b34 - 64*m.b26*m.b27*m.b35 - 608*
                       m.b26*m.b28*m.b29 - 320*m.b26*m.b28*m.b30 - 416*m.b26*m.b28*m.b31 - 320*m.b26*m.b28*m.b32 - 224*
                       m.b26*m.b28*m.b33 - 128*m.b26*m.b28*m.b34 - 64*m.b26*m.b28*m.b35 - 480*m.b26*m.b29*m.b30 - 384*
                       m.b26*m.b29*m.b31 - 160*m.b26*m.b29*m.b32 - 192*m.b26*m.b29*m.b33 - 128*m.b26*m.b29*m.b34 - 64*
                       m.b26*m.b29*m.b35 - 352*m.b26*m.b30*m.b31 - 256*m.b26*m.b30*m.b32 - 192*m.b26*m.b30*m.b33 - 64*
                       m.b26*m.b30*m.b34 - 64*m.b26*m.b30*m.b35 - 256*m.b26*m.b31*m.b32 - 192*m.b26*m.b31*m.b33 - 128*
                       m.b26*m.b31*m.b34 - 64*m.b26*m.b31*m.b35 - 192*m.b26*m.b32*m.b33 - 128*m.b26*m.b32*m.b34 - 64*
                       m.b26*m.b32*m.b35 - 128*m.b26*m.b33*m.b34 - 64*m.b26*m.b33*m.b35 - 64*m.b26*m.b34*m.b35 - 416*
                       m.b27*m.b28*m.b29 - 544*m.b27*m.b28*m.b30 - 448*m.b27*m.b28*m.b31 - 352*m.b27*m.b28*m.b32 - 256*
                       m.b27*m.b28*m.b33 - 160*m.b27*m.b28*m.b34 - 64*m.b27*m.b28*m.b35 - 512*m.b27*m.b29*m.b30 - 256*
                       m.b27*m.b29*m.b31 - 320*m.b27*m.b29*m.b32 - 224*m.b27*m.b29*m.b33 - 128*m.b27*m.b29*m.b34 - 64*
                       m.b27*m.b29*m.b35 - 384*m.b27*m.b30*m.b31 - 288*m.b27*m.b30*m.b32 - 96*m.b27*m.b30*m.b33 - 128*
                       m.b27*m.b30*m.b34 - 64*m.b27*m.b30*m.b35 - 256*m.b27*m.b31*m.b32 - 192*m.b27*m.b31*m.b33 - 128*
                       m.b27*m.b31*m.b34 - 32*m.b27*m.b31*m.b35 - 192*m.b27*m.b32*m.b33 - 128*m.b27*m.b32*m.b34 - 64*
                       m.b27*m.b32*m.b35 - 128*m.b27*m.b33*m.b34 - 64*m.b27*m.b33*m.b35 - 64*m.b27*m.b34*m.b35 - 352*
                       m.b28*m.b29*m.b30 - 448*m.b28*m.b29*m.b31 - 352*m.b28*m.b29*m.b32 - 256*m.b28*m.b29*m.b33 - 160*
                       m.b28*m.b29*m.b34 - 64*m.b28*m.b29*m.b35 - 416*m.b28*m.b30*m.b31 - 192*m.b28*m.b30*m.b32 - 224*
                       m.b28*m.b30*m.b33 - 128*m.b28*m.b30*m.b34 - 64*m.b28*m.b30*m.b35 - 288*m.b28*m.b31*m.b32 - 192*
                       m.b28*m.b31*m.b33 - 64*m.b28*m.b31*m.b34 - 64*m.b28*m.b31*m.b35 - 192*m.b28*m.b32*m.b33 - 128*
                       m.b28*m.b32*m.b34 - 64*m.b28*m.b32*m.b35 - 128*m.b28*m.b33*m.b34 - 64*m.b28*m.b33*m.b35 - 64*
                       m.b28*m.b34*m.b35 - 288*m.b29*m.b30*m.b31 - 352*m.b29*m.b30*m.b32 - 256*m.b29*m.b30*m.b33 - 160*
                       m.b29*m.b30*m.b34 - 64*m.b29*m.b30*m.b35 - 320*m.b29*m.b31*m.b32 - 128*m.b29*m.b31*m.b33 - 128*
                       m.b29*m.b31*m.b34 - 64*m.b29*m.b31*m.b35 - 192*m.b29*m.b32*m.b33 - 128*m.b29*m.b32*m.b34 - 32*
                       m.b29*m.b32*m.b35 - 128*m.b29*m.b33*m.b34 - 64*m.b29*m.b33*m.b35 - 64*m.b29*m.b34*m.b35 - 224*
                       m.b30*m.b31*m.b32 - 256*m.b30*m.b31*m.b33 - 160*m.b30*m.b31*m.b34 - 64*m.b30*m.b31*m.b35 - 224*
                       m.b30*m.b32*m.b33 - 64*m.b30*m.b32*m.b34 - 64*m.b30*m.b32*m.b35 - 128*m.b30*m.b33*m.b34 - 64*
                       m.b30*m.b33*m.b35 - 64*m.b30*m.b34*m.b35 - 160*m.b31*m.b32*m.b33 - 160*m.b31*m.b32*m.b34 - 64*
                       m.b31*m.b32*m.b35 - 128*m.b31*m.b33*m.b34 - 32*m.b31*m.b33*m.b35 - 64*m.b31*m.b34*m.b35 - 96*
                       m.b32*m.b33*m.b34 - 64*m.b32*m.b33*m.b35 - 64*m.b32*m.b34*m.b35 - 32*m.b33*m.b34*m.b35 + 368*m.b1
                       *m.b2 + 360*m.b1*m.b3 + 352*m.b1*m.b4 + 344*m.b1*m.b5 + 336*m.b1*m.b6 + 328*m.b1*m.b7 + 320*m.b1*
                       m.b8 + 312*m.b1*m.b9 + 304*m.b1*m.b10 + 296*m.b1*m.b11 + 288*m.b1*m.b12 + 280*m.b1*m.b13 + 288*
                       m.b1*m.b14 + 280*m.b1*m.b15 + 272*m.b1*m.b16 + 264*m.b1*m.b17 + 256*m.b1*m.b18 + 248*m.b1*m.b19
                        + 240*m.b1*m.b20 + 232*m.b1*m.b21 + 224*m.b1*m.b22 + 216*m.b1*m.b23 + 208*m.b1*m.b24 + 200*m.b1*
                       m.b25 + 192*m.b1*m.b26 + 736*m.b2*m.b3 + 736*m.b2*m.b4 + 720*m.b2*m.b5 + 704*m.b2*m.b6 + 688*m.b2
                       *m.b7 + 672*m.b2*m.b8 + 656*m.b2*m.b9 + 640*m.b2*m.b10 + 624*m.b2*m.b11 + 608*m.b2*m.b12 + 592*
                       m.b2*m.b13 + 576*m.b2*m.b14 + 592*m.b2*m.b15 + 576*m.b2*m.b16 + 560*m.b2*m.b17 + 544*m.b2*m.b18
                        + 528*m.b2*m.b19 + 512*m.b2*m.b20 + 496*m.b2*m.b21 + 480*m.b2*m.b22 + 464*m.b2*m.b23 + 448*m.b2*
                       m.b24 + 432*m.b2*m.b25 + 400*m.b2*m.b26 + 192*m.b2*m.b27 + 1120*m.b3*m.b4 + 1112*m.b3*m.b5 + 1104
                       *m.b3*m.b6 + 1080*m.b3*m.b7 + 1056*m.b3*m.b8 + 1032*m.b3*m.b9 + 1008*m.b3*m.b10 + 984*m.b3*m.b11
                        + 960*m.b3*m.b12 + 936*m.b3*m.b13 + 912*m.b3*m.b14 + 904*m.b3*m.b15 + 912*m.b3*m.b16 + 888*m.b3*
                       m.b17 + 864*m.b3*m.b18 + 840*m.b3*m.b19 + 816*m.b3*m.b20 + 792*m.b3*m.b21 + 768*m.b3*m.b22 + 744*
                       m.b3*m.b23 + 720*m.b3*m.b24 + 680*m.b3*m.b25 + 640*m.b3*m.b26 + 400*m.b3*m.b27 + 192*m.b3*m.b28
                        + 1520*m.b4*m.b5 + 1504*m.b4*m.b6 + 1488*m.b4*m.b7 + 1472*m.b4*m.b8 + 1440*m.b4*m.b9 + 1408*m.b4
                       *m.b10 + 1376*m.b4*m.b11 + 1344*m.b4*m.b12 + 1312*m.b4*m.b13 + 1280*m.b4*m.b14 + 1248*m.b4*m.b15
                        + 1248*m.b4*m.b16 + 1248*m.b4*m.b17 + 1216*m.b4*m.b18 + 1184*m.b4*m.b19 + 1152*m.b4*m.b20 + 1120
                       *m.b4*m.b21 + 1088*m.b4*m.b22 + 1056*m.b4*m.b23 + 1008*m.b4*m.b24 + 960*m.b4*m.b25 + 896*m.b4*
                       m.b26 + 640*m.b4*m.b27 + 400*m.b4*m.b28 + 192*m.b4*m.b29 + 1936*m.b5*m.b6 + 1912*m.b5*m.b7 + 1888
                       *m.b5*m.b8 + 1864*m.b5*m.b9 + 1840*m.b5*m.b10 + 1800*m.b5*m.b11 + 1760*m.b5*m.b12 + 1720*m.b5*
                       m.b13 + 1680*m.b5*m.b14 + 1640*m.b5*m.b15 + 1616*m.b5*m.b16 + 1608*m.b5*m.b17 + 1600*m.b5*m.b18
                        + 1560*m.b5*m.b19 + 1520*m.b5*m.b20 + 1480*m.b5*m.b21 + 1440*m.b5*m.b22 + 1384*m.b5*m.b23 + 1328
                       *m.b5*m.b24 + 1256*m.b5*m.b25 + 1184*m.b5*m.b26 + 896*m.b5*m.b27 + 640*m.b5*m.b28 + 400*m.b5*
                       m.b29 + 192*m.b5*m.b30 + 2368*m.b6*m.b7 + 2336*m.b6*m.b8 + 2304*m.b6*m.b9 + 2272*m.b6*m.b10 + 
                       2240*m.b6*m.b11 + 2208*m.b6*m.b12 + 2160*m.b6*m.b13 + 2112*m.b6*m.b14 + 2064*m.b6*m.b15 + 2016*
                       m.b6*m.b16 + 2000*m.b6*m.b17 + 1984*m.b6*m.b18 + 1968*m.b6*m.b19 + 1920*m.b6*m.b20 + 1872*m.b6*
                       m.b21 + 1808*m.b6*m.b22 + 1744*m.b6*m.b23 + 1664*m.b6*m.b24 + 1584*m.b6*m.b25 + 1488*m.b6*m.b26
                        + 1184*m.b6*m.b27 + 896*m.b6*m.b28 + 640*m.b6*m.b29 + 400*m.b6*m.b30 + 192*m.b6*m.b31 + 2816*
                       m.b7*m.b8 + 2776*m.b7*m.b9 + 2736*m.b7*m.b10 + 2696*m.b7*m.b11 + 2656*m.b7*m.b12 + 2616*m.b7*
                       m.b13 + 2576*m.b7*m.b14 + 2520*m.b7*m.b15 + 2464*m.b7*m.b16 + 2424*m.b7*m.b17 + 2400*m.b7*m.b18
                        + 2376*m.b7*m.b19 + 2352*m.b7*m.b20 + 2280*m.b7*m.b21 + 2208*m.b7*m.b22 + 2120*m.b7*m.b23 + 2032
                       *m.b7*m.b24 + 1928*m.b7*m.b25 + 1824*m.b7*m.b26 + 1488*m.b7*m.b27 + 1184*m.b7*m.b28 + 896*m.b7*
                       m.b29 + 640*m.b7*m.b30 + 400*m.b7*m.b31 + 192*m.b7*m.b32 + 3280*m.b8*m.b9 + 3232*m.b8*m.b10 + 
                       3184*m.b8*m.b11 + 3136*m.b8*m.b12 + 3088*m.b8*m.b13 + 3040*m.b8*m.b14 + 2992*m.b8*m.b15 + 2944*
                       m.b8*m.b16 + 2880*m.b8*m.b17 + 2848*m.b8*m.b18 + 2816*m.b8*m.b19 + 2768*m.b8*m.b20 + 2720*m.b8*
                       m.b21 + 2624*m.b8*m.b22 + 2528*m.b8*m.b23 + 2416*m.b8*m.b24 + 2304*m.b8*m.b25 + 2176*m.b8*m.b26
                        + 1824*m.b8*m.b27 + 1488*m.b8*m.b28 + 1184*m.b8*m.b29 + 896*m.b8*m.b30 + 640*m.b8*m.b31 + 400*
                       m.b8*m.b32 + 192*m.b8*m.b33 + 3760*m.b9*m.b10 + 3704*m.b9*m.b11 + 3648*m.b9*m.b12 + 3592*m.b9*
                       m.b13 + 3536*m.b9*m.b14 + 3480*m.b9*m.b15 + 3424*m.b9*m.b16 + 3368*m.b9*m.b17 + 3328*m.b9*m.b18
                        + 3272*m.b9*m.b19 + 3216*m.b9*m.b20 + 3144*m.b9*m.b21 + 3072*m.b9*m.b22 + 2952*m.b9*m.b23 + 2832
                       *m.b9*m.b24 + 2696*m.b9*m.b25 + 2560*m.b9*m.b26 + 2176*m.b9*m.b27 + 1824*m.b9*m.b28 + 1488*m.b9*
                       m.b29 + 1184*m.b9*m.b30 + 896*m.b9*m.b31 + 640*m.b9*m.b32 + 400*m.b9*m.b33 + 192*m.b9*m.b34 + 
                       4256*m.b10*m.b11 + 4192*m.b10*m.b12 + 4128*m.b10*m.b13 + 4064*m.b10*m.b14 + 4000*m.b10*m.b15 + 
                       3936*m.b10*m.b16 + 3872*m.b10*m.b17 + 3792*m.b10*m.b18 + 3744*m.b10*m.b19 + 3680*m.b10*m.b20 + 
                       3600*m.b10*m.b21 + 3504*m.b10*m.b22 + 3408*m.b10*m.b23 + 3264*m.b10*m.b24 + 3120*m.b10*m.b25 + 
                       2960*m.b10*m.b26 + 2560*m.b10*m.b27 + 2176*m.b10*m.b28 + 1824*m.b10*m.b29 + 1488*m.b10*m.b30 + 
                       1184*m.b10*m.b31 + 896*m.b10*m.b32 + 640*m.b10*m.b33 + 400*m.b10*m.b34 + 192*m.b10*m.b35 + 4512*
                       m.b11*m.b12 + 4448*m.b11*m.b13 + 4384*m.b11*m.b14 + 4304*m.b11*m.b15 + 4240*m.b11*m.b16 + 4160*
                       m.b11*m.b17 + 4080*m.b11*m.b18 + 4048*m.b11*m.b19 + 3984*m.b11*m.b20 + 3888*m.b11*m.b21 + 3808*
                       m.b11*m.b22 + 3680*m.b11*m.b23 + 3552*m.b11*m.b24 + 3376*m.b11*m.b25 + 3120*m.b11*m.b26 + 2696*
                       m.b11*m.b27 + 2304*m.b11*m.b28 + 1928*m.b11*m.b29 + 1584*m.b11*m.b30 + 1256*m.b11*m.b31 + 960*
                       m.b11*m.b32 + 680*m.b11*m.b33 + 432*m.b11*m.b34 + 200*m.b11*m.b35 + 4736*m.b12*m.b13 + 4656*m.b12
                       *m.b14 + 4592*m.b12*m.b15 + 4480*m.b12*m.b16 + 4400*m.b12*m.b17 + 4320*m.b12*m.b18 + 4272*m.b12*
                       m.b19 + 4256*m.b12*m.b20 + 4176*m.b12*m.b21 + 4048*m.b12*m.b22 + 3952*m.b12*m.b23 + 3808*m.b12*
                       m.b24 + 3552*m.b12*m.b25 + 3264*m.b12*m.b26 + 2832*m.b12*m.b27 + 2416*m.b12*m.b28 + 2032*m.b12*
                       m.b29 + 1664*m.b12*m.b30 + 1328*m.b12*m.b31 + 1008*m.b12*m.b32 + 720*m.b12*m.b33 + 448*m.b12*
                       m.b34 + 208*m.b12*m.b35 + 4912*m.b13*m.b14 + 4816*m.b13*m.b15 + 4720*m.b13*m.b16 + 4592*m.b13*
                       m.b17 + 4496*m.b13*m.b18 + 4464*m.b13*m.b19 + 4416*m.b13*m.b20 + 4416*m.b13*m.b21 + 4320*m.b13*
                       m.b22 + 4160*m.b13*m.b23 + 3952*m.b13*m.b24 + 3680*m.b13*m.b25 + 3408*m.b13*m.b26 + 2952*m.b13*
                       m.b27 + 2528*m.b13*m.b28 + 2120*m.b13*m.b29 + 1744*m.b13*m.b30 + 1384*m.b13*m.b31 + 1056*m.b13*
                       m.b32 + 744*m.b13*m.b33 + 464*m.b13*m.b34 + 216*m.b13*m.b35 + 5008*m.b14*m.b15 + 4912*m.b14*m.b16
                        + 4800*m.b14*m.b17 + 4640*m.b14*m.b18 + 4576*m.b14*m.b19 + 4560*m.b14*m.b20 + 4512*m.b14*m.b21
                        + 4528*m.b14*m.b22 + 4320*m.b14*m.b23 + 4048*m.b14*m.b24 + 3808*m.b14*m.b25 + 3504*m.b14*m.b26
                        + 3072*m.b14*m.b27 + 2624*m.b14*m.b28 + 2208*m.b14*m.b29 + 1808*m.b14*m.b30 + 1440*m.b14*m.b31
                        + 1088*m.b14*m.b32 + 768*m.b14*m.b33 + 480*m.b14*m.b34 + 224*m.b14*m.b35 + 5056*m.b15*m.b16 + 
                       4960*m.b15*m.b17 + 4832*m.b15*m.b18 + 4688*m.b15*m.b19 + 4624*m.b15*m.b20 + 4624*m.b15*m.b21 + 
                       4512*m.b15*m.b22 + 4416*m.b15*m.b23 + 4176*m.b15*m.b24 + 3888*m.b15*m.b25 + 3600*m.b15*m.b26 + 
                       3144*m.b15*m.b27 + 2720*m.b15*m.b28 + 2280*m.b15*m.b29 + 1872*m.b15*m.b30 + 1480*m.b15*m.b31 + 
                       1120*m.b15*m.b32 + 792*m.b15*m.b33 + 496*m.b15*m.b34 + 232*m.b15*m.b35 + 5104*m.b16*m.b17 + 5008*
                       m.b16*m.b18 + 4880*m.b16*m.b19 + 4752*m.b16*m.b20 + 4624*m.b16*m.b21 + 4560*m.b16*m.b22 + 4416*
                       m.b16*m.b23 + 4256*m.b16*m.b24 + 3984*m.b16*m.b25 + 3680*m.b16*m.b26 + 3216*m.b16*m.b27 + 2768*
                       m.b16*m.b28 + 2352*m.b16*m.b29 + 1920*m.b16*m.b30 + 1520*m.b16*m.b31 + 1152*m.b16*m.b32 + 816*
                       m.b16*m.b33 + 512*m.b16*m.b34 + 240*m.b16*m.b35 + 5152*m.b17*m.b18 + 5072*m.b17*m.b19 + 4880*
                       m.b17*m.b20 + 4688*m.b17*m.b21 + 4576*m.b17*m.b22 + 4464*m.b17*m.b23 + 4272*m.b17*m.b24 + 4048*
                       m.b17*m.b25 + 3744*m.b17*m.b26 + 3272*m.b17*m.b27 + 2816*m.b17*m.b28 + 2376*m.b17*m.b29 + 1968*
                       m.b17*m.b30 + 1560*m.b17*m.b31 + 1184*m.b17*m.b32 + 840*m.b17*m.b33 + 528*m.b17*m.b34 + 248*m.b17
                       *m.b35 + 5152*m.b18*m.b19 + 5008*m.b18*m.b20 + 4832*m.b18*m.b21 + 4640*m.b18*m.b22 + 4496*m.b18*
                       m.b23 + 4320*m.b18*m.b24 + 4080*m.b18*m.b25 + 3792*m.b18*m.b26 + 3328*m.b18*m.b27 + 2848*m.b18*
                       m.b28 + 2400*m.b18*m.b29 + 1984*m.b18*m.b30 + 1600*m.b18*m.b31 + 1216*m.b18*m.b32 + 864*m.b18*
                       m.b33 + 544*m.b18*m.b34 + 256*m.b18*m.b35 + 5104*m.b19*m.b20 + 4960*m.b19*m.b21 + 4800*m.b19*
                       m.b22 + 4592*m.b19*m.b23 + 4400*m.b19*m.b24 + 4160*m.b19*m.b25 + 3872*m.b19*m.b26 + 3368*m.b19*
                       m.b27 + 2880*m.b19*m.b28 + 2424*m.b19*m.b29 + 2000*m.b19*m.b30 + 1608*m.b19*m.b31 + 1248*m.b19*
                       m.b32 + 888*m.b19*m.b33 + 560*m.b19*m.b34 + 264*m.b19*m.b35 + 5056*m.b20*m.b21 + 4912*m.b20*m.b22
                        + 4720*m.b20*m.b23 + 4480*m.b20*m.b24 + 4240*m.b20*m.b25 + 3936*m.b20*m.b26 + 3424*m.b20*m.b27
                        + 2944*m.b20*m.b28 + 2464*m.b20*m.b29 + 2016*m.b20*m.b30 + 1616*m.b20*m.b31 + 1248*m.b20*m.b32
                        + 912*m.b20*m.b33 + 576*m.b20*m.b34 + 272*m.b20*m.b35 + 5008*m.b21*m.b22 + 4816*m.b21*m.b23 + 
                       4592*m.b21*m.b24 + 4304*m.b21*m.b25 + 4000*m.b21*m.b26 + 3480*m.b21*m.b27 + 2992*m.b21*m.b28 + 
                       2520*m.b21*m.b29 + 2064*m.b21*m.b30 + 1640*m.b21*m.b31 + 1248*m.b21*m.b32 + 904*m.b21*m.b33 + 592
                       *m.b21*m.b34 + 280*m.b21*m.b35 + 4912*m.b22*m.b23 + 4656*m.b22*m.b24 + 4384*m.b22*m.b25 + 4064*
                       m.b22*m.b26 + 3536*m.b22*m.b27 + 3040*m.b22*m.b28 + 2576*m.b22*m.b29 + 2112*m.b22*m.b30 + 1680*
                       m.b22*m.b31 + 1280*m.b22*m.b32 + 912*m.b22*m.b33 + 576*m.b22*m.b34 + 288*m.b22*m.b35 + 4736*m.b23
                       *m.b24 + 4448*m.b23*m.b25 + 4128*m.b23*m.b26 + 3592*m.b23*m.b27 + 3088*m.b23*m.b28 + 2616*m.b23*
                       m.b29 + 2160*m.b23*m.b30 + 1720*m.b23*m.b31 + 1312*m.b23*m.b32 + 936*m.b23*m.b33 + 592*m.b23*
                       m.b34 + 280*m.b23*m.b35 + 4512*m.b24*m.b25 + 4192*m.b24*m.b26 + 3648*m.b24*m.b27 + 3136*m.b24*
                       m.b28 + 2656*m.b24*m.b29 + 2208*m.b24*m.b30 + 1760*m.b24*m.b31 + 1344*m.b24*m.b32 + 960*m.b24*
                       m.b33 + 608*m.b24*m.b34 + 288*m.b24*m.b35 + 4256*m.b25*m.b26 + 3704*m.b25*m.b27 + 3184*m.b25*
                       m.b28 + 2696*m.b25*m.b29 + 2240*m.b25*m.b30 + 1800*m.b25*m.b31 + 1376*m.b25*m.b32 + 984*m.b25*
                       m.b33 + 624*m.b25*m.b34 + 296*m.b25*m.b35 + 3760*m.b26*m.b27 + 3232*m.b26*m.b28 + 2736*m.b26*
                       m.b29 + 2272*m.b26*m.b30 + 1840*m.b26*m.b31 + 1408*m.b26*m.b32 + 1008*m.b26*m.b33 + 640*m.b26*
                       m.b34 + 304*m.b26*m.b35 + 3280*m.b27*m.b28 + 2776*m.b27*m.b29 + 2304*m.b27*m.b30 + 1864*m.b27*
                       m.b31 + 1440*m.b27*m.b32 + 1032*m.b27*m.b33 + 656*m.b27*m.b34 + 312*m.b27*m.b35 + 2816*m.b28*
                       m.b29 + 2336*m.b28*m.b30 + 1888*m.b28*m.b31 + 1472*m.b28*m.b32 + 1056*m.b28*m.b33 + 672*m.b28*
                       m.b34 + 320*m.b28*m.b35 + 2368*m.b29*m.b30 + 1912*m.b29*m.b31 + 1488*m.b29*m.b32 + 1080*m.b29*
                       m.b33 + 688*m.b29*m.b34 + 328*m.b29*m.b35 + 1936*m.b30*m.b31 + 1504*m.b30*m.b32 + 1104*m.b30*
                       m.b33 + 704*m.b30*m.b34 + 336*m.b30*m.b35 + 1520*m.b31*m.b32 + 1112*m.b31*m.b33 + 720*m.b31*m.b34
                        + 344*m.b31*m.b35 + 1120*m.b32*m.b33 + 736*m.b32*m.b34 + 352*m.b32*m.b35 + 736*m.b33*m.b34 + 360
                       *m.b33*m.b35 + 368*m.b34*m.b35 - 1200*m.b1 - 2488*m.b2 - 3856*m.b3 - 5296*m.b4 - 6800*m.b5 - 8360
                       *m.b6 - 9968*m.b7 - 11616*m.b8 - 13296*m.b9 - 15000*m.b10 - 15784*m.b11 - 16400*m.b12 - 16848*
                       m.b13 - 17144*m.b14 - 17312*m.b15 - 17416*m.b16 - 17456*m.b17 - 17440*m.b18 - 17456*m.b19 - 17416
                       *m.b20 - 17312*m.b21 - 17144*m.b22 - 16848*m.b23 - 16400*m.b24 - 15784*m.b25 - 15000*m.b26 - 
                       13296*m.b27 - 11616*m.b28 - 9968*m.b29 - 8360*m.b30 - 6800*m.b31 - 5296*m.b32 - 3856*m.b33 - 2488
                       *m.b34 - 1200*m.b35 - m.x36 <= 0)
