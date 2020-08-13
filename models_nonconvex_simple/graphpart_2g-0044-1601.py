#  MINLP written by GAMS Convert at 08/13/20 17:37:50
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         17       17        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         49        1       48        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         97       49       48        0
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

m.obj = Objective(expr=13960*m.b1*m.b4 + 132180*m.b1*m.b10 - 45455*m.b1*m.b13 + 21397*m.b1*m.b37 + 13960*m.b2*m.b5 + 
                       132180*m.b2*m.b11 - 45455*m.b2*m.b14 + 21397*m.b2*m.b38 + 13960*m.b3*m.b6 + 132180*m.b3*m.b12 - 
                       45455*m.b3*m.b15 + 21397*m.b3*m.b39 - 30411*m.b4*m.b7 - 101527*m.b4*m.b16 - 8896*m.b4*m.b40 - 
                       30411*m.b5*m.b8 - 101527*m.b5*m.b17 - 8896*m.b5*m.b41 - 30411*m.b6*m.b9 - 101527*m.b6*m.b18 - 
                       8896*m.b6*m.b42 - 122332*m.b7*m.b10 + 30058*m.b7*m.b19 + 33114*m.b7*m.b43 - 122332*m.b8*m.b11 + 
                       30058*m.b8*m.b20 + 33114*m.b8*m.b44 - 122332*m.b9*m.b12 + 30058*m.b9*m.b21 + 33114*m.b9*m.b45 - 
                       13676*m.b10*m.b22 + 124553*m.b10*m.b46 - 13676*m.b11*m.b23 + 124553*m.b11*m.b47 - 13676*m.b12*
                       m.b24 + 124553*m.b12*m.b48 + 17153*m.b13*m.b16 + 73691*m.b13*m.b22 - 32022*m.b13*m.b25 + 17153*
                       m.b14*m.b17 + 73691*m.b14*m.b23 - 32022*m.b14*m.b26 + 17153*m.b15*m.b18 + 73691*m.b15*m.b24 - 
                       32022*m.b15*m.b27 - 106129*m.b16*m.b19 - 101395*m.b16*m.b28 - 106129*m.b17*m.b20 - 101395*m.b17*
                       m.b29 - 106129*m.b18*m.b21 - 101395*m.b18*m.b30 - 10958*m.b19*m.b22 - 41751*m.b19*m.b31 - 10958*
                       m.b20*m.b23 - 41751*m.b20*m.b32 - 10958*m.b21*m.b24 - 41751*m.b21*m.b33 - 30446*m.b22*m.b34 - 
                       30446*m.b23*m.b35 - 30446*m.b24*m.b36 + 94519*m.b25*m.b28 + 44613*m.b25*m.b34 + 70141*m.b25*m.b37
                        + 94519*m.b26*m.b29 + 44613*m.b26*m.b35 + 70141*m.b26*m.b38 + 94519*m.b27*m.b30 + 44613*m.b27*
                       m.b36 + 70141*m.b27*m.b39 + 73611*m.b28*m.b31 - 54792*m.b28*m.b40 + 73611*m.b29*m.b32 - 54792*
                       m.b29*m.b41 + 73611*m.b30*m.b33 - 54792*m.b30*m.b42 + 57663*m.b31*m.b34 - 147596*m.b31*m.b43 + 
                       57663*m.b32*m.b35 - 147596*m.b32*m.b44 + 57663*m.b33*m.b36 - 147596*m.b33*m.b45 + 70863*m.b34*
                       m.b46 + 70863*m.b35*m.b47 + 70863*m.b36*m.b48 + 24474*m.b37*m.b40 - 178500*m.b37*m.b46 + 24474*
                       m.b38*m.b41 - 178500*m.b38*m.b47 + 24474*m.b39*m.b42 - 178500*m.b39*m.b48 + 118713*m.b40*m.b43 + 
                       118713*m.b41*m.b44 + 118713*m.b42*m.b45 + 34279*m.b43*m.b46 + 34279*m.b44*m.b47 + 34279*m.b45*
                       m.b48, sense=minimize)

m.c1 = Constraint(expr=   m.b1 + m.b2 + m.b3 == 1)

m.c2 = Constraint(expr=   m.b4 + m.b5 + m.b6 == 1)

m.c3 = Constraint(expr=   m.b7 + m.b8 + m.b9 == 1)

m.c4 = Constraint(expr=   m.b10 + m.b11 + m.b12 == 1)

m.c5 = Constraint(expr=   m.b13 + m.b14 + m.b15 == 1)

m.c6 = Constraint(expr=   m.b16 + m.b17 + m.b18 == 1)

m.c7 = Constraint(expr=   m.b19 + m.b20 + m.b21 == 1)

m.c8 = Constraint(expr=   m.b22 + m.b23 + m.b24 == 1)

m.c9 = Constraint(expr=   m.b25 + m.b26 + m.b27 == 1)

m.c10 = Constraint(expr=   m.b28 + m.b29 + m.b30 == 1)

m.c11 = Constraint(expr=   m.b31 + m.b32 + m.b33 == 1)

m.c12 = Constraint(expr=   m.b34 + m.b35 + m.b36 == 1)

m.c13 = Constraint(expr=   m.b37 + m.b38 + m.b39 == 1)

m.c14 = Constraint(expr=   m.b40 + m.b41 + m.b42 == 1)

m.c15 = Constraint(expr=   m.b43 + m.b44 + m.b45 == 1)

m.c16 = Constraint(expr=   m.b46 + m.b47 + m.b48 == 1)
