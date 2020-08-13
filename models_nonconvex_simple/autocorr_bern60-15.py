#  MINLP written by GAMS Convert at 08/13/20 17:37:55
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         61        1       60        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61        1       60        0


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
m.x61 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x61, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b2*m.b6*m.b7
                        + 64*m.b1*m.b2*m.b7*m.b8 + 64*m.b1*m.b2*m.b8*m.b9 + 64*m.b1*m.b2*m.b9*m.b10 + 64*m.b1*m.b2*m.b10
                       *m.b11 + 64*m.b1*m.b2*m.b11*m.b12 + 64*m.b1*m.b2*m.b12*m.b13 + 64*m.b1*m.b2*m.b13*m.b14 + 64*m.b1
                       *m.b2*m.b14*m.b15 + 64*m.b1*m.b3*m.b4*m.b6 + 64*m.b1*m.b3*m.b5*m.b7 + 64*m.b1*m.b3*m.b6*m.b8 + 64
                       *m.b1*m.b3*m.b7*m.b9 + 64*m.b1*m.b3*m.b8*m.b10 + 64*m.b1*m.b3*m.b9*m.b11 + 64*m.b1*m.b3*m.b10*
                       m.b12 + 64*m.b1*m.b3*m.b11*m.b13 + 64*m.b1*m.b3*m.b12*m.b14 + 64*m.b1*m.b3*m.b13*m.b15 + 64*m.b1*
                       m.b4*m.b5*m.b8 + 64*m.b1*m.b4*m.b6*m.b9 + 64*m.b1*m.b4*m.b7*m.b10 + 64*m.b1*m.b4*m.b8*m.b11 + 64*
                       m.b1*m.b4*m.b9*m.b12 + 64*m.b1*m.b4*m.b10*m.b13 + 64*m.b1*m.b4*m.b11*m.b14 + 64*m.b1*m.b4*m.b12*
                       m.b15 + 64*m.b1*m.b5*m.b6*m.b10 + 64*m.b1*m.b5*m.b7*m.b11 + 64*m.b1*m.b5*m.b8*m.b12 + 64*m.b1*
                       m.b5*m.b9*m.b13 + 64*m.b1*m.b5*m.b10*m.b14 + 64*m.b1*m.b5*m.b11*m.b15 + 64*m.b1*m.b6*m.b7*m.b12
                        + 64*m.b1*m.b6*m.b8*m.b13 + 64*m.b1*m.b6*m.b9*m.b14 + 64*m.b1*m.b6*m.b10*m.b15 + 64*m.b1*m.b7*
                       m.b8*m.b14 + 64*m.b1*m.b7*m.b9*m.b15 + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 128*
                       m.b2*m.b3*m.b6*m.b7 + 128*m.b2*m.b3*m.b7*m.b8 + 128*m.b2*m.b3*m.b8*m.b9 + 128*m.b2*m.b3*m.b9*
                       m.b10 + 128*m.b2*m.b3*m.b10*m.b11 + 128*m.b2*m.b3*m.b11*m.b12 + 128*m.b2*m.b3*m.b12*m.b13 + 128*
                       m.b2*m.b3*m.b13*m.b14 + 128*m.b2*m.b3*m.b14*m.b15 + 64*m.b2*m.b3*m.b15*m.b16 + 128*m.b2*m.b4*m.b5
                       *m.b7 + 128*m.b2*m.b4*m.b6*m.b8 + 128*m.b2*m.b4*m.b7*m.b9 + 128*m.b2*m.b4*m.b8*m.b10 + 128*m.b2*
                       m.b4*m.b9*m.b11 + 128*m.b2*m.b4*m.b10*m.b12 + 128*m.b2*m.b4*m.b11*m.b13 + 128*m.b2*m.b4*m.b12*
                       m.b14 + 128*m.b2*m.b4*m.b13*m.b15 + 64*m.b2*m.b4*m.b14*m.b16 + 128*m.b2*m.b5*m.b6*m.b9 + 128*m.b2
                       *m.b5*m.b7*m.b10 + 128*m.b2*m.b5*m.b8*m.b11 + 128*m.b2*m.b5*m.b9*m.b12 + 128*m.b2*m.b5*m.b10*
                       m.b13 + 128*m.b2*m.b5*m.b11*m.b14 + 128*m.b2*m.b5*m.b12*m.b15 + 64*m.b2*m.b5*m.b13*m.b16 + 128*
                       m.b2*m.b6*m.b7*m.b11 + 128*m.b2*m.b6*m.b8*m.b12 + 128*m.b2*m.b6*m.b9*m.b13 + 128*m.b2*m.b6*m.b10*
                       m.b14 + 128*m.b2*m.b6*m.b11*m.b15 + 64*m.b2*m.b6*m.b12*m.b16 + 128*m.b2*m.b7*m.b8*m.b13 + 128*
                       m.b2*m.b7*m.b9*m.b14 + 128*m.b2*m.b7*m.b10*m.b15 + 64*m.b2*m.b7*m.b11*m.b16 + 128*m.b2*m.b8*m.b9*
                       m.b15 + 64*m.b2*m.b8*m.b10*m.b16 + 192*m.b3*m.b4*m.b5*m.b6 + 192*m.b3*m.b4*m.b6*m.b7 + 192*m.b3*
                       m.b4*m.b7*m.b8 + 192*m.b3*m.b4*m.b8*m.b9 + 192*m.b3*m.b4*m.b9*m.b10 + 192*m.b3*m.b4*m.b10*m.b11
                        + 192*m.b3*m.b4*m.b11*m.b12 + 192*m.b3*m.b4*m.b12*m.b13 + 192*m.b3*m.b4*m.b13*m.b14 + 192*m.b3*
                       m.b4*m.b14*m.b15 + 128*m.b3*m.b4*m.b15*m.b16 + 64*m.b3*m.b4*m.b16*m.b17 + 192*m.b3*m.b5*m.b6*m.b8
                        + 192*m.b3*m.b5*m.b7*m.b9 + 192*m.b3*m.b5*m.b8*m.b10 + 192*m.b3*m.b5*m.b9*m.b11 + 192*m.b3*m.b5*
                       m.b10*m.b12 + 192*m.b3*m.b5*m.b11*m.b13 + 192*m.b3*m.b5*m.b12*m.b14 + 192*m.b3*m.b5*m.b13*m.b15
                        + 128*m.b3*m.b5*m.b14*m.b16 + 64*m.b3*m.b5*m.b15*m.b17 + 192*m.b3*m.b6*m.b7*m.b10 + 192*m.b3*
                       m.b6*m.b8*m.b11 + 192*m.b3*m.b6*m.b9*m.b12 + 192*m.b3*m.b6*m.b10*m.b13 + 192*m.b3*m.b6*m.b11*
                       m.b14 + 192*m.b3*m.b6*m.b12*m.b15 + 128*m.b3*m.b6*m.b13*m.b16 + 64*m.b3*m.b6*m.b14*m.b17 + 192*
                       m.b3*m.b7*m.b8*m.b12 + 192*m.b3*m.b7*m.b9*m.b13 + 192*m.b3*m.b7*m.b10*m.b14 + 192*m.b3*m.b7*m.b11
                       *m.b15 + 128*m.b3*m.b7*m.b12*m.b16 + 64*m.b3*m.b7*m.b13*m.b17 + 192*m.b3*m.b8*m.b9*m.b14 + 192*
                       m.b3*m.b8*m.b10*m.b15 + 128*m.b3*m.b8*m.b11*m.b16 + 64*m.b3*m.b8*m.b12*m.b17 + 128*m.b3*m.b9*
                       m.b10*m.b16 + 64*m.b3*m.b9*m.b11*m.b17 + 256*m.b4*m.b5*m.b6*m.b7 + 256*m.b4*m.b5*m.b7*m.b8 + 256*
                       m.b4*m.b5*m.b8*m.b9 + 256*m.b4*m.b5*m.b9*m.b10 + 256*m.b4*m.b5*m.b10*m.b11 + 256*m.b4*m.b5*m.b11*
                       m.b12 + 256*m.b4*m.b5*m.b12*m.b13 + 256*m.b4*m.b5*m.b13*m.b14 + 256*m.b4*m.b5*m.b14*m.b15 + 192*
                       m.b4*m.b5*m.b15*m.b16 + 128*m.b4*m.b5*m.b16*m.b17 + 64*m.b4*m.b5*m.b17*m.b18 + 256*m.b4*m.b6*m.b7
                       *m.b9 + 256*m.b4*m.b6*m.b8*m.b10 + 256*m.b4*m.b6*m.b9*m.b11 + 256*m.b4*m.b6*m.b10*m.b12 + 256*
                       m.b4*m.b6*m.b11*m.b13 + 256*m.b4*m.b6*m.b12*m.b14 + 256*m.b4*m.b6*m.b13*m.b15 + 192*m.b4*m.b6*
                       m.b14*m.b16 + 128*m.b4*m.b6*m.b15*m.b17 + 64*m.b4*m.b6*m.b16*m.b18 + 256*m.b4*m.b7*m.b8*m.b11 + 
                       256*m.b4*m.b7*m.b9*m.b12 + 256*m.b4*m.b7*m.b10*m.b13 + 256*m.b4*m.b7*m.b11*m.b14 + 256*m.b4*m.b7*
                       m.b12*m.b15 + 192*m.b4*m.b7*m.b13*m.b16 + 128*m.b4*m.b7*m.b14*m.b17 + 64*m.b4*m.b7*m.b15*m.b18 + 
                       256*m.b4*m.b8*m.b9*m.b13 + 256*m.b4*m.b8*m.b10*m.b14 + 256*m.b4*m.b8*m.b11*m.b15 + 192*m.b4*m.b8*
                       m.b12*m.b16 + 128*m.b4*m.b8*m.b13*m.b17 + 64*m.b4*m.b8*m.b14*m.b18 + 256*m.b4*m.b9*m.b10*m.b15 + 
                       192*m.b4*m.b9*m.b11*m.b16 + 128*m.b4*m.b9*m.b12*m.b17 + 64*m.b4*m.b9*m.b13*m.b18 + 128*m.b4*m.b10
                       *m.b11*m.b17 + 64*m.b4*m.b10*m.b12*m.b18 + 320*m.b5*m.b6*m.b7*m.b8 + 320*m.b5*m.b6*m.b8*m.b9 + 
                       320*m.b5*m.b6*m.b9*m.b10 + 320*m.b5*m.b6*m.b10*m.b11 + 320*m.b5*m.b6*m.b11*m.b12 + 320*m.b5*m.b6*
                       m.b12*m.b13 + 320*m.b5*m.b6*m.b13*m.b14 + 320*m.b5*m.b6*m.b14*m.b15 + 256*m.b5*m.b6*m.b15*m.b16
                        + 192*m.b5*m.b6*m.b16*m.b17 + 128*m.b5*m.b6*m.b17*m.b18 + 64*m.b5*m.b6*m.b18*m.b19 + 320*m.b5*
                       m.b7*m.b8*m.b10 + 320*m.b5*m.b7*m.b9*m.b11 + 320*m.b5*m.b7*m.b10*m.b12 + 320*m.b5*m.b7*m.b11*
                       m.b13 + 320*m.b5*m.b7*m.b12*m.b14 + 320*m.b5*m.b7*m.b13*m.b15 + 256*m.b5*m.b7*m.b14*m.b16 + 192*
                       m.b5*m.b7*m.b15*m.b17 + 128*m.b5*m.b7*m.b16*m.b18 + 64*m.b5*m.b7*m.b17*m.b19 + 320*m.b5*m.b8*m.b9
                       *m.b12 + 320*m.b5*m.b8*m.b10*m.b13 + 320*m.b5*m.b8*m.b11*m.b14 + 320*m.b5*m.b8*m.b12*m.b15 + 256*
                       m.b5*m.b8*m.b13*m.b16 + 192*m.b5*m.b8*m.b14*m.b17 + 128*m.b5*m.b8*m.b15*m.b18 + 64*m.b5*m.b8*
                       m.b16*m.b19 + 320*m.b5*m.b9*m.b10*m.b14 + 320*m.b5*m.b9*m.b11*m.b15 + 256*m.b5*m.b9*m.b12*m.b16
                        + 192*m.b5*m.b9*m.b13*m.b17 + 128*m.b5*m.b9*m.b14*m.b18 + 64*m.b5*m.b9*m.b15*m.b19 + 256*m.b5*
                       m.b10*m.b11*m.b16 + 192*m.b5*m.b10*m.b12*m.b17 + 128*m.b5*m.b10*m.b13*m.b18 + 64*m.b5*m.b10*m.b14
                       *m.b19 + 128*m.b5*m.b11*m.b12*m.b18 + 64*m.b5*m.b11*m.b13*m.b19 + 384*m.b6*m.b7*m.b8*m.b9 + 384*
                       m.b6*m.b7*m.b9*m.b10 + 384*m.b6*m.b7*m.b10*m.b11 + 384*m.b6*m.b7*m.b11*m.b12 + 384*m.b6*m.b7*
                       m.b12*m.b13 + 384*m.b6*m.b7*m.b13*m.b14 + 384*m.b6*m.b7*m.b14*m.b15 + 320*m.b6*m.b7*m.b15*m.b16
                        + 256*m.b6*m.b7*m.b16*m.b17 + 192*m.b6*m.b7*m.b17*m.b18 + 128*m.b6*m.b7*m.b18*m.b19 + 64*m.b6*
                       m.b7*m.b19*m.b20 + 384*m.b6*m.b8*m.b9*m.b11 + 384*m.b6*m.b8*m.b10*m.b12 + 384*m.b6*m.b8*m.b11*
                       m.b13 + 384*m.b6*m.b8*m.b12*m.b14 + 384*m.b6*m.b8*m.b13*m.b15 + 320*m.b6*m.b8*m.b14*m.b16 + 256*
                       m.b6*m.b8*m.b15*m.b17 + 192*m.b6*m.b8*m.b16*m.b18 + 128*m.b6*m.b8*m.b17*m.b19 + 64*m.b6*m.b8*
                       m.b18*m.b20 + 384*m.b6*m.b9*m.b10*m.b13 + 384*m.b6*m.b9*m.b11*m.b14 + 384*m.b6*m.b9*m.b12*m.b15
                        + 320*m.b6*m.b9*m.b13*m.b16 + 256*m.b6*m.b9*m.b14*m.b17 + 192*m.b6*m.b9*m.b15*m.b18 + 128*m.b6*
                       m.b9*m.b16*m.b19 + 64*m.b6*m.b9*m.b17*m.b20 + 384*m.b6*m.b10*m.b11*m.b15 + 320*m.b6*m.b10*m.b12*
                       m.b16 + 256*m.b6*m.b10*m.b13*m.b17 + 192*m.b6*m.b10*m.b14*m.b18 + 128*m.b6*m.b10*m.b15*m.b19 + 64
                       *m.b6*m.b10*m.b16*m.b20 + 256*m.b6*m.b11*m.b12*m.b17 + 192*m.b6*m.b11*m.b13*m.b18 + 128*m.b6*
                       m.b11*m.b14*m.b19 + 64*m.b6*m.b11*m.b15*m.b20 + 128*m.b6*m.b12*m.b13*m.b19 + 64*m.b6*m.b12*m.b14*
                       m.b20 + 448*m.b7*m.b8*m.b9*m.b10 + 448*m.b7*m.b8*m.b10*m.b11 + 448*m.b7*m.b8*m.b11*m.b12 + 448*
                       m.b7*m.b8*m.b12*m.b13 + 448*m.b7*m.b8*m.b13*m.b14 + 448*m.b7*m.b8*m.b14*m.b15 + 384*m.b7*m.b8*
                       m.b15*m.b16 + 320*m.b7*m.b8*m.b16*m.b17 + 256*m.b7*m.b8*m.b17*m.b18 + 192*m.b7*m.b8*m.b18*m.b19
                        + 128*m.b7*m.b8*m.b19*m.b20 + 64*m.b7*m.b8*m.b20*m.b21 + 448*m.b7*m.b9*m.b10*m.b12 + 448*m.b7*
                       m.b9*m.b11*m.b13 + 448*m.b7*m.b9*m.b12*m.b14 + 448*m.b7*m.b9*m.b13*m.b15 + 384*m.b7*m.b9*m.b14*
                       m.b16 + 320*m.b7*m.b9*m.b15*m.b17 + 256*m.b7*m.b9*m.b16*m.b18 + 192*m.b7*m.b9*m.b17*m.b19 + 128*
                       m.b7*m.b9*m.b18*m.b20 + 64*m.b7*m.b9*m.b19*m.b21 + 448*m.b7*m.b10*m.b11*m.b14 + 448*m.b7*m.b10*
                       m.b12*m.b15 + 384*m.b7*m.b10*m.b13*m.b16 + 320*m.b7*m.b10*m.b14*m.b17 + 256*m.b7*m.b10*m.b15*
                       m.b18 + 192*m.b7*m.b10*m.b16*m.b19 + 128*m.b7*m.b10*m.b17*m.b20 + 64*m.b7*m.b10*m.b18*m.b21 + 384
                       *m.b7*m.b11*m.b12*m.b16 + 320*m.b7*m.b11*m.b13*m.b17 + 256*m.b7*m.b11*m.b14*m.b18 + 192*m.b7*
                       m.b11*m.b15*m.b19 + 128*m.b7*m.b11*m.b16*m.b20 + 64*m.b7*m.b11*m.b17*m.b21 + 256*m.b7*m.b12*m.b13
                       *m.b18 + 192*m.b7*m.b12*m.b14*m.b19 + 128*m.b7*m.b12*m.b15*m.b20 + 64*m.b7*m.b12*m.b16*m.b21 + 
                       128*m.b7*m.b13*m.b14*m.b20 + 64*m.b7*m.b13*m.b15*m.b21 + 512*m.b8*m.b9*m.b10*m.b11 + 512*m.b8*
                       m.b9*m.b11*m.b12 + 512*m.b8*m.b9*m.b12*m.b13 + 512*m.b8*m.b9*m.b13*m.b14 + 512*m.b8*m.b9*m.b14*
                       m.b15 + 448*m.b8*m.b9*m.b15*m.b16 + 384*m.b8*m.b9*m.b16*m.b17 + 320*m.b8*m.b9*m.b17*m.b18 + 256*
                       m.b8*m.b9*m.b18*m.b19 + 192*m.b8*m.b9*m.b19*m.b20 + 128*m.b8*m.b9*m.b20*m.b21 + 64*m.b8*m.b9*
                       m.b21*m.b22 + 512*m.b8*m.b10*m.b11*m.b13 + 512*m.b8*m.b10*m.b12*m.b14 + 512*m.b8*m.b10*m.b13*
                       m.b15 + 448*m.b8*m.b10*m.b14*m.b16 + 384*m.b8*m.b10*m.b15*m.b17 + 320*m.b8*m.b10*m.b16*m.b18 + 
                       256*m.b8*m.b10*m.b17*m.b19 + 192*m.b8*m.b10*m.b18*m.b20 + 128*m.b8*m.b10*m.b19*m.b21 + 64*m.b8*
                       m.b10*m.b20*m.b22 + 512*m.b8*m.b11*m.b12*m.b15 + 448*m.b8*m.b11*m.b13*m.b16 + 384*m.b8*m.b11*
                       m.b14*m.b17 + 320*m.b8*m.b11*m.b15*m.b18 + 256*m.b8*m.b11*m.b16*m.b19 + 192*m.b8*m.b11*m.b17*
                       m.b20 + 128*m.b8*m.b11*m.b18*m.b21 + 64*m.b8*m.b11*m.b19*m.b22 + 384*m.b8*m.b12*m.b13*m.b17 + 320
                       *m.b8*m.b12*m.b14*m.b18 + 256*m.b8*m.b12*m.b15*m.b19 + 192*m.b8*m.b12*m.b16*m.b20 + 128*m.b8*
                       m.b12*m.b17*m.b21 + 64*m.b8*m.b12*m.b18*m.b22 + 256*m.b8*m.b13*m.b14*m.b19 + 192*m.b8*m.b13*m.b15
                       *m.b20 + 128*m.b8*m.b13*m.b16*m.b21 + 64*m.b8*m.b13*m.b17*m.b22 + 128*m.b8*m.b14*m.b15*m.b21 + 64
                       *m.b8*m.b14*m.b16*m.b22 + 576*m.b9*m.b10*m.b11*m.b12 + 576*m.b9*m.b10*m.b12*m.b13 + 576*m.b9*
                       m.b10*m.b13*m.b14 + 576*m.b9*m.b10*m.b14*m.b15 + 512*m.b9*m.b10*m.b15*m.b16 + 448*m.b9*m.b10*
                       m.b16*m.b17 + 384*m.b9*m.b10*m.b17*m.b18 + 320*m.b9*m.b10*m.b18*m.b19 + 256*m.b9*m.b10*m.b19*
                       m.b20 + 192*m.b9*m.b10*m.b20*m.b21 + 128*m.b9*m.b10*m.b21*m.b22 + 64*m.b9*m.b10*m.b22*m.b23 + 576
                       *m.b9*m.b11*m.b12*m.b14 + 576*m.b9*m.b11*m.b13*m.b15 + 512*m.b9*m.b11*m.b14*m.b16 + 448*m.b9*
                       m.b11*m.b15*m.b17 + 384*m.b9*m.b11*m.b16*m.b18 + 320*m.b9*m.b11*m.b17*m.b19 + 256*m.b9*m.b11*
                       m.b18*m.b20 + 192*m.b9*m.b11*m.b19*m.b21 + 128*m.b9*m.b11*m.b20*m.b22 + 64*m.b9*m.b11*m.b21*m.b23
                        + 512*m.b9*m.b12*m.b13*m.b16 + 448*m.b9*m.b12*m.b14*m.b17 + 384*m.b9*m.b12*m.b15*m.b18 + 320*
                       m.b9*m.b12*m.b16*m.b19 + 256*m.b9*m.b12*m.b17*m.b20 + 192*m.b9*m.b12*m.b18*m.b21 + 128*m.b9*m.b12
                       *m.b19*m.b22 + 64*m.b9*m.b12*m.b20*m.b23 + 384*m.b9*m.b13*m.b14*m.b18 + 320*m.b9*m.b13*m.b15*
                       m.b19 + 256*m.b9*m.b13*m.b16*m.b20 + 192*m.b9*m.b13*m.b17*m.b21 + 128*m.b9*m.b13*m.b18*m.b22 + 64
                       *m.b9*m.b13*m.b19*m.b23 + 256*m.b9*m.b14*m.b15*m.b20 + 192*m.b9*m.b14*m.b16*m.b21 + 128*m.b9*
                       m.b14*m.b17*m.b22 + 64*m.b9*m.b14*m.b18*m.b23 + 128*m.b9*m.b15*m.b16*m.b22 + 64*m.b9*m.b15*m.b17*
                       m.b23 + 640*m.b10*m.b11*m.b12*m.b13 + 640*m.b10*m.b11*m.b13*m.b14 + 640*m.b10*m.b11*m.b14*m.b15
                        + 576*m.b10*m.b11*m.b15*m.b16 + 512*m.b10*m.b11*m.b16*m.b17 + 448*m.b10*m.b11*m.b17*m.b18 + 384*
                       m.b10*m.b11*m.b18*m.b19 + 320*m.b10*m.b11*m.b19*m.b20 + 256*m.b10*m.b11*m.b20*m.b21 + 192*m.b10*
                       m.b11*m.b21*m.b22 + 128*m.b10*m.b11*m.b22*m.b23 + 64*m.b10*m.b11*m.b23*m.b24 + 640*m.b10*m.b12*
                       m.b13*m.b15 + 576*m.b10*m.b12*m.b14*m.b16 + 512*m.b10*m.b12*m.b15*m.b17 + 448*m.b10*m.b12*m.b16*
                       m.b18 + 384*m.b10*m.b12*m.b17*m.b19 + 320*m.b10*m.b12*m.b18*m.b20 + 256*m.b10*m.b12*m.b19*m.b21
                        + 192*m.b10*m.b12*m.b20*m.b22 + 128*m.b10*m.b12*m.b21*m.b23 + 64*m.b10*m.b12*m.b22*m.b24 + 512*
                       m.b10*m.b13*m.b14*m.b17 + 448*m.b10*m.b13*m.b15*m.b18 + 384*m.b10*m.b13*m.b16*m.b19 + 320*m.b10*
                       m.b13*m.b17*m.b20 + 256*m.b10*m.b13*m.b18*m.b21 + 192*m.b10*m.b13*m.b19*m.b22 + 128*m.b10*m.b13*
                       m.b20*m.b23 + 64*m.b10*m.b13*m.b21*m.b24 + 384*m.b10*m.b14*m.b15*m.b19 + 320*m.b10*m.b14*m.b16*
                       m.b20 + 256*m.b10*m.b14*m.b17*m.b21 + 192*m.b10*m.b14*m.b18*m.b22 + 128*m.b10*m.b14*m.b19*m.b23
                        + 64*m.b10*m.b14*m.b20*m.b24 + 256*m.b10*m.b15*m.b16*m.b21 + 192*m.b10*m.b15*m.b17*m.b22 + 128*
                       m.b10*m.b15*m.b18*m.b23 + 64*m.b10*m.b15*m.b19*m.b24 + 128*m.b10*m.b16*m.b17*m.b23 + 64*m.b10*
                       m.b16*m.b18*m.b24 + 704*m.b11*m.b12*m.b13*m.b14 + 704*m.b11*m.b12*m.b14*m.b15 + 640*m.b11*m.b12*
                       m.b15*m.b16 + 576*m.b11*m.b12*m.b16*m.b17 + 512*m.b11*m.b12*m.b17*m.b18 + 448*m.b11*m.b12*m.b18*
                       m.b19 + 384*m.b11*m.b12*m.b19*m.b20 + 320*m.b11*m.b12*m.b20*m.b21 + 256*m.b11*m.b12*m.b21*m.b22
                        + 192*m.b11*m.b12*m.b22*m.b23 + 128*m.b11*m.b12*m.b23*m.b24 + 64*m.b11*m.b12*m.b24*m.b25 + 640*
                       m.b11*m.b13*m.b14*m.b16 + 576*m.b11*m.b13*m.b15*m.b17 + 512*m.b11*m.b13*m.b16*m.b18 + 448*m.b11*
                       m.b13*m.b17*m.b19 + 384*m.b11*m.b13*m.b18*m.b20 + 320*m.b11*m.b13*m.b19*m.b21 + 256*m.b11*m.b13*
                       m.b20*m.b22 + 192*m.b11*m.b13*m.b21*m.b23 + 128*m.b11*m.b13*m.b22*m.b24 + 64*m.b11*m.b13*m.b23*
                       m.b25 + 512*m.b11*m.b14*m.b15*m.b18 + 448*m.b11*m.b14*m.b16*m.b19 + 384*m.b11*m.b14*m.b17*m.b20
                        + 320*m.b11*m.b14*m.b18*m.b21 + 256*m.b11*m.b14*m.b19*m.b22 + 192*m.b11*m.b14*m.b20*m.b23 + 128*
                       m.b11*m.b14*m.b21*m.b24 + 64*m.b11*m.b14*m.b22*m.b25 + 384*m.b11*m.b15*m.b16*m.b20 + 320*m.b11*
                       m.b15*m.b17*m.b21 + 256*m.b11*m.b15*m.b18*m.b22 + 192*m.b11*m.b15*m.b19*m.b23 + 128*m.b11*m.b15*
                       m.b20*m.b24 + 64*m.b11*m.b15*m.b21*m.b25 + 256*m.b11*m.b16*m.b17*m.b22 + 192*m.b11*m.b16*m.b18*
                       m.b23 + 128*m.b11*m.b16*m.b19*m.b24 + 64*m.b11*m.b16*m.b20*m.b25 + 128*m.b11*m.b17*m.b18*m.b24 + 
                       64*m.b11*m.b17*m.b19*m.b25 + 768*m.b12*m.b13*m.b14*m.b15 + 704*m.b12*m.b13*m.b15*m.b16 + 640*
                       m.b12*m.b13*m.b16*m.b17 + 576*m.b12*m.b13*m.b17*m.b18 + 512*m.b12*m.b13*m.b18*m.b19 + 448*m.b12*
                       m.b13*m.b19*m.b20 + 384*m.b12*m.b13*m.b20*m.b21 + 320*m.b12*m.b13*m.b21*m.b22 + 256*m.b12*m.b13*
                       m.b22*m.b23 + 192*m.b12*m.b13*m.b23*m.b24 + 128*m.b12*m.b13*m.b24*m.b25 + 64*m.b12*m.b13*m.b25*
                       m.b26 + 640*m.b12*m.b14*m.b15*m.b17 + 576*m.b12*m.b14*m.b16*m.b18 + 512*m.b12*m.b14*m.b17*m.b19
                        + 448*m.b12*m.b14*m.b18*m.b20 + 384*m.b12*m.b14*m.b19*m.b21 + 320*m.b12*m.b14*m.b20*m.b22 + 256*
                       m.b12*m.b14*m.b21*m.b23 + 192*m.b12*m.b14*m.b22*m.b24 + 128*m.b12*m.b14*m.b23*m.b25 + 64*m.b12*
                       m.b14*m.b24*m.b26 + 512*m.b12*m.b15*m.b16*m.b19 + 448*m.b12*m.b15*m.b17*m.b20 + 384*m.b12*m.b15*
                       m.b18*m.b21 + 320*m.b12*m.b15*m.b19*m.b22 + 256*m.b12*m.b15*m.b20*m.b23 + 192*m.b12*m.b15*m.b21*
                       m.b24 + 128*m.b12*m.b15*m.b22*m.b25 + 64*m.b12*m.b15*m.b23*m.b26 + 384*m.b12*m.b16*m.b17*m.b21 + 
                       320*m.b12*m.b16*m.b18*m.b22 + 256*m.b12*m.b16*m.b19*m.b23 + 192*m.b12*m.b16*m.b20*m.b24 + 128*
                       m.b12*m.b16*m.b21*m.b25 + 64*m.b12*m.b16*m.b22*m.b26 + 256*m.b12*m.b17*m.b18*m.b23 + 192*m.b12*
                       m.b17*m.b19*m.b24 + 128*m.b12*m.b17*m.b20*m.b25 + 64*m.b12*m.b17*m.b21*m.b26 + 128*m.b12*m.b18*
                       m.b19*m.b25 + 64*m.b12*m.b18*m.b20*m.b26 + 768*m.b13*m.b14*m.b15*m.b16 + 704*m.b13*m.b14*m.b16*
                       m.b17 + 640*m.b13*m.b14*m.b17*m.b18 + 576*m.b13*m.b14*m.b18*m.b19 + 512*m.b13*m.b14*m.b19*m.b20
                        + 448*m.b13*m.b14*m.b20*m.b21 + 384*m.b13*m.b14*m.b21*m.b22 + 320*m.b13*m.b14*m.b22*m.b23 + 256*
                       m.b13*m.b14*m.b23*m.b24 + 192*m.b13*m.b14*m.b24*m.b25 + 128*m.b13*m.b14*m.b25*m.b26 + 64*m.b13*
                       m.b14*m.b26*m.b27 + 640*m.b13*m.b15*m.b16*m.b18 + 576*m.b13*m.b15*m.b17*m.b19 + 512*m.b13*m.b15*
                       m.b18*m.b20 + 448*m.b13*m.b15*m.b19*m.b21 + 384*m.b13*m.b15*m.b20*m.b22 + 320*m.b13*m.b15*m.b21*
                       m.b23 + 256*m.b13*m.b15*m.b22*m.b24 + 192*m.b13*m.b15*m.b23*m.b25 + 128*m.b13*m.b15*m.b24*m.b26
                        + 64*m.b13*m.b15*m.b25*m.b27 + 512*m.b13*m.b16*m.b17*m.b20 + 448*m.b13*m.b16*m.b18*m.b21 + 384*
                       m.b13*m.b16*m.b19*m.b22 + 320*m.b13*m.b16*m.b20*m.b23 + 256*m.b13*m.b16*m.b21*m.b24 + 192*m.b13*
                       m.b16*m.b22*m.b25 + 128*m.b13*m.b16*m.b23*m.b26 + 64*m.b13*m.b16*m.b24*m.b27 + 384*m.b13*m.b17*
                       m.b18*m.b22 + 320*m.b13*m.b17*m.b19*m.b23 + 256*m.b13*m.b17*m.b20*m.b24 + 192*m.b13*m.b17*m.b21*
                       m.b25 + 128*m.b13*m.b17*m.b22*m.b26 + 64*m.b13*m.b17*m.b23*m.b27 + 256*m.b13*m.b18*m.b19*m.b24 + 
                       192*m.b13*m.b18*m.b20*m.b25 + 128*m.b13*m.b18*m.b21*m.b26 + 64*m.b13*m.b18*m.b22*m.b27 + 128*
                       m.b13*m.b19*m.b20*m.b26 + 64*m.b13*m.b19*m.b21*m.b27 + 768*m.b14*m.b15*m.b16*m.b17 + 704*m.b14*
                       m.b15*m.b17*m.b18 + 640*m.b14*m.b15*m.b18*m.b19 + 576*m.b14*m.b15*m.b19*m.b20 + 512*m.b14*m.b15*
                       m.b20*m.b21 + 448*m.b14*m.b15*m.b21*m.b22 + 384*m.b14*m.b15*m.b22*m.b23 + 320*m.b14*m.b15*m.b23*
                       m.b24 + 256*m.b14*m.b15*m.b24*m.b25 + 192*m.b14*m.b15*m.b25*m.b26 + 128*m.b14*m.b15*m.b26*m.b27
                        + 64*m.b14*m.b15*m.b27*m.b28 + 640*m.b14*m.b16*m.b17*m.b19 + 576*m.b14*m.b16*m.b18*m.b20 + 512*
                       m.b14*m.b16*m.b19*m.b21 + 448*m.b14*m.b16*m.b20*m.b22 + 384*m.b14*m.b16*m.b21*m.b23 + 320*m.b14*
                       m.b16*m.b22*m.b24 + 256*m.b14*m.b16*m.b23*m.b25 + 192*m.b14*m.b16*m.b24*m.b26 + 128*m.b14*m.b16*
                       m.b25*m.b27 + 64*m.b14*m.b16*m.b26*m.b28 + 512*m.b14*m.b17*m.b18*m.b21 + 448*m.b14*m.b17*m.b19*
                       m.b22 + 384*m.b14*m.b17*m.b20*m.b23 + 320*m.b14*m.b17*m.b21*m.b24 + 256*m.b14*m.b17*m.b22*m.b25
                        + 192*m.b14*m.b17*m.b23*m.b26 + 128*m.b14*m.b17*m.b24*m.b27 + 64*m.b14*m.b17*m.b25*m.b28 + 384*
                       m.b14*m.b18*m.b19*m.b23 + 320*m.b14*m.b18*m.b20*m.b24 + 256*m.b14*m.b18*m.b21*m.b25 + 192*m.b14*
                       m.b18*m.b22*m.b26 + 128*m.b14*m.b18*m.b23*m.b27 + 64*m.b14*m.b18*m.b24*m.b28 + 256*m.b14*m.b19*
                       m.b20*m.b25 + 192*m.b14*m.b19*m.b21*m.b26 + 128*m.b14*m.b19*m.b22*m.b27 + 64*m.b14*m.b19*m.b23*
                       m.b28 + 128*m.b14*m.b20*m.b21*m.b27 + 64*m.b14*m.b20*m.b22*m.b28 + 768*m.b15*m.b16*m.b17*m.b18 + 
                       704*m.b15*m.b16*m.b18*m.b19 + 640*m.b15*m.b16*m.b19*m.b20 + 576*m.b15*m.b16*m.b20*m.b21 + 512*
                       m.b15*m.b16*m.b21*m.b22 + 448*m.b15*m.b16*m.b22*m.b23 + 384*m.b15*m.b16*m.b23*m.b24 + 320*m.b15*
                       m.b16*m.b24*m.b25 + 256*m.b15*m.b16*m.b25*m.b26 + 192*m.b15*m.b16*m.b26*m.b27 + 128*m.b15*m.b16*
                       m.b27*m.b28 + 64*m.b15*m.b16*m.b28*m.b29 + 640*m.b15*m.b17*m.b18*m.b20 + 576*m.b15*m.b17*m.b19*
                       m.b21 + 512*m.b15*m.b17*m.b20*m.b22 + 448*m.b15*m.b17*m.b21*m.b23 + 384*m.b15*m.b17*m.b22*m.b24
                        + 320*m.b15*m.b17*m.b23*m.b25 + 256*m.b15*m.b17*m.b24*m.b26 + 192*m.b15*m.b17*m.b25*m.b27 + 128*
                       m.b15*m.b17*m.b26*m.b28 + 64*m.b15*m.b17*m.b27*m.b29 + 512*m.b15*m.b18*m.b19*m.b22 + 448*m.b15*
                       m.b18*m.b20*m.b23 + 384*m.b15*m.b18*m.b21*m.b24 + 320*m.b15*m.b18*m.b22*m.b25 + 256*m.b15*m.b18*
                       m.b23*m.b26 + 192*m.b15*m.b18*m.b24*m.b27 + 128*m.b15*m.b18*m.b25*m.b28 + 64*m.b15*m.b18*m.b26*
                       m.b29 + 384*m.b15*m.b19*m.b20*m.b24 + 320*m.b15*m.b19*m.b21*m.b25 + 256*m.b15*m.b19*m.b22*m.b26
                        + 192*m.b15*m.b19*m.b23*m.b27 + 128*m.b15*m.b19*m.b24*m.b28 + 64*m.b15*m.b19*m.b25*m.b29 + 256*
                       m.b15*m.b20*m.b21*m.b26 + 192*m.b15*m.b20*m.b22*m.b27 + 128*m.b15*m.b20*m.b23*m.b28 + 64*m.b15*
                       m.b20*m.b24*m.b29 + 128*m.b15*m.b21*m.b22*m.b28 + 64*m.b15*m.b21*m.b23*m.b29 + 768*m.b16*m.b17*
                       m.b18*m.b19 + 704*m.b16*m.b17*m.b19*m.b20 + 640*m.b16*m.b17*m.b20*m.b21 + 576*m.b16*m.b17*m.b21*
                       m.b22 + 512*m.b16*m.b17*m.b22*m.b23 + 448*m.b16*m.b17*m.b23*m.b24 + 384*m.b16*m.b17*m.b24*m.b25
                        + 320*m.b16*m.b17*m.b25*m.b26 + 256*m.b16*m.b17*m.b26*m.b27 + 192*m.b16*m.b17*m.b27*m.b28 + 128*
                       m.b16*m.b17*m.b28*m.b29 + 64*m.b16*m.b17*m.b29*m.b30 + 640*m.b16*m.b18*m.b19*m.b21 + 576*m.b16*
                       m.b18*m.b20*m.b22 + 512*m.b16*m.b18*m.b21*m.b23 + 448*m.b16*m.b18*m.b22*m.b24 + 384*m.b16*m.b18*
                       m.b23*m.b25 + 320*m.b16*m.b18*m.b24*m.b26 + 256*m.b16*m.b18*m.b25*m.b27 + 192*m.b16*m.b18*m.b26*
                       m.b28 + 128*m.b16*m.b18*m.b27*m.b29 + 64*m.b16*m.b18*m.b28*m.b30 + 512*m.b16*m.b19*m.b20*m.b23 + 
                       448*m.b16*m.b19*m.b21*m.b24 + 384*m.b16*m.b19*m.b22*m.b25 + 320*m.b16*m.b19*m.b23*m.b26 + 256*
                       m.b16*m.b19*m.b24*m.b27 + 192*m.b16*m.b19*m.b25*m.b28 + 128*m.b16*m.b19*m.b26*m.b29 + 64*m.b16*
                       m.b19*m.b27*m.b30 + 384*m.b16*m.b20*m.b21*m.b25 + 320*m.b16*m.b20*m.b22*m.b26 + 256*m.b16*m.b20*
                       m.b23*m.b27 + 192*m.b16*m.b20*m.b24*m.b28 + 128*m.b16*m.b20*m.b25*m.b29 + 64*m.b16*m.b20*m.b26*
                       m.b30 + 256*m.b16*m.b21*m.b22*m.b27 + 192*m.b16*m.b21*m.b23*m.b28 + 128*m.b16*m.b21*m.b24*m.b29
                        + 64*m.b16*m.b21*m.b25*m.b30 + 128*m.b16*m.b22*m.b23*m.b29 + 64*m.b16*m.b22*m.b24*m.b30 + 768*
                       m.b17*m.b18*m.b19*m.b20 + 704*m.b17*m.b18*m.b20*m.b21 + 640*m.b17*m.b18*m.b21*m.b22 + 576*m.b17*
                       m.b18*m.b22*m.b23 + 512*m.b17*m.b18*m.b23*m.b24 + 448*m.b17*m.b18*m.b24*m.b25 + 384*m.b17*m.b18*
                       m.b25*m.b26 + 320*m.b17*m.b18*m.b26*m.b27 + 256*m.b17*m.b18*m.b27*m.b28 + 192*m.b17*m.b18*m.b28*
                       m.b29 + 128*m.b17*m.b18*m.b29*m.b30 + 64*m.b17*m.b18*m.b30*m.b31 + 640*m.b17*m.b19*m.b20*m.b22 + 
                       576*m.b17*m.b19*m.b21*m.b23 + 512*m.b17*m.b19*m.b22*m.b24 + 448*m.b17*m.b19*m.b23*m.b25 + 384*
                       m.b17*m.b19*m.b24*m.b26 + 320*m.b17*m.b19*m.b25*m.b27 + 256*m.b17*m.b19*m.b26*m.b28 + 192*m.b17*
                       m.b19*m.b27*m.b29 + 128*m.b17*m.b19*m.b28*m.b30 + 64*m.b17*m.b19*m.b29*m.b31 + 512*m.b17*m.b20*
                       m.b21*m.b24 + 448*m.b17*m.b20*m.b22*m.b25 + 384*m.b17*m.b20*m.b23*m.b26 + 320*m.b17*m.b20*m.b24*
                       m.b27 + 256*m.b17*m.b20*m.b25*m.b28 + 192*m.b17*m.b20*m.b26*m.b29 + 128*m.b17*m.b20*m.b27*m.b30
                        + 64*m.b17*m.b20*m.b28*m.b31 + 384*m.b17*m.b21*m.b22*m.b26 + 320*m.b17*m.b21*m.b23*m.b27 + 256*
                       m.b17*m.b21*m.b24*m.b28 + 192*m.b17*m.b21*m.b25*m.b29 + 128*m.b17*m.b21*m.b26*m.b30 + 64*m.b17*
                       m.b21*m.b27*m.b31 + 256*m.b17*m.b22*m.b23*m.b28 + 192*m.b17*m.b22*m.b24*m.b29 + 128*m.b17*m.b22*
                       m.b25*m.b30 + 64*m.b17*m.b22*m.b26*m.b31 + 128*m.b17*m.b23*m.b24*m.b30 + 64*m.b17*m.b23*m.b25*
                       m.b31 + 768*m.b18*m.b19*m.b20*m.b21 + 704*m.b18*m.b19*m.b21*m.b22 + 640*m.b18*m.b19*m.b22*m.b23
                        + 576*m.b18*m.b19*m.b23*m.b24 + 512*m.b18*m.b19*m.b24*m.b25 + 448*m.b18*m.b19*m.b25*m.b26 + 384*
                       m.b18*m.b19*m.b26*m.b27 + 320*m.b18*m.b19*m.b27*m.b28 + 256*m.b18*m.b19*m.b28*m.b29 + 192*m.b18*
                       m.b19*m.b29*m.b30 + 128*m.b18*m.b19*m.b30*m.b31 + 64*m.b18*m.b19*m.b31*m.b32 + 640*m.b18*m.b20*
                       m.b21*m.b23 + 576*m.b18*m.b20*m.b22*m.b24 + 512*m.b18*m.b20*m.b23*m.b25 + 448*m.b18*m.b20*m.b24*
                       m.b26 + 384*m.b18*m.b20*m.b25*m.b27 + 320*m.b18*m.b20*m.b26*m.b28 + 256*m.b18*m.b20*m.b27*m.b29
                        + 192*m.b18*m.b20*m.b28*m.b30 + 128*m.b18*m.b20*m.b29*m.b31 + 64*m.b18*m.b20*m.b30*m.b32 + 512*
                       m.b18*m.b21*m.b22*m.b25 + 448*m.b18*m.b21*m.b23*m.b26 + 384*m.b18*m.b21*m.b24*m.b27 + 320*m.b18*
                       m.b21*m.b25*m.b28 + 256*m.b18*m.b21*m.b26*m.b29 + 192*m.b18*m.b21*m.b27*m.b30 + 128*m.b18*m.b21*
                       m.b28*m.b31 + 64*m.b18*m.b21*m.b29*m.b32 + 384*m.b18*m.b22*m.b23*m.b27 + 320*m.b18*m.b22*m.b24*
                       m.b28 + 256*m.b18*m.b22*m.b25*m.b29 + 192*m.b18*m.b22*m.b26*m.b30 + 128*m.b18*m.b22*m.b27*m.b31
                        + 64*m.b18*m.b22*m.b28*m.b32 + 256*m.b18*m.b23*m.b24*m.b29 + 192*m.b18*m.b23*m.b25*m.b30 + 128*
                       m.b18*m.b23*m.b26*m.b31 + 64*m.b18*m.b23*m.b27*m.b32 + 128*m.b18*m.b24*m.b25*m.b31 + 64*m.b18*
                       m.b24*m.b26*m.b32 + 768*m.b19*m.b20*m.b21*m.b22 + 704*m.b19*m.b20*m.b22*m.b23 + 640*m.b19*m.b20*
                       m.b23*m.b24 + 576*m.b19*m.b20*m.b24*m.b25 + 512*m.b19*m.b20*m.b25*m.b26 + 448*m.b19*m.b20*m.b26*
                       m.b27 + 384*m.b19*m.b20*m.b27*m.b28 + 320*m.b19*m.b20*m.b28*m.b29 + 256*m.b19*m.b20*m.b29*m.b30
                        + 192*m.b19*m.b20*m.b30*m.b31 + 128*m.b19*m.b20*m.b31*m.b32 + 64*m.b19*m.b20*m.b32*m.b33 + 640*
                       m.b19*m.b21*m.b22*m.b24 + 576*m.b19*m.b21*m.b23*m.b25 + 512*m.b19*m.b21*m.b24*m.b26 + 448*m.b19*
                       m.b21*m.b25*m.b27 + 384*m.b19*m.b21*m.b26*m.b28 + 320*m.b19*m.b21*m.b27*m.b29 + 256*m.b19*m.b21*
                       m.b28*m.b30 + 192*m.b19*m.b21*m.b29*m.b31 + 128*m.b19*m.b21*m.b30*m.b32 + 64*m.b19*m.b21*m.b31*
                       m.b33 + 512*m.b19*m.b22*m.b23*m.b26 + 448*m.b19*m.b22*m.b24*m.b27 + 384*m.b19*m.b22*m.b25*m.b28
                        + 320*m.b19*m.b22*m.b26*m.b29 + 256*m.b19*m.b22*m.b27*m.b30 + 192*m.b19*m.b22*m.b28*m.b31 + 128*
                       m.b19*m.b22*m.b29*m.b32 + 64*m.b19*m.b22*m.b30*m.b33 + 384*m.b19*m.b23*m.b24*m.b28 + 320*m.b19*
                       m.b23*m.b25*m.b29 + 256*m.b19*m.b23*m.b26*m.b30 + 192*m.b19*m.b23*m.b27*m.b31 + 128*m.b19*m.b23*
                       m.b28*m.b32 + 64*m.b19*m.b23*m.b29*m.b33 + 256*m.b19*m.b24*m.b25*m.b30 + 192*m.b19*m.b24*m.b26*
                       m.b31 + 128*m.b19*m.b24*m.b27*m.b32 + 64*m.b19*m.b24*m.b28*m.b33 + 128*m.b19*m.b25*m.b26*m.b32 + 
                       64*m.b19*m.b25*m.b27*m.b33 + 768*m.b20*m.b21*m.b22*m.b23 + 704*m.b20*m.b21*m.b23*m.b24 + 640*
                       m.b20*m.b21*m.b24*m.b25 + 576*m.b20*m.b21*m.b25*m.b26 + 512*m.b20*m.b21*m.b26*m.b27 + 448*m.b20*
                       m.b21*m.b27*m.b28 + 384*m.b20*m.b21*m.b28*m.b29 + 320*m.b20*m.b21*m.b29*m.b30 + 256*m.b20*m.b21*
                       m.b30*m.b31 + 192*m.b20*m.b21*m.b31*m.b32 + 128*m.b20*m.b21*m.b32*m.b33 + 64*m.b20*m.b21*m.b33*
                       m.b34 + 640*m.b20*m.b22*m.b23*m.b25 + 576*m.b20*m.b22*m.b24*m.b26 + 512*m.b20*m.b22*m.b25*m.b27
                        + 448*m.b20*m.b22*m.b26*m.b28 + 384*m.b20*m.b22*m.b27*m.b29 + 320*m.b20*m.b22*m.b28*m.b30 + 256*
                       m.b20*m.b22*m.b29*m.b31 + 192*m.b20*m.b22*m.b30*m.b32 + 128*m.b20*m.b22*m.b31*m.b33 + 64*m.b20*
                       m.b22*m.b32*m.b34 + 512*m.b20*m.b23*m.b24*m.b27 + 448*m.b20*m.b23*m.b25*m.b28 + 384*m.b20*m.b23*
                       m.b26*m.b29 + 320*m.b20*m.b23*m.b27*m.b30 + 256*m.b20*m.b23*m.b28*m.b31 + 192*m.b20*m.b23*m.b29*
                       m.b32 + 128*m.b20*m.b23*m.b30*m.b33 + 64*m.b20*m.b23*m.b31*m.b34 + 384*m.b20*m.b24*m.b25*m.b29 + 
                       320*m.b20*m.b24*m.b26*m.b30 + 256*m.b20*m.b24*m.b27*m.b31 + 192*m.b20*m.b24*m.b28*m.b32 + 128*
                       m.b20*m.b24*m.b29*m.b33 + 64*m.b20*m.b24*m.b30*m.b34 + 256*m.b20*m.b25*m.b26*m.b31 + 192*m.b20*
                       m.b25*m.b27*m.b32 + 128*m.b20*m.b25*m.b28*m.b33 + 64*m.b20*m.b25*m.b29*m.b34 + 128*m.b20*m.b26*
                       m.b27*m.b33 + 64*m.b20*m.b26*m.b28*m.b34 + 768*m.b21*m.b22*m.b23*m.b24 + 704*m.b21*m.b22*m.b24*
                       m.b25 + 640*m.b21*m.b22*m.b25*m.b26 + 576*m.b21*m.b22*m.b26*m.b27 + 512*m.b21*m.b22*m.b27*m.b28
                        + 448*m.b21*m.b22*m.b28*m.b29 + 384*m.b21*m.b22*m.b29*m.b30 + 320*m.b21*m.b22*m.b30*m.b31 + 256*
                       m.b21*m.b22*m.b31*m.b32 + 192*m.b21*m.b22*m.b32*m.b33 + 128*m.b21*m.b22*m.b33*m.b34 + 64*m.b21*
                       m.b22*m.b34*m.b35 + 640*m.b21*m.b23*m.b24*m.b26 + 576*m.b21*m.b23*m.b25*m.b27 + 512*m.b21*m.b23*
                       m.b26*m.b28 + 448*m.b21*m.b23*m.b27*m.b29 + 384*m.b21*m.b23*m.b28*m.b30 + 320*m.b21*m.b23*m.b29*
                       m.b31 + 256*m.b21*m.b23*m.b30*m.b32 + 192*m.b21*m.b23*m.b31*m.b33 + 128*m.b21*m.b23*m.b32*m.b34
                        + 64*m.b21*m.b23*m.b33*m.b35 + 512*m.b21*m.b24*m.b25*m.b28 + 448*m.b21*m.b24*m.b26*m.b29 + 384*
                       m.b21*m.b24*m.b27*m.b30 + 320*m.b21*m.b24*m.b28*m.b31 + 256*m.b21*m.b24*m.b29*m.b32 + 192*m.b21*
                       m.b24*m.b30*m.b33 + 128*m.b21*m.b24*m.b31*m.b34 + 64*m.b21*m.b24*m.b32*m.b35 + 384*m.b21*m.b25*
                       m.b26*m.b30 + 320*m.b21*m.b25*m.b27*m.b31 + 256*m.b21*m.b25*m.b28*m.b32 + 192*m.b21*m.b25*m.b29*
                       m.b33 + 128*m.b21*m.b25*m.b30*m.b34 + 64*m.b21*m.b25*m.b31*m.b35 + 256*m.b21*m.b26*m.b27*m.b32 + 
                       192*m.b21*m.b26*m.b28*m.b33 + 128*m.b21*m.b26*m.b29*m.b34 + 64*m.b21*m.b26*m.b30*m.b35 + 128*
                       m.b21*m.b27*m.b28*m.b34 + 64*m.b21*m.b27*m.b29*m.b35 + 768*m.b22*m.b23*m.b24*m.b25 + 704*m.b22*
                       m.b23*m.b25*m.b26 + 640*m.b22*m.b23*m.b26*m.b27 + 576*m.b22*m.b23*m.b27*m.b28 + 512*m.b22*m.b23*
                       m.b28*m.b29 + 448*m.b22*m.b23*m.b29*m.b30 + 384*m.b22*m.b23*m.b30*m.b31 + 320*m.b22*m.b23*m.b31*
                       m.b32 + 256*m.b22*m.b23*m.b32*m.b33 + 192*m.b22*m.b23*m.b33*m.b34 + 128*m.b22*m.b23*m.b34*m.b35
                        + 64*m.b22*m.b23*m.b35*m.b36 + 640*m.b22*m.b24*m.b25*m.b27 + 576*m.b22*m.b24*m.b26*m.b28 + 512*
                       m.b22*m.b24*m.b27*m.b29 + 448*m.b22*m.b24*m.b28*m.b30 + 384*m.b22*m.b24*m.b29*m.b31 + 320*m.b22*
                       m.b24*m.b30*m.b32 + 256*m.b22*m.b24*m.b31*m.b33 + 192*m.b22*m.b24*m.b32*m.b34 + 128*m.b22*m.b24*
                       m.b33*m.b35 + 64*m.b22*m.b24*m.b34*m.b36 + 512*m.b22*m.b25*m.b26*m.b29 + 448*m.b22*m.b25*m.b27*
                       m.b30 + 384*m.b22*m.b25*m.b28*m.b31 + 320*m.b22*m.b25*m.b29*m.b32 + 256*m.b22*m.b25*m.b30*m.b33
                        + 192*m.b22*m.b25*m.b31*m.b34 + 128*m.b22*m.b25*m.b32*m.b35 + 64*m.b22*m.b25*m.b33*m.b36 + 384*
                       m.b22*m.b26*m.b27*m.b31 + 320*m.b22*m.b26*m.b28*m.b32 + 256*m.b22*m.b26*m.b29*m.b33 + 192*m.b22*
                       m.b26*m.b30*m.b34 + 128*m.b22*m.b26*m.b31*m.b35 + 64*m.b22*m.b26*m.b32*m.b36 + 256*m.b22*m.b27*
                       m.b28*m.b33 + 192*m.b22*m.b27*m.b29*m.b34 + 128*m.b22*m.b27*m.b30*m.b35 + 64*m.b22*m.b27*m.b31*
                       m.b36 + 128*m.b22*m.b28*m.b29*m.b35 + 64*m.b22*m.b28*m.b30*m.b36 + 768*m.b23*m.b24*m.b25*m.b26 + 
                       704*m.b23*m.b24*m.b26*m.b27 + 640*m.b23*m.b24*m.b27*m.b28 + 576*m.b23*m.b24*m.b28*m.b29 + 512*
                       m.b23*m.b24*m.b29*m.b30 + 448*m.b23*m.b24*m.b30*m.b31 + 384*m.b23*m.b24*m.b31*m.b32 + 320*m.b23*
                       m.b24*m.b32*m.b33 + 256*m.b23*m.b24*m.b33*m.b34 + 192*m.b23*m.b24*m.b34*m.b35 + 128*m.b23*m.b24*
                       m.b35*m.b36 + 64*m.b23*m.b24*m.b36*m.b37 + 640*m.b23*m.b25*m.b26*m.b28 + 576*m.b23*m.b25*m.b27*
                       m.b29 + 512*m.b23*m.b25*m.b28*m.b30 + 448*m.b23*m.b25*m.b29*m.b31 + 384*m.b23*m.b25*m.b30*m.b32
                        + 320*m.b23*m.b25*m.b31*m.b33 + 256*m.b23*m.b25*m.b32*m.b34 + 192*m.b23*m.b25*m.b33*m.b35 + 128*
                       m.b23*m.b25*m.b34*m.b36 + 64*m.b23*m.b25*m.b35*m.b37 + 512*m.b23*m.b26*m.b27*m.b30 + 448*m.b23*
                       m.b26*m.b28*m.b31 + 384*m.b23*m.b26*m.b29*m.b32 + 320*m.b23*m.b26*m.b30*m.b33 + 256*m.b23*m.b26*
                       m.b31*m.b34 + 192*m.b23*m.b26*m.b32*m.b35 + 128*m.b23*m.b26*m.b33*m.b36 + 64*m.b23*m.b26*m.b34*
                       m.b37 + 384*m.b23*m.b27*m.b28*m.b32 + 320*m.b23*m.b27*m.b29*m.b33 + 256*m.b23*m.b27*m.b30*m.b34
                        + 192*m.b23*m.b27*m.b31*m.b35 + 128*m.b23*m.b27*m.b32*m.b36 + 64*m.b23*m.b27*m.b33*m.b37 + 256*
                       m.b23*m.b28*m.b29*m.b34 + 192*m.b23*m.b28*m.b30*m.b35 + 128*m.b23*m.b28*m.b31*m.b36 + 64*m.b23*
                       m.b28*m.b32*m.b37 + 128*m.b23*m.b29*m.b30*m.b36 + 64*m.b23*m.b29*m.b31*m.b37 + 768*m.b24*m.b25*
                       m.b26*m.b27 + 704*m.b24*m.b25*m.b27*m.b28 + 640*m.b24*m.b25*m.b28*m.b29 + 576*m.b24*m.b25*m.b29*
                       m.b30 + 512*m.b24*m.b25*m.b30*m.b31 + 448*m.b24*m.b25*m.b31*m.b32 + 384*m.b24*m.b25*m.b32*m.b33
                        + 320*m.b24*m.b25*m.b33*m.b34 + 256*m.b24*m.b25*m.b34*m.b35 + 192*m.b24*m.b25*m.b35*m.b36 + 128*
                       m.b24*m.b25*m.b36*m.b37 + 64*m.b24*m.b25*m.b37*m.b38 + 640*m.b24*m.b26*m.b27*m.b29 + 576*m.b24*
                       m.b26*m.b28*m.b30 + 512*m.b24*m.b26*m.b29*m.b31 + 448*m.b24*m.b26*m.b30*m.b32 + 384*m.b24*m.b26*
                       m.b31*m.b33 + 320*m.b24*m.b26*m.b32*m.b34 + 256*m.b24*m.b26*m.b33*m.b35 + 192*m.b24*m.b26*m.b34*
                       m.b36 + 128*m.b24*m.b26*m.b35*m.b37 + 64*m.b24*m.b26*m.b36*m.b38 + 512*m.b24*m.b27*m.b28*m.b31 + 
                       448*m.b24*m.b27*m.b29*m.b32 + 384*m.b24*m.b27*m.b30*m.b33 + 320*m.b24*m.b27*m.b31*m.b34 + 256*
                       m.b24*m.b27*m.b32*m.b35 + 192*m.b24*m.b27*m.b33*m.b36 + 128*m.b24*m.b27*m.b34*m.b37 + 64*m.b24*
                       m.b27*m.b35*m.b38 + 384*m.b24*m.b28*m.b29*m.b33 + 320*m.b24*m.b28*m.b30*m.b34 + 256*m.b24*m.b28*
                       m.b31*m.b35 + 192*m.b24*m.b28*m.b32*m.b36 + 128*m.b24*m.b28*m.b33*m.b37 + 64*m.b24*m.b28*m.b34*
                       m.b38 + 256*m.b24*m.b29*m.b30*m.b35 + 192*m.b24*m.b29*m.b31*m.b36 + 128*m.b24*m.b29*m.b32*m.b37
                        + 64*m.b24*m.b29*m.b33*m.b38 + 128*m.b24*m.b30*m.b31*m.b37 + 64*m.b24*m.b30*m.b32*m.b38 + 768*
                       m.b25*m.b26*m.b27*m.b28 + 704*m.b25*m.b26*m.b28*m.b29 + 640*m.b25*m.b26*m.b29*m.b30 + 576*m.b25*
                       m.b26*m.b30*m.b31 + 512*m.b25*m.b26*m.b31*m.b32 + 448*m.b25*m.b26*m.b32*m.b33 + 384*m.b25*m.b26*
                       m.b33*m.b34 + 320*m.b25*m.b26*m.b34*m.b35 + 256*m.b25*m.b26*m.b35*m.b36 + 192*m.b25*m.b26*m.b36*
                       m.b37 + 128*m.b25*m.b26*m.b37*m.b38 + 64*m.b25*m.b26*m.b38*m.b39 + 640*m.b25*m.b27*m.b28*m.b30 + 
                       576*m.b25*m.b27*m.b29*m.b31 + 512*m.b25*m.b27*m.b30*m.b32 + 448*m.b25*m.b27*m.b31*m.b33 + 384*
                       m.b25*m.b27*m.b32*m.b34 + 320*m.b25*m.b27*m.b33*m.b35 + 256*m.b25*m.b27*m.b34*m.b36 + 192*m.b25*
                       m.b27*m.b35*m.b37 + 128*m.b25*m.b27*m.b36*m.b38 + 64*m.b25*m.b27*m.b37*m.b39 + 512*m.b25*m.b28*
                       m.b29*m.b32 + 448*m.b25*m.b28*m.b30*m.b33 + 384*m.b25*m.b28*m.b31*m.b34 + 320*m.b25*m.b28*m.b32*
                       m.b35 + 256*m.b25*m.b28*m.b33*m.b36 + 192*m.b25*m.b28*m.b34*m.b37 + 128*m.b25*m.b28*m.b35*m.b38
                        + 64*m.b25*m.b28*m.b36*m.b39 + 384*m.b25*m.b29*m.b30*m.b34 + 320*m.b25*m.b29*m.b31*m.b35 + 256*
                       m.b25*m.b29*m.b32*m.b36 + 192*m.b25*m.b29*m.b33*m.b37 + 128*m.b25*m.b29*m.b34*m.b38 + 64*m.b25*
                       m.b29*m.b35*m.b39 + 256*m.b25*m.b30*m.b31*m.b36 + 192*m.b25*m.b30*m.b32*m.b37 + 128*m.b25*m.b30*
                       m.b33*m.b38 + 64*m.b25*m.b30*m.b34*m.b39 + 128*m.b25*m.b31*m.b32*m.b38 + 64*m.b25*m.b31*m.b33*
                       m.b39 + 768*m.b26*m.b27*m.b28*m.b29 + 704*m.b26*m.b27*m.b29*m.b30 + 640*m.b26*m.b27*m.b30*m.b31
                        + 576*m.b26*m.b27*m.b31*m.b32 + 512*m.b26*m.b27*m.b32*m.b33 + 448*m.b26*m.b27*m.b33*m.b34 + 384*
                       m.b26*m.b27*m.b34*m.b35 + 320*m.b26*m.b27*m.b35*m.b36 + 256*m.b26*m.b27*m.b36*m.b37 + 192*m.b26*
                       m.b27*m.b37*m.b38 + 128*m.b26*m.b27*m.b38*m.b39 + 64*m.b26*m.b27*m.b39*m.b40 + 640*m.b26*m.b28*
                       m.b29*m.b31 + 576*m.b26*m.b28*m.b30*m.b32 + 512*m.b26*m.b28*m.b31*m.b33 + 448*m.b26*m.b28*m.b32*
                       m.b34 + 384*m.b26*m.b28*m.b33*m.b35 + 320*m.b26*m.b28*m.b34*m.b36 + 256*m.b26*m.b28*m.b35*m.b37
                        + 192*m.b26*m.b28*m.b36*m.b38 + 128*m.b26*m.b28*m.b37*m.b39 + 64*m.b26*m.b28*m.b38*m.b40 + 512*
                       m.b26*m.b29*m.b30*m.b33 + 448*m.b26*m.b29*m.b31*m.b34 + 384*m.b26*m.b29*m.b32*m.b35 + 320*m.b26*
                       m.b29*m.b33*m.b36 + 256*m.b26*m.b29*m.b34*m.b37 + 192*m.b26*m.b29*m.b35*m.b38 + 128*m.b26*m.b29*
                       m.b36*m.b39 + 64*m.b26*m.b29*m.b37*m.b40 + 384*m.b26*m.b30*m.b31*m.b35 + 320*m.b26*m.b30*m.b32*
                       m.b36 + 256*m.b26*m.b30*m.b33*m.b37 + 192*m.b26*m.b30*m.b34*m.b38 + 128*m.b26*m.b30*m.b35*m.b39
                        + 64*m.b26*m.b30*m.b36*m.b40 + 256*m.b26*m.b31*m.b32*m.b37 + 192*m.b26*m.b31*m.b33*m.b38 + 128*
                       m.b26*m.b31*m.b34*m.b39 + 64*m.b26*m.b31*m.b35*m.b40 + 128*m.b26*m.b32*m.b33*m.b39 + 64*m.b26*
                       m.b32*m.b34*m.b40 + 768*m.b27*m.b28*m.b29*m.b30 + 704*m.b27*m.b28*m.b30*m.b31 + 640*m.b27*m.b28*
                       m.b31*m.b32 + 576*m.b27*m.b28*m.b32*m.b33 + 512*m.b27*m.b28*m.b33*m.b34 + 448*m.b27*m.b28*m.b34*
                       m.b35 + 384*m.b27*m.b28*m.b35*m.b36 + 320*m.b27*m.b28*m.b36*m.b37 + 256*m.b27*m.b28*m.b37*m.b38
                        + 192*m.b27*m.b28*m.b38*m.b39 + 128*m.b27*m.b28*m.b39*m.b40 + 64*m.b27*m.b28*m.b40*m.b41 + 640*
                       m.b27*m.b29*m.b30*m.b32 + 576*m.b27*m.b29*m.b31*m.b33 + 512*m.b27*m.b29*m.b32*m.b34 + 448*m.b27*
                       m.b29*m.b33*m.b35 + 384*m.b27*m.b29*m.b34*m.b36 + 320*m.b27*m.b29*m.b35*m.b37 + 256*m.b27*m.b29*
                       m.b36*m.b38 + 192*m.b27*m.b29*m.b37*m.b39 + 128*m.b27*m.b29*m.b38*m.b40 + 64*m.b27*m.b29*m.b39*
                       m.b41 + 512*m.b27*m.b30*m.b31*m.b34 + 448*m.b27*m.b30*m.b32*m.b35 + 384*m.b27*m.b30*m.b33*m.b36
                        + 320*m.b27*m.b30*m.b34*m.b37 + 256*m.b27*m.b30*m.b35*m.b38 + 192*m.b27*m.b30*m.b36*m.b39 + 128*
                       m.b27*m.b30*m.b37*m.b40 + 64*m.b27*m.b30*m.b38*m.b41 + 384*m.b27*m.b31*m.b32*m.b36 + 320*m.b27*
                       m.b31*m.b33*m.b37 + 256*m.b27*m.b31*m.b34*m.b38 + 192*m.b27*m.b31*m.b35*m.b39 + 128*m.b27*m.b31*
                       m.b36*m.b40 + 64*m.b27*m.b31*m.b37*m.b41 + 256*m.b27*m.b32*m.b33*m.b38 + 192*m.b27*m.b32*m.b34*
                       m.b39 + 128*m.b27*m.b32*m.b35*m.b40 + 64*m.b27*m.b32*m.b36*m.b41 + 128*m.b27*m.b33*m.b34*m.b40 + 
                       64*m.b27*m.b33*m.b35*m.b41 + 768*m.b28*m.b29*m.b30*m.b31 + 704*m.b28*m.b29*m.b31*m.b32 + 640*
                       m.b28*m.b29*m.b32*m.b33 + 576*m.b28*m.b29*m.b33*m.b34 + 512*m.b28*m.b29*m.b34*m.b35 + 448*m.b28*
                       m.b29*m.b35*m.b36 + 384*m.b28*m.b29*m.b36*m.b37 + 320*m.b28*m.b29*m.b37*m.b38 + 256*m.b28*m.b29*
                       m.b38*m.b39 + 192*m.b28*m.b29*m.b39*m.b40 + 128*m.b28*m.b29*m.b40*m.b41 + 64*m.b28*m.b29*m.b41*
                       m.b42 + 640*m.b28*m.b30*m.b31*m.b33 + 576*m.b28*m.b30*m.b32*m.b34 + 512*m.b28*m.b30*m.b33*m.b35
                        + 448*m.b28*m.b30*m.b34*m.b36 + 384*m.b28*m.b30*m.b35*m.b37 + 320*m.b28*m.b30*m.b36*m.b38 + 256*
                       m.b28*m.b30*m.b37*m.b39 + 192*m.b28*m.b30*m.b38*m.b40 + 128*m.b28*m.b30*m.b39*m.b41 + 64*m.b28*
                       m.b30*m.b40*m.b42 + 512*m.b28*m.b31*m.b32*m.b35 + 448*m.b28*m.b31*m.b33*m.b36 + 384*m.b28*m.b31*
                       m.b34*m.b37 + 320*m.b28*m.b31*m.b35*m.b38 + 256*m.b28*m.b31*m.b36*m.b39 + 192*m.b28*m.b31*m.b37*
                       m.b40 + 128*m.b28*m.b31*m.b38*m.b41 + 64*m.b28*m.b31*m.b39*m.b42 + 384*m.b28*m.b32*m.b33*m.b37 + 
                       320*m.b28*m.b32*m.b34*m.b38 + 256*m.b28*m.b32*m.b35*m.b39 + 192*m.b28*m.b32*m.b36*m.b40 + 128*
                       m.b28*m.b32*m.b37*m.b41 + 64*m.b28*m.b32*m.b38*m.b42 + 256*m.b28*m.b33*m.b34*m.b39 + 192*m.b28*
                       m.b33*m.b35*m.b40 + 128*m.b28*m.b33*m.b36*m.b41 + 64*m.b28*m.b33*m.b37*m.b42 + 128*m.b28*m.b34*
                       m.b35*m.b41 + 64*m.b28*m.b34*m.b36*m.b42 + 768*m.b29*m.b30*m.b31*m.b32 + 704*m.b29*m.b30*m.b32*
                       m.b33 + 640*m.b29*m.b30*m.b33*m.b34 + 576*m.b29*m.b30*m.b34*m.b35 + 512*m.b29*m.b30*m.b35*m.b36
                        + 448*m.b29*m.b30*m.b36*m.b37 + 384*m.b29*m.b30*m.b37*m.b38 + 320*m.b29*m.b30*m.b38*m.b39 + 256*
                       m.b29*m.b30*m.b39*m.b40 + 192*m.b29*m.b30*m.b40*m.b41 + 128*m.b29*m.b30*m.b41*m.b42 + 64*m.b29*
                       m.b30*m.b42*m.b43 + 640*m.b29*m.b31*m.b32*m.b34 + 576*m.b29*m.b31*m.b33*m.b35 + 512*m.b29*m.b31*
                       m.b34*m.b36 + 448*m.b29*m.b31*m.b35*m.b37 + 384*m.b29*m.b31*m.b36*m.b38 + 320*m.b29*m.b31*m.b37*
                       m.b39 + 256*m.b29*m.b31*m.b38*m.b40 + 192*m.b29*m.b31*m.b39*m.b41 + 128*m.b29*m.b31*m.b40*m.b42
                        + 64*m.b29*m.b31*m.b41*m.b43 + 512*m.b29*m.b32*m.b33*m.b36 + 448*m.b29*m.b32*m.b34*m.b37 + 384*
                       m.b29*m.b32*m.b35*m.b38 + 320*m.b29*m.b32*m.b36*m.b39 + 256*m.b29*m.b32*m.b37*m.b40 + 192*m.b29*
                       m.b32*m.b38*m.b41 + 128*m.b29*m.b32*m.b39*m.b42 + 64*m.b29*m.b32*m.b40*m.b43 + 384*m.b29*m.b33*
                       m.b34*m.b38 + 320*m.b29*m.b33*m.b35*m.b39 + 256*m.b29*m.b33*m.b36*m.b40 + 192*m.b29*m.b33*m.b37*
                       m.b41 + 128*m.b29*m.b33*m.b38*m.b42 + 64*m.b29*m.b33*m.b39*m.b43 + 256*m.b29*m.b34*m.b35*m.b40 + 
                       192*m.b29*m.b34*m.b36*m.b41 + 128*m.b29*m.b34*m.b37*m.b42 + 64*m.b29*m.b34*m.b38*m.b43 + 128*
                       m.b29*m.b35*m.b36*m.b42 + 64*m.b29*m.b35*m.b37*m.b43 + 768*m.b30*m.b31*m.b32*m.b33 + 704*m.b30*
                       m.b31*m.b33*m.b34 + 640*m.b30*m.b31*m.b34*m.b35 + 576*m.b30*m.b31*m.b35*m.b36 + 512*m.b30*m.b31*
                       m.b36*m.b37 + 448*m.b30*m.b31*m.b37*m.b38 + 384*m.b30*m.b31*m.b38*m.b39 + 320*m.b30*m.b31*m.b39*
                       m.b40 + 256*m.b30*m.b31*m.b40*m.b41 + 192*m.b30*m.b31*m.b41*m.b42 + 128*m.b30*m.b31*m.b42*m.b43
                        + 64*m.b30*m.b31*m.b43*m.b44 + 640*m.b30*m.b32*m.b33*m.b35 + 576*m.b30*m.b32*m.b34*m.b36 + 512*
                       m.b30*m.b32*m.b35*m.b37 + 448*m.b30*m.b32*m.b36*m.b38 + 384*m.b30*m.b32*m.b37*m.b39 + 320*m.b30*
                       m.b32*m.b38*m.b40 + 256*m.b30*m.b32*m.b39*m.b41 + 192*m.b30*m.b32*m.b40*m.b42 + 128*m.b30*m.b32*
                       m.b41*m.b43 + 64*m.b30*m.b32*m.b42*m.b44 + 512*m.b30*m.b33*m.b34*m.b37 + 448*m.b30*m.b33*m.b35*
                       m.b38 + 384*m.b30*m.b33*m.b36*m.b39 + 320*m.b30*m.b33*m.b37*m.b40 + 256*m.b30*m.b33*m.b38*m.b41
                        + 192*m.b30*m.b33*m.b39*m.b42 + 128*m.b30*m.b33*m.b40*m.b43 + 64*m.b30*m.b33*m.b41*m.b44 + 384*
                       m.b30*m.b34*m.b35*m.b39 + 320*m.b30*m.b34*m.b36*m.b40 + 256*m.b30*m.b34*m.b37*m.b41 + 192*m.b30*
                       m.b34*m.b38*m.b42 + 128*m.b30*m.b34*m.b39*m.b43 + 64*m.b30*m.b34*m.b40*m.b44 + 256*m.b30*m.b35*
                       m.b36*m.b41 + 192*m.b30*m.b35*m.b37*m.b42 + 128*m.b30*m.b35*m.b38*m.b43 + 64*m.b30*m.b35*m.b39*
                       m.b44 + 128*m.b30*m.b36*m.b37*m.b43 + 64*m.b30*m.b36*m.b38*m.b44 + 768*m.b31*m.b32*m.b33*m.b34 + 
                       704*m.b31*m.b32*m.b34*m.b35 + 640*m.b31*m.b32*m.b35*m.b36 + 576*m.b31*m.b32*m.b36*m.b37 + 512*
                       m.b31*m.b32*m.b37*m.b38 + 448*m.b31*m.b32*m.b38*m.b39 + 384*m.b31*m.b32*m.b39*m.b40 + 320*m.b31*
                       m.b32*m.b40*m.b41 + 256*m.b31*m.b32*m.b41*m.b42 + 192*m.b31*m.b32*m.b42*m.b43 + 128*m.b31*m.b32*
                       m.b43*m.b44 + 64*m.b31*m.b32*m.b44*m.b45 + 640*m.b31*m.b33*m.b34*m.b36 + 576*m.b31*m.b33*m.b35*
                       m.b37 + 512*m.b31*m.b33*m.b36*m.b38 + 448*m.b31*m.b33*m.b37*m.b39 + 384*m.b31*m.b33*m.b38*m.b40
                        + 320*m.b31*m.b33*m.b39*m.b41 + 256*m.b31*m.b33*m.b40*m.b42 + 192*m.b31*m.b33*m.b41*m.b43 + 128*
                       m.b31*m.b33*m.b42*m.b44 + 64*m.b31*m.b33*m.b43*m.b45 + 512*m.b31*m.b34*m.b35*m.b38 + 448*m.b31*
                       m.b34*m.b36*m.b39 + 384*m.b31*m.b34*m.b37*m.b40 + 320*m.b31*m.b34*m.b38*m.b41 + 256*m.b31*m.b34*
                       m.b39*m.b42 + 192*m.b31*m.b34*m.b40*m.b43 + 128*m.b31*m.b34*m.b41*m.b44 + 64*m.b31*m.b34*m.b42*
                       m.b45 + 384*m.b31*m.b35*m.b36*m.b40 + 320*m.b31*m.b35*m.b37*m.b41 + 256*m.b31*m.b35*m.b38*m.b42
                        + 192*m.b31*m.b35*m.b39*m.b43 + 128*m.b31*m.b35*m.b40*m.b44 + 64*m.b31*m.b35*m.b41*m.b45 + 256*
                       m.b31*m.b36*m.b37*m.b42 + 192*m.b31*m.b36*m.b38*m.b43 + 128*m.b31*m.b36*m.b39*m.b44 + 64*m.b31*
                       m.b36*m.b40*m.b45 + 128*m.b31*m.b37*m.b38*m.b44 + 64*m.b31*m.b37*m.b39*m.b45 + 768*m.b32*m.b33*
                       m.b34*m.b35 + 704*m.b32*m.b33*m.b35*m.b36 + 640*m.b32*m.b33*m.b36*m.b37 + 576*m.b32*m.b33*m.b37*
                       m.b38 + 512*m.b32*m.b33*m.b38*m.b39 + 448*m.b32*m.b33*m.b39*m.b40 + 384*m.b32*m.b33*m.b40*m.b41
                        + 320*m.b32*m.b33*m.b41*m.b42 + 256*m.b32*m.b33*m.b42*m.b43 + 192*m.b32*m.b33*m.b43*m.b44 + 128*
                       m.b32*m.b33*m.b44*m.b45 + 64*m.b32*m.b33*m.b45*m.b46 + 640*m.b32*m.b34*m.b35*m.b37 + 576*m.b32*
                       m.b34*m.b36*m.b38 + 512*m.b32*m.b34*m.b37*m.b39 + 448*m.b32*m.b34*m.b38*m.b40 + 384*m.b32*m.b34*
                       m.b39*m.b41 + 320*m.b32*m.b34*m.b40*m.b42 + 256*m.b32*m.b34*m.b41*m.b43 + 192*m.b32*m.b34*m.b42*
                       m.b44 + 128*m.b32*m.b34*m.b43*m.b45 + 64*m.b32*m.b34*m.b44*m.b46 + 512*m.b32*m.b35*m.b36*m.b39 + 
                       448*m.b32*m.b35*m.b37*m.b40 + 384*m.b32*m.b35*m.b38*m.b41 + 320*m.b32*m.b35*m.b39*m.b42 + 256*
                       m.b32*m.b35*m.b40*m.b43 + 192*m.b32*m.b35*m.b41*m.b44 + 128*m.b32*m.b35*m.b42*m.b45 + 64*m.b32*
                       m.b35*m.b43*m.b46 + 384*m.b32*m.b36*m.b37*m.b41 + 320*m.b32*m.b36*m.b38*m.b42 + 256*m.b32*m.b36*
                       m.b39*m.b43 + 192*m.b32*m.b36*m.b40*m.b44 + 128*m.b32*m.b36*m.b41*m.b45 + 64*m.b32*m.b36*m.b42*
                       m.b46 + 256*m.b32*m.b37*m.b38*m.b43 + 192*m.b32*m.b37*m.b39*m.b44 + 128*m.b32*m.b37*m.b40*m.b45
                        + 64*m.b32*m.b37*m.b41*m.b46 + 128*m.b32*m.b38*m.b39*m.b45 + 64*m.b32*m.b38*m.b40*m.b46 + 768*
                       m.b33*m.b34*m.b35*m.b36 + 704*m.b33*m.b34*m.b36*m.b37 + 640*m.b33*m.b34*m.b37*m.b38 + 576*m.b33*
                       m.b34*m.b38*m.b39 + 512*m.b33*m.b34*m.b39*m.b40 + 448*m.b33*m.b34*m.b40*m.b41 + 384*m.b33*m.b34*
                       m.b41*m.b42 + 320*m.b33*m.b34*m.b42*m.b43 + 256*m.b33*m.b34*m.b43*m.b44 + 192*m.b33*m.b34*m.b44*
                       m.b45 + 128*m.b33*m.b34*m.b45*m.b46 + 64*m.b33*m.b34*m.b46*m.b47 + 640*m.b33*m.b35*m.b36*m.b38 + 
                       576*m.b33*m.b35*m.b37*m.b39 + 512*m.b33*m.b35*m.b38*m.b40 + 448*m.b33*m.b35*m.b39*m.b41 + 384*
                       m.b33*m.b35*m.b40*m.b42 + 320*m.b33*m.b35*m.b41*m.b43 + 256*m.b33*m.b35*m.b42*m.b44 + 192*m.b33*
                       m.b35*m.b43*m.b45 + 128*m.b33*m.b35*m.b44*m.b46 + 64*m.b33*m.b35*m.b45*m.b47 + 512*m.b33*m.b36*
                       m.b37*m.b40 + 448*m.b33*m.b36*m.b38*m.b41 + 384*m.b33*m.b36*m.b39*m.b42 + 320*m.b33*m.b36*m.b40*
                       m.b43 + 256*m.b33*m.b36*m.b41*m.b44 + 192*m.b33*m.b36*m.b42*m.b45 + 128*m.b33*m.b36*m.b43*m.b46
                        + 64*m.b33*m.b36*m.b44*m.b47 + 384*m.b33*m.b37*m.b38*m.b42 + 320*m.b33*m.b37*m.b39*m.b43 + 256*
                       m.b33*m.b37*m.b40*m.b44 + 192*m.b33*m.b37*m.b41*m.b45 + 128*m.b33*m.b37*m.b42*m.b46 + 64*m.b33*
                       m.b37*m.b43*m.b47 + 256*m.b33*m.b38*m.b39*m.b44 + 192*m.b33*m.b38*m.b40*m.b45 + 128*m.b33*m.b38*
                       m.b41*m.b46 + 64*m.b33*m.b38*m.b42*m.b47 + 128*m.b33*m.b39*m.b40*m.b46 + 64*m.b33*m.b39*m.b41*
                       m.b47 + 768*m.b34*m.b35*m.b36*m.b37 + 704*m.b34*m.b35*m.b37*m.b38 + 640*m.b34*m.b35*m.b38*m.b39
                        + 576*m.b34*m.b35*m.b39*m.b40 + 512*m.b34*m.b35*m.b40*m.b41 + 448*m.b34*m.b35*m.b41*m.b42 + 384*
                       m.b34*m.b35*m.b42*m.b43 + 320*m.b34*m.b35*m.b43*m.b44 + 256*m.b34*m.b35*m.b44*m.b45 + 192*m.b34*
                       m.b35*m.b45*m.b46 + 128*m.b34*m.b35*m.b46*m.b47 + 64*m.b34*m.b35*m.b47*m.b48 + 640*m.b34*m.b36*
                       m.b37*m.b39 + 576*m.b34*m.b36*m.b38*m.b40 + 512*m.b34*m.b36*m.b39*m.b41 + 448*m.b34*m.b36*m.b40*
                       m.b42 + 384*m.b34*m.b36*m.b41*m.b43 + 320*m.b34*m.b36*m.b42*m.b44 + 256*m.b34*m.b36*m.b43*m.b45
                        + 192*m.b34*m.b36*m.b44*m.b46 + 128*m.b34*m.b36*m.b45*m.b47 + 64*m.b34*m.b36*m.b46*m.b48 + 512*
                       m.b34*m.b37*m.b38*m.b41 + 448*m.b34*m.b37*m.b39*m.b42 + 384*m.b34*m.b37*m.b40*m.b43 + 320*m.b34*
                       m.b37*m.b41*m.b44 + 256*m.b34*m.b37*m.b42*m.b45 + 192*m.b34*m.b37*m.b43*m.b46 + 128*m.b34*m.b37*
                       m.b44*m.b47 + 64*m.b34*m.b37*m.b45*m.b48 + 384*m.b34*m.b38*m.b39*m.b43 + 320*m.b34*m.b38*m.b40*
                       m.b44 + 256*m.b34*m.b38*m.b41*m.b45 + 192*m.b34*m.b38*m.b42*m.b46 + 128*m.b34*m.b38*m.b43*m.b47
                        + 64*m.b34*m.b38*m.b44*m.b48 + 256*m.b34*m.b39*m.b40*m.b45 + 192*m.b34*m.b39*m.b41*m.b46 + 128*
                       m.b34*m.b39*m.b42*m.b47 + 64*m.b34*m.b39*m.b43*m.b48 + 128*m.b34*m.b40*m.b41*m.b47 + 64*m.b34*
                       m.b40*m.b42*m.b48 + 768*m.b35*m.b36*m.b37*m.b38 + 704*m.b35*m.b36*m.b38*m.b39 + 640*m.b35*m.b36*
                       m.b39*m.b40 + 576*m.b35*m.b36*m.b40*m.b41 + 512*m.b35*m.b36*m.b41*m.b42 + 448*m.b35*m.b36*m.b42*
                       m.b43 + 384*m.b35*m.b36*m.b43*m.b44 + 320*m.b35*m.b36*m.b44*m.b45 + 256*m.b35*m.b36*m.b45*m.b46
                        + 192*m.b35*m.b36*m.b46*m.b47 + 128*m.b35*m.b36*m.b47*m.b48 + 64*m.b35*m.b36*m.b48*m.b49 + 640*
                       m.b35*m.b37*m.b38*m.b40 + 576*m.b35*m.b37*m.b39*m.b41 + 512*m.b35*m.b37*m.b40*m.b42 + 448*m.b35*
                       m.b37*m.b41*m.b43 + 384*m.b35*m.b37*m.b42*m.b44 + 320*m.b35*m.b37*m.b43*m.b45 + 256*m.b35*m.b37*
                       m.b44*m.b46 + 192*m.b35*m.b37*m.b45*m.b47 + 128*m.b35*m.b37*m.b46*m.b48 + 64*m.b35*m.b37*m.b47*
                       m.b49 + 512*m.b35*m.b38*m.b39*m.b42 + 448*m.b35*m.b38*m.b40*m.b43 + 384*m.b35*m.b38*m.b41*m.b44
                        + 320*m.b35*m.b38*m.b42*m.b45 + 256*m.b35*m.b38*m.b43*m.b46 + 192*m.b35*m.b38*m.b44*m.b47 + 128*
                       m.b35*m.b38*m.b45*m.b48 + 64*m.b35*m.b38*m.b46*m.b49 + 384*m.b35*m.b39*m.b40*m.b44 + 320*m.b35*
                       m.b39*m.b41*m.b45 + 256*m.b35*m.b39*m.b42*m.b46 + 192*m.b35*m.b39*m.b43*m.b47 + 128*m.b35*m.b39*
                       m.b44*m.b48 + 64*m.b35*m.b39*m.b45*m.b49 + 256*m.b35*m.b40*m.b41*m.b46 + 192*m.b35*m.b40*m.b42*
                       m.b47 + 128*m.b35*m.b40*m.b43*m.b48 + 64*m.b35*m.b40*m.b44*m.b49 + 128*m.b35*m.b41*m.b42*m.b48 + 
                       64*m.b35*m.b41*m.b43*m.b49 + 768*m.b36*m.b37*m.b38*m.b39 + 704*m.b36*m.b37*m.b39*m.b40 + 640*
                       m.b36*m.b37*m.b40*m.b41 + 576*m.b36*m.b37*m.b41*m.b42 + 512*m.b36*m.b37*m.b42*m.b43 + 448*m.b36*
                       m.b37*m.b43*m.b44 + 384*m.b36*m.b37*m.b44*m.b45 + 320*m.b36*m.b37*m.b45*m.b46 + 256*m.b36*m.b37*
                       m.b46*m.b47 + 192*m.b36*m.b37*m.b47*m.b48 + 128*m.b36*m.b37*m.b48*m.b49 + 64*m.b36*m.b37*m.b49*
                       m.b50 + 640*m.b36*m.b38*m.b39*m.b41 + 576*m.b36*m.b38*m.b40*m.b42 + 512*m.b36*m.b38*m.b41*m.b43
                        + 448*m.b36*m.b38*m.b42*m.b44 + 384*m.b36*m.b38*m.b43*m.b45 + 320*m.b36*m.b38*m.b44*m.b46 + 256*
                       m.b36*m.b38*m.b45*m.b47 + 192*m.b36*m.b38*m.b46*m.b48 + 128*m.b36*m.b38*m.b47*m.b49 + 64*m.b36*
                       m.b38*m.b48*m.b50 + 512*m.b36*m.b39*m.b40*m.b43 + 448*m.b36*m.b39*m.b41*m.b44 + 384*m.b36*m.b39*
                       m.b42*m.b45 + 320*m.b36*m.b39*m.b43*m.b46 + 256*m.b36*m.b39*m.b44*m.b47 + 192*m.b36*m.b39*m.b45*
                       m.b48 + 128*m.b36*m.b39*m.b46*m.b49 + 64*m.b36*m.b39*m.b47*m.b50 + 384*m.b36*m.b40*m.b41*m.b45 + 
                       320*m.b36*m.b40*m.b42*m.b46 + 256*m.b36*m.b40*m.b43*m.b47 + 192*m.b36*m.b40*m.b44*m.b48 + 128*
                       m.b36*m.b40*m.b45*m.b49 + 64*m.b36*m.b40*m.b46*m.b50 + 256*m.b36*m.b41*m.b42*m.b47 + 192*m.b36*
                       m.b41*m.b43*m.b48 + 128*m.b36*m.b41*m.b44*m.b49 + 64*m.b36*m.b41*m.b45*m.b50 + 128*m.b36*m.b42*
                       m.b43*m.b49 + 64*m.b36*m.b42*m.b44*m.b50 + 768*m.b37*m.b38*m.b39*m.b40 + 704*m.b37*m.b38*m.b40*
                       m.b41 + 640*m.b37*m.b38*m.b41*m.b42 + 576*m.b37*m.b38*m.b42*m.b43 + 512*m.b37*m.b38*m.b43*m.b44
                        + 448*m.b37*m.b38*m.b44*m.b45 + 384*m.b37*m.b38*m.b45*m.b46 + 320*m.b37*m.b38*m.b46*m.b47 + 256*
                       m.b37*m.b38*m.b47*m.b48 + 192*m.b37*m.b38*m.b48*m.b49 + 128*m.b37*m.b38*m.b49*m.b50 + 64*m.b37*
                       m.b38*m.b50*m.b51 + 640*m.b37*m.b39*m.b40*m.b42 + 576*m.b37*m.b39*m.b41*m.b43 + 512*m.b37*m.b39*
                       m.b42*m.b44 + 448*m.b37*m.b39*m.b43*m.b45 + 384*m.b37*m.b39*m.b44*m.b46 + 320*m.b37*m.b39*m.b45*
                       m.b47 + 256*m.b37*m.b39*m.b46*m.b48 + 192*m.b37*m.b39*m.b47*m.b49 + 128*m.b37*m.b39*m.b48*m.b50
                        + 64*m.b37*m.b39*m.b49*m.b51 + 512*m.b37*m.b40*m.b41*m.b44 + 448*m.b37*m.b40*m.b42*m.b45 + 384*
                       m.b37*m.b40*m.b43*m.b46 + 320*m.b37*m.b40*m.b44*m.b47 + 256*m.b37*m.b40*m.b45*m.b48 + 192*m.b37*
                       m.b40*m.b46*m.b49 + 128*m.b37*m.b40*m.b47*m.b50 + 64*m.b37*m.b40*m.b48*m.b51 + 384*m.b37*m.b41*
                       m.b42*m.b46 + 320*m.b37*m.b41*m.b43*m.b47 + 256*m.b37*m.b41*m.b44*m.b48 + 192*m.b37*m.b41*m.b45*
                       m.b49 + 128*m.b37*m.b41*m.b46*m.b50 + 64*m.b37*m.b41*m.b47*m.b51 + 256*m.b37*m.b42*m.b43*m.b48 + 
                       192*m.b37*m.b42*m.b44*m.b49 + 128*m.b37*m.b42*m.b45*m.b50 + 64*m.b37*m.b42*m.b46*m.b51 + 128*
                       m.b37*m.b43*m.b44*m.b50 + 64*m.b37*m.b43*m.b45*m.b51 + 768*m.b38*m.b39*m.b40*m.b41 + 704*m.b38*
                       m.b39*m.b41*m.b42 + 640*m.b38*m.b39*m.b42*m.b43 + 576*m.b38*m.b39*m.b43*m.b44 + 512*m.b38*m.b39*
                       m.b44*m.b45 + 448*m.b38*m.b39*m.b45*m.b46 + 384*m.b38*m.b39*m.b46*m.b47 + 320*m.b38*m.b39*m.b47*
                       m.b48 + 256*m.b38*m.b39*m.b48*m.b49 + 192*m.b38*m.b39*m.b49*m.b50 + 128*m.b38*m.b39*m.b50*m.b51
                        + 64*m.b38*m.b39*m.b51*m.b52 + 640*m.b38*m.b40*m.b41*m.b43 + 576*m.b38*m.b40*m.b42*m.b44 + 512*
                       m.b38*m.b40*m.b43*m.b45 + 448*m.b38*m.b40*m.b44*m.b46 + 384*m.b38*m.b40*m.b45*m.b47 + 320*m.b38*
                       m.b40*m.b46*m.b48 + 256*m.b38*m.b40*m.b47*m.b49 + 192*m.b38*m.b40*m.b48*m.b50 + 128*m.b38*m.b40*
                       m.b49*m.b51 + 64*m.b38*m.b40*m.b50*m.b52 + 512*m.b38*m.b41*m.b42*m.b45 + 448*m.b38*m.b41*m.b43*
                       m.b46 + 384*m.b38*m.b41*m.b44*m.b47 + 320*m.b38*m.b41*m.b45*m.b48 + 256*m.b38*m.b41*m.b46*m.b49
                        + 192*m.b38*m.b41*m.b47*m.b50 + 128*m.b38*m.b41*m.b48*m.b51 + 64*m.b38*m.b41*m.b49*m.b52 + 384*
                       m.b38*m.b42*m.b43*m.b47 + 320*m.b38*m.b42*m.b44*m.b48 + 256*m.b38*m.b42*m.b45*m.b49 + 192*m.b38*
                       m.b42*m.b46*m.b50 + 128*m.b38*m.b42*m.b47*m.b51 + 64*m.b38*m.b42*m.b48*m.b52 + 256*m.b38*m.b43*
                       m.b44*m.b49 + 192*m.b38*m.b43*m.b45*m.b50 + 128*m.b38*m.b43*m.b46*m.b51 + 64*m.b38*m.b43*m.b47*
                       m.b52 + 128*m.b38*m.b44*m.b45*m.b51 + 64*m.b38*m.b44*m.b46*m.b52 + 768*m.b39*m.b40*m.b41*m.b42 + 
                       704*m.b39*m.b40*m.b42*m.b43 + 640*m.b39*m.b40*m.b43*m.b44 + 576*m.b39*m.b40*m.b44*m.b45 + 512*
                       m.b39*m.b40*m.b45*m.b46 + 448*m.b39*m.b40*m.b46*m.b47 + 384*m.b39*m.b40*m.b47*m.b48 + 320*m.b39*
                       m.b40*m.b48*m.b49 + 256*m.b39*m.b40*m.b49*m.b50 + 192*m.b39*m.b40*m.b50*m.b51 + 128*m.b39*m.b40*
                       m.b51*m.b52 + 64*m.b39*m.b40*m.b52*m.b53 + 640*m.b39*m.b41*m.b42*m.b44 + 576*m.b39*m.b41*m.b43*
                       m.b45 + 512*m.b39*m.b41*m.b44*m.b46 + 448*m.b39*m.b41*m.b45*m.b47 + 384*m.b39*m.b41*m.b46*m.b48
                        + 320*m.b39*m.b41*m.b47*m.b49 + 256*m.b39*m.b41*m.b48*m.b50 + 192*m.b39*m.b41*m.b49*m.b51 + 128*
                       m.b39*m.b41*m.b50*m.b52 + 64*m.b39*m.b41*m.b51*m.b53 + 512*m.b39*m.b42*m.b43*m.b46 + 448*m.b39*
                       m.b42*m.b44*m.b47 + 384*m.b39*m.b42*m.b45*m.b48 + 320*m.b39*m.b42*m.b46*m.b49 + 256*m.b39*m.b42*
                       m.b47*m.b50 + 192*m.b39*m.b42*m.b48*m.b51 + 128*m.b39*m.b42*m.b49*m.b52 + 64*m.b39*m.b42*m.b50*
                       m.b53 + 384*m.b39*m.b43*m.b44*m.b48 + 320*m.b39*m.b43*m.b45*m.b49 + 256*m.b39*m.b43*m.b46*m.b50
                        + 192*m.b39*m.b43*m.b47*m.b51 + 128*m.b39*m.b43*m.b48*m.b52 + 64*m.b39*m.b43*m.b49*m.b53 + 256*
                       m.b39*m.b44*m.b45*m.b50 + 192*m.b39*m.b44*m.b46*m.b51 + 128*m.b39*m.b44*m.b47*m.b52 + 64*m.b39*
                       m.b44*m.b48*m.b53 + 128*m.b39*m.b45*m.b46*m.b52 + 64*m.b39*m.b45*m.b47*m.b53 + 768*m.b40*m.b41*
                       m.b42*m.b43 + 704*m.b40*m.b41*m.b43*m.b44 + 640*m.b40*m.b41*m.b44*m.b45 + 576*m.b40*m.b41*m.b45*
                       m.b46 + 512*m.b40*m.b41*m.b46*m.b47 + 448*m.b40*m.b41*m.b47*m.b48 + 384*m.b40*m.b41*m.b48*m.b49
                        + 320*m.b40*m.b41*m.b49*m.b50 + 256*m.b40*m.b41*m.b50*m.b51 + 192*m.b40*m.b41*m.b51*m.b52 + 128*
                       m.b40*m.b41*m.b52*m.b53 + 64*m.b40*m.b41*m.b53*m.b54 + 640*m.b40*m.b42*m.b43*m.b45 + 576*m.b40*
                       m.b42*m.b44*m.b46 + 512*m.b40*m.b42*m.b45*m.b47 + 448*m.b40*m.b42*m.b46*m.b48 + 384*m.b40*m.b42*
                       m.b47*m.b49 + 320*m.b40*m.b42*m.b48*m.b50 + 256*m.b40*m.b42*m.b49*m.b51 + 192*m.b40*m.b42*m.b50*
                       m.b52 + 128*m.b40*m.b42*m.b51*m.b53 + 64*m.b40*m.b42*m.b52*m.b54 + 512*m.b40*m.b43*m.b44*m.b47 + 
                       448*m.b40*m.b43*m.b45*m.b48 + 384*m.b40*m.b43*m.b46*m.b49 + 320*m.b40*m.b43*m.b47*m.b50 + 256*
                       m.b40*m.b43*m.b48*m.b51 + 192*m.b40*m.b43*m.b49*m.b52 + 128*m.b40*m.b43*m.b50*m.b53 + 64*m.b40*
                       m.b43*m.b51*m.b54 + 384*m.b40*m.b44*m.b45*m.b49 + 320*m.b40*m.b44*m.b46*m.b50 + 256*m.b40*m.b44*
                       m.b47*m.b51 + 192*m.b40*m.b44*m.b48*m.b52 + 128*m.b40*m.b44*m.b49*m.b53 + 64*m.b40*m.b44*m.b50*
                       m.b54 + 256*m.b40*m.b45*m.b46*m.b51 + 192*m.b40*m.b45*m.b47*m.b52 + 128*m.b40*m.b45*m.b48*m.b53
                        + 64*m.b40*m.b45*m.b49*m.b54 + 128*m.b40*m.b46*m.b47*m.b53 + 64*m.b40*m.b46*m.b48*m.b54 + 768*
                       m.b41*m.b42*m.b43*m.b44 + 704*m.b41*m.b42*m.b44*m.b45 + 640*m.b41*m.b42*m.b45*m.b46 + 576*m.b41*
                       m.b42*m.b46*m.b47 + 512*m.b41*m.b42*m.b47*m.b48 + 448*m.b41*m.b42*m.b48*m.b49 + 384*m.b41*m.b42*
                       m.b49*m.b50 + 320*m.b41*m.b42*m.b50*m.b51 + 256*m.b41*m.b42*m.b51*m.b52 + 192*m.b41*m.b42*m.b52*
                       m.b53 + 128*m.b41*m.b42*m.b53*m.b54 + 64*m.b41*m.b42*m.b54*m.b55 + 640*m.b41*m.b43*m.b44*m.b46 + 
                       576*m.b41*m.b43*m.b45*m.b47 + 512*m.b41*m.b43*m.b46*m.b48 + 448*m.b41*m.b43*m.b47*m.b49 + 384*
                       m.b41*m.b43*m.b48*m.b50 + 320*m.b41*m.b43*m.b49*m.b51 + 256*m.b41*m.b43*m.b50*m.b52 + 192*m.b41*
                       m.b43*m.b51*m.b53 + 128*m.b41*m.b43*m.b52*m.b54 + 64*m.b41*m.b43*m.b53*m.b55 + 512*m.b41*m.b44*
                       m.b45*m.b48 + 448*m.b41*m.b44*m.b46*m.b49 + 384*m.b41*m.b44*m.b47*m.b50 + 320*m.b41*m.b44*m.b48*
                       m.b51 + 256*m.b41*m.b44*m.b49*m.b52 + 192*m.b41*m.b44*m.b50*m.b53 + 128*m.b41*m.b44*m.b51*m.b54
                        + 64*m.b41*m.b44*m.b52*m.b55 + 384*m.b41*m.b45*m.b46*m.b50 + 320*m.b41*m.b45*m.b47*m.b51 + 256*
                       m.b41*m.b45*m.b48*m.b52 + 192*m.b41*m.b45*m.b49*m.b53 + 128*m.b41*m.b45*m.b50*m.b54 + 64*m.b41*
                       m.b45*m.b51*m.b55 + 256*m.b41*m.b46*m.b47*m.b52 + 192*m.b41*m.b46*m.b48*m.b53 + 128*m.b41*m.b46*
                       m.b49*m.b54 + 64*m.b41*m.b46*m.b50*m.b55 + 128*m.b41*m.b47*m.b48*m.b54 + 64*m.b41*m.b47*m.b49*
                       m.b55 + 768*m.b42*m.b43*m.b44*m.b45 + 704*m.b42*m.b43*m.b45*m.b46 + 640*m.b42*m.b43*m.b46*m.b47
                        + 576*m.b42*m.b43*m.b47*m.b48 + 512*m.b42*m.b43*m.b48*m.b49 + 448*m.b42*m.b43*m.b49*m.b50 + 384*
                       m.b42*m.b43*m.b50*m.b51 + 320*m.b42*m.b43*m.b51*m.b52 + 256*m.b42*m.b43*m.b52*m.b53 + 192*m.b42*
                       m.b43*m.b53*m.b54 + 128*m.b42*m.b43*m.b54*m.b55 + 64*m.b42*m.b43*m.b55*m.b56 + 640*m.b42*m.b44*
                       m.b45*m.b47 + 576*m.b42*m.b44*m.b46*m.b48 + 512*m.b42*m.b44*m.b47*m.b49 + 448*m.b42*m.b44*m.b48*
                       m.b50 + 384*m.b42*m.b44*m.b49*m.b51 + 320*m.b42*m.b44*m.b50*m.b52 + 256*m.b42*m.b44*m.b51*m.b53
                        + 192*m.b42*m.b44*m.b52*m.b54 + 128*m.b42*m.b44*m.b53*m.b55 + 64*m.b42*m.b44*m.b54*m.b56 + 512*
                       m.b42*m.b45*m.b46*m.b49 + 448*m.b42*m.b45*m.b47*m.b50 + 384*m.b42*m.b45*m.b48*m.b51 + 320*m.b42*
                       m.b45*m.b49*m.b52 + 256*m.b42*m.b45*m.b50*m.b53 + 192*m.b42*m.b45*m.b51*m.b54 + 128*m.b42*m.b45*
                       m.b52*m.b55 + 64*m.b42*m.b45*m.b53*m.b56 + 384*m.b42*m.b46*m.b47*m.b51 + 320*m.b42*m.b46*m.b48*
                       m.b52 + 256*m.b42*m.b46*m.b49*m.b53 + 192*m.b42*m.b46*m.b50*m.b54 + 128*m.b42*m.b46*m.b51*m.b55
                        + 64*m.b42*m.b46*m.b52*m.b56 + 256*m.b42*m.b47*m.b48*m.b53 + 192*m.b42*m.b47*m.b49*m.b54 + 128*
                       m.b42*m.b47*m.b50*m.b55 + 64*m.b42*m.b47*m.b51*m.b56 + 128*m.b42*m.b48*m.b49*m.b55 + 64*m.b42*
                       m.b48*m.b50*m.b56 + 768*m.b43*m.b44*m.b45*m.b46 + 704*m.b43*m.b44*m.b46*m.b47 + 640*m.b43*m.b44*
                       m.b47*m.b48 + 576*m.b43*m.b44*m.b48*m.b49 + 512*m.b43*m.b44*m.b49*m.b50 + 448*m.b43*m.b44*m.b50*
                       m.b51 + 384*m.b43*m.b44*m.b51*m.b52 + 320*m.b43*m.b44*m.b52*m.b53 + 256*m.b43*m.b44*m.b53*m.b54
                        + 192*m.b43*m.b44*m.b54*m.b55 + 128*m.b43*m.b44*m.b55*m.b56 + 64*m.b43*m.b44*m.b56*m.b57 + 640*
                       m.b43*m.b45*m.b46*m.b48 + 576*m.b43*m.b45*m.b47*m.b49 + 512*m.b43*m.b45*m.b48*m.b50 + 448*m.b43*
                       m.b45*m.b49*m.b51 + 384*m.b43*m.b45*m.b50*m.b52 + 320*m.b43*m.b45*m.b51*m.b53 + 256*m.b43*m.b45*
                       m.b52*m.b54 + 192*m.b43*m.b45*m.b53*m.b55 + 128*m.b43*m.b45*m.b54*m.b56 + 64*m.b43*m.b45*m.b55*
                       m.b57 + 512*m.b43*m.b46*m.b47*m.b50 + 448*m.b43*m.b46*m.b48*m.b51 + 384*m.b43*m.b46*m.b49*m.b52
                        + 320*m.b43*m.b46*m.b50*m.b53 + 256*m.b43*m.b46*m.b51*m.b54 + 192*m.b43*m.b46*m.b52*m.b55 + 128*
                       m.b43*m.b46*m.b53*m.b56 + 64*m.b43*m.b46*m.b54*m.b57 + 384*m.b43*m.b47*m.b48*m.b52 + 320*m.b43*
                       m.b47*m.b49*m.b53 + 256*m.b43*m.b47*m.b50*m.b54 + 192*m.b43*m.b47*m.b51*m.b55 + 128*m.b43*m.b47*
                       m.b52*m.b56 + 64*m.b43*m.b47*m.b53*m.b57 + 256*m.b43*m.b48*m.b49*m.b54 + 192*m.b43*m.b48*m.b50*
                       m.b55 + 128*m.b43*m.b48*m.b51*m.b56 + 64*m.b43*m.b48*m.b52*m.b57 + 128*m.b43*m.b49*m.b50*m.b56 + 
                       64*m.b43*m.b49*m.b51*m.b57 + 768*m.b44*m.b45*m.b46*m.b47 + 704*m.b44*m.b45*m.b47*m.b48 + 640*
                       m.b44*m.b45*m.b48*m.b49 + 576*m.b44*m.b45*m.b49*m.b50 + 512*m.b44*m.b45*m.b50*m.b51 + 448*m.b44*
                       m.b45*m.b51*m.b52 + 384*m.b44*m.b45*m.b52*m.b53 + 320*m.b44*m.b45*m.b53*m.b54 + 256*m.b44*m.b45*
                       m.b54*m.b55 + 192*m.b44*m.b45*m.b55*m.b56 + 128*m.b44*m.b45*m.b56*m.b57 + 64*m.b44*m.b45*m.b57*
                       m.b58 + 640*m.b44*m.b46*m.b47*m.b49 + 576*m.b44*m.b46*m.b48*m.b50 + 512*m.b44*m.b46*m.b49*m.b51
                        + 448*m.b44*m.b46*m.b50*m.b52 + 384*m.b44*m.b46*m.b51*m.b53 + 320*m.b44*m.b46*m.b52*m.b54 + 256*
                       m.b44*m.b46*m.b53*m.b55 + 192*m.b44*m.b46*m.b54*m.b56 + 128*m.b44*m.b46*m.b55*m.b57 + 64*m.b44*
                       m.b46*m.b56*m.b58 + 512*m.b44*m.b47*m.b48*m.b51 + 448*m.b44*m.b47*m.b49*m.b52 + 384*m.b44*m.b47*
                       m.b50*m.b53 + 320*m.b44*m.b47*m.b51*m.b54 + 256*m.b44*m.b47*m.b52*m.b55 + 192*m.b44*m.b47*m.b53*
                       m.b56 + 128*m.b44*m.b47*m.b54*m.b57 + 64*m.b44*m.b47*m.b55*m.b58 + 384*m.b44*m.b48*m.b49*m.b53 + 
                       320*m.b44*m.b48*m.b50*m.b54 + 256*m.b44*m.b48*m.b51*m.b55 + 192*m.b44*m.b48*m.b52*m.b56 + 128*
                       m.b44*m.b48*m.b53*m.b57 + 64*m.b44*m.b48*m.b54*m.b58 + 256*m.b44*m.b49*m.b50*m.b55 + 192*m.b44*
                       m.b49*m.b51*m.b56 + 128*m.b44*m.b49*m.b52*m.b57 + 64*m.b44*m.b49*m.b53*m.b58 + 128*m.b44*m.b50*
                       m.b51*m.b57 + 64*m.b44*m.b50*m.b52*m.b58 + 768*m.b45*m.b46*m.b47*m.b48 + 704*m.b45*m.b46*m.b48*
                       m.b49 + 640*m.b45*m.b46*m.b49*m.b50 + 576*m.b45*m.b46*m.b50*m.b51 + 512*m.b45*m.b46*m.b51*m.b52
                        + 448*m.b45*m.b46*m.b52*m.b53 + 384*m.b45*m.b46*m.b53*m.b54 + 320*m.b45*m.b46*m.b54*m.b55 + 256*
                       m.b45*m.b46*m.b55*m.b56 + 192*m.b45*m.b46*m.b56*m.b57 + 128*m.b45*m.b46*m.b57*m.b58 + 64*m.b45*
                       m.b46*m.b58*m.b59 + 640*m.b45*m.b47*m.b48*m.b50 + 576*m.b45*m.b47*m.b49*m.b51 + 512*m.b45*m.b47*
                       m.b50*m.b52 + 448*m.b45*m.b47*m.b51*m.b53 + 384*m.b45*m.b47*m.b52*m.b54 + 320*m.b45*m.b47*m.b53*
                       m.b55 + 256*m.b45*m.b47*m.b54*m.b56 + 192*m.b45*m.b47*m.b55*m.b57 + 128*m.b45*m.b47*m.b56*m.b58
                        + 64*m.b45*m.b47*m.b57*m.b59 + 512*m.b45*m.b48*m.b49*m.b52 + 448*m.b45*m.b48*m.b50*m.b53 + 384*
                       m.b45*m.b48*m.b51*m.b54 + 320*m.b45*m.b48*m.b52*m.b55 + 256*m.b45*m.b48*m.b53*m.b56 + 192*m.b45*
                       m.b48*m.b54*m.b57 + 128*m.b45*m.b48*m.b55*m.b58 + 64*m.b45*m.b48*m.b56*m.b59 + 384*m.b45*m.b49*
                       m.b50*m.b54 + 320*m.b45*m.b49*m.b51*m.b55 + 256*m.b45*m.b49*m.b52*m.b56 + 192*m.b45*m.b49*m.b53*
                       m.b57 + 128*m.b45*m.b49*m.b54*m.b58 + 64*m.b45*m.b49*m.b55*m.b59 + 256*m.b45*m.b50*m.b51*m.b56 + 
                       192*m.b45*m.b50*m.b52*m.b57 + 128*m.b45*m.b50*m.b53*m.b58 + 64*m.b45*m.b50*m.b54*m.b59 + 128*
                       m.b45*m.b51*m.b52*m.b58 + 64*m.b45*m.b51*m.b53*m.b59 + 768*m.b46*m.b47*m.b48*m.b49 + 704*m.b46*
                       m.b47*m.b49*m.b50 + 640*m.b46*m.b47*m.b50*m.b51 + 576*m.b46*m.b47*m.b51*m.b52 + 512*m.b46*m.b47*
                       m.b52*m.b53 + 448*m.b46*m.b47*m.b53*m.b54 + 384*m.b46*m.b47*m.b54*m.b55 + 320*m.b46*m.b47*m.b55*
                       m.b56 + 256*m.b46*m.b47*m.b56*m.b57 + 192*m.b46*m.b47*m.b57*m.b58 + 128*m.b46*m.b47*m.b58*m.b59
                        + 64*m.b46*m.b47*m.b59*m.b60 + 640*m.b46*m.b48*m.b49*m.b51 + 576*m.b46*m.b48*m.b50*m.b52 + 512*
                       m.b46*m.b48*m.b51*m.b53 + 448*m.b46*m.b48*m.b52*m.b54 + 384*m.b46*m.b48*m.b53*m.b55 + 320*m.b46*
                       m.b48*m.b54*m.b56 + 256*m.b46*m.b48*m.b55*m.b57 + 192*m.b46*m.b48*m.b56*m.b58 + 128*m.b46*m.b48*
                       m.b57*m.b59 + 64*m.b46*m.b48*m.b58*m.b60 + 512*m.b46*m.b49*m.b50*m.b53 + 448*m.b46*m.b49*m.b51*
                       m.b54 + 384*m.b46*m.b49*m.b52*m.b55 + 320*m.b46*m.b49*m.b53*m.b56 + 256*m.b46*m.b49*m.b54*m.b57
                        + 192*m.b46*m.b49*m.b55*m.b58 + 128*m.b46*m.b49*m.b56*m.b59 + 64*m.b46*m.b49*m.b57*m.b60 + 384*
                       m.b46*m.b50*m.b51*m.b55 + 320*m.b46*m.b50*m.b52*m.b56 + 256*m.b46*m.b50*m.b53*m.b57 + 192*m.b46*
                       m.b50*m.b54*m.b58 + 128*m.b46*m.b50*m.b55*m.b59 + 64*m.b46*m.b50*m.b56*m.b60 + 256*m.b46*m.b51*
                       m.b52*m.b57 + 192*m.b46*m.b51*m.b53*m.b58 + 128*m.b46*m.b51*m.b54*m.b59 + 64*m.b46*m.b51*m.b55*
                       m.b60 + 128*m.b46*m.b52*m.b53*m.b59 + 64*m.b46*m.b52*m.b54*m.b60 + 704*m.b47*m.b48*m.b49*m.b50 + 
                       640*m.b47*m.b48*m.b50*m.b51 + 576*m.b47*m.b48*m.b51*m.b52 + 512*m.b47*m.b48*m.b52*m.b53 + 448*
                       m.b47*m.b48*m.b53*m.b54 + 384*m.b47*m.b48*m.b54*m.b55 + 320*m.b47*m.b48*m.b55*m.b56 + 256*m.b47*
                       m.b48*m.b56*m.b57 + 192*m.b47*m.b48*m.b57*m.b58 + 128*m.b47*m.b48*m.b58*m.b59 + 64*m.b47*m.b48*
                       m.b59*m.b60 + 576*m.b47*m.b49*m.b50*m.b52 + 512*m.b47*m.b49*m.b51*m.b53 + 448*m.b47*m.b49*m.b52*
                       m.b54 + 384*m.b47*m.b49*m.b53*m.b55 + 320*m.b47*m.b49*m.b54*m.b56 + 256*m.b47*m.b49*m.b55*m.b57
                        + 192*m.b47*m.b49*m.b56*m.b58 + 128*m.b47*m.b49*m.b57*m.b59 + 64*m.b47*m.b49*m.b58*m.b60 + 448*
                       m.b47*m.b50*m.b51*m.b54 + 384*m.b47*m.b50*m.b52*m.b55 + 320*m.b47*m.b50*m.b53*m.b56 + 256*m.b47*
                       m.b50*m.b54*m.b57 + 192*m.b47*m.b50*m.b55*m.b58 + 128*m.b47*m.b50*m.b56*m.b59 + 64*m.b47*m.b50*
                       m.b57*m.b60 + 320*m.b47*m.b51*m.b52*m.b56 + 256*m.b47*m.b51*m.b53*m.b57 + 192*m.b47*m.b51*m.b54*
                       m.b58 + 128*m.b47*m.b51*m.b55*m.b59 + 64*m.b47*m.b51*m.b56*m.b60 + 192*m.b47*m.b52*m.b53*m.b58 + 
                       128*m.b47*m.b52*m.b54*m.b59 + 64*m.b47*m.b52*m.b55*m.b60 + 64*m.b47*m.b53*m.b54*m.b60 + 640*m.b48
                       *m.b49*m.b50*m.b51 + 576*m.b48*m.b49*m.b51*m.b52 + 512*m.b48*m.b49*m.b52*m.b53 + 448*m.b48*m.b49*
                       m.b53*m.b54 + 384*m.b48*m.b49*m.b54*m.b55 + 320*m.b48*m.b49*m.b55*m.b56 + 256*m.b48*m.b49*m.b56*
                       m.b57 + 192*m.b48*m.b49*m.b57*m.b58 + 128*m.b48*m.b49*m.b58*m.b59 + 64*m.b48*m.b49*m.b59*m.b60 + 
                       512*m.b48*m.b50*m.b51*m.b53 + 448*m.b48*m.b50*m.b52*m.b54 + 384*m.b48*m.b50*m.b53*m.b55 + 320*
                       m.b48*m.b50*m.b54*m.b56 + 256*m.b48*m.b50*m.b55*m.b57 + 192*m.b48*m.b50*m.b56*m.b58 + 128*m.b48*
                       m.b50*m.b57*m.b59 + 64*m.b48*m.b50*m.b58*m.b60 + 384*m.b48*m.b51*m.b52*m.b55 + 320*m.b48*m.b51*
                       m.b53*m.b56 + 256*m.b48*m.b51*m.b54*m.b57 + 192*m.b48*m.b51*m.b55*m.b58 + 128*m.b48*m.b51*m.b56*
                       m.b59 + 64*m.b48*m.b51*m.b57*m.b60 + 256*m.b48*m.b52*m.b53*m.b57 + 192*m.b48*m.b52*m.b54*m.b58 + 
                       128*m.b48*m.b52*m.b55*m.b59 + 64*m.b48*m.b52*m.b56*m.b60 + 128*m.b48*m.b53*m.b54*m.b59 + 64*m.b48
                       *m.b53*m.b55*m.b60 + 576*m.b49*m.b50*m.b51*m.b52 + 512*m.b49*m.b50*m.b52*m.b53 + 448*m.b49*m.b50*
                       m.b53*m.b54 + 384*m.b49*m.b50*m.b54*m.b55 + 320*m.b49*m.b50*m.b55*m.b56 + 256*m.b49*m.b50*m.b56*
                       m.b57 + 192*m.b49*m.b50*m.b57*m.b58 + 128*m.b49*m.b50*m.b58*m.b59 + 64*m.b49*m.b50*m.b59*m.b60 + 
                       448*m.b49*m.b51*m.b52*m.b54 + 384*m.b49*m.b51*m.b53*m.b55 + 320*m.b49*m.b51*m.b54*m.b56 + 256*
                       m.b49*m.b51*m.b55*m.b57 + 192*m.b49*m.b51*m.b56*m.b58 + 128*m.b49*m.b51*m.b57*m.b59 + 64*m.b49*
                       m.b51*m.b58*m.b60 + 320*m.b49*m.b52*m.b53*m.b56 + 256*m.b49*m.b52*m.b54*m.b57 + 192*m.b49*m.b52*
                       m.b55*m.b58 + 128*m.b49*m.b52*m.b56*m.b59 + 64*m.b49*m.b52*m.b57*m.b60 + 192*m.b49*m.b53*m.b54*
                       m.b58 + 128*m.b49*m.b53*m.b55*m.b59 + 64*m.b49*m.b53*m.b56*m.b60 + 64*m.b49*m.b54*m.b55*m.b60 + 
                       512*m.b50*m.b51*m.b52*m.b53 + 448*m.b50*m.b51*m.b53*m.b54 + 384*m.b50*m.b51*m.b54*m.b55 + 320*
                       m.b50*m.b51*m.b55*m.b56 + 256*m.b50*m.b51*m.b56*m.b57 + 192*m.b50*m.b51*m.b57*m.b58 + 128*m.b50*
                       m.b51*m.b58*m.b59 + 64*m.b50*m.b51*m.b59*m.b60 + 384*m.b50*m.b52*m.b53*m.b55 + 320*m.b50*m.b52*
                       m.b54*m.b56 + 256*m.b50*m.b52*m.b55*m.b57 + 192*m.b50*m.b52*m.b56*m.b58 + 128*m.b50*m.b52*m.b57*
                       m.b59 + 64*m.b50*m.b52*m.b58*m.b60 + 256*m.b50*m.b53*m.b54*m.b57 + 192*m.b50*m.b53*m.b55*m.b58 + 
                       128*m.b50*m.b53*m.b56*m.b59 + 64*m.b50*m.b53*m.b57*m.b60 + 128*m.b50*m.b54*m.b55*m.b59 + 64*m.b50
                       *m.b54*m.b56*m.b60 + 448*m.b51*m.b52*m.b53*m.b54 + 384*m.b51*m.b52*m.b54*m.b55 + 320*m.b51*m.b52*
                       m.b55*m.b56 + 256*m.b51*m.b52*m.b56*m.b57 + 192*m.b51*m.b52*m.b57*m.b58 + 128*m.b51*m.b52*m.b58*
                       m.b59 + 64*m.b51*m.b52*m.b59*m.b60 + 320*m.b51*m.b53*m.b54*m.b56 + 256*m.b51*m.b53*m.b55*m.b57 + 
                       192*m.b51*m.b53*m.b56*m.b58 + 128*m.b51*m.b53*m.b57*m.b59 + 64*m.b51*m.b53*m.b58*m.b60 + 192*
                       m.b51*m.b54*m.b55*m.b58 + 128*m.b51*m.b54*m.b56*m.b59 + 64*m.b51*m.b54*m.b57*m.b60 + 64*m.b51*
                       m.b55*m.b56*m.b60 + 384*m.b52*m.b53*m.b54*m.b55 + 320*m.b52*m.b53*m.b55*m.b56 + 256*m.b52*m.b53*
                       m.b56*m.b57 + 192*m.b52*m.b53*m.b57*m.b58 + 128*m.b52*m.b53*m.b58*m.b59 + 64*m.b52*m.b53*m.b59*
                       m.b60 + 256*m.b52*m.b54*m.b55*m.b57 + 192*m.b52*m.b54*m.b56*m.b58 + 128*m.b52*m.b54*m.b57*m.b59
                        + 64*m.b52*m.b54*m.b58*m.b60 + 128*m.b52*m.b55*m.b56*m.b59 + 64*m.b52*m.b55*m.b57*m.b60 + 320*
                       m.b53*m.b54*m.b55*m.b56 + 256*m.b53*m.b54*m.b56*m.b57 + 192*m.b53*m.b54*m.b57*m.b58 + 128*m.b53*
                       m.b54*m.b58*m.b59 + 64*m.b53*m.b54*m.b59*m.b60 + 192*m.b53*m.b55*m.b56*m.b58 + 128*m.b53*m.b55*
                       m.b57*m.b59 + 64*m.b53*m.b55*m.b58*m.b60 + 64*m.b53*m.b56*m.b57*m.b60 + 256*m.b54*m.b55*m.b56*
                       m.b57 + 192*m.b54*m.b55*m.b57*m.b58 + 128*m.b54*m.b55*m.b58*m.b59 + 64*m.b54*m.b55*m.b59*m.b60 + 
                       128*m.b54*m.b56*m.b57*m.b59 + 64*m.b54*m.b56*m.b58*m.b60 + 192*m.b55*m.b56*m.b57*m.b58 + 128*
                       m.b55*m.b56*m.b58*m.b59 + 64*m.b55*m.b56*m.b59*m.b60 + 64*m.b55*m.b57*m.b58*m.b60 + 128*m.b56*
                       m.b57*m.b58*m.b59 + 64*m.b56*m.b57*m.b59*m.b60 + 64*m.b57*m.b58*m.b59*m.b60 - 32*m.b1*m.b2*m.b3
                        - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 64*m.b1*m.b2*m.b6 - 64*m.b1*m.b2*m.b7 - 64*m.b1*m.b2*
                       m.b8 - 64*m.b1*m.b2*m.b9 - 64*m.b1*m.b2*m.b10 - 64*m.b1*m.b2*m.b11 - 64*m.b1*m.b2*m.b12 - 64*m.b1
                       *m.b2*m.b13 - 64*m.b1*m.b2*m.b14 - 32*m.b1*m.b2*m.b15 - 64*m.b1*m.b3*m.b4 - 32*m.b1*m.b3*m.b5 - 
                       64*m.b1*m.b3*m.b6 - 64*m.b1*m.b3*m.b7 - 64*m.b1*m.b3*m.b8 - 64*m.b1*m.b3*m.b9 - 64*m.b1*m.b3*
                       m.b10 - 64*m.b1*m.b3*m.b11 - 64*m.b1*m.b3*m.b12 - 64*m.b1*m.b3*m.b13 - 32*m.b1*m.b3*m.b14 - 32*
                       m.b1*m.b3*m.b15 - 64*m.b1*m.b4*m.b5 - 64*m.b1*m.b4*m.b6 - 32*m.b1*m.b4*m.b7 - 64*m.b1*m.b4*m.b8
                        - 64*m.b1*m.b4*m.b9 - 64*m.b1*m.b4*m.b10 - 64*m.b1*m.b4*m.b11 - 64*m.b1*m.b4*m.b12 - 32*m.b1*
                       m.b4*m.b13 - 32*m.b1*m.b4*m.b14 - 32*m.b1*m.b4*m.b15 - 64*m.b1*m.b5*m.b6 - 64*m.b1*m.b5*m.b7 - 64
                       *m.b1*m.b5*m.b8 - 32*m.b1*m.b5*m.b9 - 64*m.b1*m.b5*m.b10 - 64*m.b1*m.b5*m.b11 - 32*m.b1*m.b5*
                       m.b12 - 32*m.b1*m.b5*m.b13 - 32*m.b1*m.b5*m.b14 - 32*m.b1*m.b5*m.b15 - 64*m.b1*m.b6*m.b7 - 64*
                       m.b1*m.b6*m.b8 - 64*m.b1*m.b6*m.b9 - 64*m.b1*m.b6*m.b10 - 32*m.b1*m.b6*m.b12 - 32*m.b1*m.b6*m.b13
                        - 32*m.b1*m.b6*m.b14 - 32*m.b1*m.b6*m.b15 - 64*m.b1*m.b7*m.b8 - 64*m.b1*m.b7*m.b9 - 32*m.b1*m.b7
                       *m.b10 - 32*m.b1*m.b7*m.b11 - 32*m.b1*m.b7*m.b12 - 32*m.b1*m.b7*m.b14 - 32*m.b1*m.b7*m.b15 - 32*
                       m.b1*m.b8*m.b9 - 32*m.b1*m.b8*m.b10 - 32*m.b1*m.b8*m.b11 - 32*m.b1*m.b8*m.b12 - 32*m.b1*m.b8*
                       m.b13 - 32*m.b1*m.b8*m.b14 - 32*m.b1*m.b9*m.b10 - 32*m.b1*m.b9*m.b11 - 32*m.b1*m.b9*m.b12 - 32*
                       m.b1*m.b9*m.b13 - 32*m.b1*m.b9*m.b14 - 32*m.b1*m.b9*m.b15 - 32*m.b1*m.b10*m.b11 - 32*m.b1*m.b10*
                       m.b12 - 32*m.b1*m.b10*m.b13 - 32*m.b1*m.b10*m.b14 - 32*m.b1*m.b10*m.b15 - 32*m.b1*m.b11*m.b12 - 
                       32*m.b1*m.b11*m.b13 - 32*m.b1*m.b11*m.b14 - 32*m.b1*m.b11*m.b15 - 32*m.b1*m.b12*m.b13 - 32*m.b1*
                       m.b12*m.b14 - 32*m.b1*m.b12*m.b15 - 32*m.b1*m.b13*m.b14 - 32*m.b1*m.b13*m.b15 - 32*m.b1*m.b14*
                       m.b15 - 96*m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 128*m.b2*m.b3*m.b6 - 128*m.b2*m.b3*m.b7 - 128*
                       m.b2*m.b3*m.b8 - 128*m.b2*m.b3*m.b9 - 128*m.b2*m.b3*m.b10 - 128*m.b2*m.b3*m.b11 - 128*m.b2*m.b3*
                       m.b12 - 128*m.b2*m.b3*m.b13 - 128*m.b2*m.b3*m.b14 - 96*m.b2*m.b3*m.b15 - 32*m.b2*m.b3*m.b16 - 160
                       *m.b2*m.b4*m.b5 - 64*m.b2*m.b4*m.b6 - 128*m.b2*m.b4*m.b7 - 128*m.b2*m.b4*m.b8 - 128*m.b2*m.b4*
                       m.b9 - 128*m.b2*m.b4*m.b10 - 128*m.b2*m.b4*m.b11 - 128*m.b2*m.b4*m.b12 - 128*m.b2*m.b4*m.b13 - 96
                       *m.b2*m.b4*m.b14 - 64*m.b2*m.b4*m.b15 - 32*m.b2*m.b4*m.b16 - 160*m.b2*m.b5*m.b6 - 128*m.b2*m.b5*
                       m.b7 - 64*m.b2*m.b5*m.b8 - 128*m.b2*m.b5*m.b9 - 128*m.b2*m.b5*m.b10 - 128*m.b2*m.b5*m.b11 - 128*
                       m.b2*m.b5*m.b12 - 96*m.b2*m.b5*m.b13 - 64*m.b2*m.b5*m.b14 - 64*m.b2*m.b5*m.b15 - 32*m.b2*m.b5*
                       m.b16 - 160*m.b2*m.b6*m.b7 - 128*m.b2*m.b6*m.b8 - 128*m.b2*m.b6*m.b9 - 64*m.b2*m.b6*m.b10 - 128*
                       m.b2*m.b6*m.b11 - 96*m.b2*m.b6*m.b12 - 64*m.b2*m.b6*m.b13 - 64*m.b2*m.b6*m.b14 - 64*m.b2*m.b6*
                       m.b15 - 32*m.b2*m.b6*m.b16 - 160*m.b2*m.b7*m.b8 - 128*m.b2*m.b7*m.b9 - 128*m.b2*m.b7*m.b10 - 96*
                       m.b2*m.b7*m.b11 - 64*m.b2*m.b7*m.b13 - 64*m.b2*m.b7*m.b14 - 64*m.b2*m.b7*m.b15 - 32*m.b2*m.b7*
                       m.b16 - 160*m.b2*m.b8*m.b9 - 96*m.b2*m.b8*m.b10 - 64*m.b2*m.b8*m.b11 - 64*m.b2*m.b8*m.b12 - 64*
                       m.b2*m.b8*m.b13 - 64*m.b2*m.b8*m.b15 - 32*m.b2*m.b8*m.b16 - 96*m.b2*m.b9*m.b10 - 64*m.b2*m.b9*
                       m.b11 - 64*m.b2*m.b9*m.b12 - 64*m.b2*m.b9*m.b13 - 64*m.b2*m.b9*m.b14 - 64*m.b2*m.b9*m.b15 - 96*
                       m.b2*m.b10*m.b11 - 64*m.b2*m.b10*m.b12 - 64*m.b2*m.b10*m.b13 - 64*m.b2*m.b10*m.b14 - 64*m.b2*
                       m.b10*m.b15 - 32*m.b2*m.b10*m.b16 - 96*m.b2*m.b11*m.b12 - 64*m.b2*m.b11*m.b13 - 64*m.b2*m.b11*
                       m.b14 - 64*m.b2*m.b11*m.b15 - 32*m.b2*m.b11*m.b16 - 96*m.b2*m.b12*m.b13 - 64*m.b2*m.b12*m.b14 - 
                       64*m.b2*m.b12*m.b15 - 32*m.b2*m.b12*m.b16 - 96*m.b2*m.b13*m.b14 - 64*m.b2*m.b13*m.b15 - 32*m.b2*
                       m.b13*m.b16 - 96*m.b2*m.b14*m.b15 - 32*m.b2*m.b14*m.b16 - 32*m.b2*m.b15*m.b16 - 160*m.b3*m.b4*
                       m.b5 - 224*m.b3*m.b4*m.b6 - 192*m.b3*m.b4*m.b7 - 192*m.b3*m.b4*m.b8 - 192*m.b3*m.b4*m.b9 - 192*
                       m.b3*m.b4*m.b10 - 192*m.b3*m.b4*m.b11 - 192*m.b3*m.b4*m.b12 - 192*m.b3*m.b4*m.b13 - 192*m.b3*m.b4
                       *m.b14 - 160*m.b3*m.b4*m.b15 - 96*m.b3*m.b4*m.b16 - 32*m.b3*m.b4*m.b17 - 256*m.b3*m.b5*m.b6 - 128
                       *m.b3*m.b5*m.b7 - 192*m.b3*m.b5*m.b8 - 192*m.b3*m.b5*m.b9 - 192*m.b3*m.b5*m.b10 - 192*m.b3*m.b5*
                       m.b11 - 192*m.b3*m.b5*m.b12 - 192*m.b3*m.b5*m.b13 - 160*m.b3*m.b5*m.b14 - 128*m.b3*m.b5*m.b15 - 
                       64*m.b3*m.b5*m.b16 - 32*m.b3*m.b5*m.b17 - 256*m.b3*m.b6*m.b7 - 224*m.b3*m.b6*m.b8 - 96*m.b3*m.b6*
                       m.b9 - 192*m.b3*m.b6*m.b10 - 192*m.b3*m.b6*m.b11 - 192*m.b3*m.b6*m.b12 - 160*m.b3*m.b6*m.b13 - 
                       128*m.b3*m.b6*m.b14 - 96*m.b3*m.b6*m.b15 - 64*m.b3*m.b6*m.b16 - 32*m.b3*m.b6*m.b17 - 256*m.b3*
                       m.b7*m.b8 - 224*m.b3*m.b7*m.b9 - 192*m.b3*m.b7*m.b10 - 96*m.b3*m.b7*m.b11 - 160*m.b3*m.b7*m.b12
                        - 128*m.b3*m.b7*m.b13 - 96*m.b3*m.b7*m.b14 - 96*m.b3*m.b7*m.b15 - 64*m.b3*m.b7*m.b16 - 32*m.b3*
                       m.b7*m.b17 - 256*m.b3*m.b8*m.b9 - 224*m.b3*m.b8*m.b10 - 160*m.b3*m.b8*m.b11 - 128*m.b3*m.b8*m.b12
                        - 96*m.b3*m.b8*m.b14 - 96*m.b3*m.b8*m.b15 - 64*m.b3*m.b8*m.b16 - 32*m.b3*m.b8*m.b17 - 224*m.b3*
                       m.b9*m.b10 - 160*m.b3*m.b9*m.b11 - 96*m.b3*m.b9*m.b12 - 96*m.b3*m.b9*m.b13 - 96*m.b3*m.b9*m.b14
                        - 64*m.b3*m.b9*m.b16 - 32*m.b3*m.b9*m.b17 - 160*m.b3*m.b10*m.b11 - 128*m.b3*m.b10*m.b12 - 96*
                       m.b3*m.b10*m.b13 - 96*m.b3*m.b10*m.b14 - 96*m.b3*m.b10*m.b15 - 64*m.b3*m.b10*m.b16 - 160*m.b3*
                       m.b11*m.b12 - 128*m.b3*m.b11*m.b13 - 96*m.b3*m.b11*m.b14 - 96*m.b3*m.b11*m.b15 - 64*m.b3*m.b11*
                       m.b16 - 32*m.b3*m.b11*m.b17 - 160*m.b3*m.b12*m.b13 - 128*m.b3*m.b12*m.b14 - 96*m.b3*m.b12*m.b15
                        - 64*m.b3*m.b12*m.b16 - 32*m.b3*m.b12*m.b17 - 160*m.b3*m.b13*m.b14 - 128*m.b3*m.b13*m.b15 - 64*
                       m.b3*m.b13*m.b16 - 32*m.b3*m.b13*m.b17 - 160*m.b3*m.b14*m.b15 - 64*m.b3*m.b14*m.b16 - 32*m.b3*
                       m.b14*m.b17 - 96*m.b3*m.b15*m.b16 - 32*m.b3*m.b15*m.b17 - 32*m.b3*m.b16*m.b17 - 224*m.b4*m.b5*
                       m.b6 - 320*m.b4*m.b5*m.b7 - 288*m.b4*m.b5*m.b8 - 256*m.b4*m.b5*m.b9 - 256*m.b4*m.b5*m.b10 - 256*
                       m.b4*m.b5*m.b11 - 256*m.b4*m.b5*m.b12 - 256*m.b4*m.b5*m.b13 - 256*m.b4*m.b5*m.b14 - 224*m.b4*m.b5
                       *m.b15 - 160*m.b4*m.b5*m.b16 - 96*m.b4*m.b5*m.b17 - 32*m.b4*m.b5*m.b18 - 352*m.b4*m.b6*m.b7 - 192
                       *m.b4*m.b6*m.b8 - 288*m.b4*m.b6*m.b9 - 256*m.b4*m.b6*m.b10 - 256*m.b4*m.b6*m.b11 - 256*m.b4*m.b6*
                       m.b12 - 256*m.b4*m.b6*m.b13 - 224*m.b4*m.b6*m.b14 - 192*m.b4*m.b6*m.b15 - 128*m.b4*m.b6*m.b16 - 
                       64*m.b4*m.b6*m.b17 - 32*m.b4*m.b6*m.b18 - 352*m.b4*m.b7*m.b8 - 320*m.b4*m.b7*m.b9 - 160*m.b4*m.b7
                       *m.b10 - 256*m.b4*m.b7*m.b11 - 256*m.b4*m.b7*m.b12 - 224*m.b4*m.b7*m.b13 - 192*m.b4*m.b7*m.b14 - 
                       160*m.b4*m.b7*m.b15 - 96*m.b4*m.b7*m.b16 - 64*m.b4*m.b7*m.b17 - 32*m.b4*m.b7*m.b18 - 352*m.b4*
                       m.b8*m.b9 - 320*m.b4*m.b8*m.b10 - 288*m.b4*m.b8*m.b11 - 96*m.b4*m.b8*m.b12 - 192*m.b4*m.b8*m.b13
                        - 160*m.b4*m.b8*m.b14 - 128*m.b4*m.b8*m.b15 - 96*m.b4*m.b8*m.b16 - 64*m.b4*m.b8*m.b17 - 32*m.b4*
                       m.b8*m.b18 - 352*m.b4*m.b9*m.b10 - 288*m.b4*m.b9*m.b11 - 224*m.b4*m.b9*m.b12 - 160*m.b4*m.b9*
                       m.b13 - 128*m.b4*m.b9*m.b15 - 96*m.b4*m.b9*m.b16 - 64*m.b4*m.b9*m.b17 - 32*m.b4*m.b9*m.b18 - 288*
                       m.b4*m.b10*m.b11 - 224*m.b4*m.b10*m.b12 - 160*m.b4*m.b10*m.b13 - 128*m.b4*m.b10*m.b14 - 128*m.b4*
                       m.b10*m.b15 - 64*m.b4*m.b10*m.b17 - 32*m.b4*m.b10*m.b18 - 224*m.b4*m.b11*m.b12 - 192*m.b4*m.b11*
                       m.b13 - 160*m.b4*m.b11*m.b14 - 128*m.b4*m.b11*m.b15 - 96*m.b4*m.b11*m.b16 - 64*m.b4*m.b11*m.b17
                        - 224*m.b4*m.b12*m.b13 - 192*m.b4*m.b12*m.b14 - 160*m.b4*m.b12*m.b15 - 96*m.b4*m.b12*m.b16 - 64*
                       m.b4*m.b12*m.b17 - 32*m.b4*m.b12*m.b18 - 224*m.b4*m.b13*m.b14 - 192*m.b4*m.b13*m.b15 - 96*m.b4*
                       m.b13*m.b16 - 64*m.b4*m.b13*m.b17 - 32*m.b4*m.b13*m.b18 - 224*m.b4*m.b14*m.b15 - 128*m.b4*m.b14*
                       m.b16 - 64*m.b4*m.b14*m.b17 - 32*m.b4*m.b14*m.b18 - 160*m.b4*m.b15*m.b16 - 64*m.b4*m.b15*m.b17 - 
                       32*m.b4*m.b15*m.b18 - 96*m.b4*m.b16*m.b17 - 32*m.b4*m.b16*m.b18 - 32*m.b4*m.b17*m.b18 - 288*m.b5*
                       m.b6*m.b7 - 416*m.b5*m.b6*m.b8 - 384*m.b5*m.b6*m.b9 - 352*m.b5*m.b6*m.b10 - 320*m.b5*m.b6*m.b11
                        - 320*m.b5*m.b6*m.b12 - 320*m.b5*m.b6*m.b13 - 320*m.b5*m.b6*m.b14 - 288*m.b5*m.b6*m.b15 - 224*
                       m.b5*m.b6*m.b16 - 160*m.b5*m.b6*m.b17 - 96*m.b5*m.b6*m.b18 - 32*m.b5*m.b6*m.b19 - 448*m.b5*m.b7*
                       m.b8 - 256*m.b5*m.b7*m.b9 - 384*m.b5*m.b7*m.b10 - 352*m.b5*m.b7*m.b11 - 320*m.b5*m.b7*m.b12 - 320
                       *m.b5*m.b7*m.b13 - 288*m.b5*m.b7*m.b14 - 256*m.b5*m.b7*m.b15 - 192*m.b5*m.b7*m.b16 - 128*m.b5*
                       m.b7*m.b17 - 64*m.b5*m.b7*m.b18 - 32*m.b5*m.b7*m.b19 - 448*m.b5*m.b8*m.b9 - 416*m.b5*m.b8*m.b10
                        - 224*m.b5*m.b8*m.b11 - 352*m.b5*m.b8*m.b12 - 288*m.b5*m.b8*m.b13 - 256*m.b5*m.b8*m.b14 - 224*
                       m.b5*m.b8*m.b15 - 160*m.b5*m.b8*m.b16 - 96*m.b5*m.b8*m.b17 - 64*m.b5*m.b8*m.b18 - 32*m.b5*m.b8*
                       m.b19 - 448*m.b5*m.b9*m.b10 - 416*m.b5*m.b9*m.b11 - 352*m.b5*m.b9*m.b12 - 128*m.b5*m.b9*m.b13 - 
                       224*m.b5*m.b9*m.b14 - 192*m.b5*m.b9*m.b15 - 128*m.b5*m.b9*m.b16 - 96*m.b5*m.b9*m.b17 - 64*m.b5*
                       m.b9*m.b18 - 32*m.b5*m.b9*m.b19 - 416*m.b5*m.b10*m.b11 - 352*m.b5*m.b10*m.b12 - 288*m.b5*m.b10*
                       m.b13 - 224*m.b5*m.b10*m.b14 - 128*m.b5*m.b10*m.b16 - 96*m.b5*m.b10*m.b17 - 64*m.b5*m.b10*m.b18
                        - 32*m.b5*m.b10*m.b19 - 352*m.b5*m.b11*m.b12 - 288*m.b5*m.b11*m.b13 - 224*m.b5*m.b11*m.b14 - 192
                       *m.b5*m.b11*m.b15 - 128*m.b5*m.b11*m.b16 - 64*m.b5*m.b11*m.b18 - 32*m.b5*m.b11*m.b19 - 288*m.b5*
                       m.b12*m.b13 - 256*m.b5*m.b12*m.b14 - 224*m.b5*m.b12*m.b15 - 128*m.b5*m.b12*m.b16 - 96*m.b5*m.b12*
                       m.b17 - 64*m.b5*m.b12*m.b18 - 288*m.b5*m.b13*m.b14 - 256*m.b5*m.b13*m.b15 - 160*m.b5*m.b13*m.b16
                        - 96*m.b5*m.b13*m.b17 - 64*m.b5*m.b13*m.b18 - 32*m.b5*m.b13*m.b19 - 288*m.b5*m.b14*m.b15 - 192*
                       m.b5*m.b14*m.b16 - 96*m.b5*m.b14*m.b17 - 64*m.b5*m.b14*m.b18 - 32*m.b5*m.b14*m.b19 - 224*m.b5*
                       m.b15*m.b16 - 128*m.b5*m.b15*m.b17 - 64*m.b5*m.b15*m.b18 - 32*m.b5*m.b15*m.b19 - 160*m.b5*m.b16*
                       m.b17 - 64*m.b5*m.b16*m.b18 - 32*m.b5*m.b16*m.b19 - 96*m.b5*m.b17*m.b18 - 32*m.b5*m.b17*m.b19 - 
                       32*m.b5*m.b18*m.b19 - 352*m.b6*m.b7*m.b8 - 512*m.b6*m.b7*m.b9 - 480*m.b6*m.b7*m.b10 - 448*m.b6*
                       m.b7*m.b11 - 416*m.b6*m.b7*m.b12 - 384*m.b6*m.b7*m.b13 - 384*m.b6*m.b7*m.b14 - 352*m.b6*m.b7*
                       m.b15 - 288*m.b6*m.b7*m.b16 - 224*m.b6*m.b7*m.b17 - 160*m.b6*m.b7*m.b18 - 96*m.b6*m.b7*m.b19 - 32
                       *m.b6*m.b7*m.b20 - 544*m.b6*m.b8*m.b9 - 320*m.b6*m.b8*m.b10 - 480*m.b6*m.b8*m.b11 - 448*m.b6*m.b8
                       *m.b12 - 416*m.b6*m.b8*m.b13 - 352*m.b6*m.b8*m.b14 - 320*m.b6*m.b8*m.b15 - 256*m.b6*m.b8*m.b16 - 
                       192*m.b6*m.b8*m.b17 - 128*m.b6*m.b8*m.b18 - 64*m.b6*m.b8*m.b19 - 32*m.b6*m.b8*m.b20 - 544*m.b6*
                       m.b9*m.b10 - 512*m.b6*m.b9*m.b11 - 288*m.b6*m.b9*m.b12 - 416*m.b6*m.b9*m.b13 - 352*m.b6*m.b9*
                       m.b14 - 288*m.b6*m.b9*m.b15 - 224*m.b6*m.b9*m.b16 - 160*m.b6*m.b9*m.b17 - 96*m.b6*m.b9*m.b18 - 64
                       *m.b6*m.b9*m.b19 - 32*m.b6*m.b9*m.b20 - 544*m.b6*m.b10*m.b11 - 480*m.b6*m.b10*m.b12 - 416*m.b6*
                       m.b10*m.b13 - 160*m.b6*m.b10*m.b14 - 288*m.b6*m.b10*m.b15 - 192*m.b6*m.b10*m.b16 - 128*m.b6*m.b10
                       *m.b17 - 96*m.b6*m.b10*m.b18 - 64*m.b6*m.b10*m.b19 - 32*m.b6*m.b10*m.b20 - 480*m.b6*m.b11*m.b12
                        - 416*m.b6*m.b11*m.b13 - 352*m.b6*m.b11*m.b14 - 288*m.b6*m.b11*m.b15 - 128*m.b6*m.b11*m.b17 - 96
                       *m.b6*m.b11*m.b18 - 64*m.b6*m.b11*m.b19 - 32*m.b6*m.b11*m.b20 - 416*m.b6*m.b12*m.b13 - 352*m.b6*
                       m.b12*m.b14 - 288*m.b6*m.b12*m.b15 - 192*m.b6*m.b12*m.b16 - 128*m.b6*m.b12*m.b17 - 64*m.b6*m.b12*
                       m.b19 - 32*m.b6*m.b12*m.b20 - 352*m.b6*m.b13*m.b14 - 320*m.b6*m.b13*m.b15 - 224*m.b6*m.b13*m.b16
                        - 128*m.b6*m.b13*m.b17 - 96*m.b6*m.b13*m.b18 - 64*m.b6*m.b13*m.b19 - 352*m.b6*m.b14*m.b15 - 256*
                       m.b6*m.b14*m.b16 - 160*m.b6*m.b14*m.b17 - 96*m.b6*m.b14*m.b18 - 64*m.b6*m.b14*m.b19 - 32*m.b6*
                       m.b14*m.b20 - 288*m.b6*m.b15*m.b16 - 192*m.b6*m.b15*m.b17 - 96*m.b6*m.b15*m.b18 - 64*m.b6*m.b15*
                       m.b19 - 32*m.b6*m.b15*m.b20 - 224*m.b6*m.b16*m.b17 - 128*m.b6*m.b16*m.b18 - 64*m.b6*m.b16*m.b19
                        - 32*m.b6*m.b16*m.b20 - 160*m.b6*m.b17*m.b18 - 64*m.b6*m.b17*m.b19 - 32*m.b6*m.b17*m.b20 - 96*
                       m.b6*m.b18*m.b19 - 32*m.b6*m.b18*m.b20 - 32*m.b6*m.b19*m.b20 - 416*m.b7*m.b8*m.b9 - 608*m.b7*m.b8
                       *m.b10 - 576*m.b7*m.b8*m.b11 - 544*m.b7*m.b8*m.b12 - 512*m.b7*m.b8*m.b13 - 480*m.b7*m.b8*m.b14 - 
                       416*m.b7*m.b8*m.b15 - 352*m.b7*m.b8*m.b16 - 288*m.b7*m.b8*m.b17 - 224*m.b7*m.b8*m.b18 - 160*m.b7*
                       m.b8*m.b19 - 96*m.b7*m.b8*m.b20 - 32*m.b7*m.b8*m.b21 - 640*m.b7*m.b9*m.b10 - 384*m.b7*m.b9*m.b11
                        - 576*m.b7*m.b9*m.b12 - 544*m.b7*m.b9*m.b13 - 480*m.b7*m.b9*m.b14 - 416*m.b7*m.b9*m.b15 - 320*
                       m.b7*m.b9*m.b16 - 256*m.b7*m.b9*m.b17 - 192*m.b7*m.b9*m.b18 - 128*m.b7*m.b9*m.b19 - 64*m.b7*m.b9*
                       m.b20 - 32*m.b7*m.b9*m.b21 - 640*m.b7*m.b10*m.b11 - 608*m.b7*m.b10*m.b12 - 320*m.b7*m.b10*m.b13
                        - 480*m.b7*m.b10*m.b14 - 416*m.b7*m.b10*m.b15 - 288*m.b7*m.b10*m.b16 - 224*m.b7*m.b10*m.b17 - 
                       160*m.b7*m.b10*m.b18 - 96*m.b7*m.b10*m.b19 - 64*m.b7*m.b10*m.b20 - 32*m.b7*m.b10*m.b21 - 608*m.b7
                       *m.b11*m.b12 - 544*m.b7*m.b11*m.b13 - 480*m.b7*m.b11*m.b14 - 192*m.b7*m.b11*m.b15 - 288*m.b7*
                       m.b11*m.b16 - 192*m.b7*m.b11*m.b17 - 128*m.b7*m.b11*m.b18 - 96*m.b7*m.b11*m.b19 - 64*m.b7*m.b11*
                       m.b20 - 32*m.b7*m.b11*m.b21 - 544*m.b7*m.b12*m.b13 - 480*m.b7*m.b12*m.b14 - 416*m.b7*m.b12*m.b15
                        - 288*m.b7*m.b12*m.b16 - 128*m.b7*m.b12*m.b18 - 96*m.b7*m.b12*m.b19 - 64*m.b7*m.b12*m.b20 - 32*
                       m.b7*m.b12*m.b21 - 480*m.b7*m.b13*m.b14 - 416*m.b7*m.b13*m.b15 - 288*m.b7*m.b13*m.b16 - 192*m.b7*
                       m.b13*m.b17 - 128*m.b7*m.b13*m.b18 - 64*m.b7*m.b13*m.b20 - 32*m.b7*m.b13*m.b21 - 416*m.b7*m.b14*
                       m.b15 - 320*m.b7*m.b14*m.b16 - 224*m.b7*m.b14*m.b17 - 128*m.b7*m.b14*m.b18 - 96*m.b7*m.b14*m.b19
                        - 64*m.b7*m.b14*m.b20 - 352*m.b7*m.b15*m.b16 - 256*m.b7*m.b15*m.b17 - 160*m.b7*m.b15*m.b18 - 96*
                       m.b7*m.b15*m.b19 - 64*m.b7*m.b15*m.b20 - 32*m.b7*m.b15*m.b21 - 288*m.b7*m.b16*m.b17 - 192*m.b7*
                       m.b16*m.b18 - 96*m.b7*m.b16*m.b19 - 64*m.b7*m.b16*m.b20 - 32*m.b7*m.b16*m.b21 - 224*m.b7*m.b17*
                       m.b18 - 128*m.b7*m.b17*m.b19 - 64*m.b7*m.b17*m.b20 - 32*m.b7*m.b17*m.b21 - 160*m.b7*m.b18*m.b19
                        - 64*m.b7*m.b18*m.b20 - 32*m.b7*m.b18*m.b21 - 96*m.b7*m.b19*m.b20 - 32*m.b7*m.b19*m.b21 - 32*
                       m.b7*m.b20*m.b21 - 480*m.b8*m.b9*m.b10 - 704*m.b8*m.b9*m.b11 - 672*m.b8*m.b9*m.b12 - 640*m.b8*
                       m.b9*m.b13 - 608*m.b8*m.b9*m.b14 - 544*m.b8*m.b9*m.b15 - 416*m.b8*m.b9*m.b16 - 352*m.b8*m.b9*
                       m.b17 - 288*m.b8*m.b9*m.b18 - 224*m.b8*m.b9*m.b19 - 160*m.b8*m.b9*m.b20 - 96*m.b8*m.b9*m.b21 - 32
                       *m.b8*m.b9*m.b22 - 736*m.b8*m.b10*m.b11 - 448*m.b8*m.b10*m.b12 - 672*m.b8*m.b10*m.b13 - 608*m.b8*
                       m.b10*m.b14 - 544*m.b8*m.b10*m.b15 - 416*m.b8*m.b10*m.b16 - 320*m.b8*m.b10*m.b17 - 256*m.b8*m.b10
                       *m.b18 - 192*m.b8*m.b10*m.b19 - 128*m.b8*m.b10*m.b20 - 64*m.b8*m.b10*m.b21 - 32*m.b8*m.b10*m.b22
                        - 736*m.b8*m.b11*m.b12 - 672*m.b8*m.b11*m.b13 - 352*m.b8*m.b11*m.b14 - 544*m.b8*m.b11*m.b15 - 
                       416*m.b8*m.b11*m.b16 - 288*m.b8*m.b11*m.b17 - 224*m.b8*m.b11*m.b18 - 160*m.b8*m.b11*m.b19 - 96*
                       m.b8*m.b11*m.b20 - 64*m.b8*m.b11*m.b21 - 32*m.b8*m.b11*m.b22 - 672*m.b8*m.b12*m.b13 - 608*m.b8*
                       m.b12*m.b14 - 544*m.b8*m.b12*m.b15 - 192*m.b8*m.b12*m.b16 - 288*m.b8*m.b12*m.b17 - 192*m.b8*m.b12
                       *m.b18 - 128*m.b8*m.b12*m.b19 - 96*m.b8*m.b12*m.b20 - 64*m.b8*m.b12*m.b21 - 32*m.b8*m.b12*m.b22
                        - 608*m.b8*m.b13*m.b14 - 544*m.b8*m.b13*m.b15 - 416*m.b8*m.b13*m.b16 - 288*m.b8*m.b13*m.b17 - 
                       128*m.b8*m.b13*m.b19 - 96*m.b8*m.b13*m.b20 - 64*m.b8*m.b13*m.b21 - 32*m.b8*m.b13*m.b22 - 544*m.b8
                       *m.b14*m.b15 - 416*m.b8*m.b14*m.b16 - 288*m.b8*m.b14*m.b17 - 192*m.b8*m.b14*m.b18 - 128*m.b8*
                       m.b14*m.b19 - 64*m.b8*m.b14*m.b21 - 32*m.b8*m.b14*m.b22 - 416*m.b8*m.b15*m.b16 - 320*m.b8*m.b15*
                       m.b17 - 224*m.b8*m.b15*m.b18 - 128*m.b8*m.b15*m.b19 - 96*m.b8*m.b15*m.b20 - 64*m.b8*m.b15*m.b21
                        - 352*m.b8*m.b16*m.b17 - 256*m.b8*m.b16*m.b18 - 160*m.b8*m.b16*m.b19 - 96*m.b8*m.b16*m.b20 - 64*
                       m.b8*m.b16*m.b21 - 32*m.b8*m.b16*m.b22 - 288*m.b8*m.b17*m.b18 - 192*m.b8*m.b17*m.b19 - 96*m.b8*
                       m.b17*m.b20 - 64*m.b8*m.b17*m.b21 - 32*m.b8*m.b17*m.b22 - 224*m.b8*m.b18*m.b19 - 128*m.b8*m.b18*
                       m.b20 - 64*m.b8*m.b18*m.b21 - 32*m.b8*m.b18*m.b22 - 160*m.b8*m.b19*m.b20 - 64*m.b8*m.b19*m.b21 - 
                       32*m.b8*m.b19*m.b22 - 96*m.b8*m.b20*m.b21 - 32*m.b8*m.b20*m.b22 - 32*m.b8*m.b21*m.b22 - 544*m.b9*
                       m.b10*m.b11 - 800*m.b9*m.b10*m.b12 - 768*m.b9*m.b10*m.b13 - 736*m.b9*m.b10*m.b14 - 672*m.b9*m.b10
                       *m.b15 - 544*m.b9*m.b10*m.b16 - 416*m.b9*m.b10*m.b17 - 352*m.b9*m.b10*m.b18 - 288*m.b9*m.b10*
                       m.b19 - 224*m.b9*m.b10*m.b20 - 160*m.b9*m.b10*m.b21 - 96*m.b9*m.b10*m.b22 - 32*m.b9*m.b10*m.b23
                        - 832*m.b9*m.b11*m.b12 - 512*m.b9*m.b11*m.b13 - 736*m.b9*m.b11*m.b14 - 672*m.b9*m.b11*m.b15 - 
                       544*m.b9*m.b11*m.b16 - 416*m.b9*m.b11*m.b17 - 320*m.b9*m.b11*m.b18 - 256*m.b9*m.b11*m.b19 - 192*
                       m.b9*m.b11*m.b20 - 128*m.b9*m.b11*m.b21 - 64*m.b9*m.b11*m.b22 - 32*m.b9*m.b11*m.b23 - 800*m.b9*
                       m.b12*m.b13 - 736*m.b9*m.b12*m.b14 - 384*m.b9*m.b12*m.b15 - 544*m.b9*m.b12*m.b16 - 416*m.b9*m.b12
                       *m.b17 - 288*m.b9*m.b12*m.b18 - 224*m.b9*m.b12*m.b19 - 160*m.b9*m.b12*m.b20 - 96*m.b9*m.b12*m.b21
                        - 64*m.b9*m.b12*m.b22 - 32*m.b9*m.b12*m.b23 - 736*m.b9*m.b13*m.b14 - 672*m.b9*m.b13*m.b15 - 544*
                       m.b9*m.b13*m.b16 - 192*m.b9*m.b13*m.b17 - 288*m.b9*m.b13*m.b18 - 192*m.b9*m.b13*m.b19 - 128*m.b9*
                       m.b13*m.b20 - 96*m.b9*m.b13*m.b21 - 64*m.b9*m.b13*m.b22 - 32*m.b9*m.b13*m.b23 - 672*m.b9*m.b14*
                       m.b15 - 544*m.b9*m.b14*m.b16 - 416*m.b9*m.b14*m.b17 - 288*m.b9*m.b14*m.b18 - 128*m.b9*m.b14*m.b20
                        - 96*m.b9*m.b14*m.b21 - 64*m.b9*m.b14*m.b22 - 32*m.b9*m.b14*m.b23 - 544*m.b9*m.b15*m.b16 - 416*
                       m.b9*m.b15*m.b17 - 288*m.b9*m.b15*m.b18 - 192*m.b9*m.b15*m.b19 - 128*m.b9*m.b15*m.b20 - 64*m.b9*
                       m.b15*m.b22 - 32*m.b9*m.b15*m.b23 - 416*m.b9*m.b16*m.b17 - 320*m.b9*m.b16*m.b18 - 224*m.b9*m.b16*
                       m.b19 - 128*m.b9*m.b16*m.b20 - 96*m.b9*m.b16*m.b21 - 64*m.b9*m.b16*m.b22 - 352*m.b9*m.b17*m.b18
                        - 256*m.b9*m.b17*m.b19 - 160*m.b9*m.b17*m.b20 - 96*m.b9*m.b17*m.b21 - 64*m.b9*m.b17*m.b22 - 32*
                       m.b9*m.b17*m.b23 - 288*m.b9*m.b18*m.b19 - 192*m.b9*m.b18*m.b20 - 96*m.b9*m.b18*m.b21 - 64*m.b9*
                       m.b18*m.b22 - 32*m.b9*m.b18*m.b23 - 224*m.b9*m.b19*m.b20 - 128*m.b9*m.b19*m.b21 - 64*m.b9*m.b19*
                       m.b22 - 32*m.b9*m.b19*m.b23 - 160*m.b9*m.b20*m.b21 - 64*m.b9*m.b20*m.b22 - 32*m.b9*m.b20*m.b23 - 
                       96*m.b9*m.b21*m.b22 - 32*m.b9*m.b21*m.b23 - 32*m.b9*m.b22*m.b23 - 608*m.b10*m.b11*m.b12 - 896*
                       m.b10*m.b11*m.b13 - 864*m.b10*m.b11*m.b14 - 800*m.b10*m.b11*m.b15 - 672*m.b10*m.b11*m.b16 - 544*
                       m.b10*m.b11*m.b17 - 416*m.b10*m.b11*m.b18 - 352*m.b10*m.b11*m.b19 - 288*m.b10*m.b11*m.b20 - 224*
                       m.b10*m.b11*m.b21 - 160*m.b10*m.b11*m.b22 - 96*m.b10*m.b11*m.b23 - 32*m.b10*m.b11*m.b24 - 928*
                       m.b10*m.b12*m.b13 - 544*m.b10*m.b12*m.b14 - 800*m.b10*m.b12*m.b15 - 672*m.b10*m.b12*m.b16 - 544*
                       m.b10*m.b12*m.b17 - 416*m.b10*m.b12*m.b18 - 320*m.b10*m.b12*m.b19 - 256*m.b10*m.b12*m.b20 - 192*
                       m.b10*m.b12*m.b21 - 128*m.b10*m.b12*m.b22 - 64*m.b10*m.b12*m.b23 - 32*m.b10*m.b12*m.b24 - 864*
                       m.b10*m.b13*m.b14 - 800*m.b10*m.b13*m.b15 - 384*m.b10*m.b13*m.b16 - 544*m.b10*m.b13*m.b17 - 416*
                       m.b10*m.b13*m.b18 - 288*m.b10*m.b13*m.b19 - 224*m.b10*m.b13*m.b20 - 160*m.b10*m.b13*m.b21 - 96*
                       m.b10*m.b13*m.b22 - 64*m.b10*m.b13*m.b23 - 32*m.b10*m.b13*m.b24 - 800*m.b10*m.b14*m.b15 - 672*
                       m.b10*m.b14*m.b16 - 544*m.b10*m.b14*m.b17 - 192*m.b10*m.b14*m.b18 - 288*m.b10*m.b14*m.b19 - 192*
                       m.b10*m.b14*m.b20 - 128*m.b10*m.b14*m.b21 - 96*m.b10*m.b14*m.b22 - 64*m.b10*m.b14*m.b23 - 32*
                       m.b10*m.b14*m.b24 - 672*m.b10*m.b15*m.b16 - 544*m.b10*m.b15*m.b17 - 416*m.b10*m.b15*m.b18 - 288*
                       m.b10*m.b15*m.b19 - 128*m.b10*m.b15*m.b21 - 96*m.b10*m.b15*m.b22 - 64*m.b10*m.b15*m.b23 - 32*
                       m.b10*m.b15*m.b24 - 544*m.b10*m.b16*m.b17 - 416*m.b10*m.b16*m.b18 - 288*m.b10*m.b16*m.b19 - 192*
                       m.b10*m.b16*m.b20 - 128*m.b10*m.b16*m.b21 - 64*m.b10*m.b16*m.b23 - 32*m.b10*m.b16*m.b24 - 416*
                       m.b10*m.b17*m.b18 - 320*m.b10*m.b17*m.b19 - 224*m.b10*m.b17*m.b20 - 128*m.b10*m.b17*m.b21 - 96*
                       m.b10*m.b17*m.b22 - 64*m.b10*m.b17*m.b23 - 352*m.b10*m.b18*m.b19 - 256*m.b10*m.b18*m.b20 - 160*
                       m.b10*m.b18*m.b21 - 96*m.b10*m.b18*m.b22 - 64*m.b10*m.b18*m.b23 - 32*m.b10*m.b18*m.b24 - 288*
                       m.b10*m.b19*m.b20 - 192*m.b10*m.b19*m.b21 - 96*m.b10*m.b19*m.b22 - 64*m.b10*m.b19*m.b23 - 32*
                       m.b10*m.b19*m.b24 - 224*m.b10*m.b20*m.b21 - 128*m.b10*m.b20*m.b22 - 64*m.b10*m.b20*m.b23 - 32*
                       m.b10*m.b20*m.b24 - 160*m.b10*m.b21*m.b22 - 64*m.b10*m.b21*m.b23 - 32*m.b10*m.b21*m.b24 - 96*
                       m.b10*m.b22*m.b23 - 32*m.b10*m.b22*m.b24 - 32*m.b10*m.b23*m.b24 - 672*m.b11*m.b12*m.b13 - 992*
                       m.b11*m.b12*m.b14 - 928*m.b11*m.b12*m.b15 - 800*m.b11*m.b12*m.b16 - 672*m.b11*m.b12*m.b17 - 544*
                       m.b11*m.b12*m.b18 - 416*m.b11*m.b12*m.b19 - 352*m.b11*m.b12*m.b20 - 288*m.b11*m.b12*m.b21 - 224*
                       m.b11*m.b12*m.b22 - 160*m.b11*m.b12*m.b23 - 96*m.b11*m.b12*m.b24 - 32*m.b11*m.b12*m.b25 - 992*
                       m.b11*m.b13*m.b14 - 576*m.b11*m.b13*m.b15 - 800*m.b11*m.b13*m.b16 - 672*m.b11*m.b13*m.b17 - 544*
                       m.b11*m.b13*m.b18 - 416*m.b11*m.b13*m.b19 - 320*m.b11*m.b13*m.b20 - 256*m.b11*m.b13*m.b21 - 192*
                       m.b11*m.b13*m.b22 - 128*m.b11*m.b13*m.b23 - 64*m.b11*m.b13*m.b24 - 32*m.b11*m.b13*m.b25 - 928*
                       m.b11*m.b14*m.b15 - 800*m.b11*m.b14*m.b16 - 384*m.b11*m.b14*m.b17 - 544*m.b11*m.b14*m.b18 - 416*
                       m.b11*m.b14*m.b19 - 288*m.b11*m.b14*m.b20 - 224*m.b11*m.b14*m.b21 - 160*m.b11*m.b14*m.b22 - 96*
                       m.b11*m.b14*m.b23 - 64*m.b11*m.b14*m.b24 - 32*m.b11*m.b14*m.b25 - 800*m.b11*m.b15*m.b16 - 672*
                       m.b11*m.b15*m.b17 - 544*m.b11*m.b15*m.b18 - 192*m.b11*m.b15*m.b19 - 288*m.b11*m.b15*m.b20 - 192*
                       m.b11*m.b15*m.b21 - 128*m.b11*m.b15*m.b22 - 96*m.b11*m.b15*m.b23 - 64*m.b11*m.b15*m.b24 - 32*
                       m.b11*m.b15*m.b25 - 672*m.b11*m.b16*m.b17 - 544*m.b11*m.b16*m.b18 - 416*m.b11*m.b16*m.b19 - 288*
                       m.b11*m.b16*m.b20 - 128*m.b11*m.b16*m.b22 - 96*m.b11*m.b16*m.b23 - 64*m.b11*m.b16*m.b24 - 32*
                       m.b11*m.b16*m.b25 - 544*m.b11*m.b17*m.b18 - 416*m.b11*m.b17*m.b19 - 288*m.b11*m.b17*m.b20 - 192*
                       m.b11*m.b17*m.b21 - 128*m.b11*m.b17*m.b22 - 64*m.b11*m.b17*m.b24 - 32*m.b11*m.b17*m.b25 - 416*
                       m.b11*m.b18*m.b19 - 320*m.b11*m.b18*m.b20 - 224*m.b11*m.b18*m.b21 - 128*m.b11*m.b18*m.b22 - 96*
                       m.b11*m.b18*m.b23 - 64*m.b11*m.b18*m.b24 - 352*m.b11*m.b19*m.b20 - 256*m.b11*m.b19*m.b21 - 160*
                       m.b11*m.b19*m.b22 - 96*m.b11*m.b19*m.b23 - 64*m.b11*m.b19*m.b24 - 32*m.b11*m.b19*m.b25 - 288*
                       m.b11*m.b20*m.b21 - 192*m.b11*m.b20*m.b22 - 96*m.b11*m.b20*m.b23 - 64*m.b11*m.b20*m.b24 - 32*
                       m.b11*m.b20*m.b25 - 224*m.b11*m.b21*m.b22 - 128*m.b11*m.b21*m.b23 - 64*m.b11*m.b21*m.b24 - 32*
                       m.b11*m.b21*m.b25 - 160*m.b11*m.b22*m.b23 - 64*m.b11*m.b22*m.b24 - 32*m.b11*m.b22*m.b25 - 96*
                       m.b11*m.b23*m.b24 - 32*m.b11*m.b23*m.b25 - 32*m.b11*m.b24*m.b25 - 736*m.b12*m.b13*m.b14 - 1056*
                       m.b12*m.b13*m.b15 - 928*m.b12*m.b13*m.b16 - 800*m.b12*m.b13*m.b17 - 672*m.b12*m.b13*m.b18 - 544*
                       m.b12*m.b13*m.b19 - 416*m.b12*m.b13*m.b20 - 352*m.b12*m.b13*m.b21 - 288*m.b12*m.b13*m.b22 - 224*
                       m.b12*m.b13*m.b23 - 160*m.b12*m.b13*m.b24 - 96*m.b12*m.b13*m.b25 - 32*m.b12*m.b13*m.b26 - 1056*
                       m.b12*m.b14*m.b15 - 576*m.b12*m.b14*m.b16 - 800*m.b12*m.b14*m.b17 - 672*m.b12*m.b14*m.b18 - 544*
                       m.b12*m.b14*m.b19 - 416*m.b12*m.b14*m.b20 - 320*m.b12*m.b14*m.b21 - 256*m.b12*m.b14*m.b22 - 192*
                       m.b12*m.b14*m.b23 - 128*m.b12*m.b14*m.b24 - 64*m.b12*m.b14*m.b25 - 32*m.b12*m.b14*m.b26 - 928*
                       m.b12*m.b15*m.b16 - 800*m.b12*m.b15*m.b17 - 384*m.b12*m.b15*m.b18 - 544*m.b12*m.b15*m.b19 - 416*
                       m.b12*m.b15*m.b20 - 288*m.b12*m.b15*m.b21 - 224*m.b12*m.b15*m.b22 - 160*m.b12*m.b15*m.b23 - 96*
                       m.b12*m.b15*m.b24 - 64*m.b12*m.b15*m.b25 - 32*m.b12*m.b15*m.b26 - 800*m.b12*m.b16*m.b17 - 672*
                       m.b12*m.b16*m.b18 - 544*m.b12*m.b16*m.b19 - 192*m.b12*m.b16*m.b20 - 288*m.b12*m.b16*m.b21 - 192*
                       m.b12*m.b16*m.b22 - 128*m.b12*m.b16*m.b23 - 96*m.b12*m.b16*m.b24 - 64*m.b12*m.b16*m.b25 - 32*
                       m.b12*m.b16*m.b26 - 672*m.b12*m.b17*m.b18 - 544*m.b12*m.b17*m.b19 - 416*m.b12*m.b17*m.b20 - 288*
                       m.b12*m.b17*m.b21 - 128*m.b12*m.b17*m.b23 - 96*m.b12*m.b17*m.b24 - 64*m.b12*m.b17*m.b25 - 32*
                       m.b12*m.b17*m.b26 - 544*m.b12*m.b18*m.b19 - 416*m.b12*m.b18*m.b20 - 288*m.b12*m.b18*m.b21 - 192*
                       m.b12*m.b18*m.b22 - 128*m.b12*m.b18*m.b23 - 64*m.b12*m.b18*m.b25 - 32*m.b12*m.b18*m.b26 - 416*
                       m.b12*m.b19*m.b20 - 320*m.b12*m.b19*m.b21 - 224*m.b12*m.b19*m.b22 - 128*m.b12*m.b19*m.b23 - 96*
                       m.b12*m.b19*m.b24 - 64*m.b12*m.b19*m.b25 - 352*m.b12*m.b20*m.b21 - 256*m.b12*m.b20*m.b22 - 160*
                       m.b12*m.b20*m.b23 - 96*m.b12*m.b20*m.b24 - 64*m.b12*m.b20*m.b25 - 32*m.b12*m.b20*m.b26 - 288*
                       m.b12*m.b21*m.b22 - 192*m.b12*m.b21*m.b23 - 96*m.b12*m.b21*m.b24 - 64*m.b12*m.b21*m.b25 - 32*
                       m.b12*m.b21*m.b26 - 224*m.b12*m.b22*m.b23 - 128*m.b12*m.b22*m.b24 - 64*m.b12*m.b22*m.b25 - 32*
                       m.b12*m.b22*m.b26 - 160*m.b12*m.b23*m.b24 - 64*m.b12*m.b23*m.b25 - 32*m.b12*m.b23*m.b26 - 96*
                       m.b12*m.b24*m.b25 - 32*m.b12*m.b24*m.b26 - 32*m.b12*m.b25*m.b26 - 768*m.b13*m.b14*m.b15 - 1056*
                       m.b13*m.b14*m.b16 - 928*m.b13*m.b14*m.b17 - 800*m.b13*m.b14*m.b18 - 672*m.b13*m.b14*m.b19 - 544*
                       m.b13*m.b14*m.b20 - 416*m.b13*m.b14*m.b21 - 352*m.b13*m.b14*m.b22 - 288*m.b13*m.b14*m.b23 - 224*
                       m.b13*m.b14*m.b24 - 160*m.b13*m.b14*m.b25 - 96*m.b13*m.b14*m.b26 - 32*m.b13*m.b14*m.b27 - 1056*
                       m.b13*m.b15*m.b16 - 576*m.b13*m.b15*m.b17 - 800*m.b13*m.b15*m.b18 - 672*m.b13*m.b15*m.b19 - 544*
                       m.b13*m.b15*m.b20 - 416*m.b13*m.b15*m.b21 - 320*m.b13*m.b15*m.b22 - 256*m.b13*m.b15*m.b23 - 192*
                       m.b13*m.b15*m.b24 - 128*m.b13*m.b15*m.b25 - 64*m.b13*m.b15*m.b26 - 32*m.b13*m.b15*m.b27 - 928*
                       m.b13*m.b16*m.b17 - 800*m.b13*m.b16*m.b18 - 384*m.b13*m.b16*m.b19 - 544*m.b13*m.b16*m.b20 - 416*
                       m.b13*m.b16*m.b21 - 288*m.b13*m.b16*m.b22 - 224*m.b13*m.b16*m.b23 - 160*m.b13*m.b16*m.b24 - 96*
                       m.b13*m.b16*m.b25 - 64*m.b13*m.b16*m.b26 - 32*m.b13*m.b16*m.b27 - 800*m.b13*m.b17*m.b18 - 672*
                       m.b13*m.b17*m.b19 - 544*m.b13*m.b17*m.b20 - 192*m.b13*m.b17*m.b21 - 288*m.b13*m.b17*m.b22 - 192*
                       m.b13*m.b17*m.b23 - 128*m.b13*m.b17*m.b24 - 96*m.b13*m.b17*m.b25 - 64*m.b13*m.b17*m.b26 - 32*
                       m.b13*m.b17*m.b27 - 672*m.b13*m.b18*m.b19 - 544*m.b13*m.b18*m.b20 - 416*m.b13*m.b18*m.b21 - 288*
                       m.b13*m.b18*m.b22 - 128*m.b13*m.b18*m.b24 - 96*m.b13*m.b18*m.b25 - 64*m.b13*m.b18*m.b26 - 32*
                       m.b13*m.b18*m.b27 - 544*m.b13*m.b19*m.b20 - 416*m.b13*m.b19*m.b21 - 288*m.b13*m.b19*m.b22 - 192*
                       m.b13*m.b19*m.b23 - 128*m.b13*m.b19*m.b24 - 64*m.b13*m.b19*m.b26 - 32*m.b13*m.b19*m.b27 - 416*
                       m.b13*m.b20*m.b21 - 320*m.b13*m.b20*m.b22 - 224*m.b13*m.b20*m.b23 - 128*m.b13*m.b20*m.b24 - 96*
                       m.b13*m.b20*m.b25 - 64*m.b13*m.b20*m.b26 - 352*m.b13*m.b21*m.b22 - 256*m.b13*m.b21*m.b23 - 160*
                       m.b13*m.b21*m.b24 - 96*m.b13*m.b21*m.b25 - 64*m.b13*m.b21*m.b26 - 32*m.b13*m.b21*m.b27 - 288*
                       m.b13*m.b22*m.b23 - 192*m.b13*m.b22*m.b24 - 96*m.b13*m.b22*m.b25 - 64*m.b13*m.b22*m.b26 - 32*
                       m.b13*m.b22*m.b27 - 224*m.b13*m.b23*m.b24 - 128*m.b13*m.b23*m.b25 - 64*m.b13*m.b23*m.b26 - 32*
                       m.b13*m.b23*m.b27 - 160*m.b13*m.b24*m.b25 - 64*m.b13*m.b24*m.b26 - 32*m.b13*m.b24*m.b27 - 96*
                       m.b13*m.b25*m.b26 - 32*m.b13*m.b25*m.b27 - 32*m.b13*m.b26*m.b27 - 768*m.b14*m.b15*m.b16 - 1056*
                       m.b14*m.b15*m.b17 - 928*m.b14*m.b15*m.b18 - 800*m.b14*m.b15*m.b19 - 672*m.b14*m.b15*m.b20 - 544*
                       m.b14*m.b15*m.b21 - 416*m.b14*m.b15*m.b22 - 352*m.b14*m.b15*m.b23 - 288*m.b14*m.b15*m.b24 - 224*
                       m.b14*m.b15*m.b25 - 160*m.b14*m.b15*m.b26 - 96*m.b14*m.b15*m.b27 - 32*m.b14*m.b15*m.b28 - 1056*
                       m.b14*m.b16*m.b17 - 576*m.b14*m.b16*m.b18 - 800*m.b14*m.b16*m.b19 - 672*m.b14*m.b16*m.b20 - 544*
                       m.b14*m.b16*m.b21 - 416*m.b14*m.b16*m.b22 - 320*m.b14*m.b16*m.b23 - 256*m.b14*m.b16*m.b24 - 192*
                       m.b14*m.b16*m.b25 - 128*m.b14*m.b16*m.b26 - 64*m.b14*m.b16*m.b27 - 32*m.b14*m.b16*m.b28 - 928*
                       m.b14*m.b17*m.b18 - 800*m.b14*m.b17*m.b19 - 384*m.b14*m.b17*m.b20 - 544*m.b14*m.b17*m.b21 - 416*
                       m.b14*m.b17*m.b22 - 288*m.b14*m.b17*m.b23 - 224*m.b14*m.b17*m.b24 - 160*m.b14*m.b17*m.b25 - 96*
                       m.b14*m.b17*m.b26 - 64*m.b14*m.b17*m.b27 - 32*m.b14*m.b17*m.b28 - 800*m.b14*m.b18*m.b19 - 672*
                       m.b14*m.b18*m.b20 - 544*m.b14*m.b18*m.b21 - 192*m.b14*m.b18*m.b22 - 288*m.b14*m.b18*m.b23 - 192*
                       m.b14*m.b18*m.b24 - 128*m.b14*m.b18*m.b25 - 96*m.b14*m.b18*m.b26 - 64*m.b14*m.b18*m.b27 - 32*
                       m.b14*m.b18*m.b28 - 672*m.b14*m.b19*m.b20 - 544*m.b14*m.b19*m.b21 - 416*m.b14*m.b19*m.b22 - 288*
                       m.b14*m.b19*m.b23 - 128*m.b14*m.b19*m.b25 - 96*m.b14*m.b19*m.b26 - 64*m.b14*m.b19*m.b27 - 32*
                       m.b14*m.b19*m.b28 - 544*m.b14*m.b20*m.b21 - 416*m.b14*m.b20*m.b22 - 288*m.b14*m.b20*m.b23 - 192*
                       m.b14*m.b20*m.b24 - 128*m.b14*m.b20*m.b25 - 64*m.b14*m.b20*m.b27 - 32*m.b14*m.b20*m.b28 - 416*
                       m.b14*m.b21*m.b22 - 320*m.b14*m.b21*m.b23 - 224*m.b14*m.b21*m.b24 - 128*m.b14*m.b21*m.b25 - 96*
                       m.b14*m.b21*m.b26 - 64*m.b14*m.b21*m.b27 - 352*m.b14*m.b22*m.b23 - 256*m.b14*m.b22*m.b24 - 160*
                       m.b14*m.b22*m.b25 - 96*m.b14*m.b22*m.b26 - 64*m.b14*m.b22*m.b27 - 32*m.b14*m.b22*m.b28 - 288*
                       m.b14*m.b23*m.b24 - 192*m.b14*m.b23*m.b25 - 96*m.b14*m.b23*m.b26 - 64*m.b14*m.b23*m.b27 - 32*
                       m.b14*m.b23*m.b28 - 224*m.b14*m.b24*m.b25 - 128*m.b14*m.b24*m.b26 - 64*m.b14*m.b24*m.b27 - 32*
                       m.b14*m.b24*m.b28 - 160*m.b14*m.b25*m.b26 - 64*m.b14*m.b25*m.b27 - 32*m.b14*m.b25*m.b28 - 96*
                       m.b14*m.b26*m.b27 - 32*m.b14*m.b26*m.b28 - 32*m.b14*m.b27*m.b28 - 768*m.b15*m.b16*m.b17 - 1056*
                       m.b15*m.b16*m.b18 - 928*m.b15*m.b16*m.b19 - 800*m.b15*m.b16*m.b20 - 672*m.b15*m.b16*m.b21 - 544*
                       m.b15*m.b16*m.b22 - 416*m.b15*m.b16*m.b23 - 352*m.b15*m.b16*m.b24 - 288*m.b15*m.b16*m.b25 - 224*
                       m.b15*m.b16*m.b26 - 160*m.b15*m.b16*m.b27 - 96*m.b15*m.b16*m.b28 - 32*m.b15*m.b16*m.b29 - 1056*
                       m.b15*m.b17*m.b18 - 576*m.b15*m.b17*m.b19 - 800*m.b15*m.b17*m.b20 - 672*m.b15*m.b17*m.b21 - 544*
                       m.b15*m.b17*m.b22 - 416*m.b15*m.b17*m.b23 - 320*m.b15*m.b17*m.b24 - 256*m.b15*m.b17*m.b25 - 192*
                       m.b15*m.b17*m.b26 - 128*m.b15*m.b17*m.b27 - 64*m.b15*m.b17*m.b28 - 32*m.b15*m.b17*m.b29 - 928*
                       m.b15*m.b18*m.b19 - 800*m.b15*m.b18*m.b20 - 384*m.b15*m.b18*m.b21 - 544*m.b15*m.b18*m.b22 - 416*
                       m.b15*m.b18*m.b23 - 288*m.b15*m.b18*m.b24 - 224*m.b15*m.b18*m.b25 - 160*m.b15*m.b18*m.b26 - 96*
                       m.b15*m.b18*m.b27 - 64*m.b15*m.b18*m.b28 - 32*m.b15*m.b18*m.b29 - 800*m.b15*m.b19*m.b20 - 672*
                       m.b15*m.b19*m.b21 - 544*m.b15*m.b19*m.b22 - 192*m.b15*m.b19*m.b23 - 288*m.b15*m.b19*m.b24 - 192*
                       m.b15*m.b19*m.b25 - 128*m.b15*m.b19*m.b26 - 96*m.b15*m.b19*m.b27 - 64*m.b15*m.b19*m.b28 - 32*
                       m.b15*m.b19*m.b29 - 672*m.b15*m.b20*m.b21 - 544*m.b15*m.b20*m.b22 - 416*m.b15*m.b20*m.b23 - 288*
                       m.b15*m.b20*m.b24 - 128*m.b15*m.b20*m.b26 - 96*m.b15*m.b20*m.b27 - 64*m.b15*m.b20*m.b28 - 32*
                       m.b15*m.b20*m.b29 - 544*m.b15*m.b21*m.b22 - 416*m.b15*m.b21*m.b23 - 288*m.b15*m.b21*m.b24 - 192*
                       m.b15*m.b21*m.b25 - 128*m.b15*m.b21*m.b26 - 64*m.b15*m.b21*m.b28 - 32*m.b15*m.b21*m.b29 - 416*
                       m.b15*m.b22*m.b23 - 320*m.b15*m.b22*m.b24 - 224*m.b15*m.b22*m.b25 - 128*m.b15*m.b22*m.b26 - 96*
                       m.b15*m.b22*m.b27 - 64*m.b15*m.b22*m.b28 - 352*m.b15*m.b23*m.b24 - 256*m.b15*m.b23*m.b25 - 160*
                       m.b15*m.b23*m.b26 - 96*m.b15*m.b23*m.b27 - 64*m.b15*m.b23*m.b28 - 32*m.b15*m.b23*m.b29 - 288*
                       m.b15*m.b24*m.b25 - 192*m.b15*m.b24*m.b26 - 96*m.b15*m.b24*m.b27 - 64*m.b15*m.b24*m.b28 - 32*
                       m.b15*m.b24*m.b29 - 224*m.b15*m.b25*m.b26 - 128*m.b15*m.b25*m.b27 - 64*m.b15*m.b25*m.b28 - 32*
                       m.b15*m.b25*m.b29 - 160*m.b15*m.b26*m.b27 - 64*m.b15*m.b26*m.b28 - 32*m.b15*m.b26*m.b29 - 96*
                       m.b15*m.b27*m.b28 - 32*m.b15*m.b27*m.b29 - 32*m.b15*m.b28*m.b29 - 768*m.b16*m.b17*m.b18 - 1056*
                       m.b16*m.b17*m.b19 - 928*m.b16*m.b17*m.b20 - 800*m.b16*m.b17*m.b21 - 672*m.b16*m.b17*m.b22 - 544*
                       m.b16*m.b17*m.b23 - 416*m.b16*m.b17*m.b24 - 352*m.b16*m.b17*m.b25 - 288*m.b16*m.b17*m.b26 - 224*
                       m.b16*m.b17*m.b27 - 160*m.b16*m.b17*m.b28 - 96*m.b16*m.b17*m.b29 - 32*m.b16*m.b17*m.b30 - 1056*
                       m.b16*m.b18*m.b19 - 576*m.b16*m.b18*m.b20 - 800*m.b16*m.b18*m.b21 - 672*m.b16*m.b18*m.b22 - 544*
                       m.b16*m.b18*m.b23 - 416*m.b16*m.b18*m.b24 - 320*m.b16*m.b18*m.b25 - 256*m.b16*m.b18*m.b26 - 192*
                       m.b16*m.b18*m.b27 - 128*m.b16*m.b18*m.b28 - 64*m.b16*m.b18*m.b29 - 32*m.b16*m.b18*m.b30 - 928*
                       m.b16*m.b19*m.b20 - 800*m.b16*m.b19*m.b21 - 384*m.b16*m.b19*m.b22 - 544*m.b16*m.b19*m.b23 - 416*
                       m.b16*m.b19*m.b24 - 288*m.b16*m.b19*m.b25 - 224*m.b16*m.b19*m.b26 - 160*m.b16*m.b19*m.b27 - 96*
                       m.b16*m.b19*m.b28 - 64*m.b16*m.b19*m.b29 - 32*m.b16*m.b19*m.b30 - 800*m.b16*m.b20*m.b21 - 672*
                       m.b16*m.b20*m.b22 - 544*m.b16*m.b20*m.b23 - 192*m.b16*m.b20*m.b24 - 288*m.b16*m.b20*m.b25 - 192*
                       m.b16*m.b20*m.b26 - 128*m.b16*m.b20*m.b27 - 96*m.b16*m.b20*m.b28 - 64*m.b16*m.b20*m.b29 - 32*
                       m.b16*m.b20*m.b30 - 672*m.b16*m.b21*m.b22 - 544*m.b16*m.b21*m.b23 - 416*m.b16*m.b21*m.b24 - 288*
                       m.b16*m.b21*m.b25 - 128*m.b16*m.b21*m.b27 - 96*m.b16*m.b21*m.b28 - 64*m.b16*m.b21*m.b29 - 32*
                       m.b16*m.b21*m.b30 - 544*m.b16*m.b22*m.b23 - 416*m.b16*m.b22*m.b24 - 288*m.b16*m.b22*m.b25 - 192*
                       m.b16*m.b22*m.b26 - 128*m.b16*m.b22*m.b27 - 64*m.b16*m.b22*m.b29 - 32*m.b16*m.b22*m.b30 - 416*
                       m.b16*m.b23*m.b24 - 320*m.b16*m.b23*m.b25 - 224*m.b16*m.b23*m.b26 - 128*m.b16*m.b23*m.b27 - 96*
                       m.b16*m.b23*m.b28 - 64*m.b16*m.b23*m.b29 - 352*m.b16*m.b24*m.b25 - 256*m.b16*m.b24*m.b26 - 160*
                       m.b16*m.b24*m.b27 - 96*m.b16*m.b24*m.b28 - 64*m.b16*m.b24*m.b29 - 32*m.b16*m.b24*m.b30 - 288*
                       m.b16*m.b25*m.b26 - 192*m.b16*m.b25*m.b27 - 96*m.b16*m.b25*m.b28 - 64*m.b16*m.b25*m.b29 - 32*
                       m.b16*m.b25*m.b30 - 224*m.b16*m.b26*m.b27 - 128*m.b16*m.b26*m.b28 - 64*m.b16*m.b26*m.b29 - 32*
                       m.b16*m.b26*m.b30 - 160*m.b16*m.b27*m.b28 - 64*m.b16*m.b27*m.b29 - 32*m.b16*m.b27*m.b30 - 96*
                       m.b16*m.b28*m.b29 - 32*m.b16*m.b28*m.b30 - 32*m.b16*m.b29*m.b30 - 768*m.b17*m.b18*m.b19 - 1056*
                       m.b17*m.b18*m.b20 - 928*m.b17*m.b18*m.b21 - 800*m.b17*m.b18*m.b22 - 672*m.b17*m.b18*m.b23 - 544*
                       m.b17*m.b18*m.b24 - 416*m.b17*m.b18*m.b25 - 352*m.b17*m.b18*m.b26 - 288*m.b17*m.b18*m.b27 - 224*
                       m.b17*m.b18*m.b28 - 160*m.b17*m.b18*m.b29 - 96*m.b17*m.b18*m.b30 - 32*m.b17*m.b18*m.b31 - 1056*
                       m.b17*m.b19*m.b20 - 576*m.b17*m.b19*m.b21 - 800*m.b17*m.b19*m.b22 - 672*m.b17*m.b19*m.b23 - 544*
                       m.b17*m.b19*m.b24 - 416*m.b17*m.b19*m.b25 - 320*m.b17*m.b19*m.b26 - 256*m.b17*m.b19*m.b27 - 192*
                       m.b17*m.b19*m.b28 - 128*m.b17*m.b19*m.b29 - 64*m.b17*m.b19*m.b30 - 32*m.b17*m.b19*m.b31 - 928*
                       m.b17*m.b20*m.b21 - 800*m.b17*m.b20*m.b22 - 384*m.b17*m.b20*m.b23 - 544*m.b17*m.b20*m.b24 - 416*
                       m.b17*m.b20*m.b25 - 288*m.b17*m.b20*m.b26 - 224*m.b17*m.b20*m.b27 - 160*m.b17*m.b20*m.b28 - 96*
                       m.b17*m.b20*m.b29 - 64*m.b17*m.b20*m.b30 - 32*m.b17*m.b20*m.b31 - 800*m.b17*m.b21*m.b22 - 672*
                       m.b17*m.b21*m.b23 - 544*m.b17*m.b21*m.b24 - 192*m.b17*m.b21*m.b25 - 288*m.b17*m.b21*m.b26 - 192*
                       m.b17*m.b21*m.b27 - 128*m.b17*m.b21*m.b28 - 96*m.b17*m.b21*m.b29 - 64*m.b17*m.b21*m.b30 - 32*
                       m.b17*m.b21*m.b31 - 672*m.b17*m.b22*m.b23 - 544*m.b17*m.b22*m.b24 - 416*m.b17*m.b22*m.b25 - 288*
                       m.b17*m.b22*m.b26 - 128*m.b17*m.b22*m.b28 - 96*m.b17*m.b22*m.b29 - 64*m.b17*m.b22*m.b30 - 32*
                       m.b17*m.b22*m.b31 - 544*m.b17*m.b23*m.b24 - 416*m.b17*m.b23*m.b25 - 288*m.b17*m.b23*m.b26 - 192*
                       m.b17*m.b23*m.b27 - 128*m.b17*m.b23*m.b28 - 64*m.b17*m.b23*m.b30 - 32*m.b17*m.b23*m.b31 - 416*
                       m.b17*m.b24*m.b25 - 320*m.b17*m.b24*m.b26 - 224*m.b17*m.b24*m.b27 - 128*m.b17*m.b24*m.b28 - 96*
                       m.b17*m.b24*m.b29 - 64*m.b17*m.b24*m.b30 - 352*m.b17*m.b25*m.b26 - 256*m.b17*m.b25*m.b27 - 160*
                       m.b17*m.b25*m.b28 - 96*m.b17*m.b25*m.b29 - 64*m.b17*m.b25*m.b30 - 32*m.b17*m.b25*m.b31 - 288*
                       m.b17*m.b26*m.b27 - 192*m.b17*m.b26*m.b28 - 96*m.b17*m.b26*m.b29 - 64*m.b17*m.b26*m.b30 - 32*
                       m.b17*m.b26*m.b31 - 224*m.b17*m.b27*m.b28 - 128*m.b17*m.b27*m.b29 - 64*m.b17*m.b27*m.b30 - 32*
                       m.b17*m.b27*m.b31 - 160*m.b17*m.b28*m.b29 - 64*m.b17*m.b28*m.b30 - 32*m.b17*m.b28*m.b31 - 96*
                       m.b17*m.b29*m.b30 - 32*m.b17*m.b29*m.b31 - 32*m.b17*m.b30*m.b31 - 768*m.b18*m.b19*m.b20 - 1056*
                       m.b18*m.b19*m.b21 - 928*m.b18*m.b19*m.b22 - 800*m.b18*m.b19*m.b23 - 672*m.b18*m.b19*m.b24 - 544*
                       m.b18*m.b19*m.b25 - 416*m.b18*m.b19*m.b26 - 352*m.b18*m.b19*m.b27 - 288*m.b18*m.b19*m.b28 - 224*
                       m.b18*m.b19*m.b29 - 160*m.b18*m.b19*m.b30 - 96*m.b18*m.b19*m.b31 - 32*m.b18*m.b19*m.b32 - 1056*
                       m.b18*m.b20*m.b21 - 576*m.b18*m.b20*m.b22 - 800*m.b18*m.b20*m.b23 - 672*m.b18*m.b20*m.b24 - 544*
                       m.b18*m.b20*m.b25 - 416*m.b18*m.b20*m.b26 - 320*m.b18*m.b20*m.b27 - 256*m.b18*m.b20*m.b28 - 192*
                       m.b18*m.b20*m.b29 - 128*m.b18*m.b20*m.b30 - 64*m.b18*m.b20*m.b31 - 32*m.b18*m.b20*m.b32 - 928*
                       m.b18*m.b21*m.b22 - 800*m.b18*m.b21*m.b23 - 384*m.b18*m.b21*m.b24 - 544*m.b18*m.b21*m.b25 - 416*
                       m.b18*m.b21*m.b26 - 288*m.b18*m.b21*m.b27 - 224*m.b18*m.b21*m.b28 - 160*m.b18*m.b21*m.b29 - 96*
                       m.b18*m.b21*m.b30 - 64*m.b18*m.b21*m.b31 - 32*m.b18*m.b21*m.b32 - 800*m.b18*m.b22*m.b23 - 672*
                       m.b18*m.b22*m.b24 - 544*m.b18*m.b22*m.b25 - 192*m.b18*m.b22*m.b26 - 288*m.b18*m.b22*m.b27 - 192*
                       m.b18*m.b22*m.b28 - 128*m.b18*m.b22*m.b29 - 96*m.b18*m.b22*m.b30 - 64*m.b18*m.b22*m.b31 - 32*
                       m.b18*m.b22*m.b32 - 672*m.b18*m.b23*m.b24 - 544*m.b18*m.b23*m.b25 - 416*m.b18*m.b23*m.b26 - 288*
                       m.b18*m.b23*m.b27 - 128*m.b18*m.b23*m.b29 - 96*m.b18*m.b23*m.b30 - 64*m.b18*m.b23*m.b31 - 32*
                       m.b18*m.b23*m.b32 - 544*m.b18*m.b24*m.b25 - 416*m.b18*m.b24*m.b26 - 288*m.b18*m.b24*m.b27 - 192*
                       m.b18*m.b24*m.b28 - 128*m.b18*m.b24*m.b29 - 64*m.b18*m.b24*m.b31 - 32*m.b18*m.b24*m.b32 - 416*
                       m.b18*m.b25*m.b26 - 320*m.b18*m.b25*m.b27 - 224*m.b18*m.b25*m.b28 - 128*m.b18*m.b25*m.b29 - 96*
                       m.b18*m.b25*m.b30 - 64*m.b18*m.b25*m.b31 - 352*m.b18*m.b26*m.b27 - 256*m.b18*m.b26*m.b28 - 160*
                       m.b18*m.b26*m.b29 - 96*m.b18*m.b26*m.b30 - 64*m.b18*m.b26*m.b31 - 32*m.b18*m.b26*m.b32 - 288*
                       m.b18*m.b27*m.b28 - 192*m.b18*m.b27*m.b29 - 96*m.b18*m.b27*m.b30 - 64*m.b18*m.b27*m.b31 - 32*
                       m.b18*m.b27*m.b32 - 224*m.b18*m.b28*m.b29 - 128*m.b18*m.b28*m.b30 - 64*m.b18*m.b28*m.b31 - 32*
                       m.b18*m.b28*m.b32 - 160*m.b18*m.b29*m.b30 - 64*m.b18*m.b29*m.b31 - 32*m.b18*m.b29*m.b32 - 96*
                       m.b18*m.b30*m.b31 - 32*m.b18*m.b30*m.b32 - 32*m.b18*m.b31*m.b32 - 768*m.b19*m.b20*m.b21 - 1056*
                       m.b19*m.b20*m.b22 - 928*m.b19*m.b20*m.b23 - 800*m.b19*m.b20*m.b24 - 672*m.b19*m.b20*m.b25 - 544*
                       m.b19*m.b20*m.b26 - 416*m.b19*m.b20*m.b27 - 352*m.b19*m.b20*m.b28 - 288*m.b19*m.b20*m.b29 - 224*
                       m.b19*m.b20*m.b30 - 160*m.b19*m.b20*m.b31 - 96*m.b19*m.b20*m.b32 - 32*m.b19*m.b20*m.b33 - 1056*
                       m.b19*m.b21*m.b22 - 576*m.b19*m.b21*m.b23 - 800*m.b19*m.b21*m.b24 - 672*m.b19*m.b21*m.b25 - 544*
                       m.b19*m.b21*m.b26 - 416*m.b19*m.b21*m.b27 - 320*m.b19*m.b21*m.b28 - 256*m.b19*m.b21*m.b29 - 192*
                       m.b19*m.b21*m.b30 - 128*m.b19*m.b21*m.b31 - 64*m.b19*m.b21*m.b32 - 32*m.b19*m.b21*m.b33 - 928*
                       m.b19*m.b22*m.b23 - 800*m.b19*m.b22*m.b24 - 384*m.b19*m.b22*m.b25 - 544*m.b19*m.b22*m.b26 - 416*
                       m.b19*m.b22*m.b27 - 288*m.b19*m.b22*m.b28 - 224*m.b19*m.b22*m.b29 - 160*m.b19*m.b22*m.b30 - 96*
                       m.b19*m.b22*m.b31 - 64*m.b19*m.b22*m.b32 - 32*m.b19*m.b22*m.b33 - 800*m.b19*m.b23*m.b24 - 672*
                       m.b19*m.b23*m.b25 - 544*m.b19*m.b23*m.b26 - 192*m.b19*m.b23*m.b27 - 288*m.b19*m.b23*m.b28 - 192*
                       m.b19*m.b23*m.b29 - 128*m.b19*m.b23*m.b30 - 96*m.b19*m.b23*m.b31 - 64*m.b19*m.b23*m.b32 - 32*
                       m.b19*m.b23*m.b33 - 672*m.b19*m.b24*m.b25 - 544*m.b19*m.b24*m.b26 - 416*m.b19*m.b24*m.b27 - 288*
                       m.b19*m.b24*m.b28 - 128*m.b19*m.b24*m.b30 - 96*m.b19*m.b24*m.b31 - 64*m.b19*m.b24*m.b32 - 32*
                       m.b19*m.b24*m.b33 - 544*m.b19*m.b25*m.b26 - 416*m.b19*m.b25*m.b27 - 288*m.b19*m.b25*m.b28 - 192*
                       m.b19*m.b25*m.b29 - 128*m.b19*m.b25*m.b30 - 64*m.b19*m.b25*m.b32 - 32*m.b19*m.b25*m.b33 - 416*
                       m.b19*m.b26*m.b27 - 320*m.b19*m.b26*m.b28 - 224*m.b19*m.b26*m.b29 - 128*m.b19*m.b26*m.b30 - 96*
                       m.b19*m.b26*m.b31 - 64*m.b19*m.b26*m.b32 - 352*m.b19*m.b27*m.b28 - 256*m.b19*m.b27*m.b29 - 160*
                       m.b19*m.b27*m.b30 - 96*m.b19*m.b27*m.b31 - 64*m.b19*m.b27*m.b32 - 32*m.b19*m.b27*m.b33 - 288*
                       m.b19*m.b28*m.b29 - 192*m.b19*m.b28*m.b30 - 96*m.b19*m.b28*m.b31 - 64*m.b19*m.b28*m.b32 - 32*
                       m.b19*m.b28*m.b33 - 224*m.b19*m.b29*m.b30 - 128*m.b19*m.b29*m.b31 - 64*m.b19*m.b29*m.b32 - 32*
                       m.b19*m.b29*m.b33 - 160*m.b19*m.b30*m.b31 - 64*m.b19*m.b30*m.b32 - 32*m.b19*m.b30*m.b33 - 96*
                       m.b19*m.b31*m.b32 - 32*m.b19*m.b31*m.b33 - 32*m.b19*m.b32*m.b33 - 768*m.b20*m.b21*m.b22 - 1056*
                       m.b20*m.b21*m.b23 - 928*m.b20*m.b21*m.b24 - 800*m.b20*m.b21*m.b25 - 672*m.b20*m.b21*m.b26 - 544*
                       m.b20*m.b21*m.b27 - 416*m.b20*m.b21*m.b28 - 352*m.b20*m.b21*m.b29 - 288*m.b20*m.b21*m.b30 - 224*
                       m.b20*m.b21*m.b31 - 160*m.b20*m.b21*m.b32 - 96*m.b20*m.b21*m.b33 - 32*m.b20*m.b21*m.b34 - 1056*
                       m.b20*m.b22*m.b23 - 576*m.b20*m.b22*m.b24 - 800*m.b20*m.b22*m.b25 - 672*m.b20*m.b22*m.b26 - 544*
                       m.b20*m.b22*m.b27 - 416*m.b20*m.b22*m.b28 - 320*m.b20*m.b22*m.b29 - 256*m.b20*m.b22*m.b30 - 192*
                       m.b20*m.b22*m.b31 - 128*m.b20*m.b22*m.b32 - 64*m.b20*m.b22*m.b33 - 32*m.b20*m.b22*m.b34 - 928*
                       m.b20*m.b23*m.b24 - 800*m.b20*m.b23*m.b25 - 384*m.b20*m.b23*m.b26 - 544*m.b20*m.b23*m.b27 - 416*
                       m.b20*m.b23*m.b28 - 288*m.b20*m.b23*m.b29 - 224*m.b20*m.b23*m.b30 - 160*m.b20*m.b23*m.b31 - 96*
                       m.b20*m.b23*m.b32 - 64*m.b20*m.b23*m.b33 - 32*m.b20*m.b23*m.b34 - 800*m.b20*m.b24*m.b25 - 672*
                       m.b20*m.b24*m.b26 - 544*m.b20*m.b24*m.b27 - 192*m.b20*m.b24*m.b28 - 288*m.b20*m.b24*m.b29 - 192*
                       m.b20*m.b24*m.b30 - 128*m.b20*m.b24*m.b31 - 96*m.b20*m.b24*m.b32 - 64*m.b20*m.b24*m.b33 - 32*
                       m.b20*m.b24*m.b34 - 672*m.b20*m.b25*m.b26 - 544*m.b20*m.b25*m.b27 - 416*m.b20*m.b25*m.b28 - 288*
                       m.b20*m.b25*m.b29 - 128*m.b20*m.b25*m.b31 - 96*m.b20*m.b25*m.b32 - 64*m.b20*m.b25*m.b33 - 32*
                       m.b20*m.b25*m.b34 - 544*m.b20*m.b26*m.b27 - 416*m.b20*m.b26*m.b28 - 288*m.b20*m.b26*m.b29 - 192*
                       m.b20*m.b26*m.b30 - 128*m.b20*m.b26*m.b31 - 64*m.b20*m.b26*m.b33 - 32*m.b20*m.b26*m.b34 - 416*
                       m.b20*m.b27*m.b28 - 320*m.b20*m.b27*m.b29 - 224*m.b20*m.b27*m.b30 - 128*m.b20*m.b27*m.b31 - 96*
                       m.b20*m.b27*m.b32 - 64*m.b20*m.b27*m.b33 - 352*m.b20*m.b28*m.b29 - 256*m.b20*m.b28*m.b30 - 160*
                       m.b20*m.b28*m.b31 - 96*m.b20*m.b28*m.b32 - 64*m.b20*m.b28*m.b33 - 32*m.b20*m.b28*m.b34 - 288*
                       m.b20*m.b29*m.b30 - 192*m.b20*m.b29*m.b31 - 96*m.b20*m.b29*m.b32 - 64*m.b20*m.b29*m.b33 - 32*
                       m.b20*m.b29*m.b34 - 224*m.b20*m.b30*m.b31 - 128*m.b20*m.b30*m.b32 - 64*m.b20*m.b30*m.b33 - 32*
                       m.b20*m.b30*m.b34 - 160*m.b20*m.b31*m.b32 - 64*m.b20*m.b31*m.b33 - 32*m.b20*m.b31*m.b34 - 96*
                       m.b20*m.b32*m.b33 - 32*m.b20*m.b32*m.b34 - 32*m.b20*m.b33*m.b34 - 768*m.b21*m.b22*m.b23 - 1056*
                       m.b21*m.b22*m.b24 - 928*m.b21*m.b22*m.b25 - 800*m.b21*m.b22*m.b26 - 672*m.b21*m.b22*m.b27 - 544*
                       m.b21*m.b22*m.b28 - 416*m.b21*m.b22*m.b29 - 352*m.b21*m.b22*m.b30 - 288*m.b21*m.b22*m.b31 - 224*
                       m.b21*m.b22*m.b32 - 160*m.b21*m.b22*m.b33 - 96*m.b21*m.b22*m.b34 - 32*m.b21*m.b22*m.b35 - 1056*
                       m.b21*m.b23*m.b24 - 576*m.b21*m.b23*m.b25 - 800*m.b21*m.b23*m.b26 - 672*m.b21*m.b23*m.b27 - 544*
                       m.b21*m.b23*m.b28 - 416*m.b21*m.b23*m.b29 - 320*m.b21*m.b23*m.b30 - 256*m.b21*m.b23*m.b31 - 192*
                       m.b21*m.b23*m.b32 - 128*m.b21*m.b23*m.b33 - 64*m.b21*m.b23*m.b34 - 32*m.b21*m.b23*m.b35 - 928*
                       m.b21*m.b24*m.b25 - 800*m.b21*m.b24*m.b26 - 384*m.b21*m.b24*m.b27 - 544*m.b21*m.b24*m.b28 - 416*
                       m.b21*m.b24*m.b29 - 288*m.b21*m.b24*m.b30 - 224*m.b21*m.b24*m.b31 - 160*m.b21*m.b24*m.b32 - 96*
                       m.b21*m.b24*m.b33 - 64*m.b21*m.b24*m.b34 - 32*m.b21*m.b24*m.b35 - 800*m.b21*m.b25*m.b26 - 672*
                       m.b21*m.b25*m.b27 - 544*m.b21*m.b25*m.b28 - 192*m.b21*m.b25*m.b29 - 288*m.b21*m.b25*m.b30 - 192*
                       m.b21*m.b25*m.b31 - 128*m.b21*m.b25*m.b32 - 96*m.b21*m.b25*m.b33 - 64*m.b21*m.b25*m.b34 - 32*
                       m.b21*m.b25*m.b35 - 672*m.b21*m.b26*m.b27 - 544*m.b21*m.b26*m.b28 - 416*m.b21*m.b26*m.b29 - 288*
                       m.b21*m.b26*m.b30 - 128*m.b21*m.b26*m.b32 - 96*m.b21*m.b26*m.b33 - 64*m.b21*m.b26*m.b34 - 32*
                       m.b21*m.b26*m.b35 - 544*m.b21*m.b27*m.b28 - 416*m.b21*m.b27*m.b29 - 288*m.b21*m.b27*m.b30 - 192*
                       m.b21*m.b27*m.b31 - 128*m.b21*m.b27*m.b32 - 64*m.b21*m.b27*m.b34 - 32*m.b21*m.b27*m.b35 - 416*
                       m.b21*m.b28*m.b29 - 320*m.b21*m.b28*m.b30 - 224*m.b21*m.b28*m.b31 - 128*m.b21*m.b28*m.b32 - 96*
                       m.b21*m.b28*m.b33 - 64*m.b21*m.b28*m.b34 - 352*m.b21*m.b29*m.b30 - 256*m.b21*m.b29*m.b31 - 160*
                       m.b21*m.b29*m.b32 - 96*m.b21*m.b29*m.b33 - 64*m.b21*m.b29*m.b34 - 32*m.b21*m.b29*m.b35 - 288*
                       m.b21*m.b30*m.b31 - 192*m.b21*m.b30*m.b32 - 96*m.b21*m.b30*m.b33 - 64*m.b21*m.b30*m.b34 - 32*
                       m.b21*m.b30*m.b35 - 224*m.b21*m.b31*m.b32 - 128*m.b21*m.b31*m.b33 - 64*m.b21*m.b31*m.b34 - 32*
                       m.b21*m.b31*m.b35 - 160*m.b21*m.b32*m.b33 - 64*m.b21*m.b32*m.b34 - 32*m.b21*m.b32*m.b35 - 96*
                       m.b21*m.b33*m.b34 - 32*m.b21*m.b33*m.b35 - 32*m.b21*m.b34*m.b35 - 768*m.b22*m.b23*m.b24 - 1056*
                       m.b22*m.b23*m.b25 - 928*m.b22*m.b23*m.b26 - 800*m.b22*m.b23*m.b27 - 672*m.b22*m.b23*m.b28 - 544*
                       m.b22*m.b23*m.b29 - 416*m.b22*m.b23*m.b30 - 352*m.b22*m.b23*m.b31 - 288*m.b22*m.b23*m.b32 - 224*
                       m.b22*m.b23*m.b33 - 160*m.b22*m.b23*m.b34 - 96*m.b22*m.b23*m.b35 - 32*m.b22*m.b23*m.b36 - 1056*
                       m.b22*m.b24*m.b25 - 576*m.b22*m.b24*m.b26 - 800*m.b22*m.b24*m.b27 - 672*m.b22*m.b24*m.b28 - 544*
                       m.b22*m.b24*m.b29 - 416*m.b22*m.b24*m.b30 - 320*m.b22*m.b24*m.b31 - 256*m.b22*m.b24*m.b32 - 192*
                       m.b22*m.b24*m.b33 - 128*m.b22*m.b24*m.b34 - 64*m.b22*m.b24*m.b35 - 32*m.b22*m.b24*m.b36 - 928*
                       m.b22*m.b25*m.b26 - 800*m.b22*m.b25*m.b27 - 384*m.b22*m.b25*m.b28 - 544*m.b22*m.b25*m.b29 - 416*
                       m.b22*m.b25*m.b30 - 288*m.b22*m.b25*m.b31 - 224*m.b22*m.b25*m.b32 - 160*m.b22*m.b25*m.b33 - 96*
                       m.b22*m.b25*m.b34 - 64*m.b22*m.b25*m.b35 - 32*m.b22*m.b25*m.b36 - 800*m.b22*m.b26*m.b27 - 672*
                       m.b22*m.b26*m.b28 - 544*m.b22*m.b26*m.b29 - 192*m.b22*m.b26*m.b30 - 288*m.b22*m.b26*m.b31 - 192*
                       m.b22*m.b26*m.b32 - 128*m.b22*m.b26*m.b33 - 96*m.b22*m.b26*m.b34 - 64*m.b22*m.b26*m.b35 - 32*
                       m.b22*m.b26*m.b36 - 672*m.b22*m.b27*m.b28 - 544*m.b22*m.b27*m.b29 - 416*m.b22*m.b27*m.b30 - 288*
                       m.b22*m.b27*m.b31 - 128*m.b22*m.b27*m.b33 - 96*m.b22*m.b27*m.b34 - 64*m.b22*m.b27*m.b35 - 32*
                       m.b22*m.b27*m.b36 - 544*m.b22*m.b28*m.b29 - 416*m.b22*m.b28*m.b30 - 288*m.b22*m.b28*m.b31 - 192*
                       m.b22*m.b28*m.b32 - 128*m.b22*m.b28*m.b33 - 64*m.b22*m.b28*m.b35 - 32*m.b22*m.b28*m.b36 - 416*
                       m.b22*m.b29*m.b30 - 320*m.b22*m.b29*m.b31 - 224*m.b22*m.b29*m.b32 - 128*m.b22*m.b29*m.b33 - 96*
                       m.b22*m.b29*m.b34 - 64*m.b22*m.b29*m.b35 - 352*m.b22*m.b30*m.b31 - 256*m.b22*m.b30*m.b32 - 160*
                       m.b22*m.b30*m.b33 - 96*m.b22*m.b30*m.b34 - 64*m.b22*m.b30*m.b35 - 32*m.b22*m.b30*m.b36 - 288*
                       m.b22*m.b31*m.b32 - 192*m.b22*m.b31*m.b33 - 96*m.b22*m.b31*m.b34 - 64*m.b22*m.b31*m.b35 - 32*
                       m.b22*m.b31*m.b36 - 224*m.b22*m.b32*m.b33 - 128*m.b22*m.b32*m.b34 - 64*m.b22*m.b32*m.b35 - 32*
                       m.b22*m.b32*m.b36 - 160*m.b22*m.b33*m.b34 - 64*m.b22*m.b33*m.b35 - 32*m.b22*m.b33*m.b36 - 96*
                       m.b22*m.b34*m.b35 - 32*m.b22*m.b34*m.b36 - 32*m.b22*m.b35*m.b36 - 768*m.b23*m.b24*m.b25 - 1056*
                       m.b23*m.b24*m.b26 - 928*m.b23*m.b24*m.b27 - 800*m.b23*m.b24*m.b28 - 672*m.b23*m.b24*m.b29 - 544*
                       m.b23*m.b24*m.b30 - 416*m.b23*m.b24*m.b31 - 352*m.b23*m.b24*m.b32 - 288*m.b23*m.b24*m.b33 - 224*
                       m.b23*m.b24*m.b34 - 160*m.b23*m.b24*m.b35 - 96*m.b23*m.b24*m.b36 - 32*m.b23*m.b24*m.b37 - 1056*
                       m.b23*m.b25*m.b26 - 576*m.b23*m.b25*m.b27 - 800*m.b23*m.b25*m.b28 - 672*m.b23*m.b25*m.b29 - 544*
                       m.b23*m.b25*m.b30 - 416*m.b23*m.b25*m.b31 - 320*m.b23*m.b25*m.b32 - 256*m.b23*m.b25*m.b33 - 192*
                       m.b23*m.b25*m.b34 - 128*m.b23*m.b25*m.b35 - 64*m.b23*m.b25*m.b36 - 32*m.b23*m.b25*m.b37 - 928*
                       m.b23*m.b26*m.b27 - 800*m.b23*m.b26*m.b28 - 384*m.b23*m.b26*m.b29 - 544*m.b23*m.b26*m.b30 - 416*
                       m.b23*m.b26*m.b31 - 288*m.b23*m.b26*m.b32 - 224*m.b23*m.b26*m.b33 - 160*m.b23*m.b26*m.b34 - 96*
                       m.b23*m.b26*m.b35 - 64*m.b23*m.b26*m.b36 - 32*m.b23*m.b26*m.b37 - 800*m.b23*m.b27*m.b28 - 672*
                       m.b23*m.b27*m.b29 - 544*m.b23*m.b27*m.b30 - 192*m.b23*m.b27*m.b31 - 288*m.b23*m.b27*m.b32 - 192*
                       m.b23*m.b27*m.b33 - 128*m.b23*m.b27*m.b34 - 96*m.b23*m.b27*m.b35 - 64*m.b23*m.b27*m.b36 - 32*
                       m.b23*m.b27*m.b37 - 672*m.b23*m.b28*m.b29 - 544*m.b23*m.b28*m.b30 - 416*m.b23*m.b28*m.b31 - 288*
                       m.b23*m.b28*m.b32 - 128*m.b23*m.b28*m.b34 - 96*m.b23*m.b28*m.b35 - 64*m.b23*m.b28*m.b36 - 32*
                       m.b23*m.b28*m.b37 - 544*m.b23*m.b29*m.b30 - 416*m.b23*m.b29*m.b31 - 288*m.b23*m.b29*m.b32 - 192*
                       m.b23*m.b29*m.b33 - 128*m.b23*m.b29*m.b34 - 64*m.b23*m.b29*m.b36 - 32*m.b23*m.b29*m.b37 - 416*
                       m.b23*m.b30*m.b31 - 320*m.b23*m.b30*m.b32 - 224*m.b23*m.b30*m.b33 - 128*m.b23*m.b30*m.b34 - 96*
                       m.b23*m.b30*m.b35 - 64*m.b23*m.b30*m.b36 - 352*m.b23*m.b31*m.b32 - 256*m.b23*m.b31*m.b33 - 160*
                       m.b23*m.b31*m.b34 - 96*m.b23*m.b31*m.b35 - 64*m.b23*m.b31*m.b36 - 32*m.b23*m.b31*m.b37 - 288*
                       m.b23*m.b32*m.b33 - 192*m.b23*m.b32*m.b34 - 96*m.b23*m.b32*m.b35 - 64*m.b23*m.b32*m.b36 - 32*
                       m.b23*m.b32*m.b37 - 224*m.b23*m.b33*m.b34 - 128*m.b23*m.b33*m.b35 - 64*m.b23*m.b33*m.b36 - 32*
                       m.b23*m.b33*m.b37 - 160*m.b23*m.b34*m.b35 - 64*m.b23*m.b34*m.b36 - 32*m.b23*m.b34*m.b37 - 96*
                       m.b23*m.b35*m.b36 - 32*m.b23*m.b35*m.b37 - 32*m.b23*m.b36*m.b37 - 768*m.b24*m.b25*m.b26 - 1056*
                       m.b24*m.b25*m.b27 - 928*m.b24*m.b25*m.b28 - 800*m.b24*m.b25*m.b29 - 672*m.b24*m.b25*m.b30 - 544*
                       m.b24*m.b25*m.b31 - 416*m.b24*m.b25*m.b32 - 352*m.b24*m.b25*m.b33 - 288*m.b24*m.b25*m.b34 - 224*
                       m.b24*m.b25*m.b35 - 160*m.b24*m.b25*m.b36 - 96*m.b24*m.b25*m.b37 - 32*m.b24*m.b25*m.b38 - 1056*
                       m.b24*m.b26*m.b27 - 576*m.b24*m.b26*m.b28 - 800*m.b24*m.b26*m.b29 - 672*m.b24*m.b26*m.b30 - 544*
                       m.b24*m.b26*m.b31 - 416*m.b24*m.b26*m.b32 - 320*m.b24*m.b26*m.b33 - 256*m.b24*m.b26*m.b34 - 192*
                       m.b24*m.b26*m.b35 - 128*m.b24*m.b26*m.b36 - 64*m.b24*m.b26*m.b37 - 32*m.b24*m.b26*m.b38 - 928*
                       m.b24*m.b27*m.b28 - 800*m.b24*m.b27*m.b29 - 384*m.b24*m.b27*m.b30 - 544*m.b24*m.b27*m.b31 - 416*
                       m.b24*m.b27*m.b32 - 288*m.b24*m.b27*m.b33 - 224*m.b24*m.b27*m.b34 - 160*m.b24*m.b27*m.b35 - 96*
                       m.b24*m.b27*m.b36 - 64*m.b24*m.b27*m.b37 - 32*m.b24*m.b27*m.b38 - 800*m.b24*m.b28*m.b29 - 672*
                       m.b24*m.b28*m.b30 - 544*m.b24*m.b28*m.b31 - 192*m.b24*m.b28*m.b32 - 288*m.b24*m.b28*m.b33 - 192*
                       m.b24*m.b28*m.b34 - 128*m.b24*m.b28*m.b35 - 96*m.b24*m.b28*m.b36 - 64*m.b24*m.b28*m.b37 - 32*
                       m.b24*m.b28*m.b38 - 672*m.b24*m.b29*m.b30 - 544*m.b24*m.b29*m.b31 - 416*m.b24*m.b29*m.b32 - 288*
                       m.b24*m.b29*m.b33 - 128*m.b24*m.b29*m.b35 - 96*m.b24*m.b29*m.b36 - 64*m.b24*m.b29*m.b37 - 32*
                       m.b24*m.b29*m.b38 - 544*m.b24*m.b30*m.b31 - 416*m.b24*m.b30*m.b32 - 288*m.b24*m.b30*m.b33 - 192*
                       m.b24*m.b30*m.b34 - 128*m.b24*m.b30*m.b35 - 64*m.b24*m.b30*m.b37 - 32*m.b24*m.b30*m.b38 - 416*
                       m.b24*m.b31*m.b32 - 320*m.b24*m.b31*m.b33 - 224*m.b24*m.b31*m.b34 - 128*m.b24*m.b31*m.b35 - 96*
                       m.b24*m.b31*m.b36 - 64*m.b24*m.b31*m.b37 - 352*m.b24*m.b32*m.b33 - 256*m.b24*m.b32*m.b34 - 160*
                       m.b24*m.b32*m.b35 - 96*m.b24*m.b32*m.b36 - 64*m.b24*m.b32*m.b37 - 32*m.b24*m.b32*m.b38 - 288*
                       m.b24*m.b33*m.b34 - 192*m.b24*m.b33*m.b35 - 96*m.b24*m.b33*m.b36 - 64*m.b24*m.b33*m.b37 - 32*
                       m.b24*m.b33*m.b38 - 224*m.b24*m.b34*m.b35 - 128*m.b24*m.b34*m.b36 - 64*m.b24*m.b34*m.b37 - 32*
                       m.b24*m.b34*m.b38 - 160*m.b24*m.b35*m.b36 - 64*m.b24*m.b35*m.b37 - 32*m.b24*m.b35*m.b38 - 96*
                       m.b24*m.b36*m.b37 - 32*m.b24*m.b36*m.b38 - 32*m.b24*m.b37*m.b38 - 768*m.b25*m.b26*m.b27 - 1056*
                       m.b25*m.b26*m.b28 - 928*m.b25*m.b26*m.b29 - 800*m.b25*m.b26*m.b30 - 672*m.b25*m.b26*m.b31 - 544*
                       m.b25*m.b26*m.b32 - 416*m.b25*m.b26*m.b33 - 352*m.b25*m.b26*m.b34 - 288*m.b25*m.b26*m.b35 - 224*
                       m.b25*m.b26*m.b36 - 160*m.b25*m.b26*m.b37 - 96*m.b25*m.b26*m.b38 - 32*m.b25*m.b26*m.b39 - 1056*
                       m.b25*m.b27*m.b28 - 576*m.b25*m.b27*m.b29 - 800*m.b25*m.b27*m.b30 - 672*m.b25*m.b27*m.b31 - 544*
                       m.b25*m.b27*m.b32 - 416*m.b25*m.b27*m.b33 - 320*m.b25*m.b27*m.b34 - 256*m.b25*m.b27*m.b35 - 192*
                       m.b25*m.b27*m.b36 - 128*m.b25*m.b27*m.b37 - 64*m.b25*m.b27*m.b38 - 32*m.b25*m.b27*m.b39 - 928*
                       m.b25*m.b28*m.b29 - 800*m.b25*m.b28*m.b30 - 384*m.b25*m.b28*m.b31 - 544*m.b25*m.b28*m.b32 - 416*
                       m.b25*m.b28*m.b33 - 288*m.b25*m.b28*m.b34 - 224*m.b25*m.b28*m.b35 - 160*m.b25*m.b28*m.b36 - 96*
                       m.b25*m.b28*m.b37 - 64*m.b25*m.b28*m.b38 - 32*m.b25*m.b28*m.b39 - 800*m.b25*m.b29*m.b30 - 672*
                       m.b25*m.b29*m.b31 - 544*m.b25*m.b29*m.b32 - 192*m.b25*m.b29*m.b33 - 288*m.b25*m.b29*m.b34 - 192*
                       m.b25*m.b29*m.b35 - 128*m.b25*m.b29*m.b36 - 96*m.b25*m.b29*m.b37 - 64*m.b25*m.b29*m.b38 - 32*
                       m.b25*m.b29*m.b39 - 672*m.b25*m.b30*m.b31 - 544*m.b25*m.b30*m.b32 - 416*m.b25*m.b30*m.b33 - 288*
                       m.b25*m.b30*m.b34 - 128*m.b25*m.b30*m.b36 - 96*m.b25*m.b30*m.b37 - 64*m.b25*m.b30*m.b38 - 32*
                       m.b25*m.b30*m.b39 - 544*m.b25*m.b31*m.b32 - 416*m.b25*m.b31*m.b33 - 288*m.b25*m.b31*m.b34 - 192*
                       m.b25*m.b31*m.b35 - 128*m.b25*m.b31*m.b36 - 64*m.b25*m.b31*m.b38 - 32*m.b25*m.b31*m.b39 - 416*
                       m.b25*m.b32*m.b33 - 320*m.b25*m.b32*m.b34 - 224*m.b25*m.b32*m.b35 - 128*m.b25*m.b32*m.b36 - 96*
                       m.b25*m.b32*m.b37 - 64*m.b25*m.b32*m.b38 - 352*m.b25*m.b33*m.b34 - 256*m.b25*m.b33*m.b35 - 160*
                       m.b25*m.b33*m.b36 - 96*m.b25*m.b33*m.b37 - 64*m.b25*m.b33*m.b38 - 32*m.b25*m.b33*m.b39 - 288*
                       m.b25*m.b34*m.b35 - 192*m.b25*m.b34*m.b36 - 96*m.b25*m.b34*m.b37 - 64*m.b25*m.b34*m.b38 - 32*
                       m.b25*m.b34*m.b39 - 224*m.b25*m.b35*m.b36 - 128*m.b25*m.b35*m.b37 - 64*m.b25*m.b35*m.b38 - 32*
                       m.b25*m.b35*m.b39 - 160*m.b25*m.b36*m.b37 - 64*m.b25*m.b36*m.b38 - 32*m.b25*m.b36*m.b39 - 96*
                       m.b25*m.b37*m.b38 - 32*m.b25*m.b37*m.b39 - 32*m.b25*m.b38*m.b39 - 768*m.b26*m.b27*m.b28 - 1056*
                       m.b26*m.b27*m.b29 - 928*m.b26*m.b27*m.b30 - 800*m.b26*m.b27*m.b31 - 672*m.b26*m.b27*m.b32 - 544*
                       m.b26*m.b27*m.b33 - 416*m.b26*m.b27*m.b34 - 352*m.b26*m.b27*m.b35 - 288*m.b26*m.b27*m.b36 - 224*
                       m.b26*m.b27*m.b37 - 160*m.b26*m.b27*m.b38 - 96*m.b26*m.b27*m.b39 - 32*m.b26*m.b27*m.b40 - 1056*
                       m.b26*m.b28*m.b29 - 576*m.b26*m.b28*m.b30 - 800*m.b26*m.b28*m.b31 - 672*m.b26*m.b28*m.b32 - 544*
                       m.b26*m.b28*m.b33 - 416*m.b26*m.b28*m.b34 - 320*m.b26*m.b28*m.b35 - 256*m.b26*m.b28*m.b36 - 192*
                       m.b26*m.b28*m.b37 - 128*m.b26*m.b28*m.b38 - 64*m.b26*m.b28*m.b39 - 32*m.b26*m.b28*m.b40 - 928*
                       m.b26*m.b29*m.b30 - 800*m.b26*m.b29*m.b31 - 384*m.b26*m.b29*m.b32 - 544*m.b26*m.b29*m.b33 - 416*
                       m.b26*m.b29*m.b34 - 288*m.b26*m.b29*m.b35 - 224*m.b26*m.b29*m.b36 - 160*m.b26*m.b29*m.b37 - 96*
                       m.b26*m.b29*m.b38 - 64*m.b26*m.b29*m.b39 - 32*m.b26*m.b29*m.b40 - 800*m.b26*m.b30*m.b31 - 672*
                       m.b26*m.b30*m.b32 - 544*m.b26*m.b30*m.b33 - 192*m.b26*m.b30*m.b34 - 288*m.b26*m.b30*m.b35 - 192*
                       m.b26*m.b30*m.b36 - 128*m.b26*m.b30*m.b37 - 96*m.b26*m.b30*m.b38 - 64*m.b26*m.b30*m.b39 - 32*
                       m.b26*m.b30*m.b40 - 672*m.b26*m.b31*m.b32 - 544*m.b26*m.b31*m.b33 - 416*m.b26*m.b31*m.b34 - 288*
                       m.b26*m.b31*m.b35 - 128*m.b26*m.b31*m.b37 - 96*m.b26*m.b31*m.b38 - 64*m.b26*m.b31*m.b39 - 32*
                       m.b26*m.b31*m.b40 - 544*m.b26*m.b32*m.b33 - 416*m.b26*m.b32*m.b34 - 288*m.b26*m.b32*m.b35 - 192*
                       m.b26*m.b32*m.b36 - 128*m.b26*m.b32*m.b37 - 64*m.b26*m.b32*m.b39 - 32*m.b26*m.b32*m.b40 - 416*
                       m.b26*m.b33*m.b34 - 320*m.b26*m.b33*m.b35 - 224*m.b26*m.b33*m.b36 - 128*m.b26*m.b33*m.b37 - 96*
                       m.b26*m.b33*m.b38 - 64*m.b26*m.b33*m.b39 - 352*m.b26*m.b34*m.b35 - 256*m.b26*m.b34*m.b36 - 160*
                       m.b26*m.b34*m.b37 - 96*m.b26*m.b34*m.b38 - 64*m.b26*m.b34*m.b39 - 32*m.b26*m.b34*m.b40 - 288*
                       m.b26*m.b35*m.b36 - 192*m.b26*m.b35*m.b37 - 96*m.b26*m.b35*m.b38 - 64*m.b26*m.b35*m.b39 - 32*
                       m.b26*m.b35*m.b40 - 224*m.b26*m.b36*m.b37 - 128*m.b26*m.b36*m.b38 - 64*m.b26*m.b36*m.b39 - 32*
                       m.b26*m.b36*m.b40 - 160*m.b26*m.b37*m.b38 - 64*m.b26*m.b37*m.b39 - 32*m.b26*m.b37*m.b40 - 96*
                       m.b26*m.b38*m.b39 - 32*m.b26*m.b38*m.b40 - 32*m.b26*m.b39*m.b40 - 768*m.b27*m.b28*m.b29 - 1056*
                       m.b27*m.b28*m.b30 - 928*m.b27*m.b28*m.b31 - 800*m.b27*m.b28*m.b32 - 672*m.b27*m.b28*m.b33 - 544*
                       m.b27*m.b28*m.b34 - 416*m.b27*m.b28*m.b35 - 352*m.b27*m.b28*m.b36 - 288*m.b27*m.b28*m.b37 - 224*
                       m.b27*m.b28*m.b38 - 160*m.b27*m.b28*m.b39 - 96*m.b27*m.b28*m.b40 - 32*m.b27*m.b28*m.b41 - 1056*
                       m.b27*m.b29*m.b30 - 576*m.b27*m.b29*m.b31 - 800*m.b27*m.b29*m.b32 - 672*m.b27*m.b29*m.b33 - 544*
                       m.b27*m.b29*m.b34 - 416*m.b27*m.b29*m.b35 - 320*m.b27*m.b29*m.b36 - 256*m.b27*m.b29*m.b37 - 192*
                       m.b27*m.b29*m.b38 - 128*m.b27*m.b29*m.b39 - 64*m.b27*m.b29*m.b40 - 32*m.b27*m.b29*m.b41 - 928*
                       m.b27*m.b30*m.b31 - 800*m.b27*m.b30*m.b32 - 384*m.b27*m.b30*m.b33 - 544*m.b27*m.b30*m.b34 - 416*
                       m.b27*m.b30*m.b35 - 288*m.b27*m.b30*m.b36 - 224*m.b27*m.b30*m.b37 - 160*m.b27*m.b30*m.b38 - 96*
                       m.b27*m.b30*m.b39 - 64*m.b27*m.b30*m.b40 - 32*m.b27*m.b30*m.b41 - 800*m.b27*m.b31*m.b32 - 672*
                       m.b27*m.b31*m.b33 - 544*m.b27*m.b31*m.b34 - 192*m.b27*m.b31*m.b35 - 288*m.b27*m.b31*m.b36 - 192*
                       m.b27*m.b31*m.b37 - 128*m.b27*m.b31*m.b38 - 96*m.b27*m.b31*m.b39 - 64*m.b27*m.b31*m.b40 - 32*
                       m.b27*m.b31*m.b41 - 672*m.b27*m.b32*m.b33 - 544*m.b27*m.b32*m.b34 - 416*m.b27*m.b32*m.b35 - 288*
                       m.b27*m.b32*m.b36 - 128*m.b27*m.b32*m.b38 - 96*m.b27*m.b32*m.b39 - 64*m.b27*m.b32*m.b40 - 32*
                       m.b27*m.b32*m.b41 - 544*m.b27*m.b33*m.b34 - 416*m.b27*m.b33*m.b35 - 288*m.b27*m.b33*m.b36 - 192*
                       m.b27*m.b33*m.b37 - 128*m.b27*m.b33*m.b38 - 64*m.b27*m.b33*m.b40 - 32*m.b27*m.b33*m.b41 - 416*
                       m.b27*m.b34*m.b35 - 320*m.b27*m.b34*m.b36 - 224*m.b27*m.b34*m.b37 - 128*m.b27*m.b34*m.b38 - 96*
                       m.b27*m.b34*m.b39 - 64*m.b27*m.b34*m.b40 - 352*m.b27*m.b35*m.b36 - 256*m.b27*m.b35*m.b37 - 160*
                       m.b27*m.b35*m.b38 - 96*m.b27*m.b35*m.b39 - 64*m.b27*m.b35*m.b40 - 32*m.b27*m.b35*m.b41 - 288*
                       m.b27*m.b36*m.b37 - 192*m.b27*m.b36*m.b38 - 96*m.b27*m.b36*m.b39 - 64*m.b27*m.b36*m.b40 - 32*
                       m.b27*m.b36*m.b41 - 224*m.b27*m.b37*m.b38 - 128*m.b27*m.b37*m.b39 - 64*m.b27*m.b37*m.b40 - 32*
                       m.b27*m.b37*m.b41 - 160*m.b27*m.b38*m.b39 - 64*m.b27*m.b38*m.b40 - 32*m.b27*m.b38*m.b41 - 96*
                       m.b27*m.b39*m.b40 - 32*m.b27*m.b39*m.b41 - 32*m.b27*m.b40*m.b41 - 768*m.b28*m.b29*m.b30 - 1056*
                       m.b28*m.b29*m.b31 - 928*m.b28*m.b29*m.b32 - 800*m.b28*m.b29*m.b33 - 672*m.b28*m.b29*m.b34 - 544*
                       m.b28*m.b29*m.b35 - 416*m.b28*m.b29*m.b36 - 352*m.b28*m.b29*m.b37 - 288*m.b28*m.b29*m.b38 - 224*
                       m.b28*m.b29*m.b39 - 160*m.b28*m.b29*m.b40 - 96*m.b28*m.b29*m.b41 - 32*m.b28*m.b29*m.b42 - 1056*
                       m.b28*m.b30*m.b31 - 576*m.b28*m.b30*m.b32 - 800*m.b28*m.b30*m.b33 - 672*m.b28*m.b30*m.b34 - 544*
                       m.b28*m.b30*m.b35 - 416*m.b28*m.b30*m.b36 - 320*m.b28*m.b30*m.b37 - 256*m.b28*m.b30*m.b38 - 192*
                       m.b28*m.b30*m.b39 - 128*m.b28*m.b30*m.b40 - 64*m.b28*m.b30*m.b41 - 32*m.b28*m.b30*m.b42 - 928*
                       m.b28*m.b31*m.b32 - 800*m.b28*m.b31*m.b33 - 384*m.b28*m.b31*m.b34 - 544*m.b28*m.b31*m.b35 - 416*
                       m.b28*m.b31*m.b36 - 288*m.b28*m.b31*m.b37 - 224*m.b28*m.b31*m.b38 - 160*m.b28*m.b31*m.b39 - 96*
                       m.b28*m.b31*m.b40 - 64*m.b28*m.b31*m.b41 - 32*m.b28*m.b31*m.b42 - 800*m.b28*m.b32*m.b33 - 672*
                       m.b28*m.b32*m.b34 - 544*m.b28*m.b32*m.b35 - 192*m.b28*m.b32*m.b36 - 288*m.b28*m.b32*m.b37 - 192*
                       m.b28*m.b32*m.b38 - 128*m.b28*m.b32*m.b39 - 96*m.b28*m.b32*m.b40 - 64*m.b28*m.b32*m.b41 - 32*
                       m.b28*m.b32*m.b42 - 672*m.b28*m.b33*m.b34 - 544*m.b28*m.b33*m.b35 - 416*m.b28*m.b33*m.b36 - 288*
                       m.b28*m.b33*m.b37 - 128*m.b28*m.b33*m.b39 - 96*m.b28*m.b33*m.b40 - 64*m.b28*m.b33*m.b41 - 32*
                       m.b28*m.b33*m.b42 - 544*m.b28*m.b34*m.b35 - 416*m.b28*m.b34*m.b36 - 288*m.b28*m.b34*m.b37 - 192*
                       m.b28*m.b34*m.b38 - 128*m.b28*m.b34*m.b39 - 64*m.b28*m.b34*m.b41 - 32*m.b28*m.b34*m.b42 - 416*
                       m.b28*m.b35*m.b36 - 320*m.b28*m.b35*m.b37 - 224*m.b28*m.b35*m.b38 - 128*m.b28*m.b35*m.b39 - 96*
                       m.b28*m.b35*m.b40 - 64*m.b28*m.b35*m.b41 - 352*m.b28*m.b36*m.b37 - 256*m.b28*m.b36*m.b38 - 160*
                       m.b28*m.b36*m.b39 - 96*m.b28*m.b36*m.b40 - 64*m.b28*m.b36*m.b41 - 32*m.b28*m.b36*m.b42 - 288*
                       m.b28*m.b37*m.b38 - 192*m.b28*m.b37*m.b39 - 96*m.b28*m.b37*m.b40 - 64*m.b28*m.b37*m.b41 - 32*
                       m.b28*m.b37*m.b42 - 224*m.b28*m.b38*m.b39 - 128*m.b28*m.b38*m.b40 - 64*m.b28*m.b38*m.b41 - 32*
                       m.b28*m.b38*m.b42 - 160*m.b28*m.b39*m.b40 - 64*m.b28*m.b39*m.b41 - 32*m.b28*m.b39*m.b42 - 96*
                       m.b28*m.b40*m.b41 - 32*m.b28*m.b40*m.b42 - 32*m.b28*m.b41*m.b42 - 768*m.b29*m.b30*m.b31 - 1056*
                       m.b29*m.b30*m.b32 - 928*m.b29*m.b30*m.b33 - 800*m.b29*m.b30*m.b34 - 672*m.b29*m.b30*m.b35 - 544*
                       m.b29*m.b30*m.b36 - 416*m.b29*m.b30*m.b37 - 352*m.b29*m.b30*m.b38 - 288*m.b29*m.b30*m.b39 - 224*
                       m.b29*m.b30*m.b40 - 160*m.b29*m.b30*m.b41 - 96*m.b29*m.b30*m.b42 - 32*m.b29*m.b30*m.b43 - 1056*
                       m.b29*m.b31*m.b32 - 576*m.b29*m.b31*m.b33 - 800*m.b29*m.b31*m.b34 - 672*m.b29*m.b31*m.b35 - 544*
                       m.b29*m.b31*m.b36 - 416*m.b29*m.b31*m.b37 - 320*m.b29*m.b31*m.b38 - 256*m.b29*m.b31*m.b39 - 192*
                       m.b29*m.b31*m.b40 - 128*m.b29*m.b31*m.b41 - 64*m.b29*m.b31*m.b42 - 32*m.b29*m.b31*m.b43 - 928*
                       m.b29*m.b32*m.b33 - 800*m.b29*m.b32*m.b34 - 384*m.b29*m.b32*m.b35 - 544*m.b29*m.b32*m.b36 - 416*
                       m.b29*m.b32*m.b37 - 288*m.b29*m.b32*m.b38 - 224*m.b29*m.b32*m.b39 - 160*m.b29*m.b32*m.b40 - 96*
                       m.b29*m.b32*m.b41 - 64*m.b29*m.b32*m.b42 - 32*m.b29*m.b32*m.b43 - 800*m.b29*m.b33*m.b34 - 672*
                       m.b29*m.b33*m.b35 - 544*m.b29*m.b33*m.b36 - 192*m.b29*m.b33*m.b37 - 288*m.b29*m.b33*m.b38 - 192*
                       m.b29*m.b33*m.b39 - 128*m.b29*m.b33*m.b40 - 96*m.b29*m.b33*m.b41 - 64*m.b29*m.b33*m.b42 - 32*
                       m.b29*m.b33*m.b43 - 672*m.b29*m.b34*m.b35 - 544*m.b29*m.b34*m.b36 - 416*m.b29*m.b34*m.b37 - 288*
                       m.b29*m.b34*m.b38 - 128*m.b29*m.b34*m.b40 - 96*m.b29*m.b34*m.b41 - 64*m.b29*m.b34*m.b42 - 32*
                       m.b29*m.b34*m.b43 - 544*m.b29*m.b35*m.b36 - 416*m.b29*m.b35*m.b37 - 288*m.b29*m.b35*m.b38 - 192*
                       m.b29*m.b35*m.b39 - 128*m.b29*m.b35*m.b40 - 64*m.b29*m.b35*m.b42 - 32*m.b29*m.b35*m.b43 - 416*
                       m.b29*m.b36*m.b37 - 320*m.b29*m.b36*m.b38 - 224*m.b29*m.b36*m.b39 - 128*m.b29*m.b36*m.b40 - 96*
                       m.b29*m.b36*m.b41 - 64*m.b29*m.b36*m.b42 - 352*m.b29*m.b37*m.b38 - 256*m.b29*m.b37*m.b39 - 160*
                       m.b29*m.b37*m.b40 - 96*m.b29*m.b37*m.b41 - 64*m.b29*m.b37*m.b42 - 32*m.b29*m.b37*m.b43 - 288*
                       m.b29*m.b38*m.b39 - 192*m.b29*m.b38*m.b40 - 96*m.b29*m.b38*m.b41 - 64*m.b29*m.b38*m.b42 - 32*
                       m.b29*m.b38*m.b43 - 224*m.b29*m.b39*m.b40 - 128*m.b29*m.b39*m.b41 - 64*m.b29*m.b39*m.b42 - 32*
                       m.b29*m.b39*m.b43 - 160*m.b29*m.b40*m.b41 - 64*m.b29*m.b40*m.b42 - 32*m.b29*m.b40*m.b43 - 96*
                       m.b29*m.b41*m.b42 - 32*m.b29*m.b41*m.b43 - 32*m.b29*m.b42*m.b43 - 768*m.b30*m.b31*m.b32 - 1056*
                       m.b30*m.b31*m.b33 - 928*m.b30*m.b31*m.b34 - 800*m.b30*m.b31*m.b35 - 672*m.b30*m.b31*m.b36 - 544*
                       m.b30*m.b31*m.b37 - 416*m.b30*m.b31*m.b38 - 352*m.b30*m.b31*m.b39 - 288*m.b30*m.b31*m.b40 - 224*
                       m.b30*m.b31*m.b41 - 160*m.b30*m.b31*m.b42 - 96*m.b30*m.b31*m.b43 - 32*m.b30*m.b31*m.b44 - 1056*
                       m.b30*m.b32*m.b33 - 576*m.b30*m.b32*m.b34 - 800*m.b30*m.b32*m.b35 - 672*m.b30*m.b32*m.b36 - 544*
                       m.b30*m.b32*m.b37 - 416*m.b30*m.b32*m.b38 - 320*m.b30*m.b32*m.b39 - 256*m.b30*m.b32*m.b40 - 192*
                       m.b30*m.b32*m.b41 - 128*m.b30*m.b32*m.b42 - 64*m.b30*m.b32*m.b43 - 32*m.b30*m.b32*m.b44 - 928*
                       m.b30*m.b33*m.b34 - 800*m.b30*m.b33*m.b35 - 384*m.b30*m.b33*m.b36 - 544*m.b30*m.b33*m.b37 - 416*
                       m.b30*m.b33*m.b38 - 288*m.b30*m.b33*m.b39 - 224*m.b30*m.b33*m.b40 - 160*m.b30*m.b33*m.b41 - 96*
                       m.b30*m.b33*m.b42 - 64*m.b30*m.b33*m.b43 - 32*m.b30*m.b33*m.b44 - 800*m.b30*m.b34*m.b35 - 672*
                       m.b30*m.b34*m.b36 - 544*m.b30*m.b34*m.b37 - 192*m.b30*m.b34*m.b38 - 288*m.b30*m.b34*m.b39 - 192*
                       m.b30*m.b34*m.b40 - 128*m.b30*m.b34*m.b41 - 96*m.b30*m.b34*m.b42 - 64*m.b30*m.b34*m.b43 - 32*
                       m.b30*m.b34*m.b44 - 672*m.b30*m.b35*m.b36 - 544*m.b30*m.b35*m.b37 - 416*m.b30*m.b35*m.b38 - 288*
                       m.b30*m.b35*m.b39 - 128*m.b30*m.b35*m.b41 - 96*m.b30*m.b35*m.b42 - 64*m.b30*m.b35*m.b43 - 32*
                       m.b30*m.b35*m.b44 - 544*m.b30*m.b36*m.b37 - 416*m.b30*m.b36*m.b38 - 288*m.b30*m.b36*m.b39 - 192*
                       m.b30*m.b36*m.b40 - 128*m.b30*m.b36*m.b41 - 64*m.b30*m.b36*m.b43 - 32*m.b30*m.b36*m.b44 - 416*
                       m.b30*m.b37*m.b38 - 320*m.b30*m.b37*m.b39 - 224*m.b30*m.b37*m.b40 - 128*m.b30*m.b37*m.b41 - 96*
                       m.b30*m.b37*m.b42 - 64*m.b30*m.b37*m.b43 - 352*m.b30*m.b38*m.b39 - 256*m.b30*m.b38*m.b40 - 160*
                       m.b30*m.b38*m.b41 - 96*m.b30*m.b38*m.b42 - 64*m.b30*m.b38*m.b43 - 32*m.b30*m.b38*m.b44 - 288*
                       m.b30*m.b39*m.b40 - 192*m.b30*m.b39*m.b41 - 96*m.b30*m.b39*m.b42 - 64*m.b30*m.b39*m.b43 - 32*
                       m.b30*m.b39*m.b44 - 224*m.b30*m.b40*m.b41 - 128*m.b30*m.b40*m.b42 - 64*m.b30*m.b40*m.b43 - 32*
                       m.b30*m.b40*m.b44 - 160*m.b30*m.b41*m.b42 - 64*m.b30*m.b41*m.b43 - 32*m.b30*m.b41*m.b44 - 96*
                       m.b30*m.b42*m.b43 - 32*m.b30*m.b42*m.b44 - 32*m.b30*m.b43*m.b44 - 768*m.b31*m.b32*m.b33 - 1056*
                       m.b31*m.b32*m.b34 - 928*m.b31*m.b32*m.b35 - 800*m.b31*m.b32*m.b36 - 672*m.b31*m.b32*m.b37 - 544*
                       m.b31*m.b32*m.b38 - 416*m.b31*m.b32*m.b39 - 352*m.b31*m.b32*m.b40 - 288*m.b31*m.b32*m.b41 - 224*
                       m.b31*m.b32*m.b42 - 160*m.b31*m.b32*m.b43 - 96*m.b31*m.b32*m.b44 - 32*m.b31*m.b32*m.b45 - 1056*
                       m.b31*m.b33*m.b34 - 576*m.b31*m.b33*m.b35 - 800*m.b31*m.b33*m.b36 - 672*m.b31*m.b33*m.b37 - 544*
                       m.b31*m.b33*m.b38 - 416*m.b31*m.b33*m.b39 - 320*m.b31*m.b33*m.b40 - 256*m.b31*m.b33*m.b41 - 192*
                       m.b31*m.b33*m.b42 - 128*m.b31*m.b33*m.b43 - 64*m.b31*m.b33*m.b44 - 32*m.b31*m.b33*m.b45 - 928*
                       m.b31*m.b34*m.b35 - 800*m.b31*m.b34*m.b36 - 384*m.b31*m.b34*m.b37 - 544*m.b31*m.b34*m.b38 - 416*
                       m.b31*m.b34*m.b39 - 288*m.b31*m.b34*m.b40 - 224*m.b31*m.b34*m.b41 - 160*m.b31*m.b34*m.b42 - 96*
                       m.b31*m.b34*m.b43 - 64*m.b31*m.b34*m.b44 - 32*m.b31*m.b34*m.b45 - 800*m.b31*m.b35*m.b36 - 672*
                       m.b31*m.b35*m.b37 - 544*m.b31*m.b35*m.b38 - 192*m.b31*m.b35*m.b39 - 288*m.b31*m.b35*m.b40 - 192*
                       m.b31*m.b35*m.b41 - 128*m.b31*m.b35*m.b42 - 96*m.b31*m.b35*m.b43 - 64*m.b31*m.b35*m.b44 - 32*
                       m.b31*m.b35*m.b45 - 672*m.b31*m.b36*m.b37 - 544*m.b31*m.b36*m.b38 - 416*m.b31*m.b36*m.b39 - 288*
                       m.b31*m.b36*m.b40 - 128*m.b31*m.b36*m.b42 - 96*m.b31*m.b36*m.b43 - 64*m.b31*m.b36*m.b44 - 32*
                       m.b31*m.b36*m.b45 - 544*m.b31*m.b37*m.b38 - 416*m.b31*m.b37*m.b39 - 288*m.b31*m.b37*m.b40 - 192*
                       m.b31*m.b37*m.b41 - 128*m.b31*m.b37*m.b42 - 64*m.b31*m.b37*m.b44 - 32*m.b31*m.b37*m.b45 - 416*
                       m.b31*m.b38*m.b39 - 320*m.b31*m.b38*m.b40 - 224*m.b31*m.b38*m.b41 - 128*m.b31*m.b38*m.b42 - 96*
                       m.b31*m.b38*m.b43 - 64*m.b31*m.b38*m.b44 - 352*m.b31*m.b39*m.b40 - 256*m.b31*m.b39*m.b41 - 160*
                       m.b31*m.b39*m.b42 - 96*m.b31*m.b39*m.b43 - 64*m.b31*m.b39*m.b44 - 32*m.b31*m.b39*m.b45 - 288*
                       m.b31*m.b40*m.b41 - 192*m.b31*m.b40*m.b42 - 96*m.b31*m.b40*m.b43 - 64*m.b31*m.b40*m.b44 - 32*
                       m.b31*m.b40*m.b45 - 224*m.b31*m.b41*m.b42 - 128*m.b31*m.b41*m.b43 - 64*m.b31*m.b41*m.b44 - 32*
                       m.b31*m.b41*m.b45 - 160*m.b31*m.b42*m.b43 - 64*m.b31*m.b42*m.b44 - 32*m.b31*m.b42*m.b45 - 96*
                       m.b31*m.b43*m.b44 - 32*m.b31*m.b43*m.b45 - 32*m.b31*m.b44*m.b45 - 768*m.b32*m.b33*m.b34 - 1056*
                       m.b32*m.b33*m.b35 - 928*m.b32*m.b33*m.b36 - 800*m.b32*m.b33*m.b37 - 672*m.b32*m.b33*m.b38 - 544*
                       m.b32*m.b33*m.b39 - 416*m.b32*m.b33*m.b40 - 352*m.b32*m.b33*m.b41 - 288*m.b32*m.b33*m.b42 - 224*
                       m.b32*m.b33*m.b43 - 160*m.b32*m.b33*m.b44 - 96*m.b32*m.b33*m.b45 - 32*m.b32*m.b33*m.b46 - 1056*
                       m.b32*m.b34*m.b35 - 576*m.b32*m.b34*m.b36 - 800*m.b32*m.b34*m.b37 - 672*m.b32*m.b34*m.b38 - 544*
                       m.b32*m.b34*m.b39 - 416*m.b32*m.b34*m.b40 - 320*m.b32*m.b34*m.b41 - 256*m.b32*m.b34*m.b42 - 192*
                       m.b32*m.b34*m.b43 - 128*m.b32*m.b34*m.b44 - 64*m.b32*m.b34*m.b45 - 32*m.b32*m.b34*m.b46 - 928*
                       m.b32*m.b35*m.b36 - 800*m.b32*m.b35*m.b37 - 384*m.b32*m.b35*m.b38 - 544*m.b32*m.b35*m.b39 - 416*
                       m.b32*m.b35*m.b40 - 288*m.b32*m.b35*m.b41 - 224*m.b32*m.b35*m.b42 - 160*m.b32*m.b35*m.b43 - 96*
                       m.b32*m.b35*m.b44 - 64*m.b32*m.b35*m.b45 - 32*m.b32*m.b35*m.b46 - 800*m.b32*m.b36*m.b37 - 672*
                       m.b32*m.b36*m.b38 - 544*m.b32*m.b36*m.b39 - 192*m.b32*m.b36*m.b40 - 288*m.b32*m.b36*m.b41 - 192*
                       m.b32*m.b36*m.b42 - 128*m.b32*m.b36*m.b43 - 96*m.b32*m.b36*m.b44 - 64*m.b32*m.b36*m.b45 - 32*
                       m.b32*m.b36*m.b46 - 672*m.b32*m.b37*m.b38 - 544*m.b32*m.b37*m.b39 - 416*m.b32*m.b37*m.b40 - 288*
                       m.b32*m.b37*m.b41 - 128*m.b32*m.b37*m.b43 - 96*m.b32*m.b37*m.b44 - 64*m.b32*m.b37*m.b45 - 32*
                       m.b32*m.b37*m.b46 - 544*m.b32*m.b38*m.b39 - 416*m.b32*m.b38*m.b40 - 288*m.b32*m.b38*m.b41 - 192*
                       m.b32*m.b38*m.b42 - 128*m.b32*m.b38*m.b43 - 64*m.b32*m.b38*m.b45 - 32*m.b32*m.b38*m.b46 - 416*
                       m.b32*m.b39*m.b40 - 320*m.b32*m.b39*m.b41 - 224*m.b32*m.b39*m.b42 - 128*m.b32*m.b39*m.b43 - 96*
                       m.b32*m.b39*m.b44 - 64*m.b32*m.b39*m.b45 - 352*m.b32*m.b40*m.b41 - 256*m.b32*m.b40*m.b42 - 160*
                       m.b32*m.b40*m.b43 - 96*m.b32*m.b40*m.b44 - 64*m.b32*m.b40*m.b45 - 32*m.b32*m.b40*m.b46 - 288*
                       m.b32*m.b41*m.b42 - 192*m.b32*m.b41*m.b43 - 96*m.b32*m.b41*m.b44 - 64*m.b32*m.b41*m.b45 - 32*
                       m.b32*m.b41*m.b46 - 224*m.b32*m.b42*m.b43 - 128*m.b32*m.b42*m.b44 - 64*m.b32*m.b42*m.b45 - 32*
                       m.b32*m.b42*m.b46 - 160*m.b32*m.b43*m.b44 - 64*m.b32*m.b43*m.b45 - 32*m.b32*m.b43*m.b46 - 96*
                       m.b32*m.b44*m.b45 - 32*m.b32*m.b44*m.b46 - 32*m.b32*m.b45*m.b46 - 768*m.b33*m.b34*m.b35 - 1056*
                       m.b33*m.b34*m.b36 - 928*m.b33*m.b34*m.b37 - 800*m.b33*m.b34*m.b38 - 672*m.b33*m.b34*m.b39 - 544*
                       m.b33*m.b34*m.b40 - 416*m.b33*m.b34*m.b41 - 352*m.b33*m.b34*m.b42 - 288*m.b33*m.b34*m.b43 - 224*
                       m.b33*m.b34*m.b44 - 160*m.b33*m.b34*m.b45 - 96*m.b33*m.b34*m.b46 - 32*m.b33*m.b34*m.b47 - 1056*
                       m.b33*m.b35*m.b36 - 576*m.b33*m.b35*m.b37 - 800*m.b33*m.b35*m.b38 - 672*m.b33*m.b35*m.b39 - 544*
                       m.b33*m.b35*m.b40 - 416*m.b33*m.b35*m.b41 - 320*m.b33*m.b35*m.b42 - 256*m.b33*m.b35*m.b43 - 192*
                       m.b33*m.b35*m.b44 - 128*m.b33*m.b35*m.b45 - 64*m.b33*m.b35*m.b46 - 32*m.b33*m.b35*m.b47 - 928*
                       m.b33*m.b36*m.b37 - 800*m.b33*m.b36*m.b38 - 384*m.b33*m.b36*m.b39 - 544*m.b33*m.b36*m.b40 - 416*
                       m.b33*m.b36*m.b41 - 288*m.b33*m.b36*m.b42 - 224*m.b33*m.b36*m.b43 - 160*m.b33*m.b36*m.b44 - 96*
                       m.b33*m.b36*m.b45 - 64*m.b33*m.b36*m.b46 - 32*m.b33*m.b36*m.b47 - 800*m.b33*m.b37*m.b38 - 672*
                       m.b33*m.b37*m.b39 - 544*m.b33*m.b37*m.b40 - 192*m.b33*m.b37*m.b41 - 288*m.b33*m.b37*m.b42 - 192*
                       m.b33*m.b37*m.b43 - 128*m.b33*m.b37*m.b44 - 96*m.b33*m.b37*m.b45 - 64*m.b33*m.b37*m.b46 - 32*
                       m.b33*m.b37*m.b47 - 672*m.b33*m.b38*m.b39 - 544*m.b33*m.b38*m.b40 - 416*m.b33*m.b38*m.b41 - 288*
                       m.b33*m.b38*m.b42 - 128*m.b33*m.b38*m.b44 - 96*m.b33*m.b38*m.b45 - 64*m.b33*m.b38*m.b46 - 32*
                       m.b33*m.b38*m.b47 - 544*m.b33*m.b39*m.b40 - 416*m.b33*m.b39*m.b41 - 288*m.b33*m.b39*m.b42 - 192*
                       m.b33*m.b39*m.b43 - 128*m.b33*m.b39*m.b44 - 64*m.b33*m.b39*m.b46 - 32*m.b33*m.b39*m.b47 - 416*
                       m.b33*m.b40*m.b41 - 320*m.b33*m.b40*m.b42 - 224*m.b33*m.b40*m.b43 - 128*m.b33*m.b40*m.b44 - 96*
                       m.b33*m.b40*m.b45 - 64*m.b33*m.b40*m.b46 - 352*m.b33*m.b41*m.b42 - 256*m.b33*m.b41*m.b43 - 160*
                       m.b33*m.b41*m.b44 - 96*m.b33*m.b41*m.b45 - 64*m.b33*m.b41*m.b46 - 32*m.b33*m.b41*m.b47 - 288*
                       m.b33*m.b42*m.b43 - 192*m.b33*m.b42*m.b44 - 96*m.b33*m.b42*m.b45 - 64*m.b33*m.b42*m.b46 - 32*
                       m.b33*m.b42*m.b47 - 224*m.b33*m.b43*m.b44 - 128*m.b33*m.b43*m.b45 - 64*m.b33*m.b43*m.b46 - 32*
                       m.b33*m.b43*m.b47 - 160*m.b33*m.b44*m.b45 - 64*m.b33*m.b44*m.b46 - 32*m.b33*m.b44*m.b47 - 96*
                       m.b33*m.b45*m.b46 - 32*m.b33*m.b45*m.b47 - 32*m.b33*m.b46*m.b47 - 768*m.b34*m.b35*m.b36 - 1056*
                       m.b34*m.b35*m.b37 - 928*m.b34*m.b35*m.b38 - 800*m.b34*m.b35*m.b39 - 672*m.b34*m.b35*m.b40 - 544*
                       m.b34*m.b35*m.b41 - 416*m.b34*m.b35*m.b42 - 352*m.b34*m.b35*m.b43 - 288*m.b34*m.b35*m.b44 - 224*
                       m.b34*m.b35*m.b45 - 160*m.b34*m.b35*m.b46 - 96*m.b34*m.b35*m.b47 - 32*m.b34*m.b35*m.b48 - 1056*
                       m.b34*m.b36*m.b37 - 576*m.b34*m.b36*m.b38 - 800*m.b34*m.b36*m.b39 - 672*m.b34*m.b36*m.b40 - 544*
                       m.b34*m.b36*m.b41 - 416*m.b34*m.b36*m.b42 - 320*m.b34*m.b36*m.b43 - 256*m.b34*m.b36*m.b44 - 192*
                       m.b34*m.b36*m.b45 - 128*m.b34*m.b36*m.b46 - 64*m.b34*m.b36*m.b47 - 32*m.b34*m.b36*m.b48 - 928*
                       m.b34*m.b37*m.b38 - 800*m.b34*m.b37*m.b39 - 384*m.b34*m.b37*m.b40 - 544*m.b34*m.b37*m.b41 - 416*
                       m.b34*m.b37*m.b42 - 288*m.b34*m.b37*m.b43 - 224*m.b34*m.b37*m.b44 - 160*m.b34*m.b37*m.b45 - 96*
                       m.b34*m.b37*m.b46 - 64*m.b34*m.b37*m.b47 - 32*m.b34*m.b37*m.b48 - 800*m.b34*m.b38*m.b39 - 672*
                       m.b34*m.b38*m.b40 - 544*m.b34*m.b38*m.b41 - 192*m.b34*m.b38*m.b42 - 288*m.b34*m.b38*m.b43 - 192*
                       m.b34*m.b38*m.b44 - 128*m.b34*m.b38*m.b45 - 96*m.b34*m.b38*m.b46 - 64*m.b34*m.b38*m.b47 - 32*
                       m.b34*m.b38*m.b48 - 672*m.b34*m.b39*m.b40 - 544*m.b34*m.b39*m.b41 - 416*m.b34*m.b39*m.b42 - 288*
                       m.b34*m.b39*m.b43 - 128*m.b34*m.b39*m.b45 - 96*m.b34*m.b39*m.b46 - 64*m.b34*m.b39*m.b47 - 32*
                       m.b34*m.b39*m.b48 - 544*m.b34*m.b40*m.b41 - 416*m.b34*m.b40*m.b42 - 288*m.b34*m.b40*m.b43 - 192*
                       m.b34*m.b40*m.b44 - 128*m.b34*m.b40*m.b45 - 64*m.b34*m.b40*m.b47 - 32*m.b34*m.b40*m.b48 - 416*
                       m.b34*m.b41*m.b42 - 320*m.b34*m.b41*m.b43 - 224*m.b34*m.b41*m.b44 - 128*m.b34*m.b41*m.b45 - 96*
                       m.b34*m.b41*m.b46 - 64*m.b34*m.b41*m.b47 - 352*m.b34*m.b42*m.b43 - 256*m.b34*m.b42*m.b44 - 160*
                       m.b34*m.b42*m.b45 - 96*m.b34*m.b42*m.b46 - 64*m.b34*m.b42*m.b47 - 32*m.b34*m.b42*m.b48 - 288*
                       m.b34*m.b43*m.b44 - 192*m.b34*m.b43*m.b45 - 96*m.b34*m.b43*m.b46 - 64*m.b34*m.b43*m.b47 - 32*
                       m.b34*m.b43*m.b48 - 224*m.b34*m.b44*m.b45 - 128*m.b34*m.b44*m.b46 - 64*m.b34*m.b44*m.b47 - 32*
                       m.b34*m.b44*m.b48 - 160*m.b34*m.b45*m.b46 - 64*m.b34*m.b45*m.b47 - 32*m.b34*m.b45*m.b48 - 96*
                       m.b34*m.b46*m.b47 - 32*m.b34*m.b46*m.b48 - 32*m.b34*m.b47*m.b48 - 768*m.b35*m.b36*m.b37 - 1056*
                       m.b35*m.b36*m.b38 - 928*m.b35*m.b36*m.b39 - 800*m.b35*m.b36*m.b40 - 672*m.b35*m.b36*m.b41 - 544*
                       m.b35*m.b36*m.b42 - 416*m.b35*m.b36*m.b43 - 352*m.b35*m.b36*m.b44 - 288*m.b35*m.b36*m.b45 - 224*
                       m.b35*m.b36*m.b46 - 160*m.b35*m.b36*m.b47 - 96*m.b35*m.b36*m.b48 - 32*m.b35*m.b36*m.b49 - 1056*
                       m.b35*m.b37*m.b38 - 576*m.b35*m.b37*m.b39 - 800*m.b35*m.b37*m.b40 - 672*m.b35*m.b37*m.b41 - 544*
                       m.b35*m.b37*m.b42 - 416*m.b35*m.b37*m.b43 - 320*m.b35*m.b37*m.b44 - 256*m.b35*m.b37*m.b45 - 192*
                       m.b35*m.b37*m.b46 - 128*m.b35*m.b37*m.b47 - 64*m.b35*m.b37*m.b48 - 32*m.b35*m.b37*m.b49 - 928*
                       m.b35*m.b38*m.b39 - 800*m.b35*m.b38*m.b40 - 384*m.b35*m.b38*m.b41 - 544*m.b35*m.b38*m.b42 - 416*
                       m.b35*m.b38*m.b43 - 288*m.b35*m.b38*m.b44 - 224*m.b35*m.b38*m.b45 - 160*m.b35*m.b38*m.b46 - 96*
                       m.b35*m.b38*m.b47 - 64*m.b35*m.b38*m.b48 - 32*m.b35*m.b38*m.b49 - 800*m.b35*m.b39*m.b40 - 672*
                       m.b35*m.b39*m.b41 - 544*m.b35*m.b39*m.b42 - 192*m.b35*m.b39*m.b43 - 288*m.b35*m.b39*m.b44 - 192*
                       m.b35*m.b39*m.b45 - 128*m.b35*m.b39*m.b46 - 96*m.b35*m.b39*m.b47 - 64*m.b35*m.b39*m.b48 - 32*
                       m.b35*m.b39*m.b49 - 672*m.b35*m.b40*m.b41 - 544*m.b35*m.b40*m.b42 - 416*m.b35*m.b40*m.b43 - 288*
                       m.b35*m.b40*m.b44 - 128*m.b35*m.b40*m.b46 - 96*m.b35*m.b40*m.b47 - 64*m.b35*m.b40*m.b48 - 32*
                       m.b35*m.b40*m.b49 - 544*m.b35*m.b41*m.b42 - 416*m.b35*m.b41*m.b43 - 288*m.b35*m.b41*m.b44 - 192*
                       m.b35*m.b41*m.b45 - 128*m.b35*m.b41*m.b46 - 64*m.b35*m.b41*m.b48 - 32*m.b35*m.b41*m.b49 - 416*
                       m.b35*m.b42*m.b43 - 320*m.b35*m.b42*m.b44 - 224*m.b35*m.b42*m.b45 - 128*m.b35*m.b42*m.b46 - 96*
                       m.b35*m.b42*m.b47 - 64*m.b35*m.b42*m.b48 - 352*m.b35*m.b43*m.b44 - 256*m.b35*m.b43*m.b45 - 160*
                       m.b35*m.b43*m.b46 - 96*m.b35*m.b43*m.b47 - 64*m.b35*m.b43*m.b48 - 32*m.b35*m.b43*m.b49 - 288*
                       m.b35*m.b44*m.b45 - 192*m.b35*m.b44*m.b46 - 96*m.b35*m.b44*m.b47 - 64*m.b35*m.b44*m.b48 - 32*
                       m.b35*m.b44*m.b49 - 224*m.b35*m.b45*m.b46 - 128*m.b35*m.b45*m.b47 - 64*m.b35*m.b45*m.b48 - 32*
                       m.b35*m.b45*m.b49 - 160*m.b35*m.b46*m.b47 - 64*m.b35*m.b46*m.b48 - 32*m.b35*m.b46*m.b49 - 96*
                       m.b35*m.b47*m.b48 - 32*m.b35*m.b47*m.b49 - 32*m.b35*m.b48*m.b49 - 768*m.b36*m.b37*m.b38 - 1056*
                       m.b36*m.b37*m.b39 - 928*m.b36*m.b37*m.b40 - 800*m.b36*m.b37*m.b41 - 672*m.b36*m.b37*m.b42 - 544*
                       m.b36*m.b37*m.b43 - 416*m.b36*m.b37*m.b44 - 352*m.b36*m.b37*m.b45 - 288*m.b36*m.b37*m.b46 - 224*
                       m.b36*m.b37*m.b47 - 160*m.b36*m.b37*m.b48 - 96*m.b36*m.b37*m.b49 - 32*m.b36*m.b37*m.b50 - 1056*
                       m.b36*m.b38*m.b39 - 576*m.b36*m.b38*m.b40 - 800*m.b36*m.b38*m.b41 - 672*m.b36*m.b38*m.b42 - 544*
                       m.b36*m.b38*m.b43 - 416*m.b36*m.b38*m.b44 - 320*m.b36*m.b38*m.b45 - 256*m.b36*m.b38*m.b46 - 192*
                       m.b36*m.b38*m.b47 - 128*m.b36*m.b38*m.b48 - 64*m.b36*m.b38*m.b49 - 32*m.b36*m.b38*m.b50 - 928*
                       m.b36*m.b39*m.b40 - 800*m.b36*m.b39*m.b41 - 384*m.b36*m.b39*m.b42 - 544*m.b36*m.b39*m.b43 - 416*
                       m.b36*m.b39*m.b44 - 288*m.b36*m.b39*m.b45 - 224*m.b36*m.b39*m.b46 - 160*m.b36*m.b39*m.b47 - 96*
                       m.b36*m.b39*m.b48 - 64*m.b36*m.b39*m.b49 - 32*m.b36*m.b39*m.b50 - 800*m.b36*m.b40*m.b41 - 672*
                       m.b36*m.b40*m.b42 - 544*m.b36*m.b40*m.b43 - 192*m.b36*m.b40*m.b44 - 288*m.b36*m.b40*m.b45 - 192*
                       m.b36*m.b40*m.b46 - 128*m.b36*m.b40*m.b47 - 96*m.b36*m.b40*m.b48 - 64*m.b36*m.b40*m.b49 - 32*
                       m.b36*m.b40*m.b50 - 672*m.b36*m.b41*m.b42 - 544*m.b36*m.b41*m.b43 - 416*m.b36*m.b41*m.b44 - 288*
                       m.b36*m.b41*m.b45 - 128*m.b36*m.b41*m.b47 - 96*m.b36*m.b41*m.b48 - 64*m.b36*m.b41*m.b49 - 32*
                       m.b36*m.b41*m.b50 - 544*m.b36*m.b42*m.b43 - 416*m.b36*m.b42*m.b44 - 288*m.b36*m.b42*m.b45 - 192*
                       m.b36*m.b42*m.b46 - 128*m.b36*m.b42*m.b47 - 64*m.b36*m.b42*m.b49 - 32*m.b36*m.b42*m.b50 - 416*
                       m.b36*m.b43*m.b44 - 320*m.b36*m.b43*m.b45 - 224*m.b36*m.b43*m.b46 - 128*m.b36*m.b43*m.b47 - 96*
                       m.b36*m.b43*m.b48 - 64*m.b36*m.b43*m.b49 - 352*m.b36*m.b44*m.b45 - 256*m.b36*m.b44*m.b46 - 160*
                       m.b36*m.b44*m.b47 - 96*m.b36*m.b44*m.b48 - 64*m.b36*m.b44*m.b49 - 32*m.b36*m.b44*m.b50 - 288*
                       m.b36*m.b45*m.b46 - 192*m.b36*m.b45*m.b47 - 96*m.b36*m.b45*m.b48 - 64*m.b36*m.b45*m.b49 - 32*
                       m.b36*m.b45*m.b50 - 224*m.b36*m.b46*m.b47 - 128*m.b36*m.b46*m.b48 - 64*m.b36*m.b46*m.b49 - 32*
                       m.b36*m.b46*m.b50 - 160*m.b36*m.b47*m.b48 - 64*m.b36*m.b47*m.b49 - 32*m.b36*m.b47*m.b50 - 96*
                       m.b36*m.b48*m.b49 - 32*m.b36*m.b48*m.b50 - 32*m.b36*m.b49*m.b50 - 768*m.b37*m.b38*m.b39 - 1056*
                       m.b37*m.b38*m.b40 - 928*m.b37*m.b38*m.b41 - 800*m.b37*m.b38*m.b42 - 672*m.b37*m.b38*m.b43 - 544*
                       m.b37*m.b38*m.b44 - 416*m.b37*m.b38*m.b45 - 352*m.b37*m.b38*m.b46 - 288*m.b37*m.b38*m.b47 - 224*
                       m.b37*m.b38*m.b48 - 160*m.b37*m.b38*m.b49 - 96*m.b37*m.b38*m.b50 - 32*m.b37*m.b38*m.b51 - 1056*
                       m.b37*m.b39*m.b40 - 576*m.b37*m.b39*m.b41 - 800*m.b37*m.b39*m.b42 - 672*m.b37*m.b39*m.b43 - 544*
                       m.b37*m.b39*m.b44 - 416*m.b37*m.b39*m.b45 - 320*m.b37*m.b39*m.b46 - 256*m.b37*m.b39*m.b47 - 192*
                       m.b37*m.b39*m.b48 - 128*m.b37*m.b39*m.b49 - 64*m.b37*m.b39*m.b50 - 32*m.b37*m.b39*m.b51 - 928*
                       m.b37*m.b40*m.b41 - 800*m.b37*m.b40*m.b42 - 384*m.b37*m.b40*m.b43 - 544*m.b37*m.b40*m.b44 - 416*
                       m.b37*m.b40*m.b45 - 288*m.b37*m.b40*m.b46 - 224*m.b37*m.b40*m.b47 - 160*m.b37*m.b40*m.b48 - 96*
                       m.b37*m.b40*m.b49 - 64*m.b37*m.b40*m.b50 - 32*m.b37*m.b40*m.b51 - 800*m.b37*m.b41*m.b42 - 672*
                       m.b37*m.b41*m.b43 - 544*m.b37*m.b41*m.b44 - 192*m.b37*m.b41*m.b45 - 288*m.b37*m.b41*m.b46 - 192*
                       m.b37*m.b41*m.b47 - 128*m.b37*m.b41*m.b48 - 96*m.b37*m.b41*m.b49 - 64*m.b37*m.b41*m.b50 - 32*
                       m.b37*m.b41*m.b51 - 672*m.b37*m.b42*m.b43 - 544*m.b37*m.b42*m.b44 - 416*m.b37*m.b42*m.b45 - 288*
                       m.b37*m.b42*m.b46 - 128*m.b37*m.b42*m.b48 - 96*m.b37*m.b42*m.b49 - 64*m.b37*m.b42*m.b50 - 32*
                       m.b37*m.b42*m.b51 - 544*m.b37*m.b43*m.b44 - 416*m.b37*m.b43*m.b45 - 288*m.b37*m.b43*m.b46 - 192*
                       m.b37*m.b43*m.b47 - 128*m.b37*m.b43*m.b48 - 64*m.b37*m.b43*m.b50 - 32*m.b37*m.b43*m.b51 - 416*
                       m.b37*m.b44*m.b45 - 320*m.b37*m.b44*m.b46 - 224*m.b37*m.b44*m.b47 - 128*m.b37*m.b44*m.b48 - 96*
                       m.b37*m.b44*m.b49 - 64*m.b37*m.b44*m.b50 - 352*m.b37*m.b45*m.b46 - 256*m.b37*m.b45*m.b47 - 160*
                       m.b37*m.b45*m.b48 - 96*m.b37*m.b45*m.b49 - 64*m.b37*m.b45*m.b50 - 32*m.b37*m.b45*m.b51 - 288*
                       m.b37*m.b46*m.b47 - 192*m.b37*m.b46*m.b48 - 96*m.b37*m.b46*m.b49 - 64*m.b37*m.b46*m.b50 - 32*
                       m.b37*m.b46*m.b51 - 224*m.b37*m.b47*m.b48 - 128*m.b37*m.b47*m.b49 - 64*m.b37*m.b47*m.b50 - 32*
                       m.b37*m.b47*m.b51 - 160*m.b37*m.b48*m.b49 - 64*m.b37*m.b48*m.b50 - 32*m.b37*m.b48*m.b51 - 96*
                       m.b37*m.b49*m.b50 - 32*m.b37*m.b49*m.b51 - 32*m.b37*m.b50*m.b51 - 768*m.b38*m.b39*m.b40 - 1056*
                       m.b38*m.b39*m.b41 - 928*m.b38*m.b39*m.b42 - 800*m.b38*m.b39*m.b43 - 672*m.b38*m.b39*m.b44 - 544*
                       m.b38*m.b39*m.b45 - 416*m.b38*m.b39*m.b46 - 352*m.b38*m.b39*m.b47 - 288*m.b38*m.b39*m.b48 - 224*
                       m.b38*m.b39*m.b49 - 160*m.b38*m.b39*m.b50 - 96*m.b38*m.b39*m.b51 - 32*m.b38*m.b39*m.b52 - 1056*
                       m.b38*m.b40*m.b41 - 576*m.b38*m.b40*m.b42 - 800*m.b38*m.b40*m.b43 - 672*m.b38*m.b40*m.b44 - 544*
                       m.b38*m.b40*m.b45 - 416*m.b38*m.b40*m.b46 - 320*m.b38*m.b40*m.b47 - 256*m.b38*m.b40*m.b48 - 192*
                       m.b38*m.b40*m.b49 - 128*m.b38*m.b40*m.b50 - 64*m.b38*m.b40*m.b51 - 32*m.b38*m.b40*m.b52 - 928*
                       m.b38*m.b41*m.b42 - 800*m.b38*m.b41*m.b43 - 384*m.b38*m.b41*m.b44 - 544*m.b38*m.b41*m.b45 - 416*
                       m.b38*m.b41*m.b46 - 288*m.b38*m.b41*m.b47 - 224*m.b38*m.b41*m.b48 - 160*m.b38*m.b41*m.b49 - 96*
                       m.b38*m.b41*m.b50 - 64*m.b38*m.b41*m.b51 - 32*m.b38*m.b41*m.b52 - 800*m.b38*m.b42*m.b43 - 672*
                       m.b38*m.b42*m.b44 - 544*m.b38*m.b42*m.b45 - 192*m.b38*m.b42*m.b46 - 288*m.b38*m.b42*m.b47 - 192*
                       m.b38*m.b42*m.b48 - 128*m.b38*m.b42*m.b49 - 96*m.b38*m.b42*m.b50 - 64*m.b38*m.b42*m.b51 - 32*
                       m.b38*m.b42*m.b52 - 672*m.b38*m.b43*m.b44 - 544*m.b38*m.b43*m.b45 - 416*m.b38*m.b43*m.b46 - 288*
                       m.b38*m.b43*m.b47 - 128*m.b38*m.b43*m.b49 - 96*m.b38*m.b43*m.b50 - 64*m.b38*m.b43*m.b51 - 32*
                       m.b38*m.b43*m.b52 - 544*m.b38*m.b44*m.b45 - 416*m.b38*m.b44*m.b46 - 288*m.b38*m.b44*m.b47 - 192*
                       m.b38*m.b44*m.b48 - 128*m.b38*m.b44*m.b49 - 64*m.b38*m.b44*m.b51 - 32*m.b38*m.b44*m.b52 - 416*
                       m.b38*m.b45*m.b46 - 320*m.b38*m.b45*m.b47 - 224*m.b38*m.b45*m.b48 - 128*m.b38*m.b45*m.b49 - 96*
                       m.b38*m.b45*m.b50 - 64*m.b38*m.b45*m.b51 - 352*m.b38*m.b46*m.b47 - 256*m.b38*m.b46*m.b48 - 160*
                       m.b38*m.b46*m.b49 - 96*m.b38*m.b46*m.b50 - 64*m.b38*m.b46*m.b51 - 32*m.b38*m.b46*m.b52 - 288*
                       m.b38*m.b47*m.b48 - 192*m.b38*m.b47*m.b49 - 96*m.b38*m.b47*m.b50 - 64*m.b38*m.b47*m.b51 - 32*
                       m.b38*m.b47*m.b52 - 224*m.b38*m.b48*m.b49 - 128*m.b38*m.b48*m.b50 - 64*m.b38*m.b48*m.b51 - 32*
                       m.b38*m.b48*m.b52 - 160*m.b38*m.b49*m.b50 - 64*m.b38*m.b49*m.b51 - 32*m.b38*m.b49*m.b52 - 96*
                       m.b38*m.b50*m.b51 - 32*m.b38*m.b50*m.b52 - 32*m.b38*m.b51*m.b52 - 768*m.b39*m.b40*m.b41 - 1056*
                       m.b39*m.b40*m.b42 - 928*m.b39*m.b40*m.b43 - 800*m.b39*m.b40*m.b44 - 672*m.b39*m.b40*m.b45 - 544*
                       m.b39*m.b40*m.b46 - 416*m.b39*m.b40*m.b47 - 352*m.b39*m.b40*m.b48 - 288*m.b39*m.b40*m.b49 - 224*
                       m.b39*m.b40*m.b50 - 160*m.b39*m.b40*m.b51 - 96*m.b39*m.b40*m.b52 - 32*m.b39*m.b40*m.b53 - 1056*
                       m.b39*m.b41*m.b42 - 576*m.b39*m.b41*m.b43 - 800*m.b39*m.b41*m.b44 - 672*m.b39*m.b41*m.b45 - 544*
                       m.b39*m.b41*m.b46 - 416*m.b39*m.b41*m.b47 - 320*m.b39*m.b41*m.b48 - 256*m.b39*m.b41*m.b49 - 192*
                       m.b39*m.b41*m.b50 - 128*m.b39*m.b41*m.b51 - 64*m.b39*m.b41*m.b52 - 32*m.b39*m.b41*m.b53 - 928*
                       m.b39*m.b42*m.b43 - 800*m.b39*m.b42*m.b44 - 384*m.b39*m.b42*m.b45 - 544*m.b39*m.b42*m.b46 - 416*
                       m.b39*m.b42*m.b47 - 288*m.b39*m.b42*m.b48 - 224*m.b39*m.b42*m.b49 - 160*m.b39*m.b42*m.b50 - 96*
                       m.b39*m.b42*m.b51 - 64*m.b39*m.b42*m.b52 - 32*m.b39*m.b42*m.b53 - 800*m.b39*m.b43*m.b44 - 672*
                       m.b39*m.b43*m.b45 - 544*m.b39*m.b43*m.b46 - 192*m.b39*m.b43*m.b47 - 288*m.b39*m.b43*m.b48 - 192*
                       m.b39*m.b43*m.b49 - 128*m.b39*m.b43*m.b50 - 96*m.b39*m.b43*m.b51 - 64*m.b39*m.b43*m.b52 - 32*
                       m.b39*m.b43*m.b53 - 672*m.b39*m.b44*m.b45 - 544*m.b39*m.b44*m.b46 - 416*m.b39*m.b44*m.b47 - 288*
                       m.b39*m.b44*m.b48 - 128*m.b39*m.b44*m.b50 - 96*m.b39*m.b44*m.b51 - 64*m.b39*m.b44*m.b52 - 32*
                       m.b39*m.b44*m.b53 - 544*m.b39*m.b45*m.b46 - 416*m.b39*m.b45*m.b47 - 288*m.b39*m.b45*m.b48 - 192*
                       m.b39*m.b45*m.b49 - 128*m.b39*m.b45*m.b50 - 64*m.b39*m.b45*m.b52 - 32*m.b39*m.b45*m.b53 - 416*
                       m.b39*m.b46*m.b47 - 320*m.b39*m.b46*m.b48 - 224*m.b39*m.b46*m.b49 - 128*m.b39*m.b46*m.b50 - 96*
                       m.b39*m.b46*m.b51 - 64*m.b39*m.b46*m.b52 - 352*m.b39*m.b47*m.b48 - 256*m.b39*m.b47*m.b49 - 160*
                       m.b39*m.b47*m.b50 - 96*m.b39*m.b47*m.b51 - 64*m.b39*m.b47*m.b52 - 32*m.b39*m.b47*m.b53 - 288*
                       m.b39*m.b48*m.b49 - 192*m.b39*m.b48*m.b50 - 96*m.b39*m.b48*m.b51 - 64*m.b39*m.b48*m.b52 - 32*
                       m.b39*m.b48*m.b53 - 224*m.b39*m.b49*m.b50 - 128*m.b39*m.b49*m.b51 - 64*m.b39*m.b49*m.b52 - 32*
                       m.b39*m.b49*m.b53 - 160*m.b39*m.b50*m.b51 - 64*m.b39*m.b50*m.b52 - 32*m.b39*m.b50*m.b53 - 96*
                       m.b39*m.b51*m.b52 - 32*m.b39*m.b51*m.b53 - 32*m.b39*m.b52*m.b53 - 768*m.b40*m.b41*m.b42 - 1056*
                       m.b40*m.b41*m.b43 - 928*m.b40*m.b41*m.b44 - 800*m.b40*m.b41*m.b45 - 672*m.b40*m.b41*m.b46 - 544*
                       m.b40*m.b41*m.b47 - 416*m.b40*m.b41*m.b48 - 352*m.b40*m.b41*m.b49 - 288*m.b40*m.b41*m.b50 - 224*
                       m.b40*m.b41*m.b51 - 160*m.b40*m.b41*m.b52 - 96*m.b40*m.b41*m.b53 - 32*m.b40*m.b41*m.b54 - 1056*
                       m.b40*m.b42*m.b43 - 576*m.b40*m.b42*m.b44 - 800*m.b40*m.b42*m.b45 - 672*m.b40*m.b42*m.b46 - 544*
                       m.b40*m.b42*m.b47 - 416*m.b40*m.b42*m.b48 - 320*m.b40*m.b42*m.b49 - 256*m.b40*m.b42*m.b50 - 192*
                       m.b40*m.b42*m.b51 - 128*m.b40*m.b42*m.b52 - 64*m.b40*m.b42*m.b53 - 32*m.b40*m.b42*m.b54 - 928*
                       m.b40*m.b43*m.b44 - 800*m.b40*m.b43*m.b45 - 384*m.b40*m.b43*m.b46 - 544*m.b40*m.b43*m.b47 - 416*
                       m.b40*m.b43*m.b48 - 288*m.b40*m.b43*m.b49 - 224*m.b40*m.b43*m.b50 - 160*m.b40*m.b43*m.b51 - 96*
                       m.b40*m.b43*m.b52 - 64*m.b40*m.b43*m.b53 - 32*m.b40*m.b43*m.b54 - 800*m.b40*m.b44*m.b45 - 672*
                       m.b40*m.b44*m.b46 - 544*m.b40*m.b44*m.b47 - 192*m.b40*m.b44*m.b48 - 288*m.b40*m.b44*m.b49 - 192*
                       m.b40*m.b44*m.b50 - 128*m.b40*m.b44*m.b51 - 96*m.b40*m.b44*m.b52 - 64*m.b40*m.b44*m.b53 - 32*
                       m.b40*m.b44*m.b54 - 672*m.b40*m.b45*m.b46 - 544*m.b40*m.b45*m.b47 - 416*m.b40*m.b45*m.b48 - 288*
                       m.b40*m.b45*m.b49 - 128*m.b40*m.b45*m.b51 - 96*m.b40*m.b45*m.b52 - 64*m.b40*m.b45*m.b53 - 32*
                       m.b40*m.b45*m.b54 - 544*m.b40*m.b46*m.b47 - 416*m.b40*m.b46*m.b48 - 288*m.b40*m.b46*m.b49 - 192*
                       m.b40*m.b46*m.b50 - 128*m.b40*m.b46*m.b51 - 64*m.b40*m.b46*m.b53 - 32*m.b40*m.b46*m.b54 - 416*
                       m.b40*m.b47*m.b48 - 320*m.b40*m.b47*m.b49 - 224*m.b40*m.b47*m.b50 - 128*m.b40*m.b47*m.b51 - 96*
                       m.b40*m.b47*m.b52 - 64*m.b40*m.b47*m.b53 - 352*m.b40*m.b48*m.b49 - 256*m.b40*m.b48*m.b50 - 160*
                       m.b40*m.b48*m.b51 - 96*m.b40*m.b48*m.b52 - 64*m.b40*m.b48*m.b53 - 32*m.b40*m.b48*m.b54 - 288*
                       m.b40*m.b49*m.b50 - 192*m.b40*m.b49*m.b51 - 96*m.b40*m.b49*m.b52 - 64*m.b40*m.b49*m.b53 - 32*
                       m.b40*m.b49*m.b54 - 224*m.b40*m.b50*m.b51 - 128*m.b40*m.b50*m.b52 - 64*m.b40*m.b50*m.b53 - 32*
                       m.b40*m.b50*m.b54 - 160*m.b40*m.b51*m.b52 - 64*m.b40*m.b51*m.b53 - 32*m.b40*m.b51*m.b54 - 96*
                       m.b40*m.b52*m.b53 - 32*m.b40*m.b52*m.b54 - 32*m.b40*m.b53*m.b54 - 768*m.b41*m.b42*m.b43 - 1056*
                       m.b41*m.b42*m.b44 - 928*m.b41*m.b42*m.b45 - 800*m.b41*m.b42*m.b46 - 672*m.b41*m.b42*m.b47 - 544*
                       m.b41*m.b42*m.b48 - 416*m.b41*m.b42*m.b49 - 352*m.b41*m.b42*m.b50 - 288*m.b41*m.b42*m.b51 - 224*
                       m.b41*m.b42*m.b52 - 160*m.b41*m.b42*m.b53 - 96*m.b41*m.b42*m.b54 - 32*m.b41*m.b42*m.b55 - 1056*
                       m.b41*m.b43*m.b44 - 576*m.b41*m.b43*m.b45 - 800*m.b41*m.b43*m.b46 - 672*m.b41*m.b43*m.b47 - 544*
                       m.b41*m.b43*m.b48 - 416*m.b41*m.b43*m.b49 - 320*m.b41*m.b43*m.b50 - 256*m.b41*m.b43*m.b51 - 192*
                       m.b41*m.b43*m.b52 - 128*m.b41*m.b43*m.b53 - 64*m.b41*m.b43*m.b54 - 32*m.b41*m.b43*m.b55 - 928*
                       m.b41*m.b44*m.b45 - 800*m.b41*m.b44*m.b46 - 384*m.b41*m.b44*m.b47 - 544*m.b41*m.b44*m.b48 - 416*
                       m.b41*m.b44*m.b49 - 288*m.b41*m.b44*m.b50 - 224*m.b41*m.b44*m.b51 - 160*m.b41*m.b44*m.b52 - 96*
                       m.b41*m.b44*m.b53 - 64*m.b41*m.b44*m.b54 - 32*m.b41*m.b44*m.b55 - 800*m.b41*m.b45*m.b46 - 672*
                       m.b41*m.b45*m.b47 - 544*m.b41*m.b45*m.b48 - 192*m.b41*m.b45*m.b49 - 288*m.b41*m.b45*m.b50 - 192*
                       m.b41*m.b45*m.b51 - 128*m.b41*m.b45*m.b52 - 96*m.b41*m.b45*m.b53 - 64*m.b41*m.b45*m.b54 - 32*
                       m.b41*m.b45*m.b55 - 672*m.b41*m.b46*m.b47 - 544*m.b41*m.b46*m.b48 - 416*m.b41*m.b46*m.b49 - 288*
                       m.b41*m.b46*m.b50 - 128*m.b41*m.b46*m.b52 - 96*m.b41*m.b46*m.b53 - 64*m.b41*m.b46*m.b54 - 32*
                       m.b41*m.b46*m.b55 - 544*m.b41*m.b47*m.b48 - 416*m.b41*m.b47*m.b49 - 288*m.b41*m.b47*m.b50 - 192*
                       m.b41*m.b47*m.b51 - 128*m.b41*m.b47*m.b52 - 64*m.b41*m.b47*m.b54 - 32*m.b41*m.b47*m.b55 - 416*
                       m.b41*m.b48*m.b49 - 320*m.b41*m.b48*m.b50 - 224*m.b41*m.b48*m.b51 - 128*m.b41*m.b48*m.b52 - 96*
                       m.b41*m.b48*m.b53 - 64*m.b41*m.b48*m.b54 - 352*m.b41*m.b49*m.b50 - 256*m.b41*m.b49*m.b51 - 160*
                       m.b41*m.b49*m.b52 - 96*m.b41*m.b49*m.b53 - 64*m.b41*m.b49*m.b54 - 32*m.b41*m.b49*m.b55 - 288*
                       m.b41*m.b50*m.b51 - 192*m.b41*m.b50*m.b52 - 96*m.b41*m.b50*m.b53 - 64*m.b41*m.b50*m.b54 - 32*
                       m.b41*m.b50*m.b55 - 224*m.b41*m.b51*m.b52 - 128*m.b41*m.b51*m.b53 - 64*m.b41*m.b51*m.b54 - 32*
                       m.b41*m.b51*m.b55 - 160*m.b41*m.b52*m.b53 - 64*m.b41*m.b52*m.b54 - 32*m.b41*m.b52*m.b55 - 96*
                       m.b41*m.b53*m.b54 - 32*m.b41*m.b53*m.b55 - 32*m.b41*m.b54*m.b55 - 768*m.b42*m.b43*m.b44 - 1056*
                       m.b42*m.b43*m.b45 - 928*m.b42*m.b43*m.b46 - 800*m.b42*m.b43*m.b47 - 672*m.b42*m.b43*m.b48 - 544*
                       m.b42*m.b43*m.b49 - 416*m.b42*m.b43*m.b50 - 352*m.b42*m.b43*m.b51 - 288*m.b42*m.b43*m.b52 - 224*
                       m.b42*m.b43*m.b53 - 160*m.b42*m.b43*m.b54 - 96*m.b42*m.b43*m.b55 - 32*m.b42*m.b43*m.b56 - 1056*
                       m.b42*m.b44*m.b45 - 576*m.b42*m.b44*m.b46 - 800*m.b42*m.b44*m.b47 - 672*m.b42*m.b44*m.b48 - 544*
                       m.b42*m.b44*m.b49 - 416*m.b42*m.b44*m.b50 - 320*m.b42*m.b44*m.b51 - 256*m.b42*m.b44*m.b52 - 192*
                       m.b42*m.b44*m.b53 - 128*m.b42*m.b44*m.b54 - 64*m.b42*m.b44*m.b55 - 32*m.b42*m.b44*m.b56 - 928*
                       m.b42*m.b45*m.b46 - 800*m.b42*m.b45*m.b47 - 384*m.b42*m.b45*m.b48 - 544*m.b42*m.b45*m.b49 - 416*
                       m.b42*m.b45*m.b50 - 288*m.b42*m.b45*m.b51 - 224*m.b42*m.b45*m.b52 - 160*m.b42*m.b45*m.b53 - 96*
                       m.b42*m.b45*m.b54 - 64*m.b42*m.b45*m.b55 - 32*m.b42*m.b45*m.b56 - 800*m.b42*m.b46*m.b47 - 672*
                       m.b42*m.b46*m.b48 - 544*m.b42*m.b46*m.b49 - 192*m.b42*m.b46*m.b50 - 288*m.b42*m.b46*m.b51 - 192*
                       m.b42*m.b46*m.b52 - 128*m.b42*m.b46*m.b53 - 96*m.b42*m.b46*m.b54 - 64*m.b42*m.b46*m.b55 - 32*
                       m.b42*m.b46*m.b56 - 672*m.b42*m.b47*m.b48 - 544*m.b42*m.b47*m.b49 - 416*m.b42*m.b47*m.b50 - 288*
                       m.b42*m.b47*m.b51 - 128*m.b42*m.b47*m.b53 - 96*m.b42*m.b47*m.b54 - 64*m.b42*m.b47*m.b55 - 32*
                       m.b42*m.b47*m.b56 - 544*m.b42*m.b48*m.b49 - 416*m.b42*m.b48*m.b50 - 288*m.b42*m.b48*m.b51 - 192*
                       m.b42*m.b48*m.b52 - 128*m.b42*m.b48*m.b53 - 64*m.b42*m.b48*m.b55 - 32*m.b42*m.b48*m.b56 - 416*
                       m.b42*m.b49*m.b50 - 320*m.b42*m.b49*m.b51 - 224*m.b42*m.b49*m.b52 - 128*m.b42*m.b49*m.b53 - 96*
                       m.b42*m.b49*m.b54 - 64*m.b42*m.b49*m.b55 - 352*m.b42*m.b50*m.b51 - 256*m.b42*m.b50*m.b52 - 160*
                       m.b42*m.b50*m.b53 - 96*m.b42*m.b50*m.b54 - 64*m.b42*m.b50*m.b55 - 32*m.b42*m.b50*m.b56 - 288*
                       m.b42*m.b51*m.b52 - 192*m.b42*m.b51*m.b53 - 96*m.b42*m.b51*m.b54 - 64*m.b42*m.b51*m.b55 - 32*
                       m.b42*m.b51*m.b56 - 224*m.b42*m.b52*m.b53 - 128*m.b42*m.b52*m.b54 - 64*m.b42*m.b52*m.b55 - 32*
                       m.b42*m.b52*m.b56 - 160*m.b42*m.b53*m.b54 - 64*m.b42*m.b53*m.b55 - 32*m.b42*m.b53*m.b56 - 96*
                       m.b42*m.b54*m.b55 - 32*m.b42*m.b54*m.b56 - 32*m.b42*m.b55*m.b56 - 768*m.b43*m.b44*m.b45 - 1056*
                       m.b43*m.b44*m.b46 - 928*m.b43*m.b44*m.b47 - 800*m.b43*m.b44*m.b48 - 672*m.b43*m.b44*m.b49 - 544*
                       m.b43*m.b44*m.b50 - 416*m.b43*m.b44*m.b51 - 352*m.b43*m.b44*m.b52 - 288*m.b43*m.b44*m.b53 - 224*
                       m.b43*m.b44*m.b54 - 160*m.b43*m.b44*m.b55 - 96*m.b43*m.b44*m.b56 - 32*m.b43*m.b44*m.b57 - 1056*
                       m.b43*m.b45*m.b46 - 576*m.b43*m.b45*m.b47 - 800*m.b43*m.b45*m.b48 - 672*m.b43*m.b45*m.b49 - 544*
                       m.b43*m.b45*m.b50 - 416*m.b43*m.b45*m.b51 - 320*m.b43*m.b45*m.b52 - 256*m.b43*m.b45*m.b53 - 192*
                       m.b43*m.b45*m.b54 - 128*m.b43*m.b45*m.b55 - 64*m.b43*m.b45*m.b56 - 32*m.b43*m.b45*m.b57 - 928*
                       m.b43*m.b46*m.b47 - 800*m.b43*m.b46*m.b48 - 384*m.b43*m.b46*m.b49 - 544*m.b43*m.b46*m.b50 - 416*
                       m.b43*m.b46*m.b51 - 288*m.b43*m.b46*m.b52 - 224*m.b43*m.b46*m.b53 - 160*m.b43*m.b46*m.b54 - 96*
                       m.b43*m.b46*m.b55 - 64*m.b43*m.b46*m.b56 - 32*m.b43*m.b46*m.b57 - 800*m.b43*m.b47*m.b48 - 672*
                       m.b43*m.b47*m.b49 - 544*m.b43*m.b47*m.b50 - 192*m.b43*m.b47*m.b51 - 288*m.b43*m.b47*m.b52 - 192*
                       m.b43*m.b47*m.b53 - 128*m.b43*m.b47*m.b54 - 96*m.b43*m.b47*m.b55 - 64*m.b43*m.b47*m.b56 - 32*
                       m.b43*m.b47*m.b57 - 672*m.b43*m.b48*m.b49 - 544*m.b43*m.b48*m.b50 - 416*m.b43*m.b48*m.b51 - 288*
                       m.b43*m.b48*m.b52 - 128*m.b43*m.b48*m.b54 - 96*m.b43*m.b48*m.b55 - 64*m.b43*m.b48*m.b56 - 32*
                       m.b43*m.b48*m.b57 - 544*m.b43*m.b49*m.b50 - 416*m.b43*m.b49*m.b51 - 288*m.b43*m.b49*m.b52 - 192*
                       m.b43*m.b49*m.b53 - 128*m.b43*m.b49*m.b54 - 64*m.b43*m.b49*m.b56 - 32*m.b43*m.b49*m.b57 - 416*
                       m.b43*m.b50*m.b51 - 320*m.b43*m.b50*m.b52 - 224*m.b43*m.b50*m.b53 - 128*m.b43*m.b50*m.b54 - 96*
                       m.b43*m.b50*m.b55 - 64*m.b43*m.b50*m.b56 - 352*m.b43*m.b51*m.b52 - 256*m.b43*m.b51*m.b53 - 160*
                       m.b43*m.b51*m.b54 - 96*m.b43*m.b51*m.b55 - 64*m.b43*m.b51*m.b56 - 32*m.b43*m.b51*m.b57 - 288*
                       m.b43*m.b52*m.b53 - 192*m.b43*m.b52*m.b54 - 96*m.b43*m.b52*m.b55 - 64*m.b43*m.b52*m.b56 - 32*
                       m.b43*m.b52*m.b57 - 224*m.b43*m.b53*m.b54 - 128*m.b43*m.b53*m.b55 - 64*m.b43*m.b53*m.b56 - 32*
                       m.b43*m.b53*m.b57 - 160*m.b43*m.b54*m.b55 - 64*m.b43*m.b54*m.b56 - 32*m.b43*m.b54*m.b57 - 96*
                       m.b43*m.b55*m.b56 - 32*m.b43*m.b55*m.b57 - 32*m.b43*m.b56*m.b57 - 768*m.b44*m.b45*m.b46 - 1056*
                       m.b44*m.b45*m.b47 - 928*m.b44*m.b45*m.b48 - 800*m.b44*m.b45*m.b49 - 672*m.b44*m.b45*m.b50 - 544*
                       m.b44*m.b45*m.b51 - 416*m.b44*m.b45*m.b52 - 352*m.b44*m.b45*m.b53 - 288*m.b44*m.b45*m.b54 - 224*
                       m.b44*m.b45*m.b55 - 160*m.b44*m.b45*m.b56 - 96*m.b44*m.b45*m.b57 - 32*m.b44*m.b45*m.b58 - 1056*
                       m.b44*m.b46*m.b47 - 576*m.b44*m.b46*m.b48 - 800*m.b44*m.b46*m.b49 - 672*m.b44*m.b46*m.b50 - 544*
                       m.b44*m.b46*m.b51 - 416*m.b44*m.b46*m.b52 - 320*m.b44*m.b46*m.b53 - 256*m.b44*m.b46*m.b54 - 192*
                       m.b44*m.b46*m.b55 - 128*m.b44*m.b46*m.b56 - 64*m.b44*m.b46*m.b57 - 32*m.b44*m.b46*m.b58 - 928*
                       m.b44*m.b47*m.b48 - 800*m.b44*m.b47*m.b49 - 384*m.b44*m.b47*m.b50 - 544*m.b44*m.b47*m.b51 - 416*
                       m.b44*m.b47*m.b52 - 288*m.b44*m.b47*m.b53 - 224*m.b44*m.b47*m.b54 - 160*m.b44*m.b47*m.b55 - 96*
                       m.b44*m.b47*m.b56 - 64*m.b44*m.b47*m.b57 - 32*m.b44*m.b47*m.b58 - 800*m.b44*m.b48*m.b49 - 672*
                       m.b44*m.b48*m.b50 - 544*m.b44*m.b48*m.b51 - 192*m.b44*m.b48*m.b52 - 288*m.b44*m.b48*m.b53 - 192*
                       m.b44*m.b48*m.b54 - 128*m.b44*m.b48*m.b55 - 96*m.b44*m.b48*m.b56 - 64*m.b44*m.b48*m.b57 - 32*
                       m.b44*m.b48*m.b58 - 672*m.b44*m.b49*m.b50 - 544*m.b44*m.b49*m.b51 - 416*m.b44*m.b49*m.b52 - 288*
                       m.b44*m.b49*m.b53 - 128*m.b44*m.b49*m.b55 - 96*m.b44*m.b49*m.b56 - 64*m.b44*m.b49*m.b57 - 32*
                       m.b44*m.b49*m.b58 - 544*m.b44*m.b50*m.b51 - 416*m.b44*m.b50*m.b52 - 288*m.b44*m.b50*m.b53 - 192*
                       m.b44*m.b50*m.b54 - 128*m.b44*m.b50*m.b55 - 64*m.b44*m.b50*m.b57 - 32*m.b44*m.b50*m.b58 - 416*
                       m.b44*m.b51*m.b52 - 320*m.b44*m.b51*m.b53 - 224*m.b44*m.b51*m.b54 - 128*m.b44*m.b51*m.b55 - 96*
                       m.b44*m.b51*m.b56 - 64*m.b44*m.b51*m.b57 - 352*m.b44*m.b52*m.b53 - 256*m.b44*m.b52*m.b54 - 160*
                       m.b44*m.b52*m.b55 - 96*m.b44*m.b52*m.b56 - 64*m.b44*m.b52*m.b57 - 32*m.b44*m.b52*m.b58 - 288*
                       m.b44*m.b53*m.b54 - 192*m.b44*m.b53*m.b55 - 96*m.b44*m.b53*m.b56 - 64*m.b44*m.b53*m.b57 - 32*
                       m.b44*m.b53*m.b58 - 224*m.b44*m.b54*m.b55 - 128*m.b44*m.b54*m.b56 - 64*m.b44*m.b54*m.b57 - 32*
                       m.b44*m.b54*m.b58 - 160*m.b44*m.b55*m.b56 - 64*m.b44*m.b55*m.b57 - 32*m.b44*m.b55*m.b58 - 96*
                       m.b44*m.b56*m.b57 - 32*m.b44*m.b56*m.b58 - 32*m.b44*m.b57*m.b58 - 768*m.b45*m.b46*m.b47 - 1056*
                       m.b45*m.b46*m.b48 - 928*m.b45*m.b46*m.b49 - 800*m.b45*m.b46*m.b50 - 672*m.b45*m.b46*m.b51 - 544*
                       m.b45*m.b46*m.b52 - 416*m.b45*m.b46*m.b53 - 352*m.b45*m.b46*m.b54 - 288*m.b45*m.b46*m.b55 - 224*
                       m.b45*m.b46*m.b56 - 160*m.b45*m.b46*m.b57 - 96*m.b45*m.b46*m.b58 - 32*m.b45*m.b46*m.b59 - 1056*
                       m.b45*m.b47*m.b48 - 576*m.b45*m.b47*m.b49 - 800*m.b45*m.b47*m.b50 - 672*m.b45*m.b47*m.b51 - 544*
                       m.b45*m.b47*m.b52 - 416*m.b45*m.b47*m.b53 - 320*m.b45*m.b47*m.b54 - 256*m.b45*m.b47*m.b55 - 192*
                       m.b45*m.b47*m.b56 - 128*m.b45*m.b47*m.b57 - 64*m.b45*m.b47*m.b58 - 32*m.b45*m.b47*m.b59 - 928*
                       m.b45*m.b48*m.b49 - 800*m.b45*m.b48*m.b50 - 384*m.b45*m.b48*m.b51 - 544*m.b45*m.b48*m.b52 - 416*
                       m.b45*m.b48*m.b53 - 288*m.b45*m.b48*m.b54 - 224*m.b45*m.b48*m.b55 - 160*m.b45*m.b48*m.b56 - 96*
                       m.b45*m.b48*m.b57 - 64*m.b45*m.b48*m.b58 - 32*m.b45*m.b48*m.b59 - 800*m.b45*m.b49*m.b50 - 672*
                       m.b45*m.b49*m.b51 - 544*m.b45*m.b49*m.b52 - 192*m.b45*m.b49*m.b53 - 288*m.b45*m.b49*m.b54 - 192*
                       m.b45*m.b49*m.b55 - 128*m.b45*m.b49*m.b56 - 96*m.b45*m.b49*m.b57 - 64*m.b45*m.b49*m.b58 - 32*
                       m.b45*m.b49*m.b59 - 672*m.b45*m.b50*m.b51 - 544*m.b45*m.b50*m.b52 - 416*m.b45*m.b50*m.b53 - 288*
                       m.b45*m.b50*m.b54 - 128*m.b45*m.b50*m.b56 - 96*m.b45*m.b50*m.b57 - 64*m.b45*m.b50*m.b58 - 32*
                       m.b45*m.b50*m.b59 - 544*m.b45*m.b51*m.b52 - 416*m.b45*m.b51*m.b53 - 288*m.b45*m.b51*m.b54 - 192*
                       m.b45*m.b51*m.b55 - 128*m.b45*m.b51*m.b56 - 64*m.b45*m.b51*m.b58 - 32*m.b45*m.b51*m.b59 - 416*
                       m.b45*m.b52*m.b53 - 320*m.b45*m.b52*m.b54 - 224*m.b45*m.b52*m.b55 - 128*m.b45*m.b52*m.b56 - 96*
                       m.b45*m.b52*m.b57 - 64*m.b45*m.b52*m.b58 - 352*m.b45*m.b53*m.b54 - 256*m.b45*m.b53*m.b55 - 160*
                       m.b45*m.b53*m.b56 - 96*m.b45*m.b53*m.b57 - 64*m.b45*m.b53*m.b58 - 32*m.b45*m.b53*m.b59 - 288*
                       m.b45*m.b54*m.b55 - 192*m.b45*m.b54*m.b56 - 96*m.b45*m.b54*m.b57 - 64*m.b45*m.b54*m.b58 - 32*
                       m.b45*m.b54*m.b59 - 224*m.b45*m.b55*m.b56 - 128*m.b45*m.b55*m.b57 - 64*m.b45*m.b55*m.b58 - 32*
                       m.b45*m.b55*m.b59 - 160*m.b45*m.b56*m.b57 - 64*m.b45*m.b56*m.b58 - 32*m.b45*m.b56*m.b59 - 96*
                       m.b45*m.b57*m.b58 - 32*m.b45*m.b57*m.b59 - 32*m.b45*m.b58*m.b59 - 768*m.b46*m.b47*m.b48 - 1056*
                       m.b46*m.b47*m.b49 - 928*m.b46*m.b47*m.b50 - 800*m.b46*m.b47*m.b51 - 672*m.b46*m.b47*m.b52 - 544*
                       m.b46*m.b47*m.b53 - 416*m.b46*m.b47*m.b54 - 352*m.b46*m.b47*m.b55 - 288*m.b46*m.b47*m.b56 - 224*
                       m.b46*m.b47*m.b57 - 160*m.b46*m.b47*m.b58 - 96*m.b46*m.b47*m.b59 - 32*m.b46*m.b47*m.b60 - 1056*
                       m.b46*m.b48*m.b49 - 576*m.b46*m.b48*m.b50 - 800*m.b46*m.b48*m.b51 - 672*m.b46*m.b48*m.b52 - 544*
                       m.b46*m.b48*m.b53 - 416*m.b46*m.b48*m.b54 - 320*m.b46*m.b48*m.b55 - 256*m.b46*m.b48*m.b56 - 192*
                       m.b46*m.b48*m.b57 - 128*m.b46*m.b48*m.b58 - 64*m.b46*m.b48*m.b59 - 32*m.b46*m.b48*m.b60 - 928*
                       m.b46*m.b49*m.b50 - 800*m.b46*m.b49*m.b51 - 384*m.b46*m.b49*m.b52 - 544*m.b46*m.b49*m.b53 - 416*
                       m.b46*m.b49*m.b54 - 288*m.b46*m.b49*m.b55 - 224*m.b46*m.b49*m.b56 - 160*m.b46*m.b49*m.b57 - 96*
                       m.b46*m.b49*m.b58 - 64*m.b46*m.b49*m.b59 - 32*m.b46*m.b49*m.b60 - 800*m.b46*m.b50*m.b51 - 672*
                       m.b46*m.b50*m.b52 - 544*m.b46*m.b50*m.b53 - 192*m.b46*m.b50*m.b54 - 288*m.b46*m.b50*m.b55 - 192*
                       m.b46*m.b50*m.b56 - 128*m.b46*m.b50*m.b57 - 96*m.b46*m.b50*m.b58 - 64*m.b46*m.b50*m.b59 - 32*
                       m.b46*m.b50*m.b60 - 672*m.b46*m.b51*m.b52 - 544*m.b46*m.b51*m.b53 - 416*m.b46*m.b51*m.b54 - 288*
                       m.b46*m.b51*m.b55 - 128*m.b46*m.b51*m.b57 - 96*m.b46*m.b51*m.b58 - 64*m.b46*m.b51*m.b59 - 32*
                       m.b46*m.b51*m.b60 - 544*m.b46*m.b52*m.b53 - 416*m.b46*m.b52*m.b54 - 288*m.b46*m.b52*m.b55 - 192*
                       m.b46*m.b52*m.b56 - 128*m.b46*m.b52*m.b57 - 64*m.b46*m.b52*m.b59 - 32*m.b46*m.b52*m.b60 - 416*
                       m.b46*m.b53*m.b54 - 320*m.b46*m.b53*m.b55 - 224*m.b46*m.b53*m.b56 - 128*m.b46*m.b53*m.b57 - 96*
                       m.b46*m.b53*m.b58 - 64*m.b46*m.b53*m.b59 - 352*m.b46*m.b54*m.b55 - 256*m.b46*m.b54*m.b56 - 160*
                       m.b46*m.b54*m.b57 - 96*m.b46*m.b54*m.b58 - 64*m.b46*m.b54*m.b59 - 32*m.b46*m.b54*m.b60 - 288*
                       m.b46*m.b55*m.b56 - 192*m.b46*m.b55*m.b57 - 96*m.b46*m.b55*m.b58 - 64*m.b46*m.b55*m.b59 - 32*
                       m.b46*m.b55*m.b60 - 224*m.b46*m.b56*m.b57 - 128*m.b46*m.b56*m.b58 - 64*m.b46*m.b56*m.b59 - 32*
                       m.b46*m.b56*m.b60 - 160*m.b46*m.b57*m.b58 - 64*m.b46*m.b57*m.b59 - 32*m.b46*m.b57*m.b60 - 96*
                       m.b46*m.b58*m.b59 - 32*m.b46*m.b58*m.b60 - 32*m.b46*m.b59*m.b60 - 736*m.b47*m.b48*m.b49 - 992*
                       m.b47*m.b48*m.b50 - 864*m.b47*m.b48*m.b51 - 736*m.b47*m.b48*m.b52 - 608*m.b47*m.b48*m.b53 - 480*
                       m.b47*m.b48*m.b54 - 352*m.b47*m.b48*m.b55 - 288*m.b47*m.b48*m.b56 - 224*m.b47*m.b48*m.b57 - 160*
                       m.b47*m.b48*m.b58 - 96*m.b47*m.b48*m.b59 - 32*m.b47*m.b48*m.b60 - 992*m.b47*m.b49*m.b50 - 544*
                       m.b47*m.b49*m.b51 - 736*m.b47*m.b49*m.b52 - 608*m.b47*m.b49*m.b53 - 480*m.b47*m.b49*m.b54 - 352*
                       m.b47*m.b49*m.b55 - 256*m.b47*m.b49*m.b56 - 192*m.b47*m.b49*m.b57 - 128*m.b47*m.b49*m.b58 - 64*
                       m.b47*m.b49*m.b59 - 32*m.b47*m.b49*m.b60 - 864*m.b47*m.b50*m.b51 - 736*m.b47*m.b50*m.b52 - 352*
                       m.b47*m.b50*m.b53 - 480*m.b47*m.b50*m.b54 - 352*m.b47*m.b50*m.b55 - 224*m.b47*m.b50*m.b56 - 160*
                       m.b47*m.b50*m.b57 - 96*m.b47*m.b50*m.b58 - 64*m.b47*m.b50*m.b59 - 32*m.b47*m.b50*m.b60 - 736*
                       m.b47*m.b51*m.b52 - 608*m.b47*m.b51*m.b53 - 480*m.b47*m.b51*m.b54 - 160*m.b47*m.b51*m.b55 - 224*
                       m.b47*m.b51*m.b56 - 128*m.b47*m.b51*m.b57 - 96*m.b47*m.b51*m.b58 - 64*m.b47*m.b51*m.b59 - 32*
                       m.b47*m.b51*m.b60 - 608*m.b47*m.b52*m.b53 - 480*m.b47*m.b52*m.b54 - 352*m.b47*m.b52*m.b55 - 224*
                       m.b47*m.b52*m.b56 - 96*m.b47*m.b52*m.b58 - 64*m.b47*m.b52*m.b59 - 32*m.b47*m.b52*m.b60 - 480*
                       m.b47*m.b53*m.b54 - 352*m.b47*m.b53*m.b55 - 256*m.b47*m.b53*m.b56 - 160*m.b47*m.b53*m.b57 - 96*
                       m.b47*m.b53*m.b58 - 32*m.b47*m.b53*m.b60 - 384*m.b47*m.b54*m.b55 - 288*m.b47*m.b54*m.b56 - 192*
                       m.b47*m.b54*m.b57 - 96*m.b47*m.b54*m.b58 - 64*m.b47*m.b54*m.b59 - 32*m.b47*m.b54*m.b60 - 320*
                       m.b47*m.b55*m.b56 - 224*m.b47*m.b55*m.b57 - 128*m.b47*m.b55*m.b58 - 64*m.b47*m.b55*m.b59 - 32*
                       m.b47*m.b55*m.b60 - 256*m.b47*m.b56*m.b57 - 160*m.b47*m.b56*m.b58 - 64*m.b47*m.b56*m.b59 - 32*
                       m.b47*m.b56*m.b60 - 192*m.b47*m.b57*m.b58 - 96*m.b47*m.b57*m.b59 - 32*m.b47*m.b57*m.b60 - 128*
                       m.b47*m.b58*m.b59 - 32*m.b47*m.b58*m.b60 - 64*m.b47*m.b59*m.b60 - 672*m.b48*m.b49*m.b50 - 928*
                       m.b48*m.b49*m.b51 - 800*m.b48*m.b49*m.b52 - 672*m.b48*m.b49*m.b53 - 544*m.b48*m.b49*m.b54 - 416*
                       m.b48*m.b49*m.b55 - 288*m.b48*m.b49*m.b56 - 224*m.b48*m.b49*m.b57 - 160*m.b48*m.b49*m.b58 - 96*
                       m.b48*m.b49*m.b59 - 32*m.b48*m.b49*m.b60 - 896*m.b48*m.b50*m.b51 - 512*m.b48*m.b50*m.b52 - 672*
                       m.b48*m.b50*m.b53 - 544*m.b48*m.b50*m.b54 - 416*m.b48*m.b50*m.b55 - 288*m.b48*m.b50*m.b56 - 192*
                       m.b48*m.b50*m.b57 - 128*m.b48*m.b50*m.b58 - 64*m.b48*m.b50*m.b59 - 32*m.b48*m.b50*m.b60 - 768*
                       m.b48*m.b51*m.b52 - 672*m.b48*m.b51*m.b53 - 320*m.b48*m.b51*m.b54 - 416*m.b48*m.b51*m.b55 - 288*
                       m.b48*m.b51*m.b56 - 160*m.b48*m.b51*m.b57 - 96*m.b48*m.b51*m.b58 - 64*m.b48*m.b51*m.b59 - 32*
                       m.b48*m.b51*m.b60 - 640*m.b48*m.b52*m.b53 - 544*m.b48*m.b52*m.b54 - 416*m.b48*m.b52*m.b55 - 128*
                       m.b48*m.b52*m.b56 - 160*m.b48*m.b52*m.b57 - 96*m.b48*m.b52*m.b58 - 64*m.b48*m.b52*m.b59 - 32*
                       m.b48*m.b52*m.b60 - 512*m.b48*m.b53*m.b54 - 416*m.b48*m.b53*m.b55 - 288*m.b48*m.b53*m.b56 - 192*
                       m.b48*m.b53*m.b57 - 64*m.b48*m.b53*m.b59 - 32*m.b48*m.b53*m.b60 - 384*m.b48*m.b54*m.b55 - 320*
                       m.b48*m.b54*m.b56 - 224*m.b48*m.b54*m.b57 - 128*m.b48*m.b54*m.b58 - 64*m.b48*m.b54*m.b59 - 320*
                       m.b48*m.b55*m.b56 - 256*m.b48*m.b55*m.b57 - 160*m.b48*m.b55*m.b58 - 64*m.b48*m.b55*m.b59 - 32*
                       m.b48*m.b55*m.b60 - 256*m.b48*m.b56*m.b57 - 192*m.b48*m.b56*m.b58 - 96*m.b48*m.b56*m.b59 - 32*
                       m.b48*m.b56*m.b60 - 192*m.b48*m.b57*m.b58 - 128*m.b48*m.b57*m.b59 - 32*m.b48*m.b57*m.b60 - 128*
                       m.b48*m.b58*m.b59 - 64*m.b48*m.b58*m.b60 - 64*m.b48*m.b59*m.b60 - 608*m.b49*m.b50*m.b51 - 832*
                       m.b49*m.b50*m.b52 - 736*m.b49*m.b50*m.b53 - 608*m.b49*m.b50*m.b54 - 480*m.b49*m.b50*m.b55 - 352*
                       m.b49*m.b50*m.b56 - 224*m.b49*m.b50*m.b57 - 160*m.b49*m.b50*m.b58 - 96*m.b49*m.b50*m.b59 - 32*
                       m.b49*m.b50*m.b60 - 800*m.b49*m.b51*m.b52 - 448*m.b49*m.b51*m.b53 - 608*m.b49*m.b51*m.b54 - 480*
                       m.b49*m.b51*m.b55 - 352*m.b49*m.b51*m.b56 - 224*m.b49*m.b51*m.b57 - 128*m.b49*m.b51*m.b58 - 64*
                       m.b49*m.b51*m.b59 - 32*m.b49*m.b51*m.b60 - 672*m.b49*m.b52*m.b53 - 576*m.b49*m.b52*m.b54 - 288*
                       m.b49*m.b52*m.b55 - 352*m.b49*m.b52*m.b56 - 224*m.b49*m.b52*m.b57 - 96*m.b49*m.b52*m.b58 - 64*
                       m.b49*m.b52*m.b59 - 32*m.b49*m.b52*m.b60 - 544*m.b49*m.b53*m.b54 - 448*m.b49*m.b53*m.b55 - 352*
                       m.b49*m.b53*m.b56 - 96*m.b49*m.b53*m.b57 - 128*m.b49*m.b53*m.b58 - 64*m.b49*m.b53*m.b59 - 32*
                       m.b49*m.b53*m.b60 - 416*m.b49*m.b54*m.b55 - 320*m.b49*m.b54*m.b56 - 256*m.b49*m.b54*m.b57 - 160*
                       m.b49*m.b54*m.b58 - 32*m.b49*m.b54*m.b60 - 320*m.b49*m.b55*m.b56 - 256*m.b49*m.b55*m.b57 - 192*
                       m.b49*m.b55*m.b58 - 96*m.b49*m.b55*m.b59 - 32*m.b49*m.b55*m.b60 - 256*m.b49*m.b56*m.b57 - 192*
                       m.b49*m.b56*m.b58 - 128*m.b49*m.b56*m.b59 - 32*m.b49*m.b56*m.b60 - 192*m.b49*m.b57*m.b58 - 128*
                       m.b49*m.b57*m.b59 - 64*m.b49*m.b57*m.b60 - 128*m.b49*m.b58*m.b59 - 64*m.b49*m.b58*m.b60 - 64*
                       m.b49*m.b59*m.b60 - 544*m.b50*m.b51*m.b52 - 736*m.b50*m.b51*m.b53 - 640*m.b50*m.b51*m.b54 - 544*
                       m.b50*m.b51*m.b55 - 416*m.b50*m.b51*m.b56 - 288*m.b50*m.b51*m.b57 - 160*m.b50*m.b51*m.b58 - 96*
                       m.b50*m.b51*m.b59 - 32*m.b50*m.b51*m.b60 - 704*m.b50*m.b52*m.b53 - 384*m.b50*m.b52*m.b54 - 512*
                       m.b50*m.b52*m.b55 - 416*m.b50*m.b52*m.b56 - 288*m.b50*m.b52*m.b57 - 160*m.b50*m.b52*m.b58 - 64*
                       m.b50*m.b52*m.b59 - 32*m.b50*m.b52*m.b60 - 576*m.b50*m.b53*m.b54 - 480*m.b50*m.b53*m.b55 - 224*
                       m.b50*m.b53*m.b56 - 288*m.b50*m.b53*m.b57 - 160*m.b50*m.b53*m.b58 - 64*m.b50*m.b53*m.b59 - 32*
                       m.b50*m.b53*m.b60 - 448*m.b50*m.b54*m.b55 - 352*m.b50*m.b54*m.b56 - 256*m.b50*m.b54*m.b57 - 96*
                       m.b50*m.b54*m.b58 - 96*m.b50*m.b54*m.b59 - 32*m.b50*m.b54*m.b60 - 320*m.b50*m.b55*m.b56 - 256*
                       m.b50*m.b55*m.b57 - 192*m.b50*m.b55*m.b58 - 128*m.b50*m.b55*m.b59 - 256*m.b50*m.b56*m.b57 - 192*
                       m.b50*m.b56*m.b58 - 128*m.b50*m.b56*m.b59 - 64*m.b50*m.b56*m.b60 - 192*m.b50*m.b57*m.b58 - 128*
                       m.b50*m.b57*m.b59 - 64*m.b50*m.b57*m.b60 - 128*m.b50*m.b58*m.b59 - 64*m.b50*m.b58*m.b60 - 64*
                       m.b50*m.b59*m.b60 - 480*m.b51*m.b52*m.b53 - 640*m.b51*m.b52*m.b54 - 544*m.b51*m.b52*m.b55 - 448*
                       m.b51*m.b52*m.b56 - 352*m.b51*m.b52*m.b57 - 224*m.b51*m.b52*m.b58 - 96*m.b51*m.b52*m.b59 - 32*
                       m.b51*m.b52*m.b60 - 608*m.b51*m.b53*m.b54 - 320*m.b51*m.b53*m.b55 - 416*m.b51*m.b53*m.b56 - 320*
                       m.b51*m.b53*m.b57 - 224*m.b51*m.b53*m.b58 - 96*m.b51*m.b53*m.b59 - 32*m.b51*m.b53*m.b60 - 480*
                       m.b51*m.b54*m.b55 - 384*m.b51*m.b54*m.b56 - 160*m.b51*m.b54*m.b57 - 192*m.b51*m.b54*m.b58 - 128*
                       m.b51*m.b54*m.b59 - 32*m.b51*m.b54*m.b60 - 352*m.b51*m.b55*m.b56 - 256*m.b51*m.b55*m.b57 - 192*
                       m.b51*m.b55*m.b58 - 64*m.b51*m.b55*m.b59 - 64*m.b51*m.b55*m.b60 - 256*m.b51*m.b56*m.b57 - 192*
                       m.b51*m.b56*m.b58 - 128*m.b51*m.b56*m.b59 - 64*m.b51*m.b56*m.b60 - 192*m.b51*m.b57*m.b58 - 128*
                       m.b51*m.b57*m.b59 - 64*m.b51*m.b57*m.b60 - 128*m.b51*m.b58*m.b59 - 64*m.b51*m.b58*m.b60 - 64*
                       m.b51*m.b59*m.b60 - 416*m.b52*m.b53*m.b54 - 544*m.b52*m.b53*m.b55 - 448*m.b52*m.b53*m.b56 - 352*
                       m.b52*m.b53*m.b57 - 256*m.b52*m.b53*m.b58 - 160*m.b52*m.b53*m.b59 - 32*m.b52*m.b53*m.b60 - 512*
                       m.b52*m.b54*m.b55 - 256*m.b52*m.b54*m.b56 - 320*m.b52*m.b54*m.b57 - 224*m.b52*m.b54*m.b58 - 128*
                       m.b52*m.b54*m.b59 - 64*m.b52*m.b54*m.b60 - 384*m.b52*m.b55*m.b56 - 288*m.b52*m.b55*m.b57 - 96*
                       m.b52*m.b55*m.b58 - 128*m.b52*m.b55*m.b59 - 64*m.b52*m.b55*m.b60 - 256*m.b52*m.b56*m.b57 - 192*
                       m.b52*m.b56*m.b58 - 128*m.b52*m.b56*m.b59 - 32*m.b52*m.b56*m.b60 - 192*m.b52*m.b57*m.b58 - 128*
                       m.b52*m.b57*m.b59 - 64*m.b52*m.b57*m.b60 - 128*m.b52*m.b58*m.b59 - 64*m.b52*m.b58*m.b60 - 64*
                       m.b52*m.b59*m.b60 - 352*m.b53*m.b54*m.b55 - 448*m.b53*m.b54*m.b56 - 352*m.b53*m.b54*m.b57 - 256*
                       m.b53*m.b54*m.b58 - 160*m.b53*m.b54*m.b59 - 64*m.b53*m.b54*m.b60 - 416*m.b53*m.b55*m.b56 - 192*
                       m.b53*m.b55*m.b57 - 224*m.b53*m.b55*m.b58 - 128*m.b53*m.b55*m.b59 - 64*m.b53*m.b55*m.b60 - 288*
                       m.b53*m.b56*m.b57 - 192*m.b53*m.b56*m.b58 - 64*m.b53*m.b56*m.b59 - 64*m.b53*m.b56*m.b60 - 192*
                       m.b53*m.b57*m.b58 - 128*m.b53*m.b57*m.b59 - 64*m.b53*m.b57*m.b60 - 128*m.b53*m.b58*m.b59 - 64*
                       m.b53*m.b58*m.b60 - 64*m.b53*m.b59*m.b60 - 288*m.b54*m.b55*m.b56 - 352*m.b54*m.b55*m.b57 - 256*
                       m.b54*m.b55*m.b58 - 160*m.b54*m.b55*m.b59 - 64*m.b54*m.b55*m.b60 - 320*m.b54*m.b56*m.b57 - 128*
                       m.b54*m.b56*m.b58 - 128*m.b54*m.b56*m.b59 - 64*m.b54*m.b56*m.b60 - 192*m.b54*m.b57*m.b58 - 128*
                       m.b54*m.b57*m.b59 - 32*m.b54*m.b57*m.b60 - 128*m.b54*m.b58*m.b59 - 64*m.b54*m.b58*m.b60 - 64*
                       m.b54*m.b59*m.b60 - 224*m.b55*m.b56*m.b57 - 256*m.b55*m.b56*m.b58 - 160*m.b55*m.b56*m.b59 - 64*
                       m.b55*m.b56*m.b60 - 224*m.b55*m.b57*m.b58 - 64*m.b55*m.b57*m.b59 - 64*m.b55*m.b57*m.b60 - 128*
                       m.b55*m.b58*m.b59 - 64*m.b55*m.b58*m.b60 - 64*m.b55*m.b59*m.b60 - 160*m.b56*m.b57*m.b58 - 160*
                       m.b56*m.b57*m.b59 - 64*m.b56*m.b57*m.b60 - 128*m.b56*m.b58*m.b59 - 32*m.b56*m.b58*m.b60 - 64*
                       m.b56*m.b59*m.b60 - 96*m.b57*m.b58*m.b59 - 64*m.b57*m.b58*m.b60 - 64*m.b57*m.b59*m.b60 - 32*m.b58
                       *m.b59*m.b60 + 192*m.b1*m.b2 + 184*m.b1*m.b3 + 176*m.b1*m.b4 + 168*m.b1*m.b5 + 160*m.b1*m.b6 + 
                       152*m.b1*m.b7 + 144*m.b1*m.b8 + 152*m.b1*m.b9 + 144*m.b1*m.b10 + 136*m.b1*m.b11 + 128*m.b1*m.b12
                        + 120*m.b1*m.b13 + 112*m.b1*m.b14 + 104*m.b1*m.b15 + 384*m.b2*m.b3 + 384*m.b2*m.b4 + 368*m.b2*
                       m.b5 + 352*m.b2*m.b6 + 336*m.b2*m.b7 + 320*m.b2*m.b8 + 320*m.b2*m.b9 + 320*m.b2*m.b10 + 304*m.b2*
                       m.b11 + 288*m.b2*m.b12 + 272*m.b2*m.b13 + 256*m.b2*m.b14 + 224*m.b2*m.b15 + 104*m.b2*m.b16 + 592*
                       m.b3*m.b4 + 584*m.b3*m.b5 + 576*m.b3*m.b6 + 552*m.b3*m.b7 + 528*m.b3*m.b8 + 504*m.b3*m.b9 + 512*
                       m.b3*m.b10 + 504*m.b3*m.b11 + 480*m.b3*m.b12 + 456*m.b3*m.b13 + 416*m.b3*m.b14 + 376*m.b3*m.b15
                        + 224*m.b3*m.b16 + 104*m.b3*m.b17 + 816*m.b4*m.b5 + 800*m.b4*m.b6 + 784*m.b4*m.b7 + 768*m.b4*
                       m.b8 + 736*m.b4*m.b9 + 720*m.b4*m.b10 + 720*m.b4*m.b11 + 704*m.b4*m.b12 + 656*m.b4*m.b13 + 608*
                       m.b4*m.b14 + 544*m.b4*m.b15 + 376*m.b4*m.b16 + 224*m.b4*m.b17 + 104*m.b4*m.b18 + 1056*m.b5*m.b6
                        + 1032*m.b5*m.b7 + 1008*m.b5*m.b8 + 984*m.b5*m.b9 + 960*m.b5*m.b10 + 952*m.b5*m.b11 + 928*m.b5*
                       m.b12 + 888*m.b5*m.b13 + 816*m.b5*m.b14 + 744*m.b5*m.b15 + 544*m.b5*m.b16 + 376*m.b5*m.b17 + 224*
                       m.b5*m.b18 + 104*m.b5*m.b19 + 1312*m.b6*m.b7 + 1280*m.b6*m.b8 + 1248*m.b6*m.b9 + 1216*m.b6*m.b10
                        + 1184*m.b6*m.b11 + 1168*m.b6*m.b12 + 1120*m.b6*m.b13 + 1056*m.b6*m.b14 + 960*m.b6*m.b15 + 744*
                       m.b6*m.b16 + 544*m.b6*m.b17 + 376*m.b6*m.b18 + 224*m.b6*m.b19 + 104*m.b6*m.b20 + 1584*m.b7*m.b8
                        + 1544*m.b7*m.b9 + 1488*m.b7*m.b10 + 1432*m.b7*m.b11 + 1392*m.b7*m.b12 + 1352*m.b7*m.b13 + 1296*
                       m.b7*m.b14 + 1208*m.b7*m.b15 + 960*m.b7*m.b16 + 744*m.b7*m.b17 + 544*m.b7*m.b18 + 376*m.b7*m.b19
                        + 224*m.b7*m.b20 + 104*m.b7*m.b21 + 1856*m.b8*m.b9 + 1792*m.b8*m.b10 + 1712*m.b8*m.b11 + 1648*
                       m.b8*m.b12 + 1584*m.b8*m.b13 + 1520*m.b8*m.b14 + 1440*m.b8*m.b15 + 1208*m.b8*m.b16 + 960*m.b8*
                       m.b17 + 744*m.b8*m.b18 + 544*m.b8*m.b19 + 376*m.b8*m.b20 + 224*m.b8*m.b21 + 104*m.b8*m.b22 + 2112
                       *m.b9*m.b10 + 2024*m.b9*m.b11 + 1920*m.b9*m.b12 + 1848*m.b9*m.b13 + 1760*m.b9*m.b14 + 1672*m.b9*
                       m.b15 + 1440*m.b9*m.b16 + 1208*m.b9*m.b17 + 960*m.b9*m.b18 + 744*m.b9*m.b19 + 544*m.b9*m.b20 + 
                       376*m.b9*m.b21 + 224*m.b9*m.b22 + 104*m.b9*m.b23 + 2352*m.b10*m.b11 + 2240*m.b10*m.b12 + 2128*
                       m.b10*m.b13 + 2032*m.b10*m.b14 + 1920*m.b10*m.b15 + 1672*m.b10*m.b16 + 1440*m.b10*m.b17 + 1208*
                       m.b10*m.b18 + 960*m.b10*m.b19 + 744*m.b10*m.b20 + 544*m.b10*m.b21 + 376*m.b10*m.b22 + 224*m.b10*
                       m.b23 + 104*m.b10*m.b24 + 2576*m.b11*m.b12 + 2440*m.b11*m.b13 + 2320*m.b11*m.b14 + 2200*m.b11*
                       m.b15 + 1920*m.b11*m.b16 + 1672*m.b11*m.b17 + 1440*m.b11*m.b18 + 1208*m.b11*m.b19 + 960*m.b11*
                       m.b20 + 744*m.b11*m.b21 + 544*m.b11*m.b22 + 376*m.b11*m.b23 + 224*m.b11*m.b24 + 104*m.b11*m.b25
                        + 2784*m.b12*m.b13 + 2640*m.b12*m.b14 + 2496*m.b12*m.b15 + 2200*m.b12*m.b16 + 1920*m.b12*m.b17
                        + 1672*m.b12*m.b18 + 1440*m.b12*m.b19 + 1208*m.b12*m.b20 + 960*m.b12*m.b21 + 744*m.b12*m.b22 + 
                       544*m.b12*m.b23 + 376*m.b12*m.b24 + 224*m.b12*m.b25 + 104*m.b12*m.b26 + 2976*m.b13*m.b14 + 2824*
                       m.b13*m.b15 + 2496*m.b13*m.b16 + 2200*m.b13*m.b17 + 1920*m.b13*m.b18 + 1672*m.b13*m.b19 + 1440*
                       m.b13*m.b20 + 1208*m.b13*m.b21 + 960*m.b13*m.b22 + 744*m.b13*m.b23 + 544*m.b13*m.b24 + 376*m.b13*
                       m.b25 + 224*m.b13*m.b26 + 104*m.b13*m.b27 + 3168*m.b14*m.b15 + 2824*m.b14*m.b16 + 2496*m.b14*
                       m.b17 + 2200*m.b14*m.b18 + 1920*m.b14*m.b19 + 1672*m.b14*m.b20 + 1440*m.b14*m.b21 + 1208*m.b14*
                       m.b22 + 960*m.b14*m.b23 + 744*m.b14*m.b24 + 544*m.b14*m.b25 + 376*m.b14*m.b26 + 224*m.b14*m.b27
                        + 104*m.b14*m.b28 + 3168*m.b15*m.b16 + 2824*m.b15*m.b17 + 2496*m.b15*m.b18 + 2200*m.b15*m.b19 + 
                       1920*m.b15*m.b20 + 1672*m.b15*m.b21 + 1440*m.b15*m.b22 + 1208*m.b15*m.b23 + 960*m.b15*m.b24 + 744
                       *m.b15*m.b25 + 544*m.b15*m.b26 + 376*m.b15*m.b27 + 224*m.b15*m.b28 + 104*m.b15*m.b29 + 3168*m.b16
                       *m.b17 + 2824*m.b16*m.b18 + 2496*m.b16*m.b19 + 2200*m.b16*m.b20 + 1920*m.b16*m.b21 + 1672*m.b16*
                       m.b22 + 1440*m.b16*m.b23 + 1208*m.b16*m.b24 + 960*m.b16*m.b25 + 744*m.b16*m.b26 + 544*m.b16*m.b27
                        + 376*m.b16*m.b28 + 224*m.b16*m.b29 + 104*m.b16*m.b30 + 3168*m.b17*m.b18 + 2824*m.b17*m.b19 + 
                       2496*m.b17*m.b20 + 2200*m.b17*m.b21 + 1920*m.b17*m.b22 + 1672*m.b17*m.b23 + 1440*m.b17*m.b24 + 
                       1208*m.b17*m.b25 + 960*m.b17*m.b26 + 744*m.b17*m.b27 + 544*m.b17*m.b28 + 376*m.b17*m.b29 + 224*
                       m.b17*m.b30 + 104*m.b17*m.b31 + 3168*m.b18*m.b19 + 2824*m.b18*m.b20 + 2496*m.b18*m.b21 + 2200*
                       m.b18*m.b22 + 1920*m.b18*m.b23 + 1672*m.b18*m.b24 + 1440*m.b18*m.b25 + 1208*m.b18*m.b26 + 960*
                       m.b18*m.b27 + 744*m.b18*m.b28 + 544*m.b18*m.b29 + 376*m.b18*m.b30 + 224*m.b18*m.b31 + 104*m.b18*
                       m.b32 + 3168*m.b19*m.b20 + 2824*m.b19*m.b21 + 2496*m.b19*m.b22 + 2200*m.b19*m.b23 + 1920*m.b19*
                       m.b24 + 1672*m.b19*m.b25 + 1440*m.b19*m.b26 + 1208*m.b19*m.b27 + 960*m.b19*m.b28 + 744*m.b19*
                       m.b29 + 544*m.b19*m.b30 + 376*m.b19*m.b31 + 224*m.b19*m.b32 + 104*m.b19*m.b33 + 3168*m.b20*m.b21
                        + 2824*m.b20*m.b22 + 2496*m.b20*m.b23 + 2200*m.b20*m.b24 + 1920*m.b20*m.b25 + 1672*m.b20*m.b26
                        + 1440*m.b20*m.b27 + 1208*m.b20*m.b28 + 960*m.b20*m.b29 + 744*m.b20*m.b30 + 544*m.b20*m.b31 + 
                       376*m.b20*m.b32 + 224*m.b20*m.b33 + 104*m.b20*m.b34 + 3168*m.b21*m.b22 + 2824*m.b21*m.b23 + 2496*
                       m.b21*m.b24 + 2200*m.b21*m.b25 + 1920*m.b21*m.b26 + 1672*m.b21*m.b27 + 1440*m.b21*m.b28 + 1208*
                       m.b21*m.b29 + 960*m.b21*m.b30 + 744*m.b21*m.b31 + 544*m.b21*m.b32 + 376*m.b21*m.b33 + 224*m.b21*
                       m.b34 + 104*m.b21*m.b35 + 3168*m.b22*m.b23 + 2824*m.b22*m.b24 + 2496*m.b22*m.b25 + 2200*m.b22*
                       m.b26 + 1920*m.b22*m.b27 + 1672*m.b22*m.b28 + 1440*m.b22*m.b29 + 1208*m.b22*m.b30 + 960*m.b22*
                       m.b31 + 744*m.b22*m.b32 + 544*m.b22*m.b33 + 376*m.b22*m.b34 + 224*m.b22*m.b35 + 104*m.b22*m.b36
                        + 3168*m.b23*m.b24 + 2824*m.b23*m.b25 + 2496*m.b23*m.b26 + 2200*m.b23*m.b27 + 1920*m.b23*m.b28
                        + 1672*m.b23*m.b29 + 1440*m.b23*m.b30 + 1208*m.b23*m.b31 + 960*m.b23*m.b32 + 744*m.b23*m.b33 + 
                       544*m.b23*m.b34 + 376*m.b23*m.b35 + 224*m.b23*m.b36 + 104*m.b23*m.b37 + 3168*m.b24*m.b25 + 2824*
                       m.b24*m.b26 + 2496*m.b24*m.b27 + 2200*m.b24*m.b28 + 1920*m.b24*m.b29 + 1672*m.b24*m.b30 + 1440*
                       m.b24*m.b31 + 1208*m.b24*m.b32 + 960*m.b24*m.b33 + 744*m.b24*m.b34 + 544*m.b24*m.b35 + 376*m.b24*
                       m.b36 + 224*m.b24*m.b37 + 104*m.b24*m.b38 + 3168*m.b25*m.b26 + 2824*m.b25*m.b27 + 2496*m.b25*
                       m.b28 + 2200*m.b25*m.b29 + 1920*m.b25*m.b30 + 1672*m.b25*m.b31 + 1440*m.b25*m.b32 + 1208*m.b25*
                       m.b33 + 960*m.b25*m.b34 + 744*m.b25*m.b35 + 544*m.b25*m.b36 + 376*m.b25*m.b37 + 224*m.b25*m.b38
                        + 104*m.b25*m.b39 + 3168*m.b26*m.b27 + 2824*m.b26*m.b28 + 2496*m.b26*m.b29 + 2200*m.b26*m.b30 + 
                       1920*m.b26*m.b31 + 1672*m.b26*m.b32 + 1440*m.b26*m.b33 + 1208*m.b26*m.b34 + 960*m.b26*m.b35 + 744
                       *m.b26*m.b36 + 544*m.b26*m.b37 + 376*m.b26*m.b38 + 224*m.b26*m.b39 + 104*m.b26*m.b40 + 3168*m.b27
                       *m.b28 + 2824*m.b27*m.b29 + 2496*m.b27*m.b30 + 2200*m.b27*m.b31 + 1920*m.b27*m.b32 + 1672*m.b27*
                       m.b33 + 1440*m.b27*m.b34 + 1208*m.b27*m.b35 + 960*m.b27*m.b36 + 744*m.b27*m.b37 + 544*m.b27*m.b38
                        + 376*m.b27*m.b39 + 224*m.b27*m.b40 + 104*m.b27*m.b41 + 3168*m.b28*m.b29 + 2824*m.b28*m.b30 + 
                       2496*m.b28*m.b31 + 2200*m.b28*m.b32 + 1920*m.b28*m.b33 + 1672*m.b28*m.b34 + 1440*m.b28*m.b35 + 
                       1208*m.b28*m.b36 + 960*m.b28*m.b37 + 744*m.b28*m.b38 + 544*m.b28*m.b39 + 376*m.b28*m.b40 + 224*
                       m.b28*m.b41 + 104*m.b28*m.b42 + 3168*m.b29*m.b30 + 2824*m.b29*m.b31 + 2496*m.b29*m.b32 + 2200*
                       m.b29*m.b33 + 1920*m.b29*m.b34 + 1672*m.b29*m.b35 + 1440*m.b29*m.b36 + 1208*m.b29*m.b37 + 960*
                       m.b29*m.b38 + 744*m.b29*m.b39 + 544*m.b29*m.b40 + 376*m.b29*m.b41 + 224*m.b29*m.b42 + 104*m.b29*
                       m.b43 + 3168*m.b30*m.b31 + 2824*m.b30*m.b32 + 2496*m.b30*m.b33 + 2200*m.b30*m.b34 + 1920*m.b30*
                       m.b35 + 1672*m.b30*m.b36 + 1440*m.b30*m.b37 + 1208*m.b30*m.b38 + 960*m.b30*m.b39 + 744*m.b30*
                       m.b40 + 544*m.b30*m.b41 + 376*m.b30*m.b42 + 224*m.b30*m.b43 + 104*m.b30*m.b44 + 3168*m.b31*m.b32
                        + 2824*m.b31*m.b33 + 2496*m.b31*m.b34 + 2200*m.b31*m.b35 + 1920*m.b31*m.b36 + 1672*m.b31*m.b37
                        + 1440*m.b31*m.b38 + 1208*m.b31*m.b39 + 960*m.b31*m.b40 + 744*m.b31*m.b41 + 544*m.b31*m.b42 + 
                       376*m.b31*m.b43 + 224*m.b31*m.b44 + 104*m.b31*m.b45 + 3168*m.b32*m.b33 + 2824*m.b32*m.b34 + 2496*
                       m.b32*m.b35 + 2200*m.b32*m.b36 + 1920*m.b32*m.b37 + 1672*m.b32*m.b38 + 1440*m.b32*m.b39 + 1208*
                       m.b32*m.b40 + 960*m.b32*m.b41 + 744*m.b32*m.b42 + 544*m.b32*m.b43 + 376*m.b32*m.b44 + 224*m.b32*
                       m.b45 + 104*m.b32*m.b46 + 3168*m.b33*m.b34 + 2824*m.b33*m.b35 + 2496*m.b33*m.b36 + 2200*m.b33*
                       m.b37 + 1920*m.b33*m.b38 + 1672*m.b33*m.b39 + 1440*m.b33*m.b40 + 1208*m.b33*m.b41 + 960*m.b33*
                       m.b42 + 744*m.b33*m.b43 + 544*m.b33*m.b44 + 376*m.b33*m.b45 + 224*m.b33*m.b46 + 104*m.b33*m.b47
                        + 3168*m.b34*m.b35 + 2824*m.b34*m.b36 + 2496*m.b34*m.b37 + 2200*m.b34*m.b38 + 1920*m.b34*m.b39
                        + 1672*m.b34*m.b40 + 1440*m.b34*m.b41 + 1208*m.b34*m.b42 + 960*m.b34*m.b43 + 744*m.b34*m.b44 + 
                       544*m.b34*m.b45 + 376*m.b34*m.b46 + 224*m.b34*m.b47 + 104*m.b34*m.b48 + 3168*m.b35*m.b36 + 2824*
                       m.b35*m.b37 + 2496*m.b35*m.b38 + 2200*m.b35*m.b39 + 1920*m.b35*m.b40 + 1672*m.b35*m.b41 + 1440*
                       m.b35*m.b42 + 1208*m.b35*m.b43 + 960*m.b35*m.b44 + 744*m.b35*m.b45 + 544*m.b35*m.b46 + 376*m.b35*
                       m.b47 + 224*m.b35*m.b48 + 104*m.b35*m.b49 + 3168*m.b36*m.b37 + 2824*m.b36*m.b38 + 2496*m.b36*
                       m.b39 + 2200*m.b36*m.b40 + 1920*m.b36*m.b41 + 1672*m.b36*m.b42 + 1440*m.b36*m.b43 + 1208*m.b36*
                       m.b44 + 960*m.b36*m.b45 + 744*m.b36*m.b46 + 544*m.b36*m.b47 + 376*m.b36*m.b48 + 224*m.b36*m.b49
                        + 104*m.b36*m.b50 + 3168*m.b37*m.b38 + 2824*m.b37*m.b39 + 2496*m.b37*m.b40 + 2200*m.b37*m.b41 + 
                       1920*m.b37*m.b42 + 1672*m.b37*m.b43 + 1440*m.b37*m.b44 + 1208*m.b37*m.b45 + 960*m.b37*m.b46 + 744
                       *m.b37*m.b47 + 544*m.b37*m.b48 + 376*m.b37*m.b49 + 224*m.b37*m.b50 + 104*m.b37*m.b51 + 3168*m.b38
                       *m.b39 + 2824*m.b38*m.b40 + 2496*m.b38*m.b41 + 2200*m.b38*m.b42 + 1920*m.b38*m.b43 + 1672*m.b38*
                       m.b44 + 1440*m.b38*m.b45 + 1208*m.b38*m.b46 + 960*m.b38*m.b47 + 744*m.b38*m.b48 + 544*m.b38*m.b49
                        + 376*m.b38*m.b50 + 224*m.b38*m.b51 + 104*m.b38*m.b52 + 3168*m.b39*m.b40 + 2824*m.b39*m.b41 + 
                       2496*m.b39*m.b42 + 2200*m.b39*m.b43 + 1920*m.b39*m.b44 + 1672*m.b39*m.b45 + 1440*m.b39*m.b46 + 
                       1208*m.b39*m.b47 + 960*m.b39*m.b48 + 744*m.b39*m.b49 + 544*m.b39*m.b50 + 376*m.b39*m.b51 + 224*
                       m.b39*m.b52 + 104*m.b39*m.b53 + 3168*m.b40*m.b41 + 2824*m.b40*m.b42 + 2496*m.b40*m.b43 + 2200*
                       m.b40*m.b44 + 1920*m.b40*m.b45 + 1672*m.b40*m.b46 + 1440*m.b40*m.b47 + 1208*m.b40*m.b48 + 960*
                       m.b40*m.b49 + 744*m.b40*m.b50 + 544*m.b40*m.b51 + 376*m.b40*m.b52 + 224*m.b40*m.b53 + 104*m.b40*
                       m.b54 + 3168*m.b41*m.b42 + 2824*m.b41*m.b43 + 2496*m.b41*m.b44 + 2200*m.b41*m.b45 + 1920*m.b41*
                       m.b46 + 1672*m.b41*m.b47 + 1440*m.b41*m.b48 + 1208*m.b41*m.b49 + 960*m.b41*m.b50 + 744*m.b41*
                       m.b51 + 544*m.b41*m.b52 + 376*m.b41*m.b53 + 224*m.b41*m.b54 + 104*m.b41*m.b55 + 3168*m.b42*m.b43
                        + 2824*m.b42*m.b44 + 2496*m.b42*m.b45 + 2200*m.b42*m.b46 + 1920*m.b42*m.b47 + 1672*m.b42*m.b48
                        + 1440*m.b42*m.b49 + 1208*m.b42*m.b50 + 960*m.b42*m.b51 + 744*m.b42*m.b52 + 544*m.b42*m.b53 + 
                       376*m.b42*m.b54 + 224*m.b42*m.b55 + 104*m.b42*m.b56 + 3168*m.b43*m.b44 + 2824*m.b43*m.b45 + 2496*
                       m.b43*m.b46 + 2200*m.b43*m.b47 + 1920*m.b43*m.b48 + 1672*m.b43*m.b49 + 1440*m.b43*m.b50 + 1208*
                       m.b43*m.b51 + 960*m.b43*m.b52 + 744*m.b43*m.b53 + 544*m.b43*m.b54 + 376*m.b43*m.b55 + 224*m.b43*
                       m.b56 + 104*m.b43*m.b57 + 3168*m.b44*m.b45 + 2824*m.b44*m.b46 + 2496*m.b44*m.b47 + 2200*m.b44*
                       m.b48 + 1920*m.b44*m.b49 + 1672*m.b44*m.b50 + 1440*m.b44*m.b51 + 1208*m.b44*m.b52 + 960*m.b44*
                       m.b53 + 744*m.b44*m.b54 + 544*m.b44*m.b55 + 376*m.b44*m.b56 + 224*m.b44*m.b57 + 104*m.b44*m.b58
                        + 3168*m.b45*m.b46 + 2824*m.b45*m.b47 + 2496*m.b45*m.b48 + 2200*m.b45*m.b49 + 1920*m.b45*m.b50
                        + 1672*m.b45*m.b51 + 1440*m.b45*m.b52 + 1208*m.b45*m.b53 + 960*m.b45*m.b54 + 744*m.b45*m.b55 + 
                       544*m.b45*m.b56 + 376*m.b45*m.b57 + 224*m.b45*m.b58 + 104*m.b45*m.b59 + 3168*m.b46*m.b47 + 2824*
                       m.b46*m.b48 + 2496*m.b46*m.b49 + 2200*m.b46*m.b50 + 1920*m.b46*m.b51 + 1672*m.b46*m.b52 + 1440*
                       m.b46*m.b53 + 1208*m.b46*m.b54 + 960*m.b46*m.b55 + 744*m.b46*m.b56 + 544*m.b46*m.b57 + 376*m.b46*
                       m.b58 + 224*m.b46*m.b59 + 104*m.b46*m.b60 + 2976*m.b47*m.b48 + 2640*m.b47*m.b49 + 2320*m.b47*
                       m.b50 + 2032*m.b47*m.b51 + 1760*m.b47*m.b52 + 1520*m.b47*m.b53 + 1296*m.b47*m.b54 + 1056*m.b47*
                       m.b55 + 816*m.b47*m.b56 + 608*m.b47*m.b57 + 416*m.b47*m.b58 + 256*m.b47*m.b59 + 112*m.b47*m.b60
                        + 2784*m.b48*m.b49 + 2440*m.b48*m.b50 + 2128*m.b48*m.b51 + 1848*m.b48*m.b52 + 1584*m.b48*m.b53
                        + 1352*m.b48*m.b54 + 1120*m.b48*m.b55 + 888*m.b48*m.b56 + 656*m.b48*m.b57 + 456*m.b48*m.b58 + 
                       272*m.b48*m.b59 + 120*m.b48*m.b60 + 2576*m.b49*m.b50 + 2240*m.b49*m.b51 + 1920*m.b49*m.b52 + 1648
                       *m.b49*m.b53 + 1392*m.b49*m.b54 + 1168*m.b49*m.b55 + 928*m.b49*m.b56 + 704*m.b49*m.b57 + 480*
                       m.b49*m.b58 + 288*m.b49*m.b59 + 128*m.b49*m.b60 + 2352*m.b50*m.b51 + 2024*m.b50*m.b52 + 1712*
                       m.b50*m.b53 + 1432*m.b50*m.b54 + 1184*m.b50*m.b55 + 952*m.b50*m.b56 + 720*m.b50*m.b57 + 504*m.b50
                       *m.b58 + 304*m.b50*m.b59 + 136*m.b50*m.b60 + 2112*m.b51*m.b52 + 1792*m.b51*m.b53 + 1488*m.b51*
                       m.b54 + 1216*m.b51*m.b55 + 960*m.b51*m.b56 + 720*m.b51*m.b57 + 512*m.b51*m.b58 + 320*m.b51*m.b59
                        + 144*m.b51*m.b60 + 1856*m.b52*m.b53 + 1544*m.b52*m.b54 + 1248*m.b52*m.b55 + 984*m.b52*m.b56 + 
                       736*m.b52*m.b57 + 504*m.b52*m.b58 + 320*m.b52*m.b59 + 152*m.b52*m.b60 + 1584*m.b53*m.b54 + 1280*
                       m.b53*m.b55 + 1008*m.b53*m.b56 + 768*m.b53*m.b57 + 528*m.b53*m.b58 + 320*m.b53*m.b59 + 144*m.b53*
                       m.b60 + 1312*m.b54*m.b55 + 1032*m.b54*m.b56 + 784*m.b54*m.b57 + 552*m.b54*m.b58 + 336*m.b54*m.b59
                        + 152*m.b54*m.b60 + 1056*m.b55*m.b56 + 800*m.b55*m.b57 + 576*m.b55*m.b58 + 352*m.b55*m.b59 + 160
                       *m.b55*m.b60 + 816*m.b56*m.b57 + 584*m.b56*m.b58 + 368*m.b56*m.b59 + 168*m.b56*m.b60 + 592*m.b57*
                       m.b58 + 384*m.b57*m.b59 + 176*m.b57*m.b60 + 384*m.b58*m.b59 + 184*m.b58*m.b60 + 192*m.b59*m.b60
                        - 364*m.b1 - 772*m.b2 - 1216*m.b3 - 1688*m.b4 - 2180*m.b5 - 2684*m.b6 - 3192*m.b7 - 3696*m.b8 - 
                       4204*m.b9 - 4708*m.b10 - 5200*m.b11 - 5672*m.b12 - 6116*m.b13 - 6524*m.b14 - 6888*m.b15 - 6888*
                       m.b16 - 6888*m.b17 - 6888*m.b18 - 6888*m.b19 - 6888*m.b20 - 6888*m.b21 - 6888*m.b22 - 6888*m.b23
                        - 6888*m.b24 - 6888*m.b25 - 6888*m.b26 - 6888*m.b27 - 6888*m.b28 - 6888*m.b29 - 6888*m.b30 - 
                       6888*m.b31 - 6888*m.b32 - 6888*m.b33 - 6888*m.b34 - 6888*m.b35 - 6888*m.b36 - 6888*m.b37 - 6888*
                       m.b38 - 6888*m.b39 - 6888*m.b40 - 6888*m.b41 - 6888*m.b42 - 6888*m.b43 - 6888*m.b44 - 6888*m.b45
                        - 6888*m.b46 - 6524*m.b47 - 6116*m.b48 - 5672*m.b49 - 5200*m.b50 - 4708*m.b51 - 4204*m.b52 - 
                       3696*m.b53 - 3192*m.b54 - 2684*m.b55 - 2180*m.b56 - 1688*m.b57 - 1216*m.b58 - 772*m.b59 - 364*
                       m.b60 - m.x61 <= 0)
