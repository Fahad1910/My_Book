from django.shortcuts import render,redirect
from django.views.generic import View
from myapps.forms import BookModelForm
from myapps.models import Books
from django.contrib import messages


class CreateBookView(View):

    def get(self,request,*args,**kwargs):
        form=BookModelForm()
        return render(request,"book_add.html",{"form":form})

    def post(self,request,*args,**kwargs):
        form=BookModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Book has been created")
            # Books.objects.create(**form.cleaned_data)
            return render(request,"book_add.html",{"form":form})
        else:
            messages.error(request,"failed to create the book")
            return render(request,"book_add.html",{"form":form})


class BookListView(View):
    def get(self,request,*args,**kwargs):
        qs=Books.objects.all()
        return render (request,"book_list.html",{"data":qs})

    def post(self,request,*args,**kwargs):
        name=request.POST.get("box")
        qs=Books.objects.filter(book_name__icontains=name)
        return render(request,"book_list.html",{"data":qs})



class BookDetailView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Books.objects.get(id=id)
        return render(request,"book_detail.html",{"data":qs})
    


class BookDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Books.objects.get(id=id).delete()
        messages.success(request,"Book has been removed")
        return redirect("book-all")
    

class BookUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookModelForm(instance=obj)
        return render(request,"book_edit.html",{"form":form})     

    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Books.objects.get(id=id)
        form=BookModelForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request,"changes has been applied")

            return redirect("book-details",pk=id)
        else:
            messages.error(request,"failed to make changes")
            return render(request,"book-edit",{"form":form})
    

