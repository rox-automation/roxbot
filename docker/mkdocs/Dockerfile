# mkdocs-material with latest release
FROM python:3-slim

# install python packages
COPY requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt && rm /requirements.txt

# copy example docs
ADD test_docs /docs
#RUN chown -R $USERNAME:$USERNAME /docs

RUN echo mkdocs >> /build_date.txt && \
    date >> /build_date.txt

WORKDIR /docs

CMD mkdocs  serve -a 0.0.0.0:8000
