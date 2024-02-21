#Problem #2: Cone Volume {This is DMOJ problem dmopc14c5p1}
"""
The Challenge
Calculate the volume of a right circular cone.

Input
The input consists of two lines of text. The first line contains integer r, the
radius of the cone. The second line contains integer h, the height of the
cone. Both r and h are between 1 and 100. (That is, the minimum value for r
and h is 1, and the maximum value is 100.)

Output
Output the volume of the right circular cone with radius r and height h. The
formula to calculate the volume is (πr 2 h)/3.
"""
PI = 3.141592
radius = int(input("Enter a radius: "))
height = int(input("Enter h height: "))

volume_circular_cone = PI*(radius**2)*height/3
print(volume_circular_cone)
