from django.shortcuts import render, redirect
from rest_framework import status

from . import forms
from .forms import Form
from .models import RegForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FormSerializers


class FormView(APIView):

    def form_view(request):
        context = {}
        form = Form(request.POST or None)
        if form.is_valid():
            form.save()
            form = Form()

        context['form'] = form
        return render(request, "register_form.html", context)

    def details(request):
        detail = RegForm.objects.all()  # stored as objects
        serializer = FormSerializers(detail, many=True)
        return Response(serializer.data)
        # return render(request, 'details.html', {'form': detail})

    def edit_details(request):
        student_list = RegForm.objects.order_by('First_Name')
        diction = {'title': "Edit Page", 'student_list': student_list}
        return render(request, 'edit_details.html', context=diction)

    def edit_studentlist(request, stud_id):
        stud_info = RegForm.objects.get(pk=stud_id)
        form = forms.Form(instance=stud_info)
        diction = {}

        if request.method == 'POST':
            form = forms.Form(request.POST, instance=stud_info)

            if form.is_valid():
                form.save(commit=True)
                diction.update({'success_text': 'Details Successfully Updated'})

        diction.update({'edit_form': form})
        diction.update({'stud_id': stud_id})
        return render(request, 'edit_studentlist.html', context=diction)

    def delete_details(self,request, stud_id):
        detail = RegForm.objects.get(pk=stud_id).delete()
        diction = {'delete_message': 'Details Deleted Successfully'}
        return render(request, 'edit_details.html', context=diction)

    def get(self,request):
        detail = RegForm.objects.all()  # stored as objects
        serializer = FormSerializers(detail, many=True)
        return Response(serializer.data)
        # return render(request, 'details.html', {'form': detail})

    def post(self, request):
        serializer = FormSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
