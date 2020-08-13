#  MINLP written by GAMS Convert at 08/13/20 17:37:51
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          1        0        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         51        1       50        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         51        1       50        0


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
m.x51 = Var(within=Reals,bounds=(None,None),initialize=0)

m.obj = Objective(expr=m.x51, sense=minimize)

m.c1 = Constraint(expr=64*m.b1*m.b2*m.b3*m.b4 + 64*m.b1*m.b2*m.b4*m.b5 + 64*m.b1*m.b2*m.b5*m.b6 + 64*m.b1*m.b3*m.b4*m.b6
                        + 128*m.b2*m.b3*m.b4*m.b5 + 128*m.b2*m.b3*m.b5*m.b6 + 64*m.b2*m.b3*m.b6*m.b7 + 64*m.b2*m.b4*m.b5
                       *m.b7 + 192*m.b3*m.b4*m.b5*m.b6 + 128*m.b3*m.b4*m.b6*m.b7 + 64*m.b3*m.b4*m.b7*m.b8 + 64*m.b3*m.b5
                       *m.b6*m.b8 + 192*m.b4*m.b5*m.b6*m.b7 + 128*m.b4*m.b5*m.b7*m.b8 + 64*m.b4*m.b5*m.b8*m.b9 + 64*m.b4
                       *m.b6*m.b7*m.b9 + 192*m.b5*m.b6*m.b7*m.b8 + 128*m.b5*m.b6*m.b8*m.b9 + 64*m.b5*m.b6*m.b9*m.b10 + 
                       64*m.b5*m.b7*m.b8*m.b10 + 192*m.b6*m.b7*m.b8*m.b9 + 128*m.b6*m.b7*m.b9*m.b10 + 64*m.b6*m.b7*m.b10
                       *m.b11 + 64*m.b6*m.b8*m.b9*m.b11 + 192*m.b7*m.b8*m.b9*m.b10 + 128*m.b7*m.b8*m.b10*m.b11 + 64*m.b7
                       *m.b8*m.b11*m.b12 + 64*m.b7*m.b9*m.b10*m.b12 + 192*m.b8*m.b9*m.b10*m.b11 + 128*m.b8*m.b9*m.b11*
                       m.b12 + 64*m.b8*m.b9*m.b12*m.b13 + 64*m.b8*m.b10*m.b11*m.b13 + 192*m.b9*m.b10*m.b11*m.b12 + 128*
                       m.b9*m.b10*m.b12*m.b13 + 64*m.b9*m.b10*m.b13*m.b14 + 64*m.b9*m.b11*m.b12*m.b14 + 192*m.b10*m.b11*
                       m.b12*m.b13 + 128*m.b10*m.b11*m.b13*m.b14 + 64*m.b10*m.b11*m.b14*m.b15 + 64*m.b10*m.b12*m.b13*
                       m.b15 + 192*m.b11*m.b12*m.b13*m.b14 + 128*m.b11*m.b12*m.b14*m.b15 + 64*m.b11*m.b12*m.b15*m.b16 + 
                       64*m.b11*m.b13*m.b14*m.b16 + 192*m.b12*m.b13*m.b14*m.b15 + 128*m.b12*m.b13*m.b15*m.b16 + 64*m.b12
                       *m.b13*m.b16*m.b17 + 64*m.b12*m.b14*m.b15*m.b17 + 192*m.b13*m.b14*m.b15*m.b16 + 128*m.b13*m.b14*
                       m.b16*m.b17 + 64*m.b13*m.b14*m.b17*m.b18 + 64*m.b13*m.b15*m.b16*m.b18 + 192*m.b14*m.b15*m.b16*
                       m.b17 + 128*m.b14*m.b15*m.b17*m.b18 + 64*m.b14*m.b15*m.b18*m.b19 + 64*m.b14*m.b16*m.b17*m.b19 + 
                       192*m.b15*m.b16*m.b17*m.b18 + 128*m.b15*m.b16*m.b18*m.b19 + 64*m.b15*m.b16*m.b19*m.b20 + 64*m.b15
                       *m.b17*m.b18*m.b20 + 192*m.b16*m.b17*m.b18*m.b19 + 128*m.b16*m.b17*m.b19*m.b20 + 64*m.b16*m.b17*
                       m.b20*m.b21 + 64*m.b16*m.b18*m.b19*m.b21 + 192*m.b17*m.b18*m.b19*m.b20 + 128*m.b17*m.b18*m.b20*
                       m.b21 + 64*m.b17*m.b18*m.b21*m.b22 + 64*m.b17*m.b19*m.b20*m.b22 + 192*m.b18*m.b19*m.b20*m.b21 + 
                       128*m.b18*m.b19*m.b21*m.b22 + 64*m.b18*m.b19*m.b22*m.b23 + 64*m.b18*m.b20*m.b21*m.b23 + 192*m.b19
                       *m.b20*m.b21*m.b22 + 128*m.b19*m.b20*m.b22*m.b23 + 64*m.b19*m.b20*m.b23*m.b24 + 64*m.b19*m.b21*
                       m.b22*m.b24 + 192*m.b20*m.b21*m.b22*m.b23 + 128*m.b20*m.b21*m.b23*m.b24 + 64*m.b20*m.b21*m.b24*
                       m.b25 + 64*m.b20*m.b22*m.b23*m.b25 + 192*m.b21*m.b22*m.b23*m.b24 + 128*m.b21*m.b22*m.b24*m.b25 + 
                       64*m.b21*m.b22*m.b25*m.b26 + 64*m.b21*m.b23*m.b24*m.b26 + 192*m.b22*m.b23*m.b24*m.b25 + 128*m.b22
                       *m.b23*m.b25*m.b26 + 64*m.b22*m.b23*m.b26*m.b27 + 64*m.b22*m.b24*m.b25*m.b27 + 192*m.b23*m.b24*
                       m.b25*m.b26 + 128*m.b23*m.b24*m.b26*m.b27 + 64*m.b23*m.b24*m.b27*m.b28 + 64*m.b23*m.b25*m.b26*
                       m.b28 + 192*m.b24*m.b25*m.b26*m.b27 + 128*m.b24*m.b25*m.b27*m.b28 + 64*m.b24*m.b25*m.b28*m.b29 + 
                       64*m.b24*m.b26*m.b27*m.b29 + 192*m.b25*m.b26*m.b27*m.b28 + 128*m.b25*m.b26*m.b28*m.b29 + 64*m.b25
                       *m.b26*m.b29*m.b30 + 64*m.b25*m.b27*m.b28*m.b30 + 192*m.b26*m.b27*m.b28*m.b29 + 128*m.b26*m.b27*
                       m.b29*m.b30 + 64*m.b26*m.b27*m.b30*m.b31 + 64*m.b26*m.b28*m.b29*m.b31 + 192*m.b27*m.b28*m.b29*
                       m.b30 + 128*m.b27*m.b28*m.b30*m.b31 + 64*m.b27*m.b28*m.b31*m.b32 + 64*m.b27*m.b29*m.b30*m.b32 + 
                       192*m.b28*m.b29*m.b30*m.b31 + 128*m.b28*m.b29*m.b31*m.b32 + 64*m.b28*m.b29*m.b32*m.b33 + 64*m.b28
                       *m.b30*m.b31*m.b33 + 192*m.b29*m.b30*m.b31*m.b32 + 128*m.b29*m.b30*m.b32*m.b33 + 64*m.b29*m.b30*
                       m.b33*m.b34 + 64*m.b29*m.b31*m.b32*m.b34 + 192*m.b30*m.b31*m.b32*m.b33 + 128*m.b30*m.b31*m.b33*
                       m.b34 + 64*m.b30*m.b31*m.b34*m.b35 + 64*m.b30*m.b32*m.b33*m.b35 + 192*m.b31*m.b32*m.b33*m.b34 + 
                       128*m.b31*m.b32*m.b34*m.b35 + 64*m.b31*m.b32*m.b35*m.b36 + 64*m.b31*m.b33*m.b34*m.b36 + 192*m.b32
                       *m.b33*m.b34*m.b35 + 128*m.b32*m.b33*m.b35*m.b36 + 64*m.b32*m.b33*m.b36*m.b37 + 64*m.b32*m.b34*
                       m.b35*m.b37 + 192*m.b33*m.b34*m.b35*m.b36 + 128*m.b33*m.b34*m.b36*m.b37 + 64*m.b33*m.b34*m.b37*
                       m.b38 + 64*m.b33*m.b35*m.b36*m.b38 + 192*m.b34*m.b35*m.b36*m.b37 + 128*m.b34*m.b35*m.b37*m.b38 + 
                       64*m.b34*m.b35*m.b38*m.b39 + 64*m.b34*m.b36*m.b37*m.b39 + 192*m.b35*m.b36*m.b37*m.b38 + 128*m.b35
                       *m.b36*m.b38*m.b39 + 64*m.b35*m.b36*m.b39*m.b40 + 64*m.b35*m.b37*m.b38*m.b40 + 192*m.b36*m.b37*
                       m.b38*m.b39 + 128*m.b36*m.b37*m.b39*m.b40 + 64*m.b36*m.b37*m.b40*m.b41 + 64*m.b36*m.b38*m.b39*
                       m.b41 + 192*m.b37*m.b38*m.b39*m.b40 + 128*m.b37*m.b38*m.b40*m.b41 + 64*m.b37*m.b38*m.b41*m.b42 + 
                       64*m.b37*m.b39*m.b40*m.b42 + 192*m.b38*m.b39*m.b40*m.b41 + 128*m.b38*m.b39*m.b41*m.b42 + 64*m.b38
                       *m.b39*m.b42*m.b43 + 64*m.b38*m.b40*m.b41*m.b43 + 192*m.b39*m.b40*m.b41*m.b42 + 128*m.b39*m.b40*
                       m.b42*m.b43 + 64*m.b39*m.b40*m.b43*m.b44 + 64*m.b39*m.b41*m.b42*m.b44 + 192*m.b40*m.b41*m.b42*
                       m.b43 + 128*m.b40*m.b41*m.b43*m.b44 + 64*m.b40*m.b41*m.b44*m.b45 + 64*m.b40*m.b42*m.b43*m.b45 + 
                       192*m.b41*m.b42*m.b43*m.b44 + 128*m.b41*m.b42*m.b44*m.b45 + 64*m.b41*m.b42*m.b45*m.b46 + 64*m.b41
                       *m.b43*m.b44*m.b46 + 192*m.b42*m.b43*m.b44*m.b45 + 128*m.b42*m.b43*m.b45*m.b46 + 64*m.b42*m.b43*
                       m.b46*m.b47 + 64*m.b42*m.b44*m.b45*m.b47 + 192*m.b43*m.b44*m.b45*m.b46 + 128*m.b43*m.b44*m.b46*
                       m.b47 + 64*m.b43*m.b44*m.b47*m.b48 + 64*m.b43*m.b45*m.b46*m.b48 + 192*m.b44*m.b45*m.b46*m.b47 + 
                       128*m.b44*m.b45*m.b47*m.b48 + 64*m.b44*m.b45*m.b48*m.b49 + 64*m.b44*m.b46*m.b47*m.b49 + 192*m.b45
                       *m.b46*m.b47*m.b48 + 128*m.b45*m.b46*m.b48*m.b49 + 64*m.b45*m.b46*m.b49*m.b50 + 64*m.b45*m.b47*
                       m.b48*m.b50 + 128*m.b46*m.b47*m.b48*m.b49 + 64*m.b46*m.b47*m.b49*m.b50 + 64*m.b47*m.b48*m.b49*
                       m.b50 - 32*m.b1*m.b2*m.b3 - 64*m.b1*m.b2*m.b4 - 64*m.b1*m.b2*m.b5 - 32*m.b1*m.b2*m.b6 - 64*m.b1*
                       m.b3*m.b4 - 32*m.b1*m.b3*m.b6 - 32*m.b1*m.b4*m.b5 - 32*m.b1*m.b4*m.b6 - 32*m.b1*m.b5*m.b6 - 96*
                       m.b2*m.b3*m.b4 - 128*m.b2*m.b3*m.b5 - 96*m.b2*m.b3*m.b6 - 32*m.b2*m.b3*m.b7 - 128*m.b2*m.b4*m.b5
                        - 32*m.b2*m.b4*m.b7 - 96*m.b2*m.b5*m.b6 - 32*m.b2*m.b5*m.b7 - 32*m.b2*m.b6*m.b7 - 160*m.b3*m.b4*
                       m.b5 - 192*m.b3*m.b4*m.b6 - 96*m.b3*m.b4*m.b7 - 32*m.b3*m.b4*m.b8 - 192*m.b3*m.b5*m.b6 - 32*m.b3*
                       m.b5*m.b8 - 96*m.b3*m.b6*m.b7 - 32*m.b3*m.b6*m.b8 - 32*m.b3*m.b7*m.b8 - 192*m.b4*m.b5*m.b6 - 192*
                       m.b4*m.b5*m.b7 - 96*m.b4*m.b5*m.b8 - 32*m.b4*m.b5*m.b9 - 192*m.b4*m.b6*m.b7 - 32*m.b4*m.b6*m.b9
                        - 96*m.b4*m.b7*m.b8 - 32*m.b4*m.b7*m.b9 - 32*m.b4*m.b8*m.b9 - 192*m.b5*m.b6*m.b7 - 192*m.b5*m.b6
                       *m.b8 - 96*m.b5*m.b6*m.b9 - 32*m.b5*m.b6*m.b10 - 192*m.b5*m.b7*m.b8 - 32*m.b5*m.b7*m.b10 - 96*
                       m.b5*m.b8*m.b9 - 32*m.b5*m.b8*m.b10 - 32*m.b5*m.b9*m.b10 - 192*m.b6*m.b7*m.b8 - 192*m.b6*m.b7*
                       m.b9 - 96*m.b6*m.b7*m.b10 - 32*m.b6*m.b7*m.b11 - 192*m.b6*m.b8*m.b9 - 32*m.b6*m.b8*m.b11 - 96*
                       m.b6*m.b9*m.b10 - 32*m.b6*m.b9*m.b11 - 32*m.b6*m.b10*m.b11 - 192*m.b7*m.b8*m.b9 - 192*m.b7*m.b8*
                       m.b10 - 96*m.b7*m.b8*m.b11 - 32*m.b7*m.b8*m.b12 - 192*m.b7*m.b9*m.b10 - 32*m.b7*m.b9*m.b12 - 96*
                       m.b7*m.b10*m.b11 - 32*m.b7*m.b10*m.b12 - 32*m.b7*m.b11*m.b12 - 192*m.b8*m.b9*m.b10 - 192*m.b8*
                       m.b9*m.b11 - 96*m.b8*m.b9*m.b12 - 32*m.b8*m.b9*m.b13 - 192*m.b8*m.b10*m.b11 - 32*m.b8*m.b10*m.b13
                        - 96*m.b8*m.b11*m.b12 - 32*m.b8*m.b11*m.b13 - 32*m.b8*m.b12*m.b13 - 192*m.b9*m.b10*m.b11 - 192*
                       m.b9*m.b10*m.b12 - 96*m.b9*m.b10*m.b13 - 32*m.b9*m.b10*m.b14 - 192*m.b9*m.b11*m.b12 - 32*m.b9*
                       m.b11*m.b14 - 96*m.b9*m.b12*m.b13 - 32*m.b9*m.b12*m.b14 - 32*m.b9*m.b13*m.b14 - 192*m.b10*m.b11*
                       m.b12 - 192*m.b10*m.b11*m.b13 - 96*m.b10*m.b11*m.b14 - 32*m.b10*m.b11*m.b15 - 192*m.b10*m.b12*
                       m.b13 - 32*m.b10*m.b12*m.b15 - 96*m.b10*m.b13*m.b14 - 32*m.b10*m.b13*m.b15 - 32*m.b10*m.b14*m.b15
                        - 192*m.b11*m.b12*m.b13 - 192*m.b11*m.b12*m.b14 - 96*m.b11*m.b12*m.b15 - 32*m.b11*m.b12*m.b16 - 
                       192*m.b11*m.b13*m.b14 - 32*m.b11*m.b13*m.b16 - 96*m.b11*m.b14*m.b15 - 32*m.b11*m.b14*m.b16 - 32*
                       m.b11*m.b15*m.b16 - 192*m.b12*m.b13*m.b14 - 192*m.b12*m.b13*m.b15 - 96*m.b12*m.b13*m.b16 - 32*
                       m.b12*m.b13*m.b17 - 192*m.b12*m.b14*m.b15 - 32*m.b12*m.b14*m.b17 - 96*m.b12*m.b15*m.b16 - 32*
                       m.b12*m.b15*m.b17 - 32*m.b12*m.b16*m.b17 - 192*m.b13*m.b14*m.b15 - 192*m.b13*m.b14*m.b16 - 96*
                       m.b13*m.b14*m.b17 - 32*m.b13*m.b14*m.b18 - 192*m.b13*m.b15*m.b16 - 32*m.b13*m.b15*m.b18 - 96*
                       m.b13*m.b16*m.b17 - 32*m.b13*m.b16*m.b18 - 32*m.b13*m.b17*m.b18 - 192*m.b14*m.b15*m.b16 - 192*
                       m.b14*m.b15*m.b17 - 96*m.b14*m.b15*m.b18 - 32*m.b14*m.b15*m.b19 - 192*m.b14*m.b16*m.b17 - 32*
                       m.b14*m.b16*m.b19 - 96*m.b14*m.b17*m.b18 - 32*m.b14*m.b17*m.b19 - 32*m.b14*m.b18*m.b19 - 192*
                       m.b15*m.b16*m.b17 - 192*m.b15*m.b16*m.b18 - 96*m.b15*m.b16*m.b19 - 32*m.b15*m.b16*m.b20 - 192*
                       m.b15*m.b17*m.b18 - 32*m.b15*m.b17*m.b20 - 96*m.b15*m.b18*m.b19 - 32*m.b15*m.b18*m.b20 - 32*m.b15
                       *m.b19*m.b20 - 192*m.b16*m.b17*m.b18 - 192*m.b16*m.b17*m.b19 - 96*m.b16*m.b17*m.b20 - 32*m.b16*
                       m.b17*m.b21 - 192*m.b16*m.b18*m.b19 - 32*m.b16*m.b18*m.b21 - 96*m.b16*m.b19*m.b20 - 32*m.b16*
                       m.b19*m.b21 - 32*m.b16*m.b20*m.b21 - 192*m.b17*m.b18*m.b19 - 192*m.b17*m.b18*m.b20 - 96*m.b17*
                       m.b18*m.b21 - 32*m.b17*m.b18*m.b22 - 192*m.b17*m.b19*m.b20 - 32*m.b17*m.b19*m.b22 - 96*m.b17*
                       m.b20*m.b21 - 32*m.b17*m.b20*m.b22 - 32*m.b17*m.b21*m.b22 - 192*m.b18*m.b19*m.b20 - 192*m.b18*
                       m.b19*m.b21 - 96*m.b18*m.b19*m.b22 - 32*m.b18*m.b19*m.b23 - 192*m.b18*m.b20*m.b21 - 32*m.b18*
                       m.b20*m.b23 - 96*m.b18*m.b21*m.b22 - 32*m.b18*m.b21*m.b23 - 32*m.b18*m.b22*m.b23 - 192*m.b19*
                       m.b20*m.b21 - 192*m.b19*m.b20*m.b22 - 96*m.b19*m.b20*m.b23 - 32*m.b19*m.b20*m.b24 - 192*m.b19*
                       m.b21*m.b22 - 32*m.b19*m.b21*m.b24 - 96*m.b19*m.b22*m.b23 - 32*m.b19*m.b22*m.b24 - 32*m.b19*m.b23
                       *m.b24 - 192*m.b20*m.b21*m.b22 - 192*m.b20*m.b21*m.b23 - 96*m.b20*m.b21*m.b24 - 32*m.b20*m.b21*
                       m.b25 - 192*m.b20*m.b22*m.b23 - 32*m.b20*m.b22*m.b25 - 96*m.b20*m.b23*m.b24 - 32*m.b20*m.b23*
                       m.b25 - 32*m.b20*m.b24*m.b25 - 192*m.b21*m.b22*m.b23 - 192*m.b21*m.b22*m.b24 - 96*m.b21*m.b22*
                       m.b25 - 32*m.b21*m.b22*m.b26 - 192*m.b21*m.b23*m.b24 - 32*m.b21*m.b23*m.b26 - 96*m.b21*m.b24*
                       m.b25 - 32*m.b21*m.b24*m.b26 - 32*m.b21*m.b25*m.b26 - 192*m.b22*m.b23*m.b24 - 192*m.b22*m.b23*
                       m.b25 - 96*m.b22*m.b23*m.b26 - 32*m.b22*m.b23*m.b27 - 192*m.b22*m.b24*m.b25 - 32*m.b22*m.b24*
                       m.b27 - 96*m.b22*m.b25*m.b26 - 32*m.b22*m.b25*m.b27 - 32*m.b22*m.b26*m.b27 - 192*m.b23*m.b24*
                       m.b25 - 192*m.b23*m.b24*m.b26 - 96*m.b23*m.b24*m.b27 - 32*m.b23*m.b24*m.b28 - 192*m.b23*m.b25*
                       m.b26 - 32*m.b23*m.b25*m.b28 - 96*m.b23*m.b26*m.b27 - 32*m.b23*m.b26*m.b28 - 32*m.b23*m.b27*m.b28
                        - 192*m.b24*m.b25*m.b26 - 192*m.b24*m.b25*m.b27 - 96*m.b24*m.b25*m.b28 - 32*m.b24*m.b25*m.b29 - 
                       192*m.b24*m.b26*m.b27 - 32*m.b24*m.b26*m.b29 - 96*m.b24*m.b27*m.b28 - 32*m.b24*m.b27*m.b29 - 32*
                       m.b24*m.b28*m.b29 - 192*m.b25*m.b26*m.b27 - 192*m.b25*m.b26*m.b28 - 96*m.b25*m.b26*m.b29 - 32*
                       m.b25*m.b26*m.b30 - 192*m.b25*m.b27*m.b28 - 32*m.b25*m.b27*m.b30 - 96*m.b25*m.b28*m.b29 - 32*
                       m.b25*m.b28*m.b30 - 32*m.b25*m.b29*m.b30 - 192*m.b26*m.b27*m.b28 - 192*m.b26*m.b27*m.b29 - 96*
                       m.b26*m.b27*m.b30 - 32*m.b26*m.b27*m.b31 - 192*m.b26*m.b28*m.b29 - 32*m.b26*m.b28*m.b31 - 96*
                       m.b26*m.b29*m.b30 - 32*m.b26*m.b29*m.b31 - 32*m.b26*m.b30*m.b31 - 192*m.b27*m.b28*m.b29 - 192*
                       m.b27*m.b28*m.b30 - 96*m.b27*m.b28*m.b31 - 32*m.b27*m.b28*m.b32 - 192*m.b27*m.b29*m.b30 - 32*
                       m.b27*m.b29*m.b32 - 96*m.b27*m.b30*m.b31 - 32*m.b27*m.b30*m.b32 - 32*m.b27*m.b31*m.b32 - 192*
                       m.b28*m.b29*m.b30 - 192*m.b28*m.b29*m.b31 - 96*m.b28*m.b29*m.b32 - 32*m.b28*m.b29*m.b33 - 192*
                       m.b28*m.b30*m.b31 - 32*m.b28*m.b30*m.b33 - 96*m.b28*m.b31*m.b32 - 32*m.b28*m.b31*m.b33 - 32*m.b28
                       *m.b32*m.b33 - 192*m.b29*m.b30*m.b31 - 192*m.b29*m.b30*m.b32 - 96*m.b29*m.b30*m.b33 - 32*m.b29*
                       m.b30*m.b34 - 192*m.b29*m.b31*m.b32 - 32*m.b29*m.b31*m.b34 - 96*m.b29*m.b32*m.b33 - 32*m.b29*
                       m.b32*m.b34 - 32*m.b29*m.b33*m.b34 - 192*m.b30*m.b31*m.b32 - 192*m.b30*m.b31*m.b33 - 96*m.b30*
                       m.b31*m.b34 - 32*m.b30*m.b31*m.b35 - 192*m.b30*m.b32*m.b33 - 32*m.b30*m.b32*m.b35 - 96*m.b30*
                       m.b33*m.b34 - 32*m.b30*m.b33*m.b35 - 32*m.b30*m.b34*m.b35 - 192*m.b31*m.b32*m.b33 - 192*m.b31*
                       m.b32*m.b34 - 96*m.b31*m.b32*m.b35 - 32*m.b31*m.b32*m.b36 - 192*m.b31*m.b33*m.b34 - 32*m.b31*
                       m.b33*m.b36 - 96*m.b31*m.b34*m.b35 - 32*m.b31*m.b34*m.b36 - 32*m.b31*m.b35*m.b36 - 192*m.b32*
                       m.b33*m.b34 - 192*m.b32*m.b33*m.b35 - 96*m.b32*m.b33*m.b36 - 32*m.b32*m.b33*m.b37 - 192*m.b32*
                       m.b34*m.b35 - 32*m.b32*m.b34*m.b37 - 96*m.b32*m.b35*m.b36 - 32*m.b32*m.b35*m.b37 - 32*m.b32*m.b36
                       *m.b37 - 192*m.b33*m.b34*m.b35 - 192*m.b33*m.b34*m.b36 - 96*m.b33*m.b34*m.b37 - 32*m.b33*m.b34*
                       m.b38 - 192*m.b33*m.b35*m.b36 - 32*m.b33*m.b35*m.b38 - 96*m.b33*m.b36*m.b37 - 32*m.b33*m.b36*
                       m.b38 - 32*m.b33*m.b37*m.b38 - 192*m.b34*m.b35*m.b36 - 192*m.b34*m.b35*m.b37 - 96*m.b34*m.b35*
                       m.b38 - 32*m.b34*m.b35*m.b39 - 192*m.b34*m.b36*m.b37 - 32*m.b34*m.b36*m.b39 - 96*m.b34*m.b37*
                       m.b38 - 32*m.b34*m.b37*m.b39 - 32*m.b34*m.b38*m.b39 - 192*m.b35*m.b36*m.b37 - 192*m.b35*m.b36*
                       m.b38 - 96*m.b35*m.b36*m.b39 - 32*m.b35*m.b36*m.b40 - 192*m.b35*m.b37*m.b38 - 32*m.b35*m.b37*
                       m.b40 - 96*m.b35*m.b38*m.b39 - 32*m.b35*m.b38*m.b40 - 32*m.b35*m.b39*m.b40 - 192*m.b36*m.b37*
                       m.b38 - 192*m.b36*m.b37*m.b39 - 96*m.b36*m.b37*m.b40 - 32*m.b36*m.b37*m.b41 - 192*m.b36*m.b38*
                       m.b39 - 32*m.b36*m.b38*m.b41 - 96*m.b36*m.b39*m.b40 - 32*m.b36*m.b39*m.b41 - 32*m.b36*m.b40*m.b41
                        - 192*m.b37*m.b38*m.b39 - 192*m.b37*m.b38*m.b40 - 96*m.b37*m.b38*m.b41 - 32*m.b37*m.b38*m.b42 - 
                       192*m.b37*m.b39*m.b40 - 32*m.b37*m.b39*m.b42 - 96*m.b37*m.b40*m.b41 - 32*m.b37*m.b40*m.b42 - 32*
                       m.b37*m.b41*m.b42 - 192*m.b38*m.b39*m.b40 - 192*m.b38*m.b39*m.b41 - 96*m.b38*m.b39*m.b42 - 32*
                       m.b38*m.b39*m.b43 - 192*m.b38*m.b40*m.b41 - 32*m.b38*m.b40*m.b43 - 96*m.b38*m.b41*m.b42 - 32*
                       m.b38*m.b41*m.b43 - 32*m.b38*m.b42*m.b43 - 192*m.b39*m.b40*m.b41 - 192*m.b39*m.b40*m.b42 - 96*
                       m.b39*m.b40*m.b43 - 32*m.b39*m.b40*m.b44 - 192*m.b39*m.b41*m.b42 - 32*m.b39*m.b41*m.b44 - 96*
                       m.b39*m.b42*m.b43 - 32*m.b39*m.b42*m.b44 - 32*m.b39*m.b43*m.b44 - 192*m.b40*m.b41*m.b42 - 192*
                       m.b40*m.b41*m.b43 - 96*m.b40*m.b41*m.b44 - 32*m.b40*m.b41*m.b45 - 192*m.b40*m.b42*m.b43 - 32*
                       m.b40*m.b42*m.b45 - 96*m.b40*m.b43*m.b44 - 32*m.b40*m.b43*m.b45 - 32*m.b40*m.b44*m.b45 - 192*
                       m.b41*m.b42*m.b43 - 192*m.b41*m.b42*m.b44 - 96*m.b41*m.b42*m.b45 - 32*m.b41*m.b42*m.b46 - 192*
                       m.b41*m.b43*m.b44 - 32*m.b41*m.b43*m.b46 - 96*m.b41*m.b44*m.b45 - 32*m.b41*m.b44*m.b46 - 32*m.b41
                       *m.b45*m.b46 - 192*m.b42*m.b43*m.b44 - 192*m.b42*m.b43*m.b45 - 96*m.b42*m.b43*m.b46 - 32*m.b42*
                       m.b43*m.b47 - 192*m.b42*m.b44*m.b45 - 32*m.b42*m.b44*m.b47 - 96*m.b42*m.b45*m.b46 - 32*m.b42*
                       m.b45*m.b47 - 32*m.b42*m.b46*m.b47 - 192*m.b43*m.b44*m.b45 - 192*m.b43*m.b44*m.b46 - 96*m.b43*
                       m.b44*m.b47 - 32*m.b43*m.b44*m.b48 - 192*m.b43*m.b45*m.b46 - 32*m.b43*m.b45*m.b48 - 96*m.b43*
                       m.b46*m.b47 - 32*m.b43*m.b46*m.b48 - 32*m.b43*m.b47*m.b48 - 192*m.b44*m.b45*m.b46 - 192*m.b44*
                       m.b45*m.b47 - 96*m.b44*m.b45*m.b48 - 32*m.b44*m.b45*m.b49 - 192*m.b44*m.b46*m.b47 - 32*m.b44*
                       m.b46*m.b49 - 96*m.b44*m.b47*m.b48 - 32*m.b44*m.b47*m.b49 - 32*m.b44*m.b48*m.b49 - 192*m.b45*
                       m.b46*m.b47 - 192*m.b45*m.b46*m.b48 - 96*m.b45*m.b46*m.b49 - 32*m.b45*m.b46*m.b50 - 192*m.b45*
                       m.b47*m.b48 - 32*m.b45*m.b47*m.b50 - 96*m.b45*m.b48*m.b49 - 32*m.b45*m.b48*m.b50 - 32*m.b45*m.b49
                       *m.b50 - 160*m.b46*m.b47*m.b48 - 128*m.b46*m.b47*m.b49 - 32*m.b46*m.b47*m.b50 - 128*m.b46*m.b48*
                       m.b49 - 64*m.b46*m.b49*m.b50 - 96*m.b47*m.b48*m.b49 - 64*m.b47*m.b48*m.b50 - 64*m.b47*m.b49*m.b50
                        - 32*m.b48*m.b49*m.b50 + 48*m.b1*m.b2 + 40*m.b1*m.b3 + 48*m.b1*m.b4 + 40*m.b1*m.b5 + 32*m.b1*
                       m.b6 + 96*m.b2*m.b3 + 96*m.b2*m.b4 + 112*m.b2*m.b5 + 80*m.b2*m.b6 + 32*m.b2*m.b7 + 160*m.b3*m.b4
                        + 152*m.b3*m.b5 + 160*m.b3*m.b6 + 80*m.b3*m.b7 + 32*m.b3*m.b8 + 208*m.b4*m.b5 + 192*m.b4*m.b6 + 
                       160*m.b4*m.b7 + 80*m.b4*m.b8 + 32*m.b4*m.b9 + 256*m.b5*m.b6 + 192*m.b5*m.b7 + 160*m.b5*m.b8 + 80*
                       m.b5*m.b9 + 32*m.b5*m.b10 + 256*m.b6*m.b7 + 192*m.b6*m.b8 + 160*m.b6*m.b9 + 80*m.b6*m.b10 + 32*
                       m.b6*m.b11 + 256*m.b7*m.b8 + 192*m.b7*m.b9 + 160*m.b7*m.b10 + 80*m.b7*m.b11 + 32*m.b7*m.b12 + 256
                       *m.b8*m.b9 + 192*m.b8*m.b10 + 160*m.b8*m.b11 + 80*m.b8*m.b12 + 32*m.b8*m.b13 + 256*m.b9*m.b10 + 
                       192*m.b9*m.b11 + 160*m.b9*m.b12 + 80*m.b9*m.b13 + 32*m.b9*m.b14 + 256*m.b10*m.b11 + 192*m.b10*
                       m.b12 + 160*m.b10*m.b13 + 80*m.b10*m.b14 + 32*m.b10*m.b15 + 256*m.b11*m.b12 + 192*m.b11*m.b13 + 
                       160*m.b11*m.b14 + 80*m.b11*m.b15 + 32*m.b11*m.b16 + 256*m.b12*m.b13 + 192*m.b12*m.b14 + 160*m.b12
                       *m.b15 + 80*m.b12*m.b16 + 32*m.b12*m.b17 + 256*m.b13*m.b14 + 192*m.b13*m.b15 + 160*m.b13*m.b16 + 
                       80*m.b13*m.b17 + 32*m.b13*m.b18 + 256*m.b14*m.b15 + 192*m.b14*m.b16 + 160*m.b14*m.b17 + 80*m.b14*
                       m.b18 + 32*m.b14*m.b19 + 256*m.b15*m.b16 + 192*m.b15*m.b17 + 160*m.b15*m.b18 + 80*m.b15*m.b19 + 
                       32*m.b15*m.b20 + 256*m.b16*m.b17 + 192*m.b16*m.b18 + 160*m.b16*m.b19 + 80*m.b16*m.b20 + 32*m.b16*
                       m.b21 + 256*m.b17*m.b18 + 192*m.b17*m.b19 + 160*m.b17*m.b20 + 80*m.b17*m.b21 + 32*m.b17*m.b22 + 
                       256*m.b18*m.b19 + 192*m.b18*m.b20 + 160*m.b18*m.b21 + 80*m.b18*m.b22 + 32*m.b18*m.b23 + 256*m.b19
                       *m.b20 + 192*m.b19*m.b21 + 160*m.b19*m.b22 + 80*m.b19*m.b23 + 32*m.b19*m.b24 + 256*m.b20*m.b21 + 
                       192*m.b20*m.b22 + 160*m.b20*m.b23 + 80*m.b20*m.b24 + 32*m.b20*m.b25 + 256*m.b21*m.b22 + 192*m.b21
                       *m.b23 + 160*m.b21*m.b24 + 80*m.b21*m.b25 + 32*m.b21*m.b26 + 256*m.b22*m.b23 + 192*m.b22*m.b24 + 
                       160*m.b22*m.b25 + 80*m.b22*m.b26 + 32*m.b22*m.b27 + 256*m.b23*m.b24 + 192*m.b23*m.b25 + 160*m.b23
                       *m.b26 + 80*m.b23*m.b27 + 32*m.b23*m.b28 + 256*m.b24*m.b25 + 192*m.b24*m.b26 + 160*m.b24*m.b27 + 
                       80*m.b24*m.b28 + 32*m.b24*m.b29 + 256*m.b25*m.b26 + 192*m.b25*m.b27 + 160*m.b25*m.b28 + 80*m.b25*
                       m.b29 + 32*m.b25*m.b30 + 256*m.b26*m.b27 + 192*m.b26*m.b28 + 160*m.b26*m.b29 + 80*m.b26*m.b30 + 
                       32*m.b26*m.b31 + 256*m.b27*m.b28 + 192*m.b27*m.b29 + 160*m.b27*m.b30 + 80*m.b27*m.b31 + 32*m.b27*
                       m.b32 + 256*m.b28*m.b29 + 192*m.b28*m.b30 + 160*m.b28*m.b31 + 80*m.b28*m.b32 + 32*m.b28*m.b33 + 
                       256*m.b29*m.b30 + 192*m.b29*m.b31 + 160*m.b29*m.b32 + 80*m.b29*m.b33 + 32*m.b29*m.b34 + 256*m.b30
                       *m.b31 + 192*m.b30*m.b32 + 160*m.b30*m.b33 + 80*m.b30*m.b34 + 32*m.b30*m.b35 + 256*m.b31*m.b32 + 
                       192*m.b31*m.b33 + 160*m.b31*m.b34 + 80*m.b31*m.b35 + 32*m.b31*m.b36 + 256*m.b32*m.b33 + 192*m.b32
                       *m.b34 + 160*m.b32*m.b35 + 80*m.b32*m.b36 + 32*m.b32*m.b37 + 256*m.b33*m.b34 + 192*m.b33*m.b35 + 
                       160*m.b33*m.b36 + 80*m.b33*m.b37 + 32*m.b33*m.b38 + 256*m.b34*m.b35 + 192*m.b34*m.b36 + 160*m.b34
                       *m.b37 + 80*m.b34*m.b38 + 32*m.b34*m.b39 + 256*m.b35*m.b36 + 192*m.b35*m.b37 + 160*m.b35*m.b38 + 
                       80*m.b35*m.b39 + 32*m.b35*m.b40 + 256*m.b36*m.b37 + 192*m.b36*m.b38 + 160*m.b36*m.b39 + 80*m.b36*
                       m.b40 + 32*m.b36*m.b41 + 256*m.b37*m.b38 + 192*m.b37*m.b39 + 160*m.b37*m.b40 + 80*m.b37*m.b41 + 
                       32*m.b37*m.b42 + 256*m.b38*m.b39 + 192*m.b38*m.b40 + 160*m.b38*m.b41 + 80*m.b38*m.b42 + 32*m.b38*
                       m.b43 + 256*m.b39*m.b40 + 192*m.b39*m.b41 + 160*m.b39*m.b42 + 80*m.b39*m.b43 + 32*m.b39*m.b44 + 
                       256*m.b40*m.b41 + 192*m.b40*m.b42 + 160*m.b40*m.b43 + 80*m.b40*m.b44 + 32*m.b40*m.b45 + 256*m.b41
                       *m.b42 + 192*m.b41*m.b43 + 160*m.b41*m.b44 + 80*m.b41*m.b45 + 32*m.b41*m.b46 + 256*m.b42*m.b43 + 
                       192*m.b42*m.b44 + 160*m.b42*m.b45 + 80*m.b42*m.b46 + 32*m.b42*m.b47 + 256*m.b43*m.b44 + 192*m.b43
                       *m.b45 + 160*m.b43*m.b46 + 80*m.b43*m.b47 + 32*m.b43*m.b48 + 256*m.b44*m.b45 + 192*m.b44*m.b46 + 
                       160*m.b44*m.b47 + 80*m.b44*m.b48 + 32*m.b44*m.b49 + 256*m.b45*m.b46 + 192*m.b45*m.b47 + 160*m.b45
                       *m.b48 + 80*m.b45*m.b49 + 32*m.b45*m.b50 + 208*m.b46*m.b47 + 152*m.b46*m.b48 + 112*m.b46*m.b49 + 
                       40*m.b46*m.b50 + 160*m.b47*m.b48 + 96*m.b47*m.b49 + 48*m.b47*m.b50 + 96*m.b48*m.b49 + 40*m.b48*
                       m.b50 + 48*m.b49*m.b50 - 40*m.b1 - 88*m.b2 - 136*m.b3 - 184*m.b4 - 232*m.b5 - 272*m.b6 - 272*m.b7
                        - 272*m.b8 - 272*m.b9 - 272*m.b10 - 272*m.b11 - 272*m.b12 - 272*m.b13 - 272*m.b14 - 272*m.b15 - 
                       272*m.b16 - 272*m.b17 - 272*m.b18 - 272*m.b19 - 272*m.b20 - 272*m.b21 - 272*m.b22 - 272*m.b23 - 
                       272*m.b24 - 272*m.b25 - 272*m.b26 - 272*m.b27 - 272*m.b28 - 272*m.b29 - 272*m.b30 - 272*m.b31 - 
                       272*m.b32 - 272*m.b33 - 272*m.b34 - 272*m.b35 - 272*m.b36 - 272*m.b37 - 272*m.b38 - 272*m.b39 - 
                       272*m.b40 - 272*m.b41 - 272*m.b42 - 272*m.b43 - 272*m.b44 - 272*m.b45 - 232*m.b46 - 184*m.b47 - 
                       136*m.b48 - 88*m.b49 - 40*m.b50 - m.x51 <= 0)
