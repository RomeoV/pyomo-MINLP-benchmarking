#  MINLP written by GAMS Convert at 08/13/20 17:37:55
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         84       15       17       52        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         61        9       52        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        341      293       48        0
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
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=-(39.2*((25*m.b1 + 25*m.b2 + 25*m.b9 + 25*m.b10 + 25*m.b17 + 25*m.b18 + 25*m.b25 + 25*m.b26 + 25*
                       m.b33 + 25*m.b34 + 25*m.b41 + 25*m.b42)**0.5 + (25*m.b3 + 25*m.b4 + 25*m.b11 + 25*m.b12 + 25*
                       m.b19 + 25*m.b20 + 25*m.b27 + 25*m.b28 + 25*m.b35 + 25*m.b36 + 25*m.b43 + 25*m.b44)**0.5 + (25*
                       m.b5 + 25*m.b6 + 25*m.b13 + 25*m.b14 + 25*m.b21 + 25*m.b22 + 25*m.b29 + 25*m.b30 + 25*m.b37 + 25*
                       m.b38 + 25*m.b45 + 25*m.b46)**0.5 + (25*m.b7 + 25*m.b8 + 25*m.b15 + 25*m.b16 + 25*m.b23 + 25*
                       m.b24 + 25*m.b31 + 25*m.b32 + 25*m.b39 + 25*m.b40 + 25*m.b47 + 25*m.b48)**0.5) - 300000*m.b1 - 
                       800000*m.b2 - 300000*m.b3 - 800000*m.b4 - 300000*m.b5 - 800000*m.b6 - 300000*m.b7 - 800000*m.b8
                        - 300000*m.b9 - 800000*m.b10 - 300000*m.b11 - 800000*m.b12 - 300000*m.b13 - 800000*m.b14 - 
                       300000*m.b15 - 800000*m.b16 - 300000*m.b17 - 800000*m.b18 - 300000*m.b19 - 800000*m.b20 - 300000*
                       m.b21 - 800000*m.b22 - 300000*m.b23 - 800000*m.b24 - 300000*m.b25 - 800000*m.b26 - 300000*m.b27
                        - 800000*m.b28 - 300000*m.b29 - 800000*m.b30 - 300000*m.b31 - 800000*m.b32 - 300000*m.b33 - 
                       800000*m.b34 - 300000*m.b35 - 800000*m.b36 - 300000*m.b37 - 800000*m.b38 - 300000*m.b39 - 800000*
                       m.b40 - 300000*m.b41 - 800000*m.b42 - 300000*m.b43 - 800000*m.b44 - 300000*m.b45 - 800000*m.b46
                        - 300000*m.b47 - 800000*m.b48 + 100000*m.b1 + 100000*m.b9 + 100000*m.b17 + 100000*m.b25 + 100000
                       *m.b33 + 100000*m.b41 + 400000*m.b2 + 400000*m.b10 + 400000*m.b18 + 400000*m.b26 + 400000*m.b34
                        + 400000*m.b42 + 100000*m.b3 + 100000*m.b11 + 100000*m.b19 + 100000*m.b27 + 100000*m.b35 + 
                       100000*m.b43 + 400000*m.b4 + 400000*m.b12 + 400000*m.b20 + 400000*m.b28 + 400000*m.b36 + 400000*
                       m.b44 + 100000*m.b5 + 100000*m.b13 + 100000*m.b21 + 100000*m.b29 + 100000*m.b37 + 100000*m.b45 + 
                       400000*m.b6 + 400000*m.b14 + 400000*m.b22 + 400000*m.b30 + 400000*m.b38 + 400000*m.b46 + 100000*
                       m.b7 + 100000*m.b15 + 100000*m.b23 + 100000*m.b31 + 100000*m.b39 + 100000*m.b47 + 400000*m.b8 + 
                       400000*m.b16 + 400000*m.b24 + 400000*m.b32 + 400000*m.b40 + 400000*m.b48 + 4000*m.b1 + 3200*m.b2
                        + 8000*m.b9 + 6400*m.b10 + 8000*m.b17 + 6400*m.b18 + 16000*m.b25 + 12800*m.b26 + 16000*m.b33 + 
                       12800*m.b34 + 32000*m.b41 + 25600*m.b42 + 8000*m.b3 + 6400*m.b4 + 4000*m.b11 + 3200*m.b12 + 16000
                       *m.b19 + 12800*m.b20 + 24000*m.b27 + 19200*m.b28 + 8000*m.b35 + 6400*m.b36 + 24000*m.b43 + 19200*
                       m.b44 + 16000*m.b5 + 12800*m.b6 + 24000*m.b13 + 19200*m.b14 + 4000*m.b21 + 3200*m.b22 + 4000*
                       m.b29 + 3200*m.b30 + 16000*m.b37 + 12800*m.b38 + 16000*m.b45 + 12800*m.b46 + 200000*m.b7 + 160000
                       *m.b8 + 200000*m.b15 + 160000*m.b16 + 150000*m.b23 + 120000*m.b24 + 50000*m.b31 + 40000*m.b32 + 
                       100000*m.b39 + 80000*m.b40 + 25000*m.b47 + 20000*m.b48) - 80000*m.b49 - 80000*m.b50 - 80000*m.b51
                        - 80000*m.b52 + 55*m.x53 + 455*m.x54 + 50*m.x55 + 450*m.x56 + 55*m.x57 + 455*m.x58 + 55*m.x59
                        + 455*m.x60, sense=maximize)

m.c1 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 >= 1)

m.c2 = Constraint(expr=   m.b1 + m.b3 + m.b5 + m.b7 == 1)

m.c3 = Constraint(expr=   m.b2 + m.b4 + m.b6 + m.b8 == 1)

m.c4 = Constraint(expr=   m.b9 + m.b11 + m.b13 + m.b15 == 1)

m.c5 = Constraint(expr=   m.b10 + m.b12 + m.b14 + m.b16 == 1)

m.c6 = Constraint(expr=   m.b17 + m.b19 + m.b21 + m.b23 == 1)

m.c7 = Constraint(expr=   m.b18 + m.b20 + m.b22 + m.b24 == 1)

m.c8 = Constraint(expr=   m.b25 + m.b27 + m.b29 + m.b31 == 1)

m.c9 = Constraint(expr=   m.b26 + m.b28 + m.b30 + m.b32 == 1)

m.c10 = Constraint(expr=   m.b33 + m.b35 + m.b37 + m.b39 == 1)

m.c11 = Constraint(expr=   m.b34 + m.b36 + m.b38 + m.b40 == 1)

m.c12 = Constraint(expr=   m.b41 + m.b43 + m.b45 + m.b47 == 1)

m.c13 = Constraint(expr=   m.b42 + m.b44 + m.b46 + m.b48 == 1)

m.c14 = Constraint(expr=   m.b1 - m.b49 <= 0)

m.c15 = Constraint(expr=   m.b2 - m.b49 <= 0)

m.c16 = Constraint(expr=   m.b3 - m.b50 <= 0)

m.c17 = Constraint(expr=   m.b4 - m.b50 <= 0)

m.c18 = Constraint(expr=   m.b5 - m.b51 <= 0)

m.c19 = Constraint(expr=   m.b6 - m.b51 <= 0)

m.c20 = Constraint(expr=   m.b7 - m.b52 <= 0)

m.c21 = Constraint(expr=   m.b8 - m.b52 <= 0)

m.c22 = Constraint(expr=   m.b9 - m.b49 <= 0)

m.c23 = Constraint(expr=   m.b10 - m.b49 <= 0)

m.c24 = Constraint(expr=   m.b11 - m.b50 <= 0)

m.c25 = Constraint(expr=   m.b12 - m.b50 <= 0)

m.c26 = Constraint(expr=   m.b13 - m.b51 <= 0)

m.c27 = Constraint(expr=   m.b14 - m.b51 <= 0)

m.c28 = Constraint(expr=   m.b15 - m.b52 <= 0)

m.c29 = Constraint(expr=   m.b16 - m.b52 <= 0)

m.c30 = Constraint(expr=   m.b17 - m.b49 <= 0)

m.c31 = Constraint(expr=   m.b18 - m.b49 <= 0)

m.c32 = Constraint(expr=   m.b19 - m.b50 <= 0)

m.c33 = Constraint(expr=   m.b20 - m.b50 <= 0)

m.c34 = Constraint(expr=   m.b21 - m.b51 <= 0)

m.c35 = Constraint(expr=   m.b22 - m.b51 <= 0)

m.c36 = Constraint(expr=   m.b23 - m.b52 <= 0)

m.c37 = Constraint(expr=   m.b24 - m.b52 <= 0)

m.c38 = Constraint(expr=   m.b25 - m.b49 <= 0)

m.c39 = Constraint(expr=   m.b26 - m.b49 <= 0)

m.c40 = Constraint(expr=   m.b27 - m.b50 <= 0)

m.c41 = Constraint(expr=   m.b28 - m.b50 <= 0)

m.c42 = Constraint(expr=   m.b29 - m.b51 <= 0)

m.c43 = Constraint(expr=   m.b30 - m.b51 <= 0)

m.c44 = Constraint(expr=   m.b31 - m.b52 <= 0)

m.c45 = Constraint(expr=   m.b32 - m.b52 <= 0)

m.c46 = Constraint(expr=   m.b33 - m.b49 <= 0)

m.c47 = Constraint(expr=   m.b34 - m.b49 <= 0)

m.c48 = Constraint(expr=   m.b35 - m.b50 <= 0)

m.c49 = Constraint(expr=   m.b36 - m.b50 <= 0)

m.c50 = Constraint(expr=   m.b37 - m.b51 <= 0)

m.c51 = Constraint(expr=   m.b38 - m.b51 <= 0)

m.c52 = Constraint(expr=   m.b39 - m.b52 <= 0)

m.c53 = Constraint(expr=   m.b40 - m.b52 <= 0)

m.c54 = Constraint(expr=   m.b41 - m.b49 <= 0)

m.c55 = Constraint(expr=   m.b42 - m.b49 <= 0)

m.c56 = Constraint(expr=   m.b43 - m.b50 <= 0)

m.c57 = Constraint(expr=   m.b44 - m.b50 <= 0)

m.c58 = Constraint(expr=   m.b45 - m.b51 <= 0)

m.c59 = Constraint(expr=   m.b46 - m.b51 <= 0)

m.c60 = Constraint(expr=   m.b47 - m.b52 <= 0)

m.c61 = Constraint(expr=   m.b48 - m.b52 <= 0)

m.c62 = Constraint(expr=   m.b1 + m.b9 + m.b17 + m.b25 + m.b33 + m.b41 - m.b49 >= 0)

m.c63 = Constraint(expr=   m.b2 + m.b10 + m.b18 + m.b26 + m.b34 + m.b42 - m.b49 >= 0)

m.c64 = Constraint(expr=   m.b3 + m.b11 + m.b19 + m.b27 + m.b35 + m.b43 - m.b50 >= 0)

m.c65 = Constraint(expr=   m.b4 + m.b12 + m.b20 + m.b28 + m.b36 + m.b44 - m.b50 >= 0)

m.c66 = Constraint(expr=   m.b5 + m.b13 + m.b21 + m.b29 + m.b37 + m.b45 - m.b51 >= 0)

m.c67 = Constraint(expr=   m.b6 + m.b14 + m.b22 + m.b30 + m.b38 + m.b46 - m.b51 >= 0)

m.c68 = Constraint(expr=   m.b7 + m.b15 + m.b23 + m.b31 + m.b39 + m.b47 - m.b52 >= 0)

m.c69 = Constraint(expr=   m.b8 + m.b16 + m.b24 + m.b32 + m.b40 + m.b48 - m.b52 >= 0)

m.c70 = Constraint(expr= - 5000*m.b49 + m.x53 + m.x54 <= 0)

m.c71 = Constraint(expr= - 3000*m.b50 + m.x55 + m.x56 <= 0)

m.c72 = Constraint(expr= - 3000*m.b51 + m.x57 + m.x58 <= 0)

m.c73 = Constraint(expr= - 2000*m.b52 + m.x59 + m.x60 <= 0)

m.c74 = Constraint(expr=   m.x53 + m.x55 + m.x57 + m.x59 == 6000)

m.c75 = Constraint(expr=   m.x54 + m.x56 + m.x58 + m.x60 == 4800)

m.c76 = Constraint(expr= - 1000*m.b1 - 1000*m.b9 - 1000*m.b17 - 1000*m.b25 - 1000*m.b33 - 1000*m.b41 + m.x53 >= 0)

m.c77 = Constraint(expr= - 800*m.b2 - 800*m.b10 - 800*m.b18 - 800*m.b26 - 800*m.b34 - 800*m.b42 + m.x54 >= 0)

m.c78 = Constraint(expr= - 1000*m.b3 - 1000*m.b11 - 1000*m.b19 - 1000*m.b27 - 1000*m.b35 - 1000*m.b43 + m.x55 >= 0)

m.c79 = Constraint(expr= - 800*m.b4 - 800*m.b12 - 800*m.b20 - 800*m.b28 - 800*m.b36 - 800*m.b44 + m.x56 >= 0)

m.c80 = Constraint(expr= - 1000*m.b5 - 1000*m.b13 - 1000*m.b21 - 1000*m.b29 - 1000*m.b37 - 1000*m.b45 + m.x57 >= 0)

m.c81 = Constraint(expr= - 800*m.b6 - 800*m.b14 - 800*m.b22 - 800*m.b30 - 800*m.b38 - 800*m.b46 + m.x58 >= 0)

m.c82 = Constraint(expr= - 1000*m.b7 - 1000*m.b15 - 1000*m.b23 - 1000*m.b31 - 1000*m.b39 - 1000*m.b47 + m.x59 >= 0)

m.c83 = Constraint(expr= - 800*m.b8 - 800*m.b16 - 800*m.b24 - 800*m.b32 - 800*m.b40 - 800*m.b48 + m.x60 >= 0)
