from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Contact

@csrf_exempt  # Remove this in production and handle CSRF tokens appropriately
def contact_view(request):
    if request.method == 'POST':
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
