#  MINLP written by GAMS Convert at 08/13/20 17:37:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         68        7       60        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         35       23       12        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        161       79       82        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,4),initialize=1)
m.x2 = Var(within=Reals,bounds=(1,4),initialize=1)
m.x3 = Var(within=Reals,bounds=(1,4),initialize=1)
m.x4 = Var(within=Reals,bounds=(1,4),initialize=1)
m.x5 = Var(within=Reals,bounds=(1,4),initialize=1)
m.x6 = Var(within=Reals,bounds=(1,4),initialize=1)
m.x7 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x8 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x9 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x10 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x11 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x12 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x13 = Var(within=Reals,bounds=(86.4583333333333,379.746835443038),initialize=86.4583333333333)
m.x14 = Var(within=Reals,bounds=(42.5,882.352941176471),initialize=42.5)
m.x15 = Var(within=Reals,bounds=(89.25,833.333333333333),initialize=89.25)
m.x16 = Var(within=Reals,bounds=(23.3333333333333,638.297872340426),initialize=23.3333333333333)
m.x17 = Var(within=Reals,bounds=(21,666.666666666667),initialize=21)
m.x18 = Var(within=Reals,bounds=(2.075,8.3),initialize=2.075)
m.x19 = Var(within=Reals,bounds=(1.7,6.8),initialize=1.7)
m.x20 = Var(within=Reals,bounds=(2.975,11.9),initialize=2.975)
m.x21 = Var(within=Reals,bounds=(0.875,3.5),initialize=0.875)
m.x22 = Var(within=Reals,bounds=(1.05,4.2),initialize=1.05)
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

m.obj = Objective(expr=250*m.x7**0.6*m.x1 + 250*m.x8**0.6*m.x2 + 250*m.x9**0.6*m.x3 + 250*m.x10**0.6*m.x4 + 250*m.x11**
                       0.6*m.x5 + 250*m.x12**0.6*m.x6, sense=minimize)

m.c2 = Constraint(expr=   m.x7 - 7.9*m.x13 >= 0)

m.c3 = Constraint(expr=   m.x8 - 2*m.x13 >= 0)

m.c4 = Constraint(expr=   m.x9 - 5.2*m.x13 >= 0)

m.c5 = Constraint(expr=   m.x10 - 4.9*m.x13 >= 0)

m.c6 = Constraint(expr=   m.x11 - 6.1*m.x13 >= 0)

m.c7 = Constraint(expr=   m.x12 - 4.2*m.x13 >= 0)

m.c8 = Constraint(expr=   m.x7 - 0.7*m.x14 >= 0)

m.c9 = Constraint(expr=   m.x8 - 0.8*m.x14 >= 0)

m.c10 = Constraint(expr=   m.x9 - 0.9*m.x14 >= 0)

m.c11 = Constraint(expr=   m.x10 - 3.4*m.x14 >= 0)

m.c12 = Constraint(expr=   m.x11 - 2.1*m.x14 >= 0)

m.c13 = Constraint(expr=   m.x12 - 2.5*m.x14 >= 0)

m.c14 = Constraint(expr=   m.x7 - 0.7*m.x15 >= 0)

m.c15 = Constraint(expr=   m.x8 - 2.6*m.x15 >= 0)

m.c16 = Constraint(expr=   m.x9 - 1.6*m.x15 >= 0)

m.c17 = Constraint(expr=   m.x10 - 3.6*m.x15 >= 0)

m.c18 = Constraint(expr=   m.x11 - 3.2*m.x15 >= 0)

m.c19 = Constraint(expr=   m.x12 - 2.9*m.x15 >= 0)

m.c20 = Constraint(expr=   m.x7 - 4.7*m.x16 >= 0)

m.c21 = Constraint(expr=   m.x8 - 2.3*m.x16 >= 0)

m.c22 = Constraint(expr=   m.x9 - 1.6*m.x16 >= 0)

m.c23 = Constraint(expr=   m.x10 - 2.7*m.x16 >= 0)

m.c24 = Constraint(expr=   m.x11 - 1.2*m.x16 >= 0)

m.c25 = Constraint(expr=   m.x12 - 2.5*m.x16 >= 0)

m.c26 = Constraint(expr=   m.x7 - 1.2*m.x17 >= 0)

m.c27 = Constraint(expr=   m.x8 - 3.6*m.x17 >= 0)

m.c28 = Constraint(expr=   m.x9 - 2.4*m.x17 >= 0)

m.c29 = Constraint(expr=   m.x10 - 4.5*m.x17 >= 0)

m.c30 = Constraint(expr=   m.x11 - 1.6*m.x17 >= 0)

m.c31 = Constraint(expr=   m.x12 - 2.1*m.x17 >= 0)

m.c32 = Constraint(expr=m.x1*m.x18 >= 6.4)

m.c33 = Constraint(expr=m.x2*m.x18 >= 4.7)

m.c34 = Constraint(expr=m.x3*m.x18 >= 8.3)

m.c35 = Constraint(expr=m.x4*m.x18 >= 3.9)

m.c36 = Constraint(expr=m.x5*m.x18 >= 2.1)

m.c37 = Constraint(expr=m.x6*m.x18 >= 1.2)

m.c38 = Constraint(expr=m.x1*m.x19 >= 6.8)

m.c39 = Constraint(expr=m.x2*m.x19 >= 6.4)

m.c40 = Constraint(expr=m.x3*m.x19 >= 6.5)

m.c41 = Constraint(expr=m.x4*m.x19 >= 4.4)

m.c42 = Constraint(expr=m.x5*m.x19 >= 2.3)

m.c43 = Constraint(expr=m.x6*m.x19 >= 3.2)

m.c44 = Constraint(expr=m.x1*m.x20 >= 1)

m.c45 = Constraint(expr=m.x2*m.x20 >= 6.3)

m.c46 = Constraint(expr=m.x3*m.x20 >= 5.4)

m.c47 = Constraint(expr=m.x4*m.x20 >= 11.9)

m.c48 = Constraint(expr=m.x5*m.x20 >= 5.7)

m.c49 = Constraint(expr=m.x6*m.x20 >= 6.2)

m.c50 = Constraint(expr=m.x1*m.x21 >= 3.2)

m.c51 = Constraint(expr=m.x2*m.x21 >= 3)

m.c52 = Constraint(expr=m.x3*m.x21 >= 3.5)

m.c53 = Constraint(expr=m.x4*m.x21 >= 3.3)

m.c54 = Constraint(expr=m.x5*m.x21 >= 2.8)

m.c55 = Constraint(expr=m.x6*m.x21 >= 3.4)

m.c56 = Constraint(expr=m.x1*m.x22 >= 2.1)

m.c57 = Constraint(expr=m.x2*m.x22 >= 2.5)

m.c58 = Constraint(expr=m.x3*m.x22 >= 4.2)

m.c59 = Constraint(expr=m.x4*m.x22 >= 3.6)

m.c60 = Constraint(expr=m.x5*m.x22 >= 3.7)

m.c61 = Constraint(expr=m.x6*m.x22 >= 2.2)

m.c62 = Constraint(expr=250000*m.x18/m.x13 + 150000*m.x19/m.x14 + 180000*m.x20/m.x15 + 160000*m.x21/m.x16 + 120000*m.x22
                        /m.x17 <= 6000)

m.c63 = Constraint(expr=   m.x1 - m.b23 - 2*m.b29 == 1)

m.c64 = Constraint(expr=   m.x2 - m.b24 - 2*m.b30 == 1)

m.c65 = Constraint(expr=   m.x3 - m.b25 - 2*m.b31 == 1)

m.c66 = Constraint(expr=   m.x4 - m.b26 - 2*m.b32 == 1)

m.c67 = Constraint(expr=   m.x5 - m.b27 - 2*m.b33 == 1)

m.c68 = Constraint(expr=   m.x6 - m.b28 - 2*m.b34 == 1)
