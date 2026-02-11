import random

print("🤖 Welcome to RoboController 1.0")
print("-" * 40)

# --- User Inputs ---
robot_name = input("Enter robot name: ")
distance_to_target = float(input("Enter distance to target (in meters): "))
obstacle_input = input("Is there an obstacle ahead? (yes/no): ").lower()

obstacle_ahead = obstacle_input == "yes"

print("\n🔍 Analyzing situation...\n")

# --- Decide Speed & Movement ---
if obstacle_ahead:
    if distance_to_target < 20:
        speed = 0
        movement = "STOPPED due to a very close obstacle!"
    else:
        speed = 2
        movement = "Moving SLOWLY to avoid obstacle."
else:
    if distance_to_target > 100:
        speed = 10
        movement = "Moving FAST towards distant target."
    elif distance_to_target > 50:
        speed = 6
        movement = "Moving at MEDIUM speed."
    else:
        speed = 3
        movement = "Moving SLOWLY, close to target."

print(f"🚀 Decision: {movement}")
print(f"⚙️ Speed set to {speed} m/s\n")

# --- Random Direction Simulation ---
directions = ["Left", "Right", "Forward", "Backward"]
direction_changes = []

for _ in range(3):
    direction = random.choice(directions)
    direction_changes.append(direction)

# --- Distance Travel Simulation ---
distance_travelled = min(distance_to_target, speed * 10)

# --- Trip Summary ---
print("\n" + "=" * 40)
print("📊 TRIP SUMMARY")
print("=" * 40)

print(f"🤖 Robot Name           : {robot_name}")
print(f"📏 Target Distance       : {distance_to_target} meters")
print(f"🚧 Obstacle Ahead        : {'Yes' if obstacle_ahead else 'No'}")
print(f"⚡ Final Speed            : {speed} m/s")
print(f"🛣️ Distance Travelled     : {distance_travelled:.2f} meters")

print("🔄 Random Direction Changes During Trip:")
for d in direction_changes:
    print("   •", d)

print("\n✅ Mission simulation complete!")










##############################################
import random

print("🤖 Welcome to RoboController 1.0")
print("-" * 40)

# --- User Inputs ---
robot_name = input("Enter robot name: ")
distance_to_target = float(input("Enter distance to target (in meters): "))
obstacle_input = input("Is there an obstacle ahead? (yes/no): ").lower()

obstacle_ahead = obstacle_input == "yes"

print("\n🔍 Analyzing situation...\n")

# --- Decide Speed & Movement ---
if obstacle_ahead:
    if distance_to_target < 20:
        speed = 0
        movement = "STOPPED due to a very close obstacle!"
    else:
        speed = 2
        movement = "Moving SLOWLY to avoid obstacle."
else:
    if distance_to_target > 100:
        speed = 10
        movement = "Moving FAST towards distant target."
    elif distance_to_target > 50:
        speed = 6
        movement = "Moving at MEDIUM speed."
    else:
        speed = 3
        movement = "Moving SLOWLY, close to target."

print(f"🚀 Decision: {movement}")
print(f"⚙️ Speed set to {speed} m/s\n")

# --- Checkpoint System ---
checkpoints = []

print("\n📍 Adding initial checkpoints...")
for i in range(3):
    cp = f"Checkpoint_{i+1}"
    checkpoints.append(cp)

print("Current Checkpoints:", checkpoints)

# Add a new checkpoint
new_cp = input("\nAdd a new checkpoint name: ")
checkpoints.append(new_cp)
print("✅ Checkpoint added!")

# Remove a checkpoint
remove_cp = input("Enter checkpoint name to remove: ")
if remove_cp in checkpoints:
    checkpoints.remove(remove_cp)
    print("❌ Checkpoint removed!")
else:
    print("⚠️ Checkpoint not found.")

print("Updated Checkpoints:", checkpoints)

# --- Random Direction Simulation ---
directions = ["Left", "Right", "Forward", "Backward"]
direction_changes = []

for _ in range(3):
    direction = random.choice(directions)
    direction_changes.append(direction)

# --- Distance Travel Simulation ---
distance_travelled = min(distance_to_target, speed * 10)

# --- Trip Summary ---
print("\n" + "=" * 40)
print("📊 TRIP SUMMARY")
print("=" * 40)

print(f"🤖 Robot Name           : {robot_name}")
print(f"📏 Target Distance       : {distance_to_target} meters")
print(f"🚧 Obstacle Ahead        : {'Yes' if obstacle_ahead else 'No'}")
print(f"⚡ Final Speed            : {speed} m/s")
print(f"🛣️ Distance Travelled     : {distance_travelled:.2f} meters")

print("\n📍 Final Checkpoints Visited:")
for cp in checkpoints:
    print("   •", cp)

print("\n🔄 Random Direction Changes During Trip:")
for d in direction_changes:
    print("   •", d)

print("\n✅ Mission simulation complete!")
