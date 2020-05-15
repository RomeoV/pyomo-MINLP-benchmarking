#  MINLP written by GAMS Convert at 05/15/20 00:50:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         67        7       12       48        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         34       13       21        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        208      136       72        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(11.5,52.5),initialize=11.5)
m.x2 = Var(within=Reals,bounds=(12.5,51.5),initialize=12.5)
m.x3 = Var(within=Reals,bounds=(10.5,53.5),initialize=10.5)
m.x4 = Var(within=Reals,bounds=(7,82),initialize=7)
m.x5 = Var(within=Reals,bounds=(6.5,82.5),initialize=6.5)
m.x6 = Var(within=Reals,bounds=(5.5,83.5),initialize=5.5)
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
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   300*m.x28 + 240*m.x29 + 100*m.x30 + 300*m.x31 + 240*m.x32 + 100*m.x33, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x28 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x29 >= 0)

m.c4 = Constraint(expr= - m.x2 + m.x3 + m.x30 >= 0)

m.c5 = Constraint(expr=   m.x1 - m.x2 + m.x28 >= 0)

m.c6 = Constraint(expr=   m.x1 - m.x3 + m.x29 >= 0)

m.c7 = Constraint(expr=   m.x2 - m.x3 + m.x30 >= 0)

m.c8 = Constraint(expr= - m.x4 + m.x5 + m.x31 >= 0)

m.c9 = Constraint(expr= - m.x4 + m.x6 + m.x32 >= 0)

m.c10 = Constraint(expr= - m.x5 + m.x6 + m.x33 >= 0)

m.c11 = Constraint(expr=   m.x4 - m.x5 + m.x31 >= 0)

m.c12 = Constraint(expr=   m.x4 - m.x6 + m.x32 >= 0)

m.c13 = Constraint(expr=   m.x5 - m.x6 + m.x33 >= 0)

m.c14 = Constraint(expr=   m.x1 - m.x2 + 46*m.b7 <= 40)

m.c15 = Constraint(expr=   m.x1 - m.x3 + 46*m.b8 <= 42)

m.c16 = Constraint(expr=   m.x2 - m.x3 + 46*m.b9 <= 41)

m.c17 = Constraint(expr= - m.x1 + m.x2 + 46*m.b10 <= 40)

m.c18 = Constraint(expr= - m.x1 + m.x3 + 46*m.b11 <= 42)

m.c19 = Constraint(expr= - m.x2 + m.x3 + 46*m.b12 <= 41)

m.c20 = Constraint(expr=   m.x4 - m.x5 + 81*m.b13 <= 75.5)

m.c21 = Constraint(expr=   m.x4 - m.x6 + 81*m.b14 <= 76.5)

m.c22 = Constraint(expr=   m.x5 - m.x6 + 81*m.b15 <= 77)

m.c23 = Constraint(expr= - m.x4 + m.x5 + 81*m.b16 <= 75.5)

m.c24 = Constraint(expr= - m.x4 + m.x6 + 81*m.b17 <= 76.5)

m.c25 = Constraint(expr= - m.x5 + m.x6 + 81*m.b18 <= 77)

m.c26 = Constraint(expr=   m.b7 + m.b10 + m.b13 + m.b16 == 1)

m.c27 = Constraint(expr=   m.b8 + m.b11 + m.b14 + m.b17 == 1)

m.c28 = Constraint(expr=   m.b9 + m.b12 + m.b15 + m.b18 == 1)

m.c29 = Constraint(expr=(-17.5 + m.x1)**2 + (-7 + m.x4)**2 + 6814*m.b19 <= 6850)

m.c30 = Constraint(expr=(-18.5 + m.x2)**2 + (-7.5 + m.x5)**2 + 6678*m.b20 <= 6714)

m.c31 = Constraint(expr=(-16.5 + m.x3)**2 + (-8.5 + m.x6)**2 + 6958*m.b21 <= 6994)

m.c32 = Constraint(expr=(-52.5 + m.x1)**2 + (-77 + m.x4)**2 + 6556*m.b22 <= 6581)

m.c33 = Constraint(expr=(-53.5 + m.x2)**2 + (-77.5 + m.x5)**2 + 6697*m.b23 <= 6722)

m.c34 = Constraint(expr=(-51.5 + m.x3)**2 + (-78.5 + m.x6)**2 + 6985*m.b24 <= 7010)

m.c35 = Constraint(expr=(-32.5 + m.x1)**2 + (-47 + m.x4)**2 + 2025*m.b25 <= 2041)

m.c36 = Constraint(expr=(-33.5 + m.x2)**2 + (-47.5 + m.x5)**2 + 2106*m.b26 <= 2122)

m.c37 = Constraint(expr=(-31.5 + m.x3)**2 + (-48.5 + m.x6)**2 + 2317*m.b27 <= 2333)

m.c38 = Constraint(expr=(-17.5 + m.x1)**2 + (-13 + m.x4)**2 + 5950*m.b19 <= 5986)

m.c39 = Constraint(expr=(-18.5 + m.x2)**2 + (-12.5 + m.x5)**2 + 5953*m.b20 <= 5989)

m.c40 = Constraint(expr=(-16.5 + m.x3)**2 + (-11.5 + m.x6)**2 + 6517*m.b21 <= 6553)

m.c41 = Constraint(expr=(-52.5 + m.x1)**2 + (-83 + m.x4)**2 + 7432*m.b22 <= 7457)

m.c42 = Constraint(expr=(-53.5 + m.x2)**2 + (-82.5 + m.x5)**2 + 7432*m.b23 <= 7457)

m.c43 = Constraint(expr=(-51.5 + m.x3)**2 + (-81.5 + m.x6)**2 + 7432*m.b24 <= 7457)

m.c44 = Constraint(expr=(-32.5 + m.x1)**2 + (-53 + m.x4)**2 + 2541*m.b25 <= 2557)

m.c45 = Constraint(expr=(-33.5 + m.x2)**2 + (-52.5 + m.x5)**2 + 2541*m.b26 <= 2557)

m.c46 = Constraint(expr=(-31.5 + m.x3)**2 + (-51.5 + m.x6)**2 + 2584*m.b27 <= 2600)

m.c47 = Constraint(expr=(-12.5 + m.x1)**2 + (-7 + m.x4)**2 + 7189*m.b19 <= 7225)

m.c48 = Constraint(expr=(-11.5 + m.x2)**2 + (-7.5 + m.x5)**2 + 7189*m.b20 <= 7225)

m.c49 = Constraint(expr=(-13.5 + m.x3)**2 + (-8.5 + m.x6)**2 + 7189*m.b21 <= 7225)

m.c50 = Constraint(expr=(-47.5 + m.x1)**2 + (-77 + m.x4)**2 + 6171*m.b22 <= 6196)

m.c51 = Constraint(expr=(-46.5 + m.x2)**2 + (-77.5 + m.x5)**2 + 6172*m.b23 <= 6197)

m.c52 = Constraint(expr=(-48.5 + m.x3)**2 + (-78.5 + m.x6)**2 + 6748*m.b24 <= 6773)

m.c53 = Constraint(expr=(-27.5 + m.x1)**2 + (-47 + m.x4)**2 + 2209*m.b25 <= 2225)

m.c54 = Constraint(expr=(-26.5 + m.x2)**2 + (-47.5 + m.x5)**2 + 2290*m.b26 <= 2306)

m.c55 = Constraint(expr=(-28.5 + m.x3)**2 + (-48.5 + m.x6)**2 + 2458*m.b27 <= 2474)

m.c56 = Constraint(expr=(-12.5 + m.x1)**2 + (-13 + m.x4)**2 + 6325*m.b19 <= 6361)

m.c57 = Constraint(expr=(-11.5 + m.x2)**2 + (-12.5 + m.x5)**2 + 6464*m.b20 <= 6500)

m.c58 = Constraint(expr=(-13.5 + m.x3)**2 + (-11.5 + m.x6)**2 + 6748*m.b21 <= 6784)

m.c59 = Constraint(expr=(-47.5 + m.x1)**2 + (-83 + m.x4)**2 + 7047*m.b22 <= 7072)

m.c60 = Constraint(expr=(-46.5 + m.x2)**2 + (-82.5 + m.x5)**2 + 6907*m.b23 <= 6932)

m.c61 = Constraint(expr=(-48.5 + m.x3)**2 + (-81.5 + m.x6)**2 + 7195*m.b24 <= 7220)

m.c62 = Constraint(expr=(-27.5 + m.x1)**2 + (-53 + m.x4)**2 + 2725*m.b25 <= 2741)

m.c63 = Constraint(expr=(-26.5 + m.x2)**2 + (-52.5 + m.x5)**2 + 2725*m.b26 <= 2741)

m.c64 = Constraint(expr=(-28.5 + m.x3)**2 + (-51.5 + m.x6)**2 + 2725*m.b27 <= 2741)

m.c65 = Constraint(expr=   m.b19 + m.b22 + m.b25 == 1)

m.c66 = Constraint(expr=   m.b20 + m.b23 + m.b26 == 1)

m.c67 = Constraint(expr=   m.b21 + m.b24 + m.b27 == 1)
