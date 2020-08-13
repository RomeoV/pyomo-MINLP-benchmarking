#  MINLP written by GAMS Convert at 08/13/20 17:38:08
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         92       71       21        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         92        1       91        0


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
m.x22 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x23 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x24 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x25 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x26 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x27 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x28 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x29 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x30 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x31 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x32 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x33 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x34 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x35 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x36 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x37 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x38 = Var(within=Reals,bounds=(None,None),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x44 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x45 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x46 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x47 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x48 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x49 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x50 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x51 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x52 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x53 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x54 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x55 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x56 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x57 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x58 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x59 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x60 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x61 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x62 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x63 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x64 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x65 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x66 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x67 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x68 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x69 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x70 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x71 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x72 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x73 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x89 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x90 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x91 = Var(within=Reals,bounds=(0,1),initialize=0)
m.x92 = Var(within=Reals,bounds=(0,1),initialize=0)

m.obj = Objective(expr=m.x38, sense=maximize)

m.c1 = Constraint(expr=2*m.x43*m.x30 - 4*m.x30 - 2*m.x43 - 2*m.x43*m.x59 + 2*m.x59 + 2*m.x43*m.x69 + 2*m.x43*m.x70 + 2*
                       m.x46*m.x47 - 2*m.x46 - 4*m.x47 + 2*m.x46*m.x63 - 2*m.x63 + 2*m.x46*m.x84 - 2*m.x84 - 2*m.x46*
                       m.b14 + 2*m.x47*m.x64 - 2*m.x64 + 2*m.x47*m.x88 - 2*m.x88 + 2*m.x47*m.x74 + 2*m.x52*m.x54 + 2*
                       m.x52 - 4*m.x54 - 2*m.x52*m.x84 - 2*m.x52*m.x76 - 2*m.x52*m.b15 + 2*m.x54*m.x88 + 2*m.x54*m.x25
                        - 4*m.x25 + 2*m.x54*m.x78 + 2*m.x58*m.x60 - 2*m.x58 - 2*m.x60 + 2*m.x58*m.b12 - 4*m.b12 + 2*
                       m.x60*m.x62 - 2*m.x62 + 2*m.x60*m.x73 - 4*m.x73 - 2*m.x60*m.x83 + 2*m.x62*m.x77 - 4*m.x77 + 2*
                       m.x63*m.x37 - 2*m.x37 + 2*m.x64*m.x66 - 2*m.x66 + 2*m.x64*m.x84 - 2*m.x64*m.x82 + 2*m.x66*m.x67
                        - 2*m.x67 - 2*m.x66*m.x26 - 2*m.x26 + 2*m.x66*m.x56 - 4*m.x56 + 2*m.x67*m.x90 - 4*m.x90 + 2*
                       m.x67*m.x57 + 2*m.x57 - 2*m.x67*m.x71 + 2*m.x73*m.x23 - 4*m.x23 + 2*m.x73*m.x32 - 4*m.x32 + 2*
                       m.x73*m.x85 + 2*m.x77*m.x81 - 2*m.x81 + 2*m.x77*m.x22 - 4*m.x22 + 2*m.x77*m.x83 + 2*m.x81*m.x23
                        + 2*m.x84*m.x89 - 2*m.x89 + 2*m.x88*m.x90 - 2*m.x88*m.x79 + 2*m.x89*m.x90 + 2*m.x89*m.x39 - 4*
                       m.x39 - 2*m.x89*m.x87 + 2*m.x90*m.x91 - 4*m.x91 + 2*m.x91*m.x42 + 2*m.x42 + 2*m.x91*m.x55 - 2*
                       m.x55 + 2*m.x91*m.x71 + 2*m.x92*m.x22 - 4*m.x92 + 2*m.x92*m.b3 - 2*m.b3 + 2*m.x92*m.x83 + 2*m.x92
                       *m.x86 + 2*m.x22*m.x34 - 4*m.x34 + 2*m.x22*m.b4 - 2*m.b4 + 2*m.x23*m.x24 - 2*m.x24 + 2*m.x23*
                       m.x33 - 4*m.x33 + 2*m.x24*m.x34 + 2*m.x25*m.x39 + 2*m.x25*m.x53 - 2*m.x53 + 2*m.x25*m.x55 + 2*
                       m.x26*m.b1 - 2*m.b1 + 2*m.x26*m.x55 + 2*m.x26*m.x87 + 2*m.x27*m.x39 - 2*m.x27 - 2*m.x27*m.x42 + 2
                       *m.x27*m.x75 + 2*m.x27*m.x79 + 2*m.x28*m.x29 - 4*m.x28 - 2*m.x29 + 2*m.x28*m.x30 + 2*m.x28*m.x41
                        - 2*m.x41 + 2*m.x28*m.x56 - 2*m.x29*m.x31 - 2*m.x31 + 2*m.x29*m.x45 - 2*m.x45 + 2*m.x29*m.x71 + 
                       2*m.x30*m.x31 + 2*m.x30*m.x75 + 2*m.x31*m.x32 + 2*m.x31*m.x85 + 2*m.x32*m.x33 + 2*m.x32*m.b9 - 2*
                       m.b9 + 2*m.x33*m.x49 - 4*m.x49 + 2*m.x33*m.b10 - 2*m.b10 + 2*m.x34*m.x35 - 2*m.x35 + 2*m.x34*
                       m.x48 - 2*m.x48 + 2*m.x35*m.x49 - 2*m.x36*m.x74 + 2*m.x36 - 2*m.x36*m.b19 - 2*m.x37*m.b1 + 2*
                       m.x37*m.x53 + 2*m.x37*m.x76 + 2*m.b1*m.b17 + 2*m.b1*m.b19 + 2*m.x39*m.x41 + 2*m.x40*m.b2 - 4*m.b2
                        - 2*m.x40 - 2*m.x40*m.x57 + 2*m.x40*m.x79 + 2*m.x40*m.x82 + 2*m.x41*m.b2 - 2*m.x41*m.b21 - 2*
                       m.x42*m.x59 - 2*m.x42*m.b18 + 2*m.b2*m.x72 + 2*m.b2*m.b18 - 2*m.x44*m.b3 + 2*m.x44 - 2*m.x44*
                       m.x57 + 2*m.x44*m.x61 + 2*m.x61 - 2*m.x44*m.x71 - 2*m.x45*m.b4 + 2*m.x45*m.x70 + 2*m.x45*m.x72 + 
                       2*m.b3*m.b4 + 2*m.b3*m.b18 + 2*m.b4*m.x48 + 2*m.x48*m.x65 - 2*m.x65 - 2*m.x48*m.x70 + 2*m.x49*
                       m.x50 - 2*m.x50 + 2*m.x49*m.b11 - 2*m.b11 + 2*m.x50*m.x65 - 2*m.x51*m.b5 - 2*m.b5 + 2*m.x51 - 2*
                       m.x51*m.x78 + 2*m.b5*m.b6 - 2*m.b6 + 2*m.b5*m.b14 + 2*m.b5*m.x87 + 2*m.x53*m.x74 - 2*m.x53*m.b16
                        - 2*m.b6*m.x78 + 2*m.b6*m.b16 + 2*m.b6*m.b17 - 2*m.x55*m.b20 + 2*m.x56*m.b7 - 4*m.b7 + 2*m.x56*
                       m.x82 - 2*m.x57*m.b8 - 2*m.b8 + 2*m.b7*m.x59 + 2*m.b7*m.b8 + 2*m.b7*m.b20 - 2*m.x59*m.b9 + 2*m.b8
                       *m.b9 + 2*m.b8*m.x86 - 2*m.x61*m.b10 - 2*m.x61*m.x69 - 2*m.x61*m.x72 + 2*m.b9*m.b10 + 2*m.b10*
                       m.b11 + 2*m.b11*m.b12 - 2*m.b11*m.x69 + 2*m.x65*m.b13 - 2*m.b13 - 2*m.x65*m.x68 + 2*m.b12*m.b13
                        + 2*m.b12*m.x68 + 2*m.x68*m.x69 - 2*m.x68*m.x70 - 2*m.x72*m.x75 - 2*m.x74*m.x80 - 2*m.x75*m.b20
                        + 2*m.b15*m.b19 + 2*m.x78*m.x80 - 2*m.x79*m.b16 + 2*m.b16*m.b21 - 2*m.x82*m.b17 - 2*m.x83*m.x85
                        - 2*m.b17*m.b21 - 2*m.x85*m.x86 - 2*m.x86*m.b18 - 2*m.x87*m.b19 + 2*m.b20*m.b21 + m.x38 <= 0)
