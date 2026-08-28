from database import get_connection

VALID_STATUSES={"Applied","Interview","Rejected","Selected","On Hold"}

def add_application(company,role,location,date,status,source,notes):
    if status not in VALID_STATUSES:
        status="Applied"
    conn=get_connection(); cur=conn.cursor()
    cur.execute("""
        INSERT INTO applications
        (company,role,location,application_date,status,source,notes)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
    """,(company,role,location or None,date,status,source or None,notes or None))
    conn.commit(); cur.close(); conn.close()

def list_applications():
    conn=get_connection(); cur=conn.cursor(dictionary=True)
    cur.execute("""SELECT id,company,role,location,application_date,status,source
                   FROM applications ORDER BY application_date DESC,id DESC""")
    rows=cur.fetchall(); cur.close(); conn.close()
    return rows

def search_applications(keyword):
    conn=get_connection(); cur=conn.cursor(dictionary=True)
    pattern=f"%{keyword}%"
    cur.execute("""SELECT id,company,role,location,application_date,status,source
                   FROM applications
                   WHERE company LIKE %s OR role LIKE %s OR location LIKE %s
                      OR status LIKE %s OR source LIKE %s
                   ORDER BY application_date DESC,id DESC""",
                (pattern,pattern,pattern,pattern,pattern))
    rows=cur.fetchall(); cur.close(); conn.close()
    return rows

def update_status(app_id,status):
    if status not in VALID_STATUSES: return False
    conn=get_connection(); cur=conn.cursor()
    cur.execute("UPDATE applications SET status=%s WHERE id=%s",(status,app_id))
    ok=cur.rowcount>0
    conn.commit(); cur.close(); conn.close()
    return ok

def delete_application(app_id):
    conn=get_connection(); cur=conn.cursor()
    cur.execute("DELETE FROM applications WHERE id=%s",(app_id,))
    ok=cur.rowcount>0
    conn.commit(); cur.close(); conn.close()
    return ok

def dashboard():
    conn=get_connection(); cur=conn.cursor(dictionary=True)
    cur.execute("""
        SELECT COUNT(*) total,
               SUM(status='Applied') Applied,
               SUM(status='Interview') Interview,
               SUM(status='Selected') Selected,
               SUM(status='Rejected') Rejected,
               SUM(status='On Hold') `On Hold`
        FROM applications
    """)
    d=cur.fetchone() or {}
    cur.close(); conn.close()
    for k in ["total","Applied","Interview","Selected","Rejected","On Hold"]:
        d[k]=int(d.get(k) or 0)
    return d
