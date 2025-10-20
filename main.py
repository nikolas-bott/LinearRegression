point_a = (0.5,1)
point_b = (1,0.5)
point_c = (2,1.5)

all_points = [point_a, point_b, point_c]

def main():
    print(f(2,2,all_points))
    return
   
# funktion aufgelöst für den geringsten abstand für einen Punkt |==| beispiel mit zwei punkten 
# f(m,n) = n² + y² - 2*x*y*m + 2*y*n + x²*m² + 2*x*m*n |==| f(m,n) = 2n² + y2² - 2*x2*y2*m + 2*y2*n + x2²*m² + 2*x2*m*n
#
# Ableitung von f(m) = f'(m)
# f'(m) = 2mx² + 2xn - 2xy |==| f'(m) = 2*m*x1² + 2*x1*n - 2*x1*y1 + 2*m*x2² + 2*x2*n - 2*x2y2
#
# => nach 0 umstellen
# m = y/x - n/x 
# 
# ALlgemeine Formel für m: 
# m = (xᵢ₊₁ * yᵢ₊₁ + ... + xᵢ + yᵢ) - (xᵢ₊₁ + ... + xᵢ)*n / xᵢ₊₁² + ... + xᵢ 
#
# TODO: allgemeine formel für n rausfinden und in formel für n einsetzen und dann code schreiben
def f(m, n, all_points):
    value = 0
    
    for point in all_points:
        value += (point[0] - (m * point[1] + n))
        
    return value
    
if __name__ == "__main__":
    main()