from django.shortcuts import render


def register(request):
    """Simple registration view that accepts name and email and shows a thank-you message.
    This does not persist data — it simply demonstrates a basic form flow.
    """
    context = {}
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        # In a real app you'd validate and save these values.
        context['submitted'] = True
        context['name'] = name or None
        context['email'] = email or None
        context['message'] = message or None
    return render(request, 'register.html', context)
