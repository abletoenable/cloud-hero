import boto3

# Yandex Objext Storage Access
os = boto3.client(
    's3',
    aws_access_key_id = 'YANDEX_CLOUD_ACCESS_KEY',
    aws_secret_access_key = 'YANDEX_CLOUD_SECRET_ACCESS_KEY',
    region_name = 'ru-central1',
    endpoint_url = 'https://storage.yandexcloud.net'
)

#print(os.list_buckets())
#print(os.list_objects(Bucket=bucket_name))

# Перечень корзин
def ls():
    for bucket in os.list_buckets()['Buckets']:
        print(bucket['Name'])

# Перечень объектов в корзине
def keys(bucket_name):
    for key in os.list_objects(Bucket=bucket_name)['Contents']:
        print(key['Key'])

# Создание корзины
def mb(bucket_name):
    os.create_bucket(Bucket = bucket_name)

# Запись объекта в корзину
def upload(bucket_name, object_name):
    os.upload_file(object_name, bucket_name, object_name)

# Удалить объект из корзины
def delete(bucket_name, object_name):
    os.delete_object(Bucket=bucket_name, Key=object_name)

# Загрузить объект из корзины
def download(bucket_name, object_name):
    os.download_file(bucket_name, object_name, object_name)
