import qrcode
from io import BytesIO
import base64

def generar_qr_base64(texto: str) -> str:
    """
    Genera un QR con el texto indicado y lo devuelve como imagen en base64.
    Ideal para enviar al frontend sin guardar archivos.
    """
    qr = qrcode.QRCode(version=1, box_size=10, border=2)
    qr.add_data(texto)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
