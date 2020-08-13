#  MINLP written by GAMS Convert at 08/13/20 17:37:55
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         41       13        0       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         61       17       44        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        197      161       36        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.b1 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b2 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b3 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b4 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b5 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b6 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b7 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b8 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b9 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b10 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b11 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b12 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b13 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b14 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b15 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b16 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b17 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b18 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b19 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b20 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b21 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b22 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b23 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b24 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b25 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b26 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b27 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b28 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b29 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b30 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b31 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b32 = Var(within=Binary,bounds=(0,1),initialize=0.25)
m.b33 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b34 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b35 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b36 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b37 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b38 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b39 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b40 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b41 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b42 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b43 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.b44 = Var(within=Binary,bounds=(0,1),initialize=0.333333333333333)
m.x45 = Var(within=Reals,bounds=(0,None),initialize=1.11031856270584)
m.x46 = Var(within=Reals,bounds=(0,None),initialize=1.47346120210071)
m.x47 = Var(within=Reals,bounds=(0,None),initialize=2.45215090742002)
m.x48 = Var(within=Reals,bounds=(0,None),initialize=1.49443619616504)
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0.175379297755911)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0.175379297755911)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0.175379297755911)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0.198569411000437)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0.198569411000437)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0.198569411000437)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0.23677517516682)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0.23677517516682)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0.23677517516682)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0.199702601929659)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0.199702601929659)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0.199702601929659)

m.obj = Objective(expr=   222.395350591392*m.b1 + 582.786400468795*m.b2 + 119.753843399653*m.b3 + 338.549698035479*m.b4
                        + 119.783636606301*m.b5 + 409.374679229076*m.b6 + 278.20529021903*m.b7 + 306.426594992684*m.b8
                        + 441.233650379831*m.b9 + 153.049293317818*m.b10 + 439.090557840933*m.b11
                        + 175.155823424664*m.b12 + 612.328425893001*m.b13 + 146.717315955674*m.b14
                        + 676.916374379371*m.b15 + 425.643803755754*m.b16 + 476.000407399777*m.b17
                        + 218.667102585295*m.b18 + 429.494068158725*m.b19 + 260.065761415496*m.b20
                        + 228.081133173702*m.b21 + 290.916261365409*m.b22 + 358.983740312016*m.b23
                        + 303.078553779965*m.b24 + 224.102176788463*m.b25 + 372.279886491354*m.b26
                        + 217.090150838618*m.b27 + 84.469492807076*m.b28 + 274.179320847966*m.b29
                        + 209.61866336051*m.b30 + 205.445642503502*m.b31 + 144.701484010017*m.b32 + 270.520699*m.b33
                        + 100.444790162654*m.b34 + 64.9166596734302*m.b35 + 330.80933975*m.b36 + 110.205022516595*m.b37
                        + 67.4648851252699*m.b38 + 297.23545225*m.b39 + 96.7703053435877*m.b40 + 58.5635369942729*m.b41
                        + 252.028512*m.b42 + 91.7540307917193*m.b43 + 58.7189192724058*m.b44 + 67691.6374379371*m.x45
                        + 67691.6374379371*m.x46 + 67691.6374379371*m.x47 + 67691.6374379371*m.x48, sense=minimize)

m.c2 = Constraint(expr=   0.990828132*m.b1 + 0.7867768*m.b5 + 1.1494727*m.b9 + 1.090185213*m.b13 + 0.861308711*m.b17
                        + 0.646379815*m.b21 + 1.205697202*m.b25 + 0.554843463*m.b29 - 1.730889404*m.x49
                        - 3.461778808*m.x50 - 5.192668212*m.x51 == 0)

m.c3 = Constraint(expr=   0.990828132*m.b2 + 0.7867768*m.b6 + 1.1494727*m.b10 + 1.090185213*m.b14 + 0.861308711*m.b18
                        + 0.646379815*m.b22 + 1.205697202*m.b26 + 0.554843463*m.b30 - 1.528745876*m.x52
                        - 3.057491752*m.x53 - 4.586237628*m.x54 == 0)

m.c4 = Constraint(expr=   0.990828132*m.b3 + 0.7867768*m.b7 + 1.1494727*m.b11 + 1.090185213*m.b15 + 0.861308711*m.b19
                        + 0.646379815*m.b23 + 1.205697202*m.b27 + 0.554843463*m.b31 - 1.282069237*m.x55
                        - 2.564138474*m.x56 - 3.846207711*m.x57 == 0)

m.c5 = Constraint(expr=   0.990828132*m.b4 + 0.7867768*m.b8 + 1.1494727*m.b12 + 1.090185213*m.b16 + 0.861308711*m.b20
                        + 0.646379815*m.b24 + 1.205697202*m.b28 + 0.554843463*m.b32 - 1.520071172*m.x58
                        - 3.040142344*m.x59 - 4.560213516*m.x60 == 0)

m.c6 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 == 1)

m.c7 = Constraint(expr=   m.b5 + m.b6 + m.b7 + m.b8 == 1)

m.c8 = Constraint(expr=   m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c9 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 == 1)

m.c10 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 == 1)

m.c11 = Constraint(expr=   m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c12 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 == 1)

m.c13 = Constraint(expr=   m.b29 + m.b30 + m.b31 + m.b32 == 1)

m.c14 = Constraint(expr=   m.b33 + m.b34 + m.b35 <= 1)

m.c15 = Constraint(expr=   m.b36 + m.b37 + m.b38 <= 1)

m.c16 = Constraint(expr=   m.b39 + m.b40 + m.b41 <= 1)

m.c17 = Constraint(expr=   m.b42 + m.b43 + m.b44 <= 1)

m.c18 = Constraint(expr= - m.b33 + m.x49 <= 0)

m.c19 = Constraint(expr= - m.b34 + m.x50 <= 0)

m.c20 = Constraint(expr= - m.b35 + m.x51 <= 0)

m.c21 = Constraint(expr= - m.b36 + m.x52 <= 0)

m.c22 = Constraint(expr= - m.b37 + m.x53 <= 0)

m.c23 = Constraint(expr= - m.b38 + m.x54 <= 0)

m.c24 = Constraint(expr= - m.b39 + m.x55 <= 0)

m.c25 = Constraint(expr= - m.b40 + m.x56 <= 0)

m.c26 = Constraint(expr= - m.b41 + m.x57 <= 0)

m.c27 = Constraint(expr= - m.b42 + m.x58 <= 0)

m.c28 = Constraint(expr= - m.b43 + m.x59 <= 0)

m.c29 = Constraint(expr= - m.b44 + m.x60 <= 0)

m.c30 = Constraint(expr=m.x49*m.b33 + m.x49*m.x45 - m.x45*m.b33 <= 0)

m.c31 = Constraint(expr=m.x50*m.b34 + m.x50*m.x45 - m.x45*m.b34 <= 0)

m.c32 = Constraint(expr=m.x51*m.b35 + m.x51*m.x45 - m.x45*m.b35 <= 0)

m.c33 = Constraint(expr=m.x52*m.b36 + m.x52*m.x46 - m.x46*m.b36 <= 0)

m.c34 = Constraint(expr=m.x53*m.b37 + m.x53*m.x46 - m.x46*m.b37 <= 0)

m.c35 = Constraint(expr=m.x54*m.b38 + m.x54*m.x46 - m.x46*m.b38 <= 0)

m.c36 = Constraint(expr=m.x55*m.b39 + m.x55*m.x47 - m.x47*m.b39 <= 0)

m.c37 = Constraint(expr=m.x56*m.b40 + m.x56*m.x47 - m.x47*m.b40 <= 0)

m.c38 = Constraint(expr=m.x57*m.b41 + m.x57*m.x47 - m.x47*m.b41 <= 0)

m.c39 = Constraint(expr=m.x58*m.b42 + m.x58*m.x48 - m.x48*m.b42 <= 0)

m.c40 = Constraint(expr=m.x59*m.b43 + m.x59*m.x48 - m.x48*m.b43 <= 0)

m.c41 = Constraint(expr=m.x60*m.b44 + m.x60*m.x48 - m.x48*m.b44 <= 0)
