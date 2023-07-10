employees={
    {"name":"john","salary":3000,"desgination":"developer"},
     {"name":"emma","salary":4000,"desgination":"manager"},
      {"name":"kelly","salary":3500,"desgination":"tester"}
}

def max_salary_employee(employees):
 max_salary=employees[0]
 for emp in employees:
  if emp["salary"]>max_salary["salary"]:
   max_salary=emp

 return max_salary