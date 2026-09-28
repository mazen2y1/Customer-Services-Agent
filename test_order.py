from db import fetch_order

print("Existing order:")
print(fetch_order("1003"))

print("\nNon-existing order:")
print(fetch_order("9999"))