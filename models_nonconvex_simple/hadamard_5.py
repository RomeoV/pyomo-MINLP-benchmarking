#  MINLP written by GAMS Convert at 08/13/20 17:37:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        1        0        0        0        0        0
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

m.obj = Objective(expr=m.x26, sense=maximize)

m.c1 = Constraint(expr=m.b1*m.b7*m.b13*m.b19*m.b25 - m.b1*m.b7*m.b13*m.b20*m.b24 + m.b1*m.b7*m.b15*m.b18*m.b24 - m.b1*
                       m.b10*m.b12*m.b18*m.b24 + m.b5*m.b6*m.b12*m.b18*m.b24 - m.b5*m.b6*m.b12*m.b19*m.b23 + m.b1*m.b10*
                       m.b12*m.b19*m.b23 - m.b1*m.b7*m.b15*m.b19*m.b23 + m.b1*m.b7*m.b14*m.b20*m.b23 - m.b1*m.b7*m.b14*
                       m.b18*m.b25 + m.b1*m.b9*m.b12*m.b18*m.b25 - m.b1*m.b9*m.b12*m.b20*m.b23 + m.b1*m.b9*m.b15*m.b17*
                       m.b23 - m.b1*m.b10*m.b14*m.b17*m.b23 + m.b5*m.b6*m.b14*m.b17*m.b23 - m.b5*m.b9*m.b11*m.b17*m.b23
                        + m.b4*m.b10*m.b11*m.b17*m.b23 - m.b4*m.b6*m.b15*m.b17*m.b23 + m.b4*m.b6*m.b12*m.b20*m.b23 - 
                       m.b4*m.b6*m.b12*m.b18*m.b25 + m.b4*m.b6*m.b13*m.b17*m.b25 - m.b4*m.b6*m.b13*m.b20*m.b22 + m.b4*
                       m.b6*m.b15*m.b18*m.b22 - m.b4*m.b10*m.b11*m.b18*m.b22 + m.b5*m.b9*m.b11*m.b18*m.b22 - m.b5*m.b6*
                       m.b14*m.b18*m.b22 + m.b1*m.b10*m.b14*m.b18*m.b22 - m.b1*m.b9*m.b15*m.b18*m.b22 + m.b1*m.b9*m.b13*
                       m.b20*m.b22 - m.b1*m.b9*m.b13*m.b17*m.b25 + m.b1*m.b8*m.b14*m.b17*m.b25 - m.b1*m.b8*m.b14*m.b20*
                       m.b22 + m.b1*m.b8*m.b15*m.b19*m.b22 - m.b1*m.b10*m.b13*m.b19*m.b22 + m.b5*m.b6*m.b13*m.b19*m.b22
                        - m.b5*m.b6*m.b13*m.b17*m.b24 + m.b1*m.b10*m.b13*m.b17*m.b24 - m.b1*m.b8*m.b15*m.b17*m.b24 + 
                       m.b1*m.b8*m.b12*m.b20*m.b24 - m.b1*m.b8*m.b12*m.b19*m.b25 + m.b3*m.b6*m.b12*m.b19*m.b25 - m.b3*
                       m.b6*m.b12*m.b20*m.b24 + m.b3*m.b6*m.b15*m.b17*m.b24 - m.b3*m.b10*m.b11*m.b17*m.b24 + m.b5*m.b8*
                       m.b11*m.b17*m.b24 - m.b5*m.b8*m.b11*m.b19*m.b22 + m.b3*m.b10*m.b11*m.b19*m.b22 - m.b3*m.b6*m.b15*
                       m.b19*m.b22 + m.b3*m.b6*m.b14*m.b20*m.b22 - m.b3*m.b6*m.b14*m.b17*m.b25 + m.b3*m.b9*m.b11*m.b17*
                       m.b25 - m.b3*m.b9*m.b11*m.b20*m.b22 + m.b3*m.b9*m.b15*m.b16*m.b22 - m.b3*m.b10*m.b14*m.b16*m.b22
                        + m.b5*m.b8*m.b14*m.b16*m.b22 - m.b5*m.b9*m.b13*m.b16*m.b22 + m.b4*m.b10*m.b13*m.b16*m.b22 - 
                       m.b4*m.b8*m.b15*m.b16*m.b22 + m.b4*m.b8*m.b11*m.b20*m.b22 - m.b4*m.b8*m.b11*m.b17*m.b25 + m.b4*
                       m.b8*m.b12*m.b16*m.b25 - m.b4*m.b8*m.b12*m.b20*m.b21 + m.b4*m.b8*m.b15*m.b17*m.b21 - m.b4*m.b10*
                       m.b13*m.b17*m.b21 + m.b5*m.b9*m.b13*m.b17*m.b21 - m.b5*m.b8*m.b14*m.b17*m.b21 + m.b3*m.b10*m.b14*
                       m.b17*m.b21 - m.b3*m.b9*m.b15*m.b17*m.b21 + m.b3*m.b9*m.b12*m.b20*m.b21 - m.b3*m.b9*m.b12*m.b16*
                       m.b25 + m.b3*m.b7*m.b14*m.b16*m.b25 - m.b3*m.b7*m.b14*m.b20*m.b21 + m.b3*m.b7*m.b15*m.b19*m.b21
                        - m.b3*m.b10*m.b12*m.b19*m.b21 + m.b5*m.b8*m.b12*m.b19*m.b21 - m.b5*m.b8*m.b12*m.b16*m.b24 + 
                       m.b3*m.b10*m.b12*m.b16*m.b24 - m.b3*m.b7*m.b15*m.b16*m.b24 + m.b3*m.b7*m.b11*m.b20*m.b24 - m.b3*
                       m.b7*m.b11*m.b19*m.b25 + m.b2*m.b8*m.b11*m.b19*m.b25 - m.b2*m.b8*m.b11*m.b20*m.b24 + m.b2*m.b8*
                       m.b15*m.b16*m.b24 - m.b2*m.b10*m.b13*m.b16*m.b24 + m.b5*m.b7*m.b13*m.b16*m.b24 - m.b5*m.b7*m.b13*
                       m.b19*m.b21 + m.b2*m.b10*m.b13*m.b19*m.b21 - m.b2*m.b8*m.b15*m.b19*m.b21 + m.b2*m.b8*m.b14*m.b20*
                       m.b21 - m.b2*m.b8*m.b14*m.b16*m.b25 + m.b2*m.b9*m.b13*m.b16*m.b25 - m.b2*m.b9*m.b13*m.b20*m.b21
                        + m.b2*m.b9*m.b15*m.b18*m.b21 - m.b2*m.b10*m.b14*m.b18*m.b21 + m.b5*m.b7*m.b14*m.b18*m.b21 - 
                       m.b5*m.b9*m.b12*m.b18*m.b21 + m.b4*m.b10*m.b12*m.b18*m.b21 - m.b4*m.b7*m.b15*m.b18*m.b21 + m.b4*
                       m.b7*m.b13*m.b20*m.b21 - m.b4*m.b7*m.b13*m.b16*m.b25 + m.b4*m.b7*m.b11*m.b18*m.b25 - m.b4*m.b7*
                       m.b11*m.b20*m.b23 + m.b4*m.b7*m.b15*m.b16*m.b23 - m.b4*m.b10*m.b12*m.b16*m.b23 + m.b5*m.b9*m.b12*
                       m.b16*m.b23 - m.b5*m.b7*m.b14*m.b16*m.b23 + m.b2*m.b10*m.b14*m.b16*m.b23 - m.b2*m.b9*m.b15*m.b16*
                       m.b23 + m.b2*m.b9*m.b11*m.b20*m.b23 - m.b2*m.b9*m.b11*m.b18*m.b25 + m.b2*m.b6*m.b14*m.b18*m.b25
                        - m.b2*m.b6*m.b14*m.b20*m.b23 + m.b2*m.b6*m.b15*m.b19*m.b23 - m.b2*m.b10*m.b11*m.b19*m.b23 + 
                       m.b5*m.b7*m.b11*m.b19*m.b23 - m.b5*m.b7*m.b11*m.b18*m.b24 + m.b2*m.b10*m.b11*m.b18*m.b24 - m.b2*
                       m.b6*m.b15*m.b18*m.b24 + m.b2*m.b6*m.b13*m.b20*m.b24 - m.b2*m.b6*m.b13*m.b19*m.b25 - m.x26 >= 0)
