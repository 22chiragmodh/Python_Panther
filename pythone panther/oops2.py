class Employee:
    no_of_leave=6
    fm=5
    pass
mohan=Employee()
raghav=Employee()
mohan.name="mohankumar"
mohan.salary=12500
mohan.role="coder"
raghav.name="raghavkumar"
raghav.salary=18500
raghav.role="instructer"
# fm class ki property hai ussko kisibhi object se acsees kar sakte hai
print(raghav.fm)
print(mohan.fm)
raghav.fm=7
Employee.fm=7
print(raghav.__dict__)
# raghav ka fm change kiya usse employee ko koi fark nhi padta object apna instant variable banata hai
# employee class se fm ko chnage kar sakte hai kyu ki vo apni class ki property hai
print(Employee.fm)
