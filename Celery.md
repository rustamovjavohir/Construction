# This is a README file for the Celery services
- celery -A your-application worker -l info --concurrency 8 -P eventlet # Celery 4 dan kattasini windowsga moslashtirish
- celery -A your-application worker -l info --pool=solo # Celery ni Windows bilan integratsiya qilishda worker ni ishga tushuradi
- celery -A your-application beat -l info # Periodic(davriy) tasklarni ishga tushuradi
- celery -A your-application flower --port=5001 # flowerni ishga tushurish
- celery -A your-application beat # beat(davriy) Mavjud schedule orqali ishga tushirish