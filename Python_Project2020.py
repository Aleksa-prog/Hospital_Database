from tkinter import*
import tkinter.messagebox
from tkinter import ttk
import pypyodbc
import matplotlib
from PIL import ImageTk, Image
import cx_Oracle

conn = cx_Oracle.connect('HR/At10042001@USER-PC/xe')
cur = conn.cursor()
cur2 = conn.cursor()
cur3 = conn.cursor()
cur4 = conn.cursor()
cur5 = conn.cursor()
cur6 = conn.cursor()
cur7 = conn.cursor()
cur8 = conn.cursor()

time = 'select* from Timetable'
appointment = 'select Employee_name, Out_Patient_name, Department_name, Appointment_day, Appointment_time from Appointments'
employ = 'select Employee_name, Employee_id, Department_name, Phone_num, Job_name, Salary from Hexinger_Employees e, Hexinger_Departments d, Hospital_Jobs j where e.Job_id = j.Job_id and e.Department_id = d.Department_id'
departments = 'select* from Hexinger_Departments'
history = 'select e.Employee_name, h.Start_job_date, h.Finish_job_date, h.Job_id, h.Department_id from Employee_Job_History h, Hexinger_Employees e where h.Employee_id = e.Employee_id'
ins = 'select p.Patient_name, p.Ident_code, p.Ailment_id, p.Department_id, e.Employee_name, p.Category_id from In_Hospital_Patients p, Hexinger_Employees e where p.Employee_id = e.Employee_id'
pat = 'select o.Out_Patient_name, o.Ident_code, o.Phone_num, e.Employee_name from Out_Hospital_Patients o, Hexinger_Employees e where o.Employee_id = e.Employee_id'
ail = 'select* from Ailments'

cur.execute(time)
cur2.execute(appointment)
cur3.execute(employ)
cur4.execute(departments)
cur5.execute(history)
cur6.execute(ins)
cur7.execute(pat)
cur8.execute(ail)              


rows = cur.fetchall()
backs = cur2.fetchall()
ems = cur3.fetchall()
departs = cur4.fetchall()
hiss = cur5.fetchall()
inses = cur6.fetchall()
patt = cur7.fetchall()
els = cur8.fetchall()

cur.close()
cur2.close()
cur3.close()
cur4.close()
cur5.close()
cur6.close()
cur7.close()
cur8.close()



# ГЛАВНАЯ СТРАНИЦА
app = Tk()
app.title("Kraileseng Hospital")
app.geometry('1273x663')
app.configure(background = "peachpuff")

def timetab():
    hour = Tk()
    hour.title("Timetable of receptions")
    hour.geometry('1273x663')
    hour.configure(background = "peachpuff")
    hitime = Label(hour, text = "Timetable of receptions", font = ("Times", 22, "bold italic"), background = "peachpuff")
    hitime.place(x = 424, y = 13, height = 60, width = 500)

    frame = Frame(hour)
    frame.place(x = 37, y = 100, height = 179, width = 1200)
 
    tv = ttk.Treeview(frame, columns = (1,2,3,4,5,6), show = "headings", height = "10")
    tv.pack()

    tv.heading(1, text = "Врач")
    tv.heading(2, text = "Отделение")
    tv.heading(3, text = "Профессия")
    tv.heading(4, text = "Номер телефона")
    tv.heading(5, text = "Дни приема")
    tv.heading(6, text = "Время приема")

    for i in rows:
        tv.insert('', 'end', values = i)

def appoint():
    aps = Tk()
    aps.title("Appointments")
    aps.geometry('1273x663')
    aps.configure(background = "peachpuff")
    hiaps = Label(aps, text = "Make an appointment", font = ("Times", 22, "bold italic"), background = "peachpuff")
    hiaps.place(x = 424, y = 13, height = 60, width = 500)

    def makein():
        m = Tk()
        m.title("Make an appointment")
        m.geometry('459x502')
        m.configure(background = "peachpuff")
        
        def confirm():
            one = didtxt.get()
            seven = datamtxt.get()
            dock = doctxt.get()
            pati = pattxt.get()
            departmes = deptxt.get()
            das = daytxt.get()
            timothy = timtxt.get()
            id = idtxt.get()
            if dock != None and pati != None and departmes != None and das != None and timothy != None and id != None and one != None and seven != None:
                m.destroy()
                tv.insert('', 'end', values = (dock, pati, departmes, das, timothy))
                def fun_insert():
                    cur9 = conn.cursor()
                    command9 = "insert into Appointments values(:one, :dock, :pati, :id, :departmes, :das, :timothy, :seven)" 
                    cur9.execute(command9, (one, dock, pati, id, departmes, das, timothy, seven))
                    conn.commit()
                    cur9.close()
                fun_insert()
                

                new_db = open("C:/Users/User/Desktop/Функ.Прог/Python/NewData.txt", "a")
                new_db.write(dock + " ; " + pati + " ; " + id + " ; " + departmes + " ; " + das + " ; " + timothy + " ; " + "\n")
                new_db.close() 


        dint = Label(m, text = "Doctor's ID", font = ("Times", 12, "bold"), bg = "peachpuff")
        dint.pack()
        
        didtxt = Entry(m, width = 20, font = ("Times", 14))
        didtxt.pack()

        doctor = Label(m, text = "Doctor", font = ("Times", 12, "bold"), bg = "peachpuff")
        doctor.pack()
        
        doctxt = Entry(m, width = 20, font = ("Times", 14))
        doctxt.pack()
        
        patient = Label(m, text = "Pation Name", font = ("Times", 12, "bold"), bg = "peachpuff")
        patient.pack()
        
        pattxt = Entry(m, width = 20, font = ("Times", 14))
        pattxt.pack()

        ident =  Label(m, text = "Identification code", font = ("Times", 12, "bold"), bg = "peachpuff")
        ident.pack()

        idtxt = Entry(m, width = 20, font = ("Times", 14))
        idtxt.pack()

        department = Label(m, text = "Department Name", font = ("Times", 12, "bold"), bg = "peachpuff")
        department.pack()
        
        deptxt = Entry(m, width = 20, font = ("Times", 14))
        deptxt.pack()

        day = Label(m, text = "Appointment Day", font = ("Times", 12, "bold"), bg = "peachpuff")
        day.pack()
        
        daytxt = Entry(m, width = 20, font = ("Times", 14))
        daytxt.pack()

        tim = Label(m, text = "Appointment Time", font = ("Times", 12, "bold"), bg = "peachpuff")
        tim.pack()
        
        timtxt = Entry(m, width = 20, font = ("Times", 14))
        timtxt.pack()

        datam = Label(m, text = "Appointment Date", font = ("Times", 12, "bold"), bg = "peachpuff")
        datam.pack()
        
        datamtxt = Entry(m, width = 20, font = ("Times", 14))
        datamtxt.pack()

        confirm_btn = Button(m, text = "Confirm", font = ("Times", 16, "bold"), bg = "lightsalmon", command = confirm)
        confirm_btn.pack()



    make_btn = Button(aps, text = "Make an appointment", font = ("Times", 16, "bold"), bg = "lightsalmon", command = makein)
    make_btn.place(x = 116, y = 341, height = 93, width = 300)

    frame2 = Frame(aps)
    frame2.place(x = 37, y = 100, height = 179, width = 1200)
    frame2.configure(background = "peachpuff")

    tv = ttk.Treeview(frame2, columns = (1,2,3,4,5), show = "headings", height = "10")
    tv.pack()

    tv.heading(1, text = "Врач")
    tv.heading(2, text = "Ф.И.О. пациента")
    tv.heading(3, text = "Отделение")
    tv.heading(4, text = "День приема")
    tv.heading(5, text = "Время приема")

    for i in backs:
        tv.insert('', 'end', values = i)

def opn():
    #АВТОРИЗАЦИЯ
    window = Tk()
    window.title("Autorisation")
    window.geometry('459x502')
    window.configure(background = "peachpuff")

    def go():
        mustlog = "FogfallsAd"
        mustpas = "HKlH1923"
        log = logintxt.get()
        pas = passtxt.get()
        if log == mustlog and pas == mustpas:
            #app.destroy()
            window.destroy()

            #ГЛАВНАЯ СТРАНИЦА 2
            int = Tk()
            int.title("Limited Information")
            int.geometry('505x650')
            int.configure(background = "peachpuff")

            def docs():
                d = Tk()
                d.title("Employees Information")
                d.geometry('1273x663')
                dis = Label(d, text = "Employees Information", font = ("Times", 22, "bold italic"), background = "peachpuff")
                dis.place(x = 424, y = 13, height = 60, width = 500)
                d.configure(background = "peachpuff")
                
                frame1_1 = Frame(d)
                frame1_1.place(x = 37, y = 100, height = 179, width = 1200)
                frame1_1.configure(background = "peachpuff")
                
                tv1_1 = ttk.Treeview(frame1_1, columns = (1,2,3,4,5,6), show = "headings", height = "10")
                tv1_1.pack()
                
                tv1_1.heading(1, text = "Ф.И.О")
                tv1_1.heading(2, text = "Идент.код")
                tv1_1.heading(3, text = "Отделение")
                tv1_1.heading(4, text = "Номер телефона")
                tv1_1.heading(5, text = "Должность")
                tv1_1.heading(6, text = "Зарплата")

                for i in ems:
                    tv1_1.insert('', 'end', values = i)

            def deps():
                deps = Tk()
                deps.title("Hospital Departments")
                deps.geometry('1273x663')
                deps.configure(background = "peachpuff")
                
                dеs = Label(deps, text = "Hospital Departments", font = ("Times", 22, "bold italic"), background = "peachpuff")
                dеs.place(x = 424, y = 13, height = 60, width = 500)
                
                frame1_2 = Frame(deps)
                frame1_2.place(x = 37, y = 100, height = 179, width = 1200)
                frame1_2.configure(background = "peachpuff")
               
                tv1_2 = ttk.Treeview(frame1_2, columns = (1,2), show = "headings", height = "10")
                tv1_2.pack()
                
                tv1_2.heading(1, text = "Название")
                tv1_2.heading(2, text = "Код")

                for i in departs:
                    tv1_2.insert('', 'end', values = i)

            def j():
                j = Tk()
                j.title("Employees Job History")
                j.geometry('1273x663')
                j.configure(background = "peachpuff")
                
                jis = Label(j, text = "Employees Job History", font = ("Times", 22, "bold italic"), background = "peachpuff")
                jis.place(x = 424, y = 13, height = 60, width = 500)
                
                frame1_3 = Frame(j)
                frame1_3.place(x = 37, y = 100, height = 179, width = 1200)
                frame1_3.configure(background = "peachpuff")
                
                tv1_3 = ttk.Treeview(frame1_3, columns = (1,2,3,4,5), show = "headings", height = "10")
                tv1_3.pack()
                
                tv1_3.heading(1, text = "Ф.И.О.")
                tv1_3.heading(2, text = "Дата начала")
                tv1_3.heading(3, text = "Дата оконч.")
                tv1_3.heading(4, text = "Код_должн.")
                tv1_3.heading(5, text = "Код_отдел.")

                for i in hiss:
                    tv1_3.insert('', 'end', values = i)

            def sicks():
               sicks = Tk()
               sicks.title("In-Hospital Patients")
               sicks.geometry('1273x663')
               sicks.configure(background = "peachpuff")
               
               sis = Label(sicks, text = "In-Hospital Patients", font = ("Times", 22, "bold italic"), background = "peachpuff")
               sis.place(x = 424, y = 13, height = 60, width = 500)
               
               frame1_4 = Frame(sicks)
               frame1_4.place(x = 37, y = 100, height = 179, width = 1200)
               frame1_4.configure(background = "peachpuff")
               
               tv1_4 = ttk.Treeview(frame1_4, columns = (1,2,3,4,5,6), show = "headings", height = "10")
               tv1_4.pack()
               
               tv1_4.heading(1, text = "Ф.И.О")
               tv1_4.heading(2, text = "Идент.код")
               tv1_4.heading(3, text = "Код_болезни")
               tv1_4.heading(4, text = "Код_отдел.")
               tv1_4.heading(5, text = "Врач")
               tv1_4.heading(6, text = "Категория")

               for i in inses:
                    tv1_4.insert('', 'end', values = i)

            def pats():
              pats = Tk()
              pats.title("Out-Hospital Patients")
              pats.geometry('1273x663')
              pats.configure(background = "peachpuff")
              
              pis = Label(pats, text = "Out-Hospital Patients", font = ("Times", 22, "bold italic"), background = "peachpuff")
              pis.place(x = 424, y = 13, height = 60, width = 500)
              
              frame1_5 = Frame(pats)
              frame1_5.place(x = 37, y = 100, height = 179, width = 1200)
              frame1_5.configure(background = "peachpuff")
              
              tv1_5 = ttk.Treeview(frame1_5, columns = (1,2,3,4), show = "headings", height = "10")
              tv1_5.pack()
              
              tv1_5.heading(1, text = "Ф.И.О")
              tv1_5.heading(2, text = "Идент.код")
              tv1_5.heading(3, text = "Телефон")
              tv1_5.heading(4, text = "Врач")

              for i in patt:
                    tv1_5.insert('', 'end', values = i)

            def ills():
                ills = Tk()
                ills.title("Ailments List")
                ills.geometry('1273x663')
                ills.configure(background = "peachpuff")
                
                iеs = Label(ills, text = "Ailments List", font = ("Times", 22, "bold italic"), background = "peachpuff")
                iеs.place(x = 424, y = 13, height = 60, width = 500)
                
                frame1_6 = Frame(ills)
                frame1_6.place(x = 37, y = 100, height = 179, width = 1200)
                frame1_6.configure(background = "peachpuff")
                
                tv1_6 = ttk.Treeview(frame1_6, columns = (1,2), show = "headings", height = "10")
                tv1_6.pack()
                
                tv1_6.heading(1, text = "Код_забол.")
                tv1_6.heading(2, text = "Название")

                for i in els:
                    tv1_6.insert('', 'end', values = i)

            hello = Label(int, text = "Limited Access Information", font = ("Times", 22, "bold italic"), background = "peachpuff")
            hello.place(x = 11, y = 21, height = 60, width = 500)
                
            docs_btn = Button(int, text = "Employees", font = ("Times", 16, "bold"), bg = "lightsalmon", command = docs)
            docs_btn.place(x = 116, y = 101, height = 93, width = 300)
                
            dep_btn = Button(int, text = "Departments", font = ("Times", 16, "bold"), bg = "lightsalmon", command = deps)
            dep_btn.place(x = 116, y = 181, height = 93, width = 300)
                
            jobhis_btn = Button(int, text = "Job Histories", font = ("Times", 16, "bold"), bg = "lightsalmon", command = j)
            jobhis_btn.place(x = 116, y = 261, height = 93, width = 300)
                
            sicks_btn = Button(int, text = "In-Hos Patients", font = ("Times", 16, "bold"), bg = "lightsalmon", command = sicks)
            sicks_btn.place(x = 116, y = 341, height = 93, width = 300)
                
            patients_btn = Button(int, text = "Out-Hos Patients", font = ("Times", 16, "bold"), bg = "lightsalmon", command = pats)
            patients_btn.place(x = 116, y = 421, height = 93, width = 300)
                
            ills_btn = Button(int, text = "Ailments List", font = ("Times", 16, "bold"), bg = "lightsalmon", command = ills)
            ills_btn.place(x = 116, y = 501, height = 93, width = 300)
        else: 
            tkinter.messagebox.showinfo("Information", "Access to the hospital files denied! You are not a hospital employee.")
            window.destroy()



#АВТОРИЗАЦИЯ
    login = Label(window, text = "Login", font = ("Times", 12, "bold"), bg = "peachpuff")
    login.place(x = 19, y = 100)

    logintxt = Entry(window, width = 20, font = ("Times", 14))
    logintxt.place(x = 94, y = 130, height = 64, width = 339)

    password = Label(window, text = "Password", font = ("Times", 12, "bold"), bg = "peachpuff")
    password.place(x = 19, y = 215)

    passtxt = Entry(window, width = 20, font = ("Times", 14))
    passtxt.place(x = 94, y = 245, height = 64, width = 339)

    img1 = ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/Функ.Прог/Python/user_icon.png'))
    view = Label(image = img1, background = "peachpuff")
    view.place(x = 24, y = 130, height = 64, width = 64)

    img2 = ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/Функ.Прог/Python/password_icon.png'))
    view = Label(image = img2, background = "peachpuff")
    view.place(x = 24, y = 245, height = 64, width = 64)

    autor = Label(window, text = "Autorisation", font = ("Times", 22, "bold italic"), background = "peachpuff")
    autor.place(x = 116, y = 21, height = 46, width = 224)

    autobtn = Button(window, text = "Enter", font = ("Times", 16, "bold"), bg = "lightsalmon", command = go)
    autobtn.place(x = 157, y = 351, height = 93, width = 171)

#ГЛАВНАЯ СТРАНИЦА
hi = Label(app, text = "Welcome to Kraileseng Hospital", font = ("Times", 22, "bold italic"), background = "peachpuff")
hi.place(x = 424, y = 13, height = 60, width = 500)

img1_1 = ImageTk.PhotoImage(Image.open('C:/Users/User/Desktop/Функ.Прог/Python/Hosp.jpg'))
view1_1 = Label(image = img1_1, background = "peachpuff")
view1_1.place(x = 300, y = 75)#, height = 100, width = 150)

timetb_btn = Button(app, text = "Timetable", font = ("Times", 16, "bold"), bg = "lightsalmon", command = timetab)
timetb_btn.place(x = 50, y = 351, height = 93, width = 171)

appoint_btn = Button(app, text = "Appointments", font = ("Times", 16, "bold"), bg = "lightsalmon", command = appoint)
appoint_btn.place(x = 50, y = 451, height = 93, width = 171)

login_btn = Button(app, text = "Log in", font = ("Times", 16, "bold"), bg = "lightsalmon", command = opn)
login_btn.place(x = 50, y = 551, height = 93, width = 171)

app.mainloop()
conn.close()
























#root = Tk()
#root.geometry('1273x663')

#def close():
 #   root.destroy()
 #   app = Tk()
#    app.title("Timetable of receptions")
#    app.geometry('1273x663')


#button = Button(text = "Close", command = close)
#button.pack()

#root.mainloop()


#Подключаем к бд
      #conn = cx_Oracle.connect('HR/XE@localhost', 'At10042001', 'Hospital_DataBase')
      #Создаем курсор
      #mycursor = conn.cursor()
      #Выполняем sql-запрос
      #mycursor.execute('select * from Timetable')
      #Парсим полученный результат в список кортежей
      #result = mycursor.fetchall()
      #for(Employee_name, Department_name, Job_name, Phone_num, Reception_days, Reception_time) in result:
      #    print Employee_name + '|' + Department_name + '|' + Job_name + '|' + Phone_num + '|' + Reception_days + '|' + Reception_time
      #conn.close

#def back(app):
  #  app.show()