FROM condaforge/mambaforge:24.1.2-0

RUN mamba install -c conda-forge \
    django \
    numpy \
    pandas \
    matplotlib \
    sqlalchemy \
    pymongo \
    pgspecial=1 \
    django-extensions \
    jupysql \
    psycopg2-binary=2.9.3 \
    jupyterlab --yes

CMD ["jupyter-lab","--ip=0.0.0.0","--no-browser","--allow-root"]
