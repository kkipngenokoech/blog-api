# customer user model

### [model description](./accounts/models.py)

we are going to create a custom user model that extends django.contrib.auth.models AbstractUser

## django.contrib.auth.models

The django.contrib.auth.models path is an essential part of Django's built-in authentication system, providing models and functionality for user authentication, permissions, groups, and user profiles.

this is a module in django that provides the models for user authentication and authorization

this module provides a couple of models:

1. User  - This  model represents a user account and stores information such as username and password, email. it also includes authentication, password management and user permissions methods.
2. Group - This model represents a user group which is used to manage user permissions and assign permissions as a group
3. Permission - This model represents a user permission that can be granted to a user
4. AbstractUser - This model represents a base class that provides a customizeable user model. it includes fields such as username, email and password as well as customizable  fields for addtional data
5. AbstractBaseUser - This model represents another base class that provides a more customized user model, it includes fields such as username(custom username field), email and password.
6. PermissionMixin - This is a mixin class that can be used to add permissions to custom user models it includes fields for permissions and methods for checking permissions
7. BaseUserManager - This is a base class that for custom user managers which are used to customize the creation of and management of user accounts

One of the most significant advantages of using the django.contrib.auth.models path is that it is highly customizable. Developers can extend the User model to include additional fields or functionality, or they can create custom authentication backends to authenticate users against custom data sources.

Another advantage of using the built-in authentication system in Django is that it integrates well with other Django modules and functionality, such as the admin site, forms, and templates.

 the django.contrib.auth.models path in Django provides a solid foundation for user authentication and authorization in Django applications. Its comprehensive set of models and functionality allow developers to easily implement user management features, such as permissions, groups, and user profiles, while its customizable nature allows for flexibility and extensibility.

By using the django.contrib.auth.models path, developers can ensure that their Django applications have a reliable and secure authentication system that integrates well with other Django modules and functionality. With its ease of use and flexibility, the built-in authentication system in Django can save developers time and effort in implementing user authentication and authorization features, enabling them to focus on building other core features of their application.

