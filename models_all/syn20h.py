#  MINLP written by GAMS Convert at 05/15/20 00:51:24
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        234      107       27      100        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        152      132       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        534      492       42        0
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
m.x30 = Var(within=Reals,bounds=(0,5),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,5),initialize=0)
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
m.x69 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x93 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x94 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x95 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x96 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x97 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x98 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x99 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x100 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x101 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x102 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x103 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x104 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x111 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x112 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x113 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x114 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x115 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x116 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x117 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x118 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x119 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x120 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x121 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x122 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x123 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x124 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x125 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x126 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x127 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x128 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b133 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b134 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b135 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b136 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b137 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b138 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b139 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b140 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b141 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b142 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b143 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b144 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b145 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b146 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b147 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b148 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b149 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b150 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b151 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b152 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   5*m.x8 + 200*m.x38 + 250*m.x39 + 200*m.x40 + 700*m.x41 + 400*m.x42 + 500*m.x43 + 400*m.x44
                        + 600*m.x45 + 700*m.x46 - 5*m.b133 - 8*m.b134 - 6*m.b135 - 10*m.b136 - 6*m.b137 - 7*m.b138
                        - 4*m.b139 - 5*m.b140 - 2*m.b141 - 4*m.b142 - 3*m.b143 - 7*m.b144 - 3*m.b145 - 2*m.b146
                        - 4*m.b147 - 2*m.b148 - 3*m.b149 - 5*m.b150 - 2*m.b151 - 8*m.b152, sense=maximize)

m.c2 = Constraint(expr=   m.x2 - m.x3 - m.x4 == 0)

m.c3 = Constraint(expr= - m.x5 - m.x6 + m.x7 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x8 - m.x9 == 0)

m.c5 = Constraint(expr=   m.x9 - m.x10 - m.x11 - m.x12 == 0)

m.c6 = Constraint(expr=   m.x14 - m.x17 - m.x18 == 0)

m.c7 = Constraint(expr=   m.x16 - m.x19 - m.x20 - m.x21 == 0)

m.c8 = Constraint(expr=   m.x24 - m.x28 - m.x29 == 0)

m.c9 = Constraint(expr= - m.x25 - m.x31 + m.x32 == 0)

m.c10 = Constraint(expr=   m.x26 - m.x33 - m.x34 == 0)

m.c11 = Constraint(expr=   m.x27 - m.x35 - m.x36 - m.x37 == 0)

m.c12 = Constraint(expr=(m.x51/(1e-6 + m.b133) - log(1 + m.x47/(1e-6 + m.b133)))*(1e-6 + m.b133) <= 0)

m.c13 = Constraint(expr=   m.x48 == 0)

m.c14 = Constraint(expr=   m.x52 == 0)

m.c15 = Constraint(expr=   m.x3 - m.x47 - m.x48 == 0)

m.c16 = Constraint(expr=   m.x5 - m.x51 - m.x52 == 0)

m.c17 = Constraint(expr=   m.x47 - 10*m.b133 <= 0)

m.c18 = Constraint(expr=   m.x48 + 10*m.b133 <= 10)

m.c19 = Constraint(expr=   m.x51 - 2.39789527279837*m.b133 <= 0)

m.c20 = Constraint(expr=   m.x52 + 2.39789527279837*m.b133 <= 2.39789527279837)

m.c21 = Constraint(expr=(m.x53/(1e-6 + m.b134) - 1.2*log(1 + m.x49/(1e-6 + m.b134)))*(1e-6 + m.b134) <= 0)

m.c22 = Constraint(expr=   m.x50 == 0)

m.c23 = Constraint(expr=   m.x54 == 0)

m.c24 = Constraint(expr=   m.x4 - m.x49 - m.x50 == 0)

m.c25 = Constraint(expr=   m.x6 - m.x53 - m.x54 == 0)

m.c26 = Constraint(expr=   m.x49 - 10*m.b134 <= 0)

m.c27 = Constraint(expr=   m.x50 + 10*m.b134 <= 10)

m.c28 = Constraint(expr=   m.x53 - 2.87747432735804*m.b134 <= 0)

m.c29 = Constraint(expr=   m.x54 + 2.87747432735804*m.b134 <= 2.87747432735804)

m.c30 = Constraint(expr= - 0.75*m.x55 + m.x63 == 0)

m.c31 = Constraint(expr=   m.x56 == 0)

m.c32 = Constraint(expr=   m.x64 == 0)

m.c33 = Constraint(expr=   m.x10 - m.x55 - m.x56 == 0)

m.c34 = Constraint(expr=   m.x14 - m.x63 - m.x64 == 0)

m.c35 = Constraint(expr=   m.x55 - 2.87747432735804*m.b135 <= 0)

m.c36 = Constraint(expr=   m.x56 + 2.87747432735804*m.b135 <= 2.87747432735804)

m.c37 = Constraint(expr=   m.x63 - 2.15810574551853*m.b135 <= 0)

m.c38 = Constraint(expr=   m.x64 + 2.15810574551853*m.b135 <= 2.15810574551853)

m.c39 = Constraint(expr=(m.x65/(1e-6 + m.b136) - 1.5*log(1 + m.x57/(1e-6 + m.b136)))*(1e-6 + m.b136) <= 0)

m.c40 = Constraint(expr=   m.x58 == 0)

m.c41 = Constraint(expr=   m.x67 == 0)

m.c42 = Constraint(expr=   m.x11 - m.x57 - m.x58 == 0)

m.c43 = Constraint(expr=   m.x15 - m.x65 - m.x67 == 0)

m.c44 = Constraint(expr=   m.x57 - 2.87747432735804*m.b136 <= 0)

m.c45 = Constraint(expr=   m.x58 + 2.87747432735804*m.b136 <= 2.87747432735804)

m.c46 = Constraint(expr=   m.x65 - 2.03277599268042*m.b136 <= 0)

m.c47 = Constraint(expr=   m.x67 + 2.03277599268042*m.b136 <= 2.03277599268042)

m.c48 = Constraint(expr= - m.x59 + m.x69 == 0)

m.c49 = Constraint(expr= - 0.5*m.x61 + m.x69 == 0)

m.c50 = Constraint(expr=   m.x60 == 0)

m.c51 = Constraint(expr=   m.x62 == 0)

m.c52 = Constraint(expr=   m.x70 == 0)

m.c53 = Constraint(expr=   m.x12 - m.x59 - m.x60 == 0)

m.c54 = Constraint(expr=   m.x13 - m.x61 - m.x62 == 0)

m.c55 = Constraint(expr=   m.x16 - m.x69 - m.x70 == 0)

m.c56 = Constraint(expr=   m.x59 - 2.87747432735804*m.b137 <= 0)

m.c57 = Constraint(expr=   m.x60 + 2.87747432735804*m.b137 <= 2.87747432735804)

m.c58 = Constraint(expr=   m.x61 - 7*m.b137 <= 0)

m.c59 = Constraint(expr=   m.x62 + 7*m.b137 <= 7)

m.c60 = Constraint(expr=   m.x69 - 3.5*m.b137 <= 0)

m.c61 = Constraint(expr=   m.x70 + 3.5*m.b137 <= 3.5)

m.c62 = Constraint(expr=(m.x81/(1e-6 + m.b138) - 1.25*log(1 + m.x71/(1e-6 + m.b138)))*(1e-6 + m.b138) <= 0)

m.c63 = Constraint(expr=   m.x72 == 0)

m.c64 = Constraint(expr=   m.x83 == 0)

m.c65 = Constraint(expr=   m.x17 - m.x71 - m.x72 == 0)

m.c66 = Constraint(expr=   m.x22 - m.x81 - m.x83 == 0)

m.c67 = Constraint(expr=   m.x71 - 2.15810574551853*m.b138 <= 0)

m.c68 = Constraint(expr=   m.x72 + 2.15810574551853*m.b138 <= 2.15810574551853)

m.c69 = Constraint(expr=   m.x81 - 1.43746550029693*m.b138 <= 0)

m.c70 = Constraint(expr=   m.x83 + 1.43746550029693*m.b138 <= 1.43746550029693)

m.c71 = Constraint(expr=(m.x85/(1e-6 + m.b139) - 0.9*log(1 + m.x73/(1e-6 + m.b139)))*(1e-6 + m.b139) <= 0)

m.c72 = Constraint(expr=   m.x74 == 0)

m.c73 = Constraint(expr=   m.x87 == 0)

m.c74 = Constraint(expr=   m.x18 - m.x73 - m.x74 == 0)

m.c75 = Constraint(expr=   m.x23 - m.x85 - m.x87 == 0)

m.c76 = Constraint(expr=   m.x73 - 2.15810574551853*m.b139 <= 0)

m.c77 = Constraint(expr=   m.x74 + 2.15810574551853*m.b139 <= 2.15810574551853)

m.c78 = Constraint(expr=   m.x85 - 1.03497516021379*m.b139 <= 0)

m.c79 = Constraint(expr=   m.x87 + 1.03497516021379*m.b139 <= 1.03497516021379)

m.c80 = Constraint(expr=(m.x89/(1e-6 + m.b140) - log(1 + m.x66/(1e-6 + m.b140)))*(1e-6 + m.b140) <= 0)

m.c81 = Constraint(expr=   m.x68 == 0)

m.c82 = Constraint(expr=   m.x90 == 0)

m.c83 = Constraint(expr=   m.x15 - m.x66 - m.x68 == 0)

m.c84 = Constraint(expr=   m.x24 - m.x89 - m.x90 == 0)

m.c85 = Constraint(expr=   m.x66 - 2.03277599268042*m.b140 <= 0)

m.c86 = Constraint(expr=   m.x68 + 2.03277599268042*m.b140 <= 2.03277599268042)

m.c87 = Constraint(expr=   m.x89 - 1.10947836929589*m.b140 <= 0)

m.c88 = Constraint(expr=   m.x90 + 1.10947836929589*m.b140 <= 1.10947836929589)

m.c89 = Constraint(expr= - 0.9*m.x75 + m.x91 == 0)

m.c90 = Constraint(expr=   m.x76 == 0)

m.c91 = Constraint(expr=   m.x92 == 0)

m.c92 = Constraint(expr=   m.x19 - m.x75 - m.x76 == 0)

m.c93 = Constraint(expr=   m.x25 - m.x91 - m.x92 == 0)

m.c94 = Constraint(expr=   m.x75 - 3.5*m.b141 <= 0)

m.c95 = Constraint(expr=   m.x76 + 3.5*m.b141 <= 3.5)

m.c96 = Constraint(expr=   m.x91 - 3.15*m.b141 <= 0)

m.c97 = Constraint(expr=   m.x92 + 3.15*m.b141 <= 3.15)

m.c98 = Constraint(expr= - 0.6*m.x77 + m.x93 == 0)

m.c99 = Constraint(expr=   m.x78 == 0)

m.c100 = Constraint(expr=   m.x94 == 0)

m.c101 = Constraint(expr=   m.x20 - m.x77 - m.x78 == 0)

m.c102 = Constraint(expr=   m.x26 - m.x93 - m.x94 == 0)

m.c103 = Constraint(expr=   m.x77 - 3.5*m.b142 <= 0)

m.c104 = Constraint(expr=   m.x78 + 3.5*m.b142 <= 3.5)

m.c105 = Constraint(expr=   m.x93 - 2.1*m.b142 <= 0)

m.c106 = Constraint(expr=   m.x94 + 2.1*m.b142 <= 2.1)

m.c107 = Constraint(expr=(m.x95/(1e-6 + m.b143) - 1.1*log(1 + m.x79/(1e-6 + m.b143)))*(1e-6 + m.b143) <= 0)

m.c108 = Constraint(expr=   m.x80 == 0)

m.c109 = Constraint(expr=   m.x96 == 0)

m.c110 = Constraint(expr=   m.x21 - m.x79 - m.x80 == 0)

m.c111 = Constraint(expr=   m.x27 - m.x95 - m.x96 == 0)

m.c112 = Constraint(expr=   m.x79 - 3.5*m.b143 <= 0)

m.c113 = Constraint(expr=   m.x80 + 3.5*m.b143 <= 3.5)

m.c114 = Constraint(expr=   m.x95 - 1.6544851364539*m.b143 <= 0)

m.c115 = Constraint(expr=   m.x96 + 1.6544851364539*m.b143 <= 1.6544851364539)

m.c116 = Constraint(expr= - 0.9*m.x82 + m.x115 == 0)

m.c117 = Constraint(expr= - m.x101 + m.x115 == 0)

m.c118 = Constraint(expr=   m.x84 == 0)

m.c119 = Constraint(expr=   m.x102 == 0)

m.c120 = Constraint(expr=   m.x116 == 0)

m.c121 = Constraint(expr=   m.x22 - m.x82 - m.x84 == 0)

m.c122 = Constraint(expr=   m.x30 - m.x101 - m.x102 == 0)

m.c123 = Constraint(expr=   m.x38 - m.x115 - m.x116 == 0)

m.c124 = Constraint(expr=   m.x82 - 1.43746550029693*m.b144 <= 0)

m.c125 = Constraint(expr=   m.x84 + 1.43746550029693*m.b144 <= 1.43746550029693)

m.c126 = Constraint(expr=   m.x101 - 5*m.b144 <= 0)

m.c127 = Constraint(expr=   m.x102 + 5*m.b144 <= 5)

m.c128 = Constraint(expr=   m.x115 - 5*m.b144 <= 0)

m.c129 = Constraint(expr=   m.x116 + 5*m.b144 <= 5)

m.c130 = Constraint(expr=(m.x117/(1e-6 + m.b145) - log(1 + m.x86/(1e-6 + m.b145)))*(1e-6 + m.b145) <= 0)

m.c131 = Constraint(expr=   m.x88 == 0)

m.c132 = Constraint(expr=   m.x118 == 0)

m.c133 = Constraint(expr=   m.x23 - m.x86 - m.x88 == 0)

m.c134 = Constraint(expr=   m.x39 - m.x117 - m.x118 == 0)

m.c135 = Constraint(expr=   m.x86 - 1.03497516021379*m.b145 <= 0)

m.c136 = Constraint(expr=   m.x88 + 1.03497516021379*m.b145 <= 1.03497516021379)

m.c137 = Constraint(expr=   m.x117 - 0.710483612536911*m.b145 <= 0)

m.c138 = Constraint(expr=   m.x118 + 0.710483612536911*m.b145 <= 0.710483612536911)

m.c139 = Constraint(expr=(m.x119/(1e-6 + m.b146) - 0.7*log(1 + m.x97/(1e-6 + m.b146)))*(1e-6 + m.b146) <= 0)

m.c140 = Constraint(expr=   m.x98 == 0)

m.c141 = Constraint(expr=   m.x120 == 0)

m.c142 = Constraint(expr=   m.x28 - m.x97 - m.x98 == 0)

m.c143 = Constraint(expr=   m.x40 - m.x119 - m.x120 == 0)

m.c144 = Constraint(expr=   m.x97 - 1.10947836929589*m.b146 <= 0)

m.c145 = Constraint(expr=   m.x98 + 1.10947836929589*m.b146 <= 1.10947836929589)

m.c146 = Constraint(expr=   m.x119 - 0.522508489006913*m.b146 <= 0)

m.c147 = Constraint(expr=   m.x120 + 0.522508489006913*m.b146 <= 0.522508489006913)

m.c148 = Constraint(expr=(m.x121/(1e-6 + m.b147) - 0.65*log(1 + m.x99/(1e-6 + m.b147)))*(1e-6 + m.b147) <= 0)

m.c149 = Constraint(expr=(m.x121/(1e-6 + m.b147) - 0.65*log(1 + m.x103/(1e-6 + m.b147)))*(1e-6 + m.b147) <= 0)

m.c150 = Constraint(expr=   m.x100 == 0)

m.c151 = Constraint(expr=   m.x104 == 0)

m.c152 = Constraint(expr=   m.x122 == 0)

m.c153 = Constraint(expr=   m.x29 - m.x99 - m.x100 == 0)

m.c154 = Constraint(expr=   m.x32 - m.x103 - m.x104 == 0)

m.c155 = Constraint(expr=   m.x41 - m.x121 - m.x122 == 0)

m.c156 = Constraint(expr=   m.x99 - 1.10947836929589*m.b147 <= 0)

m.c157 = Constraint(expr=   m.x100 + 1.10947836929589*m.b147 <= 1.10947836929589)

m.c158 = Constraint(expr=   m.x103 - 8.15*m.b147 <= 0)

m.c159 = Constraint(expr=   m.x104 + 8.15*m.b147 <= 8.15)

m.c160 = Constraint(expr=   m.x121 - 1.43894002153683*m.b147 <= 0)

m.c161 = Constraint(expr=   m.x122 + 1.43894002153683*m.b147 <= 1.43894002153683)

m.c162 = Constraint(expr= - m.x105 + m.x123 == 0)

m.c163 = Constraint(expr=   m.x106 == 0)

m.c164 = Constraint(expr=   m.x124 == 0)

m.c165 = Constraint(expr=   m.x33 - m.x105 - m.x106 == 0)

m.c166 = Constraint(expr=   m.x42 - m.x123 - m.x124 == 0)

m.c167 = Constraint(expr=   m.x105 - 2.1*m.b148 <= 0)

m.c168 = Constraint(expr=   m.x106 + 2.1*m.b148 <= 2.1)

m.c169 = Constraint(expr=   m.x123 - 2.1*m.b148 <= 0)

m.c170 = Constraint(expr=   m.x124 + 2.1*m.b148 <= 2.1)

m.c171 = Constraint(expr= - m.x107 + m.x125 == 0)

m.c172 = Constraint(expr=   m.x108 == 0)

m.c173 = Constraint(expr=   m.x126 == 0)

m.c174 = Constraint(expr=   m.x34 - m.x107 - m.x108 == 0)

m.c175 = Constraint(expr=   m.x43 - m.x125 - m.x126 == 0)

m.c176 = Constraint(expr=   m.x107 - 2.1*m.b149 <= 0)

m.c177 = Constraint(expr=   m.x108 + 2.1*m.b149 <= 2.1)

m.c178 = Constraint(expr=   m.x125 - 2.1*m.b149 <= 0)

m.c179 = Constraint(expr=   m.x126 + 2.1*m.b149 <= 2.1)

m.c180 = Constraint(expr=(m.x127/(1e-6 + m.b150) - 0.75*log(1 + m.x109/(1e-6 + m.b150)))*(1e-6 + m.b150) <= 0)

m.c181 = Constraint(expr=   m.x110 == 0)

m.c182 = Constraint(expr=   m.x128 == 0)

m.c183 = Constraint(expr=   m.x35 - m.x109 - m.x110 == 0)

m.c184 = Constraint(expr=   m.x44 - m.x127 - m.x128 == 0)

m.c185 = Constraint(expr=   m.x109 - 1.6544851364539*m.b150 <= 0)

m.c186 = Constraint(expr=   m.x110 + 1.6544851364539*m.b150 <= 1.6544851364539)

m.c187 = Constraint(expr=   m.x127 - 0.732188035236726*m.b150 <= 0)

m.c188 = Constraint(expr=   m.x128 + 0.732188035236726*m.b150 <= 0.732188035236726)

m.c189 = Constraint(expr=(m.x129/(1e-6 + m.b151) - 0.8*log(1 + m.x111/(1e-6 + m.b151)))*(1e-6 + m.b151) <= 0)

m.c190 = Constraint(expr=   m.x112 == 0)

m.c191 = Constraint(expr=   m.x130 == 0)

m.c192 = Constraint(expr=   m.x36 - m.x111 - m.x112 == 0)

m.c193 = Constraint(expr=   m.x45 - m.x129 - m.x130 == 0)

m.c194 = Constraint(expr=   m.x111 - 1.6544851364539*m.b151 <= 0)

m.c195 = Constraint(expr=   m.x112 + 1.6544851364539*m.b151 <= 1.6544851364539)

m.c196 = Constraint(expr=   m.x129 - 0.781000570919175*m.b151 <= 0)

m.c197 = Constraint(expr=   m.x130 + 0.781000570919175*m.b151 <= 0.781000570919175)

m.c198 = Constraint(expr=(m.x131/(1e-6 + m.b152) - 0.85*log(1 + m.x113/(1e-6 + m.b152)))*(1e-6 + m.b152) <= 0)

m.c199 = Constraint(expr=   m.x114 == 0)

m.c200 = Constraint(expr=   m.x132 == 0)

m.c201 = Constraint(expr=   m.x37 - m.x113 - m.x114 == 0)

m.c202 = Constraint(expr=   m.x46 - m.x131 - m.x132 == 0)

m.c203 = Constraint(expr=   m.x113 - 1.6544851364539*m.b152 <= 0)

m.c204 = Constraint(expr=   m.x114 + 1.6544851364539*m.b152 <= 1.6544851364539)

m.c205 = Constraint(expr=   m.x131 - 0.829813106601623*m.b152 <= 0)

m.c206 = Constraint(expr=   m.x132 + 0.829813106601623*m.b152 <= 0.829813106601623)

m.c207 = Constraint(expr=   m.b133 + m.b134 == 1)

m.c208 = Constraint(expr= - m.b135 + m.b138 + m.b139 >= 0)

m.c209 = Constraint(expr= - m.b138 + m.b144 >= 0)

m.c210 = Constraint(expr= - m.b139 + m.b145 >= 0)

m.c211 = Constraint(expr= - m.b136 + m.b140 >= 0)

m.c212 = Constraint(expr= - m.b140 + m.b146 + m.b147 >= 0)

m.c213 = Constraint(expr= - m.b137 + m.b141 + m.b142 + m.b143 >= 0)

m.c214 = Constraint(expr= - m.b141 + m.b147 >= 0)

m.c215 = Constraint(expr= - m.b142 + m.b148 + m.b149 >= 0)

m.c216 = Constraint(expr= - m.b143 + m.b150 + m.b151 + m.b152 >= 0)

m.c217 = Constraint(expr=   m.b133 + m.b134 - m.b135 >= 0)

m.c218 = Constraint(expr=   m.b133 + m.b134 - m.b136 >= 0)

m.c219 = Constraint(expr=   m.b133 + m.b134 - m.b137 >= 0)

m.c220 = Constraint(expr=   m.b135 - m.b138 >= 0)

m.c221 = Constraint(expr=   m.b135 - m.b139 >= 0)

m.c222 = Constraint(expr=   m.b136 - m.b140 >= 0)

m.c223 = Constraint(expr=   m.b137 - m.b141 >= 0)

m.c224 = Constraint(expr=   m.b137 - m.b142 >= 0)

m.c225 = Constraint(expr=   m.b137 - m.b143 >= 0)

m.c226 = Constraint(expr=   m.b138 - m.b144 >= 0)

m.c227 = Constraint(expr=   m.b139 - m.b145 >= 0)

m.c228 = Constraint(expr=   m.b140 - m.b146 >= 0)

m.c229 = Constraint(expr=   m.b140 - m.b147 >= 0)

m.c230 = Constraint(expr=   m.b142 - m.b148 >= 0)

m.c231 = Constraint(expr=   m.b142 - m.b149 >= 0)

m.c232 = Constraint(expr=   m.b143 - m.b150 >= 0)

m.c233 = Constraint(expr=   m.b143 - m.b151 >= 0)

m.c234 = Constraint(expr=   m.b143 - m.b152 >= 0)
