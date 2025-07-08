import qrcode
from io import BytesIO
import base64

def generar_qr_base64(texto: str) -> str:
    """
    Genera un código QR en formato imagen, lo codifica en base64 y lo devuelve como string.

    Args:
        texto (str): Texto que se desea codificar en el QR.

    Returns:
        str: Imagen en base64 lista para enviar al frontend o embeber en HTML.
    """
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    qr_base64 = base64.b64encode(img_bytes).decode("utf-8")

    return qr_base64
