#  MINLP written by GAMS Convert at 08/13/20 17:37:45
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         29        1       28        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         29        1       28        0


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
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x29, sense=maximize)

m.c1 = Constraint(expr=2*m.b1*m.b10 - 4*m.b1 - 2*m.b10 + 2*m.b1*m.b17 + 2*m.b1*m.b18 + 2*m.b1*m.b20 + 2*m.b2*m.b4 - 2*
                       m.b2 - 2*m.b4 + 2*m.b2*m.b14 - 4*m.b14 + 2*m.b3*m.b19 - 2*m.b3 + 2*m.b3*m.b21 + 2*m.b3*m.b23 - 2*
                       m.b3*m.b24 + 2*m.b4*m.b5 - 2*m.b5 + 2*m.b4*m.b7 - 2*m.b7 - 2*m.b4*m.b25 + 2*m.b5*m.b8 - 4*m.b8 + 
                       2*m.b6*m.b7 + 2*m.b6 - 2*m.b6*m.b23 - 2*m.b6*m.b25 - 2*m.b6*m.b28 + 2*m.b7*m.b13 - 2*m.b13 - 2*
                       m.b7*m.b18 + 2*m.b8*m.b9 - 2*m.b9 + 2*m.b8*m.b12 - 2*m.b12 + 2*m.b8*m.b25 + 2*m.b9*m.b13 + 2*
                       m.b10*m.b24 + 2*m.b10*m.b27 - 2*m.b10*m.b28 + 2*m.b11*m.b12 - 2*m.b11 - 2*m.b11*m.b19 + 2*m.b11*
                       m.b25 + 2*m.b11*m.b28 + 2*m.b12*m.b14 - 2*m.b12*m.b17 + 2*m.b13*m.b15 - 2*m.b15 - 2*m.b13*m.b16
                        + 2*m.b14*m.b15 + 2*m.b14*m.b16 + 2*m.b16*m.b17 - 2*m.b16*m.b18 - 2*m.b17*m.b19 + 2*m.b18*m.b23
                        + 2*m.b19*m.b20 - 2*m.b20*m.b21 - 2*m.b20*m.b22 + 2*m.b22*m.b26 - 2*m.b23*m.b26 - 2*m.b26*m.b27
                        + 2*m.b26*m.b28 + m.x29 <= 0)
