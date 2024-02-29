import ru_local as ru
import math

side_a = float(input())
side_b = float(input())
side_c = float(input())
if side_a+side_b < side_c or side_b + side_c < side_a or side_a + side_c < side_b:
    print(ru.MISTAKE)
else:
    angle_a_r = math.acos((side_c**2 + side_b**2 - side_a**2) / (2*side_c*side_b))
    angle_b_r = math.acos((side_c**2 + side_a**2 - side_b**2) / (2*side_c*side_a))
    angle_c_r = math.acos((side_a**2 + side_b**2 - side_c**2) / (2*side_a*side_b))
    angle_a_d = math.degrees(angle_a_r)
    angle_b_d = math.degrees(angle_b_r)
    angle_c_d = math.degrees(angle_c_r)
    print(angle_a_d, angle_b_d, angle_c_d)
