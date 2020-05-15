#  MINLP written by GAMS Convert at 05/15/20 00:50:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        218       25      192        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        101       41       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        545      505       40        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,1.6094379124341),initialize=0)
m.x13 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x14 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x15 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x16 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x17 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x18 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x19 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x20 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x21 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x22 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x23 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x24 = Var(within=Reals,bounds=(5.7037824746562,8.00636756765025),initialize=5.7037824746562)
m.x25 = Var(within=Reals,bounds=(4.89920702407788,5.93950480817727),initialize=4.89920702407788)
m.x26 = Var(within=Reals,bounds=(4.2094573693226,6.78259213602813),initialize=4.2094573693226)
m.x27 = Var(within=Reals,bounds=(4.8436620142491,6.4803112641552),initialize=4.8436620142491)
m.x28 = Var(within=Reals,bounds=(3.49701248447645,6.45880505893423),initialize=3.49701248447645)
m.x29 = Var(within=Reals,bounds=(4.2336716274432,6.50229017087397),initialize=4.2336716274432)
m.x30 = Var(within=Reals,bounds=(3.62545142726039,6.08944495546819),initialize=3.62545142726039)
m.x31 = Var(within=Reals,bounds=(3.74336763939801,6.35770894206286),initialize=3.74336763939801)
m.x32 = Var(within=Reals,bounds=(3.03415138345794,7.21791020728598),initialize=3.03415138345794)
m.x33 = Var(within=Reals,bounds=(0.506817602368452,2.11625551480255),initialize=0.506817602368452)
m.x34 = Var(within=Reals,bounds=(0.307484699747961,1.91692261218206),initialize=0.307484699747961)
m.x35 = Var(within=Reals,bounds=(0.867100487683383,2.47653840011748),initialize=0.867100487683383)
m.x36 = Var(within=Reals,bounds=(-0.356674943938732,1.25276296849537),initialize=-0.356674943938732)
m.x37 = Var(within=Reals,bounds=(0.131028262406404,1.7404661748405),initialize=0.131028262406404)
m.x38 = Var(within=Reals,bounds=(-0.162518929497775,1.44691898293633),initialize=-0.162518929497775)
m.x39 = Var(within=Reals,bounds=(-0.127833371509885,1.48160454092422),initialize=-0.127833371509885)
m.x40 = Var(within=Reals,bounds=(-0.150822889734584,1.45861502269952),initialize=-0.150822889734584)
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
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=250*exp(m.x1 + 0.6*m.x13) + 550*exp(m.x2 + 0.6*m.x14) + 250*exp(m.x3 + 0.6*m.x15) + 1000*exp(m.x4
                        + 0.6*m.x16) + 300*exp(m.x5 + 0.6*m.x17) + 800*exp(m.x6 + 0.6*m.x18) + 200*exp(m.x7 + 0.6*m.x19)
                        + 1200*exp(m.x8 + 0.6*m.x20) + 250*exp(m.x9 + 0.6*m.x21) + 250*exp(m.x10 + 0.6*m.x22) + 450*exp(
                       m.x11 + 0.6*m.x23) + 700*exp(m.x12 + 0.6*m.x24), sense=minimize)

m.c2 = Constraint(expr=   m.x13 - m.x25 >= 2.06686275947298)

m.c3 = Constraint(expr=   m.x14 - m.x25 >= 0.693147180559945)

m.c4 = Constraint(expr=   m.x15 - m.x25 >= 1.64865862558738)

m.c5 = Constraint(expr=   m.x16 - m.x25 >= 1.58923520511658)

m.c6 = Constraint(expr=   m.x17 - m.x25 >= 1.80828877117927)

m.c7 = Constraint(expr=   m.x18 - m.x25 >= 1.43508452528932)

m.c8 = Constraint(expr=   m.x19 - m.x25 >= 1.02961941718116)

m.c9 = Constraint(expr=   m.x20 - m.x25 >= 1.19392246847243)

m.c10 = Constraint(expr=   m.x21 - m.x25 >= 1.41098697371026)

m.c11 = Constraint(expr=   m.x22 - m.x25 >= 1.33500106673234)

m.c12 = Constraint(expr=   m.x23 - m.x25 >= 1.02961941718116)

m.c13 = Constraint(expr=   m.x24 - m.x25 >= 1.3609765531356)

m.c14 = Constraint(expr=   m.x13 - m.x26 >= -0.356674943938732)

m.c15 = Constraint(expr=   m.x14 - m.x26 >= -0.22314355131421)

m.c16 = Constraint(expr=   m.x15 - m.x26 >= -0.105360515657826)

m.c17 = Constraint(expr=   m.x16 - m.x26 >= 1.22377543162212)

m.c18 = Constraint(expr=   m.x17 - m.x26 >= 0.741937344729377)

m.c19 = Constraint(expr=   m.x18 - m.x26 >= 0.916290731874155)

m.c20 = Constraint(expr=   m.x19 - m.x26 >= 1.19392246847243)

m.c21 = Constraint(expr=   m.x20 - m.x26 >= 1.09861228866811)

m.c22 = Constraint(expr=   m.x21 - m.x26 >= 0.993251773010283)

m.c23 = Constraint(expr=   m.x22 - m.x26 >= 0.8754687373539)

m.c24 = Constraint(expr=   m.x23 - m.x26 >= 0.78845736036427)

m.c25 = Constraint(expr=   m.x24 - m.x26 >= 1.1314021114911)

m.c26 = Constraint(expr=   m.x13 - m.x27 >= -0.356674943938732)

m.c27 = Constraint(expr=   m.x14 - m.x27 >= 0.955511445027436)

m.c28 = Constraint(expr=   m.x15 - m.x27 >= 0.470003629245736)

m.c29 = Constraint(expr=   m.x16 - m.x27 >= 1.28093384546206)

m.c30 = Constraint(expr=   m.x17 - m.x27 >= 1.16315080980568)

m.c31 = Constraint(expr=   m.x18 - m.x27 >= 1.06471073699243)

m.c32 = Constraint(expr=   m.x19 - m.x27 >= 0.955511445027436)

m.c33 = Constraint(expr=   m.x20 - m.x27 >= 0.78845736036427)

m.c34 = Constraint(expr=   m.x21 - m.x27 >= 1.52605630349505)

m.c35 = Constraint(expr=   m.x22 - m.x27 >= 1.45861502269952)

m.c36 = Constraint(expr=   m.x23 - m.x27 >= 1.43508452528932)

m.c37 = Constraint(expr=   m.x24 - m.x27 >= 1.52605630349505)

m.c38 = Constraint(expr=   m.x13 - m.x28 >= 1.54756250871601)

m.c39 = Constraint(expr=   m.x14 - m.x28 >= 0.832909122935104)

m.c40 = Constraint(expr=   m.x15 - m.x28 >= 0.470003629245736)

m.c41 = Constraint(expr=   m.x16 - m.x28 >= 0.993251773010283)

m.c42 = Constraint(expr=   m.x17 - m.x28 >= 0.182321556793955)

m.c43 = Constraint(expr=   m.x18 - m.x28 >= 0.916290731874155)

m.c44 = Constraint(expr=   m.x19 - m.x28 >= 0.405465108108164)

m.c45 = Constraint(expr=   m.x20 - m.x28 >= 0.405465108108164)

m.c46 = Constraint(expr=   m.x21 - m.x28 >= 0.262364264467491)

m.c47 = Constraint(expr=   m.x22 - m.x28 >= 0.53062825106217)

m.c48 = Constraint(expr=   m.x23 - m.x28 >= 0.405465108108164)

m.c49 = Constraint(expr=   m.x24 - m.x28 >= 0.587786664902119)

m.c50 = Constraint(expr=   m.x13 - m.x29 >= 0.182321556793955)

m.c51 = Constraint(expr=   m.x14 - m.x29 >= 1.28093384546206)

m.c52 = Constraint(expr=   m.x15 - m.x29 >= 0.8754687373539)

m.c53 = Constraint(expr=   m.x16 - m.x29 >= 1.50407739677627)

m.c54 = Constraint(expr=   m.x17 - m.x29 >= 0.470003629245736)

m.c55 = Constraint(expr=   m.x18 - m.x29 >= 0.741937344729377)

m.c56 = Constraint(expr=   m.x19 - m.x29 >= 0.8754687373539)

m.c57 = Constraint(expr=   m.x20 - m.x29 >= 0.993251773010283)

m.c58 = Constraint(expr=   m.x21 - m.x29 >= 1.02961941718116)

m.c59 = Constraint(expr=   m.x22 - m.x29 >= 1.25276296849537)

m.c60 = Constraint(expr=   m.x23 - m.x29 >= 1.25276296849537)

m.c61 = Constraint(expr=   m.x24 - m.x29 >= 1.45861502269952)

m.c62 = Constraint(expr=   m.x13 - m.x30 >= -0.356674943938732)

m.c63 = Constraint(expr=   m.x14 - m.x30 >= 0.8754687373539)

m.c64 = Constraint(expr=   m.x15 - m.x30 >= 1.1314021114911)

m.c65 = Constraint(expr=   m.x16 - m.x30 >= 0.78845736036427)

m.c66 = Constraint(expr=   m.x17 - m.x30 >= 1.30833281965018)

m.c67 = Constraint(expr=   m.x18 - m.x30 >= 1.56861591791385)

m.c68 = Constraint(expr=   m.x19 - m.x30 >= 1.50407739677627)

m.c69 = Constraint(expr=   m.x20 - m.x30 >= 1.64865862558738)

m.c70 = Constraint(expr=   m.x21 - m.x30 >= 1.85629799036563)

m.c71 = Constraint(expr=   m.x22 - m.x30 >= 1.7404661748405)

m.c72 = Constraint(expr=   m.x23 - m.x30 >= 1.85629799036563)

m.c73 = Constraint(expr=   m.x24 - m.x30 >= 1.91692261218206)

m.c74 = Constraint(expr=   m.x13 - m.x31 >= 0.832909122935104)

m.c75 = Constraint(expr=   m.x14 - m.x31 >= 1.54756250871601)

m.c76 = Constraint(expr=   m.x15 - m.x31 >= 1.64865862558738)

m.c77 = Constraint(expr=   m.x16 - m.x31 >= 1.25276296849537)

m.c78 = Constraint(expr=   m.x17 - m.x31 >= 1.06471073699243)

m.c79 = Constraint(expr=   m.x18 - m.x31 >= 1.28093384546206)

m.c80 = Constraint(expr=   m.x19 - m.x31 >= 1.19392246847243)

m.c81 = Constraint(expr=   m.x20 - m.x31 >= 1.16315080980568)

m.c82 = Constraint(expr=   m.x21 - m.x31 >= 1.41098697371026)

m.c83 = Constraint(expr=   m.x22 - m.x31 >= 1.30833281965018)

m.c84 = Constraint(expr=   m.x23 - m.x31 >= 1.22377543162212)

m.c85 = Constraint(expr=   m.x24 - m.x31 >= 1.30833281965018)

m.c86 = Constraint(expr=   m.x13 - m.x32 >= -0.916290731874155)

m.c87 = Constraint(expr=   m.x14 - m.x32 >= -0.105360515657826)

m.c88 = Constraint(expr=   m.x15 - m.x32 >= 0.0953101798043249)

m.c89 = Constraint(expr=   m.x16 - m.x32 >= 0.336472236621213)

m.c90 = Constraint(expr=   m.x17 - m.x32 >= 0.470003629245736)

m.c91 = Constraint(expr=   m.x18 - m.x32 >= 0.78845736036427)

m.c92 = Constraint(expr=   m.x19 - m.x32 >= 0.693147180559945)

m.c93 = Constraint(expr=   m.x20 - m.x32 >= 0.587786664902119)

m.c94 = Constraint(expr=   m.x21 - m.x32 >= 0.587786664902119)

m.c95 = Constraint(expr=   m.x22 - m.x32 >= 0.470003629245736)

m.c96 = Constraint(expr=   m.x23 - m.x32 >= 0.587786664902119)

m.c97 = Constraint(expr=   m.x24 - m.x32 >= 0.693147180559945)

m.c98 = Constraint(expr=   m.x1 + m.x33 >= 1.85629799036563)

m.c99 = Constraint(expr=   m.x2 + m.x33 >= 1.54756250871601)

m.c100 = Constraint(expr=   m.x3 + m.x33 >= 2.11625551480255)

m.c101 = Constraint(expr=   m.x4 + m.x33 >= 1.3609765531356)

m.c102 = Constraint(expr=   m.x5 + m.x33 >= 0.741937344729377)

m.c103 = Constraint(expr=   m.x6 + m.x33 >= 0.182321556793955)

m.c104 = Constraint(expr=   m.x7 + m.x33 >= -0.22314355131421)

m.c105 = Constraint(expr=   m.x8 + m.x33 >= 0.78845736036427)

m.c106 = Constraint(expr=   m.x9 + m.x33 >= 0.182321556793955)

m.c107 = Constraint(expr=   m.x10 + m.x33 >= 0.916290731874155)

m.c108 = Constraint(expr=   m.x11 + m.x33 >= 1.22377543162212)

m.c109 = Constraint(expr=   m.x12 + m.x33 >= 1.33500106673234)

m.c110 = Constraint(expr=   m.x1 + m.x34 >= 1.91692261218206)

m.c111 = Constraint(expr=   m.x2 + m.x34 >= 1.85629799036563)

m.c112 = Constraint(expr=   m.x3 + m.x34 >= 1.87180217690159)

m.c113 = Constraint(expr=   m.x4 + m.x34 >= 1.48160454092422)

m.c114 = Constraint(expr=   m.x5 + m.x34 >= 0.832909122935104)

m.c115 = Constraint(expr=   m.x6 + m.x34 >= 1.16315080980568)

m.c116 = Constraint(expr=   m.x7 + m.x34 >= -0.916290731874155)

m.c117 = Constraint(expr=   m.x8 + m.x34 >= -1.6094379124341)

m.c118 = Constraint(expr=   m.x9 + m.x34 >= -0.693147180559945)

m.c119 = Constraint(expr=   m.x10 + m.x34 >= 1.19392246847243)

m.c120 = Constraint(expr=   m.x11 + m.x34 >= -0.510825623765991)

m.c121 = Constraint(expr=   m.x12 + m.x34 >= 0.182321556793955)

m.c122 = Constraint(expr=   m.x1 + m.x35 >= 0)

m.c123 = Constraint(expr=   m.x2 + m.x35 >= 1.84054963339749)

m.c124 = Constraint(expr=   m.x3 + m.x35 >= 1.68639895357023)

m.c125 = Constraint(expr=   m.x4 + m.x35 >= 2.47653840011748)

m.c126 = Constraint(expr=   m.x5 + m.x35 >= 1.7404661748405)

m.c127 = Constraint(expr=   m.x6 + m.x35 >= 1.82454929205105)

m.c128 = Constraint(expr=   m.x7 + m.x35 >= 0.0953101798043249)

m.c129 = Constraint(expr=   m.x8 + m.x35 >= -0.510825623765991)

m.c130 = Constraint(expr=   m.x9 + m.x35 >= 0.182321556793955)

m.c131 = Constraint(expr=   m.x10 + m.x35 >= 1.45861502269952)

m.c132 = Constraint(expr=   m.x11 + m.x35 >= 1.02961941718116)

m.c133 = Constraint(expr=   m.x12 + m.x35 >= 1.64865862558738)

m.c134 = Constraint(expr=   m.x1 + m.x36 >= 1.16315080980568)

m.c135 = Constraint(expr=   m.x2 + m.x36 >= 1.09861228866811)

m.c136 = Constraint(expr=   m.x3 + m.x36 >= 1.25276296849537)

m.c137 = Constraint(expr=   m.x4 + m.x36 >= 1.19392246847243)

m.c138 = Constraint(expr=   m.x5 + m.x36 >= 1.02961941718116)

m.c139 = Constraint(expr=   m.x6 + m.x36 >= 1.22377543162212)

m.c140 = Constraint(expr=   m.x7 + m.x36 >= 0.53062825106217)

m.c141 = Constraint(expr=   m.x8 + m.x36 >= -0.105360515657826)

m.c142 = Constraint(expr=   m.x9 + m.x36 >= 0.78845736036427)

m.c143 = Constraint(expr=   m.x10 + m.x36 >= 0.765467842139571)

m.c144 = Constraint(expr=   m.x11 + m.x36 >= 0.587786664902119)

m.c145 = Constraint(expr=   m.x12 + m.x36 >= 0.916290731874155)

m.c146 = Constraint(expr=   m.x1 + m.x37 >= 0.741937344729377)

m.c147 = Constraint(expr=   m.x2 + m.x37 >= 0.916290731874155)

m.c148 = Constraint(expr=   m.x3 + m.x37 >= 1.43508452528932)

m.c149 = Constraint(expr=   m.x4 + m.x37 >= 1.28093384546206)

m.c150 = Constraint(expr=   m.x5 + m.x37 >= 1.7404661748405)

m.c151 = Constraint(expr=   m.x6 + m.x37 >= 0.78845736036427)

m.c152 = Constraint(expr=   m.x7 + m.x37 >= 0.182321556793955)

m.c153 = Constraint(expr=   m.x8 + m.x37 >= -0.510825623765991)

m.c154 = Constraint(expr=   m.x9 + m.x37 >= 0.139761942375159)

m.c155 = Constraint(expr=   m.x10 + m.x37 >= 1.1314021114911)

m.c156 = Constraint(expr=   m.x11 + m.x37 >= 1.43508452528932)

m.c157 = Constraint(expr=   m.x12 + m.x37 >= 0.470003629245736)

m.c158 = Constraint(expr=   m.x1 + m.x38 >= 0.0953101798043249)

m.c159 = Constraint(expr=   m.x2 + m.x38 >= -0.22314355131421)

m.c160 = Constraint(expr=   m.x3 + m.x38 >= -0.916290731874155)

m.c161 = Constraint(expr=   m.x4 + m.x38 >= 0.0953101798043249)

m.c162 = Constraint(expr=   m.x5 + m.x38 >= 0.587786664902119)

m.c163 = Constraint(expr=   m.x6 + m.x38 >= 0.916290731874155)

m.c164 = Constraint(expr=   m.x7 + m.x38 >= -0.693147180559945)

m.c165 = Constraint(expr=   m.x8 + m.x38 >= 0.262364264467491)

m.c166 = Constraint(expr=   m.x9 + m.x38 >= 0.336472236621213)

m.c167 = Constraint(expr=   m.x10 + m.x38 >= 1.44691898293633)

m.c168 = Constraint(expr=   m.x11 + m.x38 >= 0.993251773010283)

m.c169 = Constraint(expr=   m.x12 + m.x38 >= -0.105360515657826)

m.c170 = Constraint(expr=   m.x1 + m.x39 >= 1.43508452528932)

m.c171 = Constraint(expr=   m.x2 + m.x39 >= 1.38629436111989)

m.c172 = Constraint(expr=   m.x3 + m.x39 >= 0.78845736036427)

m.c173 = Constraint(expr=   m.x4 + m.x39 >= -0.693147180559945)

m.c174 = Constraint(expr=   m.x5 + m.x39 >= 1.22377543162212)

m.c175 = Constraint(expr=   m.x6 + m.x39 >= 0.78845736036427)

m.c176 = Constraint(expr=   m.x7 + m.x39 >= 0.336472236621213)

m.c177 = Constraint(expr=   m.x8 + m.x39 >= -0.105360515657826)

m.c178 = Constraint(expr=   m.x9 + m.x39 >= 0.741937344729377)

m.c179 = Constraint(expr=   m.x10 + m.x39 >= 1.48160454092422)

m.c180 = Constraint(expr=   m.x11 + m.x39 >= 0.78845736036427)

m.c181 = Constraint(expr=   m.x12 + m.x39 >= 1.16315080980568)

m.c182 = Constraint(expr=   m.x1 + m.x40 >= 0.993251773010283)

m.c183 = Constraint(expr=   m.x2 + m.x40 >= 1.45861502269952)

m.c184 = Constraint(expr=   m.x3 + m.x40 >= 0.641853886172395)

m.c185 = Constraint(expr=   m.x4 + m.x40 >= 0.693147180559945)

m.c186 = Constraint(expr=   m.x5 + m.x40 >= 0.53062825106217)

m.c187 = Constraint(expr=   m.x6 + m.x40 >= -0.356674943938732)

m.c188 = Constraint(expr=   m.x7 + m.x40 >= -1.20397280432594)

m.c189 = Constraint(expr=   m.x8 + m.x40 >= -1.6094379124341)

m.c190 = Constraint(expr=   m.x9 + m.x40 >= 0.470003629245736)

m.c191 = Constraint(expr=   m.x10 + m.x40 >= 1.25276296849537)

m.c192 = Constraint(expr=   m.x11 + m.x40 >= 1.22377543162212)

m.c193 = Constraint(expr=   m.x12 + m.x40 >= 0.741937344729377)

m.c194 = Constraint(expr=485000*exp(m.x33 - m.x25) + 297000*exp(m.x34 - m.x26) + 320000*exp(m.x35 - m.x27) + 283000*exp(
                         m.x36 - m.x28) + 363000*exp(m.x37 - m.x29) + 265000*exp(m.x38 - m.x30) + 288000*exp(m.x39 - 
                         m.x31) + 145000*exp(m.x40 - m.x32) <= 6000)

m.c195 = Constraint(expr=   m.x1 - 0.693147180559945*m.b53 - 1.09861228866811*m.b65 - 1.38629436111989*m.b77
                          - 1.6094379124341*m.b89 == 0)

m.c196 = Constraint(expr=   m.x2 - 0.693147180559945*m.b54 - 1.09861228866811*m.b66 - 1.38629436111989*m.b78
                          - 1.6094379124341*m.b90 == 0)

m.c197 = Constraint(expr=   m.x3 - 0.693147180559945*m.b55 - 1.09861228866811*m.b67 - 1.38629436111989*m.b79
                          - 1.6094379124341*m.b91 == 0)

m.c198 = Constraint(expr=   m.x4 - 0.693147180559945*m.b56 - 1.09861228866811*m.b68 - 1.38629436111989*m.b80
                          - 1.6094379124341*m.b92 == 0)

m.c199 = Constraint(expr=   m.x5 - 0.693147180559945*m.b57 - 1.09861228866811*m.b69 - 1.38629436111989*m.b81
                          - 1.6094379124341*m.b93 == 0)

m.c200 = Constraint(expr=   m.x6 - 0.693147180559945*m.b58 - 1.09861228866811*m.b70 - 1.38629436111989*m.b82
                          - 1.6094379124341*m.b94 == 0)

m.c201 = Constraint(expr=   m.x7 - 0.693147180559945*m.b59 - 1.09861228866811*m.b71 - 1.38629436111989*m.b83
                          - 1.6094379124341*m.b95 == 0)

m.c202 = Constraint(expr=   m.x8 - 0.693147180559945*m.b60 - 1.09861228866811*m.b72 - 1.38629436111989*m.b84
                          - 1.6094379124341*m.b96 == 0)

m.c203 = Constraint(expr=   m.x9 - 0.693147180559945*m.b61 - 1.09861228866811*m.b73 - 1.38629436111989*m.b85
                          - 1.6094379124341*m.b97 == 0)

m.c204 = Constraint(expr=   m.x10 - 0.693147180559945*m.b62 - 1.09861228866811*m.b74 - 1.38629436111989*m.b86
                          - 1.6094379124341*m.b98 == 0)

m.c205 = Constraint(expr=   m.x11 - 0.693147180559945*m.b63 - 1.09861228866811*m.b75 - 1.38629436111989*m.b87
                          - 1.6094379124341*m.b99 == 0)

m.c206 = Constraint(expr=   m.x12 - 0.693147180559945*m.b64 - 1.09861228866811*m.b76 - 1.38629436111989*m.b88
                          - 1.6094379124341*m.b100 == 0)

m.c207 = Constraint(expr=   m.b41 + m.b53 + m.b65 + m.b77 + m.b89 == 1)

m.c208 = Constraint(expr=   m.b42 + m.b54 + m.b66 + m.b78 + m.b90 == 1)

m.c209 = Constraint(expr=   m.b43 + m.b55 + m.b67 + m.b79 + m.b91 == 1)

m.c210 = Constraint(expr=   m.b44 + m.b56 + m.b68 + m.b80 + m.b92 == 1)

m.c211 = Constraint(expr=   m.b45 + m.b57 + m.b69 + m.b81 + m.b93 == 1)

m.c212 = Constraint(expr=   m.b46 + m.b58 + m.b70 + m.b82 + m.b94 == 1)

m.c213 = Constraint(expr=   m.b47 + m.b59 + m.b71 + m.b83 + m.b95 == 1)

m.c214 = Constraint(expr=   m.b48 + m.b60 + m.b72 + m.b84 + m.b96 == 1)

m.c215 = Constraint(expr=   m.b49 + m.b61 + m.b73 + m.b85 + m.b97 == 1)

m.c216 = Constraint(expr=   m.b50 + m.b62 + m.b74 + m.b86 + m.b98 == 1)

m.c217 = Constraint(expr=   m.b51 + m.b63 + m.b75 + m.b87 + m.b99 == 1)

m.c218 = Constraint(expr=   m.b52 + m.b64 + m.b76 + m.b88 + m.b100 == 1)
