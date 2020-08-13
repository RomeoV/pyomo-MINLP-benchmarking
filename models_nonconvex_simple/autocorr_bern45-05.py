#  MINLP written by GAMS Convert at 08/13/20 17:37:49
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         46        1       45        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         46        1       45        0


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
m.x46 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x46, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 128*m.b2*m.b3*m.b4*m.b5 + 64*m.b2*m.b3*m.b5*
                       m.b6 + 128*m.b3*m.b4*m.b5*m.b6 + 64*m.b3*m.b4*m.b6*m.b7 + 128*m.b4*m.b5*m.b6*m.b7 + 64*m.b4*m.b5*
                       m.b7*m.b8 + 128*m.b5*m.b6*m.b7*m.b8 + 64*m.b5*m.b6*m.b8*m.b9 + 128*m.b6*m.b7*m.b8*m.b9 + 64*m.b6*
                       m.b7*m.b9*m.b10 + 128*m.b7*m.b8*m.b9*m.b10 + 64*m.b7*m.b8*m.b10*m.b11 + 128*m.b8*m.b9*m.b10*m.b11
                        + 64*m.b8*m.b9*m.b11*m.b12 + 128*m.b9*m.b10*m.b11*m.b12 + 64*m.b9*m.b10*m.b12*m.b13 + 128*m.b10*
                       m.b11*m.b12*m.b13 + 64*m.b10*m.b11*m.b13*m.b14 + 128*m.b11*m.b12*m.b13*m.b14 + 64*m.b11*m.b12*
                       m.b14*m.b15 + 128*m.b12*m.b13*m.b14*m.b15 + 64*m.b12*m.b13*m.b15*m.b16 + 128*m.b13*m.b14*m.b15*
                       m.b16 + 64*m.b13*m.b14*m.b16*m.b17 + 128*m.b14*m.b15*m.b16*m.b17 + 64*m.b14*m.b15*m.b17*m.b18 + 
                       128*m.b15*m.b16*m.b17*m.b18 + 64*m.b15*m.b16*m.b18*m.b19 + 128*m.b16*m.b17*m.b18*m.b19 + 64*m.b16
                       *m.b17*m.b19*m.b20 + 128*m.b17*m.b18*m.b19*m.b20 + 64*m.b17*m.b18*m.b20*m.b21 + 128*m.b18*m.b19*
                       m.b20*m.b21 + 64*m.b18*m.b19*m.b21*m.b22 + 128*m.b19*m.b20*m.b21*m.b22 + 64*m.b19*m.b20*m.b22*
                       m.b23 + 128*m.b20*m.b21*m.b22*m.b23 + 64*m.b20*m.b21*m.b23*m.b24 + 128*m.b21*m.b22*m.b23*m.b24 + 
                       64*m.b21*m.b22*m.b24*m.b25 + 128*m.b22*m.b23*m.b24*m.b25 + 64*m.b22*m.b23*m.b25*m.b26 + 128*m.b23
                       *m.b24*m.b25*m.b26 + 64*m.b23*m.b24*m.b26*m.b27 + 128*m.b24*m.b25*m.b26*m.b27 + 64*m.b24*m.b25*
                       m.b27*m.b28 + 128*m.b25*m.b26*m.b27*m.b28 + 64*m.b25*m.b26*m.b28*m.b29 + 128*m.b26*m.b27*m.b28*
                       m.b29 + 64*m.b26*m.b27*m.b29*m.b30 + 128*m.b27*m.b28*m.b29*m.b30 + 64*m.b27*m.b28*m.b30*m.b31 + 
                       128*m.b28*m.b29*m.b30*m.b31 + 64*m.b28*m.b29*m.b31*m.b32 + 128*m.b29*m.b30*m.b31*m.b32 + 64*m.b29
                       *m.b30*m.b32*m.b33 + 128*m.b30*m.b31*m.b32*m.b33 + 64*m.b30*m.b31*m.b33*m.b34 + 128*m.b31*m.b32*
                       m.b33*m.b34 + 64*m.b31*m.b32*m.b34*m.b35 + 128*m.b32*m.b33*m.b34*m.b35 + 64*m.b32*m.b33*m.b35*
                       m.b36 + 128*m.b33*m.b34*m.b35*m.b36 + 64*m.b33*m.b34*m.b36*m.b37 + 128*m.b34*m.b35*m.b36*m.b37 + 
                       64*m.b34*m.b35*m.b37*m.b38 + 128*m.b35*m.b36*m.b37*m.b38 + 64*m.b35*m.b36*m.b38*m.b39 + 128*m.b36
                       *m.b37*m.b38*m.b39 + 64*m.b36*m.b37*m.b39*m.b40 + 128*m.b37*m.b38*m.b39*m.b40 + 64*m.b37*m.b38*
                       m.b40*m.b41 + 128*m.b38*m.b39*m.b40*m.b41 + 64*m.b38*m.b39*m.b41*m.b42 + 128*m.b39*m.b40*m.b41*
                       m.b42 + 64*m.b39*m.b40*m.b42*m.b43 + 128*m.b40*m.b41*m.b42*m.b43 + 64*m.b40*m.b41*m.b43*m.b44 + 
                       128*m.b41*m.b42*m.b43*m.b44 + 64*m.b41*m.b42*m.b44*m.b45 + 64*m.b42*m.b43*m.b44*m.b45 - 32*m.b1*
                       m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 32*m.b1*m.b2*m.b5 - 32*m.b1*m.b3*m.b4 - 32*m.b1*m.b4*m.b5 - 96*
                       m.b2*m.b3*m.b4 - 96*m.b2*m.b3*m.b5 - 32*m.b2*m.b3*m.b6 - 96*m.b2*m.b4*m.b5 - 32*m.b2*m.b5*m.b6 - 
                       128*m.b3*m.b4*m.b5 - 96*m.b3*m.b4*m.b6 - 32*m.b3*m.b4*m.b7 - 96*m.b3*m.b5*m.b6 - 32*m.b3*m.b6*
                       m.b7 - 128*m.b4*m.b5*m.b6 - 96*m.b4*m.b5*m.b7 - 32*m.b4*m.b5*m.b8 - 96*m.b4*m.b6*m.b7 - 32*m.b4*
                       m.b7*m.b8 - 128*m.b5*m.b6*m.b7 - 96*m.b5*m.b6*m.b8 - 32*m.b5*m.b6*m.b9 - 96*m.b5*m.b7*m.b8 - 32*
                       m.b5*m.b8*m.b9 - 128*m.b6*m.b7*m.b8 - 96*m.b6*m.b7*m.b9 - 32*m.b6*m.b7*m.b10 - 96*m.b6*m.b8*m.b9
                        - 32*m.b6*m.b9*m.b10 - 128*m.b7*m.b8*m.b9 - 96*m.b7*m.b8*m.b10 - 32*m.b7*m.b8*m.b11 - 96*m.b7*
                       m.b9*m.b10 - 32*m.b7*m.b10*m.b11 - 128*m.b8*m.b9*m.b10 - 96*m.b8*m.b9*m.b11 - 32*m.b8*m.b9*m.b12
                        - 96*m.b8*m.b10*m.b11 - 32*m.b8*m.b11*m.b12 - 128*m.b9*m.b10*m.b11 - 96*m.b9*m.b10*m.b12 - 32*
                       m.b9*m.b10*m.b13 - 96*m.b9*m.b11*m.b12 - 32*m.b9*m.b12*m.b13 - 128*m.b10*m.b11*m.b12 - 96*m.b10*
                       m.b11*m.b13 - 32*m.b10*m.b11*m.b14 - 96*m.b10*m.b12*m.b13 - 32*m.b10*m.b13*m.b14 - 128*m.b11*
                       m.b12*m.b13 - 96*m.b11*m.b12*m.b14 - 32*m.b11*m.b12*m.b15 - 96*m.b11*m.b13*m.b14 - 32*m.b11*m.b14
                       *m.b15 - 128*m.b12*m.b13*m.b14 - 96*m.b12*m.b13*m.b15 - 32*m.b12*m.b13*m.b16 - 96*m.b12*m.b14*
                       m.b15 - 32*m.b12*m.b15*m.b16 - 128*m.b13*m.b14*m.b15 - 96*m.b13*m.b14*m.b16 - 32*m.b13*m.b14*
                       m.b17 - 96*m.b13*m.b15*m.b16 - 32*m.b13*m.b16*m.b17 - 128*m.b14*m.b15*m.b16 - 96*m.b14*m.b15*
                       m.b17 - 32*m.b14*m.b15*m.b18 - 96*m.b14*m.b16*m.b17 - 32*m.b14*m.b17*m.b18 - 128*m.b15*m.b16*
                       m.b17 - 96*m.b15*m.b16*m.b18 - 32*m.b15*m.b16*m.b19 - 96*m.b15*m.b17*m.b18 - 32*m.b15*m.b18*m.b19
                        - 128*m.b16*m.b17*m.b18 - 96*m.b16*m.b17*m.b19 - 32*m.b16*m.b17*m.b20 - 96*m.b16*m.b18*m.b19 - 
                       32*m.b16*m.b19*m.b20 - 128*m.b17*m.b18*m.b19 - 96*m.b17*m.b18*m.b20 - 32*m.b17*m.b18*m.b21 - 96*
                       m.b17*m.b19*m.b20 - 32*m.b17*m.b20*m.b21 - 128*m.b18*m.b19*m.b20 - 96*m.b18*m.b19*m.b21 - 32*
                       m.b18*m.b19*m.b22 - 96*m.b18*m.b20*m.b21 - 32*m.b18*m.b21*m.b22 - 128*m.b19*m.b20*m.b21 - 96*
                       m.b19*m.b20*m.b22 - 32*m.b19*m.b20*m.b23 - 96*m.b19*m.b21*m.b22 - 32*m.b19*m.b22*m.b23 - 128*
                       m.b20*m.b21*m.b22 - 96*m.b20*m.b21*m.b23 - 32*m.b20*m.b21*m.b24 - 96*m.b20*m.b22*m.b23 - 32*m.b20
                       *m.b23*m.b24 - 128*m.b21*m.b22*m.b23 - 96*m.b21*m.b22*m.b24 - 32*m.b21*m.b22*m.b25 - 96*m.b21*
                       m.b23*m.b24 - 32*m.b21*m.b24*m.b25 - 128*m.b22*m.b23*m.b24 - 96*m.b22*m.b23*m.b25 - 32*m.b22*
                       m.b23*m.b26 - 96*m.b22*m.b24*m.b25 - 32*m.b22*m.b25*m.b26 - 128*m.b23*m.b24*m.b25 - 96*m.b23*
                       m.b24*m.b26 - 32*m.b23*m.b24*m.b27 - 96*m.b23*m.b25*m.b26 - 32*m.b23*m.b26*m.b27 - 128*m.b24*
                       m.b25*m.b26 - 96*m.b24*m.b25*m.b27 - 32*m.b24*m.b25*m.b28 - 96*m.b24*m.b26*m.b27 - 32*m.b24*m.b27
                       *m.b28 - 128*m.b25*m.b26*m.b27 - 96*m.b25*m.b26*m.b28 - 32*m.b25*m.b26*m.b29 - 96*m.b25*m.b27*
                       m.b28 - 32*m.b25*m.b28*m.b29 - 128*m.b26*m.b27*m.b28 - 96*m.b26*m.b27*m.b29 - 32*m.b26*m.b27*
                       m.b30 - 96*m.b26*m.b28*m.b29 - 32*m.b26*m.b29*m.b30 - 128*m.b27*m.b28*m.b29 - 96*m.b27*m.b28*
                       m.b30 - 32*m.b27*m.b28*m.b31 - 96*m.b27*m.b29*m.b30 - 32*m.b27*m.b30*m.b31 - 128*m.b28*m.b29*
                       m.b30 - 96*m.b28*m.b29*m.b31 - 32*m.b28*m.b29*m.b32 - 96*m.b28*m.b30*m.b31 - 32*m.b28*m.b31*m.b32
                        - 128*m.b29*m.b30*m.b31 - 96*m.b29*m.b30*m.b32 - 32*m.b29*m.b30*m.b33 - 96*m.b29*m.b31*m.b32 - 
                       32*m.b29*m.b32*m.b33 - 128*m.b30*m.b31*m.b32 - 96*m.b30*m.b31*m.b33 - 32*m.b30*m.b31*m.b34 - 96*
                       m.b30*m.b32*m.b33 - 32*m.b30*m.b33*m.b34 - 128*m.b31*m.b32*m.b33 - 96*m.b31*m.b32*m.b34 - 32*
                       m.b31*m.b32*m.b35 - 96*m.b31*m.b33*m.b34 - 32*m.b31*m.b34*m.b35 - 128*m.b32*m.b33*m.b34 - 96*
                       m.b32*m.b33*m.b35 - 32*m.b32*m.b33*m.b36 - 96*m.b32*m.b34*m.b35 - 32*m.b32*m.b35*m.b36 - 128*
                       m.b33*m.b34*m.b35 - 96*m.b33*m.b34*m.b36 - 32*m.b33*m.b34*m.b37 - 96*m.b33*m.b35*m.b36 - 32*m.b33
                       *m.b36*m.b37 - 128*m.b34*m.b35*m.b36 - 96*m.b34*m.b35*m.b37 - 32*m.b34*m.b35*m.b38 - 96*m.b34*
                       m.b36*m.b37 - 32*m.b34*m.b37*m.b38 - 128*m.b35*m.b36*m.b37 - 96*m.b35*m.b36*m.b38 - 32*m.b35*
                       m.b36*m.b39 - 96*m.b35*m.b37*m.b38 - 32*m.b35*m.b38*m.b39 - 128*m.b36*m.b37*m.b38 - 96*m.b36*
                       m.b37*m.b39 - 32*m.b36*m.b37*m.b40 - 96*m.b36*m.b38*m.b39 - 32*m.b36*m.b39*m.b40 - 128*m.b37*
                       m.b38*m.b39 - 96*m.b37*m.b38*m.b40 - 32*m.b37*m.b38*m.b41 - 96*m.b37*m.b39*m.b40 - 32*m.b37*m.b40
                       *m.b41 - 128*m.b38*m.b39*m.b40 - 96*m.b38*m.b39*m.b41 - 32*m.b38*m.b39*m.b42 - 96*m.b38*m.b40*
                       m.b41 - 32*m.b38*m.b41*m.b42 - 128*m.b39*m.b40*m.b41 - 96*m.b39*m.b40*m.b42 - 32*m.b39*m.b40*
                       m.b43 - 96*m.b39*m.b41*m.b42 - 32*m.b39*m.b42*m.b43 - 128*m.b40*m.b41*m.b42 - 96*m.b40*m.b41*
                       m.b43 - 32*m.b40*m.b41*m.b44 - 96*m.b40*m.b42*m.b43 - 32*m.b40*m.b43*m.b44 - 128*m.b41*m.b42*
                       m.b43 - 96*m.b41*m.b42*m.b44 - 32*m.b41*m.b42*m.b45 - 96*m.b41*m.b43*m.b44 - 32*m.b41*m.b44*m.b45
                        - 96*m.b42*m.b43*m.b44 - 32*m.b42*m.b43*m.b45 - 64*m.b42*m.b44*m.b45 - 32*m.b43*m.b44*m.b45 + 32
                       *m.b1*m.b2 + 24*m.b1*m.b3 + 32*m.b1*m.b4 + 24*m.b1*m.b5 + 64*m.b2*m.b3 + 80*m.b2*m.b4 + 64*m.b2*
                       m.b5 + 24*m.b2*m.b6 + 96*m.b3*m.b4 + 104*m.b3*m.b5 + 64*m.b3*m.b6 + 24*m.b3*m.b7 + 128*m.b4*m.b5
                        + 104*m.b4*m.b6 + 64*m.b4*m.b7 + 24*m.b4*m.b8 + 128*m.b5*m.b6 + 104*m.b5*m.b7 + 64*m.b5*m.b8 + 
                       24*m.b5*m.b9 + 128*m.b6*m.b7 + 104*m.b6*m.b8 + 64*m.b6*m.b9 + 24*m.b6*m.b10 + 128*m.b7*m.b8 + 104
                       *m.b7*m.b9 + 64*m.b7*m.b10 + 24*m.b7*m.b11 + 128*m.b8*m.b9 + 104*m.b8*m.b10 + 64*m.b8*m.b11 + 24*
                       m.b8*m.b12 + 128*m.b9*m.b10 + 104*m.b9*m.b11 + 64*m.b9*m.b12 + 24*m.b9*m.b13 + 128*m.b10*m.b11 + 
                       104*m.b10*m.b12 + 64*m.b10*m.b13 + 24*m.b10*m.b14 + 128*m.b11*m.b12 + 104*m.b11*m.b13 + 64*m.b11*
                       m.b14 + 24*m.b11*m.b15 + 128*m.b12*m.b13 + 104*m.b12*m.b14 + 64*m.b12*m.b15 + 24*m.b12*m.b16 + 
                       128*m.b13*m.b14 + 104*m.b13*m.b15 + 64*m.b13*m.b16 + 24*m.b13*m.b17 + 128*m.b14*m.b15 + 104*m.b14
                       *m.b16 + 64*m.b14*m.b17 + 24*m.b14*m.b18 + 128*m.b15*m.b16 + 104*m.b15*m.b17 + 64*m.b15*m.b18 + 
                       24*m.b15*m.b19 + 128*m.b16*m.b17 + 104*m.b16*m.b18 + 64*m.b16*m.b19 + 24*m.b16*m.b20 + 128*m.b17*
                       m.b18 + 104*m.b17*m.b19 + 64*m.b17*m.b20 + 24*m.b17*m.b21 + 128*m.b18*m.b19 + 104*m.b18*m.b20 + 
                       64*m.b18*m.b21 + 24*m.b18*m.b22 + 128*m.b19*m.b20 + 104*m.b19*m.b21 + 64*m.b19*m.b22 + 24*m.b19*
                       m.b23 + 128*m.b20*m.b21 + 104*m.b20*m.b22 + 64*m.b20*m.b23 + 24*m.b20*m.b24 + 128*m.b21*m.b22 + 
                       104*m.b21*m.b23 + 64*m.b21*m.b24 + 24*m.b21*m.b25 + 128*m.b22*m.b23 + 104*m.b22*m.b24 + 64*m.b22*
                       m.b25 + 24*m.b22*m.b26 + 128*m.b23*m.b24 + 104*m.b23*m.b25 + 64*m.b23*m.b26 + 24*m.b23*m.b27 + 
                       128*m.b24*m.b25 + 104*m.b24*m.b26 + 64*m.b24*m.b27 + 24*m.b24*m.b28 + 128*m.b25*m.b26 + 104*m.b25
                       *m.b27 + 64*m.b25*m.b28 + 24*m.b25*m.b29 + 128*m.b26*m.b27 + 104*m.b26*m.b28 + 64*m.b26*m.b29 + 
                       24*m.b26*m.b30 + 128*m.b27*m.b28 + 104*m.b27*m.b29 + 64*m.b27*m.b30 + 24*m.b27*m.b31 + 128*m.b28*
                       m.b29 + 104*m.b28*m.b30 + 64*m.b28*m.b31 + 24*m.b28*m.b32 + 128*m.b29*m.b30 + 104*m.b29*m.b31 + 
                       64*m.b29*m.b32 + 24*m.b29*m.b33 + 128*m.b30*m.b31 + 104*m.b30*m.b32 + 64*m.b30*m.b33 + 24*m.b30*
                       m.b34 + 128*m.b31*m.b32 + 104*m.b31*m.b33 + 64*m.b31*m.b34 + 24*m.b31*m.b35 + 128*m.b32*m.b33 + 
                       104*m.b32*m.b34 + 64*m.b32*m.b35 + 24*m.b32*m.b36 + 128*m.b33*m.b34 + 104*m.b33*m.b35 + 64*m.b33*
                       m.b36 + 24*m.b33*m.b37 + 128*m.b34*m.b35 + 104*m.b34*m.b36 + 64*m.b34*m.b37 + 24*m.b34*m.b38 + 
                       128*m.b35*m.b36 + 104*m.b35*m.b37 + 64*m.b35*m.b38 + 24*m.b35*m.b39 + 128*m.b36*m.b37 + 104*m.b36
                       *m.b38 + 64*m.b36*m.b39 + 24*m.b36*m.b40 + 128*m.b37*m.b38 + 104*m.b37*m.b39 + 64*m.b37*m.b40 + 
                       24*m.b37*m.b41 + 128*m.b38*m.b39 + 104*m.b38*m.b40 + 64*m.b38*m.b41 + 24*m.b38*m.b42 + 128*m.b39*
                       m.b40 + 104*m.b39*m.b41 + 64*m.b39*m.b42 + 24*m.b39*m.b43 + 128*m.b40*m.b41 + 104*m.b40*m.b42 + 
                       64*m.b40*m.b43 + 24*m.b40*m.b44 + 128*m.b41*m.b42 + 104*m.b41*m.b43 + 64*m.b41*m.b44 + 24*m.b41*
                       m.b45 + 96*m.b42*m.b43 + 80*m.b42*m.b44 + 32*m.b42*m.b45 + 64*m.b43*m.b44 + 24*m.b43*m.b45 + 32*
                       m.b44*m.b45 - 24*m.b1 - 52*m.b2 - 76*m.b3 - 104*m.b4 - 128*m.b5 - 128*m.b6 - 128*m.b7 - 128*m.b8
                        - 128*m.b9 - 128*m.b10 - 128*m.b11 - 128*m.b12 - 128*m.b13 - 128*m.b14 - 128*m.b15 - 128*m.b16
                        - 128*m.b17 - 128*m.b18 - 128*m.b19 - 128*m.b20 - 128*m.b21 - 128*m.b22 - 128*m.b23 - 128*m.b24
                        - 128*m.b25 - 128*m.b26 - 128*m.b27 - 128*m.b28 - 128*m.b29 - 128*m.b30 - 128*m.b31 - 128*m.b32
                        - 128*m.b33 - 128*m.b34 - 128*m.b35 - 128*m.b36 - 128*m.b37 - 128*m.b38 - 128*m.b39 - 128*m.b40
                        - 128*m.b41 - 104*m.b42 - 76*m.b43 - 52*m.b44 - 24*m.b45 - m.x46 <= 0)
