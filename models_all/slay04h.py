#  MINLP written by GAMS Convert at 05/15/20 00:51:18
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        175       31       24      120        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        141      117       24        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        501      493        8        0
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
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x129 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x130 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x131 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x132 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x133 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x134 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x135 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x136 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x137 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x138 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x139 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x140 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=150*((-4 + m.x1)**2 + (-10 + m.x5)**2) + 390*((-10 + m.x2)**2 + (-15 + m.x6)**2) + 240*((-7 + 
                       m.x3)**2 + (-9 + m.x7)**2) + 70*((-3 + m.x4)**2 + (-3 + m.x8)**2) + 300*m.x129 + 240*m.x130
                        + 210*m.x131 + 100*m.x132 + 150*m.x133 + 120*m.x134 + 300*m.x135 + 240*m.x136 + 210*m.x137
                        + 100*m.x138 + 150*m.x139 + 120*m.x140, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x129 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x130 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x131 >= 0)

m.c5 = Constraint(expr= - m.x2 + m.x3 + m.x132 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x4 + m.x133 >= 0)

m.c7 = Constraint(expr= - m.x3 + m.x4 + m.x134 >= 0)

m.c8 = Constraint(expr=   m.x1 - m.x2 + m.x129 >= 0)

m.c9 = Constraint(expr=   m.x1 - m.x3 + m.x130 >= 0)

m.c10 = Constraint(expr=   m.x1 - m.x4 + m.x131 >= 0)

m.c11 = Constraint(expr=   m.x2 - m.x3 + m.x132 >= 0)

m.c12 = Constraint(expr=   m.x2 - m.x4 + m.x133 >= 0)

m.c13 = Constraint(expr=   m.x3 - m.x4 + m.x134 >= 0)

m.c14 = Constraint(expr= - m.x5 + m.x6 + m.x135 >= 0)

m.c15 = Constraint(expr= - m.x5 + m.x7 + m.x136 >= 0)

m.c16 = Constraint(expr= - m.x5 + m.x8 + m.x137 >= 0)

m.c17 = Constraint(expr= - m.x6 + m.x7 + m.x138 >= 0)

m.c18 = Constraint(expr= - m.x6 + m.x8 + m.x139 >= 0)

m.c19 = Constraint(expr= - m.x7 + m.x8 + m.x140 >= 0)

m.c20 = Constraint(expr=   m.x5 - m.x6 + m.x135 >= 0)

m.c21 = Constraint(expr=   m.x5 - m.x7 + m.x136 >= 0)

m.c22 = Constraint(expr=   m.x5 - m.x8 + m.x137 >= 0)

m.c23 = Constraint(expr=   m.x6 - m.x7 + m.x138 >= 0)

m.c24 = Constraint(expr=   m.x6 - m.x8 + m.x139 >= 0)

m.c25 = Constraint(expr=   m.x7 - m.x8 + m.x140 >= 0)

m.c26 = Constraint(expr=   m.x1 - m.x9 - m.x12 - m.x15 - m.x18 == 0)

m.c27 = Constraint(expr=   m.x1 - m.x10 - m.x13 - m.x16 - m.x19 == 0)

m.c28 = Constraint(expr=   m.x1 - m.x11 - m.x14 - m.x17 - m.x20 == 0)

m.c29 = Constraint(expr=   m.x2 - m.x21 - m.x24 - m.x27 - m.x30 == 0)

m.c30 = Constraint(expr=   m.x2 - m.x22 - m.x25 - m.x28 - m.x31 == 0)

m.c31 = Constraint(expr=   m.x2 - m.x23 - m.x26 - m.x29 - m.x32 == 0)

m.c32 = Constraint(expr=   m.x3 - m.x33 - m.x36 - m.x39 - m.x42 == 0)

m.c33 = Constraint(expr=   m.x3 - m.x34 - m.x37 - m.x40 - m.x43 == 0)

m.c34 = Constraint(expr=   m.x3 - m.x35 - m.x38 - m.x41 - m.x44 == 0)

m.c35 = Constraint(expr=   m.x4 - m.x45 - m.x48 - m.x51 - m.x54 == 0)

m.c36 = Constraint(expr=   m.x4 - m.x46 - m.x49 - m.x52 - m.x55 == 0)

m.c37 = Constraint(expr=   m.x4 - m.x47 - m.x50 - m.x53 - m.x56 == 0)

m.c38 = Constraint(expr=   m.x5 - m.x57 - m.x60 - m.x63 - m.x66 == 0)

m.c39 = Constraint(expr=   m.x5 - m.x58 - m.x61 - m.x64 - m.x67 == 0)

m.c40 = Constraint(expr=   m.x5 - m.x59 - m.x62 - m.x65 - m.x68 == 0)

m.c41 = Constraint(expr=   m.x6 - m.x69 - m.x72 - m.x75 - m.x78 == 0)

m.c42 = Constraint(expr=   m.x6 - m.x70 - m.x73 - m.x76 - m.x79 == 0)

m.c43 = Constraint(expr=   m.x6 - m.x71 - m.x74 - m.x77 - m.x80 == 0)

m.c44 = Constraint(expr=   m.x7 - m.x81 - m.x84 - m.x87 - m.x90 == 0)

m.c45 = Constraint(expr=   m.x7 - m.x82 - m.x85 - m.x88 - m.x91 == 0)

m.c46 = Constraint(expr=   m.x7 - m.x83 - m.x86 - m.x89 - m.x92 == 0)

m.c47 = Constraint(expr=   m.x8 - m.x93 - m.x96 - m.x99 - m.x102 == 0)

m.c48 = Constraint(expr=   m.x8 - m.x94 - m.x97 - m.x100 - m.x103 == 0)

m.c49 = Constraint(expr=   m.x8 - m.x95 - m.x98 - m.x101 - m.x104 == 0)

m.c50 = Constraint(expr=   m.x9 - 27.5*m.b105 <= 0)

m.c51 = Constraint(expr=   m.x10 - 27.5*m.b106 <= 0)

m.c52 = Constraint(expr=   m.x11 - 27.5*m.b107 <= 0)

m.c53 = Constraint(expr=   m.x12 - 27.5*m.b111 <= 0)

m.c54 = Constraint(expr=   m.x13 - 27.5*m.b112 <= 0)

m.c55 = Constraint(expr=   m.x14 - 27.5*m.b113 <= 0)

m.c56 = Constraint(expr=   m.x15 - 27.5*m.b117 <= 0)

m.c57 = Constraint(expr=   m.x16 - 27.5*m.b118 <= 0)

m.c58 = Constraint(expr=   m.x17 - 27.5*m.b119 <= 0)

m.c59 = Constraint(expr=   m.x18 - 27.5*m.b123 <= 0)

m.c60 = Constraint(expr=   m.x19 - 27.5*m.b124 <= 0)

m.c61 = Constraint(expr=   m.x20 - 27.5*m.b125 <= 0)

m.c62 = Constraint(expr=   m.x21 - 27.5*m.b105 <= 0)

m.c63 = Constraint(expr=   m.x22 - 26.5*m.b108 <= 0)

m.c64 = Constraint(expr=   m.x23 - 26.5*m.b109 <= 0)

m.c65 = Constraint(expr=   m.x24 - 27.5*m.b111 <= 0)

m.c66 = Constraint(expr=   m.x25 - 26.5*m.b114 <= 0)

m.c67 = Constraint(expr=   m.x26 - 26.5*m.b115 <= 0)

m.c68 = Constraint(expr=   m.x27 - 27.5*m.b117 <= 0)

m.c69 = Constraint(expr=   m.x28 - 26.5*m.b120 <= 0)

m.c70 = Constraint(expr=   m.x29 - 26.5*m.b121 <= 0)

m.c71 = Constraint(expr=   m.x30 - 27.5*m.b123 <= 0)

m.c72 = Constraint(expr=   m.x31 - 26.5*m.b126 <= 0)

m.c73 = Constraint(expr=   m.x32 - 26.5*m.b127 <= 0)

m.c74 = Constraint(expr=   m.x33 - 27.5*m.b106 <= 0)

m.c75 = Constraint(expr=   m.x34 - 26.5*m.b108 <= 0)

m.c76 = Constraint(expr=   m.x35 - 28.5*m.b110 <= 0)

m.c77 = Constraint(expr=   m.x36 - 27.5*m.b112 <= 0)

m.c78 = Constraint(expr=   m.x37 - 26.5*m.b114 <= 0)

m.c79 = Constraint(expr=   m.x38 - 28.5*m.b116 <= 0)

m.c80 = Constraint(expr=   m.x39 - 27.5*m.b118 <= 0)

m.c81 = Constraint(expr=   m.x40 - 26.5*m.b120 <= 0)

m.c82 = Constraint(expr=   m.x41 - 28.5*m.b122 <= 0)

m.c83 = Constraint(expr=   m.x42 - 27.5*m.b124 <= 0)

m.c84 = Constraint(expr=   m.x43 - 26.5*m.b126 <= 0)

m.c85 = Constraint(expr=   m.x44 - 28.5*m.b128 <= 0)

m.c86 = Constraint(expr=   m.x45 - 27.5*m.b107 <= 0)

m.c87 = Constraint(expr=   m.x46 - 26.5*m.b109 <= 0)

m.c88 = Constraint(expr=   m.x47 - 28.5*m.b110 <= 0)

m.c89 = Constraint(expr=   m.x48 - 27.5*m.b113 <= 0)

m.c90 = Constraint(expr=   m.x49 - 26.5*m.b115 <= 0)

m.c91 = Constraint(expr=   m.x50 - 28.5*m.b116 <= 0)

m.c92 = Constraint(expr=   m.x51 - 27.5*m.b119 <= 0)

m.c93 = Constraint(expr=   m.x52 - 26.5*m.b121 <= 0)

m.c94 = Constraint(expr=   m.x53 - 28.5*m.b122 <= 0)

m.c95 = Constraint(expr=   m.x54 - 27.5*m.b125 <= 0)

m.c96 = Constraint(expr=   m.x55 - 26.5*m.b127 <= 0)

m.c97 = Constraint(expr=   m.x56 - 28.5*m.b128 <= 0)

m.c98 = Constraint(expr=   m.x57 - 27*m.b105 <= 0)

m.c99 = Constraint(expr=   m.x58 - 27*m.b106 <= 0)

m.c100 = Constraint(expr=   m.x59 - 27*m.b107 <= 0)

m.c101 = Constraint(expr=   m.x60 - 27*m.b111 <= 0)

m.c102 = Constraint(expr=   m.x61 - 27*m.b112 <= 0)

m.c103 = Constraint(expr=   m.x62 - 27*m.b113 <= 0)

m.c104 = Constraint(expr=   m.x63 - 27*m.b117 <= 0)

m.c105 = Constraint(expr=   m.x64 - 27*m.b118 <= 0)

m.c106 = Constraint(expr=   m.x65 - 27*m.b119 <= 0)

m.c107 = Constraint(expr=   m.x66 - 27*m.b123 <= 0)

m.c108 = Constraint(expr=   m.x67 - 27*m.b124 <= 0)

m.c109 = Constraint(expr=   m.x68 - 27*m.b125 <= 0)

m.c110 = Constraint(expr=   m.x69 - 27*m.b105 <= 0)

m.c111 = Constraint(expr=   m.x70 - 27.5*m.b108 <= 0)

m.c112 = Constraint(expr=   m.x71 - 27.5*m.b109 <= 0)

m.c113 = Constraint(expr=   m.x72 - 27*m.b111 <= 0)

m.c114 = Constraint(expr=   m.x73 - 27.5*m.b114 <= 0)

m.c115 = Constraint(expr=   m.x74 - 27.5*m.b115 <= 0)

m.c116 = Constraint(expr=   m.x75 - 27*m.b117 <= 0)

m.c117 = Constraint(expr=   m.x76 - 27.5*m.b120 <= 0)

m.c118 = Constraint(expr=   m.x77 - 27.5*m.b121 <= 0)

m.c119 = Constraint(expr=   m.x78 - 27*m.b123 <= 0)

m.c120 = Constraint(expr=   m.x79 - 27.5*m.b126 <= 0)

m.c121 = Constraint(expr=   m.x80 - 27.5*m.b127 <= 0)

m.c122 = Constraint(expr=   m.x81 - 27*m.b106 <= 0)

m.c123 = Constraint(expr=   m.x82 - 27.5*m.b108 <= 0)

m.c124 = Constraint(expr=   m.x83 - 28.5*m.b110 <= 0)

m.c125 = Constraint(expr=   m.x84 - 27*m.b112 <= 0)

m.c126 = Constraint(expr=   m.x85 - 27.5*m.b114 <= 0)

m.c127 = Constraint(expr=   m.x86 - 28.5*m.b116 <= 0)

m.c128 = Constraint(expr=   m.x87 - 27*m.b118 <= 0)

m.c129 = Constraint(expr=   m.x88 - 27.5*m.b120 <= 0)

m.c130 = Constraint(expr=   m.x89 - 28.5*m.b122 <= 0)

m.c131 = Constraint(expr=   m.x90 - 27*m.b124 <= 0)

m.c132 = Constraint(expr=   m.x91 - 27.5*m.b126 <= 0)

m.c133 = Constraint(expr=   m.x92 - 28.5*m.b128 <= 0)

m.c134 = Constraint(expr=   m.x93 - 27*m.b107 <= 0)

m.c135 = Constraint(expr=   m.x94 - 27.5*m.b109 <= 0)

m.c136 = Constraint(expr=   m.x95 - 28.5*m.b110 <= 0)

m.c137 = Constraint(expr=   m.x96 - 27*m.b113 <= 0)

m.c138 = Constraint(expr=   m.x97 - 27.5*m.b115 <= 0)

m.c139 = Constraint(expr=   m.x98 - 28.5*m.b116 <= 0)

m.c140 = Constraint(expr=   m.x99 - 27*m.b119 <= 0)

m.c141 = Constraint(expr=   m.x100 - 27.5*m.b121 <= 0)

m.c142 = Constraint(expr=   m.x101 - 28.5*m.b122 <= 0)

m.c143 = Constraint(expr=   m.x102 - 27*m.b125 <= 0)

m.c144 = Constraint(expr=   m.x103 - 27.5*m.b127 <= 0)

m.c145 = Constraint(expr=   m.x104 - 28.5*m.b128 <= 0)

m.c146 = Constraint(expr=   m.x9 - m.x21 + 6*m.b105 <= 0)

m.c147 = Constraint(expr=   m.x10 - m.x33 + 4*m.b106 <= 0)

m.c148 = Constraint(expr=   m.x11 - m.x45 + 3.5*m.b107 <= 0)

m.c149 = Constraint(expr=   m.x22 - m.x34 + 5*m.b108 <= 0)

m.c150 = Constraint(expr=   m.x23 - m.x46 + 4.5*m.b109 <= 0)

m.c151 = Constraint(expr=   m.x35 - m.x47 + 2.5*m.b110 <= 0)

m.c152 = Constraint(expr= - m.x12 + m.x24 + 6*m.b111 <= 0)

m.c153 = Constraint(expr= - m.x13 + m.x36 + 4*m.b112 <= 0)

m.c154 = Constraint(expr= - m.x14 + m.x48 + 3.5*m.b113 <= 0)

m.c155 = Constraint(expr= - m.x25 + m.x37 + 5*m.b114 <= 0)

m.c156 = Constraint(expr= - m.x26 + m.x49 + 4.5*m.b115 <= 0)

m.c157 = Constraint(expr= - m.x38 + m.x50 + 2.5*m.b116 <= 0)

m.c158 = Constraint(expr=   m.x63 - m.x75 + 5.5*m.b117 <= 0)

m.c159 = Constraint(expr=   m.x64 - m.x87 + 4.5*m.b118 <= 0)

m.c160 = Constraint(expr=   m.x65 - m.x99 + 4.5*m.b119 <= 0)

m.c161 = Constraint(expr=   m.x76 - m.x88 + 4*m.b120 <= 0)

m.c162 = Constraint(expr=   m.x77 - m.x100 + 4*m.b121 <= 0)

m.c163 = Constraint(expr=   m.x89 - m.x101 + 3*m.b122 <= 0)

m.c164 = Constraint(expr= - m.x66 + m.x78 + 5.5*m.b123 <= 0)

m.c165 = Constraint(expr= - m.x67 + m.x90 + 4.5*m.b124 <= 0)

m.c166 = Constraint(expr= - m.x68 + m.x102 + 4.5*m.b125 <= 0)

m.c167 = Constraint(expr= - m.x79 + m.x91 + 4*m.b126 <= 0)

m.c168 = Constraint(expr= - m.x80 + m.x103 + 4*m.b127 <= 0)

m.c169 = Constraint(expr= - m.x92 + m.x104 + 3*m.b128 <= 0)

m.c170 = Constraint(expr=   m.b105 + m.b111 + m.b117 + m.b123 == 1)

m.c171 = Constraint(expr=   m.b106 + m.b112 + m.b118 + m.b124 == 1)

m.c172 = Constraint(expr=   m.b107 + m.b113 + m.b119 + m.b125 == 1)

m.c173 = Constraint(expr=   m.b108 + m.b114 + m.b120 + m.b126 == 1)

m.c174 = Constraint(expr=   m.b109 + m.b115 + m.b121 + m.b127 == 1)

m.c175 = Constraint(expr=   m.b110 + m.b116 + m.b122 + m.b128 == 1)
