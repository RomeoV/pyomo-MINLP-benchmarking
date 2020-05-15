#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         52       10        4       38        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         47       43        4        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        139      137        2        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x5 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x6 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x7 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x8 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x9 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   2*m.x9 + 2*m.x10, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x5 + m.x9 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x6 + m.x9 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x7 + m.x10 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x8 + m.x10 >= 0)

m.c6 = Constraint(expr=40/m.x7 - m.x5 <= 0)

m.c7 = Constraint(expr=50/m.x8 - m.x6 <= 0)

m.c8 = Constraint(expr=   m.x1 - m.x11 - m.x12 - m.x13 - m.x14 == 0)

m.c9 = Constraint(expr=   m.x2 - m.x15 - m.x16 - m.x17 - m.x18 == 0)

m.c10 = Constraint(expr=   m.x3 - m.x19 - m.x20 - m.x21 - m.x22 == 0)

m.c11 = Constraint(expr=   m.x4 - m.x23 - m.x24 - m.x25 - m.x26 == 0)

m.c12 = Constraint(expr=   m.x5 - m.x27 - m.x28 - m.x29 - m.x30 == 0)

m.c13 = Constraint(expr=   m.x6 - m.x31 - m.x32 - m.x33 - m.x34 == 0)

m.c14 = Constraint(expr=   m.x7 - m.x35 - m.x36 - m.x37 - m.x38 == 0)

m.c15 = Constraint(expr=   m.x8 - m.x39 - m.x40 - m.x41 - m.x42 == 0)

m.c16 = Constraint(expr=   m.x11 - 29*m.b43 <= 0)

m.c17 = Constraint(expr=   m.x12 - 29*m.b44 <= 0)

m.c18 = Constraint(expr=   m.x13 - 29*m.b45 <= 0)

m.c19 = Constraint(expr=   m.x14 - 29*m.b46 <= 0)

m.c20 = Constraint(expr=   m.x15 - 29*m.b43 <= 0)

m.c21 = Constraint(expr=   m.x16 - 29*m.b44 <= 0)

m.c22 = Constraint(expr=   m.x17 - 29*m.b45 <= 0)

m.c23 = Constraint(expr=   m.x18 - 29*m.b46 <= 0)

m.c24 = Constraint(expr=   m.x19 - 29*m.b43 <= 0)

m.c25 = Constraint(expr=   m.x20 - 29*m.b44 <= 0)

m.c26 = Constraint(expr=   m.x21 - 29*m.b45 <= 0)

m.c27 = Constraint(expr=   m.x22 - 29*m.b46 <= 0)

m.c28 = Constraint(expr=   m.x23 - 29*m.b43 <= 0)

m.c29 = Constraint(expr=   m.x24 - 29*m.b44 <= 0)

m.c30 = Constraint(expr=   m.x25 - 29*m.b45 <= 0)

m.c31 = Constraint(expr=   m.x26 - 29*m.b46 <= 0)

m.c32 = Constraint(expr=   m.x27 - 40*m.b43 <= 0)

m.c33 = Constraint(expr=   m.x28 - 40*m.b44 <= 0)

m.c34 = Constraint(expr=   m.x29 - 40*m.b45 <= 0)

m.c35 = Constraint(expr=   m.x30 - 40*m.b46 <= 0)

m.c36 = Constraint(expr=   m.x31 - 40*m.b43 <= 0)

m.c37 = Constraint(expr=   m.x32 - 40*m.b44 <= 0)

m.c38 = Constraint(expr=   m.x33 - 40*m.b45 <= 0)

m.c39 = Constraint(expr=   m.x34 - 40*m.b46 <= 0)

m.c40 = Constraint(expr=   m.x35 - 40*m.b43 <= 0)

m.c41 = Constraint(expr=   m.x36 - 40*m.b44 <= 0)

m.c42 = Constraint(expr=   m.x37 - 40*m.b45 <= 0)

m.c43 = Constraint(expr=   m.x38 - 40*m.b46 <= 0)

m.c44 = Constraint(expr=   m.x39 - 40*m.b43 <= 0)

m.c45 = Constraint(expr=   m.x40 - 40*m.b44 <= 0)

m.c46 = Constraint(expr=   m.x41 - 40*m.b45 <= 0)

m.c47 = Constraint(expr=   m.x42 - 40*m.b46 <= 0)

m.c48 = Constraint(expr=   m.x11 - m.x15 + m.x27 <= 0)

m.c49 = Constraint(expr= - m.x12 + m.x16 + m.x32 <= 0)

m.c50 = Constraint(expr=   m.x21 - m.x25 + m.x37 <= 0)

m.c51 = Constraint(expr= - m.x22 + m.x26 + m.x42 <= 0)

m.c52 = Constraint(expr=   m.b43 + m.b44 + m.b45 + m.b46 == 1)
