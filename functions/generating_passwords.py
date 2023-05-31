import pyotp

secret_key = pyotp.random_base32()

    # Generate a QR code URL
url = pyotp.totp.TOTP(secret_key).provisioning_uri('hello', issuer_name="name")
