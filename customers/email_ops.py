# email_ops.py
# Path: appointment/utils/email_ops.py

"""
Author: Adams Pierre David
Since: 1.1.0
"""

import datetime

from django.conf import settings
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.utils.translation import gettext as _

from appointment import messages_ as email_messages
from appointment.email_sender import notify_admin, send_email
from appointment.logger_config import get_logger
from appointment.models import AppointmentRequest, EmailVerificationCode, PasswordResetToken
from appointment.settings import APPOINTMENT_PAYMENT_URL
from appointment.utils.date_time import convert_24_hour_time_to_12_hour_time
from appointment.utils.db_helpers import get_absolute_url_, get_website_name

from customers.models import Inquiry

logger = get_logger(__name__)

def send_inquiry_email(inquiry: Inquiry, email: str, request):
    """Send a thank-you email to the client for booking an appointment.

    :param ar: The appointment request associated with the booking.
    :param user: The user who booked the appointment.
    :param email: The email address of the client.
    :param appointment_details: Additional details about the appointment (default None).
    :param account_details: Additional details about the account (default None).
    :param request: The request object.
    :return: None
    """
    # Month and year like "J A N 2 0 2 1"
    month_year = inquiry.create_date.strftime("%b %Y").upper()
    day = inquiry.create_date.strftime("%d")

    relative_detail_url = reverse('customers:detail', args=[inquiry.inquiry_id])
    detail_link = get_absolute_url_(relative_detail_url, request)

    email_context = {
        'first_name': inquiry.customer.name,
        'current_year': datetime.datetime.now().year,
        'company': get_website_name(),
        'month_year': month_year,
        'day': day,
        'detail_url': detail_link,
        'main_title': _("We have gotten your inquiry."),
        'message_1': _("""We've gotten your inquiry! We will send another email when our mechanic needs to follow up with you or approves 
                       an appointment for you.""")
    }
    send_email(
            recipient_list=[email], subject=_("Thank you for inquiring with us."),
            template_url='customers/inquiry_email.html', context=email_context
    )

def notify_admin_about_inquiry(inquiry, client_name: str):
    """Notify the admin and the staff member about a new appointment request."""
    logger.info(f"Sending admin notification for new inquiry {inquiry.id}")
    email_context = {
        'client_name': client_name,
        'inquiry': inquiry
    }

    subject = _("New Inquiry Request for ") + client_name
    notify_admin(subject=subject, template_url='customers/admin_inquiry_email.html', context=email_context)