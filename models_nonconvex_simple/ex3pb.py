#  MINLP written by GAMS Convert at 08/13/20 17:37:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         32       18        2       12        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         33       25        8        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        100       95        5        0
# 
#  Reformulation has removed 1 variable and 1 equation


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
m.x9 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x10 = Var(within=Reals,bounds=(0,2),initialize=1.5)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0.75)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0.5)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0.5)
m.x16 = Var(within=Reals,bounds=(0,2),initialize=0.75)
m.x17 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=1.5)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=1.34)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=2)
m.x21 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,100),initialize=0.75)
m.x26 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,100),initialize=1.5)
m.x28 = Var(within=Reals,bounds=(0,2),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=1.7)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=1.5)
m.x32 = Var(within=Reals,bounds=(0,3),initialize=0.5)

m.obj = Objective(expr=   8*m.b1 + 6*m.b2 + 10*m.b3 + 6*m.b4 + 7*m.b5 + 4*m.b6 + 5*m.b7 + 5*m.b8 + m.x9 - 10*m.x10
                        + m.x11 - 15*m.x12 - 40*m.x16 + 15*m.x17 + 15*m.x21 + 80*m.x24 - 65*m.x25 + 25*m.x26 - 60*m.x27
                        + 35*m.x28 - 80*m.x29 - 35*m.x32 + 122, sense=minimize)

m.c1 = Constraint(expr=exp(m.x10) - m.x9 == 1)

m.c2 = Constraint(expr=exp(0.833333333333333*m.x12) - m.x11 == 1)

m.c3 = Constraint(expr= - m.x15 + 1.5*m.x16 + m.x17 == 0)

m.c4 = Constraint(expr=   1.25*m.x19 - m.x20 + 1.25*m.x21 == 0)

m.c5 = Constraint(expr=   m.x22 - 2*m.x23 == 0)

m.c6 = Constraint(expr=exp(0.666666666666667*m.x27) - m.x26 == 1)

m.c7 = Constraint(expr=exp(m.x29) - m.x28 == 1)

m.c8 = Constraint(expr=exp(m.x25) - m.x17 - m.x24 == 1)

m.c9 = Constraint(expr=   m.x20 - m.x26 - m.x28 == 0)

m.c10 = Constraint(expr= - m.x16 - m.x23 + m.x24 - m.x32 == 0)

m.c11 = Constraint(expr=   m.x18 - m.x19 - m.x22 == 0)

m.c12 = Constraint(expr=   m.x10 + m.x12 - m.x13 - m.x18 == 0)

m.c13 = Constraint(expr=   m.x13 - m.x14 - m.x15 == 0)

m.c14 = Constraint(expr= - m.x27 - m.x29 + m.x30 == 0)

m.c15 = Constraint(expr= - m.x21 + m.x30 - m.x31 == 0)

m.c16 = Constraint(expr=   m.x17 - 0.8*m.x24 <= 0)

m.c17 = Constraint(expr=   m.x17 - 0.4*m.x24 >= 0)

m.c18 = Constraint(expr=   m.x19 - 5*m.x21 <= 0)

m.c19 = Constraint(expr=   m.x19 - 2*m.x21 >= 0)

m.c20 = Constraint(expr= - 10*m.b8 + m.x9 <= 0)

m.c21 = Constraint(expr= - 10*m.b1 + m.x11 <= 0)

m.c22 = Constraint(expr= - 10*m.b2 + m.x16 <= 0)

m.c23 = Constraint(expr= - 10*m.b3 + m.x19 + m.x21 <= 0)

m.c24 = Constraint(expr= - 10*m.b4 + m.x22 <= 0)

m.c25 = Constraint(expr= - 10*m.b5 + m.x26 <= 0)

m.c26 = Constraint(expr= - 10*m.b6 + m.x28 <= 0)

m.c27 = Constraint(expr= - 10*m.b7 + m.x17 + m.x24 <= 0)

m.c28 = Constraint(expr=   m.b1 + m.b8 == 1)

m.c29 = Constraint(expr=   m.b3 + m.b4 <= 1)

m.c30 = Constraint(expr= - m.b3 + m.b5 + m.b6 == 0)

m.c31 = Constraint(expr=   m.b2 - m.b7 <= 0)
