#  MINLP written by GAMS Convert at 05/15/20 00:51:23
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        113       55       10       48        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         78       68       10        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        261      243       18        0
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
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   5*m.x8 - 2*m.x13 + 200*m.x21 + 250*m.x22 + 200*m.x23 + 200*m.x24 + 500*m.x25 + 350*m.x26
                        - 5*m.b69 - 8*m.b70 - 6*m.b71 - 10*m.b72 - 6*m.b73 - 7*m.b74 - 4*m.b75 - 5*m.b76 - 2*m.b77
                        - 4*m.b78, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=   m.x14 - m.x17 - m.x18 == 0)

m.c7 = Constraint(expr=   m.x16 - m.x19 - m.x20 - m.x21 == 0)

m.c8 = Constraint(expr=(m.x31/(1e-6 + m.b69) - log(1 + m.x27/(1e-6 + m.b69)))*(1e-6 + m.b69) <= 0)

m.c9 = Constraint(expr=   m.x28 == 0)

m.c10 = Constraint(expr=   m.x32 == 0)

m.c11 = Constraint(expr=   m.x3 - m.x27 - m.x28 == 0)

m.c12 = Constraint(expr=   m.x5 - m.x31 - m.x32 == 0)

m.c13 = Constraint(expr=   m.x27 - 10*m.b69 <= 0)

m.c14 = Constraint(expr=   m.x28 + 10*m.b69 <= 10)

m.c15 = Constraint(expr=   m.x31 - 2.39789527279837*m.b69 <= 0)

m.c16 = Constraint(expr=   m.x32 + 2.39789527279837*m.b69 <= 2.39789527279837)

m.c17 = Constraint(expr=(m.x33/(1e-6 + m.b70) - 1.2*log(1 + m.x29/(1e-6 + m.b70)))*(1e-6 + m.b70) <= 0)

m.c18 = Constraint(expr=   m.x30 == 0)

m.c19 = Constraint(expr=   m.x34 == 0)

m.c20 = Constraint(expr=   m.x4 - m.x29 - m.x30 == 0)

m.c21 = Constraint(expr=   m.x6 - m.x33 - m.x34 == 0)

m.c22 = Constraint(expr=   m.x29 - 10*m.b70 <= 0)

m.c23 = Constraint(expr=   m.x30 + 10*m.b70 <= 10)

m.c24 = Constraint(expr=   m.x33 - 2.87747432735804*m.b70 <= 0)

m.c25 = Constraint(expr=   m.x34 + 2.87747432735804*m.b70 <= 2.87747432735804)

m.c26 = Constraint(expr= - 0.75*m.x35 + m.x43 == 0)

m.c27 = Constraint(expr=   m.x36 == 0)

m.c28 = Constraint(expr=   m.x44 == 0)

m.c29 = Constraint(expr=   m.x10 - m.x35 - m.x36 == 0)

m.c30 = Constraint(expr=   m.x14 - m.x43 - m.x44 == 0)

m.c31 = Constraint(expr=   m.x35 - 2.87747432735804*m.b71 <= 0)

m.c32 = Constraint(expr=   m.x36 + 2.87747432735804*m.b71 <= 2.87747432735804)

m.c33 = Constraint(expr=   m.x43 - 2.15810574551853*m.b71 <= 0)

m.c34 = Constraint(expr=   m.x44 + 2.15810574551853*m.b71 <= 2.15810574551853)

m.c35 = Constraint(expr=(m.x45/(1e-6 + m.b72) - 1.5*log(1 + m.x37/(1e-6 + m.b72)))*(1e-6 + m.b72) <= 0)

m.c36 = Constraint(expr=   m.x38 == 0)

m.c37 = Constraint(expr=   m.x47 == 0)

m.c38 = Constraint(expr=   m.x11 - m.x37 - m.x38 == 0)

m.c39 = Constraint(expr=   m.x15 - m.x45 - m.x47 == 0)

m.c40 = Constraint(expr=   m.x37 - 2.87747432735804*m.b72 <= 0)

m.c41 = Constraint(expr=   m.x38 + 2.87747432735804*m.b72 <= 2.87747432735804)

m.c42 = Constraint(expr=   m.x45 - 2.03277599268042*m.b72 <= 0)

m.c43 = Constraint(expr=   m.x47 + 2.03277599268042*m.b72 <= 2.03277599268042)

m.c44 = Constraint(expr= - m.x39 + m.x49 == 0)

m.c45 = Constraint(expr= - 0.5*m.x41 + m.x49 == 0)

m.c46 = Constraint(expr=   m.x40 == 0)

m.c47 = Constraint(expr=   m.x42 == 0)

m.c48 = Constraint(expr=   m.x50 == 0)

m.c49 = Constraint(expr=   m.x12 - m.x39 - m.x40 == 0)

m.c50 = Constraint(expr=   m.x13 - m.x41 - m.x42 == 0)

m.c51 = Constraint(expr=   m.x16 - m.x49 - m.x50 == 0)

m.c52 = Constraint(expr=   m.x39 - 2.87747432735804*m.b73 <= 0)

m.c53 = Constraint(expr=   m.x40 + 2.87747432735804*m.b73 <= 2.87747432735804)

m.c54 = Constraint(expr=   m.x41 - 7*m.b73 <= 0)

m.c55 = Constraint(expr=   m.x42 + 7*m.b73 <= 7)

m.c56 = Constraint(expr=   m.x49 - 3.5*m.b73 <= 0)

m.c57 = Constraint(expr=   m.x50 + 3.5*m.b73 <= 3.5)

m.c58 = Constraint(expr=(m.x59/(1e-6 + m.b74) - 1.25*log(1 + m.x51/(1e-6 + m.b74)))*(1e-6 + m.b74) <= 0)

m.c59 = Constraint(expr=   m.x52 == 0)

m.c60 = Constraint(expr=   m.x60 == 0)

m.c61 = Constraint(expr=   m.x17 - m.x51 - m.x52 == 0)

m.c62 = Constraint(expr=   m.x22 - m.x59 - m.x60 == 0)

m.c63 = Constraint(expr=   m.x51 - 2.15810574551853*m.b74 <= 0)

m.c64 = Constraint(expr=   m.x52 + 2.15810574551853*m.b74 <= 2.15810574551853)

m.c65 = Constraint(expr=   m.x59 - 1.43746550029693*m.b74 <= 0)

m.c66 = Constraint(expr=   m.x60 + 1.43746550029693*m.b74 <= 1.43746550029693)

m.c67 = Constraint(expr=(m.x61/(1e-6 + m.b75) - 0.9*log(1 + m.x53/(1e-6 + m.b75)))*(1e-6 + m.b75) <= 0)

m.c68 = Constraint(expr=   m.x54 == 0)

m.c69 = Constraint(expr=   m.x62 == 0)

m.c70 = Constraint(expr=   m.x18 - m.x53 - m.x54 == 0)

m.c71 = Constraint(expr=   m.x23 - m.x61 - m.x62 == 0)

m.c72 = Constraint(expr=   m.x53 - 2.15810574551853*m.b75 <= 0)

m.c73 = Constraint(expr=   m.x54 + 2.15810574551853*m.b75 <= 2.15810574551853)

m.c74 = Constraint(expr=   m.x61 - 1.03497516021379*m.b75 <= 0)

m.c75 = Constraint(expr=   m.x62 + 1.03497516021379*m.b75 <= 1.03497516021379)

m.c76 = Constraint(expr=(m.x63/(1e-6 + m.b76) - log(1 + m.x46/(1e-6 + m.b76)))*(1e-6 + m.b76) <= 0)

m.c77 = Constraint(expr=   m.x48 == 0)

m.c78 = Constraint(expr=   m.x64 == 0)

m.c79 = Constraint(expr=   m.x15 - m.x46 - m.x48 == 0)

m.c80 = Constraint(expr=   m.x24 - m.x63 - m.x64 == 0)

m.c81 = Constraint(expr=   m.x46 - 2.03277599268042*m.b76 <= 0)

m.c82 = Constraint(expr=   m.x48 + 2.03277599268042*m.b76 <= 2.03277599268042)

m.c83 = Constraint(expr=   m.x63 - 1.10947836929589*m.b76 <= 0)

m.c84 = Constraint(expr=   m.x64 + 1.10947836929589*m.b76 <= 1.10947836929589)

m.c85 = Constraint(expr= - 0.9*m.x55 + m.x65 == 0)

m.c86 = Constraint(expr=   m.x56 == 0)

m.c87 = Constraint(expr=   m.x66 == 0)

m.c88 = Constraint(expr=   m.x19 - m.x55 - m.x56 == 0)

m.c89 = Constraint(expr=   m.x25 - m.x65 - m.x66 == 0)

m.c90 = Constraint(expr=   m.x55 - 3.5*m.b77 <= 0)

m.c91 = Constraint(expr=   m.x56 + 3.5*m.b77 <= 3.5)

m.c92 = Constraint(expr=   m.x65 - 3.15*m.b77 <= 0)

m.c93 = Constraint(expr=   m.x66 + 3.15*m.b77 <= 3.15)

m.c94 = Constraint(expr= - 0.6*m.x57 + m.x67 == 0)

m.c95 = Constraint(expr=   m.x58 == 0)

m.c96 = Constraint(expr=   m.x68 == 0)

m.c97 = Constraint(expr=   m.x20 - m.x57 - m.x58 == 0)

m.c98 = Constraint(expr=   m.x26 - m.x67 - m.x68 == 0)

m.c99 = Constraint(expr=   m.x57 - 3.5*m.b78 <= 0)

m.c100 = Constraint(expr=   m.x58 + 3.5*m.b78 <= 3.5)

m.c101 = Constraint(expr=   m.x67 - 2.1*m.b78 <= 0)

m.c102 = Constraint(expr=   m.x68 + 2.1*m.b78 <= 2.1)

m.c103 = Constraint(expr=   m.b69 + m.b70 == 1)

m.c104 = Constraint(expr= - m.b71 + m.b74 + m.b75 >= 0)

m.c105 = Constraint(expr= - m.b72 + m.b76 >= 0)

m.c106 = Constraint(expr=   m.b69 + m.b70 - m.b71 >= 0)

m.c107 = Constraint(expr=   m.b69 + m.b70 - m.b72 >= 0)

m.c108 = Constraint(expr=   m.b69 + m.b70 - m.b73 >= 0)

m.c109 = Constraint(expr=   m.b71 - m.b74 >= 0)

m.c110 = Constraint(expr=   m.b71 - m.b75 >= 0)

m.c111 = Constraint(expr=   m.b72 - m.b76 >= 0)

m.c112 = Constraint(expr=   m.b73 - m.b77 >= 0)

m.c113 = Constraint(expr=   m.b73 - m.b78 >= 0)
