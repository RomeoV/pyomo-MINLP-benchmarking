#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         55        8       15       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         36       26       10        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        155      149        6        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,7),initialize=0)
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

m.obj = Objective(expr=   5*m.x8 - 2*m.x13 + 200*m.x21 + 250*m.x22 + 200*m.x23 + 200*m.x24 + 500*m.x25 + 350*m.x26
                        - 5*m.b27 - 8*m.b28 - 6*m.b29 - 10*m.b30 - 6*m.b31 - 7*m.b32 - 4*m.b33 - 5*m.b34 - 2*m.b35
                        - 4*m.b36, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=   m.x14 - m.x17 - m.x18 == 0)

m.c7 = Constraint(expr=   m.x16 - m.x19 - m.x20 - m.x21 == 0)

m.c8 = Constraint(expr=-log(1 + m.x3) + m.x5 + m.b27 <= 1)

m.c9 = Constraint(expr=   m.x3 - 10*m.b27 <= 0)

m.c10 = Constraint(expr=   m.x5 - 2.39789527279837*m.b27 <= 0)

m.c11 = Constraint(expr=-1.2*log(1 + m.x4) + m.x6 + m.b28 <= 1)

m.c12 = Constraint(expr=   m.x4 - 10*m.b28 <= 0)

m.c13 = Constraint(expr=   m.x6 - 2.87747432735804*m.b28 <= 0)

m.c14 = Constraint(expr= - 0.75*m.x10 + m.x14 + m.b29 <= 1)

m.c15 = Constraint(expr= - 0.75*m.x10 + m.x14 - m.b29 >= -1)

m.c16 = Constraint(expr=   m.x10 - 2.87747432735804*m.b29 <= 0)

m.c17 = Constraint(expr=   m.x14 - 2.15810574551853*m.b29 <= 0)

m.c18 = Constraint(expr=-1.5*log(1 + m.x11) + m.x15 + m.b30 <= 1)

m.c19 = Constraint(expr=   m.x11 - 2.87747432735804*m.b30 <= 0)

m.c20 = Constraint(expr=   m.x15 - 2.03277599268042*m.b30 <= 0)

m.c21 = Constraint(expr= - m.x12 + m.x16 + m.b31 <= 1)

m.c22 = Constraint(expr= - m.x12 + m.x16 - m.b31 >= -1)

m.c23 = Constraint(expr= - 0.5*m.x13 + m.x16 + m.b31 <= 1)

m.c24 = Constraint(expr= - 0.5*m.x13 + m.x16 - m.b31 >= -1)

m.c25 = Constraint(expr=   m.x12 - 2.87747432735804*m.b31 <= 0)

m.c26 = Constraint(expr=   m.x13 - 7*m.b31 <= 0)

m.c27 = Constraint(expr=   m.x16 - 3.5*m.b31 <= 0)

m.c28 = Constraint(expr=-1.25*log(1 + m.x17) + m.x22 + m.b32 <= 1)

m.c29 = Constraint(expr=   m.x17 - 2.15810574551853*m.b32 <= 0)

m.c30 = Constraint(expr=   m.x22 - 1.43746550029693*m.b32 <= 0)

m.c31 = Constraint(expr=-0.9*log(1 + m.x18) + m.x23 + m.b33 <= 1)

m.c32 = Constraint(expr=   m.x18 - 2.15810574551853*m.b33 <= 0)

m.c33 = Constraint(expr=   m.x23 - 1.03497516021379*m.b33 <= 0)

m.c34 = Constraint(expr=-log(1 + m.x15) + m.x24 + m.b34 <= 1)

m.c35 = Constraint(expr=   m.x15 - 2.03277599268042*m.b34 <= 0)

m.c36 = Constraint(expr=   m.x24 - 1.10947836929589*m.b34 <= 0)

m.c37 = Constraint(expr= - 0.9*m.x19 + m.x25 + m.b35 <= 1)

m.c38 = Constraint(expr= - 0.9*m.x19 + m.x25 - m.b35 >= -1)

m.c39 = Constraint(expr=   m.x19 - 3.5*m.b35 <= 0)

m.c40 = Constraint(expr=   m.x25 - 3.15*m.b35 <= 0)

m.c41 = Constraint(expr= - 0.6*m.x20 + m.x26 + m.b36 <= 1)

m.c42 = Constraint(expr= - 0.6*m.x20 + m.x26 - m.b36 >= -1)

m.c43 = Constraint(expr=   m.x20 - 3.5*m.b36 <= 0)

m.c44 = Constraint(expr=   m.x26 - 2.1*m.b36 <= 0)

m.c45 = Constraint(expr=   m.b27 + m.b28 == 1)

m.c46 = Constraint(expr= - m.b29 + m.b32 + m.b33 >= 0)

m.c47 = Constraint(expr= - m.b30 + m.b34 >= 0)

m.c48 = Constraint(expr=   m.b27 + m.b28 - m.b29 >= 0)

m.c49 = Constraint(expr=   m.b27 + m.b28 - m.b30 >= 0)

m.c50 = Constraint(expr=   m.b27 + m.b28 - m.b31 >= 0)

m.c51 = Constraint(expr=   m.b29 - m.b32 >= 0)

m.c52 = Constraint(expr=   m.b29 - m.b33 >= 0)

m.c53 = Constraint(expr=   m.b30 - m.b34 >= 0)

m.c54 = Constraint(expr=   m.b31 - m.b35 >= 0)

m.c55 = Constraint(expr=   m.b31 - m.b36 >= 0)
