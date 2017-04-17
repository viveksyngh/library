from django.shortcuts import render
from django.views.generic import View
from django.http.request import QueryDict
from models import *
from library.response import send_200, send_400, send_201, send_404

# Create your views here.

class BookListView(View):

    def __init__(self):
        self.response = {"message": '',
                        "result": {}
                        }

    def dispatch(self, request, *args, **kwargs):
        return super(BookListView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        
        books = Book.objects.get_all_books()
        book_list = []
        for book in books:
            book_list.append(book.serializer())
        self.response = {"message" : "Success"}
        self.response["result"] = book_list
        return send_200(self.response)
    
    def post(self, request):
        book_name = request.POST.get('book_name')
        category = request.POST.get('category')
        if not book_name or not category:
            self.response["message"] = "Failure"
            return send_400(self.response)
        if category not in [cat[0] for cat in Book.category_choices]:
            self.response["message"] = "Failure !! Invalid category."
            return send_400(self.response)
        book = Book.objects.create_book(book_name, category)
        self.response["message"] = "Success"
        self.response["result"] = book.serializer()
        return send_201(self.response)


class BookView(View):
    def __init__(self):
        self.response = {"message": '',
                        "result": {}
                        }

    def dispatch(self, request, *args, **kwargs):
        return super(BookView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist, e:
            self.response["message"] = "Failure !! Book not found!"
            return send_404(self.response)
        else:
            self.response["message"] = "Success"
            self.response["result"] = book.serializer()
            return send_200(self.response)
        
    def put(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist, e:
            self.response["message"] = "Failure !! Book not found!"
            return send_404(self.response)
        else:
            request_data = QueryDict(request.body)
            book_name = request_data.get('book_name')
            category = request_data.get('category')
            if category and category not in [cat[0] for cat in Book.category_choices]:
                self.response["message"] = "Failure !! Invalid category."
                send_400(self.response)
            if book_name:
                book.book_name = book_name
            if category:
                book.category = category
            book.save()
            self.response["message"] = "Sucess"
            self.response["result"] = book.serializer()
            return send_200(self.response)
    
    def delete(self, request, book_id):
        try:
            book = Book.objects.get(pk=book_id)
        except Book.DoesNotExist, e:
            self.response["message"] = "Failure !! Book not found!"
            return send_404(self.response)
        else:
            book.is_active = False
            book.save()
        self.response["message"] = "Success"
        return send_200(self.response)


class MemberListView(View):

    def __init__(self):
        self.response = {"message": '',
                        "result": {}
                        }

    def dispatch(self, request, *args, **kwargs):
        return super(MemberListView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        members = Member.objects.get_all_members()
        member_list = []
        for member in members:
            member_list.append(member.serializer())
        self.response = {"message" : "Success"}
        self.response["result"] = member_list
        return send_200(self.response)
    
    def post(self, request):
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name', '')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        if not first_name or not last_name or not email:
            self.response["message"] = "Failure"
            return send_400(self.response)
        member = Member.objects.create_member(first_name, middle_name, last_name, email)
        self.response["message"] = "Success"
        self.response["result"] = member.serializer()
        return send_201(self.response)


class MemberView(View):
    def __init__(self):
        self.response = {"message": '',
                        "result": {}
                        }

    def dispatch(self, request, *args, **kwargs):
        return super(MemberView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request, member_id):
        try:
            member = Member.objects.get(pk=member_id)
        except Member.DoesNotExist, e:
            self.response["message"] = "Failure !! Book not found!"
            return send_404(self.response)
        else:
            self.response["message"] = "Success"
            self.response["result"] = member.serializer()
            return send_200(self.response)
        
    def put(self, request, member_id):
        try:
            member = Member.objects.get(pk=member_id)
        except Member.DoesNotExist, e:
            self.response["message"] = "Failure !! Book not found!"
            return send_404(self.response)
        else:
            request_data = QueryDict(request.body)
            first_name = request_data.get('first_name')
            last_name = request_data.get('last_name')
            middle_name = request_data.get('middle_name')
            email = request_data.get('email')
            if first_name:
                member.first_name = first_name
            if last_name:
                member.last_name = last_name
            if middle_name:
                member.middle_name = middle_name
            if email:
                member.email = email
            member.save()
            self.response["message"] = "Sucess"
            self.response["result"] = member.serializer()
            return send_200(self.response)
    
    def delete(self, request, member_id):
        try:
            member = Member.objects.get(pk=member_id)
        except Member.DoesNotExist, e:
            self.response["message"] = "Failure !! Book not found!"
            return send_404(self.response)
        else:
            member.is_active = False
            member.save()
        self.response["message"] = "Success"
        return send_200(self.response)


class IssueListView(View):

    def __init__(self):
        self.response = {"message": '',
                        "result": {}
                        }

    def dispatch(self, request, *args, **kwargs):
        return super(IssueListView, self).dispatch(request, *args, **kwargs)
    
    def get(self, request):
        issues = Issue.objects.select_related('book', 'm    ember').all().filter(is_active=True)
        issue_list = []
        for issue in issues:
            issue_list.append(issue.serializer())
        self.response = {"message" : "Success"}
        self.response["result"] = issue_list
        return send_200(self.response)


class IssueView(View):
    def __init__(self):
        self.response = {"message": '',
                        "result": {}
                        }
    
    def dispatch(self, request, *args, **kwargs):
        return super(IssueView, self).dispatch(request, *args, **kwargs)

    def post(self, request, book_id, member_id):
        try:
            book = Book.objects.get(pk=book_id, is_active=True)
            member = Member.objects.get(pk=member_id, is_active=True)
        except Book.DoesNotExist, e:
            self.response["message"] = "Failure! Invalid Book."
            return send_400(self.response)
        except Member.DoesNotExist, e:
            self.response["message"] = "Failure! Invalid Member."
            return send_400(self.response)
        else:
            issue = Issue.objects.create(member=member, book=book)
            self.response["message"] = "Success"
            self.response["result"] = issue.serializer()
        return send_201(self.response)