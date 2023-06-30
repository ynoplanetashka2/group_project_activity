import matplotlib.pyplot as plt
import numpy  as np
import time

from lib import is_stable

epsilon_range = np.linspace(0, 0.3, 30)
delta_range = np.linspace(0.15, 0.35, 50)
points_count = epsilon_range.size * delta_range.size

stable_values = []
i = 0
for epsilon in epsilon_range:
    for delta in delta_range:
        print(i / points_count)
        i += 1
        if is_stable(
            epsilon = epsilon,
            delta = delta,
        ):
            stable_values.append({
                'epsilon': epsilon,
                'delta': delta,
            })

stable_epsilon_values = list(map(lambda item: item['epsilon'], stable_values))
stable_delta_values = list(map(lambda item: item['delta'], stable_values))

stable_epsilon_values = np.array(stable_epsilon_values)
stable_delta_values = np.array(stable_delta_values)

print(stable_values)
fig, ax = plt.subplots()
ax.plot(
    stable_delta_values,
    stable_epsilon_values, 
    'o',
    color = 'blue',
    )

unstable_epsilon_values = []
unstable_delta_values = []
for epsilon in epsilon_range:
    for delta in delta_range:
        if not { 'epsilon': epsilon, 'delta': delta } in stable_values:
            unstable_epsilon_values.append(epsilon)
            unstable_delta_values.append(delta)

unstable_epsilon_values = np.array(unstable_epsilon_values)
unstable_delta_values = np.array(unstable_delta_values)

ax.plot(
    unstable_delta_values,
    unstable_epsilon_values,
    'o',
    color = 'red',
)
ax.set_xlabel('delta')
ax.set_ylabel('epsilon')

plt.savefig(f'./images/{time.time()}.png')
plt.show()