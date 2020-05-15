#  MINLP written by GAMS Convert at 05/15/20 00:50:42
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#          2        1        0        1        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#         31        1        0       30        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#         61       31       30        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.i2 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i3 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i4 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i5 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i6 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i7 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i8 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i9 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i10 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i11 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i12 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i13 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i14 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i15 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i16 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i17 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i18 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i19 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i20 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i21 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i22 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i23 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i24 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i25 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i26 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i27 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i28 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i29 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i30 = Var(within=Integers,bounds=(-1,2),initialize=0)
m.i31 = Var(within=Integers,bounds=(-1,2),initialize=0)

m.obj = Objective(expr= - m.i2 - m.i3 - m.i4 - m.i5 - m.i6 - m.i7 - m.i8 - m.i9 - m.i10 - m.i11 - m.i12 - m.i13 - m.i14
                        - m.i15 - m.i16 - m.i17 - m.i18 - m.i19 - m.i20 - m.i21 - m.i22 - m.i23 - m.i24 - m.i25 - m.i26
                        - m.i27 - m.i28 - m.i29 - m.i30 - m.i31, sense=minimize)

m.c2 = Constraint(expr=0.0394468602581308*m.i30**2 - 0.0394468602581308*m.i30 + 0.016482781963216*m.i29**2 - 
                       0.016482781963216*m.i29 + 0.0565703047972114*m.i28**2 - 0.0565703047972114*m.i28 + 
                       0.0585014464120386*m.i27**2 - 0.0585014464120386*m.i27 + 0.0118746308986698*m.i26**2 - 
                       0.0118746308986698*m.i26 + 0.0451913403894453*m.i25**2 - 0.0451913403894453*m.i25 + 
                       0.0362882980369683*m.i24**2 - 0.0362882980369683*m.i24 + 0.0204948265573191*m.i23**2 - 
                       0.0204948265573191*m.i23 + 0.0252301288903778*m.i22**2 - 0.0252301288903778*m.i22 + 
                       0.0283867992035166*m.i21**2 - 0.0283867992035166*m.i21 + 0.0425137327561133*m.i20**2 - 
                       0.0425137327561133*m.i20 + 0.037617677558166*m.i19**2 - 0.037617677558166*m.i19 + 
                       0.0576726558598861*m.i18**2 - 0.0576726558598861*m.i18 + 0.0259924550955063*m.i17**2 - 
                       0.0259924550955063*m.i17 + 0.00625392202854311*m.i16**2 - 0.00625392202854311*m.i16 + 
                       0.0474635696658564*m.i15**2 - 0.0474635696658564*m.i15 + 0.030733721879364*m.i14**2 - 
                       0.030733721879364*m.i14 + 0.015401148979499*m.i13**2 - 0.015401148979499*m.i13 + 
                       0.049224183717334*m.i12**2 - 0.049224183717334*m.i12 + 0.0519656343340015*m.i11**2 - 
                       0.0519656343340015*m.i11 + 0.0384040110374736*m.i10**2 - 0.0384040110374736*m.i10 + 
                       0.0172067356549738*m.i9**2 - 0.0172067356549738*m.i9 + 0.019974781798624*m.i8**2 - 
                       0.019974781798624*m.i8 + 0.0352372440378746*m.i7**2 - 0.0352372440378746*m.i7 + 
                       0.0152163994975552*m.i6**2 - 0.0152163994975552*m.i6 + 0.0075711399569244*m.i5**2 - 
                       0.0075711399569244*m.i5 + 0.0243048911732161*m.i4**2 - 0.0243048911732161*m.i4 + 
                       0.0502208123501935*m.i3**2 - 0.0502208123501935*m.i3 + 0.041161312091797*m.i2**2 - 
                       0.041161312091797*m.i2 + 0.0473965531202045*m.i31**2 - 0.0473965531202045*m.i31
                        <= -9.99999999999612E-5)
