#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         26       26        0        0        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         76        1       75        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        151       76       75        0
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
m.b66 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b67 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b68 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b69 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b70 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b71 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b72 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=(-11669*m.b1*m.b4) - 144456*m.b1*m.b13 + 30835*m.b1*m.b16 - 33555*m.b1*m.b61 - 11669*m.b2*m.b5 - 
                       144456*m.b2*m.b14 + 30835*m.b2*m.b17 - 33555*m.b2*m.b62 - 11669*m.b3*m.b6 - 144456*m.b3*m.b15 + 
                       30835*m.b3*m.b18 - 33555*m.b3*m.b63 + 52284*m.b4*m.b7 + 145893*m.b4*m.b19 - 140641*m.b4*m.b64 + 
                       52284*m.b5*m.b8 + 145893*m.b5*m.b20 - 140641*m.b5*m.b65 + 52284*m.b6*m.b9 + 145893*m.b6*m.b21 - 
                       140641*m.b6*m.b66 + 127397*m.b7*m.b10 - 12640*m.b7*m.b22 + 217400*m.b7*m.b67 + 127397*m.b8*m.b11
                        - 12640*m.b8*m.b23 + 217400*m.b8*m.b68 + 127397*m.b9*m.b12 - 12640*m.b9*m.b24 + 217400*m.b9*
                       m.b69 + 50562*m.b10*m.b13 - 78959*m.b10*m.b25 - 36333*m.b10*m.b70 + 50562*m.b11*m.b14 - 78959*
                       m.b11*m.b26 - 36333*m.b11*m.b71 + 50562*m.b12*m.b15 - 78959*m.b12*m.b27 - 36333*m.b12*m.b72 + 
                       98784*m.b13*m.b28 - 31218*m.b13*m.b73 + 98784*m.b14*m.b29 - 31218*m.b14*m.b74 + 98784*m.b15*m.b30
                        - 31218*m.b15*m.b75 + 6320*m.b16*m.b19 + 171989*m.b16*m.b28 - 39163*m.b16*m.b31 + 6320*m.b17*
                       m.b20 + 171989*m.b17*m.b29 - 39163*m.b17*m.b32 + 6320*m.b18*m.b21 + 171989*m.b18*m.b30 - 39163*
                       m.b18*m.b33 - 183413*m.b19*m.b22 + 60462*m.b19*m.b34 - 183413*m.b20*m.b23 + 60462*m.b20*m.b35 - 
                       183413*m.b21*m.b24 + 60462*m.b21*m.b36 + 45778*m.b22*m.b25 + 192287*m.b22*m.b37 + 45778*m.b23*
                       m.b26 + 192287*m.b23*m.b38 + 45778*m.b24*m.b27 + 192287*m.b24*m.b39 + 125824*m.b25*m.b28 + 41371*
                       m.b25*m.b40 + 125824*m.b26*m.b29 + 41371*m.b26*m.b41 + 125824*m.b27*m.b30 + 41371*m.b27*m.b42 + 
                       17724*m.b28*m.b43 + 17724*m.b29*m.b44 + 17724*m.b30*m.b45 + 12200*m.b31*m.b34 + 106251*m.b31*
                       m.b43 - 88012*m.b31*m.b46 + 12200*m.b32*m.b35 + 106251*m.b32*m.b44 - 88012*m.b32*m.b47 + 12200*
                       m.b33*m.b36 + 106251*m.b33*m.b45 - 88012*m.b33*m.b48 - 17583*m.b34*m.b37 + 118167*m.b34*m.b49 - 
                       17583*m.b35*m.b38 + 118167*m.b35*m.b50 - 17583*m.b36*m.b39 + 118167*m.b36*m.b51 - 5402*m.b37*
                       m.b40 - 27062*m.b37*m.b52 - 5402*m.b38*m.b41 - 27062*m.b38*m.b53 - 5402*m.b39*m.b42 - 27062*m.b39
                       *m.b54 - 117425*m.b40*m.b43 - 125320*m.b40*m.b55 - 117425*m.b41*m.b44 - 125320*m.b41*m.b56 - 
                       117425*m.b42*m.b45 - 125320*m.b42*m.b57 + 29332*m.b43*m.b58 + 29332*m.b44*m.b59 + 29332*m.b45*
                       m.b60 + 69937*m.b46*m.b49 + 65415*m.b46*m.b58 - 197304*m.b46*m.b61 + 69937*m.b47*m.b50 + 65415*
                       m.b47*m.b59 - 197304*m.b47*m.b62 + 69937*m.b48*m.b51 + 65415*m.b48*m.b60 - 197304*m.b48*m.b63 + 
                       66551*m.b49*m.b52 + 92080*m.b49*m.b64 + 66551*m.b50*m.b53 + 92080*m.b50*m.b65 + 66551*m.b51*m.b54
                        + 92080*m.b51*m.b66 + 47821*m.b52*m.b55 + 68105*m.b52*m.b67 + 47821*m.b53*m.b56 + 68105*m.b53*
                       m.b68 + 47821*m.b54*m.b57 + 68105*m.b54*m.b69 - 116706*m.b55*m.b58 - 6426*m.b55*m.b70 - 116706*
                       m.b56*m.b59 - 6426*m.b56*m.b71 - 116706*m.b57*m.b60 - 6426*m.b57*m.b72 - 154797*m.b58*m.b73 - 
                       154797*m.b59*m.b74 - 154797*m.b60*m.b75 - 14848*m.b61*m.b64 - 2103*m.b61*m.b73 - 14848*m.b62*
                       m.b65 - 2103*m.b62*m.b74 - 14848*m.b63*m.b66 - 2103*m.b63*m.b75 + 17019*m.b64*m.b67 + 17019*m.b65
                       *m.b68 + 17019*m.b66*m.b69 + 83365*m.b67*m.b70 + 83365*m.b68*m.b71 + 83365*m.b69*m.b72 - 20293*
                       m.b70*m.b73 - 20293*m.b71*m.b74 - 20293*m.b72*m.b75, sense=minimize)

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

m.c17 = Constraint(expr=   m.b49 + m.b50 + m.b51 == 1)

m.c18 = Constraint(expr=   m.b52 + m.b53 + m.b54 == 1)

m.c19 = Constraint(expr=   m.b55 + m.b56 + m.b57 == 1)

m.c20 = Constraint(expr=   m.b58 + m.b59 + m.b60 == 1)

m.c21 = Constraint(expr=   m.b61 + m.b62 + m.b63 == 1)

m.c22 = Constraint(expr=   m.b64 + m.b65 + m.b66 == 1)

m.c23 = Constraint(expr=   m.b67 + m.b68 + m.b69 == 1)

m.c24 = Constraint(expr=   m.b70 + m.b71 + m.b72 == 1)

m.c25 = Constraint(expr=   m.b73 + m.b74 + m.b75 == 1)
