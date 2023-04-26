# blog-api

a Blog API using the full set of Django REST Framework features. It will have users, permissions, and allow for full CRUD (Create-Read-Update-Delete) functionality.

## api endpoints

we don't normally write a lot of code when using django rest_framework, all we just have to do is to update the views.py class . that is what we are passing to the class method.


the magic lies in the `rest_framework.generics` it has all the functions.

## rest_framework.generics

this is a module provided by django rest framework that contains a set of reusable views and mixins that can be quickly used to create commonly used API views.

### ListAPIView

a read-only view for listing a queryset of objects

### CreateAPIView

A view for creating a new object

### RetrieveAPIView

this is used to retrieve an object using an id

### UpdateAPIView

a view for updating an existing object

### DeleteAPIView

a view for deleting an object

### ListCreateAPIView

A view that supports both listing a queryset of objects and creating a new object in the same file.

### RetrieveUpdateAPIView

A view that supports both retrieving a single object by its IDs and deleting the object in the same way

### RetrieveDestroyAPIView

A  view that supports both retrieving a single object and deleting the object in the same view.

### RetrieveUpdateDestroyAPIView

A view that supports retrieving a single object by its ID, updating the object, and deleting the object in the same view.



Additionally, rest_framework.generics provides mixins that can be used to customize the behavior of these views, such as filtering, pagination, and authentication.