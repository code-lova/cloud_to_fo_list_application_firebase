import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Firestore reference
db = firestore.client()

# === GLOBAL USER VARIABLE ===
current_user = None

# Add a task to the user's collection
def add_task(title, description):
    task = {
        "title": title,
        "description": description,
        "completed": False
    }
    db.collection("users").document(current_user).collection("tasks").add(task)
    print("✅ Task added successfully.\n")


# List tasks for the current user
def list_tasks():
    tasks = db.collection("users").document(current_user).collection("tasks").stream()
    print("\n📋 Your Tasks:")
    found = False
    for doc in tasks:
        found = True
        task = doc.to_dict()
        print(f"- ID: {doc.id}")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Completed: {task['completed']}\n")
    if not found:
        print("⚠️ No tasks found.\n")


# Mark a task complete
def mark_task_complete(task_id):
    db.collection("users").document(current_user).collection("tasks").document(task_id).update({"completed": True})
    print("✅ Task marked as complete.\n")


# Delete task
def delete_task(task_id):
    db.collection("users").document(current_user).collection("tasks").document(task_id).delete()
    print("🗑️ Task deleted.\n")


# Login function, just simulation
def login():
    global current_user
    print("===== Login =====")
    username = input("Enter your username: ").strip()
    if not username:
        print("❗ Username cannot be empty.")
        return login()
    current_user = username
    print(f"✅ Logged in as '{current_user}'\n")


# Main program
def main():
    login()

    print("===== Cloud To-Do List for", current_user, "=====")

    while True:
        print("\nChoose an option:")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Logout")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(title, description)

        elif choice == "2":
            list_tasks()

        elif choice == "3":
            task_id = input("Enter Task ID to mark as complete: ")
            mark_task_complete(task_id)

        elif choice == "4":
            task_id = input("Enter Task ID to delete: ")
            delete_task(task_id)

        elif choice == "5":
            print("🔒 Logging out...")
            return main()

        elif choice == "6":
            print("👋 Goodbye!")
            break

        else:
            print("❗ Invalid choice, try again.")


if __name__ == "__main__":
    main()
