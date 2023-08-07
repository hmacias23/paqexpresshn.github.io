from flask import Flask, render_template, request, flash
import smtplib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Configura la información de tu cuenta de correo electrónico
EMAIL_ADDRESS = 'paqexpresshn@gmail.com'
EMAIL_PASSWORD = 'jjfjftpmvbkjqkmu'

@app.route('/', methods=['GET', 'POST'])
def contact_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        delivery_experience = request.form['delivery_experience']
        delivery_punctuality = request.form['delivery_punctuality']
        delivery_information = request.form['delivery_information']
        delivery_staff = request.form['delivery_staff']
        package_security = request.form['package_security']
        improvement_suggestions = request.form['improvement_suggestions']
        recommendation = request.form['recommendation']
        negative_experience = request.form['negative_experience']
        negative_details = request.form['negative_details']

        try:
            # Establece la conexión con el servidor de correo electrónico
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()

            # Inicia sesión en tu cuenta de correo
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            # Construye el mensaje del correo electrónico
            subject = f'Nuevo formulario de contacto de {name}'
            body = f'Nombre: {name}\nCorreo: {email}\n\nRespuestas:\n\n' \
                   f'¿Cómo ha sido tu experiencia con la entrega de paquetes?: {delivery_experience}\n' \
                   f'¿Cómo calificarías la puntualidad de las entregas?: {delivery_punctuality}\n' \
                   f'¿La información proporcionada sobre el estado de tus envíos ha sido clara y oportuna?: {delivery_information}\n' \
                   f'¿El personal de entrega ha sido amable y profesional?: {delivery_staff}\n' \
                   f'¿Hemos cumplido con tus expectativas en cuanto a la seguridad de tus paquetes?: {package_security}\n' \
                   f'¿Qué aspectos crees que podríamos mejorar para brindarte una mejor experiencia?: {improvement_suggestions}\n' \
                   f'¿Recomendarías nuestros servicios de paquetería a otras personas?: {recommendation}\n' \
                   f'¿Has tenido una experiencia negativa con nuestros servicios?: {negative_experience}\n\n' \
                   f'¿Si es así, ¿puedes proporcionar más detalles?: \n{negative_details}'
            msg = f'Subject: {subject}\nContent-Type: text/plain; charset=utf-8\n\n{body}'  # Agregamos la codificación UTF-8

            # Envía el correo electrónico
            server.sendmail(EMAIL_ADDRESS, 'support@paqexpress.freshdesk.com', msg.encode('utf-8'))  # Codificamos el mensaje como UTF-8

            flash('Mensaje enviado con éxito!', 'success')
        except Exception as e:
            flash('Error al enviar el mensaje. Por favor, inténtalo de nuevo más tarde.', 'error')
            print(str(e))
        finally:
            # Cierra la conexión con el servidor de correo
            server.quit()

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

