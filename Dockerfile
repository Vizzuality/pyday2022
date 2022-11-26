FROM mambaorg/micromamba:0.27.0 AS base

COPY --chown=$MAMBA_USER:$MAMBA_USER environment.yml /tmp/environment.yml

RUN micromamba install -n base --yes --file /tmp/environment.yml && \
    micromamba clean --all --yes

# Otherwise python will not be found
ARG MAMBA_DOCKERFILE_ACTIVATE=1

# Jupyter with Docker Compose
EXPOSE 8888
WORKDIR /home/$MAMBA_USER

FROM base AS dev

ENTRYPOINT ["/usr/local/bin/_entrypoint.sh", "jupyter", "lab", "--ip=0.0.0.0","--allow-root", "--no-browser"]