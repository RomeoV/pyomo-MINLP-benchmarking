#  MINLP written by GAMS Convert at 08/13/20 17:37:50
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         74       23       27       24        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         47       38        9        0        0        0        0        0
#  FX      5        1        4        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        291      228       63        0


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x2 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x3 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x13 = Var(within=Reals,bounds=(643,643),initialize=643)
m.x14 = Var(within=Reals,bounds=(643,4018.36),initialize=643)
m.x15 = Var(within=Reals,bounds=(643,4018.36),initialize=643)
m.x16 = Var(within=Reals,bounds=(536,3348.63),initialize=536)
m.x17 = Var(within=Reals,bounds=(536,3348.63),initialize=536)
m.x18 = Var(within=Reals,bounds=(536,3348.63),initialize=536)
m.x19 = Var(within=Reals,bounds=(214,1339.45),initialize=214)
m.x20 = Var(within=Reals,bounds=(214,1339.45),initialize=214)
m.x21 = Var(within=Reals,bounds=(214,1339.45),initialize=214)
m.x22 = Var(within=Reals,bounds=(643,4018.36),initialize=643)
m.x23 = Var(within=Reals,bounds=(536,3348.63),initialize=536)
m.x24 = Var(within=Reals,bounds=(214,1339.45),initialize=214)
m.x25 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,None),initialize=0)
m.b38 = Var(within=Binary,bounds=(1,1),initialize=1)
m.b39 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0.550375356)
m.b41 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0.292212117)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0.224052867)
m.b44 = Var(within=Binary,bounds=(0,0),initialize=0)
m.b45 = Var(within=Binary,bounds=(0,1),initialize=0.856270347)
m.b46 = Var(within=Binary,bounds=(0,1),initialize=0.067113723)
m.x47 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x47, sense=minimize)

m.c1 = Constraint(expr=   m.x1 + m.x2 + m.x3 - m.x37 + 0.4*m.b38 + 0.4*m.b39 + 0.4*m.b40 + 0.2*m.b41 + 0.2*m.b42
                        + 0.2*m.b43 + 0.1*m.b44 + 0.1*m.b45 + 0.1*m.b46 == 0)

m.c2 = Constraint(expr=   m.b38 + m.b41 + m.b44 <= 1)

m.c3 = Constraint(expr=   m.b39 + m.b42 + m.b45 <= 1)

m.c4 = Constraint(expr=   m.b40 + m.b43 + m.b46 <= 1)

m.c5 = Constraint(expr=   11.4794520547945*m.x1 - m.x4 - m.x13 + m.x14 + 4.59178082191781*m.b38 + 2.2958904109589*m.b41
                        + 1.14794520547945*m.b44 == 0)

m.c6 = Constraint(expr=   11.4794520547945*m.x2 - m.x5 - m.x14 + m.x15 + 4.59178082191781*m.b39 + 2.2958904109589*m.b42
                        + 1.14794520547945*m.b45 == 0)

m.c7 = Constraint(expr=   11.4794520547945*m.x3 - m.x6 + m.x13 - m.x15 + 4.59178082191781*m.b40 + 2.2958904109589*m.b43
                        + 1.14794520547945*m.b46 == 0)

m.c8 = Constraint(expr=   9.56712328767123*m.x1 - m.x7 - m.x16 + m.x17 + 3.82684931506849*m.b38 + 1.91342465753425*m.b41
                        + 0.956712328767123*m.b44 == 0)

m.c9 = Constraint(expr=   9.56712328767123*m.x2 - m.x8 - m.x17 + m.x18 + 3.82684931506849*m.b39 + 1.91342465753425*m.b42
                        + 0.956712328767123*m.b45 == 0)

m.c10 = Constraint(expr=   9.56712328767123*m.x3 - m.x9 + m.x16 - m.x18 + 3.82684931506849*m.b40
                         + 1.91342465753425*m.b43 + 0.956712328767123*m.b46 == 0)

m.c11 = Constraint(expr=   3.82739726027397*m.x1 - m.x10 - m.x19 + m.x20 + 1.53095890410959*m.b38
                         + 0.765479452054795*m.b41 + 0.382739726027397*m.b44 == 0)

m.c12 = Constraint(expr=   3.82739726027397*m.x2 - m.x11 - m.x20 + m.x21 + 1.53095890410959*m.b39
                         + 0.765479452054795*m.b42 + 0.382739726027397*m.b45 == 0)

m.c13 = Constraint(expr=   3.82739726027397*m.x3 - m.x12 + m.x19 - m.x21 + 1.53095890410959*m.b40
                         + 0.765479452054795*m.b43 + 0.382739726027397*m.b46 == 0)

m.c14 = Constraint(expr=   m.x13 - m.x22 <= 0)

m.c15 = Constraint(expr=   m.x14 - m.x22 <= 0)

m.c16 = Constraint(expr=   m.x15 - m.x22 <= 0)

m.c17 = Constraint(expr=   m.x16 - m.x23 <= 0)

m.c18 = Constraint(expr=   m.x17 - m.x23 <= 0)

m.c19 = Constraint(expr=   m.x18 - m.x23 <= 0)

m.c20 = Constraint(expr=   m.x19 - m.x24 <= 0)

m.c21 = Constraint(expr=   m.x20 - m.x24 <= 0)

m.c22 = Constraint(expr=   m.x21 - m.x24 <= 0)

m.c23 = Constraint(expr=-50*m.x1*m.b38 + m.x4 <= 0)

m.c24 = Constraint(expr=-50*m.x2*m.b39 + m.x5 <= 0)

m.c25 = Constraint(expr=-50*m.x3*m.b40 + m.x6 <= 0)

m.c26 = Constraint(expr=-50*m.x1*m.b41 + m.x7 <= 0)

m.c27 = Constraint(expr=-50*m.x2*m.b42 + m.x8 <= 0)

m.c28 = Constraint(expr=-50*m.x3*m.b43 + m.x9 <= 0)

m.c29 = Constraint(expr=-50*m.x1*m.b44 + m.x10 <= 0)

m.c30 = Constraint(expr=-50*m.x2*m.b45 + m.x11 <= 0)

m.c31 = Constraint(expr=-50*m.x3*m.b46 + m.x12 <= 0)

m.c32 = Constraint(expr=-15*m.x1*m.b38 + m.x4 >= 0)

m.c33 = Constraint(expr=-15*m.x2*m.b39 + m.x5 >= 0)

m.c34 = Constraint(expr=-15*m.x3*m.b40 + m.x6 >= 0)

m.c35 = Constraint(expr=-15*m.x1*m.b41 + m.x7 >= 0)

m.c36 = Constraint(expr=-15*m.x2*m.b42 + m.x8 >= 0)

m.c37 = Constraint(expr=-15*m.x3*m.b43 + m.x9 >= 0)

m.c38 = Constraint(expr=-7*m.x1*m.b44 + m.x10 >= 0)

m.c39 = Constraint(expr=-7*m.x2*m.b45 + m.x11 >= 0)

m.c40 = Constraint(expr=-7*m.x3*m.b46 + m.x12 >= 0)

m.c41 = Constraint(expr=   m.x1 - 40*m.b38 - 40*m.b41 - 40*m.b44 <= 0)

m.c42 = Constraint(expr=   m.x2 - 40*m.b39 - 40*m.b42 - 40*m.b45 <= 0)

m.c43 = Constraint(expr=   m.x3 - 40*m.b40 - 40*m.b43 - 40*m.b46 <= 0)

m.c44 = Constraint(expr=   m.x1 - m.b38 - m.b41 - m.b44 >= 0)

m.c45 = Constraint(expr=   m.x2 - m.b39 - m.b42 - m.b45 >= 0)

m.c46 = Constraint(expr=   m.x3 - m.b40 - m.b43 - m.b46 >= 0)

m.c47 = Constraint(expr=   m.x35 - 10*m.b38 - 10*m.b39 - 10*m.b40 - 20*m.b41 - 20*m.b42 - 20*m.b43 - 30*m.b44 - 30*m.b45
                         - 30*m.b46 == 0)

m.c48 = Constraint(expr=-0.3271*(sqrt(m.x22) + sqrt(m.x23) + sqrt(m.x24)) + m.x34 == 0)

m.c49 = Constraint(expr=-(0.0515901369863014*m.x25*(m.x1 + 0.4*m.b38 + 0.2*m.b41 + 0.1*m.b44) + 0.0515901369863014*m.x26
                        *(m.x2 + 0.4*m.b39 + 0.2*m.b42 + 0.1*m.b45) + 0.0515901369863014*m.x27*(m.x3 + 0.4*m.b40 + 0.2*
                        m.b43 + 0.1*m.b46) + 0.0528586301369863*m.x28*(m.x1 + 0.4*m.b38 + 0.2*m.b41 + 0.1*m.b44) + 
                        0.0528586301369863*m.x29*(m.x2 + 0.4*m.b39 + 0.2*m.b42 + 0.1*m.b45) + 0.0528586301369863*m.x30*(
                        m.x3 + 0.4*m.b40 + 0.2*m.b43 + 0.1*m.b46) + 0.0541268493150685*m.x31*(m.x1 + 0.4*m.b38 + 0.2*
                        m.b41 + 0.1*m.b44) + 0.0541268493150685*m.x32*(m.x2 + 0.4*m.b39 + 0.2*m.b42 + 0.1*m.b45) + 
                        0.0541268493150685*m.x33*(m.x3 + 0.4*m.b40 + 0.2*m.b43 + 0.1*m.b46)) + m.x36 == 0)

m.c50 = Constraint(expr= - 0.5*m.x13 - 0.5*m.x14 + m.x25 == -643)

m.c51 = Constraint(expr= - 0.5*m.x14 - 0.5*m.x15 + m.x26 == -643)

m.c52 = Constraint(expr= - 0.5*m.x13 - 0.5*m.x15 + m.x27 == -643)

m.c53 = Constraint(expr= - 0.5*m.x16 - 0.5*m.x17 + m.x28 == -536)

m.c54 = Constraint(expr= - 0.5*m.x17 - 0.5*m.x18 + m.x29 == -536)

m.c55 = Constraint(expr= - 0.5*m.x16 - 0.5*m.x18 + m.x30 == -536)

m.c56 = Constraint(expr= - 0.5*m.x19 - 0.5*m.x20 + m.x31 == -214)

m.c57 = Constraint(expr= - 0.5*m.x20 - 0.5*m.x21 + m.x32 == -214)

m.c58 = Constraint(expr= - 0.5*m.x19 - 0.5*m.x21 + m.x33 == -214)

m.c59 = Constraint(expr=(24.8739726027397*m.x47 - m.x34)*m.x37 - m.x35 - m.x36 == 0)

m.c60 = Constraint(expr= - m.x1 + 40*m.b38 + 40*m.b41 + 40*m.b44 >= 0)

m.c61 = Constraint(expr= - m.x2 + 40*m.b39 + 40*m.b42 + 40*m.b45 >= 0)

m.c62 = Constraint(expr= - m.x3 + 40*m.b40 + 40*m.b43 + 40*m.b46 >= 0)

m.c63 = Constraint(expr= - m.b38 - m.b39 >= -1)

m.c64 = Constraint(expr= - m.b39 - m.b40 >= -1)

m.c65 = Constraint(expr= - m.b40 >= -1)

m.c66 = Constraint(expr= - m.b41 - m.b42 >= -1)

m.c67 = Constraint(expr= - m.b42 - m.b43 >= -1)

m.c68 = Constraint(expr= - m.b43 >= -1)

m.c69 = Constraint(expr= - m.b44 - m.b45 >= -1)

m.c70 = Constraint(expr= - m.b45 - m.b46 >= -1)

m.c71 = Constraint(expr= - m.b46 >= -1)

m.c72 = Constraint(expr=   m.b38 - m.b39 + m.b41 - m.b42 + m.b44 - m.b45 >= 0)

m.c73 = Constraint(expr=   m.b39 - m.b40 + m.b42 - m.b43 + m.b45 - m.b46 >= 0)

m.c74 = Constraint(expr=   m.b40 + m.b43 + m.b46 >= 0)
