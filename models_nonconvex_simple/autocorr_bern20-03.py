#  MINLP written by GAMS Convert at 08/13/20 17:37:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21        1       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21        1       20        0


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
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x21, sense=minimize)

m.c1 = Constraint(expr=8*m.b1*m.b3 - 4*m.b1 - 8*m.b3 + 8*m.b2*m.b4 - 4*m.b2 - 8*m.b4 + 8*m.b3*m.b5 - 8*m.b5 + 8*m.b4*
                       m.b6 - 8*m.b6 + 8*m.b5*m.b7 - 8*m.b7 + 8*m.b6*m.b8 - 8*m.b8 + 8*m.b7*m.b9 - 8*m.b9 + 8*m.b8*m.b10
                        - 8*m.b10 + 8*m.b9*m.b11 - 8*m.b11 + 8*m.b10*m.b12 - 8*m.b12 + 8*m.b11*m.b13 - 8*m.b13 + 8*m.b12
                       *m.b14 - 8*m.b14 + 8*m.b13*m.b15 - 8*m.b15 + 8*m.b14*m.b16 - 8*m.b16 + 8*m.b15*m.b17 - 8*m.b17 + 
                       8*m.b16*m.b18 - 8*m.b18 + 8*m.b17*m.b19 - 4*m.b19 + 8*m.b18*m.b20 - 4*m.b20 - m.x21 <= 0)
