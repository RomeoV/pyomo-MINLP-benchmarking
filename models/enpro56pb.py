#  MINLP written by GAMS Convert at 05/15/20 00:50:46
#  
#  Equation counts
#      Total        E        G        L        N        X        C        B
#        192       25      136       31        0        0        0        0
#  
#  Variable counts
#                   x        b        i      s1s      s2s       sc       si
#      Total     cont   binary  integer     sos1     sos2    scont     sint
#        128       55       73        0        0        0        0        0
#  FX      0        0        0        0        0        0        0        0
#  
#  Nonzero counts
#      Total    const       NL      DLL
#        651      627       24        0
# 
#  Reformulation has removed 1 variable and 1 equation


from pyomo.environ import *

model = m = ConcreteModel()


m.x1 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x2 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x3 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x4 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x5 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x6 = Var(within=Reals,bounds=(5.7037824746562,8.1605182474775),initialize=5.7037824746562)
m.x7 = Var(within=Reals,bounds=(4.45966260231685,6.09365548800453),initialize=5.27665904516069)
m.x8 = Var(within=Reals,bounds=(4.45966260231685,6.09365548800453),initialize=5.27665904516069)
m.x9 = Var(within=Reals,bounds=(4.45966260231685,6.09365548800453),initialize=5.27665904516069)
m.x10 = Var(within=Reals,bounds=(4.45966260231685,6.09365548800453),initialize=5.27665904516069)
m.x11 = Var(within=Reals,bounds=(4.45966260231685,6.09365548800453),initialize=5.27665904516069)
m.x12 = Var(within=Reals,bounds=(4.45966260231685,6.09365548800453),initialize=5.27665904516069)
m.x13 = Var(within=Reals,bounds=(3.74950407593037,6.93674281585539),initialize=5.34312344589288)
m.x14 = Var(within=Reals,bounds=(3.74950407593037,6.93674281585539),initialize=5.34312344589288)
m.x15 = Var(within=Reals,bounds=(3.74950407593037,6.93674281585539),initialize=5.34312344589288)
m.x16 = Var(within=Reals,bounds=(3.74950407593037,6.93674281585539),initialize=5.34312344589288)
m.x17 = Var(within=Reals,bounds=(3.74950407593037,6.93674281585539),initialize=5.34312344589288)
m.x18 = Var(within=Reals,bounds=(3.74950407593037,6.93674281585539),initialize=5.34312344589288)
m.x19 = Var(within=Reals,bounds=(4.49144142065975,6.87958440201544),initialize=5.68551291133759)
m.x20 = Var(within=Reals,bounds=(4.49144142065975,6.87958440201544),initialize=5.68551291133759)
m.x21 = Var(within=Reals,bounds=(4.49144142065975,6.87958440201544),initialize=5.68551291133759)
m.x22 = Var(within=Reals,bounds=(4.49144142065975,6.87958440201544),initialize=5.68551291133759)
m.x23 = Var(within=Reals,bounds=(4.49144142065975,6.87958440201544),initialize=5.68551291133759)
m.x24 = Var(within=Reals,bounds=(4.49144142065975,6.87958440201544),initialize=5.68551291133759)
m.x25 = Var(within=Reals,bounds=(3.14988295338125,6.61295573876149),initialize=4.88141934607137)
m.x26 = Var(within=Reals,bounds=(3.14988295338125,6.61295573876149),initialize=4.88141934607137)
m.x27 = Var(within=Reals,bounds=(3.14988295338125,6.61295573876149),initialize=4.88141934607137)
m.x28 = Var(within=Reals,bounds=(3.14988295338125,6.61295573876149),initialize=4.88141934607137)
m.x29 = Var(within=Reals,bounds=(3.14988295338125,6.61295573876149),initialize=4.88141934607137)
m.x30 = Var(within=Reals,bounds=(3.14988295338125,6.61295573876149),initialize=4.88141934607137)
m.x31 = Var(within=Reals,bounds=(3.04452243772342,6.65644085070123),initialize=4.85048164421233)
m.x32 = Var(within=Reals,bounds=(3.04452243772342,6.65644085070123),initialize=4.85048164421233)
m.x33 = Var(within=Reals,bounds=(3.04452243772342,6.65644085070123),initialize=4.85048164421233)
m.x34 = Var(within=Reals,bounds=(3.04452243772342,6.65644085070123),initialize=4.85048164421233)
m.x35 = Var(within=Reals,bounds=(3.04452243772342,6.65644085070123),initialize=4.85048164421233)
m.x36 = Var(within=Reals,bounds=(3.04452243772342,6.65644085070123),initialize=4.85048164421233)
m.x37 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x38 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x39 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x40 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x41 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x42 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0)
m.x43 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x44 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x45 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x46 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x47 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x48 = Var(within=Reals,bounds=(0,1.38629436111989),initialize=0.693147180559945)
m.x50 = Var(within=Reals,bounds=(4.60517018598809,9.61580548008435),initialize=7.11048783303622)
m.x51 = Var(within=Reals,bounds=(None,100),initialize=0)
m.x52 = Var(within=Reals,bounds=(None,100),initialize=0)
m.x53 = Var(within=Reals,bounds=(None,100),initialize=0)
m.x54 = Var(within=Reals,bounds=(None,100),initialize=0)
m.x55 = Var(within=Reals,bounds=(None,100),initialize=0)
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
m.b73 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b74 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b75 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b76 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b77 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b78 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b79 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b80 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b81 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b82 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b83 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b84 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b85 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b86 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b87 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b88 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b89 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b90 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b91 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b92 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b93 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b94 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b95 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b96 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b97 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b98 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b99 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b100 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b101 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b102 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b103 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b104 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b105 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b106 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b107 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b108 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b109 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b110 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b111 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b112 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b113 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b114 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b115 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b116 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b117 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b118 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b119 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b120 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b121 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b122 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b123 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b124 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b125 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b126 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b127 = Var(within=Binary,bounds=(0,1),initialize=0)
m.b128 = Var(within=Binary,bounds=(0,1),initialize=0)

m.obj = Objective(expr=250*(exp(0.6*m.x1 + m.x37 + m.x43) + exp(0.6*m.x2 + m.x38 + m.x44) + exp(0.6*m.x3 + m.x39 + m.x45
                       ) + exp(0.6*m.x4 + m.x40 + m.x46) + exp(0.6*m.x5 + m.x41 + m.x47) + exp(0.6*m.x6 + m.x42 + m.x48)
                       ) + 150*exp(0.5*m.x50), sense=minimize)

m.c1 = Constraint(expr=   m.x1 - m.x7 + m.x37 >= 2.06686275947298)

m.c2 = Constraint(expr=   m.x2 - m.x8 + m.x38 >= 0.693147180559945)

m.c3 = Constraint(expr=   m.x3 - m.x9 + m.x39 >= 1.64865862558738)

m.c4 = Constraint(expr=   m.x4 - m.x10 + m.x40 >= 1.58923520511658)

m.c5 = Constraint(expr=   m.x5 - m.x11 + m.x41 >= 1.80828877117927)

m.c6 = Constraint(expr=   m.x6 - m.x12 + m.x42 >= 1.43508452528932)

m.c7 = Constraint(expr=   m.x1 - m.x13 + m.x37 >= -0.356674943938732)

m.c8 = Constraint(expr=   m.x2 - m.x14 + m.x38 >= -0.22314355131421)

m.c9 = Constraint(expr=   m.x3 - m.x15 + m.x39 >= -0.105360515657826)

m.c10 = Constraint(expr=   m.x4 - m.x16 + m.x40 >= 1.22377543162212)

m.c11 = Constraint(expr=   m.x5 - m.x17 + m.x41 >= 0.741937344729377)

m.c12 = Constraint(expr=   m.x6 - m.x18 + m.x42 >= 0.916290731874155)

m.c13 = Constraint(expr=   m.x1 - m.x19 + m.x37 >= -0.356674943938732)

m.c14 = Constraint(expr=   m.x2 - m.x20 + m.x38 >= 0.955511445027436)

m.c15 = Constraint(expr=   m.x3 - m.x21 + m.x39 >= 0.470003629245736)

m.c16 = Constraint(expr=   m.x4 - m.x22 + m.x40 >= 1.28093384546206)

m.c17 = Constraint(expr=   m.x5 - m.x23 + m.x41 >= 1.16315080980568)

m.c18 = Constraint(expr=   m.x6 - m.x24 + m.x42 >= 1.06471073699243)

m.c19 = Constraint(expr=   m.x1 - m.x25 + m.x37 >= 1.54756250871601)

m.c20 = Constraint(expr=   m.x2 - m.x26 + m.x38 >= 0.832909122935104)

m.c21 = Constraint(expr=   m.x3 - m.x27 + m.x39 >= 0.470003629245736)

m.c22 = Constraint(expr=   m.x4 - m.x28 + m.x40 >= 0.993251773010283)

m.c23 = Constraint(expr=   m.x5 - m.x29 + m.x41 >= 0.182321556793955)

m.c24 = Constraint(expr=   m.x6 - m.x30 + m.x42 >= 0.916290731874155)

m.c25 = Constraint(expr=   m.x1 - m.x31 + m.x37 >= 0.182321556793955)

m.c26 = Constraint(expr=   m.x2 - m.x32 + m.x38 >= 1.28093384546206)

m.c27 = Constraint(expr=   m.x3 - m.x33 + m.x39 >= 0.8754687373539)

m.c28 = Constraint(expr=   m.x4 - m.x34 + m.x40 >= 1.50407739677627)

m.c29 = Constraint(expr=   m.x5 - m.x35 + m.x41 >= 0.470003629245736)

m.c30 = Constraint(expr=   m.x6 - m.x36 + m.x42 >= 0.741937344729377)

m.c31 = Constraint(expr=   m.x7 + m.x43 + m.x51 >= 1.85629799036563)

m.c32 = Constraint(expr=   m.x8 + m.x44 + m.x51 >= 1.54756250871601)

m.c33 = Constraint(expr=   m.x9 + m.x45 + m.x51 >= 2.11625551480255)

m.c34 = Constraint(expr=   m.x10 + m.x46 + m.x51 >= 1.3609765531356)

m.c35 = Constraint(expr=   m.x11 + m.x47 + m.x51 >= 0.741937344729377)

m.c36 = Constraint(expr=   m.x12 + m.x48 + m.x51 >= 0.182321556793955)

m.c37 = Constraint(expr=   m.x13 + m.x43 + m.x52 >= 1.91692261218206)

m.c38 = Constraint(expr=   m.x14 + m.x44 + m.x52 >= 1.85629799036563)

m.c39 = Constraint(expr=   m.x15 + m.x45 + m.x52 >= 1.87180217690159)

m.c40 = Constraint(expr=   m.x16 + m.x46 + m.x52 >= 1.48160454092422)

m.c41 = Constraint(expr=   m.x17 + m.x47 + m.x52 >= 0.832909122935104)

m.c42 = Constraint(expr=   m.x18 + m.x48 + m.x52 >= 1.16315080980568)

m.c43 = Constraint(expr=   m.x19 + m.x43 + m.x53 >= 0)

m.c44 = Constraint(expr=   m.x20 + m.x44 + m.x53 >= 1.84054963339749)

m.c45 = Constraint(expr=   m.x21 + m.x45 + m.x53 >= 1.68639895357023)

m.c46 = Constraint(expr=   m.x22 + m.x46 + m.x53 >= 2.47653840011748)

m.c47 = Constraint(expr=   m.x23 + m.x47 + m.x53 >= 1.7404661748405)

m.c48 = Constraint(expr=   m.x24 + m.x48 + m.x53 >= 1.82454929205105)

m.c49 = Constraint(expr=   m.x25 + m.x43 + m.x54 >= 1.16315080980568)

m.c50 = Constraint(expr=   m.x26 + m.x44 + m.x54 >= 1.09861228866811)

m.c51 = Constraint(expr=   m.x27 + m.x45 + m.x54 >= 1.25276296849537)

m.c52 = Constraint(expr=   m.x28 + m.x46 + m.x54 >= 1.19392246847243)

m.c53 = Constraint(expr=   m.x29 + m.x47 + m.x54 >= 1.02961941718116)

m.c54 = Constraint(expr=   m.x30 + m.x48 + m.x54 >= 1.22377543162212)

m.c55 = Constraint(expr=   m.x31 + m.x43 + m.x55 >= 0.741937344729377)

m.c56 = Constraint(expr=   m.x32 + m.x44 + m.x55 >= 0.916290731874155)

m.c57 = Constraint(expr=   m.x33 + m.x45 + m.x55 >= 1.43508452528932)

m.c58 = Constraint(expr=   m.x34 + m.x46 + m.x55 >= 1.28093384546206)

m.c59 = Constraint(expr=   m.x35 + m.x47 + m.x55 >= 1.30833281965018)

m.c60 = Constraint(expr=   m.x36 + m.x48 + m.x55 >= 0.78845736036427)

m.c61 = Constraint(expr=250000*exp(m.x51) + 150000*exp(m.x52) + 180000*exp(m.x53) + 160000*exp(m.x54) + 120000*exp(m.x55
                        ) <= 6000)

m.c62 = Constraint(expr= - m.x8 + m.x50 - 10*m.b104 >= -7.69741490700595)

m.c63 = Constraint(expr= - m.x9 + m.x50 - 10*m.b105 >= -7.69741490700595)

m.c64 = Constraint(expr= - m.x10 + m.x50 - 10*m.b106 >= -7.69741490700595)

m.c65 = Constraint(expr= - m.x11 + m.x50 - 10*m.b107 >= -7.69741490700595)

m.c66 = Constraint(expr= - m.x12 + m.x50 - 10*m.b108 >= -7.69741490700595)

m.c67 = Constraint(expr= - m.x14 + m.x50 - 10*m.b109 >= -7.69741490700595)

m.c68 = Constraint(expr= - m.x15 + m.x50 - 10*m.b110 >= -7.69741490700595)

m.c69 = Constraint(expr= - m.x16 + m.x50 - 10*m.b111 >= -7.69741490700595)

m.c70 = Constraint(expr= - m.x17 + m.x50 - 10*m.b112 >= -7.69741490700595)

m.c71 = Constraint(expr= - m.x18 + m.x50 - 10*m.b113 >= -7.69741490700595)

m.c72 = Constraint(expr= - m.x20 + m.x50 - 10*m.b114 >= -7.69741490700595)

m.c73 = Constraint(expr= - m.x21 + m.x50 - 10*m.b115 >= -7.69741490700595)

m.c74 = Constraint(expr= - m.x22 + m.x50 - 10*m.b116 >= -7.69741490700595)

m.c75 = Constraint(expr= - m.x23 + m.x50 - 10*m.b117 >= -7.69741490700595)

m.c76 = Constraint(expr= - m.x24 + m.x50 - 10*m.b118 >= -7.69741490700595)

m.c77 = Constraint(expr= - m.x26 + m.x50 - 10*m.b119 >= -7.69741490700595)

m.c78 = Constraint(expr= - m.x27 + m.x50 - 10*m.b120 >= -7.69741490700595)

m.c79 = Constraint(expr= - m.x28 + m.x50 - 10*m.b121 >= -7.69741490700595)

m.c80 = Constraint(expr= - m.x29 + m.x50 - 10*m.b122 >= -7.69741490700595)

m.c81 = Constraint(expr= - m.x30 + m.x50 - 10*m.b123 >= -7.69741490700595)

m.c82 = Constraint(expr= - m.x32 + m.x50 - 10*m.b124 >= -7.69741490700595)

m.c83 = Constraint(expr= - m.x33 + m.x50 - 10*m.b125 >= -7.69741490700595)

m.c84 = Constraint(expr= - m.x34 + m.x50 - 10*m.b126 >= -7.69741490700595)

m.c85 = Constraint(expr= - m.x35 + m.x50 - 10*m.b127 >= -7.69741490700595)

m.c86 = Constraint(expr= - m.x36 + m.x50 - 10*m.b128 >= -7.69741490700595)

m.c87 = Constraint(expr= - m.x7 + m.x50 - 10*m.b104 >= -7.69741490700595)

m.c88 = Constraint(expr= - m.x8 + m.x50 - 10*m.b105 >= -7.69741490700595)

m.c89 = Constraint(expr= - m.x9 + m.x50 - 10*m.b106 >= -7.69741490700595)

m.c90 = Constraint(expr= - m.x10 + m.x50 - 10*m.b107 >= -7.69741490700595)

m.c91 = Constraint(expr= - m.x11 + m.x50 - 10*m.b108 >= -7.69741490700595)

m.c92 = Constraint(expr= - m.x13 + m.x50 - 10*m.b109 >= -7.69741490700595)

m.c93 = Constraint(expr= - m.x14 + m.x50 - 10*m.b110 >= -7.69741490700595)

m.c94 = Constraint(expr= - m.x15 + m.x50 - 10*m.b111 >= -7.69741490700595)

m.c95 = Constraint(expr= - m.x16 + m.x50 - 10*m.b112 >= -7.69741490700595)

m.c96 = Constraint(expr= - m.x17 + m.x50 - 10*m.b113 >= -7.69741490700595)

m.c97 = Constraint(expr= - m.x19 + m.x50 - 10*m.b114 >= -7.69741490700595)

m.c98 = Constraint(expr= - m.x20 + m.x50 - 10*m.b115 >= -7.69741490700595)

m.c99 = Constraint(expr= - m.x21 + m.x50 - 10*m.b116 >= -7.69741490700595)

m.c100 = Constraint(expr= - m.x22 + m.x50 - 10*m.b117 >= -7.69741490700595)

m.c101 = Constraint(expr= - m.x23 + m.x50 - 10*m.b118 >= -7.69741490700595)

m.c102 = Constraint(expr= - m.x25 + m.x50 - 10*m.b119 >= -7.69741490700595)

m.c103 = Constraint(expr= - m.x26 + m.x50 - 10*m.b120 >= -7.69741490700595)

m.c104 = Constraint(expr= - m.x27 + m.x50 - 10*m.b121 >= -7.69741490700595)

m.c105 = Constraint(expr= - m.x28 + m.x50 - 10*m.b122 >= -7.69741490700595)

m.c106 = Constraint(expr= - m.x29 + m.x50 - 10*m.b123 >= -7.69741490700595)

m.c107 = Constraint(expr= - m.x31 + m.x50 - 10*m.b124 >= -7.69741490700595)

m.c108 = Constraint(expr= - m.x32 + m.x50 - 10*m.b125 >= -7.69741490700595)

m.c109 = Constraint(expr= - m.x33 + m.x50 - 10*m.b126 >= -7.69741490700595)

m.c110 = Constraint(expr= - m.x34 + m.x50 - 10*m.b127 >= -7.69741490700595)

m.c111 = Constraint(expr= - m.x35 + m.x50 - 10*m.b128 >= -7.69741490700595)

m.c112 = Constraint(expr=   m.x37 - 0.693147180559945*m.b62 - 1.09861228866811*m.b68 - 1.38629436111989*m.b74 == 0)

m.c113 = Constraint(expr=   m.x38 - 0.693147180559945*m.b63 - 1.09861228866811*m.b69 - 1.38629436111989*m.b75 == 0)

m.c114 = Constraint(expr=   m.x39 - 0.693147180559945*m.b64 - 1.09861228866811*m.b70 - 1.38629436111989*m.b76 == 0)

m.c115 = Constraint(expr=   m.x40 - 0.693147180559945*m.b65 - 1.09861228866811*m.b71 - 1.38629436111989*m.b77 == 0)

m.c116 = Constraint(expr=   m.x41 - 0.693147180559945*m.b66 - 1.09861228866811*m.b72 - 1.38629436111989*m.b78 == 0)

m.c117 = Constraint(expr=   m.x42 - 0.693147180559945*m.b67 - 1.09861228866811*m.b73 - 1.38629436111989*m.b79 == 0)

m.c118 = Constraint(expr=   m.x43 - 0.693147180559945*m.b86 - 1.09861228866811*m.b92 - 1.38629436111989*m.b98 == 0)

m.c119 = Constraint(expr=   m.x44 - 0.693147180559945*m.b87 - 1.09861228866811*m.b93 - 1.38629436111989*m.b99 == 0)

m.c120 = Constraint(expr=   m.x45 - 0.693147180559945*m.b88 - 1.09861228866811*m.b94 - 1.38629436111989*m.b100 == 0)

m.c121 = Constraint(expr=   m.x46 - 0.693147180559945*m.b89 - 1.09861228866811*m.b95 - 1.38629436111989*m.b101 == 0)

m.c122 = Constraint(expr=   m.x47 - 0.693147180559945*m.b90 - 1.09861228866811*m.b96 - 1.38629436111989*m.b102 == 0)

m.c123 = Constraint(expr=   m.x48 - 0.693147180559945*m.b91 - 1.09861228866811*m.b97 - 1.38629436111989*m.b103 == 0)

m.c124 = Constraint(expr=   m.b56 + m.b62 + m.b68 + m.b74 == 1)

m.c125 = Constraint(expr=   m.b57 + m.b63 + m.b69 + m.b75 == 1)

m.c126 = Constraint(expr=   m.b58 + m.b64 + m.b70 + m.b76 == 1)

m.c127 = Constraint(expr=   m.b59 + m.b65 + m.b71 + m.b77 == 1)

m.c128 = Constraint(expr=   m.b60 + m.b66 + m.b72 + m.b78 == 1)

m.c129 = Constraint(expr=   m.b61 + m.b67 + m.b73 + m.b79 == 1)

m.c130 = Constraint(expr=   m.b80 + m.b86 + m.b92 + m.b98 == 1)

m.c131 = Constraint(expr=   m.b81 + m.b87 + m.b93 + m.b99 == 1)

m.c132 = Constraint(expr=   m.b82 + m.b88 + m.b94 + m.b100 == 1)

m.c133 = Constraint(expr=   m.b83 + m.b89 + m.b95 + m.b101 == 1)

m.c134 = Constraint(expr=   m.b84 + m.b90 + m.b96 + m.b102 == 1)

m.c135 = Constraint(expr=   m.b85 + m.b91 + m.b97 + m.b103 == 1)

m.c136 = Constraint(expr=   m.b104 + m.b105 + m.b106 + m.b107 + m.b108 <= 1)

m.c137 = Constraint(expr=   m.b109 + m.b110 + m.b111 + m.b112 + m.b113 <= 1)

m.c138 = Constraint(expr=   m.b114 + m.b115 + m.b116 + m.b117 + m.b118 <= 1)

m.c139 = Constraint(expr=   m.b119 + m.b120 + m.b121 + m.b122 + m.b123 <= 1)

m.c140 = Constraint(expr=   m.b124 + m.b125 + m.b126 + m.b127 + m.b128 <= 1)

m.c141 = Constraint(expr=   m.b104 + m.b105 + m.b106 + m.b107 + m.b108 + m.b109 + m.b110 + m.b111 + m.b112 + m.b113
                          + m.b114 + m.b115 + m.b116 + m.b117 + m.b118 + m.b119 + m.b120 + m.b121 + m.b122 + m.b123
                          + m.b124 + m.b125 + m.b126 + m.b127 + m.b128 >= 1)

m.c142 = Constraint(expr=   m.x7 - m.x8 - 0.693147180559945*m.b104 <= 0)

m.c143 = Constraint(expr=   m.x8 - m.x9 - 0.693147180559945*m.b105 <= 0)

m.c144 = Constraint(expr=   m.x9 - m.x10 - 0.693147180559945*m.b106 <= 0)

m.c145 = Constraint(expr=   m.x10 - m.x11 - 0.693147180559945*m.b107 <= 0)

m.c146 = Constraint(expr=   m.x11 - m.x12 - 0.693147180559945*m.b108 <= 0)

m.c147 = Constraint(expr=   m.x13 - m.x14 - 0.693147180559945*m.b109 <= 0)

m.c148 = Constraint(expr=   m.x14 - m.x15 - 0.693147180559945*m.b110 <= 0)

m.c149 = Constraint(expr=   m.x15 - m.x16 - 0.693147180559945*m.b111 <= 0)

m.c150 = Constraint(expr=   m.x16 - m.x17 - 0.693147180559945*m.b112 <= 0)

m.c151 = Constraint(expr=   m.x17 - m.x18 - 0.693147180559945*m.b113 <= 0)

m.c152 = Constraint(expr=   m.x19 - m.x20 - 0.693147180559945*m.b114 <= 0)

m.c153 = Constraint(expr=   m.x20 - m.x21 - 0.693147180559945*m.b115 <= 0)

m.c154 = Constraint(expr=   m.x21 - m.x22 - 0.693147180559945*m.b116 <= 0)

m.c155 = Constraint(expr=   m.x22 - m.x23 - 0.693147180559945*m.b117 <= 0)

m.c156 = Constraint(expr=   m.x23 - m.x24 - 0.693147180559945*m.b118 <= 0)

m.c157 = Constraint(expr=   m.x25 - m.x26 - 0.693147180559945*m.b119 <= 0)

m.c158 = Constraint(expr=   m.x26 - m.x27 - 0.693147180559945*m.b120 <= 0)

m.c159 = Constraint(expr=   m.x27 - m.x28 - 0.693147180559945*m.b121 <= 0)

m.c160 = Constraint(expr=   m.x28 - m.x29 - 0.693147180559945*m.b122 <= 0)

m.c161 = Constraint(expr=   m.x29 - m.x30 - 0.693147180559945*m.b123 <= 0)

m.c162 = Constraint(expr=   m.x31 - m.x32 - 0.693147180559945*m.b124 <= 0)

m.c163 = Constraint(expr=   m.x32 - m.x33 - 0.693147180559945*m.b125 <= 0)

m.c164 = Constraint(expr=   m.x33 - m.x34 - 0.693147180559945*m.b126 <= 0)

m.c165 = Constraint(expr=   m.x34 - m.x35 - 0.693147180559945*m.b127 <= 0)

m.c166 = Constraint(expr=   m.x35 - m.x36 - 0.693147180559945*m.b128 <= 0)

m.c167 = Constraint(expr=   m.x7 - m.x8 + 0.693147180559945*m.b104 >= 0)

m.c168 = Constraint(expr=   m.x8 - m.x9 + 0.693147180559945*m.b105 >= 0)

m.c169 = Constraint(expr=   m.x9 - m.x10 + 0.693147180559945*m.b106 >= 0)

m.c170 = Constraint(expr=   m.x10 - m.x11 + 0.693147180559945*m.b107 >= 0)

m.c171 = Constraint(expr=   m.x11 - m.x12 + 0.693147180559945*m.b108 >= 0)

m.c172 = Constraint(expr=   m.x13 - m.x14 + 0.693147180559945*m.b109 >= 0)

m.c173 = Constraint(expr=   m.x14 - m.x15 + 0.693147180559945*m.b110 >= 0)

m.c174 = Constraint(expr=   m.x15 - m.x16 + 0.693147180559945*m.b111 >= 0)

m.c175 = Constraint(expr=   m.x16 - m.x17 + 0.693147180559945*m.b112 >= 0)

m.c176 = Constraint(expr=   m.x17 - m.x18 + 0.693147180559945*m.b113 >= 0)

m.c177 = Constraint(expr=   m.x19 - m.x20 + 0.693147180559945*m.b114 >= 0)

m.c178 = Constraint(expr=   m.x20 - m.x21 + 0.693147180559945*m.b115 >= 0)

m.c179 = Constraint(expr=   m.x21 - m.x22 + 0.693147180559945*m.b116 >= 0)

m.c180 = Constraint(expr=   m.x22 - m.x23 + 0.693147180559945*m.b117 >= 0)

m.c181 = Constraint(expr=   m.x23 - m.x24 + 0.693147180559945*m.b118 >= 0)

m.c182 = Constraint(expr=   m.x25 - m.x26 + 0.693147180559945*m.b119 >= 0)

m.c183 = Constraint(expr=   m.x26 - m.x27 + 0.693147180559945*m.b120 >= 0)

m.c184 = Constraint(expr=   m.x27 - m.x28 + 0.693147180559945*m.b121 >= 0)

m.c185 = Constraint(expr=   m.x28 - m.x29 + 0.693147180559945*m.b122 >= 0)

m.c186 = Constraint(expr=   m.x29 - m.x30 + 0.693147180559945*m.b123 >= 0)

m.c187 = Constraint(expr=   m.x31 - m.x32 + 0.693147180559945*m.b124 >= 0)

m.c188 = Constraint(expr=   m.x32 - m.x33 + 0.693147180559945*m.b125 >= 0)

m.c189 = Constraint(expr=   m.x33 - m.x34 + 0.693147180559945*m.b126 >= 0)

m.c190 = Constraint(expr=   m.x34 - m.x35 + 0.693147180559945*m.b127 >= 0)

m.c191 = Constraint(expr=   m.x35 - m.x36 + 0.693147180559945*m.b128 >= 0)
