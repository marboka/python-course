
'''deep vs shallow copy'''
#x = [17, 19, 23]
#y = x
#z = x[:]
#
#print("Before the change:")
#print("  x =", x)
#print("  y =", y)
#print("  z =", z)
#
#y[1] = 13
#z[2] = 11
#
#print("After the change:")
#print("  x =", x)
#print("  y =", y)
#print("  z =", z)


# =============================================================================
# def f(a, b, c):
#     a = 19
#     b = [2, 3, 5]
#     c[0] = 11
# 
# x = 17
# y = [17, 19, 23]
# z = [29, 31, 37]
# 
# print("Initial values:")
# print("  x =", x)
# print("  y =", y)
# print("  z =", z)
# 
# f(x, y, z)
# 
# print("After a call to the function `f`:")
# print("  x =", x)
# print("  y =", y)
# print("  z =", z)# -*- coding: utf-8 -*-
# =============================================================================
'''lenght'''
# =============================================================================
# x = [17, 19, 23, 29, 31]
# 
# print("Before change:")
# print("  x =", x)
# print("  Length of x:", len(x))
# 
# x[1:3] = [2]
# 
# print("After change:")
# print("  x =", x)
# print("  Length of x:", len(x))
# =============================================================================

''' append can only take one element'''

'''extend can do more'''
# =============================================================================
# x = [17, 19, 23]
# print("Before extending:", x)
# x.extend([29,31])
#'''y = x + [29,31] is the same'''
# print("After extending: ", x)
# =============================================================================
'''list in list type, getting out an int from list in list'''
# =============================================================================
# x = [17, 1.7, [23, 29]]
# for i in range(len(x)):
#     print("x[" + str(i) + "] =", x[i])
#     print("  type(x[" + str(i) + "]) =", type(x[i]))
# print("x[2][0] =", x[2][0])
# print("  type(x[2][0]) =", type(x[2][0]))
# =============================================================================

