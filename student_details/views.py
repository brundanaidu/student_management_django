from django.shortcuts import render,redirect
from .models import Student

# Create your views here.
def index(request):
     i=Student.objects.all()
     context={'i':i}
     return render(request,'index.html',context)
def create(request):
     if request.method == 'POST':
         name = request.POST['name']
         age = request.POST['age']
         email = request.POST['email']
         mobile = request.POST['mobile']
         Hindi = int(request.POST['Hindi'])
         Telugu = int(request.POST['Telugu'])
         English = int(request.POST['English'])
         Maths = int(request.POST['Maths'])
         Science = int(request.POST['Science'])
         Social = int(request.POST['Social'])
         Total_Marks = Hindi+Telugu+English+Maths+Science+Social

         data = Student(name=name, age=age, email=email, mobile=mobile, Hindi=Hindi, Telugu=Telugu, English=English, Maths=Maths, Science=Science, Social=Social, Total_Marks=Total_Marks)
         data.save()
         return redirect('index')

     return render(request, 'create.html')

def delete(request,pk):
    student=Student.objects.get(id=pk)
    student.delete()
    return redirect('index')
def edit(request, pk):
    edit_student = Student.objects.get(id=pk)
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        mobile = request.POST['mobile']
        Hindi = int(request.POST['Hindi'])
        Telugu = int(request.POST['Telugu'])
        English = int(request.POST['English'])
        Maths = int(request.POST['Maths'])
        Science = int(request.POST['Science'])
        Social = int(request.POST['Social'])
        Total_Marks = Hindi + Telugu + English + Maths + Science + Social

        edit_data = Student(id=pk, name=name, age=age, email=email, mobile=mobile, Hindi=Hindi, Telugu=Telugu,
                            English=English, Maths=Maths, Science=Science, Social=Social, Total_Marks=Total_Marks)
        edit_data.save()
        return redirect('index')
    context = {'edit_student': edit_student}
    return render(request, 'edit.html', context)


def view(request, pk):
    view = Student.objects.get(id=pk)

    return render(request, 'view.html', {'view': view})



