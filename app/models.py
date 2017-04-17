from __future__ import unicode_literals

from django.db import models

# Create your models here.

class BookManager(models.Manager):

    def get_all_books(self):
        books = self.all().filter(is_active=True)
        return books
    
    def create_book(self, book_name, category):
        book = self.create(book_name=book_name, category=category)
        return book


class Book(models.Model):
    category_choices = (('Fiction', 'Fiction'),
                        ('Thriller', 'Thriller'),
                        ('Comedy', 'Comedy'))
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    category = models.CharField(max_length=255, choices=())
    is_active = models.BooleanField(default=True)

    objects = BookManager()

    def __str__(self):
        return str(self.book_id) + ' ' + str(self.book_name)
    
    def serializer(self):
        data = {}
        data['book_id'] = self.book_id
        data['book_name'] = self.book_name
        data['category'] = self.category
        return data

class MemberManager(models.Manager):

    def get_all_members(self):
        books = self.all().filter(is_active=True)
        return books

    def create_member(self, first_name, middle_name, last_name, email):
        member = self.create(first_name=first_name, 
                            middle_name=middle_name,
                            last_name=last_name,
                            email=email)
        return member


class Member(models.Model):
    member_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, default='', blank=True)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    objects = MemberManager()

    def get_full_name(self):
        name = self.first_name + ' '
        if self.middle_name :
            name += self.middle_name + ' '
        name += self.last_name
        return name
    
    def __str__(self):
        return str(self.member_id) + ' ' + str(self.first_name) + ' ' + str(self.last_name)
    
    def serializer(self):
        data = {}
        data['member_id'] = self.member_id
        data['first_name'] = self.first_name
        data['last_name'] = self.last_name
        data['middle_name'] = self.middle_name
        data['email'] = self.email
        return data


class Issue(models.Model):
    issue_id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member)
    book = models.ForeignKey(Book)
    issued_on = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.issue_id
    
    def serializer(self):
        data = {}
        data['member'] = self.member.serializer()
        data['book'] = self.book.serializer()
        data['issue_id'] = self.issue_id
        data['issued_on'] = str(self.issued_on)
        return data

