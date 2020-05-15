#  MINLP written by GAMS Convert at 05/15/20 00:50:47
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         43        7        8       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         43       19       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        155      151        4        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,97),initialize=0)
m.x9 = Var(within=Reals,bounds=(3,13.3333333333333),initialize=3)
m.x10 = Var(within=Reals,bounds=(3,16.6666666666667),initialize=3)
m.x11 = Var(within=Reals,bounds=(3,20),initialize=3)
m.x12 = Var(within=Reals,bounds=(3,11.6666666666667),initialize=3)
m.x13 = Var(within=Reals,bounds=(3,13.3333333333333),initialize=3)
m.x14 = Var(within=Reals,bounds=(3,16.6666666666667),initialize=3)
m.x15 = Var(within=Reals,bounds=(3,20),initialize=3)
m.x16 = Var(within=Reals,bounds=(3,11.6666666666667),initialize=3)
m.x17 = Var(within=Reals,bounds=(0,100),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,100),initialize=0)
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
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   2*m.x17 + 2*m.x18, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x9 + m.x17 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x10 + m.x17 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x11 + m.x17 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x12 + m.x17 >= 0)

m.c6 = Constraint(expr= - m.x5 - m.x13 + m.x18 >= 0)

m.c7 = Constraint(expr= - m.x6 - m.x14 + m.x18 >= 0)

m.c8 = Constraint(expr= - m.x7 - m.x15 + m.x18 >= 0)

m.c9 = Constraint(expr= - m.x8 - m.x16 + m.x18 >= 0)

m.c10 = Constraint(expr=40/m.x13 - m.x9 <= 0)

m.c11 = Constraint(expr=50/m.x14 - m.x10 <= 0)

m.c12 = Constraint(expr=60/m.x15 - m.x11 <= 0)

m.c13 = Constraint(expr=35/m.x16 - m.x12 <= 0)

m.c14 = Constraint(expr=   m.x1 - m.x2 + m.x9 + 110.333333333333*m.b19 <= 110.333333333333)

m.c15 = Constraint(expr=   m.x1 - m.x3 + m.x9 + 110.333333333333*m.b20 <= 110.333333333333)

m.c16 = Constraint(expr=   m.x1 - m.x4 + m.x9 + 110.333333333333*m.b21 <= 110.333333333333)

m.c17 = Constraint(expr=   m.x2 - m.x3 + m.x10 + 113.666666666667*m.b22 <= 113.666666666667)

m.c18 = Constraint(expr=   m.x2 - m.x4 + m.x10 + 113.666666666667*m.b23 <= 113.666666666667)

m.c19 = Constraint(expr=   m.x3 - m.x4 + m.x11 + 117*m.b24 <= 117)

m.c20 = Constraint(expr= - m.x1 + m.x2 + m.x10 + 113.666666666667*m.b25 <= 113.666666666667)

m.c21 = Constraint(expr= - m.x1 + m.x3 + m.x11 + 117*m.b26 <= 117)

m.c22 = Constraint(expr= - m.x1 + m.x4 + m.x12 + 108.666666666667*m.b27 <= 108.666666666667)

m.c23 = Constraint(expr= - m.x2 + m.x3 + m.x11 + 117*m.b28 <= 117)

m.c24 = Constraint(expr= - m.x2 + m.x4 + m.x12 + 108.666666666667*m.b29 <= 108.666666666667)

m.c25 = Constraint(expr= - m.x3 + m.x4 + m.x12 + 108.666666666667*m.b30 <= 108.666666666667)

m.c26 = Constraint(expr=   m.x5 - m.x6 + m.x13 + 110.333333333333*m.b31 <= 110.333333333333)

m.c27 = Constraint(expr=   m.x5 - m.x7 + m.x13 + 110.333333333333*m.b32 <= 110.333333333333)

m.c28 = Constraint(expr=   m.x5 - m.x8 + m.x13 + 110.333333333333*m.b33 <= 110.333333333333)

m.c29 = Constraint(expr=   m.x6 - m.x7 + m.x14 + 113.666666666667*m.b34 <= 113.666666666667)

m.c30 = Constraint(expr=   m.x6 - m.x8 + m.x14 + 113.666666666667*m.b35 <= 113.666666666667)

m.c31 = Constraint(expr=   m.x7 - m.x8 + m.x15 + 117*m.b36 <= 117)

m.c32 = Constraint(expr= - m.x5 + m.x6 + m.x14 + 113.666666666667*m.b37 <= 113.666666666667)

m.c33 = Constraint(expr= - m.x5 + m.x7 + m.x15 + 117*m.b38 <= 117)

m.c34 = Constraint(expr= - m.x5 + m.x8 + m.x16 + 108.666666666667*m.b39 <= 108.666666666667)

m.c35 = Constraint(expr= - m.x6 + m.x7 + m.x15 + 117*m.b40 <= 117)

m.c36 = Constraint(expr= - m.x6 + m.x8 + m.x16 + 108.666666666667*m.b41 <= 108.666666666667)

m.c37 = Constraint(expr= - m.x7 + m.x8 + m.x16 + 108.666666666667*m.b42 <= 108.666666666667)

m.c38 = Constraint(expr=   m.b19 + m.b25 + m.b31 + m.b37 == 1)

m.c39 = Constraint(expr=   m.b20 + m.b26 + m.b32 + m.b38 == 1)

m.c40 = Constraint(expr=   m.b21 + m.b27 + m.b33 + m.b39 == 1)

m.c41 = Constraint(expr=   m.b22 + m.b28 + m.b34 + m.b40 == 1)

m.c42 = Constraint(expr=   m.b23 + m.b29 + m.b35 + m.b41 == 1)

m.c43 = Constraint(expr=   m.b24 + m.b30 + m.b36 + m.b42 == 1)
