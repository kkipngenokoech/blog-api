# CORS - CROSS ORIGIN RESOURCE SHARING

It is a security feature implemented in web browsers to restrict access to resources (such as fonts, images, videos, and scripts) across different domains.

When a web page tries to access a resource from a different domain, the browser sends a CORS request to the server hosting that resource. The server then responds with a set of headers indicating whether the request is allowed or not. If the server approves the request, the browser is allowed to access the resource and display it on the page.

As for django, we are going to use a third party package django-cors-headers to help us deal with CORS requests

## django-cors-headers

this is a django cors headers is a python/django package that provides middleware for handling CORS in django web applications.

The django-cors-headers package helps to handle CORS requests in Django by allowing or blocking requests from different origins (domains).

