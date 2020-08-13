#  MINLP written by GAMS Convert at 08/13/20 17:38:07
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        104       72        8       24        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         91       85        6        0        0        0        0        0
#  FX      1        0        1        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        336      244       92        0
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
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x15 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x16 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x17 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x18 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x19 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x20 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x21 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x22 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x23 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x24 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x25 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x26 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x27 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x35 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x36 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x37 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x38 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x39 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x40 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x41 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x42 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x43 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x44 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x45 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x46 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x47 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x48 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x49 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x50 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x51 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x52 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x53 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x54 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x55 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x56 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x57 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x58 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x59 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x60 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x61 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x62 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x63 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x64 = Var(within=Reals,bounds=(0.001,10),initialize=0.001)
m.x65 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x66 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x67 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x68 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x69 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x70 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x71 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x72 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x73 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x74 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x75 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x76 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x77 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x78 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x79 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x80 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x81 = Var(within=Reals,bounds=(1E-5,10),initialize=1E-5)
m.x82 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x83 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.x84 = Var(within=Reals,bounds=(-10,10),initialize=0)
m.b85 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=   m.x1, sense=maximize)

m.c2 = Constraint(expr= - m.x8 + 0.001*m.b85 <= 0)

m.c3 = Constraint(expr= - m.x9 + 0.001*m.b86 <= 0)

m.c4 = Constraint(expr= - m.x10 + 0.001*m.b87 <= 0)

m.c5 = Constraint(expr= - m.x11 + 0.001*m.b88 <= 0)

m.c6 = Constraint(expr= - m.x12 + 0.001*m.b89 <= 0)

m.c7 = Constraint(expr= - m.x13 + 0.001*m.b90 <= 0)

m.c8 = Constraint(expr=   m.x8 - 10*m.b85 <= 0)

m.c9 = Constraint(expr=   m.x9 - 10*m.b86 <= 0)

m.c10 = Constraint(expr=   m.x10 - 10*m.b87 <= 0)

m.c11 = Constraint(expr=   m.x11 - 10*m.b88 <= 0)

m.c12 = Constraint(expr=   m.x12 - 10*m.b89 <= 0)

m.c13 = Constraint(expr=   m.x13 - 10*m.b90 <= 0)

m.c14 = Constraint(expr= - m.x28 + 0.001*m.b85 <= 0)

m.c15 = Constraint(expr= - m.x29 + 0.001*m.b86 <= 0)

m.c16 = Constraint(expr= - m.x30 + 0.001*m.b87 <= 0)

m.c17 = Constraint(expr= - m.x31 + 0.001*m.b88 <= 0)

m.c18 = Constraint(expr= - m.x32 + 0.001*m.b89 <= 0)

m.c19 = Constraint(expr= - m.x33 + 0.001*m.b90 <= 0)

m.c20 = Constraint(expr=   m.x28 - 10*m.b85 <= 0)

m.c21 = Constraint(expr=   m.x29 - 10*m.b86 <= 0)

m.c22 = Constraint(expr=   m.x30 - 10*m.b87 <= 0)

m.c23 = Constraint(expr=   m.x31 - 10*m.b88 <= 0)

m.c24 = Constraint(expr=   m.x32 - 10*m.b89 <= 0)

m.c25 = Constraint(expr=   m.x33 - 10*m.b90 <= 0)

m.c26 = Constraint(expr=   m.b85 - m.b86 >= 0)

m.c27 = Constraint(expr=   m.b86 - m.b87 >= 0)

m.c28 = Constraint(expr=   m.b87 - m.b88 >= 0)

m.c29 = Constraint(expr=   m.b88 - m.b89 >= 0)

m.c30 = Constraint(expr=   m.b89 - m.b90 >= 0)

m.c31 = Constraint(expr= - 10000000*m.x2 + 10000000*m.x8 + m.x14 == 0)

m.c32 = Constraint(expr=2000000*m.x1*m.x2 - 1000000*m.x3 + 1000000*m.x9 + m.x15 == 0)

m.c33 = Constraint(expr=200000*m.x1*m.x3 - 100000*m.x2 - 100000*m.x4 - 100000*m.x8 + 100000*m.x10 + m.x16 == 0)

m.c34 = Constraint(expr=20000*m.x1*m.x4 - 10000*m.x3 - 10000*m.x5 - 10000*m.x9 + 10000*m.x11 + m.x17 == 0)

m.c35 = Constraint(expr=2000*m.x1*m.x5 - 1000*m.x4 - 1000*m.x6 - 1000*m.x10 + 1000*m.x12 + m.x18 == 0)

m.c36 = Constraint(expr=200*m.x1*m.x6 - 100*m.x5 - 100*m.x7 - 100*m.x11 + 100*m.x13 + m.x19 == 0)

m.c37 = Constraint(expr=20*m.x1*m.x7 - 10*m.x6 - 10*m.x12 + m.x20 == 0)

m.c38 = Constraint(expr= - m.x7 - m.x13 + m.x21 == 0)

m.c39 = Constraint(expr= - m.x2 + 1E-5*m.x3 - 1E-10*m.x4 + m.x22 == 0)

m.c40 = Constraint(expr= - m.x3 + 2E-5*m.x4 - 3E-10*m.x5 + m.x23 == 0)

m.c41 = Constraint(expr= - m.x4 + 3E-5*m.x5 - 6E-10*m.x6 + m.x24 == 0)

m.c42 = Constraint(expr= - m.x5 + 4E-5*m.x6 - 1E-9*m.x7 + m.x25 == 0)

m.c43 = Constraint(expr= - m.x6 + 5E-5*m.x7 + m.x26 == 0)

m.c44 = Constraint(expr= - m.x7 + m.x27 == 0)

m.c45 = Constraint(expr= - m.x8 + 1E-5*m.x9 - 1E-10*m.x10 + m.x28 == 0)

m.c46 = Constraint(expr= - m.x9 + 2E-5*m.x10 - 3E-10*m.x11 + m.x29 == 0)

m.c47 = Constraint(expr= - m.x10 + 3E-5*m.x11 - 6E-10*m.x12 + m.x30 == 0)

m.c48 = Constraint(expr= - m.x11 + 4E-5*m.x12 - 1E-9*m.x13 + m.x31 == 0)

m.c49 = Constraint(expr= - m.x12 + 5E-5*m.x13 + m.x32 == 0)

m.c50 = Constraint(expr= - m.x13 + m.x33 == 0)

m.c51 = Constraint(expr= - m.x14 + 1E-5*m.x15 - 1E-10*m.x16 + m.x34 == 0)

m.c52 = Constraint(expr= - m.x15 + 2E-5*m.x16 - 3E-10*m.x17 + m.x35 == 0)

m.c53 = Constraint(expr= - m.x16 + 3E-5*m.x17 - 6E-10*m.x18 + m.x36 == 0)

m.c54 = Constraint(expr= - m.x17 + 4E-5*m.x18 - 1E-9*m.x19 + m.x37 == 0)

m.c55 = Constraint(expr= - m.x18 + 5E-5*m.x19 - 1.5E-9*m.x20 + m.x38 == 0)

m.c56 = Constraint(expr= - m.x19 + 6E-5*m.x20 - 2.1E-9*m.x21 + m.x39 == 0)

m.c57 = Constraint(expr= - m.x20 + 7E-5*m.x21 + m.x40 == 0)

m.c58 = Constraint(expr= - m.x21 + m.x41 == 0)

m.c59 = Constraint(expr= - m.x27 + m.x42 == 0)

m.c60 = Constraint(expr= - m.x25 + m.x43 == 0)

m.c61 = Constraint(expr= - m.x23 + m.x44 == 0)

m.c62 = Constraint(expr= - m.x26 + m.x45 == 0)

m.c63 = Constraint(expr= - m.x24 + m.x46 == 0)

m.c64 = Constraint(expr= - m.x22 + m.x47 == 0)

m.c65 = Constraint(expr=m.x42/m.x45*m.x46 - m.x43 + m.x48 == 0)

m.c66 = Constraint(expr=m.x42/m.x45*m.x47 - m.x44 + m.x49 == 0)

m.c67 = Constraint(expr=m.x45/m.x48*m.x49 - m.x46 + m.x51 == 0)

m.c68 = Constraint(expr=m.x45/m.x48*m.x50 - m.x47 + m.x52 == 0)

m.c69 = Constraint(expr=m.x48/m.x51*m.x52 - m.x49 + m.x54 == 0)

m.c70 = Constraint(expr=m.x48/m.x51*m.x53 - m.x50 + m.x55 == 0)

m.c71 = Constraint(expr=   m.x50 == 0)

m.c72 = Constraint(expr=   m.x53 == 0)

m.c73 = Constraint(expr=   m.x56 == 0)

m.c74 = Constraint(expr= - m.x41 + m.x57 == 0)

m.c75 = Constraint(expr= - m.x39 + m.x58 == 0)

m.c76 = Constraint(expr= - m.x37 + m.x59 == 0)

m.c77 = Constraint(expr= - m.x35 + m.x60 == 0)

m.c78 = Constraint(expr= - m.x40 + m.x61 == 0)

m.c79 = Constraint(expr= - m.x38 + m.x62 == 0)

m.c80 = Constraint(expr= - m.x36 + m.x63 == 0)

m.c81 = Constraint(expr= - m.x34 + m.x64 == 0)

m.c82 = Constraint(expr=m.x57/m.x61*m.x62 - m.x58 + m.x65 == 0)

m.c83 = Constraint(expr=m.x57/m.x61*m.x63 - m.x59 + m.x66 == 0)

m.c84 = Constraint(expr=m.x57/m.x61*m.x64 - m.x60 + m.x67 == 0)

m.c85 = Constraint(expr=m.x61/m.x65*m.x66 - m.x62 + m.x69 == 0)

m.c86 = Constraint(expr=m.x61/m.x65*m.x67 - m.x63 + m.x70 == 0)

m.c87 = Constraint(expr=m.x61/m.x65*m.x68 - m.x64 + m.x71 == 0)

m.c88 = Constraint(expr=m.x65/m.x69*m.x70 - m.x66 + m.x73 == 0)

m.c89 = Constraint(expr=m.x65/m.x69*m.x71 - m.x67 + m.x74 == 0)

m.c90 = Constraint(expr=m.x65/m.x69*m.x72 - m.x68 + m.x75 == 0)

m.c91 = Constraint(expr=m.x69/m.x73*m.x74 - m.x70 + m.x77 == 0)

m.c92 = Constraint(expr=m.x69/m.x73*m.x75 - m.x71 + m.x78 == 0)

m.c93 = Constraint(expr=m.x69/m.x73*m.x76 - m.x72 + m.x79 == 0)

m.c94 = Constraint(expr=m.x73/m.x77*m.x78 - m.x74 + m.x81 == 0)

m.c95 = Constraint(expr=m.x73/m.x77*m.x79 - m.x75 + m.x82 == 0)

m.c96 = Constraint(expr=m.x73/m.x77*m.x80 - m.x76 + m.x83 == 0)

m.c97 = Constraint(expr=   m.x68 == 0)

m.c98 = Constraint(expr=   m.x72 == 0)

m.c99 = Constraint(expr=   m.x76 == 0)

m.c100 = Constraint(expr=   m.x80 == 0)

m.c101 = Constraint(expr=   m.x84 == 0)

m.c102 = Constraint(expr=m.x31*m.x32 - m.x30*m.x33 - 1E-5*m.b90 >= 0)

m.c103 = Constraint(expr=m.x30*m.x31*m.x32 - m.x30*m.x30*m.x33 + m.x28*m.x32*m.x33 - m.x29*m.x32*m.x32 - 1E-5*m.b89
                          >= 0)

m.c104 = Constraint(expr=m.x29*m.x30*m.x31*m.x32 - m.x30**2*m.x29*m.x33 - m.x29**2*m.x32**2 + 2*m.x28*m.x29*m.x32*m.x33
                          + m.x28*m.x30*m.x31*m.x33 - m.x28**2*m.x33**2 - m.x31**2*m.x28*m.x32 + (m.x29*m.x30 - m.x28*
                         m.x31)*(1 - m.b89) - 1E-5*m.b88 >= 0)
