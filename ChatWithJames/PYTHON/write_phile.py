content = """Michael Jordan's career

Michael Jordan is one of the greatest basketball players in history. He played for the Chicago Bulls, won six NBA championships, and was a five-time MVP. He also won two Olympic gold medals and became a global sports icon. After retiring from basketball, he became a businessman and a successful entrepreneur.

Michael Jordan's story is a mix of athletic excellence, leadership, and business success.
"""

with open("brain.txt", "w", encoding="utf-8") as file:
    file.write(content)

print("brain.txt created successfully.")
