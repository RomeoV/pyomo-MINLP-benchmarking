#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         55        7       24       24        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         45       21       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        189      181        8        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x2 = Var(within=Reals,bounds=(3.5,26.5),initialize=3.5)
m.x3 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x4 = Var(within=Reals,bounds=(1,29),initialize=1)
m.x5 = Var(within=Reals,bounds=(3,27),initialize=3)
m.x6 = Var(within=Reals,bounds=(2.5,27.5),initialize=2.5)
m.x7 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
m.x8 = Var(within=Reals,bounds=(1.5,28.5),initialize=1.5)
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
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x5)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x6)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x7)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x8)**2) + 300*m.x33 + 240*m.x34
                        + 210*m.x35 + 100*m.x36 + 150*m.x37 + 120*m.x38 + 300*m.x39 + 240*m.x40 + 210*m.x41 + 100*m.x42
                        + 150*m.x43 + 120*m.x44, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x33 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x34 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x35 >= 0)

m.c5 = Constraint(expr= - m.x2 + m.x3 + m.x36 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x4 + m.x37 >= 0)

m.c7 = Constraint(expr= - m.x3 + m.x4 + m.x38 >= 0)

m.c8 = Constraint(expr=   m.x1 - m.x2 + m.x33 >= 0)

m.c9 = Constraint(expr=   m.x1 - m.x3 + m.x34 >= 0)

m.c10 = Constraint(expr=   m.x1 - m.x4 + m.x35 >= 0)

m.c11 = Constraint(expr=   m.x2 - m.x3 + m.x36 >= 0)

m.c12 = Constraint(expr=   m.x2 - m.x4 + m.x37 >= 0)

m.c13 = Constraint(expr=   m.x3 - m.x4 + m.x38 >= 0)

m.c14 = Constraint(expr= - m.x5 + m.x6 + m.x39 >= 0)

m.c15 = Constraint(expr= - m.x5 + m.x7 + m.x40 >= 0)

m.c16 = Constraint(expr= - m.x5 + m.x8 + m.x41 >= 0)

m.c17 = Constraint(expr= - m.x6 + m.x7 + m.x42 >= 0)

m.c18 = Constraint(expr= - m.x6 + m.x8 + m.x43 >= 0)

m.c19 = Constraint(expr= - m.x7 + m.x8 + m.x44 >= 0)

m.c20 = Constraint(expr=   m.x5 - m.x6 + m.x39 >= 0)

m.c21 = Constraint(expr=   m.x5 - m.x7 + m.x40 >= 0)

m.c22 = Constraint(expr=   m.x5 - m.x8 + m.x41 >= 0)

m.c23 = Constraint(expr=   m.x6 - m.x7 + m.x42 >= 0)

m.c24 = Constraint(expr=   m.x6 - m.x8 + m.x43 >= 0)

m.c25 = Constraint(expr=   m.x7 - m.x8 + m.x44 >= 0)

m.c26 = Constraint(expr=   m.x1 - m.x2 + 30*m.b9 <= 24)

m.c27 = Constraint(expr=   m.x1 - m.x3 + 30*m.b10 <= 26)

m.c28 = Constraint(expr=   m.x1 - m.x4 + 30*m.b11 <= 26.5)

m.c29 = Constraint(expr=   m.x2 - m.x3 + 30*m.b12 <= 25)

m.c30 = Constraint(expr=   m.x2 - m.x4 + 30*m.b13 <= 25.5)

m.c31 = Constraint(expr=   m.x3 - m.x4 + 30*m.b14 <= 27.5)

m.c32 = Constraint(expr= - m.x1 + m.x2 + 30*m.b15 <= 24)

m.c33 = Constraint(expr= - m.x1 + m.x3 + 30*m.b16 <= 26)

m.c34 = Constraint(expr= - m.x1 + m.x4 + 30*m.b17 <= 26.5)

m.c35 = Constraint(expr= - m.x2 + m.x3 + 30*m.b18 <= 25)

m.c36 = Constraint(expr= - m.x2 + m.x4 + 30*m.b19 <= 25.5)

m.c37 = Constraint(expr= - m.x3 + m.x4 + 30*m.b20 <= 27.5)

m.c38 = Constraint(expr=   m.x5 - m.x6 + 30*m.b21 <= 24.5)

m.c39 = Constraint(expr=   m.x5 - m.x7 + 30*m.b22 <= 25.5)

m.c40 = Constraint(expr=   m.x5 - m.x8 + 30*m.b23 <= 25.5)

m.c41 = Constraint(expr=   m.x6 - m.x7 + 30*m.b24 <= 26)

m.c42 = Constraint(expr=   m.x6 - m.x8 + 30*m.b25 <= 26)

m.c43 = Constraint(expr=   m.x7 - m.x8 + 30*m.b26 <= 27)

m.c44 = Constraint(expr= - m.x5 + m.x6 + 30*m.b27 <= 24.5)

m.c45 = Constraint(expr= - m.x5 + m.x7 + 30*m.b28 <= 25.5)

m.c46 = Constraint(expr= - m.x5 + m.x8 + 30*m.b29 <= 25.5)

m.c47 = Constraint(expr= - m.x6 + m.x7 + 30*m.b30 <= 26)

m.c48 = Constraint(expr= - m.x6 + m.x8 + 30*m.b31 <= 26)

m.c49 = Constraint(expr= - m.x7 + m.x8 + 30*m.b32 <= 27)

m.c50 = Constraint(expr=   m.b9 + m.b15 + m.b21 + m.b27 == 1)

m.c51 = Constraint(expr=   m.b10 + m.b16 + m.b22 + m.b28 == 1)

m.c52 = Constraint(expr=   m.b11 + m.b17 + m.b23 + m.b29 == 1)

m.c53 = Constraint(expr=   m.b12 + m.b18 + m.b24 + m.b30 == 1)

m.c54 = Constraint(expr=   m.b13 + m.b19 + m.b25 + m.b31 == 1)

m.c55 = Constraint(expr=   m.b14 + m.b20 + m.b26 + m.b32 == 1)
