#  MINLP written by GAMS Convert at 08/13/20 17:37:59
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         84       43        0       41        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         75       55       20        0        0        0        0        0
#  FX      6        6        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        302      188      114        0
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
m.x22 = Var(within=Reals,bounds=(40,90),initialize=40)
m.x23 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x27 = Var(within=Reals,bounds=(40,40),initialize=40)
m.x28 = Var(within=Reals,bounds=(50,50),initialize=50)
m.x29 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,40),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,90),initialize=0)
m.x49 = Var(within=Reals,bounds=(40,90),initialize=40)
m.x50 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,0),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,50),initialize=0)
m.x54 = Var(within=Reals,bounds=(25,25),initialize=25)
m.x55 = Var(within=Reals,bounds=(37.5,37.5),initialize=37.5)
m.x56 = Var(within=Reals,bounds=(20,70),initialize=20)
m.x57 = Var(within=Reals,bounds=(20,70),initialize=20)
m.x58 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,3.5),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,3.5),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,25),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,37.5),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,3.5),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,70),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,3.5),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,10),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,10),initialize=0)

m.obj = Objective(expr=0.1*(16800*(0.001 + m.x47)**0.7 + 12600*(0.001 + m.x48)**0.7) + 8000*m.x47 + 53.6*m.x48 + 0.1*(
                       100*(0.001 + m.x23)**0.6 + 100*(0.001 + m.x24)**0.6 + 100*(0.001 + m.x25)**0.6 + 100*(0.001 + 
                       m.x26)**0.6 + 100*(0.001 + m.x29)**0.6 + 100*(0.001 + m.x30)**0.6 + 100*(0.001 + m.x31)**0.6 + 
                       100*(0.001 + m.x32)**0.6 + 100*(0.001 + m.x33)**0.6 + 100*(0.001 + m.x34)**0.6 + 100*(0.001 + 
                       m.x35)**0.6 + 100*(0.001 + m.x36)**0.6 + 100*(0.001 + m.x37)**0.6 + 100*(0.001 + m.x38)**0.6 + 
                       100*(0.001 + m.x39)**0.6 + 100*(0.001 + m.x40)**0.6 + 100*(0.001 + m.x43)**0.6 + 100*(0.001 + 
                       m.x44)**0.6 + 100*(0.001 + m.x41)**0.6 + 100*(0.001 + m.x42)**0.6) + 48*m.x23 + 48*m.x24 + 48*
                       m.x25 + 48*m.x26 + 48*m.x29 + 48*m.x30 + 48*m.x31 + 48*m.x32 + 48*m.x33 + 48*m.x34 + 48*m.x35 + 
                       48*m.x36 + 48*m.x37 + 48*m.x38 + 48*m.x39 + 48*m.x40 + 48*m.x41 + 48*m.x42 + 48*m.x43 + 48*m.x44
                        + 0.6*m.b1 + 0.6*m.b2 + 0.6*m.b3 + 0.6*m.b4 + 0.6*m.b5 + 0.6*m.b6 + 0.6*m.b7 + 0.6*m.b8
                        + 0.6*m.b9 + 0.6*m.b10 + 0.6*m.b11 + 0.6*m.b12 + 0.6*m.b13 + 0.6*m.b14 + 0.6*m.b15 + 0.6*m.b16
                        + 0.6*m.b17 + 0.6*m.b18 + 0.6*m.b19 + 0.6*m.b20 + 8000*m.x22, sense=minimize)

m.c2 = Constraint(expr=   m.x22 - m.x23 - m.x24 - m.x25 - m.x26 == 0)

m.c3 = Constraint(expr= - m.x23 - m.x30 - m.x37 - m.x39 == -40)

m.c4 = Constraint(expr= - m.x24 - m.x29 - m.x38 - m.x40 == -50)

m.c5 = Constraint(expr=-(m.x30*m.x56 + m.x37*m.x62 + m.x39*m.x64) + 40*m.x50 == 0)

m.c6 = Constraint(expr=-(m.x30*m.x57 + m.x37*m.x63 + m.x39*m.x65) + 40*m.x51 == 0)

m.c7 = Constraint(expr=-(m.x29*m.x54 + m.x38*m.x62 + m.x40*m.x64) + 50*m.x52 == 0)

m.c8 = Constraint(expr=-(m.x29*m.x55 + m.x38*m.x63 + m.x40*m.x65) + 50*m.x53 == 0)

m.c9 = Constraint(expr= - m.x27 == -40)

m.c10 = Constraint(expr= - m.x28 == -50)

m.c11 = Constraint(expr=-m.x27*m.x54 + 40*m.x50 == -1000)

m.c12 = Constraint(expr=-m.x27*m.x55 + 40*m.x51 == -1500)

m.c13 = Constraint(expr=-m.x28*m.x56 + 50*m.x52 == -1000)

m.c14 = Constraint(expr=-m.x28*m.x57 + 50*m.x53 == -1000)

m.c15 = Constraint(expr=   m.x27 - m.x29 - m.x31 - m.x32 - m.x35 == 0)

m.c16 = Constraint(expr=   m.x28 - m.x30 - m.x33 - m.x34 - m.x36 == 0)

m.c17 = Constraint(expr= - m.x54 + m.x66 == 0)

m.c18 = Constraint(expr= - m.x55 + m.x67 == 0)

m.c19 = Constraint(expr= - m.x56 + m.x68 == 0)

m.c20 = Constraint(expr= - m.x57 + m.x69 == 0)

m.c21 = Constraint(expr= - m.x25 - m.x31 - m.x33 - m.x42 + m.x45 == 0)

m.c22 = Constraint(expr= - m.x26 - m.x32 - m.x34 - m.x41 + m.x46 == 0)

m.c23 = Constraint(expr=m.x45*m.x58 - (m.x42*m.x72 + m.x31*m.x66 + m.x33*m.x68) == 0)

m.c24 = Constraint(expr=m.x45*m.x59 - (m.x42*m.x73 + m.x31*m.x67 + m.x33*m.x69) == 0)

m.c25 = Constraint(expr=m.x46*m.x60 - (m.x41*m.x70 + m.x32*m.x66 + m.x34*m.x68) == 0)

m.c26 = Constraint(expr=m.x46*m.x61 - (m.x41*m.x71 + m.x32*m.x67 + m.x34*m.x69) == 0)

m.c27 = Constraint(expr=   m.x45 - m.x47 == 0)

m.c28 = Constraint(expr=   m.x46 - m.x48 == 0)

m.c29 = Constraint(expr= - 0.0499999999999999*m.x58 + m.x62 == 0)

m.c30 = Constraint(expr= - m.x59 + m.x63 == 0)

m.c31 = Constraint(expr= - m.x60 + m.x64 == 0)

m.c32 = Constraint(expr= - 0.0499999999999999*m.x61 + m.x65 == 0)

m.c33 = Constraint(expr= - m.x37 - m.x38 - m.x41 - m.x43 + m.x47 == 0)

m.c34 = Constraint(expr= - m.x39 - m.x40 - m.x42 - m.x44 + m.x48 == 0)

m.c35 = Constraint(expr= - m.x62 + m.x70 == 0)

m.c36 = Constraint(expr= - m.x63 + m.x71 == 0)

m.c37 = Constraint(expr= - m.x64 + m.x72 == 0)

m.c38 = Constraint(expr= - m.x65 + m.x73 == 0)

m.c39 = Constraint(expr= - m.x35 - m.x36 - m.x43 - m.x44 + m.x49 == 0)

m.c40 = Constraint(expr=m.x49*m.x74 - (m.x35*m.x66 + m.x36*m.x68 + m.x43*m.x70 + m.x44*m.x72) == 0)

m.c41 = Constraint(expr=m.x49*m.x75 - (m.x35*m.x67 + m.x36*m.x69 + m.x43*m.x71 + m.x44*m.x73) == 0)

m.c42 = Constraint(expr=-(0.95*m.x45*m.x58 + m.x49*m.x74) == -2000)

m.c43 = Constraint(expr=-(0.95*m.x46*m.x61 + m.x49*m.x75) == -2500)

m.c44 = Constraint(expr= - 40*m.b17 + m.x37 <= 0)

m.c45 = Constraint(expr= - 50*m.b18 + m.x38 <= 0)

m.c46 = Constraint(expr= - 40*m.b19 + m.x39 <= 0)

m.c47 = Constraint(expr= - 50*m.b20 + m.x40 <= 0)

m.c48 = Constraint(expr= - m.x37 <= 0)

m.c49 = Constraint(expr= - m.x38 <= 0)

m.c50 = Constraint(expr= - m.x39 <= 0)

m.c51 = Constraint(expr= - m.x40 <= 0)

m.c52 = Constraint(expr= - 40*m.b5 + m.x29 <= 0)

m.c53 = Constraint(expr= - 40*m.b6 + m.x30 <= 0)

m.c54 = Constraint(expr= - m.x29 <= 0)

m.c55 = Constraint(expr= - m.x30 <= 0)

m.c56 = Constraint(expr= - 40*m.b7 + m.x31 <= 0)

m.c57 = Constraint(expr= - 40*m.b8 + m.x32 <= 0)

m.c58 = Constraint(expr= - 50*m.b9 + m.x33 <= 0)

m.c59 = Constraint(expr= - 50*m.b10 + m.x34 <= 0)

m.c60 = Constraint(expr= - m.x31 <= 0)

m.c61 = Constraint(expr= - m.x32 <= 0)

m.c62 = Constraint(expr= - m.x33 <= 0)

m.c63 = Constraint(expr= - m.x34 <= 0)

m.c64 = Constraint(expr= - 40*m.b11 + m.x35 <= 0)

m.c65 = Constraint(expr= - 50*m.b12 + m.x36 <= 0)

m.c66 = Constraint(expr= - m.x35 <= 0)

m.c67 = Constraint(expr= - m.x36 <= 0)

m.c68 = Constraint(expr= - 90*m.b13 + m.x43 <= 0)

m.c69 = Constraint(expr= - 90*m.b14 + m.x44 <= 0)

m.c70 = Constraint(expr= - m.x43 <= 0)

m.c71 = Constraint(expr= - m.x44 <= 0)

m.c72 = Constraint(expr= - 90*m.b15 + m.x41 <= 0)

m.c73 = Constraint(expr= - 90*m.b16 + m.x42 <= 0)

m.c74 = Constraint(expr= - m.x41 <= 0)

m.c75 = Constraint(expr= - m.x42 <= 0)

m.c76 = Constraint(expr= - 40*m.b1 + m.x23 <= 0)

m.c77 = Constraint(expr= - 50*m.b2 + m.x24 <= 0)

m.c78 = Constraint(expr= - m.x23 <= 0)

m.c79 = Constraint(expr= - m.x24 <= 0)

m.c80 = Constraint(expr= - 90*m.b3 + m.x25 <= 0)

m.c81 = Constraint(expr= - 90*m.b4 + m.x26 <= 0)

m.c82 = Constraint(expr= - m.x25 <= 0)

m.c83 = Constraint(expr= - m.x26 <= 0)

m.c84 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 + m.b11 + m.b12 + m.b13
                         + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 <= 20)
