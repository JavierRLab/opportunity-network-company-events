FROM python:3.9
ENV PYTHONUNBUFFERED 1

# Clone ONLY the /backend folder (see: https://stackoverflow.com/a/52269934)
# RUN git clone --depth 1 --filter=blob:none --sparse https://github.com/JavierRLab/opportunity-network-company-events.git /company-events
# RUN cd /company-events
# RUN git sparse-checkout set backend
WORKDIR /code

# alternative for private repos?
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . /code/

RUN ls .