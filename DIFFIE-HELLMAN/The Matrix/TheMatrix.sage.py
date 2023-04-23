

# This file was *autogenerated* from the file TheMatrix.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_31337 = Integer(31337); _sage_const_1 = Integer(1); _sage_const_32 = Integer(32); _sage_const_8 = Integer(8); _sage_const_50 = Integer(50); _sage_const_34 = Integer(34)
M = Matrix(GF(_sage_const_2 ), [list(map(int, row)) for row in open("flag.enc").read().splitlines()])
M **= pow(_sage_const_31337 , -_sage_const_1 , M.multiplicative_order())
bin_flag = ''.join([str(bit) for col in M.columns()[:(_sage_const_32 *_sage_const_8 //_sage_const_50 )+_sage_const_1 ] for bit in col])
print(bytes.fromhex(hex(int(bin_flag[:_sage_const_34 *_sage_const_8 ],_sage_const_2 ))[_sage_const_2 :]).decode())

