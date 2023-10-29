from pathlib import Path

import uvicorn
from fastapi import FastAPI, BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
# from typing import List
from  jwt_na_fast_api.conf.config import  settings


class EmailSchema(BaseModel):
    email: EmailStr



conf = ConnectionConfig(
    MAIL_USERNAME=  settings.mail_username,
    MAIL_PASSWORD= settings.mail_password,
    MAIL_FROM= settings.mail_from,
    MAIL_PORT=settings.mail_port,
    MAIL_SERVER=settings.mail_server,
    MAIL_FROM_NAME="Anton for homework",
    MAIL_STARTTLS=False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
    TEMPLATE_FOLDER=Path(__file__).parent / 'templates',
)

app = FastAPI()



@app.post("/send-email")
async def send_in_background(background_tasks: BackgroundTasks, body: EmailSchema):
    message = MessageSchema(
        subject="This is a very important message",
        recipients=[body.email],
        template_body={"fullname": "My Friend",},
        subtype=MessageType.html
    )

    fm = FastMail(conf)

    background_tasks.add_task(fm.send_message, message, template_name="example_email.html")

    return {"message": "email has been sent"}


if __name__ == '__main__':
    uvicorn.run('mail_togo:app', port=8000, reload=True)
