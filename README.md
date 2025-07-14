
```markdown
# 🚍 WiFi Bus WIOO – Backend Técnico

Sistema de validación de acceso a WiFi para pasajeros de transporte público. Diseñado con FastAPI, modularizado y seguro, compatible con estándares bancarios y listo para escalar en rutas urbanas.

---

## ⚙️ Estructura técnica (FastAPI)

- Carpeta `models/` con entidades: `ticket.py`, `comprobante.py`, `usuario.py`, etc.
- Carpeta `schemas/` con validadores estrictos (`constr()`, `EmailStr`, separación `Request`/`Response`)
- Carpetas `services/` y `routers/` separadas por funcionalidad (IP, usuario, tickets, publicidad, estadísticas)
- Carpeta `utils/` con funciones especializadas (QR base64, IP pública, token JWT)
- Seguridad en `core/security.py` + configuración central en `config/settings.py`
- Variables protegidas en `.env` con claves, tiempos de expiración y credenciales externas

---

## 🔐 Seguridad avanzada

- Tokens JWT con expiración automática y firma segura desde `.env`
- Validación activa por rol (`admin`, `chofer`) en rutas protegidas
- Sanitización de entradas con `constr(strip_whitespace=True)`
- Función `verificar_token()` integrada en routers privados
- Preparado para auditorías y revisión institucional

---

## 🎟️ Sistema de tickets (efectivo)

- Generación de código con duración configurada (`ticket_service.py`)
- Visualización opcional como QR en base64
- Validación automática por IP con redireccionamiento
- Preparado para integración con mini app del chófer

---

## 🧑‍💼 Mini app del chófer

- Lógica de login y generación de tickets estructurada
- Compatible con interfaz ligera web o Progressive Web App (PWA)
- Seguridad con JWT y control por rol

---

## 📡 Servicios incluidos (`services/`)

- `validar_service.py`: Verifica ticket o comprobante
- `redireccionar_service.py`: Decide si se navega o no
- `verificar_pago_service.py`: Comprobantes bancarios
- `publicidad_service.py`: Muestra anuncios por hora/zona/IP
- `estadisticas_service.py`: Métricas por método/fecha/ruta
- `usuario_service.py`: Manejo de login y perfiles

---

## 📊 Flujo técnico completo

```plaintext
IP pública → Validación de método → Redirección → Acceso WiFi
```

- Frontend detecta IP (`/mi-ip`)
- Usuario elige método de validación
- Formulario envía datos → backend evalúa → navegación autorizada o rechazada

---

## 📍 Escalabilidad y despliegue

- Compatible con MikroTik: captura IP, evalúa, autoriza acceso
- Preparado para control de ancho de banda y Queue por IP
- Integrable con panel administrativo para logs, métricas y exportación
- Certificados HTTPS previstos con Let’s Encrypt
- Subida prevista a VPS, Render o Railway

---

## 📜 Legal y operatividad

- Política de privacidad visible para usuarios
- Manual técnico para conductores y administradores
- Pruebas funcionales vía Postman + documentación Swagger
- Preparado para registro legal como C.A. y presentación ante inversores

---

## 🧩 Checklist técnico

- [x] Carpeta `models/` completada
- [x] Carpeta `schemas/` validada y lista
- [x] Lógica por entidad en `services/`
- [x] Seguridad por JWT (`security.py`, `settings.py`)
- [x] Eliminación de archivos obsoletos
- [x] Flujo completo desde IP → Validación → Redirección
- [x] Publicidad y estadísticas implementadas
- [ ] Rutas protegidas según rol (admin/chofer)
- [ ] Panel administrativo con exportación
- [ ] Pruebas unitarias en carpeta `tests/`
- [ ] Documentación final en Postman + Swagger

---

## 🚦 Estado actual

- Backend funcional y modularizado ✅
- Seguridad avanzada por JWT ✅
- Integración con frontend e IP pública ✅
- Panel y despliegue en progreso 🟡
- Preparado para operar en buses reales y escalar 🌐

---

## 👨‍💼 Autor

Desarrollado por [Wioo C.A] — emprendedor digital con visión técnica, profesional y estratégica para soluciones urbanas en conectividad y validación móvil.
