from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Passenger, Driver, Admin
import json
from django.views.decorators.csrf import csrf_exempt

@require_http_methods(["GET"])
def hello(request):
    return JsonResponse({
        'message': 'Hello! Welcome to XDriver API',
        'status': 'Server is running'
    }, status=200)





@csrf_exempt
@require_http_methods(["POST"])
def sign_up(request):
    try:
        data = json.loads(request.body)
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        password_confirm = data.get('password_confirm')
        phone_number = data.get('phone_number')
        user_type = data.get('user_type', 'passenger')  # 'passenger', 'driver', or 'admin'
        
        # Validate required fields
        if not all([first_name, last_name, email, password, password_confirm, phone_number]):
            return JsonResponse({'error': 'All fields are required'}, status=400)
        
        # Validate password match
        if password != password_confirm:
            return JsonResponse({'error': 'Passwords do not match'}, status=400)
        
        # Validate password strength
        if len(password) < 6:
            return JsonResponse({'error': 'Password must be at least 6 characters'}, status=400)
        
        # Check email uniqueness across all user types
        if Passenger.objects.filter(email=email).exists() or \
           Driver.objects.filter(email=email).exists() or \
           Admin.objects.filter(email=email).exists():
            return JsonResponse({'error': 'Email already exists'}, status=400)
        
        # Validate user_type
        if user_type not in ['passenger', 'driver', 'admin']:
            return JsonResponse({'error': 'Invalid user type'}, status=400)
        
        # Create user based on type
        hashed_password = make_password(password)
        
        if user_type == 'passenger':
            user = Passenger.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password,
                phone_number=phone_number,
                avg_rating=5.0
            )
        elif user_type == 'driver':
            vehicle_info = data.get('vehicle_info', '')
            user = Driver.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password,
                phone_number=phone_number,
                avg_rating=5.0,
                vehicle_info=vehicle_info,
                number_of_rides=0
            )
        else:  # admin
            user = Admin.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=hashed_password,
                phone_number=phone_number
            )
        
        return JsonResponse({
            'success': f'{user_type.capitalize()} registered successfully',
            'user_id': user.id,
            'user_type': user_type
        }, status=201)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)


@csrf_exempt  
@require_http_methods(["POST"])
def sign_in(request):
    try:
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        
        if not all([email, password]):
            return JsonResponse({'error': 'Email and password are required'}, status=400)
        
        # Check Passenger
        user = Passenger.objects.filter(email=email).first()
        user_type = 'passenger'
        
        # Check Driver if not found
        if not user:
            user = Driver.objects.filter(email=email).first()
            user_type = 'driver'
        
        # Check Admin if not found
        if not user:
            user = Admin.objects.filter(email=email).first()
            user_type = 'admin'
        
        # Verify password
        if user and check_password(password, user.password):
            return JsonResponse({
                'success': 'Login successful',
                'user_id': user.id,
                'user_type': user_type,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email
            }, status=200)
        else:
            return JsonResponse({'error': 'Invalid email or password'}, status=401)
    
    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON'}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)




@csrf_exempt  
@require_http_methods(["POST"])
def sign_out(request):
   
    try:
        return JsonResponse({'success': 'Logout successful'}, status=200)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)