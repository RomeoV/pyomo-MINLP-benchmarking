#  MINLP written by GAMS Convert at 07/30/20 19:42:38
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        191      141       14       36        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        169      160        9        0        0        0        0        0
#  FX      1        0        1        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        695      434      261        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0.95,1),initialize=0.95)
m.x2 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x3 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x4 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x5 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x6 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x7 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x8 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x9 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x10 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x21 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x22 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x23 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x24 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x25 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x26 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x27 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x28 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x29 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x30 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x31 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x32 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x33 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x34 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x35 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x36 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x37 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x38 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x39 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x50 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x51 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x52 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x53 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x54 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x55 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x56 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x57 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x58 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x59 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x60 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x61 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x62 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x63 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x64 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x65 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x66 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x67 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x68 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x69 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x70 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x71 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x72 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x73 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x74 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x75 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x76 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x77 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x78 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x79 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x80 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x81 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x82 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x83 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x84 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x85 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x86 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x87 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x88 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x89 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x90 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x91 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x92 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x93 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x94 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x95 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x96 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x97 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x98 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x99 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x100 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x101 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x102 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x103 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x104 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x105 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x106 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x107 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x108 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x109 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x110 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x111 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x112 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x113 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x114 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x115 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x116 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x117 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x118 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x119 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x120 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x121 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x122 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x123 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x124 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x125 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x126 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x127 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x128 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x129 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x130 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x131 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x132 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x133 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x134 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x135 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x136 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x137 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x138 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x139 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x140 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x141 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x142 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x143 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x144 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x145 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x146 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x147 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x148 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x149 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x150 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x151 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x152 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x153 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x154 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x155 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x156 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x157 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x158 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x159 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.b160 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b161 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b162 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b163 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b164 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b165 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b166 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b167 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b168 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x1, sense=maximize)

m.c2 = Constraint(expr= - m.x11 + 0.001*m.b160 <= 0)

m.c3 = Constraint(expr= - m.x12 + 0.001*m.b161 <= 0)

m.c4 = Constraint(expr= - m.x13 + 0.001*m.b162 <= 0)

m.c5 = Constraint(expr= - m.x14 + 0.001*m.b163 <= 0)

m.c6 = Constraint(expr= - m.x15 + 0.001*m.b164 <= 0)

m.c7 = Constraint(expr= - m.x16 + 0.001*m.b165 <= 0)

m.c8 = Constraint(expr= - m.x17 + 0.001*m.b166 <= 0)

m.c9 = Constraint(expr= - m.x18 + 0.001*m.b167 <= 0)

m.c10 = Constraint(expr= - m.x19 + 0.001*m.b168 <= 0)

m.c11 = Constraint(expr=   m.x11 - 10*m.b160 <= 0)

m.c12 = Constraint(expr=   m.x12 - 10*m.b161 <= 0)

m.c13 = Constraint(expr=   m.x13 - 10*m.b162 <= 0)

m.c14 = Constraint(expr=   m.x14 - 10*m.b163 <= 0)

m.c15 = Constraint(expr=   m.x15 - 10*m.b164 <= 0)

m.c16 = Constraint(expr=   m.x16 - 10*m.b165 <= 0)

m.c17 = Constraint(expr=   m.x17 - 10*m.b166 <= 0)

m.c18 = Constraint(expr=   m.x18 - 10*m.b167 <= 0)

m.c19 = Constraint(expr=   m.x19 - 10*m.b168 <= 0)

m.c20 = Constraint(expr= - m.x40 + 0.001*m.b160 <= 0)

m.c21 = Constraint(expr= - m.x41 + 0.001*m.b161 <= 0)

m.c22 = Constraint(expr= - m.x42 + 0.001*m.b162 <= 0)

m.c23 = Constraint(expr= - m.x43 + 0.001*m.b163 <= 0)

m.c24 = Constraint(expr= - m.x44 + 0.001*m.b164 <= 0)

m.c25 = Constraint(expr= - m.x45 + 0.001*m.b165 <= 0)

m.c26 = Constraint(expr= - m.x46 + 0.001*m.b166 <= 0)

m.c27 = Constraint(expr= - m.x47 + 0.001*m.b167 <= 0)

m.c28 = Constraint(expr= - m.x48 + 0.001*m.b168 <= 0)

m.c29 = Constraint(expr=   m.x40 - 10*m.b160 <= 0)

m.c30 = Constraint(expr=   m.x41 - 10*m.b161 <= 0)

m.c31 = Constraint(expr=   m.x42 - 10*m.b162 <= 0)

m.c32 = Constraint(expr=   m.x43 - 10*m.b163 <= 0)

m.c33 = Constraint(expr=   m.x44 - 10*m.b164 <= 0)

m.c34 = Constraint(expr=   m.x45 - 10*m.b165 <= 0)

m.c35 = Constraint(expr=   m.x46 - 10*m.b166 <= 0)

m.c36 = Constraint(expr=   m.x47 - 10*m.b167 <= 0)

m.c37 = Constraint(expr=   m.x48 - 10*m.b168 <= 0)

m.c38 = Constraint(expr=   m.b160 - m.b161 >= 0)

m.c39 = Constraint(expr=   m.b161 - m.b162 >= 0)

m.c40 = Constraint(expr=   m.b162 - m.b163 >= 0)

m.c41 = Constraint(expr=   m.b163 - m.b164 >= 0)

m.c42 = Constraint(expr=   m.b164 - m.b165 >= 0)

m.c43 = Constraint(expr=   m.b165 - m.b166 >= 0)

m.c44 = Constraint(expr=   m.b166 - m.b167 >= 0)

m.c45 = Constraint(expr=   m.b167 - m.b168 >= 0)

m.c46 = Constraint(expr= - 10000000000*m.x2 + 10000000000*m.x11 + m.x20 == 0)

m.c47 = Constraint(expr=2000000000.00001*m.x1*m.x2 - 1000000000*m.x3 + 1000000000*m.x12 + m.x21 == 0)

m.c48 = Constraint(expr=200000000*m.x1*m.x3 - 100000000*m.x2 - 100000000*m.x4 - 100000000*m.x11 + 100000000*m.x13
                         + m.x22 == 0)

m.c49 = Constraint(expr=20000000*m.x1*m.x4 - 10000000*m.x3 - 10000000*m.x5 - 10000000*m.x12 + 10000000*m.x14 + m.x23
                         == 0)

m.c50 = Constraint(expr=2000000*m.x1*m.x5 - 1000000*m.x4 - 1000000*m.x6 - 1000000*m.x13 + 1000000*m.x15 + m.x24 == 0)

m.c51 = Constraint(expr=200000*m.x1*m.x6 - 100000*m.x5 - 100000*m.x7 - 100000*m.x14 + 100000*m.x16 + m.x25 == 0)

m.c52 = Constraint(expr=20000*m.x1*m.x7 - 10000*m.x6 - 10000*m.x8 - 10000*m.x15 + 10000*m.x17 + m.x26 == 0)

m.c53 = Constraint(expr=2000*m.x1*m.x8 - 1000*m.x7 - 1000*m.x9 - 1000*m.x16 + 1000*m.x18 + m.x27 == 0)

m.c54 = Constraint(expr=200*m.x1*m.x9 - 100*m.x8 - 100*m.x10 - 100*m.x17 + 100*m.x19 + m.x28 == 0)

m.c55 = Constraint(expr=20*m.x1*m.x10 - 10*m.x9 - 10*m.x18 + m.x29 == 0)

m.c56 = Constraint(expr= - m.x10 - m.x19 + m.x30 == 0)

m.c57 = Constraint(expr= - m.x2 + 1E-5*m.x3 - 1E-10*m.x4 + m.x31 == 0)

m.c58 = Constraint(expr= - m.x3 + 2E-5*m.x4 - 3E-10*m.x5 + m.x32 == 0)

m.c59 = Constraint(expr= - m.x4 + 3E-5*m.x5 - 6E-10*m.x6 + m.x33 == 0)

m.c60 = Constraint(expr= - m.x5 + 4E-5*m.x6 - 1E-9*m.x7 + m.x34 == 0)

m.c61 = Constraint(expr= - m.x6 + 5E-5*m.x7 - 1.5E-9*m.x8 + m.x35 == 0)

m.c62 = Constraint(expr= - m.x7 + 6E-5*m.x8 - 2.1E-9*m.x9 + m.x36 == 0)

m.c63 = Constraint(expr= - m.x8 + 7E-5*m.x9 - 2.8E-9*m.x10 + m.x37 == 0)

m.c64 = Constraint(expr= - m.x9 + 8E-5*m.x10 + m.x38 == 0)

m.c65 = Constraint(expr= - m.x10 + m.x39 == 0)

m.c66 = Constraint(expr= - m.x11 + 1E-5*m.x12 - 1E-10*m.x13 + m.x40 == 0)

m.c67 = Constraint(expr= - m.x12 + 2E-5*m.x13 - 3E-10*m.x14 + m.x41 == 0)

m.c68 = Constraint(expr= - m.x13 + 3E-5*m.x14 - 6E-10*m.x15 + m.x42 == 0)

m.c69 = Constraint(expr= - m.x14 + 4E-5*m.x15 - 1E-9*m.x16 + m.x43 == 0)

m.c70 = Constraint(expr= - m.x15 + 5E-5*m.x16 - 1.5E-9*m.x17 + m.x44 == 0)

m.c71 = Constraint(expr= - m.x16 + 6E-5*m.x17 - 2.1E-9*m.x18 + m.x45 == 0)

m.c72 = Constraint(expr= - m.x17 + 7E-5*m.x18 - 2.8E-9*m.x19 + m.x46 == 0)

m.c73 = Constraint(expr= - m.x18 + 8E-5*m.x19 + m.x47 == 0)

m.c74 = Constraint(expr= - m.x19 + m.x48 == 0)

m.c75 = Constraint(expr= - m.x20 + 1E-5*m.x21 - 1E-10*m.x22 + m.x49 == 0)

m.c76 = Constraint(expr= - m.x21 + 2E-5*m.x22 - 3E-10*m.x23 + m.x50 == 0)

m.c77 = Constraint(expr= - m.x22 + 3E-5*m.x23 - 6E-10*m.x24 + m.x51 == 0)

m.c78 = Constraint(expr= - m.x23 + 4E-5*m.x24 - 1E-9*m.x25 + m.x52 == 0)

m.c79 = Constraint(expr= - m.x24 + 5E-5*m.x25 - 1.5E-9*m.x26 + m.x53 == 0)

m.c80 = Constraint(expr= - m.x25 + 6E-5*m.x26 - 2.1E-9*m.x27 + m.x54 == 0)

m.c81 = Constraint(expr= - m.x26 + 7E-5*m.x27 - 2.8E-9*m.x28 + m.x55 == 0)

m.c82 = Constraint(expr= - m.x27 + 8E-5*m.x28 - 3.6E-9*m.x29 + m.x56 == 0)

m.c83 = Constraint(expr= - m.x28 + 9E-5*m.x29 - 4.5E-9*m.x30 + m.x57 == 0)

m.c84 = Constraint(expr= - m.x29 + 0.0001*m.x30 + m.x58 == 0)

m.c85 = Constraint(expr= - m.x30 + m.x59 == 0)

m.c86 = Constraint(expr= - m.x39 + m.x60 == 0)

m.c87 = Constraint(expr= - m.x37 + m.x61 == 0)

m.c88 = Constraint(expr= - m.x35 + m.x62 == 0)

m.c89 = Constraint(expr= - m.x33 + m.x63 == 0)

m.c90 = Constraint(expr= - m.x31 + m.x64 == 0)

m.c91 = Constraint(expr= - m.x38 + m.x65 == 0)

m.c92 = Constraint(expr= - m.x36 + m.x66 == 0)

m.c93 = Constraint(expr= - m.x34 + m.x67 == 0)

m.c94 = Constraint(expr= - m.x32 + m.x68 == 0)

m.c95 = Constraint(expr=   m.x69 == 0)

m.c96 = Constraint(expr=m.x60*m.x66/m.x65 - m.x61 + m.x70 == 0)

m.c97 = Constraint(expr=m.x60*m.x67/m.x65 - m.x62 + m.x71 == 0)

m.c98 = Constraint(expr=m.x60*m.x68/m.x65 - m.x63 + m.x72 == 0)

m.c99 = Constraint(expr=m.x60*m.x69/m.x65 - m.x64 + m.x73 == 0)

m.c100 = Constraint(expr=m.x65*m.x71/m.x70 - m.x66 + m.x75 == 0)

m.c101 = Constraint(expr=m.x65*m.x72/m.x70 - m.x67 + m.x76 == 0)

m.c102 = Constraint(expr=m.x65*m.x73/m.x70 - m.x68 + m.x77 == 0)

m.c103 = Constraint(expr=m.x65*m.x74/m.x70 - m.x69 + m.x78 == 0)

m.c104 = Constraint(expr=m.x70*m.x76/m.x75 - m.x71 + m.x80 == 0)

m.c105 = Constraint(expr=m.x70*m.x77/m.x75 - m.x72 + m.x81 == 0)

m.c106 = Constraint(expr=m.x70*m.x78/m.x75 - m.x73 + m.x82 == 0)

m.c107 = Constraint(expr=m.x70*m.x79/m.x75 - m.x74 + m.x83 == 0)

m.c108 = Constraint(expr=m.x75*m.x81/m.x80 - m.x76 + m.x85 == 0)

m.c109 = Constraint(expr=m.x75*m.x82/m.x80 - m.x77 + m.x86 == 0)

m.c110 = Constraint(expr=m.x75*m.x83/m.x80 - m.x78 + m.x87 == 0)

m.c111 = Constraint(expr=m.x75*m.x84/m.x80 - m.x79 + m.x88 == 0)

m.c112 = Constraint(expr=m.x80*m.x86/m.x85 - m.x81 + m.x90 == 0)

m.c113 = Constraint(expr=m.x80*m.x87/m.x85 - m.x82 + m.x91 == 0)

m.c114 = Constraint(expr=m.x80*m.x88/m.x85 - m.x83 + m.x92 == 0)

m.c115 = Constraint(expr=m.x80*m.x89/m.x85 - m.x84 + m.x93 == 0)

m.c116 = Constraint(expr=m.x85*m.x91/m.x90 - m.x86 + m.x95 == 0)

m.c117 = Constraint(expr=m.x85*m.x92/m.x90 - m.x87 + m.x96 == 0)

m.c118 = Constraint(expr=m.x85*m.x93/m.x90 - m.x88 + m.x97 == 0)

m.c119 = Constraint(expr=m.x85*m.x94/m.x90 - m.x89 + m.x98 == 0)

m.c120 = Constraint(expr=   m.x74 == 0)

m.c121 = Constraint(expr=   m.x79 == 0)

m.c122 = Constraint(expr=   m.x84 == 0)

m.c123 = Constraint(expr=   m.x89 == 0)

m.c124 = Constraint(expr=   m.x94 == 0)

m.c125 = Constraint(expr=   m.x99 == 0)

m.c126 = Constraint(expr= - m.x59 + m.x100 == 0)

m.c127 = Constraint(expr= - m.x57 + m.x101 == 0)

m.c128 = Constraint(expr= - m.x55 + m.x102 == 0)

m.c129 = Constraint(expr= - m.x53 + m.x103 == 0)

m.c130 = Constraint(expr= - m.x51 + m.x104 == 0)

m.c131 = Constraint(expr= - m.x49 + m.x105 == 0)

m.c132 = Constraint(expr= - m.x58 + m.x106 == 0)

m.c133 = Constraint(expr= - m.x56 + m.x107 == 0)

m.c134 = Constraint(expr= - m.x54 + m.x108 == 0)

m.c135 = Constraint(expr= - m.x52 + m.x109 == 0)

m.c136 = Constraint(expr= - m.x50 + m.x110 == 0)

m.c137 = Constraint(expr=   m.x111 == 0)

m.c138 = Constraint(expr=m.x100*m.x107/m.x106 - m.x101 + m.x112 == 0)

m.c139 = Constraint(expr=m.x100*m.x108/m.x106 - m.x102 + m.x113 == 0)

m.c140 = Constraint(expr=m.x100*m.x109/m.x106 - m.x103 + m.x114 == 0)

m.c141 = Constraint(expr=m.x100*m.x110/m.x106 - m.x104 + m.x115 == 0)

m.c142 = Constraint(expr=m.x100*m.x111/m.x106 - m.x105 + m.x116 == 0)

m.c143 = Constraint(expr=m.x106*m.x113/m.x112 - m.x107 + m.x118 == 0)

m.c144 = Constraint(expr=m.x106*m.x114/m.x112 - m.x108 + m.x119 == 0)

m.c145 = Constraint(expr=m.x106*m.x115/m.x112 - m.x109 + m.x120 == 0)

m.c146 = Constraint(expr=m.x106*m.x116/m.x112 - m.x110 + m.x121 == 0)

m.c147 = Constraint(expr=m.x106*m.x117/m.x112 - m.x111 + m.x122 == 0)

m.c148 = Constraint(expr=m.x112*m.x119/m.x118 - m.x113 + m.x124 == 0)

m.c149 = Constraint(expr=m.x112*m.x120/m.x118 - m.x114 + m.x125 == 0)

m.c150 = Constraint(expr=m.x112*m.x121/m.x118 - m.x115 + m.x126 == 0)

m.c151 = Constraint(expr=m.x112*m.x122/m.x118 - m.x116 + m.x127 == 0)

m.c152 = Constraint(expr=m.x112*m.x123/m.x118 - m.x117 + m.x128 == 0)

m.c153 = Constraint(expr=m.x118*m.x125/m.x124 - m.x119 + m.x130 == 0)

m.c154 = Constraint(expr=m.x118*m.x126/m.x124 - m.x120 + m.x131 == 0)

m.c155 = Constraint(expr=m.x118*m.x127/m.x124 - m.x121 + m.x132 == 0)

m.c156 = Constraint(expr=m.x118*m.x128/m.x124 - m.x122 + m.x133 == 0)

m.c157 = Constraint(expr=m.x118*m.x129/m.x124 - m.x123 + m.x134 == 0)

m.c158 = Constraint(expr=m.x124*m.x131/m.x130 - m.x125 + m.x136 == 0)

m.c159 = Constraint(expr=m.x124*m.x132/m.x130 - m.x126 + m.x137 == 0)

m.c160 = Constraint(expr=m.x124*m.x133/m.x130 - m.x127 + m.x138 == 0)

m.c161 = Constraint(expr=m.x124*m.x134/m.x130 - m.x128 + m.x139 == 0)

m.c162 = Constraint(expr=m.x124*m.x135/m.x130 - m.x129 + m.x140 == 0)

m.c163 = Constraint(expr=m.x130*m.x137/m.x136 - m.x131 + m.x142 == 0)

m.c164 = Constraint(expr=m.x130*m.x138/m.x136 - m.x132 + m.x143 == 0)

m.c165 = Constraint(expr=m.x130*m.x139/m.x136 - m.x133 + m.x144 == 0)

m.c166 = Constraint(expr=m.x130*m.x140/m.x136 - m.x134 + m.x145 == 0)

m.c167 = Constraint(expr=m.x130*m.x141/m.x136 - m.x135 + m.x146 == 0)

m.c168 = Constraint(expr=m.x136*m.x143/m.x142 - m.x137 + m.x148 == 0)

m.c169 = Constraint(expr=m.x136*m.x144/m.x142 - m.x138 + m.x149 == 0)

m.c170 = Constraint(expr=m.x136*m.x145/m.x142 - m.x139 + m.x150 == 0)

m.c171 = Constraint(expr=m.x136*m.x146/m.x142 - m.x140 + m.x151 == 0)

m.c172 = Constraint(expr=m.x136*m.x147/m.x142 - m.x141 + m.x152 == 0)

m.c173 = Constraint(expr=m.x142*m.x149/m.x148 - m.x143 + m.x154 == 0)

m.c174 = Constraint(expr=m.x142*m.x150/m.x148 - m.x144 + m.x155 == 0)

m.c175 = Constraint(expr=m.x142*m.x151/m.x148 - m.x145 + m.x156 == 0)

m.c176 = Constraint(expr=m.x142*m.x152/m.x148 - m.x146 + m.x157 == 0)

m.c177 = Constraint(expr=m.x142*m.x153/m.x148 - m.x147 + m.x158 == 0)

m.c178 = Constraint(expr=   m.x117 == 0)

m.c179 = Constraint(expr=   m.x123 == 0)

m.c180 = Constraint(expr=   m.x129 == 0)

m.c181 = Constraint(expr=   m.x135 == 0)

m.c182 = Constraint(expr=   m.x141 == 0)

m.c183 = Constraint(expr=   m.x147 == 0)

m.c184 = Constraint(expr=   m.x153 == 0)

m.c185 = Constraint(expr=   m.x159 == 0)

m.c186 = Constraint(expr=m.x46*m.x47 - m.x45*m.x48 - 1E-5*m.b168 >= 0)

m.c187 = Constraint(expr=m.x45*m.x46*m.x47 - m.x45*m.x45*m.x48 + m.x43*m.x47*m.x48 - m.x44*m.x47*m.x47 - 1E-5*m.b167
                          >= 0)

m.c188 = Constraint(expr=m.x44*m.x45*m.x46*m.x47 - m.x45**2*m.x44*m.x48 - m.x44**2*m.x47**2 + 2*m.x43*m.x44*m.x47*m.x48
                          + m.x43*m.x45*m.x46*m.x48 - m.x43**2*m.x48**2 - m.x46**2*m.x43*m.x47 + m.x42*m.x46*m.x47**2 - 
                         m.x42*m.x45*m.x47*m.x48 - m.x41*m.x46*m.x47*m.x48 + m.x41*m.x45*m.x48**2 + (m.x44*m.x45 - m.x43
                         *m.x46)*(1 - m.b167) - 1E-5*m.b166 >= 0)

m.c189 = Constraint(expr=m.x41*m.x45*m.x46**2*m.x47 - m.x43**2*m.x46**2*m.x47 + 2*m.x42*m.x43*m.x46*m.x47**2 - m.x41*
                         m.x44*m.x46*m.x47**2 - m.x40*m.x45*m.x46*m.x47**2 + m.x43*m.x44*m.x45*m.x46*m.x47 - m.x41*m.x43
                         *m.x46*m.x47*m.x48 - m.x45**2*m.x42*m.x46*m.x47 + m.x43**2*m.x45*m.x46*m.x48 - m.x45**2*m.x41*
                         m.x46*m.x48 + m.x40*m.x44*m.x47**3 - m.x42**2*m.x47**3 + m.x42*m.x44*m.x45*m.x47**2 + 2*m.x41*
                         m.x42*m.x47**2*m.x48 - m.x40*m.x43*m.x47**2*m.x48 - m.x44**2*m.x43*m.x47**2 - 3*m.x42*m.x43*
                         m.x45*m.x47*m.x48 - m.x41**2*m.x47*m.x48**2 + 2*m.x43**2*m.x44*m.x47*m.x48 + m.x45**2*m.x40*
                         m.x47*m.x48 - m.x43**3*m.x48**2 - m.x43*m.x44*m.x45**2*m.x48 + 2*m.x41*m.x43*m.x45*m.x48**2 + 
                         m.x45**3*m.x42*m.x48 + (m.x43*m.x44*m.x45 - m.x43**2*m.x46 - m.x45**2*m.x42 + m.x41*m.x45*m.x46
                         )*(1 - m.b167) - 1E-5*m.b165 >= 0)

m.c190 = Constraint(expr=m.x41**3*m.x48**3 - m.x40*m.x42*m.x45*m.x46*m.x47**2 + 2*m.x41*m.x42*m.x45*m.x46**2*m.x47 - 
                         m.x40**2*m.x46*m.x47**3 + m.x44**3*m.x41*m.x47**2 - m.x43**3*m.x42*m.x48**2 - m.x41**2*m.x46**3
                         *m.x47 + 2*m.x40*m.x42*m.x44*m.x47**3 - m.x44**2*m.x40*m.x45*m.x47**2 + 2*m.x40*m.x41*m.x46**2*
                         m.x47**2 + m.x42**2*m.x44*m.x45*m.x47**2 - m.x42**2*m.x45**2*m.x46*m.x47 - 3*m.x41**2*m.x42*
                         m.x47*m.x48**2 + m.x40*m.x41*m.x45**2*m.x48**2 - 2*m.x41**2*m.x44*m.x45*m.x48**2 + m.x40**2*
                         m.x45*m.x47**2*m.x48 + 3*m.x42**2*m.x41*m.x47**2*m.x48 + m.x41**2*m.x45*m.x46**2*m.x48 - m.x40*
                         m.x44*m.x45**3*m.x48 + m.x44**2*m.x41*m.x45**2*m.x48 - 3*m.x41*m.x42*m.x44*m.x46*m.x47**2 + 
                         m.x40*m.x44*m.x45**2*m.x46*m.x47 - m.x44**2*m.x41*m.x45*m.x46*m.x47 + m.x42**2*m.x45**3*m.x48
                          - 2*m.x40*m.x41*m.x44*m.x47**2*m.x48 + m.x40*m.x42*m.x45**2*m.x47*m.x48 + m.x41*m.x42*m.x44*
                         m.x45*m.x47*m.x48 - 3*m.x40*m.x41*m.x45*m.x46*m.x47*m.x48 + 3*m.x41**2*m.x44*m.x46*m.x47*m.x48
                          - 2*m.x41*m.x42*m.x45**2*m.x46*m.x48 - m.x41**2*m.x43*m.x46*m.x48**2 - m.x42*m.x43*m.x44**2*
                         m.x47**2 + 2*m.x42**2*m.x43*m.x46*m.x47**2 + m.x43**2*m.x41*m.x44*m.x48**2 - m.x43**2*m.x40*
                         m.x45*m.x48**2 - m.x43**2*m.x42*m.x46**2*m.x47 + m.x40*m.x43*m.x45**2*m.x46*m.x48 - m.x41*m.x43
                         *m.x44*m.x45*m.x46*m.x48 - m.x40*m.x43*m.x45*m.x46**2*m.x47 + m.x42*m.x43*m.x44*m.x45*m.x46*
                         m.x47 + m.x41*m.x43*m.x44*m.x46**2*m.x47 + 2*m.x43**2*m.x42*m.x44*m.x47*m.x48 + m.x43**2*m.x42*
                         m.x45*m.x46*m.x48 + 2*m.x40*m.x41*m.x43*m.x47*m.x48**2 + 3*m.x41*m.x42*m.x43*m.x45*m.x48**2 - 2
                         *m.x40*m.x42*m.x43*m.x47**2*m.x48 + 2*m.x40*m.x43*m.x44*m.x45*m.x47*m.x48 - 3*m.x42**2*m.x43*
                         m.x45*m.x47*m.x48 - 2*m.x41*m.x43*m.x44**2*m.x47*m.x48 - m.x41*m.x42*m.x43*m.x46*m.x47*m.x48 - 
                         m.x42*m.x43*m.x44*m.x45**2*m.x48 - m.x47**3*m.x42**3 + (m.x42*m.x43*m.x44*m.x45 - m.x43**2*
                         m.x42*m.x46 - m.x42**2*m.x45**2 + 2*m.x41*m.x42*m.x45*m.x46 + m.x41*m.x43*m.x44*m.x46 - m.x41**
                         2*m.x46**2 - m.x44**2*m.x41*m.x45 + m.x40*m.x44*m.x45**2 - m.x40*m.x43*m.x45*m.x46)*(1 - m.b167
                         ) + (m.x42*m.x43 - m.x41*m.x44)*(1 - m.b165) - 1E-5*m.b164 >= 0)

m.c191 = Constraint(expr=4*m.x41**2*m.x40*m.x43*m.x47*m.x48**2 - 2*m.x40*m.x41*m.x44*m.x45**3*m.x48 - 2*m.x43**3*m.x40*
                         m.x44*m.x47*m.x48 - 4*m.x40**2*m.x43*m.x45**2*m.x47*m.x48 + 3*m.x40**2*m.x43*m.x45*m.x46*m.x47
                         **2 + 4*m.x40**2*m.x41*m.x45*m.x47**2*m.x48 + m.x40**2*m.x44*m.x45**2*m.x47**2 - m.x42**3*m.x41
                         *m.x47**3 + m.x43**4*m.x40*m.x48**2 + m.x40**2*m.x48*m.x45**4 - 2*m.x40*m.x42*m.x43**2*m.x46*
                         m.x47**2 - m.x43**3*m.x40*m.x45*m.x46*m.x48 + m.x43**2*m.x40*m.x44*m.x45**2*m.x48 - m.x40*m.x42
                         *m.x43*m.x45**3*m.x48 - 4*m.x40*m.x41*m.x43**2*m.x45*m.x48**2 - 2*m.x40*m.x41*m.x44**2*m.x45*
                         m.x47**2 + 3*m.x40*m.x41*m.x42*m.x44*m.x47**3 - 3*m.x41**2*m.x40*m.x44*m.x47**2*m.x48 + 4*m.x40
                         *m.x41*m.x43*m.x44*m.x45*m.x47*m.x48 - m.x41**3*m.x43*m.x46*m.x48**2 - m.x41*m.x42*m.x43*m.x44*
                         m.x45**2*m.x48 + m.x41**2*m.x44**3*m.x47**2 + 2*m.x41**2*m.x42*m.x45*m.x46**2*m.x47 + m.x41**2*
                         m.x43*m.x44*m.x46**2*m.x47 - m.x41**2*m.x42*m.x43*m.x46*m.x47*m.x48 - m.x41**2*m.x43*m.x44*
                         m.x45*m.x46*m.x48 - 2*m.x41**2*m.x42*m.x45**2*m.x46*m.x48 - 3*m.x41**2*m.x42*m.x44*m.x46*m.x47
                         **2 - m.x41**2*m.x44**2*m.x45*m.x46*m.x47 + 3*m.x41**2*m.x42*m.x43*m.x45*m.x48**2 + m.x41**2*
                         m.x42*m.x44*m.x45*m.x47*m.x48 - 2*m.x41**2*m.x43*m.x44**2*m.x47*m.x48 + m.x42**2*m.x41*m.x44*
                         m.x45*m.x47**2 - m.x42**2*m.x41*m.x45**2*m.x46*m.x47 + m.x42**2*m.x41*m.x45**3*m.x48 - m.x41*
                         m.x42*m.x43*m.x44**2*m.x47**2 + 2*m.x42**2*m.x41*m.x43*m.x46*m.x47**2 - m.x41*m.x42*m.x43**2*
                         m.x46**2*m.x47 + m.x41*m.x42*m.x43*m.x44*m.x45*m.x46*m.x47 + 2*m.x41*m.x42*m.x43**2*m.x44*m.x47
                         *m.x48 + m.x41*m.x42*m.x43**2*m.x45*m.x46*m.x48 - 3*m.x42**2*m.x41*m.x43*m.x45*m.x47*m.x48 + 2*
                         m.x41**2*m.x40*m.x45**2*m.x48**2 + m.x48**3*m.x41**4 + 3*m.x41**2*m.x40*m.x46**2*m.x47**2 + 
                         m.x40*m.x42*m.x43*m.x45**2*m.x46*m.x47 - m.x43**2*m.x40*m.x44*m.x45*m.x46*m.x47 - 5*m.x40*m.x41
                         *m.x42*m.x43*m.x47**2*m.x48 + 3*m.x40*m.x41*m.x43*m.x45**2*m.x46*m.x48 + m.x40*m.x41*m.x42*
                         m.x45**2*m.x47*m.x48 + 2*m.x40*m.x41*m.x44*m.x45**2*m.x46*m.x47 - 5*m.x41**2*m.x40*m.x45*m.x46*
                         m.x47*m.x48 - m.x40*m.x42*m.x43*m.x44*m.x45*m.x47**2 + m.x40*m.x41*m.x43*m.x44*m.x46*m.x47**2
                          + 3*m.x40*m.x42*m.x43**2*m.x45*m.x47*m.x48 + m.x40*m.x41*m.x43**2*m.x46*m.x47*m.x48 - m.x40*
                         m.x41*m.x42*m.x45*m.x46*m.x47**2 - 3*m.x40*m.x41*m.x43*m.x45*m.x46**2*m.x47 - 2*m.x40**2*m.x43*
                         m.x44*m.x47**3 - m.x40**2*m.x42*m.x45*m.x47**3 - 3*m.x40**2*m.x41*m.x46*m.x47**3 + 2*m.x40**2*
                         m.x43**2*m.x47**2*m.x48 - m.x40**2*m.x45**3*m.x46*m.x47 + m.x42**2*m.x40*m.x43*m.x47**3 + m.x43
                         **2*m.x40*m.x44**2*m.x47**2 + m.x43**3*m.x40*m.x46**2*m.x47 - 2*m.x41**3*m.x44*m.x45*m.x48**2
                          + m.x40**3*m.x47**4 + 3*m.x41**3*m.x44*m.x46*m.x47*m.x48 - 3*m.x41**3*m.x42*m.x47*m.x48**2 + 
                         m.x41**2*m.x43**2*m.x44*m.x48**2 + 3*m.x41**2*m.x42**2*m.x47**2*m.x48 + m.x41**2*m.x44**2*m.x45
                         **2*m.x48 - m.x41*m.x42*m.x43**3*m.x48**2 + m.x41**3*m.x45*m.x46**2*m.x48 - m.x41**3*m.x47*
                         m.x46**3 + (m.x43**3*m.x40*m.x46 - m.x41*m.x42*m.x43**2*m.x46 - m.x43**2*m.x40*m.x44*m.x45 - 3*
                         m.x40*m.x41*m.x43*m.x45*m.x46 + m.x41**2*m.x43*m.x46*m.x44 + m.x41*m.x42*m.x43*m.x44*m.x45 + 
                         m.x40*m.x42*m.x43*m.x45**2 - m.x41**3*m.x46**2 + 2*m.x41**2*m.x42*m.x45*m.x46 - m.x41**2*m.x44
                         **2*m.x45 - m.x42**2*m.x41*m.x45**2 + 2*m.x40*m.x41*m.x44*m.x45**2 - m.x40**2*m.x45**3)*(1 - 
                         m.b167) + (m.x41*m.x42*m.x43 - m.x41**2*m.x44 - m.x43**2*m.x40)*(1 - m.b165) - 1E-5*m.b163
                          >= 0)
