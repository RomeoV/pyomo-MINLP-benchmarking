#  MINLP written by GAMS Convert at 08/13/20 17:38:06
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         75       25       18       32        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         88       70       18        0        0        0        0        0
#  FX      1        1        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        269      215       54        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(0,254.001),initialize=254)
m.x2 = Var(within=Reals,bounds=(0,254.001),initialize=254)
m.x3 = Var(within=Reals,bounds=(0,254.001),initialize=254)
m.x4 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x5 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x6 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x7 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x8 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x9 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x10 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x11 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x12 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x38 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=0)
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
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x71 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x72 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x73 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(254,254),initialize=254)
m.x86 = Var(within=Reals,bounds=(None,None),initialize=254)
m.x87 = Var(within=Reals,bounds=(None,None),initialize=254)

m.obj = Objective(expr= - 300.544*m.x22 - 225.408*m.x23 - 150.272*m.x24 - 300.544*m.x25 - 225.408*m.x26 - 150.272*m.x27
                        - 300.544*m.x28 - 225.408*m.x29 - 150.272*m.x30 - 2.66666666666667*m.x31 - 4*m.x32
                        - 5.33333333333333*m.x33 - 2.66666666666667*m.x34 - 4*m.x35 - 5.33333333333333*m.x36
                        - 2.66666666666667*m.x37 - 4*m.x38 - 5.33333333333333*m.x39 + 1.33333333333333*m.x67 + m.x68
                        + m.x69 + 1.33333333333333*m.x70 + m.x71 + m.x72 + 1.33333333333333*m.x73 + m.x74 + m.x75
                        + 1.33333333333333*m.x76 + m.x77 + m.x78 + 1.33333333333333*m.x79 + m.x80 + m.x81
                        + 1.33333333333333*m.x82 + m.x83 + m.x84, sense=minimize)

m.c1 = Constraint(expr=   m.b58 + m.b61 + m.b64 <= 1)

m.c2 = Constraint(expr=   m.b59 + m.b62 + m.b65 <= 1)

m.c3 = Constraint(expr=   m.b60 + m.b63 + m.b66 <= 1)

m.c4 = Constraint(expr=   m.x4 + m.x5 + m.x6 + m.x13 + m.x14 + m.x15 == 1)

m.c5 = Constraint(expr=   m.x7 + m.x8 + m.x9 + m.x16 + m.x17 + m.x18 == 1)

m.c6 = Constraint(expr=   m.x10 + m.x11 + m.x12 + m.x19 + m.x20 + m.x21 == 1)

m.c7 = Constraint(expr= - 3.16363636363636*m.x4 - 3.16363636363636*m.x5 - 3.16363636363636*m.x6 + 56.3636363636364*m.b58
                        + 43.2*m.b61 + 33.8181818181818*m.b64 - m.x85 + m.x86 <= 0)

m.c8 = Constraint(expr= - 3.16363636363636*m.x7 - 3.16363636363636*m.x8 - 3.16363636363636*m.x9 + 56.3636363636364*m.b59
                        + 43.2*m.b62 + 33.8181818181818*m.b65 - m.x86 + m.x87 <= 0)

m.c9 = Constraint(expr=-6.353*m.x1**0.172*m.x40 + m.x22 + m.x23 + m.x24 <= 0)

m.c10 = Constraint(expr=-6.353*m.x2**0.172*m.x41 + m.x25 + m.x26 + m.x27 <= 0)

m.c11 = Constraint(expr=-6.353*m.x3**0.172*m.x42 + m.x28 + m.x29 + m.x30 <= 0)

m.c12 = Constraint(expr=-0.32*m.x1**0.617*m.x43 + m.x31 + m.x32 + m.x33 <= 0)

m.c13 = Constraint(expr=-0.32*m.x2**0.617*m.x44 + m.x34 + m.x35 + m.x36 <= 0)

m.c14 = Constraint(expr=-0.32*m.x3**0.617*m.x45 + m.x37 + m.x38 + m.x39 <= 0)

m.c15 = Constraint(expr=   m.x22 + m.x31 - 50*m.b58 <= 0)

m.c16 = Constraint(expr=   m.x25 + m.x34 - 50*m.b59 <= 0)

m.c17 = Constraint(expr=   m.x28 + m.x37 - 50*m.b60 <= 0)

m.c18 = Constraint(expr=   m.x23 + m.x32 - 50*m.b61 <= 0)

m.c19 = Constraint(expr=   m.x26 + m.x35 - 50*m.b62 <= 0)

m.c20 = Constraint(expr=   m.x29 + m.x38 - 50*m.b63 <= 0)

m.c21 = Constraint(expr=   m.x24 + m.x33 - 50*m.b64 <= 0)

m.c22 = Constraint(expr=   m.x27 + m.x36 - 50*m.b65 <= 0)

m.c23 = Constraint(expr=   m.x30 + m.x39 - 50*m.b66 <= 0)

m.c24 = Constraint(expr=   m.x4 + m.x13 - m.b58 <= 0)

m.c25 = Constraint(expr=   m.x7 + m.x16 - m.b59 <= 0)

m.c26 = Constraint(expr=   m.x10 + m.x19 - m.b60 <= 0)

m.c27 = Constraint(expr=   m.x5 + m.x14 - m.b61 <= 0)

m.c28 = Constraint(expr=   m.x8 + m.x17 - m.b62 <= 0)

m.c29 = Constraint(expr=   m.x11 + m.x20 - m.b63 <= 0)

m.c30 = Constraint(expr=   m.x6 + m.x15 - m.b64 <= 0)

m.c31 = Constraint(expr=   m.x9 + m.x18 - m.b65 <= 0)

m.c32 = Constraint(expr=   m.x12 + m.x21 - m.b66 <= 0)

m.c33 = Constraint(expr= - 200*m.b52 + m.x85 >= 0)

m.c34 = Constraint(expr= - 200*m.b53 + m.x86 >= 0)

m.c35 = Constraint(expr= - 200*m.b54 + m.x87 >= 0)

m.c36 = Constraint(expr= - 200*m.b55 + m.x85 >= 0)

m.c37 = Constraint(expr= - 200*m.b56 + m.x86 >= 0)

m.c38 = Constraint(expr= - 200*m.b57 + m.x87 >= 0)

m.c39 = Constraint(expr= - m.x40 + m.b52 >= 0)

m.c40 = Constraint(expr= - m.x41 + m.b53 >= 0)

m.c41 = Constraint(expr= - m.x42 + m.b54 >= 0)

m.c42 = Constraint(expr= - m.x43 + m.b55 >= 0)

m.c43 = Constraint(expr= - m.x44 + m.b56 >= 0)

m.c44 = Constraint(expr= - m.x45 + m.b57 >= 0)

m.c45 = Constraint(expr= - m.x46 + m.b49 == 0)

m.c46 = Constraint(expr= - m.x47 + m.b50 == 0)

m.c47 = Constraint(expr= - m.x48 + m.b51 == 0)

m.c48 = Constraint(expr=m.x85*(1 - m.x46) - m.x1 >= -0.001)

m.c49 = Constraint(expr=m.x86*(1 - m.x47) - m.x2 >= -0.001)

m.c50 = Constraint(expr=m.x87*(1 - m.x48) - m.x3 >= -0.001)

m.c51 = Constraint(expr=   508*m.b49 + m.x85 >= 200)

m.c52 = Constraint(expr=   508*m.b50 + m.x86 >= 200)

m.c53 = Constraint(expr=   508*m.b51 + m.x87 >= 200)

m.c54 = Constraint(expr=   508*m.b49 + m.x85 <= 708)

m.c55 = Constraint(expr=   508*m.b50 + m.x86 <= 708)

m.c56 = Constraint(expr=   508*m.b51 + m.x87 <= 708)

m.c57 = Constraint(expr=-81.9*m.x40*m.x4 + m.x67 == 0)

m.c58 = Constraint(expr=-81.9*m.x41*m.x7 + m.x70 == 0)

m.c59 = Constraint(expr=-81.9*m.x42*m.x10 + m.x73 == 0)

m.c60 = Constraint(expr=-81.9*m.x40*m.x5 + m.x68 == 0)

m.c61 = Constraint(expr=-81.9*m.x41*m.x8 + m.x71 == 0)

m.c62 = Constraint(expr=-81.9*m.x42*m.x11 + m.x74 == 0)

m.c63 = Constraint(expr=-54.6*m.x40*m.x6 + m.x69 == 0)

m.c64 = Constraint(expr=-54.6*m.x41*m.x9 + m.x72 == 0)

m.c65 = Constraint(expr=-54.6*m.x42*m.x12 + m.x75 == 0)

m.c66 = Constraint(expr=-136.62*m.x40*m.x13 + m.x76 == 0)

m.c67 = Constraint(expr=-136.62*m.x41*m.x16 + m.x79 == 0)

m.c68 = Constraint(expr=-136.62*m.x42*m.x19 + m.x82 == 0)

m.c69 = Constraint(expr=-136.62*m.x40*m.x14 + m.x77 == 0)

m.c70 = Constraint(expr=-136.62*m.x41*m.x17 + m.x80 == 0)

m.c71 = Constraint(expr=-136.62*m.x42*m.x20 + m.x83 == 0)

m.c72 = Constraint(expr=-91.08*m.x40*m.x15 + m.x78 == 0)

m.c73 = Constraint(expr=-91.08*m.x41*m.x18 + m.x81 == 0)

m.c74 = Constraint(expr=-91.08*m.x42*m.x21 + m.x84 == 0)
