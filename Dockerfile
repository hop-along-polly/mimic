FROM python:3.11

ENV ENV=dev

WORKDIR /opt/code-scribes

COPY requirements* .
RUN pip install -r requirements.txt && \
  if [[ $ENV = dev ]]; then \
    pip install -r requirements-dev.txt; \
  fi

COPY testerozza testerozza

EXPOSE 8000

ENTRYPOINT [ "uvicorn", "testerozza.app:app"] 
CMD ["--host", "0.0.0.0", "--port", "8000" ]
