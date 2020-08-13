#  MINLP written by GAMS Convert at 08/13/20 17:37:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         16        1       15        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         16        1       15        0


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
m.x16 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x16, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b3 - 2*m.b1 + 2*m.b3 + 2*m.b1*m.b7 - 2*m.b7 + 2*m.b2*m.b5 - 2*m.b2 - 2*m.b5 + 2*m.b2*
                       m.b10 - 4*m.b10 - 2*m.b3*m.b4 + 2*m.b4 - 2*m.b3*m.b12 - 2*m.b3*m.b14 - 2*m.b4*m.b5 + 2*m.b4*m.b9
                        - 2*m.b9 - 2*m.b4*m.b15 + 2*m.b5*m.b6 - 2*m.b6 + 2*m.b5*m.b8 - 2*m.b8 + 2*m.b6*m.b9 - 2*m.b7*
                       m.b8 + 2*m.b7*m.b12 + 2*m.b7*m.b13 + 2*m.b8*m.b10 + 2*m.b8*m.b15 + 2*m.b9*m.b11 - 2*m.b11 - 2*
                       m.b9*m.b12 + 2*m.b10*m.b11 + 2*m.b10*m.b12 - 2*m.b13*m.b15 + 2*m.b14*m.b15 + m.x16 <= 0)
