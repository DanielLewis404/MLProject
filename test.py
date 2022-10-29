import sys
def hello_world:
  print("hello world!")
print("hacktober")
print("2022")
a=[1,2,3,4,5]
for i in a:
  print(i)
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
  
    # mean of x and y vector
    m_x = np.mean(x)
    m_y = np.mean(y)
  
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x) - n*m_y*m_x
    SS_xx = np.sum(x*x) - n*m_x*m_x
  
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_2 = m_y - b_1*m_x
  
    return (b_2, b_1)
