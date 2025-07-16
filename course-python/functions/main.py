import math

def main():
    z	
    # w = vector_sum(u=[1,2,3], v=[2,4,6])
    # z = (3,4,0)
    
    # print(w)
    # print(z)
    
    # print(vector_module(z))
    # print(dot_product(w,z))
    
    # print(vector_cos(u=[1,0,0],v=[1,1,0]))
    
    print_matrix([-1,0,[2,3,4],[3,4,5])
    

def vector_sum(u: list[int], v: list[int]) -> list[int]:
	return [u[0] + v[0], u[1] + v[1], u[2] + v[2]]
   
   
def vector_module(u: list[int]) -> int:
	return math.ceil(math.sqrt(u[0] * u[0] + u[1] + u[1] + u[2] + u[2]))
	
    
def dot_product(u: list[int] = None, v : list[int] = None) -> int:
	return u[0] * v[0] +  u[1] * v[1] +  u[2] * v[2]

def vector_cos(u: list[int],v: list[int]) -> int:

	cos_theta = dot_product(u, v) / (vector_module(u) * vector_module(v))
	theta_rad = math.acos(cos_theta)  # Converte cosseno para ângulo em radianos
	theta_deg = math.degrees(theta_rad)  # Converte radianos para graus
	return theta_deg
	
	
def print_matrix(v1 : list[list[int]], v2 : list[list[int]], v3: list[list[int]]):

	print(v1,v2,v3,sep="\n")



    
if __name__ == "__main__":
    main()
