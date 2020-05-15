#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         59       31        3       25        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         43       38        5        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        138      129        9        0
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
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   5*m.x8 - 2*m.x13 + 200*m.x14 + 250*m.x15 + 300*m.x16 - 5*m.b39 - 8*m.b40 - 6*m.b41 - 10*m.b42
                        - 6*m.b43, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=(m.x21/(1e-6 + m.b39) - log(1 + m.x17/(1e-6 + m.b39)))*(1e-6 + m.b39) <= 0)

m.c7 = Constraint(expr=   m.x18 == 0)

m.c8 = Constraint(expr=   m.x22 == 0)

m.c9 = Constraint(expr=   m.x3 - m.x17 - m.x18 == 0)

m.c10 = Constraint(expr=   m.x5 - m.x21 - m.x22 == 0)

m.c11 = Constraint(expr=   m.x17 - 10*m.b39 <= 0)

m.c12 = Constraint(expr=   m.x18 + 10*m.b39 <= 10)

m.c13 = Constraint(expr=   m.x21 - 2.39789527279837*m.b39 <= 0)

m.c14 = Constraint(expr=   m.x22 + 2.39789527279837*m.b39 <= 2.39789527279837)

m.c15 = Constraint(expr=(m.x23/(1e-6 + m.b40) - 1.2*log(1 + m.x19/(1e-6 + m.b40)))*(1e-6 + m.b40) <= 0)

m.c16 = Constraint(expr=   m.x20 == 0)

m.c17 = Constraint(expr=   m.x24 == 0)

m.c18 = Constraint(expr=   m.x4 - m.x19 - m.x20 == 0)

m.c19 = Constraint(expr=   m.x6 - m.x23 - m.x24 == 0)

m.c20 = Constraint(expr=   m.x19 - 10*m.b40 <= 0)

m.c21 = Constraint(expr=   m.x20 + 10*m.b40 <= 10)

m.c22 = Constraint(expr=   m.x23 - 2.87747432735804*m.b40 <= 0)

m.c23 = Constraint(expr=   m.x24 + 2.87747432735804*m.b40 <= 2.87747432735804)

m.c24 = Constraint(expr= - 0.75*m.x25 + m.x33 == 0)

m.c25 = Constraint(expr=   m.x26 == 0)

m.c26 = Constraint(expr=   m.x34 == 0)

m.c27 = Constraint(expr=   m.x10 - m.x25 - m.x26 == 0)

m.c28 = Constraint(expr=   m.x14 - m.x33 - m.x34 == 0)

m.c29 = Constraint(expr=   m.x25 - 2.87747432735804*m.b41 <= 0)

m.c30 = Constraint(expr=   m.x26 + 2.87747432735804*m.b41 <= 2.87747432735804)

m.c31 = Constraint(expr=   m.x33 - 2.15810574551853*m.b41 <= 0)

m.c32 = Constraint(expr=   m.x34 + 2.15810574551853*m.b41 <= 2.15810574551853)

m.c33 = Constraint(expr=(m.x35/(1e-6 + m.b42) - 1.5*log(1 + m.x27/(1e-6 + m.b42)))*(1e-6 + m.b42) <= 0)

m.c34 = Constraint(expr=   m.x28 == 0)

m.c35 = Constraint(expr=   m.x36 == 0)

m.c36 = Constraint(expr=   m.x11 - m.x27 - m.x28 == 0)

m.c37 = Constraint(expr=   m.x15 - m.x35 - m.x36 == 0)

m.c38 = Constraint(expr=   m.x27 - 2.87747432735804*m.b42 <= 0)

m.c39 = Constraint(expr=   m.x28 + 2.87747432735804*m.b42 <= 2.87747432735804)

m.c40 = Constraint(expr=   m.x35 - 2.03277599268042*m.b42 <= 0)

m.c41 = Constraint(expr=   m.x36 + 2.03277599268042*m.b42 <= 2.03277599268042)

m.c42 = Constraint(expr= - m.x29 + m.x37 == 0)

m.c43 = Constraint(expr= - 0.5*m.x31 + m.x37 == 0)

m.c44 = Constraint(expr=   m.x30 == 0)

m.c45 = Constraint(expr=   m.x32 == 0)

m.c46 = Constraint(expr=   m.x38 == 0)

m.c47 = Constraint(expr=   m.x12 - m.x29 - m.x30 == 0)

m.c48 = Constraint(expr=   m.x13 - m.x31 - m.x32 == 0)

m.c49 = Constraint(expr=   m.x16 - m.x37 - m.x38 == 0)

m.c50 = Constraint(expr=   m.x29 - 2.87747432735804*m.b43 <= 0)

m.c51 = Constraint(expr=   m.x30 + 2.87747432735804*m.b43 <= 2.87747432735804)

m.c52 = Constraint(expr=   m.x31 - 7*m.b43 <= 0)

m.c53 = Constraint(expr=   m.x32 + 7*m.b43 <= 7)

m.c54 = Constraint(expr=   m.x37 - 3.5*m.b43 <= 0)

m.c55 = Constraint(expr=   m.x38 + 3.5*m.b43 <= 3.5)

m.c56 = Constraint(expr=   m.b39 + m.b40 == 1)

m.c57 = Constraint(expr=   m.b39 + m.b40 - m.b41 >= 0)

m.c58 = Constraint(expr=   m.b39 + m.b40 - m.b42 >= 0)

m.c59 = Constraint(expr=   m.b39 + m.b40 - m.b43 >= 0)
