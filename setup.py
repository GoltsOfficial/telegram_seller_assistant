from setuptools import setup, find_packages

setup(
    name="telegram-bot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aiogram==3.1.1",
        "python-dotenv==1.0.0",
        "aiohttp==3.8.5"
    ],
    python_requires=">=3.8",
)