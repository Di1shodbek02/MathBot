FROM python:3.11-alpine
WORKDIR aps/
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt
RUN sed -i 's/\r$//g' /aps/entrypoint.sh
RUN chmod +x /aps/entrypoint.sh
ENTRYPOINT ["/aps/entrypoint.sh"]