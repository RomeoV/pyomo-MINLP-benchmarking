#  MINLP written by GAMS Convert at 05/15/20 00:50:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        107       11       24       72        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         57       21       36        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        337      241       96        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(11.5,52.5),initialize=11.5)
m.x2 = Var(within=Reals,bounds=(12.5,51.5),initialize=12.5)
m.x3 = Var(within=Reals,bounds=(10.5,53.5),initialize=10.5)
m.x4 = Var(within=Reals,bounds=(10,54),initialize=10)
m.x5 = Var(within=Reals,bounds=(7,82),initialize=7)
m.x6 = Var(within=Reals,bounds=(6.5,82.5),initialize=6.5)
m.x7 = Var(within=Reals,bounds=(5.5,83.5),initialize=5.5)
m.x8 = Var(within=Reals,bounds=(5.5,83.5),initialize=5.5)
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

m.obj = Objective(expr=   300*m.x45 + 240*m.x46 + 210*m.x47 + 100*m.x48 + 150*m.x49 + 120*m.x50 + 300*m.x51 + 240*m.x52
                        + 210*m.x53 + 100*m.x54 + 150*m.x55 + 120*m.x56, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x45 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x46 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x47 >= 0)

m.c5 = Constraint(expr= - m.x2 + m.x3 + m.x48 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x4 + m.x49 >= 0)

m.c7 = Constraint(expr= - m.x3 + m.x4 + m.x50 >= 0)

m.c8 = Constraint(expr=   m.x1 - m.x2 + m.x45 >= 0)

m.c9 = Constraint(expr=   m.x1 - m.x3 + m.x46 >= 0)

m.c10 = Constraint(expr=   m.x1 - m.x4 + m.x47 >= 0)

m.c11 = Constraint(expr=   m.x2 - m.x3 + m.x48 >= 0)

m.c12 = Constraint(expr=   m.x2 - m.x4 + m.x49 >= 0)

m.c13 = Constraint(expr=   m.x3 - m.x4 + m.x50 >= 0)

m.c14 = Constraint(expr= - m.x5 + m.x6 + m.x51 >= 0)

m.c15 = Constraint(expr= - m.x5 + m.x7 + m.x52 >= 0)

m.c16 = Constraint(expr= - m.x5 + m.x8 + m.x53 >= 0)

m.c17 = Constraint(expr= - m.x6 + m.x7 + m.x54 >= 0)

m.c18 = Constraint(expr= - m.x6 + m.x8 + m.x55 >= 0)

m.c19 = Constraint(expr= - m.x7 + m.x8 + m.x56 >= 0)

m.c20 = Constraint(expr=   m.x5 - m.x6 + m.x51 >= 0)

m.c21 = Constraint(expr=   m.x5 - m.x7 + m.x52 >= 0)

m.c22 = Constraint(expr=   m.x5 - m.x8 + m.x53 >= 0)

m.c23 = Constraint(expr=   m.x6 - m.x7 + m.x54 >= 0)

m.c24 = Constraint(expr=   m.x6 - m.x8 + m.x55 >= 0)

m.c25 = Constraint(expr=   m.x7 - m.x8 + m.x56 >= 0)

m.c26 = Constraint(expr=   m.x1 - m.x2 + 46*m.b9 <= 40)

m.c27 = Constraint(expr=   m.x1 - m.x3 + 46*m.b10 <= 42)

m.c28 = Constraint(expr=   m.x1 - m.x4 + 46*m.b11 <= 42.5)

m.c29 = Constraint(expr=   m.x2 - m.x3 + 46*m.b12 <= 41)

m.c30 = Constraint(expr=   m.x2 - m.x4 + 46*m.b13 <= 41.5)

m.c31 = Constraint(expr=   m.x3 - m.x4 + 46*m.b14 <= 43.5)

m.c32 = Constraint(expr= - m.x1 + m.x2 + 46*m.b15 <= 40)

m.c33 = Constraint(expr= - m.x1 + m.x3 + 46*m.b16 <= 42)

m.c34 = Constraint(expr= - m.x1 + m.x4 + 46*m.b17 <= 42.5)

m.c35 = Constraint(expr= - m.x2 + m.x3 + 46*m.b18 <= 41)

m.c36 = Constraint(expr= - m.x2 + m.x4 + 46*m.b19 <= 41.5)

m.c37 = Constraint(expr= - m.x3 + m.x4 + 46*m.b20 <= 43.5)

m.c38 = Constraint(expr=   m.x5 - m.x6 + 81*m.b21 <= 75.5)

m.c39 = Constraint(expr=   m.x5 - m.x7 + 81*m.b22 <= 76.5)

m.c40 = Constraint(expr=   m.x5 - m.x8 + 81*m.b23 <= 76.5)

m.c41 = Constraint(expr=   m.x6 - m.x7 + 81*m.b24 <= 77)

m.c42 = Constraint(expr=   m.x6 - m.x8 + 81*m.b25 <= 77)

m.c43 = Constraint(expr=   m.x7 - m.x8 + 81*m.b26 <= 78)

m.c44 = Constraint(expr= - m.x5 + m.x6 + 81*m.b27 <= 75.5)

m.c45 = Constraint(expr= - m.x5 + m.x7 + 81*m.b28 <= 76.5)

m.c46 = Constraint(expr= - m.x5 + m.x8 + 81*m.b29 <= 76.5)

m.c47 = Constraint(expr= - m.x6 + m.x7 + 81*m.b30 <= 77)

m.c48 = Constraint(expr= - m.x6 + m.x8 + 81*m.b31 <= 77)

m.c49 = Constraint(expr= - m.x7 + m.x8 + 81*m.b32 <= 78)

m.c50 = Constraint(expr=   m.b9 + m.b15 + m.b21 + m.b27 == 1)

m.c51 = Constraint(expr=   m.b10 + m.b16 + m.b22 + m.b28 == 1)

m.c52 = Constraint(expr=   m.b11 + m.b17 + m.b23 + m.b29 == 1)

m.c53 = Constraint(expr=   m.b12 + m.b18 + m.b24 + m.b30 == 1)

m.c54 = Constraint(expr=   m.b13 + m.b19 + m.b25 + m.b31 == 1)

m.c55 = Constraint(expr=   m.b14 + m.b20 + m.b26 + m.b32 == 1)

m.c56 = Constraint(expr=(-17.5 + m.x1)**2 + (-7 + m.x5)**2 + 6814*m.b33 <= 6850)

m.c57 = Constraint(expr=(-18.5 + m.x2)**2 + (-7.5 + m.x6)**2 + 6678*m.b34 <= 6714)

m.c58 = Constraint(expr=(-16.5 + m.x3)**2 + (-8.5 + m.x7)**2 + 6958*m.b35 <= 6994)

m.c59 = Constraint(expr=(-16 + m.x4)**2 + (-8.5 + m.x8)**2 + 7033*m.b36 <= 7069)

m.c60 = Constraint(expr=(-52.5 + m.x1)**2 + (-77 + m.x5)**2 + 6556*m.b37 <= 6581)

m.c61 = Constraint(expr=(-53.5 + m.x2)**2 + (-77.5 + m.x6)**2 + 6697*m.b38 <= 6722)

m.c62 = Constraint(expr=(-51.5 + m.x3)**2 + (-78.5 + m.x7)**2 + 6985*m.b39 <= 7010)

m.c63 = Constraint(expr=(-51 + m.x4)**2 + (-78.5 + m.x8)**2 + 6985*m.b40 <= 7010)

m.c64 = Constraint(expr=(-32.5 + m.x1)**2 + (-47 + m.x5)**2 + 2025*m.b41 <= 2041)

m.c65 = Constraint(expr=(-33.5 + m.x2)**2 + (-47.5 + m.x6)**2 + 2106*m.b42 <= 2122)

m.c66 = Constraint(expr=(-31.5 + m.x3)**2 + (-48.5 + m.x7)**2 + 2317*m.b43 <= 2333)

m.c67 = Constraint(expr=(-31 + m.x4)**2 + (-48.5 + m.x8)**2 + 2362*m.b44 <= 2378)

m.c68 = Constraint(expr=(-17.5 + m.x1)**2 + (-13 + m.x5)**2 + 5950*m.b33 <= 5986)

m.c69 = Constraint(expr=(-18.5 + m.x2)**2 + (-12.5 + m.x6)**2 + 5953*m.b34 <= 5989)

m.c70 = Constraint(expr=(-16.5 + m.x3)**2 + (-11.5 + m.x7)**2 + 6517*m.b35 <= 6553)

m.c71 = Constraint(expr=(-16 + m.x4)**2 + (-11.5 + m.x8)**2 + 6592*m.b36 <= 6628)

m.c72 = Constraint(expr=(-52.5 + m.x1)**2 + (-83 + m.x5)**2 + 7432*m.b37 <= 7457)

m.c73 = Constraint(expr=(-53.5 + m.x2)**2 + (-82.5 + m.x6)**2 + 7432*m.b38 <= 7457)

m.c74 = Constraint(expr=(-51.5 + m.x3)**2 + (-81.5 + m.x7)**2 + 7432*m.b39 <= 7457)

m.c75 = Constraint(expr=(-51 + m.x4)**2 + (-81.5 + m.x8)**2 + 7432*m.b40 <= 7457)

m.c76 = Constraint(expr=(-32.5 + m.x1)**2 + (-53 + m.x5)**2 + 2541*m.b41 <= 2557)

m.c77 = Constraint(expr=(-33.5 + m.x2)**2 + (-52.5 + m.x6)**2 + 2541*m.b42 <= 2557)

m.c78 = Constraint(expr=(-31.5 + m.x3)**2 + (-51.5 + m.x7)**2 + 2584*m.b43 <= 2600)

m.c79 = Constraint(expr=(-31 + m.x4)**2 + (-51.5 + m.x8)**2 + 2629*m.b44 <= 2645)

m.c80 = Constraint(expr=(-12.5 + m.x1)**2 + (-7 + m.x5)**2 + 7189*m.b33 <= 7225)

m.c81 = Constraint(expr=(-11.5 + m.x2)**2 + (-7.5 + m.x6)**2 + 7189*m.b34 <= 7225)

m.c82 = Constraint(expr=(-13.5 + m.x3)**2 + (-8.5 + m.x7)**2 + 7189*m.b35 <= 7225)

m.c83 = Constraint(expr=(-14 + m.x4)**2 + (-8.5 + m.x8)**2 + 7189*m.b36 <= 7225)

m.c84 = Constraint(expr=(-47.5 + m.x1)**2 + (-77 + m.x5)**2 + 6171*m.b37 <= 6196)

m.c85 = Constraint(expr=(-46.5 + m.x2)**2 + (-77.5 + m.x6)**2 + 6172*m.b38 <= 6197)

m.c86 = Constraint(expr=(-48.5 + m.x3)**2 + (-78.5 + m.x7)**2 + 6748*m.b39 <= 6773)

m.c87 = Constraint(expr=(-49 + m.x4)**2 + (-78.5 + m.x8)**2 + 6825*m.b40 <= 6850)

m.c88 = Constraint(expr=(-27.5 + m.x1)**2 + (-47 + m.x5)**2 + 2209*m.b41 <= 2225)

m.c89 = Constraint(expr=(-26.5 + m.x2)**2 + (-47.5 + m.x6)**2 + 2290*m.b42 <= 2306)

m.c90 = Constraint(expr=(-28.5 + m.x3)**2 + (-48.5 + m.x7)**2 + 2458*m.b43 <= 2474)

m.c91 = Constraint(expr=(-29 + m.x4)**2 + (-48.5 + m.x8)**2 + 2458*m.b44 <= 2474)

m.c92 = Constraint(expr=(-12.5 + m.x1)**2 + (-13 + m.x5)**2 + 6325*m.b33 <= 6361)

m.c93 = Constraint(expr=(-11.5 + m.x2)**2 + (-12.5 + m.x6)**2 + 6464*m.b34 <= 6500)

m.c94 = Constraint(expr=(-13.5 + m.x3)**2 + (-11.5 + m.x7)**2 + 6748*m.b35 <= 6784)

m.c95 = Constraint(expr=(-14 + m.x4)**2 + (-11.5 + m.x8)**2 + 6748*m.b36 <= 6784)

m.c96 = Constraint(expr=(-47.5 + m.x1)**2 + (-83 + m.x5)**2 + 7047*m.b37 <= 7072)

m.c97 = Constraint(expr=(-46.5 + m.x2)**2 + (-82.5 + m.x6)**2 + 6907*m.b38 <= 6932)

m.c98 = Constraint(expr=(-48.5 + m.x3)**2 + (-81.5 + m.x7)**2 + 7195*m.b39 <= 7220)

m.c99 = Constraint(expr=(-49 + m.x4)**2 + (-81.5 + m.x8)**2 + 7272*m.b40 <= 7297)

m.c100 = Constraint(expr=(-27.5 + m.x1)**2 + (-53 + m.x5)**2 + 2725*m.b41 <= 2741)

m.c101 = Constraint(expr=(-26.5 + m.x2)**2 + (-52.5 + m.x6)**2 + 2725*m.b42 <= 2741)

m.c102 = Constraint(expr=(-28.5 + m.x3)**2 + (-51.5 + m.x7)**2 + 2725*m.b43 <= 2741)

m.c103 = Constraint(expr=(-29 + m.x4)**2 + (-51.5 + m.x8)**2 + 2725*m.b44 <= 2741)

m.c104 = Constraint(expr=   m.b33 + m.b37 + m.b41 == 1)

m.c105 = Constraint(expr=   m.b34 + m.b38 + m.b42 == 1)

m.c106 = Constraint(expr=   m.b35 + m.b39 + m.b43 == 1)

m.c107 = Constraint(expr=   m.b36 + m.b40 + m.b44 == 1)
