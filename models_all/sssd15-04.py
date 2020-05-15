#  MINLP written by GAMS Convert at 05/15/20 00:51:22
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#         48       20        0       28        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         89       17       72        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        269      257       12        0
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
m.x73 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x74 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x75 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x76 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x77 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x78 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x79 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x80 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x81 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x82 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x83 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x84 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x85 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x86 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x87 = Var(within=Reals,bounds=(0,None),initialize=0)
m.x88 = Var(within=Reals,bounds=(0,None),initialize=0)

m.obj = Objective(expr=   53.1533839248115*m.b1 + 177.583181382496*m.b2 + 80.6428266602653*m.b3 + 231.95916447606*m.b4
                        + 394.432428138298*m.b5 + 444.974070084717*m.b6 + 459.794817811195*m.b7 + 695.629649483288*m.b8
                        + 323.203981426319*m.b9 + 107.360282998709*m.b10 + 361.859887112392*m.b11
                        + 367.306912008994*m.b12 + 282.872191198352*m.b13 + 44.0762253696262*m.b14
                        + 317.877544418109*m.b15 + 316.134390405973*m.b16 + 100.330419683223*m.b17
                        + 127.926900226391*m.b18 + 139.263247551061*m.b19 + 254.000222645919*m.b20
                        + 194.145316904472*m.b21 + 116.037290266393*m.b22 + 222.112787515659*m.b23
                        + 263.356262140469*m.b24 + 571.289311491824*m.b25 + 347.171110484916*m.b26
                        + 646.58041890394*m.b27 + 747.500077392939*m.b28 + 267.180266374013*m.b29
                        + 432.187536801291*m.b30 + 223.193932764969*m.b31 + 305.606281730255*m.b32
                        + 484.148164648118*m.b33 + 255.18826726263*m.b34 + 500.409280467716*m.b35
                        + 357.348895559311*m.b36 + 154.81861346409*m.b37 + 47.9482185242841*m.b38
                        + 178.01500365671*m.b39 + 197.299183634545*m.b40 + 110.221327583974*m.b41
                        + 276.335219124972*m.b42 + 66.6367550739739*m.b43 + 215.126920582161*m.b44
                        + 251.865680365869*m.b45 + 259.485555817488*m.b46 + 325.903992788768*m.b47
                        + 533.263861665761*m.b48 + 365.289467328013*m.b49 + 698.425848556873*m.b50
                        + 342.854784735801*m.b51 + 672.157315207286*m.b52 + 278.522996301316*m.b53
                        + 127.656852798454*m.b54 + 302.312726976851*m.b55 + 281.218053524739*m.b56
                        + 629.708028128623*m.b57 + 303.067014885745*m.b58 + 662.424721658793*m.b59
                        + 521.27200594153*m.b60 + 313.6973235*m.b61 + 136.4460104172*m.b62 + 95.4447793733688*m.b63
                        + 401.4402965*m.b64 + 160.307673981768*m.b65 + 107.445134115433*m.b66 + 456.70672375*m.b67
                        + 163.727629808624*m.b68 + 103.975094190251*m.b69 + 349.50038725*m.b70 + 137.744259121245*m.b71
                        + 91.7174793486262*m.b72 + 74750.0077392939*m.x73 + 74750.0077392939*m.x74
                        + 74750.0077392939*m.x75 + 74750.0077392939*m.x76, sense=minimize)

m.c2 = Constraint(expr=   0.609376132*m.b1 + 1.180016336*m.b5 + 0.967493052*m.b9 + 1.004918785*m.b13 + 0.698898063*m.b17
                        + 0.540292599*m.b21 + 1.460452986*m.b25 + 0.811980791*m.b29 + 0.973180988*m.b33
                        + 0.544914116*m.b37 + 0.78515855*m.b41 + 1.312281472*m.b45 + 1.346783152*m.b49
                        + 0.635811295*m.b53 + 1.327207817*m.b57 - 3.22664386875*m.x77 - 6.4532877375*m.x78
                        - 9.67993160625*m.x79 == 0)

m.c3 = Constraint(expr=   0.609376132*m.b2 + 1.180016336*m.b6 + 0.967493052*m.b10 + 1.004918785*m.b14
                        + 0.698898063*m.b18 + 0.540292599*m.b22 + 1.460452986*m.b26 + 0.811980791*m.b30
                        + 0.973180988*m.b34 + 0.544914116*m.b38 + 0.78515855*m.b42 + 1.312281472*m.b46
                        + 1.346783152*m.b50 + 0.635811295*m.b54 + 1.327207817*m.b58 - 3.1952881621875*m.x80
                        - 6.390576324375*m.x81 - 9.5858644865625*m.x82 == 0)

m.c4 = Constraint(expr=   0.609376132*m.b3 + 1.180016336*m.b7 + 0.967493052*m.b11 + 1.004918785*m.b15
                        + 0.698898063*m.b19 + 0.540292599*m.b23 + 1.460452986*m.b27 + 0.811980791*m.b31
                        + 0.973180988*m.b35 + 0.544914116*m.b39 + 0.78515855*m.b43 + 1.312281472*m.b47
                        + 1.346783152*m.b51 + 0.635811295*m.b55 + 1.327207817*m.b59 - 2.6301391753125*m.x83
                        - 5.260278350625*m.x84 - 7.8904175259375*m.x85 == 0)

m.c5 = Constraint(expr=   0.609376132*m.b4 + 1.180016336*m.b8 + 0.967493052*m.b12 + 1.004918785*m.b16
                        + 0.698898063*m.b20 + 0.540292599*m.b24 + 1.460452986*m.b28 + 0.811980791*m.b32
                        + 0.973180988*m.b36 + 0.544914116*m.b40 + 0.78515855*m.b44 + 1.312281472*m.b48
                        + 1.346783152*m.b52 + 0.635811295*m.b56 + 1.327207817*m.b60 - 2.6743241765625*m.x86
                        - 5.348648353125*m.x87 - 8.0229725296875*m.x88 == 0)

m.c6 = Constraint(expr=   m.b1 + m.b2 + m.b3 + m.b4 == 1)

m.c7 = Constraint(expr=   m.b5 + m.b6 + m.b7 + m.b8 == 1)

m.c8 = Constraint(expr=   m.b9 + m.b10 + m.b11 + m.b12 == 1)

m.c9 = Constraint(expr=   m.b13 + m.b14 + m.b15 + m.b16 == 1)

m.c10 = Constraint(expr=   m.b17 + m.b18 + m.b19 + m.b20 == 1)

m.c11 = Constraint(expr=   m.b21 + m.b22 + m.b23 + m.b24 == 1)

m.c12 = Constraint(expr=   m.b25 + m.b26 + m.b27 + m.b28 == 1)

m.c13 = Constraint(expr=   m.b29 + m.b30 + m.b31 + m.b32 == 1)

m.c14 = Constraint(expr=   m.b33 + m.b34 + m.b35 + m.b36 == 1)

m.c15 = Constraint(expr=   m.b37 + m.b38 + m.b39 + m.b40 == 1)

m.c16 = Constraint(expr=   m.b41 + m.b42 + m.b43 + m.b44 == 1)

m.c17 = Constraint(expr=   m.b45 + m.b46 + m.b47 + m.b48 == 1)

m.c18 = Constraint(expr=   m.b49 + m.b50 + m.b51 + m.b52 == 1)

m.c19 = Constraint(expr=   m.b53 + m.b54 + m.b55 + m.b56 == 1)

m.c20 = Constraint(expr=   m.b57 + m.b58 + m.b59 + m.b60 == 1)

m.c21 = Constraint(expr=   m.b61 + m.b62 + m.b63 <= 1)

m.c22 = Constraint(expr=   m.b64 + m.b65 + m.b66 <= 1)

m.c23 = Constraint(expr=   m.b67 + m.b68 + m.b69 <= 1)

m.c24 = Constraint(expr=   m.b70 + m.b71 + m.b72 <= 1)

m.c25 = Constraint(expr= - m.b61 + m.x77 <= 0)

m.c26 = Constraint(expr= - m.b62 + m.x78 <= 0)

m.c27 = Constraint(expr= - m.b63 + m.x79 <= 0)

m.c28 = Constraint(expr= - m.b64 + m.x80 <= 0)

m.c29 = Constraint(expr= - m.b65 + m.x81 <= 0)

m.c30 = Constraint(expr= - m.b66 + m.x82 <= 0)

m.c31 = Constraint(expr= - m.b67 + m.x83 <= 0)

m.c32 = Constraint(expr= - m.b68 + m.x84 <= 0)

m.c33 = Constraint(expr= - m.b69 + m.x85 <= 0)

m.c34 = Constraint(expr= - m.b70 + m.x86 <= 0)

m.c35 = Constraint(expr= - m.b71 + m.x87 <= 0)

m.c36 = Constraint(expr= - m.b72 + m.x88 <= 0)

m.c37 = Constraint(expr=-m.x73/(1 + m.x73) + m.x77 <= 0)

m.c38 = Constraint(expr=-m.x73/(1 + m.x73) + m.x78 <= 0)

m.c39 = Constraint(expr=-m.x73/(1 + m.x73) + m.x79 <= 0)

m.c40 = Constraint(expr=-m.x74/(1 + m.x74) + m.x80 <= 0)

m.c41 = Constraint(expr=-m.x74/(1 + m.x74) + m.x81 <= 0)

m.c42 = Constraint(expr=-m.x74/(1 + m.x74) + m.x82 <= 0)

m.c43 = Constraint(expr=-m.x75/(1 + m.x75) + m.x83 <= 0)

m.c44 = Constraint(expr=-m.x75/(1 + m.x75) + m.x84 <= 0)

m.c45 = Constraint(expr=-m.x75/(1 + m.x75) + m.x85 <= 0)

m.c46 = Constraint(expr=-m.x76/(1 + m.x76) + m.x86 <= 0)

m.c47 = Constraint(expr=-m.x76/(1 + m.x76) + m.x87 <= 0)

m.c48 = Constraint(expr=-m.x76/(1 + m.x76) + m.x88 <= 0)
