from database import initialize_database
from services import add_application, list_applications, search_applications, update_status, delete_application, dashboard

MENU = """
================ JOB APPLICATION TRACKER ================
1. Add application
2. View all applications
3. Search applications
4. Update application status
5. Delete application
6. Dashboard
0. Exit
===========================================================
"""

def required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field cannot be empty.")

def print_table(rows):
    if not rows:
        print("No applications found.")
        return
    headers = ["ID","Company","Role","Location","Applied","Status","Source"]
    widths = [4,18,25,16,12,12,18]
    print("\n" + " | ".join(h.ljust(w) for h,w in zip(headers,widths)))
    print("-+-".join("-"*w for w in widths))
    for r in rows:
        vals = [r["id"],r["company"],r["role"],r["location"] or "-",
                r["application_date"],r["status"],r["source"] or "-"]
        out=[]
        for v,w in zip(vals,widths):
            s=str(v)
            if len(s)>w: s=s[:w-3]+"..."
            out.append(s.ljust(w))
        print(" | ".join(out))

def main():
    try:
        initialize_database()
    except Exception as e:
        print("Database connection failed. Check config.py and MySQL.")
        print("Details:", e)
        return

    while True:
        print(MENU)
        choice=input("Choose an option: ").strip()

        if choice=="1":
            company=required("Company: ")
            role=required("Job role: ")
            location=input("Location (optional): ").strip()
            date=required("Application date (YYYY-MM-DD): ")
            status=input("Status [Applied]: ").strip() or "Applied"
            source=input("Source: ").strip()
            notes=input("Notes (optional): ").strip()
            try:
                add_application(company,role,location,date,status,source,notes)
                print("Application added successfully.")
            except Exception as e:
                print("Could not add application:",e)

        elif choice=="2":
            print_table(list_applications())

        elif choice=="3":
            keyword=required("Search keyword: ")
            print_table(search_applications(keyword))

        elif choice=="4":
            try:
                app_id=int(input("Application ID: "))
                status=required("New status [Applied/Interview/Rejected/Selected/On Hold]: ")
                if update_status(app_id,status):
                    print("Status updated.")
                else:
                    print("Application not found or invalid status.")
            except ValueError:
                print("Enter a valid numeric ID.")

        elif choice=="5":
            try:
                app_id=int(input("Application ID to delete: "))
                if input("Type DELETE to confirm: ").strip()=="DELETE":
                    print("Application deleted." if delete_application(app_id) else "Application not found.")
                else:
                    print("Deletion cancelled.")
            except ValueError:
                print("Enter a valid numeric ID.")

        elif choice=="6":
            d=dashboard()
            print("\n--- Dashboard ---")
            print("Total applications :",d["total"])
            print("Applied             :",d["Applied"])
            print("Interview           :",d["Interview"])
            print("Selected            :",d["Selected"])
            print("Rejected            :",d["Rejected"])
            print("On Hold             :",d["On Hold"])
            if d["total"]:
                print(f"Interview rate      : {d['Interview']/d['total']*100:.1f}%")
                print(f"Selection rate      : {d['Selected']/d['total']*100:.1f}%")

        elif choice=="0":
            print("Good luck with your job search!")
            break
        else:
            print("Invalid option.")

if __name__=="__main__":
    main()
