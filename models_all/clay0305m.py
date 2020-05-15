#  MINLP written by GAMS Convert at 05/15/20 00:50:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        156       16       40      100        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         86       31       55        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        496      376      120        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(11.5,57.5),initialize=11.5)
m.x2 = Var(within=Reals,bounds=(12.5,56.5),initialize=12.5)
m.x3 = Var(within=Reals,bounds=(10.5,58.5),initialize=10.5)
m.x4 = Var(within=Reals,bounds=(10,59),initialize=10)
m.x5 = Var(within=Reals,bounds=(13.5,55.5),initialize=13.5)
m.x6 = Var(within=Reals,bounds=(7,87),initialize=7)
m.x7 = Var(within=Reals,bounds=(6.5,87.5),initialize=6.5)
m.x8 = Var(within=Reals,bounds=(5.5,88.5),initialize=5.5)
m.x9 = Var(within=Reals,bounds=(5.5,88.5),initialize=5.5)
m.x10 = Var(within=Reals,bounds=(7.5,86.5),initialize=7.5)
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
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0)
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

m.obj = Objective(expr=   300*m.x66 + 240*m.x67 + 210*m.x68 + 50*m.x69 + 100*m.x70 + 150*m.x71 + 30*m.x72 + 120*m.x73
                        + 25*m.x74 + 60*m.x75 + 300*m.x76 + 240*m.x77 + 210*m.x78 + 50*m.x79 + 100*m.x80 + 150*m.x81
                        + 30*m.x82 + 120*m.x83 + 25*m.x84 + 60*m.x85, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x66 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x67 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x68 >= 0)

m.c5 = Constraint(expr= - m.x1 + m.x5 + m.x69 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x3 + m.x70 >= 0)

m.c7 = Constraint(expr= - m.x2 + m.x4 + m.x71 >= 0)

m.c8 = Constraint(expr= - m.x2 + m.x5 + m.x72 >= 0)

m.c9 = Constraint(expr= - m.x3 + m.x4 + m.x73 >= 0)

m.c10 = Constraint(expr= - m.x3 + m.x5 + m.x74 >= 0)

m.c11 = Constraint(expr= - m.x4 + m.x5 + m.x75 >= 0)

m.c12 = Constraint(expr=   m.x1 - m.x2 + m.x66 >= 0)

m.c13 = Constraint(expr=   m.x1 - m.x3 + m.x67 >= 0)

m.c14 = Constraint(expr=   m.x1 - m.x4 + m.x68 >= 0)

m.c15 = Constraint(expr=   m.x1 - m.x5 + m.x69 >= 0)

m.c16 = Constraint(expr=   m.x2 - m.x3 + m.x70 >= 0)

m.c17 = Constraint(expr=   m.x2 - m.x4 + m.x71 >= 0)

m.c18 = Constraint(expr=   m.x2 - m.x5 + m.x72 >= 0)

m.c19 = Constraint(expr=   m.x3 - m.x4 + m.x73 >= 0)

m.c20 = Constraint(expr=   m.x3 - m.x5 + m.x74 >= 0)

m.c21 = Constraint(expr=   m.x4 - m.x5 + m.x75 >= 0)

m.c22 = Constraint(expr= - m.x6 + m.x7 + m.x76 >= 0)

m.c23 = Constraint(expr= - m.x6 + m.x8 + m.x77 >= 0)

m.c24 = Constraint(expr= - m.x6 + m.x9 + m.x78 >= 0)

m.c25 = Constraint(expr= - m.x6 + m.x10 + m.x79 >= 0)

m.c26 = Constraint(expr= - m.x7 + m.x8 + m.x80 >= 0)

m.c27 = Constraint(expr= - m.x7 + m.x9 + m.x81 >= 0)

m.c28 = Constraint(expr= - m.x7 + m.x10 + m.x82 >= 0)

m.c29 = Constraint(expr= - m.x8 + m.x9 + m.x83 >= 0)

m.c30 = Constraint(expr= - m.x8 + m.x10 + m.x84 >= 0)

m.c31 = Constraint(expr= - m.x9 + m.x10 + m.x85 >= 0)

m.c32 = Constraint(expr=   m.x6 - m.x7 + m.x76 >= 0)

m.c33 = Constraint(expr=   m.x6 - m.x8 + m.x77 >= 0)

m.c34 = Constraint(expr=   m.x6 - m.x9 + m.x78 >= 0)

m.c35 = Constraint(expr=   m.x6 - m.x10 + m.x79 >= 0)

m.c36 = Constraint(expr=   m.x7 - m.x8 + m.x80 >= 0)

m.c37 = Constraint(expr=   m.x7 - m.x9 + m.x81 >= 0)

m.c38 = Constraint(expr=   m.x7 - m.x10 + m.x82 >= 0)

m.c39 = Constraint(expr=   m.x8 - m.x9 + m.x83 >= 0)

m.c40 = Constraint(expr=   m.x8 - m.x10 + m.x84 >= 0)

m.c41 = Constraint(expr=   m.x9 - m.x10 + m.x85 >= 0)

m.c42 = Constraint(expr=   m.x1 - m.x2 + 51*m.b11 <= 45)

m.c43 = Constraint(expr=   m.x1 - m.x3 + 51*m.b12 <= 47)

m.c44 = Constraint(expr=   m.x1 - m.x4 + 51*m.b13 <= 47.5)

m.c45 = Constraint(expr=   m.x1 - m.x5 + 51*m.b14 <= 44)

m.c46 = Constraint(expr=   m.x2 - m.x3 + 51*m.b15 <= 46)

m.c47 = Constraint(expr=   m.x2 - m.x4 + 51*m.b16 <= 46.5)

m.c48 = Constraint(expr=   m.x2 - m.x5 + 51*m.b17 <= 43)

m.c49 = Constraint(expr=   m.x3 - m.x4 + 51*m.b18 <= 48.5)

m.c50 = Constraint(expr=   m.x3 - m.x5 + 51*m.b19 <= 45)

m.c51 = Constraint(expr=   m.x4 - m.x5 + 51*m.b20 <= 45.5)

m.c52 = Constraint(expr= - m.x1 + m.x2 + 51*m.b21 <= 45)

m.c53 = Constraint(expr= - m.x1 + m.x3 + 51*m.b22 <= 47)

m.c54 = Constraint(expr= - m.x1 + m.x4 + 51*m.b23 <= 47.5)

m.c55 = Constraint(expr= - m.x1 + m.x5 + 51*m.b24 <= 44)

m.c56 = Constraint(expr= - m.x2 + m.x3 + 51*m.b25 <= 46)

m.c57 = Constraint(expr= - m.x2 + m.x4 + 51*m.b26 <= 46.5)

m.c58 = Constraint(expr= - m.x2 + m.x5 + 51*m.b27 <= 43)

m.c59 = Constraint(expr= - m.x3 + m.x4 + 51*m.b28 <= 48.5)

m.c60 = Constraint(expr= - m.x3 + m.x5 + 51*m.b29 <= 45)

m.c61 = Constraint(expr= - m.x4 + m.x5 + 51*m.b30 <= 45.5)

m.c62 = Constraint(expr=   m.x6 - m.x7 + 86*m.b31 <= 80.5)

m.c63 = Constraint(expr=   m.x6 - m.x8 + 86*m.b32 <= 81.5)

m.c64 = Constraint(expr=   m.x6 - m.x9 + 86*m.b33 <= 81.5)

m.c65 = Constraint(expr=   m.x6 - m.x10 + 86*m.b34 <= 79.5)

m.c66 = Constraint(expr=   m.x7 - m.x8 + 86*m.b35 <= 82)

m.c67 = Constraint(expr=   m.x7 - m.x9 + 86*m.b36 <= 82)

m.c68 = Constraint(expr=   m.x7 - m.x10 + 86*m.b37 <= 80)

m.c69 = Constraint(expr=   m.x8 - m.x9 + 86*m.b38 <= 83)

m.c70 = Constraint(expr=   m.x8 - m.x10 + 86*m.b39 <= 81)

m.c71 = Constraint(expr=   m.x9 - m.x10 + 86*m.b40 <= 81)

m.c72 = Constraint(expr= - m.x6 + m.x7 + 86*m.b41 <= 80.5)

m.c73 = Constraint(expr= - m.x6 + m.x8 + 86*m.b42 <= 81.5)

m.c74 = Constraint(expr= - m.x6 + m.x9 + 86*m.b43 <= 81.5)

m.c75 = Constraint(expr= - m.x6 + m.x10 + 86*m.b44 <= 79.5)

m.c76 = Constraint(expr= - m.x7 + m.x8 + 86*m.b45 <= 82)

m.c77 = Constraint(expr= - m.x7 + m.x9 + 86*m.b46 <= 82)

m.c78 = Constraint(expr= - m.x7 + m.x10 + 86*m.b47 <= 80)

m.c79 = Constraint(expr= - m.x8 + m.x9 + 86*m.b48 <= 83)

m.c80 = Constraint(expr= - m.x8 + m.x10 + 86*m.b49 <= 81)

m.c81 = Constraint(expr= - m.x9 + m.x10 + 86*m.b50 <= 81)

m.c82 = Constraint(expr=   m.b11 + m.b21 + m.b31 + m.b41 == 1)

m.c83 = Constraint(expr=   m.b12 + m.b22 + m.b32 + m.b42 == 1)

m.c84 = Constraint(expr=   m.b13 + m.b23 + m.b33 + m.b43 == 1)

m.c85 = Constraint(expr=   m.b14 + m.b24 + m.b34 + m.b44 == 1)

m.c86 = Constraint(expr=   m.b15 + m.b25 + m.b35 + m.b45 == 1)

m.c87 = Constraint(expr=   m.b16 + m.b26 + m.b36 + m.b46 == 1)

m.c88 = Constraint(expr=   m.b17 + m.b27 + m.b37 + m.b47 == 1)

m.c89 = Constraint(expr=   m.b18 + m.b28 + m.b38 + m.b48 == 1)

m.c90 = Constraint(expr=   m.b19 + m.b29 + m.b39 + m.b49 == 1)

m.c91 = Constraint(expr=   m.b20 + m.b30 + m.b40 + m.b50 == 1)

m.c92 = Constraint(expr=(-17.5 + m.x1)**2 + (-7 + m.x6)**2 + 7964*m.b51 <= 8000)

m.c93 = Constraint(expr=(-18.5 + m.x2)**2 + (-7.5 + m.x7)**2 + 7808*m.b52 <= 7844)

m.c94 = Constraint(expr=(-16.5 + m.x3)**2 + (-8.5 + m.x8)**2 + 8128*m.b53 <= 8164)

m.c95 = Constraint(expr=(-16 + m.x4)**2 + (-8.5 + m.x9)**2 + 8213*m.b54 <= 8249)

m.c96 = Constraint(expr=(-19.5 + m.x5)**2 + (-6.5 + m.x10)**2 + 7660*m.b55 <= 7696)

m.c97 = Constraint(expr=(-52.5 + m.x1)**2 + (-77 + m.x6)**2 + 6481*m.b56 <= 6581)

m.c98 = Constraint(expr=(-53.5 + m.x2)**2 + (-77.5 + m.x7)**2 + 6622*m.b57 <= 6722)

m.c99 = Constraint(expr=(-51.5 + m.x3)**2 + (-78.5 + m.x8)**2 + 6910*m.b58 <= 7010)

m.c100 = Constraint(expr=(-51 + m.x4)**2 + (-78.5 + m.x9)**2 + 6910*m.b59 <= 7010)

m.c101 = Constraint(expr=(-54.5 + m.x5)**2 + (-76.5 + m.x10)**2 + 6342*m.b60 <= 6442)

m.c102 = Constraint(expr=(-32.5 + m.x1)**2 + (-47 + m.x6)**2 + 2209*m.b61 <= 2225)

m.c103 = Constraint(expr=(-33.5 + m.x2)**2 + (-47.5 + m.x7)**2 + 2194*m.b62 <= 2210)

m.c104 = Constraint(expr=(-31.5 + m.x3)**2 + (-48.5 + m.x8)**2 + 2562*m.b63 <= 2578)

m.c105 = Constraint(expr=(-31 + m.x4)**2 + (-48.5 + m.x9)**2 + 2617*m.b64 <= 2633)

m.c106 = Constraint(expr=(-34.5 + m.x5)**2 + (-46.5 + m.x10)**2 + 2025*m.b65 <= 2041)

m.c107 = Constraint(expr=(-17.5 + m.x1)**2 + (-13 + m.x6)**2 + 7040*m.b51 <= 7076)

m.c108 = Constraint(expr=(-18.5 + m.x2)**2 + (-12.5 + m.x7)**2 + 7033*m.b52 <= 7069)

m.c109 = Constraint(expr=(-16.5 + m.x3)**2 + (-11.5 + m.x8)**2 + 7657*m.b53 <= 7693)

m.c110 = Constraint(expr=(-16 + m.x4)**2 + (-11.5 + m.x9)**2 + 7742*m.b54 <= 7778)

m.c111 = Constraint(expr=(-19.5 + m.x5)**2 + (-13.5 + m.x10)**2 + 6589*m.b55 <= 6625)

m.c112 = Constraint(expr=(-52.5 + m.x1)**2 + (-83 + m.x6)**2 + 7357*m.b56 <= 7457)

m.c113 = Constraint(expr=(-53.5 + m.x2)**2 + (-82.5 + m.x7)**2 + 7357*m.b57 <= 7457)

m.c114 = Constraint(expr=(-51.5 + m.x3)**2 + (-81.5 + m.x8)**2 + 7357*m.b58 <= 7457)

m.c115 = Constraint(expr=(-51 + m.x4)**2 + (-81.5 + m.x9)**2 + 7357*m.b59 <= 7457)

m.c116 = Constraint(expr=(-54.5 + m.x5)**2 + (-83.5 + m.x10)**2 + 7357*m.b60 <= 7457)

m.c117 = Constraint(expr=(-32.5 + m.x1)**2 + (-53 + m.x6)**2 + 2725*m.b61 <= 2741)

m.c118 = Constraint(expr=(-33.5 + m.x2)**2 + (-52.5 + m.x7)**2 + 2629*m.b62 <= 2645)

m.c119 = Constraint(expr=(-31.5 + m.x3)**2 + (-51.5 + m.x8)**2 + 2829*m.b63 <= 2845)

m.c120 = Constraint(expr=(-31 + m.x4)**2 + (-51.5 + m.x9)**2 + 2884*m.b64 <= 2900)

m.c121 = Constraint(expr=(-34.5 + m.x5)**2 + (-53.5 + m.x10)**2 + 2541*m.b65 <= 2557)

m.c122 = Constraint(expr=(-12.5 + m.x1)**2 + (-7 + m.x6)**2 + 8389*m.b51 <= 8425)

m.c123 = Constraint(expr=(-11.5 + m.x2)**2 + (-7.5 + m.x7)**2 + 8389*m.b52 <= 8425)

m.c124 = Constraint(expr=(-13.5 + m.x3)**2 + (-8.5 + m.x8)**2 + 8389*m.b53 <= 8425)

m.c125 = Constraint(expr=(-14 + m.x4)**2 + (-8.5 + m.x9)**2 + 8389*m.b54 <= 8425)

m.c126 = Constraint(expr=(-10.5 + m.x5)**2 + (-6.5 + m.x10)**2 + 8389*m.b55 <= 8425)

m.c127 = Constraint(expr=(-47.5 + m.x1)**2 + (-77 + m.x6)**2 + 6096*m.b56 <= 6196)

m.c128 = Constraint(expr=(-46.5 + m.x2)**2 + (-77.5 + m.x7)**2 + 6097*m.b57 <= 6197)

m.c129 = Constraint(expr=(-48.5 + m.x3)**2 + (-78.5 + m.x8)**2 + 6673*m.b58 <= 6773)

m.c130 = Constraint(expr=(-49 + m.x4)**2 + (-78.5 + m.x9)**2 + 6750*m.b59 <= 6850)

m.c131 = Constraint(expr=(-45.5 + m.x5)**2 + (-76.5 + m.x10)**2 + 5685*m.b60 <= 5785)

m.c132 = Constraint(expr=(-27.5 + m.x1)**2 + (-47 + m.x6)**2 + 2484*m.b61 <= 2500)

m.c133 = Constraint(expr=(-26.5 + m.x2)**2 + (-47.5 + m.x7)**2 + 2565*m.b62 <= 2581)

m.c134 = Constraint(expr=(-28.5 + m.x3)**2 + (-48.5 + m.x8)**2 + 2733*m.b63 <= 2749)

m.c135 = Constraint(expr=(-29 + m.x4)**2 + (-48.5 + m.x9)**2 + 2733*m.b64 <= 2749)

m.c136 = Constraint(expr=(-25.5 + m.x5)**2 + (-46.5 + m.x10)**2 + 2484*m.b65 <= 2500)

m.c137 = Constraint(expr=(-12.5 + m.x1)**2 + (-13 + m.x6)**2 + 7465*m.b51 <= 7501)

m.c138 = Constraint(expr=(-11.5 + m.x2)**2 + (-12.5 + m.x7)**2 + 7614*m.b52 <= 7650)

m.c139 = Constraint(expr=(-13.5 + m.x3)**2 + (-11.5 + m.x8)**2 + 7918*m.b53 <= 7954)

m.c140 = Constraint(expr=(-14 + m.x4)**2 + (-11.5 + m.x9)**2 + 7918*m.b54 <= 7954)

m.c141 = Constraint(expr=(-10.5 + m.x5)**2 + (-13.5 + m.x10)**2 + 7318*m.b55 <= 7354)

m.c142 = Constraint(expr=(-47.5 + m.x1)**2 + (-83 + m.x6)**2 + 6972*m.b56 <= 7072)

m.c143 = Constraint(expr=(-46.5 + m.x2)**2 + (-82.5 + m.x7)**2 + 6832*m.b57 <= 6932)

m.c144 = Constraint(expr=(-48.5 + m.x3)**2 + (-81.5 + m.x8)**2 + 7120*m.b58 <= 7220)

m.c145 = Constraint(expr=(-49 + m.x4)**2 + (-81.5 + m.x9)**2 + 7197*m.b59 <= 7297)

m.c146 = Constraint(expr=(-45.5 + m.x5)**2 + (-83.5 + m.x10)**2 + 6700*m.b60 <= 6800)

m.c147 = Constraint(expr=(-27.5 + m.x1)**2 + (-53 + m.x6)**2 + 3000*m.b61 <= 3016)

m.c148 = Constraint(expr=(-26.5 + m.x2)**2 + (-52.5 + m.x7)**2 + 3000*m.b62 <= 3016)

m.c149 = Constraint(expr=(-28.5 + m.x3)**2 + (-51.5 + m.x8)**2 + 3000*m.b63 <= 3016)

m.c150 = Constraint(expr=(-29 + m.x4)**2 + (-51.5 + m.x9)**2 + 3000*m.b64 <= 3016)

m.c151 = Constraint(expr=(-25.5 + m.x5)**2 + (-53.5 + m.x10)**2 + 3000*m.b65 <= 3016)

m.c152 = Constraint(expr=   m.b51 + m.b56 + m.b61 == 1)

m.c153 = Constraint(expr=   m.b52 + m.b57 + m.b62 == 1)

m.c154 = Constraint(expr=   m.b53 + m.b58 + m.b63 == 1)

m.c155 = Constraint(expr=   m.b54 + m.b59 + m.b64 == 1)

m.c156 = Constraint(expr=   m.b55 + m.b60 + m.b65 == 1)
