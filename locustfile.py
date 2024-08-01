from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time=between(1,2)
    @task
    def index(self):
        # Cargar la página principal
        response=self.client.get("http://wordpress1:80")

    @task
    def submit_form(self):
        # Enviar el formulario con los campos de nombre, correo electrónico, número de teléfono y mensaje
        response=self.client.post("http://wordpress1:80", {
            "name-1": "John Doe",
            "email-1": "john.doe@example.com",
            "phone-1": "1234567890",
            "textarea-1": "This is a test message."
        })

