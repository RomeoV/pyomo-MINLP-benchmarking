#  MINLP written by GAMS Convert at 05/15/20 00:50:51
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         44        1        0       43        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         27       21        6        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        157      151        6        0
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
m.x8 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(2,5.4772),initialize=2)
m.x15 = Var(within=Reals,bounds=(3,6.7081),initialize=3)
m.x16 = Var(within=Reals,bounds=(3.8,7.5498),initialize=3.8)
m.x17 = Var(within=Reals,bounds=(10,10),initialize=10)
m.x18 = Var(within=Reals,bounds=(1.8258,5),initialize=1.8258)
m.x19 = Var(within=Reals,bounds=(2.2361,5),initialize=2.2361)
m.x20 = Var(within=Reals,bounds=(2.5166,5),initialize=2.5166)
m.x21 = Var(within=Reals,bounds=(5,5),initialize=5)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   6*m.x10 + 6*m.x11 + 6*m.x12 + 6*m.x13, sense=minimize)

m.c2 = Constraint(expr=   m.x22 - m.x23 <= 0)

m.c3 = Constraint(expr=   0.5*m.x14 - m.x17 + m.x22 <= 0)

m.c4 = Constraint(expr=   0.5*m.x14 - m.x22 <= 0)

m.c5 = Constraint(expr=   0.5*m.x18 - m.x21 + m.x25 <= 0)

m.c6 = Constraint(expr=   0.5*m.x18 - m.x25 <= 0)

m.c7 = Constraint(expr=   0.5*m.x15 - m.x17 + m.x23 <= 0)

m.c8 = Constraint(expr=   0.5*m.x15 - m.x23 <= 0)

m.c9 = Constraint(expr=   0.5*m.x19 - m.x21 + m.x26 <= 0)

m.c10 = Constraint(expr=   0.5*m.x19 - m.x26 <= 0)

m.c11 = Constraint(expr=   0.5*m.x16 - m.x17 + m.x24 <= 0)

m.c12 = Constraint(expr=   0.5*m.x16 - m.x24 <= 0)

m.c13 = Constraint(expr=   0.5*m.x20 - m.x21 + m.x27 <= 0)

m.c14 = Constraint(expr=   0.5*m.x20 - m.x27 <= 0)

m.c15 = Constraint(expr= - m.x8 + m.x22 - m.x23 <= 0)

m.c16 = Constraint(expr= - m.x8 - m.x22 + m.x23 <= 0)

m.c17 = Constraint(expr= - m.x9 + m.x25 - m.x26 <= 0)

m.c18 = Constraint(expr= - m.x9 - m.x25 + m.x26 <= 0)

m.c19 = Constraint(expr= - 10*m.b1 - 10*m.b2 + 0.5*m.x14 + 0.5*m.x15 - m.x22 + m.x23 <= 0)

m.c20 = Constraint(expr= - 10*m.b1 + 10*m.b2 + 0.5*m.x14 + 0.5*m.x15 + m.x22 - m.x23 <= 10)

m.c21 = Constraint(expr=   5*m.b1 - 5*m.b2 + 0.5*m.x18 + 0.5*m.x19 - m.x25 + m.x26 <= 5)

m.c22 = Constraint(expr=   5*m.b1 + 5*m.b2 + 0.5*m.x18 + 0.5*m.x19 + m.x25 - m.x26 <= 10)

m.c23 = Constraint(expr= - m.x10 + m.x22 - m.x24 <= 0)

m.c24 = Constraint(expr= - m.x10 - m.x22 + m.x24 <= 0)

m.c25 = Constraint(expr= - m.x11 + m.x25 - m.x27 <= 0)

m.c26 = Constraint(expr= - m.x11 - m.x25 + m.x27 <= 0)

m.c27 = Constraint(expr= - 10*m.b3 - 10*m.b4 + 0.5*m.x14 + 0.5*m.x16 - m.x22 + m.x24 <= 0)

m.c28 = Constraint(expr= - 10*m.b3 + 10*m.b4 + 0.5*m.x14 + 0.5*m.x16 + m.x22 - m.x24 <= 10)

m.c29 = Constraint(expr=   5*m.b3 - 5*m.b4 + 0.5*m.x18 + 0.5*m.x20 - m.x25 + m.x27 <= 5)

m.c30 = Constraint(expr=   5*m.b3 + 5*m.b4 + 0.5*m.x18 + 0.5*m.x20 + m.x25 - m.x27 <= 10)

m.c31 = Constraint(expr= - m.x12 + m.x23 - m.x24 <= 0)

m.c32 = Constraint(expr= - m.x12 - m.x23 + m.x24 <= 0)

m.c33 = Constraint(expr= - m.x13 + m.x26 - m.x27 <= 0)

m.c34 = Constraint(expr= - m.x13 - m.x26 + m.x27 <= 0)

m.c35 = Constraint(expr= - 10*m.b5 - 10*m.b6 + 0.5*m.x15 + 0.5*m.x16 - m.x23 + m.x24 <= 0)

m.c36 = Constraint(expr= - 10*m.b5 + 10*m.b6 + 0.5*m.x15 + 0.5*m.x16 + m.x23 - m.x24 <= 10)

m.c37 = Constraint(expr=   5*m.b5 - 5*m.b6 + 0.5*m.x19 + 0.5*m.x20 - m.x26 + m.x27 <= 5)

m.c38 = Constraint(expr=   5*m.b5 + 5*m.b6 + 0.5*m.x19 + 0.5*m.x20 + m.x26 - m.x27 <= 10)

m.c39 = Constraint(expr=10/m.x14 - m.x18 <= 0)

m.c40 = Constraint(expr=10/m.x18 - m.x14 <= 0)

m.c41 = Constraint(expr=15/m.x15 - m.x19 <= 0)

m.c42 = Constraint(expr=15/m.x19 - m.x15 <= 0)

m.c43 = Constraint(expr=19/m.x16 - m.x20 <= 0)

m.c44 = Constraint(expr=19/m.x20 - m.x16 <= 0)
