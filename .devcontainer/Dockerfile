# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.234.0/containers/codespaces-linux/.devcontainer/base.Dockerfile

FROM mcr.microsoft.com/vscode/devcontainers/universal:2-focal

ENV MICROPYPATH="./lib"

# ** [Optional] Uncomment this section to install additional packages. **
USER root

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends micropython

USER codespace
