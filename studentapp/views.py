from django.shortcuts import render,redirect
from studentapp.models import StudentDetails

# Create your views here.
def f1(request):
    return render(request,"student.html")
def add_studdetails(request):
    if request.method=='POST':
        name=request.POST['student_name']
        address=request.POST['student_address']
        stage=request.POST['student_age']
        email=request.POST['student_email']
        date1=request.POST['joining_date']
        qual=request.POST['qualification']
        gender=request.POST['gender']
        
        mno=request.POST['mobileno']
        student=StudentDetails(student_name=name,student_address=address,student_age=stage,student_email=email,joining_date=date1,qualification=qual,gender=gender,mobileno=mno)
        student.save()
        return redirect('/')
def show_students(request):
    student=StudentDetails.objects.all()
    return render(request,'showstudent.html',{'students':student})
def editpage(request,pk):
    student=StudentDetails.objects.get(id=pk)
    qual=StudentDetails.objects.values('qualification').distinct()
    return render(request,'edit.html',{'student':student,'q':qual})
def studname(request,pk):
    student=StudentDetails.objects.get(id=pk)
    return render(request,'studname.html',{'students':student})
def edit_student_details(request,pk):
    if request.method=='POST':
        student=StudentDetails.objects.get(id=pk)
        student.student_name=request.POST['student_name']
        student.student_address=request.POST['student_address']
        student.student_age=request.POST['student_age']
        student.student_email=request.POST['student_email']
        student.joining_date=request.POST['joining_date']
        student.qualification=request.POST['qualification']
        student.gender=request.POST['gender']
        student.mobileno=request.POST['mobileno']
        student.save()
        return redirect('show_students')
    return render(request,"edit.html")
def deletepage(request,pk):
    student=StudentDetails.objects.get(id=pk)
    student.delete()
    return redirect('show_students')
