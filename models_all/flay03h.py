#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        145       28        6      111        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        123      111       12        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        387      384        3        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,29),initialize=0)
m.x7 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x8 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x9 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x10 = Var(within=Reals,bounds=(1,40),initialize=1)
m.x11 = Var(within=Reals,bounds=(1,50),initialize=1)
m.x12 = Var(within=Reals,bounds=(1,60),initialize=1)
m.x13 = Var(within=Reals,bounds=(0,30),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,30),initialize=0)
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
m.x105 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x106 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x107 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x108 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x109 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x110 = Var(within=Reals,bounds=(0,None),initialize=0)
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

m.obj = Objective(expr=   2*m.x13 + 2*m.x14, sense=minimize)

m.c2 = Constraint(expr= - m.x1 - m.x7 + m.x13 >= 0)

m.c3 = Constraint(expr= - m.x2 - m.x8 + m.x13 >= 0)

m.c4 = Constraint(expr= - m.x3 - m.x9 + m.x13 >= 0)

m.c5 = Constraint(expr= - m.x4 - m.x10 + m.x14 >= 0)

m.c6 = Constraint(expr= - m.x5 - m.x11 + m.x14 >= 0)

m.c7 = Constraint(expr= - m.x6 - m.x12 + m.x14 >= 0)

m.c8 = Constraint(expr=40/m.x10 - m.x7 <= 0)

m.c9 = Constraint(expr=50/m.x11 - m.x8 <= 0)

m.c10 = Constraint(expr=60/m.x12 - m.x9 <= 0)

m.c11 = Constraint(expr=   m.x1 - m.x15 - m.x17 - m.x19 - m.x21 == 0)

m.c12 = Constraint(expr=   m.x1 - m.x16 - m.x18 - m.x20 - m.x22 == 0)

m.c13 = Constraint(expr=   m.x2 - m.x23 - m.x25 - m.x27 - m.x29 == 0)

m.c14 = Constraint(expr=   m.x2 - m.x24 - m.x26 - m.x28 - m.x30 == 0)

m.c15 = Constraint(expr=   m.x3 - m.x31 - m.x33 - m.x35 - m.x37 == 0)

m.c16 = Constraint(expr=   m.x3 - m.x32 - m.x34 - m.x36 - m.x38 == 0)

m.c17 = Constraint(expr=   m.x4 - m.x39 - m.x41 - m.x43 - m.x45 == 0)

m.c18 = Constraint(expr=   m.x4 - m.x40 - m.x42 - m.x44 - m.x46 == 0)

m.c19 = Constraint(expr=   m.x5 - m.x47 - m.x49 - m.x51 - m.x53 == 0)

m.c20 = Constraint(expr=   m.x5 - m.x48 - m.x50 - m.x52 - m.x54 == 0)

m.c21 = Constraint(expr=   m.x6 - m.x55 - m.x57 - m.x59 - m.x61 == 0)

m.c22 = Constraint(expr=   m.x6 - m.x56 - m.x58 - m.x60 - m.x62 == 0)

m.c23 = Constraint(expr=   m.x7 - m.x63 - m.x65 - m.x67 - m.x69 == 0)

m.c24 = Constraint(expr=   m.x7 - m.x64 - m.x66 - m.x68 - m.x70 == 0)

m.c25 = Constraint(expr=   m.x8 - m.x71 - m.x73 - m.x75 - m.x77 == 0)

m.c26 = Constraint(expr=   m.x8 - m.x72 - m.x74 - m.x76 - m.x78 == 0)

m.c27 = Constraint(expr=   m.x9 - m.x79 - m.x81 - m.x83 - m.x85 == 0)

m.c28 = Constraint(expr=   m.x9 - m.x80 - m.x82 - m.x84 - m.x86 == 0)

m.c29 = Constraint(expr=   m.x10 - m.x87 - m.x89 - m.x91 - m.x93 == 0)

m.c30 = Constraint(expr=   m.x10 - m.x88 - m.x90 - m.x92 - m.x94 == 0)

m.c31 = Constraint(expr=   m.x11 - m.x95 - m.x97 - m.x99 - m.x101 == 0)

m.c32 = Constraint(expr=   m.x11 - m.x96 - m.x98 - m.x100 - m.x102 == 0)

m.c33 = Constraint(expr=   m.x12 - m.x103 - m.x105 - m.x107 - m.x109 == 0)

m.c34 = Constraint(expr=   m.x12 - m.x104 - m.x106 - m.x108 - m.x110 == 0)

m.c35 = Constraint(expr=   m.x15 - 29*m.b111 <= 0)

m.c36 = Constraint(expr=   m.x16 - 29*m.b112 <= 0)

m.c37 = Constraint(expr=   m.x17 - 29*m.b114 <= 0)

m.c38 = Constraint(expr=   m.x18 - 29*m.b115 <= 0)

m.c39 = Constraint(expr=   m.x19 - 29*m.b117 <= 0)

m.c40 = Constraint(expr=   m.x20 - 29*m.b118 <= 0)

m.c41 = Constraint(expr=   m.x21 - 29*m.b120 <= 0)

m.c42 = Constraint(expr=   m.x22 - 29*m.b121 <= 0)

m.c43 = Constraint(expr=   m.x23 - 29*m.b111 <= 0)

m.c44 = Constraint(expr=   m.x24 - 29*m.b113 <= 0)

m.c45 = Constraint(expr=   m.x25 - 29*m.b114 <= 0)

m.c46 = Constraint(expr=   m.x26 - 29*m.b116 <= 0)

m.c47 = Constraint(expr=   m.x27 - 29*m.b117 <= 0)

m.c48 = Constraint(expr=   m.x28 - 29*m.b119 <= 0)

m.c49 = Constraint(expr=   m.x29 - 29*m.b120 <= 0)

m.c50 = Constraint(expr=   m.x30 - 29*m.b122 <= 0)

m.c51 = Constraint(expr=   m.x31 - 29*m.b112 <= 0)

m.c52 = Constraint(expr=   m.x32 - 29*m.b113 <= 0)

m.c53 = Constraint(expr=   m.x33 - 29*m.b115 <= 0)

m.c54 = Constraint(expr=   m.x34 - 29*m.b116 <= 0)

m.c55 = Constraint(expr=   m.x35 - 29*m.b118 <= 0)

m.c56 = Constraint(expr=   m.x36 - 29*m.b119 <= 0)

m.c57 = Constraint(expr=   m.x37 - 29*m.b121 <= 0)

m.c58 = Constraint(expr=   m.x38 - 29*m.b122 <= 0)

m.c59 = Constraint(expr=   m.x39 - 29*m.b111 <= 0)

m.c60 = Constraint(expr=   m.x40 - 29*m.b112 <= 0)

m.c61 = Constraint(expr=   m.x41 - 29*m.b114 <= 0)

m.c62 = Constraint(expr=   m.x42 - 29*m.b115 <= 0)

m.c63 = Constraint(expr=   m.x43 - 29*m.b117 <= 0)

m.c64 = Constraint(expr=   m.x44 - 29*m.b118 <= 0)

m.c65 = Constraint(expr=   m.x45 - 29*m.b120 <= 0)

m.c66 = Constraint(expr=   m.x46 - 29*m.b121 <= 0)

m.c67 = Constraint(expr=   m.x47 - 29*m.b111 <= 0)

m.c68 = Constraint(expr=   m.x48 - 29*m.b113 <= 0)

m.c69 = Constraint(expr=   m.x49 - 29*m.b114 <= 0)

m.c70 = Constraint(expr=   m.x50 - 29*m.b116 <= 0)

m.c71 = Constraint(expr=   m.x51 - 29*m.b117 <= 0)

m.c72 = Constraint(expr=   m.x52 - 29*m.b119 <= 0)

m.c73 = Constraint(expr=   m.x53 - 29*m.b120 <= 0)

m.c74 = Constraint(expr=   m.x54 - 29*m.b122 <= 0)

m.c75 = Constraint(expr=   m.x55 - 29*m.b112 <= 0)

m.c76 = Constraint(expr=   m.x56 - 29*m.b113 <= 0)

m.c77 = Constraint(expr=   m.x57 - 29*m.b115 <= 0)

m.c78 = Constraint(expr=   m.x58 - 29*m.b116 <= 0)

m.c79 = Constraint(expr=   m.x59 - 29*m.b118 <= 0)

m.c80 = Constraint(expr=   m.x60 - 29*m.b119 <= 0)

m.c81 = Constraint(expr=   m.x61 - 29*m.b121 <= 0)

m.c82 = Constraint(expr=   m.x62 - 29*m.b122 <= 0)

m.c83 = Constraint(expr=   m.x63 - 40*m.b111 <= 0)

m.c84 = Constraint(expr=   m.x64 - 40*m.b112 <= 0)

m.c85 = Constraint(expr=   m.x65 - 40*m.b114 <= 0)

m.c86 = Constraint(expr=   m.x66 - 40*m.b115 <= 0)

m.c87 = Constraint(expr=   m.x67 - 40*m.b117 <= 0)

m.c88 = Constraint(expr=   m.x68 - 40*m.b118 <= 0)

m.c89 = Constraint(expr=   m.x69 - 40*m.b120 <= 0)

m.c90 = Constraint(expr=   m.x70 - 40*m.b121 <= 0)

m.c91 = Constraint(expr=   m.x71 - 40*m.b111 <= 0)

m.c92 = Constraint(expr=   m.x72 - 50*m.b113 <= 0)

m.c93 = Constraint(expr=   m.x73 - 40*m.b114 <= 0)

m.c94 = Constraint(expr=   m.x74 - 50*m.b116 <= 0)

m.c95 = Constraint(expr=   m.x75 - 40*m.b117 <= 0)

m.c96 = Constraint(expr=   m.x76 - 50*m.b119 <= 0)

m.c97 = Constraint(expr=   m.x77 - 40*m.b120 <= 0)

m.c98 = Constraint(expr=   m.x78 - 50*m.b122 <= 0)

m.c99 = Constraint(expr=   m.x79 - 40*m.b112 <= 0)

m.c100 = Constraint(expr=   m.x80 - 50*m.b113 <= 0)

m.c101 = Constraint(expr=   m.x81 - 40*m.b115 <= 0)

m.c102 = Constraint(expr=   m.x82 - 50*m.b116 <= 0)

m.c103 = Constraint(expr=   m.x83 - 40*m.b118 <= 0)

m.c104 = Constraint(expr=   m.x84 - 50*m.b119 <= 0)

m.c105 = Constraint(expr=   m.x85 - 40*m.b121 <= 0)

m.c106 = Constraint(expr=   m.x86 - 50*m.b122 <= 0)

m.c107 = Constraint(expr=   m.x87 - 40*m.b111 <= 0)

m.c108 = Constraint(expr=   m.x88 - 40*m.b112 <= 0)

m.c109 = Constraint(expr=   m.x89 - 40*m.b114 <= 0)

m.c110 = Constraint(expr=   m.x90 - 40*m.b115 <= 0)

m.c111 = Constraint(expr=   m.x91 - 40*m.b117 <= 0)

m.c112 = Constraint(expr=   m.x92 - 40*m.b118 <= 0)

m.c113 = Constraint(expr=   m.x93 - 40*m.b120 <= 0)

m.c114 = Constraint(expr=   m.x94 - 40*m.b121 <= 0)

m.c115 = Constraint(expr=   m.x95 - 40*m.b111 <= 0)

m.c116 = Constraint(expr=   m.x96 - 50*m.b113 <= 0)

m.c117 = Constraint(expr=   m.x97 - 40*m.b114 <= 0)

m.c118 = Constraint(expr=   m.x98 - 50*m.b116 <= 0)

m.c119 = Constraint(expr=   m.x99 - 40*m.b117 <= 0)

m.c120 = Constraint(expr=   m.x100 - 50*m.b119 <= 0)

m.c121 = Constraint(expr=   m.x101 - 40*m.b120 <= 0)

m.c122 = Constraint(expr=   m.x102 - 50*m.b122 <= 0)

m.c123 = Constraint(expr=   m.x103 - 40*m.b112 <= 0)

m.c124 = Constraint(expr=   m.x104 - 50*m.b113 <= 0)

m.c125 = Constraint(expr=   m.x105 - 40*m.b115 <= 0)

m.c126 = Constraint(expr=   m.x106 - 50*m.b116 <= 0)

m.c127 = Constraint(expr=   m.x107 - 40*m.b118 <= 0)

m.c128 = Constraint(expr=   m.x108 - 50*m.b119 <= 0)

m.c129 = Constraint(expr=   m.x109 - 40*m.b121 <= 0)

m.c130 = Constraint(expr=   m.x110 - 50*m.b122 <= 0)

m.c131 = Constraint(expr=   m.x15 - m.x23 + m.x63 <= 0)

m.c132 = Constraint(expr=   m.x16 - m.x31 + m.x64 <= 0)

m.c133 = Constraint(expr=   m.x24 - m.x32 + m.x72 <= 0)

m.c134 = Constraint(expr= - m.x17 + m.x25 + m.x73 <= 0)

m.c135 = Constraint(expr= - m.x18 + m.x33 + m.x81 <= 0)

m.c136 = Constraint(expr= - m.x26 + m.x34 + m.x82 <= 0)

m.c137 = Constraint(expr=   m.x43 - m.x51 + m.x91 <= 0)

m.c138 = Constraint(expr=   m.x44 - m.x59 + m.x92 <= 0)

m.c139 = Constraint(expr=   m.x52 - m.x60 + m.x100 <= 0)

m.c140 = Constraint(expr= - m.x45 + m.x53 + m.x101 <= 0)

m.c141 = Constraint(expr= - m.x46 + m.x61 + m.x109 <= 0)

m.c142 = Constraint(expr= - m.x54 + m.x62 + m.x110 <= 0)

m.c143 = Constraint(expr=   m.b111 + m.b114 + m.b117 + m.b120 == 1)

m.c144 = Constraint(expr=   m.b112 + m.b115 + m.b118 + m.b121 == 1)

m.c145 = Constraint(expr=   m.b113 + m.b116 + m.b119 + m.b122 == 1)
