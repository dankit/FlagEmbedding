FROM pytorch/pytorch:2.8.0-cuda12.8-cudnn9-devel
WORKDIR /app
COPY setup.py ./
RUN pip install --upgrade pip && pip install .[finetune]
COPY . .

RUN chmod +x /app/base.sh

CMD ["bash", "/app/base.sh"]