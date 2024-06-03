FROM condaforge/mambaforge:24.1.2-0

RUN mamba install -c conda-forge \
    django \
    numpy \
    pandas \
    matplotlib \
    sqlalchemy \
    pgspecial=1 \
    django-extensions \
    jupysql \
    psycopg2-binary=2.9.3 \
    jupyterlab --yes

ENV PGSERVICEFILE=/Session21/Day2/docker/.pg_service.conf
ENV PGPASSFILE=/Session21/Day2/docker/.pgpass

COPY kernel.json /opt/conda/share/jupyter/kernels/python3/kernel.json
ENV DJANGO_ALLOW_ASYNC_UNSAFE="true"

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]
