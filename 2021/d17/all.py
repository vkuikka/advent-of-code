#!/usr/bin/python3

f = {'x':[128,160], 'y':[-88,-142]}
# f = {'x':[20,30], 'y':[-5,-10]}

max_y = -12345
amount = 0

steps = 10000 # doesnt matter
vely_a = 200 # matters
while vely_a > -200: # matters
	velx_a = 200 # matters
	vely_a -= 1
	while velx_a > 0:
		velx_a -= 1
		velx = velx_a
		vely = vely_a
		x = 0
		y = 0
		local_max_y = 0
		for step in range(steps):
			x += velx
			y += vely
			if velx > 0:
				velx -= 1
			vely -= 1
			if y > local_max_y:
				local_max_y = y
			if x >= min(f['x']) and x <= max(f['x']) and y <= max(f['y']) and y >= min(f['y']):
				max_y = max(local_max_y, max_y)
				amount += 1
				break
			if x > max(f['x']) or y < min(f['y']) or (velx == 0 and (x < min(f['x']) or x > max(f['x']))):
				break
print(max_y)
print(amount)
