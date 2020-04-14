/*Appointments*/
CREATE TABLE Appointments
(Employee_id number not null,
Employee_name varchar2 (1000) not null,
Out_Patient_name varchar2 (1000) not null,
Ident_code number not null,
Department_name varchar2 (1000) not null,
Appointment_day varchar2 (1000) not null,
Appointment_time varchar2 (1000) not null,
Appointment_date varchar2 (1000) not null,
CONSTRAINT e_p PRIMARY KEY (Employee_id, Ident_code, Appointment_date),
CONSTRAINT zsxdgfh FOREIGN KEY(Employee_name)
REFERENCES Hexinger_Employees(Employee_name),
CONSTRAINT sdxre FOREIGN KEY(Department_name)
REFERENCES Hexinger_Departments(Department_name),
CONSTRAINT sadfvfvgd FOREIGN KEY(Out_Patient_name)
REFERENCES Out_Hospital_Patients(Out_Patient_name),
CONSTRAINT FERB FOREIGN KEY(Employee_id)
REFERENCES Hexinger_Employees(Employee_id),
CONSTRAINT wer FOREIGN KEY(Ident_code)
REFERENCES Out_Hospital_Patients(Ident_code)
);



INSERT INTO Appointments
(Employee_id, Employee_name, Out_Patient_name, Ident_code, Department_name, Appointment_day, Appointment_time, Appointment_date)
VALUES(3495678590230, 'Catters, Katherine E.', 'Robinson, Mae A.', 23456789087654, 'Cardiac Surgery', 'Tuesday', '11:00-14:00', '23-янв-2017')


select * from Appointments






/*Out_Hospital_Patients*/

CREATE TABLE Out_Hospital_Patients
(Ident_code number not null,
Out_Patient_name varchar2 (1000) not null,
Birthdate date not null,
Phone_num number (38) not null,
District_id number (38) not null,
Ad_street varchar2 (100) not null,
Ad_house number (38) not null,
Ad_flat number (38),
Employee_id number not null,
CONSTRAINT jpat PRIMARY KEY (Ident_code),
CONSTRAINT pat_un unique(Out_Patient_name),
CONSTRAINT out_pat_dist FOREIGN KEY(District_id)
REFERENCES Districts(District_id),
CONSTRAINT skmlfr FOREIGN KEY(Employee_id)
REFERENCES Hexinger_Employees(Employee_id)
);

INSERT INTO Out_Hospital_Patients
(Ident_code, Out_Patient_name, Birthdate, Phone_num, District_id, Ad_street,
Ad_house, Ad_flat, Employee_id)
VALUES(095859404580, 'Catters, Neil A.D.J.', '18-сен-2000', 0686055993, 54, 'Superno',
137, 0, 3495678590230)

INSERT INTO Out_Hospital_Patients
(Ident_code, Out_Patient_name, Birthdate, Phone_num, District_id, Ad_street,
Ad_house, Ad_flat, Employee_id)
VALUES(23456789087654, 'Robinson, Mae A.', '5-дек-2000', 0685593993, 56, 'Fidele',
17, 0, 3495678590230)

delete from Out_Hospital_Patients
where Phone_num =0685593993

select * from Out_Hospital_Patients

Select o.Out_Patient_name, emp.Employee_id, emp.Employee_name
from Out_Hospital_Patients o, Hospital_Employees emp
where o.Employee_id = emp.Employee_id AND emp.Employee_name = 'Catters, Katherine E.'




/*Timetable*/

CREATE TABLE Timetable
(Employee_name varchar2 (1000) not null,
Department_name varchar2 (1000) not null,
Job_name varchar2 (1000) not null,
Phone_num number (38) not null,
Reception_days varchar2 (1000) not null,
Reception_time varchar2 (1000) not null,
CONSTRAINT dtj PRIMARY KEY (Employee_name,Phone_num, Reception_days, Reception_time),
CONSTRAINT srht FOREIGN KEY(Employee_name)
REFERENCES Hexinger_Employees(Employee_name),
CONSTRAINT ahtgyj FOREIGN KEY(Department_name)
REFERENCES Hexinger_Departments(Department_name),
CONSTRAINT trajn FOREIGN KEY(Job_name)
REFERENCES Hospital_Jobs(Job_name),
CONSTRAINT tarjyu FOREIGN KEY(Phone_num)
REFERENCES Hexinger_Employees(Phone_num)
);

/*alter table Timetable
add constraint hdf PRIMARY KEY (Employee_name,Phone_num, Reception_day, Start_of_reception)*/

/*alter table Timetable
modify End_of_reception varchar2 (1000);*/

INSERT INTO Timetable
(Employee_name, Department_name, Job_name, Phone_num, Reception_days, Reception_time)
VALUES('Catters, Katherine E.', 'Cardiac Surgery', 'Surgeon', 4356457657, 'Tuesday, Thursday', '11:00-14:00')

/*INSERT INTO Timetable
(Employee_name, Department_name, Job_name, Phone_num, Reception_day, Reception_time)
VALUES('Catters, Katherine E.', 'Cardiac Surgery', 'Surgeon', 4356457657, 'Thursday', '11:00-14:00')*/

INSERT INTO Timetable
(Employee_name, Department_name, Job_name, Phone_num, Reception_days, Reception_time)
VALUES('Gallivan, Viktoria', 'Reanimation', 'Surgeon', 87654321234, 'Wednesday', '10:00-13:00')

/*delete from Timetable
where Phone_num =4356457657*/

select * from Timetable

/*INSERT INTO Employee_Job_History
(Employee_id, Start_job_date, Finish_job_date, Job_id, Department_id)
VALUES(23456789009876, '6-май-2000', '1-янв-1970', 201, 107)*/



/*In-Hospital Patients*/

CREATE TABLE In_Hospital_Patients
(Patient_name varchar2 (1000) not null,
Ident_code number not null,
Birthdate date not null,
Phone_num number (38) not null,
District_id number (38) not null,
Ad_street varchar2 (100) not null,
Ad_house number (38) not null,
Ad_flat number (38),
Department_id number (38) not null,
Ailment_id number (38) not null,
Category_id number not null,
Employee_id number (38) not null,
Start_date date not null,
Finish_date date not null,
CONSTRAINT InHosP PRIMARY KEY (Ident_code),
CONSTRAINT InHosDep FOREIGN KEY(Department_id)
REFERENCES Hexinger_Departments(Department_id),
CONSTRAINT InHosIlls FOREIGN KEY(Ailment_id)
REFERENCES Ailments(Ailment_id),
CONSTRAINT InHosCategs FOREIGN KEY(Category_id)
REFERENCES Ailment_Categories(Category_id),
CONSTRAINT Doctor FOREIGN KEY(Employee_id)
REFERENCES Hexinger_Employees(Employee_id),
CONSTRAINT InHosDis FOREIGN KEY(District_id)
REFERENCES Districts(District_id)
);




INSERT INTO In_Hospital_Patients
(Patient_name, Ident_code, Birthdate, Phone_num, District_id, Ad_street,
Ad_house, Ad_flat, Department_id, Ailment_id, Category_id, Employee_id, Start_date, Finish_date)
VALUES('Grace, Virginia', 7689049385949, '7-янв-2001', 4356457657, 54, 'Lackenrid',
456, 0, 107, 35,1, 23456789009876, '21-дек-2016', '19-мар-2017')


Select *
from In_Hospital_Patients
order by District_id


/*Job History*/
CREATE TABLE Employee_Job_History
(Employee_id number not null,
Start_job_date date not null,
Finish_job_date date,
Job_id number not null,
Department_id number not null,
CONSTRAINT job_his PRIMARY KEY (Employee_id, Job_id),
CONSTRAINT jst FOREIGN KEY(Job_id)
REFERENCES Hospital_Jobs(Job_id),
CONSTRAINT dtpsg FOREIGN KEY(Department_id)
REFERENCES Hexinger_Departments(Department_id),
CONSTRAINT fher FOREIGN KEY(Employee_id)
REFERENCES Hexinger_Employees(Employee_id)
);


INSERT INTO Employee_Job_History
(Employee_id, Start_job_date, Finish_job_date, Job_id, Department_id)
VALUES(23456789009876, '6-май-2000', '1-янв-1970', 201, 107)

INSERT INTO Employee_Job_History
(Employee_id, Start_job_date, Finish_job_date, Job_id, Department_id)
VALUES(3495678590230, '23-авг-1998', '1-янв-1970', 201, 113)

VALUES('Catters, Katherine E.', 3495678590230, '9-авг-1974', 4356457657, 54, 'Superno',
137, 0, 113, 201, 3100)
VALUES('Gallivan, Viktoria', 23456789009876, '24-окт-1981', 87654321234, 56, 'Elphenost',
678, 0, 107, 201, 3225)

Select *
from Employee_Job_History
order by Job_id

/*Ailments*/

CREATE TABLE Ailments
(Ailment_id number not null,
Ailment_name varchar2 (1000) not null,
CONSTRAINT Ails PRIMARY KEY (Ailment_id));

INSERT INTO Ailments
(Ailment_id, Ailment_name)
VALUES(33, 'Witch Cold')

Select *
from Ailments
order by Ailment_id

31  Cancer
32  Strangetown Syndrome
33  Witch Cold
34  Leukemia
35  Stab Wounds

/*Ailment Categories*/

CREATE TABLE Ailment_Categories
(Category_id number not null,
Category_name varchar2 (1000) not null,
CONSTRAINT Cats PRIMARY KEY (Category_id));

INSERT INTO Ailment_Categories
(Category_id, Category_name)
VALUES(01, 'Critical')

delete from Ailment_Categories
where Category_id = 01

Select *
from Ailment_Categories
order by Category_id

1   Critical
2   Bad
3   Acceptable
4   Normal


/*Hospital Jobs*/

CREATE TABLE Hospital_Jobs
(Job_id number not null,
Job_name varchar2 (1000) not null,
Min_salary number not null,
Max_salary number not null,
CONSTRAINT job PRIMARY KEY (Job_id),
constraint job_un unique(Job_name)
);

INSERT INTO Hospital_Jobs
(Job_id, Job_name, Min_salary, Max_salary)
VALUES(201, 'Surgeon', 1250, 4500)

Select *
from Hospital_Jobs
order by Job_id



/*Districts*/

CREATE TABLE Districts
(District_id number not null,
District_name varchar2 (1000) not null,
CONSTRAINT Dist PRIMARY KEY (District_id));

INSERT INTO Districts
(District_id, District_name)
VALUES(51, 'Fogden')

Select *
from Districts
order by District_id

51  Fogden
52  Saint-Bane
53  Fasematter
54  Peregrin
55  New-Gallet
56  Blicksaine


/*Hexinger Departments*/

CREATE TABLE Hexinger_Departments
(Department_id number not null,
Department_name varchar2 (1000) not null,
CONSTRAINT Deps PRIMARY KEY (Department_id),
constraint dep_un unique(Department_name)
);

INSERT INTO Hexinger_Departments
(Department_id, Department_name)
VALUES(101, 'Therapy')

101 Therapy
102 Neurology
103 Cardiology
104 Gastroenterology
105 Diagnostic Reception
106 Allergological
107 Reanimation
108 Gynecology
109 Urology
110 Traumatological
111 Surgery
112 Neurosurgical
113 Cardiac Surgery
114 Anesthesiology
115 Pediatrics
/*
alter table Hos_Departments
add (Dep_head_id number)

alter table Hos_Departments
add constraint adbfgb FOREIGN KEY(Dep_head_id)
REFERENCES Hospital_Employees(Employee_id)

alter table Hos_Departments
drop column Dep_head_id

INSERT INTO Hos_Departments
(Department_id, Department_name)
VALUES(113, 'Surge')

update Hos_Departments
set Department_id = 113,
Department_name = 'Surge',
 Dep_head_id = 3495678590230

select * from Hos_Departments
*/

alter table Hexinger_Departments
add (Dep_head_id number)

alter table Hexinger_Departments
drop column Dep_head_id

alter table Hexinger_Departments
add constraint lokhj FOREIGN KEY(Dep_head_id)
REFERENCES Hexinger_Employees(Employee_id)

update Hexinger_Departments
set Department_id = 107,
Department_name = 'Reanimation',
 Dep_head_id = 23456789009876

101 Therapy
102 Neurology
103 Cardiology
104 Gastroenterology
105 Diagnostic Reception
106 Allergological
107 Reanimation
108 Gynecology
109 Urology
110 Traumatological
111 Surgery
112 Neurosurgical
113 Cardiac Surgery
114 Anesthesiology
115 Pediatrics

Select *
from Hexinger_Departments
order by Department_id







/*Hexinger Doctors*/

CREATE TABLE Hexinger_Employees
(Employee_name varchar2 (1000) not null,
Employee_id number not null,
Birthdate date not null,
Phone_num number (38) not null,
District_id number (38) not null,
Ad_street varchar2 (100) not null,
Ad_house number (38) not null,
Ad_flat number (38),
Department_id number (38) not null,
Job_id number (38) not null,
Salary number not null,
CONSTRAINT emps_id PRIMARY KEY (Employee_id),
constraint empg_un unique(Employee_name),
constraint pho_un unique(Phone_num),
CONSTRAINT emps_dep FOREIGN KEY(Department_id)
REFERENCES Hexinger_Departments(Department_id),
CONSTRAINT empvg_j FOREIGN KEY(Job_id)
REFERENCES Hospital_Jobs(Job_id),
CONSTRAINT empsw_dist FOREIGN KEY(District_id)
REFERENCES Districts(District_id)
);


INSERT INTO Hexinger_Employees
(Employee_name, Employee_id, Birthdate, Phone_num, District_id, Ad_street,
Ad_house, Ad_flat, Department_id, Job_id, Salary)
VALUES('Catters, Katherine E.', 3495678590230, '9-авг-1974', 4356457657, 54, 'Superno',
137, 0, 113, 201, 3100)

INSERT INTO Hexinger_Employees
(Employee_name, Employee_id, Birthdate, Phone_num, District_id, Ad_street,
Ad_house, Ad_flat, Department_id, Job_id, Salary)
VALUES('Gallivan, Viktoria', 23456789009876, '24-окт-1981', 87654321234, 56, 'Elphenost',
678, 0, 107, 201, 3225)


Select *
from Hexinger_Employees



