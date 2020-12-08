teaches_subject(Ram,ode).
teaches_subject(Kavita,dsa).
teaches_subject(Neeta,dtl).
teaches_subject(Rajesh,dsgt).
teaches_subject(Ganesh,fcs).
teaches_subject(Raj,ppl).

has_subject(math_dept,ode).
has_subject(computer_dept,dsa).
has_subject(computer_dept,dtl).
has_subject(computer_dept,dsgt).
has_subject(computer_dept,fcs).
has_subject(computer_dept,dsa).

has_student(comp_dept,rashmi).
has_student(comp_dept,nikita).
has_student(comp_dept,prasad).
has_student(comp_dept,samrudhi).
has_student(comp_dept,akash).
has_student(comp_dept,sakshi).
has_student(comp_dept,neha).
has_student(comp_dept,pradeep).
has_student(comp_dept,sanket).
has_student(comp_dept,arjun).
has_student(comp_dept,rani).
has_student(comp_dept,nilam).
has_student(comp_dept,rajesh).
has_student(comp_dept,om).
has_student(comp_dept,pallavi).
has_student(comp_dept,aishwarya).
has_student(comp_dept,deepa).
has_student(comp_dept,pratiksha).
has_student(comp_dept,pratik).
has_student(comp_dept,srushti).

has_enroll(ST,SB):-has_student(D,ST),has_subject(D,SB).
has_faculty(D,F):-teaches_subject(F,S),has_subject(D,S).
studies_under(S,F):-has_student(D,S),has_subject(D,SB),teaches_subject(F,SB).
