#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        206       13      192        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         77       41       36        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        473      241      232        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x2 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x3 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x4 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x5 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x6 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x7 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x8 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x9 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x10 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x11 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x12 = Var(within=Reals,bounds=(1,5),initialize=1)
m.x13 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x14 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x15 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x16 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x17 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x18 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x19 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x20 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x21 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x22 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x23 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x24 = Var(within=Reals,bounds=(300,3000),initialize=300)
m.x25 = Var(within=Reals,bounds=(134.183333333333,379.746835443038),initialize=134.183333333333)
m.x26 = Var(within=Reals,bounds=(67.32,882.352941176471),initialize=67.32)
m.x27 = Var(within=Reals,bounds=(126.933333333333,652.173913043478),initialize=126.933333333333)
m.x28 = Var(within=Reals,bounds=(33.0166666666667,638.297872340426),initialize=33.0166666666667)
m.x29 = Var(within=Reals,bounds=(68.97,666.666666666667),initialize=68.97)
m.x30 = Var(within=Reals,bounds=(37.5416666666667,441.176470588235),initialize=37.5416666666667)
m.x31 = Var(within=Reals,bounds=(42.24,576.923076923077),initialize=42.24)
m.x32 = Var(within=Reals,bounds=(20.7833333333333,1363.63636363636),initialize=20.7833333333333)
m.x33 = Var(within=Reals,bounds=(1.66,8.3),initialize=1.66)
m.x34 = Var(within=Reals,bounds=(1.36,6.8),initialize=1.36)
m.x35 = Var(within=Reals,bounds=(2.38,11.9),initialize=2.38)
m.x36 = Var(within=Reals,bounds=(0.7,3.5),initialize=0.7)
m.x37 = Var(within=Reals,bounds=(1.14,5.7),initialize=1.14)
m.x38 = Var(within=Reals,bounds=(0.85,4.25),initialize=0.85)
m.x39 = Var(within=Reals,bounds=(0.88,4.4),initialize=0.88)
m.x40 = Var(within=Reals,bounds=(0.86,4.3),initialize=0.86)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b47 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b48 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b49 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b52 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b53 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b54 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b55 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b56 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b57 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b58 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b59 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b60 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b61 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b62 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b63 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b64 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b65 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=250*m.x13**0.6*m.x1 + 550*m.x14**0.6*m.x2 + 250*m.x15**0.6*m.x3 + 1000*m.x16**0.6*m.x4 + 300*
                       m.x17**0.6*m.x5 + 800*m.x18**0.6*m.x6 + 200*m.x19**0.6*m.x7 + 1200*m.x20**0.6*m.x8 + 250*m.x21**
                       0.6*m.x9 + 250*m.x22**0.6*m.x10 + 450*m.x23**0.6*m.x11 + 700*m.x24**0.6*m.x12, sense=minimize)

m.c2 = Constraint(expr=   m.x13 - 7.9*m.x25 >= 0)

m.c3 = Constraint(expr=   m.x14 - 2*m.x25 >= 0)

m.c4 = Constraint(expr=   m.x15 - 5.2*m.x25 >= 0)

m.c5 = Constraint(expr=   m.x16 - 4.9*m.x25 >= 0)

m.c6 = Constraint(expr=   m.x17 - 6.1*m.x25 >= 0)

m.c7 = Constraint(expr=   m.x18 - 4.2*m.x25 >= 0)

m.c8 = Constraint(expr=   m.x19 - 2.8*m.x25 >= 0)

m.c9 = Constraint(expr=   m.x20 - 3.3*m.x25 >= 0)

m.c10 = Constraint(expr=   m.x21 - 4.1*m.x25 >= 0)

m.c11 = Constraint(expr=   m.x22 - 3.8*m.x25 >= 0)

m.c12 = Constraint(expr=   m.x23 - 2.8*m.x25 >= 0)

m.c13 = Constraint(expr=   m.x24 - 3.9*m.x25 >= 0)

m.c14 = Constraint(expr=   m.x13 - 0.7*m.x26 >= 0)

m.c15 = Constraint(expr=   m.x14 - 0.8*m.x26 >= 0)

m.c16 = Constraint(expr=   m.x15 - 0.9*m.x26 >= 0)

m.c17 = Constraint(expr=   m.x16 - 3.4*m.x26 >= 0)

m.c18 = Constraint(expr=   m.x17 - 2.1*m.x26 >= 0)

m.c19 = Constraint(expr=   m.x18 - 2.5*m.x26 >= 0)

m.c20 = Constraint(expr=   m.x19 - 3.3*m.x26 >= 0)

m.c21 = Constraint(expr=   m.x20 - 3*m.x26 >= 0)

m.c22 = Constraint(expr=   m.x21 - 2.7*m.x26 >= 0)

m.c23 = Constraint(expr=   m.x22 - 2.4*m.x26 >= 0)

m.c24 = Constraint(expr=   m.x23 - 2.2*m.x26 >= 0)

m.c25 = Constraint(expr=   m.x24 - 3.1*m.x26 >= 0)

m.c26 = Constraint(expr=   m.x13 - 0.7*m.x27 >= 0)

m.c27 = Constraint(expr=   m.x14 - 2.6*m.x27 >= 0)

m.c28 = Constraint(expr=   m.x15 - 1.6*m.x27 >= 0)

m.c29 = Constraint(expr=   m.x16 - 3.6*m.x27 >= 0)

m.c30 = Constraint(expr=   m.x17 - 3.2*m.x27 >= 0)

m.c31 = Constraint(expr=   m.x18 - 2.9*m.x27 >= 0)

m.c32 = Constraint(expr=   m.x19 - 2.6*m.x27 >= 0)

m.c33 = Constraint(expr=   m.x20 - 2.2*m.x27 >= 0)

m.c34 = Constraint(expr=   m.x21 - 4.6*m.x27 >= 0)

m.c35 = Constraint(expr=   m.x22 - 4.3*m.x27 >= 0)

m.c36 = Constraint(expr=   m.x23 - 4.2*m.x27 >= 0)

m.c37 = Constraint(expr=   m.x24 - 4.6*m.x27 >= 0)

m.c38 = Constraint(expr=   m.x13 - 4.7*m.x28 >= 0)

m.c39 = Constraint(expr=   m.x14 - 2.3*m.x28 >= 0)

m.c40 = Constraint(expr=   m.x15 - 1.6*m.x28 >= 0)

m.c41 = Constraint(expr=   m.x16 - 2.7*m.x28 >= 0)

m.c42 = Constraint(expr=   m.x17 - 1.2*m.x28 >= 0)

m.c43 = Constraint(expr=   m.x18 - 2.5*m.x28 >= 0)

m.c44 = Constraint(expr=   m.x19 - 1.5*m.x28 >= 0)

m.c45 = Constraint(expr=   m.x20 - 1.5*m.x28 >= 0)

m.c46 = Constraint(expr=   m.x21 - 1.3*m.x28 >= 0)

m.c47 = Constraint(expr=   m.x22 - 1.7*m.x28 >= 0)

m.c48 = Constraint(expr=   m.x23 - 1.5*m.x28 >= 0)

m.c49 = Constraint(expr=   m.x24 - 1.8*m.x28 >= 0)

m.c50 = Constraint(expr=   m.x13 - 1.2*m.x29 >= 0)

m.c51 = Constraint(expr=   m.x14 - 3.6*m.x29 >= 0)

m.c52 = Constraint(expr=   m.x15 - 2.4*m.x29 >= 0)

m.c53 = Constraint(expr=   m.x16 - 4.5*m.x29 >= 0)

m.c54 = Constraint(expr=   m.x17 - 1.6*m.x29 >= 0)

m.c55 = Constraint(expr=   m.x18 - 2.1*m.x29 >= 0)

m.c56 = Constraint(expr=   m.x19 - 2.4*m.x29 >= 0)

m.c57 = Constraint(expr=   m.x20 - 2.7*m.x29 >= 0)

m.c58 = Constraint(expr=   m.x21 - 2.8*m.x29 >= 0)

m.c59 = Constraint(expr=   m.x22 - 3.5*m.x29 >= 0)

m.c60 = Constraint(expr=   m.x23 - 3.5*m.x29 >= 0)

m.c61 = Constraint(expr=   m.x24 - 4.3*m.x29 >= 0)

m.c62 = Constraint(expr=   m.x13 - 0.7*m.x30 >= 0)

m.c63 = Constraint(expr=   m.x14 - 2.4*m.x30 >= 0)

m.c64 = Constraint(expr=   m.x15 - 3.1*m.x30 >= 0)

m.c65 = Constraint(expr=   m.x16 - 2.2*m.x30 >= 0)

m.c66 = Constraint(expr=   m.x17 - 3.7*m.x30 >= 0)

m.c67 = Constraint(expr=   m.x18 - 4.8*m.x30 >= 0)

m.c68 = Constraint(expr=   m.x19 - 4.5*m.x30 >= 0)

m.c69 = Constraint(expr=   m.x20 - 5.2*m.x30 >= 0)

m.c70 = Constraint(expr=   m.x21 - 6.4*m.x30 >= 0)

m.c71 = Constraint(expr=   m.x22 - 5.7*m.x30 >= 0)

m.c72 = Constraint(expr=   m.x23 - 6.4*m.x30 >= 0)

m.c73 = Constraint(expr=   m.x24 - 6.8*m.x30 >= 0)

m.c74 = Constraint(expr=   m.x13 - 2.3*m.x31 >= 0)

m.c75 = Constraint(expr=   m.x14 - 4.7*m.x31 >= 0)

m.c76 = Constraint(expr=   m.x15 - 5.2*m.x31 >= 0)

m.c77 = Constraint(expr=   m.x16 - 3.5*m.x31 >= 0)

m.c78 = Constraint(expr=   m.x17 - 2.9*m.x31 >= 0)

m.c79 = Constraint(expr=   m.x18 - 3.6*m.x31 >= 0)

m.c80 = Constraint(expr=   m.x19 - 3.3*m.x31 >= 0)

m.c81 = Constraint(expr=   m.x20 - 3.2*m.x31 >= 0)

m.c82 = Constraint(expr=   m.x21 - 4.1*m.x31 >= 0)

m.c83 = Constraint(expr=   m.x22 - 3.7*m.x31 >= 0)

m.c84 = Constraint(expr=   m.x23 - 3.4*m.x31 >= 0)

m.c85 = Constraint(expr=   m.x24 - 3.7*m.x31 >= 0)

m.c86 = Constraint(expr=   m.x13 - 0.4*m.x32 >= 0)

m.c87 = Constraint(expr=   m.x14 - 0.9*m.x32 >= 0)

m.c88 = Constraint(expr=   m.x15 - 1.1*m.x32 >= 0)

m.c89 = Constraint(expr=   m.x16 - 1.4*m.x32 >= 0)

m.c90 = Constraint(expr=   m.x17 - 1.6*m.x32 >= 0)

m.c91 = Constraint(expr=   m.x18 - 2.2*m.x32 >= 0)

m.c92 = Constraint(expr=   m.x19 - 2*m.x32 >= 0)

m.c93 = Constraint(expr=   m.x20 - 1.8*m.x32 >= 0)

m.c94 = Constraint(expr=   m.x21 - 1.8*m.x32 >= 0)

m.c95 = Constraint(expr=   m.x22 - 1.6*m.x32 >= 0)

m.c96 = Constraint(expr=   m.x23 - 1.8*m.x32 >= 0)

m.c97 = Constraint(expr=   m.x24 - 2*m.x32 >= 0)

m.c98 = Constraint(expr=m.x1*m.x33 >= 6.4)

m.c99 = Constraint(expr=m.x2*m.x33 >= 4.7)

m.c100 = Constraint(expr=m.x3*m.x33 >= 8.3)

m.c101 = Constraint(expr=m.x4*m.x33 >= 3.9)

m.c102 = Constraint(expr=m.x5*m.x33 >= 2.1)

m.c103 = Constraint(expr=m.x6*m.x33 >= 1.2)

m.c104 = Constraint(expr=m.x7*m.x33 >= 0.8)

m.c105 = Constraint(expr=m.x8*m.x33 >= 2.2)

m.c106 = Constraint(expr=m.x9*m.x33 >= 1.2)

m.c107 = Constraint(expr=m.x10*m.x33 >= 2.5)

m.c108 = Constraint(expr=m.x11*m.x33 >= 3.4)

m.c109 = Constraint(expr=m.x12*m.x33 >= 3.8)

m.c110 = Constraint(expr=m.x1*m.x34 >= 6.8)

m.c111 = Constraint(expr=m.x2*m.x34 >= 6.4)

m.c112 = Constraint(expr=m.x3*m.x34 >= 6.5)

m.c113 = Constraint(expr=m.x4*m.x34 >= 4.4)

m.c114 = Constraint(expr=m.x5*m.x34 >= 2.3)

m.c115 = Constraint(expr=m.x6*m.x34 >= 3.2)

m.c116 = Constraint(expr=m.x7*m.x34 >= 0.4)

m.c117 = Constraint(expr=m.x8*m.x34 >= 0.2)

m.c118 = Constraint(expr=m.x9*m.x34 >= 0.5)

m.c119 = Constraint(expr=m.x10*m.x34 >= 3.3)

m.c120 = Constraint(expr=m.x11*m.x34 >= 0.6)

m.c121 = Constraint(expr=m.x12*m.x34 >= 1.2)

m.c122 = Constraint(expr=m.x1*m.x35 >= 1)

m.c123 = Constraint(expr=m.x2*m.x35 >= 6.3)

m.c124 = Constraint(expr=m.x3*m.x35 >= 5.4)

m.c125 = Constraint(expr=m.x4*m.x35 >= 11.9)

m.c126 = Constraint(expr=m.x5*m.x35 >= 5.7)

m.c127 = Constraint(expr=m.x6*m.x35 >= 6.2)

m.c128 = Constraint(expr=m.x7*m.x35 >= 1.1)

m.c129 = Constraint(expr=m.x8*m.x35 >= 0.6)

m.c130 = Constraint(expr=m.x9*m.x35 >= 1.2)

m.c131 = Constraint(expr=m.x10*m.x35 >= 4.3)

m.c132 = Constraint(expr=m.x11*m.x35 >= 2.8)

m.c133 = Constraint(expr=m.x12*m.x35 >= 5.2)

m.c134 = Constraint(expr=m.x1*m.x36 >= 3.2)

m.c135 = Constraint(expr=m.x2*m.x36 >= 3)

m.c136 = Constraint(expr=m.x3*m.x36 >= 3.5)

m.c137 = Constraint(expr=m.x4*m.x36 >= 3.3)

m.c138 = Constraint(expr=m.x5*m.x36 >= 2.8)

m.c139 = Constraint(expr=m.x6*m.x36 >= 3.4)

m.c140 = Constraint(expr=m.x7*m.x36 >= 1.7)

m.c141 = Constraint(expr=m.x8*m.x36 >= 0.9)

m.c142 = Constraint(expr=m.x9*m.x36 >= 2.2)

m.c143 = Constraint(expr=m.x10*m.x36 >= 2.15)

m.c144 = Constraint(expr=m.x11*m.x36 >= 1.8)

m.c145 = Constraint(expr=m.x12*m.x36 >= 2.5)

m.c146 = Constraint(expr=m.x1*m.x37 >= 2.1)

m.c147 = Constraint(expr=m.x2*m.x37 >= 2.5)

m.c148 = Constraint(expr=m.x3*m.x37 >= 4.2)

m.c149 = Constraint(expr=m.x4*m.x37 >= 3.6)

m.c150 = Constraint(expr=m.x5*m.x37 >= 5.7)

m.c151 = Constraint(expr=m.x6*m.x37 >= 2.2)

m.c152 = Constraint(expr=m.x7*m.x37 >= 1.2)

m.c153 = Constraint(expr=m.x8*m.x37 >= 0.6)

m.c154 = Constraint(expr=m.x9*m.x37 >= 1.15)

m.c155 = Constraint(expr=m.x10*m.x37 >= 3.1)

m.c156 = Constraint(expr=m.x11*m.x37 >= 4.2)

m.c157 = Constraint(expr=m.x12*m.x37 >= 1.6)

m.c158 = Constraint(expr=m.x1*m.x38 >= 1.1)

m.c159 = Constraint(expr=m.x2*m.x38 >= 0.8)

m.c160 = Constraint(expr=m.x3*m.x38 >= 0.4)

m.c161 = Constraint(expr=m.x4*m.x38 >= 1.1)

m.c162 = Constraint(expr=m.x5*m.x38 >= 1.8)

m.c163 = Constraint(expr=m.x6*m.x38 >= 2.5)

m.c164 = Constraint(expr=m.x7*m.x38 >= 0.5)

m.c165 = Constraint(expr=m.x8*m.x38 >= 1.3)

m.c166 = Constraint(expr=m.x9*m.x38 >= 1.4)

m.c167 = Constraint(expr=m.x10*m.x38 >= 4.25)

m.c168 = Constraint(expr=m.x11*m.x38 >= 2.7)

m.c169 = Constraint(expr=m.x12*m.x38 >= 0.9)

m.c170 = Constraint(expr=m.x1*m.x39 >= 4.2)

m.c171 = Constraint(expr=m.x2*m.x39 >= 4)

m.c172 = Constraint(expr=m.x3*m.x39 >= 2.2)

m.c173 = Constraint(expr=m.x4*m.x39 >= 0.5)

m.c174 = Constraint(expr=m.x5*m.x39 >= 3.4)

m.c175 = Constraint(expr=m.x6*m.x39 >= 2.2)

m.c176 = Constraint(expr=m.x7*m.x39 >= 1.4)

m.c177 = Constraint(expr=m.x8*m.x39 >= 0.9)

m.c178 = Constraint(expr=m.x9*m.x39 >= 2.1)

m.c179 = Constraint(expr=m.x10*m.x39 >= 4.4)

m.c180 = Constraint(expr=m.x11*m.x39 >= 2.2)

m.c181 = Constraint(expr=m.x12*m.x39 >= 3.2)

m.c182 = Constraint(expr=m.x1*m.x40 >= 2.7)

m.c183 = Constraint(expr=m.x2*m.x40 >= 4.3)

m.c184 = Constraint(expr=m.x3*m.x40 >= 1.9)

m.c185 = Constraint(expr=m.x4*m.x40 >= 2)

m.c186 = Constraint(expr=m.x5*m.x40 >= 1.7)

m.c187 = Constraint(expr=m.x6*m.x40 >= 0.7)

m.c188 = Constraint(expr=m.x7*m.x40 >= 0.3)

m.c189 = Constraint(expr=m.x8*m.x40 >= 0.2)

m.c190 = Constraint(expr=m.x9*m.x40 >= 1.6)

m.c191 = Constraint(expr=m.x10*m.x40 >= 3.5)

m.c192 = Constraint(expr=m.x11*m.x40 >= 3.4)

m.c193 = Constraint(expr=m.x12*m.x40 >= 2.1)

m.c194 = Constraint(expr=485000*m.x33/m.x25 + 297000*m.x34/m.x26 + 320000*m.x35/m.x27 + 283000*m.x36/m.x28 + 363000*
                         m.x37/m.x29 + 265000*m.x38/m.x30 + 288000*m.x39/m.x31 + 145000*m.x40/m.x32 <= 6000)

m.c195 = Constraint(expr=   m.x1 - m.b41 - 2*m.b53 - 4*m.b65 == 1)

m.c196 = Constraint(expr=   m.x2 - m.b42 - 2*m.b54 - 4*m.b66 == 1)

m.c197 = Constraint(expr=   m.x3 - m.b43 - 2*m.b55 - 4*m.b67 == 1)

m.c198 = Constraint(expr=   m.x4 - m.b44 - 2*m.b56 - 4*m.b68 == 1)

m.c199 = Constraint(expr=   m.x5 - m.b45 - 2*m.b57 - 4*m.b69 == 1)

m.c200 = Constraint(expr=   m.x6 - m.b46 - 2*m.b58 - 4*m.b70 == 1)

m.c201 = Constraint(expr=   m.x7 - m.b47 - 2*m.b59 - 4*m.b71 == 1)

m.c202 = Constraint(expr=   m.x8 - m.b48 - 2*m.b60 - 4*m.b72 == 1)

m.c203 = Constraint(expr=   m.x9 - m.b49 - 2*m.b61 - 4*m.b73 == 1)

m.c204 = Constraint(expr=   m.x10 - m.b50 - 2*m.b62 - 4*m.b74 == 1)

m.c205 = Constraint(expr=   m.x11 - m.b51 - 2*m.b63 - 4*m.b75 == 1)

m.c206 = Constraint(expr=   m.x12 - m.b52 - 2*m.b64 - 4*m.b76 == 1)
