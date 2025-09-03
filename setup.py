from setuptools import setup, find_packages

setup(
    name='FlagEmbedding',
    version='1.3.5',
    description='FlagEmbedding',
    author_email='2906698981@qq.com',
    url='https://github.com/FlagOpen/FlagEmbedding',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'torch>=1.6.0',
        'transformers>=4.44.2',
        'datasets>=2.19.0',
        'accelerate>=0.20.1',
        'sentence_transformers',
        'peft',
        'ir-datasets',
        'sentencepiece',
        'protobuf'
    ],
    extras_require={
        'finetune': ['deepspeed', 'flash-attn'],
    },
)
