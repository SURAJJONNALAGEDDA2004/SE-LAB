import matplotlib.pyplot as plt
import numpy as np

a_user = int(input("Enter the value of a: "))
b_user = int(input("Enter the value of b: "))
c_user = int(input("Enter the value of c: "))

x = np.linspace(-10, 10, 400)

y1_user = a_user * x**2 + b_user * x + c_user

plt.plot(x, y1_user, label=f'User Input: {a_user}x^2 + {b_user}x + {c_user}')

a_fixed = 5
b_fixed = -5
c_fixed = 3

y2_fixed = a_fixed * x**2 + b_fixed * x + c_fixed

plt.plot(x, y2_fixed, label=f'Fixed Constants: {a_fixed}x^2 + {b_fixed}x + {c_fixed}')
plt.title('Plot of the quadratic functions')
plt.xlabel('Temperature')
plt.ylabel('Time')

plt.legend()
plt.grid(True)
plt.show()