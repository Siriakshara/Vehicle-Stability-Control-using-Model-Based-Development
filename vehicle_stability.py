def vehicle_stability(speed, slip_angle):
    stability_factor = 1 - abs(slip_angle) / 30  # hypothetical factor
    adjusted_speed = speed * stability_factor
    return adjusted_speed

# Example values
speed = 60  # initial speed in km/h
slip_angle = 5  # degrees

new_speed = vehicle_stability(speed, slip_angle)
print(f"Adjusted Speed for Stability: {new_speed} km/h")