from django.shortcuts import render

# Create your views here.
def aboutMe(request):
    return render(request,"index.html")

def education(request):
    return render(request,"edu.html")

def contact(request):
    context = {}

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        context = {
            "thank_you" : f"Thank you {name}, your message has been received!"
        }
    return render(request,"contact.html", context)