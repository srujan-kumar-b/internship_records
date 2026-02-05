
raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]

has_id05 = "ID05" in raw_logs

unique_users = set(raw_logs)

print("Raw logs:", raw_logs)
print("Unique users:", unique_users)
print(f"Is 'ID05' a unique visitor? {has_id05}")
print(f"Count in raw logs: {len(raw_logs)}")
print(f"Count of unique users: {len(unique_users)}")

