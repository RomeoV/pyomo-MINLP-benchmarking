#  MINLP written by GAMS Convert at 08/13/20 17:38:00
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        101       61       20       20        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         82       72       10        0        0        0        0        0
#  FX      2        2        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        287      226       61        0
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
m.x21 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x22 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x23 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x24 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x25 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x26 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x27 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x28 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x29 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x30 = Var(within=Reals,bounds=(0.16,0.24),initialize=0.2)
m.x31 = Var(within=Reals,bounds=(-2,-2),initialize=-2)
m.x32 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x33 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x34 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x35 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x36 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x37 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x39 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x40 = Var(within=Reals,bounds=(None,None),initialize=-2)
m.x41 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x42 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x43 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x44 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x45 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x46 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x48 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x49 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x50 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x51 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x52 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x53 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x54 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x55 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x56 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x57 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x58 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x59 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x60 = Var(within=Reals,bounds=(None,None),initialize=1)
m.x61 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x62 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x63 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x64 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x65 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x66 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x67 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x68 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x69 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x70 = Var(within=Reals,bounds=(-2,2),initialize=-2)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=1)

m.obj = Objective(expr=(-1.66666666666667 + m.x81)**2 + m.x61**2*m.x21 + m.x62**2*m.x22 + m.x63**2*m.x23 + m.x64**2*
                       m.x24 + m.x65**2*m.x25 + m.x66**2*m.x26 + m.x67**2*m.x27 + m.x68**2*m.x28 + m.x69**2*m.x29 + 
                       m.x70**2*m.x30, sense=minimize)

m.c2 = Constraint(expr= - m.x21 - m.x41 + m.x51 == 0)

m.c3 = Constraint(expr= - m.x22 - m.x42 + m.x52 == 0)

m.c4 = Constraint(expr= - m.x23 - m.x43 + m.x53 == 0)

m.c5 = Constraint(expr= - m.x24 - m.x44 + m.x54 == 0)

m.c6 = Constraint(expr= - m.x25 - m.x45 + m.x55 == 0)

m.c7 = Constraint(expr= - m.x26 - m.x46 + m.x56 == 0)

m.c8 = Constraint(expr= - m.x27 - m.x47 + m.x57 == 0)

m.c9 = Constraint(expr= - m.x28 - m.x48 + m.x58 == 0)

m.c10 = Constraint(expr= - m.x29 - m.x49 + m.x59 == 0)

m.c11 = Constraint(expr= - m.x30 - m.x50 + m.x60 == 0)

m.c12 = Constraint(expr=-m.x21*m.x71 - m.x31 + m.x61 == 0)

m.c13 = Constraint(expr=-m.x22*m.x72 - m.x32 + m.x62 == 0)

m.c14 = Constraint(expr=-m.x23*m.x73 - m.x33 + m.x63 == 0)

m.c15 = Constraint(expr=-m.x24*m.x74 - m.x34 + m.x64 == 0)

m.c16 = Constraint(expr=-m.x25*m.x75 - m.x35 + m.x65 == 0)

m.c17 = Constraint(expr=-m.x26*m.x76 - m.x36 + m.x66 == 0)

m.c18 = Constraint(expr=-m.x27*m.x77 - m.x37 + m.x67 == 0)

m.c19 = Constraint(expr=-m.x28*m.x78 - m.x38 + m.x68 == 0)

m.c20 = Constraint(expr=-m.x29*m.x79 - m.x39 + m.x69 == 0)

m.c21 = Constraint(expr=-m.x30*m.x80 - m.x40 + m.x70 == 0)

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

m.c32 = Constraint(expr=   2*m.b11 - m.x61 <= 2)

m.c33 = Constraint(expr=   2*m.b12 - m.x62 <= 2)

m.c34 = Constraint(expr=   2*m.b13 - m.x63 <= 2)

m.c35 = Constraint(expr=   2*m.b14 - m.x64 <= 2)

m.c36 = Constraint(expr=   2*m.b15 - m.x65 <= 2)

m.c37 = Constraint(expr=   2*m.b16 - m.x66 <= 2)

m.c38 = Constraint(expr=   2*m.b17 - m.x67 <= 2)

m.c39 = Constraint(expr=   2*m.b18 - m.x68 <= 2)

m.c40 = Constraint(expr=   2*m.b19 - m.x69 <= 2)

m.c41 = Constraint(expr=   2*m.b20 - m.x70 <= 2)

m.c42 = Constraint(expr=   2*m.b11 - m.x61 >= 0)

m.c43 = Constraint(expr=   2*m.b12 - m.x62 >= 0)

m.c44 = Constraint(expr=   2*m.b13 - m.x63 >= 0)

m.c45 = Constraint(expr=   2*m.b14 - m.x64 >= 0)

m.c46 = Constraint(expr=   2*m.b15 - m.x65 >= 0)

m.c47 = Constraint(expr=   2*m.b16 - m.x66 >= 0)

m.c48 = Constraint(expr=   2*m.b17 - m.x67 >= 0)

m.c49 = Constraint(expr=   2*m.b18 - m.x68 >= 0)

m.c50 = Constraint(expr=   2*m.b19 - m.x69 >= 0)

m.c51 = Constraint(expr=   2*m.b20 - m.x70 >= 0)

m.c52 = Constraint(expr=   2*m.b11 <= 2)

m.c53 = Constraint(expr=   2*m.b12 - m.x61 <= 2)

m.c54 = Constraint(expr=   2*m.b13 - m.x62 <= 2)

m.c55 = Constraint(expr=   2*m.b14 - m.x63 <= 2)

m.c56 = Constraint(expr=   2*m.b15 - m.x64 <= 2)

m.c57 = Constraint(expr=   2*m.b16 - m.x65 <= 2)

m.c58 = Constraint(expr=   2*m.b17 - m.x66 <= 2)

m.c59 = Constraint(expr=   2*m.b18 - m.x67 <= 2)

m.c60 = Constraint(expr=   2*m.b19 - m.x68 <= 2)

m.c61 = Constraint(expr=   2*m.b20 - m.x69 <= 2)

m.c62 = Constraint(expr=   2*m.b11 >= 0)

m.c63 = Constraint(expr=   2*m.b12 - m.x61 >= 0)

m.c64 = Constraint(expr=   2*m.b13 - m.x62 >= 0)

m.c65 = Constraint(expr=   2*m.b14 - m.x63 >= 0)

m.c66 = Constraint(expr=   2*m.b15 - m.x64 >= 0)

m.c67 = Constraint(expr=   2*m.b16 - m.x65 >= 0)

m.c68 = Constraint(expr=   2*m.b17 - m.x66 >= 0)

m.c69 = Constraint(expr=   2*m.b18 - m.x67 >= 0)

m.c70 = Constraint(expr=   2*m.b19 - m.x68 >= 0)

m.c71 = Constraint(expr=   2*m.b20 - m.x69 >= 0)

m.c72 = Constraint(expr= - m.x21 - m.x41 + m.x42 == 0)

m.c73 = Constraint(expr= - m.x22 - m.x42 + m.x43 == 0)

m.c74 = Constraint(expr= - m.x23 - m.x43 + m.x44 == 0)

m.c75 = Constraint(expr= - m.x24 - m.x44 + m.x45 == 0)

m.c76 = Constraint(expr= - m.x25 - m.x45 + m.x46 == 0)

m.c77 = Constraint(expr= - m.x26 - m.x46 + m.x47 == 0)

m.c78 = Constraint(expr= - m.x27 - m.x47 + m.x48 == 0)

m.c79 = Constraint(expr= - m.x28 - m.x48 + m.x49 == 0)

m.c80 = Constraint(expr= - m.x29 - m.x49 + m.x50 == 0)

m.c81 = Constraint(expr=-m.x21*m.x71 - m.x31 + m.x32 == 0)

m.c82 = Constraint(expr=-m.x22*m.x72 - m.x32 + m.x33 == 0)

m.c83 = Constraint(expr=-m.x23*m.x73 - m.x33 + m.x34 == 0)

m.c84 = Constraint(expr=-m.x24*m.x74 - m.x34 + m.x35 == 0)

m.c85 = Constraint(expr=-m.x25*m.x75 - m.x35 + m.x36 == 0)

m.c86 = Constraint(expr=-m.x26*m.x76 - m.x36 + m.x37 == 0)

m.c87 = Constraint(expr=-m.x27*m.x77 - m.x37 + m.x38 == 0)

m.c88 = Constraint(expr=-m.x28*m.x78 - m.x38 + m.x39 == 0)

m.c89 = Constraint(expr=-m.x29*m.x79 - m.x39 + m.x40 == 0)

m.c90 = Constraint(expr=-m.x30*m.x80 - m.x40 + m.x81 == 0)

m.c91 = Constraint(expr=   m.x1 + m.x71 == 2)

m.c92 = Constraint(expr=   m.x2 + m.x72 == 2)

m.c93 = Constraint(expr=   m.x3 + m.x73 == 2)

m.c94 = Constraint(expr=   m.x4 + m.x74 == 2)

m.c95 = Constraint(expr=   m.x5 + m.x75 == 2)

m.c96 = Constraint(expr=   m.x6 + m.x76 == 2)

m.c97 = Constraint(expr=   m.x7 + m.x77 == 2)

m.c98 = Constraint(expr=   m.x8 + m.x78 == 2)

m.c99 = Constraint(expr=   m.x9 + m.x79 == 2)

m.c100 = Constraint(expr=   m.x10 + m.x80 == 2)

m.c101 = Constraint(expr=   m.x21 + m.x22 + m.x23 + m.x24 + m.x25 + m.x26 + m.x27 + m.x28 + m.x29 + m.x30 == 2)
