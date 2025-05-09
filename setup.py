from setuptools import setup, find_packages

setup(
    name='nunchaku',
    version='0.2.0+torch2.5',
    description='',
    packages=find_packages(),
    python_requires='>=3.10',
    install_requires=[
        'diffusers>=0.32.2',
        'transformers',
        'accelerate',
        'sentencepiece',
        'protobuf',
        'huggingface-hub',
    ],
    license_files=['LICENCE.txt'],
    include_package_data=True,
    package_data={
        'nunchaku': ['*.so', '**/*.py', '**/*.so'],  # 必要ならワイルドカードで細かく指定
    },
)