#  MINLP written by GAMS Convert at 08/13/20 17:37:51
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         44       42        0        2        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         51       49        2        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        197       75      122        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x2 = Var(within=Reals,bounds=(0,300),initialize=150)
m.x3 = Var(within=Reals,bounds=(0,300),initialize=150)
m.x4 = Var(within=Reals,bounds=(0,300),initialize=150)
m.x5 = Var(within=Reals,bounds=(0,300),initialize=150)
m.x6 = Var(within=Reals,bounds=(0,300),initialize=75)
m.x7 = Var(within=Reals,bounds=(0,300),initialize=75)
m.x8 = Var(within=Reals,bounds=(0,300),initialize=75)
m.x9 = Var(within=Reals,bounds=(0,300),initialize=75)
m.x10 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x11 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x12 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x13 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x14 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x15 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x16 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x17 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x18 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x19 = Var(within=Reals,bounds=(0,300),initialize=37.5)
m.x20 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x21 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x22 = Var(within=Reals,bounds=(0,100),initialize=50)
m.x23 = Var(within=Reals,bounds=(0,100),initialize=50)
m.x24 = Var(within=Reals,bounds=(0,100),initialize=50)
m.x25 = Var(within=Reals,bounds=(0,100),initialize=50)
m.x26 = Var(within=Reals,bounds=(0,100),initialize=50)
m.x27 = Var(within=Reals,bounds=(0,100),initialize=50)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x38 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0.333333333333333)
m.x46 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x47 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x48 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.x49 = Var(within=Reals,bounds=(0.85,1),initialize=0.85)
m.b50 = Var(within=Binary,bounds=(0,1),initialize=0.5)
m.b51 = Var(within=Binary,bounds=(0,1),initialize=0.5)

m.obj = Objective(expr=(-0.0139904 - 0.0005719*m.x28 + 0.0042656*m.x29 + 0.0093514*m.x46 + 0.0077308*m.x47)*m.x4 + (-
                       0.0661588 + 0.0016371*m.x31 + 0.0288996*m.x32 + 0.0338147*m.x48 + 0.0373349*m.x49)*m.x5
                        + 0.23947*m.b50 + 0.75835*m.b51, sense=minimize)

m.c2 = Constraint(expr=   m.x2 + m.x3 + m.x20 + m.x21 == 300)

m.c3 = Constraint(expr=   m.x6 - m.x12 - m.x13 == 0)

m.c4 = Constraint(expr=   m.x7 - m.x11 - m.x14 - m.x15 == 0)

m.c5 = Constraint(expr=   m.x8 - m.x10 - m.x16 - m.x17 == 0)

m.c6 = Constraint(expr=   m.x9 - m.x18 - m.x19 == 0)

m.c7 = Constraint(expr=-m.x10*m.x40 - 0.333333333333333*m.x2 + m.x22 == 0)

m.c8 = Constraint(expr=-m.x10*m.x41 - 0.333333333333333*m.x2 + m.x23 == 0)

m.c9 = Constraint(expr=-m.x10*m.x42 - 0.333333333333333*m.x2 + m.x24 == 0)

m.c10 = Constraint(expr=-m.x11*m.x37 - 0.333333333333333*m.x3 + m.x25 == 0)

m.c11 = Constraint(expr=-m.x11*m.x38 - 0.333333333333333*m.x3 + m.x26 == 0)

m.c12 = Constraint(expr=-m.x11*m.x39 - 0.333333333333333*m.x3 + m.x27 == 0)

m.c13 = Constraint(expr=-(m.x6*m.x34 + m.x7*m.x37) + m.x22 == 0)

m.c14 = Constraint(expr=-(m.x6*m.x35 + m.x7*m.x38) + m.x23 == 0)

m.c15 = Constraint(expr=-(m.x6*m.x36 + m.x7*m.x39) + m.x24 == 0)

m.c16 = Constraint(expr=-(m.x8*m.x40 + m.x9*m.x43) + m.x25 == 0)

m.c17 = Constraint(expr=-(m.x8*m.x41 + m.x9*m.x44) + m.x26 == 0)

m.c18 = Constraint(expr=-(m.x8*m.x42 + m.x9*m.x45) + m.x27 == 0)

m.c19 = Constraint(expr=m.x22*m.x46 - m.x6*m.x34 == 0)

m.c20 = Constraint(expr=m.x23*m.x47 - m.x7*m.x38 == 0)

m.c21 = Constraint(expr=m.x26*m.x48 - m.x8*m.x41 == 0)

m.c22 = Constraint(expr=m.x27*m.x49 - m.x9*m.x45 == 0)

m.c23 = Constraint(expr=m.x12*m.x34 + m.x14*m.x37 + m.x16*m.x40 + m.x18*m.x43 + 0.333333333333333*m.x20 == 80)

m.c24 = Constraint(expr=m.x12*m.x35 + m.x14*m.x38 + m.x16*m.x41 + m.x18*m.x44 + 0.333333333333333*m.x20 == 30)

m.c25 = Constraint(expr=m.x12*m.x36 + m.x14*m.x39 + m.x16*m.x42 + m.x18*m.x45 + 0.333333333333333*m.x20 == 20)

m.c26 = Constraint(expr=m.x13*m.x34 + m.x15*m.x37 + m.x17*m.x40 + m.x19*m.x43 + 0.333333333333333*m.x21 == 20)

m.c27 = Constraint(expr=m.x13*m.x35 + m.x15*m.x38 + m.x17*m.x41 + m.x19*m.x44 + 0.333333333333333*m.x21 == 70)

m.c28 = Constraint(expr=m.x13*m.x36 + m.x15*m.x39 + m.x17*m.x42 + m.x19*m.x45 + 0.333333333333333*m.x21 == 80)

m.c29 = Constraint(expr=m.x4*m.x28 - m.x22 == 0)

m.c30 = Constraint(expr=m.x4*m.x29 - m.x23 == 0)

m.c31 = Constraint(expr=m.x4*m.x30 - m.x24 == 0)

m.c32 = Constraint(expr=m.x5*m.x31 - m.x25 == 0)

m.c33 = Constraint(expr=m.x5*m.x32 - m.x26 == 0)

m.c34 = Constraint(expr=m.x5*m.x33 - m.x27 == 0)

m.c35 = Constraint(expr=   m.x34 + m.x35 + m.x36 == 1)

m.c36 = Constraint(expr=   m.x37 + m.x38 + m.x39 == 1)

m.c37 = Constraint(expr=   m.x40 + m.x41 + m.x42 == 1)

m.c38 = Constraint(expr=   m.x43 + m.x44 + m.x45 == 1)

m.c39 = Constraint(expr=   m.x28 + m.x29 + m.x30 == 1)

m.c40 = Constraint(expr=   m.x31 + m.x32 + m.x33 == 1)

m.c41 = Constraint(expr=   m.x36 == 0)

m.c42 = Constraint(expr=   m.x43 == 0)

m.c43 = Constraint(expr=   m.x4 - 300*m.b50 <= 0)

m.c44 = Constraint(expr=   m.x5 - 300*m.b51 <= 0)
