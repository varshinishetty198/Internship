raw_logs=["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users=set(raw_logs)

is_present="ID05" in unique_users

print("ID05 is present in the unique users:", is_present)

print("Raw Logs:", raw_logs)
print("Unique Users:", unique_users)

print("\nComparison Count:")
print("Total log entries:", len(raw_logs))
print("Unique visitors:", len(unique_users))