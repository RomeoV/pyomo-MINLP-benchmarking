#  MINLP written by GAMS Convert at 08/13/20 17:37:44
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         21        1       20        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         21        1       20        0


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
m.x21 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x21, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 128*m.b2*m.b3*m.b4*m.b5 + 64*m.b2*m.b3*m.b5*
                       m.b6 + 128*m.b3*m.b4*m.b5*m.b6 + 64*m.b3*m.b4*m.b6*m.b7 + 128*m.b4*m.b5*m.b6*m.b7 + 64*m.b4*m.b5*
                       m.b7*m.b8 + 128*m.b5*m.b6*m.b7*m.b8 + 64*m.b5*m.b6*m.b8*m.b9 + 128*m.b6*m.b7*m.b8*m.b9 + 64*m.b6*
                       m.b7*m.b9*m.b10 + 128*m.b7*m.b8*m.b9*m.b10 + 64*m.b7*m.b8*m.b10*m.b11 + 128*m.b8*m.b9*m.b10*m.b11
                        + 64*m.b8*m.b9*m.b11*m.b12 + 128*m.b9*m.b10*m.b11*m.b12 + 64*m.b9*m.b10*m.b12*m.b13 + 128*m.b10*
                       m.b11*m.b12*m.b13 + 64*m.b10*m.b11*m.b13*m.b14 + 128*m.b11*m.b12*m.b13*m.b14 + 64*m.b11*m.b12*
                       m.b14*m.b15 + 128*m.b12*m.b13*m.b14*m.b15 + 64*m.b12*m.b13*m.b15*m.b16 + 128*m.b13*m.b14*m.b15*
                       m.b16 + 64*m.b13*m.b14*m.b16*m.b17 + 128*m.b14*m.b15*m.b16*m.b17 + 64*m.b14*m.b15*m.b17*m.b18 + 
                       128*m.b15*m.b16*m.b17*m.b18 + 64*m.b15*m.b16*m.b18*m.b19 + 128*m.b16*m.b17*m.b18*m.b19 + 64*m.b16
                       *m.b17*m.b19*m.b20 + 64*m.b17*m.b18*m.b19*m.b20 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 32*m.b1
                       *m.b2*m.b5 - 32*m.b1*m.b3*m.b4 - 32*m.b1*m.b4*m.b5 - 96*m.b2*m.b3*m.b4 - 96*m.b2*m.b3*m.b5 - 32*
                       m.b2*m.b3*m.b6 - 96*m.b2*m.b4*m.b5 - 32*m.b2*m.b5*m.b6 - 128*m.b3*m.b4*m.b5 - 96*m.b3*m.b4*m.b6
                        - 32*m.b3*m.b4*m.b7 - 96*m.b3*m.b5*m.b6 - 32*m.b3*m.b6*m.b7 - 128*m.b4*m.b5*m.b6 - 96*m.b4*m.b5*
                       m.b7 - 32*m.b4*m.b5*m.b8 - 96*m.b4*m.b6*m.b7 - 32*m.b4*m.b7*m.b8 - 128*m.b5*m.b6*m.b7 - 96*m.b5*
                       m.b6*m.b8 - 32*m.b5*m.b6*m.b9 - 96*m.b5*m.b7*m.b8 - 32*m.b5*m.b8*m.b9 - 128*m.b6*m.b7*m.b8 - 96*
                       m.b6*m.b7*m.b9 - 32*m.b6*m.b7*m.b10 - 96*m.b6*m.b8*m.b9 - 32*m.b6*m.b9*m.b10 - 128*m.b7*m.b8*m.b9
                        - 96*m.b7*m.b8*m.b10 - 32*m.b7*m.b8*m.b11 - 96*m.b7*m.b9*m.b10 - 32*m.b7*m.b10*m.b11 - 128*m.b8*
                       m.b9*m.b10 - 96*m.b8*m.b9*m.b11 - 32*m.b8*m.b9*m.b12 - 96*m.b8*m.b10*m.b11 - 32*m.b8*m.b11*m.b12
                        - 128*m.b9*m.b10*m.b11 - 96*m.b9*m.b10*m.b12 - 32*m.b9*m.b10*m.b13 - 96*m.b9*m.b11*m.b12 - 32*
                       m.b9*m.b12*m.b13 - 128*m.b10*m.b11*m.b12 - 96*m.b10*m.b11*m.b13 - 32*m.b10*m.b11*m.b14 - 96*m.b10
                       *m.b12*m.b13 - 32*m.b10*m.b13*m.b14 - 128*m.b11*m.b12*m.b13 - 96*m.b11*m.b12*m.b14 - 32*m.b11*
                       m.b12*m.b15 - 96*m.b11*m.b13*m.b14 - 32*m.b11*m.b14*m.b15 - 128*m.b12*m.b13*m.b14 - 96*m.b12*
                       m.b13*m.b15 - 32*m.b12*m.b13*m.b16 - 96*m.b12*m.b14*m.b15 - 32*m.b12*m.b15*m.b16 - 128*m.b13*
                       m.b14*m.b15 - 96*m.b13*m.b14*m.b16 - 32*m.b13*m.b14*m.b17 - 96*m.b13*m.b15*m.b16 - 32*m.b13*m.b16
                       *m.b17 - 128*m.b14*m.b15*m.b16 - 96*m.b14*m.b15*m.b17 - 32*m.b14*m.b15*m.b18 - 96*m.b14*m.b16*
                       m.b17 - 32*m.b14*m.b17*m.b18 - 128*m.b15*m.b16*m.b17 - 96*m.b15*m.b16*m.b18 - 32*m.b15*m.b16*
                       m.b19 - 96*m.b15*m.b17*m.b18 - 32*m.b15*m.b18*m.b19 - 128*m.b16*m.b17*m.b18 - 96*m.b16*m.b17*
                       m.b19 - 32*m.b16*m.b17*m.b20 - 96*m.b16*m.b18*m.b19 - 32*m.b16*m.b19*m.b20 - 96*m.b17*m.b18*m.b19
                        - 32*m.b17*m.b18*m.b20 - 64*m.b17*m.b19*m.b20 - 32*m.b18*m.b19*m.b20 + 32*m.b1*m.b2 + 24*m.b1*
                       m.b3 + 32*m.b1*m.b4 + 24*m.b1*m.b5 + 64*m.b2*m.b3 + 80*m.b2*m.b4 + 64*m.b2*m.b5 + 24*m.b2*m.b6 + 
                       96*m.b3*m.b4 + 104*m.b3*m.b5 + 64*m.b3*m.b6 + 24*m.b3*m.b7 + 128*m.b4*m.b5 + 104*m.b4*m.b6 + 64*
                       m.b4*m.b7 + 24*m.b4*m.b8 + 128*m.b5*m.b6 + 104*m.b5*m.b7 + 64*m.b5*m.b8 + 24*m.b5*m.b9 + 128*m.b6
                       *m.b7 + 104*m.b6*m.b8 + 64*m.b6*m.b9 + 24*m.b6*m.b10 + 128*m.b7*m.b8 + 104*m.b7*m.b9 + 64*m.b7*
                       m.b10 + 24*m.b7*m.b11 + 128*m.b8*m.b9 + 104*m.b8*m.b10 + 64*m.b8*m.b11 + 24*m.b8*m.b12 + 128*m.b9
                       *m.b10 + 104*m.b9*m.b11 + 64*m.b9*m.b12 + 24*m.b9*m.b13 + 128*m.b10*m.b11 + 104*m.b10*m.b12 + 64*
                       m.b10*m.b13 + 24*m.b10*m.b14 + 128*m.b11*m.b12 + 104*m.b11*m.b13 + 64*m.b11*m.b14 + 24*m.b11*
                       m.b15 + 128*m.b12*m.b13 + 104*m.b12*m.b14 + 64*m.b12*m.b15 + 24*m.b12*m.b16 + 128*m.b13*m.b14 + 
                       104*m.b13*m.b15 + 64*m.b13*m.b16 + 24*m.b13*m.b17 + 128*m.b14*m.b15 + 104*m.b14*m.b16 + 64*m.b14*
                       m.b17 + 24*m.b14*m.b18 + 128*m.b15*m.b16 + 104*m.b15*m.b17 + 64*m.b15*m.b18 + 24*m.b15*m.b19 + 
                       128*m.b16*m.b17 + 104*m.b16*m.b18 + 64*m.b16*m.b19 + 24*m.b16*m.b20 + 96*m.b17*m.b18 + 80*m.b17*
                       m.b19 + 32*m.b17*m.b20 + 64*m.b18*m.b19 + 24*m.b18*m.b20 + 32*m.b19*m.b20 - 24*m.b1 - 52*m.b2 - 
                       76*m.b3 - 104*m.b4 - 128*m.b5 - 128*m.b6 - 128*m.b7 - 128*m.b8 - 128*m.b9 - 128*m.b10 - 128*m.b11
                        - 128*m.b12 - 128*m.b13 - 128*m.b14 - 128*m.b15 - 128*m.b16 - 104*m.b17 - 76*m.b18 - 52*m.b19 - 
                       24*m.b20 - m.x21 <= 0)
