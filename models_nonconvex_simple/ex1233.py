#  MINLP written by GAMS Convert at 08/13/20 17:37:52
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         65       21        0       44        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         53       41       12        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        221      193       28        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(370,650),initialize=370)
m.x2 = Var(within=Reals,bounds=(370,650),initialize=370)
m.x3 = Var(within=Reals,bounds=(370,650),initialize=370)
m.x4 = Var(within=Reals,bounds=(370,590),initialize=370)
m.x5 = Var(within=Reals,bounds=(370,590),initialize=370)
m.x6 = Var(within=Reals,bounds=(370,590),initialize=370)
m.x7 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x8 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x9 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x10 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x11 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x12 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x13 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x14 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x15 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x16 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x17 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x18 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x19 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x25 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x26 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x27 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x28 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x29 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x30 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x31 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x32 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x33 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x34 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x35 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x36 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x37 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x38 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x39 = Var(within=Reals,bounds=(10,None),initialize=10)
m.x40 = Var(within=Reals,bounds=(10,None),initialize=10)
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

m.obj = Objective(expr=300*m.x13/(0.5*m.x25*m.x26*(m.x25 + m.x26))**0.3333 + 300*m.x14/(0.5*m.x26*m.x27*(m.x26 + m.x27))
                       **0.3333 + 300*m.x15/(0.5*m.x28*m.x29*(m.x28 + m.x29))**0.3333 + 300*m.x16/(0.5*m.x29*m.x30*(
                       m.x29 + m.x30))**0.3333 + 300*m.x17/(0.5*m.x31*m.x32*(m.x31 + m.x32))**0.3333 + 300*m.x18/(0.5*
                       m.x32*m.x33*(m.x32 + m.x33))**0.3333 + 300*m.x19/(0.5*m.x34*m.x35*(m.x34 + m.x35))**0.3333 + 300*
                       m.x20/(0.5*m.x35*m.x36*(m.x35 + m.x36))**0.3333 + 300*m.x21/(35*m.x37*(70 + m.x37))**0.33333 + 
                       300*m.x22/(35*m.x38*(70 + m.x38))**0.33333 + 180*m.x23/(15*m.x39*(30 + m.x39))**0.33333 + 180*
                       m.x24/(90*m.x40*(180 + m.x40))**0.33333 + 80*m.x23 + 80*m.x24 + 15*m.x21 + 15*m.x22 + 5500*m.b41
                        + 5500*m.b42 + 5500*m.b43 + 5500*m.b44 + 5500*m.b45 + 5500*m.b46 + 5500*m.b47 + 5500*m.b48
                        + 5500*m.b49 + 5500*m.b50 + 5500*m.b51 + 5500*m.b52, sense=minimize)

m.c2 = Constraint(expr=   m.x13 + m.x14 + m.x15 + m.x16 + m.x21 == 2800)

m.c3 = Constraint(expr=   m.x17 + m.x18 + m.x19 + m.x20 + m.x22 == 4400)

m.c4 = Constraint(expr=   m.x13 + m.x14 + m.x17 + m.x18 + m.x23 == 3600)

m.c5 = Constraint(expr=   m.x15 + m.x16 + m.x19 + m.x20 + m.x24 == 1950)

m.c6 = Constraint(expr=   10*m.x1 - 10*m.x2 - m.x13 - m.x15 == 0)

m.c7 = Constraint(expr=   10*m.x2 - 10*m.x3 - m.x14 - m.x16 == 0)

m.c8 = Constraint(expr=   20*m.x4 - 20*m.x5 - m.x17 - m.x19 == 0)

m.c9 = Constraint(expr=   20*m.x5 - 20*m.x6 - m.x18 - m.x20 == 0)

m.c10 = Constraint(expr=   15*m.x7 - 15*m.x8 - m.x13 - m.x17 == 0)

m.c11 = Constraint(expr=   15*m.x8 - 15*m.x9 - m.x14 - m.x18 == 0)

m.c12 = Constraint(expr=   13*m.x10 - 13*m.x11 - m.x15 - m.x19 == 0)

m.c13 = Constraint(expr=   13*m.x11 - 13*m.x12 - m.x16 - m.x20 == 0)

m.c14 = Constraint(expr=   m.x1 == 650)

m.c15 = Constraint(expr=   m.x4 == 590)

m.c16 = Constraint(expr=   m.x9 == 410)

m.c17 = Constraint(expr=   m.x12 == 350)

m.c18 = Constraint(expr= - m.x1 + m.x2 <= 0)

m.c19 = Constraint(expr= - m.x2 + m.x3 <= 0)

m.c20 = Constraint(expr= - m.x4 + m.x5 <= 0)

m.c21 = Constraint(expr= - m.x5 + m.x6 <= 0)

m.c22 = Constraint(expr= - m.x7 + m.x8 <= 0)

m.c23 = Constraint(expr= - m.x8 + m.x9 <= 0)

m.c24 = Constraint(expr= - m.x10 + m.x11 <= 0)

m.c25 = Constraint(expr= - m.x11 + m.x12 <= 0)

m.c26 = Constraint(expr= - m.x3 <= -370)

m.c27 = Constraint(expr= - m.x6 <= -370)

m.c28 = Constraint(expr=   m.x7 <= 650)

m.c29 = Constraint(expr=   m.x10 <= 500)

m.c30 = Constraint(expr=   10*m.x3 - m.x21 == 3700)

m.c31 = Constraint(expr=   20*m.x6 - m.x22 == 7400)

m.c32 = Constraint(expr=   15*m.x7 + m.x23 == 9750)

m.c33 = Constraint(expr=   13*m.x10 + m.x24 == 6500)

m.c34 = Constraint(expr=   m.x13 - 2800*m.b41 <= 0)

m.c35 = Constraint(expr=   m.x14 - 2800*m.b42 <= 0)

m.c36 = Constraint(expr=   m.x15 - 1950*m.b43 <= 0)

m.c37 = Constraint(expr=   m.x16 - 1950*m.b44 <= 0)

m.c38 = Constraint(expr=   m.x17 - 3600*m.b45 <= 0)

m.c39 = Constraint(expr=   m.x18 - 3600*m.b46 <= 0)

m.c40 = Constraint(expr=   m.x19 - 1950*m.b47 <= 0)

m.c41 = Constraint(expr=   m.x20 - 1950*m.b48 <= 0)

m.c42 = Constraint(expr=   m.x21 - 2800*m.b49 <= 0)

m.c43 = Constraint(expr=   m.x22 - 4400*m.b50 <= 0)

m.c44 = Constraint(expr=   m.x23 - 3600*m.b51 <= 0)

m.c45 = Constraint(expr=   m.x24 - 1950*m.b52 <= 0)

m.c46 = Constraint(expr= - m.x1 + m.x7 + m.x25 + 280*m.b41 <= 280)

m.c47 = Constraint(expr= - m.x2 + m.x8 + m.x26 + 130*m.b42 <= 130)

m.c48 = Constraint(expr= - m.x1 + m.x10 + m.x28 + 280*m.b43 <= 280)

m.c49 = Constraint(expr= - m.x2 + m.x11 + m.x29 + 150*m.b44 <= 150)

m.c50 = Constraint(expr= - m.x4 + m.x7 + m.x31 + 280*m.b45 <= 280)

m.c51 = Constraint(expr= - m.x5 + m.x8 + m.x32 + 130*m.b46 <= 130)

m.c52 = Constraint(expr= - m.x4 + m.x10 + m.x34 + 280*m.b47 <= 280)

m.c53 = Constraint(expr= - m.x5 + m.x11 + m.x35 + 150*m.b48 <= 150)

m.c54 = Constraint(expr= - m.x2 + m.x8 + m.x26 + 280*m.b41 <= 280)

m.c55 = Constraint(expr= - m.x3 + m.x9 + m.x27 + 130*m.b42 <= 130)

m.c56 = Constraint(expr= - m.x2 + m.x11 + m.x29 + 280*m.b43 <= 280)

m.c57 = Constraint(expr= - m.x3 + m.x12 + m.x30 + 150*m.b44 <= 150)

m.c58 = Constraint(expr= - m.x5 + m.x8 + m.x32 + 280*m.b45 <= 280)

m.c59 = Constraint(expr= - m.x6 + m.x9 + m.x33 + 130*m.b46 <= 130)

m.c60 = Constraint(expr= - m.x5 + m.x11 + m.x35 + 280*m.b47 <= 280)

m.c61 = Constraint(expr= - m.x6 + m.x12 + m.x36 + 150*m.b48 <= 150)

m.c62 = Constraint(expr= - m.x3 + m.x37 <= -320)

m.c63 = Constraint(expr= - m.x6 + m.x38 <= -320)

m.c64 = Constraint(expr=   m.x7 + m.x39 <= 680)

m.c65 = Constraint(expr=   m.x10 + m.x40 <= 680)
