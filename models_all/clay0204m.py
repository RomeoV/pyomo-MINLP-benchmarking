#  MINLP written by GAMS Convert at 05/15/20 00:50:43
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         91       11       24       56        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         53       21       32        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        285      221       64        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(11.5,57.5),initialize=11.5)
m.x2 = Var(within=Reals,bounds=(12.5,56.5),initialize=12.5)
m.x3 = Var(within=Reals,bounds=(10.5,58.5),initialize=10.5)
m.x4 = Var(within=Reals,bounds=(10,59),initialize=10)
m.x5 = Var(within=Reals,bounds=(7,87),initialize=7)
m.x6 = Var(within=Reals,bounds=(6.5,87.5),initialize=6.5)
m.x7 = Var(within=Reals,bounds=(5.5,88.5),initialize=5.5)
m.x8 = Var(within=Reals,bounds=(5.5,88.5),initialize=5.5)
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
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   300*m.x41 + 240*m.x42 + 210*m.x43 + 100*m.x44 + 150*m.x45 + 120*m.x46 + 300*m.x47 + 240*m.x48
                        + 210*m.x49 + 100*m.x50 + 150*m.x51 + 120*m.x52, sense=minimize)

m.c2 = Constraint(expr= - m.x1 + m.x2 + m.x41 >= 0)

m.c3 = Constraint(expr= - m.x1 + m.x3 + m.x42 >= 0)

m.c4 = Constraint(expr= - m.x1 + m.x4 + m.x43 >= 0)

m.c5 = Constraint(expr= - m.x2 + m.x3 + m.x44 >= 0)

m.c6 = Constraint(expr= - m.x2 + m.x4 + m.x45 >= 0)

m.c7 = Constraint(expr= - m.x3 + m.x4 + m.x46 >= 0)

m.c8 = Constraint(expr=   m.x1 - m.x2 + m.x41 >= 0)

m.c9 = Constraint(expr=   m.x1 - m.x3 + m.x42 >= 0)

m.c10 = Constraint(expr=   m.x1 - m.x4 + m.x43 >= 0)

m.c11 = Constraint(expr=   m.x2 - m.x3 + m.x44 >= 0)

m.c12 = Constraint(expr=   m.x2 - m.x4 + m.x45 >= 0)

m.c13 = Constraint(expr=   m.x3 - m.x4 + m.x46 >= 0)

m.c14 = Constraint(expr= - m.x5 + m.x6 + m.x47 >= 0)

m.c15 = Constraint(expr= - m.x5 + m.x7 + m.x48 >= 0)

m.c16 = Constraint(expr= - m.x5 + m.x8 + m.x49 >= 0)

m.c17 = Constraint(expr= - m.x6 + m.x7 + m.x50 >= 0)

m.c18 = Constraint(expr= - m.x6 + m.x8 + m.x51 >= 0)

m.c19 = Constraint(expr= - m.x7 + m.x8 + m.x52 >= 0)

m.c20 = Constraint(expr=   m.x5 - m.x6 + m.x47 >= 0)

m.c21 = Constraint(expr=   m.x5 - m.x7 + m.x48 >= 0)

m.c22 = Constraint(expr=   m.x5 - m.x8 + m.x49 >= 0)

m.c23 = Constraint(expr=   m.x6 - m.x7 + m.x50 >= 0)

m.c24 = Constraint(expr=   m.x6 - m.x8 + m.x51 >= 0)

m.c25 = Constraint(expr=   m.x7 - m.x8 + m.x52 >= 0)

m.c26 = Constraint(expr=   m.x1 - m.x2 + 51*m.b9 <= 45)

m.c27 = Constraint(expr=   m.x1 - m.x3 + 51*m.b10 <= 47)

m.c28 = Constraint(expr=   m.x1 - m.x4 + 51*m.b11 <= 47.5)

m.c29 = Constraint(expr=   m.x2 - m.x3 + 51*m.b12 <= 46)

m.c30 = Constraint(expr=   m.x2 - m.x4 + 51*m.b13 <= 46.5)

m.c31 = Constraint(expr=   m.x3 - m.x4 + 51*m.b14 <= 48.5)

m.c32 = Constraint(expr= - m.x1 + m.x2 + 51*m.b15 <= 45)

m.c33 = Constraint(expr= - m.x1 + m.x3 + 51*m.b16 <= 47)

m.c34 = Constraint(expr= - m.x1 + m.x4 + 51*m.b17 <= 47.5)

m.c35 = Constraint(expr= - m.x2 + m.x3 + 51*m.b18 <= 46)

m.c36 = Constraint(expr= - m.x2 + m.x4 + 51*m.b19 <= 46.5)

m.c37 = Constraint(expr= - m.x3 + m.x4 + 51*m.b20 <= 48.5)

m.c38 = Constraint(expr=   m.x5 - m.x6 + 86*m.b21 <= 80.5)

m.c39 = Constraint(expr=   m.x5 - m.x7 + 86*m.b22 <= 81.5)

m.c40 = Constraint(expr=   m.x5 - m.x8 + 86*m.b23 <= 81.5)

m.c41 = Constraint(expr=   m.x6 - m.x7 + 86*m.b24 <= 82)

m.c42 = Constraint(expr=   m.x6 - m.x8 + 86*m.b25 <= 82)

m.c43 = Constraint(expr=   m.x7 - m.x8 + 86*m.b26 <= 83)

m.c44 = Constraint(expr= - m.x5 + m.x6 + 86*m.b27 <= 80.5)

m.c45 = Constraint(expr= - m.x5 + m.x7 + 86*m.b28 <= 81.5)

m.c46 = Constraint(expr= - m.x5 + m.x8 + 86*m.b29 <= 81.5)

m.c47 = Constraint(expr= - m.x6 + m.x7 + 86*m.b30 <= 82)

m.c48 = Constraint(expr= - m.x6 + m.x8 + 86*m.b31 <= 82)

m.c49 = Constraint(expr= - m.x7 + m.x8 + 86*m.b32 <= 83)

m.c50 = Constraint(expr=   m.b9 + m.b15 + m.b21 + m.b27 == 1)

m.c51 = Constraint(expr=   m.b10 + m.b16 + m.b22 + m.b28 == 1)

m.c52 = Constraint(expr=   m.b11 + m.b17 + m.b23 + m.b29 == 1)

m.c53 = Constraint(expr=   m.b12 + m.b18 + m.b24 + m.b30 == 1)

m.c54 = Constraint(expr=   m.b13 + m.b19 + m.b25 + m.b31 == 1)

m.c55 = Constraint(expr=   m.b14 + m.b20 + m.b26 + m.b32 == 1)

m.c56 = Constraint(expr=(-17.5 + m.x1)**2 + (-7 + m.x5)**2 + 7964*m.b33 <= 8000)

m.c57 = Constraint(expr=(-18.5 + m.x2)**2 + (-7.5 + m.x6)**2 + 7808*m.b34 <= 7844)

m.c58 = Constraint(expr=(-16.5 + m.x3)**2 + (-8.5 + m.x7)**2 + 8128*m.b35 <= 8164)

m.c59 = Constraint(expr=(-16 + m.x4)**2 + (-8.5 + m.x8)**2 + 8213*m.b36 <= 8249)

m.c60 = Constraint(expr=(-52.5 + m.x1)**2 + (-77 + m.x5)**2 + 6481*m.b37 <= 6581)

m.c61 = Constraint(expr=(-53.5 + m.x2)**2 + (-77.5 + m.x6)**2 + 6622*m.b38 <= 6722)

m.c62 = Constraint(expr=(-51.5 + m.x3)**2 + (-78.5 + m.x7)**2 + 6951.25*m.b39 <= 7051.25)

m.c63 = Constraint(expr=(-51 + m.x4)**2 + (-78.5 + m.x8)**2 + 6910*m.b40 <= 7010)

m.c64 = Constraint(expr=(-17.5 + m.x1)**2 + (-13 + m.x5)**2 + 7040*m.b33 <= 7076)

m.c65 = Constraint(expr=(-18.5 + m.x2)**2 + (-12.5 + m.x6)**2 + 7033*m.b34 <= 7069)

m.c66 = Constraint(expr=(-16.5 + m.x3)**2 + (-11.5 + m.x7)**2 + 7657*m.b35 <= 7693)

m.c67 = Constraint(expr=(-16 + m.x4)**2 + (-11.5 + m.x8)**2 + 7742*m.b36 <= 7778)

m.c68 = Constraint(expr=(-52.5 + m.x1)**2 + (-83 + m.x5)**2 + 7357*m.b37 <= 7457)

m.c69 = Constraint(expr=(-53.5 + m.x2)**2 + (-82.5 + m.x6)**2 + 7357*m.b38 <= 7457)

m.c70 = Constraint(expr=(-51.5 + m.x3)**2 + (-81.5 + m.x7)**2 + 7398.25*m.b39 <= 7498.25)

m.c71 = Constraint(expr=(-51 + m.x4)**2 + (-81.5 + m.x8)**2 + 7357*m.b40 <= 7457)

m.c72 = Constraint(expr=(-12.5 + m.x1)**2 + (-7 + m.x5)**2 + 8389*m.b33 <= 8425)

m.c73 = Constraint(expr=(-11.5 + m.x2)**2 + (-7.5 + m.x6)**2 + 8389*m.b34 <= 8425)

m.c74 = Constraint(expr=(-13.5 + m.x3)**2 + (-8.5 + m.x7)**2 + 8389*m.b35 <= 8425)

m.c75 = Constraint(expr=(-14 + m.x4)**2 + (-8.5 + m.x8)**2 + 8389*m.b36 <= 8425)

m.c76 = Constraint(expr=(-47.5 + m.x1)**2 + (-77 + m.x5)**2 + 6096*m.b37 <= 6196)

m.c77 = Constraint(expr=(-46.5 + m.x2)**2 + (-77.5 + m.x6)**2 + 6097*m.b38 <= 6197)

m.c78 = Constraint(expr=(-48.5 + m.x3)**2 + (-78.5 + m.x7)**2 + 6711.25*m.b39 <= 6811.25)

m.c79 = Constraint(expr=(-49 + m.x4)**2 + (-78.5 + m.x8)**2 + 6750*m.b40 <= 6850)

m.c80 = Constraint(expr=(-12.5 + m.x1)**2 + (-13 + m.x5)**2 + 7465*m.b33 <= 7501)

m.c81 = Constraint(expr=(-11.5 + m.x2)**2 + (-12.5 + m.x6)**2 + 7614*m.b34 <= 7650)

m.c82 = Constraint(expr=(-13.5 + m.x3)**2 + (-11.5 + m.x7)**2 + 7918*m.b35 <= 7954)

m.c83 = Constraint(expr=(-14 + m.x4)**2 + (-11.5 + m.x8)**2 + 7918*m.b36 <= 7954)

m.c84 = Constraint(expr=(-47.5 + m.x1)**2 + (-83 + m.x5)**2 + 6972*m.b37 <= 7072)

m.c85 = Constraint(expr=(-46.5 + m.x2)**2 + (-82.5 + m.x6)**2 + 6832*m.b38 <= 6932)

m.c86 = Constraint(expr=(-48.5 + m.x3)**2 + (-81.5 + m.x7)**2 + 7158.25*m.b39 <= 7258.25)

m.c87 = Constraint(expr=(-49 + m.x4)**2 + (-81.5 + m.x8)**2 + 7197*m.b40 <= 7297)

m.c88 = Constraint(expr=   m.b33 + m.b37 == 1)

m.c89 = Constraint(expr=   m.b34 + m.b38 == 1)

m.c90 = Constraint(expr=   m.b35 + m.b39 == 1)

m.c91 = Constraint(expr=   m.b36 + m.b40 == 1)
