import matplotlib.pyplot as plt
import numpy  as np

from lib import is_stable

cos_coef_range = np.arange(.1, 1, .1)
omega_range = np.arange(.1, 1, .1)
points_count = cos_coef_range.size * omega_range.size

stable_values = []
i = 0
for cos_coef in cos_coef_range:
    for omega in omega_range:
        print(i / points_count)
        i += 1
        if is_stable(
            cos_coef = cos_coef,
            omega = omega,
        ):
            stable_values.append({
                'cos_coef': cos_coef,
                'omega': omega,
            })

stable_cos_coef_values = list(map(lambda item: item['cos_coef'], stable_values))
stable_omega_values = list(map(lambda item: item['omega'], stable_values))

stable_cos_coef_values = np.array(stable_cos_coef_values)
stable_omega_values = np.array(stable_omega_values)

print(stable_values)
fig, ax = plt.subplots()
ax.plot(
    stable_cos_coef_values, 
    stable_omega_values,
    'o',
    color = 'blue',
    )

unstable_cos_coef_values = []
unstable_omega_values = []
for cos_coef in cos_coef_range:
    for omega in omega_range:
        if not { 'cos_coef': cos_coef, 'omega': omega } in stable_values:
            unstable_cos_coef_values.append(cos_coef)
            unstable_omega_values.append(omega)

unstable_cos_coef_values = np.array(unstable_cos_coef_values)
unstable_omega_values = np.array(unstable_omega_values)

ax.plot(
    unstable_cos_coef_values,
    unstable_omega_values,
    'o',
    color = 'red',
)

plt.show()