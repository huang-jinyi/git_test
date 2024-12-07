import os
from dotenv import load_dotenv

def main():
    load_dotenv() #加载环境变量

    # 访问环境变量
    database_url = os.getenv('DATABASE_URL')
    secret_key = os.getenv('SECRET_KEY')
    debug_mode = os.getenv('DEBUG')

    print(database_url)
    print(secret_key)
    print(debug_mode)



if __name__ == "__main__":
    main()