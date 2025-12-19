from setuptools import find_packages, setup

setup(
    name="awesomelights",
    version="1.0.0",  # 必须与 awesomelights/__init__.py 中的版本保持一致
    packages=find_packages(),
    description="A simulated library for AwesomeLights Home Assistant integration.",
    install_requires=[],  # 如果您的库有其他 PyPI 依赖，在这里列出
    long_description="A placeholder library.",
    url="http://your-project-url.com",
)
