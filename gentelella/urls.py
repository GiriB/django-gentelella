from django.conf.urls import url
from django.shortcuts import render


urlpatterns = [
    url(r'^(?P<template_name>.*\.html)', render),
    url(r'^$', render, kwargs=dict(template_name='gentelella/index.html')),
]
