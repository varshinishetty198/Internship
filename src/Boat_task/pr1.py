import random

# -------- INPUT SECTION --------
bot_name = input("Enter bot name: ")
target_distance = int(input("Enter distance to target (meters): "))
obstacle_ahead = input("Is there an obstacle ahead? (yes/no): ").lower()

# -------- INITIAL SETUP --------
distance_travelled = 0
checkpoints = ["Start"]

speed_levels = ["Slow", "Medium", "High"]
speed_values = {"Slow": 1, "Medium": 2, "High": 3}

total_speed_value = 0
move_count = 0
human_wait_count = 0
obstacle_count = 0

# -------- INITIAL SPEED DECISION --------
if obstacle_ahead == "yes":
    base_speed = "Medium" if target_distance <= 100 else "Slow"
else:
    if target_distance > 100:
        base_speed = "High"
    elif target_distance > 50:
        base_speed = "Medium"
    else:
        base_speed = "Slow"

checkpoints.append(f"Initial Speed: {base_speed}")

# -------- MOVEMENT SIMULATION --------
while distance_travelled < target_distance:

    # 60% chance obstacle detection
    if random.random() < 0.6:
        detected_type = random.choice(["human", "object"])
        obstacle_count += 1

        if detected_type == "human":
            human_wait_count += 1
            checkpoints.append("Human detected – Waiting")

            if human_wait_count >= 2:
                turn = random.choice(["Turn Left", "Turn Right"])
                checkpoints.append(f"Too much waiting – {turn}")
                human_wait_count = 0
            continue

        else:
            action = random.choice(["Reverse", "Turn Left", "Turn Right"])

            if action == "Reverse":
                step_back = random.randint(5, 10)
                distance_travelled = max(0, distance_travelled - step_back)
                checkpoints.append(f"Object detected – Reverse to {distance_travelled}m")

            else:
                checkpoints.append(f"Object detected – {action}")
            continue

    # -------- DYNAMIC SPEED ADJUSTMENT --------
    if obstacle_count > 3:
        chosen_speed = "Slow"
    else:
        chosen_speed = base_speed if random.random() < 0.7 else random.choice(speed_levels)

    # -------- STEP SIZE --------
    if chosen_speed == "Slow":
        step_forward = random.randint(5, 8)
    elif chosen_speed == "Medium":
        step_forward = random.randint(9, 12)
    else:
        step_forward = random.randint(13, 18)

    # Prevent overshooting
    if distance_travelled + step_forward > target_distance:
        step_forward = target_distance - distance_travelled

    distance_travelled += step_forward
    total_speed_value += speed_values[chosen_speed]
    move_count += 1

    checkpoints.append(f"Move Forward ({chosen_speed}) → {distance_travelled}m")

# -------- CHECKPOINT UPDATE OPTION --------
remove_choice = input("Do you want to remove the last checkpoint? (yes/no): ").lower()
if remove_choice == "yes" and len(checkpoints) > 1:
    removed = checkpoints.pop()
    print(f"Removed checkpoint: {removed}")

# -------- AVERAGE SPEED CALCULATION --------
average_speed = total_speed_value / move_count if move_count > 0 else 0

# -------- TRIP SUMMARY --------
print("\n------ TRIP SUMMARY ------")
print(f"Bot Name            : {bot_name}")
print(f"Target Distance     : {target_distance}m")
print(f"Final Distance      : {distance_travelled}m")
print(f"Obstacle Ahead      : {obstacle_ahead}")
print(f"Initial Speed       : {base_speed}")
print(f"Total Moves         : {move_count}")
print(f"Total Obstacles     : {obstacle_count}")
print(f"Average Speed Level : {average_speed:.2f}")

if distance_travelled >= target_distance:
    print("Status              : Target Reached Successfully ✅")

print("\nJourney Log:")
for point in checkpoints:
    print("-", point)

print("--------------------------")
