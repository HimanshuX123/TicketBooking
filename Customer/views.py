from django.http import HttpResponse
from django.shortcuts import render
from .form import PassengerRegistration
from TicketBooking import settings
from .models import Passenger
import datetime
from django.core.mail import send_mail


def booking(request):
    if request.method == 'POST':
        fm = PassengerRegistration(request.POST)
        if fm.is_valid():

            fn = fm.cleaned_data['full_name']
            gen = fm.cleaned_data['gender']
            ag = fm.cleaned_data['age']
            ad = fm.cleaned_data['address']
            em = fm.cleaned_data['email']  # User's email
            co = fm.cleaned_data['contact_number']
            src = fm.cleaned_data['source_station']
            dest = fm.cleaned_data['destination_station']
            doj = fm.cleaned_data['date_of_journey']

            # Save passenger details to the database
            reg = Passenger(full_name=fn, gender=gen, age=ag, address=ad, email=em,
                            contact_number=co, source_station=src,
                            destination_station=dest, date_of_journey=doj)
            reg.save()

            subject = "Your Ticket Booking Confirmation"
            message = f"Dear {fn},\n\nYour ticket has been successfully booked.\n\n" \
                      f"Travel Details:\nSource: {src}\nDestination: {dest}\n" \
                      f"Date of Journey: {doj}\n\nThank you for choosing us!"
            email = settings.EMAIL_HOST_USER
            recipient_list = [em]

            send_mail(subject, message, email, recipient_list)

            return HttpResponse("""
                <h2>Booking Successful!</h2>
                <p>A confirmation email has been sent to your email address.</p>
                <nav>
                    <ul>
                        <li><a href='/'>Home</a></li>
                        <li><a href='/about/'>About Us</a></li>
                        <li><a href='/booking/'>Book Another Ticket</a></li>
                        <li><a href='/contact/'>Contact Us</a></li>
                    </ul>
                </nav>
            """)

        else:
            return HttpResponse("Form is invalid. Please check the details and try again.")

    else:
        fm = PassengerRegistration()

    return render(request, 'booking.html', {'form': fm})


def home(request):
    return render(request, 'Homepage.html')


def about(request):
    return render(request, 'Aboutus.html')


def cont(request):
    return render(request, 'Contact.html')


def hi(request):
    return render(request, 'Home.html')


def time():
    now = datetime.datetime.now()
    return HttpResponse("booking.html")


def index(request):
    return render(request, "mail.html", {"message": ""})


def mail(request):
    global user_email, message
    if request.method == "POST":
        user_email = request.POST.get('email')
        user_name = request.POST.get('full_name')
        message = request.POST.get('message')
    subject = "Greetings"
    msg = message
    to = user_email
    res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])
    if res == 1:
        msg = "mail sent successfully"
    else:
        msg = "not sent"

    return HttpResponse(msg)
