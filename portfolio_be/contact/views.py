from django.core.validators import validate_email
from django.core.exceptions import ValidationError
import bleach
from django.http import JsonResponse
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from .models import Contact

@ensure_csrf_cookie
def get_csrf(request):
    return JsonResponse({'message': 'CSRF cookie set'})

def contact_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        # Validate and sanitize name
        name = bleach.clean(data.get('name', '').strip())
        if not name or len(name) > 100:
            return JsonResponse({'error': 'Invalid name'}, status=400)

        # Validate and sanitize email
        email = data.get('email', '').strip()
        try:
            validate_email(email)
        except ValidationError:
            return JsonResponse({'error': 'Invalid email'}, status=400)

        # Validate and sanitize message
        message = bleach.clean(data.get('message', '').strip())
        if not message or len(message) > 500:
            return JsonResponse({'error': 'Invalid message'}, status=400)

        # Process the sanitized data (e.g., save to database, send email)
        # return JsonResponse({'message': 'Your message has been sent successfully!'})
        try:
            # Parse the JSON data from the request body
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')

            # Create a new Contact instance and save it to the database
            contact = Contact.objects.create(name=name, email=email, message=message)

            # Return a 201 Created response with the saved contact's ID
            return JsonResponse(
                {'message': 'Contact saved successfully', 'contact_id': contact.id},
                status=201
            )
        except (json.JSONDecodeError, KeyError) as e:
            return JsonResponse(
                {'error': 'Invalid data', 'detail': str(e)},
                status=400
            )
    else:
        # If the method is not POST, return an error
        return JsonResponse({'error': 'Method not allowed'}, status=405)
