import admin_import


privileges = ["can add post", "can delete post", "can ban user", "can change database"]

obj1 = admin_import.Admin("Master", "Lee", 27, "Male", "India", privileges)
obj1.privilege.show_privileges()