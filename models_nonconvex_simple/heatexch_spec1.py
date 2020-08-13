#  MINLP written by GAMS Convert at 08/13/20 17:37:54
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         65       21       12       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         57       45       12        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        225      193       32        0
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
m.x13 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x14 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x15 = Var(within=Reals,bounds=(370,650),initialize=650)
m.x16 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x17 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x18 = Var(within=Reals,bounds=(370,590),initialize=590)
m.x19 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x20 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x21 = Var(within=Reals,bounds=(410,650),initialize=410)
m.x22 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x23 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x24 = Var(within=Reals,bounds=(350,500),initialize=350)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=2800)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=2800)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=3600)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=3600)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=1950)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x42 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x43 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x44 = Var(within=Reals,bounds=(10,None),initialize=300)
m.x45 = Var(within=Reals,bounds=(10,None),initialize=300)
m.x46 = Var(within=Reals,bounds=(10,None),initialize=300)
m.x47 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x48 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x49 = Var(within=Reals,bounds=(10,None),initialize=180)
m.x50 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x51 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x52 = Var(within=Reals,bounds=(10,None),initialize=240)
m.x53 = Var(within=Reals,bounds=(10,None),initialize=330)
m.x54 = Var(within=Reals,bounds=(10,None),initialize=270)
m.x55 = Var(within=Reals,bounds=(10,None),initialize=270)
m.x56 = Var(within=Reals,bounds=(10,None),initialize=330)

m.obj = Objective(expr=150*((1e-6 + 2*m.x25/(1e-6 + (1e-6 + 0.5*m.x41*m.x42*(m.x41 + m.x42))**0.33333))**1 + (1e-6 + 2*
                       m.x26/(1e-6 + (1e-6 + 0.5*m.x42*m.x43*(m.x42 + m.x43))**0.33333))**1 + (1e-6 + 199.970793713208*
                       m.x27)**1 + (1e-6 + 2*m.x28/(1e-6 + (1e-6 + 0.5*m.x44*m.x45*(m.x44 + m.x45))**0.33333))**1 + (
                       1e-6 + 2*m.x29/(1e-6 + (1e-6 + 0.5*m.x45*m.x46*(m.x45 + m.x46))**0.33333))**1 + (1e-6 + 
                       199.970793713208*m.x30)**1 + (1e-6 + 2*m.x31/(1e-6 + (1e-6 + 0.5*m.x47*m.x48*(m.x47 + m.x48))**
                       0.33333))**1 + (1e-6 + 2*m.x32/(1e-6 + (1e-6 + 0.5*m.x48*m.x49*(m.x48 + m.x49))**0.33333))**1 + (
                       1e-6 + 199.970793713208*m.x33)**1 + (1e-6 + 2*m.x34/(1e-6 + (1e-6 + 0.5*m.x50*m.x51*(m.x50 + 
                       m.x51))**0.33333))**1 + (1e-6 + 2*m.x35/(1e-6 + (1e-6 + 0.5*m.x51*m.x52*(m.x51 + m.x52))**0.33333
                       ))**1 + (1e-6 + 199.970793713208*m.x36)**1) + 150*(2e-6 + 1.2*m.x39/(1e-6 + 30*m.x55*(15 + 0.5*
                       m.x55))**0.33333 + 1.2*m.x40/(1e-6 + 180*m.x56*(90 + 0.5*m.x56))**0.33333)**1 + 80*m.x39 + 80*
                       m.x40 + 150*((1e-6 + 2*m.x37/(1e-6 + 35*m.x53*(70 + m.x53))**0.33333)**1 + (1e-6 + 2*m.x38/(1e-6
                        + 35*m.x54*(70 + m.x54))**0.33333)**1) + 15*m.x37 + 15*m.x38 + 5500*m.b1 + 5500*m.b2 + 5500*m.b3
                        + 5500*m.b4 + 5500*m.b5 + 5500*m.b6 + 5500*m.b7 + 5500*m.b8 + 5500*m.b9 + 5500*m.b10
                        + 5500*m.b11 + 5500*m.b12, sense=minimize)

m.c1 = Constraint(expr=   10*m.x13 - 10*m.x14 - m.x25 - m.x28 == 0)

m.c2 = Constraint(expr=   10*m.x14 - 10*m.x15 - m.x26 - m.x29 == 0)

m.c3 = Constraint(expr=   20*m.x16 - 20*m.x17 - m.x31 - m.x34 == 0)

m.c4 = Constraint(expr=   20*m.x17 - 20*m.x18 - m.x32 - m.x35 == 0)

m.c5 = Constraint(expr=   15*m.x19 - 15*m.x20 - m.x25 - m.x31 == 0)

m.c6 = Constraint(expr=   15*m.x20 - 15*m.x21 - m.x26 - m.x32 == 0)

m.c7 = Constraint(expr=   13*m.x22 - 13*m.x23 - m.x28 - m.x34 == 0)

m.c8 = Constraint(expr=   13*m.x23 - 13*m.x24 - m.x29 - m.x35 == 0)

m.c9 = Constraint(expr=   10*m.x15 - m.x37 == 3700)

m.c10 = Constraint(expr=   20*m.x18 - m.x38 == 7400)

m.c11 = Constraint(expr= - m.x25 - m.x26 - m.x28 - m.x29 - m.x37 == -2800)

m.c12 = Constraint(expr= - m.x31 - m.x32 - m.x34 - m.x35 - m.x38 == -4400)

m.c13 = Constraint(expr= - 15*m.x19 - m.x39 == -9750)

m.c14 = Constraint(expr= - 13*m.x22 - m.x40 == -6500)

m.c15 = Constraint(expr= - m.x25 - m.x26 - m.x31 - m.x32 - m.x39 == -3600)

m.c16 = Constraint(expr= - m.x28 - m.x29 - m.x34 - m.x35 - m.x40 == -1950)

m.c17 = Constraint(expr=   m.x13 - m.x14 >= 0)

m.c18 = Constraint(expr=   m.x14 - m.x15 >= 0)

m.c19 = Constraint(expr=   m.x16 - m.x17 >= 0)

m.c20 = Constraint(expr=   m.x17 - m.x18 >= 0)

m.c21 = Constraint(expr=   m.x19 - m.x20 >= 0)

m.c22 = Constraint(expr=   m.x20 - m.x21 >= 0)

m.c23 = Constraint(expr=   m.x22 - m.x23 >= 0)

m.c24 = Constraint(expr=   m.x23 - m.x24 >= 0)

m.c25 = Constraint(expr=   m.x15 >= 370)

m.c26 = Constraint(expr=   m.x18 >= 370)

m.c27 = Constraint(expr= - m.x19 >= -650)

m.c28 = Constraint(expr= - m.x22 >= -500)

m.c29 = Constraint(expr= - m.x13 == -650)

m.c30 = Constraint(expr= - m.x16 == -590)

m.c31 = Constraint(expr= - m.x21 == -410)

m.c32 = Constraint(expr= - m.x24 == -350)

m.c33 = Constraint(expr= - 2800*m.b1 + m.x25 <= 0)

m.c34 = Constraint(expr= - 2800*m.b2 + m.x26 <= 0)

m.c35 = Constraint(expr= - 1950*m.b3 + m.x28 <= 0)

m.c36 = Constraint(expr= - 1950*m.b4 + m.x29 <= 0)

m.c37 = Constraint(expr= - 3600*m.b5 + m.x31 <= 0)

m.c38 = Constraint(expr= - 3600*m.b6 + m.x32 <= 0)

m.c39 = Constraint(expr= - 1950*m.b7 + m.x34 <= 0)

m.c40 = Constraint(expr= - 1950*m.b8 + m.x35 <= 0)

m.c41 = Constraint(expr= - 3600*m.b11 + m.x39 <= 0)

m.c42 = Constraint(expr= - 1950*m.b12 + m.x40 <= 0)

m.c43 = Constraint(expr= - 2800*m.b9 + m.x37 <= 0)

m.c44 = Constraint(expr= - 4400*m.b10 + m.x38 <= 0)

m.c45 = Constraint(expr=   280*m.b1 - m.x13 + m.x19 + m.x41 <= 280)

m.c46 = Constraint(expr=   280*m.b2 - m.x14 + m.x20 + m.x42 <= 280)

m.c47 = Constraint(expr=   130*m.b3 - m.x13 + m.x22 + m.x44 <= 130)

m.c48 = Constraint(expr=   130*m.b4 - m.x14 + m.x23 + m.x45 <= 130)

m.c49 = Constraint(expr=   280*m.b5 - m.x16 + m.x19 + m.x47 <= 280)

m.c50 = Constraint(expr=   280*m.b6 - m.x17 + m.x20 + m.x48 <= 280)

m.c51 = Constraint(expr=   130*m.b7 - m.x16 + m.x22 + m.x50 <= 130)

m.c52 = Constraint(expr=   130*m.b8 - m.x17 + m.x23 + m.x51 <= 130)

m.c53 = Constraint(expr=   280*m.b1 - m.x14 + m.x20 + m.x42 <= 280)

m.c54 = Constraint(expr=   280*m.b2 - m.x15 + m.x21 + m.x43 <= 280)

m.c55 = Constraint(expr=   130*m.b3 - m.x14 + m.x23 + m.x45 <= 130)

m.c56 = Constraint(expr=   130*m.b4 - m.x15 + m.x24 + m.x46 <= 130)

m.c57 = Constraint(expr=   280*m.b5 - m.x17 + m.x20 + m.x48 <= 280)

m.c58 = Constraint(expr=   280*m.b6 - m.x18 + m.x21 + m.x49 <= 280)

m.c59 = Constraint(expr=   130*m.b7 - m.x17 + m.x23 + m.x51 <= 130)

m.c60 = Constraint(expr=   130*m.b8 - m.x18 + m.x24 + m.x52 <= 130)

m.c61 = Constraint(expr= - m.x15 + m.x53 <= -320)

m.c62 = Constraint(expr= - m.x18 + m.x54 <= -320)

m.c63 = Constraint(expr=   m.x19 + m.x55 <= 680)

m.c64 = Constraint(expr=   m.x22 + m.x56 <= 680)
