#  MINLP written by GAMS Convert at 05/15/20 00:50:52
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        158        1        0      157        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         87       57       30        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        635      623       12        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0)
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
m.x32 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(2.8,7.4833),initialize=2.8)
m.x63 = Var(within=Reals,bounds=(2,6.3246),initialize=2)
m.x64 = Var(within=Reals,bounds=(1.8,6),initialize=1.8)
m.x65 = Var(within=Reals,bounds=(1.2247,4.899),initialize=1.2247)
m.x66 = Var(within=Reals,bounds=(2,6.3246),initialize=2)
m.x67 = Var(within=Reals,bounds=(5,10),initialize=5)
m.x68 = Var(within=Reals,bounds=(15,15),initialize=15)
m.x69 = Var(within=Reals,bounds=(1.8708,5),initialize=1.8708)
m.x70 = Var(within=Reals,bounds=(1.5811,5),initialize=1.5811)
m.x71 = Var(within=Reals,bounds=(1.5,5),initialize=1.5)
m.x72 = Var(within=Reals,bounds=(1.2247,4.899),initialize=1.2247)
m.x73 = Var(within=Reals,bounds=(1.5811,5),initialize=1.5811)
m.x74 = Var(within=Reals,bounds=(2.5,5),initialize=2.5)
m.x75 = Var(within=Reals,bounds=(5,5),initialize=5)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   2.4*m.x32 + 2.4*m.x33 + 12*m.x50 + 12*m.x51 + 12*m.x58 + 12*m.x59 + 6*m.x60 + 6*m.x61
                       , sense=minimize)

m.c2 = Constraint(expr=   m.x76 - m.x77 <= 0)

m.c3 = Constraint(expr=   0.5*m.x62 - m.x68 + m.x76 <= 0)

m.c4 = Constraint(expr=   0.5*m.x62 - m.x76 <= 0)

m.c5 = Constraint(expr=   0.5*m.x69 - m.x75 + m.x82 <= 0)

m.c6 = Constraint(expr=   0.5*m.x69 - m.x82 <= 0)

m.c7 = Constraint(expr=   0.5*m.x63 - m.x68 + m.x77 <= 0)

m.c8 = Constraint(expr=   0.5*m.x63 - m.x77 <= 0)

m.c9 = Constraint(expr=   0.5*m.x70 - m.x75 + m.x83 <= 0)

m.c10 = Constraint(expr=   0.5*m.x70 - m.x83 <= 0)

m.c11 = Constraint(expr=   0.5*m.x64 - m.x68 + m.x78 <= 0)

m.c12 = Constraint(expr=   0.5*m.x64 - m.x78 <= 0)

m.c13 = Constraint(expr=   0.5*m.x71 - m.x75 + m.x84 <= 0)

m.c14 = Constraint(expr=   0.5*m.x71 - m.x84 <= 0)

m.c15 = Constraint(expr=   0.5*m.x65 - m.x68 + m.x79 <= 0)

m.c16 = Constraint(expr=   0.5*m.x65 - m.x79 <= 0)

m.c17 = Constraint(expr=   0.5*m.x72 - m.x75 + m.x85 <= 0)

m.c18 = Constraint(expr=   0.5*m.x72 - m.x85 <= 0)

m.c19 = Constraint(expr=   0.5*m.x66 - m.x68 + m.x80 <= 0)

m.c20 = Constraint(expr=   0.5*m.x66 - m.x80 <= 0)

m.c21 = Constraint(expr=   0.5*m.x73 - m.x75 + m.x86 <= 0)

m.c22 = Constraint(expr=   0.5*m.x73 - m.x86 <= 0)

m.c23 = Constraint(expr=   0.5*m.x67 - m.x68 + m.x81 <= 0)

m.c24 = Constraint(expr=   0.5*m.x67 - m.x81 <= 0)

m.c25 = Constraint(expr=   0.5*m.x74 - m.x75 + m.x87 <= 0)

m.c26 = Constraint(expr=   0.5*m.x74 - m.x87 <= 0)

m.c27 = Constraint(expr= - m.x32 + m.x76 - m.x77 <= 0)

m.c28 = Constraint(expr= - m.x32 - m.x76 + m.x77 <= 0)

m.c29 = Constraint(expr= - m.x33 + m.x82 - m.x83 <= 0)

m.c30 = Constraint(expr= - m.x33 - m.x82 + m.x83 <= 0)

m.c31 = Constraint(expr= - 15*m.b1 - 15*m.b2 + 0.5*m.x62 + 0.5*m.x63 - m.x76 + m.x77 <= 0)

m.c32 = Constraint(expr= - 15*m.b1 + 15*m.b2 + 0.5*m.x62 + 0.5*m.x63 + m.x76 - m.x77 <= 15)

m.c33 = Constraint(expr=   5*m.b1 - 5*m.b2 + 0.5*m.x69 + 0.5*m.x70 - m.x82 + m.x83 <= 5)

m.c34 = Constraint(expr=   5*m.b1 + 5*m.b2 + 0.5*m.x69 + 0.5*m.x70 + m.x82 - m.x83 <= 10)

m.c35 = Constraint(expr= - m.x34 + m.x76 - m.x78 <= 0)

m.c36 = Constraint(expr= - m.x34 - m.x76 + m.x78 <= 0)

m.c37 = Constraint(expr= - m.x35 + m.x82 - m.x84 <= 0)

m.c38 = Constraint(expr= - m.x35 - m.x82 + m.x84 <= 0)

m.c39 = Constraint(expr= - 15*m.b3 - 15*m.b4 + 0.5*m.x62 + 0.5*m.x64 - m.x76 + m.x78 <= 0)

m.c40 = Constraint(expr= - 15*m.b3 + 15*m.b4 + 0.5*m.x62 + 0.5*m.x64 + m.x76 - m.x78 <= 15)

m.c41 = Constraint(expr=   5*m.b3 - 5*m.b4 + 0.5*m.x69 + 0.5*m.x71 - m.x82 + m.x84 <= 5)

m.c42 = Constraint(expr=   5*m.b3 + 5*m.b4 + 0.5*m.x69 + 0.5*m.x71 + m.x82 - m.x84 <= 10)

m.c43 = Constraint(expr= - m.x36 + m.x76 - m.x79 <= 0)

m.c44 = Constraint(expr= - m.x36 - m.x76 + m.x79 <= 0)

m.c45 = Constraint(expr= - m.x37 + m.x82 - m.x85 <= 0)

m.c46 = Constraint(expr= - m.x37 - m.x82 + m.x85 <= 0)

m.c47 = Constraint(expr= - 15*m.b5 - 15*m.b6 + 0.5*m.x62 + 0.5*m.x65 - m.x76 + m.x79 <= 0)

m.c48 = Constraint(expr= - 15*m.b5 + 15*m.b6 + 0.5*m.x62 + 0.5*m.x65 + m.x76 - m.x79 <= 15)

m.c49 = Constraint(expr=   5*m.b5 - 5*m.b6 + 0.5*m.x69 + 0.5*m.x72 - m.x82 + m.x85 <= 5)

m.c50 = Constraint(expr=   5*m.b5 + 5*m.b6 + 0.5*m.x69 + 0.5*m.x72 + m.x82 - m.x85 <= 10)

m.c51 = Constraint(expr= - m.x38 + m.x76 - m.x80 <= 0)

m.c52 = Constraint(expr= - m.x38 - m.x76 + m.x80 <= 0)

m.c53 = Constraint(expr= - m.x39 + m.x82 - m.x86 <= 0)

m.c54 = Constraint(expr= - m.x39 - m.x82 + m.x86 <= 0)

m.c55 = Constraint(expr= - 15*m.b7 - 15*m.b8 + 0.5*m.x62 + 0.5*m.x66 - m.x76 + m.x80 <= 0)

m.c56 = Constraint(expr= - 15*m.b7 + 15*m.b8 + 0.5*m.x62 + 0.5*m.x66 + m.x76 - m.x80 <= 15)

m.c57 = Constraint(expr=   5*m.b7 - 5*m.b8 + 0.5*m.x69 + 0.5*m.x73 - m.x82 + m.x86 <= 5)

m.c58 = Constraint(expr=   5*m.b7 + 5*m.b8 + 0.5*m.x69 + 0.5*m.x73 + m.x82 - m.x86 <= 10)

m.c59 = Constraint(expr= - m.x40 + m.x76 - m.x81 <= 0)

m.c60 = Constraint(expr= - m.x40 - m.x76 + m.x81 <= 0)

m.c61 = Constraint(expr= - m.x41 + m.x82 - m.x87 <= 0)

m.c62 = Constraint(expr= - m.x41 - m.x82 + m.x87 <= 0)

m.c63 = Constraint(expr= - 15*m.b9 - 15*m.b10 + 0.5*m.x62 + 0.5*m.x67 - m.x76 + m.x81 <= 0)

m.c64 = Constraint(expr= - 15*m.b9 + 15*m.b10 + 0.5*m.x62 + 0.5*m.x67 + m.x76 - m.x81 <= 15)

m.c65 = Constraint(expr=   5*m.b9 - 5*m.b10 + 0.5*m.x69 + 0.5*m.x74 - m.x82 + m.x87 <= 5)

m.c66 = Constraint(expr=   5*m.b9 + 5*m.b10 + 0.5*m.x69 + 0.5*m.x74 + m.x82 - m.x87 <= 10)

m.c67 = Constraint(expr= - m.x42 + m.x77 - m.x78 <= 0)

m.c68 = Constraint(expr= - m.x42 - m.x77 + m.x78 <= 0)

m.c69 = Constraint(expr= - m.x43 + m.x83 - m.x84 <= 0)

m.c70 = Constraint(expr= - m.x43 - m.x83 + m.x84 <= 0)

m.c71 = Constraint(expr= - 15*m.b11 - 15*m.b12 + 0.5*m.x63 + 0.5*m.x64 - m.x77 + m.x78 <= 0)

m.c72 = Constraint(expr= - 15*m.b11 + 15*m.b12 + 0.5*m.x63 + 0.5*m.x64 + m.x77 - m.x78 <= 15)

m.c73 = Constraint(expr=   5*m.b11 - 5*m.b12 + 0.5*m.x70 + 0.5*m.x71 - m.x83 + m.x84 <= 5)

m.c74 = Constraint(expr=   5*m.b11 + 5*m.b12 + 0.5*m.x70 + 0.5*m.x71 + m.x83 - m.x84 <= 10)

m.c75 = Constraint(expr= - m.x44 + m.x77 - m.x79 <= 0)

m.c76 = Constraint(expr= - m.x44 - m.x77 + m.x79 <= 0)

m.c77 = Constraint(expr= - m.x45 + m.x83 - m.x85 <= 0)

m.c78 = Constraint(expr= - m.x45 - m.x83 + m.x85 <= 0)

m.c79 = Constraint(expr= - 15*m.b13 - 15*m.b14 + 0.5*m.x63 + 0.5*m.x65 - m.x77 + m.x79 <= 0)

m.c80 = Constraint(expr= - 15*m.b13 + 15*m.b14 + 0.5*m.x63 + 0.5*m.x65 + m.x77 - m.x79 <= 15)

m.c81 = Constraint(expr=   5*m.b13 - 5*m.b14 + 0.5*m.x70 + 0.5*m.x72 - m.x83 + m.x85 <= 5)

m.c82 = Constraint(expr=   5*m.b13 + 5*m.b14 + 0.5*m.x70 + 0.5*m.x72 + m.x83 - m.x85 <= 10)

m.c83 = Constraint(expr= - m.x46 + m.x77 - m.x80 <= 0)

m.c84 = Constraint(expr= - m.x46 - m.x77 + m.x80 <= 0)

m.c85 = Constraint(expr= - m.x47 + m.x83 - m.x86 <= 0)

m.c86 = Constraint(expr= - m.x47 - m.x83 + m.x86 <= 0)

m.c87 = Constraint(expr= - 15*m.b15 - 15*m.b16 + 0.5*m.x63 + 0.5*m.x66 - m.x77 + m.x80 <= 0)

m.c88 = Constraint(expr= - 15*m.b15 + 15*m.b16 + 0.5*m.x63 + 0.5*m.x66 + m.x77 - m.x80 <= 15)

m.c89 = Constraint(expr=   5*m.b15 - 5*m.b16 + 0.5*m.x70 + 0.5*m.x73 - m.x83 + m.x86 <= 5)

m.c90 = Constraint(expr=   5*m.b15 + 5*m.b16 + 0.5*m.x70 + 0.5*m.x73 + m.x83 - m.x86 <= 10)

m.c91 = Constraint(expr= - m.x48 + m.x77 - m.x81 <= 0)

m.c92 = Constraint(expr= - m.x48 - m.x77 + m.x81 <= 0)

m.c93 = Constraint(expr= - m.x49 + m.x83 - m.x87 <= 0)

m.c94 = Constraint(expr= - m.x49 - m.x83 + m.x87 <= 0)

m.c95 = Constraint(expr= - 15*m.b17 - 15*m.b18 + 0.5*m.x63 + 0.5*m.x67 - m.x77 + m.x81 <= 0)

m.c96 = Constraint(expr= - 15*m.b17 + 15*m.b18 + 0.5*m.x63 + 0.5*m.x67 + m.x77 - m.x81 <= 15)

m.c97 = Constraint(expr=   5*m.b17 - 5*m.b18 + 0.5*m.x70 + 0.5*m.x74 - m.x83 + m.x87 <= 5)

m.c98 = Constraint(expr=   5*m.b17 + 5*m.b18 + 0.5*m.x70 + 0.5*m.x74 + m.x83 - m.x87 <= 10)

m.c99 = Constraint(expr= - m.x50 + m.x78 - m.x79 <= 0)

m.c100 = Constraint(expr= - m.x50 - m.x78 + m.x79 <= 0)

m.c101 = Constraint(expr= - m.x51 + m.x84 - m.x85 <= 0)

m.c102 = Constraint(expr= - m.x51 - m.x84 + m.x85 <= 0)

m.c103 = Constraint(expr= - 15*m.b19 - 15*m.b20 + 0.5*m.x64 + 0.5*m.x65 - m.x78 + m.x79 <= 0)

m.c104 = Constraint(expr= - 15*m.b19 + 15*m.b20 + 0.5*m.x64 + 0.5*m.x65 + m.x78 - m.x79 <= 15)

m.c105 = Constraint(expr=   5*m.b19 - 5*m.b20 + 0.5*m.x71 + 0.5*m.x72 - m.x84 + m.x85 <= 5)

m.c106 = Constraint(expr=   5*m.b19 + 5*m.b20 + 0.5*m.x71 + 0.5*m.x72 + m.x84 - m.x85 <= 10)

m.c107 = Constraint(expr= - m.x52 + m.x78 - m.x80 <= 0)

m.c108 = Constraint(expr= - m.x52 - m.x78 + m.x80 <= 0)

m.c109 = Constraint(expr= - m.x53 + m.x84 - m.x86 <= 0)

m.c110 = Constraint(expr= - m.x53 - m.x84 + m.x86 <= 0)

m.c111 = Constraint(expr= - 15*m.b21 - 15*m.b22 + 0.5*m.x64 + 0.5*m.x66 - m.x78 + m.x80 <= 0)

m.c112 = Constraint(expr= - 15*m.b21 + 15*m.b22 + 0.5*m.x64 + 0.5*m.x66 + m.x78 - m.x80 <= 15)

m.c113 = Constraint(expr=   5*m.b21 - 5*m.b22 + 0.5*m.x71 + 0.5*m.x73 - m.x84 + m.x86 <= 5)

m.c114 = Constraint(expr=   5*m.b21 + 5*m.b22 + 0.5*m.x71 + 0.5*m.x73 + m.x84 - m.x86 <= 10)

m.c115 = Constraint(expr= - m.x54 + m.x78 - m.x81 <= 0)

m.c116 = Constraint(expr= - m.x54 - m.x78 + m.x81 <= 0)

m.c117 = Constraint(expr= - m.x55 + m.x84 - m.x87 <= 0)

m.c118 = Constraint(expr= - m.x55 - m.x84 + m.x87 <= 0)

m.c119 = Constraint(expr= - 15*m.b23 - 15*m.b24 + 0.5*m.x64 + 0.5*m.x67 - m.x78 + m.x81 <= 0)

m.c120 = Constraint(expr= - 15*m.b23 + 15*m.b24 + 0.5*m.x64 + 0.5*m.x67 + m.x78 - m.x81 <= 15)

m.c121 = Constraint(expr=   5*m.b23 - 5*m.b24 + 0.5*m.x71 + 0.5*m.x74 - m.x84 + m.x87 <= 5)

m.c122 = Constraint(expr=   5*m.b23 + 5*m.b24 + 0.5*m.x71 + 0.5*m.x74 + m.x84 - m.x87 <= 10)

m.c123 = Constraint(expr= - m.x56 + m.x79 - m.x80 <= 0)

m.c124 = Constraint(expr= - m.x56 - m.x79 + m.x80 <= 0)

m.c125 = Constraint(expr= - m.x57 + m.x85 - m.x86 <= 0)

m.c126 = Constraint(expr= - m.x57 - m.x85 + m.x86 <= 0)

m.c127 = Constraint(expr= - 15*m.b25 - 15*m.b26 + 0.5*m.x65 + 0.5*m.x66 - m.x79 + m.x80 <= 0)

m.c128 = Constraint(expr= - 15*m.b25 + 15*m.b26 + 0.5*m.x65 + 0.5*m.x66 + m.x79 - m.x80 <= 15)

m.c129 = Constraint(expr=   5*m.b25 - 5*m.b26 + 0.5*m.x72 + 0.5*m.x73 - m.x85 + m.x86 <= 5)

m.c130 = Constraint(expr=   5*m.b25 + 5*m.b26 + 0.5*m.x72 + 0.5*m.x73 + m.x85 - m.x86 <= 10)

m.c131 = Constraint(expr= - m.x58 + m.x79 - m.x81 <= 0)

m.c132 = Constraint(expr= - m.x58 - m.x79 + m.x81 <= 0)

m.c133 = Constraint(expr= - m.x59 + m.x85 - m.x87 <= 0)

m.c134 = Constraint(expr= - m.x59 - m.x85 + m.x87 <= 0)

m.c135 = Constraint(expr= - 15*m.b27 - 15*m.b28 + 0.5*m.x65 + 0.5*m.x67 - m.x79 + m.x81 <= 0)

m.c136 = Constraint(expr= - 15*m.b27 + 15*m.b28 + 0.5*m.x65 + 0.5*m.x67 + m.x79 - m.x81 <= 15)

m.c137 = Constraint(expr=   5*m.b27 - 5*m.b28 + 0.5*m.x72 + 0.5*m.x74 - m.x85 + m.x87 <= 5)

m.c138 = Constraint(expr=   5*m.b27 + 5*m.b28 + 0.5*m.x72 + 0.5*m.x74 + m.x85 - m.x87 <= 10)

m.c139 = Constraint(expr= - m.x60 + m.x80 - m.x81 <= 0)

m.c140 = Constraint(expr= - m.x60 - m.x80 + m.x81 <= 0)

m.c141 = Constraint(expr= - m.x61 + m.x86 - m.x87 <= 0)

m.c142 = Constraint(expr= - m.x61 - m.x86 + m.x87 <= 0)

m.c143 = Constraint(expr= - 15*m.b29 - 15*m.b30 + 0.5*m.x66 + 0.5*m.x67 - m.x80 + m.x81 <= 0)

m.c144 = Constraint(expr= - 15*m.b29 + 15*m.b30 + 0.5*m.x66 + 0.5*m.x67 + m.x80 - m.x81 <= 15)

m.c145 = Constraint(expr=   5*m.b29 - 5*m.b30 + 0.5*m.x73 + 0.5*m.x74 - m.x86 + m.x87 <= 5)

m.c146 = Constraint(expr=   5*m.b29 + 5*m.b30 + 0.5*m.x73 + 0.5*m.x74 + m.x86 - m.x87 <= 10)

m.c147 = Constraint(expr=14/m.x62 - m.x69 <= 0)

m.c148 = Constraint(expr=14/m.x69 - m.x62 <= 0)

m.c149 = Constraint(expr=10/m.x63 - m.x70 <= 0)

m.c150 = Constraint(expr=10/m.x70 - m.x63 <= 0)

m.c151 = Constraint(expr=9/m.x64 - m.x71 <= 0)

m.c152 = Constraint(expr=9/m.x71 - m.x64 <= 0)

m.c153 = Constraint(expr=6/m.x65 - m.x72 <= 0)

m.c154 = Constraint(expr=6/m.x72 - m.x65 <= 0)

m.c155 = Constraint(expr=10/m.x66 - m.x73 <= 0)

m.c156 = Constraint(expr=10/m.x73 - m.x66 <= 0)

m.c157 = Constraint(expr=25/m.x67 - m.x74 <= 0)

m.c158 = Constraint(expr=25/m.x74 - m.x67 <= 0)
