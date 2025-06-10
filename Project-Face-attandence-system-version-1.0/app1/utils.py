import resend

resend.api_key = "re_EsdxwPHY_8ckKVdVmMvWSfNiwqEhuyHaD"

def send_resend_email(to_email, subject, body, from_email="onboarding@resend.dev"):
    try:
        response = resend.Emails.send({
            "from": from_email,
            "to": [to_email],
            "subject": subject,
            "html": f"<pre>{body}</pre>",
        })
        return True
    except Exception as e:
        import logging
        logging.error(f"Resend email error: {e}")
        return False 