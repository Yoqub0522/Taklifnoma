from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import GuestResponse, WeddingSong
import json
from datetime import datetime


def invitation_page(request):
    # Faol qo'shiqlarni olish
    songs = WeddingSong.objects.filter(is_active=True)

    context = {
        'songs': songs,
    }
    return render(request, 'invitation.html', context)


def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('/admin/login/')

    responses = GuestResponse.objects.all()
    total_responses = responses.count()
    attending = responses.filter(attendance='yes').count()
    not_attending = responses.filter(attendance='no').count()
    total_guests = sum(response.guests_count for response in responses)

    context = {
        'responses': responses,
        'total_responses': total_responses,
        'attending': attending,
        'not_attending': not_attending,
        'total_guests': total_guests,
    }
    return render(request, 'admin_dashboard.html', context)


@csrf_exempt
def save_response(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            response = GuestResponse(
                name=data.get('name'),
                guests_count=int(data.get('guests', 1)),
                attendance=data.get('attendance'),
                phone=data.get('phone', ''),
                message=data.get('message', '')
            )
            response.save()

            return JsonResponse({'status': 'success', 'message': 'Javobingiz qabul qilindi!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)})

    return JsonResponse({'status': 'error', 'message': 'Faqat POST so\'rovi qabul qilinadi'})


def get_responses_stats(request):
    if not request.user.is_staff:
        return JsonResponse({'error': 'Ruxsat yo\'q'})

    responses = GuestResponse.objects.all()
    stats = {
        'total': responses.count(),
        'attending': responses.filter(attendance='yes').count(),
        'not_attending': responses.filter(attendance='no').count(),
        'total_guests': sum(r.guests_count for r in responses)
    }

    return JsonResponse(stats)