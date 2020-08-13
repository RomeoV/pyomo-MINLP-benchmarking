#  MINLP written by GAMS Convert at 08/13/20 17:37:58
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         73       10       33       30        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         70       40       30        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        409      169      240        0
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
m.x49 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x62 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x63 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x64 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x65 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x66 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x67 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x68 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x69 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x70 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=   m.x62 + m.x63 + m.x64 + m.x65 + m.x66 + m.x67 + m.x68 + m.x69 + 2*m.x70, sense=minimize)

m.c1 = Constraint(expr=-((5.02 - 0.0003*m.x31 - 0.0007*m.x32 - 0.0066*m.x33 - 0.0044*m.x34 - 0.0208*m.x35 - 0.0518*m.x36
                        - 0.0036*m.x37 - 0.0507*m.x38 - 0.0905*m.x39 - 0.0016*m.x40)*(5.02 - 0.0003*m.x31 - 0.0007*m.x32
                        - 0.0066*m.x33 - 0.0044*m.x34 - 0.0208*m.x35 - 0.0518*m.x36 - 0.0036*m.x37 - 0.0507*m.x38 - 
                       0.0905*m.x39 - 0.0016*m.x40) + (0.97 - 0.0003*m.x41 - 0.0007*m.x42 - 0.0066*m.x43 - 0.0044*m.x44
                        - 0.0208*m.x45 - 0.0518*m.x46 - 0.0036*m.x47 - 0.0507*m.x48 - 0.0905*m.x49 - 0.0016*m.x50)*(0.97
                        - 0.0003*m.x41 - 0.0007*m.x42 - 0.0066*m.x43 - 0.0044*m.x44 - 0.0208*m.x45 - 0.0518*m.x46 - 
                       0.0036*m.x47 - 0.0507*m.x48 - 0.0905*m.x49 - 0.0016*m.x50) + (-0.0003*m.x51 - 0.0007*m.x52 - 
                       0.0066*m.x53 - 0.0044*m.x54 - 0.0208*m.x55 - 0.0518*m.x56 - 0.0036*m.x57 - 0.0507*m.x58 - 0.0905*
                       m.x59 - 0.0016*m.x60)*(-0.0003*m.x51 - 0.0007*m.x52 - 0.0066*m.x53 - 0.0044*m.x54 - 0.0208*m.x55
                        - 0.0518*m.x56 - 0.0036*m.x57 - 0.0507*m.x58 - 0.0905*m.x59 - 0.0016*m.x60)) + m.x62 == 0)

m.c2 = Constraint(expr=-((2.04 - 0.0764*m.x31 - 0.0003*m.x32 - 0.0789*m.x33 - 0.0186*m.x34 - 0.0605*m.x35 - 0.1656*m.x36
                        - 0.0035*m.x37 - 0.0361*m.x38 - 0.06*m.x39 - 0.0209*m.x40)*(2.04 - 0.0764*m.x31 - 0.0003*m.x32
                        - 0.0789*m.x33 - 0.0186*m.x34 - 0.0605*m.x35 - 0.1656*m.x36 - 0.0035*m.x37 - 0.0361*m.x38 - 0.06
                       *m.x39 - 0.0209*m.x40) + (3.51 - 0.0764*m.x41 - 0.0003*m.x42 - 0.0789*m.x43 - 0.0186*m.x44 - 
                       0.0605*m.x45 - 0.1656*m.x46 - 0.0035*m.x47 - 0.0361*m.x48 - 0.06*m.x49 - 0.0209*m.x50)*(3.51 - 
                       0.0764*m.x41 - 0.0003*m.x42 - 0.0789*m.x43 - 0.0186*m.x44 - 0.0605*m.x45 - 0.1656*m.x46 - 0.0035*
                       m.x47 - 0.0361*m.x48 - 0.06*m.x49 - 0.0209*m.x50) + (2.2 - 0.0764*m.x51 - 0.0003*m.x52 - 0.0789*
                       m.x53 - 0.0186*m.x54 - 0.0605*m.x55 - 0.1656*m.x56 - 0.0035*m.x57 - 0.0361*m.x58 - 0.06*m.x59 - 
                       0.0209*m.x60)*(2.2 - 0.0764*m.x51 - 0.0003*m.x52 - 0.0789*m.x53 - 0.0186*m.x54 - 0.0605*m.x55 - 
                       0.1656*m.x56 - 0.0035*m.x57 - 0.0361*m.x58 - 0.06*m.x59 - 0.0209*m.x60)) + m.x63 == 0)

m.c3 = Constraint(expr=-((3.53 - 0.0318*m.x31 - 0.0004*m.x32 - 0.0275*m.x33 - 0.018*m.x34 - 0.0601*m.x35 - 0.1491*m.x36
                        - 0.0032*m.x37 - 0.0433*m.x38 - 0.0754*m.x39 - 0.0063*m.x40)*(3.53 - 0.0318*m.x31 - 0.0004*m.x32
                        - 0.0275*m.x33 - 0.018*m.x34 - 0.0601*m.x35 - 0.1491*m.x36 - 0.0032*m.x37 - 0.0433*m.x38 - 
                       0.0754*m.x39 - 0.0063*m.x40) + (3.51 - 0.0318*m.x41 - 0.0004*m.x42 - 0.0275*m.x43 - 0.018*m.x44
                        - 0.0601*m.x45 - 0.1491*m.x46 - 0.0032*m.x47 - 0.0433*m.x48 - 0.0754*m.x49 - 0.0063*m.x50)*(3.51
                        - 0.0318*m.x41 - 0.0004*m.x42 - 0.0275*m.x43 - 0.018*m.x44 - 0.0601*m.x45 - 0.1491*m.x46 - 
                       0.0032*m.x47 - 0.0433*m.x48 - 0.0754*m.x49 - 0.0063*m.x50) + (0.8 - 0.0318*m.x51 - 0.0004*m.x52
                        - 0.0275*m.x53 - 0.018*m.x54 - 0.0601*m.x55 - 0.1491*m.x56 - 0.0032*m.x57 - 0.0433*m.x58 - 
                       0.0754*m.x59 - 0.0063*m.x60)*(0.8 - 0.0318*m.x51 - 0.0004*m.x52 - 0.0275*m.x53 - 0.018*m.x54 - 
                       0.0601*m.x55 - 0.1491*m.x56 - 0.0032*m.x57 - 0.0433*m.x58 - 0.0754*m.x59 - 0.0063*m.x60)) + m.x64
                        == 0)

m.c4 = Constraint(expr=-((7.02 - 0.0007*m.x31 - 0.0009*m.x32 - 0.0043*m.x33 - 0.0179*m.x34 - 0.0604*m.x35 - 0.1385*m.x36
                        - 0.0051*m.x37 - 0.0635*m.x38 - 0.1098*m.x39 - 0.001*m.x40)*(7.02 - 0.0007*m.x31 - 0.0009*m.x32
                        - 0.0043*m.x33 - 0.0179*m.x34 - 0.0604*m.x35 - 0.1385*m.x36 - 0.0051*m.x37 - 0.0635*m.x38 - 
                       0.1098*m.x39 - 0.001*m.x40) + (3.51 - 0.0007*m.x41 - 0.0009*m.x42 - 0.0043*m.x43 - 0.0179*m.x44
                        - 0.0604*m.x45 - 0.1385*m.x46 - 0.0051*m.x47 - 0.0635*m.x48 - 0.1098*m.x49 - 0.001*m.x50)*(3.51
                        - 0.0007*m.x41 - 0.0009*m.x42 - 0.0043*m.x43 - 0.0179*m.x44 - 0.0604*m.x45 - 0.1385*m.x46 - 
                       0.0051*m.x47 - 0.0635*m.x48 - 0.1098*m.x49 - 0.001*m.x50) + (-0.0007*m.x51 - 0.0009*m.x52 - 
                       0.0043*m.x53 - 0.0179*m.x54 - 0.0604*m.x55 - 0.1385*m.x56 - 0.0051*m.x57 - 0.0635*m.x58 - 0.1098*
                       m.x59 - 0.001*m.x60)*(-0.0007*m.x51 - 0.0009*m.x52 - 0.0043*m.x53 - 0.0179*m.x54 - 0.0604*m.x55
                        - 0.1385*m.x56 - 0.0051*m.x57 - 0.0635*m.x58 - 0.1098*m.x59 - 0.001*m.x60)) + m.x65 == 0)

m.c5 = Constraint(expr=-((-0.0534*m.x31 - 0.0005*m.x32 - 0.0704*m.x33 - 0.0351*m.x34 - 0.0981*m.x35 - 0.2389*m.x36 - 
                       0.0015*m.x37 - 0.0048*m.x38 - 0.0038*m.x39 - 0.0132*m.x40)*(-0.0534*m.x31 - 0.0005*m.x32 - 0.0704
                       *m.x33 - 0.0351*m.x34 - 0.0981*m.x35 - 0.2389*m.x36 - 0.0015*m.x37 - 0.0048*m.x38 - 0.0038*m.x39
                        - 0.0132*m.x40) + (7 - 0.0534*m.x41 - 0.0005*m.x42 - 0.0704*m.x43 - 0.0351*m.x44 - 0.0981*m.x45
                        - 0.2389*m.x46 - 0.0015*m.x47 - 0.0048*m.x48 - 0.0038*m.x49 - 0.0132*m.x50)*(7 - 0.0534*m.x41 - 
                       0.0005*m.x42 - 0.0704*m.x43 - 0.0351*m.x44 - 0.0981*m.x45 - 0.2389*m.x46 - 0.0015*m.x47 - 0.0048*
                       m.x48 - 0.0038*m.x49 - 0.0132*m.x50) + (1.4 - 0.0534*m.x51 - 0.0005*m.x52 - 0.0704*m.x53 - 0.0351
                       *m.x54 - 0.0981*m.x55 - 0.2389*m.x56 - 0.0015*m.x57 - 0.0048*m.x58 - 0.0038*m.x59 - 0.0132*m.x60)
                       *(1.4 - 0.0534*m.x51 - 0.0005*m.x52 - 0.0704*m.x53 - 0.0351*m.x54 - 0.0981*m.x55 - 0.2389*m.x56
                        - 0.0015*m.x57 - 0.0048*m.x58 - 0.0038*m.x59 - 0.0132*m.x60)) + m.x66 == 0)

m.c6 = Constraint(expr=-((10.16 - 0.0773*m.x31 - 0.0009*m.x32 - 0.0683*m.x33 - 0.0024*m.x34 - 0.0025*m.x35 - 0.0248*
                       m.x36 - 0.0094*m.x37 - 0.0891*m.x38 - 0.1443*m.x39 - 0.0203*m.x40)*(10.16 - 0.0773*m.x31 - 0.0009
                       *m.x32 - 0.0683*m.x33 - 0.0024*m.x34 - 0.0025*m.x35 - 0.0248*m.x36 - 0.0094*m.x37 - 0.0891*m.x38
                        - 0.1443*m.x39 - 0.0203*m.x40) + (-0.0773*m.x41 - 0.0009*m.x42 - 0.0683*m.x43 - 0.0024*m.x44 - 
                       0.0025*m.x45 - 0.0248*m.x46 - 0.0094*m.x47 - 0.0891*m.x48 - 0.1443*m.x49 - 0.0203*m.x50)*(-0.0773
                       *m.x41 - 0.0009*m.x42 - 0.0683*m.x43 - 0.0024*m.x44 - 0.0025*m.x45 - 0.0248*m.x46 - 0.0094*m.x47
                        - 0.0891*m.x48 - 0.1443*m.x49 - 0.0203*m.x50) + (2.2 - 0.0773*m.x51 - 0.0009*m.x52 - 0.0683*
                       m.x53 - 0.0024*m.x54 - 0.0025*m.x55 - 0.0248*m.x56 - 0.0094*m.x57 - 0.0891*m.x58 - 0.1443*m.x59
                        - 0.0203*m.x60)*(2.2 - 0.0773*m.x51 - 0.0009*m.x52 - 0.0683*m.x53 - 0.0024*m.x54 - 0.0025*m.x55
                        - 0.0248*m.x56 - 0.0094*m.x57 - 0.0891*m.x58 - 0.1443*m.x59 - 0.0203*m.x60)) + m.x67 == 0)

m.c7 = Constraint(expr=-((1.04 - 0.0536*m.x31 - 0.0005*m.x32 - 0.0842*m.x33 - 0.0108*m.x34 - 0.0394*m.x35 - 0.1122*m.x36
                        - 0.0015*m.x37 - 0.0213*m.x38 - 0.042*m.x39 - 0.0139*m.x40)*(1.04 - 0.0536*m.x31 - 0.0005*m.x32
                        - 0.0842*m.x33 - 0.0108*m.x34 - 0.0394*m.x35 - 0.1122*m.x36 - 0.0015*m.x37 - 0.0213*m.x38 - 
                       0.042*m.x39 - 0.0139*m.x40) + (2.01 - 0.0536*m.x41 - 0.0005*m.x42 - 0.0842*m.x43 - 0.0108*m.x44
                        - 0.0394*m.x45 - 0.1122*m.x46 - 0.0015*m.x47 - 0.0213*m.x48 - 0.042*m.x49 - 0.0139*m.x50)*(2.01
                        - 0.0536*m.x41 - 0.0005*m.x42 - 0.0842*m.x43 - 0.0108*m.x44 - 0.0394*m.x45 - 0.1122*m.x46 - 
                       0.0015*m.x47 - 0.0213*m.x48 - 0.042*m.x49 - 0.0139*m.x50) + (1.4 - 0.0536*m.x51 - 0.0005*m.x52 - 
                       0.0842*m.x53 - 0.0108*m.x54 - 0.0394*m.x55 - 0.1122*m.x56 - 0.0015*m.x57 - 0.0213*m.x58 - 0.042*
                       m.x59 - 0.0139*m.x60)*(1.4 - 0.0536*m.x51 - 0.0005*m.x52 - 0.0842*m.x53 - 0.0108*m.x54 - 0.0394*
                       m.x55 - 0.1122*m.x56 - 0.0015*m.x57 - 0.0213*m.x58 - 0.042*m.x59 - 0.0139*m.x60)) + m.x68 == 0)

m.c8 = Constraint(expr=-((2.04 - 0.032*m.x31 - 0.0003*m.x32 - 0.0309*m.x33 - 0.0052*m.x34 - 0.0221*m.x35 - 0.0633*m.x36
                        - 0.0024*m.x37 - 0.031*m.x38 - 0.0574*m.x39 - 0.0057*m.x40)*(2.04 - 0.032*m.x31 - 0.0003*m.x32
                        - 0.0309*m.x33 - 0.0052*m.x34 - 0.0221*m.x35 - 0.0633*m.x36 - 0.0024*m.x37 - 0.031*m.x38 - 
                       0.0574*m.x39 - 0.0057*m.x40) + (0.97 - 0.032*m.x41 - 0.0003*m.x42 - 0.0309*m.x43 - 0.0052*m.x44
                        - 0.0221*m.x45 - 0.0633*m.x46 - 0.0024*m.x47 - 0.031*m.x48 - 0.0574*m.x49 - 0.0057*m.x50)*(0.97
                        - 0.032*m.x41 - 0.0003*m.x42 - 0.0309*m.x43 - 0.0052*m.x44 - 0.0221*m.x45 - 0.0633*m.x46 - 
                       0.0024*m.x47 - 0.031*m.x48 - 0.0574*m.x49 - 0.0057*m.x50) + (0.8 - 0.032*m.x51 - 0.0003*m.x52 - 
                       0.0309*m.x53 - 0.0052*m.x54 - 0.0221*m.x55 - 0.0633*m.x56 - 0.0024*m.x57 - 0.031*m.x58 - 0.0574*
                       m.x59 - 0.0057*m.x60)*(0.8 - 0.032*m.x51 - 0.0003*m.x52 - 0.0309*m.x53 - 0.0052*m.x54 - 0.0221*
                       m.x55 - 0.0633*m.x56 - 0.0024*m.x57 - 0.031*m.x58 - 0.0574*m.x59 - 0.0057*m.x60)) + m.x69 == 0)

m.c9 = Constraint(expr=   m.x31 >= 0)

m.c10 = Constraint(expr=   m.x32 >= 0)

m.c11 = Constraint(expr=   m.x33 >= 0)

m.c12 = Constraint(expr=   m.x34 >= 0)

m.c13 = Constraint(expr=   m.x35 >= 0)

m.c14 = Constraint(expr=   m.x36 >= 0)

m.c15 = Constraint(expr=   m.x37 >= 0)

m.c16 = Constraint(expr=   m.x38 >= 0)

m.c17 = Constraint(expr=   m.x39 >= 0)

m.c18 = Constraint(expr=   m.x40 >= 0)

m.c19 = Constraint(expr=   m.x41 >= 0)

m.c20 = Constraint(expr=   m.x42 >= 0)

m.c21 = Constraint(expr=   m.x43 >= 0)

m.c22 = Constraint(expr=   m.x44 >= 0)

m.c23 = Constraint(expr=   m.x45 >= 0)

m.c24 = Constraint(expr=   m.x46 >= 0)

m.c25 = Constraint(expr=   m.x47 >= 0)

m.c26 = Constraint(expr=   m.x48 >= 0)

m.c27 = Constraint(expr=   m.x49 >= 0)

m.c28 = Constraint(expr=   m.x50 >= 0)

m.c29 = Constraint(expr=   m.x51 >= 0)

m.c30 = Constraint(expr=   m.x52 >= 0)

m.c31 = Constraint(expr=   m.x53 >= 0)

m.c32 = Constraint(expr=   m.x54 >= 0)

m.c33 = Constraint(expr=   m.x55 >= 0)

m.c34 = Constraint(expr=   m.x56 >= 0)

m.c35 = Constraint(expr=   m.x57 >= 0)

m.c36 = Constraint(expr=   m.x58 >= 0)

m.c37 = Constraint(expr=   m.x59 >= 0)

m.c38 = Constraint(expr=   m.x60 >= 0)

m.c39 = Constraint(expr= - 1000*m.b1 + m.x31 <= 0)

m.c40 = Constraint(expr= - 1000*m.b2 + m.x32 <= 0)

m.c41 = Constraint(expr= - 1000*m.b3 + m.x33 <= 0)

m.c42 = Constraint(expr= - 1000*m.b4 + m.x34 <= 0)

m.c43 = Constraint(expr= - 1000*m.b5 + m.x35 <= 0)

m.c44 = Constraint(expr= - 1000*m.b6 + m.x36 <= 0)

m.c45 = Constraint(expr= - 1000*m.b7 + m.x37 <= 0)

m.c46 = Constraint(expr= - 1000*m.b8 + m.x38 <= 0)

m.c47 = Constraint(expr= - 1000*m.b9 + m.x39 <= 0)

m.c48 = Constraint(expr= - 1000*m.b10 + m.x40 <= 0)

m.c49 = Constraint(expr= - 1000*m.b11 + m.x41 <= 0)

m.c50 = Constraint(expr= - 1000*m.b12 + m.x42 <= 0)

m.c51 = Constraint(expr= - 1000*m.b13 + m.x43 <= 0)

m.c52 = Constraint(expr= - 1000*m.b14 + m.x44 <= 0)

m.c53 = Constraint(expr= - 1000*m.b15 + m.x45 <= 0)

m.c54 = Constraint(expr= - 1000*m.b16 + m.x46 <= 0)

m.c55 = Constraint(expr= - 1000*m.b17 + m.x47 <= 0)

m.c56 = Constraint(expr= - 1000*m.b18 + m.x48 <= 0)

m.c57 = Constraint(expr= - 1000*m.b19 + m.x49 <= 0)

m.c58 = Constraint(expr= - 1000*m.b20 + m.x50 <= 0)

m.c59 = Constraint(expr= - 1000*m.b21 + m.x51 <= 0)

m.c60 = Constraint(expr= - 1000*m.b22 + m.x52 <= 0)

m.c61 = Constraint(expr= - 1000*m.b23 + m.x53 <= 0)

m.c62 = Constraint(expr= - 1000*m.b24 + m.x54 <= 0)

m.c63 = Constraint(expr= - 1000*m.b25 + m.x55 <= 0)

m.c64 = Constraint(expr= - 1000*m.b26 + m.x56 <= 0)

m.c65 = Constraint(expr= - 1000*m.b27 + m.x57 <= 0)

m.c66 = Constraint(expr= - 1000*m.b28 + m.x58 <= 0)

m.c67 = Constraint(expr= - 1000*m.b29 + m.x59 <= 0)

m.c68 = Constraint(expr= - 1000*m.b30 + m.x60 <= 0)

m.c69 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 + m.b5 + m.b6 + m.b7 + m.b8 + m.b9 + m.b10 >= 0)

m.c70 = Constraint(expr=   m.b11 + m.b12 + m.b13 + m.b14 + m.b15 + m.b16 + m.b17 + m.b18 + m.b19 + m.b20 >= 0)

m.c71 = Constraint(expr=   m.b21 + m.b22 + m.b23 + m.b24 + m.b25 + m.b26 + m.b27 + m.b28 + m.b29 + m.b30 >= 0)

m.c72 = Constraint(expr= - m.b1 - m.b2 - m.b3 - m.b4 - m.b5 - m.b6 - m.b7 - m.b8 - m.b9 - m.b10 - m.b11 - m.b12 - m.b13
                         - m.b14 - m.b15 - m.b16 - m.b17 - m.b18 - m.b19 - m.b20 - m.b21 - m.b22 - m.b23 - m.b24 - m.b25
                         - m.b26 - m.b27 - m.b28 - m.b29 - m.b30 + m.x70 == 0)
