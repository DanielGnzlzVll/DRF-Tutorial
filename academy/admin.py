# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Topic, Course, Document


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'topic',
        'name',
        'abstract',
        'created_date',
        'updated_date',
    )
    list_filter = ('topic', 'created_date', 'updated_date')
    search_fields = ('name',)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'course',
        'name',
        'file',
        'created_date',
        'updated_date',
    )
    list_filter = ('course', 'created_date', 'updated_date')
    search_fields = ('name',)
