#  MINLP written by GAMS Convert at 05/15/20 00:50:48
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         80       60       10       10        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         72       62       10        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        190      179       11        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x2 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x3 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x4 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x5 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x6 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x7 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x8 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x9 = Var(within=Reals,bounds=(-1,1),initialize=-1)
m.x10 = Var(within=Reals,bounds=(-1,1),initialize=-1)
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
m.x21 = Var(within=Reals,bounds=(-2,-2),initialize=-2)
m.x22 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x23 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x24 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x25 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x26 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x27 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x28 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x30 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x31 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x41 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x51 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x52 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x53 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x54 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x55 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x56 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x57 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x58 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x59 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x60 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=(-1.66666666666667 + m.x71)**2 + 0.2*m.x51**2 + 0.2*m.x52**2 + 0.2*m.x53**2 + 0.2*m.x54**2 + 0.2*
                       m.x55**2 + 0.2*m.x56**2 + 0.2*m.x57**2 + 0.2*m.x58**2 + 0.2*m.x59**2 + 0.2*m.x60**2
                       , sense=minimize)

m.c2 = Constraint(expr= - m.x31 + m.x41 == 0.2)

m.c3 = Constraint(expr= - m.x32 + m.x42 == 0.2)

m.c4 = Constraint(expr= - m.x33 + m.x43 == 0.2)

m.c5 = Constraint(expr= - m.x34 + m.x44 == 0.2)

m.c6 = Constraint(expr= - m.x35 + m.x45 == 0.2)

m.c7 = Constraint(expr= - m.x36 + m.x46 == 0.2)

m.c8 = Constraint(expr= - m.x37 + m.x47 == 0.2)

m.c9 = Constraint(expr= - m.x38 + m.x48 == 0.2)

m.c10 = Constraint(expr= - m.x39 + m.x49 == 0.2)

m.c11 = Constraint(expr= - m.x40 + m.x50 == 0.2)

m.c12 = Constraint(expr= - m.x21 + m.x51 - 0.2*m.x61 == 0)

m.c13 = Constraint(expr= - m.x22 + m.x52 - 0.2*m.x62 == 0)

m.c14 = Constraint(expr= - m.x23 + m.x53 - 0.2*m.x63 == 0)

m.c15 = Constraint(expr= - m.x24 + m.x54 - 0.2*m.x64 == 0)

m.c16 = Constraint(expr= - m.x25 + m.x55 - 0.2*m.x65 == 0)

m.c17 = Constraint(expr= - m.x26 + m.x56 - 0.2*m.x66 == 0)

m.c18 = Constraint(expr= - m.x27 + m.x57 - 0.2*m.x67 == 0)

m.c19 = Constraint(expr= - m.x28 + m.x58 - 0.2*m.x68 == 0)

m.c20 = Constraint(expr= - m.x29 + m.x59 - 0.2*m.x69 == 0)

m.c21 = Constraint(expr= - m.x30 + m.x60 - 0.2*m.x70 == 0)

m.c22 = Constraint(expr=   m.x1 - 2*m.b11 == -1)

m.c23 = Constraint(expr=   m.x2 - 2*m.b12 == -1)

m.c24 = Constraint(expr=   m.x3 - 2*m.b13 == -1)

m.c25 = Constraint(expr=   m.x4 - 2*m.b14 == -1)

m.c26 = Constraint(expr=   m.x5 - 2*m.b15 == -1)

m.c27 = Constraint(expr=   m.x6 - 2*m.b16 == -1)

m.c28 = Constraint(expr=   m.x7 - 2*m.b17 == -1)

m.c29 = Constraint(expr=   m.x8 - 2*m.b18 == -1)

m.c30 = Constraint(expr=   m.x9 - 2*m.b19 == -1)

m.c31 = Constraint(expr=   m.x10 - 2*m.b20 == -1)

m.c32 = Constraint(expr=   2*m.b11 - m.x51 <= 2)

m.c33 = Constraint(expr=   2*m.b12 - m.x52 <= 2)

m.c34 = Constraint(expr=   2*m.b13 - m.x53 <= 2)

m.c35 = Constraint(expr=   2*m.b14 - m.x54 <= 2)

m.c36 = Constraint(expr=   2*m.b15 - m.x55 <= 2)

m.c37 = Constraint(expr=   2*m.b16 - m.x56 <= 2)

m.c38 = Constraint(expr=   2*m.b17 - m.x57 <= 2)

m.c39 = Constraint(expr=   2*m.b18 - m.x58 <= 2)

m.c40 = Constraint(expr=   2*m.b19 - m.x59 <= 2)

m.c41 = Constraint(expr=   2*m.b20 - m.x60 <= 2)

m.c42 = Constraint(expr=   2*m.b11 - m.x51 >= 0)

m.c43 = Constraint(expr=   2*m.b12 - m.x52 >= 0)

m.c44 = Constraint(expr=   2*m.b13 - m.x53 >= 0)

m.c45 = Constraint(expr=   2*m.b14 - m.x54 >= 0)

m.c46 = Constraint(expr=   2*m.b15 - m.x55 >= 0)

m.c47 = Constraint(expr=   2*m.b16 - m.x56 >= 0)

m.c48 = Constraint(expr=   2*m.b17 - m.x57 >= 0)

m.c49 = Constraint(expr=   2*m.b18 - m.x58 >= 0)

m.c50 = Constraint(expr=   2*m.b19 - m.x59 >= 0)

m.c51 = Constraint(expr=   2*m.b20 - m.x60 >= 0)

m.c52 = Constraint(expr= - m.x31 + m.x32 == 0.2)

m.c53 = Constraint(expr= - m.x32 + m.x33 == 0.2)

m.c54 = Constraint(expr= - m.x33 + m.x34 == 0.2)

m.c55 = Constraint(expr= - m.x34 + m.x35 == 0.2)

m.c56 = Constraint(expr= - m.x35 + m.x36 == 0.2)

m.c57 = Constraint(expr= - m.x36 + m.x37 == 0.2)

m.c58 = Constraint(expr= - m.x37 + m.x38 == 0.2)

m.c59 = Constraint(expr= - m.x38 + m.x39 == 0.2)

m.c60 = Constraint(expr= - m.x39 + m.x40 == 0.2)

m.c61 = Constraint(expr= - m.x21 + m.x22 - 0.2*m.x61 == 0)

m.c62 = Constraint(expr= - m.x22 + m.x23 - 0.2*m.x62 == 0)

m.c63 = Constraint(expr= - m.x23 + m.x24 - 0.2*m.x63 == 0)

m.c64 = Constraint(expr= - m.x24 + m.x25 - 0.2*m.x64 == 0)

m.c65 = Constraint(expr= - m.x25 + m.x26 - 0.2*m.x65 == 0)

m.c66 = Constraint(expr= - m.x26 + m.x27 - 0.2*m.x66 == 0)

m.c67 = Constraint(expr= - m.x27 + m.x28 - 0.2*m.x67 == 0)

m.c68 = Constraint(expr= - m.x28 + m.x29 - 0.2*m.x68 == 0)

m.c69 = Constraint(expr= - m.x29 + m.x30 - 0.2*m.x69 == 0)

m.c70 = Constraint(expr= - m.x30 - 0.2*m.x70 + m.x71 == 0)

m.c71 = Constraint(expr=   m.x1 + m.x61 == 2)

m.c72 = Constraint(expr=   m.x2 + m.x62 == 2)

m.c73 = Constraint(expr=   m.x3 + m.x63 == 2)

m.c74 = Constraint(expr=   m.x4 + m.x64 == 2)

m.c75 = Constraint(expr=   m.x5 + m.x65 == 2)

m.c76 = Constraint(expr=   m.x6 + m.x66 == 2)

m.c77 = Constraint(expr=   m.x7 + m.x67 == 2)

m.c78 = Constraint(expr=   m.x8 + m.x68 == 2)

m.c79 = Constraint(expr=   m.x9 + m.x69 == 2)

m.c80 = Constraint(expr=   m.x10 + m.x70 == 2)
