FROM python:3
ARG name_creator
ARG created_date

LABEL maintainer=$name_creator

RUN pip install Flask
RUN pip install pytz


COPY . /


ENV DATE_CREATED=$created_date
ENV NAME_CREATOR=$name_creator


EXPOSE 5000

CMD ["python3", "app.py"]
